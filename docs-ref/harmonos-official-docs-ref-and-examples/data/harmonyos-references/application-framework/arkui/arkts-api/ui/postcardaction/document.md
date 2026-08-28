# postCardAction

Provides information for interaction between the widget and widget provider. Currently, router, message, and call events are supported. This API can only be called within the widget.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/LJsXzCzkRbaMwbH7rDeiAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1913E1BF181E3DB76BBB2C59E19B9F45F747CE801994F30D12CF92F02AAC00DF)

This API is supported since API version 9.

#### postCardAction

postCardAction(component: Object, action: Object): void

Performs internal interactions within a function and processes operations related to the **component** and **action** objects. This API does not return any value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Model constraint**: This API can be used only in the stage model.

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| component | Object | Yes | Instance of the current custom component. Generally, **this** is passed in. |
| action | Object | Yes | Action description. For details, see the following table. |

**Description of the action parameter**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| action | string | Yes | 
Action type.

\- **"router"**: redirection to the specified UIAbility of the widget provider. This type of action can be triggered only in a click event.

\- **"message"**: custom message. If this type of action is triggered, the [onFormEvent()](../../../../form-kit/arkts-apis/ohos-app-form-formextensionability-formextensionability/document.md#formextensionabilityonformevent) lifecycle callback of the provider **FormExtensionAbility** is called.

\- **"call"**: launch of the widget provider in the background. If this type of action is triggered, the specified **UIAbility** (whose [launch type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-launch-type) must be singleton) of the widget provider is started in the background, but not displayed in the foreground. This action type requires that the widget provider have the [ohos.permission.KEEP\_BACKGROUND\_RUNNING](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all#ohospermissionkeep_background_running) permission.

 |
| bundleName | string | No | Name of the target bundle when **action** is **"router"** or **"call"**. |
| moduleName | string | No | Name of the target module when **action** is **"router"** or **"call"**. |
| abilityName | string | No | Name of the target **UIAbility** when **action** is **"router"** or **"call"**. |
| uri11+ | string | No | URI of the target **UIAbility** when action is **"router"**. If both **uri** and **abilityName** are set, **abilityName** takes precedence. |
| params | Object | No | Additional parameters carried in the current action. The value is a key-value pair in JSON format. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/wY0YSxnWRQ6FpeKwwwMv-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AE8182467CE99CF48A498145EDE1B02C0FAA279682F793F306C8AED3DDF10DD)

When **action** is **"call"**, a string value of **'method'** must be passed to **params** to trigger the corresponding method in the **UIAbility**.

**Example**

Button('Redirect')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        message: 'testForRouter' // Customize the message to send.
      }
    });
  })

Button('Start in Background')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'call',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        method: 'fun', // Set the name of the method to call. It is mandatory.
        message: 'testForCall' // Customize the message to send.
      }
    });
  })

Button('Redirect URI')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      uri: 'example://uri.ohos.com/link\_page',
      params: {
        message: 'router msg for dynamic uri deeplink' // Customize the message to send.
      }
    });
  })

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
          }
        \]
      }
    \]
  }
\]
