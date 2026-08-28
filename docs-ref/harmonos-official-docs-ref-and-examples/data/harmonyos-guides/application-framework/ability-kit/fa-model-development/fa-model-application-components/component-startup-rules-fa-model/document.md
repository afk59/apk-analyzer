# Component Startup Rules (FA Model)

Component startup refers to the behavior of starting or connecting to an application component.

-   Start the PageAbility and ServiceAbility. For example, you can use **startAbility()**.
    
-   Connect to the ServiceAbility and DataAbility. For example, you can use **connectAbility()** and **acquireDataAbilityHelper()**.
    

To deliver a better user experience, the system restricts the following behavior:

-   A background application randomly displays a dialog box, such as an ad pop-up.
    
-   Background applications wake up each other. This type of behavior occupies system resources and increases power consumption, or even causes system frozen.
    
-   A foreground application randomly redirects to another application, for example, redirecting to the payment page of another application. This type of behavior poses security risks.
    

In view of this, the system formulates a set of component startup rules, as follows:

-   **Before starting a component of another application, verify the visible field of the target component.**
    
    -   This rule applies only to cross-application scenarios.
    -   If the **visible** field of the target component is **false**, verify the ohos.permission.START\_INVISIBLE\_ABILITY permission, which is available only for system applications.
    -   For details about the **visible** field, see [Internal Structure of the abilities Attribute](../../../../../getting-started/development-fundamentals/application-configuration-files-in-fa-model/structure-of-the-module-tag/document.md#internal-structure-of-the-abilities-attribute).
-   **Before starting a component of a background application, verify the BACKGROUND permission.**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/z3E1DGw8TGi6Ht1kZO0_VQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3505707FB6E6403845D2591795B658FBCB6ECD11ED59192774ED3EB6C78C222A)
    
    Applications developed using the SDK of API version 8 or earlier are not restricted by this restriction when starting the ServiceAbility or DataAbility.
    
    -   An application is considered as a foreground application only when the application process gains focus or its UIAbility component is running in the foreground.
    -   Verify the ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND permission, which is available only for system applications.
-   **Before starting the ServiceAbility or DataAbility component of an application in the [FA model](../../../ability-kit-terminology/document.md#fa-model), verify the AssociateWakeUp field of the target application.**
    
    -   This rule applies only to cross-application scenarios.
    -   This rule is valid only when the target component is ServiceAbility or DataAbility.
    -   The ServiceAbility and DataAbility of an application can be accessed by other applications only when **AssociateWakeUp** of the target application is set to **true**.
    -   The **AssociateWakeUp** field can be configured only for preset applications. For other applications, this field is set to **false** by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ImkRVj2JTYirSAguZRu1ZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EB470DEA54DD3D3155AB99E0A13FA1944AC17639CC95C84479EB1BCB2800768)

1.  Component startup control has been implemented since v3.2 Release.
    
2.  The new component startup rules are more strict than the original ones. Get familiar with the new startup rules to prevent service exceptions.
    

#### Intra-Device Component Startup Rules

The rules for starting components on the same device vary in the following scenarios:

-   Starting a PageAbility
    
-   Starting a ServiceAbility or DataAbility
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Vid9xYe0SWKCJb1zjzEwNg/en-us_image_0000002568764093.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDD3CFC6D63E925D4E34DC2878BEF2FCC337B9105F8FA278540E6675B6993E6A)

#### Inter-Device Component Startup Rules

The rules for starting components on a different device vary in the following scenarios:

-   Starting a PageAbility
    
-   Starting a ServiceAbility
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/scde87ojRDqO87BWkW6TwA/en-us_image_0000002537764368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061918Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FDFF03D40D548103689AB4A7D671C5C9A16303A3EA5E03F8F2CBDA2E2B70EDD)
