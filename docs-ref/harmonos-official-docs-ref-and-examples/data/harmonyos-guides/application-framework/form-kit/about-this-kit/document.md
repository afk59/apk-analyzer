# About This Kit

Form Kit provides a development framework and APIs for embedding application information into system entries like the home screen and lock screen. It can extract key user information or frequent operations into service widgets (referred to as "widgets"), which can be added to the home screen and lock screen for easy access to information and direct service interactions.

#### Scenarios for Widget Usage

-   Supported devices: smartphones, tablets, PCs/2-in-1 devices, smart TVs, smart watches, and head units. This kit is not supported on lite wearables.
-   Supported application types: Widgets can be developed in both applications and atomic services.
-   Supported positions: Users can add widgets to the home screen and lock screen. Widgets cannot be embedded in common applications.
-   To use a widget:

1.  Touch and hold an application icon on the home screen to display the shortcut menu.
2.  Tap **widget**, go to the widget management page, and preview the widget.
3.  Tap the **Add to home** button. You can then view the widget on the home screen.

**Figure 1** Typical procedure of using a widget

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/yTAT3cSITou6xZoHk1UmDA/en-us_image_0000002568684763.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57B6B931B7F32781A6BE72E048E9B3DC5A026E698CDC663EEA9C28B816799253)

#### Widget Architecture

**Figure 2** Widget architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/zQHBKBs7QFeSZ5VuxBlmuQ/en-us_image_0000002568764773.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=946A1422BF830CB44EA83E1AD475D538E267365FE72F55EC2983D24926101319)

**Fundamental Concepts in Widget Usage Scenarios**

-   Widget host: an application that displays the widget content and controls the widget location. It enables direct user interactions and manages widget addition, deletion, and display. An example is the home screen in the preceding figure.
-   Widget provider: an application or atomic service that provides the widget. It is responsible for implementing the widget features, including designing the UI, updating data, and handling click interactions.
-   Widget manager: a system service within the operating system that manages all widget information on the device. As a bridge between widget providers and hosts, it offers capabilities such as querying, adding, and deleting widget information to the hosts, and provides notifications like widget addition, deletion, refresh, and click events to the providers.

#### Features

-   Information display: Key information from applications or atomic services is displayed on the home screen as widgets. The information can be updated periodically so that users can view relevant information at any time.
    
-   Instant service access: Users can perform quick actions by touching buttons within the widget and can also navigate to the corresponding functional pages of the application or atomic service, achieving seamless one-step service access.
    

#### Development Modes

**Model Selection**

The system currently supports two application development models: stage and FA. Consequently, Form Kit accommodates both models for widget development, with a preference for the stage model.

**UI Development Paradigm Selection**

-   The stage model allows for two UI development paradigms for widgets: ArkTS-based declarative development paradigm (for developing ArkTS widgets) and web-like development paradigm (for developing JS widgets).
-   The FA model supports only the development of JS widgets with the web-like development paradigm.

ArkTS widgets and JS widgets have different implementation principles and features. The following table lists the differences in capabilities.

| Category | JS Widget | ArkTS Widget |
| :-- | :-- | :-- |
| Development paradigm | Web-like paradigm | Declarative paradigm |
| Component capability | Supported | Supported |
| Layout capability | Supported | Supported |
| Event capability | Supported | Supported |
| Custom animation | Not supported | Supported |
| Custom drawing | Not supported | Supported |
| Logic code execution | Not supported | Supported |

#### Related Kits

-   Ability Kit: Form Kit relies on the Extension abilities of Ability Kit for its internal implementation and interacts with Ability Kit during lifecycle scheduling.
-   ArkUI: Form Kit widget hosts can use some components, events, animations, and state management capabilities provided by ArkUI on their pages.
