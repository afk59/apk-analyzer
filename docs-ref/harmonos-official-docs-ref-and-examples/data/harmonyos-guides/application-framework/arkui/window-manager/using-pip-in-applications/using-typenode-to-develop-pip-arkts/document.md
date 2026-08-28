# Using typeNode to Develop PiP (ArkTS)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/8v5TZYjbSLq7pj1tXk8EhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF543067F731DFF8266124BC6C542DE7DF3EAE3CEFA5D6C91BEDE98F1911BB85)

-   Since API version 12, typeNode can be used to develop the PiP feature.
-   In versions earlier than HarmonyOS 6.0.0, typeNode can be used to develop the PiP feature on phones and tablets. Since HarmonyOS 6.0.0, phones, PCs/2-in-1 devices, and tablets supports PiP development using typeNode.

This development mode applies to all scenarios that requires the PiP feature. Typical development scenarios are as follows:

-   [Using Free typeNode (Not Added to the Layout) to Develop PiP](#section7627141117162)
-   [Using typeNode to Develop PiP When router Is Used for Redirection](#section1236517470234)
-   [Using typeNode to Develop PiP When Navigation Is Used for Redirection](#section173761626124613)
-   [Using typeNode to Develop PiP When the Ability Has Only One Page](#section8907336134011)

This topic uses video playback as an example to describe how to develop the PiP feature using typeNode.

The video player used in this section is implementation using the code below:

// model/AVPlayer.ets
// Simple player implementation
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { media } from '@kit.MediaKit';
import { Logger } from '../util/LogUtil';

export class AVPlayer {
  private avPlayer?: media.AVPlayer;
  public surfaceID: string = '';

  setAVPlayerCallback() {
    this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
      Logger.info(\`AVPlayer seek succeeded, seek time is ${seekDoneTime}\`);
    })
    this.avPlayer?.on('stateChange', async (state, reason) => {
      if (!this.avPlayer) {
        return;
      }
      switch (state) {
        case 'idle':
          this.avPlayer.release();
          break;
        case 'initialized':
          this.avPlayer.surfaceId = this.surfaceID;
          this.avPlayer.prepare().then(() => {
            Logger.info('AVPlayer prepare succeeded.');
          }, (err: BusinessError) => {
            Logger.error(\`Invoke prepare failed, code is ${err.code}, message is ${err.message}\`);
          });
          break;
        case 'prepared':
          this.avPlayer.play();
          break;
        case 'stopped':
          this.avPlayer.reset();
          break;
        default:
          break;
      }
    })
  }

  async avPlayerFdSrc() {

    try {
      this.avPlayer = await media.createAVPlayer();
    } catch(err) {
      Logger.error(\`create AVPlayer failed\`);
    };
    this.setAVPlayerCallback();
    let uiContext = AppStorage.get('UIContext') as UIContext;
    let context = uiContext.getHostContext() as common.UIAbilityContext;
    let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');

    if (this.avPlayer) {
      this.avPlayer.fdSrc = fileDescriptor;
    }
  }
}

#### Constraints

-   When constructing the PiP configuration parameters, you are advised to pass in the **contentWidth** and **contentHeight** parameters to calculate the initial PiP window ratio. Otherwise, the default ratio 16:9 is used.
-   **contentNode** supports the **XComponentType.SURFACE** type, and the **XComponent** type must be specified when the typeNode is created.
-   When the PiP mode is disabled, check whether the custom component nodes are released to avoid memory leakage.

#### Using Free typeNode (Not Added to the Layout) to Develop PiP

1.  Create a PiP controller, and register the lifecycle event callback and control event callback.
    
    -   Create a typeNode through the UIContext in the main window.
    -   Use **create(config: PiPConfiguration, contentNode: typeNode.XComponent)** to create a PIP controller instance.
    -   Use **setAutoStartEnabled** to set whether to automatically enable the PiP feature when users return to the home screen.
    -   Use **on('stateChange')** to register the lifecycle event callback.
    -   Use **on('controlEvent')** to register the control event callback.
    
2.  Start a PiP window.
    
    Use **startPiP** to start a PiP window.
    
3.  Update the media content size.
    
    After the PiP media content is updated (for example, the video is switched), call **updateContentSize** of the PiP controller instance to update the media content size and adjust the PiP window ratio.
    
4.  Stop the PiP window.
    
    When there is no need to display the PiP window, you can stop the PiP window by calling **stopPiP** of the PiP controller instance.
    

// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
// ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    Logger.info('testTag', '%{public}s', 'Ability onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let windowClassId: number = -1;

    windowStage.getMainWindow().then((window) => {
      if (window == null) {
        Logger.error('Failed to obtaining the window. Cause: The data is empty');
        return;
      }
      windowClass = window;
      windowClass.setUIContent('pages/Index');
      windowClassId = windowClass.getWindowProperties().id;
      AppStorage.setOrCreate('windowId', windowClassId);
      Logger.info('Succeeded in obtaining the window')

      let ctx = window.getUIContext();
      AppStorage.setOrCreate('UIContext', ctx);
      // Create a typeNode through the UIContext in the main window.
      PipManager.getInstance().makeTypeNode(ctx);
    }).catch((err: BusinessError) => {
      Logger.error(\`Failed to obtaining the window. Cause code: ${err.code}, message: ${err.message}\`);
    });
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        Logger.error('testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      Logger.info('testTag', 'Succeeded in loading the content.');
    });
  }
  // ...
}

// pages/Index.ets
// Application home screen
import { router } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      Scroll() {
        Flex({ direction: FlexDirection.Column }) {
          // ...
          this.featureButton('Implement PiP Using typeNode', this.typeNodeFree);
          // ...
        }
      }
    }
    .hideBackButton(true)
    .titleMode(NavigationTitleMode.Mini)
    .backgroundColor('#FFF1F3F5')
    .mode(NavigationMode.Stack)
    .title('Sample Code for PiP')
  }

  @Builder
  featureButton(buttonText: string, callbackOnClick: () => void) {
    Button({ type: ButtonType.Normal }) {
      Row() {
        Column() {
          Text(buttonText)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .fontColor('#000000')
          Rect()
            .radius(1)
            .fill('#0A59F7')
            .height(2)
            .width(30)
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .width('100%')
    }
    .width('90%')
    .padding('5%')
    .margin({ top: '3%', bottom: '2%', right: '3%' })
    .backgroundColor('#FFFFFF')
    .borderRadius(20)
    .onClick(callbackOnClick)
  }

  // ...
  private typeNodeFree = () => {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/TypeNodeFreePage' }, router.RouterMode.Standard)
  }
  // ...
}

// pages/TypeNodeFreePage.ets
// This page is used to display the application layout file. The created typeNode is not added to this layout.
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'TypeNodeFreePage'
@Entry
@Component
struct TypeNodeFreePage {
  build() {
    Column() {
      Text('This is MainPage')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 20 })

      Text('This is not typeNode')
        .size({ width: '100%', height: '800px' })
        .fontSize(30)
        .textAlign(TextAlign.Center)
        .fontWeight(FontWeight.Bold)
        .backgroundColor('#4d5b5858')

      Row({ space: 20 }) {
        Button('startPip') // Start PiP.
          .onClick(() => {
            PipManager.getInstance().startPip();
          })

        Button('stopPip') // Stop PiP.
          .onClick(() => {
            PipManager.getInstance().stopPip();
          })

        Button('updateSize') // Update the video size.
          .onClick(() => {
            PipManager.getInstance().updateContentSize(900, 1600);
          })
      }
      .backgroundColor('#4da99797')
      .size({ width: '100%', height: 60 })
      .justifyContent(FlexAlign.SpaceAround)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }

  aboutToDisappear(): void {
    PipManager.getInstance().unregisterPipStateChangeListener(); // Unregister the lifecycle event callback of the PiP controller.
  }

  onPageShow(): void {
    Logger.info(TAG, 'onPageShow')
    PipManager.getInstance().init(this.getUIContext().getHostContext() as Context); // Create a PiP controller.
    PipManager.getInstance().setAutoStart(true); // Set the application to automatically start PiP when it switches to the background.
  }

  onPageHide(): void {
    Logger.info(TAG, 'onPageHide')
    PipManager.getInstance().setAutoStart(false);
  }
}

// nodeFree/PipManager.ets
// PiP controller singleton
import { PiPWindow, typeNode } from '@kit.ArkUI'; // Import the PiPWindow module.
import { BusinessError } from '@kit.BasicServicesKit';
import { AVPlayer} from '../model/AVPlayer';
import { Logger } from '../util/LogUtil';

// Customize an XComponentController.
class CustomXComponentController extends XComponentController {
  // Listen for the onSurfaceCreated event and set the surface ID to the player.
  onSurfaceCreated(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceCreated surfaceId: ${surfaceId}\`);
    if (PipManager.getInstance().player.surfaceID === surfaceId) {
      return;
    }
    PipManager.getInstance().player.surfaceID = surfaceId;
    PipManager.getInstance().player.avPlayerFdSrc();
  }

  onSurfaceDestroyed(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
  }
}

const TAG = 'PipManager';

export class PipManager {
  public player: AVPlayer;
  private static instance: PipManager = new PipManager();
  private pipController?: PiPWindow.PiPController = undefined;
  private mXComponentController: XComponentController;
  private xComponent: typeNode.XComponent| null = null; // typeNode

  public static getInstance(): PipManager {
    return PipManager.instance;
  }

  constructor() {
    this.player = new AVPlayer();
    this.mXComponentController = new CustomXComponentController();
  }

  onActionEvent(control: PiPWindow.ControlEventParam) {
    switch (control.controlType) {
      case PiPWindow.PiPControlType.VIDEO\_PLAY\_PAUSE:
        if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
         // Stop the video.
        } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
          // Play the video.
        }
        break;
      case PiPWindow.PiPControlType.VIDEO\_NEXT:
        // Switch to the next video.
        break;
      case PiPWindow.PiPControlType.VIDEO\_PREVIOUS:
        // Switch to the previous video.
        break;
      case PiPWindow.PiPControlType.FAST\_FORWARD:
        // Fast forward the video.
        break;
      case PiPWindow.PiPControlType.FAST\_BACKWARD:
        // Rewind the video.
        break;
      default:
        break;
    }
    Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
  }

  // Listen for the PiP lifecycle.
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

  // Unregister the listener.
  unregisterPipStateChangeListener() {
    Logger.info(TAG, 'aboutToDisappear');
    this.pipController?.off('stateChange');
    this.pipController?.off('controlEvent');
  }

  getXComponentController(): CustomXComponentController {
    return this.mXComponentController;
  }

  // Step 1: Create a PiP controller, and register the lifecycle event callback and control event callback.
  init(ctx: Context) {
    if (this.pipController !== null && this.pipController != undefined) {
      return;
    }
    Logger.info(TAG, 'onPageShow');
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(TAG, \`picture in picture disabled for current OS\`);
      return;
    }

    let config: PiPWindow.PiPConfiguration = {
      context: ctx,
      componentController: this.getXComponentController(),
      templateType: PiPWindow.PiPTemplateType.VIDEO\_PLAY,
      contentWidth: 1920, // When typeNode is used to start PiP, contentWidth must be set to a value greater than 0. Otherwise, the default ratio 16:9 is used.
      contentHeight: 1080, // When typeNode is used to start PiP, contentHeight must be set to a value greater than 0. Otherwise, the default ratio 16:9 is used.
    };
    // Use create to create a PiP controller instance.

    PiPWindow.create(config, this.xComponent).then((controller: PiPWindow.PiPController) => {
      this.pipController = controller;
     // Use setAutoStartEnabled to set whether to automatically enable the PiP feature when users return to the home screen.
      this.pipController.setAutoStartEnabled(true);
      // Use on('stateChange') to register the lifecycle event callback.
      this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
        this.onStateChange(state, reason);
      });
      // Use on('controlEvent') to register the control event callback.
      this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
        this.onActionEvent(control);
      });
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to create pip controller. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 2: Use startPiP to start a PiP window.
  startPip() {
    this.pipController?.startPiP().then(() => {
      Logger.info(TAG, \`Succeeded in starting pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to start pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 3: Update the media content size.
  updateContentSize(width: number, height: number) {
    if (this.pipController) {
      this.pipController.updateContentSize(width, height);
    }
  }

  // Step 4: Stop PiP.
  stopPip() {
    if (this.pipController === null || this.pipController === undefined) {
      return;
    }
    let promise: Promise<void> = this.pipController.stopPiP();
    promise.then(() => {
      Logger.info(TAG, \`Succeeded in stopping pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to stop pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  setAutoStart(autoStart: boolean): void {
    this.pipController?.setAutoStartEnabled(autoStart);
  }

  // Create a typeNode.
  makeTypeNode(ctx: UIContext) {
    if (this.xComponent === null || this.xComponent === undefined) {
      // Create a typeNode of the XComponent type.
      this.xComponent = typeNode.createNode(ctx, 'XComponent', {
        // Set the type to SURFACE.
        type: XComponentType.SURFACE,
        // Set an XComponentController.
        controller: PipManager.getInstance().getXComponentController(),
      });
    }
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/7wgtgNeGQr-J5LSaabOBuA/en-us_image_0000002497742074.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90A1F82204BA5B8779356E6A3F06313E84D79675221ECC34F9DF51233F2C223E "Click to enlarge")

#### Using typeNode to Develop PiP When router Is Used for Redirection

1.  Create a PiP controller, and register the lifecycle event callback and control event callback.
    
    -   Create a custom NodeController, implement the **makeNode** method, and create a typeNode in the method.
    -   Use **create(config: PiPConfiguration, contentNode: typeNode.XComponent)** to create a PIP controller instance.
    -   Use **setAutoStartEnabled** to set whether to automatically enable the PiP feature when users return to the home screen.
    -   Use **on('stateChange')** to register the lifecycle event callback.
    -   Use **on('controlEvent')** to register the control event callback.
    
2.  Start a PiP window.
    
    After a PIP controller instance is created, call **startPiP** to start PiP. In the **ABOUT\_TO\_START** lifecycle, remove the typeNode from the layout and return to the upper-level page (optional). If returning to the upper-level page is enabled, you also need to redirect to the original page in the **ABOUT\_TO\_RESTORE** callback (during restoration).
    
3.  Update the media content size.
    
    After the PiP media content is updated (for example, the video is switched), call **updateContentSize** of the PiP controller instance to update the media content size and adjust the PiP window ratio.
    
4.  Stop the PiP window.
    
    When there is no need to display the PiP window, you can stop the PiP window by calling **stopPiP** of the PiP controller instance, and add the typeNode to the layout again in the **ABOUT\_TO\_STOP** lifecycle.
    

// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
// ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...
    windowStage.loadContent('pages/Index', (err) => {
      // ...
    });
  }
  // ...
}

// pages/RouterImplementPage.ets
import { PipManager } from '../route/PipManager';
import { PiPWindow, router, Router } from '@kit.ArkUI'; // Import the PiPWindow module.
import { Logger } from '../util/LogUtil';

const TAG = 'RouterImplementPage'
@Entry
@Component
struct RouterImplementPage {
  private page1: string = 'route/Page1';
  private pageRouter: Router | null = null;

  // Listen for the PiP lifecycle event, which is used for page and node operations.
  private callback: Function = (state: PiPWindow.PiPState) => {
    Logger.info(TAG, \`pipStateChange: state ${state}\`);
    if (state === PiPWindow.PiPState.ABOUT\_TO\_START) {
      // (Optional) Return to the upper-level page.
      this.pageRouter?.back();
    } else if (state === PiPWindow.PiPState.ABOUT\_TO\_STOP) {
      // Add the typeNode to the layout again, for example, in the restoration scenario.
      PipManager.getInstance().addNode();
    } else if (state === PiPWindow.PiPState.ABOUT\_TO\_RESTORE) {
      // If the upper-level page is returned in the ABOUT\_TO\_START callback, push the original page during the restoration.
      this.jumpNext();
    }
  };

  aboutToAppear(): void {
    this.pageRouter = this.getUIContext().getRouter();
    PipManager.getInstance().registerLifecycleCallback(this.callback);
  }

  aboutToDisappear(): void {
    PipManager.getInstance().unregisterPipStateChangeListener();
    PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
  }

  jumpNext(): void {
    let topPage = this.pageRouter?.getState();
    if (topPage !== undefined && (this.page1.toString() === topPage.path + topPage.name)) {
      Logger.info(TAG, \`page1 aready at top\`)
      return;
    }
    this.pageRouter?.pushUrl({
      url: this.page1 // Target URL.
    }, router.RouterMode.Standard, (err) => {
      if (err) {
        Logger.error(TAG, \`Invoke pushUrl failed, code is ${err.code}: ${err.message}\`);
        return;
      }
      Logger.info(TAG, 'Invoke pushUrl succeeded.');
    });
  }

  build() {
    Row() {
      Column() {
        Text('Main Page')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)

        Button('Jump Next')
          .onClick(() => {
            this.jumpNext();
          })
          .margin({ top: 16, bottom: 16 })
      }
      .width('100%')
    }
    .height('100%')
  }
}

// route/Page1.ets
import { PipManager } from '../route/PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'Page1';

@Entry
@Component
export struct Page1 {
  build() {
    Column() {
      Text('This is Page1')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({bottom: 20})

      // Add typeNode to the layout.
      NodeContainer(PipManager.getInstance().getNodeController())
        .size({ width: '100%', height: '800px' })

      Row({ space: 20 }) {
        Button('startPip') // Start PiP.
          .onClick(() => {
            PipManager.getInstance().startPip();
          })

        Button('stopPip') // Stop PiP.
          .onClick(() => {
            PipManager.getInstance().stopPip();
          })

        Button('updateSize') // Update the video size.
          .onClick(() => {
            // The width and height set here must be those of the media content and be obtained through media-related APIs or callbacks.
            // For example, when the AVPlayer is used to play a video, the videoSizeChange callback function can be used to obtain the updated media content size.
            PipManager.getInstance().updateContentSize(900, 1600);
          })
      }
      .backgroundColor('#4da99797')
      .size({ width: '100%', height: 60 })
      .justifyContent(FlexAlign.SpaceAround)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }

  onPageShow(): void {
    Logger.info(TAG, 'onPageShow')
    PipManager.getInstance().initPipController(this.getUIContext().getHostContext() as Context);
    PipManager.getInstance().setAutoStart(true);
  }

  onPageHide(): void {
    Logger.info(TAG, 'onPageHide')
    PipManager.getInstance().setAutoStart(false);
    PipManager.getInstance().removeNode();
  }
}

// route/PipManager.ets
import { PiPWindow, typeNode } from '@kit.ArkUI'; // Import the PiPWindow module.
import { BusinessError } from '@kit.BasicServicesKit';
import { XCNodeController } from './XCNodeController';
import { AVPlayer } from '../model/AVPlayer';
import { Logger } from '../util/LogUtil';

export class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceCreated surfaceId: ${surfaceId}\`);
    if (PipManager.getInstance().player.surfaceID === surfaceId) {
      return;
    }
    // Set the surface ID to the media source.
    PipManager.getInstance().player.surfaceID = surfaceId;
    PipManager.getInstance().player.avPlayerFdSrc();
  }

  onSurfaceDestroyed(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
  }
}

const TAG = 'PipManager';

export class PipManager {
  private static instance: PipManager = new PipManager();
  private pipController?: PiPWindow.PiPController = undefined;
  private xcNodeController: XCNodeController;
  private mXComponentController: XComponentController;
  private lifeCycleCallback: Set<Function> = new Set();
  public player: AVPlayer;

  public static getInstance(): PipManager {
    return PipManager.instance;
  }

  constructor() {
    this.xcNodeController = new XCNodeController();
    this.player = new AVPlayer();
    this.mXComponentController = new CustomXComponentController();
  }

  public registerLifecycleCallback(callBack: Function) {
    this.lifeCycleCallback.add(callBack);
  }

  public unRegisterLifecycleCallback(callBack: Function): void {
    this.lifeCycleCallback.delete(callBack);
  }

  getNode(): typeNode.XComponent | null {
    return this.xcNodeController.getNode();
  }

  onActionEvent(control: PiPWindow.ControlEventParam) {
    switch (control.controlType) {
      case PiPWindow.PiPControlType.VIDEO\_PLAY\_PAUSE:
        if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
         // Stop the video.
        } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
          // Play the video.
        }
        break;
      case PiPWindow.PiPControlType.VIDEO\_NEXT:
        // Switch to the next video.
        break;
      case PiPWindow.PiPControlType.VIDEO\_PREVIOUS:
        // Switch to the previous video.
        break;
      case PiPWindow.PiPControlType.FAST\_FORWARD:
        // Fast forward the video.
        break;
      case PiPWindow.PiPControlType.FAST\_BACKWARD:
        // Rewind the video.
        break;
      default:
        break;
    }
    Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
  }

  onStateChange(state: PiPWindow.PiPState, reason: string) {
    let curState: string = '';
    this.xcNodeController.setCanAddNode(
      state === PiPWindow.PiPState.ABOUT\_TO\_STOP || state === PiPWindow.PiPState.STOPPED)
    if (this.lifeCycleCallback !== null) {
      this.lifeCycleCallback.forEach((fun) => {
        fun(state)
      });
    }
    switch (state) {
      case PiPWindow.PiPState.ABOUT\_TO\_START:
        curState = 'ABOUT\_TO\_START';
        // Remove the typeNode from the layout.
        this.xcNodeController.removeNode();
        break;
      case PiPWindow.PiPState.STARTED:
        curState = 'STARTED';
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_STOP:
        curState = 'ABOUT\_TO\_STOP';
        this.xcNodeController.dispose();
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

  unregisterPipStateChangeListener() {
    Logger.info(\`${TAG} aboutToDisappear\`)
    this.pipController?.off('stateChange');
    this.pipController?.off('controlEvent');
    this.pipController = undefined;
  }

  getXComponentController(): CustomXComponentController {
    return this.mXComponentController;
  }

  // Step 1: Create a PiP controller, and register the lifecycle event callback and control event callback.
  initPipController(ctx: Context) {
    if (this.pipController !== null && this.pipController != undefined) {
      return;
    }
    Logger.info(\`${TAG} onPageShow\`)
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(TAG, \`picture in picture disabled for current OS\`);
      return;
    }
    let config: PiPWindow.PiPConfiguration = {
      context: ctx,
      componentController: this.getXComponentController(),
      templateType: PiPWindow.PiPTemplateType.VIDEO\_PLAY,
      contentWidth: 1920, // When typeNode is used to start PiP, contentWidth must be set to a value greater than 0. Otherwise, the PIP fails to be created.
      contentHeight: 1080, // When typeNode is used to start PiP, contentHeight must be set to a value greater than 0. Otherwise, the PIP fails to be created.
    };
    // Use create to create a PiP controller instance.

    PiPWindow.create(config, this.getNode()).then((controller: PiPWindow.PiPController) => {
      this.pipController = controller;
     // Use setAutoStartEnabled to set whether to automatically enable the PiP feature when users return to the home screen.
      this.pipController.setAutoStartEnabled(true)
      // Use on('stateChange') to register the lifecycle event callback.
      this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
        this.onStateChange(state, reason);
      });
      // Use on('controlEvent') to register the control event callback.
      this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
        this.onActionEvent(control);
      });
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to create pip controller. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 2: Start PiP.
  startPip() {
    this.pipController?.startPiP().then(() => {
      Logger.info(TAG, \`Succeeded in starting pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to start pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 3: Update the media content size.
  updateContentSize(width: number, height: number) {
    if (this.pipController) {
      this.pipController.updateContentSize(width, height);
    }
  }

  // Step 4: Stop PiP.
  stopPip() {
    if (this.pipController) {
      let promise: Promise<void> = this.pipController.stopPiP();
      promise.then(() => {
        Logger.info(TAG, \`Succeeded in stopping pip.\`);
      }).catch((err: BusinessError) => {
        Logger.error(TAG, \`Failed to stop pip. Cause:${err.code}, message:${err.message}\`);
      });
    }
  }

  getNodeController(): XCNodeController {
    Logger.info(TAG, \`getNodeController.\`);
    return this.xcNodeController;
  }

  setAutoStart(autoStart: boolean): void {
    this.pipController?.setAutoStartEnabled(autoStart);
  }

  removeNode(): void {
    this.xcNodeController.removeNode();
  }

  addNode(): void {
    this.xcNodeController.addNode();
  }
}

// route/XCNodeController.ets
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
import { PipManager } from './PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'XCNodeController';
// Create a custom NodeController.
export class XCNodeController extends NodeController {
  public xComponent: typeNode.XComponent | null = null;
  private node: FrameNode | null = null;
  private canAddNode: boolean = true;

  // Set whether nodes can be added.
  setCanAddNode(canAddNode: boolean) {
    this.canAddNode = canAddNode;
  }

  // Implement the makeNode method. This method is called when the custom NodeController is added to the layout.
  makeNode(context: UIContext): FrameNode | null {
    this.node = new FrameNode(context);
    this.node.commonAttribute
    if (this.xComponent === null || this.xComponent === undefined) {
      // Create a typeNode of the XComponent type.
      this.xComponent = typeNode.createNode(context, 'XComponent', {
        // Set the type to SURFACE.
        type: XComponentType.SURFACE,
        // Set an XComponentController.
        controller: PipManager.getInstance().getXComponentController(),
      });
    }
    if (this.canAddNode) {

      try {
        this.xComponent.getParent()?.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
    return this.node;
  }

  // Add the typeNode again.
  addNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'addNode');

      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
  }

  // Remove the typeNode.
  removeNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'removeNode');

      try {
        this.node.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
    }
  }

  getNode(): typeNode.XComponent | null {
    Logger.info(TAG, 'getNode is null: '+ (this.xComponent === null || this.xComponent === undefined));
    return this.xComponent;
  }

  // You need to define this method to unregister the layout to avoid memory leakage.
  dispose() {
    Logger.info(TAG, 'execute node dispose');
    if (this.node !== null) {
      this.node.dispose();
    }
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/5Dn81QMBQwm34sNVv_xoYA/en-us_image_0000002497902048.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4E6182C0B5AFB46F4A95E14F8D8AE90CA3D089223F956F49095B0D883F7E983 "Click to enlarge")

#### Using typeNode to Develop PiP When Navigation Is Used for Redirection

1.  Create a PiP controller, and register the lifecycle event callback and control event callback.
    
    -   Create a custom NodeController, implement the makeNode method, and create a typeNode in the method.
    -   Use **create(config: PiPConfiguration, contentNode: typeNode.XComponent)** to create a PIP controller instance.
    -   Use **setAutoStartEnabled** to set whether to automatically enable the PiP feature when users return to the home screen.
    -   Use **on('stateChange')** to register the lifecycle event callback.
    -   Use **on('controlEvent')** to register the control event callback.
    
2.  Start a PiP window.
    
    After a PIP controller instance is created, call **startPiP** to start PiP. In the **ABOUT\_TO\_START** lifecycle, remove the typeNode from the layout and return to the upper-level page (optional). If returning to the upper-level page is enabled, you also need to redirect to the original page in the **ABOUT\_TO\_RESTORE** callback (during restoration).
    
3.  Update the media content size.
    
    After the PiP media content is updated (for example, the video is switched), call **updateContentSize** of the PiP controller instance to update the media content size and adjust the PiP window ratio.
    
4.  Stop the PiP window.
    
    When there is no need to display the PiP window, you can stop the PiP window by calling **stopPiP** of the PiP controller instance, and add the typeNode to the layout again in the **ABOUT\_TO\_STOP** lifecycle.
    

// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
// ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...
    windowStage.loadContent('pages/Index', (err) => {
      // ...
    });
  }
  // ...
}

// pages/NavigationImplementPage.ets
import { PipManager } from '../navigation/PipManager';
import { Page1 } from '../navigation/Page1';
import { PiPWindow } from '@kit.ArkUI';
import { Logger } from '../util/LogUtil';

const TAG = 'NavigationImplementPage';

@Entry
@Component
struct NavigationImplementPage {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  // Listen for the PiP lifecycle event, which is used for page and node operations.
  private callback: Function = (state: PiPWindow.PiPState) => {
    Logger.info(TAG, \`pipStateChange: state ${state}\`);
    if (state === PiPWindow.PiPState.ABOUT\_TO\_START) {
      // (Optional) Return to the upper-level page.
      this.pageInfos.pop();
    } else if (state === PiPWindow.PiPState.ABOUT\_TO\_STOP) {
      // Add the typeNode to the layout again, for example, in the restoration scenario.
      PipManager.getInstance().addNode();
    } else if (state === PiPWindow.PiPState.ABOUT\_TO\_RESTORE) {
      // If the upper-level page is returned in the ABOUT\_TO\_START callback, push the original page during the restoration.
      this.jumpNext();
    }
  };

  jumpNext() {
    if (this.pageInfos.getAllPathName()\[0\] === 'Page1') {
      Logger.info(TAG, 'Page1 already at top');
      return;
    }
    this.pageInfos.pushPath({ name: 'Page1' });
  }

  aboutToAppear(): void {
    PipManager.getInstance().registerLifecycleCallback(this.callback);
  }

  aboutToDisappear(): void {
    PipManager.getInstance().unregisterPipStateChangeListener();
    PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
  }

  @Builder
  PageMap(name: string) {
    if (name === 'Page1') {
      Page1();
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Text('This is Main Page')
        Column()
          .height('200px')
        Row({ space: 12 }) {
          Button('Jump Page1')
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.jumpNext();
            })
        }
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#DCDCDC')
    }
    .title('MainTitle')
    .navDestination(this.PageMap)
  }
}

// navigation/Page1.ets
import { PipManager } from './PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'Page1';

@Entry
@Component
export struct Page1 {
  build() {
    NavDestination() {
      Column() {
        Text('This is Page1')
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
          .margin({ bottom: 20 })

        // Add typeNode to the layout.
        NodeContainer(PipManager.getInstance().getNodeController())
          .size({ width: '100%', height: '800px' })

        Row({ space: 20 }) {
          Button('startPip') // Start PiP.
            .onClick(() => {
              PipManager.getInstance().startPip();
            })
          Button('stopPip') // Stop PiP.
            .onClick(() => {
              PipManager.getInstance().stopPip();
            })
          Button('updateSize') // Update the video size.
            .onClick(() => {
              // The width and height set here must be those of the media content and be obtained through media-related APIs or callbacks.
              // For example, when the AVPlayer is used to play a video, the videoSizeChange callback function can be used to obtain the updated media content size.
              PipManager.getInstance().updateContentSize(900, 1600);
            })
        }
        .backgroundColor('#4da99797')
        .size({ width: '100%', height: 60 })
        .justifyContent(FlexAlign.SpaceAround)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
    }
    .title('page1')
    .onShown(() => {
      Logger.info(TAG, 'onShown')
      PipManager.getInstance().init(this.getUIContext().getHostContext() as Context);
      PipManager.getInstance().setAutoStart(true);
    })
    .onHidden(() => {
      Logger.info(TAG, 'onHidden')
      PipManager.getInstance().setAutoStart(false);
      PipManager.getInstance().removeNode();
    })
  }
}

// navigation/XCNodeController.ets
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
import { PipManager } from './PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'XCNodeController';

// Create a custom NodeController.
export class XCNodeController extends NodeController {
  public xComponent: typeNode.XComponent| null = null;
  private node: FrameNode | null = null;
  private canAddNode: boolean = true;

  // Set whether nodes can be added.
  setCanAddNode(canAddNode: boolean) {
    this.canAddNode = canAddNode;
  }

  // Implement the makeNode method. This method is called when the custom NodeController is added to the layout.
  makeNode(context: UIContext): FrameNode | null {
    Logger.info(TAG, 'makeNode');
    this.node = new FrameNode(context);
    if (this.xComponent === null || this.xComponent === undefined) {
      // Create a typeNode of the XComponent type.
      this.xComponent = typeNode.createNode(context, 'XComponent', {
        type: XComponentType.SURFACE, // Set the type to SURFACE.
        controller: PipManager.getInstance().getXComponentController(), // Set an XComponentController.
      });
    }
    if (this.canAddNode) {

      try {
        this.xComponent.getParent()?.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
    return this.node;
  }

  // Add the typeNode again.
  addNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'addNode id:'+(this.node?.getUniqueId())+' '+this.xComponent?.getUniqueId());
      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
  }

  // Remove the typeNode.
  removeNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'removeNode');

      try {
        this.node.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
    }
  }

  getNode(): typeNode.XComponent | null {
    Logger.info(TAG, 'getNode is null:'+ (this.xComponent === null || this.xComponent === undefined))
    return this.xComponent;
  }

  // You need to define this method to unregister the layout to avoid memory leakage.
  dispose() {
    Logger.info(TAG, 'execute node dispose');
    if (this.node !== null) {
      this.node.dispose();
    }
  }
}

// navigation/PipManager.ets
import { PiPWindow, typeNode } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { XCNodeController } from './XCNodeController';
import { AVPlayer } from '../model/AVPlayer';
import { Logger } from '../util/LogUtil';

export class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceCreated surfaceId: ${surfaceId}\`);
    if (PipManager.getInstance().player.surfaceID === surfaceId) {
      return;
    }
    // Set the surface ID to the media source.
    PipManager.getInstance().player.surfaceID = surfaceId;
    PipManager.getInstance().player.avPlayerFdSrc();
  }

  onSurfaceDestroyed(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
  }
}

const TAG = 'PipManager';

export class PipManager {
  private static instance: PipManager = new PipManager();
  private pipController?: PiPWindow.PiPController = undefined;
  private xcNodeController: XCNodeController;
  private mXComponentController: XComponentController;
  private lifeCycleCallback: Set<Function> = new Set();
  public player: AVPlayer;

  public static getInstance(): PipManager {
    return PipManager.instance;
  }

  constructor() {
    this.xcNodeController = new XCNodeController();
    this.player = new AVPlayer();
    this.mXComponentController = new CustomXComponentController();
  }

  public registerLifecycleCallback(callBack: Function) {
    this.lifeCycleCallback.add(callBack);
  }

  public unRegisterLifecycleCallback(callBack: Function): void {
    this.lifeCycleCallback.delete(callBack);
  }

  getNode(): typeNode.XComponent | null {
    return this.xcNodeController.getNode();
  }

  onActionEvent(control: PiPWindow.ControlEventParam) {
    switch (control.controlType) {
      case PiPWindow.PiPControlType.VIDEO\_PLAY\_PAUSE:
        if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
         // Stop the video.
        } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
          // Play the video.
        }
        break;
      case PiPWindow.PiPControlType.VIDEO\_NEXT:
        // Switch to the next video.
        break;
      case PiPWindow.PiPControlType.VIDEO\_PREVIOUS:
        // Switch to the previous video.
        break;
      case PiPWindow.PiPControlType.FAST\_FORWARD:
        // Fast forward the video.
        break;
      case PiPWindow.PiPControlType.FAST\_BACKWARD:
        // Rewind the video.
        break;
      default:
        break;
    }
    Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
  }

  onStateChange(state: PiPWindow.PiPState, reason: string) {
    let curState: string = '';
    this.xcNodeController.setCanAddNode(
      state === PiPWindow.PiPState.ABOUT\_TO\_STOP || state === PiPWindow.PiPState.STOPPED)
    if (this.lifeCycleCallback !== null) {
      this.lifeCycleCallback.forEach((fun) => {
        fun(state);
      });
    }
    switch (state) {
      case PiPWindow.PiPState.ABOUT\_TO\_START:
        curState = 'ABOUT\_TO\_START';
        // Remove the typeNode from the layout.
        this.xcNodeController.removeNode();
        break;
      case PiPWindow.PiPState.STARTED:
        curState = 'STARTED';
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_STOP:
        curState = 'ABOUT\_TO\_STOP';
        this.xcNodeController.dispose();
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

  unregisterPipStateChangeListener() {
    Logger.info(\`${TAG} aboutToDisappear\`);
    this.pipController?.off('stateChange');
    this.pipController?.off('controlEvent');
    this.pipController = undefined;
  }

  getXComponentController(): CustomXComponentController {
    return this.mXComponentController;
  }

  // Step 1: Create a PiP controller, and register the lifecycle event callback and control event callback.
  init(ctx: Context) {
    if (this.pipController !== null && this.pipController != undefined) {
      return;
    }
    Logger.info(\`${TAG} onPageShow\`)
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(TAG, \`picture in picture disabled for current OS\`);
      return;
    }

    let config: PiPWindow.PiPConfiguration = {
      context: ctx,
      componentController: this.getXComponentController(),
      templateType: PiPWindow.PiPTemplateType.VIDEO\_PLAY,
      contentWidth: 1920, // When typeNode is used to start PiP, contentWidth must be set to a value greater than 0. Otherwise, the PIP fails to be created.
      contentHeight: 1080, // When typeNode is used to start PiP, contentHeight must be set to a value greater than 0. Otherwise, the PIP fails to be created.
    };
    // Use create to create a PiP controller instance.

    PiPWindow.create(config, this.xcNodeController.getNode()).then((controller: PiPWindow.PiPController) => {
      this.pipController = controller;
     // Use setAutoStartEnabled to set whether to automatically enable the PiP feature when users return to the home screen.
      this.pipController?.setAutoStartEnabled(true);
      // Use on('stateChange') to register the lifecycle event callback.
      this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
        this.onStateChange(state, reason);
      });
      // Use on('controlEvent') to register the control event callback.
      this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
        this.onActionEvent(control);
      });
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to create pip controller. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 2: Start PiP.
  startPip() {
    this.pipController?.startPiP().then(() => {
      Logger.info(TAG, \`Succeeded in starting pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to start pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 3: Update the media content size.
  updateContentSize(width: number, height: number) {
    if (this.pipController) {
      this.pipController.updateContentSize(width, height);
    }
  }

  // Step 4: Stop PiP.
  stopPip() {
    if (this.pipController === null || this.pipController === undefined) {
      return;
    }
    let promise: Promise<void> = this.pipController.stopPiP();
    promise.then(() => {
      Logger.info(TAG, \`Succeeded in stopping pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to stop pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  getNodeController(): XCNodeController {
    Logger.info(TAG, \`getNodeController.\`);
    return this.xcNodeController;
  }

  setAutoStart(autoStart: boolean): void {
    this.pipController?.setAutoStartEnabled(autoStart);
  }

  removeNode() {
    this.xcNodeController.removeNode();
  }

  addNode(): void {
    this.xcNodeController.addNode();
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/LGZkb4lLRmCBIHQ_g1kk4w/en-us_image_0000002529702009.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CE374A9702893BCEE43524DF5E649F68DAAB6E689B8F1D03FCA38A04EDF0D5D "Click to enlarge")

#### Using typeNode to Develop PiP When the Ability Has Only One Page

1.  Create a PiP controller, and register the lifecycle event callback and control event callback.
    
    -   Create a custom NodeController, implement the **makeNode** method, and create a typeNode in the method.
    -   Use **create(config: PiPConfiguration, contentNode: typeNode.XComponent)** to create a PIP controller instance.
    -   Use **setAutoStartEnabled** to set whether to automatically enable the PiP feature when users return to the home screen.
    -   Use **on('stateChange')** to register the lifecycle event callback.
    -   Use **on('controlEvent')** to register the control event callback.
    
2.  Start a PiP window.
    
    After a PIP controller instance is created, call **startPiP** to start PiP. In the **ABOUT\_TO\_START** lifecycle, remove the typeNode from the layout.
    
3.  Update the media content size.
    
    After the PiP media content is updated (for example, the video is switched), call **updateContentSize** of the PiP controller instance to update the media content size and adjust the PiP window ratio.
    
4.  Stop the PiP window.
    
    When there is no need to display the PiP window, you can stop the PiP window by calling **stopPiP** of the PiP controller instance, and add the typeNode to the layout again in the **ABOUT\_TO\_STOP** lifecycle.
    

// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
// ...
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // ...
    windowStage.loadContent('pages/Index', (err) => {
      // ...
    });
  }
  // ...
}

// pages/AbilityImplementPage.ets
import { PipManager } from '../ability/PipManager';
import { PiPWindow } from '@kit.ArkUI'; // Import the PiPWindow module.
import { Logger } from '../util/LogUtil';

const TAG = 'AbilityImplementPage'
@Entry
@Component
struct AbilityImplementPage {
  private callback: Function = (state: PiPWindow.PiPState) => {
    if (state === PiPWindow.PiPState.ABOUT\_TO\_STOP) {
      // The ABOUT\_TO\_STOP lifecycle is triggered when the PiP window is closed or restored, and you need to add the node again at this time.
      PipManager.getInstance().addNode();
    }
  };

  build() {
    Column() {
      Text('This is MainPage')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 20 })

      // Add typeNode to the layout.
      NodeContainer(PipManager.getInstance().getNodeController())
        .size({ width: '100%', height: '800px' })

      Row({ space: 20 }) {
        Button('startPip') // Start PiP.
          .onClick(() => {
            PipManager.getInstance().startPip();
          })

        Button('stopPip') // Stop PiP.
          .onClick(() => {
            PipManager.getInstance().stopPip();
          })

        Button('updateSize') // Update the video size.
          .onClick(() => {
            // The width and height set here must be those of the media content and be obtained through media-related APIs or callbacks.
            // For example, when the AVPlayer is used to play a video, the videoSizeChange callback function can be used to obtain the updated media content size.
            PipManager.getInstance().updateContentSize(900, 1600);
          })
      }
      .backgroundColor('#4da99797')
      .size({ width: '100%', height: 60 })
      .justifyContent(FlexAlign.SpaceAround)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }

  aboutToAppear(): void {
    PipManager.getInstance().registerLifecycleCallback(this.callback);
  }

  aboutToDisappear(): void {
    PipManager.getInstance().unregisterPipStateChangeListener();
    PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
  }

  onPageShow(): void {
    Logger.info(TAG, 'onPageShow')
    PipManager.getInstance().init(this.getUIContext().getHostContext() as Context);
    PipManager.getInstance().setAutoStart(true);
  }

  onPageHide(): void {
    Logger.info(TAG, 'onPageHide')
    PipManager.getInstance().setAutoStart(false);
  }
}

// ability/XCNodeController.ets
import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
import { PipManager } from './PipManager';
import { Logger } from '../util/LogUtil';

const TAG = 'XCNodeController';

// Create a custom NodeController.
export class XCNodeController extends NodeController {
  public xComponent: typeNode.XComponent | null = null;
  private node: FrameNode | null = null;
  private canAddNode: boolean = true;

  // Set whether nodes can be added.
  setCanAddNode(canAddNode: boolean) {
    this.canAddNode = canAddNode;
  }

  // Implement the makeNode method. This method is called when the custom NodeController is added to the layout.
  makeNode(context: UIContext): FrameNode | null {
    this.node = new FrameNode(context);
    this.node.commonAttribute
    if (this.xComponent === null || this.xComponent === undefined) {
      // Create a typeNode of the XComponent type.
      this.xComponent = typeNode.createNode(context, 'XComponent', {
        type: XComponentType.SURFACE, // Set the type to SURFACE.
        controller: PipManager.getInstance().getXComponentController(), // Set an XComponentController.
      });
    }
    if (this.canAddNode) {

      try {
        this.xComponent.getParent()?.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
    return this.node;
  }

  // Add the typeNode again.
  addNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'addNode');

      try {
        this.node.appendChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to appendChild');
      }
    }
  }

  // Remove the typeNode.
  removeNode() {
    if (this.node !== null && this.node !== undefined) {
      Logger.info(TAG, 'removeNode');

      try {
        this.node.removeChild(this.xComponent);
      } catch (error) {
        Logger.error(TAG, 'Failed to removeChild');
      }
    }
  }

  getNode(): typeNode.XComponent | null {
    Logger.info(TAG, 'getNode is null: '+ (this.xComponent === null || this.xComponent === undefined));
    return this.xComponent;
  }

  // You need to define this method to unregister the layout to avoid memory leakage.
  dispose() {
    Logger.info(TAG, 'execute node dispose');
    if (this.node !== null) {
      this.node.dispose();
    }
  }
}

// ability/PipManager.ets
import { PiPWindow, typeNode } from '@kit.ArkUI'; // Import the PiPWindow module.
import { BusinessError } from '@kit.BasicServicesKit';
import { XCNodeController } from './XCNodeController';
import { AVPlayer } from '../model/AVPlayer';
import { Logger } from '../util/LogUtil';

// Customize an XComponentController.
export class CustomXComponentController extends XComponentController {
  onSurfaceCreated(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceCreated surfaceId: ${surfaceId}\`);
    if (PipManager.getInstance().player.surfaceID === surfaceId) {
      return;
    }
    PipManager.getInstance().player.surfaceID = surfaceId;
    PipManager.getInstance().player.avPlayerFdSrc();
  }

  onSurfaceDestroyed(surfaceId: string): void {
    Logger.info(TAG, \`onSurfaceDestroyed surfaceId: ${surfaceId}\`);
  }
}

const TAG = 'PipManager';

export class PipManager {
  private static instance: PipManager = new PipManager();
  private pipController?: PiPWindow.PiPController = undefined;
  private xcNodeController: XCNodeController;
  private mXComponentController: XComponentController;
  private lifeCycleCallback: Set<Function> = new Set();
  public player: AVPlayer;

  public static getInstance(): PipManager {
    return PipManager.instance;
  }

  constructor() {
    this.xcNodeController = new XCNodeController();
    this.player = new AVPlayer();
    this.mXComponentController = new CustomXComponentController();
  }

  public registerLifecycleCallback(callBack: Function) {
    this.lifeCycleCallback.add(callBack);
  }

  public unRegisterLifecycleCallback(callBack: Function): void {
    this.lifeCycleCallback.delete(callBack);
  }

  getNode(): typeNode.XComponent | null {
    return this.xcNodeController.getNode();
  }

  onActionEvent(control: PiPWindow.ControlEventParam) {
    switch (control.controlType) {
      case PiPWindow.PiPControlType.VIDEO\_PLAY\_PAUSE:
        if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
         // Stop the video.
        } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
          // Play the video.
        }
        break;
      case PiPWindow.PiPControlType.VIDEO\_NEXT:
        // Switch to the next video.
        break;
      case PiPWindow.PiPControlType.VIDEO\_PREVIOUS:
        // Switch to the previous video.
        break;
      case PiPWindow.PiPControlType.FAST\_FORWARD:
        // Fast forward the video.
        break;
      case PiPWindow.PiPControlType.FAST\_BACKWARD:
        // Rewind the video.
        break;
      default:
        break;
    }
    Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
  }

  onStateChange(state: PiPWindow.PiPState, reason: string) {
    let curState: string = '';
    this.xcNodeController.setCanAddNode(
      state === PiPWindow.PiPState.ABOUT\_TO\_STOP || state === PiPWindow.PiPState.STOPPED);
    if (this.lifeCycleCallback !== null) {
      this.lifeCycleCallback.forEach((fun) => {
        fun(state);
      });
    }
    switch (state) {
      case PiPWindow.PiPState.ABOUT\_TO\_START:
        curState = 'ABOUT\_TO\_START';
        // Remove the typeNode from the layout.
        this.xcNodeController.removeNode();
        break;
      case PiPWindow.PiPState.STARTED:
        curState = 'STARTED';
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_STOP:
        curState = 'ABOUT\_TO\_STOP';
        this.xcNodeController.dispose();
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

  unregisterPipStateChangeListener() {
    Logger.info(\`${TAG} aboutToDisappear\`);
    this.pipController?.off('stateChange');
    this.pipController?.off('controlEvent');
  }

  getXComponentController(): CustomXComponentController {
    return this.mXComponentController;
  }

  // Step 1: Create a PiP controller, and register the lifecycle event callback and control event callback.
  init(ctx: Context) {
    if (this.pipController !== null && this.pipController != undefined) {
      return;
    }
    Logger.info(\`${TAG} onPageShow\`)
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(TAG, \`picture in picture disabled for current OS\`);
      return;
    }
    let config: PiPWindow.PiPConfiguration = {
      context: ctx,
      componentController: this.getXComponentController(),
      templateType: PiPWindow.PiPTemplateType.VIDEO\_PLAY,
      contentWidth: 1920, // When typeNode is used to start PiP, contentWidth must be set to a value greater than 0. Otherwise, the PIP fails to be created.
      contentHeight: 1080, // When typeNode is used to start PiP, contentHeight must be set to a value greater than 0. Otherwise, the PIP fails to be created.
    };
    // Use create to create a PiP controller instance.

    PiPWindow.create(config, this.xcNodeController.getNode()).then((controller: PiPWindow.PiPController) => {
      this.pipController = controller;
     // Use setAutoStartEnabled to set whether to automatically enable the PiP feature when users return to the home screen.
      this.pipController?.setAutoStartEnabled(true);
      // Use on('stateChange') to register the lifecycle event callback.
      this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
        this.onStateChange(state, reason);
      });
      // Use on('controlEvent') to register the control event callback.
      this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
        this.onActionEvent(control);
      });
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to create pip controller. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 2: Start PiP.
  startPip() {
    this.pipController?.startPiP().then(() => {
      Logger.info(TAG, \`Succeeded in starting pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to start pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  // Step 3: Update the media content size.
  updateContentSize(width: number, height: number) {
    if (this.pipController) {
      this.pipController.updateContentSize(width, height);
    }
  }

  // Step 4: Stop PiP.
  stopPip() {
    if (this.pipController === null || this.pipController === undefined) {
      return;
    }
    let promise: Promise<void> = this.pipController.stopPiP();
    promise.then(() => {
      Logger.info(TAG, \`Succeeded in stopping pip.\`);
    }).catch((err: BusinessError) => {
      Logger.error(TAG, \`Failed to stop pip. Cause:${err.code}, message:${err.message}\`);
    });
  }

  getNodeController(): XCNodeController {
    Logger.info(TAG, \`getNodeController.\`);
    return this.xcNodeController;
  }

  setAutoStart(autoStart: boolean): void {
    this.pipController?.setAutoStartEnabled(autoStart);
  }

  // Add the typeNode to the original parent node.
  addNode(): void {
    this.xcNodeController.addNode();
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/AExxw1OVTwy88-9p9N2UvA/en-us_image_0000002529582041.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=466BA83386EDCFA1B14BD69E5140B435B317E8ACD21D09065B9DA195E4A77104 "Click to enlarge")
