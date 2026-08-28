# Reading Control

#### Application Scenario

The reading control is widely used when it is inconvenient for a user to view texts on the screen, and the control will read news and provide information for the user.

This section describes how to use the reading control, as shown in the following figures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/t9RCIWbKR7SYf8HfnLgpNQ/en-us_image_0000002533509989.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B58AEC2C4C55E24557D92F21C037E25DC68DF7C26219C91A953510D65A8BCC6)

#### API Description

The following lists only some main APIs called in the demo. For details about all APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api#section173751154134515)(context: [common.BaseContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-basecontext), readParams: [ReaderParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api#section6129163245310)): Promise<void>

 | 

Initializes **TextReader**.

 |
| 

[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api#section143611912403)(readInfoList: [ReadInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api#section129918404172)\[\], articleId?: string): Promise<void>

 | 

Starts **TextReader**.

 |
| 

on(type: string, callback: function): void

 | 

Registers callbacks for all events. For details about the event types, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-textreader-api).

 |

#### Development Procedure

1.  Open the **/src/main/ets/entryability/EntryAbility.ets** file in the project root directory and add the WindowManager to the project.
    
    import { WindowManager } from '@kit.SpeechKit';
    import { ConfigurationConstant } from '@kit.AbilityKit';
    
2.  (Optional) Add the **setWindowStage** method to **onWindowStageCreate(windowStage: window.WindowStage)** to set the window manager.
    
    onWindowStageCreate(windowStage: window.WindowStage): void {
      console.info('Ability onWindowStageCreate');
      WindowManager.setWindowStage(windowStage);
      
      windowStage.loadContent('pages/Index', (err, data) => {
        if (err) {
          console.error(\`Failed to load the content. Code: ${err.code}, message: ${err.message}\`);
          return;
        }
        console.info(\`Succeeded in loading the content. Data: ${JSON.stringify(data)}.\` );
      });
    }
    
3.  Set the color mode of the app through the **onCreate()** lifecycle method to ensure that the color mode of the control is the same as that of the app.
    
    -   To synchronize the app's color mode with the system, set the mode to **COLOR\_MODE\_NOT\_SET**.
    -   To configure the color mode of the app, set the mode to **COLOR\_MODE\_LIGHT** (light) or **COLOR\_MODE\_DARK** (dark).
    
    Synchronizing the color mode with the system is used as an example.
    
    onCreate(): void {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
    }
    
4.  Add the **TextReader** class and other related classes to the **/src/main/ets/pages/Index.ets** file in the project root directory.
    
    import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';
    
5.  Configure the page layout, add the receiver icon, and set the **onClick** event.
    
    /\*\*
     \* Playback state.
     \*/
    @State readState: ReadStateCode = ReadStateCode.WAITING;
    
    build() {
        Column() {
          TextReaderIcon({ readState: this.readState })
            .margin({ right: 20 })
            .width(32)
            .height(32)
            .onClick(() => {
                // Set the click event.
                // ...
            })
        }
    }
    
6.  Initialize the reading control.
    
    // Display the button status on the current page.
    @State isInit: boolean = false;
    /\*\*
    \* Articles to load.
    \*/
    @State readInfoList: TextReader.ReadInfo\[\] = \[\];
    @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList\[0\];
    
    async aboutToAppear() {
      // ...
      void this.init();
      /\*\*
       \* Load the data.
       \*/
      let readInfoList: TextReader.ReadInfo\[\] = \[{
        id: '001',
        title: {
          text:'_Title of the text to read_',
          isClickable:true
        },
        author:{
          text:'_Author of the text to read_',
          isClickable:true
        },
        date: {
          text:'2024/01/01',
          isClickable:false
        },
        bodyInfo: '_Text body to read_'
      }\];
      this.readInfoList = readInfoList;
      this.selectedReadInfo = this.readInfoList\[0\];
      // ...
    }
    
    /\*\*
     \* Initialization.
     \*/
    async init() {
      const readerParam: TextReader.ReaderParam = {
        isVoiceBrandVisible: true,
        businessBrandInfo: {
          panelName: 'AI Reader',
          panelIcon: $r('app.media.startIcon')
        }
      }
      try {
        let context: Context | undefined = this.getUIContext().getHostContext()
        if (context) {
          await TextReader.init(context, readerParam);
          this.isInit = true;
          this.setActionListener();
        }
      } catch (err) {
        console.error(\`TextReader failed to init. Code: ${err.code}, message: ${err.message}\`);
      }
    }
    
    onStateChanged = (state: TextReader.ReadState) => {
      if (this.selectedReadInfo?.id === state.id) {
        this.readState = state.state;
      } else {
        this.readState = ReadStateCode.WAITING;
      }
    }
    
    // Set action listeners.
    setActionListener() {
      TextReader.on('stateChange', (state: TextReader.ReadState) => {
        this.onStateChanged(state);
      });
      // When there is no more content on the list page, a loading failure message will be displayed. To get correct display information, you need to set a **requestMore** listener and call the **loadMore** function.
      TextReader.on('requestMore', () => {
        TextReader.loadMore(\[\], true);
      })
    }
    
    // Unregister the listeners. Call this method at an appropriate time based on your service needs.
    releaseActionListener() {
      TextReader.off('stateChange');
      TextReader.off('requestMore');
    }
    
7.  (Optional) Use the **setActionListener** method to set more listeners that trigger callbacks when users interact with the control. Unregister the listeners and release resources after the listening is complete.
    
    // Set the listeners.
    setActionListener() {
      TextReader.on('setArticle', async (id: string) => { console.info(\`setArticle ${id}\`) });
      TextReader.on('clickArticle', (id: string) => {console.info(\`onClickArticle ${id}\`) });
      TextReader.on('clickAuthor', (id: string) => { console.info(\`onClickAuthor ${id}\`) });
      TextReader.on('clickNotification',  (id: string) => { console.info(\`onClickNotification ${id}\`) });
      TextReader.on('showPanel', () => { console.info(\`onShowPanel\`) });
      TextReader.on('hidePanel', () => { console.info(\`onHidePanel\`) });
      // ...
    }
    // Unregister the listeners.
    releaseActionListener() {
      TextReader.off('setArticle');
      TextReader.off('clickArticle');
      TextReader.off('clickAuthor');
      TextReader.off('clickNotification');
      TextReader.off('showPanel');
      TextReader.off('hidePanel');
      // ...
    }
    
8.  Start the reading control.
    
    build() {
      Column() {
        TextReaderIcon({ readState: this.readState })
          // ...
          .onClick(() => {
            try {
              void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
            } catch (err) {
              console.error(\`TextReader failed to start. Code: ${err.code}, message: ${err.message}\`);
            }
          })
      }
    }
    
9.  (Optional) To configure a long-duration task, add the **ohos.permission.KEEP\_BACKGROUND\_RUNNING** permission to the [module.json5 configuration file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md), add the **backgroundModes** option, and then set **keepBackgroundRunning** to **true** in **readerParam** to ensure that the background playback of the reading control is normal.
    
    // module.json5
    {
      "module": {
        // ...
        "requestPermissions": \[
          {
            "name": "ohos.permission.KEEP\_BACKGROUND\_RUNNING",
            "usedScene": {
              "abilities": \[
                "FormAbility"
              \],
              "when": "inuse"
            }
          },
        \],
        "abilities": \[
          {
            // ...
            "backgroundModes": \[
              "audioPlayback"
            \],
            // ...
          }
        \]
      }
    }
    
    // Index.ets
    async init() {
      const readerParam: TextReader.ReaderParam = {
        // ...
        keepBackgroundRunning: true
      }
    }
    
10.  (Optional) To ensure normal timbre switching during reading control usage, add the **ohos.permission.INTERNET** and **ohos.permission.GET\_NETWORK\_INFO** permissions to the [module.json5 configuration file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
     
     // module.json5
     {
       "module": {
         // ...
         "requestPermissions": \[
           {
             "name": "ohos.permission.INTERNET",
             "reason": "$string:reason",
             "usedScene": {"abilities": \[\]}
           },
           {
             "name": "ohos.permission.GET\_NETWORK\_INFO",
             "reason": "$string:reason",
             "usedScene": {"abilities": \[\]}
           },
         \],
       }
     }
     

#### Development Example

EntryAbility.ets

import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { WindowManager } from '@kit.SpeechKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
    } catch (err) {
      console.error(\`error code: ${err.code}, message: ${err.message}.\`)
    }
    console.info('Ability onCreate');
  }

  onDestroy(): void {
    console.info('Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('Ability onWindowStageCreate');
    WindowManager.setWindowStage(windowStage);

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(\`Failed to load the content. Code: ${err.code}, message: ${err.message}\`);
        return;
      }
      console.info(\`Succeeded in loading the content. Data: ${JSON.stringify(data)}.\` );
    });
  }

  onWindowStageDestroy(): void {
    console.info('Ability onWindowStageDestroy');
  }

  onForeground(): void {
    console.info('Ability onForeground');
  }

  onBackground(): void {
    console.info('Ability onBackground');
  }
}

Index.ets

import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

@Entry
@Component
struct Index {

  /\*\*
   \* Articles to load.
   \*/
  @State readInfoList: TextReader.ReadInfo\[\] = \[\];
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList\[0\];

  /\*\*
   \* Playback state.
   \*/
  @State readState: ReadStateCode = ReadStateCode.WAITING;

  /\*\*
   \* Display the button status on the current page.
   \*/
  @State isInit: boolean = false;

  aboutToAppear(){
    /\*\*
     \* Load the data.
     \*/
    let readInfoList: TextReader.ReadInfo\[\] = \[{
      id: '001',
      title: {
        text:'_Title of the text to read_',
        isClickable:true
      },
      author:{
        text:'_Author of the text to read_',
        isClickable:true
      },
      date: {
        text:'2024/01/01',
        isClickable:false
      },
      bodyInfo: '_Text body to read_'
    }\];
    this.readInfoList = readInfoList;
    this.selectedReadInfo = this.readInfoList\[0\];
    void this.init();
  }

  /\*\*
   \* Initialization.
   \*/
  async init() {
    const readerParam: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: 'AI Reader',
        panelIcon: $r('app.media.startIcon')
      }
    }
    try {
      let context: Context | undefined = this.getUIContext().getHostContext()
      if (context) {
        await TextReader.init(context, readerParam);
        this.isInit = true;
        this.setActionListener();
      }
    } catch (err) {
      console.error(\`TextReader failed to init. Code: ${err.code}, message: ${err.message}\`);
    }
  }

  // Set action listeners.
  setActionListener() {
    TextReader.on('stateChange', (state: TextReader.ReadState) => {
      this.onStateChanged(state);
    });

    TextReader.on('requestMore', () => {
      TextReader.loadMore(\[\], true);
    })
  }

  onStateChanged = (state: TextReader.ReadState) => {
    if (this.selectedReadInfo?.id === state.id) {
      this.readState = state.state;
    } else {
      this.readState = ReadStateCode.WAITING;
    }
  }

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(() => {
          try {
            void TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch (err) {
            console.error(\`TextReader failed to start. Code: ${err.code}, message: ${err.message}\`);
          }
        })
    }
    .height('100%')
  }
}

#### Adaptation Process for 2-in-1 Devices

In addition to the development steps in [Development Procedure](#section1418318341804), you also need to perform the following steps for 2-in-1 devices. Otherwise, the playback panel cannot be shown.

1.  Create an ability in **/src/main/ets/entryability** to host the main window of the 2-in-1 device and import related dependencies.
    
    import { TextReader, WindowManager } from '@kit.SpeechKit';
    import { commonEventManager } from '@kit.BasicServicesKit';
    
2.  Declare a global status variable **isReadyToStart** in the new ability and manage the status variable using **AppStorage**.
    
    private link: SubscribedAbstractProperty<boolean>= AppStorage.link('isReadyToStart');
    
3.  Create a global status variable **isReadyToStart** in the **aboutToAppear** lifecycle method of **Index.ets**.
    
    aboutToAppear() {
      AppStorage.setOrCreate('isReadyToStart', false);
      // Other configurations.
    }
    
4.  Configure **WindowStage**. Note that the following logic is used from version 6.0.0(20). For 5.1.1(19) and earlier versions, the **getContext(this)** API is used.
    
    -   In the **onWindowStageCreate** lifecycle method of the new ability, publish the **onLoadSubAbility** event.
    -   Set **windowStage** of the new ability using **WindowManager.setWindowStage(windowStage)**.
    -   Set **isReadyToStart** to **true** in **onWindowStageCreate**.
    
    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      WindowManager.setWindowStage(windowStage)
      let eventData: emitter.EventData = {
        data: {
          'state': 'publish'
        }
      }
      emitter.emit("onLoadSubAbility", eventData);
      this.link.set(true);
    }
    
5.  In the **onWindowStageDestroy** lifecycle method of the new ability, set **isReadyToStart** to **false**. Additionally, hide the panel and stop the playback.
    
    async onWindowStageDestroy(): Promise<void> {
      try {
        TextReader.hidePanel();
        await TextReader.stop();
        this.link.set(false);
      }catch (e) {
        console.error(\`onWindowStageDestroy fail , msg: ${e}\`)
      }
    }
    
6.  In **entryability**, set the **onShowPanel** callback in **onCreate** using **eventHub** to create a new ability. In the **onShowPanel** callback, construct **want** first, and then create a new ability through the **context.startAbility** API.
    
    import { AbilityConstant, Want } from '@kit.AbilityKit';
    import { common } from "@kit.AbilityKit";
    import { BusinessError } from "@kit.BasicServicesKit";
    
    
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      // Other configurations.
      let eventHub = this.context.eventHub;
      eventHub.on('onShowPanel', this.onShowPanel);
    }
    
    onShowPanel = () => {
      let context: common.UIAbilityContext = this.context;
      let want: Want = {
        deviceId: '',
        bundleName: 'com.example.speechkit', // Replace the bundle name with the actual one.
        abilityName: 'SubAbility',
        parameters: {
          info: 'From EntryAbility onShowPanel'
        }
      }
      context?.startAbility(want).then(() => {
        console.info('Succeeded in starting ability');
      }).catch((e: BusinessError) => {
        console.error(\`Failed to start ability. Code is ${e.code}, message is ${e.message}\`);
      })
    }
    
7.  Before calling **start**, check the device type. If the device is a 2-in-1 device, emit the **onShowPanel** event to construct an ability.
    
    import { deviceInfo } from '@kit.BasicServicesKit';
    
    if (deviceInfo.deviceType === '2in1') {
      let context = this.getUIContext().getHostContext();
      context?.eventHub.emit('onShowPanel');
    }
    try {
      TextReader.showPanel();
    } catch (err) {
      console.error(\`error code: ${err.code}, message: ${err.message}.\`)
    }
    
8.  Add the ability configurations to **module.json5**. Set **max** and **min** values to the same to fix the window size.
    
    {
      "name": "SubAbility", // Name of the **UIAbility** component.
      "srcEntry": "./ets/entryability/SubAbility.ets", // Code path of the **UIAbility** component.
      "description": "$string:SubAbility\_desc", // Description of the **UIAbility** component.
      "icon": "$media:icon", // Icon of the **UIAbility** component.
      "label": "$string:EntryAbility\_label", // Label of the **UIAbility** component.
      "startWindowIcon": "$media:icon", // Index of the resource file for the icon on the **UIAbility** startup page.
      "startWindowBackground": "$color:start\_window\_background", // Index of the resource file for the background color of the **UIAbility** startup page.
      "supportWindowMode": \['floating'\], // The window supports display in floating mode.
      "maxWindowWidth": 1158,  // Maximum window width.
      "minWindowWidth": 1158,  // Minimum window width.
      "maxWindowHeight": 772,  // Maximum window height.
      "minWindowHeight": 772,  // Minimum window height.
     }
