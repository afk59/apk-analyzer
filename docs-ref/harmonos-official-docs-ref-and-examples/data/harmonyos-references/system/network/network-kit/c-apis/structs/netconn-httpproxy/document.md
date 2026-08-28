# NetConn\_HttpProxy

typedef struct NetConn\_HttpProxy {...} NetConn\_HttpProxy

#### Overview

Defines the proxy configuration.

**Since**: 11

**Related module**: [NetConnection](../../modules/netconnection/document.md)

**Header file**: [net\_connection\_type.h](../../header-files/net-connection-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char host[\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Host name. |
| char exclusionList[\[NETCONN\_MAX\_EXCLUSION\_SIZE\]](../../header-files/net-connection-type-h/document.md#macros) [\[NETCONN\_MAX\_STR\_LEN\]](../../header-files/net-connection-type-h/document.md#macros) | Exclusion list of proxy servers. |
| int32\_t exclusionListSize | Actual size of the exclusion list. |
| uint16\_t port | Port number. |
