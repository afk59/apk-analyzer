# When the Camera Is Blocked for a Period of Time and Then Uncovered, the Output Pose Changes Dramatically

#### Problem

During the usage of the motion tracking capability, if the camera is blocked for a period of time and then uncovered, the translation component or rotation component obtained by calling [HMS\_AREngine\_ARPose\_GetPoseRaw](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1ee66c006ffe8255cc04f2a24c277709) changes dramatically.

#### Possible Causes

AR Engine perceives the device's pose in the real world by collecting data from the camera. When the camera is blocked, AR Engine cannot accurately detect changes in the device's pose in the real world. After the camera is uncovered, if you continue to call [HMS\_AREngine\_ARSession\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1d1cacf372a8011a439f0e4e76994259), AR Engine will attempt to recover based on the data recognized before the camera is blocked. If the current camera data is similar to the data before the camera is blocked, it may lead to incorrect matching with old results, causing dramatic data changes.

#### Procedure

If [HMS\_AREngine\_ARCamera\_GetTrackingState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dc931eee56ae5ea899f8acc08eb3f36) returns **ARENGINE\_TRACKING\_STATE\_PAUSED**, call [HMS\_AREngine\_ARCamera\_GetTrackingStateReason](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab5411813f2e4ac6de4ebbccfc1bbbd35) to further troubleshoot the cause of tracking being paused. If the cause returned is **ARENGINE\_TRACKING\_STATE\_REASON\_INSUFFICIENT\_FEATURES** or **ARENGINE\_TRACKING\_STATE\_REASON\_EXCESSIVE\_MOTION**, you are advised to notify the user in your app and initialize the session again after the tracking is resumed (when the status returned by [HMS\_AREngine\_ARCamera\_GetTrackingState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dc931eee56ae5ea899f8acc08eb3f36) is **ARENGINE\_TRACKING\_STATE\_TRACKING**). For details, please refer to [Creating an AR Session](../../ar-engine-development-guidelines-c-c/managing-ar-sessions/document.md#section416624191615).
