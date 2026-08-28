# Security Mode of the Input Method

To protect user data, the input method module has incorporated a security mode, which includes the basic mode (**BASIC**) and full experience mode (**FULL**). In basic mode, the InputMethodExtensionAbility cannot call any system capability that may involve accessing or disclosing user privacy data. In full experience mode, there is no such restriction.

Users can switch between the basic mode and the full experience mode in **Settings**.

#### Basic Mode

1.  The **InputMethodExtensionAbility** process cannot start any other UIAbility or ExtensionAbility.
2.  The InputMethodExtensionAbility is controlled by the system and cannot call the APIs that may access or disclose user personal data, or transfer data out of the process. Specifically, the InputMethodExtensionAbility cannot call the APIs related to the following: network, SMS, phone, microphone, location, camera, Bluetooth, wallpaper, payment, calendar, games, speaker, Wi-Fi, pasteboard, multimedia, contacts, common events, system account, health data, map service, push service, fusion search, shared memory, distributed features, advertising device identifier, vibration, and more.
3.  The InputMethodExtensionAbility can use necessary system capabilities like IME Kit, ArkUI, windows, graphics, and screen management.
4.  The InputMethodExtensionAbility has the read-only permission for the [shared sandbox](#section4219152220459), and has read and write permissions for its independent sandbox. The application main entry has read and write permissions for the [shared sandbox](#section4219152220459) and the InputMethodExtensionAbility's independent sandbox.

#### Full Experience Mode

1.  The InputMethodExtensionAbility does not have the restrictions of the basic mode. It can start UIAbility or ExtensionAbility to call the APIs for accessing user data.
2.  The InputMethodExtensionAbility has read and write permissions for the [shared sandbox](#section4219152220459).

#### How to Develop

You can obtain the security mode of the InputMethodExtensionAbility by calling [getSecurityMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-inputmethodengine-V5#getsecuritymode11) in the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-inputmethod-extension-ability-V5#inputmethodextensionabilityoncreate) callback function of the InputMethodExtensionAbility.

-   In basic mode, display the internal functionalities that can be used.
-   In full experience mode, you can use the user data access APIs for improving user experience.

To ensure stable input method functions, use only the basic input capabilities in basic mode. Do not transfer data outside the InputMethodExtensionAbility by bypassing the system mechanism.

#### Shared Sandbox

1.  The InputMethodExtensionAbility and the application main entry each have their own sandbox and cannot access each other's sandbox.
2.  A shared sandbox is provided to facilitate data transfer and share between them.
    
    **Figure 1** Shared sandbox  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/ucRHT3KxQNiiBeGo6vifmw/en-us_image_0000002531250320.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8A4724F33C2483F3ECD884FA59E389DC1A0235BCE0942D656FFFFD4F5F3BBAA "Click to enlarge")
    
3.  To use the shared sandbox, configure **data-group-ids** in the [profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-releaseprofile-0000001914714796) of your application and configure [dataGroupIds](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/module-configuration-file-V5#extensionabilities) in the **module.json5** file containing **InputMethodExtensionAbility**. The procedure for requesting **data-group-id** is as follows.
    1.  Send an email to agconnect@huawei.com in the following format:
        1.  Email title: \[Requesting in-app data sharing\] _xxx_ app
        2.  Email body:
            
            App ID: _xxx_
            
            App name: _xxx_
            
            Developer ID: _xxx_
            
            Required attachments:
            
            1\. Screenshot of the input method application in the input method list.
            
            2\. Screenshot of the **dataGroupIds** setting in the **module.json5** file for **InputMethodExtensionAbility**.
            
    2.  After the approval, you will receive an email reply.
4.  Input method applications can obtain the shared sandbox path using [getGroupDir](https://developer.huawei.com/consumer/en/doc/harmonyos-references-V5/js-apis-inner-application-context-V5#contextgetgroupdir10).
