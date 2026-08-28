# Pushing a Widget Update Message

#### Use Cases

Our smartphones have become all-in-one devices for everything from shopping to streaming. However, the constant need to open and close apps for simple tasks can be a frustrating user experience. To solve this problem, HarmonyOS provides [Form Kit](../../../../application-framework/form-kit/document.md) for you to develop widgets that can display important information or operations specific to an app, so that users can directly access a desired app service, without the need to open the app first.

Push Kit helps make user experience even better by allowing you to update your widget content in real time. By integrating Push Kit and obtaining a push token, your app can push updated widget content via the system-level channel provided by Push Kit at the right moment to engage users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/s0-GTHXRQWmWY8Ckmw5yPQ/en-us_image_0000002368705872.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=063673A5FEC71983C1D986955D81C3F1485A041BF0F6F06A81D8F0EE9327EE44 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/MY4w8LKNQtK2oJx-LdIIzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6300D58898609BD4BC80C4BF5552F038EC0A18A272C89BE538755861A05AA36)

The function of widget update messages supports phones, tablets, PCs, and 2-in-1 devices.

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

The frequency control policy of a single service widget varies depending on whether the corresponding app has been released:

-   Released app: For a single widget of an app, up to two messages can be pushed per device per day.
-   Unreleased app: For a single widget of an app, up to five messages can be pushed per device per day.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/_Wt8Ba3_TWmRSCwsIwywhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A723A2C9D30F2B621DD7105141F3C8B9270C53FD802CF22D21EE88F4661F749D)

Regardless of whether it's a test message or a formal message, a widget update message can carry only one push token per push.

#### Development Procedure

## Developing a Widget

Before pushing widget update messages, you need to complete widget development locally.

1.  Create a service widget by referring to [Creating an ArkTS Widget](../../../../application-framework/form-kit/arkts-widget-development-recommended/creating-an-arkts-widget/document.md).
2.  Set the **dataProxyEnabled** field to **true** in **src/main/resources/base/profile/form\_config.json** at the module level to enable the proxy-based widget update function.
    
    {
      "forms": \[
        {
          "name": "widget",
          "src": "./ets/widget/pages/WidgetCard.ets",
          "uiSyntax": "arkts",
          "window": {
            "designWidth": 720,
            "autoDesignWidth": true
          },
          "colorMode": "auto",
          "isDefault": true,
          "updateEnabled": true,
          "updateDuration": 1,
          "scheduledUpdateTime": "10:30",
          "defaultDimension": "2\*2",
          "supportDimensions": \["2\*2"\],
          **"dataProxyEnabled": true**
        }
      \]
    }
    
3.  Obtain **formId** in the [onAddForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonaddform)() method of the widget lifecycle management file (for example, **EntryFormAbility**) and define the fields to be updated by Push Kit in the widget page file (for example, **WidgetCard**). The following code uses fields **text\_key** and **image\_key** as examples:
    
    import { formBindingData, formInfo, FormExtensionAbility } from '@kit.FormKit';
    import { Want } from '@kit.AbilityKit';
    
    export default class EntryFormAbility extends FormExtensionAbility {
      onAddForm(want: Want): formBindingData.FormBindingData {
        // Obtain formId.
        const formId = want.parameters!\[formInfo.FormParam.IDENTITY\_KEY\] as string;
    
        // Define the fields to be updated in WidgetCard.
        class CreateFormData {
          formId: string = '';
          text\_key: string = '';
          image\_key: string = '';
        }
    
        const obj: CreateFormData = {
          formId: formId,
          text\_key: 'Default text',
          image\_key: ''
        }
        const bindingData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
    
        // Define fields that need to be updated by Push Kit. The key of each field must be defined in **bindingData**.
        const text\_key: formBindingData.ProxyData = {
          key: 'text\_key',
          subscriberId: formId
        };
        const image\_key: formBindingData.ProxyData = {
          key: 'image\_key',
          subscriberId: formId
        };
        bindingData.proxies = \[text\_key, image\_key\];
        return bindingData;
      }
    }
    
4.  Create the **[LocalStorage](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/localstorage-storing-page-level-ui-state/document.md)** variable in the widget page file (for example, **src/main/ets/widget/pages/WidgetCard.ets**) and bind them to the **[@Entry](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/custom-components/creating-a-custom-component/document.md#entry)** decorator. Use the **[@LocalStorageProp](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/localstorage-storing-page-level-ui-state/document.md#localstorageprop)** decorator to create key-value pairs for the variables.
    
    In this section, three variables, **formId**, **text**, and **image** are created, corresponding to keys **formId**, **text\_key**, and **image\_key** respectively. Note that **image** in the widget page layout indicates the Image component. Any variable transferred by the Image component must start with **memory://**.
    
    // Define **LocalStorage** that stores the page-level UI state.
    const storage = new LocalStorage();
    
    // Bind.
    @Entry(storage)
    @Component
    struct WidgetCard {
      @LocalStorageProp('formId') formId: string = '';
      @LocalStorageProp('text\_key') text: string = '';
      @LocalStorageProp('image\_key') image: string = '';
    
      build() {
        Flex({ direction: FlexDirection.Column }) {
          Row() {
            Text() {
              // Span is a subcomponent of the Text component and is used to display the inline text.
              Span('formID:')
              Span(this.formId)
            }
            .fontSize(10)
          }
    
          Row() {
            Text() {
              Span('Text:')
              Span(this.text)
            }
            .fontSize(10)
          }
    
          Row() {
            if (this.image) {
              Image('memory://' + this.image).height(80)
            }
          }
        }
        .padding(10)
        .onClick(() => {
          postCardAction(this, {
            action: 'router',
            abilityName: 'MainAbility', // Set this parameter to the actual ability name of the app.
          });
        })
      }
    }
    

## Pushing a Widget Update Message

1.  [Obtain a push token](../../preparations/obtaining-a-push-token/document.md).
2.  (Optional) Report information such as **formId** and **pushToken** to your app server to send widget update messages to your users.
    
    // The pseudo-code is as follows:
    import { Want } from '@kit.AbilityKit';
    import { pushService } from '@kit.PushKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { formInfo } from '@kit.FormKit';
    
    async function saveFormInfo(want: Want): Promise<void> {
      try {
        const formId = want.parameters!\[formInfo.FormParam.IDENTITY\_KEY\] as string;
        const moduleName = want.moduleName;
        const abilityName = want.abilityName;
        const formName = want.parameters!\[formInfo.FormParam.NAME\_KEY\] as string;
        const pushToken: string = await pushService.getToken();
    
        // Report **formId**, **moduleName**, **abilityName**, **formName**, and **pushToken** to the app server.
      } catch (err) {
        let e: BusinessError = err as BusinessError;
        hilog.error(0x0000, 'testTag', 'Failed to save form info: %{public}d %{public}s', e.code, e.message);
      }
    }
    
3.  Call the REST API provided by Push Kit from your app server to push a widget update message. For details, please refer to [Scenario-Specific Message API Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-intro). The following is a request example:
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* 
    **push-type: 1**
    
    // Request Body
    {
        "payload": {
        "moduleName": "entry",
        "abilityName": "EntryFormAbility",
        "formName": "widget",
        "formId": 423434262,
        "version": 123456,
        "formData": {
          "text\_key": "Text to be updated"
        },
        "images": \[
          {
            "keyName": "image\_key",
            "url": "https://\*\*\*.png"**,**
            "require": 1
          }
        \]
      },
      "target": {
        "token": \[
          "MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"
        \]
      },
      "pushOptions": {
         "testMessage": true
      }
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
    -   **push-type**: The value **1** indicates the service widget update message type.
    -   **moduleName**: value of **name** under the **module** section in **src/main/module.json5** at the module level.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/qKNz5WUMR9OEAzWS-EzBoQ/en-us_image_0000002402225577.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F799953C7D0CB3BF25C76AC052AFF27E9E9388391A97773ED657FDDE9F3BF174 "Click to enlarge")
        
    -   **abilityName**: ability name of the service widget under the **extensionAbilities** section in **src/main/module.json5** at the module level.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/GdRHanECSTexVv3qg4198g/en-us_image_0000002402305721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D4F309A67C8924AB9273B6846A5FE83036A40EECB87B1D6BBCBCC1510841DEF "Click to enlarge")
        
    -   **formName**: name of the service widget under the **forms** section in **src/main/resources/base/profile/form\_config.json** at the module level. The following figure uses the **form\_config** configuration file as an example.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/dXl9fgQxTyuTlgO91NwgZA/en-us_image_0000002368545980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC46A73C3386C63F905B4EB4011DB4A0228F28CC543D4865ABB51D37B1F65B05 "Click to enlarge")
        
    -   **version**: version number of the current widget update message. A new refresh message must have a **higher** version number to be successfully applied. For details, please refer to [version](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section6471174713249).
    -   **formId**: instance ID of a service widget, which is obtained when [onAddForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonaddform)() is called (a user adds the widget to the home screen). The maximum value is **2^31-1**.
    -   **formData**: service data of the service widget to be updated. The data comes from the declarative paradigm component name in **src/main/ets/widget/pages/WidgetCard.ets** at the module level. The following figure uses the widget page file **WidgetCard** as an example.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/oXdgLhXCQ2qgL-CL5BJC5w/en-us_image_0000002368705868.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D1E68CBB0C3CC70A7E050E78311F39E4B95A90518E3099132D8F29E67498E30 "Click to enlarge")
        
    -   **images**: image data in the service data of the service widget to be updated. **keyName** indicates the key value of the image control in the widget, and **url** indicates the image URL. The following figure uses the widget page file **WidgetCard** as an example.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/XkhcNwNCSY63sCGlPZo9rA/en-us_image_0000002402225573.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AD319BBECD0086A02C3A7C2FCEB746F852305CC409711DA874194DB389A158A "Click to enlarge")
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/NSWm_4lWTrKcFqIHphb3xw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=823AFF6A7823C0F83382635A1961EE069C94112B88C5DA696530D920AA6EF43C)
        
        Do not push images that contain sensitive content.
        
        The supported image formats are PNG, JPG, and JPEG. The image size cannot exceed 512 KB. The image width x height must be less than 12,800 pixels.
        
    -   **require**: image update control policy. **0** indicates to update only the text if the image fails to be downloaded. **1** indicates not to update the widget if the image fails to be downloaded.
    -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
    -   **testMessage** (optional): indicates whether a message is a test message. The value **true** indicates a test message. In each project, a maximum of 1000 test messages can be sent every day. Each push can carry only one token. For details, please refer to [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
