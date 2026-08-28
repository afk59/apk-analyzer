# Zooming Web Pages

ArkWeb supports gesture zoom, mouse wheel zoom, and keyboard zoom, allowing users to adjust the display to a comfortable size. It also provides the capability of listening for and controlling the page zoom scale for applications to achieve personalized visual effects.

#### Setting Web Page Zoom

## Setting Gesture Zoom

You can use the [zoomAccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#zoomaccess) attribute to set the web page zoom functionality. When this attribute is set to **false**, the web page cannot be zoomed in or out using gestures.

When <meta name="viewport" id="viewport" content="user-scalable=no"> is set for the HTML web page, the web page cannot be zoomed in or out using gestures.

Gestures can be used to zoom in or out only when both the **zoomAccess** and **viewport** tags are set to allow zooming.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/z1V0Ny3oSiuFrgZBOQreqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061948Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=874178F47533293CB7603A5071C0E4E1C93AC8B7CD21ACFCC966710C2752809C)

On a PC or 2-in-1 device, the **viewport** tag does not take effect. You can only set **zoomAccess** to **false** to disable gesture zoom.

The preceding tags can only be used to enable or disable the zoom functionality. If **minimum-scale** and **maximum-scale** are set in the **viewport** tag, the zoom range is also restricted by the two attributes. When the maximum and minimum values are the same, the web page cannot be zoomed in or out.

In addition, the zoom-out scale is limited by the width of the web page.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(false)
    }
  }
}

## Setting Forcible Gesture Zoom

You can use the [forceEnableZoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#forceenablezoom21) attribute to set the forcible zoom functionality of a web page. When this attribute is set to **true**, the gesture zoom behavior is not restricted by **minimum-scale**, **maximum-scale**, and **user-scalable=no**.

## Setting Keyboard and Mouse Wheel Zoom

By default, ArkWeb supports zooming by pressing the **Ctrl**+**'-'/'+'** keys or using the mouse wheel with the **Ctrl** key. An application can intercept keyboard events to disable keyboard zoom.

Example of intercepting keyboard events to disable keyboard zoom:

import { webview } from '@kit.ArkWeb';
import { KeyCode } from '@kit.InputKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
        .onKeyPreIme((event) => {
          if (event.type === KeyType.Down &&
          event.getModifierKeyState &&
          event.getModifierKeyState(\['Ctrl'\]) &&
            (event.keyCode === KeyCode.KEYCODE\_MINUS || event.keyCode === KeyCode.KEYCODE\_EQUALS ||
              event.keyCode === KeyCode.KEYCODE\_NUMPAD\_SUBTRACT || event.keyCode === KeyCode.KEYCODE\_NUMPAD\_ADD)) {
            return true;
          }
          return false;
        })
    }
  }
}

You can also use the [zoomControlAccess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#zoomcontrolaccess22) attribute to set whether to allow zooming by using the combination keys (**Ctrl** + '**\-**/**+**' or **Ctrl** + mouse wheel/touchpad).

// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomControlAccess(false)
    }
  }
}

#### Listening for Page Zoom Scale Changes

The application can listen for page zoom scale changes through the [onScaleChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onscalechange9) API. This API event corresponds to the gesture event (zoom with two fingers). **event.newScale** corresponds to the web page attribute **visualViewport.scale**.

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScaleChange((event) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
        })
    }
  }
}

#### Controlling Page Zoom Scale

You can use the [initialScale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#initialscale9) attribute to set the initial page zoom scale.

You can call the [zoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoom), [zoomIn](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoomin) and [zoomOut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoomout) APIs to control the page zoom scale.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/z7_YwXCuRwuk5GJ21LUw4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061948Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7A31260EB5DCBF559977167FCD444AE5EA914E3F9E7DFC404BEDAE87CF75229)

When the preceding APIs are used to control page zooming, you must set **zoomAccess** to **true**. Otherwise, the **zoom** class APIs throw exception 17100004.

## Zooming at Fixed Scale

You can use **zoomIn** to zoom in the current web page by 25% or **zoomOut** to zoom out the current web page by 20%.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('zoomIn')
        .onClick(() => {
          try {
            this.controller.zoomIn();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Button('zoomOut')
        .onClick(() => {
          try {
            this.controller.zoomOut();
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}

## Controlling Zoom Scale Based on Input Values

You can use **zoom** to zoom in or out on the current web page. When the input parameter is set to **1**, the default page size is used. When the input parameter is set to a value less than 1, the page is zoomed out. When the input parameter is set to a value greater than 1, the page is zoomed in. The value must be greater than 0.

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State factor: number = 1;

  build() {
    Column() {
      TextInput()
        .type(InputType.NUMBER\_DECIMAL)
        .onChange((value)=>{
          this.factor = Number(value);
        })
      Button('zoom')
        .onClick(() => {
          try {
            this.controller.zoom(this.factor);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/S_sMwV4ES_eRYdodjTH_SQ/en-us_image_0000002568764735.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061948Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FF074C55523F51EF2C7B13469CB1450B2051A4679BFF5AFBC1AFFDF69B0642A)

## Zooming to Target Scale

You can call the **onScaleChange** API to obtain the current page zoom scale, and then call the **zoom** API to zoom in or out the page to the specified scale. You can calculate the input parameter of **zoom** based on **pageFactor** and **targetFactor** as follows:

factor = 100 \* targetFactor / pageFactor

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State targetFactor: number = 1;
  // This represents the page zoom level
  @State pageFactor: number = 100;
  // Represents the integer 100
  intNumber: number = 100;

  build() {
    Column() {
      TextInput()
        .type(InputType.NUMBER\_DECIMAL)
        .onChange((value)=>{
          this.targetFactor = Number(value);
        })
      Button('zoom')
        .onClick(() => {
          try {
            let factor = this.targetFactor \* this.intNumber / this.pageFactor;
            this.controller.zoom(factor);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
        .onScaleChange((event) => {
          console.error('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
          this.pageFactor = event.newScale;
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DAlQc1_WQ_25C-hJtLpQQw/en-us_image_0000002537765010.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061948Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73A1F5B642D5CA77736AB7FDE2CD8F95A2B30BD8AB19B5FF4A3658189257DE1A)
