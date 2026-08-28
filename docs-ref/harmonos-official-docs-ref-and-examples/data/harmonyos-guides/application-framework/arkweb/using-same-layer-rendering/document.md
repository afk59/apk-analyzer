# Using Same-Layer Rendering

In the system, applications can use the **Web** component to load web pages. If the capability or performance of non-system UI components is inferior to that of system components, you can use the ArkUI component to render these components (same-layer components).

#### When to Use

## On the Web Page

To improve the performance of an applet, you can use the ArkUI **XComponent** component to render the map component, and use the ArkUI **TextInput** component to render the input box component.

-   On the web page, you can render the UI components (same-layer tags) such as **<embed>** and **<object>** at the same layer based on certain rules. For details, see [Specifications and Constraints](#specifications-and-constraints).
    
-   On the application, you can use the same-layer rendering event reporting API of the **Web** component to detect the lifecycle and input event of the HTML5 same-layer tags, and process the service logic of the same-layer rendered components.
    
-   In addition, you can use ArkUI APIs such as **NodeContainer** to construct same-layer rendered components corresponding to HTML5 same-layer tags. Common ArkUI components that support same-layer rendering: [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput), [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent), [Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-canvas-canvas), [Video](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video), [Web](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web). For details, see [Specifications and Constraints](#specifications-and-constraints).
    

## On the Third-Party UI Framework

Flutter provides the **PlatformView** and **Texture** abstract components that can be rendered using system components, which complete the functionalities of the Flutter components. In the Weex 2.0 framework, the **Camera**, **Video**, and **Canvas** components can be rendered using system components to enhance functionality and performance.

-   Since third-party frameworks such as Flutter and Weex are not operated in the OS, the available third-party framework UI components that can be rendered at the same layer are not listed in the following.
    
-   On the application, you can use ArkUI APIs such as **NodeContainer** to construct same-layer rendered components corresponding to third-party framework same-layer tags. Common ArkUI components that support same-layer rendering: [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput), [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent), [Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-canvas-canvas), [Video](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video), [Web](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web). For details, see [Specifications and Constraints](#specifications-and-constraints).
    

#### Overall Architecture

The ArkWeb same-layer rendering feature supports same-layer tag lifecycle and event hit forwarding.

The lifecycle of same-layer tags is associated with front-end tags (<embed>/<object>). Events that hit the same-layer tags are reported to you, and you should distribute them to the corresponding component tree. The following figure shows the overall framework.

**Figure 1** Overall architecture of same-layer rendering

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/LUmUj229SOuZaWSTU_6gWw/en-us_image_0000002568764755.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71AE6A9EA1DCEBD09869F78EFBF4469951E0C0E15990C07E1C4CBEEC0514A196)

#### Specifications and Constraints

## ArkUI Components That Can Be Rendered at the Same Layer

The following specifications take effect in both web pages and third-party frameworks.

**Supported Components**:

-   Basic components: [AlphabetIndexer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-alphabet-indexer), [Blank](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-blank), [Button](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button), [CalendarPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-calendarpicker), [Checkbox](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-checkbox), [CheckboxGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-checkboxgroup), [ContainerSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-containerspan), [DataPanel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-datapanel), [DatePicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-datepicker), [Divider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-divider), [Gauge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-gauge), [Hyperlink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-hyperlink), [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image), [ImageAnimator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-imageanimator), [ImageSpan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-imagespan), [LoadingProgress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-loadingprogress), [Marquee](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-marquee), [PatternLock](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-patternlock), [Progress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-progress), [QRCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-qrcode), [Radio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-radio), [Rating](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-rating), [Refresh](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-refresh), [ScrollBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), [Search](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-search), [Span](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-span), [Select](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-select), [Slider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-slider), [Text](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-text), [TextArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea), [TextClock](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textclock), [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput), [TextPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textpicker), [TextTimer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-texttimer), [TimePicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-timepicker), [Toggle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-toggle)
    
-   Container components: [Badge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-badge), [Column](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-column), [ColumnSplit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-columnsplit), [Counter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-counter), [Flex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-flex), [GridCol](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-gridcol), [GridRow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-gridrow), [Grid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-grid), [GridItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-griditem) and [List](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-list), [ListItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitem), [ListItemGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-listitemgroup), [RelativeContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-relativecontainer), [Row](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-row), [RowSplit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-rowsplit), [Scroll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-scroll), [Stack](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-stack), [Swiper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-swiper), [Tabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabs), [TabContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-tabcontent), [NodeContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-nodecontainer), [SideBarContainer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-sidebarcontainer), [Stepper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-stepper), [StepperItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-stepperitem), [WaterFlow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-waterflow), [FlowItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-flowitem)
    
-   Self-drawing components: [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent), [Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-canvas-canvas), [Video](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video), [Web](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web)
    
-   Command-based custom drawing nodes: [BuilderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-buildernode), [ComponentContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-componentcontent), [ContentSlot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-components-contentslot), [FrameNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-framenode), [Graphics](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-graphics), [NodeController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-nodecontroller), [RenderNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-rendernode), [XComponentNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-xcomponentnode), [AttributeUpdater](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-attributeupdater) and [CAPI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule). (The components that support same-layer rendering are the same as that of ArkTS.)
    

**Supported Common Component Attributes and Events**:

-   Common attributes that are not supported: [restoreId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-restoreid) and [Special Effect Drawing Combination](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-use-effect).
    
-   Other attributes, events, and component capabilities that are not clearly marked as not supported are supported by default.
    

## Same-Layer Rendering Tags of the Web Page

This specification applies only to web pages and does not apply to third-party frameworks.

If an application needs to use same-layer rendering on a web page loaded by the **Web** component, you need to specify the **<embed>** and **<object>** tags on the web page as the same-layer rendered components based on the following specifications.

**Supported HTML5 Tags**:

-   **<embed>**: After same-layer rendering is enabled, only tags whose type is prefixed with **native** can be identified as same-layer components. Attributes cannot be customized.
    
-   **<object>**: After same-layer rendering is enabled, the **<object>** tag of the non-standard **MIME** type can be identified as a same-layer component and parsed based on the custom **param**/**value** attribute.
    
-   W3C standard tags (such as **<input>** and **<video>**) cannot be defined as same-layer tags.
    
-   The **<object>** and **<embed>** tags cannot be configured as the same-layer tags at the same time.
    
-   The tag types contain only English characters and are case insensitive.
    

**Supported CSS Attributes**:

**display**, **position**, **z-index**, **visibility**, **opacity**, **background-color**, **background-image**, **width**, **height**, **padding**, **padding-left**, **padding-top**, **padding-right**, **padding-bottom**, **margin**, **margin-left**, **margin-top**, **margin-right**, **margin-bottom**, **border-width**, **border-style**, **border-color**, **border-left-width**, **border-left-style**, **border-left-color**, **border-top-width**, **border-top-style**, **border-top-color**, **border-right-width**, **border-right-style**, **border-right-color**, **border-bottom-width**, **border-bottom-style**, **border-bottom-color**, **border-left**, **border-right**, **border-top**, **border-bottom**, **border**, **border-top-left-radius**, **border-top-right-radius**, **border-bottom-left-radius**, **border-bottom-right-radius**, **border-radius**, **transition**, and **transform** (Only **translate** and **scale** are supported. The value of **scale** must be greater than or equal to 0.)

Other CSS attributes, such as **rotate** and **skew** in the **transform** attribute, may not meet the expectation.

**Lifecycle Management**:

When the lifecycle of a tag at the same layer changes, the [onNativeEmbedLifecycleChange()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedlifecyclechange11) callback is triggered.

-   Creation, destruction, and position width and height change are supported.
    
-   Web pages containing same-layer components support back-forward cache.
    

**Distribution and Processing of the Input Events**:

-   The **DOWN**, **UP**, **MOVE**, and **CANCEL** touch events are supported. The [onnativeembedgestureevent11](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11) can be configured. By default, the touch event is consumed on the application side.
    
-   Application pages with same-layer tags cannot be scaled, and scaling APIs such as [initialScale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#initialscale9), [zoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoom), [zoomIn](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoomin) and [zoomOut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#zoomout) are not supported.
    
-   Mouse, keyboard, and touchpad events are not supported.
    
-   By default, the mouse and touchpad left button events (**MousePress**/**MouseRelease**/**MouseMOVE**) can be converted into touch events (**TouchDOWN**/**TouchUP**/**TouchMOVE**) for reporting.
    

**Visibility Changes**:

The [onNativeEmbedVisibilityChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedvisibilitychange12) callback is triggered when the visibility of the same-layer tag changes.

-   The visibility of the same-layer tag relative to the viewport can be reported.
    
-   By default, visibility changes caused by the CSS style or size change of the same-layer tag are not reported. For details, see [onNativeEmbedVisibilityChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedvisibilitychange12).
    

Status change of the **param** element embedded in the same-layer rendering tag **<object>**:

The [onNativeEmbedObjectParamChange()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedobjectparamchange21) callback is triggered when the param element of the same-layer rendering tag **<object>** changes.

-   The addition, modification, and deletion of the **param** element can be reported.
    
-   A maximum of 500 **param** element changes can be reported at a time. More changes will be reported subsequently.
    
-   For details about the report, see [NativeEmbedParamDataInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-i#nativeembedparamdatainfo21).
    

**Constraints**:

-   A maximum of five same-layer tag can be displayed on a web page. Otherwise, the rendering performance deteriorates.
    
-   Due to GPU restrictions, the maximum height and texture size of a same-layer tag are 8000 px.
    
-   After same-layer rendering is enabled, all web pages opened by the **Web** component do not support the synchronous [rendering mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-e#rendermode12).
    
-   When the non-full-screen mode is changed to the full-screen mode, the **Video** component is exported through non-texture mode and the video playback status remains unchanged. When the non-full-screen mode is restored, the **Video** component is exported through texture mode and the video playback status remains unchanged.
    
-   The **Web** component supports only same-layer rendering nesting at one layer. Input events such as swiping, tapping, and touching and holding are supported. Dragging, rotating, and zooming are not supported.
    
-   In the page layout of ArkUI components (such as **TextInput**), you are advised to use a **Stack** component to wrap the same-layer **NodeContainer** and **BuilderNode** and ensure that they are in the same position. In addition, the **NodeContainer** must be aligned with the **<embed>**/**<object>** tag to ensure proper component interaction. If the positions of the two components are different, the following problems may occur: The position of the text selection box attached to the **TextInput**/**TextArea** component is incorrect (as shown in the following figure). The animation start and stop of the **LoadingProgress**/**Marquee** component do not match the visibility status of the component.
    
    **Figure 2** Misplaced **TextInput** without **Stack**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/oIHSq8f3QOWqsXBMgH6Snw/en-us_image_0000002537765030.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=342E116094EB739DD5DF2B219984651F0D29F49BC709273C8194D8D6AD845BD1)
    
    **Figure 3** Proper **TextInput** with **Stack**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/nBzUO5SDQlqZKfNnc8DMSA/en-us_image_0000002537924970.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8070F62BDC1DDDEC166902FF8E8D65C9635FAA3F0AE8AF36B6C98CCAC936E1A5)
    

#### Rendering Text Boxes at the Same Layer on Web Pages

On web pages, you can render the system ArkUI **TextInput** components at the same layer. The following figure shows the effect of three text boxes that are rendered at the same layer.

**Figure 4** Same-layer rendering text boxes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/aDD-hyMkRLWgkL9ImPp9cw/en-us_image_0000002568684747.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59A16706098640F42548AB1E6255D3DE4C93512BF316392508911347DEF343C5)

1.  Mark the HTML tags that need to be rendered at the same layer on the web page.
    
    The **<embed>** and **<object>** tags support same-layer rendering, and the **type** can be specified randomly. They are case insensitive and will be converted to lowercase letters by the ArkWeb kernel. The **tag** string is matched using the entire string, and the **type** string is matched using the prefix.
    
    If this API is not used or receives an invalid string (empty string), the ArkWeb kernel uses the default setting, that is, "embed" + "native/" prefix. If the specified **type** is the same as the W3C standard **<object>** or **<embed>** type, for example, **registerNativeEmbedRule**("**object**," "**application**/**pdf**"), ArkWeb will comply with the W3C standard behavior and will not identify it as a same-layer tag.
    
    -   Use the <embed> tags.
        
        <!--HAP's src/main/resources/rawfile/text.html-->
        <!DOCTYPE html>
        <html>
        <head>
            <title>Same-Layer Rendering HTML</title>
            <meta name="viewport">
        </head>
        
        <body style="background:white">
        
        <embed id = "input1" type="native/view" style="width: 100%; height: 100px; margin: 30px; margin-top: 600px"/>
        
        <embed id = "input2" type="native/view2" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"/>
        
        <embed id = "input3" type="native/view3" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"/>
        
        </body>
        </html>
        
    -   Use the <object> tags.
        
        Call **registerNativeEmbedRule** to register a **<object>** tag.
        
        // ...
        Web({src: $rawfile("text.html"), controller: this.browserTabController})
          // Register the same-layer tag of "object" and type of "test."
          .registerNativeEmbedRule("object", "test")
          // ...
        
        Example of using **registerNativeEmbedRule** on the frontend page, with the tag of "object" and type of "test":
        
        <!--HAP's src/main/resources/rawfile/text.html-->
        <!DOCTYPE html>
        <html>
        <head>
            <title>Same-Layer Rendering HTML</title>
            <meta name="viewport">
        </head>
        
        <body style="background:white">
        
        <object id = "input1" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 600px"></object>
        
        <object id = "input2" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"></object>
        
        <object id = "input3" type="test/input" style="width: 100%; height: 100px; margin: 30px; margin-top: 50px"></object>
        
        </body>
        </html>
        
2.  Use **enableNativeEmbedMode** to enable same-layer rendering on the application.
    
    The same-layer rendering feature is disabled by default. To enable this feature, set [enableNativeEmbedMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#enablenativeembedmode11).
    
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    @Entry
    @Component
    struct WebComponent {
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Web({ src: 'www.example.com', controller: this.controller })
            // Enable same-layer rendering.
            .enableNativeEmbedMode(true)
        }
      }
    }
    
3.  Create a custom component.
    
    The custom component is displayed as a system component in the corresponding area after same-layer rendering is enabled.
    
    @Component
    struct TextInputComponent {
      @Prop params: Params
      @State bkColor: Color = Color.White
    
      build() {
        Column() {
          TextInput({text: '', placeholder: 'please input your word...'})
            .placeholderColor(Color.Gray)
            .id(this.params?.elementId)
            .placeholderFont({size: 13, weight: 400})
            .caretColor(Color.Gray)
            .width(this.params?.width)
            .height(this.params?.height)
            .fontSize(14)
            .fontColor(Color.Black)
        }
        // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
        .width(this.params.width)
        .height(this.params.height)
      }
    }
    
    @Builder
    function TextInputBuilder(params:Params) {
      TextInputComponent({params: params})
        .width(params.width)
        .height(params.height)
        .backgroundColor(Color.White)
    }
    
4.  Create a node controller.
    
    The node controller is used to control and report node behaviors of the corresponding NodeContainer.
    
    class MyNodeController extends NodeController {
      private rootNode: BuilderNode<\[Params\]> | undefined | null;
      private embedId\_: string = "";
      private surfaceId\_: string = "";
      private renderType\_: NodeRenderType = NodeRenderType.RENDER\_TYPE\_DISPLAY;
      private width\_: number = 0;
      private height\_: number = 0;
      private type\_: string = "";
      private isDestroy\_: boolean = false;
    
      setRenderOption(params: NodeControllerParams) {
        this.surfaceId\_ = params.surfaceId;
        this.renderType\_ = params.renderType;
        this.embedId\_ = params.embedId;
        this.width\_ = params.width;
        this.height\_ = params.height;
        this.type\_ = params.type;
      }
    
      // Method that must be overridden. It is used to build the number of nodes and return the number of nodes that will be mounted to the corresponding NodeContainer.
      // Called when the corresponding NodeContainer is created or called by the rebuild method.
      makeNode(uiContext: UIContext): FrameNode | null {
        if (this.isDestroy\_) { // rootNode is null.
          return null;
        }
        if (!this.rootNode) {// rootNode is set to undefined.
          this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId\_, type: this.renderType\_ });
          if(this.rootNode) {
            this.rootNode.build(wrapBuilder(TextInputBuilder), {  textOne: "myTextInput", width: this.width\_, height: this.height\_  })
            return this.rootNode.getFrameNode();
          }else{
            return null;
          }
        }
        // Return the FrameNode object.
        return this.rootNode.getFrameNode();
      }
    
      updateNode(arg: Object): void {
        this.rootNode?.update(arg);
      }
    
      getEmbedId(): string {
        return this.embedId\_;
      }
      
      setDestroy(isDestroy: boolean): void {
        this.isDestroy\_ = isDestroy;
        if (this.isDestroy\_) {
          this.rootNode = null;
        }
      }
     
      postEvent(event: TouchEvent | undefined): boolean {
        return this.rootNode?.postTouchEvent(event) as boolean
      }
    }
    
5.  Listen for the lifecycle changes of the same-layer rendered tags.
    
    After this feature is enabled, the ArkWeb kernel triggers the callback registered by [onNativeEmbedLifecycleChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedlifecyclechange11) each time a same-layer rendered tag is used on the web page.
    
    Call [onNativeEmbedLifecycleChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedlifecyclechange11) to listen for the lifecycle changes of the same-layer rendered tags.
    
    build() {
      Row() {
        Column() {
          Stack() {
            ForEach(this.componentIdArr, (componentId: string) => {
              NodeContainer(this.nodeControllerMap.get(componentId))
                .position(this.positionMap.get(componentId))
                .width(this.widthMap.get(componentId))
                .height(this.heightMap.get(componentId))
            }, (embedId: string) => embedId)
            // Load the local text.html page.
            Web({src: $rawfile("text.html"), controller: this.browserTabController})
              // Enable same-layer rendering.
              .enableNativeEmbedMode(true)
                // Register the same-layer tag of <object> and type of "test."
              .registerNativeEmbedRule("object", "test")
                // Obtain the lifecycle change data of the <embed> tag.
              .onNativeEmbedLifecycleChange((embed) => {
                console.info("NativeEmbed surfaceId" + embed.surfaceId);
                // If embed.info.id is used as the key for mapping nodeController, explicitly specify the ID on the HTML5 page.
                const componentId = embed.info?.id?.toString() as string
                if (embed.status == NativeEmbedStatus.CREATE) {
                  console.info("NativeEmbed create" + JSON.stringify(embed.info));
                  // Create a node controller and set parameters.
                  let nodeController = new MyNodeController()
                  // The unit of embed.info.width and embed.info.height is px, which needs to be converted to the default unit vp on the eTS side.
                  nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
                    type : embed.info?.type as string,
                    renderType : NodeRenderType.RENDER\_TYPE\_TEXTURE,
                    embedId : embed.embedId as string,
                    width : this.uiContext.px2vp(embed.info?.width),
                    height : this.uiContext.px2vp(embed.info?.height)})
                  this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                  nodeController.setDestroy(false);
                  // Save the nodeController instance to the Map, with the Id attribute of the embed tag passed in by the Web component as the key.
                  this.nodeControllerMap.set(componentId, nodeController);
                  this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                  this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                  this.positionMap.set(componentId, this.edges);
                  // Save the Id attribute of the embed tag passed in by the Web component to the @State decorated variable for dynamically creating a nodeContainer. The push action must be executed after the set action.
                  this.componentIdArr.push(componentId)
                } else if (embed.status == NativeEmbedStatus.UPDATE) {
                  let nodeController = this.nodeControllerMap.get(componentId);
                  console.info("NativeEmbed update" + JSON.stringify(embed));
                  this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                  this.positionMap.set(componentId, this.edges);
                  this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                  this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                  nodeController?.updateNode({textOne: 'update', width: this.uiContext.px2vp(embed.info?.width), height: this.uiContext.px2vp(embed.info?.height)} as ESObject)
                } else if (embed.status == NativeEmbedStatus.DESTROY) {
                  console.info("NativeEmbed destroy" + JSON.stringify(embed));
                  let nodeController = this.nodeControllerMap.get(componentId);
                  nodeController?.setDestroy(true);
                  this.nodeControllerMap.delete(componentId);
                  this.positionMap.delete(componentId);
                  this.widthMap.delete(componentId);
                  this.heightMap.delete(componentId);
                  this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
                } else {
                  console.info("NativeEmbed status" + embed.status);
                }
              })
          }.height("80%")
        }
      }
    }
    
6.  Listen for gesture events of same-layer rendered region.
    
    When this feature is enabled, the ArkWeb kernel triggers the callback registered by [onNativeEmbedGestureEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11) each time a touch operation is performed in the same-layer rendered region.
    
    Call [onNativeEmbedGestureEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedgestureevent11) to listen for gesture events of the same-layer rendered region.
    
    build() {
      Row() {
        Column() {
          Stack() {
            ForEach(this.componentIdArr, (componentId: string) => {
              NodeContainer(this.nodeControllerMap.get(componentId))
                .position(this.positionMap.get(componentId))
                .width(this.widthMap.get(componentId))
                .height(this.heightMap.get(componentId))
            }, (embedId: string) => embedId)
            // Load the local text.html page.
            Web({src: $rawfile("text.html"), controller: this.browserTabController})
              // Enable same-layer rendering.
              .enableNativeEmbedMode(true)
                // Obtain the lifecycle change data of the <embed> tag.
              .onNativeEmbedLifecycleChange((embed) => {
                // Implement lifecycle changes.
              })
              .onNativeEmbedGestureEvent((touch) => {
                console.info("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
                this.componentIdArr.forEach((componentId: string) => {
                  let nodeController = this.nodeControllerMap.get(componentId);
                  // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                  if(nodeController?.getEmbedId() == touch.embedId) {
                    let ret = nodeController?.postEvent(touch.touchEvent)
                    if(ret) {
                      console.info("onNativeEmbedGestureEvent success " + componentId);
                    } else {
                      console.info("onNativeEmbedGestureEvent fail " + componentId);
                    }
                    if(touch.result) {
                      // Notify the Web component of the consumption result of the gesture event.
                      touch.result.setGestureEventResult(ret);
                    }
                  }
                })
              })
          }
        }
      }
    }
    
7.  Listen for mouse events of the same-layer rendered region.
    
    After this feature is enabled, the ArkWeb kernel triggers the callback registered by [onNativeEmbedMouseEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedmouseevent20) when the following operations are performed in the same-layer rendered area:
    
    -   Tapping or holding with the left, middle, or right mouse button.
    -   Tapping or holding the left, middle, or right mouse button using the touchpad.
    
    Call [onNativeEmbedMouseEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-events#onnativeembedmouseevent20) to listen for the mouse events in the same-layer rendering region.
    
    build() {
      Row() {
        Column() {
          Stack() {
            ForEach(this.componentIdArr, (componentId: string) => {
              NodeContainer(this.nodeControllerMap.get(componentId))
                .position(this.positionMap.get(componentId))
                .width(this.widthMap.get(componentId))
                .height(this.heightMap.get(componentId))
            }, (embedId: string) => embedId)
            // Load the local text.html page.
            Web({src: $rawfile("text.html"), controller: this.browserTabController})
              // Enable same-layer rendering.
              .enableNativeEmbedMode(true)
                // Obtain the lifecycle change data of the <embed> tag.
              .onNativeEmbedLifecycleChange((embed) => {
                // Implement lifecycle changes.
              })
              .onNativeEmbedGestureEvent((touch) => {
                // Process the gesture event at the same layer.
              })
              .onNativeEmbedMouseEvent((mouse) => {
                console.info("NativeEmbed onNativeEmbedMouseEvent" + JSON.stringify(mouse.mouseEvent));
                this.componentIdArr.forEach((componentId: string) => {
                  let nodeController = this.nodeControllerMap.get(componentId);
                  // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                  if(nodeController?.getEmbedId() == mouse.embedId) {
                    let ret = nodeController?.postInputEvent(mouse.mouseEvent)
                    if(ret) {
                      console.info("onNativeEmbedMouseEvent success " + componentId);
                    } else {
                      console.info("onNativeEmbedMouseEvent fail " + componentId);
                    }
                    if(mouse.result) {
                      // Notify the Web component of the consumption result of the mouse event.
                      mouse.result.setMouseEventResult(ret);
                    }
                  }
                })
              })
          }
        }
      }
    }
    

**Sample Code**

To start with, add network permissions to **module.json5**. For details, see [Declaring Permissions in the Configuration File](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).

"requestPermissions":\[
  {
    "name" : "ohos.permission.INTERNET"
  }
\],

Code on the application side:

// Create a NodeController instance.
import { webview } from '@kit.ArkWeb';
import { UIContext } from '@kit.ArkUI';
import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';

@Observed
declare class Params{
  elementId: string
  textOne: string
  textTwo: string
  width: number
  height: number
}

declare class NodeControllerParams {
  surfaceId: string
  type: string
  renderType: NodeRenderType
  embedId: string
  width: number
  height: number
}

// The NodeController instance must be used with a NodeContainer for controlling and feeding back the behavior of the nodes in the container.
class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | undefined | null;
  private embedId\_: string = "";
  private surfaceId\_: string = "";
  private renderType\_: NodeRenderType = NodeRenderType.RENDER\_TYPE\_DISPLAY;
  private width\_: number = 0;
  private height\_: number = 0;
  private type\_: string = "";
  private isDestroy\_: boolean = false;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId\_ = params.surfaceId;
    this.renderType\_ = params.renderType;
    this.embedId\_ = params.embedId;
    this.width\_ = params.width;
    this.height\_ = params.height;
    this.type\_ = params.type;
  }

  // Method that must be overridden. It is used to build the number of nodes and return the number of nodes that will be mounted to the corresponding NodeContainer.
  // Called when the corresponding NodeContainer is created or called by the rebuild method.
  makeNode(uiContext: UIContext): FrameNode | null {
    if (this.isDestroy\_) { // rootNode is null.
      return null;
    }
    if (!this.rootNode) {// rootNode is set to undefined.
      this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId\_, type: this.renderType\_ });
      if(this.rootNode) {
        this.rootNode.build(wrapBuilder(TextInputBuilder), {  textOne: "myTextInput", width: this.width\_, height: this.height\_  })
        return this.rootNode.getFrameNode();
      }else{
        return null;
      }
    }
    // Return the FrameNode object.
    return this.rootNode.getFrameNode();
  }

  updateNode(arg: Object): void {
    this.rootNode?.update(arg);
  }

  getEmbedId(): string {
    return this.embedId\_;
  }

  setDestroy(isDestroy: boolean): void {
    this.isDestroy\_ = isDestroy;
    if (this.isDestroy\_) {
      this.rootNode = null;
    }
  }

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean
  }

  postInputEvent(event: MouseEvent | undefined): boolean {
    return this.rootNode?.postInputEvent(event) as boolean
  }
}

@Component
struct TextInputComponent {
  @Prop params: Params
  @State bkColor: Color = Color.White

  build() {
    Column() {
      TextInput({text: '', placeholder: 'please input your word...'})
        .placeholderColor(Color.Gray)
        .id(this.params?.elementId)
        .placeholderFont({size: 13, weight: 400})
        .caretColor(Color.Gray)
        .fontSize(14)
        .fontColor(Color.Black)
    }
    // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
    .width(this.params.width)
    .height(this.params.height)
  }
}

// In @Builder, add the specific dynamic component content.
@Builder
function TextInputBuilder(params:Params) {
  TextInputComponent({params: params})
    .width(params.width)
    .height(params.height)
    .backgroundColor(Color.White)
}

@Entry
@Component
struct Page{
  browserTabController: WebviewController = new webview.WebviewController()
  private nodeControllerMap: Map<string, MyNodeController> = new Map();
  @State componentIdArr: Array<string> = \[\];
  @State widthMap: Map<string, number> = new Map();
  @State heightMap: Map<string, number> = new Map();
  @State positionMap: Map<string, Edges> = new Map();
  @State edges: Edges = {};
  uiContext: UIContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Stack() {
          ForEach(this.componentIdArr, (componentId: string) => {
            NodeContainer(this.nodeControllerMap.get(componentId))
              .position(this.positionMap.get(componentId))
              .width(this.widthMap.get(componentId))
              .height(this.heightMap.get(componentId))
          }, (embedId: string) => embedId)
          // Load the local text.html page.
          Web({src: $rawfile("text.html"), controller: this.browserTabController})
            // Enable same-layer rendering.
            .enableNativeEmbedMode(true)
            // Obtain the lifecycle change data of the <embed> tag.
            .onNativeEmbedLifecycleChange((embed) => {
               console.info("NativeEmbed surfaceId" + embed.surfaceId);
               // If embed.info.id is used as the key for mapping nodeController, explicitly specify the ID on the HTML5 page.
               const componentId = embed.info?.id?.toString() as string
               if (embed.status == NativeEmbedStatus.CREATE) {
                 console.info("NativeEmbed create" + JSON.stringify(embed.info));
                 // Create a node controller and set parameters.
                 let nodeController = new MyNodeController()
                 // The unit of embed.info.width and embed.info.height is px, which needs to be converted to the default unit vp on the eTS side.
                 nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
                   type : embed.info?.type as string,
                   renderType : NodeRenderType.RENDER\_TYPE\_TEXTURE,
                   embedId : embed.embedId as string,
                   width : this.uiContext.px2vp(embed.info?.width),
                   height : this.uiContext.px2vp(embed.info?.height)})
                 this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                 nodeController.setDestroy(false);
                 // Save the nodeController instance to the Map, with the Id attribute of the embed tag passed in by the Web component as the key.
                 this.nodeControllerMap.set(componentId, nodeController);
                 this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                 this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                 this.positionMap.set(componentId, this.edges);
                 // Save the Id attribute of the embed tag passed in by the Web component to the @State decorated variable for dynamically creating a nodeContainer. The push action must be executed after the set action.
                 this.componentIdArr.push(componentId)
               } else if (embed.status == NativeEmbedStatus.UPDATE) {
                 let nodeController = this.nodeControllerMap.get(componentId);
                 console.info("NativeEmbed update" + JSON.stringify(embed));
                 this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                 this.positionMap.set(componentId, this.edges);
                 this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                 this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                 nodeController?.updateNode({textOne: 'update', width: this.uiContext.px2vp(embed.info?.width), height: this.uiContext.px2vp(embed.info?.height)} as ESObject)
               } else if (embed.status == NativeEmbedStatus.DESTROY) {
                 console.info("NativeEmbed destroy" + JSON.stringify(embed));
                 let nodeController = this.nodeControllerMap.get(componentId);
                 nodeController?.setDestroy(true);
                 this.nodeControllerMap.delete(componentId);
                 this.positionMap.delete(componentId);
                 this.widthMap.delete(componentId);
                 this.heightMap.delete(componentId);
                 this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
               } else {
                 console.info("NativeEmbed status" + embed.status);
               }
             })// Obtain the touch event information of components for same-layer rendering.
            .onNativeEmbedGestureEvent((touch) => {
              console.info("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
              this.componentIdArr.forEach((componentId: string) => {
                let nodeController = this.nodeControllerMap.get(componentId);
                // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                if(nodeController?.getEmbedId() == touch.embedId) {
                  let ret = nodeController?.postEvent(touch.touchEvent)
                  if(ret) {
                    console.info("onNativeEmbedGestureEvent success " + componentId);
                  } else {
                    console.info("onNativeEmbedGestureEvent fail " + componentId);
                  }
                  if(touch.result) {
                    // Notify the Web component of the consumption result of the gesture event.
                    touch.result.setGestureEventResult(ret);
                  }
                }
              })
            })
            .onNativeEmbedMouseEvent((mouse) => {
              console.info("NativeEmbed onNativeEmbedMouseEvent" + JSON.stringify(mouse.mouseEvent));
              this.componentIdArr.forEach((componentId: string) => {
                let nodeController = this.nodeControllerMap.get(componentId);
                // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                if(nodeController?.getEmbedId() == mouse.embedId) {
                  let ret = nodeController?.postInputEvent(mouse.mouseEvent)
                  if(ret) {
                    console.info("onNativeEmbedMouseEvent success " + componentId);
                  } else {
                    console.info("onNativeEmbedMouseEvent fail " + componentId);
                  }
                  if(mouse.result) {
                    // Notify the Web component of the consumption result of the mouse event.
                    mouse.result.setMouseEventResult(ret);
                  }
                }
              })
            })
        }
      }
    }
  }
}

#### Drawing the XComponent+AVPlayer and Button Components

-   Example of using same-layer rendering on the application side:
    
    // HAP's src/main/ets/pages/Index.ets
    // Create a NodeController instance.
    import { webview } from '@kit.ArkWeb';
    import { UIContext, NodeController, BuilderNode, NodeRenderType, FrameNode } from "@kit.ArkUI";
    import { AVPlayerDemo } from './PlayerDemo';
    
    @Observed
    declare class Params {
      textOne : string
      textTwo : string
      width : number
      height : number
    }
    
    declare class NodeControllerParams {
      surfaceId : string
      type : string
      renderType : NodeRenderType
      embedId : string
      width : number
      height : number
    }
    
    // The NodeController instance must be used with a NodeContainer for controlling and feeding back the behavior of the nodes in the container.
    class MyNodeController extends NodeController {
      private rootNode: BuilderNode<\[Params\]> | undefined | null;
      private embedId\_ : string = "";
      private surfaceId\_ : string = "";
      private renderType\_ :NodeRenderType = NodeRenderType.RENDER\_TYPE\_DISPLAY;
      private width\_ : number = 0;
      private height\_ : number = 0;
      private type\_ : string = "";
      private isDestroy\_ : boolean = false;
    
      setRenderOption(params : NodeControllerParams) {
        this.surfaceId\_ = params.surfaceId;
        this.renderType\_ = params.renderType;
        this.embedId\_ = params.embedId;
        this.width\_ = params.width;
        this.height\_ = params.height;
        this.type\_ = params.type;
      }
      // Method that must be overridden. It is used to build the number of nodes and return the number of nodes that will be mounted to the corresponding NodeContainer.
      // Called when the corresponding NodeContainer is created or called by the rebuild method.
      makeNode(uiContext: UIContext): FrameNode | null{
        if (this.isDestroy\_) { // rootNode is null.
          return null;
        }
        if (!this.rootNode) { // rootNode is set to undefined.
          this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId\_, type: this.renderType\_});
          if (this.type\_ === 'native/video') {
            this.rootNode.build(wrapBuilder(VideoBuilder), {textOne: "myButton", width : this.width\_, height : this.height\_});
          } else {
            // other
          }
        }
        // Return the FrameNode object.
        return this.rootNode.getFrameNode();
      }
    
      updateNode(arg: Object): void {
        this.rootNode?.update(arg);
      }
      getEmbedId() : string {
        return this.embedId\_;
      }
    
      setDestroy(isDestroy : boolean) : void {
        this.isDestroy\_ = isDestroy;
        if (this.isDestroy\_) {
          this.rootNode = null;
        }
      }
    
      postEvent(event: TouchEvent | undefined) : boolean {
        return this.rootNode?.postTouchEvent(event) as boolean
      }
    
      postInputEvent(event: MouseEvent | undefined): boolean {
        return this.rootNode?.postInputEvent(event) as boolean
      }
    }
    
    @Component
    struct VideoComponent {
      @ObjectLink params: Params
      @State bkColor: Color = Color.Red
      mXComponentController: XComponentController = new XComponentController();
      @State player\_changed: boolean = false;
      player?: AVPlayerDemo;
    
      build() {
        Column() {
          Button(this.params.textOne)
    
          XComponent({ id: 'video\_player\_id', type: XComponentType.SURFACE, controller: this.mXComponentController})
            .border({width: 1, color: Color.Red})
            .onLoad(() => {
              this.player = new AVPlayerDemo();
              this.player.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
              this.player\_changed = !this.player\_changed;
              this.player.avPlayerLiveDemo()
            })
            .width(300)
            .height(200)
        }
        // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
        .width(this.params.width)
        .height(this.params.height)
      }
    }
    // In @Builder, add the specific dynamic component content.
    @Builder
    function VideoBuilder(params: Params) {
      VideoComponent({ params: params })
        .backgroundColor(Color.Gray)
    }
    
    @Entry
    @Component
    struct WebIndex {
      browserTabController: WebviewController = new webview.WebviewController()
      private nodeControllerMap: Map<string, MyNodeController> = new Map();
      @State componentIdArr: Array<string> = \[\];
      @State widthMap: Map<string, number> = new Map();
      @State heightMap: Map<string, number> = new Map();
      @State positionMap: Map<string, Edges> = new Map();
      @State edges: Edges = {};
      uiContext: UIContext = this.getUIContext();
    
      aboutToAppear() {
        // Enable web frontend page debugging.
        webview.WebviewController.setWebDebuggingAccess(true);
      }
    
      build(){
        Row() {
          Column() {
            Stack() {
              ForEach(this.componentIdArr, (componentId: string) => {
                NodeContainer(this.nodeControllerMap.get(componentId))
                  .position(this.positionMap.get(componentId))
                  .width(this.widthMap.get(componentId))
                  .height(this.heightMap.get(componentId))
              }, (embedId: string) => embedId)
              // Load the local test.html page.
              Web({ src: $rawfile("test.html"), controller: this.browserTabController })
                // Enable same-layer rendering.
                .enableNativeEmbedMode(true)
                  // Obtain the lifecycle change data of the <embed> tag.
                .onNativeEmbedLifecycleChange((embed) => {
                  console.info("NativeEmbed surfaceId" + embed.surfaceId);
                  // 1. If embed.info.id is used as the key for mapping nodeController, explicitly specify the ID on the HTML5 page.
                  const componentId = embed.info?.id?.toString() as string
                  if (embed.status == NativeEmbedStatus.CREATE) {
                    console.info("NativeEmbed create" + JSON.stringify(embed.info))
                    // Create a node controller and set parameters.
                    let nodeController = new MyNodeController()
                    // 1. The unit of embed.info.width and embed.info.height is px, which needs to be converted to the default unit vp on the eTS side.
                    nodeController.setRenderOption({surfaceId : embed.surfaceId as string, type : embed.info?.type as string,
                      renderType : NodeRenderType.RENDER\_TYPE\_TEXTURE, embedId : embed.embedId as string,
                      width : this.uiContext.px2vp(embed.info?.width), height : this.uiContext.px2vp(embed.info?.height)})
                    this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                    nodeController.setDestroy(false);
                    // Save the nodeController instance to the Map, with the Id attribute of the embed tag passed in by the Web component as the key.
                    this.nodeControllerMap.set(componentId, nodeController)
                    this.widthMap.set(componentId,  this.uiContext.px2vp(embed.info?.width));
                    this.heightMap.set(componentId,  this.uiContext.px2vp(embed.info?.height));
                    this.positionMap.set(componentId, this.edges);
                    // Save the Id attribute of the embed tag passed in by the Web component to the @State decorated variable for dynamically creating a nodeContainer. The push action must be executed after the set action.
                    this.componentIdArr.push(componentId)
                  } else if (embed.status == NativeEmbedStatus.UPDATE) {
                    let nodeController = this.nodeControllerMap.get(componentId)
                    this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                    this.positionMap.set(componentId, this.edges);
                    this.widthMap.set(componentId,  this.uiContext.px2vp(embed.info?.width));
                    this.heightMap.set(componentId,  this.uiContext.px2vp(embed.info?.height));
                    nodeController?.updateNode({textOne: 'update', width: this.uiContext.px2vp(embed.info?.width), height: this.uiContext.px2vp(embed.info?.height)} as ESObject)
                  } else if (embed.status == NativeEmbedStatus.DESTROY) {
                    let nodeController = this.nodeControllerMap.get(componentId);
                    nodeController?.setDestroy(true);
                    this.nodeControllerMap.delete(componentId);
                    this.positionMap.delete(componentId);
                    this.widthMap.delete(componentId);
                    this.heightMap.delete(componentId);
                    this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
                  } else {
                    console.info("NativeEmbed status" + embed.status);
                  }
                })// Obtain the touch event information of components for same-layer rendering.
                .onNativeEmbedGestureEvent((touch) => {
                  console.info("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
                  this.componentIdArr.forEach((componentId: string) => {
                    let nodeController = this.nodeControllerMap.get(componentId)
                    // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                    if (nodeController?.getEmbedId() === touch.embedId) {
                      let ret = nodeController?.postEvent(touch.touchEvent)
                      if (ret) {
                        console.info("onNativeEmbedGestureEvent success " + componentId)
                      } else {
                        console.info("onNativeEmbedGestureEvent fail " + componentId)
                      }
                      if (touch.result) {
                        // Notify the Web component of the consumption result of the gesture event.
                        touch.result.setGestureEventResult(ret);
                      }
                    }
                  })
                })
                .onNativeEmbedMouseEvent((mouse) => {
                  console.info("NativeEmbed onNativeEmbedMouseEvent" + JSON.stringify(mouse.mouseEvent));
                  this.componentIdArr.forEach((componentId: string) => {
                    let nodeController = this.nodeControllerMap.get(componentId);
                    // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                    if(nodeController?.getEmbedId() == mouse.embedId) {
                      let ret = nodeController?.postInputEvent(mouse.mouseEvent)
                      if(ret) {
                        console.info("onNativeEmbedMouseEvent success " + componentId);
                      } else {
                        console.info("onNativeEmbedMouseEvent fail " + componentId);
                      }
                      if(mouse.result) {
                        // Notify the Web component of the consumption result of the mouse event.
                        mouse.result.setMouseEventResult(ret);
                      }
                    }
                  })
                })
            }
          }
        }
      }
    }
    
-   Code example of video playback on the application side. Replace the URL with the correct video URL in practice.
    
    // HAP's src/main/ets/pages/PlayerDemo.ets
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export class AVPlayerDemo {
      private count: number = 0;
      private surfaceID: string = ''; // The surfaceID parameter specifies the window used to display the video. Its value is obtained through XComponent.
      private isSeek: boolean = true; // Specify whether the seek operation is supported.
    
      setSurfaceID(surface\_id: string){
        console.info('setSurfaceID : ' + surface\_id);
        this.surfaceID = surface\_id;
      }
      // Set AVPlayer callback functions.
      setAVPlayerCallback(avPlayer: media.AVPlayer) {
        // Callback function for the seek operation.
        avPlayer.on('seekDone', (seekDoneTime: number) => {
          console.info(\`AVPlayer seek succeeded, seek time is ${seekDoneTime}\`);
        })
        // Callback function for errors. If an error occurs during the operation on the AVPlayer, reset() is called to reset the AVPlayer.
        avPlayer.on('error', (err: BusinessError) => {
          console.error(\`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}\`);
          avPlayer.reset();
        })
        // Callback for state changes.
        avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
          switch (state) {
            case 'idle': // This state is reported upon a successful callback of reset().
              console.info('AVPlayer state idle called.');
              avPlayer.release(); // Call release() to release the instance.
              break;
            case 'initialized': // This state is reported when the AVPlayer sets the playback source.
              console.info('AVPlayer state initialized called.');
              avPlayer.surfaceId = this.surfaceID; // Set the window to display the video. This setting is not required when a pure audio asset is to be played.
              avPlayer.prepare();
              break;
            case 'prepared': // This state is reported upon a successful callback of prepare().
              console.info('AVPlayer state prepared called.');
              avPlayer.play(); // Call play() to start playback.
              break;
            case 'playing': // This state is reported upon a successful callback of play().
              console.info('AVPlayer state playing called.');
              if(this.count !== 0) {
                if (this.isSeek) {
                  console.info('AVPlayer start to seek.');
                  avPlayer.seek(avPlayer.duration); // Call seek() to seek to the end of the video clip.
                } else {
                  // When the seek operation is not supported, the playback continues until it reaches the end.
                  console.info('AVPlayer wait to play end.');
                }
              } else {
                avPlayer.pause(); // Call pause() to pause the playback.
              }
              this.count++;
              break;
            case 'paused': // This state is reported upon a successful callback of pause().
              console.info('AVPlayer state paused called.');
              avPlayer.play(); // Call play() again to start playback.
              break;
            case 'completed': // This state is reported upon the completion of the playback.
              console.info('AVPlayer state completed called.');
              avPlayer.stop(); // Call the playback API.
              break;
            case 'stopped': // This state is reported upon a successful callback of stop().
              console.info('AVPlayer state stopped called.');
              avPlayer.reset(); // Call reset() to reset the AVPlayer.
              break;
            case 'released': // This state is reported upon the release of the AVPlayer.
              console.info('AVPlayer state released called.');
              break;
            default:
              break;
          }
        })
      }
    
      // Set the live stream source through the URL.
      async avPlayerLiveDemo(){
        // Create an AVPlayer instance.
        let avPlayer: media.AVPlayer = await media.createAVPlayer();
        // Create a callback for state changes.
        this.setAVPlayerCallback(avPlayer);
        this.isSeek = false; // The seek operation is not supported.
        // Replace the URL with the actual URL of the video source.
        avPlayer.url = 'https://xxx.xxx/demo.mp4';
      }
    }
    
-   Example of the frontend page:
    
    <!--HAP's src/main/resources/rawfile/test.html-->
    <!DOCTYPE html>
    <html>
    <head>
        <title>Same-Layer Rendering Test HTML</title>
        <meta name="viewport">
    </head>
    <body>
    <div>
        <div id="bodyId">
            <embed id="nativeVideo" type = "native/video" width="1000" height="1500" src="test" style = "background-color:red"/>
        </div>
    </div>
    </body>
    </html>
    
-   Demo
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/WtnK1GARRvS_aHgD8flXQQ/en-us_image_0000002568764757.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=564819C250BE3EB37C5605B65B92C0FDA4B0B68BF1ED0384A91431452BE83D5A)
    

#### Setting the Same-Layer Tag to the Highest Level

The same-layer rendering supports the private attribute **arkwebnativestyle**, which takes effect only in **<embed>** and **<object>** after same-layer rendering is enabled. The **display** attribute of **arkwebnativestyle** is used to set the level of the same-layer tag to be above other web elements. When multiple same-layer tags have the same **display** value in **arkwebnativestyle**, their stacking order follows the W3C standard: first by **z-index**, then by their order in the DOM if **z-index** values are the same. The values of the **display** attribute are listed in the following table.

| Value | Description |
| :-- | :-- |
| overlay | Sets the level of the same-layer tag to be higher than that of other web elements. |
| overlay-infinity | Sets the level of the same-layer tag to be higher than that of other web elements and the same-layer tag with the **overlay** value. |

-   Code on the application side:
    
    import { webview } from '@kit.ArkWeb';
    import { UIContext } from '@kit.ArkUI';
    import { NodeController, BuilderNode, NodeRenderType, FrameNode } from '@kit.ArkUI';
    
    @Observed
    declare class Params{
      elementId: string
      textOne: string
      textTwo: string
      width: number
      height: number
    }
    
    declare class NodeControllerParams {
      surfaceId: string
      type: string
      renderType: NodeRenderType
      embedId: string
      width: number
      height: number
    }
    
    // The NodeController instance must be used with a NodeContainer for controlling and feeding back the behavior of the nodes in the container.
    class MyNodeController extends NodeController {
      private rootNode: BuilderNode<\[Params\]> | undefined | null;
      private embedId\_: string = "";
      private surfaceId\_: string = "";
      private renderType\_: NodeRenderType = NodeRenderType.RENDER\_TYPE\_DISPLAY;
      private width\_: number = 0;
      private height\_: number = 0;
      private type\_: string = "";
      private isDestroy\_: boolean = false;
    
      setRenderOption(params: NodeControllerParams) {
        this.surfaceId\_ = params.surfaceId;
        this.renderType\_ = params.renderType;
        this.embedId\_ = params.embedId;
        this.width\_ = params.width;
        this.height\_ = params.height;
        this.type\_ = params.type;
      }
    
      // Method that must be overridden. It is used to build the number of nodes and return the number of nodes that will be mounted to the corresponding NodeContainer.
      // Called when the corresponding NodeContainer is created or called by the rebuild method.
      makeNode(uiContext: UIContext): FrameNode | null {
        if (this.isDestroy\_) { // rootNode is null.
          return null;
        }
        if (!this.rootNode) {// rootNode is set to undefined.
          this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId\_, type: this.renderType\_ });
          if (this.type\_ == 'native/view1') {
            this.rootNode.build(wrapBuilder(TextInputBuilder1), {  textOne: "myTextInput", width: this.width\_, height: this.height\_  })
            return this.rootNode.getFrameNode();
          } else if (this.type\_ == 'native/view2') {
            this.rootNode.build(wrapBuilder(TextInputBuilder2), {  textOne: "myTextInput", width: this.width\_, height: this.height\_  })
            return this.rootNode.getFrameNode();
          } else{
            return null;
          }
        }
        // Return the FrameNode object.
        return this.rootNode.getFrameNode();
      }
    
      updateNode(arg: Object): void {
        this.rootNode?.update(arg);
      }
    
      getEmbedId(): string {
        return this.embedId\_;
      }
    
      setDestroy(isDestroy: boolean): void {
        this.isDestroy\_ = isDestroy;
        if (this.isDestroy\_) {
          this.rootNode = null;
        }
      }
    
      postEvent(event: TouchEvent | undefined): boolean {
        return this.rootNode?.postTouchEvent(event) as boolean
      }
    }
    
    @Component
    struct TextInputComponent1 {
      @Prop params: Params;
      @State bkColor: Color = Color.White;
    
      build() {
        Column() {
          Text("display:overlay-infinity")
          TextInput({text: '', placeholder: 'please input your word...'})
            .placeholderColor(Color.Gray)
            .id(this.params?.elementId)
            .placeholderFont({size: 13, weight: 400})
            .caretColor(Color.Gray)
            .fontSize(14)
            .fontColor(Color.Black)
        }
        // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
        .width(this.params.width)
        .height(this.params.height)
      }
    }
    
    // In @Builder, add the specific dynamic component content.
    @Builder
    function TextInputBuilder1(params:Params) {
      TextInputComponent1({params: params})
        .width(params.width)
        .height(params.height)
        .backgroundColor(Color.Pink)
    }
    
    @Component
    struct TextInputComponent2 {
      @Prop params: Params;
      @State bkColor: Color = Color.White;
    
      build() {
        Column() {
          Text("display:overlay")
          TextInput({text: '', placeholder: 'please input your word...'})
            .placeholderColor(Color.Gray)
            .id(this.params?.elementId)
            .placeholderFont({size: 13, weight: 400})
            .caretColor(Color.Gray)
            .fontSize(14)
            .fontColor(Color.Black)
        }
        // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
        .width(this.params.width)
        .height(this.params.height)
      }
    }
    
    
    // In @Builder, add the specific dynamic component content.
    @Builder
    function TextInputBuilder2(params:Params) {
      TextInputComponent2({params: params})
        .width(params.width)
        .height(params.height)
        .backgroundColor(Color.Gray)
    }
    
    @Entry
    @Component
    struct Page{
      browserTabController: webview.WebviewController = new webview.WebviewController();
      private nodeControllerMap: Map<string, MyNodeController> = new Map();
      @State componentIdArr: Array<string> = \[\];
      @State widthMap: Map<string, number> = new Map();
      @State heightMap: Map<string, number> = new Map();
      @State positionMap: Map<string, Edges> = new Map();
      @State edges: Edges = {};
      uiContext: UIContext = this.getUIContext();
    
      build() {
        Row() {
          Column() {
            Stack() {
              ForEach(this.componentIdArr, (componentId: string) => {
                NodeContainer(this.nodeControllerMap.get(componentId))
                  .position(this.positionMap.get(componentId))
                  .width(this.widthMap.get(componentId))
                  .height(this.heightMap.get(componentId))
              }, (embedId: string) => embedId)
              // Load the local text.html page.
              Web({src: $rawfile("overlay.html"), controller: this.browserTabController})
                // Enable same-layer rendering.
                .enableNativeEmbedMode(true)
                  // Obtain the lifecycle change data of the <embed> tag.
                .onNativeEmbedLifecycleChange((embed) => {
                  console.info("NativeEmbed surfaceId" + embed.surfaceId);
                  // If embed.info.id is used as the key for mapping nodeController, explicitly specify the ID on the HTML5 page.
                  const componentId = embed.info?.id?.toString() as string
                  if (embed.status == NativeEmbedStatus.CREATE) {
                    console.info("NativeEmbed create" + JSON.stringify(embed.info));
                    // Create a node controller and set parameters.
                    let nodeController = new MyNodeController()
                    // The unit of embed.info.width and embed.info.height is px, which needs to be converted to the default unit vp on the eTS side.
                    nodeController.setRenderOption({surfaceId : embed.surfaceId as string,
                      type : embed.info?.type as string,
                      renderType : NodeRenderType.RENDER\_TYPE\_TEXTURE,
                      embedId : embed.embedId as string,
                      width : this.uiContext.px2vp(embed.info?.width),
                      height : this.uiContext.px2vp(embed.info?.height)})
                    this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                    nodeController.setDestroy(false);
                    // Save the nodeController instance to the Map, with the Id attribute of the embed tag passed in by the Web component as the key.
                    this.nodeControllerMap.set(componentId, nodeController);
                    this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                    this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                    this.positionMap.set(componentId, this.edges);
                    // Save the Id attribute of the embed tag passed in by the Web component to the @State decorated variable for dynamically creating a nodeContainer. The push action must be executed after the set action.
                    this.componentIdArr.push(componentId)
                  } else if (embed.status == NativeEmbedStatus.UPDATE) {
                    let nodeController = this.nodeControllerMap.get(componentId);
                    console.info("NativeEmbed update" + JSON.stringify(embed));
                    this.edges = {left: \`${embed.info?.position?.x as number}px\`, top: \`${embed.info?.position?.y as number}px\`}
                    this.positionMap.set(componentId, this.edges);
                    this.widthMap.set(componentId, this.uiContext.px2vp(embed.info?.width));
                    this.heightMap.set(componentId, this.uiContext.px2vp(embed.info?.height));
                    nodeController?.updateNode({textOne: 'update', width: this.uiContext.px2vp(embed.info?.width), height: this.uiContext.px2vp(embed.info?.height)} as ESObject)
                  } else if (embed.status == NativeEmbedStatus.DESTROY) {
                    console.info("NativeEmbed destroy" + JSON.stringify(embed));
                    let nodeController = this.nodeControllerMap.get(componentId);
                    nodeController?.setDestroy(true);
                    this.nodeControllerMap.delete(componentId);
                    this.positionMap.delete(componentId);
                    this.widthMap.delete(componentId);
                    this.heightMap.delete(componentId);
                    this.componentIdArr = this.componentIdArr.filter((value: string) => value !== componentId);
                  } else {
                    console.info("NativeEmbed status" + embed.status);
                  }
                })// Obtain the touch event information of components for same-layer rendering.
                .onNativeEmbedGestureEvent((touch) => {
                  console.info("NativeEmbed onNativeEmbedGestureEvent" + JSON.stringify(touch.touchEvent));
                  this.componentIdArr.forEach((componentId: string) => {
                    let nodeController = this.nodeControllerMap.get(componentId);
                    // Send the obtained event of the region at the same layer to the nodeController corresponding to embedId of the region.
                    if(nodeController?.getEmbedId() == touch.embedId) {
                      let ret = nodeController?.postEvent(touch.touchEvent)
                      if(ret) {
                        console.info("onNativeEmbedGestureEvent success " + componentId);
                      } else {
                        console.info("onNativeEmbedGestureEvent fail " + componentId);
                      }
                      if(touch.result) {
                        // Notify the Web component of the consumption result of the gesture event.
                        touch.result.setGestureEventResult(ret);
                      }
                    }
                  })
                })
                .border({width: 2, color: Color.Gray})
                .height("50%")
            }
          }
        }
      }
    }
    
-   Example of a frontend page:
    
    The sample code uses the **<embed>** tag. To use the **<object>** tag, register it and **<type>** on the eTS side.
    
    <!--HAP's src/main/resources/rawfile/overlay.html-->
    <!DOCTYPE html>
    <html>
    <head>
        <title>Same-Layer Rendering HTML</title>
        <meta name="viewport" content="initial-scale=1.0">
    </head>
    <body>
    <div>
        <div id = "test" style = "position: absolute; z-index: 9999; text-align: center; background-color: rgb(61, 157, 180); top: 40px; left: 30px; width: 300px; height: 120px">
            z-index: 9999
        </div>
    
        <embed id = "input1" type = "native/view1" arkwebnativestyle = "display:overlay-infinity" style = "position: absolute; top: 60px; left: 50px; width: 300px; height: 100px">
    
        <embed id = "input2" type = "native/view2" arkwebnativestyle = "display:overlay" style = "position: absolute; top: 150px; left: 40px; width: 300px; height: 100px">
    </div>
    </body>
    </html>
    
-   Demo:
    
    The **display** attribute of **arkwebnativestyle** is not set.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/rs67IvRvQo-lArEenfzGTA/en-us_image_0000002537765032.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80D5CAB533DB47EC45205144E49D7A7B9554BD27874BBC3FC053303B5DDEDB84)
    
    The **display** attribute of **arkwebnativestyle** is set.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/qakU-T2-RWOkvLaXMK8YJg/en-us_image_0000002537924972.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F7E2246AA55A01DF7F0915AC6DB2DD566AA5D4A5DF000A005B656046D9D18E7)
    

#### FAQs

## What should I do if the same-layer rendered components are stretched?

-   The component height is too high.
    
    Due to GPU limitations, the maximum height of the same-layer tag is 8000 px. If this limit is exceeded, the component will be stretched. In this case, you need to set the height of the same-layer tag to less than 8000 px.
    
-   The width and height of the custom component do not match those of the same-layer rendered tag.
    
    The width and height of the custom same-layer rendered component must be the same as those of the same-layer tag. The following is an example:
    
      @Component
      struct TextInputComponent {
        @Prop params: Params
        @State bkColor: Color = Color.White
    
        build() {
          Column() {
            TextInput({text: '', placeholder: 'please input your word...'})
              .fontColor(Color.Black)
          }
          // The width and height of the outermost custom container component must be the same as those of the same-layer tag.
          .width(this.params.width)
          .height(this.params.height)
        }
      }
    

## How do I transparently transmit the events captured by the same-layer rendered component to the web front end?

For gesture events of the same-layer rendered tag, you can set the gesture event consumption result through [setGestureEventResult()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-eventresult#setgestureeventresult14). The gesture events can be consumed on the system component side or ArkWeb side. To consume gesture events on the system component side and ArkWeb side at the same time, set **stopPropagation** to **false** in [setGestureEventResult()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-eventresult#setgestureeventresult14). In this way, gesture events are propagated to ArkWeb when being consumed on the system component side.

## What should I do if plug-ins cannot be displayed on the same-layer rendered page?

-   The same-layer rendering [enableNativeEmbedMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#enablenativeembedmode11) is not enabled.
    
    Explicitly enable same-layer rendering.
    
    Web({ src: $rawfile("text.html"), controller: this.controller })
      // Enable same-layer rendering.
      .enableNativeEmbedMode(true)
    
-   The same-layer tag is incorrectly used.
    
    To use the **<embed>** tag, you need to explicitly write "embed" and use the **type** starting with "native/". To use the **<object>** tag, you need to register it and **type**.
    

## What should I do if the cursor and text box of the ArkUI component (such as TextInput) that involves UI interaction are misplaced?

You need to use a **Stack** to wrap the same-layer component container and **BuilderNode**. Then you need to bind **NodeContainer** to the position of the same-layer tag. The following is an example:

ForEach(this.componentIdArr, (componentId: string) => {
  NodeContainer(this.nodeControllerMap.get(componentId))
    // The same-layer component container should be bound to the width, height, and position of the same-layer tag.
    .position(this.positionMap.get(componentId))
    .width(this.widthMap.get(componentId))
    .height(this.heightMap.get(componentId))
}, (embedId: string) => embedId)
