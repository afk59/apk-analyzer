# @ohos.UiTest

The **UiTest** module provides APIs that you can use to simulate UI actions during testing, such as clicks, double-clicks, long-clicks, and swipes.

This module provides the following functions:

-   [On9+](#on9): provides UI component feature description APIs for component filtering and matching.
-   [Component9+](#component9): represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.
-   [Driver9+](#driver9): works as the entry class and provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot.
-   [UiWindow9+](#uiwindow9): works as the entry class and provides APIs for obtaining window attributes, dragging windows, and adjusting window sizes.
-   [By(deprecated)](#bydeprecated): provides UI component feature description APIs for component filtering and matching. This API is supported since API version 8 and deprecated since API version 9. You are advised to use [On9+](#on9) instead.
-   [UiComponent(deprecated)](#uicomponentdeprecated): represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection. This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Component9+](#component9) instead.
-   [UiDriver(deprecated)](#uidriverdeprecated): works as the entry class and provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot. This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Driver9+](#driver9) instead.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/T6rbqvkxRkOFVCJgHQ2e3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB1D0D13765E967745F0833BB4E6C65735D9DB233910CBCB4AA9801A98E3D25A)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in [uitest](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uitest-guidelines).
-   The APIs of this module do not support concurrent calls.

#### Modules to Import

import { Component, Driver, UiWindow, ON, MatchPattern, DisplayRotation, ResizeDirection, WindowMode, PointerMatrix, UiDirection, MouseButton, UIElementInfo, UIEventObserver, UiComponent, UiDriver, BY } from '@kit.TestKit';

#### MatchPattern

Enumerates the match patterns supported for component attributes.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| EQUALS | 0 | 
Equals the given value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CONTAINS | 1 | 

Contains the given value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| STARTS\_WITH | 2 | 

Starts with the given value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ENDS\_WITH | 3 | 

Ends with the given value.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| REG\_EXP18+ | 4 | 

Uses regular expression matching.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| REG\_EXP\_ICASE18+ | 5 | 

Uses case-insensitive regular expression matching.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ResizeDirection9+

Enumerates the directions in which a window can be resized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | Left. |
| RIGHT | 1 | Right. |
| UP | 2 | Up. |
| DOWN | 3 | Down. |
| LEFT\_UP | 4 | Upper left. |
| LEFT\_DOWN | 5 | Lower left. |
| RIGHT\_UP | 6 | Upper right. |
| RIGHT\_DOWN | 7 | Lower right. |

#### Point9+

Provides the coordinates of a point.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | 
Horizontal coordinate of a coordinate point. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| y | number | No | No | 

Vertical coordinate of a coordinate point. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayId20+ | number | No | Yes | 

ID of the display to which the coordinate point belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### Rect9+

Provides bounds information of a component.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | 
X coordinate of the upper left corner of the component border. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| top | number | No | No | 

Y coordinate of the upper left corner of the component border. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| right | number | No | No | 

X coordinate of the lower right corner of the component border. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| bottom | number | No | No | 

Y coordinate of the lower right corner of the component border. The value is an integer greater than 0.

**Note**: Since API version 20, this attribute is no longer read-only.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayId20+ | number | No | Yes | 

ID of the display to which the component border belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### WindowMode9+

Enumerates the window modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| FULLSCREEN | 0 | Full-screen mode. |
| PRIMARY | 1 | Primary window mode. |
| SECONDARY | 2 | Secondary window mode. |
| FLOATING | 3 | Floating window mode. |

#### DisplayRotation9+

Describes the display rotation of the device.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| ROTATION\_0 | 0 | The device display is not rotated and is in its original vertical orientation. |
| ROTATION\_90 | 1 | The device display rotates 90° clockwise and is in landscape orientation. |
| ROTATION\_180 | 2 | The device display rotates 180° clockwise and is in reverse vertical orientation. |
| ROTATION\_270 | 3 | The device display rotates 270° clockwise and is in reverse landscape orientation. |

#### WindowFilter9+

Provides the flag attributes of this window.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | Yes | 
Bundle name of the application to which the window belongs. The default value is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| title | string | No | Yes | 

Title of the window. The default value is empty.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| focused | boolean | No | Yes | 

Whether the window is focused. The value **true** indicates that the window is focused, and **false** indicates the opposite. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| actived(deprecated) | boolean | No | Yes | 

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite.

This API is deprecated since API version 11. You are advised to use the **active** API instead.

 |
| active11+ | boolean | No | Yes | 

Whether the window is interacting with the user. The value **true** indicates that the window is interacting with the user, and **false** indicates the opposite.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayId20+ | number | No | Yes | 

ID of the display to which the window belongs. The value is an integer greater than or equal to 0. The default value is the default screen ID of the device.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### UiDirection10+

Describes the direction of a UI operation such as fling.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| LEFT | 0 | Leftward. |
| RIGHT | 1 | Rightward. |
| UP | 2 | Upward. |
| DOWN | 3 | Downward. |

#### MouseButton10+

Describes the injected simulated mouse button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| MOUSE\_BUTTON\_LEFT | 0 | Left button on the mouse. |
| MOUSE\_BUTTON\_RIGHT | 1 | Right button on the mouse. |
| MOUSE\_BUTTON\_MIDDLE | 2 | Middle button on the mouse. |

#### WindowChangeType22+

Enumerates the window change event types that can be listened for.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| WINDOW\_UNDEFINED | 0 | 
Non-window change event.

Note: This value can only be used as a return value. If it is passed in an API, an exception will be thrown.

 |
| WINDOW\_ADDED | 1 | Window adding event. |
| WINDOW\_REMOVED | 2 | Window removing event. |
| WINDOW\_BOUNDS\_CHANGED | 3 | Window bounds change event. |

#### ComponentEventType22+

Enumerates the component operation event types that can be listened for.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPONENT\_UNDEFINED | 0 | 
Non-component operation event.

Note: This value can only be used as a return value. If it is passed in an API, an exception will be thrown.

 |
| COMPONENT\_CLICKED | 1 | Component clicked event. |
| COMPONENT\_LONG\_CLICKED | 2 | Component long-clicked event. |
| COMPONENT\_SCROLL\_START | 3 | Component scroll start event. |
| COMPONENT\_SCROLL\_END | 4 | Component scroll end event. |
| COMPONENT\_TEXT\_CHANGED | 5 | Text change event of the [text input component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-text-input). |

#### WindowChangeOptions22+

Describes the extended configuration of window change event listening, which is used to specify the listening process configuration and event filtering conditions.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | No | Yes | Listening timeout interval, in milliseconds. The default value is 10000. |
| bundleName | string | No | Yes | Bundle name of the window to be listened for. By default, all windows are listened for. |

#### ComponentEventOptions22+

Describes the extended configuration of component operation event listening, which is used to specify the listening process configuration and event filtering conditions.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | No | Yes | Listening timeout interval, in milliseconds. The default value is 10000. |
| on | [On](#on9) | No | Yes | 
Attribute requirements of the target component to listen for. By default, all components are listened for.

**Note**: Only components with specified attributes can be listened for. Components with relative positions such as **On.isBefore**, **On.isAfter**, and **On.within** cannot be listened for.

 |

#### UIElementInfo10+

Provides information about the UI event.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | Yes | No | 
Bundle name of the application.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| type | string | Yes | No | 

Component or window type.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| text | string | Yes | No | 

Text information of the component or window.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| windowChangeType22+ | [WindowChangeType](#windowchangetype22) | Yes | Yes | 

Window change event type. If the event is not a window change event, **WindowChangeType.WINDOW\_UNDEFINED** is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| componentEventType22+ | [ComponentEventType](#componenteventtype22) | Yes | Yes | 

Component operation event type. If it is not a component operation event, **ComponentEventType.COMPONENT\_UNDEFINED** is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| windowId22+ | number | Yes | Yes | 

ID of the window where the component belongs.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| componentId22+ | string | Yes | Yes | 

Component ID. If it is not a component operation event, an empty string is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| componentRect22+ | [Rect](#rect9) | Yes | Yes | 

Component border information. If it is not a component operation event, a **Rect** object with all attribute values being **0** is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### TouchPadSwipeOptions18+

Describes information about the touchpad swipe gesture option.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| stay | boolean | No | Yes | Whether the swipe gesture stays on the touchpad for 1s before it is lifted. The value **true** indicates that the swipe gesture stays on the touchpad for 1s, and **false** indicates the opposite. The default value is **false**. |
| speed | number | No | Yes | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **2000**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value 2000 is used. If the value is a negative number, an error code indicating a parameter error is returned. |

#### InputTextMode20+

Describes the text input mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| paste | boolean | No | Yes | 
Whether to copy and paste text. The value **true** means to copy and paste text, and **false** means to type text. Default value: **false**

**Note**: If the input text contains Chinese characters, special characters, or the text length exceeds 200 characters, the text is copied and pasted regardless of the value of this parameter.

 |
| addition | boolean | No | Yes | Whether to input text in addition mode. The value **true** means to input text in addition mode, and **false** means the opposite. Default value: **false** |

#### On9+

Since API version 9, the UiTest framework provides a wide range of UI component feature description APIs in the **On** class to filter and match components.

The APIs provided by the **On** class exhibit the following features:

1\. Allow one or more attributes as the match conditions. For example, you can specify both the **text** and **id** attributes to find the target component.

2\. Provide multiple match patterns for component attributes.

3\. Support absolute positioning and relative positioning for components. APIs such as [ON.isBefore](#isbefore9) and [ON.isAfter](#isafter9) can be used to specify the features of adjacent components to assist positioning.

All APIs provided in the **On** class are synchronous. You are advised to use the static constructor **ON** to create an **On** object in chain mode.

// xxx.test.ets
import { ON } from '@kit.TestKit';

ON.text('123').type('Button');

#### \[h2\]text9+

text(txt: string, pattern?: MatchPattern): On

Specifies the text attribute of the target component. Multiple match patterns are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/QUDeP_ZHTPyRiyJ0cWZCWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D8FAD686C7FC013DDDF7AF1D3CA7AEF8E14BF430DAEF20DD6995ECC1EBFE842)

If the [accessibilityLevel](../../../../../application-framework/arkui/arkts-components/universal-attributes/accessibility/document.md#accessibilitylevel) of a component is set to **no** or **no-hide-descendants**, this API cannot be used to specify the text attribute of the target component for searching for the component. In this case, you can use the [On.originalText()](#originaltext20) API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| txt | string | Yes | Component text, used to match the target component. |
| pattern | [MatchPattern](#matchpattern) | No | Match pattern. The default value is [EQUALS](#matchpattern). |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the text attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // Use the static constructor ON to create an On object and specify the text attribute of the target component.

#### \[h2\]id9+

id(id: string): On

Specifies the ID attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Component ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the ID attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.id('123'); // Use the static constructor ON to create an On object and specify the ID attribute of the target component.

#### \[h2\]id18+

id(id: string, pattern: MatchPattern): On

Specifies the **id** attribute and match pattern of the target component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Component ID. |
| pattern | [MatchPattern](#matchpattern) | Yes | Text matching pattern. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the ID attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.id('id', MatchPattern.REG\_EXP\_ICASE); // Use case-insensitive regular expression to match the ID attribute value of the component.

#### \[h2\]type9+

type(tp: string): On

Specifies the type attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tp | string | Yes | Component type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the type attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // Use the static constructor ON to create an On object and specify the type attribute of the target component.

#### \[h2\]type18+

type(tp: string, pattern: MatchPattern): On

Specifies the **type** attribute and match pattern of the target component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tp | string | Yes | Component type. |
| pattern | [MatchPattern](#matchpattern) | Yes | Text matching pattern. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the type attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // Use the static constructor ON to create an On object and specify the type attribute of the target component.

#### \[h2\]clickable9+

clickable(b?: boolean): On

Specifies the clickable attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Clickable status of the component. The value **true** indicates that the component is clickable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the clickable attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.clickable(true); // Use the static constructor ON to create an On object and specify the clickable attribute of the target component.

#### \[h2\]longClickable9+

longClickable(b?: boolean): On

Specifies the long-clickable attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Long-clickable status of the component. The value **true** indicates that the component is long-clickable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the long-clickable attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.longClickable(true); // Use the static constructor ON to create an On object and specify the longClickable attribute of the target component.

#### \[h2\]scrollable9+

scrollable(b?: boolean): On

Specifies the scrollable attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Scrollable status of the component. The value **true** indicates that the component is scrollable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the scrollable attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.scrollable(true); // Use the static constructor ON to create an On object and specify the scrollable attribute of the target component.

#### \[h2\]enabled9+

enabled(b?: boolean): On

Specifies the enabled attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Enabled status of the component. The value **true** indicates that the component is enabled, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the enabled attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.enabled(true); // Use the static constructor ON to create an On object and specify the enabled attribute of the target component.

#### \[h2\]focused9+

focused(b?: boolean): On

Specifies the focused attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Focused status of the component. The value **true** indicates that the component is focused, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the focused attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.focused(true); // Use the static constructor ON to create an On object and specify the focused attribute of the target component.

#### \[h2\]selected9+

selected(b?: boolean): On

Specifies the selected attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Selected status of the component. The value **true** indicates that the component is selected, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the selected attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.selected(true); // Use the static constructor ON to create an On object and specify the selected attribute of the target component.

#### \[h2\]checked9+

checked(b?: boolean): On

Specifies the checked attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Checked status of the component. The value **true** indicates that the component is checked, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the checked attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checked(true); // Use the static constructor ON to create an On object and specify the checked attribute of the target component.

#### \[h2\]checkable9+

checkable(b?: boolean): On

Specifies the checkable attribute of the target component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Checkable status of the component. The value **true** indicates that the component is checkable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the checkable attribute of the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checkable(true); // Use the static constructor ON to create an On object and specify the checkable attribute of the target component.

#### \[h2\]isBefore9+

isBefore(on: On): On

Specifies that the target component is located before the given attribute component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Information about the attribute component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located before the given attribute component.
let on: On = ON.type('Button').isBefore(ON.text('123')); // Search for the first Button component located before the component whose text is 123.

#### \[h2\]isAfter9+

isAfter(on: On): On

Specifies that the target component is located after the given attribute component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Information about the attribute component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located after the given attribute component.
let on: On = ON.type('Text').isAfter(ON.text('123')); // Search for the first Text component located after the component whose text is 123.

#### \[h2\]within10+

within(on: On): On

Specifies that the target component is located within the given attribute component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Information about the attribute component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// Use the static constructor ON to create an On object and specify that the target component is located within the given attribute component.
let on: On = ON.text('java').within(ON.type('Scroll')); // Search for the child component whose text is java within the Scroller component.

#### \[h2\]inWindow10+

inWindow(bundleName: string): On

Specifies that the target component is located within the given application window.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application window. |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.inWindow('com.uitestScene.acts'); // Use the static constructor ON to create an On object and specify that the target component is located within the given application window.

#### \[h2\]description11+

description(val: string, pattern?: MatchPattern): On

Specifies the description of the target component. Multiple match patterns are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | string | Yes | Description of the component. |
| pattern | [MatchPattern](#matchpattern) | No | Match pattern. The default value is [EQUALS](#matchpattern). |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.description('123'); // Use the static constructor ON to create an On object and specify the description attribute of the target component.

#### \[h2\]hint18+

hint(val: string, pattern?: MatchPattern): On

Obtains the component object of the specified hint text and returns the **On** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | string | Yes | The specified hint text of the component. |
| pattern | [MatchPattern](#matchpattern) | No | Match pattern. The default value is [EQUALS](#matchpattern). |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | The **On** object of the specified hint text component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.hint('welcome', MatchPattern.EQUALS); // Use the static constructor ON to create an On object with the hint text attribute of the target component specified.

#### \[h2\]belongingDisplay20+

belongingDisplay(displayId: number): On

Obtains the component object on the specified display.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
ID of the display to which the component belongs. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported. You can use [getAllDisplays](../../../../../application-framework/arkui/arkts-api/display-management/ohos-display-display/document.md#displaygetalldisplays9) to obtain all current **display** objects and use them to obtain the corresponding display IDs.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | The **On** object of the display to which the specified component belongs. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.belongingDisplay(0); // Use the static constructor ON to create an On object and specify the ID of the display to which the target component belongs.

#### \[h2\]originalText20+

originalText(text: string, pattern?: MatchPattern): On

Specifies the text content and text matching pattern of the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/YSt_K6xMQ_GAfIKFMCLyeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57B6742832F870B23CB6752F46AEC78D9AA71FE388A9E8E30B45FB68DF977E70)

If the [accessibilityLevel](../../../../../application-framework/arkui/arkts-components/universal-attributes/accessibility/document.md#accessibilitylevel) of a component is set to **no** or **no-hide-descendants**, this API can be used to specify the text attribute of the target component for searching for the component. In this case, the [On.text()](#text9) API does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Component text, used to match the target component. |
| pattern | [MatchPattern](#matchpattern) | No | Match pattern. The default value is [EQUALS](#matchpattern). |

**Return value**

| Type | Description |
| :-- | :-- |
| [On](#on9) | **On** object that matches the text attribute of the target component. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.originalText('123'); // Use the static constructor ON to create an On object and specify the originalText attribute of the target component.

#### Component9+

Represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.

All APIs provided in this class use a promise to return the result and must be invoked using **await**.

#### \[h2\]click9+

click(): Promise<void>

Clicks this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.click();
}

#### \[h2\]doubleClick9+

doubleClick(): Promise<void>

Double-clicks this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.doubleClick();
}

#### \[h2\]longClick9+

longClick(): Promise<void>

Long-clicks this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.longClick();
}

#### \[h2\]getId9+

getId(): Promise<string>

Obtains the ID of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the component ID. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let id = await button.getId();
}

#### \[h2\]getText9+

getText(): Promise<string>

Obtains the text information of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/sV_IIeCIQ36fTu2vDedJsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEF41BCF91B482D0AEC4C070F0A2B4784B07118317DACC502E0B3A0C83F07A81)

If the [accessibilityLevel](../../../../../application-framework/arkui/arkts-components/universal-attributes/accessibility/document.md#accessibilitylevel) attribute of the component is set to **no** or **no-hide-descendants**, this API cannot be used to obtain the text information of the component. In this case, you can use [Component.getOriginalText ()](#getoriginaltext20) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the text information of the component. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getText();
}

#### \[h2\]getType9+

getType(): Promise<string>

Obtains the type of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the component type. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let type = await button.getType();
}

#### \[h2\]getBounds9+

getBounds(): Promise<Rect>

Obtains the bounds information of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Rect](#rect9)\> | Promise used to return the bound information of the component object. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let rect = await button.getBounds();
}

#### \[h2\]getBoundsCenter9+

getBoundsCenter(): Promise<Point>

Obtains the center point of the area occupied by this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise used to return the center point of the area occupied by the component object. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let point = await button.getBoundsCenter();
}

#### \[h2\]isClickable9+

isClickable(): Promise<boolean>

Obtains the clickable status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component object is clickable. The value **true** indicates that the component is clickable, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}

#### \[h2\]isLongClickable9+

isLongClickable(): Promise<boolean>

Obtains the long-clickable status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component object is long-clickable. The value **true** indicates that the component is long-clickable, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isLongClickable()) {
    console.info('This button can longClick');
  } else {
    console.info('This button can not longClick');
  }
}

#### \[h2\]isChecked9+

isChecked(): Promise<boolean>

Obtains the checked status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the checked status of the component object. The value **true** indicates that the component is checked, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isChecked()) {
    console.info('This checkBox is checked');
  } else {
    console.info('This checkBox is not checked');
  }
}

#### \[h2\]isCheckable9+

isCheckable(): Promise<boolean>

Obtains the checkable status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component object is checkable. The value **true** indicates that the component is checkable, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isCheckable()) {
    console.info('This checkBox is checkable');
  } else {
    console.info('This checkBox is not checkable');
  }
}

#### \[h2\]isScrollable9+

isScrollable(): Promise<boolean>

Obtains the scrollable status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component object is scrollable. The value **true** indicates that the component is scrollable, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}

#### \[h2\]isEnabled9+

isEnabled(): Promise<boolean>

Obtains the enabled status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is enabled. The value **true** indicates that the component is enabled, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}

#### \[h2\]isFocused9+

isFocused(): Promise<boolean>

Checks whether a component is focused. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is focused. The value **true** indicates that the component is focused, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}

#### \[h2\]isSelected9+

isSelected(): Promise<boolean>

Obtains the selected status of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is selected. The value **true** indicates that the component is selected, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}

#### \[h2\]inputText9+

inputText(text: string): Promise<void>

Clears the original text in a component and inputs the specified text. This API takes effect only for editable text components. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123');
}

#### \[h2\]inputText20+

inputText(text: string, mode: InputTextMode): Promise<void>

Inputs text to a component in a specified text input mode. This API takes effect only for editable text components. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |
| mode | [InputTextMode](#inputtextmode20) | Yes | 
Text input mode. For details, see [InputTextMode](#inputtextmode20).

**Note**: If **InputTextMode.addition** is set to **true**, the specified text is added to the end of the existing text in the component. Otherwise, the specified text overwrites the existing text of the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported, function can not work correctly due to limited device capabilities. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode\_demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123', { paste: true, addition: false });
}

#### \[h2\]clearText9+

clearText(): Promise<void>

Clears the text information of a component. This API takes effect only for editable text components. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.clearText();
}

#### \[h2\]scrollSearch9+

scrollSearch(on: On): Promise<Component>

Scrolls on this component to search for the target component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise used to return the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}

#### \[h2\]scrollSearch18+

scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>

Scrolls on this component to search for the target component. This API is applicable to components that support scrolling. You can specify the scrolling direction and the offset between the scrolling start and end points and the component border. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |
| vertical | boolean | No | Whether the search direction is vertical. The default value **true** indicates that the search direction is vertical. **false** indicates that the search direction is horizontal. |
| offset | number | No | Offset from the scrolling start/end point to the component border, in pixels. The default value is **80**. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise used to return the target component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}

#### \[h2\]scrollToTop9+

scrollToTop(speed?: number): Promise<void>

Scrolls to the top of this component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToTop();
}

#### \[h2\]scrollToBottom9+

scrollToBottom(speed?: number): Promise<void>

Scrolls to the bottom of this component. This API is applicable to components that support scrolling. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToBottom();
}

#### \[h2\]dragTo9+

dragTo(target: Component): Promise<void>

Drags a component to the target component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | [Component](#component9) | Yes | Target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await button.dragTo(text);
}

#### \[h2\]pinchOut9+

pinchOut(scale: number): Promise<void>

Pinches out a component at the specified scale. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | Scale factor, which is a value greater than 1. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchOut(1.5);
}

#### \[h2\]pinchIn9+

pinchIn(scale: number): Promise<void>

Pinches in a component at the specified scale. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | number | Yes | Scale factor, which is a value ranging from 0 to 1. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchIn(0.5);
}

#### \[h2\]getDescription11+

getDescription(): Promise<string>

Obtains the description of this component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the description of the component. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let description = await button.getDescription();
}

#### \[h2\]getHint18+

getHint(): Promise<string>

Obtains the hint text of a component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the hint text of a component. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let hints = await button.getHint();
}

#### \[h2\]getDisplayId20+

getDisplayId(): Promise<number>

Obtains the ID of the display to which the component belongs. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the ID of the display to which the component belongs. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let displayId = await button.getDisplayId();
}

#### \[h2\]getOriginalText20+

getOriginalText(): Promise<string>

Obtains the text information of this component. This API uses a promise to return the result. If the [accessibilityLevel](../../../../../application-framework/arkui/arkts-components/universal-attributes/accessibility/document.md#accessibilitylevel) attribute of the component is set to **no** or **no-hide-descendants**, this API can be used to obtain the text information of the component, but [Component.getText()](#gettext9) cannot.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the text information of the component. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getOriginalText();
}

#### Driver9+

The **Driver** class is the main entry to the UiTest framework. It provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot.

All APIs provided by this class, except **Driver.create()**, use a promise to return the result and must be invoked using **await**.

#### \[h2\]create9+

static create(): Driver

Creates a **Driver** object and returns the object created. This API is a static API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Driver | **Driver** object created. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000001 | Initialization failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
}

#### \[h2\]delayMs9+

delayMs(duration: number): Promise<void>

Delays execution for the specified duration. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | Specified time, in ms. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}

#### \[h2\]findComponent9+

findComponent(on: On): Promise<Component>

Searches for the target component based on the specified attributes. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise used to return the component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.text('next page'));
}

#### \[h2\]findComponents9+

findComponents(on: On): Promise<Array<Component>>

Searches for all matched components based on the specified attributes and saves them in a list. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Component](#component9)\>> | Promise used to return the list of components. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}

#### \[h2\]findWindow9+

findWindow(filter: WindowFilter): Promise<UiWindow>

Searches for a window based on the specified attributes. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filter | [WindowFilter](#windowfilter9) | Yes | Attributes of the target window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UiWindow](#uiwindow9)\> | Promise used to return the target window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
}

#### \[h2\]waitForComponent9+

waitForComponent(on: On, time: number): Promise<Component>

Searches for the target component based on the attributes within a specified time. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |
| time | number | Yes | Duration for searching for the target component, in ms. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise used to return the component. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
}

#### \[h2\]assertComponentExist9+

assertComponentExist(on: On): Promise<void>

Asserts whether a component matches the specified attributes exists on the current page. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000003 | Assertion failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}

#### \[h2\]pressBack9+

pressBack(): Promise<void>

Presses the Back button. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}

#### \[h2\]pressBack20+

pressBack(displayId: number): Promise<void>

Presses the Back button on the specified screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack(0);
}

#### \[h2\]triggerKey9+

triggerKey(keyCode: number): Promise<void>

Triggers a key event by passing the key value. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyCode | number | Yes | Key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE\_BACK); // Back button
}

#### \[h2\]triggerKey20+

triggerKey(keyCode: number, displayId: number): Promise<void>

Triggers a key event by passing the key value on the specified screen. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyCode | number | Yes | Key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE\_BACK, 0); // Back button
}

#### \[h2\]triggerCombineKeys9+

triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>

Triggers a combination key event based on the specified key values. This API uses a promise to return the result. For example, if the value of **Key** is (2072, 2019), the combination key **Ctrl+C** that matches the value is found and clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key0 | number | Yes | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| key1 | number | Yes | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| key2 | number | No | Third key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035);
}

#### \[h2\]triggerCombineKeys20+

triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>

Triggers a combination key event based on the specified key values on the specified screen. This API uses a promise to return the result. For example, if the value of **Key** is (2072, 2019), the combination key **Ctrl+C** that matches the value is found and clicked.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key0 | number | Yes | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| key1 | number | Yes | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| key2 | number | No | Third key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| displayId | number | No | Display ID. The value is an integer greater than or equal to 0. The default value is the default display ID of the device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}

#### \[h2\]click9+

click(x: number, y: number): Promise<void>

Clicks the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.click(100, 100);
}

#### \[h2\]clickAt20+

clickAt(point: Point): Promise<void>

Clicks the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Point object, which is used to transfer the target point information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.clickAt({ x: 100, y: 100, displayId: 0 });
}

#### \[h2\]doubleClick9+

doubleClick(x: number, y: number): Promise<void>

Double-clicks the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClick(100, 100);
}

#### \[h2\]doubleClickAt20+

doubleClickAt(point: Point): Promise<void>

Double-clicks the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Point object, which is used to transfer the target point information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
}

#### \[h2\]longClick9+

longClick(x: number, y: number): Promise<void>

Long-clicks the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}

#### \[h2\]longClickAt20+

longClickAt(point: Point, duration?: number): Promise<void>

Long-clicks the target coordinate point for a specified duration. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Point object, which is used to transfer the target point information. |
| duration | number | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClickAt({ x: 100, y: 100, displayId: 0 }, 1500);
}

#### \[h2\]swipe9+

swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startx | number | Yes | Number, which indicates the horizontal coordinate of the start point. The value is an integer greater than or equal to 0. |
| starty | number | Yes | Number, which indicates the vertical coordinate of the start point. The value is an integer greater than or equal to 0. |
| endx | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| endy | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipe(100, 100, 200, 200, 600);
}

#### \[h2\]swipeBetween20+

swipeBetween(from: Point, to: Point, speed?: number): Promise<void>

Swipes from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](#point9) | Yes | 
Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs.

**Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, the 17000007 error code is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
}

#### \[h2\]drag9+

drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

Drags from the start coordinate point to the target coordinate point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startx | number | Yes | Number, which indicates the horizontal coordinate of the start point. The value is an integer greater than or equal to 0. |
| starty | number | Yes | Number, which indicates the vertical coordinate of the start point. The value is an integer greater than or equal to 0. |
| endx | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| endy | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.drag(100, 100, 200, 200, 600);
}

#### \[h2\]dragBetween20+

dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

Drags from the start point to the target point. You can specify the drag speed and the click duration before dragging. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](#point9) | Yes | 
Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs.

**Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, the 17000007 error code is returned. |
| duration | number | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
}

#### \[h2\]screenCap9+

screenCap(savePath: string): Promise<boolean>

Captures the current screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) of the current application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the screenshot operation is successful. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}

#### \[h2\]screenCap20+

screenCap(savePath: string, displayId: number): Promise<boolean>

Captures the specified screen and saves it as a PNG image to the given save path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) of the current application. |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the screenshot operation is successful. The value **true** indicates that the screen capture operation is successful, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
}

#### \[h2\]setDisplayRotation9+

setDisplayRotation(rotation: DisplayRotation): Promise<void>

Sets the display rotation of the current scene. This API uses a promise to return the result. It applies to rotatable scenarios.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotation | [DisplayRotation](#displayrotation9) | Yes | Display rotation of the device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, DisplayRotation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotation(DisplayRotation.ROTATION\_180);
}

#### \[h2\]getDisplayRotation9+

getDisplayRotation(): Promise<DisplayRotation>

Obtains the display rotation of the current device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DisplayRotation](#displayrotation9)\> | Promise used to return the display rotation of the current device. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}

#### \[h2\]getDisplayRotation20+

getDisplayRotation(displayId: number): Promise<DisplayRotation>

Obtains the display rotation of the specified device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DisplayRotation](#displayrotation9)\> | Promise used to return the display rotation of the specified device. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation(0);
}

#### \[h2\]setDisplayRotationEnabled9+

setDisplayRotationEnabled(enabled: boolean): Promise<void>

Enables or disables display rotation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether the screen can be rotated. The value **true** indicates that the screen can be rotated, and **false** indicates the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotationEnabled(false);
}

#### \[h2\]getDisplaySize9+

getDisplaySize(): Promise<Point>

Obtains the display size of the current device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise used to return the **Point** object. The size of the current device screen is **Point.x \* Point.y**. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}

#### \[h2\]getDisplaySize20+

getDisplaySize(displayId: number): Promise<Point>

Obtains the size of the specified display on the current device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise used to return the **Point** object. The size of the specified display is **Point.x \* Point.y**. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}

#### \[h2\]getDisplayDensity9+

getDisplayDensity(): Promise<Point>

Obtains the display density of the current device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise used to return the **Point** object. The density of the current device display is **Point.x\*Point.y**. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}

#### \[h2\]getDisplayDensity20+

getDisplayDensity(displayId: number): Promise<Point>

Obtains the density of the specified display of the current device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise used to return the **Point** object. The density of the specified display is **Point.x\*Point.y**. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity(0);
}

#### \[h2\]wakeUpDisplay9+

wakeUpDisplay(): Promise<void>

Wakes up the current display. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}

#### \[h2\]pressHome9+

pressHome(): Promise<void>

Injects an operation of returning to the home screen on the device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}

#### \[h2\]pressHome20+

pressHome(displayId: number): Promise<void>

Injects an operation of returning to the home screen on the specified display. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome(0);
}

#### \[h2\]waitForIdle9+

waitForIdle(idleTime: number, timeout: number): Promise<boolean>

Checks whether all components on the current UI are idle. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| idleTime | number | Yes | Idle time threshold, in ms. If the duration for which a component remains inactive reaches this threshold, it is considered as idle. The value must be an integer greater than or equal to 0. |
| timeout | number | Yes | Maximum waiting time, in milliseconds. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether all components on the current UI are idle. The value true indicates that all components on the current UI are idle, and false indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let idled: boolean = await driver.waitForIdle(4000, 5000);
}

#### \[h2\]fling9+

fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>

Simulates a fling operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Coordinates of the point where the finger touches the screen. |
| to | [Point](#point9) | Yes | Coordinates of the point where the finger leaves the screen. |
| stepLen | number | Yes | Step length, in pixels. The value is an integer greater than or equal to 0. |
| speed | number | Yes | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the range, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}

#### \[h2\]injectMultiPointerAction9+

injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>

Injects a multi-finger operation into a device. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | Yes | Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the operation is successful. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  await driver.injectMultiPointerAction(pointers);
}

#### \[h2\]fling10+

fling(direction: UiDirection, speed: number): Promise<void>

Simulates a fling operation with the specified direction and speed. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | [UiDirection](#uidirection10) | Yes | Direction of the fling operation. |
| speed | number | Yes | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the range, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}

#### \[h2\]fling20+

fling(direction: UiDirection, speed: number, displayId: number): Promise<void>

Simulates a fling operation on a specified display with the specified direction and speed. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | [UiDirection](#uidirection10) | Yes | Direction of the fling operation. |
| speed | number | Yes | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the range, the default value **600** is used. If the value is a negative number, error code 401 is returned. |
| displayId | number | Yes | 
Display ID. The value is an integer greater than or equal to 0.

**Note**: If the input **displayId** does not exist, the exception **17000007** is reported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000, 0);
}

#### \[h2\]screenCapture10+

screenCapture(savePath: string, rect?: Rect): Promise<boolean>

Captures the specified area of the current screen and saves the captured screenshot as a PNG image to the specified path. This API uses a promise to return the result. This API can be used in scenarios where screenshots are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| savePath | string | Yes | File save path. The path must be the [sandbox path](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) of the current application. |
| rect | [Rect](#rect9) | No | Area of the screen to capture. The default value is the entire screen. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the screenshot operation is successful. The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCapture('/data/storage/el2/base/cache/1.png', {
    left: 0,
    top: 0,
    right: 100,
    bottom: 100
  });
}

#### \[h2\]mouseClick10+

mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

Injects a mouse click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the value of **key1** is **2072**, the **Ctrl** button is pressed with the mouse click.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the mouse click. |
| btnId | [MouseButton](#mousebutton10) | Yes | Mouse button pressed. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE\_BUTTON\_LEFT, 2072);
}

#### \[h2\]mouseScroll10+

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the value of **key1** is **2072**, the **Ctrl** button is pressed with mouse scrolling.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the mouse click. |
| down | boolean | Yes | Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls downward, and **false** indicates the mouse wheel scrolls upward. |
| d | number | Yes | Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px shift to the target point. The value is an integer greater than or equal to 0. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}

#### \[h2\]mouseMoveTo10+

mouseMoveTo(p: Point): Promise<void>

Moves the mouse cursor to the target point. This API uses a promise to return the result.

**System capability**: SystemCapability.Test.UiTest

**Atomic service API**: This API can be used in atomic services since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the end point. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveTo({ x: 100, y: 100 });
}

#### \[h2\]createUIEventObserver10+

createUIEventObserver(): UIEventObserver;

Creates a UI event listener.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| [UIEventObserver](#uieventobserver10) | UI event listener. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**Example**

// xxx.test.ets
import { Driver, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
}

#### \[h2\]mouseScroll11+

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>

Injects a mouse scroll action at the specified coordinates, with the optional key or key combination and the specified scroll speed. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the mouse click. |
| down | boolean | Yes | Whether the mouse wheel scrolls downward. The value **true** indicates the mouse wheel scrolls downward, and **false** indicates the mouse wheel scrolls upward. |
| d | number | Yes | Number of ticks scrolled by the mouse wheel. A tick indicates a 120 px shift to the target point. The value is an integer greater than or equal to 0. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| speed | number | No | Scrolling speed of the mouse wheel, in ticks/s. The value is an integer ranging from 1 to 500. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **20** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
}

#### \[h2\]mouseDoubleClick11+

mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

Injects a double-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the value of **key** is **2072**, the **Ctrl** button is pressed with the double-click.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the double-click. |
| btnId | [MouseButton](#mousebutton10) | Yes | Mouse button pressed. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDoubleClick({ x: 248, y: 194 }, MouseButton.MOUSE\_BUTTON\_LEFT, 2072);
}

#### \[h2\]mouseLongClick11+

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination. This API uses a promise to return the result. For example, if the value of **Key** is **2072**, the **Ctrl** button is long-clicked with the mouse device.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the long-click of the mouse device. |
| btnId | [MouseButton](#mousebutton10) | Yes | Mouse button pressed. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE\_BUTTON\_LEFT, 2072);
}

#### \[h2\]mouseLongClick20+

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>

Injects a mouse long-click action at the specified coordinates, with the optional key or key combination and the specified duration. This API uses a promise to return the result. For example, if the value of **Key** is **2072**, the **Ctrl** button is long-clicked with the mouse device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the long-click of the mouse device. |
| btnId | [MouseButton](#mousebutton10) | Yes | Mouse button pressed. |
| key1 | number | No | First key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| key2 | number | No | Second key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). The default value is 0. |
| duration | number | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE\_BUTTON\_LEFT, 2072, 0, 2000);
}

#### \[h2\]mouseMoveWithTrack11+

mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>

Moves the mouse pointer from the start point to the end point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Coordinates of the start point. |
| to | [Point](#point9) | Yes | Coordinates of the end point. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveWithTrack({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}

#### \[h2\]mouseDrag11+

mouseDrag(from: Point, to: Point, speed?: number): Promise<void>

Drags the mouse pointer from the start point to the end point. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Coordinates of the start point. |
| to | [Point](#point9) | Yes | Coordinates of the end point. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}

#### \[h2\]mouseDrag20+

mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

Drags the mouse from the start point to the end point. You can specify the dragging speed and the duration before dragging. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Device behavior difference**: This API takes effect only on phones, tablets, PCs/2-in-1 devices, and TVs.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | Yes | Coordinates of the start point. |
| to | [Point](#point9) | Yes | Coordinates of the end point. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |
| duration | number | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
}

#### \[h2\]inputText11+

inputText(p: Point, text: string): Promise<void>

Inputs text at a specified coordinate without clearing the original text in the component. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the end point. |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123');
}

#### \[h2\]inputText20+

inputText(p: Point, text: string, mode: InputTextMode): Promise<void>

Inputs text at a specified coordinate point in a specified input mode. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | Yes | Coordinates of the end point. |
| text | string | Yes | Input text. Currently, English, Chinese, and special characters are supported. |
| mode | [InputTextMode](#inputtextmode20) | Yes | 
Text input mode. For details, see [InputTextMode](#inputtextmode20).

**NOTE**

If **InputTextMode.addition** is set to **true**, the cursor moves to the end of the text and the specified text is input. If the value is **false**, the specified text is input at the coordinate point.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**Example**

// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123', { paste: true, addition: false });
}

async function demo\_Chinese() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, 'Chinese&', { paste: false, addition: true });
  // Copy and paste Chinese and a special character to the end of the specified text.
}

#### \[h2\]touchPadMultiFingerSwipe18+

touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>

Simulates a multi-finger swipe gesture on the touchpad. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 17000005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fingers | number | Yes | Number of fingers. The value can be 3 or 4. |
| direction | [UiDirection](#uidirection10) | Yes | Swipe direction. |
| options | [TouchPadSwipeOptions](#touchpadswipeoptions18) | No | Additional options for the multi-finger swipe gesture on the touchpad. The default values of the attributes in **TouchPadSwipeOptions** are used by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
}

#### \[h2\]touchPadTwoFingersScroll22+

touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>

Simulates a two-finger scroll gesture on the touchpad. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 17000005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Point of the mouse cursor when the two-finger scrolling is performed on the touchpad. |
| direction | [UiDirection](#uidirection10) | Yes | Direction of two-finger scrolling on the touchpad. |
| d | number | Yes | Number of grids scrolled by two fingers on the touchpad. A grid indicates a 120 px shift to the target point. The value is an integer greater than or equal to 0. |
| speed | number | No | Scrolling speed of two fingers on the touchpad, in ticks/s. The value is an integer ranging from 1 to 500. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **20** is used. If the value is a negative number, the 17000007 error code is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadTwoFingersScroll({ x: 100, y: 100 }, UiDirection.UP, 20, 10);
}

#### \[h2\]penClick18+

penClick(point: Point): Promise<void>

Simulates a pen click operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Coordinates of the clicked point. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penClick({ x: 100, y: 100 });
}

#### \[h2\]penLongClick18+

penLongClick(point: Point, pressure?: number): Promise<void>

Simulates a pen long-click operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Coordinates of the long-clicked point. |
| pressure | number | No | Swipe pressure of the pen. The value ranges from 0.0 to 1.0. The default value is **1.0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penLongClick({ x: 100, y: 100 }, 0.5);
}

#### \[h2\]penDoubleClick18+

penDoubleClick(point: Point): Promise<void>

Simulates a pen double-click operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | Yes | Coordinates of the double-clicked point. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penDoubleClick({ x: 100, y: 100 });
}

#### \[h2\]penSwipe18+

penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>

Simulates a pen swipe operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startPoint | [Point](#point9) | Yes | Coordinates of the start point. |
| endPoint | [Point](#point9) | Yes | Coordinates of the end point. |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |
| pressure | number | No | Swipe pressure of the pen. The value ranges from 0.0 to 1.0. The default value is **1.0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
}

#### \[h2\]injectPenPointerAction18+

injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>

Simulates a continuous multi-point pen injection operation. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | Yes | 
Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory.

**Note**: Currently, only the single-finger operation is supported. The value of **fingers** in **PointerMatrix** must be set to **1**.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, error code 401 is returned. |
| pressure | number | No | Injection pressure. The value ranges from 0.0 to 1.0. The default value is **1.0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointer = PointerMatrix.create(1, 8);
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 \* step });
  }
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}

#### \[h2\]crownRotate20+

crownRotate(d: number, speed?: number): Promise<void>

Injects a crown rotation event. You can specify the rotation speed. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called on wearables. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| d | number | Yes | Number of rotation ticks. A positive value indicates rotation, and a negative value indicates counterclockwise rotation. The value must be an integer. |
| speed | number | No | 
Rotation speed, in ticks/s. The value is an integer ranging from 1 to 500. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **20** is used. If the value is a negative number, the 17000007 error code is returned.

**Note**: If the set value is not in the range, the default value 20 is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**Example**

// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Rotate 50 ticks clockwise at a speed of 30 ticks per second.
  await driver.crownRotate(50, 30);
  // Rotate 20 ticks counterclockwise at a speed of 30 ticks per second.
  await driver.crownRotate(-20, 30);
}

#### \[h2\]knuckleKnock22+

knuckleKnock(pointers: Array<Point>, times: number): Promise<void>

Simulates a knuckle knock on the display. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/i0U1u_o4RQSItoX8rfXGiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7DE78AA874593A7821B55AF86C1513FCD211FCF0ACABB30A79418B2895C5A12)

If the knuckle gesture is disabled on the device, 17000005 is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called on phones and tablets that support knuckle operations. On other devices, the error code 17000005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pointers | Array<[Point](#point9)\> | Yes | Array of knuckle knock coordinates on the display. The array length can be 1 or 2. |
| times | number | Yes | Number of consecutive knocks on the display. The value can be 1 or 2. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, Point } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Simulate a single-knuckle double-knock gesture.
  let points: Array<Point> = \[{ x: 100, y: 100 }\];
  await driver.knuckleKnock(points, 2);
}

#### \[h2\]injectKnucklePointerAction22+

injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>

Simulates a multi-point knuckle scrolling operation. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/Psa2TttsTp-MrIjhejCDrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C5CB08CC4B143399A7BEF4C0CD29813934DFE2BD124C195D093A5C8D27FB8EA)

If the knuckle gesture is disabled on the device, 17000005 is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called on phones and tablets that support knuckle operations. On other devices, the error code 17000005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | Yes | 
Scroll trajectory, including the number of fingers and an array of coordinates along the trajectory.

**Note**: Currently, only the single-finger operation is supported. The value of **fingers** in **PointerMatrix** must be set to **1**.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, the 17000007 error code is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // Simulate a knuckle gesture to draw an S on the display.
  let pointers: PointerMatrix = PointerMatrix.create(1, 6);
  pointers.setPoint(0, 0, { x: 750, y: 300 });
  pointers.setPoint(0, 1, { x: 500, y: 100 });
  pointers.setPoint(0, 2, { x: 250, y: 300 });
  pointers.setPoint(0, 3, { x: 750, y: 800 });
  pointers.setPoint(0, 4, { x: 500, y: 1000 });
  pointers.setPoint(0, 5, { x: 250, y: 800 });
  await driver.injectKnucklePointerAction(pointers);
}

#### \[h2\]isComponentPresentWhenLongClick22+

isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>

Long-clicks at the specified coordinates and checks whether the target component exists. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |
| point | [Point](#point9) | Yes | Coordinates of the long-clicked point. |
| duration | number | No | Long-click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the target component exists during a long-click operation. The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
}

#### \[h2\]isComponentPresentWhenDrag22+

isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>

Drags from the start point to the end point and checks whether the target component exists. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |
| from | [Point](#point9) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](#point9) | Yes | 
Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs.

**Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, the 17000007 error code is returned. |
| duration | number | No | Click duration, in ms. The value is an integer greater than or equal to 1500. The default value is 1500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the target component exists during the dragging operation. The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
}

#### \[h2\]isComponentPresentWhenSwipe22+

isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>

Swipes from the start point to the end point and checks whether the target component exists. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | Yes | Attributes of the target component. |
| from | [Point](#point9) | Yes | Point object, which transfers the coordinates of the start point and the ID of the display to which the start point belongs. |
| to | [Point](#point9) | Yes | 
Point object, which transfers the coordinates of the target point and the ID of the display to which it belongs.

**Note**: The target point and the start point must be on the same screen. Otherwise, the **17000007** exception is thrown.

 |
| speed | number | No | Swipe speed, in px/s. The value is an integer ranging from 200 to 40000. The default value is **600**. If the value is a non-negative number that is not within the specified range or is **null** or **undefined**, the default value **600** is used. If the value is a negative number, the 17000007 error code is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the target component exists during the swiping operation. The value **true** indicates that the target component exists, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
}

#### PointerMatrix9+

Implements a **PointerMatrix** object that stores coordinates and behaviors of each action of each finger in a multi-touch operation.

#### \[h2\]create9+

static create(fingers: number, steps: number): PointerMatrix

Creates a **PointerMatrix** object and returns the object created. This API is a static API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fingers | number | Yes | Number of fingers injected during the multi-finger operation. The value is an integer ranging from 1 to 10. |
| steps | number | Yes | Number of steps performed by a finger. The value is an integer ranging from 1 to 1000. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PointerMatrix](#pointermatrix9) | **PointerMatrix** object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
}

#### \[h2\]setPoint9+

setPoint(finger: number, step: number, point: Point): void

Sets the coordinates for the action corresponding to the specified finger and step in the **PointerMatrix** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| finger | number | Yes | Number of fingers. The value is an integer greater than or equal to 0 and cannot exceed the number of fingers set when the **PointerMatrix** object is constructed. |
| step | number | Yes | Number of steps. The value is an integer greater than or equal to 0 and cannot exceed the number of steps set when the **PointerMatrix** object is constructed. |
| point | [Point](#point9) | Yes | Coordinates of the action. It is recommended that the distance between adjacent coordinates be within the range of 10 px to 80 px. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
}

#### UiWindow9+

The **UiWindow** class represents a window on the UI and provides APIs for obtaining window attributes, dragging a window, and adjusting the window size.

All APIs provided in this class use a promise to return the result and must be invoked using **await**.

#### \[h2\]getBundleName9+

getBundleName(): Promise<string>

Obtains the bundle name of the application to which a window belongs. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the bundle name of the application to which the window belongs. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let name: string = await window.getBundleName();
}

#### \[h2\]getBounds9+

getBounds(): Promise<Rect>

Obtains the bounds information of a window. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Rect](#rect9)\> | Promise used to return the window border information. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let rect = await window.getBounds();
}

#### \[h2\]getTitle9+

getTitle(): Promise<string>

Obtains the window title. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the window title. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let title = await window.getTitle();
}

#### \[h2\]getWindowMode9+

getWindowMode(): Promise<WindowMode>

Obtains the window mode. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WindowMode](#windowmode9)\> | Promise used to return the window mode information. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let mode = await window.getWindowMode();
}

#### \[h2\]isFocused9+

isFocused(): Promise<boolean>

Checks whether a window is focused. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the window is focused. The value **true** indicates that the component is focused, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isFocused();
}

#### \[h2\]isActived(deprecated)

isActived(): Promise<boolean>

Checks whether a window is active. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/u5X8DZtqQ--lena6TKCbhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B817CAD8C6EC26B92F006553845086305ADC3817E514E1F86FEB9DFDCA4F8BBB)

This API is supported since API version 9 and deprecated since API version 11. You are advised to use [isActive11+](#isactive11) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the window is active. The value **true** indicates that the window is active, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isActived();
}

#### \[h2\]focus9+

focus(): Promise<void>

Focuses a window. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.focus();
}

#### \[h2\]moveTo9+

moveTo(x: number, y: number): Promise<void>

Moves a window to the target point. This API uses a promise to return the result. This API is applicable to moveable windows.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.moveTo(100, 100);
}

#### \[h2\]resize9+

resize(wide: number, height: number, direction: ResizeDirection): Promise<void>

Resizes a window based on the specified width, height, and direction. This API uses a promise to return the result. This API is applicable to resizable windows.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wide | number | Yes | Width of the adjusted window, in number format. The value is an integer greater than or equal to 0. |
| height | number | Yes | Height of the adjusted window, in number format. The value is an integer greater than or equal to 0. |
| direction | [ResizeDirection](#resizedirection9) | Yes | Resize direction. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, ResizeDirection, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resize(100, 100, ResizeDirection.LEFT);
}

#### \[h2\]split9+

split(): Promise<void>

Switches to the split-screen mode. This API uses a promise to return the result. This API is applicable to windows that support screen splitting.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.split();
}

#### \[h2\]maximize9+

maximize(): Promise<void>

Maximizes a window. This API uses a promise to return the result. This API is applicable to windows that can be maximized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.maximize();
}

#### \[h2\]minimize9+

minimize(): Promise<void>

Minimizes a window. This API uses a promise to return the result. This API is applicable to windows that can be minimized.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.minimize();
}

#### \[h2\]resume9+

resume(): Promise<void>

Resumes a window to its previous mode. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resume();
}

#### \[h2\]close9+

close(): Promise<void>

Closes a window. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices and tablets. If it is called on other device types, error code 17000005 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.close();
}

#### \[h2\]isActive11+

isActive(): Promise<boolean>

Checks whether a window is active. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the window is active. The value **true** indicates that the window is active, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isActive();
}

#### \[h2\]getDisplayId20+

getDisplayId(): Promise<number>

Obtains the ID of the display to which a window belongs. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the ID of the display to which the window belongs. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**Example**

// xxx.test.ets
import { UiWindow, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let id = await window.getDisplayId();
}

#### UIEventObserver10+

UI event listener.

#### \[h2\]once('toastShow')10+

once(type: 'toastShow', callback: Callback<UIElementInfo>): void

Subscribes to events of the toast component. This API uses a callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'toastShow'**. |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('toastShow', callback);
}

#### \[h2\]once('dialogShow')10+

once(type: 'dialogShow', callback: Callback<UIElementInfo>): void

Subscribes to events of the dialog component. This API uses a callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'dialogShow'**. |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('dialogShow', callback);
}

#### \[h2\]once('windowChange')22+

once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void

Starts listening for window change events of the specified type with extended configuration supported. This API triggers a callback when a specified window change event is detected. This API can be used only in [free windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#free-windows) mode.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to subscribe to, which can be **windowChange**. This event is triggered when the window changes. |
| windowChangeType | [WindowChangeType](#windowchangetype22) | Yes | Type of the window change event. |
| options | [WindowChangeOptions](#windowchangeoptions22) | Yes | Extended configuration, including the listening timeout interval and the bundle name of the window to be listened for. |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | Yes | Callback triggered to return event information when an event occurs. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let options: WindowChangeOptions = {
    timeout: 20000,
    bundleName: 'com.example.myapplication'  // Use the actual bundle name.
  }
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.windowChangeType?.toString());
    console.info(UIElementInfo.windowId?.toString());
  }
  observer.once('windowChange', WindowChangeType.WINDOW\_ADDED, options, callback);
}

#### \[h2\]once('componentEventOccur')22+

once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void

Starts listening for component operation events of the specified type with extended configuration supported. This API triggers a callback when a specified component operation event is detected.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to subscribe to, which can be **componentEventOccur**. This event is triggered when the component operation is detected. |
| componentEventType | [ComponentEventType](#componenteventtype22) | Yes | Type of the component operation event. |
| options | [ComponentEventOptions](#componenteventoptions22) | Yes | Extended configuration, including the listening timeout interval and the matching condition of the component to be listened for. |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**Example**

// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let option: ComponentEventOptions = {
    timeout: 20000,
    on: ON.id('123')  // Use the actual component ID.
  };
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.componentEventType?.toString());
    console.info(UIElementInfo.windowId?.toString());
    console.info(UIElementInfo.componentId);
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
  };
  observer.once('componentEventOccur', ComponentEventType.COMPONENT\_CLICKED, option, callback);
}

#### By(deprecated)

The UiTest framework provides a wide range of UI component feature description APIs in the **By** class to filter and match components.

The APIs provided by the **By** class exhibit the following features:

1\. Allow one or more attributes as the match conditions. For example, you can specify both the **text** and **id** attributes to find the target component.

2\. Provide multiple match patterns for component attributes.

3\. Support absolute positioning and relative positioning for components. APIs such as [By.isBefore(deprecated)](#isbeforedeprecated) and [By.isAfter(deprecated)](#isafterdeprecated) can be used to specify the features of adjacent components to assist positioning.

All APIs provided in the **By** class are synchronous. You are advised to use the static constructor **BY** to create a **By** object in chain mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/WaDN5hmcSw23GzetgsNbxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B157C52D338D999F8C28FA8B20A10FCE197C9E696E6EB313CBB9D3AB770F282D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [On9+](#on9) instead.

// xxx.test.ets
import { BY } from '@kit.TestKit';

BY.text('123').type('Button');

#### \[h2\]text(deprecated)

text(txt: string, pattern?: MatchPattern): By

Specifies the text attribute of the target component. Multiple match patterns are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/2actgAIVQ3SoP8PfWhXYyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDCB11375287FCC94BD88CC6393049DE6FFC90757D785D4BD8AC2BAE42A26B27)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [text9+](#text9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| txt | string | Yes | Component text, used to match the target component. |
| pattern | [MatchPattern](#matchpattern) | No | Match pattern. The default value is [EQUALS](#matchpattern). |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the text attribute of the target component. |

**Example**

// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // Use the static constructor BY to create a By object and specify the text attribute of the target component.

#### \[h2\]key(deprecated)

key(key: string): By

Specifies the key attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/XzarX_ofTxK-VwLnD_OKpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FC98CF290DDF65DCC55324C7136EA8C027425A7675F971A9F5DE5332F28C890)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [id9+](#id9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | string | Yes | Component key. |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the key attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.key('123'); // Use the static constructor BY to create a By object and specify the key attribute of the target component.

#### \[h2\]id(deprecated)

id(id: number): By

Specifies the ID attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/on54DXG6Su6RyN74TF0ArQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5323770E50934D93F4C6147681A7FCC2B004DEB52C5823574FA3D0EDCD84D689)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [id9+](#id9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Component ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the ID attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.id(123); // Use the static constructor BY to create a By object and specify the id attribute of the target component.

#### \[h2\]type(deprecated)

type(tp: string): By

Specifies the type attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LsxBRyAURh2B_l2fkAPimw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ED364C184A99CE4BD128D6524663554626AC13C50E324228703D2D100C91984)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [type9+](#type9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tp | string | Yes | Component type. |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the type attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // Use the static constructor BY to create a By object and specify the type attribute of the target component.

#### \[h2\]clickable(deprecated)

clickable(b?: boolean): By

Specifies the clickable attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-e-t3lsNQe68T-7Q73GDQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C89E40D2C825D2A330F601A50FB88C424564F5B253A7B3D44FAA929C9DC08A8B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [clickable9+](#clickable9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Clickable status of the component. The value **true** indicates that the component is clickable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the clickable attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.clickable(true); // Use the static constructor BY to create a By object and specify the clickable attribute of the target component.

#### \[h2\]scrollable(deprecated)

scrollable(b?: boolean): By

Specifies the scrollable attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/xfZ0vSh-SBSj14dlwS4viA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D12829C4C8C104A0C55CED2BF39FE431D202668ACEA0BAE4A1EB77E995DFA3ED)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [scrollable9+](#scrollable9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Scrollable status of the component. The value **true** indicates that the component is scrollable, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the scrollable attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.scrollable(true); // Use the static constructor BY to create a By object and specify the scrollable attribute of the target component.

#### \[h2\]enabled(deprecated)

enabled(b?: boolean): By

Specifies the enabled attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/DBoHHaHyQFKhoP1yD6AGDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C02BA07D842A2CCE8DD4CD9E6CEED6B001E7F9AE26174B634A088E81FE00F050)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [enabled9+](#enabled9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Enabled status of the component. The value **true** indicates that the component is enabled, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the enabled attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.enabled(true); // Use the static constructor BY to create a By object and specify the enabled attribute of the target component.

#### \[h2\]focused(deprecated)

focused(b?: boolean): By

Specifies the focused attribute of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/c2fVghyoSVysEeI1eSFG0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=827249EB6AFDA98E9B3EEB3AE00ABDD17BA6C0130CF327FAD9E55F5486AFED17)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [focused9+](#focused9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Focused status of the component. The value **true** indicates that the component is focused, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the focused attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.focused(true); // Use the static constructor BY to create a By object and specify the focused attribute of the target component.

#### \[h2\]selected(deprecated)

selected(b?: boolean): By

Specifies the selected status of the target component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/fxeD9faPT8CMDbfWsI42xQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A315C915807A9F6D5EE782BFE31647DC7BFB3BCC19FADF2708A0F2F86B6DFC6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [selected9+](#selected9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| b | boolean | No | Selected status of the component. The value **true** indicates that the component is selected, and **false** indicates the opposite. Default value: **true** |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object that matches the selected attribute of the target component. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.selected(true); // Use the static constructor BY to create a By object and specify the selected attribute of the target component.

#### \[h2\]isBefore(deprecated)

isBefore(by: By): By

Specifies that the target component is located before the given attribute component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/pgJHOT3yQfSf6DxjaTVh5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03AB0643122F7FBD83C421D487C1CCAC33D795F91C29B49FE039EBEC9AC49E77)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isBefore9+](#isbefore9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Information about the attribute component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// Use the static constructor BY to create a by object and specify that the target component is located before the given attribute component.
let by: By = BY.type('Button').isBefore(BY.text('123')); // Search for the first Button component located before the component whose text is 123.

#### \[h2\]isAfter(deprecated)

isAfter(by: By): By

Specifies that the target component is located after the given attribute component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/aFhNOCR1TaWpTWQodxbPNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDD250545C4A418BB1EBE0A26374BC8B6F901D1DAE7F5DB3D0A9E05976D3486E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isAfter9+](#isafter9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Information about the attribute component. |

**Return value**

| Type | Description |
| :-- | :-- |
| [By](#bydeprecated) | **By** object. |

**Example**

// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// Use the static constructor BY to create a by object and specify that the target component is located after the given attribute component.
let by: By = BY.type('Text').isAfter(BY.text('123')); // Search for the first Text component located after the component whose text is 123.

#### UiComponent(deprecated)

In **UiTest**, the **UiComponent** class represents a component on the UI and provides APIs for obtaining component attributes, clicking a component, scrolling to search for a component, and text injection.

All APIs provided in this class use a promise to return the result and must be invoked using **await**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/OxocPztXR_uVqz5e8YAAzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A0029D09A510F48D71683397BB7BE1C4F00AF374A30419D83756EFE06BED0A1)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Component9+](#component9) instead.

#### \[h2\]click(deprecated)

click(): Promise<void>

Clicks this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/46TwQet8Qp2dV6zI5_nQ7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ED588689C42470DB673EDFC59043E732639A5134F934B5901A724922D4C266A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [click9+](#click9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver, BY, Driver, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.click();
}

#### \[h2\]doubleClick(deprecated)

doubleClick(): Promise<void>

Double-clicks this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/jEKtekWqTMOUUOT08GbyYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1B478E5788E121CD785EC830D8CE1A93C63901C0A59DB4C495B32C726DE2301)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [doubleClick9+](#doubleclick9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.doubleClick();
}

#### \[h2\]longClick(deprecated)

longClick(): Promise<void>

Long-clicks this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/kKI-yNyBTMe6Pqp2Kwyl9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED2B88FE79BC2127B15347664DCFB05148FFA09A53A75F389BB8F49888CDD1DD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [longClick9+](#longclick9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.longClick();
}

#### \[h2\]getId(deprecated)

getId(): Promise<number>

Obtains the ID of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/I4I-xFFhRJ2dMT5J8D1gpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A52EE754A1735EE8BA6B744A9DC15DCF831672F888D0E9897EB23F7EA3F035F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getId9+](#getid9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the component ID. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let id = await button.getId();
}

#### \[h2\]getKey(deprecated)

getKey(): Promise<string>

Obtains the key of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/pHQNnXaZQ8ajtLAfANscCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1158BD6ACE46F39F234ED6CCA691AEBCC54C63DFE85660B116F6B3F96BB13F4C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getId9+](#getid9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the key value. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let str\_key = await button.getKey();
}

#### \[h2\]getText(deprecated)

getText(): Promise<string>

Obtains the text information of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/fQyIOPSYTHOBdda13nGXJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A02E86EB3B5E2BBA8953CB068A9E2493CFA4DA509C31B18A77F26C88EFB1A7B3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getText9+](#gettext9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the text information of the component. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let text = await button.getText();
}

#### \[h2\]getType(deprecated)

getType(): Promise<string>

Obtains the type of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/UNdXmO5yQ8KQ0uyXnnhIZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3255DD6C00C925B64F6E3D9B1725A88E9524BCD09F747B88B0E6D6557C90551)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getType9+](#gettype9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the component type. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let type = await button.getType();
}

#### \[h2\]isClickable(deprecated)

isClickable(): Promise<boolean>

Obtains the clickable status of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/sNlYVia5Syy8G4CGvOEOWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95DD8C9870CEBACB59B80D11A40F441755543EECC7A6CD1CE23FDFC5A0A03445)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isClickable9+](#isclickable9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is clickable. The value **true** indicates that the component is clickable, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}

#### \[h2\]isScrollable(deprecated)

isScrollable(): Promise<boolean>

Obtains the scrollable status of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ewNZyM-8RA6SpgH2jM3BFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=643F0C6FC34B40C51DF3FEBF9D2D451A1D1D3ACCC4A55ACBFD7ABC82F55CCF7D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isScrollable9+](#isscrollable9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is scrollable. The value **true** indicates that the component is scrollable, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}

#### \[h2\]isEnabled(deprecated)

isEnabled(): Promise<boolean>

Obtains the enabled status of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/IakM28pqSMmcHZ8ld4RsZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44D5E93BA6944F8E928D025C694E7DC5EE6BE375D84CCA1F4A828C86B31EE936)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isEnabled9+](#isenabled9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is enabled. The value **true** indicates that the component is enabled, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}

#### \[h2\]isFocused(deprecated)

isFocused(): Promise<boolean>

Obtains the focused status of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/297qaZ4gQkqNyvsukPZrQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF0A08152ECF14F13A7422E486D7C2C2FFA1243C22780F330CB69FD4FACC18A6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isFocused9+](#isfocused9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is focused. The value **true** indicates that the component is focused, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}

#### \[h2\]isSelected(deprecated)

isSelected(): Promise<boolean>

Obtains the selected status of this component. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/MpuGjuiWRmal41VkyO7E4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B807F3A20B6F8A328D21C4184770E7815F43D11E84E2B34D27C96FE51BC2DF32)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [isSelected9+](#isselected9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the component is selected. The value **true** indicates that the component is selected, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}

#### \[h2\]inputText(deprecated)

inputText(text: string): Promise<void>

Inputs text to a component. This API takes effect only for editable text components. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/O0dORKOGT2-p1PQLP3Gf9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC0D50EDB4C9777162A8557F71CEB4A73070D78FE6C78C7ACCDB77EDF20F294A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [inputText9+](#inputtext9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to enter. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let text: UiComponent = await driver.findComponent(BY.text('hello world'));
  await text.inputText('123');
}

#### \[h2\]scrollSearch(deprecated)

scrollSearch(by: By): Promise<UiComponent>

Scrolls on this component to search for the target component (applicable to components that support scrolling, such as **List**). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/xRDImbcMRiSyOoBQQkoEJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6C12AA06509D3C7D7CCC2CD4E2EACB1D235C021D71855BF68B4B0968DA55C5E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [scrollSearch9+](#scrollsearch9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UiComponent](#uicomponentdeprecated)\> | Promise used to return the target component. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
  let button = await scrollBar.scrollSearch(BY.text('next page'));
}

#### UiDriver(deprecated)

The **UiDriver** class is the main entry to the UiTest framework. It provides APIs for features such as component matching/search, key injection, coordinate clicking/sliding, and screenshot.

All APIs provided by this class, except **UiDriver.create()**, use a promise to return the result and must be invoked using **await**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/wNmsSZMWSGKeiW1Wy_Be7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FABB6B684D426C2ABEC685EE7DFE718FBB32E34EF85AF617029B524A943D004B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [Driver9+](#driver9) instead.

#### \[h2\]create(deprecated)

static create(): UiDriver

Creates a **UiDriver** object and returns the object created. This API is a static API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/EEm2qfDHSG6XzuODCixFEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C4DE5FDB81B99364288A24E0103CF7B2213FF87194CCF992995A5D13AF0FC7)

This method is supported since API version 8 and deprecated since API version 9. You are advised to use [create9+](#create9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| UiDriver | **UiDriver** object created. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}

#### \[h2\]delayMs(deprecated)

delayMs(duration: number): Promise<void>

Delays this **UiDriver** object within the specified duration. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/70U-7336TNCtc9S_pfjkMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=751694382063C510FD4DB795D8C97A7D35EB463CDF2A528079912C6E73AFE981)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [delayMs9+](#delayms9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| duration | number | Yes | Duration of time. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.delayMs(1000);
}

#### \[h2\]findComponent(deprecated)

findComponent(by: By): Promise<UiComponent>

Searches this **UiDriver** object for the target component that matches the given attributes. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2F9FlFmpT62cG93VF7sdDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D3C90C7777F6F42FF692661B8E49310710F4B5642F005041D3C3EF76CB1E4A5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [findComponent9+](#findcomponent9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[UiComponent](#uicomponentdeprecated)\> | Promise used to return the component. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}

#### \[h2\]findComponents(deprecated)

findComponents(by: By): Promise<Array<UiComponent>>

Searches this **UiDriver** object for all components that match the given attributes. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ywZUCFxDT6Wq-SDyRJZtFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FDF5F3564DD14525CC94BDB01E49054598633FBF5759808D49C8E64B46A4EDE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [findComponents9+](#findcomponents9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[UiComponent](#uicomponentdeprecated)\>> | Promise used to return the list of components. |

**Example**

// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}

#### \[h2\]assertComponentExist(deprecated)

assertComponentExist(by: By): Promise<void>

Asserts that a component that matches the given attributes exists on the current page. If the component does not exist, the API throws a JS exception, causing the current test case to fail. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/WSqpfCwJTwW5HFdvmkd9uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F25A72E0265032DF0D4CE7041D025539C84E5C4833D1EF09A7D6F08780AE69EF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [assertComponentExist9+](#assertcomponentexist9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | Yes | Attributes of the target component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [UiTest Error Codes](../../error-codes/uitest-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | if the input parameters are invalid. |
| 17000002 | if the async function was not called with await. |
| 17000003 | if the assertion failed. |

**Example**

// xxx.test.ets
import { UiDriver, BY } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.assertComponentExist(BY.text('next page'));
}

#### \[h2\]pressBack(deprecated)

pressBack(): Promise<void>

Presses the Back button on this **UiDriver** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/oaCrFUALRMCoLo7bDsTxMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F46EAB2D9B6CC91662493E2C8A1532F7A4FA897D5B318F6429ABBEC687F16AD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [pressBack9+](#pressback9) instead.

**System capability**: SystemCapability.Test.UiTest

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}

#### \[h2\]triggerKey(deprecated)

triggerKey(keyCode: number): Promise<void>

Triggers the key of this **UiDriver** object that matches the given key code. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/PMs2kbzBQOmwvtjGr4Q-RA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15DFBEBFDD865F73F56426E6B36924A1F4764DFE79BE2A123768C670C9B77FBB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [triggerKey9+](#triggerkey9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyCode | number | Yes | Key value. The value is an integer greater than or equal to 0. For details, see [KeyCode](../../../../basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { Driver, UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE\_BACK); // Back button
}

#### \[h2\]click(deprecated)

click(x: number, y: number): Promise<void>

Clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/fzvrXpouQOeYqzrpwf34fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C534578EE56B41A6BB485820EC6B44527FE3E331B47596E05A2726E3AAA7EF8C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [click9+](#click9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}

#### \[h2\]doubleClick(deprecated)

doubleClick(x: number, y: number): Promise<void>

Double-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/4WljHQluTge4CWlo7pi8zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AA5B403B7766F506B837EB374284B1E0D6648C5B3A200E318D389FF3004D28F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [doubleClick9+](#doubleclick9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}

#### \[h2\]longClick(deprecated)

longClick(x: number, y: number): Promise<void>

Long-clicks a specific point of this **UiDriver** object based on the given coordinates. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/z79di9mhSjiVnZz7N4xTRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADFA0BB6078892DD9F485594D191F04D0D63478B6A512CE444A17A03E3F20C54)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [longClick9+](#longclick9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| y | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
}

#### \[h2\]swipe(deprecated)

swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>

Swipes on this **UiDriver** object from the start point to the end point based on the given coordinates. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/bBAb_gjxQBq_UoKXpP0PMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90D25D7DB1E2C456075FC9AE0018C28CCF9A991FD10A3D3140954968D2B85369)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [swipe9+](#swipe9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startx | number | Yes | Number, which indicates the horizontal coordinate of the start point. The value is an integer greater than or equal to 0. |
| starty | number | Yes | Number, which indicates the vertical coordinate of the start point. The value is an integer greater than or equal to 0. |
| endx | number | Yes | Number, which indicates the horizontal coordinate of the target point. The value is an integer greater than or equal to 0. |
| endy | number | Yes | Number, which indicates the vertical coordinate of the target point. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}

#### \[h2\]screenCap(deprecated)

screenCap(savePath: string): Promise<boolean>

Captures the current screen of this **UiDriver** object and saves it as a PNG image to the given save path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/uPb4n-baRLuzxj2BGN92PA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93A943089B1C7F0F9231A68943F46D8F6600D2246AA27E113ED2D84D0CF7C068)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [screenCap9+](#screencap9) instead.

**System capability**: SystemCapability.Test.UiTest

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| savePath | string | Yes | File save path. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the screenshot operation is successful. The value **true** indicates the screenshot operation is successful, and **false** indicates the opposite. |

**Example**

// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
