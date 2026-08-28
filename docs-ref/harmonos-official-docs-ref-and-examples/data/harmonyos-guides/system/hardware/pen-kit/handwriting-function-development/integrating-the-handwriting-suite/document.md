# Integrating the Handwriting Suite

Starting from version 5.1.0(18), the handwriting suite supports configuring the default brush, brush type, pen width, and default width by brush on the toolbar.

Starting from version 6.0.0(20), the handwriting suite adds support for thumbnails and customizing the canvas size.

After the handwriting suite is integrated, you can create a handwriting screen in your app. The screen consists of two parts: canvas and toolbar. The canvas supports drawing with a stylus or finger. The toolbar provides multiple brushes and editing tools, and allows users to adjust the settings. After the handwriting suite is integrated, Instant Shape and point prediction will be automatically enabled.

#### Use Case

Create a handwriting screen in the app. The effect is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/EIebHK0eTh-JWXzlW3dz6g/en-us_image_0000002503542522.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E05B895E617500BE87642B9F7CA097D669D7CF8F76C5609555A9D27B4B83E898 "Click to enlarge")

1.  Load and display handwritten files.
2.  Edit and save handwritten files.
3.  The handwriting suite of Pen Kit can only be swiped up and down, but cannot be swiped left or right.

#### Development Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/N6rfte8sTjWd0gjCU3Mp8w/en-us_image_0000002503702336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A70FD96456E96B8749738CB9D50C9BA038998AB91C34421E1F354C8EBE04551C)

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HandwriteComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-handwritecomponent)

 | 

Constructs a canvas control.

 |
| 

[HandwriteController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-handwritecontroller)

 | 

Main function entry class of the canvas.

 |

#### Development Procedure

1\. Set **Context** for **EntryAbility**.

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import GlobalContext from '../utils/ContextConfig';

export default class EntryAbility extends UIAbility {

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // The main window has been created. Set the main page for this function.
    windowStage.loadContent('pages/HandWritingDemo', (err) => {
      if (err.code) {
        return;
      }
    });
    GlobalContext.setContext(this.context);
  }
}

2\. Create a **GlobalContext** class.

import { common } from "@kit.AbilityKit";

declare namespace globalThis {
  let \_brushEngineContext: common.UIAbilityContext;
};

export default class GlobalContext {
  static getContext(): common.UIAbilityContext {
    return globalThis.\_brushEngineContext;
  }

  static setContext(context: common.UIAbilityContext): void {
    globalThis.\_brushEngineContext = context;
  }
}

3\. Construct a control or screen that contains a handwriting component. The following uses a component as an example.

import { HandwriteController, HandwriteComponent, PenType, PenHspInfo } from '@kit.Penkit';

@Entry
@Component
struct HandWriteDemoComp {
  controller: HandwriteController = new HandwriteController();
  // Obtain the path for storing the handwritten file based on the app's storage rule. The path is for reference only.
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
          widthRatio: 1, // (Optional) Width ratio of the custom canvas size (ranging from 0 to 1).
          heightRatio: 1, // (Optional) Height ratio of the custom canvas size (ranging from 0 to 1).
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
            // Obtain the path for storing the handwritten file based on the app's storage rule. The path is for reference only.
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

For details about the complete sample code, please refer to [Penkit (ArkTS)](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_PenKit-Next-Easy).
