/*** Autogenerated by WIDL 1.0-rc1 from mshtmhst.idl - Do not edit ***/
#include <rpc.h>
#include <rpcndr.h>

#ifndef __WIDL_MSHTMHST_H
#define __WIDL_MSHTMHST_H
#ifdef __cplusplus
extern "C" {
#endif

#include <ocidl.h>
#include <objidl.h>
#include <oleidl.h>
#include <oaidl.h>
#include <docobj.h>
#define CONTEXT_MENU_DEFAULT     0
#define CONTEXT_MENU_IMAGE       1
#define CONTEXT_MENU_CONTROL     2
#define CONTEXT_MENU_TABLE       3
#define CONTEXT_MENU_TEXTSELECT  4
#define CONTEXT_MENU_ANCHOR      5
#define CONTEXT_MENU_UNKNOWN     6
#define CONTEXT_MENU_IMGDYNSRC   7
#define CONTEXT_MENU_IMGART      8
#define CONTEXT_MENU_DEBUG       9
#define CONTEXT_MENU_VSCROLL    10
#define CONTEXT_MENU_HSCROLL    11
#define MENUEXT_SHOWDIALOG 1
#define DOCHOSTUIFLAG_BROWSER (DOCHOSTUIFLAG_DISABLE_HELP_MENU|DOCHOSTUIFLAG_DISABLE_SCRIPT_INACTIVE)
#define HTMLDLG_NOUI            0x0010
#define HTMLDLG_MODAL           0x0020
#define HTMLDLG_MODELESS        0x0040
#define HTMLDLG_PRINT_TEMPLATE  0x0080
#define HTMLDLG_VERIFY          0x0100
#define PRINT_DONTBOTHERUSER     0x0001
#define PRINT_WAITFORCOMPLETION  0x0002
DEFINE_GUID(CGID_MSHTML, 0xde4ba900,0x59ca,0x11cf,0x95,0x92,0x44,0x45,0x53,0x54,0x00,0x00);
#define CMDSETID_Forms3 CGID_MSHTML
#if defined(__GNUC__)
#define SZ_HTML_CLIENTSITE_OBJECTPARAM (const WCHAR[]) {'{','d','4','d','b','6','8','5','0','-','5','3','8','5','-','1','1','d','0','-','8','9','e','9','-','0','0','a','0','c','9','0','a','9','0','a','c','}',0}
#elif defined(_MSC_VER)
#define SZ_HTML_CLIENTSITE_OBJECTPARAM L"{d4db6850-5385-11d0-89e9-00a0c90a90ac}"
#else
static const WCHAR SZ_HTML_CLIENTSITE_OBJECTPARAM[] = {'{','d','4','d','b','6','8','5','0','-','5','3','8','5','-','1','1','d','0','-','8','9','e','9','-','0','0','a','0','c','9','0','a','9','0','a','c','}',0};
#endif
#ifndef __IHTMLWindow2_FWD_DEFINED__
#define __IHTMLWindow2_FWD_DEFINED__
typedef interface IHTMLWindow2 IHTMLWindow2;
#endif
#ifndef __IHostDialogHelper_FWD_DEFINED__
#define __IHostDialogHelper_FWD_DEFINED__
typedef interface IHostDialogHelper IHostDialogHelper;
#endif

/*****************************************************************************
 * IHostDialogHelper interface
 */
#ifndef __IHostDialogHelper_INTERFACE_DEFINED__
#define __IHostDialogHelper_INTERFACE_DEFINED__

DEFINE_GUID(IID_IHostDialogHelper, 0x53dec138, 0xa51e, 0x11d2, 0x86,0x1e, 0x00,0xc0,0x4f,0xa3,0x5c,0x89);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IHostDialogHelper : public IUnknown
{
    virtual HRESULT STDMETHODCALLTYPE ShowHTMLDialog(
        HWND hwndParent,
        IMoniker *pMk,
        VARIANT *pvarArgIn,
        WCHAR *pchOptions,
        VARIANT *pvarArgOut,
        IUnknown *punkHost) = 0;

};
#else
typedef struct IHostDialogHelperVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IHostDialogHelper* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IHostDialogHelper* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IHostDialogHelper* This);

    /*** IHostDialogHelper methods ***/
    HRESULT (STDMETHODCALLTYPE *ShowHTMLDialog)(
        IHostDialogHelper* This,
        HWND hwndParent,
        IMoniker *pMk,
        VARIANT *pvarArgIn,
        WCHAR *pchOptions,
        VARIANT *pvarArgOut,
        IUnknown *punkHost);

    END_INTERFACE
} IHostDialogHelperVtbl;
interface IHostDialogHelper {
    CONST_VTBL IHostDialogHelperVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IHostDialogHelper_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IHostDialogHelper_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IHostDialogHelper_Release(This) (This)->lpVtbl->Release(This)
/*** IHostDialogHelper methods ***/
#define IHostDialogHelper_ShowHTMLDialog(This,hwndParent,pMk,pvarArgIn,pchOptions,pvarArgOut,punkHost) (This)->lpVtbl->ShowHTMLDialog(This,hwndParent,pMk,pvarArgIn,pchOptions,pvarArgOut,punkHost)
#endif

#endif

HRESULT STDMETHODCALLTYPE IHostDialogHelper_ShowHTMLDialog_Proxy(
    IHostDialogHelper* This,
    HWND hwndParent,
    IMoniker *pMk,
    VARIANT *pvarArgIn,
    WCHAR *pchOptions,
    VARIANT *pvarArgOut,
    IUnknown *punkHost);
void __RPC_STUB IHostDialogHelper_ShowHTMLDialog_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IHostDialogHelper_INTERFACE_DEFINED__ */

/*****************************************************************************
 * HostDialogHelper coclass
 */

DEFINE_GUID(CLSID_HostDialogHelper, 0x429af92c, 0xa51f, 0x11d2, 0x86,0x1e, 0x00,0xc0,0x4f,0xa3,0x5c,0x89);

#ifndef __HostDialogHelper_FWD_DEFINED__
#define __HostDialogHelper_FWD_DEFINED__
typedef struct HostDialogHelper HostDialogHelper;
#endif /* defined __HostDialogHelper_FWD_DEFINED__ */

typedef enum tagDOCHOSTUITYPE {
    DOCHOSTUITYPE_BROWSE = 0,
    DOCHOSTUITYPE_AUTHOR = 1
} DOCHOSTUITYPE;
typedef enum tagDOCHOSTUIDBLCLK {
    DOCHOSTUIDBLCLK_DEFAULT = 0,
    DOCHOSTUIDBLCLK_SHOWPROPERTIES = 1,
    DOCHOSTUIDBLCLK_SHOWCODE = 2
} DOCHOSTUIDBLCLK;
typedef enum tagDOCHOSTUIFLAG {
    DOCHOSTUIFLAG_DIALOG = 0x1,
    DOCHOSTUIFLAG_DISABLE_HELP_MENU = 0x2,
    DOCHOSTUIFLAG_NO3DBORDER = 0x4,
    DOCHOSTUIFLAG_SCROLL_NO = 0x8,
    DOCHOSTUIFLAG_DISABLE_SCRIPT_INACTIVE = 0x10,
    DOCHOSTUIFLAG_OPENNEWWIN = 0x20,
    DOCHOSTUIFLAG_DISABLE_OFFSCREEN = 0x40,
    DOCHOSTUIFLAG_FLAT_SCROLLBAR = 0x80,
    DOCHOSTUIFLAG_DIV_BLOCKDEFAULT = 0x100,
    DOCHOSTUIFLAG_ACTIVATE_CLIENTHIT_ONLY = 0x200,
    DOCHOSTUIFLAG_OVERRIDEBEHAVIORFACTORY = 0x400,
    DOCHOSTUIFLAG_CODEPAGELINKEDFONTS = 0x800,
    DOCHOSTUIFLAG_URL_ENCODING_DISABLE_UTF8 = 0x1000,
    DOCHOSTUIFLAG_URL_ENCODING_ENABLE_UTF8 = 0x2000,
    DOCHOSTUIFLAG_ENABLE_FORMS_AUTOCOMPLETE = 0x4000,
    DOCHOSTUIFLAG_ENABLE_INPLACE_NAVIGATION = 0x10000,
    DOCHOSTUIFLAG_IME_ENABLE_RECONVERSION = 0x20000,
    DOCHOSTUIFLAG_THEME = 0x40000,
    DOCHOSTUIFLAG_NOTHEME = 0x80000,
    DOCHOSTUIFLAG_NOPICS = 0x100000,
    DOCHOSTUIFLAG_NO3DOUTERBORDER = 0x200000,
    DOCHOSTUIFLAG_DISABLE_EDIT_NS_FIXUP = 0x400000,
    DOCHOSTUIFLAG_LOCAL_MACHINE_ACCESS_CHECK = 0x800000,
    DOCHOSTUIFLAG_DISABLE_UNTRUSTEDPROTOCOL = 0x1000000
} DOCHOSTUIFLAG;
#ifndef __IDocHostUIHandler_FWD_DEFINED__
#define __IDocHostUIHandler_FWD_DEFINED__
typedef interface IDocHostUIHandler IDocHostUIHandler;
#endif

typedef struct _DOCHOSTUIINFO {
    ULONG cbSize;
    DWORD dwFlags;
    DWORD dwDoubleClick;
    OLECHAR *pchHostCss;
    OLECHAR *pchHostNS;
} DOCHOSTUIINFO;
/*****************************************************************************
 * IDocHostUIHandler interface
 */
#ifndef __IDocHostUIHandler_INTERFACE_DEFINED__
#define __IDocHostUIHandler_INTERFACE_DEFINED__

DEFINE_GUID(IID_IDocHostUIHandler, 0xbd3f23c0, 0xd43e, 0x11cf, 0x89,0x3b, 0x00,0xaa,0x00,0xbd,0xce,0x1a);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IDocHostUIHandler : public IUnknown
{
    virtual HRESULT STDMETHODCALLTYPE ShowContextMenu(
        DWORD dwID,
        POINT *ppt,
        IUnknown *pcmdtReserved,
        IDispatch *pdispReserved) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetHostInfo(
        DOCHOSTUIINFO *pInfo) = 0;

    virtual HRESULT STDMETHODCALLTYPE ShowUI(
        DWORD dwID,
        IOleInPlaceActiveObject *pActiveObject,
        IOleCommandTarget *pCommandTarget,
        IOleInPlaceFrame *pFrame,
        IOleInPlaceUIWindow *pDoc) = 0;

    virtual HRESULT STDMETHODCALLTYPE HideUI(
        ) = 0;

    virtual HRESULT STDMETHODCALLTYPE UpdateUI(
        ) = 0;

    virtual HRESULT STDMETHODCALLTYPE EnableModeless(
        BOOL fEnable) = 0;

    virtual HRESULT STDMETHODCALLTYPE OnDocWindowActivate(
        BOOL fActivate) = 0;

    virtual HRESULT STDMETHODCALLTYPE OnFrameWindowActivate(
        BOOL fActivate) = 0;

    virtual HRESULT STDMETHODCALLTYPE ResizeBorder(
        LPCRECT prcBorder,
        IOleInPlaceUIWindow *pUIWindow,
        BOOL fRameWindow) = 0;

    virtual HRESULT STDMETHODCALLTYPE TranslateAccelerator(
        LPMSG lpMsg,
        const GUID *pguidCmdGroup,
        DWORD nCmdID) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetOptionKeyPath(
        LPOLESTR *pchKey,
        DWORD dw) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetDropTarget(
        IDropTarget *pDropTarget,
        IDropTarget **ppDropTarget) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetExternal(
        IDispatch **ppDispatch) = 0;

    virtual HRESULT STDMETHODCALLTYPE TranslateUrl(
        DWORD dwTranslate,
        OLECHAR *pchURLIn,
        OLECHAR **ppchURLOut) = 0;

    virtual HRESULT STDMETHODCALLTYPE FilterDataObject(
        IDataObject *pDO,
        IDataObject **ppDORet) = 0;

};
#else
typedef struct IDocHostUIHandlerVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IDocHostUIHandler* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IDocHostUIHandler* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IDocHostUIHandler* This);

    /*** IDocHostUIHandler methods ***/
    HRESULT (STDMETHODCALLTYPE *ShowContextMenu)(
        IDocHostUIHandler* This,
        DWORD dwID,
        POINT *ppt,
        IUnknown *pcmdtReserved,
        IDispatch *pdispReserved);

    HRESULT (STDMETHODCALLTYPE *GetHostInfo)(
        IDocHostUIHandler* This,
        DOCHOSTUIINFO *pInfo);

    HRESULT (STDMETHODCALLTYPE *ShowUI)(
        IDocHostUIHandler* This,
        DWORD dwID,
        IOleInPlaceActiveObject *pActiveObject,
        IOleCommandTarget *pCommandTarget,
        IOleInPlaceFrame *pFrame,
        IOleInPlaceUIWindow *pDoc);

    HRESULT (STDMETHODCALLTYPE *HideUI)(
        IDocHostUIHandler* This);

    HRESULT (STDMETHODCALLTYPE *UpdateUI)(
        IDocHostUIHandler* This);

    HRESULT (STDMETHODCALLTYPE *EnableModeless)(
        IDocHostUIHandler* This,
        BOOL fEnable);

    HRESULT (STDMETHODCALLTYPE *OnDocWindowActivate)(
        IDocHostUIHandler* This,
        BOOL fActivate);

    HRESULT (STDMETHODCALLTYPE *OnFrameWindowActivate)(
        IDocHostUIHandler* This,
        BOOL fActivate);

    HRESULT (STDMETHODCALLTYPE *ResizeBorder)(
        IDocHostUIHandler* This,
        LPCRECT prcBorder,
        IOleInPlaceUIWindow *pUIWindow,
        BOOL fRameWindow);

    HRESULT (STDMETHODCALLTYPE *TranslateAccelerator)(
        IDocHostUIHandler* This,
        LPMSG lpMsg,
        const GUID *pguidCmdGroup,
        DWORD nCmdID);

    HRESULT (STDMETHODCALLTYPE *GetOptionKeyPath)(
        IDocHostUIHandler* This,
        LPOLESTR *pchKey,
        DWORD dw);

    HRESULT (STDMETHODCALLTYPE *GetDropTarget)(
        IDocHostUIHandler* This,
        IDropTarget *pDropTarget,
        IDropTarget **ppDropTarget);

    HRESULT (STDMETHODCALLTYPE *GetExternal)(
        IDocHostUIHandler* This,
        IDispatch **ppDispatch);

    HRESULT (STDMETHODCALLTYPE *TranslateUrl)(
        IDocHostUIHandler* This,
        DWORD dwTranslate,
        OLECHAR *pchURLIn,
        OLECHAR **ppchURLOut);

    HRESULT (STDMETHODCALLTYPE *FilterDataObject)(
        IDocHostUIHandler* This,
        IDataObject *pDO,
        IDataObject **ppDORet);

    END_INTERFACE
} IDocHostUIHandlerVtbl;
interface IDocHostUIHandler {
    CONST_VTBL IDocHostUIHandlerVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IDocHostUIHandler_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IDocHostUIHandler_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IDocHostUIHandler_Release(This) (This)->lpVtbl->Release(This)
/*** IDocHostUIHandler methods ***/
#define IDocHostUIHandler_ShowContextMenu(This,dwID,ppt,pcmdtReserved,pdispReserved) (This)->lpVtbl->ShowContextMenu(This,dwID,ppt,pcmdtReserved,pdispReserved)
#define IDocHostUIHandler_GetHostInfo(This,pInfo) (This)->lpVtbl->GetHostInfo(This,pInfo)
#define IDocHostUIHandler_ShowUI(This,dwID,pActiveObject,pCommandTarget,pFrame,pDoc) (This)->lpVtbl->ShowUI(This,dwID,pActiveObject,pCommandTarget,pFrame,pDoc)
#define IDocHostUIHandler_HideUI(This) (This)->lpVtbl->HideUI(This)
#define IDocHostUIHandler_UpdateUI(This) (This)->lpVtbl->UpdateUI(This)
#define IDocHostUIHandler_EnableModeless(This,fEnable) (This)->lpVtbl->EnableModeless(This,fEnable)
#define IDocHostUIHandler_OnDocWindowActivate(This,fActivate) (This)->lpVtbl->OnDocWindowActivate(This,fActivate)
#define IDocHostUIHandler_OnFrameWindowActivate(This,fActivate) (This)->lpVtbl->OnFrameWindowActivate(This,fActivate)
#define IDocHostUIHandler_ResizeBorder(This,prcBorder,pUIWindow,fRameWindow) (This)->lpVtbl->ResizeBorder(This,prcBorder,pUIWindow,fRameWindow)
#define IDocHostUIHandler_TranslateAccelerator(This,lpMsg,pguidCmdGroup,nCmdID) (This)->lpVtbl->TranslateAccelerator(This,lpMsg,pguidCmdGroup,nCmdID)
#define IDocHostUIHandler_GetOptionKeyPath(This,pchKey,dw) (This)->lpVtbl->GetOptionKeyPath(This,pchKey,dw)
#define IDocHostUIHandler_GetDropTarget(This,pDropTarget,ppDropTarget) (This)->lpVtbl->GetDropTarget(This,pDropTarget,ppDropTarget)
#define IDocHostUIHandler_GetExternal(This,ppDispatch) (This)->lpVtbl->GetExternal(This,ppDispatch)
#define IDocHostUIHandler_TranslateUrl(This,dwTranslate,pchURLIn,ppchURLOut) (This)->lpVtbl->TranslateUrl(This,dwTranslate,pchURLIn,ppchURLOut)
#define IDocHostUIHandler_FilterDataObject(This,pDO,ppDORet) (This)->lpVtbl->FilterDataObject(This,pDO,ppDORet)
#endif

#endif

HRESULT STDMETHODCALLTYPE IDocHostUIHandler_ShowContextMenu_Proxy(
    IDocHostUIHandler* This,
    DWORD dwID,
    POINT *ppt,
    IUnknown *pcmdtReserved,
    IDispatch *pdispReserved);
void __RPC_STUB IDocHostUIHandler_ShowContextMenu_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_GetHostInfo_Proxy(
    IDocHostUIHandler* This,
    DOCHOSTUIINFO *pInfo);
void __RPC_STUB IDocHostUIHandler_GetHostInfo_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_ShowUI_Proxy(
    IDocHostUIHandler* This,
    DWORD dwID,
    IOleInPlaceActiveObject *pActiveObject,
    IOleCommandTarget *pCommandTarget,
    IOleInPlaceFrame *pFrame,
    IOleInPlaceUIWindow *pDoc);
void __RPC_STUB IDocHostUIHandler_ShowUI_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_HideUI_Proxy(
    IDocHostUIHandler* This);
void __RPC_STUB IDocHostUIHandler_HideUI_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_UpdateUI_Proxy(
    IDocHostUIHandler* This);
void __RPC_STUB IDocHostUIHandler_UpdateUI_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_EnableModeless_Proxy(
    IDocHostUIHandler* This,
    BOOL fEnable);
void __RPC_STUB IDocHostUIHandler_EnableModeless_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_OnDocWindowActivate_Proxy(
    IDocHostUIHandler* This,
    BOOL fActivate);
void __RPC_STUB IDocHostUIHandler_OnDocWindowActivate_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_OnFrameWindowActivate_Proxy(
    IDocHostUIHandler* This,
    BOOL fActivate);
void __RPC_STUB IDocHostUIHandler_OnFrameWindowActivate_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_ResizeBorder_Proxy(
    IDocHostUIHandler* This,
    LPCRECT prcBorder,
    IOleInPlaceUIWindow *pUIWindow,
    BOOL fRameWindow);
void __RPC_STUB IDocHostUIHandler_ResizeBorder_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_TranslateAccelerator_Proxy(
    IDocHostUIHandler* This,
    LPMSG lpMsg,
    const GUID *pguidCmdGroup,
    DWORD nCmdID);
void __RPC_STUB IDocHostUIHandler_TranslateAccelerator_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_GetOptionKeyPath_Proxy(
    IDocHostUIHandler* This,
    LPOLESTR *pchKey,
    DWORD dw);
void __RPC_STUB IDocHostUIHandler_GetOptionKeyPath_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_GetDropTarget_Proxy(
    IDocHostUIHandler* This,
    IDropTarget *pDropTarget,
    IDropTarget **ppDropTarget);
void __RPC_STUB IDocHostUIHandler_GetDropTarget_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_GetExternal_Proxy(
    IDocHostUIHandler* This,
    IDispatch **ppDispatch);
void __RPC_STUB IDocHostUIHandler_GetExternal_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_TranslateUrl_Proxy(
    IDocHostUIHandler* This,
    DWORD dwTranslate,
    OLECHAR *pchURLIn,
    OLECHAR **ppchURLOut);
void __RPC_STUB IDocHostUIHandler_TranslateUrl_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostUIHandler_FilterDataObject_Proxy(
    IDocHostUIHandler* This,
    IDataObject *pDO,
    IDataObject **ppDORet);
void __RPC_STUB IDocHostUIHandler_FilterDataObject_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IDocHostUIHandler_INTERFACE_DEFINED__ */

DEFINE_GUID(CGID_DocHostCommandHandler,0xf38bc242,0xb950,0x11d1,0x89,0x18,0x00,0xc0,0x4f,0xc2,0xc8,0x36);
#ifndef __IDocHostUIHandler2_FWD_DEFINED__
#define __IDocHostUIHandler2_FWD_DEFINED__
typedef interface IDocHostUIHandler2 IDocHostUIHandler2;
#endif

/*****************************************************************************
 * IDocHostUIHandler2 interface
 */
#ifndef __IDocHostUIHandler2_INTERFACE_DEFINED__
#define __IDocHostUIHandler2_INTERFACE_DEFINED__

DEFINE_GUID(IID_IDocHostUIHandler2, 0x3050f6d0, 0x98b5, 0x11cf, 0xbb,0x82, 0x00,0xaa,0x00,0xbd,0xce,0x0b);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IDocHostUIHandler2 : public IDocHostUIHandler
{
    virtual HRESULT STDMETHODCALLTYPE GetOverrideKeyPath(
        LPOLESTR *pchKey,
        DWORD dw) = 0;

};
#else
typedef struct IDocHostUIHandler2Vtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IDocHostUIHandler2* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IDocHostUIHandler2* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IDocHostUIHandler2* This);

    /*** IDocHostUIHandler methods ***/
    HRESULT (STDMETHODCALLTYPE *ShowContextMenu)(
        IDocHostUIHandler2* This,
        DWORD dwID,
        POINT *ppt,
        IUnknown *pcmdtReserved,
        IDispatch *pdispReserved);

    HRESULT (STDMETHODCALLTYPE *GetHostInfo)(
        IDocHostUIHandler2* This,
        DOCHOSTUIINFO *pInfo);

    HRESULT (STDMETHODCALLTYPE *ShowUI)(
        IDocHostUIHandler2* This,
        DWORD dwID,
        IOleInPlaceActiveObject *pActiveObject,
        IOleCommandTarget *pCommandTarget,
        IOleInPlaceFrame *pFrame,
        IOleInPlaceUIWindow *pDoc);

    HRESULT (STDMETHODCALLTYPE *HideUI)(
        IDocHostUIHandler2* This);

    HRESULT (STDMETHODCALLTYPE *UpdateUI)(
        IDocHostUIHandler2* This);

    HRESULT (STDMETHODCALLTYPE *EnableModeless)(
        IDocHostUIHandler2* This,
        BOOL fEnable);

    HRESULT (STDMETHODCALLTYPE *OnDocWindowActivate)(
        IDocHostUIHandler2* This,
        BOOL fActivate);

    HRESULT (STDMETHODCALLTYPE *OnFrameWindowActivate)(
        IDocHostUIHandler2* This,
        BOOL fActivate);

    HRESULT (STDMETHODCALLTYPE *ResizeBorder)(
        IDocHostUIHandler2* This,
        LPCRECT prcBorder,
        IOleInPlaceUIWindow *pUIWindow,
        BOOL fRameWindow);

    HRESULT (STDMETHODCALLTYPE *TranslateAccelerator)(
        IDocHostUIHandler2* This,
        LPMSG lpMsg,
        const GUID *pguidCmdGroup,
        DWORD nCmdID);

    HRESULT (STDMETHODCALLTYPE *GetOptionKeyPath)(
        IDocHostUIHandler2* This,
        LPOLESTR *pchKey,
        DWORD dw);

    HRESULT (STDMETHODCALLTYPE *GetDropTarget)(
        IDocHostUIHandler2* This,
        IDropTarget *pDropTarget,
        IDropTarget **ppDropTarget);

    HRESULT (STDMETHODCALLTYPE *GetExternal)(
        IDocHostUIHandler2* This,
        IDispatch **ppDispatch);

    HRESULT (STDMETHODCALLTYPE *TranslateUrl)(
        IDocHostUIHandler2* This,
        DWORD dwTranslate,
        OLECHAR *pchURLIn,
        OLECHAR **ppchURLOut);

    HRESULT (STDMETHODCALLTYPE *FilterDataObject)(
        IDocHostUIHandler2* This,
        IDataObject *pDO,
        IDataObject **ppDORet);

    /*** IDocHostUIHandler2 methods ***/
    HRESULT (STDMETHODCALLTYPE *GetOverrideKeyPath)(
        IDocHostUIHandler2* This,
        LPOLESTR *pchKey,
        DWORD dw);

    END_INTERFACE
} IDocHostUIHandler2Vtbl;
interface IDocHostUIHandler2 {
    CONST_VTBL IDocHostUIHandler2Vtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IDocHostUIHandler2_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IDocHostUIHandler2_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IDocHostUIHandler2_Release(This) (This)->lpVtbl->Release(This)
/*** IDocHostUIHandler methods ***/
#define IDocHostUIHandler2_ShowContextMenu(This,dwID,ppt,pcmdtReserved,pdispReserved) (This)->lpVtbl->ShowContextMenu(This,dwID,ppt,pcmdtReserved,pdispReserved)
#define IDocHostUIHandler2_GetHostInfo(This,pInfo) (This)->lpVtbl->GetHostInfo(This,pInfo)
#define IDocHostUIHandler2_ShowUI(This,dwID,pActiveObject,pCommandTarget,pFrame,pDoc) (This)->lpVtbl->ShowUI(This,dwID,pActiveObject,pCommandTarget,pFrame,pDoc)
#define IDocHostUIHandler2_HideUI(This) (This)->lpVtbl->HideUI(This)
#define IDocHostUIHandler2_UpdateUI(This) (This)->lpVtbl->UpdateUI(This)
#define IDocHostUIHandler2_EnableModeless(This,fEnable) (This)->lpVtbl->EnableModeless(This,fEnable)
#define IDocHostUIHandler2_OnDocWindowActivate(This,fActivate) (This)->lpVtbl->OnDocWindowActivate(This,fActivate)
#define IDocHostUIHandler2_OnFrameWindowActivate(This,fActivate) (This)->lpVtbl->OnFrameWindowActivate(This,fActivate)
#define IDocHostUIHandler2_ResizeBorder(This,prcBorder,pUIWindow,fRameWindow) (This)->lpVtbl->ResizeBorder(This,prcBorder,pUIWindow,fRameWindow)
#define IDocHostUIHandler2_TranslateAccelerator(This,lpMsg,pguidCmdGroup,nCmdID) (This)->lpVtbl->TranslateAccelerator(This,lpMsg,pguidCmdGroup,nCmdID)
#define IDocHostUIHandler2_GetOptionKeyPath(This,pchKey,dw) (This)->lpVtbl->GetOptionKeyPath(This,pchKey,dw)
#define IDocHostUIHandler2_GetDropTarget(This,pDropTarget,ppDropTarget) (This)->lpVtbl->GetDropTarget(This,pDropTarget,ppDropTarget)
#define IDocHostUIHandler2_GetExternal(This,ppDispatch) (This)->lpVtbl->GetExternal(This,ppDispatch)
#define IDocHostUIHandler2_TranslateUrl(This,dwTranslate,pchURLIn,ppchURLOut) (This)->lpVtbl->TranslateUrl(This,dwTranslate,pchURLIn,ppchURLOut)
#define IDocHostUIHandler2_FilterDataObject(This,pDO,ppDORet) (This)->lpVtbl->FilterDataObject(This,pDO,ppDORet)
/*** IDocHostUIHandler2 methods ***/
#define IDocHostUIHandler2_GetOverrideKeyPath(This,pchKey,dw) (This)->lpVtbl->GetOverrideKeyPath(This,pchKey,dw)
#endif

#endif

HRESULT STDMETHODCALLTYPE IDocHostUIHandler2_GetOverrideKeyPath_Proxy(
    IDocHostUIHandler2* This,
    LPOLESTR *pchKey,
    DWORD dw);
void __RPC_STUB IDocHostUIHandler2_GetOverrideKeyPath_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IDocHostUIHandler2_INTERFACE_DEFINED__ */

#ifndef __ICustomDoc_FWD_DEFINED__
#define __ICustomDoc_FWD_DEFINED__
typedef interface ICustomDoc ICustomDoc;
#endif

/*****************************************************************************
 * ICustomDoc interface
 */
#ifndef __ICustomDoc_INTERFACE_DEFINED__
#define __ICustomDoc_INTERFACE_DEFINED__

DEFINE_GUID(IID_ICustomDoc, 0x3050f3f0, 0x98b5, 0x11cf, 0xbb,0x82, 0x00,0xaa,0x00,0xbd,0xce,0x0b);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface ICustomDoc : public IUnknown
{
    virtual HRESULT STDMETHODCALLTYPE SetUIHandler(
        IDocHostUIHandler *pUIHandler) = 0;

};
#else
typedef struct ICustomDocVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        ICustomDoc* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        ICustomDoc* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        ICustomDoc* This);

    /*** ICustomDoc methods ***/
    HRESULT (STDMETHODCALLTYPE *SetUIHandler)(
        ICustomDoc* This,
        IDocHostUIHandler *pUIHandler);

    END_INTERFACE
} ICustomDocVtbl;
interface ICustomDoc {
    CONST_VTBL ICustomDocVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define ICustomDoc_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define ICustomDoc_AddRef(This) (This)->lpVtbl->AddRef(This)
#define ICustomDoc_Release(This) (This)->lpVtbl->Release(This)
/*** ICustomDoc methods ***/
#define ICustomDoc_SetUIHandler(This,pUIHandler) (This)->lpVtbl->SetUIHandler(This,pUIHandler)
#endif

#endif

HRESULT STDMETHODCALLTYPE ICustomDoc_SetUIHandler_Proxy(
    ICustomDoc* This,
    IDocHostUIHandler *pUIHandler);
void __RPC_STUB ICustomDoc_SetUIHandler_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __ICustomDoc_INTERFACE_DEFINED__ */

#ifndef __IDocHostShowUI_FWD_DEFINED__
#define __IDocHostShowUI_FWD_DEFINED__
typedef interface IDocHostShowUI IDocHostShowUI;
#endif

/*****************************************************************************
 * IDocHostShowUI interface
 */
#ifndef __IDocHostShowUI_INTERFACE_DEFINED__
#define __IDocHostShowUI_INTERFACE_DEFINED__

DEFINE_GUID(IID_IDocHostShowUI, 0xc4d244b0, 0xd43e, 0x11cf, 0x89,0x3b, 0x00,0xaa,0x00,0xbd,0xce,0x1a);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IDocHostShowUI : public IUnknown
{
    virtual HRESULT STDMETHODCALLTYPE ShowMessage(
        HWND hwnd,
        LPOLESTR lpstrText,
        LPOLESTR lpstrCaption,
        DWORD dwType,
        LPOLESTR lpstrHelpFile,
        DWORD dwHelpContext,
        LRESULT *plResult) = 0;

    virtual HRESULT STDMETHODCALLTYPE ShowHelp(
        HWND hwnd,
        LPOLESTR pszHelpFile,
        UINT uCommand,
        DWORD dwData,
        POINT ptMouse,
        IDispatch *pDispatchObjectHit) = 0;

};
#else
typedef struct IDocHostShowUIVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IDocHostShowUI* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IDocHostShowUI* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IDocHostShowUI* This);

    /*** IDocHostShowUI methods ***/
    HRESULT (STDMETHODCALLTYPE *ShowMessage)(
        IDocHostShowUI* This,
        HWND hwnd,
        LPOLESTR lpstrText,
        LPOLESTR lpstrCaption,
        DWORD dwType,
        LPOLESTR lpstrHelpFile,
        DWORD dwHelpContext,
        LRESULT *plResult);

    HRESULT (STDMETHODCALLTYPE *ShowHelp)(
        IDocHostShowUI* This,
        HWND hwnd,
        LPOLESTR pszHelpFile,
        UINT uCommand,
        DWORD dwData,
        POINT ptMouse,
        IDispatch *pDispatchObjectHit);

    END_INTERFACE
} IDocHostShowUIVtbl;
interface IDocHostShowUI {
    CONST_VTBL IDocHostShowUIVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IDocHostShowUI_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IDocHostShowUI_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IDocHostShowUI_Release(This) (This)->lpVtbl->Release(This)
/*** IDocHostShowUI methods ***/
#define IDocHostShowUI_ShowMessage(This,hwnd,lpstrText,lpstrCaption,dwType,lpstrHelpFile,dwHelpContext,plResult) (This)->lpVtbl->ShowMessage(This,hwnd,lpstrText,lpstrCaption,dwType,lpstrHelpFile,dwHelpContext,plResult)
#define IDocHostShowUI_ShowHelp(This,hwnd,pszHelpFile,uCommand,dwData,ptMouse,pDispatchObjectHit) (This)->lpVtbl->ShowHelp(This,hwnd,pszHelpFile,uCommand,dwData,ptMouse,pDispatchObjectHit)
#endif

#endif

HRESULT STDMETHODCALLTYPE IDocHostShowUI_ShowMessage_Proxy(
    IDocHostShowUI* This,
    HWND hwnd,
    LPOLESTR lpstrText,
    LPOLESTR lpstrCaption,
    DWORD dwType,
    LPOLESTR lpstrHelpFile,
    DWORD dwHelpContext,
    LRESULT *plResult);
void __RPC_STUB IDocHostShowUI_ShowMessage_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IDocHostShowUI_ShowHelp_Proxy(
    IDocHostShowUI* This,
    HWND hwnd,
    LPOLESTR pszHelpFile,
    UINT uCommand,
    DWORD dwData,
    POINT ptMouse,
    IDispatch *pDispatchObjectHit);
void __RPC_STUB IDocHostShowUI_ShowHelp_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IDocHostShowUI_INTERFACE_DEFINED__ */

#define IClassFactory3 IClassFactoryEx
#define IID_IClassFactory3 IID_IClassFactoryEx
#ifndef __IClassFactoryEx_FWD_DEFINED__
#define __IClassFactoryEx_FWD_DEFINED__
typedef interface IClassFactoryEx IClassFactoryEx;
#endif

/*****************************************************************************
 * IClassFactoryEx interface
 */
#ifndef __IClassFactoryEx_INTERFACE_DEFINED__
#define __IClassFactoryEx_INTERFACE_DEFINED__

DEFINE_GUID(IID_IClassFactoryEx, 0x342d1ea0, 0xae25, 0x11d1, 0x89,0xc5, 0x00,0x60,0x08,0xc3,0xfb,0xfc);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IClassFactoryEx : public IClassFactory
{
    virtual HRESULT STDMETHODCALLTYPE CreateInstanceWithContext(
        IUnknown *punkContext,
        IUnknown *punkOuter,
        REFIID riid,
        void **ppv) = 0;

};
#else
typedef struct IClassFactoryExVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IClassFactoryEx* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IClassFactoryEx* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IClassFactoryEx* This);

    /*** IClassFactory methods ***/
    HRESULT (STDMETHODCALLTYPE *CreateInstance)(
        IClassFactoryEx* This,
        IUnknown *pUnkOuter,
        REFIID riid,
        void **ppvObject);

    HRESULT (STDMETHODCALLTYPE *LockServer)(
        IClassFactoryEx* This,
        BOOL fLock);

    /*** IClassFactoryEx methods ***/
    HRESULT (STDMETHODCALLTYPE *CreateInstanceWithContext)(
        IClassFactoryEx* This,
        IUnknown *punkContext,
        IUnknown *punkOuter,
        REFIID riid,
        void **ppv);

    END_INTERFACE
} IClassFactoryExVtbl;
interface IClassFactoryEx {
    CONST_VTBL IClassFactoryExVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IClassFactoryEx_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IClassFactoryEx_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IClassFactoryEx_Release(This) (This)->lpVtbl->Release(This)
/*** IClassFactory methods ***/
#define IClassFactoryEx_CreateInstance(This,pUnkOuter,riid,ppvObject) (This)->lpVtbl->CreateInstance(This,pUnkOuter,riid,ppvObject)
#define IClassFactoryEx_LockServer(This,fLock) (This)->lpVtbl->LockServer(This,fLock)
/*** IClassFactoryEx methods ***/
#define IClassFactoryEx_CreateInstanceWithContext(This,punkContext,punkOuter,riid,ppv) (This)->lpVtbl->CreateInstanceWithContext(This,punkContext,punkOuter,riid,ppv)
#endif

#endif

HRESULT STDMETHODCALLTYPE IClassFactoryEx_CreateInstanceWithContext_Proxy(
    IClassFactoryEx* This,
    IUnknown *punkContext,
    IUnknown *punkOuter,
    REFIID riid,
    void **ppv);
void __RPC_STUB IClassFactoryEx_CreateInstanceWithContext_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IClassFactoryEx_INTERFACE_DEFINED__ */

typedef HRESULT WINAPI SHOWHTMLDIALOGFN(HWND,IMoniker*,VARIANT*,WCHAR*,VARIANT*);
typedef HRESULT WINAPI SHOWHTMLDIALOGEXFN(HWND,IMoniker*,DWORD,VARIANT*,WCHAR*,VARIANT*);
typedef HRESULT WINAPI SHOWMODELESSHTMLDIALOGFN(HWND,IMoniker*,VARIANT*,VARIANT*,IHTMLWindow2**);
EXTERN_C HRESULT WINAPI ShowHTMLDialog(HWND,IMoniker*,VARIANT*,WCHAR*,VARIANT*);
EXTERN_C HRESULT WINAPI ShowHTMLDialogEx(HWND,IMoniker*,DWORD,VARIANT*,WCHAR*,VARIANT*);
EXTERN_C HRESULT WINAPI ShowModelessHTMLDialog(HWND,IMoniker*,VARIANT*,VARIANT*,IHTMLWindow2**);
EXTERN_C HRESULT WINAPI RunHTMLApplication(HINSTANCE,HINSTANCE,LPSTR,int);
EXTERN_C HRESULT WINAPI CreateHTMLPropertyPage(IMoniker*,IPropertyPage**);
/* Begin additional prototypes for all interfaces */

ULONG           __RPC_USER HWND_UserSize     (ULONG *, ULONG, HWND *);
unsigned char * __RPC_USER HWND_UserMarshal  (ULONG *, unsigned char *, HWND *);
unsigned char * __RPC_USER HWND_UserUnmarshal(ULONG *, unsigned char *, HWND *);
void            __RPC_USER HWND_UserFree     (ULONG *, HWND *);
ULONG           __RPC_USER VARIANT_UserSize     (ULONG *, ULONG, VARIANT *);
unsigned char * __RPC_USER VARIANT_UserMarshal  (ULONG *, unsigned char *, VARIANT *);
unsigned char * __RPC_USER VARIANT_UserUnmarshal(ULONG *, unsigned char *, VARIANT *);
void            __RPC_USER VARIANT_UserFree     (ULONG *, VARIANT *);
ULONG           __RPC_USER BSTR_UserSize     (ULONG *, ULONG, BSTR *);
unsigned char * __RPC_USER BSTR_UserMarshal  (ULONG *, unsigned char *, BSTR *);
unsigned char * __RPC_USER BSTR_UserUnmarshal(ULONG *, unsigned char *, BSTR *);
void            __RPC_USER BSTR_UserFree     (ULONG *, BSTR *);

/* End additional prototypes */

#ifdef __cplusplus
}
#endif

#endif /* __WIDL_MSHTMHST_H */