/*** Autogenerated by WIDL 1.0-rc1 from bits1_5.idl - Do not edit ***/
#include <rpc.h>
#include <rpcndr.h>

#ifndef __WIDL_BITS1_5_H
#define __WIDL_BITS1_5_H
#ifdef __cplusplus
extern "C" {
#endif

#include <bits.h>
#ifndef __IBackgroundCopyJob2_FWD_DEFINED__
#define __IBackgroundCopyJob2_FWD_DEFINED__
typedef interface IBackgroundCopyJob2 IBackgroundCopyJob2;
#endif

typedef struct _BG_JOB_REPLY_PROGRESS {
    UINT64 BytesTotal;
    UINT64 BytesTransferred;
} BG_JOB_REPLY_PROGRESS;
typedef enum __WIDL_bits1_5_generated_name_00000000 {
    BG_AUTH_TARGET_SERVER = 1,
    BG_AUTH_TARGET_PROXY = 2
} BG_AUTH_TARGET;
typedef enum __WIDL_bits1_5_generated_name_00000001 {
    BG_AUTH_SCHEME_BASIC = 1,
    BG_AUTH_SCHEME_DIGEST = 2,
    BG_AUTH_SCHEME_NTLM = 3,
    BG_AUTH_SCHEME_NEGOTIATE = 4,
    BG_AUTH_SCHEME_PASSPORT = 5
} BG_AUTH_SCHEME;
typedef struct __WIDL_bits1_5_generated_name_00000002 {
    LPWSTR UserName;
    LPWSTR Password;
} BG_BASIC_CREDENTIALS;
typedef BG_BASIC_CREDENTIALS *PBG_BASIC_CREDENTIALS;
typedef union __WIDL_bits1_5_generated_name_00000003 {
    BG_BASIC_CREDENTIALS Basic;
} BG_AUTH_CREDENTIALS_UNION;
typedef struct __WIDL_bits1_5_generated_name_00000004 {
    BG_AUTH_TARGET Target;
    BG_AUTH_SCHEME Scheme;
    BG_AUTH_CREDENTIALS_UNION Credentials;
} BG_AUTH_CREDENTIALS;
typedef BG_AUTH_CREDENTIALS *PBG_AUTH_CREDENTIALS;
/*****************************************************************************
 * IBackgroundCopyJob2 interface
 */
#ifndef __IBackgroundCopyJob2_INTERFACE_DEFINED__
#define __IBackgroundCopyJob2_INTERFACE_DEFINED__

DEFINE_GUID(IID_IBackgroundCopyJob2, 0x54b50739, 0x686f, 0x45eb, 0x9d,0xff, 0xd6,0xa9,0xa0,0xfa,0xa9,0xaf);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IBackgroundCopyJob2 : public IBackgroundCopyJob
{
    virtual HRESULT STDMETHODCALLTYPE SetNotifyCmdLine(
        LPCWSTR prog,
        LPCWSTR params) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetNotifyCmdLine(
        LPWSTR prog,
        LPWSTR params) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetReplyProgress(
        BG_JOB_REPLY_PROGRESS *progress) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetReplyData(
        byte **pBuffer,
        UINT64 *pLength) = 0;

    virtual HRESULT STDMETHODCALLTYPE SetReplyFileName(
        LPCWSTR filename) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetReplyFileName(
        LPWSTR *pFilename) = 0;

    virtual HRESULT STDMETHODCALLTYPE SetCredentials(
        BG_AUTH_CREDENTIALS *cred) = 0;

    virtual HRESULT STDMETHODCALLTYPE RemoveCredentials(
        BG_AUTH_TARGET target,
        BG_AUTH_SCHEME scheme) = 0;

};
#else
typedef struct IBackgroundCopyJob2Vtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IBackgroundCopyJob2* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IBackgroundCopyJob2* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IBackgroundCopyJob2* This);

    /*** IBackgroundCopyJob methods ***/
    HRESULT (STDMETHODCALLTYPE *AddFileSet)(
        IBackgroundCopyJob2* This,
        ULONG cFileCount,
        BG_FILE_INFO *pFileSet);

    HRESULT (STDMETHODCALLTYPE *AddFile)(
        IBackgroundCopyJob2* This,
        LPCWSTR RemoteUrl,
        LPCWSTR LocalName);

    HRESULT (STDMETHODCALLTYPE *EnumFiles)(
        IBackgroundCopyJob2* This,
        IEnumBackgroundCopyFiles **pEnum);

    HRESULT (STDMETHODCALLTYPE *Suspend)(
        IBackgroundCopyJob2* This);

    HRESULT (STDMETHODCALLTYPE *Resume)(
        IBackgroundCopyJob2* This);

    HRESULT (STDMETHODCALLTYPE *Cancel)(
        IBackgroundCopyJob2* This);

    HRESULT (STDMETHODCALLTYPE *Complete)(
        IBackgroundCopyJob2* This);

    HRESULT (STDMETHODCALLTYPE *GetId)(
        IBackgroundCopyJob2* This,
        GUID *pVal);

    HRESULT (STDMETHODCALLTYPE *GetType)(
        IBackgroundCopyJob2* This,
        BG_JOB_TYPE *pVal);

    HRESULT (STDMETHODCALLTYPE *GetProgress)(
        IBackgroundCopyJob2* This,
        BG_JOB_PROGRESS *pVal);

    HRESULT (STDMETHODCALLTYPE *GetTimes)(
        IBackgroundCopyJob2* This,
        BG_JOB_TIMES *pVal);

    HRESULT (STDMETHODCALLTYPE *GetState)(
        IBackgroundCopyJob2* This,
        BG_JOB_STATE *pVal);

    HRESULT (STDMETHODCALLTYPE *GetError)(
        IBackgroundCopyJob2* This,
        IBackgroundCopyError **ppError);

    HRESULT (STDMETHODCALLTYPE *GetOwner)(
        IBackgroundCopyJob2* This,
        LPWSTR *pVal);

    HRESULT (STDMETHODCALLTYPE *SetDisplayName)(
        IBackgroundCopyJob2* This,
        LPCWSTR Val);

    HRESULT (STDMETHODCALLTYPE *GetDisplayName)(
        IBackgroundCopyJob2* This,
        LPWSTR *pVal);

    HRESULT (STDMETHODCALLTYPE *SetDescription)(
        IBackgroundCopyJob2* This,
        LPCWSTR Val);

    HRESULT (STDMETHODCALLTYPE *GetDescription)(
        IBackgroundCopyJob2* This,
        LPWSTR *pVal);

    HRESULT (STDMETHODCALLTYPE *SetPriority)(
        IBackgroundCopyJob2* This,
        BG_JOB_PRIORITY Val);

    HRESULT (STDMETHODCALLTYPE *GetPriority)(
        IBackgroundCopyJob2* This,
        BG_JOB_PRIORITY *pVal);

    HRESULT (STDMETHODCALLTYPE *SetNotifyFlags)(
        IBackgroundCopyJob2* This,
        ULONG Val);

    HRESULT (STDMETHODCALLTYPE *GetNotifyFlags)(
        IBackgroundCopyJob2* This,
        ULONG *pVal);

    HRESULT (STDMETHODCALLTYPE *SetNotifyInterface)(
        IBackgroundCopyJob2* This,
        IUnknown *Val);

    HRESULT (STDMETHODCALLTYPE *GetNotifyInterface)(
        IBackgroundCopyJob2* This,
        IUnknown **pVal);

    HRESULT (STDMETHODCALLTYPE *SetMinimumRetryDelay)(
        IBackgroundCopyJob2* This,
        ULONG Seconds);

    HRESULT (STDMETHODCALLTYPE *GetMinimumRetryDelay)(
        IBackgroundCopyJob2* This,
        ULONG *Seconds);

    HRESULT (STDMETHODCALLTYPE *SetNoProgressTimeout)(
        IBackgroundCopyJob2* This,
        ULONG Seconds);

    HRESULT (STDMETHODCALLTYPE *GetNoProgressTimeout)(
        IBackgroundCopyJob2* This,
        ULONG *Seconds);

    HRESULT (STDMETHODCALLTYPE *GetErrorCount)(
        IBackgroundCopyJob2* This,
        ULONG *Errors);

    HRESULT (STDMETHODCALLTYPE *SetProxySettings)(
        IBackgroundCopyJob2* This,
        BG_JOB_PROXY_USAGE ProxyUsage,
        const WCHAR *ProxyList,
        const WCHAR *ProxyBypassList);

    HRESULT (STDMETHODCALLTYPE *GetProxySettings)(
        IBackgroundCopyJob2* This,
        BG_JOB_PROXY_USAGE *pProxyUsage,
        LPWSTR *pProxyList,
        LPWSTR *pProxyBypassList);

    HRESULT (STDMETHODCALLTYPE *TakeOwnership)(
        IBackgroundCopyJob2* This);

    /*** IBackgroundCopyJob2 methods ***/
    HRESULT (STDMETHODCALLTYPE *SetNotifyCmdLine)(
        IBackgroundCopyJob2* This,
        LPCWSTR prog,
        LPCWSTR params);

    HRESULT (STDMETHODCALLTYPE *GetNotifyCmdLine)(
        IBackgroundCopyJob2* This,
        LPWSTR prog,
        LPWSTR params);

    HRESULT (STDMETHODCALLTYPE *GetReplyProgress)(
        IBackgroundCopyJob2* This,
        BG_JOB_REPLY_PROGRESS *progress);

    HRESULT (STDMETHODCALLTYPE *GetReplyData)(
        IBackgroundCopyJob2* This,
        byte **pBuffer,
        UINT64 *pLength);

    HRESULT (STDMETHODCALLTYPE *SetReplyFileName)(
        IBackgroundCopyJob2* This,
        LPCWSTR filename);

    HRESULT (STDMETHODCALLTYPE *GetReplyFileName)(
        IBackgroundCopyJob2* This,
        LPWSTR *pFilename);

    HRESULT (STDMETHODCALLTYPE *SetCredentials)(
        IBackgroundCopyJob2* This,
        BG_AUTH_CREDENTIALS *cred);

    HRESULT (STDMETHODCALLTYPE *RemoveCredentials)(
        IBackgroundCopyJob2* This,
        BG_AUTH_TARGET target,
        BG_AUTH_SCHEME scheme);

    END_INTERFACE
} IBackgroundCopyJob2Vtbl;
interface IBackgroundCopyJob2 {
    CONST_VTBL IBackgroundCopyJob2Vtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IBackgroundCopyJob2_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IBackgroundCopyJob2_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IBackgroundCopyJob2_Release(This) (This)->lpVtbl->Release(This)
/*** IBackgroundCopyJob methods ***/
#define IBackgroundCopyJob2_AddFileSet(This,cFileCount,pFileSet) (This)->lpVtbl->AddFileSet(This,cFileCount,pFileSet)
#define IBackgroundCopyJob2_AddFile(This,RemoteUrl,LocalName) (This)->lpVtbl->AddFile(This,RemoteUrl,LocalName)
#define IBackgroundCopyJob2_EnumFiles(This,pEnum) (This)->lpVtbl->EnumFiles(This,pEnum)
#define IBackgroundCopyJob2_Suspend(This) (This)->lpVtbl->Suspend(This)
#define IBackgroundCopyJob2_Resume(This) (This)->lpVtbl->Resume(This)
#define IBackgroundCopyJob2_Cancel(This) (This)->lpVtbl->Cancel(This)
#define IBackgroundCopyJob2_Complete(This) (This)->lpVtbl->Complete(This)
#define IBackgroundCopyJob2_GetId(This,pVal) (This)->lpVtbl->GetId(This,pVal)
#define IBackgroundCopyJob2_GetType(This,pVal) (This)->lpVtbl->GetType(This,pVal)
#define IBackgroundCopyJob2_GetProgress(This,pVal) (This)->lpVtbl->GetProgress(This,pVal)
#define IBackgroundCopyJob2_GetTimes(This,pVal) (This)->lpVtbl->GetTimes(This,pVal)
#define IBackgroundCopyJob2_GetState(This,pVal) (This)->lpVtbl->GetState(This,pVal)
#define IBackgroundCopyJob2_GetError(This,ppError) (This)->lpVtbl->GetError(This,ppError)
#define IBackgroundCopyJob2_GetOwner(This,pVal) (This)->lpVtbl->GetOwner(This,pVal)
#define IBackgroundCopyJob2_SetDisplayName(This,Val) (This)->lpVtbl->SetDisplayName(This,Val)
#define IBackgroundCopyJob2_GetDisplayName(This,pVal) (This)->lpVtbl->GetDisplayName(This,pVal)
#define IBackgroundCopyJob2_SetDescription(This,Val) (This)->lpVtbl->SetDescription(This,Val)
#define IBackgroundCopyJob2_GetDescription(This,pVal) (This)->lpVtbl->GetDescription(This,pVal)
#define IBackgroundCopyJob2_SetPriority(This,Val) (This)->lpVtbl->SetPriority(This,Val)
#define IBackgroundCopyJob2_GetPriority(This,pVal) (This)->lpVtbl->GetPriority(This,pVal)
#define IBackgroundCopyJob2_SetNotifyFlags(This,Val) (This)->lpVtbl->SetNotifyFlags(This,Val)
#define IBackgroundCopyJob2_GetNotifyFlags(This,pVal) (This)->lpVtbl->GetNotifyFlags(This,pVal)
#define IBackgroundCopyJob2_SetNotifyInterface(This,Val) (This)->lpVtbl->SetNotifyInterface(This,Val)
#define IBackgroundCopyJob2_GetNotifyInterface(This,pVal) (This)->lpVtbl->GetNotifyInterface(This,pVal)
#define IBackgroundCopyJob2_SetMinimumRetryDelay(This,Seconds) (This)->lpVtbl->SetMinimumRetryDelay(This,Seconds)
#define IBackgroundCopyJob2_GetMinimumRetryDelay(This,Seconds) (This)->lpVtbl->GetMinimumRetryDelay(This,Seconds)
#define IBackgroundCopyJob2_SetNoProgressTimeout(This,Seconds) (This)->lpVtbl->SetNoProgressTimeout(This,Seconds)
#define IBackgroundCopyJob2_GetNoProgressTimeout(This,Seconds) (This)->lpVtbl->GetNoProgressTimeout(This,Seconds)
#define IBackgroundCopyJob2_GetErrorCount(This,Errors) (This)->lpVtbl->GetErrorCount(This,Errors)
#define IBackgroundCopyJob2_SetProxySettings(This,ProxyUsage,ProxyList,ProxyBypassList) (This)->lpVtbl->SetProxySettings(This,ProxyUsage,ProxyList,ProxyBypassList)
#define IBackgroundCopyJob2_GetProxySettings(This,pProxyUsage,pProxyList,pProxyBypassList) (This)->lpVtbl->GetProxySettings(This,pProxyUsage,pProxyList,pProxyBypassList)
#define IBackgroundCopyJob2_TakeOwnership(This) (This)->lpVtbl->TakeOwnership(This)
/*** IBackgroundCopyJob2 methods ***/
#define IBackgroundCopyJob2_SetNotifyCmdLine(This,prog,params) (This)->lpVtbl->SetNotifyCmdLine(This,prog,params)
#define IBackgroundCopyJob2_GetNotifyCmdLine(This,prog,params) (This)->lpVtbl->GetNotifyCmdLine(This,prog,params)
#define IBackgroundCopyJob2_GetReplyProgress(This,progress) (This)->lpVtbl->GetReplyProgress(This,progress)
#define IBackgroundCopyJob2_GetReplyData(This,pBuffer,pLength) (This)->lpVtbl->GetReplyData(This,pBuffer,pLength)
#define IBackgroundCopyJob2_SetReplyFileName(This,filename) (This)->lpVtbl->SetReplyFileName(This,filename)
#define IBackgroundCopyJob2_GetReplyFileName(This,pFilename) (This)->lpVtbl->GetReplyFileName(This,pFilename)
#define IBackgroundCopyJob2_SetCredentials(This,cred) (This)->lpVtbl->SetCredentials(This,cred)
#define IBackgroundCopyJob2_RemoveCredentials(This,target,scheme) (This)->lpVtbl->RemoveCredentials(This,target,scheme)
#endif

#endif

HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_SetNotifyCmdLine_Proxy(
    IBackgroundCopyJob2* This,
    LPCWSTR prog,
    LPCWSTR params);
void __RPC_STUB IBackgroundCopyJob2_SetNotifyCmdLine_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_GetNotifyCmdLine_Proxy(
    IBackgroundCopyJob2* This,
    LPWSTR prog,
    LPWSTR params);
void __RPC_STUB IBackgroundCopyJob2_GetNotifyCmdLine_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_GetReplyProgress_Proxy(
    IBackgroundCopyJob2* This,
    BG_JOB_REPLY_PROGRESS *progress);
void __RPC_STUB IBackgroundCopyJob2_GetReplyProgress_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_GetReplyData_Proxy(
    IBackgroundCopyJob2* This,
    byte **pBuffer,
    UINT64 *pLength);
void __RPC_STUB IBackgroundCopyJob2_GetReplyData_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_SetReplyFileName_Proxy(
    IBackgroundCopyJob2* This,
    LPCWSTR filename);
void __RPC_STUB IBackgroundCopyJob2_SetReplyFileName_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_GetReplyFileName_Proxy(
    IBackgroundCopyJob2* This,
    LPWSTR *pFilename);
void __RPC_STUB IBackgroundCopyJob2_GetReplyFileName_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_SetCredentials_Proxy(
    IBackgroundCopyJob2* This,
    BG_AUTH_CREDENTIALS *cred);
void __RPC_STUB IBackgroundCopyJob2_SetCredentials_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IBackgroundCopyJob2_RemoveCredentials_Proxy(
    IBackgroundCopyJob2* This,
    BG_AUTH_TARGET target,
    BG_AUTH_SCHEME scheme);
void __RPC_STUB IBackgroundCopyJob2_RemoveCredentials_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IBackgroundCopyJob2_INTERFACE_DEFINED__ */

/* Begin additional prototypes for all interfaces */


/* End additional prototypes */

#ifdef __cplusplus
}
#endif

#endif /* __WIDL_BITS1_5_H */
