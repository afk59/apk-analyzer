# Accessibility

You can set accessibility attributes and events for components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/wsPHlrnBS76MLBir_5-7xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062300Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A81FC93EBE6D7F86C000D9BFD5C15C6A9F584DDC74B4433432CC15682B36B8F)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Attributes

| Name | Type | Default Value | Description |
| :-- | :-- | :-- | :-- |
| accessibilitygroup | boolean | false | Accessibility group. If this attribute is set to **true**, the component and all its child components form an entire selectable component, and the accessibility service will no longer be available for the content of its child components. |
| accessibilitytext | string | \- | Accessibility text. If a component does not contain text information, it will not be read when the component is selected by the screen reader. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set this attribute for components without text information. When the component is selected by the screen reader, the specified accessibility text will be read, informing the user which component is selected. If a component with this attribute set contains text information, only the accessibility text will be read. |
| accessibilitydescription | string | \- | Accessibility description. You can specify further explanation of the current component, for example, possible operation consequences, especially those that cannot be learned from component attributes and accessibility text. You can set a detailed description text for the attribute of the component to help users understand the operation to be performed. If a component contains both text information and the accessibility description, the text is read first and then the accessibility description, when the component is selected. |
| accessibilityimportance | string | auto | 
Accessibility importance, which is used to decide whether a component can be identified by the accessibility service. The value can be **auto**, **yes**, **no**, or **no-hide-descendants**. The last value forces the screen reader to ignore the current component and all its subcomponents.

**yes**: The current component is selectable for the accessibility service.

**no**: The current component cannot be selected for the barrier-free auxiliary service.

 |

-   accessibilitygroup
    
    <div accessibilitygroup="true">
      <text>text1</text>
      <text>text2</text>
    </div>
    
-   accessibilitytext
    
    <image src="common/image/barrierfree.jpg" accessibilitytext=" This is a landscape image. "></image>
    
-   accessibilitydescription
    
    <button accessibilitydescription="Click to open a dialog box." onclick="DialogShow">Show dialog</button>
    
-   accessibilityimportance
    
    In the following **accessibilityImportance** example, **<div>** and **<text>** are not selected by the accessibility service. To select a component that is unselected by default, add **accessibilityimportance="yes"** to the component.
    
    <div accessibilityimportance="no-hide-descendants">
      <text>text</text>
    </div>
    

#### Accessibility Events

| Name | Parameter | Description |
| :-- | :-- | :-- |
| accessibility | AbilityEvent | Event dispatched by the accessibility service. |

**Table 1** AbilityEvent attributes

| Name | Type | Description |
| :-- | :-- | :-- |
| eventType | number | 
Event type.

\- **0**: custom event.

\- **1**: accessibility focus.

\- **2**: clear accessibility focus

For non-focus-related events dispatched by the accessibility system, the **eventType** value is **0**. For onfocus events dispatched by the accessibility system, the **eventType** value is **1**. For onblur events dispatched by the accessibility system, the **eventType** value is **2**.

 |
| param | Object | Parameter that accessibility applications need to pass when sending custom events. |
