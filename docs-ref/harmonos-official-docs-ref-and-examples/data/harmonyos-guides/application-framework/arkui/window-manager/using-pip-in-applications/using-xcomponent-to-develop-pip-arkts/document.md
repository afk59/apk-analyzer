# Using XComponent to Develop PiP (ArkTS)

This topic uses video playback as an example to describe how to develop the PiP feature using the **XComponent**.

#### Constraints

-   In versions earlier than HarmonyOS 6.0.0, **XComponent** can be used to develop the PiP feature on phones and tablets. Since HarmonyOS 6.0.0, phones, PCs/2-in-1 devices, and tablets supports PiP development using **XComponent**.
-   Only the UI that uses the [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) as the media stream playback component can enter the PiP mode. The type of the **XComponent** must be **surface** or **XComponentType.SURFACE**.
-   When the UIAbility uses the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation) component to manage pages, you must set an ID for the component and pass the ID to the PiP controller. This ensures that the original page can be restored from the PiP window.
-   If the main window of the application is not in the foreground, you are advised not to perform UI operations, for example, pushing or popping pages, in the PiP lifecycle callbacks. These operations are deferred and may lead to unpredictable outcomes.
-   When the PiP mode is disabled, check whether the custom component nodes are released to avoid memory leakage.

#### How to Develop

1.  Create a PiP controller, and register the lifecycle event callback and control event callback.
    
    -   Use **create(config: PiPConfiguration)** to create a PiP controller instance.
    -   Use **setAutoStartEnabled** to set whether to automatically enable the PiP feature when users return to the home screen.
    -   Use **on('stateChange')** to register the lifecycle event callback.
    -   Use **on('controlPanelActionEvent')** to register the control event callback.
    
2.  Start a PiP window.
    
    Use **startPiP** to start a PiP window.
    
3.  Update the media content size.
    
    After the PiP media content is updated (for example, the video is switched), call **updateContentSize** of the PiP controller instance to update the media content size and adjust the PiP window ratio.
    
4.  Stop the PiP window.
    
    When there is no need to display the PiP window, you can stop the PiP window by calling **stopPiP** of the PiP controller instance.
    

// pages/XComponentImplementPage.ets
// This page is used to display the use of the Navigation component in the PiP window. If the UIAbility contains a single page, the Navigation component is not required.
import { Page1 } from '../xcomponent/Page1'

@Entry
@Component
struct XComponentImplementPage {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  private navId: string = 'navId';

  @Builder
  PageMap(name: string) {
    if (name === 'pageOne') {
      Page1({ navId: this.navId });
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }) // Push the NavDestination page specified by name.
          })
          .stateStyles({
            pressed: {
              .backgroundColor(Color.Red);
            },
            normal: {
              .backgroundColor(Color.Blue);
            }
          })
      }
    }
    .title('NavIndex')
    .navDestination(this.PageMap)
    .id(this.navId) // Set the ID of the Navigation component.
  }
}

The AVPlayer is required for video playback in the example. For details, see [Using AVPlayer to Play Videos (ArkTS)](../../../../../media/media-kit/media-development-arkts/playback/using-avplayer-to-play-videos-arkts/document.md).

// xcomponent/Page1.ets
// This page is used to display the basic usage of PiP.
import { AVPlayer } from '../model/AVPlayer';
import { BuilderNode, FrameNode, NodeController, UIContext, PiPWindow } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { Logger } from '../util/LogUtil';

const TAG = 'Page1';

class Params {
  public text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

// You can use the @Builder decorator to construct layouts.
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontColor(Color.Red)
  }
  .width('100%') // The PiP window extends to the full width.
  .height('100%') // The PiP window extends to the full height.
}

// You can extend NodeController to customize a UI controller.
class TextNodeController extends NodeController {
  private message: string;
  private textNode: BuilderNode<\[Params\]> | null = null;

  constructor(message: string) {
    super();
    this.message = message;
  }

  // Use BuilderNode to load the custom layouts.
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<\[Params\]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // You can customize this method to update layouts.
  update(message: string) {
    Logger.info(\`update message: ${message}\`);
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
    }
  }

  // You need to define this method to unregister the layout to avoid memory leakage.
  dispose() {
    Logger.info('dispose message: execute node dispose');
    if (this.textNode !== null) {
      this.textNode.dispose();
    }
  }
}

@Entry
@Component
export struct Page1 {
  @Consume('pageInfos') pageInfos: NavPathStack;
  private surfaceId: string = ''; // Surface ID, which is used to associate the XComponent with the AVPlayer.
  private mXComponentController: XComponentController = new XComponentController();
  private player?: AVPlayer = undefined;
  private pipController?: PiPWindow.PiPController = undefined;
  private nodeController: TextNodeController = new TextNodeController('this is custom UI');
  navId: string = '';
  private options: XComponentOptions = {
    type: XComponentType.SURFACE,
    controller: this.mXComponentController
  }

  build() {
    NavDestination() {
      Column() {
        // XComponent, which is used to play video streams.
        XComponent(this.options)
          .onLoad(() => {
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
            // The surface ID of the AVPlayer needs to be set to the surface ID of the XComponentController.
            this.player = new AVPlayer();
            this.player.surfaceID = this.surfaceId;
            this.player.avPlayerFdSrc();
          })
          .onDestroy(() => {
            Logger.info(\`\[${TAG}\] XComponent onDestroy\`);
          })
          .size({ width: '100%', height: '800px' })
        Row({ space: 20 }) {
          Button('startPip') // Start PiP.
            .onClick(() => {
              this.startPip();
            })
            .stateStyles({
              pressed: {
                .backgroundColor(Color.Red);
              },
              normal: {
                .backgroundColor(Color.Blue);
              }
            })
          Button('stopPip') // Stop PiP.
            .onClick(() => {
              this.stopPip();
            })
            .stateStyles({
              pressed: {
                .backgroundColor(Color.Red);
              },
              normal: {
                .backgroundColor(Color.Blue);
              }
            })
          Button('updateSize') // Update the video size.
            .onClick(() => {
              // The width and height set here must be those of the media content and be obtained through media-related APIs or callbacks.
              // For example, when the AVPlayer is used to play a video, the videoSizeChange callback function can be used to obtain the updated media content size.
              this.updateContentSize(900, 1600);
            })
            .stateStyles({
              pressed: {
                .backgroundColor(Color.Red);
              },
              normal: {
                .backgroundColor(Color.Blue);
              }
            })
        }
        .size({ width: '100%', height: 60 })
        .justifyContent(FlexAlign.SpaceAround)
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%')
    }
  }

  startPip() {
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(\`picture in picture disabled for current OS\`);
      return;
    }
    let config: PiPWindow.PiPConfiguration = {
      context: this.getUIContext().getHostContext() as Context,
      componentController: this.mXComponentController,
      // ID of the Navigation component on the current page.
      // 1. When the UIAbility uses the Navigation component to manage pages, you must set an ID for the component and pass the ID to the PiP controller. This ensures that the original page can be restored from the PiP window.
      // 2. When the UIAbility uses the Router module for page management (not recommended), you do not need to set the ID of the Navigation component. In this mode, do not switch between pages after PiP is started. Otherwise, an exception may occur.
      // 3. If the UIAbility has only one page, there is no need to set the ID of the Navigation component. The original page can be restored from the PiP window.
      navigationId: this.navId,
      // Used in video calls and video meetings. Set the corresponding template.
      templateType: PiPWindow.PiPTemplateType.VIDEO\_PLAY,
      // Optional. When creating a PiP controller, the system can set the PiP window ratio based on the XComponent size.
      contentWidth: 1920,
      // Optional. When creating a PiP controller, the system can set the PiP window ratio based on the XComponent size.
      contentHeight: 1080,
      // Optional. In video call, video meeting, and live scenarios, this attribute can be used to select the components to be displayed under the corresponding template.
      controlGroups: \[PiPWindow.VideoPlayControlGroup.VIDEO\_PREVIOUS\_NEXT\],
      // Optional. Set this parameter if you want to display the custom UI at the top of the PiP window.
      customUIController: this.nodeController,
    };
    // Step 1: Create a PiP controller instance by calling the create API.
    PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
      this.pipController = controller;
      // Step 1: Initialize the PiP controller.
      this.initPipController();
      // Step 2: Call the startPiP API to start PiP.
      this.pipController.startPiP().then(() => {
        Logger.info(\`Succeeded in starting pip.\`);
      }).catch((err: BusinessError) => {
        Logger.error(\`Failed to start pip. Cause:${err.code}, message:${err.message}\`);
      });
    }).catch((err: BusinessError) => {
      Logger.error(\`Failed to create pip controller. Cause:${err.code}, message:${err.message}\`);
    });
  }

  initPipController() {
    if (!this.pipController) {
      return;
    }
    // Step 1: Call the setAutoStartEnabled API to set whether to automatically start a PiP window when users return to the home screen, and register the callback functions stateChange and controlPanelActionEvent.
    this.pipController.setAutoStartEnabled(false /\*or true if necessary\*/); // False by default.
    this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
      this.onStateChange(state, reason);
    });
    this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
      this.onActionEvent(event, status);
    });
  }

  onStateChange(state: PiPWindow.PiPState, reason: string) {
    let curState: string = '';
    switch (state) {
      case PiPWindow.PiPState.ABOUT\_TO\_START:
        curState = 'ABOUT\_TO\_START';
        break;
      case PiPWindow.PiPState.STARTED:
        curState = 'STARTED';
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_STOP:
        curState = 'ABOUT\_TO\_STOP';
        this.nodeController?.dispose();
        break;
      case PiPWindow.PiPState.STOPPED:
        curState = 'STOPPED';
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_RESTORE:
        curState = 'ABOUT\_TO\_RESTORE';
        break;
      case PiPWindow.PiPState.ERROR:
        curState = 'ERROR';
        break;
      default:
        break;
    }
    Logger.info(\`\[${TAG}\] onStateChange: ${curState}, reason: ${reason}\`);
  }

  onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
    switch (event) {
      case 'playbackStateChanged':
        // Start or stop the video.
        if (status === 0) {
          // Stop the video.
        } else if (status === 1) {
          // Play the video.
        }
        break;
      case 'nextVideo':
        // Play the next video.
        break;
      case 'previousVideo':
        // Play the previous video.
        break;
      default:
        break;
    }
  }

  // Step 3: When the video content changes, update the video size to the PiP controller to adjust the PiP window ratio.
  updateContentSize(width: number, height: number) {
    if (this.pipController) {
      this.pipController.updateContentSize(width, height);
    }
  }

  // Step 4: Call the stopPiP API to stop the PiP window when the PiP window is not required.
  stopPip() {
    if (this.pipController) {
      let promise: Promise<void> = this.pipController.stopPiP();
      promise.then(() => {
        Logger.info(\`Succeeded in stopping pip.\`);
        this.pipController?.off('stateChange'); // If the stateChange callback function has been registered, unregister the callback function when stopping the PiP window.
        this.pipController?.off('controlPanelActionEvent'); // If the controlPanelActionEvent callback function has been registered, unregister the callback function when stopping the PiP window.
      }).catch((err: BusinessError) => {
        Logger.error(\`Failed to stop pip. Cause:${err.code}, message:${err.message}\`);
      });
    }
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/qL4-Q2cBROGqWNzfGJuYTg/en-us_image_0000002529582037.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DD4B10BE82038B57382436352B185D4D3A8CE7734DC91E2934A061C5CFB1D33 "Click to enlarge")
