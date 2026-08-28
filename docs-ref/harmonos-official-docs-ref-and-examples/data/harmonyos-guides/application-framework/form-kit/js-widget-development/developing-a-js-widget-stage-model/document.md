# Developing a JS Widget (Stage Model)

The stage model is supported since API version 9. It is the mainstream model with a long evolution plan. This model is object-oriented and provides open application components as classes. You can derive application components for capability expansion.

#### Available APIs

The **FormExtensionAbility** class has the following APIs. For details, see [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability).

| Name | Description |
| :-- | :-- |
| onAddForm(want: Want): formBindingData.FormBindingData | Called to notify the widget provider that a widget is being created. |
| onCastToNormalForm(formId: string): void | Called to notify the widget provider that a temporary widget is being converted to a normal one. |
| onUpdateForm(formId: string, wantParams?: Record<string, Object>): void | Called to notify the widget provider that a widget is being updated. |
| onChangeFormVisibility(newStatus: Record<string, number>): void | Called to notify the widget provider that the widget visibility status is being changed. |
| onFormEvent(formId: string, message: string): void | Called to instruct the widget provider to process a widget event. |
| onRemoveForm(formId: string): void | Called to notify the widget provider that a widget is being destroyed. |
| onConfigurationUpdate(newConfig: Configuration): void | Called when the configuration of the environment where the widget is running is being updated. |

The following table lists some APIs provided by the **formProvider** class. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formprovider).

| Name | Description |
| :-- | :-- |
| setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void | Sets the next refresh time for a widget. This API uses an asynchronous callback to return the result. |
| setFormNextRefreshTime(formId: string, minute: number): Promise<void> | Sets the next refresh time for a widget. This API uses a promise to return the result. |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData, callback: AsyncCallback<void>): void | Updates a widget. This API uses an asynchronous callback to return the result. |
| updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void> | Updates a widget. This API uses a promise to return the result. |

The following table lists some APIs provided by the **formBindingData** class. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formbindingdata).

| Name | Description |
| :-- | :-- |
| createFormBindingData(obj?: Object | string): FormBindingData | Creates a **FormBindingData** object. |

#### How to Develop

The widget provider development based on the [stage model](../../../ability-kit/stage-model-development/stage-model-development-overview/document.md) involves the following key steps:

-   [Creating a FormExtensionAbility Instance](#creating-a-formextensionability-instance): Develop the lifecycle callback functions of FormExtensionAbility.
    
-   [Configuring the Widget Configuration Files](#configuring-the-widget-configuration-files): Configure the application configuration file **module.json5** and profile configuration file.
    
-   [Persistently Storing Widget Data](#persistently-storing-widget-data): Manage widget data persistence.
    
-   [Updating Widget Data](#updating-widget-data): Call **updateForm()** to update the information displayed in a widget.
    
-   [Developing the Widget UI Page](#developing-the-widget-ui-page): Use HML+CSS+JSON to develop a JS widget UI page.
    
-   [Developing Widget Events](#developing-widget-events): Add the router and message events for a widget.
    

## Creating a FormExtensionAbility Instance

To create a widget in the stage model, you need to implement the lifecycle callbacks of FormExtensionAbility. Before that, generate a widget template by referring to [Developing a Service Widget](../../../../environment-setup/creating-a-project/managing-modules/creating-a-service-widget/document.md).

1.  Import related modules in **JsCardFormAbility.ets**.
    
    // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
    import { common, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { preferences } from '@kit.ArkData';
    
2.  Implement FormExtension lifecycle callbacks in **JsCardFormAbility.ets**.
    
    // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
    const TAG: string = 'JsCardFormAbility';
    const DATA\_STORAGE\_PATH: string = '/data/storage/el2/base/haps/form\_store';
    const DOMAIN\_NUMBER: number = 0xFF00;
    let storeFormInfo =
      async (formId: string, formName: string, tempFlag: boolean, context: common.FormExtensionContext): Promise<void> => {
        // Only the widget ID (formId), widget name (formName), and whether the widget is a temporary one (tempFlag) are persistently stored.
        let formInfo: Record<string, string | boolean | number> = {
          'formName': formName,
          'tempFlag': tempFlag,
          'updateCount': 0
        };
        try {
          const storage: preferences.Preferences = await preferences.getPreferences(context, DATA\_STORAGE\_PATH);
          // put form info
          await storage.put(formId, JSON.stringify(formInfo));
          hilog.info(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] storeFormInfo, put form info successfully, formId: ${formId}\`);
          await storage.flush();
        } catch (err) {
          hilog.error(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] failed to storeFormInfo,
          err: ${JSON.stringify(err as BusinessError)}\`);
        }
      }
    let deleteFormInfo = async (formId: string, context: common.FormExtensionContext): Promise<void> => {
      try {
        const storage: preferences.Preferences = await preferences.getPreferences(context, DATA\_STORAGE\_PATH);
        // Delete the widget information.
        await storage.delete(formId);
        hilog.info(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] deleteFormInfo, del form info successfully, formId: ${formId}\`);
        await storage.flush();
      } catch (err) {
        hilog.error(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] failed to deleteFormInfo,
          err: ${JSON.stringify(err as BusinessError)}\`);
      }
    };
    
    
    export default class JsCardFormAbility extends FormExtensionAbility {
      onAddForm(want: Want): formBindingData.FormBindingData {
        hilog.info(DOMAIN\_NUMBER, TAG, '\[JsCardFormAbility\] onAddForm');
    
        if (want.parameters) {
          let formId = JSON.stringify(want.parameters\['ohos.extra.param.key.form\_identity'\]);
          let formName = JSON.stringify(want.parameters\['ohos.extra.param.key.form\_name'\]);
          let tempFlag = want.parameters\['ohos.extra.param.key.form\_temporary'\] as boolean;
          // Persistently store widget data for subsequent use, such as instance acquisition and update.
          storeFormInfo(formId, formName, tempFlag, this.context);
        }
    
        let obj: Record<string, string> = {
          'title': 'titleOnCreate',
          'detail': 'detailOnCreate'
        };
        let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
        return formData;
      }
    
      onRemoveForm(formId: string): void {
        // Delete widget data.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onRemoveForm');
        // Delete the persistent widget instance data.
        deleteFormInfo(formId, this.context);
      }
    
      onUpdateForm(formId: string): void {
        // Override this method to support interval-based updates, time-specific updates, or updates requested by the widget host.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onUpdateForm');
        let obj: Record<string, string> = {
          'title': 'titleOnUpdate',
          'detail': 'detailOnUpdate'
        };
        let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
        formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
          hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] updateForm, error:' + JSON.stringify(error));
        });
      }
    
      onFormEvent(formId: string, message: string): void {
        // If the widget supports event triggering, override this method and implement the trigger.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onFormEvent');
        // Obtain the detail parameter passed in the message event.
        let msg: Record<string, string> = JSON.parse(message);
        if (msg.detail === 'message detail') {
          // Implement the service logic.
          hilog.info(DOMAIN\_NUMBER, TAG, 'message info:' + msg.detail);
        }
      }
    
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/X_fKjW-kSaSDJxN1wmFLNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FFA8789092335978A30A27B9E070CA978FE412BA33FFCE1DAF7BB86C06D7A77)

FormExtensionAbility cannot reside in the background. Therefore, continuous tasks cannot be processed in the widget lifecycle callbacks.

## Configuring the Widget Configuration Files

1.  Configure ExtensionAbility information under **extensionAbilities** in the [module.json5 file](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md). For a FormExtensionAbility, you must specify **metadata**. Specifically, set **name** to **ohos.extension.form** (fixed), and set **resource** to the index of the widget configuration information.
    
    Example configuration:
    
    {
      "module": {
        // ...
        "extensionAbilities": \[
          {
            "name": "JsCardFormAbility",
            "srcEntry": "./ets/jscardformability/JsCardFormAbility.ets",
            "description": "$string:JSCardFormAbility\_desc",
            "label": "$string:JSCardFormAbility\_label",
            "type": "form",
            "metadata": \[
              {
                "name": "ohos.extension.form",
                "resource": "$profile:form\_jscard\_config"
              }
            \]
          }
        \]
      }
    }
    
2.  Configure the widget configuration information. In the **metadata** configuration item of FormExtensionAbility, you can specify the resource index of specific configuration information of the widget. For example, if **resource** is set to **$profile:form\_jscard\_config**, **form\_jscard\_config.json** in the **resources/base/profile/** directory of the development view is used as the profile configuration file of the widget. The following table describes the internal structure of the profile configuration file.
    
    **Table 1** Widget profile configuration file
    
    | Field | Description | Data Type | Default Value Allowed |
    | :-- | :-- | :-- | :-- |
    | name | Class name of the widget. The value is a string with a maximum of 127 bytes. | String | No |
    | description | Description of the widget. The value can be a string or a resource index to descriptions in multiple languages. The value is a string with a maximum of 255 bytes. | String | Yes (initial value: left empty) |
    | src | Full path of the UI code corresponding to the widget. | String | No |
    | window | Window-related configurations. | Object | Yes |
    | isDefault | 
    Whether the widget is a default one. Each UIAbility has only one default widget.
    
    \- **true**: The widget is the default one.
    
    \- **false**: The widget is not the default one.
    
     | Boolean | No |
    | colorMode(deprecated) | 
    
    Color mode of the widget.
    
    \- **auto**: following the system color mode
    
    \- **dark**: dark color mode
    
    \- **light**: light color mode
    
    **Note:**
    
    1\. This configuration item is supported since API version 12 and deprecated since API version 20. The color mode follows the system color mode.
    
     | String | Yes (initial value: **auto**) |
    | supportDimensions | 
    
    Supported widget dimensions. The options are as follows:
    
    \- **1 \* 2**: indicates a grid with one row and two columns.
    
    \- **2 \* 2**: indicates a grid with two rows and two columns.
    
    \- **2 \* 4**: indicates a grid with two rows and four columns.
    
    \- **2 \* 3**: indicates a grid with two rows and three columns.
    
    \- **3 \* 3**: indicates a grid with three rows and three columns.
    
    \- **4 \* 4**: indicates a grid with four rows and four columns.
    
    \- **6 \* 4**: indicates a grid with six rows and four columns.
    
    **Note**: **2 \* 3** and **3 \* 3** support only watches.
    
     | String array | No |
    | defaultDimension | Default grid style of the widget. The value must be available in the **supportDimensions** array of the widget. | String | No |
    | updateEnabled | 
    
    Whether the widget can be updated periodically.
    
    \- **true**: The widget can be updated at a specified interval (**updateDuration**) or at the scheduled time (**scheduledUpdateTime**). **updateDuration** takes precedence over **scheduledUpdateTime**.
    
    \- **false**: The widget cannot be updated periodically.
    
     | Boolean | No |
    | scheduledUpdateTime | 
    
    Scheduled time to update the widget. The value is in 24-hour format and accurate to minute.
    
    **updateDuration** takes precedence over **scheduledUpdateTime**. If both are specified, the value specified by **updateDuration** is used.
    
     | String | Yes (initial value: **0:0**) |
    | updateDuration | 
    
    Interval to update the widget. The value is a natural number, in the unit of 30 minutes.
    
    If the value is **0**, this field does not take effect.
    
    If the value is a positive integer N, the interval is calculated by multiplying N and 30 minutes.
    
    **updateDuration** takes precedence over **scheduledUpdateTime**. If both are specified, the value specified by **updateDuration** is used.
    
     | Number | Yes (initial value: **0**) |
    | formConfigAbility | Link to a specific page of the application. The value is a URI. | String | Yes (initial value: left empty) |
    | formVisibleNotify | Whether the widget is allowed to use the widget visibility notification. | String | Yes (initial value: left empty) |
    | metaData | Metadata of the widget. This field contains the array of the **customizeData** field. | Object | Yes (initial value: left empty) |
    
    Example configuration:
    
    {
      "forms": \[
        {
          "name": "WidgetJS",
          "description": "$string:JSCardEntryAbility\_desc",
          "src": "./js/WidgetJS/pages/index/index",
          "window": {
            "designWidth": 720,
            "autoDesignWidth": true
          },
          "isDefault": true,
          "updateEnabled": true,
          "scheduledUpdateTime": "10:30",
          "updateDuration": 1,
          "defaultDimension": "2\*2",
          "supportDimensions": \[
            "2\*2"
          \]
        }
      \]
    }
    

## Persistently Storing Widget Data

A widget provider is usually started when it is needed to provide information about a widget. The Widget Manager supports multi-instance management and uses the widget ID to identify an instance. If the widget provider supports widget data modification, it must persistently store the data based on the widget ID, so that it can access the data of the target widget when obtaining, updating, or starting a widget.

For details about how to import the code, see [Creating a FormExtensionAbility Instance](#creating-a-formextensionability-instance).

// entry/src/main/ets/jscardformability/JsCardFormAbility.ets
const TAG: string = 'JsCardFormAbility';
const DATA\_STORAGE\_PATH: string = '/data/storage/el2/base/haps/form\_store';
const DOMAIN\_NUMBER: number = 0xFF00;
let storeFormInfo =
  async (formId: string, formName: string, tempFlag: boolean, context: common.FormExtensionContext): Promise<void> => {
    // Only the widget ID (formId), widget name (formName), and whether the widget is a temporary one (tempFlag) are persistently stored.
    let formInfo: Record<string, string | boolean | number> = {
      'formName': formName,
      'tempFlag': tempFlag,
      'updateCount': 0
    };
    try {
      const storage: preferences.Preferences = await preferences.getPreferences(context, DATA\_STORAGE\_PATH);
      // put form info
      await storage.put(formId, JSON.stringify(formInfo));
      hilog.info(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] storeFormInfo, put form info successfully, formId: ${formId}\`);
      await storage.flush();
    } catch (err) {
      hilog.error(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] failed to storeFormInfo,
      err: ${JSON.stringify(err as BusinessError)}\`);
    }
  }
// ···

export default class JsCardFormAbility extends FormExtensionAbility {
  onAddForm(want: Want): formBindingData.FormBindingData {
    hilog.info(DOMAIN\_NUMBER, TAG, '\[JsCardFormAbility\] onAddForm');

    if (want.parameters) {
      let formId = JSON.stringify(want.parameters\['ohos.extra.param.key.form\_identity'\]);
      let formName = JSON.stringify(want.parameters\['ohos.extra.param.key.form\_name'\]);
      let tempFlag = want.parameters\['ohos.extra.param.key.form\_temporary'\] as boolean;
      // Persistently store widget data for subsequent use, such as instance acquisition and update.
      storeFormInfo(formId, formName, tempFlag, this.context);
    }

    let obj: Record<string, string> = {
      'title': 'titleOnCreate',
      'detail': 'detailOnCreate'
    };
    let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
    return formData;
  }
// ···
}

You should override **onRemoveForm** to implement widget data deletion.

// entry/src/main/ets/jscardformability/JsCardFormAbility.ets
const TAG: string = 'JsCardFormAbility';
const DATA\_STORAGE\_PATH: string = '/data/storage/el2/base/haps/form\_store';
const DOMAIN\_NUMBER: number = 0xFF00;
// ···
let deleteFormInfo = async (formId: string, context: common.FormExtensionContext): Promise<void> => {
  try {
    const storage: preferences.Preferences = await preferences.getPreferences(context, DATA\_STORAGE\_PATH);
    // Delete the widget information.
    await storage.delete(formId);
    hilog.info(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] deleteFormInfo, del form info successfully, formId: ${formId}\`);
    await storage.flush();
  } catch (err) {
    hilog.error(DOMAIN\_NUMBER, TAG, \`\[EntryFormAbility\] failed to deleteFormInfo,
      err: ${JSON.stringify(err as BusinessError)}\`);
  };
};

export default class JsCardFormAbility extends FormExtensionAbility {
// ···
  onRemoveForm(formId: string): void {
    // Delete widget data.
    hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onRemoveForm');
    // Delete the persistent widget instance data.
    deleteFormInfo(formId, this.context);
  }
// ···
}

For details about how to implement persistent data storage, see [Application Data Persistence](../../../arkdata/application-data-persistence/application-data-persistence-overview/document.md).

The **Want** object passed in by the widget host to the widget provider contains a flag that specifies whether the requested widget is normal or temporary.

-   Normal widget: a widget persistently used by the widget host
    
-   Temporary widget: a widget temporarily used by the widget host. (Currently, there is no temporary widget scenario.)
    

Data of a temporary widget will be deleted on the Widget Manager if the widget framework is killed and restarted. The widget provider, however, is not notified of the deletion and still keeps the data. Therefore, the widget provider needs to clear the data of temporary widgets proactively if the data has been kept for a long period of time. If the widget host has converted a temporary widget into a normal one, the widget provider should change the widget data from temporary storage to persistent storage. Otherwise, the widget data may be deleted by mistake.

## Updating Widget Data

When an application initiates a scheduled or periodic update, the application obtains the latest data and calls **updateForm()** to update the widget.

For details about how to import the code, see [Creating a FormExtensionAbility Instance](#creating-a-formextensionability-instance).

// entry/src/main/ets/jscardformability/JsCardFormAbility.ets
const TAG: string = 'JsCardFormAbility';
// ···
const DOMAIN\_NUMBER: number = 0xFF00;
// ···

export default class JsCardFormAbility extends FormExtensionAbility {
// ···
  onUpdateForm(formId: string): void {
    // Override this method to support interval-based updates, time-specific updates, or updates requested by the widget host.
    hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onUpdateForm');
    let obj: Record<string, string> = {
      'title': 'titleOnUpdate',
      'detail': 'detailOnUpdate'
    };
    let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
    formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
      hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] updateForm, error:' + JSON.stringify(error));
    });
  }
// ···
}

## Developing the Widget UI Page

You can use the web-like paradigm (HML+CSS+JSON) to develop JS widget pages. This section describes how to develop a page shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/EXGEVqB-SFK73py3S5HBTQ/en-us_image_0000002537925008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0B75AD916FEB8C5E872B89535632B9559B134C49B3C5DD5F153990956D18969)

-   HML: uses web-like paradigm components to describe the widget page information.
    
    <div class="container">
      <stack>
        <div class="container-img">
          <image src="https://developer.huawei.com/common/widget.png" class="bg-img"></image>
        </div>
        <div class="container-inner">
          <text class="title">{{title}}</text>
          <text class="detail\_text" onclick="routerEvent">{{detail}}</text>
        </div>
      </stack>
    </div>
    
-   CSS: defines style information about the web-like paradigm components in HML.
    
    .container {
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    
    .bg-img {
      flex-shrink: 0;
      height: 100%;
    }
    
    .container-inner {
      flex-direction: column;
      justify-content: flex-end;
      align-items: flex-start;
      height: 100%;
      width: 100%;
      padding: 12px;
    }
    
    .title {
      font-size: 19px;
      font-weight: bold;
      color: white;
      text-overflow: ellipsis;
      max-lines: 1;
    }
    
    .detail\_text {
      font-size: 16px;
      color: white;
      opacity: 0.66;
      text-overflow: ellipsis;
      max-lines: 1;
      margin-top: 6px;
    }
    
-   JSON: defines data and event interaction on the widget UI page.
    
    {
      "data": {
        "title": "TitleDefault",
        "detail": "TextDefault"
      },
      "actions": {
        "routerEvent": {
          "action": "router",
          "abilityName": "EntryAbility",
          "params": {
            "message": "add detail"
          }
        }
      }
    }
    

## Developing Widget Events

You can set router and message events for components on a widget. The router event applies to UIAbility redirection, and the message event applies to custom click events.

The key steps are as follows:

1.  Set the **onclick** field in the HML file to **routerEvent** or **messageEvent**, depending on the **actions** settings in the JSON file.
    
2.  Set the router event.
    
    -   **action**: **"router"**, which indicates a router event.
    -   **abilityName**: name of the UIAbility to redirect to (PageAbility component in the FA model and UIAbility component in the stage model). For example, the default UIAbility name of the stage model created by DevEco Studio is EntryAbility.
    -   **params**: custom parameters passed to the target UIAbility. Set them as required. The value can be obtained from **parameters** in **want** used for starting the target UIAbility. For example, in the lifecycle function **onCreate** of the MainAbility in the stage model, you can obtain **want** and its **parameters** field.
3.  Set the message event.
    
    -   **action**: **"message"**, which indicates a message event.
    -   **params**: custom parameters of the message event. Set them as required. The value can be obtained from **message** in the widget lifecycle function **onFormEvent()**.

The following are examples:

-   HML file:
    
    <div class="container">
        <stack>
            <div class="container-img">
                <image src="https://developer.huawei.com/common/CardWebImg.png" class="bg-img"></image>
                <image src="https://developer.huawei.com/common/CardWebImgMatrix.png"
                       class="bottom-img"/>
            </div>
            <div class="container-inner">
                <text class="title" onclick="routerEvent">{{ title }}</text>
                <text class="detail\_text" onclick="messageEvent">{{ detail }}</text>
            </div>
        </stack>
    </div>
    
-   CSS file:
    
    .container {
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .bg-img {
        flex-shrink: 0;
        height: 100%;
        z-index: 1;
    }
    
    .bottom-img {
        position: absolute;
        width: 150px;
        height: 56px;
        top: 63%;
        background-color: rgba(216, 216, 216, 0.15);
        filter: blur(20px);
        z-index: 2;
    }
    
    .container-inner {
        flex-direction: column;
        justify-content: flex-end;
        align-items: flex-start;
        height: 100%;
        width: 100%;
        padding: 12px;
    }
    
    .title {
        font-family: HarmonyHeiTi-Medium;
        font-size: 14px;
        color: rgba(255, 255, 255, 0.90);
        letter-spacing: 0.6px;
        font-weight: 500;
        width: 100%;
        text-overflow: ellipsis;
        max-lines: 1;
    }
    
    .detail\_text {
        font-family: HarmonyHeiTi;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.60);
        letter-spacing: 0.51px;
        font-weight: 400;
        text-overflow: ellipsis;
        max-lines: 1;
        margin-top: 6px;
        width: 100%;
    }
    
-   JSON file:
    
    {
      "data": {
        "title": "TitleDefault",
        "detail": "TextDefault"
      },
      "actions": {
        "routerEvent": {
          "action": "router",
          "abilityName": "JSCardEntryAbility",
          "params": {
            "info": "router info",
            "message": "router message"
          }
        },
        "messageEvent": {
          "action": "message",
          "params": {
            "detail": "message detail"
          }
        }
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/zndwOFSJQ_aMY-Ap-G697Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2CEF3F5B282F8963DF774474B471E0A15C161A79045BED44AEFCAF35AE9C7B7)

The JSON value of **data** supports multi-level nested data. When updating data, ensure that complete data is carried.

Suppose a widget displays Mr. Zhang's course information for July 18, as shown in the following code snippet.

"data": {
    "Day": "07.18",
    "teacher": {
        "name": "Mr.Zhang",
        "course": "Math"
    }
}

To update the widget content to the course information of Mr. Li on July 18, you must pass the complete data as follows, instead of only a single date item such as **name** or **course**:

"teacher": {
    "name": "Mr.Li",
    "course": "English"
}

-   Receive the router event in UIAbility and obtain parameters.
    
    // entry/src/main/ets/entryability/EntryAbility.ets
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { window } from '@kit.ArkUI';
    
    const TAG: string = 'EntryAbility';
    const DOMAIN\_NUMBER: number = 0xFF00;
    // ···
    export default class EntryAbility extends UIAbility {
      onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        if (want?.parameters?.params) {
          let params: Record<string, Object> = JSON.parse(JSON.stringify(want.parameters.params));
          // Obtain the info parameter passed in the router event.
          if (params.info === 'router info') {
            // Implement the service logic.
            hilog.info(DOMAIN\_NUMBER, TAG, \`router info: ${params.info}\`);
          }
          // Obtain the message parameter passed in the router event.
          if (params.message === 'router message') {
            // Implement the service logic.
            hilog.info(DOMAIN\_NUMBER, TAG, \`router message: ${params.message}\`);
          }
        }
      }
    // ···
    }
    
-   Receive the **message** event in FormExtensionAbility and obtain the parameters. For details about how to import the code, see [Creating a FormExtensionAbility Instance](#creating-a-formextensionability-instance).
    
    // entry/src/main/ets/jscardformability/JsCardFormAbility.ets
    const TAG: string = 'JsCardFormAbility';
    // ···
    const DOMAIN\_NUMBER: number = 0xFF00;
    // ···
    
    export default class JsCardFormAbility extends FormExtensionAbility {
    // ···
      onFormEvent(formId: string, message: string): void {
        // If the widget supports event triggering, override this method and implement the trigger.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onFormEvent');
        // Obtain the detail parameter passed in the message event.
        let msg: Record<string, string> = JSON.parse(message);
        if (msg.detail === 'message detail') {
          // Implement the service logic.
          hilog.info(DOMAIN\_NUMBER, TAG, 'message info:' + msg.detail);
        }
      }
    }
