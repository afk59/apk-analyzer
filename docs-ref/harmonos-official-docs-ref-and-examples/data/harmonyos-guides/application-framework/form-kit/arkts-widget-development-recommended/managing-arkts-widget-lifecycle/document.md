# Managing ArkTS Widget Lifecycle

When creating an ArkTS widget, you need to implement the [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) lifecycle APIs.

1.  Import related modules to **EntryFormAbility.ets**.
    
    // entry/src/main/ets/entryformability/EntryFormAbility.ts
    import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
    import { Configuration, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  In **EntryFormAbility.ets**, implement the [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) lifecycle API, including **onAddForm**, in which [want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) can be used to obtain the widget information through [FormParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-forminfo#formparam).
    
    // entry/src/main/ets/entryformability/EntryFormAbility.ts
    const TAG: string = 'EntryFormAbility';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
    export default class EntryFormAbility extends FormExtensionAbility {
      onAddForm(want: Want): formBindingData.FormBindingData {
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onAddForm');
        hilog.info(DOMAIN\_NUMBER, TAG, want.parameters?.\[formInfo.FormParam.NAME\_KEY\] as string);
        // Called when the widget host creates a widget. The widget provider should return the widget data binding class.
        let obj: Record<string, string> = {
          'title': 'titleOnAddForm',
          'detail': 'detailOnAddForm'
        };
        let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
        return formData;
      }
    
      onCastToNormalForm(formId: string): void {
        // This callback function is not required for the widget host.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onCastToNormalForm');
      }
    
      onUpdateForm(formId: string): void {
        // Override this method to support interval-based updates, time-specific updates, or updates requested by the widget host.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onUpdateForm');
        let obj: Record<string, string> = {
          'title': 'titleOnUpdateForm',
          'detail': 'detailOnUpdateForm'
        };
        let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
        formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
          hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] updateForm, error:' + JSON.stringify(error));
        });
      }
    
      onChangeFormVisibility(newStatus: Record<string, number>): void {
        // Called when the widget host initiates an event about visibility changes. The widget provider should do something to respond to the notification. This callback takes effect only for system applications.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onChangeFormVisibility');
      }
    
      onFormEvent(formId: string, message: string): void {
        // If the widget supports event triggering, override this method and implement the trigger.
        hilog.info(DOMAIN\_NUMBER, TAG, \`FormAbility onFormEvent, formId = ${formId}, message: ${message}\`);
        // ···
      }
    
      onRemoveForm(formId: string): void {
        // Remove widget data.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onRemoveForm');
        // Remove the persistent widget instance data.
        // Implement this API based on project requirements.
      }
    
      onConfigurationUpdate(config: Configuration) {
        // Called when the configuration of the environment where the formExtensionAbility is running is being updated.
        // The formExtensionAbility is cleared after 10 seconds of inactivity.
        hilog.info(DOMAIN\_NUMBER, TAG, '\[EntryFormAbility\] onConfigurationUpdate:' + JSON.stringify(config));
      }
    
      onAcquireFormState(want: Want): formInfo.FormState {
        // Called upon a status query request from the widget. By default, the initial widget state is returned.
        return formInfo.FormState.READY;
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/sPAsRccDQTCZ3QfXJoSKlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=619F854E7A83AAE7CE53FB9F46F95037CFECC209ED3DB6348247D9530E1A8319)

The FormExtensionAbility cannot reside in the background. It persists for 10 seconds after the lifecycle callback is completed and exits if no new lifecycle callback is invoked during this time frame. This means that continuous tasks cannot be processed in the widget lifecycle callbacks. For the service logic that may take more than 10 seconds to complete, it is recommended that you [start the application](../arkts-widget-provider-development/arkts-widget-page-interaction/overview-of-arkts-widget-page-interaction/document.md) for processing. After the processing is complete, use [updateForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formprovider#formproviderupdateform) to notify the widget of the update.
