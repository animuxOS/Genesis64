const Cc = Components.classes;
const Ci = Components.interfaces;
const Cr = Components.results;


function nsCeltxService () {
  var rdfsvc = Cc["@mozilla.org/rdf/rdf-service;1"]
    .getService(Ci.nsIRDFService);
  var rdfcu = Cc["@mozilla.org/rdf/container-utils;1"]
    .getService(Ci.nsIRDFContainerUtils);

  var ds = Cc["@mozilla.org/file/directory_service;1"]
    .getService(Ci.nsIProperties);
  var dir = ds.get("ProfD", Ci.nsIFile);
  dir.append("temp");
  if (! dir.exists() || ! (dir.isReadable() && dir.isWritable()))
    dir.createUnique(1, 0700);
  this._tempDir = dir;

  var os = Cc["@mozilla.org/observer-service;1"]
    .getService(Ci.nsIObserverService);
  os.addObserver(this, "quit-application", false);

  this.startup();
  this.fetchBannerData();
}

nsCeltxService.prototype = {
  QueryInterface: function cxsvc_QI(iid) {
    if (iid.equals(Ci.nsISupports) ||
        iid.equals(Ci.nsIObserver) ||
        iid.equals(Ci.nsICeltxService))
      return this
    throw Cr.NS_ERROR_NO_INTERFACE;
  },


  _offline: true,
  _loggedIn: false,
  _username: null,
  _workspaceURI: null,
  _autologinChecked: false,
  _banners: null,

  get VERSION ()      { return "2.0"; },
  get AUTH_REALM ()   { return "celtx"; },
  get AUTH_TYPE ()    { return "basic"; },
  get AUTH_PORT ()    { return 80;      },
  get AUTH_SCHEME ()  { return "https"; },
  get AUTH_DOMAIN ()  { return null;    },
  get AUTH_PATH ()    { return "/";     },

  get PUBLISH_SERVER () {
    var ps = Cc["@mozilla.org/preferences-service;1"]
      .getService(Ci.nsIPrefService);
    return ps.getBranch("celtx.server.").getCharPref("publish.selection");
  },
  get AUTH_URL () {
    return this.AUTH_SCHEME + "://" + this.PUBLISH_SERVER + "/app/test-auth";
  },
  get STARTUP_URL () {
    return this.AUTH_SCHEME + "://" + this.PUBLISH_SERVER + "/pub/startup";
  },
  get BANNER_URL () {
    return "http://www.celtx.com/notifier/sponsors/banners.xml";
  },

  get STUDIO_SERVER () {
    var ps = Cc["@mozilla.org/preferences-service;1"]
      .getService(Ci.nsIPrefService);
    return ps.getBranch("celtx.server.").getCharPref("studio.selection");
  },
  get STUDIO_SCHEME () {
    var ps = Cc["@mozilla.org/preferences-service;1"]
      .getService(Ci.nsIPrefService);
    return ps.getBranch("celtx.server.").getCharPref("studio.scheme");
  },
  get STUDIO_BASEURL () {
    return this.STUDIO_SCHEME + "://" + this.STUDIO_SERVER;
  },


  startup: function startup () {
    var request = Components.classes["@mozilla.org/xmlextras/xmlhttprequest;1"]
      .createInstance(Components.interfaces.nsIJSXMLHttpRequest);
    request.onload = function () {
      var cxsvc = Components.classes["@celtx.com/celtx-service;1"]
        .getService(Components.interfaces.nsICeltxService);
      if (this.status >= 200 && this.status < 300)
        cxsvc.offline = false;
      else
        cxsvc.offline = true;
    };
    request.onerror = function () {
      var cxsvc = Components.classes["@celtx.com/celtx-service;1"]
        .getService(Components.interfaces.nsICeltxService);
      cxsvc.offline = true;
    };
    request = request.QueryInterface(Ci.nsIXMLHttpRequest);
    request.open("GET", this.STARTUP_URL + "/" + this.VERSION, true);
    request.send(null);
  },


  shutdown: function shutdown () {
    try {
      this._tempDir.remove(true);
    }
    catch (ex) {
      dump("*** nsCeltxService.shutdown: " + ex + "\n");
    }

    var os = Cc["@mozilla.org/observer-service;1"]
      .getService(Ci.nsIObserverService);
    os.removeObserver(this, "quit-application");
  },


  fetchBannerData: function fetchBannerData () {
    var request = Components.classes["@mozilla.org/xmlextras/xmlhttprequest;1"]
      .createInstance(Components.interfaces.nsIJSXMLHttpRequest);
    request.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        var cxsvc = Components.classes["@celtx.com/celtx-service;1"]
          .getService(Components.interfaces.nsICeltxService);
        cxsvc.banners = this.responseXML;
      }
    };
    request.onerror = function () {
      dump("*** fetchBannerData: Unknown error\n");
    };
    request = request.QueryInterface(Ci.nsIXMLHttpRequest);
    request.open("GET", this.BANNER_URL, true);
    request.send(null);
  },


  observe: function (subject, topic, data) {
    if (topic == "quit-application") {
      this.shutdown();
    }
  },


  get tempDirSpec () {
    var ios = Cc["@mozilla.org/network/io-service;1"]
      .getService(Ci.nsIIOService);
    return ios.newFileURI(this._tempDir).spec;
  },


  get offline () {
    return this._offline;
  },


  set offline (val) {
    if (this._offline != val) {
      this._offline = val;
      var os = Cc["@mozilla.org/observer-service;1"]
        .getService(Ci.nsIObserverService);
      os.notifyObservers(this, "celtx:network-status-changed",
        val ? "offline" : "online");
    }
    return val;
  },


  get loggedIn () {
    return this._loggedIn;
  },


  loginSuccessful: function cxsvc_loginSuccessful () {
    this._loggedIn = true;
  },


  get username () {
    return this.loggedIn ? this._username : null;
  },


  get workspaceURI () {
    return this.loggedIn ? this._workspaceURI : null;
  },


  get banners () {
    return this._banners;
  },
  set banners (val) {
    this._banners = val;

    var os = Cc["@mozilla.org/observer-service;1"]
      .getService(Ci.nsIObserverService);
    os.notifyObservers(this, "celtx:banner-data-changed", null);
  },


  checkLoginFromCookie: function () {
    var ICookie = Components.interfaces.nsICookie;
    var cookiesvc = Components.classes["@mozilla.org/cookiemanager;1"]
      .getService(Components.interfaces.nsICookieManager);
    var cookieenum = cookiesvc.enumerator;
    var username = null;
    var workspace = null;
    while (cookieenum.hasMoreElements()) {
      var cookie = cookieenum.getNext().QueryInterface(ICookie);
      switch (cookie.name) {
        case "cx_studio_whoami":
          username = decodeURIComponent(cookie.value);  break;
        case "cx_studio_wsurl":
          workspace = decodeURIComponent(cookie.value); break;
      }
    }
    if (username && workspace) {
      this._username = username;
      this._workspaceURI = workspace;
      this.loginSuccessful();
      var obssvc = Cc["@mozilla.org/observer-service;1"]
        .getService(Ci.nsIObserverService);
      obssvc.notifyObservers(this, "celtx:login-status-changed", "loggedin");
    }
  },


  checkAutoLogin: function (win) {
    if (this._autologinChecked)
      return;

    this._autologinChecked = true;

    var ps = Cc["@mozilla.org/preferences-service;1"]
      .getService(Ci.nsIPrefService).getBranch("celtx.");
    if (! ps.getBoolPref("user.loginOnStartup"))
      return;

    try {
      var userid = ps.getCharPref("user.id");
      var pass = ps.getCharPref("user.encpassword");
      pass = base64_decodew(pass);
      this.loginAs(userid, pass, null, {onLogin: function (success) {}}, win);
    }
    catch (ex) {
      dump("*** nsCeltxService: " + ex + "\n");
    }
  },


  checkLogin: function (observer, win) {
    var request = Cc["@mozilla.org/xmlextras/xmlhttprequest;1"]
      .createInstance(Ci.nsIJSXMLHttpRequest);
    request.onload = function () {
      observer.onLogin(request.status == 200);
    };
    request.onerror = function () {
      observer.onLogin(false);
    };
    request = request.QueryInterface(Ci.nsIXMLHttpRequest);
    request.open("GET", this.STUDIO_BASEURL + "/auth/check", true);
    request.send(null);
  },


  // |service| is unused, but consumers expect it
  login: function (service, observer, reattempt, win) {
    if (this.loggedIn) {
      var self = this;
      var checkObserver = {
        onLogin: function (result) {
          if (result) {
            observer.onLogin(true);
          }
          else {
            self._loggedIn = false;
            self.login(service, observer, reattempt, win);
          }
        }
      };
      this.checkLogin(checkObserver, win);
      return;
    }

    var logindata = {
      username: "",
      password: "",
      prompt: true,
      reattempt: reattempt
    };
    this.attemptLogin(observer, win, logindata);
  },


  loginAs: function (username, password, service, observer, win) {
    var logindata = {
      username: username,
      password: password,
      prompt: false,
      reattempt: false
    };
    this.attemptLogin(observer, win, logindata);
  },


  attemptLogin: function (observer, win, logindata) {
    if (logindata.prompt) {
      var auth = {
        username: logindata.username,
        password: logindata.password,
        reattempt: logindata.reattempt,
        message: logindata.message,
        location: logindata.location,
        canceled: false
      };
      win.openDialog("chrome://celtx/content/authenticate.xul", "",
        "chrome,modal,centerscreen,titlebar", auth);
      if (auth.canceled) {
        observer.onLogin(false);
        return;
      }
      logindata.username = auth.username;
      logindata.password = auth.password;
    }

    // Trim leading and trailing white space
    logindata.username = logindata.username.replace(/^\s+/, "");
    logindata.username = logindata.username.replace(/\s+$/, "");

    var self = this;

    var request = Cc["@mozilla.org/xmlextras/xmlhttprequest;1"]
      .createInstance(Ci.nsIJSXMLHttpRequest);
    request.onload  = function () {
      if (request.status == 200) {
        self.checkLoginFromCookie();
        var obssvc = Cc["@mozilla.org/observer-service;1"]
          .getService(Ci.nsIObserverService);
        obssvc.notifyObservers(this, "celtx:login-status-changed", "loggedin");
        logindata.message = "";
        logindata.location = "";
        if (observer)
          observer.onLogin(true);
      }
      // If unauthorized, only reattempt if we prompted for login info
      else if (logindata.prompt) {
        // Not Authorized
        dump("*** nsCeltxService.login: " + request.status + " "
          + request.statusText + "\n");
        logindata.message = "";
        logindata.location = "";
        if (request.status >= 400 && request.status < 500) {
          logindata.message = request.responseText;
          try {
            logindata.location = request.getResponseHeader("Location");
          }
          catch (ex) {}
        }
        else {
          logindata.message = request.statusText;
          logindata.location = "";
        }
        // Retry
        logindata.reattempt = true;
        self.attemptLogin(observer, win, logindata);
      }
      else {
        dump("*** nsCeltxService.login: status: " + request.status + "\n");
        if (observer)
          observer.onLogin(false);
      }
    };
    request.onerror = function () {
      if (observer)
        observer.onLogin(false);
    };
    request.onreadystatechange = function () {
      var uninitialized = 0;
      var completed = 4;
      if (! observer)
        return;

      // If the request is aborted, it broadcasts a change to COMPLETED and
      // then silently switches to UNINITIALIZED, so we need to check on
      // a timeout if the state changes after we're notified.
      if (request.readyState == completed) {
        try {
          var jswin = win.QueryInterface(Components.interfaces.nsIDOMJSWindow);
          jswin.setTimeout(function () {
            if (request.readyState == uninitialized)
              observer.onLogin(false);
          }, 0);
        }
        catch (ex) {
          dump("*** attemptLogin: " + ex + "\n");
        }
      }
    };
    request = request.QueryInterface(Ci.nsIXMLHttpRequest);
    request.open("POST", this.STUDIO_BASEURL + "/auth/login", true);
    request.setRequestHeader("Content-Type",
      "application/x-www-form-urlencoded");
    request.setRequestHeader("Accept", "application/json");
    var poststr = "u=" + logindata.username + "&p=" + logindata.password;
    request.send(poststr);
  },


  logout: function cxsvc_logout () {
    this._loggedIn = false;
    var obssvc = Cc["@mozilla.org/observer-service;1"]
      .getService(Ci.nsIObserverService);
    obssvc.notifyObservers(this, "celtx:login-status-changed", "loggedout");

    var request = Cc["@mozilla.org/xmlextras/xmlhttprequest;1"]
      .createInstance(Ci.nsIXMLHttpRequest);
    request.open("GET", this.STUDIO_BASEURL + "/auth/logout", true);
    request.send(null);
  }
};


var initModule = {
  ServiceCID: Components.ID("{879e5daa-510e-4e1c-9420-66ac2b7bf7a3}"),
  ServiceContractID: "@celtx.com/celtx-service;1",
  ServiceName: "Celtx Service",


  registerSelf: function (compMgr, fileSpec, location, type) {
    compMgr = compMgr.QueryInterface(Ci.nsIComponentRegistrar);
    compMgr.registerFactoryLocation(this.ServiceCID, this.ServiceName,
      this.ServiceContractID, fileSpec, location, type);
  },


  unregisterSelf: function (compMgr, fileSpec, location) {
    compMgr = compMgr.QueryInterface(Ci.nsIComponentRegistrar);
    compMgr.unregisterFactoryLocation(this.ServiceCID, fileSpec);
  },


  getClassObject: function (compMgr, cid, iid) {
    if (! cid.equals(this.ServiceCID))
      throw Cr.NS_ERROR_NO_INTERFACE;
    if (! iid.equals(Ci.nsIFactory))
      throw Cr.NS_ERROR_NOT_IMPLEMENTED;
    return this.instanceFactory;
  },


  canUnload: function (compMgr) {
    return true;
  },


  instanceFactory: {
    createInstance: function (outer, iid) {
      if (outer != null)
        throw Cr.NS_ERROR_NO_AGGREGATION;
      return new nsCeltxService().QueryInterface(iid);
    }
  }
};


function NSGetModule (compMgr, fileSpec) {
  return initModule;
}


function base64_decodew (str) {
  var table =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var result = "";
  var i = 0;
  var accum = -1;
  while (i < str.length) {
    var src = [
      table.indexOf(str.charAt(i++)), table.indexOf(str.charAt(i++)),
      table.indexOf(str.charAt(i++)), table.indexOf(str.charAt(i++))
    ];
    if (isNaN(src[0]) || isNaN(src[1]) || isNaN(src[2]) || isNaN(src[3]) ||
        src[0] < 0 || src[1] < 0 || src[2] < 0 || src[3] < 0)
      throw "String does not appear to be base64";
    // Masking guarantees any '=' will be trimmed from 0x40 to 0x00
    var dst = [
      (src[0] << 2) | ((src[1] & 0x3F) >> 4),
      ((src[1] & 0x0F) << 4) | ((src[2] & 0x3F) >> 2),
      ((src[2] & 0x03) << 6) | (src[3] & 0x3F)
    ];
    if (i % 8 == 4) {
      // First char and a half
      result += String.fromCharCode((dst[0] << 8) | dst[1]);
      if (src[3] == 64) {
        break;
      }
      accum = dst[2] << 8;
    }
    else {
      result += String.fromCharCode(accum | dst[0]);
      accum = -1;
      if (dst[1] == 0 && dst[2] == 0) {
        break;
      }
      result += String.fromCharCode((dst[1] << 8) | dst[2]);
    }
  }
  return result;
}
