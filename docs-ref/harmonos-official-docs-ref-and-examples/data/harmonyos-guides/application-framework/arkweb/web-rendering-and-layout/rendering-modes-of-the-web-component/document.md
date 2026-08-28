# Rendering Modes of the Web Component

The **Web** component provides two rendering modes, which can be adapted to different container sizes as required.

#### Asynchronous Rendering Mode (Default)

In asynchronous rendering mode (renderMode: [RenderMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-e#rendermode12).ASYNC\_RENDER), the **Web** component is treated as a graphics surface node and is displayed independently. You are advised to use this mode on application pages that consist of only **Web** components to improve performance and reduce power consumption.

-   The width and height of a **Web** component cannot exceed 7,680 pixels (physical pixels). Otherwise, a white screen is displayed.
-   Dynamic mode switching is not supported.

The **Web** component is expected to display the application page as a main body. As shown in figure 1, in this scenario, the height of the **Web** component is the same as or close to the height of a screen (embedded in the navigation). The height of the HTML 5 page to be loaded is greater than the height of the **Web** component, and a scroll bar is generated inside the **Web** component. Users can scroll the scroll bar to view information on the HTML 5 page. Only **Web** components are required to implement the main content of application services. The asynchronous rendering mode is recommended to improve performance.

**Figure 1 Asynchronous rendering mode**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Pk6XlbG9ReSRUgJf-6JSmA/en-us_image_0000002537764998.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B602108C69CFAC1436CF167DAB4FA1D390C32B168C8AC744C0FEEF8263F6F1DC)

#### Synchronous Rendering Mode

In synchronous rendering mode (renderMode: [RenderMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-e#rendermode12).SYNC\_RENDER), the **Web** component is treated as the graphics canvas node and is displayed together with the system component. In this case, longer **Web** component content can be rendered, but the performance consumption increases.

-   Direct Digital Synthesis (DSS) is not supported.
-   Dynamic mode switching is not supported.

The **Web** component is expected to be a part of the application page as the carrier of rich text display and interact with other ArkUI components. As shown in Figure 2, the height of the HTML5 page is the same as that of the **Web** component. No scroll bar is generated in the **Web** component and the **Web** component is displayed as an ultra-long component. The **Scroll** component is used to implement internal scrolling of the application, ensuring that users can smoothly browse the web content and other ArkUI component content. To implement this page layout, you are advised to use the synchronous rendering mode.

**Figure 2 Synchronous rendering mode**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/I9JlpbTvQBinha_nxCMP1A/en-us_image_0000002537924938.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01F5F8BB339443854D57DDBE8CA993F3C959E7086B27477B7E8C6ABA6D1340C8)

#### Sample Code

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebHeightPage {
  private webviewController: WebviewController = new webview.WebviewController()

  build() {
    Column() {
      Web({
        src: 'www.example.com',
        controller: this.webviewController,
        renderMode: RenderMode.ASYNC\_RENDER // Set the rendering mode.
      })
    }
  }
}
