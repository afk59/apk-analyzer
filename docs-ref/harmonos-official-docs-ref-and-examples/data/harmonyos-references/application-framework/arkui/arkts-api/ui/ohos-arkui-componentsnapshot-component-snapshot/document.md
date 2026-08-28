# @ohos.arkui.componentSnapshot (Component Snapshot)

The **componentSnapshot** module provides APIs for obtaining component snapshots, including snapshots of components that have been loaded and snapshots of components that have not been loaded yet. Snapshots are strictly limited to the component's layout bounds. Content drawn outside the area of the owning component or the parent component is not visible in the snapshots. In addition, sibling components stacked in the component's area are not displayed in the snapshot.

Transformation attributes such as scaling, translation, and rotation only apply to the child components of the target component. Applying these transformation attributes directly to the target component itself has no effect; the snapshot will still display the component as it appears before any transformations are applied.

For typical use cases (for example, long screenshots) and best practices of component snapshots, see [Using Component Snapshot (ComponentSnapshot)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-uicontext-component-snapshot).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/UrmbnbZ4TjGn2XYR19OkpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92474F8A36554E8C15C2A8CC68C7858FA5BA4926E87EF6109E8085FFA4CAE8AC)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   In scenarios where [XComponent](../../../arkts-components/rendering-drawing/xcomponent/document.md) is used to, for example, display video or camera streams, obtain images through [createPixelMapFromSurface](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/functions/document.md#imagecreatepixelmapfromsurface11), instead of through an API in this module.
    
-   If the content of a component does not fill the entire area allocated for it, any remaining space in the snapshot will be rendered as transparent pixels. In addition, if the component uses [image effects](../../../arkts-components/universal-attributes/visual-effects/image-effect/document.md) or other effect-related attributes, the resulting snapshot may not be as expected. To address these potential issues, check whether to fill the component's transparent content area or to use an alternative method such as taking a [window screenshot](../../window-manager/ohos-window-window/interface-window/document.md#snapshot9).
    
-   You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
    

#### Modules to Import

import { componentSnapshot } from '@kit.ArkUI';

#### componentSnapshot.get(deprecated)

get(id: string, callback: AsyncCallback<image.PixelMap>, options?: SnapshotOptions): void

Obtains the snapshot of a component that has been loaded based on the provided [component ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md). This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/OHz1EuQQSuCE3hTRbDZKvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC3CE6F9602ACF4335995BD6D2BAF3615F955EC53778867843FD60AF74E31FCD)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [get](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md#get12) instead. Before calling this API, you need to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object using the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object associated with the current UI context.
    
-   The snapshot captures content rendered in the last frame. If this API is called when the component triggers an update, the re-rendered content will not be included in the obtained snapshot.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target component. |
| callback | [AsyncCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Yes | Callback used to return the result. |
| options12+ | [SnapshotOptions](#snapshotoptions12) | No | Custom settings of the snapshot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/8Uha9uz-T_-f_NE0RM0mWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4A86E1DA93A17ABF616D5CF228895341B612BCAFB5B01EFD1B5CBF5F0C0E4FD)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // Replace $r('app.media.img') with the image resource file you use.
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().get().
          componentSnapshot.get("root", (error: Error, pixmap: image.PixelMap) => {
            if (error) {
              console.error(\`error:${JSON.stringify(error)}\`)
              return;
            }
            this.pixmap = pixmap
          }, { scale: 2, waitUntilRenderFinished: true })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/o1tBtRMESzex0pJJBeo1nw/en-us_image_0000002568685031.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5654F10F7C84127317509F9E04C100210F2F31B03B8E44EEF7B9897DFE3E777)

#### componentSnapshot.get(deprecated)

get(id: string, options?: SnapshotOptions): Promise<image.PixelMap>

Obtains the snapshot of a component that has been loaded based on the provided [component ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md). This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Ab4S-Tg9Qi6sLLPttO14SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4B2A6D045864E517EAE570618F4A8615067521E85ED7735B2954FC99E06F564)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [get](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md#get12-1) instead. Before calling this API, you need to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object using the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object associated with the current UI context.
    
-   The snapshot captures content rendered in the last frame. If this API is called when the component triggers an update, the re-rendered content will not be included in the obtained snapshot.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target component. |
| options12+ | [SnapshotOptions](#snapshotoptions12) | No | Custom settings of the snapshot. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/8D976gkCQkWzu9fr5xKj_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDFFE7BE6044941AA44ABCEA43DD0FBF408E00B66ABF8BB154A910376D1CB765)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // Replace $r('app.media.img') with the image resource file you use.
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().get().
          componentSnapshot.get("root", { scale: 2, waitUntilRenderFinished: true })
            .then((pixmap: image.PixelMap) => {
              this.pixmap = pixmap
            }).catch((err: Error) => {
            console.error(\`error:${err}\`)
          })
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/queJUQn0TLCrp9h3m_5AyQ/en-us_image_0000002568685031.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=970460BE3486BE6DF00B3870C7FD8AC8990C5A4D9102C9491C7929976C4BF109)

#### componentSnapshot.createFromBuilder(deprecated)

createFromBuilder(builder: CustomBuilder, callback: AsyncCallback<image.PixelMap>, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): void

Renders a custom component in the application background and outputs its snapshot. This API uses an asynchronous callback to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/IDWW9PUPTaK9K4eawrLlog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F4428E93D5C7A7C7C0E53B446664D8B02F342B9C139F1A2FD0B5D08821E1BE0)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [createFromBuilder](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md#createfrombuilder12) instead. Before calling this API, you need to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object using the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object associated with the current UI context.
    
-   To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots has a delay of less than 500 ms.
    
-   Components in the builder do not support the setting of animation-related attributes, such as [transition](../../../arkts-components/animation/component-transition-transition/document.md).
    
-   If a component is on a time-consuming task, for example, an [Image](../../../arkts-components/images-and-videos/image/document.md) or [Web](../../../../arkweb/arkts-components/web/components/document.md) component that is loading online images, its loading may be still in progress when this API is called. In this case, the output snapshot does not represent the component in the way it looks when the loading is successfully completed.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | Yes | 
Builder of the custom component.

Note: The global builder is not supported.

If the root component of the builder has a width or height of zero, the snapshot operation will fail with error code 100001.

 |
| callback | [AsyncCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Yes | Callback used to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback. |
| delay12+ | number | No | 

Delay time for triggering the screenshot command. When the layout includes an image component, it is necessary to set a delay time to allow the system to decode the image resources. The decoding time is subject to the resource size. In light of this, whenever possible, use pixel map resources that do not require decoding.

When pixel map resources are used or when **syncLoad** to **true** for the **Image** component, you can set **delay** to **0** to forcibly capture snapshots without waiting. This delay time does not refer to the time from the API call to the return: As the system needs to temporarily construct the passed-in **builder** offscreen, the return time is usually longer than this delay.

Note: In the **builder** passed in, state variables should not be used to control the construction of child components. If they are used, they should not change when the API is called, so as to avoid unexpected snapshot results.

Default value: **300**

Unit: ms

Value range: \[0, +∞). If the value is less than 0, the default value is used.

 |
| checkImageStatus12+ | boolean | No | 

Whether to verify the image decoding status before taking a snapshot.

**true**: Check whether all Image components have been decoded.

**false**: Skip verification. If the verification is not completed, snapshot capture will be canceled and an exception will be returned.

Default value: **false**

 |
| options12+ | [SnapshotOptions](#snapshotoptions12) | No | Custom settings of the snapshot. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lYhyLXJiSBOzoud7lrsPbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9E108EE37197353269F2FD1138EB588415113BD20D900C4731F2F6D8B1AEC7A)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().createFromBuilder().
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          },
            (error: Error, pixmap: image.PixelMap) => {
              if (error) {
                console.error(\`error:${JSON.stringify(error)}\`)
                return;
              }
              this.pixmap = pixmap
              // Save the pixmap to a file.
              // ....
              // Obtain the component size and position.
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(info.size.width + ' ' + info.size.height + ' ' + info.localOffset.x + ' ' +
              info.localOffset.y + ' ' + info.windowOffset.x + ' ' + info.windowOffset.y)
            }, 320, true, { scale: 2, waitUntilRenderFinished: true })
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/M3ooxtNcT0G6C9oR_x3X8Q/en-us_image_0000002568765041.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A253479448FBDE61B9FD73BC3F40BCA2CFCABAF6EB72613534570A5EADE5B7E)

#### componentSnapshot.createFromBuilder(deprecated)

createFromBuilder(builder: CustomBuilder, delay?: number, checkImageStatus?: boolean, options?: SnapshotOptions): Promise<image.PixelMap>

Renders a custom component in the application background and outputs its snapshot. This API uses a promise to return the result. The coordinates and size of the offscreen component's drawing area can be obtained through the callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/XyDUWtf1RmaSBvDo_uTQ6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=414BC685325121B050C754DAC6DC5598D1C1E9E9554DB744D7AD7BB5DD34CB7E)

-   This API is supported since API version 10 and deprecated since API version 18. You are advised to use [createFromBuilder](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md#createfrombuilder12-1) instead. Before calling this API, you need to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object using the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 12, you can use the [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [ComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-componentsnapshot/document.md) object associated with the current UI context.
    
-   To account for the time spent in awaiting component building and rendering, the callback of offscreen snapshots has a delay of less than 500 ms.
    
-   Components in the builder do not support the setting of animation-related attributes, such as [transition](../../../arkts-components/animation/component-transition-transition/document.md).
    
-   If a component is on a time-consuming task, for example, an [Image](../../../arkts-components/images-and-videos/image/document.md) or [Web](../../../../arkweb/arkts-components/web/components/document.md) component that is loading online images, its loading may be still in progress when this API is called. In this case, the output snapshot does not represent the component in the way it looks when the loading is successfully completed.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [CustomBuilder](../../../arkts-components/common-definitions/basic-types/document.md#custombuilder8) | Yes | 
Builder of the custom component.

Note: The global builder is not supported.

If the root component of the builder has a width or height of zero, the snapshot operation will fail with error code 100001.

 |
| delay12+ | number | No | 

Delay time for triggering the screenshot command. When the layout includes an image component, it is necessary to set a delay time to allow the system to decode the image resources. The decoding time is subject to the resource size. In light of this, whenever possible, use pixel map resources that do not require decoding.

When pixel map resources are used or when **syncLoad** to **true** for the **Image** component, you can set **delay** to **0** to forcibly capture snapshots without waiting. This delay time does not refer to the time from the API call to the return: As the system needs to temporarily construct the passed-in **builder** offscreen, the return time is usually longer than this delay.

Note: In the **builder** passed in, state variables should not be used to control the construction of child components. If they are used, they should not change when the API is called, so as to avoid unexpected snapshot results.

Default value: **300**

Unit: ms

 |
| checkImageStatus12+ | boolean | No | 

Whether to verify the image decoding status before taking a snapshot.

**true**: Check whether all Image components have been decoded.

**false**: Skip verification. If the verification is not completed, snapshot capture will be canceled and an exception will be returned.

Default value: **false**

 |
| options12+ | [SnapshotOptions](#snapshotoptions12) | No | Custom settings of the snapshot. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The builder is not a valid build function. |
| 160001 | An image component in builder is not ready for taking a snapshot. The check for the ready state is required when the checkImageStatus option is enabled. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/m7kfT4YUSwS7MZYAVYbKKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46AF5330EF554DA64D7A3E066E58C73660F06FF5FCB266A36A540FA19B25A7FC)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { componentSnapshot } from '@kit.ArkUI'
import { image } from '@kit.ImageKit'

@Entry
@Component
struct OffscreenSnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  @Builder
  RandomBuilder() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Text('Test menu item 1')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
      Divider().height(10)
      Text('Test menu item 2')
        .fontSize(20)
        .width(100)
        .height(50)
        .textAlign(TextAlign.Center)
    }
    .width(100)
    .id("builder")
  }

  build() {
    Column() {
      Button("click to generate offscreen UI snapshot")
        .onClick(() => {
          // You are advised to use this.getUIContext().getComponentSnapshot().createFromBuilder().
          componentSnapshot.createFromBuilder(() => {
            this.RandomBuilder()
          }, 320, true, { scale: 2, waitUntilRenderFinished: true })
            .then((pixmap: image.PixelMap) => {
              this.pixmap = pixmap
              // Save the pixmap to a file.
              // ....
              // Obtain the component size and position.
              let info = this.getUIContext().getComponentUtils().getRectangleById("builder")
              console.info(\`${info.size.width} ${info.size.height} ${info.localOffset.x} ${
              info.localOffset.y} ${info.windowOffset.x} ${info.windowOffset.y}\`)
            }).catch((err: Error) => {
            console.error(\`error:${err}\`)
          })
        })
      Image(this.pixmap)
        .margin(10)
        .height(200)
        .width(200)
        .border({ color: Color.Black, width: 2 })
    }.width('100%').margin({ left: 10, top: 5, bottom: 5 }).height(300)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/O391zXo4TE-40IpXvr3rCQ/en-us_image_0000002568765041.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FCE7DB9E21F62329340228BAC9CF4575302B02837F8C6B73692949F163C1773)

#### componentSnapshot.getSync12+

getSync(id: string, options?: SnapshotOptions): image.PixelMap

Obtains the snapshot of a component that has been loaded based on the provided [component ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md). This API synchronously waits for the snapshot to complete and returns a [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/fBJB30yMSq2KP3RC5WK34A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D9F9F6F82E975767AF315457524DB986FCB2CA55A68CE4DCC0212A1F1420303)

The snapshot captures content rendered in the last frame. If this API is called when the component triggers an update, the re-rendered content will not be included in the obtained snapshot.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [ID](../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target component. |
| options | [SnapshotOptions](#snapshotoptions12) | No | Custom settings of the snapshot. |

**Return value**

| Type | Description |
| :-- | :-- |
| image.[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md), [Snapshot Error Codes](../../../error-codes/ui/snapshot-error-codes/document.md), and [API Call Error Codes](../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Invalid ID. |
| 160002 | Timeout. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/4euUfKyiRBm6GFrsiRW3TQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EF2E257A0C394E71A9BEF40E78648937EBA77BB5603EAEE46C185A886CA9280)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { componentSnapshot } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Image(this.pixmap).width(200).height(200).border({ color: Color.Black, width: 2 }).margin(5)
        // Replace $r('app.media.img') with the image resource file you use.
        Image($r('app.media.img'))
          .autoResize(true)
          .width(200)
          .height(200)
          .margin(5)
          .id("root")
      }

      Button("click to generate UI snapshot")
        .onClick(() => {
          try {
            // You are advised to use this.getUIContext().getComponentSnapshot().getSync().
            let pixelmap = componentSnapshot.getSync("root", { scale: 2, waitUntilRenderFinished: true })
            this.pixmap = pixelmap
          } catch (error) {
            console.error(\`getSync errorCode:${error.code} message:${error.message}\`)
          }
        }).margin(10)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/B_CdSt3ZRIetrY8S8TJpzQ/en-us_image_0000002568685031.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=834619E958C9CFF17CF6AEFE6E2A0A10CBC2406DC48811E2AEFEA7E7C66DB343)

#### SnapshotOptions12+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scale | number | No | Yes | 
Scale ratio for rendering pixel maps during a snapshot. Note that a high scale ratio may increase the time taken for the snapshot or even result in a snapshot failure.

Value range: \[0, +∞). If the value is less than or equal to 0, the default value is used.

Default value: **1**

**NOTE**

Avoid capturing images that are excessively large, ideally not larger than the screen size. If the size of the image to capture exceeds device-specific underlying limits, the capture will fail.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| waitUntilRenderFinished | boolean | No | Yes | 

Whether to force the system to wait for all rendering commands to complete before taking the snapshot. The value **true** means to force the system to wait for all rendering commands to complete before taking the snapshot, and **false** means the opposite. This option ensures the snapshot reflects the most up-to-date content and should be enabled whenever possible. Note that enabling this option may increase the time required for the snapshot to complete, which depends on the size of the area that needs to be redrawn at the time.

Default value: **false**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| region15+ | [SnapshotRegionType](#snapshotregiontype15) | No | Yes | 

Rectangular region for the snapshot. The default region is the entire component.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### SnapshotRegionType15+

type SnapshotRegionType = SnapshotRegion | LocalizedSnapshotRegion

Represents the region of a component to be captured in a snapshot. It can take one of the types listed in the table below.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [SnapshotRegion](#snapshotregion15) | Rectangular region for capturing the component snapshot. |
| [LocalizedSnapshotRegion](#localizedsnapshotregion15) | Rectangular region for capturing the component snapshot, with horizontal flipping based on the layout direction. If the layout direction is right-to-left (RTL), the specified region is flipped horizontally to accommodate the RTL layout. |

#### SnapshotRegion15+

Defines the rectangular region for capturing the component snapshot.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | 
X-coordinate of the upper left corner of the rectangular region.

Unit: px.

Value range: \[0, Component width\].

 |
| top | number | No | No | 

Y-coordinate of the upper left corner of the rectangular region.

Unit: px.

Value range: \[0, Component height\].

 |
| right | number | No | No | 

X-coordinate of the lower right corner of the rectangular region.

Unit: px.

Value range: \[0, Component width\].

 |
| bottom | number | No | No | 

Y-coordinate of the lower right corner of the rectangular region.

Unit: px.

Value range: \[0, Component height\].

 |

#### LocalizedSnapshotRegion15+

Defines the rectangular region for capturing the component snapshot, with coordinates adjusted based on the layout direction (LTR or RTL).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | No | 
For LTR layouts: X-coordinate of the upper left corner of the rectangular region.

For RTL layouts: X-coordinate of the upper right corner of the rectangular region.

Unit: px.

Value range: \[0, Component width\].

 |
| top | number | No | No | 

For LTR layouts: Y-coordinate of the upper left corner of the rectangular region.

For RTL layouts: Y-coordinate of the upper right corner of the rectangular region.

Unit: px.

Value range: \[0, Component height\].

 |
| end | number | No | No | 

For LTR layouts: X-coordinate of the lower right corner of the rectangular region.

For RTL layouts: X-coordinate of the lower left corner of the rectangular region.

Unit: px.

Value range: \[0, Component width\].

 |
| bottom | number | No | No | 

For LTR layouts: Y-coordinate of the lower right corner of the rectangular region.

For RTL layouts: Y-coordinate of the lower left corner of the rectangular region.

Unit: px.

Value range: \[0, Component height\].

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/aDqTtY0iQOu4OIQHfzCmgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=546ACCF73F8CF6AE5F0857FAED7123A8E4B505A696CAD1EB836B058B512247E0)

Directly using **componentSnapshot** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object using [getComponentSnapshot](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getcomponentsnapshot12).

**Example**

import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Column() {
          TextClock()
          Button("Button ABCDE").type(ButtonType.Normal)
          Row() {
            Checkbox()
            Text("√")
            Text(" | ")
            Checkbox()
            Text("×")
          }.align(Alignment.Start)

          TextInput()
        }
        .align(Alignment.Start)
        .id("component1")
        .width("600px")
        .height("600px")
        .borderRadius(6)
        .borderWidth(2)
        .borderColor(Color.Green)

      }

      Button("get capture")
        .onClick(() => {
          try {
            let pixelmap = this.getUIContext().getComponentSnapshot().getSync("component1",
              {
                scale: 2,
                waitUntilRenderFinished: true,
                region: {
                  start: 20,
                  top: 20,
                  end: 200,
                  bottom: 240
                }
              })
            this.pixmap = pixelmap
          } catch (error) {
            console.error(\`getSync errorCode:${error.code} message:${error.message}\`)
          }
        }).margin(10)
      Image(this.pixmap).border({ color: Color.Black, width: 2 }).width("600px")
    }.width("100%").align(Alignment.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/DqvWEZagSnWsnfcvdnGx7g/en-us_image_0000002537765316.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A64FFBFC200918850FED57A14F4235E1DC485E02CBB743406773B379E5CA20D)
