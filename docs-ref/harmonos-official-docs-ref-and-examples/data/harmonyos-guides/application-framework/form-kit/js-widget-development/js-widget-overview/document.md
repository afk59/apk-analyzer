# JS Widget Overview

JS widgets, developed using a web-like paradigm (HML + CSS + JSON), now support two [application models](../../../ability-kit/application-models/document.md): the FA model and the stage model. For details, see [Developing a JS Widget (Stage Model)](../developing-a-js-widget-stage-model/document.md) and [Developing a JS Widget (FA Model)](../developing-a-js-widget-fa-model/document.md). When developing a new widget, you are advised to use the ArkTS declarative syntax to build UIs. For details about the differences between the declarative paradigm and web-like paradigm, see [About This Kit](../../../arkui/about-this-kit/document.md).

#### How to Implement

Below shows the working principles of a JS widget.

**Figure 1** Working principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/IywYigZ6Teumy9DAt4c8Yw/en-us_image_0000002537765068.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8E0DA56AD66FC9BB7B96A8E8F3A3348488E008618012C70A1CEE4E976A35BC7)

The widget host consists of the following modules:

-   Widget usage: provides operations such as creating, deleting, or updating a widget.
    
-   Communication adapter: provided by the SDK for communication with the Widget Manager. It sends widget-related operation instructions to the Widget Manager.
    

The Widget Manager consists of the following modules:

-   Periodic update: starts a scheduled task based on the update policy to periodically update a widget after it is added to the Widget Manager.
    
-   Cache manager: caches view information of a widget after it is added to the Widget Manager. This enables the cached data to be directly returned when the widget is obtained next time, greatly reducing the latency.
    
-   Lifecycle manager: suspends update when a widget is switched to the background or is blocked, and updates and/or clears widget data during upgrade and deletion.
    
-   Object manager: manages RPC objects of the widget host. It is used to verify requests from the widget host and process callbacks after the widget update.
    
-   Communication adapter: communicates with the widget host and provider through RPCs.
    

The widget provider consists of the following modules:

-   Widget service: implemented by the widget provider developer to process requests on widget creation, update, and deletion, and to provide corresponding widget services.
    
-   Instance manager: implemented by the widget provider developer for persistent management of widget instances allocated by the Widget Manager.
    
-   Communication adapter: provided by the SDK for communication with the Widget Manager. It pushes update data to the Widget Manager.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/Y9-9WNgQTxaoEOd0T717KQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FBBEC61E2C40586CECBD9D96EE9E715D0FC46F3BF45F81B13441EAADA776CFF)

You only need to develop the widget provider. The system automatically handles the work of the widget host and Widget Manager.
