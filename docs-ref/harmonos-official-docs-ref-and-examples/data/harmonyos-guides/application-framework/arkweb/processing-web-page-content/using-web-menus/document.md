# Using Web Menus

Menus are key components for user interaction. They help build a clear navigation system and display feature entries in a structured layout, enabling users to quickly find target content or perform operations. As an important hub for human-machine interaction, menus significantly improve the accessibility and user experience of **Web** components and are an indispensable part of application design. The following table lists the menu types of **Web** components. You can select a menu type for your application as required.

| Menu Type | Target Element | Response Conditions | Customization Support |
| :-- | :-- | :-- | :-- |
| [Text Selection Menu](#text-selection-menu) | Text | Long press | The menu items can be added or deleted while the menu style cannot be customized. |
| [Context Menu](#context-menu) | Hyperlink, image, and text | Long press and right-click | Customization can be implemented using menu components. |
| [Custom Menu](#custom-menu) | Image | Long press | Customization can be implemented using menu components. |

#### Text Selection Menu

The text selection menu of the **Web** component is a context interaction component implemented by custom elements. It is dynamically displayed when a user selects text and provides operations such as copy, share, and mark. It has standard features and scalability and is the core feature of text operations on mobile devices. The text selection menu is displayed when a user long-presses the selected text or long-presses the single handle in the editing state. The menu items are horizontally arranged. The system provides the default menu implementation. You can use the [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#editmenuoptions12) API to customize the text selection menu.

1.  Use the **onCreateMenu** method to customize menu items. Operate Array<[TextMenuItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textmenuitem12)\> to add or delete menu items. Define the menu item name, icon, and ID in [TextMenuItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#textmenuitem12).
2.  Use the **onMenuItemClick** method to process the menu item click event. When false is returned, the default system logic is executed.
3.  Create an [EditMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-text-common#editmenuoptions) object, which contains the **onCreateMenu** and **onMenuItemClick** methods, and bind the object to the **Web** component using the [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#editmenuoptions12) method of the **Web** component.

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
    let items = menuItems.filter((menuItem) => {
      // Filter the menu items as required.
      return (
        menuItem.id.equals(TextMenuItemId.CUT) ||
        menuItem.id.equals(TextMenuItemId.COPY) ||
        menuItem.id.equals(TextMenuItemId.PASTE)
      );
    });
    let customItem1: TextMenuItem = {
      content: 'customItem1',
      id: TextMenuItemId.of('customItem1'),
      icon: $r('app.media.startIcon')
    };
    let customItem2: TextMenuItem = {
      content: $r('app.string.EntryAbility\_label'),
      id: TextMenuItemId.of('customItem2'),
      icon: $r('app.media.startIcon')
    };
    items.push(customItem1); // Add an item to the end of the item list.
    items.unshift(customItem2); // Add an item to the beginning of the item list.
    items.push(customItem1);
    items.push(customItem1);
    items.push(customItem1);
    items.push(customItem1);
    items.push(customItem1);
    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    if (menuItem.id.equals(TextMenuItemId.CUT)) {
      // Custom behavior
      console.info("Intercept ID: CUT")
      return true; // Return true to not execute the system callback.
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // Custom behavior
      console.info("Not intercept ID: COPY")
      return false; // Return false to execute the system callback.
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
      // Custom behavior
      console.info("Intercept ID: customItem1")
      return true; // Custom menu item. If true is returned, the menu is not closed after being clicked. If false is returned, the menu is closed.
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem2'))) {
      // Custom behavior
      console.info("Intercept ID: customItem2")
      return true;
    }
    return false; // Return the default value false.
  }

  @State EditMenuOptions: EditMenuOptions = { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .editMenuOptions(this.EditMenuOptions)
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>editMenuOptions Demo</h1>
    <span>edit menu options</span>
  </body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/G_wYNYb6RpeOmcifDKqlqg/en-us_image_0000002537924962.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D447FF9BE9C47F320C57287773B234049B10A5E9D0E1C081CFBF2B437116CA2B)

#### Context Menu

A context menu is a shortcut menu triggered by a specific operation (such as right-clicking or holding down the rich text) to provide feature items related to the current operation object or UI element. Items in a context menu are arranged vertically. This menu is not provided by default. If it is not implemented in the application, the context menu is not displayed. To implement a context menu, the application needs to create a [Menu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-menu) component and bind it to the **Web** component. When the menu is displayed, use the [onContextMenuShow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9) API to obtain the context menu details, including the click location and HTML element information.

1.  The [Menu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-menu) component contains the behaviors and styles of all menu items.
2.  Use the **bindPopup** method to bind the **Menu** component to the **Web** component. When the context menu is displayed, the created **Menu** component is displayed.
3.  Obtain the context menu event information [onContextMenuShowEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-i#oncontextmenushowevent12) in the **onContextMenuShow** callback. The **param** parameter is of the [WebContextMenuParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam) type, which contains the HTML element information and location information corresponding to the click position. The **result** parameter is of the [WebContextMenuResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult) type, which provides common menu capabilities.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';

const TAG = 'ContextMenu';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  private result: WebContextMenuResult | undefined = undefined;
  @State linkUrl: string = '';
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State showMenu: boolean = false;
  uiContext: UIContext = this.getUIContext();

  @Builder
  // Build and trigger a custom menu.
  MenuBuilder() {
    // A component that is used to present a vertical list of items to the user.
    Menu() {
      // A component that is used to represent an item in a menu.
      MenuItem({
        content: 'Copy image',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Cut',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copy();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Paste',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.paste();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy link',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          let pasteData = pasteboard.createData('text/plain', this.linkUrl);
          pasteboard.getSystemPasteboard().setData(pasteData, (error) => {
            if (error) {
              return;
            }
          })
          this.showMenu = false;
        })
      MenuItem({
        content: 'Select all',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.selectAll();
          this.showMenu = false;
        })
    }
    .width(150)
    .height(300)
  }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        // Trigger a custom dialog box.
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result
            console.info("x coord = " + event.param.x());
            console.info("link url = " + event.param.getLinkUrl());
            this.linkUrl = event.param.getLinkUrl();
          }
          console.info(TAG, \`x: ${this.offsetX}, y: ${this.offsetY}\`);
          this.showMenu = true;
          this.offsetX = 0;
          this.offsetY = Math.max(this.uiContext!.px2vp(event?.param.y() ?? 0) - 0, 0);
          return true;
        })
        .bindPopup(this.showMenu,
          {
            builder: this.MenuBuilder(),
            enableArrow: false,
            placement: Placement.LeftTop,
            offset: { x: this.offsetX, y: this.offsetY },
            mask: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.showMenu = false;
                this.result!.closeContextMenu();
              }
            }
          })
    }
  }
}

<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<body>
  <h1>onContextMenuShow</h1>
  <a href="http://www.example.com" style="font-size:27px">Hyperlink www.example.com</a>
  <!--example.png is an image in the same directory as the html file-->
  <div><img src="example.png"></div>
  <p>Right-click text to display the context menu</p>
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/EibLff52TVihmJJlJHh5FQ/en-us_image_0000002568684739.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4A2DA56BD6DFF89F3EDC2D9C2627FF566E3B4973B4A0E70B77CD41B5B27D4B8)

#### Custom Menu

Custom menus enable you to adjust menu triggering timing and visual display, so that your application can dynamically match feature entries based on user operation scenarios. This simplifies UI adaptation in the development process and makes application interaction more intuitive.

You can use the [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#bindselectionmenu13) API to implement the custom menu. Currently, the custom menu and text menu can be triggered by touching and holding an image, link, or text.

1.  Create a [Menu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-menu) component as the menu pop-up window.
2.  Use the [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#bindselectionmenu13) method of the **Web** component to bind the **MenuBuilder** pop-up window. Set [WebElementType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-e#webelementtype13) to **WebElementType.IMAGE** and [responseType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-e#webresponsetype13) to **WebResponseType.LONG\_PRESS**, so that the menu is displayed when the image is pressed for a long time. Define **onAppear**, **onDisappear**, **preview**, and **menuType** in [options](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-i#selectionmenuoptionsext13).

// xxx.ets
import { webview } from '@kit.ArkWeb';

interface PreviewBuilderParam {
  previewImage: Resource | string | undefined;
  width: number;
  height: number;
}

@Builder function PreviewBuilderGlobal($$: PreviewBuilderParam) {
  Column() {
    Image($$.previewImage)
      .objectFit(ImageFit.Fill)
      .autoResize(true)
  }.width($$.width).height($$.height)
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  private result: WebContextMenuResult | undefined = undefined;
  @State previewImage: Resource | string | undefined = undefined;
  @State previewWidth: number = 0;
  @State previewHeight: number = 0;
  uiContext: UIContext = this.getUIContext();

  @Builder
  MenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy', })
        .onClick(() => {
          this.result?.copy();
          this.result?.closeContextMenu();
        })
      MenuItem({ content: 'Select All', })
        .onClick(() => {
          this.result?.selectAll();
          this.result?.closeContextMenu();
        })
    }
  }
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .bindSelectionMenu(WebElementType.IMAGE, this.MenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: PreviewBuilderGlobal({
              previewImage: this.previewImage,
              width: this.previewWidth,
              height: this.previewHeight
            }),
            menuType: MenuType.PREVIEW\_MENU
          })
        .onContextMenuShow((event) => {
            if (event) {
              this.result = event.result;
              if (event.param.getLinkUrl()) {
                return false;
              }
              this.previewWidth = this.uiContext!.px2vp(event.param.getPreviewWidth());
              this.previewHeight = this.uiContext!.px2vp(event.param.getPreviewHeight());
              if (event.param.getSourceUrl().indexOf("resource://rawfile/") == 0) {
                this.previewImage = $rawfile(event.param.getSourceUrl().substr(19));
              } else {
                this.previewImage = event.param.getSourceUrl();
              }
              return true;
            }
            return false;
          })
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>bindSelectionMenu Demo</h1>
    <!--img.png is an image in the same directory as the html file-->
    <img src="./img.png" >
  </body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/CnaJt4YXSuOz-OJ8Qz4NIQ/en-us_image_0000002568764749.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A915273CB72E82B8BEAEAE7B528E40103C054FFBD03BF5669128424CEC3BB43)

Since API version 20, the hyperlink menu triggered by long-pressing can be bound. You can bind different custom menus to images and links.

The following example uses **PreviewBuilder** to define the content of the pop-up menu corresponding to the hyperlink, loads the hyperlink content using the **Web** component, and displays the loading progress using [the Progress component](../../../arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/progress-indicator-progress/document.md).

import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';

interface PreviewBuilderParam {
  width: number;
  height: number;
  url:Resource | string | undefined;
}

interface PreviewBuilderParamForImage {
  previewImage: Resource | string | undefined;
  width: number;
  height: number;
}

@Builder function PreviewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
  Column() {
    Image($$.previewImage)
      .objectFit(ImageFit.Fill)
      .autoResize(true)
  }.width($$.width).height($$.height)
}

@Entry
@Component
struct SelectionMenuLongPress {
  controller: webview.WebviewController = new webview.WebviewController();
  previewController: webview.WebviewController = new webview.WebviewController();
  @Builder PreviewBuilder($$: PreviewBuilderParam){
    Column() {
      Stack(){
        Text("") // Select whether to display the URL.
          .padding(5)
          .width('100%')
          .textAlign(TextAlign.Start)
          .backgroundColor(Color.White)
          .copyOption(CopyOptions.LocalDevice)
          .maxLines(1)
          .textOverflow({overflow:TextOverflow.Ellipsis})
        Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // Display the progress bar.
          .style({ strokeWidth: 3, enableSmoothEffect: true })
          .backgroundColor(Color.White)
          .opacity(this.progressVisible?1:0)
          .backgroundColor(Color.White)
      }.alignContent(Alignment.Bottom)
      Web({src:$$.url,controller: new webview.WebviewController()})
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .onPageBegin(()=>{
          this.progressValue = 0;
          this.progressVisible = true;
        })
        .onProgressChange((event)=>{
          this.progressValue = event.newProgress;
        })
        .onPageEnd(()=>{
          this.progressVisible = false;
        })
        .hitTestBehavior(HitTestMode.None) // Disable the gesture response during web page preview.
    }.width($$.width).height ($$.height) // Set the preview width and height.
  }

  private result: WebContextMenuResult | undefined = undefined;
  @State previewImage: Resource | string | undefined = undefined;
  @State previewWidth: number = 1;
  @State previewHeight: number = 1;
  @State previewWidthImage: number = 1;
  @State previewHeightImage: number = 1;
  @State linkURL:string = "";
  @State progressValue:number = 0;
  @State progressVisible:boolean = true;
  uiContext: UIContext = this.getUIContext();

  @Builder
  LinkMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Link', })
        .onClick(() => {
          const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, this.linkURL);
          const systemPasteboard = pasteboard.getSystemPasteboard();
          systemPasteboard.setData(pasteboardData);
        })
      MenuItem({content:'Open Link'})
        .onClick(()=>{
          this.controller.loadUrl(this.linkURL);
        })
    }
  }
  @Builder
  ImageMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Image', })
        .onClick(() => {
          this.result?.copyImage();
          this.result?.closeContextMenu();
        })
    }
  }
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .bindSelectionMenu(WebElementType.LINK, this.LinkMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: this.PreviewBuilder({
              width: 500,
              height: 400,
              url:this.linkURL
            }),
            menuType: MenuType.PREVIEW\_MENU,
          })
        .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: PreviewBuilderGlobalForImage({
              previewImage: this.previewImage,
              width: this.previewWidthImage,
              height: this.previewHeightImage,
            }),
            menuType: MenuType.PREVIEW\_MENU,
          })
        .zoomAccess(true)
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result;
            this.previewWidthImage = this.uiContext!.px2vp(event.param.getPreviewWidth());
            this.previewHeightImage = this.uiContext!.px2vp(event.param.getPreviewHeight());
            if (event.param.getSourceUrl().indexOf("resource://rawfile/") == 0) {
              this.previewImage = $rawfile(event.param.getSourceUrl().substring(19));
            } else {
              this.previewImage = event.param.getSourceUrl();
            }
            this.linkURL = event.param.getLinkUrl()
            return true;
          }
          return false;
        })
    }

  }
  // Swipe back
  onBackPress(): boolean | void {
    if (this.controller.accessStep(-1)) {
      this.controller.backward();
      return true;
    } else {
      return false;
    }
  }
}

HTML example:

<html lang="zh-CN"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Information Page</title>
</head>
<body>
<div>
    <h1>Comprehensive information and contact details</h1>
    <section>
        <a href="https://www.example.com">EXAMPLE</a>
        <br>
        <a href="https://www.example1.com/">EXAMPLE1</a>
    </section>
</div>
<footer>
    <p>Note that all the above URLs are for reference only.</p>
</footer>
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/8tDsqOtmQf-h_10LWRCwsQ/en-us_image_0000002537765024.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06C9B482F6F3385D74E6BC83E7C8873A5E924123E10D63C2587700B9FD70F84C)

#### Saving Images

1.  Create the **MenuBuilder** component as the menu pop-up window, use the [SaveButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-security-components-savebutton) component to save images, and bind **MenuBuilder** to the **Web** component using **bindContextMenu**.
2.  Obtain the image URL in **onContextMenuShow** and save the image to the application sandbox by calling **copyLocalPicToDir** or **copyUrlPicToDir**.
3.  Save images in the application sandbox to the gallery by using **photoAccessHelper**.

import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { fileIo as fs} from '@kit.CoreFileKit';
import { systemDateTime } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct WebComponent {
  saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL\_FILLED,
    text: SaveDescription.SAVE\_IMAGE,
    buttonType: ButtonType.Capsule
  }
  controller: webview.WebviewController = new webview.WebviewController();
  @State showMenu: boolean = false;
  @State imgUrl: string = '';
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  copyLocalPicToDir(rawfilePath: string, newFileName: string): string {
    let srcFileDes = this.context.resourceManager.getRawFdSync(rawfilePath);
    let dstPath = this.context.filesDir + '/' +newFileName;
    let dest: fs.File = fs.openSync(dstPath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
    let bufsize = 4096;
    let buf = new ArrayBuffer(bufsize);
    let off = 0;
    let len = 0;
    let readLen = 0;
    while ((len = fs.readSync(srcFileDes.fd, buf, { offset: srcFileDes.offset + off, length: bufsize })) != 0) {
      readLen += len;
      fs.writeSync(dest.fd, buf, { offset: off, length: len });
      off = off + len;
      if ((srcFileDes.length - readLen) < bufsize) {
        bufsize = srcFileDes.length - readLen;
      }
    }
    fs.close(dest.fd);
    return dest.path;
  }

  async copyUrlPicToDir(picUrl: string, newFileName: string): Promise<string> {
    let uri = '';
    let httpRequest = http.createHttp();
    let data: http.HttpResponse = await(httpRequest.request(picUrl) as Promise<http.HttpResponse>);
    if (data?.responseCode == http.ResponseCode.OK) {
      let dstPath = this.context.filesDir + '/' + newFileName;
      let dest: fs.File = fs.openSync(dstPath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
      let writeLen: number = fs.writeSync(dest.fd, data.result as ArrayBuffer);
      uri = dest.path;
    }
    return uri;
  }

  @Builder
  MenuBuilder() {
    Column() {
      Row() {
        SaveButton(this.saveButtonOptions)
          .onClick(async (event, result: SaveButtonOnClickResult) => {
            if (result == SaveButtonOnClickResult.SUCCESS) {
              try {
                let context = this.context;
                let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
                let uri = '';
                if (this.imgUrl?.includes('rawfile')) {
                  let rawFileName: string = this.imgUrl.substring(this.imgUrl.lastIndexOf('/') + 1);
                  uri = this.copyLocalPicToDir(rawFileName, 'copyFile.png');
                } else if (this.imgUrl?.includes('http') || this.imgUrl?.includes('https')) {
                  uri = await this.copyUrlPicToDir(this.imgUrl, \`onlinePic${systemDateTime.getTime()}.png\`);
                }
                let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
                  photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context,  uri);
                await phAccessHelper.applyChanges(assetChangeRequest);
              } catch (err) {
                console.error(\`create asset failed with error: ${err.code}, ${err.message}\`);
              }
            } else {
              console.error(\`SaveButtonOnClickResult create asset failed\`);
            }
            this.showMenu = false;
          })
      }
      .margin({ top: 20, bottom: 20 })
      .justifyContent(FlexAlign.Center)
    }
    .width('80')
    .backgroundColor(Color.White)
    .borderRadius(10)
  }

  build() {
    Column() {
      Web({src: $rawfile('index4.html'), controller: this.controller})
        .onContextMenuShow((event) => {
          if (event) {
            let hitValue = this.controller.getLastHitTest();
            this.imgUrl = hitValue.extra;
          }
          this.showMenu = true;
          return true;
        })
        .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
        .fileAccess(true)
        .javaScriptAccess(true)
        .domStorageAccess(true)
    }
  }
}

<!--index4.html-->
<!DOCTYPE html>
<html>
<head>
    <title>SavePicture</title>
</head>
<body>
<h1>SavePicture</h1>
<br>
<br>
<br>
<br>
<br>
<!--startIcon.png is an image in the same directory as the html file-->
<img src="./startIcon.png">
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/dlnCYYYnRfGXEas3_7-5Ng/en-us_image_0000002537924964.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85E3B964B1BCBA993D5B32C41703053EAE7BBC284162E00C6C5782D9E4ED3C2E)

#### Obtaining Selected Text

The [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#editmenuoptions12) API of the **Web** component cannot obtain the selected text. You can obtain the selected text in JavaScript through [javaScriptProxy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#javascriptproxy) to implement the logic of custom menus.

1.  Create a **SelectClass** class and use [javaScriptProxy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#javascriptproxy) to register the **SelectClass** object with the **Web** component.
2.  Register a selection change listener on the HTML side. When the selection changes, use the **SelectClass** object to set the selection to the ArkTS side.

import { webview } from '@kit.ArkWeb';
let selectText = '';

class SelectClass {
  constructor() {
  }

  setSelectText(param: String) {
    selectText = param.toString();
  }
}

@Entry
@Component
struct WebComponent {
  webController: webview.WebviewController = new webview.WebviewController();
  @State selectObj: SelectClass = new SelectClass();
  @State textStr: string = '';

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.webController})
        .javaScriptProxy({
          object: this.selectObj,
          name: 'selectObjName',
          methodList: \['setSelectText'\],
          controller: this.webController
        })
        .height('40%')
      Text('Click here to get the selected text.')
        .fontSize(20)
        .onClick(() => {
          this.textStr = selectText;
        })
        .height('10%')
      Text('Selected text is ' + this.textStr)
        .fontSize(20)
        .height('10%')
    }
  }
}

<!DOCTYPE html>
<html>
<head>
    <title>Test Get Select</title>
    <style>
        body {
          margin: 40px;
          background-color: #f4f4f4;
        }
        .edit-container {
          padding: 20px;
          background-color: #fff;
          border-radius: 8px;
          box-shadow: 0 0 10px rgba(0,0,0,0.1);
          margin: auto;
        }
        textarea {
          width: 100%;
          height: 400px;
          font-size: 16px;
          padding: 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
        }
    </style>
</head>
<body>
<div class="edit-container">
    <textarea placeholder="Enter the text here and select it by long pressing."></textarea>
</div>
<script>
    document.addEventListener('selectionchange', () => {
      var selection = window.getSelection();
      if(selection.rangeCount > 0) {
        var selectedText = selection.toString();
        selectObjName.setSelectText(selectedText);
      }
    })
</script>
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/x_sg7nA9QOqT_IGFQ5rG4w/en-us_image_0000002568684741.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=270DF5716E1782DE2B034F419E1B37B672452D50283B5CA72C58E72595A4692A)

#### FAQs

## How do I disable the menu triggered by a long press?

You can use the [editMenuOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#editmenuoptions12) API to filter out all default menus. Then, default menus are not displayed if there is no menu item.

// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
    let items = menuItems.filter((menuItem) => {
      // Filter the menu items as required.
      return false;
    });
    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    return false;// Return the default value false.
  }

  @State EditMenuOptions: EditMenuOptions = { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .editMenuOptions(this.EditMenuOptions)
    }
  }
}

<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>editMenuOptions Demo</h1>
    <span>edit menu options</span>
  </body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/QpjofXK0SDKXF9RFjkVkBg/en-us_image_0000002568764751.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F17CDDD06A2FA16E984587300D7B58237887579E7A542521B138392A5CE0C68)

## What should I do if the menu with a selection handle is not displayed when the selection area is displayed?

Check whether the selection area is operated using the [selection API](https://www.w3.org/TR/selection-api/) of the JavaScript. If yes, the menu with a selection handle is not displayed.

## How do I modify the style of the text selection menu?

Since API version 21, applications can use the [bindSelectionMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#bindselectionmenu13) API to implement the custom text menus.

**Sample Code**

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  clearSelection() {
    try {
      this.controller.runJavaScript(
        'clearSelection()',
        (error, result) => {
          if (error) {
            console.error(\`run clearSelection JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
            return;
          }
          if (result) {
            console.info(\`The clearSelection() return value is: ${result}\`);
          }
        });
    } catch (error) {
      console.error(\`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
    }
  }

  @Builder
  TextMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy', })
        .onClick(() => {
          try {
            this.controller.runJavaScript(
              'copySelectedText()',
              (error, result) => {
                if (error) {
                  console.error(\`run copySelectedText JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
                  return;
                }
                if (result) {
                  console.info(\`The copySelectedText() return value is: ${result}\`);
                }
              });
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}\`);
          }
          this.clearSelection()
        }).backgroundColor(Color.Pink)
    }
  }
  build() {
    Column() {
      Web({ src: $rawfile('bindSelectionMenuText.html'), controller: this.controller })
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .zoomAccess(true)
        .bindSelectionMenu(WebElementType.TEXT, this.TextMenuBuilder, WebResponseType.LONG\_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {},
            menuType: MenuType.SELECTION\_MENU,
          })
    }
  }
  onBackPress(): boolean | void {
    if (this.controller.accessStep(-1)) {
      this.controller.backward();
      return true;
    } else {
      return false;
    }
  }
}

<!--bindSelectionMenuText.html-->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom text menu</title>
    <style>
        .container {
            background-color: white;
            padding: 30px;
            margin: 20px 0;
        }

        .context {
            line-height: 1.8;
            font-size: 18px;
        }

        .context span {
            border-radius: 8px;
            background-color: #f8f9fa;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="context">
        <span>In this digital age, the text copying functionality has grown increasingly important. Whether quoting famous remarks, saving key information, or sharing interesting content, copying text is an integral part of our daily operations.</span>
    </div>
</div>

<script>
  function copySelectedText() {
      const selectedText = window.getSelection().toString();
      if (selectedText.length > 0) {
          // Use the Clipboard API to copy text.
          navigator.clipboard.writeText(selectedText)
              .then(() => {
                  showNotification();
              })
              .catch(err => {
                  console.error('copy failed:', err);
              });
      }
  }
  function clearSelection() {
    if (window.getSelection) {
      window.getSelection().removeAllRanges();
    }
  }
</script>
</body>
</html>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/CkQDfwNeQlqLJT6T7De0OA/en-us_image_0000002537765026.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D51592D911592B1201254649DF23634F0B7549938D2E964AFF0E32CFFC4D0D7D)
