# Accessibility

You can set accessibility attributes and events for components to fully leverage accessibility features.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/n3YWzXBnRMOUL8eRgb1Bng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2674B9E96A037207E647D04230E8457BF270BDEB2C41A441BBC21C3207837DD)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### accessibilityGroup

accessibilityGroup(value: boolean):T

Sets whether to enable accessibility grouping. When accessibility grouping is enabled, the component and all its children are treated as a single selectable unit, and the accessibility service will no longer focus on the individual child components.

If accessibility grouping is enabled for a component that does not contain a universal text attribute or an [accessibility text](#accessibilitytext) attribute, the system will concatenate the universal text attributes of its child components to generate merged text for the component. Child components without universal text attributes will be ignored during concatenation, and their accessibility text (if any) won't be used in the merged text.

When a child component's [accessibilityLevel](#accessibilitylevel) is set to **"yes"**, it becomes focusable by screen readers when other accessibility criteria are met, bypassing **accessibilityGroup** constraints.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable accessibility grouping. The value **true** means to enable accessibility grouping, and **false** means the opposite. When accessibility grouping is enabled, the component and all its children are treated as a single selectable unit, and the accessibility service will no longer focus on the individual child components. Text and accessibility information from child components are merged and sent to the accessibility service as a whole.

Default value: **false**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityGroup14+

accessibilityGroup(isGroup: boolean, accessibilityOptions: AccessibilityOptions):T

Sets whether to enable accessibility grouping. When accessibility grouping is enabled, the component and all its children are treated as a single selectable unit, and the accessibility service will no longer focus on the individual child components.

If accessibility grouping is enabled for a component that does not contain a universal text attribute or an [accessibility text](#accessibilitytext) attribute, the system will concatenate the universal text attributes of its child components to generate merged text for the component. Child components without universal text attributes will be ignored during concatenation.

When a child component's [accessibilityLevel](#accessibilitylevel) is set to **"yes"**, it becomes focusable by screen readers when other accessibility criteria are met, bypassing **accessibilityGroup** constraints.

When [accessibilityPreferred](../../common-definitions/basic-types/document.md#accessibilityoptions14) is set to **true**, the system prioritizes concatenating the accessibility text attributes of the child components to generate merged text for the component. If a child component has no accessibility text set, its universal text attribute will be used instead. Components without either attribute will be excluded from concatenation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/SuOZ_GcnTdy232Q0azD0MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6422900AD8A86C1BFACFE10AF712EB866A1AE9CDBA913B67B0BAC67E03C05145)

This API cannot be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 14.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isGroup | boolean | Yes | 
Whether to enable accessibility grouping. The value **true** means to enable accessibility grouping, and **false** means the opposite. When accessibility grouping is enabled, the component and all its children are treated as a single selectable unit, and the accessibility service will no longer focus on the individual child components. Text and accessibility information from child components are merged and sent to the accessibility service as a whole.

Default value: **false**

 |
| accessibilityOptions | [AccessibilityOptions](../../common-definitions/basic-types/document.md#accessibilityoptions14) | Yes | 

Options for accessibility grouping. When **accessibilityPreferred** is set to **true**, the system will prioritize concatenating accessibility text for screen readers. When **accessibilityPreferred** is set to **false**, accessibility text will not be prioritized.

**stateController** and **actionController** enable the current aggregated component to use the state information and tap events of specific child components as its accessibility capabilities.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityText

accessibilityText(value: string):T

Sets the accessibility text. If a component lacks text content, you can set the accessibility text attribute to enable text-to-speech playback for accessibility purposes. If a component already contains text content, the accessibility text takes precedence during screen reading scenarios.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | 
Accessibility text. If a component does not contain text content, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for such components. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

**NOTE**

If a component has both text content and accessibility text, only the accessibility text is announced.

If a component is grouped for accessibility purposes but lacks both text content and accessibility text, the screen reader will concatenate text from its child components (depth-first traversal).

To prioritize accessibility text concatenation, set **accessibilityPreferred** in [accessibilityGroup](#accessibilitygroup14).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityText12+

accessibilityText(text: Resource):T

Sets the accessibility text, with support for resource references using [Resource](../../common-definitions/basic-types/document.md#resource). If a component lacks text content, you can set the accessibility text attribute to enable text-to-speech playback for accessibility purposes. If a component already contains text content, the accessibility text takes precedence during screen reading scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/uUhei5qxTcm8VJOScu4YVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4331F3848569D6A7320B1CD493DE65A3AB6E55D52A15796F01B2DB1A2858A116)

This API cannot be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Resource reference of accessibility text. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for such components. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

**NOTE**

If a component has both text content and accessibility text, only the accessibility text is announced.

If a component is grouped for accessibility purposes but lacks both text content and accessibility text, the screen reader will concatenate text from its child components (depth-first traversal).

To prioritize accessibility text concatenation, set **accessibilityPreferred** in **accessibilityGroup**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityDescription

accessibilityDescription(value: string):T

Sets the accessibility description. This attribute provides additional context and explanation for the component, helping users understand its functionality and purpose.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | 
Accessibility description. You can specify further explanation of the current component, such as potential operation consequences that cannot be inferred from component attributes or accessibility text. If a component contains both text content and the accessibility description, the screen reader announces the text first, followed by the accessibility description, when the component is selected.

Default value: **""**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityDescription12+

accessibilityDescription(description: Resource):T

Sets the accessibility description, with support for resource references using [Resource](../../common-definitions/basic-types/document.md#resource). This attribute provides additional context and explanation for the component, helping users understand its functionality and purpose.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/lQIWT8lKTzGiy9LGIeHoKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2688BFDFB5E342AB3A0BB82A8EE7CDD3F88590C1E966EDDD703D350F1DA366A3)

This API cannot be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| description | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | Accessibility description resource reference. You can specify further explanation of the current component, such as potential operation consequences that cannot be inferred from component attributes or accessibility text. If a component contains both text content and the accessibility description, the screen reader announces the text first, followed by the accessibility description, when the component is selected. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityLevel

accessibilityLevel(value: string):T

Sets the accessibility level. It determines whether the component can be recognized by accessibility services.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | 
Accessibility level that determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component's recognizability is determined jointly by accessibility services and ArkUI.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**NOTE**

When accessibilityLevel is set to **"auto"**, the component's recognizability depends on the following factors:

1\. The accessibility service internally determines whether the component can be recognized.

2\. If the parent component's **accessibilityGroup** property has **isGroup** set to **true**, the accessibility service will not focus on its child components, making them unrecognizable.

3\. If the parent component's **accessibilityLevel** is set to **"no-hide-descendants"**, the component will not be recognized by accessibility services.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityVirtualNode11+

accessibilityVirtualNode(builder: CustomBuilder):T

Sets an accessibility virtual child node. For custom drawing components, a **CustomBuilder** is passed, which is used to provide accessibility information. The components within the **CustomBuilder** are only used for layout and not for display. When the accessibility service obtains node information, it returns the node information from the **CustomBuilder**. For example, when using the [Canvas](../../canvas-drawing/canvas/document.md) component, you can set placeholder components matching the position and size through virtual nodes, enabling accessibility services to recognize the drawn content in corresponding areas.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/RcVi1mPUS4eCMBpYlKgxFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46DA22EEB0E26ABB0E589A54A5EFAB384E44CE78A182E0B1207DF30676B76ABF)

This API cannot be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | Yes | Accessibility virtual node. Pass a custom builder to the custom drawing component. The components within the custom builder are used for layout only and are not visually rendered. When accessibility services retrieve node information, the node information from the custom builder is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityChecked13+

accessibilityChecked(isCheck: boolean):T

Sets the checked state for the accessibility node. This API is used in multi-select scenarios and only affects component state announcements in screen reading scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/kMN6mV1sQK6H2IzynTgkEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=401EB2824EFDE19E97F594492DD839D9FA094E949705716D5CEC6A6BCE675C84)

This API can be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 13.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isCheck | boolean | Yes | 
Whether the current component is selected.

The options are as follows:

**true**: The component is selected.

**false**: The component is not selected.

**undefined**: The component determines its own selected state.

Default value: **undefined**.

**NOTE**

1\. Setting this parameter to **true** or **false** will automatically set the component's **checkable** attribute to **true**.

2\. The **accessibilityChecked** attribute indicates that a component operates in multi-selection mode, whereas [accessibilitySelected](#accessibilityselected13) indicates single-selection mode. These two modes are mutually exclusive: A component cannot simultaneously support both. Concurrent usage creates accessibility conflicts, causing screen readers and other assistive technologies to incorrectly interpret the selection state. When implementing multi-selection mode using **accessibilityChecked** (by setting it to **true** or **false**), ensure that the **accessibilitySelected** attribute is not simultaneously configured. If it is previously set, reset **accessibilitySelected** to **undefined** using its corresponding API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilitySelected13+

accessibilitySelected(isSelect: boolean):T

Sets the checked state for the accessibility node. This API is used in single-select scenarios and only affects component state announcements in screen reading scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/403WQnCNQdKxG7d6f4YB9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7887A849896D9FF8816AE2A164B0A8518A77EAACF81EC95DA0FDBCFD7215BD8)

This API can be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 13.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isSelect | boolean | Yes | 
Whether the current component is selected.

The options are as follows:

**true**: The component is selected.

**false**: The component is not selected.

**undefined**: The component determines its own selected state.

Default value: **undefined**.

**NOTE**

1\. [accessibilityChecked](#accessibilitychecked13) indicates multi-select mode, while **accessibilitySelected** indicates single-select mode. These modes are mutually exclusive: A component cannot support both simultaneously. Concurrent usage creates accessibility conflicts, causing screen readers and other assistive technologies to misinterpret selection states.

When implementing single-select mode using this parameter (by setting it to **true** or **false**), ensure that **accessibilityChecked** is not configured.

If it is previously set, reset **accessibilityChecked** to **undefined** using its corresponding API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityRole18+

accessibilityRole(role: AccessibilityRoleType):T

Sets the role type of the accessibility component, which affects how the component is announced by screen readers.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| role | [AccessibilityRoleType](#accessibilityroletype18) | Yes | Role of the component as announced by screen readers (for example, button or chart). You can define custom roles. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### AccessibilityRoleType18+

Enumerates the component role types used by screen readers.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_SHEET | 0 | Action sheet. |
| ALERT\_DIALOG | 1 | Alert dialog box. |
| INDEXER\_COMPONENT | 2 | Indexer component. |
| BADGE\_COMPONENT | 3 | Badge component. |
| BLANK | 4 | Blank placeholder component. |
| BUTTON | 5 | Button. |
| BACK\_BUTTON | 6 | Back button on a large image page. |
| SHEET\_DRAG\_BAR | 7 | Drag bar for sheets. |
| CALENDAR\_PICKER | 8 | Calendar picker. |
| CALENDAR | 9 | Calendar. |
| CANVAS | 10 | Canvas component. |
| CANVAS\_GRADIENT | 11 | Gradient object. |
| CANVAS\_PATTERN | 12 | Pattern for image filling based on a specified source image and repetition mode. |
| CHECKBOX | 13 | Check box component. |
| CHECKBOX\_GROUP | 14 | Check box group. |
| CIRCLE | 15 | Component for drawing circles. |
| COLUMN\_SPLIT | 16 | Vertical layout of child components with horizontal dividers. |
| COLUMN | 17 | Container that lays out child components vertically. |
| CANVAS\_RENDERING\_CONTEXT\_2D | 18 | 2D drawing object, which can be used to draw rectangles, images, and texts on a canvas component. |
| CHART | 19 | Chart component. |
| COUNTER | 20 | Counter component. |
| CONTAINER\_MODAL | 21 | Modal container. |
| DATA\_PANEL | 22 | Data panel component. |
| DATE\_PICKER | 23 | Date picker. |
| DIALOG | 24 | Dialog box. |
| DIVIDER | 25 | Divider component. |
| DRAG\_BAR | 26 | Drag bar. |
| EFFECT\_COMPONENT | 27 | Container component for special effects. |
| ELLIPSE | 28 | Ellipse drawing component. |
| FLEX | 29 | Container that allows for flexible layout of child components. |
| FLOW\_ITEM | 30 | Child component of a waterfall layout container. |
| FORM\_COMPONENT | 31 | Widget component. |
| FORM\_LINK | 32 | Static widget interaction component. |
| GAUGE | 33 | Gauge component. |
| GRID | 34 | Grid container. |
| GRID\_COL | 35 | Grid column component. |
| GRID\_CONTAINER | 36 | Grid container that lays out child components vertically. |
| GRID\_ITEM | 37 | Single-item container within a grid container. |
| GRID\_ROW | 38 | Grid row component. |
| HYPERLINK | 39 | Hyperlink component. |
| IMAGE | 40 | Image component |
| IMAGE\_ANIMATOR | 41 | Frame animation component. |
| IMAGE\_BITMAP | 42 | Pixel data for canvas rendering. |
| IMAGE\_DATA | 43 | Pixel data for canvas rendering. |
| IMAGE\_SPAN | 44 | Component used to display inline images. |
| LABEL | 45 | Label. |
| LINE | 46 | Line. |
| LIST | 47 | List. |
| LIST\_ITEM | 48 | Specific item in a list. |
| LIST\_ITEM\_GROUP | 49 | List item group. |
| LOADING\_PROGRESS | 50 | Component for display loading animations. |
| MARQUEE | 51 | Marquee component. |
| MATRIX2D | 52 | 2D matrix object. |
| MENU | 53 | Menu. |
| MENU\_ITEM | 54 | Menu item. |
| MENU\_ITEM\_GROUP | 55 | Menu item group. |
| NAV\_DESTINATION | 56 | Content area of the **Navigation** component. |
| NAV\_ROUTER | 57 | Navigation component. |
| NAVIGATION | 58 | Root view container for navigation routing. |
| NAVIGATION\_BAR | 59 | Navigation bar. |
| NAVIGATION\_MENU | 60 | Navigation menu. |
| NAVIGATOR | 61 | Navigation container component. |
| OFFSCREEN\_CANVAS | 62 | Canvas for custom drawing of graphics. |
| OFFSCREEN\_CANVAS\_RENDERING\_CONTEXT2D | 63 | 2D drawing object, which can be used to draw rectangles, images, and texts on a canvas component. |
| OPTION | 64 | Specific item. |
| PANEL | 65 | Slidable panel. |
| PAPER\_PAGE | 66 | Page. |
| PATH | 67 | Path drawing component. |
| PATH2D | 68 | Path object. |
| PATTERN\_LOCK | 69 | Pattern lock component. |
| PICKER | 70 | Picker. |
| PICKER\_VIEW | 71 | Picker view. |
| PLUGIN\_COMPONENT | 72 | Plugin component. |
| POLYGON | 73 | Component used to draw a polygon. |
| POLYLINE | 74 | Component used to draw a polyline. |
| POPUP | 75 | Popup with a specific style. |
| PROGRESS | 76 | Text download button. |
| QRCODE | 77 | QR code. |
| RADIO | 78 | Radio button. |
| RATING | 79 | Component for selecting a rating within a given range. |
| RECT | 80 | Component used to draw a rectangle. |
| REFRESH | 81 | Pull-to-refresh container component. |
| RELATIVE\_CONTAINER | 82 | Relative layout component. |
| REMOTE\_WINDOW | 83 | Remote control window component. |
| RICH\_EDITOR | 84 | Component that supports rich text editing and interactive text editing. |
| RICH\_TEXT | 85 | Rich text component. |
| ROLE\_PAGER | 86 | Pagination component. |
| ROW | 87 | Container that lays out child components horizontally. |
| ROW\_SPLIT | 88 | Horizontal layout of child components with vertical dividers. |
| SCROLL | 89 | Scrollable container component. |
| SCROLL\_BAR | 90 | Scrollbar. |
| SEARCH | 91 | Search box component. |
| SEARCH\_FIELD | 92 | Search box. |
| SELECT | 93 | Drop-down list component. |
| SHAPE | 94 | Parent component of the drawing components. |
| SIDEBAR\_CONTAINER | 95 | Sidebar container that can show and hide the sidebar. |
| SLIDER | 96 | Vertical slider. |
| SPAN | 97 | Component used to display inline text. |
| STACK | 98 | Stack container. |
| STEPPER | 99 | Stepper component. |
| STEPPER\_ITEM | 100 | Page child component of the stepper component. |
| SWIPER | 101 | Swiper view container. |
| SWIPER\_INDICATOR | 102 | Navigation indicator for the **Swiper** component. |
| SWITCH | 103 | Switch. |
| SYMBOL\_GLYPH | 104 | Component for displaying a symbol glyph. |
| TAB\_CONTENT | 105 | Content view for a tab in the **Tabs** component. |
| TAB\_BAR | 106 | Tab bar. |
| TABS | 107 | Container that allows users to switch between content views through tabs. |
| TEXT | 108 | Text. |
| TEXT\_CLOCK | 109 | Text clock component. |
| TEXT\_ENTRY | 110 | Text input. |
| TEXT\_INPUT | 111 | Text box component. |
| TEXT\_PICKER | 112 | Text picker. |
| TEXT\_TIMER | 113 | Component that displays timing information and is controlled in text format. |
| TEXT\_AREA | 114 | Text area component. |
| TEXT\_FIELD | 115 | Text box. |
| TIME\_PICKER | 116 | Time picker. |
| TITLE\_BAR | 117 | Title bar. |
| TOGGLER | 118 | State component. |
| UI\_EXTENSION\_COMPONENT | 119 | UI extension component. |
| VIDEO | 120 | Component for playing video files and controlling playback. |
| WATER\_FLOW | 121 | Waterfall layout container. |
| WEB | 122 | Component for loading web pages. |
| XCOMPONENT | 123 | Custom rendering component. |
| ROLE\_NONE | 124 | Null. |

#### accessibilityNextFocusId18+

accessibilityNextFocusId(nextId: string):T

Sets the next component to receive focus during screen reader navigation.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| nextId | string | Yes | [Unique ID](../basic-attributes/component-id/document.md#id) of the next component to receive focus. If the ID does not correspond to any component, the setting is ignored. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityDefaultFocus18+

accessibilityDefaultFocus(focus: boolean):T

Sets the initial screen reader focus on the page.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| focus | boolean | Yes | Initial screen reader focus on the page. The value **true** means the component is the default initial focus for screen readers on the current page. Other values are ignored. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityUseSamePage18+

accessibilityUseSamePage(pageMode: AccessibilitySamePageMode):T

Sets the same-page mode for the current component and its host application.

Solves focus jumping issues in sub-tree scenarios for cross-process embedded components, such as [EmbeddedComponent](../../rendering-drawing/embeddedcomponent/document.md). When components are embedded across processes, timing inconsistencies between page change events in the embedded component and the host application can cause focus to shift unexpectedly from the current component to another component.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pageMode | [AccessibilitySamePageMode](#accessibilitysamepagemode18) | Yes | Same-page mode for the cross-process embedded component and the host application. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### AccessibilitySamePageMode18+

Enumerates the same-page modes for cross-process embedded components and their host applications.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SEMI\_SILENT | 0 | Ignores initial page loading events and root node page events from the cross-process embedded component. |
| FULL\_SILENT | 1 | Ignores all page events from the cross-process embedded component. |

#### accessibilityScrollTriggerable18+

accessibilityScrollTriggerable(isTriggerable: boolean):T

Sets whether the accessibility node triggers automatic screen scrolling. When no focusable components are visible on the current page within a container, this setting determines whether automatic scrolling is initiated.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isTriggerable | boolean | Yes | 
Whether the component triggers automatic scrolling for screen readers when the current page has no focusable components.

The options are as follows:

**true**: The component triggers automatic scrolling for screen readers when the current page has no focusable components.

**false**: The component does not trigger automatic scrolling for screen readers when the current page has no focusable components.

**undefined**: The default settings are restored.

Default value: **true**

**NOTE**

1\. This API does not affect the **scrollable** property in the [ElementAttributeValues](../../../../accessibility-kit/arkts-apis/accessibilityextensioncontext-accessibility-extension-context/document.md#elementattributevalues) of the native accessibility node.

2\. The final scrolling behavior is determined by the screen reader based on this API and whether the component supports scrolling.

3\. This API applies to all basic components. It is recommended for scrollable containers, such as [List](../../scroll-and-swipe/list/document.md), [Grid](../../scroll-and-swipe/grid/document.md), [Scroll](../../scroll-and-swipe/scroll/document.md), and [WaterFlow](../../scroll-and-swipe/waterflow/document.md).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityTextHint12+

accessibilityTextHint(value: string):T

Sets the text hint for the component, which can be queried by accessibility services.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/-bOrgMwCQ7y5IkXAFtbEDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=879BA171DB2848213176526750274845FB2FB3EB0211DB69D0B1DEE602CF1C96)

This API can be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Text hint for the component, which can be queried by accessibility services. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### accessibilityFocusDrawLevel19+

accessibilityFocusDrawLevel(drawLevel: FocusDrawLevel):T

Sets the drawing level for the accessibility focus highlight (green frame).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/2B34TZLGRvWNW1uoWeWbEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EE25597FFDC5B4B85A7807851B590A845FB7EE89488634FF08A48A5F4DE6DF3)

1.  By default, the accessibility focus highlight (green frame) is drawn at the same level as the focused component. This can sometimes result in the frame being obscured or clipped by parent components or siblings with higher [z-order](../basic-attributes/z-order-control/document.md).
    
2.  Drawing the green frame at the top [z-order](../basic-attributes/z-order-control/document.md) prevents obstruction from component [overlays](../basic-attributes/overlay-control/document.md#overlay) and [clipping](../visual-effects/shape-clipping/document.md#clip12). However, this approach may not be suitable for interacting with overlay components that should visually cover the focused element while keeping the accessibility highlight hidden.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| drawLevel | [FocusDrawLevel](../../common-definitions/enums/document.md#focusdrawlevel19) | Yes | Drawing level for the accessibility focus highlight frame. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current object. |

#### Example

## Example 1: Setting Accessibility Text and Description

This example demonstrates how to use **accessibilityText** and **accessibilityDescription** to customize the content announced by screen readers.

// xxx.ets
@Entry
@Component
struct Index {

  @Builder customAccessibilityNode() {
    Column() {
      Text(\`virtual node\`)
    }
    .width(10)
    .height(10)
  }

  build() {
    Row() {
      Column() {
        Text("Text 1")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Text("Text 2")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
      .accessibilityGroup(true)
      .accessibilityLevel("yes")
      .accessibilityText("Group") // If a component has both text content and accessibility text, only the accessibility text is announced.
      .accessibilityDescription("The Column component can be selected, and the announced content is 'Group'")
      .accessibilityVirtualNode(this.customAccessibilityNode)
      .accessibilityChecked(true)
      .accessibilitySelected(undefined)
    }
    .height('100%')
  }
}

## Example 2: Setting the Accessibility Group

This example shows how to prioritize reading the accessibility text of child components.

// xxx.ets
@Entry
@Component
struct Focus {
  build() {
    Column({ space: 10 }) {
      Text('123456')
        .focusable(true)
        .borderRadius(5)
        .accessibilityText("Accessibility text is announced if both accessibility text and text content are present")
        .accessibilityLevel("yes")
      Button().accessibilityLevel("yes").accessibilityText("Accessibility text is announced if no text is present")
      Button("Text content is announced if no accessibility text is present").accessibilityLevel("yes")
      Button()
      Button('btn123').accessibilityText("Button with both accessibility and text btn123").accessibilityLevel("yes")
      Button('btn123').accessibilityLevel("yes")
    }
    .accessibilityGroup(true, { accessibilityPreferred: true })
    .borderWidth(5)
    .width('100%')
    .height('100%')
  }
}

## Example 3: Setting the Initial Focus and the Next Focus of a Component

This example demonstrates the use of **accessibilityDefaultFocus** to set the default initial focus for the screen reader on the current page and **accessibilityNextFocusId** to set the next focus for components during focus traversal.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Text('Text Demo 1')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityNextFocusId('text3')
      Text('Text Demo 2')
        .id('text2')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityDefaultFocus(true)  // Set the component as initial focus for the screen reader.
        .accessibilityNextFocusId('text4')
      Text('Text Demo 3')
        .id('text3')
        .fontSize(50)
        .accessibilityLevel('yes')
        .accessibilityNextFocusId('text2')
      Text('Text Demo 4')
        .id('text4')
        .fontSize(50)
        .accessibilityLevel('yes')
    }
    .height('100%')
    .width('100%')
  }
}

## Example 4: Setting the Accessibility Component Type and Text Hint

This example demonstrates the use of **accessibilityRole** to set the accessibility component type and **accessibilityTextHint** to provide text hints for components that can be queried by assistive technologies.

// xxx.ets
@Entry
@Component
struct Index {
  @State isDownloading: boolean = false;
  @State hintStr: string = 'Click to start download';

  build() {
    Column({ space: 20 }) {
      Button(this.isDownloading ? 'Downloading' : 'Click to download')
        .accessibilityLevel('yes')
        .accessibilityTextHint(this.hintStr)
        .onClick(() => {
          this.isDownloading = !this.isDownloading;
          this.hintStr = this.isDownloading ? 'State changed to downloading' : 'State changed to paused';
        })
      TextInput({ placeholder: 'Enter phone number' })
        .accessibilityLevel('yes')
        .accessibilityTextHint('Enter an 11-digit phone number')
        .width('80%')
      Text('Announced as button type')
        .accessibilityLevel('yes')
        .accessibilityRole(AccessibilityRoleType.BUTTON)
        .accessibilityTextHint('The screen reader will announce this component as a button')
        .fontSize(30)
    }
    .height('100%')
    .width('100%')
  }
}

## Example 5: Configuring Screen Reader Scrolling, Focus Highlight Frame, and Cross-Process Focus

This example demonstrates the use of **accessibilityScrollTriggerable** to set whether an accessibility node supports screen reading scroll, **accessibilityFocusDrawLevel** to set the drawing level of the accessibility focus highlight frame, and **accessibilityUseSamePage** for cross-process embedded components, such as [EmbeddedComponent](../../rendering-drawing/embeddedcomponent/document.md).

// xxx.ets
import { Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Message: ';
  private want: Want = {
    // Bundle name of the EmbeddedComponent provider. Configure it as required.
    bundleName: 'com.example.embeddeddemo',
    // Ability name of the EmbeddedComponent provider. Configure it as required.
    abilityName: 'ExampleEmbeddedAbility',
  }

  build() {
    Row() {
      List() {
        ListItem() {
          Column() {
            Text(this.message)
              .fontSize(18)
              .fontColor('#2D2D2D')
              .fontWeight(FontWeight.Medium)
            Column() {
              EmbeddedComponent(this.want, EmbeddedType.EMBEDDED\_UI\_EXTENSION)
                .width('100%')
                .height('90%')
                .onTerminated((info) => {
                  this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
                })
                .onError((error) => {
                  this.message = 'Error: code = ' + error.code;
                })
                .accessibilityUseSamePage(AccessibilitySamePageMode.FULL\_SILENT)
                .width('90%')
                .height('50%')
                .backgroundColor('#F0F0F0')
                .borderRadius(8)
                .borderWidth(1)
                .borderColor('#D9D9D9')

              Stack() {
                Column() {
                  Text('Text 1')
                    .fontSize(18)
                    .fontColor('#2D2D2D')
                    .fontWeight(FontWeight.Medium)
                  Text('Text 1')
                    .fontSize(18)
                    .fontColor('#2D2D2D')
                    .fontWeight(FontWeight.Medium)
                    .accessibilityFocusDrawLevel(FocusDrawLevel.TOP)
                }
                .padding({ top: 8, bottom: 8 })

                Column() {
                  Text('Text 2')
                    .fontSize(18)
                    .fontColor('#FFFFFF')
                    .fontWeight(FontWeight.Medium)
                  Text('Text 2')
                    .fontSize(18)
                    .fontColor('#FFFFFF')
                    .fontWeight(FontWeight.Medium)
                }
                .backgroundColor('#4A90E2')
                .padding({
                  left: 12,
                  right: 12,
                  top: 10,
                  bottom: 10
                })
                .borderRadius(6)
              }
              .width('100%')
              .margin({ top: 10, bottom: 10 })
            }
            .width('100%')
            .height('100%')
            .margin({ top: 15 })
            .accessibilityText($r('app.string.app\_name'))
            .accessibilityDescription($r('app.string.module\_desc'))
            Column() {
              Text('Text 4')
                .fontSize(18)
                .fontWeight(FontWeight.Medium)
            }
            .margin({ top: 15 })
          }
          .width('100%')
        }
      }
      .accessibilityScrollTriggerable(false)
      .width('100%')
    }
    .height('100%')
    .backgroundColor('#F7F9FC')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/5hl5cBnDTr6NMgkOokQX2w/en-us_image_0000002568765197.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5EC483367D0759BA2F2C7B655EA8F073C8060560F7E9071791483B361173643)
