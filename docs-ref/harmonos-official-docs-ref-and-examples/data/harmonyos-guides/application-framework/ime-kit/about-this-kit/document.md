# About This Kit

IME Kit is responsible for establishing a communication channel between the application in which the text input box is located and the input method application, to ensure that the two work together to provide text input, and also enables system applications to manage the input method application.

#### When to Use

IME Kit provides two types of APIs: input method framework APIs and input method service APIs. With these APIs, you can develop and manage an input method and implement a custom text input box.

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/RULzj8BxSZK84wxzvGzq5g/en-us_image_0000002568764795.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9D5D175338C97AF84E429A212C0F6089B69F134BCB9B2F5EA47CA137D24FF10)

#### Features

-   Input method:
    
    Comes with three types of panels: fixed, floating, and status bar. One input method can be deployed across different device types, such as smartphones and tablets.
    
-   Custom text input box:
    
    Can be bound to an input method and implement operations such as typing, deleting, selecting text and moving the cursor.
    

#### Available Capabilities

-   The APIs related to the input method service are provided for input methods. You can use these APIs to create a soft keyboard window, insert or delete characters, select text, and listen for physical keyboard key events.
    
-   The APIs related to the input method framework are provided for custom text input boxes. You can use these APIs to bind the text input box with an input method and implement operations such as typing, deleting, selecting text and moving the cursor.
    
-   APIs are also provided for system applications to manage input methods. For example, they can be used to display or hide the soft keyboard, switch between input methods, and obtain the list of input methods.
    

#### Relationship with Other Kits

ArkUI: With respect to soft keyboards and custom text input boxes, IME Kit can use some components, events, animations, and state management capabilities provided by ArkUI, for example, the **<Text>** and **<Button>** components and the **onClick** event.

#### Constraints

For the system API for switching between input method applications, the system permission is required. Some APIs can be called only by the current input method application.

#### API Reference

-   [inputMethodEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodengine)
    
-   [inputMethod](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod)
    
-   [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability)
    
-   [InputMethodExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-context)
    
-   [inputMethodList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethodlist)
    
-   [InputMethodSubtype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-subtype)
    
-   [inputMethod.Panel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-panel)
