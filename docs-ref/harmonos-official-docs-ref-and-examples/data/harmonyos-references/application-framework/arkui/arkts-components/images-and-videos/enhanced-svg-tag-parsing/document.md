# Enhanced SVG Tag Parsing

In API version 21 and later, when the [supportSvg2](../image/document.md#supportsvg221) attribute of the **Image** component is set to **true**, enhanced SVG tag parsing is enabled. This feature implements the following capabilities defined in the SVG 1.1 specification:

-   Usability enhancements: (1) The default parsing format for SVG image source colors is changed from #ARGB to #RGBA, complying with the SVG standard. (2) Strict URL type validation is conducted for referenced resources. (3) The **Image** component's [colorFilter](../image/document.md#colorfilter9) attribute takes effect for the entire SVG image source. (4) The **Image** component's [fillColor](../image/document.md#fillcolor20) attribute respects **fill='none'** declarations in the SVG source.
    
-   Advanced affine transformation support: configurable global pivot points, local rotation centers for **rotate** transformations, matrix transformation modes, invalid value detection and handling, affine transformations in clipping paths, and combined transformation scenarios.
    
-   Extended parsing capabilities: [viewBox](#configurable-alignment-and-scaling-rules-for-viewbox) allows customizing alignment and scaling rules, parsing clipping path units, parsing gradient units, parsing mask units and mask content units, parsing pattern units and pattern content units, and parsing filter units and primitive units.
    
-   Enhanced display effects: (1) The opacity attribute of the **<g>** (group) element takes effect for all nested child elements in the group. (2) The following features are enhanced: processing for the **clip-path** rule in **<g>** tags, tiling effects and offset value processing for pattern elements, and translation and scaling effects for linear and radial gradients; (3) The default behavior for abnormal mask and filter parameters is updated.
    

#### Impact of Enhanced SVG Tag Parsing on Elements and Attributes

The following table describes the SVG elements and attributes affected when enhanced parsing is enabled.

| Element | Attribute | Description |
| :-- | :-- | :-- |
| clipPath | clipPathUnits | 
**clipPathUnits**: defines the coordinate system reference for the clipping path.

Values:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

 |
| filter | 

filterUnits

primitiveUnits

x

y

width

height

 | 

**filterUnits**: coordinate and size reference for the filter effect area.

**primitiveUnits**: coordinate and size reference for filter primitive elements.

Values of **filterUnits** and **primitiveUnits**:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

**x**: x-axis offset component of the filter area. The default value is **\-10%**.

**y**: y-axis offset component of the filter area. The default value is **\-10%**.

**width**: width of the filter area. The default value is **120%**.

**height**: height of the filter area. The default value is **120%**.

 |
| mask | 

maskUnits

maskContentUnits

x

y

width

height

 | 

**maskUnits**: coordinate system and rendering mode for the mask.

**maskContentUnits**: coordinate system and rendering mode for elements within the mask.

Values of **maskUnits** and **maskContentUnits**:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

**x**: x-axis offset component of the mask area. The default value is **\-10%**.

**y**: y-axis offset component of the mask area. The default value is **\-10%**.

**width**: width of the mask area. The default value is **120%**.

**height**: height of the mask area. The default value is **120%**.

 |
| radialGradient | gradientUnits | 

**gradientUnits**: coordinate reference system for the gradient.

Values:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

 |
| linearGradient | gradientUnits | 

**gradientUnits**: coordinate reference system for the gradient.

Values:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

 |
| pattern | 

patternUnits

patternContentUnits

 | 

**patternUnits**: coordinate system and scaling for the **<pattern>** element.

**patternContentUnits**: coordinate system and scaling for elements within the pattern.

Values of **patternUnits** and **patternContentUnits**:

**userSpaceOnUse** (absolute coordinate system) and **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

 |
| g | 

opacity

clip-path

 | 

**opacity**: applies to all child elements within the group.

**clip-path**: applies to all child elements within the group.

 |
| General | transform | 

Performs 2D transformations (such as translation, rotation, scaling, and skewing) on SVG elements.

translate(x, y): translates an element along the x- or y-axis. ‌

rotate(angle, \[cx\], \[cy\]): rotates an element. (The optional parameters specify the rotation center.)

scale(sx, \[sy\]): scales an element. (When there is only one parameter, the element is scaled proportionally on the x- or y-axis.)

skewX(angle)/skewY(angle): skews an element along the x- or y-axis. ‌

matrix(a, b, c, d, e, f): defines complex transformations through a matrix.

 |
| General | transform-origin | 

Defines the transformation reference point. This attribute must be used with the [transform](../../universal-attributes/visual-effects/transformation/document.md#transform) attribute.

When **transform-origin** is configured, the specified (x, y) offset serves as the center point for affine transformations.

 |

#### Improved SVG Usability

The default color parsing format for SVG image sources has been updated from #ARGB to the SVG-standard #RGBA. IRI type validation is now strictly enforced. The scope of the **Image** component's [colorFilter](../image/document.md#colorfilter9) and [fillColor](../image/document.md#fillcolor20) attributes has been adjusted for better compliance.

## Updated Color Parsing Format

When SVG image sources use hexadecimal color formats, the default parsing has changed from #ARGB to the SVG-standard #RGBA. Affected attributes include **fill**, **stroke**, **stopColor**, and **stop-color**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/JmhauJqZSuewEsGNp7b5Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94CEFFCD25A4665C535BDBAF79AD1D38177EEF7CC58692633DDAFD14F1A3C35A)

The final display of SVG images is influenced by the **Image** component's **'objectFit'** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure [objectFit](../../../../../media/media-library-kit/arkts-components/ohos-multimedia-movingphotoview-movingphotoview/document.md#objectfit) appropriately based on the actual display requirements.

8-digit hexadecimal color example:

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#ff000030" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| 
Parsed as #ARGB.

Example: display effect of the rectangle with **fill="#ff000030"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/eAx9IzzLSFKQdzoBwe0xNQ/en-us_image_0000002537925664.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=870B5B3CE7FEEB41A7EF336E888E0E75B0580C6364E446B39A378854FD750EE2)

 | 

Parsed as #RGBA.

Example: display effect of the rectangle with **fill="#ff000030"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/rTqJDJXdTc-JoOF28QfJcg/en-us_image_0000002568685441.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34EDB065F1C3910E8111EBD326B28C04CC41BF53D29A3E33C087AD6F7E866574)

 |

7-digit hexadecimal color example:

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#BB88990" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| 
Parsed as #ARGB.

Display effect of the rectangle with **fill="#BB88990"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/-avn3K4CT_K652V1i7jqgQ/en-us_image_0000002568765451.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A82468B67CDE69F2C2C223F078E0B64158C329BBA3A32ADF49EB2CBE9BF87B3)

 | 

Renders as default black.

Display effect of the rectangle with **fill="#BB88990"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Qrk4__fRTWWRsqi5V10I6w/en-us_image_0000002537765726.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDB4D44C7D1FF82B3E5E9FFAFF0737093F5DE8B5278A527FDAF67105491E20B6)

 |

4-digit hexadecimal color example:

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="80" fill="#0000" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| 
Parsed as #ARGB.

Display effect of the rectangle with **fill="#8888"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/qI39zEo3S4-aqwi9lAD9Bg/en-us_image_0000002537925666.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED49A0615432E15814409E32BE289451EE6EABD488904FBEE14A477C8BE2287F)

 | 

Parsed as #RGBA.

Example: display effect of the rectangle with **fill="#0000"** (fully transparent)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/t7V4mnaCSKGfXnhsNlyA9g/en-us_image_0000002568685443.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD3E66C4095A35568981D26C4A86324583F4E557652289A77C50C8E5A7125545)

 |

## Strict IRI Type Validation

URL references for **filter**, **clip-path**, and **mask** now undergo strict type validation to prevent reference mismatches.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ctZWtgMSQveR-JSawgSTPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E81F2E0D89EC4DB143964415841E46EAF7662143CAE6B0249A3411D0C73485A3)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| Before Enhancement | After Enhancement |
| :-- | :-- |
| Mismatched URL types for **filter**, **clip-path**, and **mask** references caused incorrect display effects. | 
When URL types for **filter**, **clip-path**, and **mask** references do not match, the corresponding effects are not applied.

For example, the mask, clipping path, filter, pattern, and gradient tags have their own IDs. If the filter, clipping path, and mask attributes are bound to the IDs of other types of tags, the corresponding effects do not take effect. The corresponding effects take effect only when the mask attribute is bound to the mask tag ID, the clipping path attribute is bound to the clipping path tag ID, and the filter attribute is bound to the filter tag ID.

 |

For example, if the URL types do not match, the mask effect does not take effect.

<svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">
  <!-- Define a mask. -->
  <defs>
    <clipPath id="myClipPath">
      <circle cx="50" cy="50" r="40"/>
    </clipPath>
    <mask id="myMask">
      <rect x="0" y="0" width="100" height="100" fill="red"/>
    </mask>
  </defs>

  <!-- Use the mask. -->
  <rect x="10" y="10" width="180" height="80" fill="blue" mask="url(#myClipPath)"/>
</svg>

## Updated colorFilter Effect Scope

The **Image** component's [colorFilter](../image/document.md#colorfilter9) attribute now applies to the entire SVG image source instead of only the stroke border.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/H9tBQnXoS16kYkUg3kQIzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE231F3E4C6768E9D2F63F0DAF6B9C0F7D9D722D149217BA18C1D15D63693985)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| Original Source | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/yRVHpR7PQTCu1qXdvgbW_A/en-us_image_0000002568765453.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62B3DA685B6ED7A1ADA5696A7356DEF63054093E0B9ADA4B45A56804786FC6D0) | 
**colorFilter** only applies to the stroke border.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/uCh9C4SVQEOVA6OGw7auyQ/en-us_image_0000002537765728.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3728D557FBE7E7F5233DFAC7118DB1DDF1D22D44C219CB3EDE2FD72285B743D0)

 | 

**colorFilter** applies to the entire SVG image source.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/6y5dM6pUQfuPFKghzaDzOQ/en-us_image_0000002537925668.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B54503DECA8133E6E9C99D02B19634A3821F774F9D20AEF18744BC7190598D4A)

 |

The sample image and sample code are as follows:

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <!-- Rectangle -->
    <rect x="10" y="10" width="180" height="80" stroke="gray" stroke-width='16' fill="orange"/>
</svg>

@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image111.svg'))
          .width(220)
          .height(220)
          .colorFilter(
            \[ 0.6, 0,   0,   0, 0,
              0.2, 0.8, 0,   0, 0,
              0.2, 0.2, 1.2, 0, 0,
              0,   0,   0,   1, 0 \]
          )
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}

## Updated fillColor Effect Scope

When the **fill** attribute of an element in the SVG image source is set to **none**, the [fillColor](../image/document.md#fillcolor20) attribute of the **Image** component will no longer apply color filling to that element.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/NwQZ2EO4TUa72s5HfUG_7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47151C6F9B67ACFC840302FA36AD7EA8588C772759280F4921D548945A42839B)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| Before Enhancement | After Enhancement |
| :-- | :-- |
| 
**fillColor** applied to the element with **fill="none"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/347jxnjnS7mmvgDzCCiJUA/en-us_image_0000002568685445.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80FB53200D647B1262251ED60B71DEA53372F234E2E0E9C43E465010157976E8)

 | 

**fillColor** not applied to the element with **fill="none"**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/uCoWMybRRFWoIxyvA_fMog/en-us_image_0000002568765455.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D6C3C2E7BB691B0A4C86BB9BFF4B9B0C2F1201241AF3B7E76C7D98CBD49AC93)

 |

The sample image and sample code are as follows:

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Rectangle -->
  <rect x="10" y="10" width="180" height="80" fill="none"/>
</svg>

@Entry
@Component

struct Index {
  @State select: boolean = true
  @State effect:ImageFit = ImageFit.Contain
  build() {
    Row() {
      Column() {
        Image($rawfile('image11.svg'))
          .width(220)
          .height(220)
          .fillColor('blue')
          .supportSvg2(true)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### Extended Affine Transformation Capabilities

The [transform](../../universal-attributes/visual-effects/transformation/document.md#transform) attribute now supports the following: configurable global pivot points, local rotation centers, matrix transformation modes, invalid value verification, affine transformations in clipping paths, and affine transformations in combined scenarios.

## Configurable Global Transformation Center

SVG supports the capability of parsing the [transform-origin](../../../javascript-components/javascript-compatible-web-like-development-paradigm-arkui-full/universal-components/animation-styles/document.md) attribute to configure the global pivot point. The following table describes the effect before and after the enhancement.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/jU8uGNCqQim4dLiH708CSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8CF6B309C0190C43B743516DAE088B387667562D66B42E1CB7C3D906414D963)

The final display of SVG images is influenced by the **Image** component's '[objectFit](../image/document.md#objectfit)' value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| SVG Scenario | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| Basic SVG graphics with the transform functionality and **transform-origin** attribute | The (0,0) coordinate in the upper left corner of the SVG viewport served as the transformation center. | The (x, y) coordinate offset specified by **transform-origin** is used as the transformation center. |
| 
**transform** attribute configured with the rotate functionality and **transform-origin**

Example: 'transform="rotate(30)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/GOiuqt-zSuW3S8_5afeuBw/en-us_image_0000002537765730.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AF765CB59910F9FE26F2FC134E4CC0248861F2BAF0A32C07630F8F9960DA996) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/B8aOUsv0QT-m-VL94ovelQ/en-us_image_0000002537925670.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=556BA492223A9194E1D0E1FACEA4924EE0964D73150098224CD3545775FB4FFF) |
| 

**transform** attribute configured with the scale functionality and **transform-origin**

Example: 'transform="scale(0.77)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/PXkFzw8xSoWApw6ZGzRavg/en-us_image_0000002568685447.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=181E3D2AE7A5EFFC83CAD471EA9E0C8DF8794098D37A0665BF9DA77634323F52) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/2oVi1lOLSTajd1r_9e12TQ/en-us_image_0000002568765457.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=870FBA64800EF1DC1E2DB3BF6C30F7381A8CBE7B96C11587150A01EE212CBC41) |
| 

**transform** attribute configured with **skewX** and **transform-origin**

Example: 'transform="skewX(30)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/mwXuTHOSTWWIgnqnQzsxgA/en-us_image_0000002537765732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=987AA03D6C79A317A9ABC83581ADFB8A8C214169070D948115BCEBA244F0476E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/J9QlKrisSOOpi6uuvQ0IUw/en-us_image_0000002537925672.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99E486F25AAFFCB28D7234EC8128584783AFADD30CD95B4F8660FBF61AA0439B) |
| 

**transform** attribute configured with **skewY** and **transform-origin**

Example: 'transform="skewY(30)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/WPFDWvnsR3eRslR0SNoETg/en-us_image_0000002568685449.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA7ECE2BD9505948EF21961537281E55D8CA815232A3CECFC2CD8A3DF439740A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/FSFJncWBRZOmF9OLoy5htA/en-us_image_0000002568765459.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00B5957B190A3601FA102A6396541E6E1C48D74BFA3CFD6EB1D0FB7DB7E212DD) |
| 

**transform** attribute configured with the translate functionality and **transform-origin**

Example: 'transform="translate(30,30)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/1zIFAqGhR62arb5EIkUV3Q/en-us_image_0000002537765734.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCAD3A3E73BD34749BF92A25BEA517FD729B8571DAE3289FED05D1FDA7444745) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/dLgxFFuPSDG9QTtAZVJaMg/en-us_image_0000002537925674.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F565893B18F36F57394182E73FD3CCE6C8977EE98780E78F08BC4BA73063C190) |
| 

**transform** attribute calling multiple functions in chain mode with the **transform-origin** attribute configured

Example: transform='"translate(10,10) rotate(10) scale(0.5) skewX(10)" transform-origin="150 150"' (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/c2k0XTxbR962fbUwruZNug/en-us_image_0000002568685451.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19DFC2937042B2BB480CD59A4D916519EBB3080717D43E2933BBEA5CF91822B7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/DjOjSlTjRVi7wyCZw2ll2w/en-us_image_0000002568765461.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCC5ED06BD905098BCA00E9BE9D005910494B9ED30CB3D1ED312973A5FFE4594) |

## Local Center Point for rotate

SVG now supports local center point specification in the **rotate** function, for example, **rotate(30, -10, -10)**, where **\-10, -10** defines the local rotation center. The following table compares the rendering effects before and after configuring the local center point for **rotate**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_LvUTyFMR2ui7CGxkCXtxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDBC803C5CAE1C48AB8C2D017A12E261B8FABFE3E9A971A19A3E53B178295DFA)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| SVG Scenario | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| 
Basic SVG graphic with both local center point (**rotate**) and **transform-origin** configured

Example: 'transform="rotate(30, -10, -10)" transform-origin="150 150"'

 | 

Rotation uses only the coordinates (x, y) specified by the last two parameters of the **rotate** function as the transformation center.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/KcEjpcEpSn-4ahri-BGNPQ/en-us_image_0000002537765736.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC18E74677CADB3681420BF0887BAE6FFEA94999780074F970E18405B551E0C7)

 | 

Rotation uses the combined offset of the sum of the global **transform-origin** coordinates (x, y) and the local center point coordinates as the transformation center.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/eaJko_M4QLCWsWHtAg4IJw/en-us_image_0000002537925676.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=088F78867DC5267138FD8B3E8BEA1342749A77F5521EEED599558135EC6169CC)

 |

## Matrix Transformation Support

SVG supports the matrix transformations via the **transform** attribute using the matrix function. This enables complex linear transformations combining translation, rotation, scaling, and skewing operations. In the matrix(a, b, c, d, e, f) function, the parameters are as follows: **a** controls scaling in the X direction, **b** controls skewing in the X direction, **c** controls skewing in the Y direction, **d** controls scaling in the Y direction, **e** controls translation in the X direction, and **f** controls translation in the Y direction.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/0lqmSyFlR7uIoBcBqk9aWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD8642CB6C4BA98954A4093EEBA32A08942BFF0639FCCE6A2D4A2BCBC503104A)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| SVG Scenario | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| 
Matrix transformation with **transform-origin** configured

Example: 'transform="matrix(0.812,0.278,0.139,0.763,5.000,5.000" transform-origin="150 150"') (global center in the lower right corner)

 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/eVQQ5KyrTJaULnO2Of32ZQ/en-us_image_0000002568685453.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AE2FC9B2B3063D04E2E1AAAAE29370F79D4A4AE86097A210F967E518786432E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/cHTnOD3PTRmKk1fiMaGSCA/en-us_image_0000002568765463.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=067318C6C86E9E2BDADDACE5F1A94D6E86350237B93BDFEF497B99CCAA257C4A) |

## Invalid Value Verification

SVG now properly handles invalid **transform** attribute values. The following table describes how invalid parameter values or incorrect parameter counts are handled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/fCPxIWAeQ1yT6iqfuOjJrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE279854D490D574712F728EA1C185DB8E459316CB88CFFF7A15F30EA4418D87)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

| SVG Scenario | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| Invalid transform value, for example, invalid parameter value in the **rotate** function, 'transform="rotate(30deg)"' | 
The first parameter value (30) is used as the rotation angle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/O-yGiByWTIifNym2BVtBKA/en-us_image_0000002537765738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCA3B813E09A079562E36081DF693F423F99F451F9D706181229C5301F513951)

 | 

No rotation is performed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/kf4GkqiJSzW_OyHvuy5YrQ/en-us_image_0000002537925678.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90A9A24A726E26C46E4ECFF8842D28EC83C72855D258E6088C6A516C9C111498)

 |
| Invalid local center point parameters, for example, invalid local center point parameter in the **rotate** function, 'transform="rotate(30,abc,abc)"' | 

The coordinate (0,0) in the upper left corner of the SVG viewport is used as the transformation center point, and the image is rotated by 30 degrees.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Kl3QCIiRQlK74tAMtTNPSw/en-us_image_0000002568685455.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFA8B2476F2E70C31055F99B0507816EE5AF96F2DB6BCCB65D7CFB1F95F57A6C)

 | 

No rotation is performed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/Xap14NHRR0WSzycIfELKTg/en-us_image_0000002568765465.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24F36E13C4AC40CB00D451FC21679B508D714E345DC8ED2556CC72B57F778412)

 |
| Incorrect parameter count, for example, incorrect parameter count in the **scale** function, 'transform="scale(0.5, 0.5, 0.5)"' | 

The first two valid parameters (0.5,0.5) are used as the scale factor along the x-axis and y-axis.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/U1-Q5rWsRj2sDTGSDVvdtg/en-us_image_0000002537765740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ECB1B4FC99156F4F79113CC6D6C2B840EC321B26AD3BFFA9DDA10DD88F78C05)

 | 

No transformation is performed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/CcQZoPN0Qg2JjEPRf8BGXg/en-us_image_0000002537925680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=398BD39C5E680ACC98B5DBFF247F4ABD7B853F69DE0DBD4D0E6024EB62A64E8C)

 |
| Invalid parameter in chained functions, for example, 'transform="rotate(30) skewX(abc) scale (0.5, 0.5)"' | 

Only valid transformation functions **rotate** and **scale** are applied. The invalid transformation function **skewX** is not applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/VJNcUOuiSN6t7MKuNnp7Nw/en-us_image_0000002568685457.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22008915DB9CAA1CBABE5C490B6398177BA10F011ECA469C880AD1C274A8C10D)

 | 

No transformations are applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/iwjwaU3SQMiw3Ts1Q_cKVw/en-us_image_0000002568765467.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C3969ADF4D28B54C8F253FAF694A313B3DA54B79EDCAF1E5E4A26F970C59FE1)

 |

## Affine Transformations in Clipping Paths

Affine transformations are now supported within clipping paths with **clip-path**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/9yzETN7USBaf30zr84_TKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D94B984BD4834718FA91A082437EB25058DA0D8A9AFE15BDEB45F4C21DE0DE8)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Define a clipPath with ID "circleClip" using objectBoundingBox units. -->
  <defs>
    <clipPath id="circleClip" clipPathUnits="objectBoundingBox">
      <!-- The circle is centered on the object, with a radius of 0.5, which clips the object into a circle that covers its entire area. -->
      <circle cx="50" cy="50" r="40" transform="translate(50 50)" />
    </clipPath>
  </defs>

  <!-- Apply clipPath to a rectangle. -->
  <rect x="10" y="10" width="250" height="250" fill="blue"
        clip-path="url(#circleClip)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/hjDV-JSERbCjwXy13S1HJg/en-us_image_0000002537765742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7ACCE559B3C1FB8B81744901A6619B92C8E144EF47240C625DD842C1CCDBDB4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/_d60m60mSFuJyugGIoeL-Q/en-us_image_0000002537925682.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4191E812C2BECCB65703EF6DE2A1584BBA2CFDF1B1F43C44F5A9FB66103BD02F) |

## Affine Transformations in Combined Scenarios

Affine transformations are now supported in complex scenarios involving multiple elements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/FgSJ6DQQTyG_pR56QyWdwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CABECE91B6C77274357C744AFC19AD613F82ADF015F3A0DF3E8BE70C18DC205A)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

The transform operation is applied within a **<use>** element that references an object in the same **<mask>** element.

<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
      <use xlink:href="#rect1" transform="translate(0.6, 0.000000) scale(0.5 0.5)" />
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5" fill="red"  />
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg> 

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/YRC-B_ThSD-iWmatPvbxmA/en-us_image_0000002568685459.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AAC08695782E21431455399B8295B8800EE2B463FE651B028EDB3468D4B7805) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/CeSwEjKNTfyIXP3BqXcAsg/en-us_image_0000002568765469.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C79C0526AF5AD84F81B66ECA3AA1B708506FC7A52011AEFF32BED13EC75E2AB9) |

The transform operation is applied within a **<g>** element without scaling.

<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <mask id="mask1"  width="1" height="1" maskContentUnits="objectBoundingBox">
        <g transform="translate(0.6, 0.000000)">
      <rect id="rect1" x="0" y="0" width="0.5" height="0.5"  fill="red"  />
      </g>
    </mask>
  </defs>
  <rect x="0" y="0" width="300" height="100" fill="red"  mask="url(#mask1)" />
  <rect x="0" y="0" width="300" height="100" fill="none"  stroke="black" stroke-width="2" />
</svg> 

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zfOaBPyMSVOynPv4eHnhRw/en-us_image_0000002537765744.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE28DAE472AA5321B417D719A73E43905BC0F805A3CF23B467FB5C3B1BF26B2E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/iw9Yq8edTISFmy-NudkzWg/en-us_image_0000002537925684.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C041ACBF4999B12C2ECC5CF556C5E2912C187069324492B641AE3EC525BE3BE3) |

#### Extended SVG Parsing Capabilities

[viewBox](#configurable-alignment-and-scaling-rules-for-viewbox) allows customizing alignment and scaling rules, parsing clipping path units, parsing gradient units, parsing mask units and mask content units, parsing pattern units and pattern content units, and parsing filter units and primitive units.

## Configurable Alignment and Scaling Rules for viewBox

The **viewBox** attribute controls SVG dynamic stretching, with the **preserveAspectRatio** parameter governing content alignment and scaling rules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/wwDlvKXzQYiCrH1S1pJf1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CD02900B292223C0E45D88874225A0DF7071F0078E409CFA41CE9D490E22915)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

Example with **preserveAspectRatio** set to **"none"**:

<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" /> <!-- x-axis -->
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" /> <!-- y-axis -->
</svg>

| Value | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| none | 
Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/OGUVXPk7RBWFGQpYgQz53w/en-us_image_0000002568685461.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53583936F4130E14C951748ACD0E59787FF8A4F34C1DCB05CFF983C2129384C9)

 | 

Graphic content scaled to completely match view rectangle boundaries

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/9der5QUTTjiLHZwyKfvq8w/en-us_image_0000002568765471.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B17F5D60E0758751598E161F48375AFF045CEA724C91CD260C438D99B35B60A2)

 |

Example with **preserveAspectRatio** set to **<align> \[<meetOrSlice>\]**:

<svg width="200" height="100" viewBox="0 0 100 100" preserveAspectRatio="xMinYMin meet" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="20" r="20" fill="red"/>
  <line x1="0" y1="0" x2="0" y2="500" stroke="black" stroke-width="2" /> <!-- x-axis -->
  <line x1="0" y1="0" x2="500" y2="0" stroke="black" stroke-width="2" /> <!-- y-axis -->
</svg>

| Value | Before Enhancement | After Enhancement |
| :-- | :-- | :-- |
| xMinYMin meet | 
Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/QF1ustg_TDKWp1xtbFY0lw/en-us_image_0000002537765746.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C4D0A484B1A562264801EE68FE873B7BA7FB081F8DF813BA5E74018C9A9A542)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** is aligned with the minimum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/5Sq5f_KqTdimzkgVrsVUlA/en-us_image_0000002537925686.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42CB412D8D3D6CA05290121884A15DF7776FE83812EA87D5E8100725FBCD10C9)

 |
| xMaxYMin meet | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/2y6CwdqdSAm6x6nI5HVgfA/en-us_image_0000002568685463.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B26F22436FAB641D73F66DD2C283BE8730E2E76BD624EBFB0684E5F2C3CCA18C)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** is aligned with the minimum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/Qp6JEe5WSKKYJUvfxeA4ag/en-us_image_0000002568765473.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=769416DD534CD70508BD23BD7160779A028DFDBC2E53CBF2B3165E82C03E3890)

 |
| xMinYMid meet | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/3J-mvrVySMusQjADo8M-Qw/en-us_image_0000002537765748.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72072F58285D86FBE8571414498420B9A2C603DAD7F8D52893265C15FF5B4E6C)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Zf64XDuATfmxc0ThsjviQA/en-us_image_0000002537925688.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FFBBBFB6EEDC6B4E661D5BBB8E311565E68C3C11C7DF5F7D573C28238F5B31C)

 |
| xMaxYMid meet | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/a1pPYZhkRZSvoup6sEJnTA/en-us_image_0000002568685465.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=586F1A40256C6B2543E4F5B24C1FBC6D131A1D6208662070E4E291EFB7E4E866)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/-h9r9mu9Ro61nFTOCXvDBg/en-us_image_0000002568765475.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CE1BFF5E82CBE1F2B8F75E1C5FF1FBB0BB8DB48321A97D24FED020D11EDDBF1)

 |
| xMinYMax meet | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Of7mR7nYS16MhFZwUBPNYQ/en-us_image_0000002537765750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2E7563A6C50A7834FA5037B7C0CC18F0039382E40D8B0E67DB23A0F91AC7D15)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** plus the element height is aligned with the maximum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/chOOU0z_TM6SZ_-QvCf3iA/en-us_image_0000002537925690.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E040684DA0A8E0222BE511CF27B1A12231A82F2BD48B1E2B07EDE993C45FA4D8)

 |
| xMaxYMax meet | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/46p7XN2-Rm65bAIfE-_Fxg/en-us_image_0000002568685467.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BC0AB6DD5DB5EC950E10C3617D038F362F9A1F1B9D8D4035A231F20969B2F62)

 | 

Uniform scaling based on the minimum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** plus the element height is aligned with the maximum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/1mwAzs5QQMG03psFZijuaw/en-us_image_0000002568765477.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68B1B5FE1D8425AC4A632991CEF0A388E1914255D1B4ABA133307C22F60DD713)

 |
| xMinYMin slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/zptOH-yrQ0qmqMK6W-wlvQ/en-us_image_0000002537765752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB4577700E34801094EBC543538B24E769F182D7619B21F54BE8BD2B07596DD9)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** is aligned with the minimum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/8dtdVwk8TnWGV6jhBtkXOw/en-us_image_0000002537925692.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A6953AB67E44C8A69969B6BB3D39416043E5E67AACA5A8DBE1DF8D1EB03AE3A)

 |
| xMidYMin slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/fgxRdYM_SvqRd71SMtK8SQ/en-us_image_0000002568685469.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1820C1503B29087D9E3C2CF94E35EB166E9D96AE51B069B7CE99D7801F5EC2B7)

 | 

Uniform scaling based on the maximum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** is aligned with the minimum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/6E4ee6DvRaey7yLD4sFKYQ/en-us_image_0000002568765479.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3093685BD0F9F0779D12DBA37E232FE1168CA83F4C33535EEED8975BC033232D)

 |
| xMaxYMin slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NBZo6rR5T-i6NM0thd-c2Q/en-us_image_0000002537765754.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69F9C47386AC2810FD2E24A3506B0D0F2239F3F180EE7CE12DAB13E13610274E)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** is aligned with the minimum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/cLc5pucBSIOwx2EJClyyrA/en-us_image_0000002537925694.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33B155A6B9C41F43216238184130DDAF79F248182642AAB406AC75A4311A4FFA)

 |
| xMinYMid slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Ugnwu9TsQiusMiv9KStCtw/en-us_image_0000002568685471.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1022EC6194ED2626D7DC320B6018A4A3F5E543EFEBF46CB9B18C0BFF0816BFE5)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/zQjQmgdtSWaT0-cLCGSHTw/en-us_image_0000002568765481.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFC312946E66CC5D0FCDE0008D4B851DC09BF2B426032209F037C051439C4D63)

 |
| xMidYMid slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/J1QqQSlpSUem5OhlGSt7yA/en-us_image_0000002537765756.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D601ECCC77A000FAC030D250B424BCCB1724228F61A415246578E29E64A96105)

 | 

Uniform scaling based on the maximum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/c-fm1OUmTdWWqzTgrLXgUw/en-us_image_0000002537925696.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E949309D7838304E22CABE8CA4D9F7EE715986E9DB9933D26CB5E0D5D82ED5C)

 |
| xMaxYMid slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/733Ub-9XSCeI1-TBA7zzHg/en-us_image_0000002568685471.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4CDB1B2105ABD19D1449EB9900E1C354B2C9D061FB62C04B2DBDB7FF7304A19)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/HHMosYLQSyO0afbsjZ4kbw/en-us_image_0000002568685473.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AD0F85F9C8FC0E6B4EA1CDFA5809C0E0FFAF6EDA35C60515F4BD933C3DBA8E9)

 |
| xMinYMax slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/D6WJIw_WTH2kAIXs4qx09A/en-us_image_0000002568765483.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=725E313CFE6C81C1F9858CA0609B8C12632D8D8B7BB70B3349060BB7C48CEF29)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** is aligned with the minimum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** plus the element height is aligned with the maximum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/CQhejtvLRaif94zxZcSkRA/en-us_image_0000002537765758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C0D5F148756AF97E74AEC5FFE1C74C870BA26191DCDEE1F9F90E437389C0CF2)

 |
| xMidYMax slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/NV221qp7TUKTsJEFq1gt4g/en-us_image_0000002537925698.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A57FDBF27FE0E37F81B60E0D7380AA1EFAFB76FD9C1E71BA252823754D6F4A1)

 | 

Uniform scaling based on the maximum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** plus the element height is aligned with the maximum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/WjKoEPZcTsCetZW-iWS4Hw/en-us_image_0000002568685475.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB5BEB60C9E7234915A6D71AB9BF3C95BF7D17AC2299295268808D4E6C6B9FD2)

 |
| xMaxYMax slice | 

Uniform scaling based on the minimum aspect ratio

The midpoint **X** value of the SVG element's **viewBox** is aligned with the midpoint **X** value of the viewport.

The midpoint **Y** value of the SVG element's **viewBox** is aligned with the midpoint **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/42T7QAX4QhamlIGVNk_h7Q/en-us_image_0000002568765485.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D61A8290963E833E28CB1967819C0F090FED798A18804615BBFDC89AD194393)

 | 

Uniform scaling based on the maximum aspect ratio

The minimum **X** value of the SVG element's **viewBox** plus the element width is aligned with the maximum **X** value of the viewport.

The minimum **Y** value of the SVG element's **viewBox** plus the element height is aligned with the maximum **Y** value of the viewport.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/lI6Eox47Q4aV-9OUJ5VChQ/en-us_image_0000002537765760.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E89D76DA01E19DA738ACC03547AA98CF8C3AF760F81DE30F514883D3D53F50B)

 |

## Clipping Path Unit Parsing

Parsing [clipPathUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) is supported. Processing is added for the scenario where **clipPathUnits** is set to **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/O_-wg69sSVWpxo6f02o5xA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B2062B5882BC9225350D64029FFCA90BA6FA1F4C486CB5E8A86344E8CBA38FC)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

In the example below, when the clipping path unit is set to **objectBoundingBox**, the rectangular clipping path is positioned relative to the upper left corner of the element to which it is applied. The x and y coordinates are interpreted as fractions of the element's bounding box width and height, respectively. Similarly, the width and height values are multiplied by the bounding box width and height to determine the actual clipping size.

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="clip1" clipPathUnits="objectBoundingBox">
      <rect x="0.2" y="0.2" width="0.7" height="0.6" />
    </clipPath>
  </defs>
  <rect x="10" y="10" width="100" height="100" fill="blue" clip-path="url(#clip1)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/K8uA3kffQea39Bfa3HBgPw/en-us_image_0000002537925700.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3576558DEAC839AEA6DE1915E8D2FE10C1A4B10513713274E7FBABC720E3E84C) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/B6QFtHMpTeulbaKRb9ImBA/en-us_image_0000002568685477.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E3876D38BF98EACB1DABBFC241D5A34D7BECF93CF7F896288511F39D06794FC) |

## Gradient Unit Parsing

Parsing [gradientUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) is supported. Processing is added for the scenario where **gradientUnits** is set to **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/i96ROPqUQrqrlig1w0sFJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D60E55F969F2A66278CBCBF5C7A2B127991888D8625EA9EAECD5F8B5A9F1DD5)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

This example illustrates a linear gradient defined with absolute coordinates from (10, 10) to (180, 180) within a rectangle.

 <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="10" y1="10" x2="180" y2="180"  gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="180" height="180" fill="url(#grad1)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/mYmrfn0rT5yW427UMpvuXQ/en-us_image_0000002568765487.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14CBB341D9149254EC8C69951376B0384942B3A03BEF8ADF917E6572793DDFD0) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Rrr1NXnnSKuT8yPRJwt6-g/en-us_image_0000002537765762.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF3607886DAAC9A4E5EE32241365D4A7306E767A85D2B7125FA6FDBFB2387A1D) |

This example illustrates a radial gradient originating from the absolute coordinate center (100, 90) with a radius of 90.

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
     <radialGradient id="grad2" cx="100" cy="100" r="90" gradientUnits="userSpaceOnUse">
      <stop offset="0%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="90" fill="url(#grad2)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/WFN0rYAFRx-aDe2DIZHIJQ/en-us_image_0000002537925702.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65989ED16460EF7063626509475573F60164717F16991D14F4AAE07EB2921339) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/FhiyVbTZS3-ghC62qRMZFw/en-us_image_0000002568685479.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39862C071C36BC8246A68A4D65D06E7112244F3BF1FA64DFF37F55AB14EAEE5B) |

## Mask Unit and Mask Content Unit Parsing

Parsing [maskUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) and [maskContentUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) is supported. Processing is added for the scenario where **maskContentUnits** and **maskUnits** are set to **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/fTPPkVqvQ9qNaemlbrL0wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=979E8B3E6CC66E5B86F12E3528A230491674240ADEBBCF799FB490D516FA312D)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

This example demonstrates a five-pointed star mask defined within absolute coordinates from (10, 10) to (200, 200). The mask content is positioned relative to the upper left corner of the target rectangle, with horizontal dimensions multiplied by the graphic's bounding box width and vertical dimensions multiplied by the bounding box height.

<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" maskUnits="userSpaceOnUse" x="10" y="10" width="200" height="200" clip-rule="evenodd" maskContentUnits="objectBoundingBox">
        <path d="M 0.5,0.05 L 0.2,0.99 L 0.95,0.39 L 0.05,0.39 L 0.8,0.99 Z" fill="blue" fill-rule="nonzero"/>
    </mask>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="red" mask="url(#mask1)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/FoLa98qOTvez3wl3vEcqFg/en-us_image_0000002568765489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D292EA8309A2271E0637801FE307AFF363059C33E5B2AC7EF817477FA199464) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/zCsEZv5fQrqMi6tye0MG1w/en-us_image_0000002537765764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DE12EDA5B6EDF8FC53A09AD0684929DA8645087D8BC61A4E404BD903E90E976) |

## Pattern Unit and Pattern Content Unit Parsing

Parsing [patternUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) and [patternContentUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) is supported. Processing is added for the scenario where **patternUnits** and **patternContentUnits** are set to **objectBoundingBox** (coordinate system relative to the bounding box of the applied element).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/znLYF8OZTT-7QvkpVaItvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF9882CEC39F474329A17181117E73804E891F7FEA254F0F61EE08C13649A7B4)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

In this example, the source pattern's position and size are defined in absolute coordinates, while the pattern content's position and size are relative to the pattern itself. The horizontal coordinates are multiplied by the bounding box width, and the vertical coordinates are multiplied by the bounding box height.

<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1" patternUnits="userSpaceOnUse" x="10" y="10" width="100" height="100" patternContentUnits="objectBoundingBox" >
      <rect x="0" y="0" width="0.25" height="0.25" fill="red" opacity="0.5" />
      <rect x="0.25" y="0.25" width="0.25" height="0.25" fill="blue" opacity="0.5" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200"  stroke="red" stroke-width="2" fill="url(#pattern1)"/>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/wIP-dY1-SRykZ86GJp3j4A/en-us_image_0000002537925704.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4918BAE1535A08305E9D770F5CE32B18BCC1B9B79FF82E61C5A1E9AE94F254C1) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/sSWYCoBpQ92Fb5S1UvYQsg/en-us_image_0000002568685481.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53FAE558EE8E7C534700D084AAD8B0F1F61F4005BF0F4CAF2E15A387EBAB300F) |

## Filter Unit and Primitive Unit Parsing

Parsing [filterUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) and [primitiveUnits](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) is supported. Processing is added for the scenario where **filterUnits** and **primitiveUnits** are set to **objectBoundingBox** (coordinate system relative to the bounding box of the applied element). Currently, the following primitives are supported: **feFlood**, **feOffset**, **feGaussianBlur**, **feBlood**, **feColorMatrix**, and **feComposite**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/au0VWUFhRDaA6MpLicYCeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=373433CBD1565924EBCA636B5028B8CC3D014039580F2681F8A4B1F0B2412D9F)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

Image source example: When the primitive value is **objectBoundingBox**, the standard deviation value (**stdDeviation**) of the X and Y axes of **feGaussianBlur** must be multiplied by the width and height of the bounding box of the filter graph. The x- and y- coordinates of filter primitive subregions are multiplied by the bounding box width and height relative to the upper left corner of the graphic, while the width and height parameters of filter primitive subregions are multiplied by the bounding box width and height respectively.

 <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg"> 
 <defs>
   <filter id="blend" primitiveUnits="objectBoundingBox">
     <feGaussianBlur in="SourceGraphic" stdDeviation="0.1, 0.1" x="25%" y="25%" width="50%" height="50%" />
   </filter>
 </defs>
 
 <g fill="none" stroke="blue" stroke-width="4">
    <rect width="200" height="200" fill="none"/>
    <line x2="200" y2="200"  stroke="blue" stroke-width="4" />
    <line x1="200" y2="200"  stroke="blue" stroke-width="4"/>
 </g>
 <circle fill="green" filter="url(#blend)" cx="100" cy="100" r="90"/>
 </svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/8M3T-mLbSD-HF0wrN2rmKg/en-us_image_0000002568765491.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8251D6602407B0B0C2B6F9FFF6EB0B8DFD45DDFE0D1190C3CD48D7F70CE01087) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/ehVRpnz8Tp-FvQMOTzC0Kg/en-us_image_0000002537765766.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2E6780336DFB4301E1913653DCCC93D8C1D3D474777E0EAC62DA77D0C3EC7A2) |

#### Enhanced Display Effects

The opacity attribute of the **<g>** (group) element takes effect for all nested child elements in the group. In addition, the following features are enhanced: processing for the **clip-path** rule in **<g>** tags, tiling effects and offset value processing for pattern elements, and translation and scaling effects for linear and radial gradients. The default behavior for abnormal mask and filter parameters is updated.

## Group Element Opacity

The **opacity** attribute applied to a **<g>** (group) element now affects all nested child elements within the group hierarchy.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/qpKNknKyTxef0RJrF6fizg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=916F6D187B6CB940625F6C24742F311EE2325FEF032524BF969C1CEF41A9F01A)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

The example source image contains two layers of nested group elements, with the semicircle created by the clipping path rendered at 40% opacity (0.4).

<svg  width="200" height="200" viewBox = "0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="myClip" clipPathUnits="userSpaceOnUse">
      <rect x="25" y="0" width="60" height="60" />
    </clipPath>
  </defs>
  <g opacity="0.4" clip-path="url(#myClip)"  fill="red"  > 
    <g >
    <circle cx="25" cy="25" r="25"  />
    </g>
  </g>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/b9LtUy6BQze2x-34EpqdRA/en-us_image_0000002537925706.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F86724B839DBACD563139A59457EED0AA43D7761D5F3F5537C27A636BC707C5B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Ojvrt_M0SWi9eZjTn_vBBA/en-us_image_0000002568685483.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B16B49B147F317D9F7536957F5412473EF18DF1699F27CB181359B0379AA0356) |

## Clipping Path Rule Processing in Group Elements

The processing of **clip-path** clipping rules within **<g>** elements has been enhanced.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/jss13U_gQNahd12Ly6uAfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42A289CF611343704E7BA1B7B5D73F5096465B82DAED6C1DD548136702D2D58E)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

The image source clipping path in the example is referenced in the **g** tag. The default clipping path rule is **nonzero**, and the filling rule in the path tag is **evenodd**. The filling rule of the left image is **evenodd**, and the filling rule of the right image is the default rule of the clipping path, that is, **nonzero**.

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <!-- Define the clipping path of the five-pointed star.- -->
  <defs>
    <clipPath id="heartClipPath" >
   <path d="M 100,10 L 40,198 L 190,78 L 10,78 L 160,198 Z" fill-rule="evenodd" /> 
    </clipPath>
  </defs>

  <!-- Apply the clipping path to the rectangle. -->
  <g opacity="0.4" clip-path="url(#heartClipPath)" >
  <rect x="0" y="0" width="200" height="200" fill="red"  />
  </g>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vejGPjd9TmaAwX7T6hoOqw/en-us_image_0000002568765493.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B78FDC7CEA0801692F7A9A04E7E32DE1B885A789D5866DD6D71F61E20F7CDDAD) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YTGQhKAEROS3fqCB_NuN1w/en-us_image_0000002537765768.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFFA66B20A122B006652FB72DA0BDC9F1661536B2D8CD541F2DEB8B0DA9A53F9) |

## Pattern Tiling Enhancement

[pattern](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) supports repeated tiling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/0dKO8yHcRZa0mtd6sjHijw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C62ADCA5BD268120B7518BD7EE7F157E42966A91AABE6C54A6CB4A523DD39BD7)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

Example:

  <svg width="210" height="210" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="pattern1"  x="0" y="0" width="0.5" height="0.5"  >
      <rect x="0" y="0" width="50" height="50" fill="red" />
      <rect x="50" y="50" width="50" height="50" fill="blue" />
    </pattern>
  </defs>
  <rect x="10" y="10" width="200" height="200" fill="url(#pattern1)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| 
No tiling

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/29KHwue4Tomd_fVZHWyMJQ/en-us_image_0000002537925708.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB98F9A49C67ABE5FD3C6F42250C22A31D02F0FD6F1CF593DA4DB27C9A22DDFF)

 | 

Proper tiling

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qnmMeekKROGCcVyKA0P_sw/en-us_image_0000002568685485.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59F3BC682678CCCE0E208D07D8A8DB4CF5064FCE14D82EF6DB808353F496E902)

 |

## Pattern Offset Handling

When pattern **x** and **y** parameters are non-zero, the entire pattern is now displayed instead of only the translated portion.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ROYUXD5lTRalUjt2mmXREg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E4569DF750E500FE1B2B7EDB53A5210062DD468C420EACF76823C0AD49547FB)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="40" height="40" fill="url(#pattern0\_0\_37)"/>
  <defs>
    <pattern id="pattern0\_0\_37" patternContentUnits="objectBoundingBox" x="0.5" width="1" height="1">
      <use xlink:href="#image0\_0\_37" transform="scale(0.00833333)"/>
    </pattern>
    <image id="image0\_0\_37" width="120" height="120" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAYAAAA5ZDbSAAAACXBIWXMAACE4AAAhOAFFljFgAAABZWlDQ1BEaXNwbGF5IFAzAAB4nHWQvUvDUBTFT6tS0DqIDh0cMolD1NIKdnFoKxRFMFQFq1OafgltfCQpUnETVyn4H1jBWXCwiFRwcXAQRAcR3Zw6KbhoeN6XVNoi3sfl/Ticc7lcwBtQGSv2AijplpFMxKS11Lrke4OHnlOqZrKooiwK/v276/PR9d5PiFlNu3YQ2U9cl84ul3aeAlN//V3Vn8maGv3f1EGNGRbgkYmVbYsJ3iUeMWgp4qrgvMvHgtMunzuelWSc+JZY0gpqhrhJLKc79HwHl4plrbWD2N6f1VeXxRzqUcxhEyYYilBRgQQF4X/8044/ji1yV2BQLo8CLMpESRETssTz0KFhEjJxCEHqkLhz634PrfvJbW3vFZhtcM4v2tpCAzidoZPV29p4BBgaAG7qTDVUR+qh9uZywPsJMJgChu8os2HmwiF3e38M6Hvh/GMM8B0CdpXzryPO7RqFn4Er/QfBIQM2AAAHoklEQVR4Ae2dT2wUVRjAv5kFW5RkV1uFxNhuYmIbTbrQgx7AlR7kYihcPGhsXALcbMQEgocm0AQPhoMkcqvETXowkQu2t3oobOGgB2B7oiZqiyER0pLdBKRN2B3fN8uQZXb+bLfzZt/7+v0S2jLbbZv9zfvee99731sDAkjN5lKPE5CzADIGQBos8a9GGph2sGh/NOzPt4STIlTgyupQftHvCYbXxc7ZXNpKwI9C6D5glMcyIG9WYNxLtOm+0DGX+7Jqwk2Wqw+GJaKscNZRyB13P/ac4M653GmownnRrFPA6EZKNMrvXkCHdTwL0dhyUS4w+mPAV2vZ/Pnal1DrczEsc8slQ8mowm7sk+0QXU3AaZZLipQ9SBYY9ojZhL+BIce2KrxsQoJHy1TBHIZpWbALGJKIbjdjio8ZYEgiMpBpsy79yFDDQsEMaVBwGhiqcAumDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmDgsmzhYgRG9nN2S2vwE9Hd2Q2vKifW1pbRmWVpehUFqAzYj2glHkF69/CCM79tqCg5j89xpM3r+2qWQbHVexeFBPxnoPCrn7n7XWZimUbsOxPy7aLZs6WgrGlnrp7VEY2N4DG+Hs0mXx7xegjHYhGuXODJwKDcfNMNZ7yP7sJxl/D0aH4sM7MP3gBkwt3wTdSGw5vOsMaEKUch2yqX77c6Hc2C8vra7AiZ6PxMCtBz5+9T27ny8/+Q/mH/0DuqDVNGnirSORynXAlpxN9jdcL5Rv2/21A/7uib6j8LPoHmT8HTLQRjC2Hqe1yWCi74jnda/wPdw9GHkkkYU2gnHELBOUNbJjT8N1bMUlEZa9vh8HeqqjheBm5rhR/R4vpldueF7HUbzsG2+jaCF4uGs3xAF2ARmPqReOov1oZR4eJ1oIfl9i3+smm+xruDZX9s98OZk0VVFeML6AcbaQgZcaW7BXH1yPX2hXAeUFD4jFgzhJbm28mcJSmjg+UDVM83Khi1SiNVGqTplYcEQkuQUz7YAFE4cFE4cFE4cFE0d5weUnj4FpHeUFh2WRomb+UWPeuZk5bjnmv7NZlBeMWaQ4JXtlrXo7uwKfg39f0IJEO9GiD56r21Uhm6LHdhyv/HQ9uGasKloIvhrTC1jbIN/4uz5IBq9mTS/fAFXRQvD0Sjy7GQs+kSJse26hrO5Gei0E+7WsqJm8f73hGm4ACBpkYbWEyhvotZkHT967DjLxu4m89mnVc/aO2hvntRGM+6JkjqaxysGLA12Dvs9RvfUi2ghGud9IKjNBSV4RIpvq8w3P+BzVWy+iVary+7szMC9hvunXesd6Dnlex5tt//y3WhSvaZeLPrpwMdJQbZeUerRebLl+G+0xkuhSmaidYEwlnvzzJ4gClHTyL++fhWUyXuANgZFEF7RcTZq8d23DZZ8oF8OsVzQIKpOZeqBuUsMLbZcLsd/cyNwYW6533rlb+WqF9aD1evCFFkMlLgxM+aQXL4VUDg6/4j9tUhGtBRdbrNP1G4njokLY7siRnXthVOFKBjdaC251s7nX5nYEB3B9v5+EYwvB53ece/NTabXKUaO14JHX9kArYLF30M2Bg7gw0diSF949Z9cJY0JEVbQ6wqEeDKcT/UehFTrNrbBjazJ0lQpb9IW7v9pHOeCig9dNUasr3mvfNLUzuVZAJbQ7Zcep5ouibNOZKjWbtECROMIOCs12ClOM8GUvjjSLNoKjFOtmvQek6SRaecEyxbrBefXZO5ebFo3JkLGeg4Fnh7RbtLKC4xTrhpJo5QS3U6yb9UpBwbhBIKggPG7RyghWSayb9Upx0p1hoqPIqYfRdsH4YmBm6DPxYqh8mAmyXtHDXYMiKfJJ6J4uPBhVFm0T3MxdrirrEd3M8YsyD0WNXTCeuTEqwrCOYt00KzpMMi5Z9ovMmYw9Z7EJxnQeboHJxngkUlw0IxozbzOZU77d0LGFH6QMvKTnop27d2bga5JyEeeQUsxN+22zraU9ZwJ/hgykCsa79rfBcbJi3Tii/bb7YF477mpJaYLtwzrfGVV+ZCwDXGnC0bMblHsh5v1c0gSH5WqpgwPJjEdVol92rPhITvmpFMHOEtpmZ2Rnc8cTY2p0WtLbBUh5z4ZscnP0uWFg2csJjy2+OOJ2ui58e4ApieWnUgSHVcRvFvy6KBxsxQWfskMcFkwcKYLjnuupigqvgxTB8w/1eV8hmahwdocUwTgVoP6WcWGoUj8sdbEBR5EHunZvumzW0tqK3XpVCNFav/soEw6PoonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgonDgomDgheBocoit2DimGBwCyaLcGsaFiwBQxMLiqZlwC1gSGJU4Za5VoE8MFS5YsJQviRi9RVgSGEYkF8dytdG0UYFDlsAJWBIYLuswDh+bQtG04lq7QKjP6LvHUen+PWzefDjofx5gyVrjyUcrgmXzv8N9zdsm80dr5hwWjyQAkYbMCwbLrmI4fXNnbO5dNWEM+LBz4FRHgMHyWIc5YTl5x4LeiKKFp/2WSbsEj8kY1mQfvpQGph2sIgfjFr2cdGqQHEbQL6EMyEf/ge9rhOytvtnwQAAAABJRU5ErkJggg=="/>
  </defs>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/7VJ7Yw38QDakvcgEZeuiBw/en-us_image_0000002568765495.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D7AED7E08F0A6CD910F8B7BDA5CA26337750C8F025DEFD6B3205BE4E11AA32B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/3e19_7XzRRuOp36Tm02WFQ/en-us_image_0000002537765770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=445D748F8CA4D937C92FD3E05559AECD40D8CDC0C97123769612A1BE6F2B3FED) |

## Linear Gradient

[linearGradient](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) supports translation and scaling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UpKfWr0jStyNpjEY14lcNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67856855FC334D35A5615472299C4E7289B2E1555A0C0E461A3CCBF87F38E93C)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <linearGradient id="grad1" x1="50%" y1="0%" x2="0%" y2="50%">
            <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1" />
            <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect x="115" y="15" width="170" height="110" fill="url(#grad1)" />
    <line x1="200" y1="15" x2="115" y2="70" stroke="black" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/gzhUwbCHT2ODpoCNRhOeSQ/en-us_image_0000002537925710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEC1115A80206A5B414DC8F6D6D99C1CF9448C4F73018F90C35DCFE53B2FC625) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/uDKdmKhbRqSgHEJTRErMjg/en-us_image_0000002568685487.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C49C9874826B2040C1E6B4F321473082B06564F07E787B20DB3A3B1CE035237) |

## Radial Gradient

[radialGradient](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) supports translation and scaling.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/rQ6FgKaKSyCP8_hybWbF7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5535E00C37F8912022EE360AC6BB110A344A2C78247D9538B2125D1C56B91825)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <defs>
        <radialGradient id="grad1" cx = "50%" cy="50%" r= "50%" fx="40%" fy="40%"  >
            <stop offset="0%" style="stop-color:rgb(255,255,255);
      stop-opacity:0" />
            <stop offset="100%" style="stop-color:rgb(0,0,255);stop-opacity:1" />
        </radialGradient>
    </defs>
    <rect x="10" y="10" width="100" height="80" fill="url(#grad1)" />
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/6cdHJTTBRgamZ0ApKhaEpg/en-us_image_0000002568765497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FBBDB280C9FFDA9511F9DF470414F543E5C75E606A38AC0ED4AA4CD21875FC9) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Yj-qD1NVRUm-MPLBVO_89g/en-us_image_0000002537765772.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=897E60886BA41A22449174164A73BE7F3CC73D88B650EB286F85AF84B0EAF5D1) |

## Default Mask Behavior for Invalid Parameters

The **x**, **y**, **width**, and **height** parameters of [mask](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) can be numbers, percentages, and decimals. When the parameters are assigned with incorrect types, the default value **{-10%, -10%, 120%, 120%}** is used instead of **0**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/iX8LRIL9RjecDJpUvqmzdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9A6EA73A2DE96F041896D1E1B2613DA5FC05B62C078128AC5D7E61917098B70)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <mask id="mask1" x="0%" y="0%" width="100" height="100" maskUnits="userSpaceOnUse" maskContentUnits="userSpaceOnUse">
      <circle cx="50" cy="50" r="50" fill="red" />
    </mask>
  </defs>
  <rect x="0" y="0" width="200" height="200" fill="blue" mask="url(#mask1)"/>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4SvhIvPUQxia7in_qQWMCw/en-us_image_0000002537925712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BB0BF68861DE605DFF6107BB41A13C0E7898ACEB0D44A76A6F175E892B49CAA) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/awY6oQyQRXuQDwNqoGCDVg/en-us_image_0000002568685489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CE45A6B883D16BD03A20879C27AA6816C3118908CFFD5AB14C8D48C323663FB) |

## Default Filter Behavior for Invalid Parameters

The **x**, **y**, **width**, and **height** parameters of [filter](#impact-of-enhanced-svg-tag-parsing-on-elements-and-attributes) can be numbers, percentages, and decimals. When the parameters are assigned with incorrect types, the default value **{-10%, -10%, 120%, 120%}** is used instead of **0**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/70F7xaUrTzC7OV6ZyMtf5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAFBEBED04CF819D65808B90B4171CFBAAA9C349F621B69B8D0092B058CC4F88)

The final display of SVG images is influenced by the **Image** component's **objectFit** value. All examples in this document use **'objectFit(ImageFit.Contain)'** to ensure complete and correct rendering. Configure **objectFit** appropriately based on actual display requirements.

<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" width="300" height="300">
  <defs>
    <filter id="blurMe" x="0%" y="0%" width="100%" height="100%">
      <feColorMatrix in="SourceGraphic" type = "hueRotate" values="180"/>
    </filter>
  </defs>
  <circle cx="60" cy="60" r="50" fill="blue" filter="url(#blurMe)"/>
</svg>

| Before Enhancement | After Enhancement |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Msdaop-KQQ-6SVgoJ9FiWA/en-us_image_0000002568765499.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CED3F78B4104B04ED6B475174A7B7193F9D2660132D90BB998C2E628C37B46B2) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/l-l2A_5lReyZNy9K20keug/en-us_image_0000002537765774.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A0A0B284A18FF3023573A619B4BC68D609C4719345CA220B171243AD2037451) |
