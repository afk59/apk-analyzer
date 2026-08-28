# Loading Web Pages

Page loading is a basic capability of the **Web** component. Depending on the data source, page loading falls into three types: loading of network pages, loading of local pages, and loading of HTML rich text data.

To obtain network resources during page loading, configure the network access permission in the **module.json5** file. For details, see [Declaring Permissions in the Configuration File](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).

"requestPermissions":\[
    {
      "name" : "ohos.permission.INTERNET"
    }
  \]

#### Loading Network Pages

You can specify the default network page to be loaded when creating a **Web** component. After the default network page is loaded, call [loadUrl()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl) if you want to change the network page displayed by the **Web** component. The value of the first parameter **src** of the [Web component](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web) cannot be dynamically changed through a state variable (for example, @State). To change the value, call [loadUrl()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl).

In the following example, after the **www.\\example.com** page is loaded by the **Web** component, **loadUrl** is called to change the displayed page to **www.example1.com**.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadUrl')
        .onClick(() => {
          try {
            // Upon button clicking, call loadUrl to redirect to www.example1.com.
            this.controller.loadUrl('www.example1.com');
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      // When creating a Web component, set the default network page to be loaded to www.example.com.
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}

#### Loading Local Pages

To reduce user waiting time in scenarios such as startup, redirection, and weak network, and save time for dynamic content loading, you can load local pages to optimize user experience.

The following example shows how to load a local page file.

Local page files are stored in the application's **rawfile** directory. You can specify the local page to be loaded by default when creating a **Web** component. After page loading is complete, you can call [loadUrl()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loadurl) to change the displayed page of the **Web** component.

To reference a local CSS file when loading a local HTML file, perform the following steps:

<link rel="stylesheet" href="resource://rawfile/xxx.css">
<link rel="stylesheet" href="file:// /data/storage/el2/base/haps/entry/cache/xxx.css">// Load the local CSS file in the sandbox path.

-   Local page file in the application's resources/rawfile directory:
    
    **Figure 1** Path of local page files
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/m5ih36QyRLG_7igg57T0eQ/en-us_image_0000002568684729.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061948Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE5CBF5A4AC6383C76782B7BE9DD2C4AAB4BEE4369E279A7511F06D6B95A7D6F)
    
-   Application code:
    
    import { webview } from '@kit.ArkWeb';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Button('loadUrl')
            .onClick(() => {
              try {
                // Upon button clicking, call loadUrl to redirect to local1.html.
                this.controller.loadUrl($rawfile('local1.html'));
              } catch (error) {
                console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
              }
            })
          // When creating a Web component, load the local.html file through $rawfile.
          Web({ src: $rawfile('local.html'), controller: this.controller });
        }
      }
    }
    
-   Code of the **local.html** page:
    
    <!-- local.html -->
    <!DOCTYPE html>
    <html>
      <body>
        <p>Hello World</p>
      </body>
    </html>
    
-   Code of the **local1.html** page:
    
    <!-- local1.html -->
    <!DOCTYPE html>
    <html>
      <body>
        <p>This is local1 page</p>
      </body>
    </html>
    

Example of loading local page files in the sandbox:

1.  Obtain the sandbox path through the constructed singleton object **GlobalContext**. You need to enable the [fileAccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#fileaccess) permission of the file system in the application.
    
    export class GlobalContext {
      private constructor() {}
      private static instance: GlobalContext;
      private \_objects = new Map<string, Object>();
    
      public static getContext(): GlobalContext {
        if (!GlobalContext.instance) {
          GlobalContext.instance = new GlobalContext();
        }
        return GlobalContext.instance;
      }
    
      getObject(value: string): Object | undefined {
        return this.\_objects.get(value);
      }
    
      setObject(key: string, objectClass: Object): void {
        this.\_objects.set(key, objectClass);
      }
    }
    
    import { webview } from '@kit.ArkWeb';
    import { GlobalContext } from './GlobalContext';
    
    let url = 'file://' + GlobalContext.getContext().getObject('filesDir') + '/index.html';
    
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Text('loading success');
          // Load the files in the sandbox.
          Web({ src: url, controller: this.controller });
        }
      }
    }
    
2.  Modify the **EntryAbility.ets** file.
    
    The following uses **filesDir** as an example to describe how to obtain the path of the sandbox. For details about how to obtain other paths, see [Obtaining Application File Paths](../../../ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-application-file-paths).
    
    // xxx.ets
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { webview } from '@kit.ArkWeb';
    import { GlobalContext } from '../GlobalContext';
    
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
        // Data synchronization between the UIAbility component and UI can be implemented by binding filesDir to the GlobalContext object.
        GlobalContext.getContext().setObject("filesDir", this.context.filesDir);
        console.info("Sandbox path is " + GlobalContext.getContext().getObject("filesDir"));
      }
    }
    
    HTML file to be loaded:
    
    <!-- index.html -->
    <!DOCTYPE html>
    <html>
        <body>
            <p>Hello World</p>
        </body>
    </html>
    

#### Loading HTML Rich Text Data

The **Web** component provides the [loadData()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#loaddata) API for you to load HTML rich text data. If you need to display only some page fragments, you can use this feature to quickly load the page. To load a large number of HTML files, set **baseUrl** to data.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('loadData')
        .onClick(() => {
          try {
            // Upon button clicking, call loadData to load HTML rich text data.
            this.controller.loadData(
              '<html><body bgcolor=\\'white\\'>Source:<pre>source</pre></body></html>',
              'text/html',
              'UTF-8'
            );
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      // When creating a Web component, set the default network page to be loaded to www.example.com.
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

The **Web** component can load HTML strings using data urls.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  htmlStr: string = 'data:text/html, <html><body bgcolor=\\'white\\'>Source:<pre>source</pre></body></html>';

  build() {
    Column() {
      // When creating a Web component, set the default network page to be loaded to htmlStr.
      Web({ src: this.htmlStr, controller: this.controller });
    }
  }
}

#### Loading Local Resources Using the Resource Protocol

The resource protocol allows access to files in the application resource directory.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct ResourceWebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('Load resources')
        .onClick(() => {
          try {
            // Load the index1.html file in resources/rawfile through using the resource protocol.
            this.controller.loadUrl('resource://rawfile/index1.html');
          } catch (error) {
            console.error(\`ErrorCode: ${error.code}, Message: ${error.message}\`);
          }
        })

      // When the component is created, use the resource protocol to load resources.
      Web({
        src: 'resource://rawfile/index.html', controller: this.controller})
    }
  }
}

Create the **index.html** file in **src/main/resources/rawfile**.

<!-- index.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World</p>
  </body>
</html>

Create the **index1.html** file in **src/main/resources/rawfile**.

<!-- index1.html -->
<!DOCTYPE html>
<html>
  <body>
    <p>Hello World Again</p>
  </body>
</html>
