/*** Autogenerated by WIDL 1.0-rc1 from sensevts.idl - Do not edit ***/
#include <rpc.h>
#include <rpcndr.h>

#ifndef __WIDL_SENSEVTS_H
#define __WIDL_SENSEVTS_H
#ifdef __cplusplus
extern "C" {
#endif

#include <oaidl.h>
typedef struct SENS_QOCINFO {
    DWORD dwSize;
    DWORD dwFlags;
    DWORD dwOutSpeed;
    DWORD dwInSpeed;
} SENS_QOCINFO;
typedef struct SENS_QOCINFO *LPSENS_QOCINFO;
#ifndef __ISensNetwork_FWD_DEFINED__
#define __ISensNetwork_FWD_DEFINED__
typedef interface ISensNetwork ISensNetwork;
#endif

/*****************************************************************************
 * ISensNetwork interface
 */
#ifndef __ISensNetwork_INTERFACE_DEFINED__
#define __ISensNetwork_INTERFACE_DEFINED__

#if defined(__cplusplus) && !defined(CINTERFACE)
interface ISensNetwork : public IDispatch
{
    virtual HRESULT STDMETHODCALLTYPE ConnectionMade(
        BSTR bstrConnection,
        ULONG ulType,
        LPSENS_QOCINFO lpQOCInfo) = 0;

    virtual HRESULT STDMETHODCALLTYPE ConnectionMadeNoQOCInfo(
        BSTR bstrConnection,
        ULONG ulType) = 0;

    virtual HRESULT STDMETHODCALLTYPE ConnectionLost(
        BSTR bstrConnection,
        ULONG ulType) = 0;

    virtual HRESULT STDMETHODCALLTYPE DestinationReachable(
        BSTR bstrDestination,
        BSTR bstrConnection,
        ULONG ulType,
        LPSENS_QOCINFO lpQOCInfo) = 0;

    virtual HRESULT STDMETHODCALLTYPE DestinationReachableNoQOCInfo(
        BSTR bstrDestination,
        BSTR bstrConnection,
        ULONG ulType) = 0;

};
#else
typedef struct ISensNetworkVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        ISensNetwork* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        ISensNetwork* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        ISensNetwork* This);

    /*** IDispatch methods ***/
    HRESULT (STDMETHODCALLTYPE *GetTypeInfoCount)(
        ISensNetwork* This,
        UINT *pctinfo);

    HRESULT (STDMETHODCALLTYPE *GetTypeInfo)(
        ISensNetwork* This,
        UINT iTInfo,
        LCID lcid,
        ITypeInfo **ppTInfo);

    HRESULT (STDMETHODCALLTYPE *GetIDsOfNames)(
        ISensNetwork* This,
        REFIID riid,
        LPOLESTR *rgszNames,
        UINT cNames,
        LCID lcid,
        DISPID *rgDispId);

    HRESULT (STDMETHODCALLTYPE *Invoke)(
        ISensNetwork* This,
        DISPID dispIdMember,
        REFIID riid,
        LCID lcid,
        WORD wFlags,
        DISPPARAMS *pDispParams,
        VARIANT *pVarResult,
        EXCEPINFO *pExcepInfo,
        UINT *puArgErr);

    /*** ISensNetwork methods ***/
    HRESULT (STDMETHODCALLTYPE *ConnectionMade)(
        ISensNetwork* This,
        BSTR bstrConnection,
        ULONG ulType,
        LPSENS_QOCINFO lpQOCInfo);

    HRESULT (STDMETHODCALLTYPE *ConnectionMadeNoQOCInfo)(
        ISensNetwork* This,
        BSTR bstrConnection,
        ULONG ulType);

    HRESULT (STDMETHODCALLTYPE *ConnectionLost)(
        ISensNetwork* This,
        BSTR bstrConnection,
        ULONG ulType);

    HRESULT (STDMETHODCALLTYPE *DestinationReachable)(
        ISensNetwork* This,
        BSTR bstrDestination,
        BSTR bstrConnection,
        ULONG ulType,
        LPSENS_QOCINFO lpQOCInfo);

    HRESULT (STDMETHODCALLTYPE *DestinationReachableNoQOCInfo)(
        ISensNetwork* This,
        BSTR bstrDestination,
        BSTR bstrConnection,
        ULONG ulType);

    END_INTERFACE
} ISensNetworkVtbl;
interface ISensNetwork {
    CONST_VTBL ISensNetworkVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define ISensNetwork_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define ISensNetwork_AddRef(This) (This)->lpVtbl->AddRef(This)
#define ISensNetwork_Release(This) (This)->lpVtbl->Release(This)
/*** IDispatch methods ***/
#define ISensNetwork_GetTypeInfoCount(This,pctinfo) (This)->lpVtbl->GetTypeInfoCount(This,pctinfo)
#define ISensNetwork_GetTypeInfo(This,iTInfo,lcid,ppTInfo) (This)->lpVtbl->GetTypeInfo(This,iTInfo,lcid,ppTInfo)
#define ISensNetwork_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) (This)->lpVtbl->GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)
#define ISensNetwork_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) (This)->lpVtbl->Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)
/*** ISensNetwork methods ***/
#define ISensNetwork_ConnectionMade(This,bstrConnection,ulType,lpQOCInfo) (This)->lpVtbl->ConnectionMade(This,bstrConnection,ulType,lpQOCInfo)
#define ISensNetwork_ConnectionMadeNoQOCInfo(This,bstrConnection,ulType) (This)->lpVtbl->ConnectionMadeNoQOCInfo(This,bstrConnection,ulType)
#define ISensNetwork_ConnectionLost(This,bstrConnection,ulType) (This)->lpVtbl->ConnectionLost(This,bstrConnection,ulType)
#define ISensNetwork_DestinationReachable(This,bstrDestination,bstrConnection,ulType,lpQOCInfo) (This)->lpVtbl->DestinationReachable(This,bstrDestination,bstrConnection,ulType,lpQOCInfo)
#define ISensNetwork_DestinationReachableNoQOCInfo(This,bstrDestination,bstrConnection,ulType) (This)->lpVtbl->DestinationReachableNoQOCInfo(This,bstrDestination,bstrConnection,ulType)
#endif

#endif

HRESULT STDMETHODCALLTYPE ISensNetwork_ConnectionMade_Proxy(
    ISensNetwork* This,
    BSTR bstrConnection,
    ULONG ulType,
    LPSENS_QOCINFO lpQOCInfo);
void __RPC_STUB ISensNetwork_ConnectionMade_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensNetwork_ConnectionMadeNoQOCInfo_Proxy(
    ISensNetwork* This,
    BSTR bstrConnection,
    ULONG ulType);
void __RPC_STUB ISensNetwork_ConnectionMadeNoQOCInfo_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensNetwork_ConnectionLost_Proxy(
    ISensNetwork* This,
    BSTR bstrConnection,
    ULONG ulType);
void __RPC_STUB ISensNetwork_ConnectionLost_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensNetwork_DestinationReachable_Proxy(
    ISensNetwork* This,
    BSTR bstrDestination,
    BSTR bstrConnection,
    ULONG ulType,
    LPSENS_QOCINFO lpQOCInfo);
void __RPC_STUB ISensNetwork_DestinationReachable_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensNetwork_DestinationReachableNoQOCInfo_Proxy(
    ISensNetwork* This,
    BSTR bstrDestination,
    BSTR bstrConnection,
    ULONG ulType);
void __RPC_STUB ISensNetwork_DestinationReachableNoQOCInfo_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __ISensNetwork_INTERFACE_DEFINED__ */

#ifndef __ISensOnNow_FWD_DEFINED__
#define __ISensOnNow_FWD_DEFINED__
typedef interface ISensOnNow ISensOnNow;
#endif

/*****************************************************************************
 * ISensOnNow interface
 */
#ifndef __ISensOnNow_INTERFACE_DEFINED__
#define __ISensOnNow_INTERFACE_DEFINED__

#if defined(__cplusplus) && !defined(CINTERFACE)
interface ISensOnNow : public IDispatch
{
    virtual HRESULT STDMETHODCALLTYPE OnAcPower(
        ) = 0;

    virtual HRESULT STDMETHODCALLTYPE OnBatteryPower(
        DWORD dwBatteryLifePercent) = 0;

    virtual HRESULT STDMETHODCALLTYPE BatteryLow(
        DWORD dwBatteryLifePercent) = 0;

};
#else
typedef struct ISensOnNowVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        ISensOnNow* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        ISensOnNow* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        ISensOnNow* This);

    /*** IDispatch methods ***/
    HRESULT (STDMETHODCALLTYPE *GetTypeInfoCount)(
        ISensOnNow* This,
        UINT *pctinfo);

    HRESULT (STDMETHODCALLTYPE *GetTypeInfo)(
        ISensOnNow* This,
        UINT iTInfo,
        LCID lcid,
        ITypeInfo **ppTInfo);

    HRESULT (STDMETHODCALLTYPE *GetIDsOfNames)(
        ISensOnNow* This,
        REFIID riid,
        LPOLESTR *rgszNames,
        UINT cNames,
        LCID lcid,
        DISPID *rgDispId);

    HRESULT (STDMETHODCALLTYPE *Invoke)(
        ISensOnNow* This,
        DISPID dispIdMember,
        REFIID riid,
        LCID lcid,
        WORD wFlags,
        DISPPARAMS *pDispParams,
        VARIANT *pVarResult,
        EXCEPINFO *pExcepInfo,
        UINT *puArgErr);

    /*** ISensOnNow methods ***/
    HRESULT (STDMETHODCALLTYPE *OnAcPower)(
        ISensOnNow* This);

    HRESULT (STDMETHODCALLTYPE *OnBatteryPower)(
        ISensOnNow* This,
        DWORD dwBatteryLifePercent);

    HRESULT (STDMETHODCALLTYPE *BatteryLow)(
        ISensOnNow* This,
        DWORD dwBatteryLifePercent);

    END_INTERFACE
} ISensOnNowVtbl;
interface ISensOnNow {
    CONST_VTBL ISensOnNowVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define ISensOnNow_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define ISensOnNow_AddRef(This) (This)->lpVtbl->AddRef(This)
#define ISensOnNow_Release(This) (This)->lpVtbl->Release(This)
/*** IDispatch methods ***/
#define ISensOnNow_GetTypeInfoCount(This,pctinfo) (This)->lpVtbl->GetTypeInfoCount(This,pctinfo)
#define ISensOnNow_GetTypeInfo(This,iTInfo,lcid,ppTInfo) (This)->lpVtbl->GetTypeInfo(This,iTInfo,lcid,ppTInfo)
#define ISensOnNow_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) (This)->lpVtbl->GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)
#define ISensOnNow_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) (This)->lpVtbl->Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)
/*** ISensOnNow methods ***/
#define ISensOnNow_OnAcPower(This) (This)->lpVtbl->OnAcPower(This)
#define ISensOnNow_OnBatteryPower(This,dwBatteryLifePercent) (This)->lpVtbl->OnBatteryPower(This,dwBatteryLifePercent)
#define ISensOnNow_BatteryLow(This,dwBatteryLifePercent) (This)->lpVtbl->BatteryLow(This,dwBatteryLifePercent)
#endif

#endif

HRESULT STDMETHODCALLTYPE ISensOnNow_OnAcPower_Proxy(
    ISensOnNow* This);
void __RPC_STUB ISensOnNow_OnAcPower_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensOnNow_OnBatteryPower_Proxy(
    ISensOnNow* This,
    DWORD dwBatteryLifePercent);
void __RPC_STUB ISensOnNow_OnBatteryPower_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensOnNow_BatteryLow_Proxy(
    ISensOnNow* This,
    DWORD dwBatteryLifePercent);
void __RPC_STUB ISensOnNow_BatteryLow_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __ISensOnNow_INTERFACE_DEFINED__ */

#ifndef __ISensLogon_FWD_DEFINED__
#define __ISensLogon_FWD_DEFINED__
typedef interface ISensLogon ISensLogon;
#endif

/*****************************************************************************
 * ISensLogon interface
 */
#ifndef __ISensLogon_INTERFACE_DEFINED__
#define __ISensLogon_INTERFACE_DEFINED__

#if defined(__cplusplus) && !defined(CINTERFACE)
interface ISensLogon : public IDispatch
{
    virtual HRESULT STDMETHODCALLTYPE Logon(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE Logoff(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE StartShell(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE DisplayLock(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE DisplayUnlock(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE StartScreenSaver(
        BSTR bstrUserName) = 0;

    virtual HRESULT STDMETHODCALLTYPE StopScreenSaver(
        BSTR bstrUserName) = 0;

};
#else
typedef struct ISensLogonVtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        ISensLogon* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        ISensLogon* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        ISensLogon* This);

    /*** IDispatch methods ***/
    HRESULT (STDMETHODCALLTYPE *GetTypeInfoCount)(
        ISensLogon* This,
        UINT *pctinfo);

    HRESULT (STDMETHODCALLTYPE *GetTypeInfo)(
        ISensLogon* This,
        UINT iTInfo,
        LCID lcid,
        ITypeInfo **ppTInfo);

    HRESULT (STDMETHODCALLTYPE *GetIDsOfNames)(
        ISensLogon* This,
        REFIID riid,
        LPOLESTR *rgszNames,
        UINT cNames,
        LCID lcid,
        DISPID *rgDispId);

    HRESULT (STDMETHODCALLTYPE *Invoke)(
        ISensLogon* This,
        DISPID dispIdMember,
        REFIID riid,
        LCID lcid,
        WORD wFlags,
        DISPPARAMS *pDispParams,
        VARIANT *pVarResult,
        EXCEPINFO *pExcepInfo,
        UINT *puArgErr);

    /*** ISensLogon methods ***/
    HRESULT (STDMETHODCALLTYPE *Logon)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *Logoff)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *StartShell)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *DisplayLock)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *DisplayUnlock)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *StartScreenSaver)(
        ISensLogon* This,
        BSTR bstrUserName);

    HRESULT (STDMETHODCALLTYPE *StopScreenSaver)(
        ISensLogon* This,
        BSTR bstrUserName);

    END_INTERFACE
} ISensLogonVtbl;
interface ISensLogon {
    CONST_VTBL ISensLogonVtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define ISensLogon_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define ISensLogon_AddRef(This) (This)->lpVtbl->AddRef(This)
#define ISensLogon_Release(This) (This)->lpVtbl->Release(This)
/*** IDispatch methods ***/
#define ISensLogon_GetTypeInfoCount(This,pctinfo) (This)->lpVtbl->GetTypeInfoCount(This,pctinfo)
#define ISensLogon_GetTypeInfo(This,iTInfo,lcid,ppTInfo) (This)->lpVtbl->GetTypeInfo(This,iTInfo,lcid,ppTInfo)
#define ISensLogon_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) (This)->lpVtbl->GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)
#define ISensLogon_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) (This)->lpVtbl->Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)
/*** ISensLogon methods ***/
#define ISensLogon_Logon(This,bstrUserName) (This)->lpVtbl->Logon(This,bstrUserName)
#define ISensLogon_Logoff(This,bstrUserName) (This)->lpVtbl->Logoff(This,bstrUserName)
#define ISensLogon_StartShell(This,bstrUserName) (This)->lpVtbl->StartShell(This,bstrUserName)
#define ISensLogon_DisplayLock(This,bstrUserName) (This)->lpVtbl->DisplayLock(This,bstrUserName)
#define ISensLogon_DisplayUnlock(This,bstrUserName) (This)->lpVtbl->DisplayUnlock(This,bstrUserName)
#define ISensLogon_StartScreenSaver(This,bstrUserName) (This)->lpVtbl->StartScreenSaver(This,bstrUserName)
#define ISensLogon_StopScreenSaver(This,bstrUserName) (This)->lpVtbl->StopScreenSaver(This,bstrUserName)
#endif

#endif

HRESULT STDMETHODCALLTYPE ISensLogon_Logon_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_Logon_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_Logoff_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_Logoff_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_StartShell_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_StartShell_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_DisplayLock_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_DisplayLock_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_DisplayUnlock_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_DisplayUnlock_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_StartScreenSaver_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_StartScreenSaver_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon_StopScreenSaver_Proxy(
    ISensLogon* This,
    BSTR bstrUserName);
void __RPC_STUB ISensLogon_StopScreenSaver_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __ISensLogon_INTERFACE_DEFINED__ */

#ifndef __ISensLogon2_FWD_DEFINED__
#define __ISensLogon2_FWD_DEFINED__
typedef interface ISensLogon2 ISensLogon2;
#endif

/*****************************************************************************
 * ISensLogon2 interface
 */
#ifndef __ISensLogon2_INTERFACE_DEFINED__
#define __ISensLogon2_INTERFACE_DEFINED__

#if defined(__cplusplus) && !defined(CINTERFACE)
interface ISensLogon2 : public IDispatch
{
    virtual HRESULT STDMETHODCALLTYPE Logon(
        BSTR bstrUserName,
        DWORD dwSessionId) = 0;

    virtual HRESULT STDMETHODCALLTYPE Logoff(
        BSTR bstrUserName,
        DWORD dwSessionId) = 0;

    virtual HRESULT STDMETHODCALLTYPE SessionDisconnect(
        BSTR bstrUserName,
        DWORD dwSessionId) = 0;

    virtual HRESULT STDMETHODCALLTYPE SessionReconnect(
        BSTR bstrUserName,
        DWORD dwSessionId) = 0;

    virtual HRESULT STDMETHODCALLTYPE PostShell(
        BSTR bstrUserName,
        DWORD dwSessionId) = 0;

};
#else
typedef struct ISensLogon2Vtbl {
    BEGIN_INTERFACE

    /*** IUnknown methods ***/
    HRESULT (STDMETHODCALLTYPE *QueryInterface)(
        ISensLogon2* This,
        REFIID riid,
        void **ppvObject);

    ULONG (STDMETHODCALLTYPE *AddRef)(
        ISensLogon2* This);

    ULONG (STDMETHODCALLTYPE *Release)(
        ISensLogon2* This);

    /*** IDispatch methods ***/
    HRESULT (STDMETHODCALLTYPE *GetTypeInfoCount)(
        ISensLogon2* This,
        UINT *pctinfo);

    HRESULT (STDMETHODCALLTYPE *GetTypeInfo)(
        ISensLogon2* This,
        UINT iTInfo,
        LCID lcid,
        ITypeInfo **ppTInfo);

    HRESULT (STDMETHODCALLTYPE *GetIDsOfNames)(
        ISensLogon2* This,
        REFIID riid,
        LPOLESTR *rgszNames,
        UINT cNames,
        LCID lcid,
        DISPID *rgDispId);

    HRESULT (STDMETHODCALLTYPE *Invoke)(
        ISensLogon2* This,
        DISPID dispIdMember,
        REFIID riid,
        LCID lcid,
        WORD wFlags,
        DISPPARAMS *pDispParams,
        VARIANT *pVarResult,
        EXCEPINFO *pExcepInfo,
        UINT *puArgErr);

    /*** ISensLogon2 methods ***/
    HRESULT (STDMETHODCALLTYPE *Logon)(
        ISensLogon2* This,
        BSTR bstrUserName,
        DWORD dwSessionId);

    HRESULT (STDMETHODCALLTYPE *Logoff)(
        ISensLogon2* This,
        BSTR bstrUserName,
        DWORD dwSessionId);

    HRESULT (STDMETHODCALLTYPE *SessionDisconnect)(
        ISensLogon2* This,
        BSTR bstrUserName,
        DWORD dwSessionId);

    HRESULT (STDMETHODCALLTYPE *SessionReconnect)(
        ISensLogon2* This,
        BSTR bstrUserName,
        DWORD dwSessionId);

    HRESULT (STDMETHODCALLTYPE *PostShell)(
        ISensLogon2* This,
        BSTR bstrUserName,
        DWORD dwSessionId);

    END_INTERFACE
} ISensLogon2Vtbl;
interface ISensLogon2 {
    CONST_VTBL ISensLogon2Vtbl* lpVtbl;
};

#ifdef COBJMACROS
/*** IUnknown methods ***/
#define ISensLogon2_QueryInterface(This,riid,ppvObject) (This)->lpVtbl->QueryInterface(This,riid,ppvObject)
#define ISensLogon2_AddRef(This) (This)->lpVtbl->AddRef(This)
#define ISensLogon2_Release(This) (This)->lpVtbl->Release(This)
/*** IDispatch methods ***/
#define ISensLogon2_GetTypeInfoCount(This,pctinfo) (This)->lpVtbl->GetTypeInfoCount(This,pctinfo)
#define ISensLogon2_GetTypeInfo(This,iTInfo,lcid,ppTInfo) (This)->lpVtbl->GetTypeInfo(This,iTInfo,lcid,ppTInfo)
#define ISensLogon2_GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId) (This)->lpVtbl->GetIDsOfNames(This,riid,rgszNames,cNames,lcid,rgDispId)
#define ISensLogon2_Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr) (This)->lpVtbl->Invoke(This,dispIdMember,riid,lcid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr)
/*** ISensLogon2 methods ***/
#define ISensLogon2_Logon(This,bstrUserName,dwSessionId) (This)->lpVtbl->Logon(This,bstrUserName,dwSessionId)
#define ISensLogon2_Logoff(This,bstrUserName,dwSessionId) (This)->lpVtbl->Logoff(This,bstrUserName,dwSessionId)
#define ISensLogon2_SessionDisconnect(This,bstrUserName,dwSessionId) (This)->lpVtbl->SessionDisconnect(This,bstrUserName,dwSessionId)
#define ISensLogon2_SessionReconnect(This,bstrUserName,dwSessionId) (This)->lpVtbl->SessionReconnect(This,bstrUserName,dwSessionId)
#define ISensLogon2_PostShell(This,bstrUserName,dwSessionId) (This)->lpVtbl->PostShell(This,bstrUserName,dwSessionId)
#endif

#endif

HRESULT STDMETHODCALLTYPE ISensLogon2_Logon_Proxy(
    ISensLogon2* This,
    BSTR bstrUserName,
    DWORD dwSessionId);
void __RPC_STUB ISensLogon2_Logon_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon2_Logoff_Proxy(
    ISensLogon2* This,
    BSTR bstrUserName,
    DWORD dwSessionId);
void __RPC_STUB ISensLogon2_Logoff_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon2_SessionDisconnect_Proxy(
    ISensLogon2* This,
    BSTR bstrUserName,
    DWORD dwSessionId);
void __RPC_STUB ISensLogon2_SessionDisconnect_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon2_SessionReconnect_Proxy(
    ISensLogon2* This,
    BSTR bstrUserName,
    DWORD dwSessionId);
void __RPC_STUB ISensLogon2_SessionReconnect_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);
HRESULT STDMETHODCALLTYPE ISensLogon2_PostShell_Proxy(
    ISensLogon2* This,
    BSTR bstrUserName,
    DWORD dwSessionId);
void __RPC_STUB ISensLogon2_PostShell_Stub(
    IRpcStubBuffer* This,
    IRpcChannelBuffer* pRpcChannelBuffer,
    PRPC_MESSAGE pRpcMessage,
    DWORD* pdwStubPhase);

#endif  /* __ISensLogon2_INTERFACE_DEFINED__ */

/* Begin additional prototypes for all interfaces */

ULONG           __RPC_USER BSTR_UserSize     (ULONG *, ULONG, BSTR *);
unsigned char * __RPC_USER BSTR_UserMarshal  (ULONG *, unsigned char *, BSTR *);
unsigned char * __RPC_USER BSTR_UserUnmarshal(ULONG *, unsigned char *, BSTR *);
void            __RPC_USER BSTR_UserFree     (ULONG *, BSTR *);

/* End additional prototypes */

#ifdef __cplusplus
}
#endif

#endif /* __WIDL_SENSEVTS_H */
