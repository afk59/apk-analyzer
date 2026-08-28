# ImageBitmap

An **ImageBitmap** object stores pixel data rendered on a canvas. Since API version 11, when an application creates a [worker thread](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction), it can use **postMessage** to transfer the **ImageBitmap** instance to the worker thread for drawing, and use **onmessage** to receive the drawing results sent by the worker thread for display.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/wCZxkpUjQsubRUYPNADAPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=288607439645252B50356255BEAC3F9E518A479D42C67A446572DB7D02E7BD46)

This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### constructor

constructor(src: string)

Creates an **ImageBitmap** object using an **ImageSrc** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | 
Image source. Local images are supported.

1\. The string format is used to load local images, for example, **ImageBitmap("common/images/example.jpg")**. For entry and feature modules, the start point of the image path for loading is the **ets** folder of the module. For HAR and shared modules, the start point is the **ets** folder of the entry or feature module into which they are built.

For modules whose **type** is **"har"** or **"shared**", you are advised to use [ImageSource](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-decoding) to decode resource images into a unified **PixelMap** object for loading and use.

2\. Supported image formats: BMP, JPG, PNG, SVG, and WEBP.

**NOTE**

\- ArkTS widgets do not support the strings with the **http://**, **datashare://**, or **file://data/storage**.

 |

#### constructor

constructor(data: PixelMap)

Creates an **ImageBitmap** object using a **PixelMap** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Image data source, which supports **PixelMap** objects. |

#### constructor12+

constructor(src: string, unit: LengthMetricsUnit)

Creates an **ImageBitmap** object using an **ImageSrc** object. The unit mode of the Path2D object can be configured using **unit**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string | Yes | 
Image source. Local images are supported.

1\. The string format is used to load local images, for example, **ImageBitmap("common/images/example.jpg")**. For entry and feature modules, the start point of the image path for loading is the **ets** folder of the module. For HAR and shared modules, the start point is the **ets** folder of the entry or feature module into which they are built.

For modules whose **type** is **"har"** or **"shared**", you are advised to use [ImageSource](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-decoding) to decode resource images into a unified **PixelMap** object for loading and use.

2\. Supported image formats: BMP, JPG, PNG, SVG, and WEBP.

**NOTE**

\- ArkTS widgets do not support the strings with the **http://**, **datashare://**, or **file://data/storage**.

 |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | Yes | 

Unit mode of the **ImageBitmap** object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md).

If the value is **undefined**, **NaN**, or **Infinity**, the default value will be used.

 |

#### constructor12+

constructor(data: PixelMap, unit: LengthMetricsUnit)

Creates an **ImageBitmap** object using a **PixelMap** object. The unit mode of the Path2D object can be configured using **unit**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Image data source, which supports **PixelMap** objects. |
| unit | [LengthMetricsUnit](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetricsunit12) | Yes | Unit mode of the **ImageBitmap** object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](../canvasrenderingcontext2d/document.md). |

#### close

close(): void

Releases all graphics resources associated with this **ImageBitmap** object and sets its width and height to **0**. For the sample code, see the code for creating an **ImageBitmap** object.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width | number | Yes | No | 
Pixel width of the **ImageBitmap** object.

Default unit: vp

 |
| height | number | Yes | No | 

Pixel height of the **ImageBitmap** object.

Default unit: vp

 |

#### Example

## Example 1: Loading an Image

This example demonstrates how to load a local image using the **ImageBitmap** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/DWdiq_9KQyayMDNAdvlStg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFFA8AA0D2D651625DE19B024B51DA932B6EE8F0101F39C46C70D8E72F247997)

The resources used in this example are not located in the **src** > **main** > **resource** directory. Starting from DevEco Studio 6.0.0 Beta2, the resources that are located outside the **resources** directory are not packaged by default when a project or module is created. To package these resources, go to **buildOption** in the module's **build-profile.json5** file > **resOptions** > **copyCodeResource**, and set **enable** to **true**. For details, see the description of [copyCodeResource](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356) in **resOptions**.

// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/YqbkuCqYRTqif2n0NtpaUQ/en-us_image_0000002568685557.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2FA86A682FA8BA6F70858A9FCE6C5BD8C9940510C0DD2A81A53E973E54CA859)

## Example 2: Creating an ImageBitmap Object

This example shows how to create an **ImageBitmap** object using a **PixelMap** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/6CUZmTiUSz6uobp2INLfcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D2C85916E5234F024C8FD3BF68B5EAEBD8FE9F83EE4C5B0B976BC267461D538)

The DevEco Studio Previewer does not support the **getPixelMap** API and cannot display content drawn by **PixelMap**.

// xxx.ets
@Entry
@Component
struct Demo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(0, 0, 100, 100)
          let pixel = this.context.getPixelMap(0, 0, 100, 100)
          let image = new ImageBitmap(pixel)
          this.context.drawImage(image, 100, 100)
        })

    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/cNGogR4kRkuN9YkcVI5ukw/en-us_image_0000002568765567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DA36E0A5602487811383539C224FD2F300E022AC0F39FD5028B0AA3A5B0EE1D)

## Example 3: Supporting Concurrent Thread Drawing

This example demonstrates how to implement concurrent thread drawing by creating a Worker thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/sKHtxypkR5eJuR1nF8K84g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23E99DCECB70F1DBF47A4E869325473768E834402DD553CAD5F82B0C43DDA002)

The content drawn in the Worker thread cannot be previewed in DevEco Studio Previewer.

import { worker } from '@kit.ArkTS';

@Entry
@Component
struct imageBitmapExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
  // Replace "common/images/example.jpg" with the image resource file you use.
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.myWorker.postMessage({ myImage: this.img });
          this.myWorker.onmessage = (e): void => {
            if (e.data.myImage) {
              let image: ImageBitmap = e.data.myImage
              this.context.transferFromImageBitmap(image)
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

In the worker thread, the application uses **onmessage** to receive the **ImageBitmap** object sent by the main thread through **postMessage** and proceeds with rendering.

import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import { image } from '@kit.ImageKit';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  if (e.data.myImage) {
    let img: ImageBitmap = e.data.myImage
    let offCanvas = new OffscreenCanvas(600, 600)
    let offContext = offCanvas.getContext("2d")
    offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
    let image = offCanvas.transferToImageBitmap()
    workerPort.postMessage({ myImage: image });
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/gDa_DMeASjewRvpEm_KQsQ/en-us_image_0000002568685557.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062245Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B8F2ECD5D5B925112F6119B011FC22CAF15522B55C41AEF381AA9C90E18743F)
