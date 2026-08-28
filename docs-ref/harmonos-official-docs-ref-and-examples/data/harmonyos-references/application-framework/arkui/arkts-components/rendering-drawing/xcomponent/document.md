# XComponent

**XComponent** provides a [surface](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines#overview) for graphics rendering and media data input into your view. You can customize the position and size of the surface as needed. For details, see [Native XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-xcomponent-guidelines).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/CAvuBjSaSxmosQOpk88HZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3416FB570D3F895C2DA405DB034A275BEAF7BC06A7E9A5922BC44E15435CBE6C)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

#### \[h2\]XComponent19+

XComponent(params: NativeXComponentParameters)

Obtains an **XComponent** node instance on the native side, and registers the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events, such as touch, mouse, and key events.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [NativeXComponentParameters](#nativexcomponentparameters19) | Yes | Options of the **XComponent**. |

#### \[h2\]XComponent12+

XComponent(options: XComponentOptions)

Creates an **XComponent** component, allowing you to obtain the **SurfaceId** value on the ArkTS side, register the lifecycle callbacks for the surface held by the **XComponent** and the callbacks for component events such as touch, mouse, and key events, and configure the AI analyzer feature.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [XComponentOptions](#xcomponentoptions12) | Yes | Options of the **XComponent**. |

#### \[h2\]XComponent10+

XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})

Creates an **XComponent** component, whose lifecycle callbacks can be triggered from the native side.

This API is deprecated since API version 12. You are advised to use [XComponent(options: XComponentOptions)](#xcomponent12) instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Unique ID of the component. The value can contain a maximum of 128 characters. |
| type | [XComponentType](../../common-definitions/enums/document.md#xcomponenttype10) | Yes | Type of the component. |
| libraryname | string | No | Name of the dynamic library compiled and output by the native layer (the corresponding dynamic library does not support cross-module loading). This parameter is effective only when **type** is **SURFACE** or **TEXTURE**. |
| controller | [XComponentController](#xcomponentcontroller) | No | Controller bound to the component, which can be used to invoke methods of the component. This parameter is effective only when **type** is **SURFACE** or **TEXTURE**. |

#### \[h2\]XComponent(deprecated)

XComponent(value: {id: string, type: string, libraryname?: string, controller?: XComponentController})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/lp9_7zv9QdmBo3IiK8BDSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59B5F1C14335C25898DCD45699B0311F79DDA26ED8C83A2B47CE50695A165881)

This API is supported since API version 8 and deprecated since API version 12. You are advised to use [XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})](#xcomponent10) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | Unique ID of the component. The value can contain a maximum of 128 characters. |
| type | string | Yes | 
Type of the component. The options are as follows:

\- **"surface"**: The custom content is displayed individually on the screen. This option is used for displaying EGL/OpenGL ES and media data.

\- **"component"**9+: The component acts a container where non-UI logic can be executed to dynamically load and display content.

Any other value is handled as **"surface"**.

 |
| libraryname | string | No | Name of the dynamic library compiled and output by the native layer (the corresponding dynamic library does not support cross-module loading). This parameter is effective only when **type** is **"surface"**. |
| controller | [XComponentcontroller](#xcomponentcontroller) | No | Controller bound to the component, which can be used to invoke methods of the component. This parameter is valid only when the component type is **"surface"**. |

#### XComponentOptions12+

Defines the options of the **XComponent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [XComponentType](../../common-definitions/enums/document.md#xcomponenttype10) | No | No | Type of the component. |
| controller | [XComponentController](#xcomponentcontroller) | No | No | Controller bound to the component, which can be used to invoke methods of the component. This parameter is effective only when **type** is **SURFACE** or **TEXTURE**. |
| imageAIOptions | [ImageAIOptions](../../images-and-videos/image-analysis-types/document.md#imageaioptions12) | No | Yes | AI analysis options. You can configure the analysis type or bind an analyzer controller through this parameter. |

#### NativeXComponentParameters19+

Defines the options of the **XComponent**. An XComponent created with such constructor parameters can pass its corresponding [FrameNode](../../../arkts-api/ui/arkui/framenode/document.md) object to the Native side, enabling the use of NDK APIs for surface lifecycle–related settings and [component event listening](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-listen-to-component-events).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [XComponentType](../../common-definitions/enums/document.md#xcomponenttype10) | No | No | Type of the component. |
| imageAIOptions | [ImageAIOptions](../../images-and-videos/image-analysis-types/document.md#imageaioptions12) | No | Yes | AI analysis options. You can configure the analysis type or bind an analyzer controller through this parameter. |

#### Attributes

In addition to universal attributes, the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/s1y9AtsEQd67eD3FiiI4hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=229A333B1DF47E219DB8A7DBB0C066CDC8D4C6A2F1178DBF463A5A7F56A0D815)

The **foregroundColor**, **obscured**, and **pixelStretchEffect** attributes are not supported. In API version 17 and earlier versions, when **type** is set to **SURFACE**, dynamic attribute setting, custom drawing, background setting (except **backgroundColor**), image effect (except **shadow**), **maskShape**, and **foregroundEffect** attributes are also not supported. Starting from API version 18, the following dynamic attributes are not supported for **type** set to **SURFACE**: **background**, **foregroundColor**, **animation**, **gesture**, **priorityGesture**, **parallelGesture**, **useEffect**, **renderGroup**, **flexGrow**, **direction**, **align**, **useSizeType**, **clip**, **geometryTransition**, **bindPopup**, **bindMenu**, **bindContextMenu**, **bindContentCover**, **bindSheet**, **stateStyles**, **restoreId**, **onVisibleAreaChange**, **accessibilityGroup**, **obscured**, **reuseId**, and **accessibilityVirtualNode**.

For the **XComponent** component of the TEXTURE or SURFACE type, if the [renderFit](../../universal-attributes/visual-effects/render-fit/document.md#renderfit) attribute is not set, it defaults to **RenderFit.RESIZE\_FILL**.

For the **XComponent** of the **SURFACE** type with an opaque black background color: In versions earlier than API version 18, the [renderFit](../../universal-attributes/visual-effects/render-fit/document.md#renderfit18) attribute only supports **RenderFit.RESIZE\_FILL**; since API version 18, the **renderFit** attribute supports all its available enum values.

For the **XComponent** component created using the [ArkUI NDK API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-access-the-arkts-page), the [getAttribute](../../../c-api/structs/arkui-nativenodeapi-1/document.md#getattribute) function is not supported for obtaining the **renderFit** attribute value.

#### \[h2\]enableAnalyzer12+

enableAnalyzer(enable: boolean)

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup.

For the settings to take effect, this attribute must be used together with [StartImageAnalyzer](#startimageanalyzer12) and [StopImageAnalyzer](#stopimageanalyzer12) of **XComponentController**.

This feature cannot be used together with the [overlay](../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) attribute. If they are set at the same time, the **CustomBuilder** attribute in **overlay** has no effect. This feature depends on device capabilities.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the AI image analyzer.

**true**: enable; **false**: disable

Default value: **false**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/15CFBBqqRdumdg5heEleHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D360F608D35BA842CAF246FBCDF17BB2BB0F487778F11EA40098986FB158A9C8)

This API has effect only when **type** is set to **SURFACE** or **TEXTURE**.

#### \[h2\]enableSecure13+

enableSecure(isSecure: boolean)

Sets whether to enable the secure surface to protect the content rendered within the component from being captured or recorded.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isSecure | boolean | Yes | 
Whether to enable the secure surface.

The value **true** means to enable the secure surface, and **false** means the opposite.

Default value: **false**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/mecxjxdHQ1aLPIF45NBEmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1555D80338D69C310D0DC4BEAD7874DFAA3C05F71698AC86F0B12AE58B4F531)

This attribute is effective only when **type** is set to **SURFACE**.

It is not supported for **XComponent** components created using the [ArkUI NDK API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-build-ui-overview).

#### \[h2\]hdrBrightness20+

hdrBrightness(brightness: number)

Sets the brightness of HDR video playback for the component.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | 
Brightness of HDR video playback.

Value range: 0.0 to 1.0. Values less than 0.0 are equivalent to 0.0, and values greater than 1.0 are equivalent to 1.0. **0.0** indicates the brightness of the SDR video, and **1.0** indicates the brightness of the HDR video.

Default value: **1.0**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/vrYNyH_0Rhy9NpjNNH0fdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6FEC4D7A625A3105963ACE7B7D84C358991F047D5B3371C54AE84617895553F)

This attribute is effective only when **type** is set to **SURFACE**.

It is not supported for **XComponent** components created using the [ArkUI NDK API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ndk-build-ui-overview).

#### Events

Since API version 12, the [universal events](../../universal-events/document.md) are supported when **type** is set to **SURFACE** or **TEXTURE**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/5RkONZvfQ5-xpzmOuwlPVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=717BD05DCB54223AD9C6894C14F6775938E12711BD6887D8E5F8C0792B4A37D9)

When the **libraryname** parameter is set, [click events](../../universal-events/interaction-response-events/click-event/document.md), [touch events](../../universal-events/basic-input-events/touch-event/document.md), [show/hide events](../../universal-events/component-change-events/show-hide-event/document.md), [key events](../../universal-events/basic-input-events/key-event/document.md), [focus events](../../universal-events/interaction-response-events/focus-event/document.md), and [mouse events](../../universal-events/basic-input-events/mouse-event/document.md) only respond to event APIs on the C API side.

The following events are effective only when **type** is set to **SURFACE** or **TEXTURE**.

#### \[h2\]onLoad

onLoad(callback: OnNativeLoadCallback )

Triggered when the plugin is loaded.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnNativeLoadCallback](#onnativeloadcallback18) | Yes | Callback triggered after the surface held by **XComponent** is created. |

#### \[h2\]onDestroy

onDestroy(event: VoidCallback )

Triggered when the plugin is destroyed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [VoidCallback](../../common-definitions/basic-types/document.md#voidcallback12) | Yes | Callback triggered after **XComponent** is destroyed. |

#### OnNativeLoadCallback18+

type OnNativeLoadCallback = (event?: object) => void

Triggered after the surface held by **XComponent** is created.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | object | No | Context of the **XComponent** object. The APIs contained in the context are defined at the native layer by developers. |

#### XComponentController

Defines the controller of the **XComponent**. You can bind the controller to the **XComponent** to call the component APIs through the controller.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

A constructor used to create a **XComponentController** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

xcomponentController: XComponentController = new XComponentController();

#### \[h2\]getXComponentSurfaceId9+

getXComponentSurfaceId(): string

Obtains the ID of the surface held by the **XComponent**. This API works only when **type** of the **XComponent** is **SURFACE("surface")** or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the surface held by the **XComponent**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/IRnETeKBRoq-H54XbR2o6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18CEC713708190200F4D8E1824796A9B2E72C2C7A17E037892A2026119BF35A6)

When you create an **XComponent** using a custom component node, the **onLoad** callback is triggered before the [onSurfaceCreated](#onsurfacecreated12) callback. This means that calling [getXComponentSurfaceId](#getxcomponentsurfaceid9) in the **onLoad** callback will not return a valid **surfaceId**. You are advised to obtain the **surfaceId** in the [onSurfaceCreated](#onsurfacecreated12) callback instead.

**Example**

// xxx.ets
@Entry
@Component
struct Index {
  myXComponentController: XComponentController = new XComponentController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.myXComponentController
      })
        .onLoad(() => {
          let surfaceId: string = this.myXComponentController.getXComponentSurfaceId();
          console.info("XComponent SurfaceId: " + surfaceId);
        })
    }
  }
}

#### \[h2\]setXComponentSurfaceSize(deprecated)

setXComponentSurfaceSize(value: {surfaceWidth: number, surfaceHeight: number}): void

Sets the width and height of the surface held by the **XComponent**. This API works only when **type** of the **XComponent** is set to **SURFACE("surface")** or **TEXTURE**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/an_iOWGTSzm69cVSmsWODw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB0823E3EBC1C17F40EF82D01F6EB46427119B5C3F0890551DCBAA24D944170E)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [setXComponentSurfaceRect](#setxcomponentsurfacerect12) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceWidth | number | Yes | Width of the surface held by the **XComponent**. |
| surfaceHeight | number | Yes | Height of the surface held by the **XComponent**. |

#### \[h2\]getXComponentContext

getXComponentContext(): Object

Obtains the context of an **XComponent** object. This API works only when **type** of the **XComponent** is set to **SURFACE("surface")** or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Object | Context of the **XComponent** object. The APIs contained in the context are defined by developers. The context is passed as the first parameter of the **onLoad** callback. |

#### \[h2\]setXComponentSurfaceRect12+

setXComponentSurfaceRect(rect: SurfaceRect): void

Sets the display area for the surface held by the **XComponent**, including the width, height, and position coordinates relative to the upper left corner of the component. This API is only effective when the **XComponent** type is **SURFACE("surface")** or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rect | [SurfaceRect](#surfacerect12) | Yes | Rectangle of the surface held by the **XComponent**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/TEltVJPwTYudqEiS0q1_Tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3DDA75AF7E3CCBA2A7149E202215FCDE9FB29ED4E00030C941F1E9D3C6E1570)

If **offsetX** or **offsetY** in **rect** is not set or an abnormal value is passed, the offset effect of the surface display area relative to the x/y-axis of the **XComponent**'s upper-left corner defaults to center alignment.

If **surfaceWidth** and **surfaceHeight** in the **rect** parameter are set to **0**, negative numbers, or other abnormal values, the display area set by calling this API does not take effect. If this API is not called to set the display area of the surface, **surfaceWidth** defaults to the component width, and **surfaceHeight** defaults to the component height.

This API has a higher priority than attributes that can change the content offset and size, such as [border](../../universal-attributes/layout-and-borders/border-styling/document.md#border) and [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding).

#### \[h2\]getXComponentSurfaceRect12+

getXComponentSurfaceRect(): SurfaceRect

Obtains the display area for the surface held by the **XComponent**, including the width, height, and position coordinates relative to the upper left corner of the component. This API is only effective when the **XComponent** type is **SURFACE("surface")** or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [SurfaceRect](#surfacerect12) | Rectangle of the surface held by the **XComponent**. |

#### \[h2\]onSurfaceCreated12+

onSurfaceCreated(surfaceId: string): void

Triggered when the surface held by the **XComponent** is created. This API works only when **type** of the **XComponent** is set to **SURFACE("surface")** or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | ID of the surface held by the **XComponent**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/0yxysUBvQWaS02iuEoZKwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02B853EDBC35108CE69959201F3BD5A54EE43943D8A015F483F2DF6E0CBE0DD0)

The callback is triggered only when the **libraryname** parameter is not set for the **XComponent**.

#### \[h2\]onSurfaceChanged12+

onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void

Triggered when the surface held by the **XComponent** has its size changed (including the time when the **XComponent** is created with the specified size). This API works only when **type** of the **XComponent** is set to **SURFACE** (**"surface"**) or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | ID of the surface held by the **XComponent**. |
| rect | [SurfaceRect](#surfacerect12) | Yes | Area for displaying the surface held by the **XComponent**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/3IH9XBvwR9OBKBSRFiGhdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDEB6ED8D171FB757910C9776EAF02A020C044938A2CFF559486225A2C4426C5)

The callback is triggered only when the **libraryname** parameter is not set for the **XComponent**.

#### \[h2\]onSurfaceDestroyed12+

onSurfaceDestroyed(surfaceId: string): void

Triggered when the surface held by the **XComponent** is destroyed. This API works only when **type** of the **XComponent** is set to **SURFACE** (**"surface"**) or **TEXTURE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | ID of the surface held by the **XComponent**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/N_dZIB3CRE-uTtlrmCHG9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95E108F82C75FDC239D68B1E1B167ED602C4E64A4D381CA527D720D0E5170716)

The callback is triggered only when the **libraryname** parameter is not set for the **XComponent**.

#### \[h2\]startImageAnalyzer12+

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

Starts AI image analysis in the given settings. Before calling this API, make sure the AI image analyzer is [enabled](#enableanalyzer12). This API uses a promise to return the result.

Because the image frame used for analysis is the one captured when this API is called, pay attention to the invoking time of this API.

If this API is repeatedly called before the execution is complete, an error callback is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/e36lllMgTeyK4gMvbM7HdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04524FDCEFE50FF5D52526807DD361F2C28185D5043FE432D508A3EBDCC382F4)

The image analysis type cannot be dynamically modified.

This API depends on device capabilities. If it is called on an incompatible device, an error code is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [ImageAnalyzerConfig](../../images-and-videos/image-analysis-types/document.md#imageanalyzerconfig12) | Yes | Settings of the AI image analyzer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. It is used to indicate AI-based analysis is successfully executed. |

**Error codes**

For details about the error codes, see [AI Image Analyzer Error Codes](../../../error-codes/ui/ai-image-analyzer-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

#### \[h2\]stopImageAnalyzer12+

stopImageAnalyzer(): void

Stops AI image analysis. The content displayed by the AI image analyzer will be destroyed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/UOnYE9OVRduzAGkWr1z4Uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C721499288959ADA4F65952CF8EE0B33C683BB25EEC5F603F9F8D700F0921B)

If this API is called when the **startImageAnalyzer** API has not yet returned any result, an error callback is triggered.

This feature depends on device capabilities.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]setXComponentSurfaceRotation12+

setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void

Sets whether to lock the orientation of the surface held by this **XComponent** when the screen rotates. This API is effective only when the **XComponent** type is **SURFACE** (**"surface"**).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationOptions | [SurfaceRotationOptions](#surfacerotationoptions12) | Yes | Whether to lock the orientation of the surface held by the current **XComponent** when the screen rotates. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/nhIfG8yMTkm_BC8wYuekkg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D96205C621F1DEF27B14B732876DE7D7FEAEA71F4BD16849CE11872AEBAE1F)

If **rotationOptions** is not set, the surface held by this **XComponent** rotates with the screen by default.

The orientation lock is only applied during the rotation process and is released once the rotation is complete.

The setting takes effect only when the screen is rotated by 90°, that is, when it switches between landscape and portrait modes.

Make sure the width and height of **Buffer** remain unchanged after locking the orientation to prevent distortion.

#### \[h2\]getXComponentSurfaceRotation12+

getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>

Obtains whether the orientation of the surface held by this **XComponent** is locked when the screen rotates. This API is effective only when the **XComponent** type is **SURFACE** (**"surface"**).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Required<[SurfaceRotationOptions](#surfacerotationoptions12)\> | Whether the orientation of the surface held by the current **XComponent** is locked when the screen rotates. |

#### \[h2\]lockCanvas20+

lockCanvas(): DrawingCanvas | null

Obtains a canvas object for drawing content on the **XComponent** component. For details about the drawing methods, see [Canvas](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-canvas/document.md).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DrawingCanvas](../../canvas-drawing/drawingrenderingcontext/document.md#drawingcanvas12) | null | Canvas object for drawing on the **XComponent** area, or **null** if it is unavailable. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/DB5lT9g3T16cLEyTorIwNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F51875D5171F039BCA3273761BE3393E958CE8A86653776DEC71B67CFBA964F8)

This API returns **null** if the canvas object cannot be obtained due to the current state of the **XComponent** component. The possible causes are as follows:

1.  The surface held by the **XComponent** has not been created yet (you can determine this by setting the [onLoad](#onload) or [onSurfaceCreated](#onsurfacecreated12) callback, which is triggered after the surface is created).
    
2.  A previous canvas object obtained using **lockCanvas()** has not been released with [unlockCanvasAndPost](#unlockcanvasandpost20).
    

This API is only effective when the **XComponent** type is **TEXTURE** or **SURFACE**.

After using this API, do not simultaneously obtain the **NativeWindow** instance on the NDK side and call related APIs for drawing. Doing so may cause buffer contention and context to occur, leading to rendering exceptions such as visual artifacts.

This API must be used in conjunction with [unlockCanvasAndPost](#unlockcanvasandpost20). For the implementation example, see [Example 3: Drawing Content on the XComponent Using a Canvas Object](#example-3-drawing-content-on-the-xcomponent-using-a-canvas-object).

#### \[h2\]unlockCanvasAndPost20+

unlockCanvasAndPost(canvas: DrawingCanvas): void

Submits the drawn content from a canvas object to the display area of the **XComponent** component and releases the canvas object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| canvas | [DrawingCanvas](../../canvas-drawing/drawingrenderingcontext/document.md#drawingcanvas12) | Yes | Canvas object previously obtained using **lockCanvas()**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Klm53s5ITLmjoq6hoW3L6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=691D921BA13748F72C69537D1A3FE5ABEAF728F1A0512415B173A35C7FE8D163)

1.  Once released using **unlockCanvasAndPost()**, a canvas object becomes immediately unusable.
    
2.  This API is only effective when the **XComponent** type is **TEXTURE** or **SURFACE**.
    
3.  After using this API, do not simultaneously obtain the **NativeWindow** instance on the NDK side and call related APIs for drawing. Doing so may cause buffer contention and context to occur, leading to rendering exceptions such as visual artifacts.
    
4.  This API must be used in conjunction with [lockCanvas](#lockcanvas20). For the implementation example, see [Example 3: Drawing Content on the XComponent Using a Canvas Object](#example-3-drawing-content-on-the-xcomponent-using-a-canvas-object).
    

#### \[h2\]setXComponentSurfaceConfig22+

setXComponentSurfaceConfig(config: SurfaceConfig): void

Sets the options of the surface created by the **XComponent**, which determine whether the surface held by the **XComponent** is considered opaque during rendering.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/5PTf65FSQrKkUok7Q4ONsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=715CA1C735B15849E166387580F2826FFEC8928D45CB7C1C6D1565764BF9AFD5)

This API takes effect only when the type of **XComponent** is **TEXTURE** or **SURFACE**.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [SurfaceConfig](#surfaceconfig22) | Yes | Surface options. |

#### SurfaceRotationOptions12+

Defines whether the orientation of the surface held by the current **XComponent** is locked when the screen rotates.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| lock | boolean | No | Yes | 
Whether the orientation of the surface is locked when the screen rotates. If this parameter is not set, the default value **false** is used, indicating that the orientation is not locked.

**true**: The orientation of the surface is locked when the screen rotates.

**false**: The orientation of the surface is not locked when the screen rotates.

 |

#### SurfaceRect12+

Describes the rectangle of the surface held by the **XComponent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| offsetX | number | No | Yes | 
X-coordinate of the surface rectangle relative to the upper-left corner of the **XComponent**.

Unit: px

 |
| offsetY | number | No | Yes | 

Y-coordinate of the surface rectangle relative to the upper left corner of the **XComponent**.

Unit: px

 |
| surfaceWidth | number | No | No | 

Width of the surface rectangle.

Unit: px.

 |
| surfaceHeight | number | No | No | 

Height of the surface rectangle.

Unit: px.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/6UiJMYzPQYyD3YoDUhPOFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C456A88CB12B0605F95DA0412D7CF18F41780A4C6C165C555894B340D8575747)

The **surfaceWidth** and **surfaceHeight** attributes default to the size of the **XComponent** if the [setXComponentSurfaceRect](#setxcomponentsurfacerect12) API is not called and neither [border](../../universal-attributes/layout-and-borders/border-styling/document.md#border) nor [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) is set.

Make sure the values of **surfaceWidth** and **surfaceHeight** do not exceed 8192 px. Exceeding this limit may lead to rendering issues.

In immersive scenarios, the default layout of **SurfaceRect** does not include the safe area. To achieve an immersive effect, you must set the surface display area using the [setXComponentSurfaceRect](#setxcomponentsurfacerect12) API.

#### SurfaceConfig22+

Describes whether the surface held by the **XComponent** is treated as opaque during rendering.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isOpaque | boolean | No | Yes | 
Whether the surface held by the **XComponent** is treated as opaque during rendering. If this attribute is not set, the default value **false** is used, indicating that the transparency of the pixels in the content drawn on the surface will be applied during rendering.

**true**: yes; **false**: no

Default value: **false**.

 |

#### Example

You can preview how this component looks on a real device, but not in DevEco Studio Previewer.

## Example 1: Enabling AI Image Analyzer

This example shows how to use the **enableAnalyzer** attribute to enable the AI image analyzer. You can use **XComponentController** to start or stop AI analysis on images.

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import nativeRender from 'libnativerender.so';// Your own .so file implementation (see above for details).

class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(\`onSurfaceCreated surfaceId: ${surfaceId}\`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(\`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}\`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(\`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct XComponentExample {
  xComponentController: XComponentController = new CustomXComponentController();
  private config: ImageAnalyzerConfig = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\]
  };
  private aiController: ImageAnalyzerController = new ImageAnalyzerController();
  private options: ImageAIOptions = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\],
    aiController: this.aiController
  };
  @State xcWidth: string = "720px";
  @State xcHeight: string = "720px";
  @State currentStatus: string = "index";

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('Native XComponent Sample')
          .fontSize('24fp')
          .fontWeight(500)
          .margin({
            left: 24,
            top: 12
          })
      }
      .margin({ top: 24 })
      .width('100%')
      .height(56)

      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentController,
        imageAIOptions: this.options
      })
        .width(this.xcWidth)
        .height(this.xcHeight)
        .enableAnalyzer(true)
        .onClick(() => {
          let surfaceId = this.xComponentController.getXComponentSurfaceId();
          nativeRender.ChangeColor(BigInt(surfaceId));
          let hasChangeColor: boolean = false;
          if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
            hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
          }
          if (hasChangeColor) {
            this.currentStatus = "change color";
          }
        })
      Text(this.currentStatus)
        .fontSize('24fp')
        .fontWeight(500)
      Column() {
        Button('start AI analyze')
          .onClick(() => {
            this.xComponentController.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete");
              })
              .catch((error: BusinessError) => {
                console.error("error code: " + error.code);
              })
          })
          .margin(2)
        Button('stop AI analyze')
          .onClick(() => {
            this.xComponentController.stopImageAnalyzer();
          })
          .margin(2)
        Button('get analyzer types')
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes();
          })
          .margin(2)
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .margin({ bottom: 24 })
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            console.info(\`surface rect is ${this.xComponentController.getXComponentSurfaceRect()}\`);
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .margin(2)
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%")
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/pCHY_AUMQTeLntMMy4Te0g/en-us_image_0000002537925830.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF462E64381AB66BCB6D64A66C0CA6827CBF69D1C01F2818991C60F0AA72428A)

## Example 2: Locking the Surface Orientation During Screen Rotation

This example shows how to use **setXComponentSurfaceRotation** to lock the surface orientation during screen rotation so that the surface does not rotate with the screen.

// xxx.ets
import nativeRender from 'libnativerender.so';

class MyXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    console.info(\`onSurfaceCreated surfaceId: ${surfaceId}\`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }

  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(\`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}\`);
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }

  onSurfaceDestroyed(surfaceId: string): void {
    console.info(\`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State isLock: boolean = true;
  @State xc\_width: number = 500;
  @State xc\_height: number = 700;
  myXComponentController: XComponentController = new MyXComponentController();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
      XComponent({
        id: "XComponent",
        type: XComponentType.SURFACE,
        controller: this.myXComponentController
      })
        .onLoad(() => {
          let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };
          this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation);
          console.info("Surface getXComponentSurfaceRotation lock = " +
          this.myXComponentController.getXComponentSurfaceRotation().lock);
        })
        .width(this.xc\_width)
        .height(this.xc\_height)
      Button("Draw")
        .onClick(() => {
          let surfaceId = this.myXComponentController.getXComponentSurfaceId();
          nativeRender.DrawPattern(BigInt(surfaceId));
        })
    }
  }
}

## Example 3: Drawing Content on the XComponent Using a Canvas Object

From API version 20, this example demonstrates how to return a canvas object by calling [lockCanvas](#lockcanvas20), call the corresponding drawing API via the canvas object, and then call [unlockCanvasAndPost](#unlockcanvasandpost20) to draw content on the **XComponent**.

// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("80%")
        .height("80%")
        .onLoad(() => {
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 240, 250, 255); // Before each drawing operation, the entire XComponent area must be fully redrawn. This API can be used to achieve this.
            const brush = new drawing.Brush(); // Create a brush object.
            brush.setColor({ // Set the color of the brush.
              alpha: 255,
              red: 39,
              green: 135,
              blue: 217
            });
            this.mCanvas.attachBrush(brush); // Attach the brush to the canvas.
            this.mCanvas.drawRect({ // Draw a rectangle.
              left: 300,
              right: 800,
              top: 100,
              bottom: 800
            });
            this.mCanvas.detachBrush(); // Detach the brush from the canvas.
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/6IUZ5aCzSlWFbvBz_hTmzw/en-us_image_0000002568685607.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FEE8F5773E2F934BA17FB7D805F0B63AF14BBE89239DB51E17DE7C91E6589B4)

## Example 4: Implementing an Immersive Effect

From API version 20, building upon Example 3, the **setXComponentSurfaceRect** API is called to set the surface area to achieve an immersive effect.

// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';
import { display } from '@kit.ArkUI'
@Entry
@Component
struct Index {
  private xcController: XComponentController = new XComponentController();
  private mCanvas: DrawingCanvas | null = null;
  @State screenWidth: number = 0;
  @State screenHeight:number = 0;
  aboutToAppear() {
    try {
      const displayClass = display.getDefaultDisplaySync();
      this.screenWidth = displayClass.width;
      this.screenHeight = displayClass.height;
    } catch (error) {
      console.error(\`Failure code: ${error.code}, message: ${error.message}\`);
    }
  }

  build() {
    Column() {
      XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
        .width("100%")
        .height("100%")
        .onLoad(() => {
          // Set the surface size. If the size is too large, the drawing time may be long.
          this.xcController.setXComponentSurfaceRect({surfaceWidth: this.screenWidth, surfaceHeight: this.screenHeight, offsetX: 0, offsetY: 0});
          this.mCanvas = this.xcController.lockCanvas();
          if (this.mCanvas) {
            this.mCanvas.drawColor(255, 39, 135, 217); // Before each drawing operation, the entire XComponent area must be fully redrawn. This API can be used to achieve this.
            this.xcController.unlockCanvasAndPost(this.mCanvas);
          }
        })
        .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM\]);
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/TQ1_PDqkReuTK1sBfVDeHg/en-us_image_0000002568765617.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=113BA9CBFB857E720BBA2EFCB18D2B4861D1F1CDCAE35EB9BDB0A4019E4DD7CF)

## Example 5 Setting Whether the Surface Held by XComponent Needs to Be Treated as Opaque During Rendering

In API version 22 and later versions, this example calls the [setXComponentSurfaceConfig](#setxcomponentsurfaceconfig22) API to set whether the surface held by the **XComponent** is treated as opaque during rendering.

// xxx.ets
import nativeRender from 'libnativerender.so'; // Your own .so file implementation (see above for details).

// Override XComponentController to set lifecycle callbacks.
class MyXComponentController extends XComponentController{
  onSurfaceCreated(surfaceId: string): void {
    console.info(\`onSurfaceCreated surfaceId: ${surfaceId}\`);
    nativeRender.SetSurfaceId(BigInt(surfaceId));
  }
  onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
    console.info(\`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}}\`);
    // Call ChangeSurface to draw content in onSurfaceChanged.
    nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
  }
  onSurfaceDestroyed(surfaceId: string): void {
    console.info(\`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
    nativeRender.DestroySurface(BigInt(surfaceId));
  }
}

@Entry
@Component
struct Index {
  @State currentStatus: string = "index";
  xComponentController: XComponentController = new MyXComponentController();

  aboutToAppear(): void {
    // Set the surface held by XComponent to be opaque during rendering.
    this.xComponentController.setXComponentSurfaceConfig({ isOpaque: true });
  }

  build() {
    Column() {
      Column({ space: 10 }) {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .backgroundColor(Color.Transparent)
        Text(this.currentStatus)
          .fontSize('24fp')
          .fontWeight(500)
      }
      .onClick(() => {
        let surfaceId = this.xComponentController.getXComponentSurfaceId();
        nativeRender.ChangeColor(BigInt(surfaceId));
        let hasChangeColor: boolean = false;
        if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
          hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
        }
        if (hasChangeColor) {
          this.currentStatus = "change color";
        }
      })
      .margin({
        top: 27,
        left: 12,
        right: 12
      })
      .height('40%')
      .width('90%')
      Row() {
        Button('Draw Star')
          .fontSize('16fp')
          .fontWeight(500)
          .margin({ bottom: 24 })
          .onClick(() => {
            let surfaceId = this.xComponentController.getXComponentSurfaceId();
            nativeRender.DrawPattern(BigInt(surfaceId));
            let hasDraw: boolean = false;
            if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
              hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
            }
            if (hasDraw) {
              this.currentStatus = "draw star";
            }
          })
          .width('53.6%')
          .height(40)
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/nJ_k6W2PR4aXE7xi2xgiYg/en-us_image_0000002537765892.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18C87D3CC12E7C4184DB316487A489B97532823C83DCC2E8B5DE51FAD6E4213C)
