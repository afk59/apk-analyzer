# WebSocket\_Header

struct WebSocket\_Header {...}

#### Overview

Defines the header linked list added to the WebSocket client.

**Since**: 11

**Related module**: [netstack](../../modules/netstack/document.md)

**Header file**: [net\_websocket\_type.h](../../header-files/net-websocket-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char \*fieldName | Pointer to the field name of a header. |
| const char \*fieldValue | Pointer to the field value of a header. |
| struct [WebSocket\_Header](#) \*next | Next pointer of the header linked list. |
