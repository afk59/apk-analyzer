# Special Effect Drawing Combination

The **useEffect** attribute is used to combine the drawing of special effects, such as background blur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/PWbmV9ChTSGdkPLwZ7tOVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=994B211E33E05918BCB929976F08B53450527BC57A369ECCF2272A5638C13AA7)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### useEffect

useEffect(value: boolean): T

Specifies whether to combine the drawing of special effects, such as background blur.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the component inherits the special effect settings of the **EffectComponent** component.

The value **true** means the component inherits the special effect settings of the **EffectComponent** component, and **false** means the opposite.

Default value: **false**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### useEffect14+

useEffect(useEffect: boolean, effectType: EffectType): T

Specifies whether to apply the effect defined by the window.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| useEffect | boolean | Yes | 
Whether to apply the effect defined by the window.

The value **true** means to apply the effect defined by the window.

Default value: **false**

 |
| effectType | [EffectType](#effecttype14) | Yes | 

Type of effect to apply to the component, which is defined by the window.

Default value: **EffectType.DEFAULT**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### useEffect18+

useEffect(useEffect: Optional<boolean>, effectType?: EffectType): T

Specifies whether to apply the effect defined by the window. Compared with [useEffect14+](#useeffect14), this **useEffect** attribute supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| useEffect | Optional<boolean> | Yes | 
Whether to apply the effect defined by the window.

The value **true** means to apply the effect defined by the window.

Default value: **false**

If **useEffect** is set to **undefined**, the previous value is retained.

 |
| effectType | [EffectType](#effecttype14) | No | 

Type of effect to apply to the component, which is defined by the window.

Default value: **EffectType.DEFAULT**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### EffectType14+

Enumerates the types of effect templates.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Uses the effect template defined. |
| WINDOW\_EFFECT | 1 | Uses the effect template defined by the window. |

Effect Template

| Device Type | Fuzzy Radius (Unit: px) | Saturation | Brightness | Color |
| :-- | :-- | :-- | :-- | :-- |
| Mobile device | 0 | 0 | 0 | '#ffffffff', displayed as white. |
| 2-in-1 device: dark mode | 80 | 1.5 | 1.0 | '#e52e3033', displayed as a semi-transparent light red. |
| 2-in-1 device: light mode | 80 | 1.9 | 1.0 | '#e5ffffff', displayed as a semi-transparent dark red. |
| Tablet | 0 | 0 | 0 | '#ffffffff', displayed as white. |
