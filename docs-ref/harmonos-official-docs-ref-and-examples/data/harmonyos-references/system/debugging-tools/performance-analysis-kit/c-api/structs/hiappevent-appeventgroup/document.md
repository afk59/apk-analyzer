# HiAppEvent\_AppEventGroup

typedef struct HiAppEvent\_AppEventGroup {...} HiAppEvent\_AppEventGroup

#### Overview

Defines the information of an event group, including its name, the array of event information grouped by name, and the length of the event array.

**Since**: 12

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

**Header file**: [hiappevent.h](../../header-files/hiappevent-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* name | Pointer to the event name. |
| const struct HiAppEvent\_AppEventInfo\* appEventInfos | Pointer to the array of events with the same event name. |
| uint32\_t infoLen | Length of the event array. |
