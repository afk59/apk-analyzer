# EmbeddedComponent

The **EmbeddedComponent** is a component used to embed into the current page the UI provided by another [EmbeddedUIExtensionAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-embeddeduiextensionability-extensionability-for-cross-process-u/document.md) in the same application. The EmbeddedUIExtensionAbility runs in an independent process for UI layout and rendering.

It is usually used in modular development scenarios where process isolation is required.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/AfQWDkmST1Gn3JTlbH5JXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F12F997F30303E867F34B8B6DF48047D3124D2721A90E78376569A120BE53E2)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Constraints

The **EmbeddedComponent** is supported only on devices configured with multi-process permissions.

The **EmbeddedComponent** can be used only in the UIAbility, and the EmbeddedUIExtensionAbility to start must belong to the same application as the UIAbility.

#### Child Components

Not supported

#### APIs

EmbeddedComponent(loader: Want, type: EmbeddedType)

Creates a cross-process embedded component to display the UI of the EmbeddedUIExtensionAbility with the same bundle name.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| loader | [Want](../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | EmbeddedUIExtensionAbility to load. |
| type | [EmbeddedType](../../common-definitions/enums/document.md#embeddedtype12) | Yes | Type of the provider. |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/74Uski2UQvm3-Hj94Qu2Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CAF697CB358BC69A5EE835B9DF8831C71E4702BDDB2B8996068E3678D114D2A)

The default and minimum width and height of the **EmbeddedComponent** are both 10 vp. The following width- and height-related attributes are not supported: **constraintSize**, **aspectRatio**, **layoutWeight**, **flexBasis**, **flexGrow**, and **flexShrink**.

#### Events

Event information related to screen coordinates is converted based on the position, width, and height of the **EmbeddedComponent**, before being transferred to the EmbeddedUIExtensionAbility for processing.

Universal events, such as the [click event](../../universal-events/interaction-response-events/click-event/document.md), are not supported. Only the following events are supported.

#### \[h2\]onTerminated

onTerminated(callback: Callback<TerminationInfo>)

Triggered when the the launched EmbeddedUIExtensionAbility exits normally by calling [terminateSelfWithResult](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#terminateselfwithresult) or [terminateSelf](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md#terminateself).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6NxQMUQCTbW3oeHYvCpskQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E13B59B120DDBD13FE6B2E99912147BACBB0232ED4A4F0DBF4CB8FE9CBC7F87)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[TerminationInfo](#terminationinfo)\> | Yes | Callback used to return the result from the EmbeddedUIExtensionAbility. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/BMuwnpvsRFWEFwsMtTlFDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B551A71E4191E4FBA349EB49EA5FF928C14D066EECE1835E1ABCDAC0BD827FB)

-   If the EmbeddedUIExtensionAbility is terminated by calling **terminateSelfWithResult**, the carried information is passed as arguments into the callback function.
-   If the EmbeddedUIExtensionAbility is terminated by calling **terminateSelf**, the input parameters **code** and **want** in the callback function are at their default values: **0** and **undefined**, respectively.

#### \[h2\]onError

onError(callback: ErrorCallback)

Called when an error occurs during the running of the started EmbeddedUIExtensionAbility. Through the **code**, **name**, and **message** in the callback parameters, error information can be obtained and handled. For details about the error codes, see [UIExtension Error Codes](../../../error-codes/ui/uiextension-error-codes/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/SHCIg9s8TYKA1kmmH98nPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D599D829D00BC04A643BEB85E89E6D073C203B2FD39CD71AE0F37B24FDB1F80)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback used to return the error information of the [BusinessError](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) type. The error information can be obtained and processed based on the **code**, **name**, and **message** parameters. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/WogzkDjjT-GiAFkenRn00A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7EB9B1CEC7642C8A3F90D489E8BF2F0E168FE5842FBD6D0214AC713AAE325B6)

This callback is called to notify the provider of the following:

-   The EmbeddedUIExtensionAbility fails to be started.
-   The EmbeddedUIExtensionAbility fails to be switched to the background.
-   The EmbeddedUIExtensionAbility fails to be destroyed.
-   The EmbeddedUIExtensionAbility exits abnormally.
-   An **EmbeddedComponent** is nested in the EmbeddedUIExtensionAbility.

#### TerminationInfo

Provides the result returned by the started **EmbeddedUIExtensionAbility**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Result code returned when the EmbeddedUIExtensionAbility exits. The result code is determined by the data passed when terminateSelfWithResult or terminateSelf is called. |
| want | [Want](../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | No | Yes | Data returned when the EmbeddedUIExtensionAbility exits. |

#### Example: Loading an EmbeddedComponent Component

This example shows the basic usage of the **EmbeddedComponent** and EmbeddedUIExtensionAbility. The bundle name of the sample application is **com.example.embeddeddemo**, and the started EmbeddedUIExtensionAbility in the same application is ExampleEmbeddedAbility. This example only supports devices with multi-process permissions, such as 2-in-1 devices.

-   The EntryAbility (UIAbility) of the sample application loads the **ets/pages/Index.ets** file, whose content is as follows:
    
    import { Want } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Message: ';
      private want: Want = {
        bundleName: "com.example.embeddedComponent",
        abilityName: "ExampleEmbeddedAbility",
      };
    
      build() {
        Row() {
          Column() {
            Text(this.message).fontSize(30)
            EmbeddedComponent(this.want, EmbeddedType.EMBEDDED\_UI\_EXTENSION)
              .width('100%')
              .height('90%')
              .onTerminated((info) => {
                // Triggered when the terminateSelfWithResult button is clicked in the extension page.
                this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
              })
              .onError((error) => {
                // Triggered on failure or exception.
                this.message = 'Error: code = ' + error.code;
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   The EmbeddedUIExtensionAbility (**ExampleEmbeddedAbility**) to start by the **EmbeddedComponent** is implemented in the **ets/extensionAbility/ExampleEmbeddedAbility.ets** file. The file content is as follows:
    
    import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
    
    const TAG: string = '\[ExampleEmbeddedAbility\]';
    
    export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
      onCreate() {
        console.info(TAG, \`onCreate\`);
      }
    
      onForeground() {
        console.info(TAG, \`onForeground\`);
      }
    
      onBackground() {
        console.info(TAG, \`onBackground\`);
      }
    
      onDestroy() {
        console.info(TAG, \`onDestroy\`);
      }
    
      onSessionCreate(want: Want, session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionCreate, want: ${JSON.stringify(want)}\`);
        let param: Record<string, UIExtensionContentSession> = {
          'session': session
        };
        let storage: LocalStorage = new LocalStorage(param);
        // Load the pages/extension.ets content.
        session.loadContent('pages/extension', storage);
      }
    
      onSessionDestroy(session: UIExtensionContentSession) {
        console.info(TAG, \`onSessionDestroy\`);
      }
    }
    
-   The entry page file **ets/pages/extension.ets** for **ExampleEmbeddedAbility** (EmbeddedUIExtensionAbility) is as follows. The path to this page must also be configured in the **resources/base/profile/main\_pages.json** file.
    
    import { UIExtensionContentSession } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Extension {
      @State message: string = 'EmbeddedUIExtensionAbility Index';
      private storage: LocalStorage | undefined = this.getUIContext()?.getSharedLocalStorage();
      private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');
    
      build() {
        Column() {
          Text(this.message)
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
          Button("terminateSelfWithResult").fontSize(20).onClick(() => {
            // Call terminateSelfWithResult to exit when the button is clicked.
            this.session?.terminateSelfWithResult({
              resultCode: 1,
              want: {
                bundleName: "com.example.embeddedComponent",
                abilityName: "ExampleEmbeddedAbility",
              }
            });
          })
        }.width('100%').height('100%')
      }
    }
    
-   Add the configuration for **ExampleEmbeddedAbility** under the **extensionAbilities** tag in the **module.json5** file. The type is set to **embeddedUI**, as shown below:
    
    {
      "name": "ExampleEmbeddedAbility",
      "srcEntry": "./ets/extensionAbility/ExampleEmbeddedAbility.ets",
      "type": "embeddedUI"
    }
    
-   The file directory structure is as follows:
    
    .
    └── main
        ├── ets
        │   ├── extensionAbility
        │   │   └── ExampleEmbeddedAbility.ets
        │   └── pages
        |       ├── extension.ets
        │       └── Index.ets
        ├── resources
        |   └── base
        |       └── profile
        |           └── main\_pages.json
        └── module.json5
    
-   The following is an example:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Jd6Mz48bSfmzQb7ixwoQig/en-us_image_0000002537925832.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062246Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCC5D002552D67424025A0E2DBAF312F2801E91E92819CDCEBDB0044A4832BD5)
