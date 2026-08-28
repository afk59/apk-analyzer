# Adding App Icons to Status Bar

This section describes how to display your app icon in the status bar, and show a custom pop-up window when users click the icon and a custom menu when users right-click the icon. Upon app exit, the icon will be removed from the status bar as the app process is destroyed.

Since version 6.0.2(22), the content displayed can be updated when the cursor hovers over an app icon in the status bar.

#### API Description

The following lists the APIs related to operating an app icon in the status bar. For details, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-kQAo0pPQ4OBD_WUWJbNoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=099708CC50C069E1D1BF7C929E48C159CCE6D78DA7EC52ABC1EF183383BAC73F)

The APIs provided by DeskTop Extension Kit take effect only on 2-in-1 devices.

**Table 1** APIs related to operating an app icon in the status bar
| 
API

 | 

Description

 |
| :-- | :-- |
| 

[addToStatusBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section665018220561)(context: common.Context, statusBarItem: StatusBarItem): void

 | 

Adds an app icon to the status bar.

 |
| 

[removeFromStatusBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section8931134111810)(context: common.Context): void

 | 

Removes an app icon from the status bar.

 |
| 

[updateQuickOperationHeight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1797215174100)(context: common.Context, height: number): void

 | 

Updates the height of the custom area in the pop-up window displayed when users click an app icon in the status bar.

 |
| 

[updateStatusBarMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section188071452172811)(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu\[\]): void

 | 

Updates the information about menu items displayed when users right-click an app icon in the status bar.

 |
| 

[updateStatusBarIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1728610265620)(context: common.Context, statusBarIcon: StatusBarIcon): void

 | 

Updates the icon in the status bar.

 |
| 

[updateStatusBarHoverTips](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section0391124717248)(context: common.Context, hoverTips: string): Promise<void>

 | 

Updates the content displayed when the cursor hovers over an app icon in the status bar.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section18493519506)(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void

 | 

Listens for status bar icon click events.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section896154419154)(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void

 | 

Unregisters status bar icon click events.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section10893144462716)(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void

 | 

Listens for status bar menu right-click events.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section5394166163416)(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void

 | 

Unregisters status bar menu right-click events.

 |

#### Development Procedure

1.  Import required modules.
    
    import { statusBarManager, StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
    import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
    import { image } from '@kit.ImageKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { emitter } from '@kit.BasicServicesKit';
    
2.  Create a **MyStatusBarViewAbility.ets** file (for example, in the **entry/src/main/ets/statusbarviewextensionability** folder) and a **StatusBarPage** page (for example, in the **entry/src/main/ets/pages** directory). This page is displayed in the pop-up window when users click an app icon in the status bar. Then build the custom **StatusBarViewExtensionAbility**.
    
    let TAG = 'MyStatusBarViewExtAbility';
    export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
      onCreate() {
        console.info(TAG, \`onCreate\`);
      }
    
      onSessionCreate(want: Want, session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionCreate, want: ${want.abilityName}\`);
        // **pages/StatusBarPage** is displayed in the pop-up window when users click an app icon in the status bar.
        session.loadContent('pages/StatusBarPage');
      }
    
      onForeground() {
        console.info(TAG, \`onForeground\`);
      }
    
      onBackground() {
        console.info(TAG, \`onBackground\`);
      }
    
      onSessionDestroy(session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionDestroy\`);
      }
    
      onDestroy() {
        console.info(TAG, \`onDestroy\`);
      }
    }
    
3.  Configure the extension ability information in the **module.json5** file in the module to which **MyStatusBarViewAbility** belongs.
    
    "extensionAbilities": \[
      {
        "name": "MyStatusBarViewAbility",
        "icon": "$media:startIcon",
        "description": "statusBar",
        "type": "statusBarView",
        "exported": true,
        // File path to which the **MyStatusBarViewAbility** class belongs.
        "srcEntry": "./ets/statusbarviewextensionability/MyStatusBarViewAbility.ets"
      }
    \]
    
4.  In the **rawfile** folder (for example, **entry/src/main/resources/rawfile**) of the corresponding module, preset two 24 [vp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-pixel-units) x 24 vp images (**testWhite.png** and **testBlack.png** in this example). Configure the icon information displayed in the status bar in the page component (for example, **index.ets**).
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error('getHostContext failed');
      return;
    }
    // Obtain a resource manager.
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    
    // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
    const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
    const whiteBuffer = whiteFileData.buffer;
    const whiteImageSource = image.createImageSource(whiteBuffer);
    let whitePixelMap = await whiteImageSource.createPixelMap();
    
    // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size 24 vp x 24 vp in the **rawfile** folder.
    const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
    const blackBuffer = blackFileData.buffer;
    const blackImageSource = image.createImageSource(blackBuffer);
    let blackPixelMap = await blackImageSource.createPixelMap();
    
    // Build icon information.
    let icon: statusBarManager.StatusBarIcon = {
      white: whitePixelMap,
      black: blackPixelMap
    }
    
5.  Configure information about the pop-up window displayed when users click an app icon in the status bar.
    
    // Build information about the pop-up window displayed when users click an app icon in the status bar. 
    let operation: statusBarManager.QuickOperation = {
      // **abilityName** is the **StatusBarViewExtensionAbility** name configured in the **module.json5** file.
      abilityName: "MyStatusBarViewAbility",
      title: "Test Demo",
      height: 300,
      // Can be left empty.
      moduleName: 'entry'
    };
    
6.  (Optional) Configure information about menu items displayed when users right-click an app icon in the status bar. You can add menu items to the status bar.
    
    // Build information about menu items displayed after users right-click an app icon in the status bar.
    let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
    let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
      abilityName: "EntryAbility"
    }
    let subMenu: statusBarManager.StatusBarSubMenuItem = {
      subTitle: "Submenu item",
      menuAction: subMenuItemAction
    }
    subMenus.push(subMenu);
    
    let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
    let menuItem: statusBarManager.StatusBarMenuItem = {
      title: "Level-1 menu item",
      // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
      subMenu: subMenus
    };
    statusBarMenuItems.push(menuItem);
    
    let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
    statusBarGroupMenus.push(statusBarMenuItems);
    
7.  Integrate the configuration information and display the app icon in the status bar.
    
    // Build information about the icon added to the status bar.
    let item: statusBarManager.StatusBarItem = {
      icons: icon,
      quickOperation: operation,
      // This parameter is optional.
      statusBarGroupMenu: statusBarGroupMenus
    };
    
    try {
      statusBarManager.addToStatusBar(context, item);
    } catch (error) {
      console.error(\`addToStatusBar failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
8.  (Optional) Call [updateStatusBarMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section188071452172811) to update the menu in the status bar.
    
    // Build information about menu items displayed after users right-click an app icon in the status bar.
    let subMenus: Array<statusBarManager.StatusBarSubMenuItem> = \[\];
    let subMenuItemAction: statusBarManager.StatusBarMenuAction = {
      abilityName: "EntryAbility"
    }
    let subMenu: statusBarManager.StatusBarSubMenuItem = {
      subTitle: "Level-2 menu item",
      menuAction: subMenuItemAction
    }
    subMenus.push(subMenu);
    
    let statusBarMenuItems: Array<statusBarManager.StatusBarMenuItem> = \[\];
    let menuItem: statusBarManager.StatusBarMenuItem = {
      title: "Level-1 menu item",
      // **menuAction** and **subMenu** cannot be left empty at the same time for a level-1 menu item.
      subMenu: subMenus
    };
    statusBarMenuItems.push(menuItem);
    
    let statusBarGroupMenus: Array<statusBarManager.StatusBarGroupMenu> = \[\];
    statusBarGroupMenus.push(statusBarMenuItems);
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error('getHostContext failed');
      return;
    }
    try {
      statusBarManager.updateStatusBarMenu(context, statusBarGroupMenus);
    } catch (error) {
      console.error(\`updateStatusBarMenu failed. error code: ${error.code}, error message: ${error.message}\`);
    }
    
9.  (Optional) Call [updateQuickOperationHeight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1797215174100) to update the height of the pop-up window displayed when users click the app icon in the status bar.
    
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error('getHostContext failed');
      return;
    }
    let height = 200;
    statusBarManager.updateQuickOperationHeight(context, height);
    
10.  (Optional) Call [updateStatusBarIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1728610265620) to update the app icon in the status bar.
     
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (!context) {
       console.error('getHostContext failed');
       return;
     }
     // Obtain a resource manager.
     const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     
     // Create white **pixelMap**. You need to preset the **testWhite.png** image with a size of 24 vp x 24 vp in the **rawfile** folder.
     const whiteFileData = resourceMgr.getRawFileContentSync('testWhite.png');
     const whiteBuffer = whiteFileData.buffer;
     const whiteImageSource = image.createImageSource(whiteBuffer);
     let whitePixelMap = await whiteImageSource.createPixelMap();
     
     // Create black **pixelMap**. You need to preset the **testBlack.png** image with a size 24 vp x 24 vp in the **rawfile** folder.
     const blackFileData = resourceMgr.getRawFileContentSync('testBlack.png');
     const blackBuffer = blackFileData.buffer;
     const blackImageSource = image.createImageSource(blackBuffer);
     let blackPixelMap = await blackImageSource.createPixelMap();
     
     // Build icon information.
     let icons: statusBarManager.StatusBarIcon = {
       white: whitePixelMap,
       black: blackPixelMap
     }
     statusBarManager.updateStatusBarIcon(context, icons);
     
11.  (Optional) Call [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section18493519506)/[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section896154419154) to customize the pop-up window displayed when users click an app icon in the status bar if the **abilityName** of [QuickOperation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1139214183436) is not specified.
     
     private onStatusBarIconClick = (eventData: emitter.EventData) => {
       // Customize the pop-up window displayed when users click an app icon.
       let data = eventData.data;
       if (data) {
         switch (data\['iconClickType'\]) {
           case 'leftClickType':
             // Customize the pop-up window displayed when users click an app icon.
             break;
           default:
             break;
         }
       }
     }
     
     // Listen for status bar icon click events.
     statusBarManager.on('statusBarIconClick', this.onStatusBarIconClick);
     
     // Unregister status bar icon click events.
     statusBarManager.off('statusBarIconClick', this.onStatusBarIconClick);
     
12.  (Optional) Call [updateStatusBarMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section188071452172811) to specify **notifyOnly** and **menuCode** for [StatusBarMenuAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section1196811528487) and call [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section18493519506)/[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section896154419154) to customize the menu displayed when users right-click an app icon in the status bar.
     
     private onRightMenuClick = (eventData: emitter.EventData) => {
       // Customize the menu displayed when users right-click an app icon.
       let data = eventData.data;
       if (data) {
         let menuCode = data\['menuCode'\] as string;
         // Process the click on a menu item.
       }
     }
     
     // Listen for status bar menu right-click events.
     statusBarManager.on('rightMenuClick', this.onRightMenuClick);
     
     // Unregister status bar menu right-click events.
     statusBarManager.off('rightMenuClick', this.onRightMenuClick);
     
13.  (Optional) Call [updateStatusBarHoverTips](https://developer.huawei.com/consumer/en/doc/harmonyos-references/statusbar-extension-manager#section0391124717248) to customize the content displayed when the cursor hovers over an app icon in the status bar.
     
     let context: Context | undefined = this.getUIContext().getHostContext();
     if (!context) {
       console.error('getHostContext failed');
       return;
     }
     let hoverTips: string = 'hoverTips';
     try {
       await statusBarManager.updateStatusBarHoverTips(context, hoverTips);
     } catch (err) {
       console.error(\`updateStatusBarHoverTips ${err.message} ${err.code}\`)
     }
     

#### Full Sample Code

For the complete sample code, please refer to the [status-bar-extension-kit-samplecode](https://gitcode.com/HarmonyOS_Samples/status-bar-extension-kit-samplecode).
