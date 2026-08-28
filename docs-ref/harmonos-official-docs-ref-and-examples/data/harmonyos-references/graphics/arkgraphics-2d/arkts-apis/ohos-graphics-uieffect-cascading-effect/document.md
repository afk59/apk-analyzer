# @ohos.graphics.uiEffect (Cascading Effect)

The uiEffect module provides basic capabilities to apply an effect, for example, blur, pixel stretch, and brightness, to a component. Effects are classified into filters and visual effects. Effects of the same category can be cascaded in an effect instance of the corresponding category. In actual development, the blur effect can be used for background blurring, and the brightness effect can be used for screen-on display.

-   [Filter](#filter): applies a filter to a component.
-   [VisualEffect](#visualeffect): applies a visual effect to a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/YpOR1MweQJ2El3-p101LVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=129A62F86F66E5EE80514C540A8DD1BA12FECDB6526613D4C8829721D4AEA1DF)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { uiEffect } from "@kit.ArkGraphics2D";

#### uiEffect.createFilter

createFilter(): Filter

Creates a **Filter** instance, which can be used to apply multiple filters to a component.

**System capability**: SystemCapability.Graphics.Drawing

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Head node of the filter. |

**Example**

let filter : uiEffect.Filter = uiEffect.createFilter()

#### uiEffect.createEffect

createEffect(): VisualEffect

Creates a **VisualEffect** instance, which can be used to apply multiple visual effects to a component.

**System capability**: SystemCapability.Graphics.Drawing

**Return value**

| Type | Description |
| :-- | :-- |
| [VisualEffect](#visualeffect) | Head node of the visual effect. |

**Example**

let visualEffect : uiEffect.VisualEffect = uiEffect.createEffect()

#### Filter

A class that can apply a filter to a component. Before calling any API in **Filter**, you must use [createFilter](#uieffectcreatefilter) to create a **Filter** instance.

#### \[h2\]blur

blur(blurRadius: number): Filter

Applies the blur effect to the component.

**System capability**: SystemCapability.Graphics.Drawing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | number | Yes | 
Blur radius.

The value must be greater than or equal to 0. The larger the radius is, the more blurred the content is.

If the value is 0, the content is not blurred.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | **Filter** instance with the blur effect. |

**Example**

// xxx.ts
import { uiEffect } from '@kit.ArkGraphics2D';

let filter: uiEffect.Filter = uiEffect.createFilter();
filter.blur(10);

@Entry
@Component
struct UIEffectFilterExample {
    build(){
        Column({ space: 15 }) {
            Text('UIEffectFilter').fontSize(20).width('75%').fontColor('#DCDCDC')
            Image($r('app.media.foreground'))
                .width(100)
                .height(100)
                .backgroundImage($r('app.media.background'))
                .backgroundImagePosition(Alignment.Center)
                .backgroundImageSize({ width: 90, height: 90 })
                .backgroundFilter(filter)
        }
        .height('100%')
        .width('100%')
    }
}

#### VisualEffect

A class that can apply a visual effect to a component. Before calling any API in **VisualEffect**, you must use [createEffect](#uieffectcreateeffect) to create a **VisualEffect** instance.
