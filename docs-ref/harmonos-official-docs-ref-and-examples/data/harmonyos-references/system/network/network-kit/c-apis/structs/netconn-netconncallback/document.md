# NetConn\_NetConnCallback

typedef struct NetConn\_NetConnCallback {...} NetConn\_NetConnCallback

#### Overview

Defines network status callbacks.

**Since**: 12

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_NetConn\_NetworkAvailable](../../header-files/net-connection-type-h/document.md#oh_netconn_networkavailable) onNetworkAvailable | Callback invoked when the network is available. |
| [OH\_NetConn\_NetCapabilitiesChange](../../header-files/net-connection-type-h/document.md#oh_netconn_netcapabilitieschange) onNetCapabilitiesChange | Callback invoked when the network capabilities change. |
| [OH\_NetConn\_NetConnectionPropertiesChange](../../header-files/net-connection-type-h/document.md#oh_netconn_netconnectionpropertieschange) onConnetionProperties | Callback invoked when network connection properties change. |
| [OH\_NetConn\_NetLost](../../header-files/net-connection-type-h/document.md#oh_netconn_netlost) onNetLost | Callback invoked when the network is disconnected. |
| [OH\_NetConn\_NetUnavailable](../../header-files/net-connection-type-h/document.md#oh_netconn_netunavailable) onNetUnavailable | Callback invoked when the network is unavailable. This callback is triggered when the network is not activated within the specified timeout interval. If the timeout interval is not set, this callback is not triggered. |
| [OH\_NetConn\_NetBlockStatusChange](../../header-files/net-connection-type-h/document.md#oh_netconn_netblockstatuschange) onNetBlockStatusChange | Callback invoked when the network blocking status changes. |
