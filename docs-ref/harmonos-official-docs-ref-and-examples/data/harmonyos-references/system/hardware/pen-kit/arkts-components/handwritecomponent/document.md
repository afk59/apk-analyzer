# HandwriteComponent

This module provides the handwriting suite components, including the canvas and toolbar, which are integrated to quickly implement the handwriting capability.

You need to provide entrances and callbacks to the handwriting canvas. The canvas will trigger a callback when the initialization, loading, and saving actions are complete. You can customize app behavior in the callback.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

#### Modules to Import

import { HandwriteController,HandwriteComponent, PenHspInfo, PenType } from '@kit.Penkit';

#### HandwriteComponent

**Model restriction**: This API can be used only in the stage model.

**Decorator type**: @Component

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

handwriteController

 | 

[HandwriteController](../../arkts-apis/handwritecontroller/document.md)

 | 

No

 | 

No

 | 

Instance of the handwriting suite function class.

 |
| 

onInit

 | 

[InitCallback](#section165621850195517)

 | 

No

 | 

Yes

 | 

InitCallback:() => void, callback for suite initialization.

 |
| 

onScale

 | 

[ScaleCallback](#section675202312586)

 | 

No

 | 

Yes

 | 

ScaleCallback: (scale: number) => void, callback for canvas scaling. The parameter of the callback method is the scaling factor of the current canvas.

 |
| 

defaultPenType

 | 

[PenType](#section10728472378)

 | 

No

 | 

Yes

 | 

Sets the default brush feature. The supported brushes are:

-   **1**: pen
-   **2**: ballpoint pen
-   **3**: pencil
-   **4**: marker
-   **5**: highlighter
-   **7**: mosaic pen
-   **8**: rubber
-   **9**: lasso
-   **10**: laser pointer

**Start version**: 5.1.0(18)

 |
| 

defaultPenInfo

 | 

[PenHspInfo](#section13968165173413)\[\]

 | 

No

 | 

Yes

 | 

Sets the default width of each brush.

**Start version**: 5.1.0(18)

 |
| 

widthRatio

 | 

number

 | 

No

 | 

Yes

 | 

Canvas width ratio (0–1).

**Start version**: 6.0.0(20)

 |
| 

heightRatio

 | 

number

 | 

No

 | 

Yes

 | 

Canvas height ratio (0–1).

**Start version**: 6.0.0(20)

 |

#### build

build(): void

Default constructor of a struct. This method cannot be directly called.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

#### InitCallback

type InitCallback = () => void

Callback for suite initialization.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.1.0(18)

#### ScaleCallback

type ScaleCallback = (scale: number) => void

Callback for canvas scaling. The parameter of the callback method is the scaling factor of the current canvas.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.1.0(18)

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

scale

 | 

number

 | 

Yes

 | 

Zoom ratio of the current canvas.

 |

#### PenType

Brush enumeration class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PEN

 | 

1

 | 

Pen.

 |
| 

BALLPOINT\_PEN

 | 

2

 | 

Ballpoint pen.

 |
| 

PENCIL

 | 

3

 | 

Pencil.

 |
| 

MARKER

 | 

4

 | 

Marker.

 |
| 

HIGHLIGHTER\_BRUSH

 | 

5

 | 

Highlighter.

 |
| 

MOSAIC

 | 

7

 | 

Mosaic pen.

 |
| 

RUBBER

 | 

8

 | 

Rubber.

 |
| 

LASSO

 | 

9

 | 

Lasso.

 |
| 

LASER

 | 

10

 | 

Laser pointer.

 |

#### PenHspInfo

Brush type and width.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.1.0(18)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

penType

 | 

[PenType](#section10728472378)

 | 

No

 | 

No

 | 

Brush type.

 |
| 

penWidth

 | 

number

 | 

No

 | 

No

 | 

Brush width. The default width and value range of each brush are as follows, in the format _Default width_ (_Width range_):

-   Pen: 4 (2–10)
-   Ballpoint pen: 4 (2–10)
-   Pencil: 8 (4–20)
-   Marker: 32 (16–80)
-   Highlighter: 32 (16–80)
-   Mosaic: 40 (8–40)
-   Rubber: 50 (10–120)
-   Laser pointer: 20 (8–48)

 |

**Example**:

import { HandwriteController,HandwriteComponent, PenHspInfo, PenType } from '@kit.Penkit';

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
          widthRatio: 1,   //(Optional) Width ratio of the custom canvas size (ranging from 0 to 1).
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
            // Obtain the thumbnail.
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/a1WXNHhLSaK4wKGc8p6wig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062411Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4C24F3C781E3AC30387CE98C892B4982024567DB72EF5277B0DC02F406C63E2)

The methods in **HandwriteController** need to be executed in the canvas control initialization callback or in customized methods in the preceding example.

[Set the context information](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pen-suite#section151484318552) before using the method.

For details about the complete sample code, please refer to [Penkit (ArkTS)](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy).
