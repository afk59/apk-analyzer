# HandwriteController

Main entrance for accessing functions of the handwriting suite, including the main methods of the handwriting capability.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

#### Modules to Import

import { HandwriteController } from '@kit.Penkit';

This module provides the methods described in the following table to load and save handwritten content.

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[load](#section81796536265)

 | 

Loads a note file from a specified path.

 |
| 

[save](#section1858041418291)

 | 

Saves handwritten content.

 |
| 

[onLoad](#section759192934316)

 | 

Provides callbacks executed when the loading is complete.

 |
| 

[getContentRange](#section2152194517128)

 | 

Obtains the stroke content range.

 |
| 

[getThumbnail](#section1464912012163)

 | 

Obtains thumbnail data.

 |

#### load

load(path: string): void

Loads a note file from a specified path. Call this API after the handwriting suite is initialized.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Path of the file to be loaded.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010400001

 | 

load failed.

 |

**Example**:

For details about the code example, please refer to [onLoad](#section759192934316).

#### save

save(path: string): Promise<void>

Saves a note to a specified path. This API returns the result asynchronously through a promise. Call this API after the handwriting suite is loaded.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Path for saving the file.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010400002

 | 

save failed.

 |

**Example**:

For details about the code example, please refer to [onLoad](#section759192934316).

#### onLoad

onLoad(callback: AsyncCallback<string>): void

Registers a callback. This callback will be triggered when loading is complete. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function. If loading is successful, **err** is **load success**. If loading fails, **err** is **load failed**. **string** indicates the loading path.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010400001

 | 

load failed.

 |

#### getContentRange

getContentRange(): Rect

Obtains the stroke content range.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Rect](#section10728472378)

 | 

Rect information, which indicates the rectangular area that includes the content.

 |

#### getThumbnail

getThumbnail(rect: Rect): Promise<PixelMap>

Obtains thumbnail data.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 6.0.0(20)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

rect

 | 

[Rect](#section10728472378)

 | 

Yes

 | 

Rect information, which indicates the rectangular area that includes the thumbnail.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Thumbnail data.

 |

#### Rect

Rect information, which indicates the rectangular area.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

left

 | 

number

 | 

Left side of the rectangle. Unit: 1/1000 of the width of the [HandwriteComponent](../../arkts-components/handwritecomponent/document.md).

 |
| 

top

 | 

number

 | 

Top of the rectangle. Unit: 1/1000 of the width of the [HandwriteComponent](../../arkts-components/handwritecomponent/document.md).

 |
| 

right

 | 

number

 | 

Right side of the rectangle. Unit: 1/1000 of the width of the [HandwriteComponent](../../arkts-components/handwritecomponent/document.md).

 |
| 

bottom

 | 

number

 | 

Bottom of the rectangle. Unit: 1/1000 of the width of the [HandwriteComponent](../../arkts-components/handwritecomponent/document.md).

 |

**Example**:

import { HandwriteController, HandwriteComponent, PenType, PenHspInfo } from '@kit.Penkit';

@Entry
@Component
struct HandWriteDemoComp {
  controller: HandwriteController = new HandwriteController();
  // Obtain the path for storing the handwritten file based on the app storage rule. The path here is for reference only.
  initPath: string = this.getUIContext().getHostContext()?.filesDir + '/aa';
  penWidth: number = 5;
  ballpointPenWidth: number = 6;

  aboutToAppear() {
    // Set the callback for the completion of the saving action during loading.
    this.controller.onLoad(this.callback);
  }

  // Callback triggered once the handwritten file is loaded and rendered on the screen. You will be notified of the result and can then customize actions here.
  callback = () => {
    // Custom action, for example, displaying the user operation guide after the file is loaded.
  }

  build() {
    Row() {
      Stack({ alignContent: Alignment.TopStart }) {
        HandwriteComponent({
          handwriteController: this.controller,
          defaultPenType: PenType.PEN, // (Optional) Default brush.
          defaultPenInfo: \[{ penType: PenType.PEN, penWidth: this.penWidth },
            { penType: PenType.BALLPOINT\_PEN, penWidth: this.ballpointPenWidth }\] as PenHspInfo\[\], // (Optional) Default width of each brush.
          widthRatio: 1,  // (Optional) Width ratio of the custom canvas size (ranging from 0 to 1).
          heightRatio: 1,  // (Optional) Height ratio of the custom canvas size (ranging from 0 to 1).
          onInit: () => {
            // Callback triggered once the canvas initialization is complete. In this case, you can call the API to load and display the note content.
            this.controller?.load(this.initPath);
          },
          onScale: (scale: number) => {
            // Callback triggered when the canvas is zoomed in or out. The scaling factor of the current handwriting control is returned. Custom actions can be performed here.
          }
        })
        Button("save")
          .onClick(async () => {
            // Obtain the path for storing the handwritten file based on the app's storage rule. The path here is for reference only.
            const path = this.getUIContext().getHostContext()?.filesDir + '/aa';
            await this.controller?.save(path).then().catch((error: Error) => {
              console.info("err: " + error);
            })
            this.controller.getThumbnail(this.controller?.getContentRange())?.then((pixelMap: PixelMap) => {
              if (pixelMap) {
                pixelMap.release()
                console.info('getThumbnail success')
              }
            })
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/hGNCXI42Q6KQZ267vbNeuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AF57EB5AAF88DE3602F1EBC8F42F94563F168B165A9851A4B17CC515E136B6A)

The methods in **HandwriteController** need to be executed in the canvas control initialization callback or in customized methods in the preceding example.

[Set the context information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pen-suite#section151484318552) before using the method.

For details about the complete sample code, please refer to [Penkit (ArkTS)](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy).
