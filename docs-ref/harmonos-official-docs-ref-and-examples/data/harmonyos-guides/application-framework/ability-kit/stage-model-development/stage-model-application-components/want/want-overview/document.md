# Want Overview

#### Definition and Usage of Want

[Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) is an object that transfers information between application components. It is often used as a parameter of [startAbility()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability). For example, when UIAbilityA needs to start UIAbilityB and transfer some data to UIAbilityB, it can use the **want** parameter in **startAbility()** to transfer the data.

**Figure 1** Want usage

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/LEbPsMKPQMKTuInN7ZLYLw/en-us_image_0000002537924290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4CA2986C20C9CD0D96E314D3F802C663B0279D0552E44B5C704F605D989AD03)

#### Types of Want

-   **Explicit Want**: If **abilityName** and **bundleName** are specified in the [want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) parameter when starting an application component, explicit Want is used.
    
    Explicit Want is usually used to start another application component in the same application. You can use the bundle name and ability name in the Want object to specify the target component. When there is an explicit object to process the request, explicit Want is a simple and effective way to start the target application component.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/NQKkeAJ6RY6P6WAtAKZdLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FF187FDB7DEA142E595F5BD5926013CEDB63D48B3EC5B1778B89AC796C5DFE8)
    
    Starting from API version 12, it is not recommended that third-party applications start other applications by specifying an ability (implicit Want mode). Instead, the [linking mode](../../../inter-application-redirection/starting-a-specified-application/overview-of-starting-a-specified-application/document.md#application-links) is recommended.
    
    import { common, Want } from '@kit.AbilityKit';
    // ···
    
    let wantInfo: Want = {
      deviceId: '', // An empty deviceId indicates the local device.
      bundleName: 'com.samples.wantoverview',
      abilityName: 'ExplicitAbility',
    };
    
-   **Implicit Want**: If **abilityName** is not specified in the [want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) parameter when starting an application component, implicit Want is used.
    
    Implicit Want can be used when the object used to process the request is unclear and the current application wants to use a capability (defined by the [skills tag](../../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills)) provided by another application. The system matches all applications that declare to support the capability. For example, for a link open request, the system matches all applications that support the request and provides the available ones for users to select.
    
    import { common, Want } from '@kit.AbilityKit';
    // ···
    
    let wantInfo: Want = {
      // Uncomment the line below if you want to implicitly query data only in the specific bundle.
      // bundleName: 'com.example.myapplication',
      action: 'ohos.want.action.search',
      // entities can be omitted.
      entities: \['entity.system.browsable'\],
      uri: 'https://www.test.com:8080/query/student',
      type: 'text/plain',
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/D_QBSiYSR1OADTEbzETc1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061915Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0D1D54997E36C9C9366F4869BEE54F65280F395EB70FF26D58C62B84D915920)
    
    -   Depending on the application component matching result, the following cases may be possible when you attempt to use implicit Want to start the application component.
        
        -   No application component is matched. The startup fails.
        -   An application component that meets the conditions is matched. That application component is started.
        -   Multiple [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) components that meet the conditions are matched. A dialog box is displayed for users to select one of them.
    -   In the scenario for starting the ServiceExtensionAbility component:
        
        -   If the [want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) parameter passed in contains **abilityName**, the ServiceExtensionAbility component cannot be started through implicit Want.
        -   If the **want** parameter passed in contains **bundleName**, the **startServiceExtensionAbility()** method can be used to implicitly start the ServiceExtensionAbility component. By default, the ServiceExtensionAbility component with the highest priority is returned. If all the matching ServiceExtensionAbility components have the same priority, the first ServiceExtensionAbility component is returned.
