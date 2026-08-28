# About This Kit

Network Kit provides the following functions:

-   [HTTP data request](../network-access/using-http-for-network-access/document.md): initiates a data request through HTTP.
-   [WebSocket connection](../network-access/using-websocket-for-network-access/document.md): establishes a bidirectional connection between the server and client through WebSocket.
-   [Socket connection](../network-access/using-socket-for-network-access/document.md): transmits data through Socket.
-   [Network connection management](../network-connection/network-connection-management/document.md): provides basic network management capabilities, including management of Wi-Fi/cellular/Ethernet connection priorities, network quality evaluation, subscription to network connection status changes, query of network connection information, and DNS resolution.
-   [mDNS management](../network-access/using-mdns-for-lan-access/document.md): provides Multicast DNS (mDNS) management capabilities, such as adding, removing, discovering, and resolving local services on a LAN.

#### Constraints

To use the functions of the network management module, you must obtain the permissions listed in the following table.

Before requesting permissions, ensure that the [basic principles for using permissions](../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).

| Permission | Description |
| :-- | :-- |
| ohos.permission.GET\_NETWORK\_INFO | Allows an application to obtain the network connection information. |
| ohos.permission.INTERNET | Allows an application to open network sockets to connect to the network. |
