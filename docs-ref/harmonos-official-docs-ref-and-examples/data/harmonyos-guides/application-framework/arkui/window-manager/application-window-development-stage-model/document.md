# Application Window Development (Stage Model)

#### Basic Concepts

-   Immersive window: a window display mode where the system windows (generally the status bar and navigation bar) are hidden to allow users to fully engage with the content. The immersive window feature is applicable only to the main window of an application in full-screen mode. It does not apply to a main window in freeform window mode or an auxiliary window (for example, a child window or a global floating window).
    
-   Global floating window: a special type of application auxiliary window that can remain displayed on the foreground even after the application's main window and corresponding ability are moved to the background. Global floating windows can be used to continue displaying the UI in a small window after the application is moved to the background, such as displaying lyrics on the home screen for a music application. Before creating a global floating window, the application needs to request the corresponding permission.
    

#### When to Use

In the stage model, you can perform the following operations during application window development:

-   Setting the properties and content of the main window of an application
    
-   Setting the properties and content of the child window of an application
    
-   Experiencing the immersive window feature
    
-   Setting a global floating window
    
-   Listening for interactive and non-interactive window events
    

The following describes the development procedure specific to each application scenario.

#### Available APIs

The table below lists the common APIs used for application window development. For details about more APIs, see [Window](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window).

| Instance | API | Description |
| :-- | :-- | :-- |
| WindowStage | getMainWindow(callback: AsyncCallback<Window>): void | 
Obtains the main window of this window stage.

This API can be used only in the stage model.

 |
| WindowStage | loadContent(path: string, callback: AsyncCallback<void>): void | 

Loads content to the main window in this window stage.

**path**: path of the page from which the content will be loaded. The path is configured in the **main\_pages.json** file of the project.

This API can be used only in the stage model.

 |
| WindowStage | createSubWindow(name: string, callback: AsyncCallback<Window>): void | 

Creates a child window.

This API can be used only in the stage model.

 |
| WindowStage | on(eventType: 'windowStageEvent', callback: Callback<WindowStageEventType>): void | 

Subscribes to window stage lifecycle change events.

This API can be used only in the stage model.

 |
| Window static method | createWindow(config: Configuration, callback: AsyncCallback<Window>): void | 

Creates a child window or system window.

**config**: parameters used for creating the window.

 |
| Window | setUIContent(path: string, callback: AsyncCallback<void>): void | 

Loads the content of a page, with its path in the current project specified, to this window.

**path**: path of the page from which the content will be loaded. The path is configured in the **main\_pages.json** file of the project in the stage model.

 |
| Window | setWindowBrightness(brightness: number, callback: AsyncCallback<void>): void | Sets the brightness for this window. |
| Window | setWindowTouchable(isTouchable: boolean, callback: AsyncCallback<void>): void | Sets whether this window is touchable. **true** if touchable, **false** otherwise. |
| Window | moveWindowTo(x: number, y: number, callback: AsyncCallback<void>): void | Moves this window. |
| Window | resize(width: number, height: number, callback: AsyncCallback<void>): void | Changes the window size. |
| Window | setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> | Sets whether to enable an immersive layout for the main window or child window. **true** to enable, **false** otherwise. |
| Window | setWindowSystemBarEnable(names: Array<'status'|'navigation'>): Promise<void> | 

Sets whether to show the main window's status bar and bottom navigation (which may appear as a navigation bar or a three-button navigation bar depending on user settings). The display of the status bar and bottom navigation is controlled by status, and the navigation parameter does not have any impact.

For example, if this parameter is set to **\['status', 'navigation'\]**, all of them are shown. If this parameter is set to **\[\]**, they are hidden.

 |
| Window | setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Promise<void> | 

Sets the properties of the status bar and navigation bar in this window.

**systemBarProperties**: properties of the status bar and navigation bar.

 |
| Window | showWindow(callback: AsyncCallback<void>): void | Shows this window. |
| Window | on(type: 'touchOutside', callback: Callback<void>): void | Subscribes to touch events outside this window. |
| Window | destroyWindow(callback: AsyncCallback<void>): void | Destroys this window. |

#### Setting the Main Window of an Application

In the stage model, the main window of an application is created and maintained by a UIAbility instance. In the **onWindowStageCreate** callback of the UIAbility instance, use **WindowStage** to obtain the main window of the application and set its properties. You can also set the properties (for example, **maxWindowWidth**) in the [abilities tag of the module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities).

## How to Develop

1.  Obtain the main window.
    
    Call **getMainWindow** to obtain the main window of the application.
    
2.  Set the properties of the main window.
    
    You can set multiple properties of the main window, such as the background color, brightness, and whether the main window is touchable. The code snippet below uses the **touchable** property as an example.
    
3.  Load content to the main window.
    
    Call **loadContent** to load content to the main window.
    

import { UIAbility} from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_CreatMainWindow\]';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 1. Obtain the main window of the application.
    let windowClass: window.Window | null = null;
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to obtain the main window. Code:${err.code}, message:${err.message}\`);
        return;
      }
      windowClass = data;
      hilog.info(DOMAIN, TAG, \`Succeeded in obtaining the main window. Result:${data}\`);
      // 2. Set the touchable property of the main window.
      let isTouchable: boolean = true;
      windowClass.setWindowTouchable(isTouchable, (err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to set the window to be touchable. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in setting the window to be touchable.\`);
      })
    })
    // 3. Load content to the main window.
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
    });
  }
};

#### Setting a Child Window of an Application

You can create an application child window, such as a dialog box, and set its properties.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/iIg1_JddTGq7adOBHnNckA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B38820ECB495ED644E608261F67C3D33C559AEF386ED8C2583E0B0A157E99BE)

In the following scenarios, you are not advised to use child windows. Instead, consider using the [overlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-overlay) capability of components first.

-   On mobile devices (tablets in non-freeform mode and phones), child windows cannot extend beyond the boundaries of the application's main window when it is in floating-window or split-screen mode, just like components.
-   In split-screen or freeform window mode, components, when compared with child windows, offer better real-time adaptability to changes in the main window's position and size.
-   On certain platforms, system configurations may restrict child windows to default system animations and rounded shadows, offering no customization options for applications and thereby limiting their versatility.

## How to Develop

1.  Create a child window.
    
    Call **createSubWindow** to create a child window.
    
    The child window created uses an [immersive layout](../window-development-terminology/document.md#immersive-layout) by default.
    
2.  Set the properties of the child window.
    
    After the child window is created, you can set its properties, such as the size, position, background color, and brightness.
    
    You are advised to set the size and position of the child window before calling **showWindow**.
    
    If the size of the child window is not set, the following will happen after **showWindow** is called:
    
    -   In [freeform window](../window-development-terminology/document.md#freeform-window) mode, the child window will default to the size of the current physical screen.
    -   In non-freeform window mode, the child window will default to the size of the main window.
3.  Load content to and show the child window.
    
    Call **setUIContent** to load content to the child window and **showWindow** to show the child window.
    
4.  Destroy the child window.
    
    When the child window is no longer needed, you can call **destroyWindow** to destroy it.
    

The code snippet for creating a child window in **onWindowStageCreate** is as follows:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_CreatSubWindow\]';

let windowStage\_: window.WindowStage | null = null;
let sub\_windowClass: window.Window | null = null;

export default class EntryAbility extends UIAbility {
  showSubWindow() {
    // 1. Create a child window.
    if (windowStage\_ == null) {
      hilog.error(DOMAIN, TAG, \`Failed to create the subwindow. Cause: windowStage\_ is null\`);
    } else {
      windowStage\_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to create the subwindow. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        sub\_windowClass = data;
        if (!sub\_windowClass) {
          hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}\`);
        // 2. Set the position, size, and other properties of the child window.
        sub\_windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to move the window. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in moving the window.\`);
        });
        sub\_windowClass.resize(500, 500, (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to change the window size. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in changing the window size.\`);
        });
        // 3. Load content to the child window.
        sub\_windowClass.setUIContent('pages/Index', (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.info(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
          if (!sub\_windowClass) {
            hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
            return;
          }
          // 3. Show the child window.
          sub\_windowClass.showWindow((err: BusinessError) => {
            let errCode: number = err.code;
            if (errCode) {
              hilog.error(DOMAIN, TAG, \`Failed to show the window. Cause: ${JSON.stringify(err)}\`);
              return;
            }
            hilog.info(DOMAIN, TAG, \`Succeeded in showing the window.\`);
          });
        });
      })
    }
  }

  destroySubWindow() {
    if (!sub\_windowClass) {
      hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
      return;
    }
    // 4. Destroy the child window when it is no longer needed (depending on the service logic).
    sub\_windowClass.destroyWindow((err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to destroy the window. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in destroying the window.\`);
    });
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage\_ = windowStage;
    // Create a child window when it is needed, for example, when a touch event occurs in the main window. Calling onWindowStageCreate is not always necessary. The code here is for reference only.
    this.showSubWindow();
  }

  onWindowStageDestroy() {
    // Destroy the child window when it is no longer needed, for example, when the Close button in the child window is touched. Calling onWindowStageDestroy is not always necessary. The code here is for reference only.
    this.destroySubWindow();
  }
};

You can also click a button on a page to create a child window. The code snippet is as follows:

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_CreatSubWindow2\]';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
    });

    // Transfer the window stage to the Index page.
    AppStorage.setOrCreate('windowStage', windowStage);
  }
}

// Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_CreatSubWindow2\]';

let windowStage\_: window.WindowStage | undefined = undefined;
let sub\_windowClass: window.Window | undefined = undefined;
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private createSubWindow(){
    // Obtain the window stage.
    windowStage\_ = AppStorage.get('windowStage');
    // 1. Create a child window.
    if (windowStage\_ == null) {
      hilog.error(DOMAIN, TAG, \`Failed to create the subwindow. Cause: windowStage\_ is null\`);
    } else {
      windowStage\_.createSubWindow('mySubWindow', (err: BusinessError, data) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to create the subwindow. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        sub\_windowClass = data;
        if (!sub\_windowClass) {
          hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}\`);
        // 2. Set the position, size, and other properties of the child window.
        sub\_windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to move the window. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in moving the window.\`);
        });
        sub\_windowClass.resize(500, 500, (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to change the window size. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in changing the window size.\`);
        });
        // 3. Load content to the child window.
        sub\_windowClass.setUIContent('pages/SubWindow', (err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
          if (!sub\_windowClass) {
            hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
            return;
          }
          // 3. Show the child window.
          sub\_windowClass.showWindow((err: BusinessError) => {
            let errCode: number = err.code;
            if (errCode) {
              hilog.error(DOMAIN, TAG, \`Failed to show the window. Cause: ${JSON.stringify(err)}\`);
              return;
            }
            hilog.info(DOMAIN, TAG, \`Succeeded in showing the window.\`);
          });
        });
      })
    }
  }
  private destroySubWindow(){
    if (!sub\_windowClass) {
      hilog.error(DOMAIN, TAG, \`sub\_windowClass is null\`);
      return;
    }
    // 4. Destroy the child window when it is no longer needed (depending on the service logic).
    sub\_windowClass.destroyWindow((err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to destroy the window. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in destroying the window.\`);
    });
  }
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button(){
          Text('CreateSubWindow')
            .fontSize(24)
            .fontWeight(FontWeight.Normal)
        }.width(220).height(68)
        .margin({left:10, top:60})
        .onClick(() => {
          this.createSubWindow()
        })
        Button(){
          Text('destroySubWindow')
            .fontSize(24)
            .fontWeight(FontWeight.Normal)
        }.width(220).height(68)
        .margin({left:10, top:60})
        .onClick(() => {
          this.destroySubWindow()
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

// subWindow.ets
@Entry
@Component
struct SubWindow {
  @State message: string = 'Hello subWindow';
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
    .backgroundColor('#0D9FFB')
  }
}

#### Experiencing the immersive window feature

To create a better video watching and gaming experience, you can use the immersive window feature to hide the status bar and navigation bar. This feature is available only for the main window of an application. Since API version 10, the immersive window has the same size as the full screen by default; its layout is controlled by the component module; the background color of its status bar and navigation bar is transparent, and the text color is black. When an application window calls **setWindowLayoutFullScreen**, with **true** passed in, an immersive window layout is used. If **false** is passed in, a non-immersive window layout is used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/sqxDxzhLR_KITCCUKTB5yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8534DAE1B9E7DAA84BB0A2AEE73E498F5401F96F794B28DAC74469DBA64D4B67)

Currently, immersive UI development supports window-level configuration, but not page-level configuration. If page redirection is required, you can set the immersive mode at the beginning of the page lifecycle, for example, in the **onPageShow** callback, and then restore the default settings when the page exits, for example, in the **onPageHide** callback.

## How to Develop

1.  Obtain the main window.
    
    Call **getMainWindow** to obtain the main window of the application.
    
2.  Implement the immersive effect. You can use either of the following methods:
    
    -   Method 1: When the main window of the application is a full-screen window, call **setWindowSystemBarEnable** to hide the status bar and navigation bar.
        
    -   Method 2: Call **setWindowLayoutFullScreen** to enable the full-screen mode for the main window layout. Call **setWindowSystemBarProperties** to set the opacity, background color, text color, and highlighted icon of the status bar and navigation bar to create a display effect consistent with that of the main window.
        
3.  Load content to the immersive window.
    
    Call **loadContent** to load content to the immersive window.
    

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG: string = '\[Sample\_SetWindowSystemBarEnable\]';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 1. Obtain the main window of the application.
    let windowClass: window.Window | null = null;
    windowStage.getMainWindow((err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to obtain the main window. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      windowClass = data;
      hilog.info(DOMAIN, TAG, \`Succeeded in obtaining the main window. Data: ${JSON.stringify(data)}\`);

      // 2. Implement the immersive effect by hiding the status bar and navigation bar.
      let names: 'status'\[\] | 'navigation'\[\] = \[\];
      windowClass.setWindowSystemBarEnable(names)
        .then(() => {
          hilog.info(DOMAIN, TAG, \`Succeeded in setting the system bar to be visible.\`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG, \`Failed to set the system bar to be visible. Cause: ${JSON.stringify(err)}\`);
        });
      // 2. Alternatively, implement the immersive effect by setting the properties of the status bar and navigation bar.
      let isLayoutFullScreen = true;
      windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
        .then(() => {
          hilog.info(DOMAIN, TAG, \`Succeeded in setting the window layout to full-screen mode.\`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG, \`Failed to set the window layout to full-screen mode. Cause: ${JSON.stringify(err)}\`);
        });
      let sysBarProps: window.SystemBarProperties = {
        statusBarColor: '#ff00ff',
        navigationBarColor: '#00ff00',
        // The following properties are supported since API version 8.
        statusBarContentColor: '#ffffff',
        navigationBarContentColor: '#ffffff'
      };
      windowClass.setWindowSystemBarProperties(sysBarProps)
        .then(() => {
          hilog.info(DOMAIN, TAG, \`Succeeded in setting the system bar properties.\`);
        })
        .catch((err: BusinessError) => {
          hilog.error(DOMAIN, TAG, \`Failed to set the system bar properties. Cause: ${JSON.stringify(err)}\`);
        });
    })
    // 3. Load content to the immersive window.
    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
    });
  }
};

#### Setting a Global Floating Window (Restricted Permission)

A global floating window can be created on top of an existing task to display a window that always stays in the foreground. Even if the task that creates the global floating window is moved to the background, the global floating window can still be displayed in the foreground. Typically, a global floating window is positioned above all application windows, and you can create a global floating window and perform operations such as setting its properties.

## How to Develop

**Prerequisites:** To create a floating window (a window of the type WindowType.TYPE\_FLOAT), you must request the ohos.permission.SYSTEM\_FLOAT\_WINDOW permission. This permission is a restricted permission and can be granted only to applications running on 2-in-1 devices in [specified scenarios](../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionsystem_float_window). For details about how to request a permission, see [Requesting Restricted Permissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).

On other devices or in other scenarios, use the PiP feature. For details, see [PiP Development Guide](../using-pip-in-applications/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/SnKDUzfjQCWJ9JNHyYXIAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CC9B2A7C5E74B076BA8B645C78B8CB981E6D4A9D2E424CBBCA8C5004BCFB34A)

If such permissions are declared in the configuration file without a permission certificate applied from HUAWEI AppGallery (AGC), the application installation will fail.

1.  Create a global floating window.
    
    Call **window.createWindow** to create a global floating window.
    
2.  Set properties of the global floating window.
    
    After the global floating window is created, you can set its properties, such as the size, position, background color, and brightness.
    
3.  Load content to and show the global floating window.
    
    Call **setUIContent** to load content to the global floating window and **showWindow** to show the window.
    
4.  Destroy the global floating window.
    
    When the global floating window is no longer needed, you can call **destroyWindow** to destroy it.
    

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_CreatFloatWindow\]';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // 1. Create a floating window.
    let windowClass: window.Window | null = null;
    let config: window.Configuration = {
      name: 'floatWindow', windowType: window.WindowType.TYPE\_FLOAT, ctx: this.context
    };
    window.createWindow(config, (err: BusinessError, data) => {
      let errCode: number = err.code;
      if (errCode) {
        hilog.error(DOMAIN, TAG, \`Failed to create the floatWindow. Cause: ${JSON.stringify(err)}\`);
        return;
      }
      hilog.info(DOMAIN, TAG, \`Succeeded in creating the floatWindow. Data: ${JSON.stringify(data)}\`);
      windowClass = data;
      // 2. Set the position, size, and other properties of the floating window.
      windowClass.moveWindowTo(300, 300, (err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to move the window. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in moving the window.\`);
      });
      windowClass.resize(500, 500, (err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to change the window size. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in changing the window size.\`);
      });
      // 3. Load content to the floating window.
      windowClass.setUIContent('pages/Index', (err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          hilog.error(DOMAIN, TAG, \`Failed to load the content. Cause: ${JSON.stringify(err)}\`);
          return;
        }
        hilog.info(DOMAIN, TAG, \`Succeeded in loading the content.\`);
        // 3. Show the floating window.
        (windowClass as window.Window).showWindow((err: BusinessError) => {
          let errCode: number = err.code;
          if (errCode) {
            hilog.error(DOMAIN, TAG, \`Failed to show the window. Cause: ${JSON.stringify(err)}\`);
            return;
          }
          hilog.info(DOMAIN, TAG, \`Succeeded in showing the window.\`);
        });
      });
      // 4. Destroy the floating window when it is no longer needed (depending on the service logic).
    });
  }
};

#### Listening for Interactive and Non-Interactive Window Events

When running in the foreground, an application may switch between interactive and non-interactive states and process services depending on the state. For example, when the user opens the multitasking screen, an application becomes non-interactive and pauses the service interaction with the user, such as video playback or camera preview; when the user switched back to the foreground, the application becomes interactive again, and the paused service needs to be resumed.

## How to Develop

After a **WindowStage** object is created, the application can listen for the **'windowStageEvent'** event to obtain window stage lifecycle changes, for example, whether the window stage is interactive or non-interactive in the foreground. The application can process services based on the reported event status.

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0X0000;
const TAG : string = '\[Sample\_ListenWindowStage\]';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // ···
    try {
      windowStage.on('windowStageEvent', (data) => {
        hilog.info(DOMAIN, TAG, \`Succeeded in enabling the listener for window stage event changes. Data: ${JSON.stringify(data)}\`);

        // Process services based on the event status.
        if (data === window.WindowStageEventType.SHOWN) {
          hilog.info(DOMAIN, TAG, \`current window stage event is SHOWN\`);
          // The application enters the foreground and is interactive by default.
          // ...
        } else if (data === window.WindowStageEventType.HIDDEN) {
          hilog.info(DOMAIN, TAG, \`current window stage event is HIDDEN\`);
          // The application enters the background and is non-interactive by default.
          // ...
        } else if (data === window.WindowStageEventType.PAUSED) {
          hilog.info(DOMAIN, TAG, \`current window stage event is PAUSED\`);
          // The user opens the multitasking screen when the application is running in the foreground, and the application becomes non-interactive.
          // ...
        } else if (data === window.WindowStageEventType.RESUMED) {
          hilog.info(DOMAIN, TAG, \`current window stage event is RESUMED\`);
          // The user switches back from the multitasking screen to the application, and the application becomes interactive.
          // ...
        }

        // ...
      });
    } catch (exception) {
      hilog.error(DOMAIN, TAG, \`Failed to enable the listener for window stage event changes. Cause: ${JSON.stringify(exception)}\`);
    }
  }
}
