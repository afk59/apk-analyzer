# Panel

The **Panel** component is a slidable panel that presents lightweight content with flexible sizes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/PWIAkDEiTMKY7vzAT_WecA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2AAD5A65B15A8DE2083F0EFB43D7F5DB272013F9A9C9EE1AABB5AFCC54270FE)

This component is deprecated since API version 12. You are advised to use the universal attribute [bindSheet](../../universal-attributes/transition/sheet-transition/document.md) instead.

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/BK3SjuIZQkiF0aPUxD-w5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67BA49EF268CD56F1F0326C6E14CAA4CE2EF90ED2BD716435CE950255119D952)

Allowed child component types: built-in and custom components, including rendering control types ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)).

#### APIs

Panel(show: boolean)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| show | boolean | Yes | 
Whether the panel is shown.

**NOTE**

The panel is hidden and does not take up space in the layout if this parameter is set to **false** or [Visible.None](../../universal-attributes/basic-attributes/visibility-control/document.md) is set.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]type

type(value: PanelType)

Sets the type of the panel.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PanelType](#paneltype) | Yes | 
Type of the panel.

Default value: **PanelType.Foldable**

 |

#### \[h2\]mode

mode(value: PanelMode)

Sets the initial mode of the panel.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [PanelMode](#panelmode) | Yes | 
Initial mode of the panel.

Default value for the Minibar type: PanelMode.Mini; default value for other types: PanelMode.Half

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

 |

#### \[h2\]dragBar

dragBar(value: boolean)

Sets whether to enable a drag bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable a drag bar. The value **true** means that the drag bar will be displayed, and **false** means the opposite.

Default value: **true**

 |

#### \[h2\]customHeight10+

customHeight(value: Dimension | PanelHeight)

Sets the height of the panel in the **PanelType.CUSTOM** type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [PanelHeight](#panelheight10) | Yes | 
Height of the panel in the **PanelType.CUSTOM** type.

Default value: **0**

**NOTE**

This attribute cannot be set in percentage.

 |

#### \[h2\]fullHeight

fullHeight(value: number | string)

Sets the height of the panel in the **PanelType.Full** type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Height of the panel in **PanelMode.Full** mode.

Default value: main axis height of the panel minus 8 vp

**NOTE**

This attribute cannot be set in percentage.

 |

#### \[h2\]halfHeight

halfHeight(value: number | string)

Sets the height of the panel in **PanelMode.Half** mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Height of the panel in **PanelMode.Half** mode.

Default value: half of the main axis height of the panel

**NOTE**

This attribute cannot be set in percentage.

 |

#### \[h2\]miniHeight

miniHeight(value: number | string)

Panel height in the **PanelMode.Mini** mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Panel height in the **PanelMode.Mini** mode.

Default value: **48**

Unit: vp

**NOTE**

This attribute cannot be set in percentage.

 |

#### \[h2\]show

show(value: boolean)

Sets whether the panel is shown.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the panel is shown. The value **true** means to show the panel, and **false** means the opposite.

Default value: **true**

**NOTE**

The priority of this attribute is higher than that of the **show** parameter.

 |

#### \[h2\]backgroundMask9+

backgroundMask(color: ResourceColor)

Background mask of the panel.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Background mask of the panel.

Default value: **'#08182431'**

 |

#### \[h2\]showCloseIcon10+

showCloseIcon(value: boolean)

Sets whether to display the close icon.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the close icon. The value **true** means to display the close icon, and **false** means the opposite.

Default value: **false**

 |

#### PanelType

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Minibar | A minibar panel that displays content in the minibar area or a large (fullscreen-like) area. |
| Foldable | A foldable panel that displays permanent content in a large (fullscreen-like), medium-sized (halfscreen-like), or small area. |
| Temporary | A temporary panel that displays content in a large (fullscreen-like) or medium-sized (halfscreen-like) area. |
| CUSTOM10+ | A custom panel that automatically adapts its height to the content, but does not support manual resizing. |

#### PanelMode

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Mini | 0 | Displays a **minibar** or **foldable** panel in its minimum size. This attribute does not take effect for **temporary** panels. |
| Half | 1 | Displays a **foldable** or **temporary** panel in a medium-sized (halfscreen-like) area. This attribute does not take effect for **minibar** panels. |
| Full | 2 | Displays a panel in a large (fullscreen-like) area. |

#### PanelHeight10+

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| WRAP\_CONTENT | When the type is **CUSTOM**, the panel automatically adapts its height to the content. |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(event: (width: number, height: number, mode: PanelMode) => void)

Triggered when the status of the panel changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Width of the content area. |
| height | number | Yes | 
Height of the content area.

When the value of **dragBar** is **true**, the panel height is the sum of the drag bar height and content area height.

 |
| mode | PanelMode | Yes | Mode of the panel. |

#### \[h2\]onHeightChange9+

onHeightChange(callback: (value: number) => void)

Triggered when the height of the panel changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Height of the content area. The default unit is px.

When the value of **dragBar** is **true**, the panel height is the sum of the drag bar height and content area height.

For user experience purposes, the panel can be slid to only this height: **fullHeight** - 8 vp.

 |

#### Example

// xxx.ets
@Entry
@Component
struct PanelExample {
  @State show: boolean = false

  build() {
    Column() {
      Text('2021-09-30    Today Calendar: 1.afternoon......Click for details')
        .width('90%')
        .height(50)
        .borderRadius(10)
        .backgroundColor(0xFFFFFF)
        .padding({ left: 20 })
        .onClick(() => {
          this.show = !this.show
        })
      Panel(this.show) { // Display calendar events.
        Column() {
          Text('Today Calendar')
          Divider()
          Text('1. afternoon 4:00 The project meeting')
        }
      }
      .type(PanelType.Foldable)
      .mode(PanelMode.Half)
      .dragBar(true) // The drag bar is enabled by default.
      .halfHeight(500) // The panel height is half of the screen height by default.
      .showCloseIcon(true) // Display the close icon.
      .onChange((width: number, height: number, mode: PanelMode) => {
        console.info(\`width:${width},height:${height},mode:${mode}\`)
      })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/4jAJlLNbRJyESHRAXJpJmg/en-us_image_0000002568765753.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A77851540C8D8C106E3FEDBA93C4EC40FB439B1E9B6477DC0DF24EA785331BD)
