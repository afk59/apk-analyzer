# HiAppEvent\_AppEventInfo

typedef struct HiAppEvent\_AppEventInfo {...} HiAppEvent\_AppEventInfo

#### Overview

Defines a struct for the information about a single event, including the domain, name, type, and custom parameter list in JSON string format.

**Since**: 12

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

**Header file**: [hiappevent.h](../../header-files/hiappevent-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* domain | Pointer to the event domain. |
| const char\* name | Pointer to the event name. |
| enum [EventType](../../header-files/hiappevent-h/document.md#eventtype) type | Event type. |
| const char\* params | Event parameter list in JSON format. |
