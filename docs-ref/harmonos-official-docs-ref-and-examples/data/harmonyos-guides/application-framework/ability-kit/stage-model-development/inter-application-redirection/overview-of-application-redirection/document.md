# Overview of Application Redirection

Application redirection enables users to jump from one application to another to transfer data or perform a specific action. It improves the convenience and smoothness of user interactions.

#### Use Cases

Application redirection is widely used in social media sharing and marketing promotions. Examples are as follows:

-   **Social media sharing**: In social apps, sharing links like location details, food recommendations, shopping deals, or game invites allows for a quick redirection to the relevant navigation, food, shopping, or gaming applications through these links.
-   **Marketing promotions**: On platforms like video applications, social media applications, and web browsers, embedding links to applications being promoted (presented as text, widgets, or videos) enables users to navigate directly to specific pages within the target application. Additionally, including these promotional links in SMS messages or emails allows users to access specific pages within the target application directly through the provided links.

#### Two Types of Application Redirection

-   [Starting a Specified Application](../starting-a-specified-application/overview-of-starting-a-specified-application/document.md): The caller application specifies the target application by specifying either an application link and an ability.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/BAlyWFQPQOyqgY1Rk-2H2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EAC7CB7C07AF5937F3697B55F0B90DB32104922224DCAAEB81C31D1517DA0AA)
    
    Starting from API version 12, it is not recommended that third-party applications start other applications by specifying an ability (implicit Want mode). For details about how to switch from the implicit Want mode to the [linking mode](../starting-a-specified-application/overview-of-starting-a-specified-application/document.md#application-links), see [Switching from Explicit Want Redirection to Linking Redirection](../starting-a-specified-application/switching-from-explicit-want-redirection-to-linking-redirection/document.md).
    
    -   Specifying an application link (recommended): Use [openLink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) or [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability) to specify an [application link](../starting-a-specified-application/overview-of-starting-a-specified-application/document.md#application-links) and start the target application page.
        
    -   Specifying an ability (not recommended): Use [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability) to specify an ability and explicitly start the target application page. This is the explicit Want mode.
        
-   [Starting an Application of the Specified Type](../starting-an-application-of-the-specified-type/overview-of-starting-an-application-of-the-specified-type/document.md): The caller application starts a vertical domain panel based on the specified application type. The panel displays all the vertical applications that can handle the intent, and users can choose to open one of them.
    

#### Typical Scenario: Starting a System Application

Starting a system application is a typical scenario of application redirection. The system provides some capabilities and interfaces for you to quickly implement system application redirection while ensuring access security. For details, see [Starting a System Application](../starting-a-system-application/document.md).
