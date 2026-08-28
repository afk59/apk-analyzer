# Camera\_ConcurrentInfo

typedef struct Camera\_ConcurrentInfo {...} Camera\_ConcurrentInfo

#### Overview

The struct describes the camera's concurrency information.

**Since**: 18

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

**Header file**: [camera.h](../../header-files/camera-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Camera\_Device](../camera-device/document.md) camera | Camera instance. |
| [Camera\_ConcurrentType](../../header-files/camera-h/document.md#camera_concurrenttype) type | Concurrency type of the camera. |
| [Camera\_SceneMode](../../header-files/camera-h/document.md#camera_scenemode)\* sceneModes | Scene modes supported by the camera. |
| [Camera\_OutputCapability](../camera-outputcapability/document.md)\* outputCapabilities | Output capabilities of the camera. |
| uint32\_t modeAndCapabilitySize | Output capability size of the camera. |
