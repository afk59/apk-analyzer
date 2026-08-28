# FormLink

The **FormLink** component is provided for interactions between static widgets and widget providers. It supports three types of events: router, message, and call.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/6CoWyvNXRg2qnwIeBsh5ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=689AC2B51F2025FE41AB99198697543588461FFBC84DFC2946AE041BAB499FEA)

-   This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.
    
-   This component can be used only in static widgets.
    
-   This document covers static widget development only. For comprehensive widget development guidance, see the [widget development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/formkit-overview).
    

#### Required Permissions

None

#### Child Components

This component supports only one child component.

#### APIs

FormLink(options: FormLinkOptions)

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FormLinkOptions](#formlinkoptions) | Yes | Widget information. |

#### FormLinkOptions

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| action | string | No | No | 
Action type.

\- **"router"**: redirection to the specified UIAbility of the widget provider.

\- **"message"**: custom message. If this type of action is triggered, the [onFormEvent()](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md#formextensionabilityonformevent) lifecycle callback of the provider FormExtensionAbility is called.

\- **"call"**: launch of the widget provider in the background. If this type of action is triggered, the specified UIAbility (whose launch type must be [singleton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type#singleton)) of the widget provider is started in the background, but not displayed in the foreground. This action type requires that the widget provider should have the [ohos.permission.KEEP\_BACKGROUND\_RUNNING](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all#ohospermissionkeep_background_running) permission.

**NOTE**

Whenever possible, avoid using the router event to refresh the widget UI.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| moduleName | string | No | Yes | 

Name of the target module when action is **"router"** or **"call"**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| bundleName | string | No | Yes | 

Name of the target bundle when action is **"router"** or **"call"**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| abilityName | string | No | Yes | 

Name of the target UIAbility when action is **"router"** or **"call"**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| uri11+ | string | No | Yes | 

URI of the target UIAbility when action is **"router"**. If both **uri** and **abilityName** are set, **abilityName** takes precedence.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

 |
| params | Object | No | Yes | 

Additional parameters carried in the current action. The value is a key-value pair in JSON format. For the **"call"** action type, the **method** parameter must be set and its value type must be string.

**NOTE**

Whenever possible, avoid using **params** to transfer internal state variables of widgets.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

@Entry
@Component
struct FormLinkDemo {
  build() {
    Column() {
      Text("This is a static widget").fontSize(20).margin(10)

      // The router event is used to redirect to the specified UIAbility from the static widget.
      FormLink({
        action: "router",
        abilityName: "EntryAbility",
        params: {
          'message': 'testForRouter' // Customize the message to send.
        }
      }) {
        Button("router event").width(120)
      }.margin(10)

      // The message event triggers the onFormEvent callback of FormExtensionAbility.
      FormLink({
        action: "message",
        abilityName: "EntryAbility",
        params: {
          'message': 'messageEvent' // Customize the message to send.
        }
      }) {
        Button("message event").width(120)
      }.margin(10)

      // The call event is used to call the specified method in the UIAbility.
      FormLink({
        action: "call",
        abilityName: "EntryAbility",
        params: {
          'method': 'funA', // Set the name of the method to call in the EntryAbility.
          'num': 1 // Set other parameters to be passed in.
        }
      }) {
        Button("call event").width(120)
      }.margin(10)

      // The router event is used to redirect to the specified UIAbility from the static widget through deep linking.
      FormLink({
        action: "router",
        uri: 'example://uri.ohos.com/link\_page',
        params: {
          message:'router msg for static uri deeplink' // Customize the message to send.
        }
      }) {
        Button("deeplink event").width(120)
      }.margin(10)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5UWuErEmTKKUBPCg2H0gLA/en-us_image_0000002537765940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C3986043975C434B155DA28B45F834A308DF00DFEBA562626326AA0F58F26D4)

The following is an example of **uris** configuration in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#skills) file of the target application:

"abilities": \[
  {
    "skills": \[
      {
        "uris": \[
          {
            "scheme": "example",
            "host": "uri.ohos.com",
            "path": "link\_page"
          },
        \]
      }
    \],
  }
\]
