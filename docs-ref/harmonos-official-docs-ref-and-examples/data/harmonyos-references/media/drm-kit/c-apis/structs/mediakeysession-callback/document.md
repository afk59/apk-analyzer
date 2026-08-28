# MediaKeySession\_Callback

typedef struct MediaKeySession\_Callback {...} MediaKeySession\_Callback

#### Overview

The MediaKeySession\_Callback struct describes the callbacks for media key session events such as key expiration and key changes. It does not provide a MediaKeySession instance, making it suitable for single-session decryption scenarios.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_mediakeysession.h](../../header-files/native-mediakeysession-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [MediaKeySession\_EventCallback](../../header-files/native-mediakeysession-h/document.md#mediakeysession_eventcallback) eventCallback | Callback for standard events, such as key expiration. |
| [MediaKeySession\_KeyChangeCallback](../../header-files/native-mediakeysession-h/document.md#mediakeysession_keychangecallback) keyChangeCallback | Callback for media key change events. |
