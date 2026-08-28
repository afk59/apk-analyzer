# Input\_InterceptorEventCallback

#### Overview

Defines the structure of interceptor callback events, including mouse events, touch events, and axis events.

**Since**: 12

**Related module**: [input](../../modules/input/document.md)

**Header file**: [oh\_input\_manager.h](../../header-files/oh-input-manager-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| Input\_MouseEventCallback mouseCallback | 
Callback for mouse events.

**Since**: 12

 |
| Input\_TouchEventCallback touchCallback | 

Callback used to return the touch event.

**Since**: 12

 |
| Input\_AxisEventCallback axisCallback | 

Callback for axis events.

**Since**: 12

 |

#### \[h2\]Member functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)](#input_keyeventcallback) | Input\_KeyEventCallback() | 
Defines the lifecycle callback for **keyEvent**. If the callback is triggered, **keyEvent** will be destroyed.

**Since**: 12

 |
| [typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)](#input_mouseeventcallback) | Input\_MouseEventCallback() | 

Defines the lifecycle callback for **mouseEvent**. If the callback is triggered, **mouseEvent** will be destroyed.

**Since**: 12

 |
| [typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)](#input_toucheventcallback) | Input\_TouchEventCallback() | 

Defines the lifecycle callback for **touchEvent**. If the callback is triggered, **touchEvent** will be destroyed.

**Since**: 12

 |
| [typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)](#input_axiseventcallback) | Input\_AxisEventCallback() | 

Defines the lifecycle callback for **axisEvent**. If the callback is triggered, **axisEvent** will be destroyed.

**Since**: 12

 |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](#input_deviceaddedcallback) | Input\_DeviceAddedCallback() | 

Defines the callback used to receive device insertion events.

**Since**: 13

 |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](#input_deviceremovedcallback) | Input\_DeviceRemovedCallback() | 

Defines the callback used to receive device removal events.

**Since**: 13

 |

#### Member Function Description

#### \[h2\]Input\_KeyEventCallback()

typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)

**Description**

Defines the lifecycle callback for **keyEvent**. If the callback is triggered, **keyEvent** will be destroyed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [Input\_KeyEvent](../input-keyevent/document.md)\* keyEvent | Key event object. |

#### \[h2\]Input\_MouseEventCallback()

typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)

**Description**

Defines the lifecycle callback for **mouseEvent**. If the callback is triggered, **mouseEvent** will be destroyed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [Input\_MouseEvent](../input-mouseevent/document.md)\* mouseEvent | Mouse event object. |

#### \[h2\]Input\_TouchEventCallback()

typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)

**Description**

Defines the lifecycle callback for **touchEvent**. If the callback is triggered, **touchEvent** will be destroyed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [Input\_TouchEvent](../input-touchevent/document.md)\* touchEvent | **touchEvent** object. |

#### \[h2\]Input\_AxisEventCallback()

typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)

**Description**

Defines the lifecycle callback for **axisEvent**. If the callback is triggered, **axisEvent** will be destroyed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [Input\_AxisEvent](../input-axisevent/document.md)\* axisEvent | Axis event object. |

#### \[h2\]Input\_DeviceAddedCallback()

typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)

**Description**

Defines the callback used to receive device insertion events.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |

#### \[h2\]Input\_DeviceRemovedCallback()

typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)

**Description**

Defines the callback used to receive device removal events.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t deviceId | Unique ID of the input device. If a physical device is repeatedly reinstalled or restarted, its ID may change. |
