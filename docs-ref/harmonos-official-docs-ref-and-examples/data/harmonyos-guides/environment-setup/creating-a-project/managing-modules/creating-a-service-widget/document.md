# Creating a Service Widget

#### Overview

[Service widgets](../../../../application-framework/form-kit/about-this-kit/document.md) present important information about apps/atomic services, allowing users to access desired features instantly via shortcut gestures.

Widgets are classified as static widgets and dynamic widgets. Static widgets occupy less memory, which helps optimize overall device memory. They support static information display, refresh, and tap-to-navigate features. Dynamic widgets support custom interactions, animations, and scrolling. They offer rich functionality but consume more memory.

From the perspective of build products, widget packages are classified into shared packages and standalone packages. For details, see [Creating an ArkTS Widget](../../../../application-framework/form-kit/arkts-widget-development-recommended/creating-an-arkts-widget/document.md).

| 
Creation Mode

 | 

Widget Type

 |
| :-- | :-- |
| 

Shared package

 | 

Static widget

 |
| 

Dynamic widget

 |
| 

Standalone package

 | 

Static standalone widget

 |
| 

Dynamic standalone widget

 |

After creating a widget, you can select different widget templates based on service requirements. The following table lists the widget templates and their descriptions.

| 
Template

 | 

Supported Device Type

 | 

Programming Language

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

Hello World

 | 

Phones, tablets, 2-in-1 devices, wearables, cars, and TVs

 | 

ArkTS, JS

 | 

This template implements a HelloWorld service widget for building the UI efficiently and intuitively. It can be in 6 x 4 dimensions.

 |
| 

Image With Information

 | 

Phones, tablets, 2-in-1 devices, wearables, and cars

 | 

ArkTS, JS

 | 

This template is used to display images and a certain amount of text in equal importance. The image size and text amount vary depending on the widget size to highlight key information.

 |
| 

Immersive Information

 | 

Phones, tablets, 2-in-1 devices, wearables, and cars

 | 

ArkTS, JS

 | 

This template delivers a touch of aesthetics and quality with a properly designed layout of information and background images, helping to create an immersive user experience.

 |
| 

List

 | 

Phones, tablets, 2-in-1 devices, and cars

 | 

ArkTS

 | 

This template provides basic list functionality. Currently, it is only available for dynamic service widgets using API version 11 or later.

 |
| 

Control Button

 | 

Phones, tablets, 2-in-1 devices, and cars

 | 

ArkTS

 | 

This template implements an actionable service widget that displays text information and buttons, with button clicks triggering events. Currently, it is only available for static service widgets using API version 11 or later.

 |
| 

Control Search

 | 

Phones, tablets, 2-in-1 devices, and cars

 | 

ArkTS

 | 

This template implements an actionable service widget applicable to search scenarios. Currently, it is only available for static service widgets using API version 11 or later.

 |

#### Constraints

-   Service widgets do not support debugging.
-   Only dynamic widgets of the application's Hello World, Image With Information, and Immersive Information types, as well as independent dynamic widgets, support the JS language. Atomic services do not support the JS language.
-   Since DevEco Studio 5.0.4 Release, widgets can be created for wearables in projects of API version 16 or later.
-   Since DevEco Studio 6.0.0 Beta3, widgets can be created for cars in projects of API version 20 or later.
-   Since DevEco Studio 6.0.0 Beta3, standalone static and dynamic widgets can be created for phones.
-   For DevEco Studio 5.1.1 Release (Build Version: 5.1.1.850), 6.0.0 Release (Build Version: 6.0.0.868), and later versions, widgets can be created for TVs in projects.
-   Within a project module, only one type of widget package (either shared package or standalone package) can be created.
-   Each module allows a maximum of 16 widgets.

#### Creating a Service Widget

After [creating a project](../../creating-a-project/document.md), you can create a widget as follows.

1.  Use either of the following methods:
    
    -   Select a file under a module (for example, an entry module), choose **File** > **New** > **Service Widget** on the menu bar, and [select a widget as required](#section6353219163116).
    -   Right-click a file under a module (for example, an entry module), choose **New** > **Service Widget** from the shortcut menu, and [select a widget as required](#section6353219163116).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/jQ3zTca4SyyCz9qcA5OqAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36A7451ABC7D12526EF64A74E88244FA7E851CF51E878199E416DEDB570190B2)
    
    -   In the stage model of API version 11 or later, no widget or EntryCard is created for a new atomic service project or a new model in an atomic service project by default.
    
2.  On the **Choose a Template for Your Service Widget** page, select a template and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/8eDmb7-cR460yZAEy6X6Yg/en-us_image_0000002532669861.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D32FF6A672B66CBF046401C580B7586FF0EE7B2AAB88E85506D9F609FA53602)
    
3.  On the **Configure Your Service Widget** page, set the following:
    
    -   **Service widget name**: service widget name, which must be unique in an app/atomic service and can contain only uppercase letters, lowercase letters, digits, and underscores (\_).
    -   **Display name**: service widget name displayed on the preview canvas. This field is only available for projects in the stage model of API version 11 or later.
    -   **Description**: description of the service widget.
    -   **Language**: programming language of the service widget, which can be ArkTS or JS.
    -   **Support dimensions**: dimensions of the service widget. Certain types of service widgets allow for multiple dimensions options. When a widget is created for the first time, an **EntryCard** folder is automatically generated for storing widget snapshots.
    -   **Default dimension**: default dimension of the service widget.
    -   **Ability name**: Form ability bound to the widget. You can select an existing one or create a new one.
    -   **Module name**: module to which the service widget belongs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/UXhrmMsKRUmBoHXub9sZrQ/en-us_image_0000002532669859.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1374CAE3014CD4EFC5A694ADF3A79D1F6B876FAF8F306F7B70391E10EB73638)
    
4.  When you have finished, click **Finish**. After the service widget is created, the tool automatically generates the layout file and writes the attributes of the service widget into the **form\_config.json** file. For details about the attributes, see [Configuring ArkTS Widget Configuration Files](../../../../application-framework/form-kit/arkts-widget-development-recommended/configuring-arkts-widget-configuration-files/document.md).
5.  Develop the service widget based on instructions in [ArkTS Widget Provider Development](../../../../application-framework/form-kit/arkts-widget-development-recommended/arkts-widget-provider-development/document.md).

#### Previewing a Service Widget

During widget development, you can preview them to ensure their functionality and appearance. The layout of a widget is designed in an ArkTS file. Once you have saved the layout file, you will be able to see layout changes in real time on the preview canvas. Widgets of phones and tablets can be previewed in three scenarios: Minimum, Default, and Maximum. Make sure your widget displays properly in all these scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/mNpeOGdlTGOpJTTwl0QBzw/en-us_image_0000002500909948.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E26247B2121B2F1E2A9B554B9B6BFDE49C2254FEE3422D384681194DEBED45AF)

For details about the preview features, see [Previewing the UI](../../../../coding-and-debugging/previewing-the-ui/document.md).
