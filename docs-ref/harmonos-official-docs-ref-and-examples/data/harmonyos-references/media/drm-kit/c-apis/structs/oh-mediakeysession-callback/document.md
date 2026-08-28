# OH\_MediaKeySession\_Callback

typedef struct OH\_MediaKeySession\_Callback {...} OH\_MediaKeySession\_Callback

#### Overview

The OH\_MediaKeySession\_Callback struct describes the callbacks for media key session events such as key expiration and key changes. It provides a MediaKeySession instance, making it suitable for multi-session decryption scenarios.

**Since**: 12

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_mediakeysession.h](../../header-files/native-mediakeysession-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_MediaKeySession\_EventCallback](../../header-files/native-mediakeysession-h/document.md#oh_mediakeysession_eventcallback) eventCallback | Callback for standard events, such as key expiration. |
| [OH\_MediaKeySession\_KeyChangeCallback](../../header-files/native-mediakeysession-h/document.md#oh_mediakeysession_keychangecallback) keyChangeCallback | Callback for media key change events. |
