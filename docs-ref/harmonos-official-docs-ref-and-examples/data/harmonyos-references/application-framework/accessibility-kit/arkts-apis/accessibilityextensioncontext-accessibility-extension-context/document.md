# AccessibilityExtensionContext (Accessibility Extension Context)

The **AccessibilityExtensionContext** module, inherited from **ExtensionContext**, provides context for **AccessibilityExtensionAbility**.

You can use the APIs of this module to configure the concerned information, obtain root information, and inject gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/dERDF7PNQneWJJQBf4Q-tQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=571132DA732E453B150ED558AA2A6AE8F02189636D9DC77478CCE7273391D52D)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Usage

Before using the **AccessibilityExtensionContext** module, you must define a child class that inherits from **AccessibilityExtensionAbility**.

import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class EntryAbility extends AccessibilityExtensionAbility {
  onConnect(): void {
    let axContext = this.context;
  }
}

#### ElementAttributeValues

Provides attribute names and value types of a node element.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| accessibilityFocused | boolean | No | No | 
Whether the element is focused for accessibility purposes. The value **true** indicates that the element is focused, and **false** indicates the opposite.

Default value: **false**.

 |
| accessibilityText12+ | string | No | No | Accessibility text information of an element. |
| bundleName | string | No | No | Bundle name. |
| checkable | boolean | No | No | 

Whether the element is checkable. The value **true** indicates that the element is checkable, and **false** indicates the opposite.

Default value: **false**.

 |
| checked | boolean | No | No | 

Whether the element is checked. The value **true** indicates that the element is checked, and **false** indicates the opposite.

Default value: **false**.

 |
| children | Array<[AccessibilityElement](#accessibilityelement)\> | No | No | All child elements. |
| clickable | boolean | No | No | 

Whether the element is clickable. The value **true** indicates that the element is clickable, and **false** indicates the opposite.

Default value: **false**.

 |
| componentId | number | No | No | 

ID of the component to which the element belongs.

Default value: **\-1**.

 |
| componentType | string | No | No | Type of the component to which the element belongs, for example, **Button** for the button component and **Image** for the image component. |
| contents | Array<string> | No | No | List of contents. Set this parameter based on site requirements. No special restrictions. |
| currentIndex | number | No | No | 

Index of the current item.

Default value: **0**.

 |
| description | string | No | No | Description of the element. Set this parameter based on site requirements. No special restrictions. |
| editable | boolean | No | No | 

Whether the element is editable. The value **true** indicates that the element is editable, and **false** indicates the opposite.

Default value: **false**.

 |
| endIndex | number | No | No | 

Index of the last list item displayed on the screen.

Default value: **0**.

 |
| error | string | No | No | Error status. |
| focusable | boolean | No | No | 

Whether the element is focusable. The value **true** indicates that the element is focusable, and **false** indicates the opposite.

Default value: **false**.

 |
| hintText | string | No | No | Hint text. |
| inputType | number | No | No | 

Type of the input text.

Default value: **0**.

 |
| inspectorKey | string | No | No | Inspector key. |
| isActive | boolean | No | No | 

Whether the element is active. The value **true** indicates that the element is active and **false** indicates the opposite.

Default value: **true**.

 |
| isEnable | boolean | No | No | 

Whether the element is enabled. The value **true** indicates that the element is enabled, and **false** indicates the opposite.

Default value: **false**.

 |
| isHint | boolean | No | No | 

Whether the element is a hint. The value **true** indicates that the element is a hint, and **false** indicates the opposite.

Default value: **false**.

 |
| isFocused | boolean | No | No | 

Whether the element is focused. The value **true** indicates that the element is focused, and **false** indicates the opposite.

Default value: **false**.

 |
| isPassword | boolean | No | No | 

Whether the element is a password. The value **true** indicates that the element is a password, and **false** indicates the opposite.

Default value: **false**.

 |
| isVisible | boolean | No | No | 

Whether the element is visible. The value **true** indicates that the element is visible, and **false** indicates the opposite.

Default value: **false**.

 |
| itemCount | number | No | No | 

Total number of items.

Default value: **0**.

 |
| lastContent | string | No | No | Last content. |
| layer | number | No | No | Display layer of the element. |
| longClickable | boolean | No | No | 

Whether the element is long-clickable. The value **true** indicates that the element is long-clickable, and **false** indicates the opposite.

Default value: **false**.

 |
| pageId | number | No | No | 

Page ID.

Default value: **\-1**.

 |
| parent | [AccessibilityElement](#accessibilityelement) | No | No | Parent element of the element. |
| pluralLineSupported | boolean | No | No | 

Whether the element supports multiple lines of text. The value **true** indicates that the element supports multiple lines of text, and **false** indicates the opposite.

Default value: **false**.

 |
| rect | [Rect](#rect) | No | No | Area of the element. |
| resourceName | string | No | No | Resource name of the element. |
| rootElement | [AccessibilityElement](#accessibilityelement) | No | No | Root element of the window element. |
| screenRect | [Rect](#rect) | No | No | Display area of the element. |
| scrollable | boolean | No | No | 

Whether the element is scrollable. The value **true** indicates that the element is scrollable, and **false** indicates the opposite.

Default value: **false**.

 |
| selected | boolean | No | No | 

Whether the element is selected. The value **true** indicates that the element is selected, and **false** indicates the opposite.

Default value: **false**.

 |
| startIndex | number | No | No | 

Index of the first list item on the screen.

Default value: **0**.

 |
| text | string | No | No | Text of the element. |
| textLengthLimit | number | No | No | Maximum text length of the element. |
| textMoveUnit | [accessibility.TextMoveUnit](../ohos-accessibility-accessibility/document.md#textmoveunit) | No | No | Unit of movement when the text is read. |
| triggerAction | [accessibility.Action](../ohos-accessibility-accessibility/document.md#action) | No | No | Action that triggers the element event. |
| type | [WindowType](#windowtype) | No | No | Window type of the element. |
| valueMax | number | No | No | 

Maximum value.

Default value: **0**.

 |
| valueMin | number | No | No | 

Minimum value.

Default value: **0**.

 |
| valueNow | number | No | No | 

Current value.

Default value: **0**.

 |
| windowId | number | No | No | 

Window ID.

Default value: **\-1**.

 |
| textType12+ | string | No | No | Accessibility text type of an element, which is configured by the **accessibilityTextHint** attribute of the component. |
| offset12+ | number | No | No | 

Pixel offset of the content area relative to the top coordinate of a scrollable component, such as **List** and **Grid**.

Default value: **0**.

 |
| hotArea12+ | [Rect](#rect) | No | No | Touchable area of an element. |
| customComponentType18+ | string | No | Yes | Custom component type. |
| accessibilityNextFocusId18+ | number | No | Yes | 

ID of the next component to be focused on. You can use **findElement('elementId')** to obtain the value of this attribute set on the component from the **AccessibilityElementInfo** object.

Default value: **\-1**.

 |
| accessibilityPreviousFocusId18+ | number | No | Yes | 

ID of the previous component to be focused on. You can use **findElement('elementId')** to obtain the value of this attribute set on the component from the **AccessibilityElementInfo** object.

Default value: **\-1**.

 |
| extraInfo18+ | string | No | Yes | 

Extended attributes, which are used to define the attributes of specific components, including:

\- **CheckboxGroupSelectedStatus**: selection status of the **CheckboxGroup** component. The options are as follows:

**0**: selected

**1**: partially selected

**2**: not selected

\- **Row**: row where a focused item is located in **Grid**.

\- **Column**: column where a focused item is located in **Grid**.

\- **ListItemIndex**: row where a focused item is located in **List**.

\- **SideBarContainerStates**: expansion state of the expandable components (such as **SideBarContainer** and **Select**). The options are as follows:

**0**: collapsed

**1**: expanded

\- **ToggleType**: type of the **Toggle** component. The options are as follows:

**0**: checkbox

**1**: switch

**2**: button

\- **BindSheet**: position of the **BindSheet** component on the screen. The options are as follows:

**0**: high

**1**: middle

**2**: low

\- **hasRegisteredHover**: whether the component has registered the **onAccessibilityHover** event callback. The value **1** indicates that the component has registered the event callback; otherwise, this field is not used.

\- **direction**: layout direction of the **List** component. The value can be **vertical** or **horizontal**.

\- **expandedState**: expanded state of list items in the **List** component. The value can be **expanded** or **collapsed**.

\- **componentTypeDescription**: detailed information about the component type.

 |
| accessibilityScrollable18+ | boolean | No | Yes | 

Whether an element is scrollable for accessibility. This attribute has a higher priority than **scrollable**.

\- **true** (default): the element is scrollable.

\- **false**: the element is not scrollable.

 |

#### FocusDirection

type FocusDirection = 'up' | 'down' | 'left' | 'right' | 'forward' | 'backward'

Enumerates the focus directions.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'up' | Search for the next focusable item above the current item in focus. |
| 'down' | Search for the next focusable item below the current item in focus. |
| 'left' | Search for the next focusable item on the left of the current item in focus. |
| 'right' | Search for the next focusable item on the right of the current item in focus. |
| 'forward' | Search for the next focusable item before the current item in focus. |
| 'backward' | Search for the next focusable item after the current item in focus. |

#### FocusType

type FocusType = 'accessibility' | 'normal'

Enumerates the focus types.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'accessibility' | Accessibility focus. |
| 'normal' | Normal focus. |

#### Rect

Defines a rectangle.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | Left boundary of the rectangle. |
| top | number | No | No | Top boundary of the rectangle. |
| width | number | No | No | Width of the rectangle. |
| height | number | No | No | Height of the rectangle. |

#### WindowType

type WindowType = 'application' | 'system'

Enumerates the window types.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'application' | Application window. |
| 'system' | System window. |

#### AccessibilityExtensionContext.setTargetBundleName(deprecated)

setTargetBundleName(targetNames: Array<string>): Promise<void>;

Sets the concerned target bundle. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/c0ThziHmSf2HKbBhLuZpsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFDCB07A18E0613DFBC085CC0E302DF908D3E6C6D9F760267DDF4C8E795BFD7D)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetNames | Array<string> | Yes | Bundle name of the concerned target application. The service receives accessibility events of the concerned application. By default, accessibility events of all applications are received. Pass in an empty array if there is no concerned application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = \['com.ohos.xyz'\];
axContext.setTargetBundleName(targetNames).then(() => {
  console.info(\`Succeeded in set target bundle names, targetNames is ${targetNames}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to set target bundle names, Code is ${err.code}, message is ${err.message}\`);
})

#### AccessibilityExtensionContext.setTargetBundleName(deprecated)

setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void;

Sets the concerned target bundle. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Vm-WoIo2T6qeDjI_fZ7L8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3014807D1264AE8E4653E82270FD9039D4AB4B5FB23182EFD51E9FB6A7483244)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetNames | Array<string> | Yes | Bundle name of the concerned target application. The service receives accessibility events of the concerned application. By default, accessibility events of all applications are received. Pass in an empty array if there is no concerned application. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, **err** that contains data is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = \['com.ohos.xyz'\];
try {
  axContext.setTargetBundleName(targetNames, (err: BusinessError) => {
    if (err && err.code) {
      console.error(\`failed to set target bundle names, Code is ${err.code}, message is ${err.message}\`);
      return;
    }
    console.info(\`Succeeded in set target bundle names, targetNames is ${targetNames}\`);
  });
} catch (error) {
  console.error(\`failed to set target bundle names, Because ${JSON.stringify(error)}\`);
}

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>;

Obtains the focus element. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ECzS0pyZSD2tk3PMBclB4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48D5AA445F36C3AE721E396F7C1AA163E2EC279A46D6B3E8ACD8D500E518A771)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isAccessibilityFocus | boolean | No | 
Whether the obtained element is an accessibility focus. The value **true** indicates that the element is an accessibility focus, and **false** indicates the opposite.

Default value: **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise used to return the current focus element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(\`Succeeded in get focus element,${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get focus element, Code is ${err.code}, message is ${err.message}\`);
})

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(callback: AsyncCallback<AccessibilityElement>): void;

Obtains the focus element. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/yN9NLsb_Taqjl8GT5vksGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=998D7D877CB46FA7C48823AB4FAB78ED64C1B42CD1F16F5FD2FD321DFA2E3F4E)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the current focus element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(\`failed to get focus element, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  rootElement = data;
  console.info(\`Succeeded in get focus element, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void;

Obtains the focus element. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/9PLuXdrzQp2f5z0DQZzPJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=371A9A7AFC24D8A78AAA21DE74CDA22DF1F28590282551FAEEEA560B6F8D9308)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isAccessibilityFocus | boolean | Yes | Whether the obtained focus element is an accessibility focus. The value **True** means that the obtained focus element is an accessibility focus, and **False** means the opposite. |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the current focus element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let isAccessibilityFocus = true;
let rootElement: AccessibilityElement;

axContext.getFocusElement(isAccessibilityFocus, (err: BusinessError, data: AccessibilityElement)=> {
  if (err && err.code) {
    console.error(\`failed to get focus element, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  rootElement = data;
  console.info(\`Succeeded in get focus element, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(windowId?: number): Promise<AccessibilityElement>;

Obtains the root element of a window. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1etI2UKyTIWCW32M7gf_2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9F2F6B2EA6ED57C76AFC6628118AD9EC2362EDF3E9C06AE835681FA530465AA)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | No | ID of the window whose root element is to be obtained. If this parameter is not specified, it indicates the current active window. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise used to return the root element of the specified window. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(\`Succeeded in get root element of the window, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get root element of the window, Code is ${err.code}, message is ${err.message}\`);
});

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void;

Obtains the root element of a window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/WGa604adRh6HovWhhMhsCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD06D8E36C8746752D929250845AA867E9599E07226FFE1D0D542FF59C29C710)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the root element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(\`failed to get root element of the window, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  rootElement = data;
  console.info(\`Succeeded in get root element of the window, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(windowId: number, callback: AsyncCallback<AccessibilityElement>): void;

Obtains the root element of a window. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/ASiDeqo4T767CavU6ko6qQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B878F8CB6D1C9344B917F8377FCD45DE8B846F6DEA100BBD4E037CD8813B0ABD)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | ID of the window whose root element is to be obtained. If this parameter is not specified, it indicates the current active window. |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the root element. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let windowId = 10;
let rootElement: AccessibilityElement;

axContext.getWindowRootElement(windowId, (err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(\`failed to get root element of the window, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  rootElement = data;
  console.info(\`Succeeded in get root element of the window, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(displayId?: number): Promise<Array<AccessibilityElement>>;

Obtains the list of windows on a display. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/PwNHPq2rQry2fgkwVVoJPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2721313122EC980B514FBEE6FFA88A1AE74A3F39DAEB705AE2A69B80BEA0DBDE)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | No | ID of the display from which the window information is obtained. If this parameter is not specified, it indicates the default main display. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AccessibilityElement](#accessibilityelement)\>> | Promise used to return the window list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows().then((data: AccessibilityElement\[\]) => {
  console.info(\`Succeeded in get windows, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get windows, Code is ${err.code}, message is ${err.message}\`);
});

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void;

Obtains the list of windows on a display. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/6E2brYvVQDuL_Q0fjXOh8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D088AA99451D4B3BA53BE6A497AE2CDC28A8A17396CCD91ABB0AD00E67F09BB0)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | Yes | Callback used to return the window list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows((err: BusinessError, data: AccessibilityElement\[\]) => {
  if (err && err.code) {
    console.error(\`failed to get windows, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get windows, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(displayId: number, callback: AsyncCallback<Array<AccessibilityElement>>): void;

Obtains the list of windows on a display. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/eoEReELJTqaA4cgymqHzHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=975343F64C6D76D0130CD48754476618F3D1DFB374D993BA2B2B0CA408D15C21)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | ID of the display from which the window information is obtained. If this parameter is not specified, it indicates the default main display. |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | Yes | Callback used to return the window list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let displayId = 10;
axContext.getWindows(displayId, (err: BusinessError, data: AccessibilityElement\[\]) => {
  if (err && err.code) {
    console.error(\`failed to get windows, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get windows, ${JSON.stringify(data)}\`);
});

#### AccessibilityExtensionContext.injectGesture(deprecated)

injectGesture(gesturePath: GesturePath): Promise<void>;

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/qGpiMCttRGScnnU7enqkyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61A5C3ADDCF1B808F95EB4AB2EDFBBAA0CE35524EC6784029515B54DD1EC21B6)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [AccessibilityExtensionContext.injectGestureSync](#accessibilityextensioncontextinjectgesturesyncdeprecated) instead.

Injects a gesture. This API uses a promise to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](../ohos-accessibility-gesturepath-gesture-path/document.md#gesturepath) | Yes | Path of the gesture to inject. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);

for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i \* 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath).then(() => {
  console.info(\`Succeeded in inject gesture,gesturePath is ${gesturePath}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to inject gesture, Code is ${err.code}, message is ${err.message}\`);
});

#### AccessibilityExtensionContext.injectGesture(deprecated)

injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/XXk2KAJRRJ2kkBizAFXwkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E268B658E1A28066731C0A6F3100B244B70B1F7549482E76B983FC56080DC60)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use [AccessibilityExtensionContext.injectGestureSync](#accessibilityextensioncontextinjectgesturesyncdeprecated) instead.

Injects a gesture. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](../ohos-accessibility-gesturepath-gesture-path/document.md#gesturepath) | Yes | Path of the gesture to inject. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i \* 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath, (err: BusinessError) => {
  if (err) {
    console.error(\`failed to inject gesture, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in inject gesture,gesturePath is ${gesturePath}\`);
});

#### AccessibilityExtensionContext.injectGestureSync(deprecated)

injectGestureSync(gesturePath: GesturePath): void

Injects a gesture.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/u_3rZ-65RlCcNon_LN7dFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0595F85F4F144E297E6B3C3488B2EDA83085B4E8909DBFBC5CBB9DBB5E9AD539)

This API is supported since API version 10 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](../ohos-accessibility-gesturepath-gesture-path/document.md#gesturepath) | Yes | Path of the gesture to inject. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**Example**

import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i \* 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGestureSync(gesturePath);

#### AccessibilityElement

Defines the **AccessibilityElement**. Before calling APIs of **AccessibilityElement**, you must call [AccessibilityExtensionContext.getFocusElement()](#accessibilityextensioncontextgetfocuselementdeprecated) or [AccessibilityExtensionContext.getWindowRootElement()](#accessibilityextensioncontextgetwindowrootelementdeprecated) to obtain an **AccessibilityElement** instance.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

#### \[h2\]attributeNames(deprecated)

attributeNames<T extends keyof ElementAttributeValues>() : Promise<Array<T>>;

Obtains all attribute names of this element. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/1p2JLZ5pTJ2g_gvTTfB2Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=739D384866786793ACB13E39927B45E6471BD1619D6A38E7DE79FDD29B213AF3)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<T>> | Promise used to return all attribute names of the element. |

**Example**

import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeNames().then((data: ElementAttributeKeys\[\]) => {
  console.info(\`Succeeded in get attribute names, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get attribute names, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]attributeNames(deprecated)

attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void;

Obtains all attribute names of this element. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Kh2YITniTv6g3L03Kj-IGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5E7897C6934F5451D16BC2F0BC2A55A5A169E5C70F6BE430872CAE221EB8284)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<T>> | Yes | Callback used to return all attribute names of the element. |

**Example**

import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeNames((err: BusinessError, data: ElementAttributeKeys\[\]) => {
  if (err && err.code) {
    console.error(\`failed to get attribute names, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get attribute names, ${JSON.stringify(data)}\`);
});

#### \[h2\]attributeValue(deprecated)

attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues\[T\]>;

Obtains the attribute value based on an attribute name. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Qkgpwsw9RsOU28uXmWAA1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D526AD8AA7AC3E44BC4A987F7138977FB79CE8BFDC3DDAC6BB0FBF701F4AE4C)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attributeName | ElementAttributeKeys | Yes | Attribute name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ElementAttributeValues\[T\]> | Promise used to return the attribute value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300004 | This property does not exist. |

**Example**

import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeValue(attributeName).then((data: string) => {
  console.info(\`Succeeded in get attribute value by name, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get attribute value, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]attributeValue(deprecated)

attributeValue<T extends keyof ElementAttributeValues>(attributeName: T, callback: AsyncCallback<ElementAttributeValues\[T\]>): void

Obtains the attribute value based on an attribute name. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ElUkg7HRQ9CpK5_EOZTssw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EB94432E7BC9A55AD8E05821F143DA32A07B1231978887E351E3E2A9A21D76C)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attributeName | ElementAttributeKeys | Yes | Attribute name. |
| callback | AsyncCallback<ElementAttributeValues\[T\]> | Yes | Callback used to return the attribute value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300004 | This property does not exist. |

**Example**

import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement is an instance of AccessibilityElement.
rootElement.attributeValue(attributeName, (err: BusinessError, data: string) => {
  if (err && err.code) {
    console.error(\`failed to get attribute value, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get attribute value, ${JSON.stringify(data)}\`);
});

#### \[h2\]actionNames(deprecated)

actionNames(): Promise<Array<string>>;

Obtains the names of all actions supported by this element. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/xUUgS8zUTCOpkRz_vwvkmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F78DEADAE26E1C5305E8458B5456F8E4E97DAEC2149CB4B167C868395715994)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the names of all actions supported by the element. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
rootElement.actionNames().then((data: string\[\]) => {
  console.info(\`Succeeded in get action names, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get action names, Code is ${err.code}, message is ${err.message}\`);
})

#### \[h2\]actionNames(deprecated)

actionNames(callback: AsyncCallback<Array<string>>): void;

Obtains the names of all actions supported by this element. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/pvz2mSNNTD2rbthQ0dQZbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBA965ABDFC5DEC90BB1219E0C4CE60F4ACC35C9EE5B5F3A19919A0639D18587)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the names of all actions supported by the element. |

**Example**

// rootElement is an instance of AccessibilityElement.
rootElement.actionNames((err: BusinessError, data: string\[\]) => {
  if (err && err.code) {
    console.error(\`failed to get action names, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get action names, ${JSON.stringify(data)}\`);
})

#### \[h2\]performAction(deprecated)

performAction(actionName: string, parameters?: object): Promise<void>;

Performs an action based on the specified action name. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/VTx9z5-lToOEiqcjFVkkfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4418AC3B24DAB5B5B11D3565B53BB9B4E9BCA2FFCC64F74627BE871CB4278837)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| actionName | string | Yes | Action name. For details, see [Action](../ohos-accessibility-accessibility/document.md#action). |
| parameters | object | No | Parameters required for performing the target action. Empty by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName).then(() => {
  console.info(\`Succeeded in perform action,actionName is ${actionName}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
});

**Example of an action without parameters:**

import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// An action that does not require any parameter setting is an action without parameters, as specified in the action description.
rootElement.performAction('click').then(() => {
  console.info(\`Succeeded in perform action.\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
});

**Example of an action with parameters:**

import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// Sample code of setSelection
rootElement.performAction('setSelection', {
  selectTextBegin: '0', // Start position of the selection.
  selectTextEnd: '8',   // End position of the selection.
  selectTextInForWard: true   // true indicates the insertion point, and false indicates the selection range.
}).then(() => {
  console.info(\`Succeeded in perform action\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
});

import { BusinessError } from '@kit.BasicServicesKit';

// rootElement is an instance of AccessibilityElement.
// Sample code of setCursorPosition
rootElement.performAction('setCursorPosition', {
  offset: '1'   // Position of the cursor.
}).then(() => {
  console.info(\`Succeeded in perform action\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]performAction(deprecated)

performAction(actionName: string, callback: AsyncCallback<void>): void;

Performs an action based on the specified action name. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/-uBHEBeiScmcY4PPYVpZzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DB969749AEB054FF0A082591D0BD117B8E5095C28ED1BE50B4C7F072F20E5AA)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| actionName | string | Yes | Action name. For details, see [Action](../ohos-accessibility-accessibility/document.md#action). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName, (err: BusinessError) => {
  if (err && err.code) {
    console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in perform action, actionName is ${actionName}\`);
});

#### \[h2\]performAction(deprecated)

performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void;

Performs an action based on the specified action name. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/rp-0pKerSiG30cW6olyCTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDE10A116EC7DCAB6F23F848432BEA1208EBDA5835701773EA9845161493C805)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| actionName | string | Yes | Action name. For details, see [Action](../ohos-accessibility-accessibility/document.md#action). |
| parameters | object | Yes | Parameters required for performing the target action. Empty by default. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Accessibility Error Codes](../../error-codes/accessibility-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';
let parameters: object = \[\];

// rootElement is an instance of AccessibilityElement.
rootElement.performAction(actionName, parameters, (err: BusinessError) => {
  if (err && err.code) {
    console.error(\`failed to perform action, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in perform action,actionName is ${actionName}, parameters is ${parameters}\`);
});

#### \[h2\]findElement('content')(deprecated)

findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>;

Finds an element based on the content type. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/hfqV7q9iTe6ZnGFyBI1K8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B61E5B4783244EA15A71E695B9CE5E1257F7E0DECCC5BE99DC659B41DA728ED)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'content'**. |
| condition | string | Yes | Search criteria. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AccessibilityElement](#accessibilityelement)\>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('content', condition).then((data: AccessibilityElement\[\]) => {
  console.info(\`Succeeded in find element, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]findElement('content')(deprecated)

findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void;

Finds an element based on the content type. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Kpvv69xrQI6ev_hYihxHiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4199F8AA0471096242026262990377196D2274F82815115A31A635829BCA4826)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'content'**. |
| condition | string | Yes | Search criteria. |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('content', condition, (err: BusinessError, data: AccessibilityElement\[\])=>{
  if (err && err.code) {
    console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in find element, ${JSON.stringify(data)}\`);
});

#### \[h2\]findElement('focusType')(deprecated)

findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>;

Finds an element based on the focus type. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/mNWpxjyLRX61CiVs06aWkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA7093B3C88ED6ECD397BE34EAC02F22B6AADC98FA15CCDB4726DB6C6ACA62D2)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'focusType'**. |
| condition | [FocusType](#focustype) | Yes | Focus type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusType', condition).then((data: AccessibilityElement) => {
  console.info(\`Succeeded in find element,${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]findElement('focusType')(deprecated)

findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void;

Finds an element based on the focus type. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/SUe_7KcuReiGMU_h5j8cAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=725BD3B7A8FB961259F752293D94701BA05FFE68A1CA7419D2E18F965D9F71A2)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'focusType'**. |
| condition | [FocusType](#focustype) | Yes | Focus type. |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusType', condition, (err: BusinessError, data: AccessibilityElement)=>{
  if (err && err.code) {
    console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in find element, ${JSON.stringify(data)}\`);
});

#### \[h2\]findElement('focusDirection')(deprecated)

findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>;

Finds an element based on the focus direction. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/KK4SBnqgTICygDrzcAkzpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D02984C5F2F3C826A5BA50C987A40EEEF89085710BF222610A45B653C03A4593)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'focusDirection'**. |
| condition | [FocusDirection](#focusdirection) | Yes | Focus direction. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusDirection', condition).then((data: AccessibilityElement) => {
  console.info(\`Succeeded in find element, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]findElement('focusDirection')(deprecated)

findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void;

Finds an element based on the focus direction. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/WmIFAGv5QXCCq3HosT7vBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07F046E9C947A1EEB50EA2E0D3DC4D62B54A12CCC1A94BB87A22DA3A3B3C59F1)

This API is supported since API version 9 and deprecated since API version 12. Related capabilities are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of element finding. The value is fixed at **'focusDirection'**. |
| condition | [FocusDirection](#focusdirection) | Yes | Direction of the next focus element. |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement is an instance of AccessibilityElement.
rootElement.findElement('focusDirection', condition, (err: BusinessError, data: AccessibilityElement) =>{
  if (err && err.code) {
    console.error(\`failed to find element, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in find element, ${JSON.stringify(data)}\`);
});
