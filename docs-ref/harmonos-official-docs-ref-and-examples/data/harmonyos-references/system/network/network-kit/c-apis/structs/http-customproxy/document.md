# Http\_CustomProxy

typedef struct Http\_CustomProxy {...} Http\_CustomProxy

#### Overview

Defines the custom proxy configuration.

**Since**: 20

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_http\_type.h](../../header-files/net-http-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char \*host | Host name of the proxy server. If no port is explicitly set, the port number is defaulted to **1080**. |
| int32\_t port | Host port. The value range is \[0, 65535\]. |
| const char \*exclusionLists | List of the names of hosts that do not use the HTTP proxy server. The host name can be a domain name, IP address, or wildcard. |
