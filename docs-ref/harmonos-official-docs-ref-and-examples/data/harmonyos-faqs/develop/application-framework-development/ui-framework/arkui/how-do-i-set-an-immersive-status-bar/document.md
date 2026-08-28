# How do I set an immersive status bar?

1.  Obtain the main window. Call **getMainWindow** to obtain the main window of the application.
2.  Implement the immersive effect. You can use either of the following methods:
    -   Method 1: Call **setWindowSystemBarEnable** to hide the navigation bar and status bar.
    -   Method 2: Call **setWindowLayoutFullScreen** to enable the full-screen mode for the main window layout. Call **setWindowSystemBarProperties** to set the opacity, background color, text color, and highlighted icon of the status bar and navigation bar to ensure that their display effect is consistent with that of the main window.
3.  Load content for the immersive window and show it. Call **loadContent** to load the content to the immersive window.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    
    export default class EntryAbility extends UIAbility {
      onWindowStageCreate(windowStage: window.WindowStage) {
        // 1.Get the main window of the application.
        let windowClass: window.Window | undefined = undefined;
        windowStage.getMainWindow((err: BusinessError, data) => {
          if (err.code) {
            console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
            return;
          }
          windowClass = data;
          console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
    
    
          // 2.Realize immersive effects. Method 1: Set the navigation bar and status bar to not display.
          let names = \[\];
          windowClass.setWindowSystemBarEnable(names).then(() => {
            console.info('Succeeded in setting the system bar to be visible.');
          }).catch((err: BusinessError) => {
            console.error('Failed to setting the system bar to be visible. Cause: ' + JSON.stringify(err));
          });
          // 2.Realize immersive effects. Method 2: Set the window to a full screen layout, and coordinate with the transparency, background/text color, and highlighted icons of the navigation bar and status bar to maintain consistency with the main window display.
          let isLayoutFullScreen = true;
          windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
            console.info('Succeeded in setting the window layout to full-screen mode.');
          }).catch((err: BusinessError) => {
            console.error('Failed to setting the window layout. Cause: ' + JSON.stringify(err));
          });
          let sysBarProps: window.SystemBarProperties = {
            statusBarColor: '#ff00ff',
            navigationBarColor: '#00ff00',
            // The following two attributes are supported starting from API Version 8
            statusBarContentColor: '#ffffff',
            navigationBarContentColor: '#ffffff'
          };
          windowClass.setWindowSystemBarProperties(sysBarProps).then(() => {
            console.info('Succeeded in setting the system bar properties.');
          }).catch((err: BusinessError) => {
            console.error('Failed to setting the system bar properties. Cause: ' + JSON.stringify(err));
          });
        })
        // 3.Load the corresponding target page for the immersive window.
        windowStage.loadContent("pages/page2", (err) => {
          if (err.code) {
            console.error('Failed to load the content. Cause:' + JSON.stringify(err));
            return;
          }
          console.info('Succeeded in loading the content.');
        });
      }
    };
