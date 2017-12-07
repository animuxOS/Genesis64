/*** Autogenerated by WIDL 1.0-rc1 from iads.idl - Do not edit ***/
#include <rpc.h>
#include <rpcndr.h>

#ifndef __WIDL_IADS_H
#define __WIDL_IADS_H
#ifdef __cplusplus
extern "C" {
#endif

#include <oaidl.h>
typedef enum __WIDL_iads_generated_name_00000000 {
    ADS_RIGHT_DS_CREATE_CHILD = 0x1,
    ADS_RIGHT_DS_DELETE_CHILD = 0x2,
    ADS_RIGHT_ACTRL_DS_LIST = 0x4,
    ADS_RIGHT_DS_SELF = 0x8,
    ADS_RIGHT_DS_READ_PROP = 0x10,
    ADS_RIGHT_DS_WRITE_PROP = 0x20,
    ADS_RIGHT_DS_DELETE_TREE = 0x40,
    ADS_RIGHT_DS_LIST_OBJECT = 0x80,
    ADS_RIGHT_DS_CONTROL_ACCESS = 0x100,
    ADS_RIGHT_DELETE = 0x10000,
    ADS_RIGHT_READ_CONTROL = 0x20000,
    ADS_RIGHT_WRITE_DAC = 0x40000,
    ADS_RIGHT_WRITE_OWNER = 0x80000,
    ADS_RIGHT_SYNCHRONIZE = 0x100000,
    ADS_RIGHT_ACCESS_SYSTEM_SECURITY = 0x200000,
    ADS_RIGHT_GENERIC_ALL = 0x10000000,
    ADS_RIGHT_GENERIC_EXECUTE = 0x20000000,
    ADS_RIGHT_GENERIC_WRITE = 0x40000000,
    ADS_RIGHT_GENERIC_READ = 0x80000000
} ADS_RIGHTS_ENUM;
#ifndef __IADsContainer_FWD_DEFINED__
#define __IADsContainer_FWD_DEFINED__
typedef interface IADsContainer IADsContainer;
#endif

/*****************************************************************************
 * IADsContainer interface
 */
#ifndef __IADsContainer_INTERFACE_DEFINED__
#define __IADsContainer_INTERFACE_DEFINED__

DEFINE_GUID(IID_IADsContainer, 0x001677d0, 0xfd16, 0x11ce, 0xab,0xc4, 0x02,0x60,0x8c,0x9e,0x75,0x53);
#if defined(__cplusplus) && !defined(CINTERFACE)
interface IADsContainer : public IDispatch
{
    virtual HRESULT STDMETHODCALLTYPE get_Count(
        long *retval) = 0;

    virtual HRESULT STDMETHODCALLTYPE get__NewEnum(
        IUnknown **retval) = 0;

    virtual HRESULT STDMETHODCALLTYPE get_Filter(
        VARIANT *pvFilter) = 0;

    virtual HRESULT STDMETHODCALLTYPE put_Filter(
        VARIANT vFilter) = 0;

    virtual HRESULT STDMETHODCALLTYPE get_Hints(
        VARIANT *pvHints) = 0;

    virtual HRESULT STDMETHODCALLTYPE put_Hints(
        VARIANT vHints) = 0;

    virtual HRESULT STDMETHODCALLTYPE GetObject(
        BSTR bstrClassName,
        BSTR bstrRelativeName,
        IDispatch **ppObject) = 0;

    virtual HRESULT STDMETHODCALLTYPE Create(
        BSTR bstrClassName,
        BSTR bstrRelativeName,
        IDispatch **ppObject) = 0;

    virtual HRESULT STDMETHODCALLTYPE Delete(
        BSTR bstrClassName,
        BSTR bstrRelativeName) = 0;

    virtual HRESULT STDMETHODCALLTYPE CopyHere(
        BSTR bstrSourceName,
        BSTR bstrNewName,
        IDispatch **ppObject) = 0;

    virtual HRESULT STDMETHODCALLTYPE MoveHere(
        BSTR bstrSourceName,
        BSTR bstrNewName,
        IDispatch **ppObject) = 0;

};
#else
typedef struct IADsContainerVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        IADsContainer* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        IADsContainer* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        IADsContainer* This);

    /*** IDispatch methods ***/
    HRESULT (STDMETHODCALLTYPE *GetTypeInfoCount)(
        IADsContainer* This,
        UINT *pctinfo);

    HRESULT (STDMETHODCALLTYPE *GetTypeInfo)(
        IADsContainer* This,
        UINT iTInfo,
        LCID lcid,
        ITypeInfo **ppTInfo);

    HRESULT (STDMETHODCALLTYPE *GetIDsOfNames)(
        IADsContainer* This,
        REFIID riid,
        LPOLESTR *rgszNames,
        UINT cNames,
        LCID lcid,
        DISPID *rgDispId);

    HRESULT (STDMETHODCALLTYPE *Invoke)(
        IADsContainer* This,
        DISPID dispIdMember,
        REFIID riid,
        LCID lcid,
        WORD wFlags,
        DISPPARAMS *pDispParams,
        VARIANT *pVarResult,
        EXCEPINFO *pExcepInfo,
        UINT *puArgErr);

    /*** IADsContainer methods ***/
    HRESULT (STDMETHODCALLTYPE *get_Count)(
        IADsContainer* This,
        long *retval);

    HRESULT (STDMETHODCALLTYPE *get__NewEnum)(
        IADsContainer* This,
        IUnknown **retval);

    HRESULT (STDMETHODCALLTYPE *get_Filter)(
        IADsContainer* This,
        VARIANT *pvFilter);

    HRESULT (STDMETHODCALLTYPE *put_Filter)(
        IADsContainer* This,
        VARIANT vFilter);

    HRESULT (STDMETHODCALLTYPE *get_Hints)(
        IADsContainer* This,
        VARIANT *pvHints);

    HRESULT (STDMETHODCALLTYPE *put_Hints)(
        IADsContainer* This,
        VARIANT vHints);

    HRESULT (STDMETHODCALLTYPE *GetObject)(
        IADsContainer* This,
        BSTR bstrClassName,
        BSTR bstrRelativeName,
        IDispatch **ppObject);

    HRESULT (STDMETHODCALLTYPE *Create)(
        IADsContainer* This,
        BSTR bstrClassName,
        BSTR bstrRelativeName,
        IDispatch **ppObject);

    HRESULT (STDMETHODCALLTYPE *Delete)(
        IADsContainer* This,
        BSTR bstrClassName,
        BSTR bstrRelativeName);

    HRESULT (STDMETHODCALLTYPE *CopyHere)(
        IADsContainer* This,
        BSTR bstrSourceName,
        BSTR bstrNewName,
        IDispatch **ppObject);

    HRESULT (STDMETHODCALLTYPE *MoveHere)(
        IADsContainer* This,
        BSTR bstrSourceName,
        BSTR bstrNewName,
        IDispatch **ppObject);

    END_INTERFACE
} IADsContainerVtbl;
interface IADsContainer {
    CONST_VTBL IADsContainerVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define IADsContainer_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define IADsContainer_AddRef(This) (This)->lpVtbl->AddRef(This)
#define IADsContainer_Release(This) (This)->lpVtbl->Release(This)
/*** IDispatch methods ***/
#define IADsContainer_GetTypeInfoCount(This,pctinfo) (This)->lpVtbl->GetTypeInfoCount(This,pctinfo)
#define IADsContainer_GetTypeInfo(This,iTInfo,lcid,ppTInfo) (This)->lpVtbl->GetTypeInfo(This,iTInfo,lcid,ppTInfo)
#define IADsContainer_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) (This)->lpVtbl->GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)
#define IADsContainer_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) (This)->lpVtbl->Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)
/*** IADsContainer methods ***/
#define IADsContainer_get_Count(This,retval) (This)->lpVtbl->get_Count(This,retval)
#define IADsContainer_get__NewEnum(This,retval) (This)->lpVtbl->get__NewEnum(This,retval)
#define IADsContainer_get_Filter(This,pvFilter) (This)->lpVtbl->get_Filter(This,pvFilter)
#define IADsContainer_put_Filter(This,vFilter) (This)->lpVtbl->put_Filter(This,vFilter)
#define IADsContainer_get_Hints(This,pvHints) (This)->lpVtbl->get_Hints(This,pvHints)
#define IADsContainer_put_Hints(This,vHints) (This)->lpVtbl->put_Hints(This,vHints)
#define IADsContainer_GetObject(This,bstrClassName,bstrRelativeName,ppObject) (This)->lpVtbl->GetObject(This,bstrClassName,bstrRelativeName,ppObject)
#define IADsContainer_Create(This,bstrClassName,bstrRelativeName,ppObject) (This)->lpVtbl->Create(This,bstrClassName,bstrRelativeName,ppObject)
#define IADsContainer_Delete(This,bstrClassName,bstrRelativeName) (This)->lpVtbl->Delete(This,bstrClassName,bstrRelativeName)
#define IADsContainer_CopyHere(This,bstrSourceName,bstrNewName,ppObject) (This)->lpVtbl->CopyHere(This,bstrSourceName,bstrNewName,ppObject)
#define IADsContainer_MoveHere(This,bstrSourceName,bstrNewName,ppObject) (This)->lpVtbl->MoveHere(This,bstrSourceName,bstrNewName,ppObject)
#endif

#endif

HRESULT STDMETHODCALLTYPE IADsContainer_get_Count_Proxy(
    IADsContainer* This,
    long *retval);
void __RPC_STUB IADsContainer_get_Count_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_get__NewEnum_Proxy(
    IADsContainer* This,
    IUnknown **retval);
void __RPC_STUB IADsContainer_get__NewEnum_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_get_Filter_Proxy(
    IADsContainer* This,
    VARIANT *pvFilter);
void __RPC_STUB IADsContainer_get_Filter_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_put_Filter_Proxy(
    IADsContainer* This,
    VARIANT vFilter);
void __RPC_STUB IADsContainer_put_Filter_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_get_Hints_Proxy(
    IADsContainer* This,
    VARIANT *pvHints);
void __RPC_STUB IADsContainer_get_Hints_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_put_Hints_Proxy(
    IADsContainer* This,
    VARIANT vHints);
void __RPC_STUB IADsContainer_put_Hints_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_GetObject_Proxy(
    IADsContainer* This,
    BSTR bstrClassName,
    BSTR bstrRelativeName,
    IDispatch **ppObject);
void __RPC_STUB IADsContainer_GetObject_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_Create_Proxy(
    IADsContainer* This,
    BSTR bstrClassName,
    BSTR bstrRelativeName,
    IDispatch **ppObject);
void __RPC_STUB IADsContainer_Create_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_Delete_Proxy(
    IADsContainer* This,
    BSTR bstrClassName,
    BSTR bstrRelativeName);
void __RPC_STUB IADsContainer_Delete_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_CopyHere_Proxy(
    IADsContainer* This,
    BSTR bstrSourceName,
    BSTR bstrNewName,
    IDispatch **ppObject);
void __RPC_STUB IADsContainer_CopyHere_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE IADsContainer_MoveHere_Proxy(
    IADsContainer* This,
    BSTR bstrSourceName,
    BSTR bstrNewName,
    IDispatch **ppObject);
void __RPC_STUB IADsContainer_MoveHere_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __IADsContainer_INTERFACE_DEFINED__ */

/* Begin additional prototypes for all interfaces */

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

#endif /* __WIDL_IADS_H */
