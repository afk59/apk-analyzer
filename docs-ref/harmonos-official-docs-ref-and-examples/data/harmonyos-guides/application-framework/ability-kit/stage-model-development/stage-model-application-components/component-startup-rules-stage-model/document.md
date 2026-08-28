# Component Startup Rules (Stage Model)

Component startup refers to the behavior of starting or connecting to an application component.

-   Start the [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability), ServiceExtensionAbility, and DataShareExtensionAbility components. For example, you can use [startAbility()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability), **startServiceExtensionAbility()**, [startAbilityByCall()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilitybycall), and [openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12).
    
-   Connect to the ServiceExtensionAbility and DataShareExtensionAbility components. For example, you can use [connectServiceExtensionAbility()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#connectserviceextensionability) and **createDataShareHelper()**.
    

#### General Component Startup Rules

To deliver a better user experience, the system restricts the following behavior:

-   A background application randomly displays a dialog box, such as an ads pop-up.
    
-   Background applications wake up each other. This type of behavior occupies system resources and increases power consumption, or even causes system frozen.
    
-   A foreground application randomly redirects to another application, for example, redirecting to the payment page of another application. This type of behavior poses security risks.
    

In view of this, the system formulates a set of component startup rules, as follows:

-   Before starting a component of another application, check whether the component can be called by others.
    
    If the **exported** field of the component is set to **true**, the component can be called by other applications. If the field is set to **false**, the component cannot be called by other applications. If this is the case, you must also verify the permission **ohos.permission.START\_INVISIBLE\_ABILITY**, which is available only for system applications. For details about the **exported** fields, see [abilities](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities).
    
-   Before starting a UIAbility component of a background application, verify the permission **ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND**, which is available only for system applications.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/OJ2NwhFVTkqQ6spp50zRrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F2B63B6DC94E6D3136665BCA4C6DF92DE7B819D0AD7112AB563E4388FA983F5)
    
    -   An application is considered as a foreground application only when the application process gains focus or its UIAbility component is running in the foreground.
    -   For 2-in-1 devices and tablets:
        -   Starting from API version 18, if an application has a floating window in the foreground, it can start other abilities without checking the BACKGROUND permission after the application moves to the background.
        -   Starting from API version 21 onwards, if an application is already in the status bar, it can start its own UIAbility without checking the BACKGROUND permission after the application moves to the background.
    
-   Before using **startAbilityByCall()** to start a component running on another device, verify the permission **ohos.permission.DISTRIBUTED\_DATASYNC**.
    

The component startup rules described above apply from API version 9 onwards. The specific version when new rules come into effect is noted separately within the rules. Familiarity with these rules helps you prevent service exceptions.

#### Intra-Device Component Startup Rules

The rules for starting components on the same device vary in the following scenarios:

-   Starting the UIAbility component
    
-   Starting the ServiceExtensionAbility and DataShareExtensionAbility components
    
-   Using [startAbilityByCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilitybycall) to start the UIAbility component
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/PRFjBXYSSDSPrmnhLtNOzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B05BE08F607AB0AFC4A41B38B0E77E0688D46D4958CCAEBA13680AF04FD44FE)

The BACKGROUND and CALL permissions in the following figure refer to ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND and ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION, respectively.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/8OVk32BnQ722gixh4Xzxkg/en-us_image_0000002537924294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46D9EE64C71080C91E7F946F690E45558A2AB130A06A75F764E2D27A3806E0C1)

#### Inter-Device Component Startup Rules

The rules for starting components on a different device vary in the following scenarios:

-   Starting the UIAbility component
    
-   Starting the ServiceExtensionAbility and DataShareExtensionAbility components
    
-   Using [startAbilityByCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startabilitybycall) to start the UIAbility component
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/PlsIxDYlSuSAWll33so5pQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27DC4C659E09D87B7E662A834765AC2472E183E291F853955964B1D24609BCF5)

The BACKGROUND and DATASYNC permissions in the following figure refer to ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND and ohos.permission.DISTRIBUTED\_DATASYNC, respectively.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/7tPZwocKQJixNc8Ur0kstA/en-us_image_0000002568684071.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B1CDDC9AAF2342EE923241A2CA82A71307DE3378C6AEBF17BFABBAE45B33815)
