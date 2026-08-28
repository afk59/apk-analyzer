# Focus Control

Focus control attributes determine whether a component can receive focus and how it participates in focus navigation. Users can switch focus between components using the Tab key or arrow keys.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/twr0gMxzSXa4wGM_qdvMJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4E050803379DFEAAEFBF41A4536A870D6332E26DD9A8D3FAC5D3A7E362C6B04)

-   The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Custom components are inherently unfocusable, and setting [focusable](#focusable) and [enabled](../enable-disable-control/document.md#enabled) attributes to **false** or setting the [visibility](../../basic-attributes/visibility-control/document.md#visibility) attribute to **Hidden** or **None** does not impact their child components' capability to gain focus.
    
-   Components can actively acquire focus independently of the window's focus state.
    
-   For details about focus development, see [Implementing Focus Support](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event).
    

#### focusable

focusable(value: boolean): T

Sets whether the component is focusable.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the component is focusable.

**true**: The component is focusable.

**false**: The component is not focusable.

**NOTE**

Components that have default interaction logic, such as [Button](../../../buttons-and-selections/button/document.md) and [TextInput](../../../text-and-input/textinput/document.md), are focusable by default. Other components, such as [Text](../../../text-and-input/text/document.md) and [Image](../../../images-and-videos/image/document.md), are not focusable by default. Only focusable components can trigger a [focus event](../../../universal-events/interaction-response-events/focus-event/document.md).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### tabIndex9+

tabIndex(index: number): T

Sets the tab navigation order of the component in sequential focus navigation with the **Tab** key. Components without explicit **tabIndex** settings follow default focus navigation rules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/q2jXEBvDSv2MdYufYMtwVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C6DD5602FCA6C6425D629FCE45955067BEF4131B308721887E0ADD0731B187E)

-   **tabIndex** only customizes **Tab** key navigation. For arrow key navigation customization, use [nextFocus](#nextfocus18).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Tab navigation order of the component in sequential focus navigation with the **Tab** key. When components with positive **tabIndex** values are present, only these components are reachable through sequential focus navigation, and they are navigated cyclically in ascending order based on the **tabIndex** value. When components with positive **tabIndex** values are not present, those components with a **tabIndex** value of **0** are navigated based on the preset focus navigation rule.

The [UiExtension](../../../../arkts-api/ui/ohos-arkui-uiextension-uiextension/document.md) component does not support **tabIndex**. As such, using **tabIndex** on [hierarchical pages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts) that contain **UiExtension** components may lead to disordered focus navigation.

\- **tabIndex** >= 0: The component is focusable and can be reached through sequential keyboard navigation.

\- **tabIndex** < 0 (usually **tabIndex** = -1): The component is focusable, but cannot be reached through sequential keyboard navigation.

**NOTE**

**tabIndex** and **focusScopeId** cannot be used together.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### defaultFocus9+

defaultFocus(value: boolean): T

Specifies whether to set this component as the default focus of the current [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts). If **defaultFocus** is not set, the component will not receive initial focus on the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/uoPq1OJ9TY-KQowlUpOf3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C1DB431C2C7F0429C7C1F7811EEF4C2E707E2CC886AFE711B718BA720CE2301)

This setting applies to pages that support routing or modal-type container components, such as **Page**, **NaviDestination**, **NavBar**, **PopUp**, and **Dialog**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to set the component as the default focus of the current [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts). This parameter takes effect only when the hierarchical page is new and accessed for the first time.

**NOTE**

The value **true** means to set the component as the default focus, and the value **false** has no effect.

If no component on the hierarchical page has **defaultFocus(true)** set:

For API version 11 and earlier, the default focus is on the first focusable non-container component.

For API version versions later than 11, the default focus is on the hierarchical page's root container.

If **defaultFocus(true)** is set for multiple components on the hierarchical page, the first component found in the component tree depth-first traversal is used as the default focus.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### groupDefaultFocus9+

groupDefaultFocus(value: boolean): T

Specifies whether to set the component as the default focus of the container. If **groupDefaultFocus** is not set, the component will not receive focus by default when its container is focused.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to set the component as the default focus of the parent container. This parameter takes effect only when the container is new and obtains focus for the first time.

**true**: The component is the default focus of the parent container.

**false**: The component is not the default focus of the parent container.

**NOTE**

This parameter must be used together with [tabIndex](#tabindex9). When **tabIndex** is set for a container and **groupDefaultFocus(true)** is set for a child in the container or for the container itself, then when the container obtains focus for the first time through sequential Tab navigation, the focus automatically moves to the specified component. If **groupDefaultFocus(true)** is set for multiple components in the container (including the container itself), the first component found in the component tree in-depth traversal receives the focus.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### focusOnTouch9+

focusOnTouch(value: boolean): T

Sets whether the component is focusable on touch. If **focusOnTouch** is not set, the component is not focusable on touch by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the component is focusable on touch.

**true**: The component is focusable on touch.

**false**: The component is not focusable on touch.

**NOTE**

This setting requires the component to be touchable.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### focusBox12+

focusBox(style: FocusBoxStyle): T

Sets the system focus box style for the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [FocusBoxStyle](#focusboxstyle12) | Yes | 
System focus box style for the component.

**NOTE**

This style affects only the components that display the system focus box during focus traversal.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### focusControl9+

Implements focus control.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]requestFocus9+

requestFocus(value: string): boolean

Requests focus transfer to the specified component during the next frame rendering. This global API provides asynchronous focus control.

For scenarios requiring immediate focus changes, it is recommended that you use the focus synchronization transfer API [requestFocus](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-focuscontroller/document.md#requestfocus12) in **FocusController**.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | String bound to the target component using **key(value: string)** or **id(value: string)**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns whether focus transfer is successfully requested for the target component. If the target component pointed to by the parameter exists, is mounted to the component tree, and is focusable, **true** is returned. Otherwise, **false** is returned. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/RnywVqM9RBWIjqVNhShW_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D3DC8AE8BA57C1977C7FA1FF48736E7EA65BF2E9305801D7493F306EA21BE32)

The following components support focus control: [TextInput](../../../text-and-input/textinput/document.md), [TextArea](../../../text-and-input/textarea/document.md), [Search](../../../text-and-input/search/document.md), [Button](../../../buttons-and-selections/button/document.md), [Text](../../../text-and-input/text/document.md), [Image](../../../images-and-videos/image/document.md), [List](../../../scroll-and-swipe/list/document.md), [Grid](../../../scroll-and-swipe/grid/document.md). Currently, the running effect of the focus event can be displayed only on a real device.

#### FocusBoxStyle12+

Sets the system focus box style for the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| margin | [LengthMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 
Distance of the focus box from the component's edge.

A positive number indicates the outside, and a negative number indicates the inside. The value cannot be in percentage.

 |
| strokeColor | [ColorMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | Stroke color of the focus box. |
| strokeWidth | [LengthMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Stroke width of the focus box.

Negative numbers and percentages are not supported.

 |

#### focusScopePriority12+

focusScopePriority(scopeId: string, priority?: FocusPriority): T

Sets the focus priority of this component in a specified container. It must be used together with [focusScopeId](#focusscopeid12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scopeId | string | Yes | 
ID of the container component where the current component's focus priority takes effect.

**NOTE**

1\. The current component must be inside the container identified by **scopeId** or inside a sub-container of that container.

2\. A component cannot set multiple priorities.

3\. A container component with **focusScopeId** set cannot have its priority set.

 |
| priority | [FocusPriority](#focuspriority12) | No | 

Focus priority.

**NOTE**

If **priority** is not set, **AUTO** is used by default.

Impact of the priority on focus traversal and component focus:

1\. When the container gains focus as a whole (hierarchical page level switching/focus switching to a focus group/container component requesting focus with **requestFocus**), if there is a component with a priority of **PREVIOUS** within the container, that component gains focus; otherwise, the last focused component does.

2\. When a container does not gain focus as a whole (using **Tab** or arrow keys in non-focus group scenarios), the highest priority component gets focus on first focus; subsequent focus follows position order regardless of priority.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### \[h2\]FocusPriority12+

Sets the focus priority of a component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Default priority, that is, the focus priority assigned by default. |
| PRIOR | 2000 | Priority that indicates the component is prioritized in the container. This level is higher than **AUTO**. |
| PREVIOUS | 3000 | Priority of a previously focused node in the container. This level is higher than **PRIOR**. |

#### \[h2\]KeyProcessingMode15+

Enumerates the modes for processing key events.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FOCUS\_NAVIGATION | 0 | Default value. When the current component does not consume the key event, focus navigation using the **Tab** and arrow keys preferentially stays within the current container. |
| ANCESTOR\_EVENT | 1 | When the current component does not consume the key event, focus navigation using the **Tab** and arrow keys is bubbled up to the parent component. |

#### focusScopeId12+

focusScopeId(id: string, isGroup?: boolean): T

Assigns an ID to this container component and specifies whether the container is a focus group.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | 
ID of the current container component.

**NOTE**

The ID must be unique within a single [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts).

 |
| isGroup | boolean | No | 

Whether the current container component is a focus group.

**true**: The current container component is a focus group.

**false**: The current container component is not a focus group.

Default value: **false**.

**NOTE**

Focus groups cannot be nested and should not be configured repeatedly.

The focus group and **tabIndex** cannot be used together.

The focus group enables the container and its elements to navigate focus according to the focus group rules as follows:

1\. Only arrow keys are allowed for focus traversal within the focus group; the **Tab** key will move the focus out of the focus group.

2\. When arrow keys are used to move the focus from outside the focus group to inside, if there is a component with a priority of **PREVIOUS** within the focus group, that component gains focus; otherwise, the last focused component does.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### focusScopeId14+

focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean): T

Assigns an ID to this container component and specifies whether the container is a focus group. Added the arrowStepOut parameter, which specifies whether the arrow keys can be used to move the focus out of the current focus group.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | 
ID of the current container component.

**NOTE**

The ID must be unique within a single [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts).

 |
| isGroup | boolean | No | 

Whether the current container component is a focus group.

**true**: The current container component is a focus group.

**false**: The current container component is not a focus group.

Default value: **false**.

**NOTE**

Focus groups cannot be nested and should not be configured repeatedly.

The focus group and **tabIndex** cannot be used together.

The focus group enables the container and its elements to navigate focus according to the focus group rules as follows:

1\. Only arrow keys are allowed for focus traversal within the focus group; the **Tab** key will move the focus out of the focus group.

2\. When arrow keys are used to move the focus from outside the focus group to inside, if there is a component with a priority of **PREVIOUS** within the focus group, that component gains focus; otherwise, the last focused component does.

 |
| arrowStepOut | boolean | No | 

Whether the focus can be moved out of the current focus group using arrow keys.

**true**: The focus can be moved out of the current focus group using arrow keys.

**false**: The focus cannot be moved out of the current focus group using arrow keys.

The default value is **true**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### tabStop14+

tabStop(isTabStop: boolean): T

Sets whether this container component is a focus stop. During focus traversal, the focus stops at the container component serving as a focus stop.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTabStop | boolean | Yes | 
Whether the current container component is a focus stop.

**true**: The current container component is a focus stop.

**false**: The current container component is not a focus stop.

**NOTE**

1\. To configure **tabStop**, make sure the component is a container and has focusable child components. By default, container components cannot directly gain focus.

2\. When [requestFocus](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-focuscontroller/document.md#requestfocus12) is used for requesting focus, if the component is a container and **tabStop** is configured, the focus can stop at the container. If **tabStop** is not configured, the component can still gain focus, even if there are other components in the focus chain with **tabStop** configured.

3\. Containers with **tabStop** configured should not be nested more than two levels deep.

Focus traversal rules with **tabStop**:

1\. During focus traversal using the **Tab** key or arrow keys, the focus stops at components with **tabStop** configured. If the focus is inside a container with **tabStop** configured, it can move to the next focusable component within the container. If the focus is outside such a container, it can move to the next focusable component outside the container.

2\. When the focus is on a container with **tabStop** configured: Pressing **Enter** moves the focus to the first focusable component inside the container.

Pressing **ESC** moves the focus back to the last component with **tabStop** configured within the current [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts).

Pressing the spacebar triggers the **onClick** event of the container.

3\. Whenever possible, avoid configuring **tabStop** on the root container. If **tabStop** is configured on the root container, the following behaviors will occur:

\- Using [clearFocus](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-focuscontroller/document.md#clearfocus12) to clear the focus to the root container and then pressing **Enter** will move the focus to the previously focused component inside the root container.

\- Using **ESC** to clear the focus to the root container and then pressing **Enter** will move the focus to the first focusable component inside the root container.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

**Example for describing the keys and focusable components during focus traversal**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/EchfR1rGQkyP4F5ivtWZpg/en-us_image_0000002537765438.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A4127B779992F1A7D51967FF0ADEDEA0FF2FC5B775FCA361E8CE9F2AADCDB33)

If the current focus is on **button2**, pressing the **Tab** key will move the focus to **Column3**. Pressing the **Tab** key again will move the focus back to **button1**.

#### nextFocus18+

nextFocus(nextStep: Optional<FocusMovement>): T

Sets the custom focus movement logic for the component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| nextStep | Optional<[FocusMovement](#focusmovement18)\> | Yes | 
Custom focus movement logic of the component.

**NOTE**

The default value resets **nextStep** to empty.

If custom focus movement is not set or the specified component does not exist, the default focus movement logic applies.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### FocusMovement18+

Sets the target component for focus movement based on key presses. If it is not specified, the default focus movement logic applies.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| forward | string | No | Yes | 
ID of the component to focus on when the **Tab** key is pressed.

The default value resets **forward** to empty.

 |
| backward | string | No | Yes | 

ID of the component to focus on when **Shift+Tab** is pressed.

The default value resets **backward** to empty.

 |
| up | string | No | Yes | 

ID of the component to focus on when the up arrow key is pressed.

The default value resets **up** to empty.

 |
| down | string | No | Yes | 

ID of the component to focus on when the down arrow key is pressed.

The default value resets **down** to empty.

 |
| left | string | No | Yes | 

ID of the component to focus on when the left arrow key is pressed.

The default value resets **left** to empty.

 |
| right | string | No | Yes | 

ID of the component to focus on when the right arrow key is pressed.

The default value resets **right** to empty.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Ke19IhfqRWeMi0606k9zmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D6D7C500072D88FE683A7F5FD9969C53889A59285C54038326C2E9DE1866D7E)

Directly using **focusControl** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain the [UIContext](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) object using the **getUIContext()** API and then obtain the **focusControl** bound to the instance using the [getFocusController](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getfocuscontroller12) API.

#### Example

## Example 1: Setting Focus and Focus Traversal Effects for Components

This example shows how to use [defaultFocus](#defaultfocus9), [groupDefaultFocus](#groupdefaultfocus9), and [focusOnTouch](#focusontouch9). **defaultFocus** sets the bound component as the initial focus after the [hierarchical page](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts) is created. **groupDefaultFocus** sets the bound component as the initial focus after the container with the specified **tabIndex** is created. **focusOnTouch** sets the bound component to obtain focus upon being clicked.

// focusTest.ets
@Entry
@Component
struct FocusableExample {
  @State inputValue: string = '';

  build() {
    Scroll() {
      Row({ space: 20 }) {
        Column({ space: 20 }) {
          Column({ space: 5 }) {
            Button('Group1')
              .width(165)
              .height(40)
              .fontColor(Color.White)
              .focusOnTouch(true) // The button is focusable on touch.
            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
                .focusOnTouch(true) // The button is focusable on touch.
            }

            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
            }
          }.borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)
          .tabIndex(1) // The Column component is the first component that obtains the focus when the Tab key is pressed.
          Column({ space: 5 }) {
            Button('Group2')
              .width(165)
              .height(40)
              .fontColor(Color.White)
            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
                .groupDefaultFocus(true) // The button obtains focus when its upper-level column is in focus.
            }

            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
            }
          }.borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)
          .tabIndex(2) // The Column component is the second component that obtains the focus when the Tab key is pressed.
        }

        Column({ space: 5 }) {
          TextInput({ placeholder: 'input', text: this.inputValue })
            .onChange((value: string) => {
              this.inputValue = value
            })
            .width(156)
            .defaultFocus(true) // The TextInput component is the initial default focus of the hierarchical page.
          Button('Group3')
            .width(165)
            .height(40)
            .fontColor(Color.White)
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }

          Button()
            .width(165)
            .height(40)
            .fontColor(Color.White)
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }

          Button()
            .width(165)
            .height(40)
            .fontColor(Color.White)
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }
        }.borderWidth(2).borderColor(Color.Orange).borderStyle(BorderStyle.Dashed)
        .tabIndex(3) // The Column component is the third component that obtains the focus when the Tab key is pressed.
      }.alignItems(VerticalAlign.Top)
    }
  }
}

Diagrams:

On first-time access, the focus is on the **TextInput** component bound to **defaultFocus**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/GP2R4f2pQweTI1PEdEriag/en-us_image_0000002537925378.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EE2DB1840D55FF88ADCEC9650209633D9F9081CDA812E7263B4AA24AF27A982)

Pressing the **Tab** key for the first time moves the focus to the container with **tabIndex(1)** and automatically navigates to the first focusable component inside the container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-PmbhOe8RvmFeUpLvs9vIg/en-us_image_0000002568685155.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0DA49D8DCD5A93DF90731B5E7531DC9DF79D14AA853BB786D15C5307F19E216)

Pressing the **Tab** key a second time shifts the focus to the container with **tabIndex(2)** and automatically navigates to the component bound to **groupDefaultFocus**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/kd6tnW1CT5OsTLHrOguZsA/en-us_image_0000002568765165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53B4A2035EBFCB44F3309B8DA5509382C3CD76932DC1BB0B94B771A7D2FF21F7)

Pressing the **Tab** key a third time shifts the focus to the container with **tabIndex(3)** and automatically navigates to the component bound to **DefaultFocus**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/4FaS7IKfRfugUWge_VbO3A/en-us_image_0000002537765440.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFDBE1C4D971C1E7F2461044E29D390417CC9DB2F4B6F10EB5A1A6FE8E4BE2DE)

Clicking the component bound to **focusOnTouch** sets the focus on the component and removes the focus indicator. Pressing the **Tab** key again displays the focus indicator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/E2eaeBPpS_apVK2v-kI_RQ/en-us_image_0000002537925380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C3281C2A326742025BE27C2DC71614B9391863B8D5EE8452D059ED771FFDC3C)

## Example 2: Setting Focus on a Specific Component

This example demonstrates how to set focus on a specific component using [focusControl.requestFocus](#requestfocus9).

// requestFocus.ets
@Entry
@Component
struct RequestFocusExample {
  @State idList: string\[\] = \['A', 'B', 'C', 'D', 'E', 'F', 'LastPageId'\];
  @State selectId: string = 'LastPageId';

  build() {
    Column({ space: 20 }) {
      Row({ space: 5 }) {
        Button("id: " + this.idList\[0\] + " focusable(false)")
          .width(180)
          .height(70)
          .fontColor(Color.White)
          .id(this.idList\[0\])
          .focusable(false)
        Button("id: " + this.idList\[1\])
          .width(180).height(70).fontColor(Color.White)
          .id(this.idList\[1\])
      }

      Row({ space: 5 }) {
        Button("id: " + this.idList\[2\])
          .width(180).height(70).fontColor(Color.White)
          .id(this.idList\[2\])
        Button("id: " + this.idList\[3\])
          .width(180).height(70).fontColor(Color.White)
          .id(this.idList\[3\])
      }

      Row({ space: 5 }) {
        Button("id: " + this.idList\[4\])
          .width(180).height(70).fontColor(Color.White)
          .id(this.idList\[4\])
        Button("id: " + this.idList\[5\])
          .width(180).height(70).fontColor(Color.White)
          .id(this.idList\[5\])
      }

      Row({ space: 5 }) {
        Select(\[{ value: this.idList\[0\] },
          { value: this.idList\[1\] },
          { value: this.idList\[2\] },
          { value: this.idList\[3\] },
          { value: this.idList\[4\] },
          { value: this.idList\[5\] },
          { value: this.idList\[6\] }\])
          .value(this.selectId)
          .onSelect((index: number) => {
            this.selectId = this.idList\[index\]
          })
        Button("RequestFocus")
          .width(180).height(70).fontColor(Color.White)
          .onClick(() => {
            // You are advised to use this.getUIContext().getFocusController().requestFocus().
            let res = focusControl.requestFocus(this.selectId) // Move the focus to the component specified by this.selectId.
            if (res) {
              this.getUIContext().getPromptAction().showToast({ message: 'Request success' })
            } else {
              this.getUIContext().getPromptAction().showToast({ message: 'Request failed' })
            }
          })
      }
    }.width('100%').margin({ top: 20 })
  }
}

Diagrams:

Press the **Tab** key to activate the focus state.

Below shows how the UI behaves when you request focus for a component that does not exist.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/sMTyLwQtRZSLXOPef-72Tg/en-us_image_0000002568685157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=406D19E3EEBCA430206DD1D633B432161956E38E1A746C408D9E2115A6D59090)

Below shows how the UI behaves when you request focus for a component that is not focusable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/u--f5WbjSdyhWYQDW-vVwA/en-us_image_0000002568765167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=766E7DC55CAF7E624D6462609FAC60810912B752434343248976E0F84C21FE8D)

Below shows how the UI behaves when you request focus for a focusable component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/EsqDUHHHSFyikQaMtAeKjw/en-us_image_0000002537765442.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38240019393629D602FC455D9FF702BE006DBC49555B0E70D87F999F69EA2C70)

## Example 3: Customizing the Focus Box Style

This example shows how to change the focus box style of a component by configuring [focusBox](#focusbox12).

import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct RequestFocusExample {
  build() {
    Column({ space: 30 }) {
      Button("small black focus box")
        .focusBox({
          margin: new LengthMetrics(0),
          strokeColor: ColorMetrics.rgba(0, 0, 0),
        })
      Button("large red focus box")
        .focusBox({
          margin: LengthMetrics.px(20),
          strokeColor: ColorMetrics.rgba(255, 0, 0),
          strokeWidth: LengthMetrics.px(10)
        })
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/hsVXc9kkRwe7MKIvApoFgg/en-us_image_0000002537925382.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC59A7F146AAEEE752FD40908D375B11B0939BA8EA1870AFCF77DA97B025DD05)

## Example 4: Setting Focus Group Traversal

This example demonstrates how to set a component as the initial focus when its container gains focus by configuring [focusScopePriority](#focusscopepriority12). Configuring [focusScopeId](#focusscopeid12) allows the bound container component to become a focus group.

// focusTest.ets
@Entry
@Component
struct FocusableExample {
  @State inputValue: string = '';

  build() {
    Scroll() {
      Row({ space: 20 }) {
        Column({ space: 20 }) { // Labeled as Column1.
          Column({ space: 5 }) {
            Button('Group1')
              .width(165)
              .height(40)
              .fontColor(Color.White)
            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
            }

            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
            }
          }.borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)

          Column({ space: 5 }) {
            Button('Group2')
              .width(165)
              .height(40)
              .fontColor(Color.White)
            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
                .focusScopePriority('ColumnScope1', FocusPriority.PRIOR) // Focus when Column1 first gains focus.
            }

            Row({ space: 5 }) {
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
              Button()
                .width(80)
                .height(40)
                .fontColor(Color.White)
            }
          }.borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)
        }
        .focusScopeId('ColumnScope1')

        Column({ space: 5 }) { // Labeled as Column2.
          TextInput({ placeholder: 'input', text: this.inputValue })
            .onChange((value: string) => {
              this.inputValue = value
            })
            .width(156)
          Button('Group3')
            .width(165)
            .height(40)
            .fontColor(Color.White)
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }

          Button()
            .width(165)
            .height(40)
            .fontColor(Color.White)
            .focusScopePriority('ColumnScope2', FocusPriority.PREVIOUS) // Focus when Column2 gains focus.
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }

          Button()
            .width(165)
            .height(40)
            .fontColor(Color.White)
          Row({ space: 5 }) {
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
            Button()
              .width(80)
              .height(40)
              .fontColor(Color.White)
          }
        }.borderWidth(2).borderColor(Color.Orange).borderStyle(BorderStyle.Dashed)
        .focusScopeId('ColumnScope2', true) // Column2 is a focus group.
      }.alignItems(VerticalAlign.Top)
    }
  }
}

Diagrams:

Pressing the **Tab** key for the first time shifts the focus to the component bound to **focusScopePriority** in container 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/q51MZid9Tk6Z9NfUDxmLsA/en-us_image_0000002568685159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF510677EE0F77FBE4577554E8AAC097400407631BA589BF91C18CD2BD647110)

Pressing the **Tab** key again moves the focus to the next component in container 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/xjZyLT1MTAKBVQBV6A3m4w/en-us_image_0000002568765169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16B72F1746CBF89EC5EF76EF636A1AE729EABB56AD43F222FFAA5447D7618382)

Pressing the **Tab** key once more shifts the focus to the subsequent component in container 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/0wm5HfToTUSvKD1-mSxjKA/en-us_image_0000002537765444.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D26573F344EEE06FD7320CC1F0290CD4C9C907C435C9087F785E77ECC9AC4FC)

Continuing to press the **Tab** key transfers the focus to the component configured with **focusScopePriority** in container 2.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/gkixA4XxRyak0BWlBxfucw/en-us_image_0000002537925384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5369101CBC81C473CCCD2F418FCDE6AE5296B2B9D836EFA6E3F569AAF2B8DD0F)

Pressing the **Tab** key again moves the focus to the component named **Group1** in container 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/B9_XZ2KcTC2ScJevxKJ1ew/en-us_image_0000002568685161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98E37011776584F2B975E71498530AC9096D8C136F4955F7C925C4C4BDC1123B)

## Example 5: Setting Focus Stop

This example illustrates how to use [tabStop](#tabstop14) to enable focus stop on a component during focus traversal with the **Tab** key.

import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TabStop {
  build() {
    Column({ space: 20 }) {
      Column({ space: 20 }) {
        Column({ space: 20 }) {
          Row({ space: 5 }) {
            Button("button 1")
              .width(200).height(70).fontColor(Color.White)
              .focusBox({
                margin: LengthMetrics.px(20),
                strokeColor: ColorMetrics.rgba(23, 169, 141),
                strokeWidth: LengthMetrics.px(10)
              })
          }

          Row({ space: 5 }) {
            Button("button 2")
              .width(200).height(70).fontColor(Color.White)
              .focusBox({
                margin: LengthMetrics.px(20),
                strokeColor: ColorMetrics.rgba(23, 169, 141),
                strokeWidth: LengthMetrics.px(10)
              })
          }
        }.width('80%').margin({ top: 30 }).borderColor(Color.Black)
      }.width('95%').margin({ top: 60 }).borderColor(Color.Black)

      Column({ space: 20 }) {
        Column({ space: 20 }) {
          Row({ space: 5 }) {
            Button("button 3")
              .width(200)
              .height('70%')
              .fontColor(Color.White)
              .focusBox({
                margin: LengthMetrics.px(20),
                strokeColor: ColorMetrics.rgba(23, 169, 141),
                strokeWidth: LengthMetrics.px(10)
              })
              .margin({ top: 15 })
          }
        }
        .width('80%')
        .height('120')
        .borderColor(Color.Black)
        .margin({ top: 10 })
        .tabStop(true)
        .focusBox({
          margin: LengthMetrics.px(20),
          strokeColor: ColorMetrics.rgba(23, 169, 141),
          strokeWidth: LengthMetrics.px(10)
        })
        .borderWidth(1)
      }.width('95%').margin({ top: 50 }).borderColor(Color.Black)
    }
  }
}

Diagrams:

Pressing **Tab** twice moves the focus to **button2**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/J-hmwWT-SvCSe2cySUOQ0Q/en-us_image_0000002568765171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A54E7EABCCB010104BBEBCBDFF007E2F7B7BDEFC6036B0C32DA78B02DE91F503)

Pressing **Tab** again moves the focus to the component configured with **tabStop**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/lyTeHEDeS-mHWILW4ZMnpg/en-us_image_0000002537765446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE2975813D5B6B87596E546736E20A768A5482DD72F17E3AB6801BE2B29952CD)

Pressing **Enter** moves the focus to **button3**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/64zPymp7QEqg0QKb7gWiPA/en-us_image_0000002537925386.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3741FB5EDC03280773FCE9503B0393BEA09970BCB50ED37F249D0E1F2794B3E8)

Pressing **ESC** again moves the focus to the component configured with **tabStop**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/_ANJio3fRneZuZqGXQaa2A/en-us_image_0000002537765446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E883C58DED19C56F5564667D65CB61BB1896D6B2720F934CD8E6AF407E975D3E)

Pressing **Tab** moves the focus back to **button1**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/-X42--TyR8WxH39vkZ9Q6w/en-us_image_0000002568685163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CDDDBDD3B86CD30F03FBC5D2B20ED1949B215A46889FE96F5571485BCE5FB7D)

## Example 6: Setting Custom Focus Movement

This example demonstrates how to implement custom focus movement logic using the [nextFocus](#nextfocus18) API, available since API version 18.

Without [nextFocus](#nextfocus18) configured, the default focus navigation order using the **Tab** key is as follows: M -> A -> B -> C. After [nextFocus](#nextfocus18) is configured, the order changes to the following: M -> D -> F -> B.

class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.id('M')
    instance.nextFocus({ forward: 'D', up: 'C', down: 'D' })
  }
}

@Entry
@Component
struct Index {
  @State modifier: MyButtonModifier = new MyButtonModifier();
  @State idList: string\[\] = \['A', 'B', 'C', 'D', 'E', 'F'\];

  build() {
    Column({ space: 10 }) {
      Row({ space: 10 }) {
        Button("id: M")
          .attributeModifier(this.modifier)
        Button("id: " + this.idList\[0\])
          .id(this.idList\[0\])
          .nextFocus({
            forward: 'C',
            backward: 'M',
            up: 'E',
            right: 'F',
            down: 'B',
            left: 'D'
          });
        Button("id: " + this.idList\[1\])
          .id(this.idList\[1\])
      }

      Column({ space: 10 }) {
        Button("id: " + this.idList\[2\])
          .id(this.idList\[2\]);
        Button("id: " + this.idList\[3\])
          .id(this.idList\[3\])
          .nextFocus({ forward: 'F' });
      }

      Row({ space: 10 }) {
        Button("id: " + this.idList\[4\])
          .id(this.idList\[4\]);
        Button("id: " + this.idList\[5\])
          .id(this.idList\[5\])
          .nextFocus({ forward: 'B' });
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/d-vwN7WYQiKY2hLV8NAi8g/en-us_image_0000002568765173.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88AFCC38B27E3038C21C621C30140BAC8ED7FC8971266A2A4F3C1FA735CCAE24)
