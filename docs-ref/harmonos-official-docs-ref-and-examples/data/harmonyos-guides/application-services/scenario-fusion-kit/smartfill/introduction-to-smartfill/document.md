# Introduction to SmartFill

SmartFill offers scenario-specific input suggestions to realize one-tap filling of complex forms for users. It helps you with system development for your app or atomic service to unleash peak input efficiency within the HarmonyOS ecosystem. This function can be started using just a single line of code after you integrate ArkUI input components (including [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput) and [TextArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textarea)).

#### Restrictions

SmartFill supports phones, tablets, and (since 5.1.0(18)) 2-in-1 devices.

#### Applying to Integrate SmartFill

## Precautions About Using SmartFill

-   SmartFill is available only to **[company developers who have passed identity verification](https://developer.huawei.com/consumer/en/doc/start/edrna-0000001062678489)**.
-   Fields that SmartFill supports meet your service requirements. For details about the supported fields, please refer to [ContentType Scenarios](../contenttype-scenarios/document.md).

## Integrating SmartFill

To integrate SmartFill, you need to send an application and wait for approval. The application process is as follows:

1.  Create an app ID for your HarmonyOS app or atomic service by referring to [Creating a HarmonyOS App or Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-createharmonyapp-0000001945392297).
2.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
3.  Select your app, find **SmartFill** on the **Manage open capabilities** tab page, and click the apply button on the right.
4.  In the **New request** dialog box, enter your application reason, upload the required attachment, and submit.
    
    -   **Request reason**: Describe your **scenario for using SmartFill**. (For example: App XXX is XXX (app introduction) and needs SmartFill to support XXX fields in the scenario XXX to improve the form filling efficiency for users.) For details about the supported fields, please refer to [ContentType Scenarios](../contenttype-scenarios/document.md).
    -   **Attachment**: Upload screenshots or videos that demonstrate how your app uses SmartFill.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Jzts09p1SHqjOm7aSHku2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6F564D28A5472667FD4C4150B4911C7F992B3E19C1809D52F3464115E961180)
    
    Apply only for necessary fields to be supported by SmartFill based on your service needs and use them properly. If your app uses SmartFill improperly, we will withdraw the service authorization.
    
5.  Go to the interaction center and check your application.
6.  Go back to the **Manage open capabilities** tab page. The switch of SmartFill is dimmed, and the apply button text changes, indicating that the capability is being requested.
7.  Wait for approval. Once your application is approved, you will receive a notification at the interaction center. Then your app has integrated SmartFill successfully.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Dxx0oPtATi2_KpB78OlhDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FE9BC988C8AD7014D642A30653A25AAA6CEF0F19DEBDB76EC8A36D6243EC043)
    
    -   The capability will take effect in about 30 minutes after approval.
    

#### Prerequisites

-   SmartFill has been enabled on the target device. To enable the function, a user can go to **Settings** > **Privacy and security** > **SmartFill** on their device. On the page, the user can check the _Statement About SmartFill and Privacy_ and _Permissions Notice_.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/tGIPBTIoR-yE5FoZlkCDAg/en-us_image_0000002506053764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FEA7BEF76BEC7873118CE8B1D1593185248104A8BC5E11F81EE1431BAD2CE33 "Click to enlarge")
    
-   The SmartFill function can be triggered in scenarios specified in the [ContentType](../contenttype-scenarios/document.md) attribute of the input component for your app or atomic service.
-   The device is connected to the Internet.

#### Intelligent Form Filling

## Suggestions for Form Filling

In the form, when a user taps any input component with the **ContentType** attribute set, input suggestions will be displayed below. For details about the data sources, please refer to [Data Sources and Logic of Suggestions](../data-sources-and-logic-of-suggestions/document.md).

-   When a user taps an input component whose **ContentType** is **PERSON\_FULL\_NAME**, or one of the input components whose **ContentType** is **PERSON\_LAST\_NAME** and **PERSON\_FIRST\_NAME** in a form, data of other **ContentType** settings in the form is also suggested. This is called the multi-box input scenario.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/k6mQYrs_QA6ki0-OFLSyUA/en-us_image_0000002503572063.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CF5557AA9F56D8E89383E02C65D0BE344BB0466B77BEB90DBB15650353FF4C7 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/hzFC9xtOTi63K7afvcm-9g/en-us_image_0000002503572065.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B78B3217A6B7C7C4861B1758479CB8C84F240446255F575B53C73A80837358D "Click to enlarge")
    

-   When a user taps an input component whose **ContentType** is not **PERSON\_FULL\_NAME**, **PERSON\_LAST\_NAME**, or **PERSON\_FIRST\_NAME**, the data of only the specified scenario setting is suggested. For example, if a user taps the input component whose **ContentType** is **NICKNAME**, only nickname data is suggested. This is called the single-box input scenario.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/yoacfbg5T-6R5iJs9pfvfQ/en-us_image_0000002503572057.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=722A7FAF7BE6ACB985BC6C27FCFB00712FF2FDC98D5C5378357D25A68997AC29 "Click to enlarge")
    

-   In the scenario where a form contains an input component whose **ContentType** is **PERSON\_FULL\_NAME** or contains two input components whose **ContentType** is **PERSON\_LAST\_NAME** and **PERSON\_FIRST\_NAME** respectively, and the corresponding information has been filled, if a user taps another input component with **ContentType** set to another value, input suggestions associated with the filled name information are displayed. For example, if the name **Zhang San** is filled, when a user taps the input component used for mobile number input, information associated with Sam Smith will be obtained from the data source for suggestions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/0FHjHS7yTdeAC6bxofRGgw/en-us_image_0000002531154017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04EE0F183CCDD3A0DCF862E16B91056FF811B5E0552060BA1BE8238AB2A2DF42 "Click to enlarge")
    
-   In the scenario where a form contains an input component whose **ContentType** is **PERSON\_FULL\_NAME** or contains two input components whose **ContentType** is **PERSON\_LAST\_NAME** and **PERSON\_FIRST\_NAME** respectively, and there is also an address input component, if any of the above mentioned components is tapped and address information associated with the specific HUAWEI ID exists, the number of associated addresses could be greater than the maxim that can be displayed. In this case, a user can tap **Other addresses** to show more.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/efJzcp-PQY2zBJCWqNSeCA/en-us_image_0000002470332192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E4E20662577CAD07587837FB1EBA18ADA8A85651F3E50C01CB2896B83CBB22D "Click to enlarge")
    

## Nickname Suggestion

If a form requires nickname input, related suggestions can be obtained from Account Kit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/QT5DX0MDQTaBOvpcTkyJ6Q/en-us_image_0000002470332188.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CA6AB22BC695380607016F4788C5F25242F52FBEEC884182BCC2AFBF21E9115 "Click to enlarge")

## Calendar Event Suggestion

If a form contains a text input component with **ContentType** set to **FORMAT\_ADDRESS** (detailed address), data will be obtained from events information generated in recent 2 hours for suggestions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/shV2D1O3TDSJJTXJaJwp-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26B28F819D4F9D07FBA7B5427FBB0EE7BC647DE9003E1E969965ADBB622E7D05)

Currently, only Chinese addresses are supported for suggestions based on calendar events data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Crzm9M_oSfelMWbSxpEVsg/en-us_image_0000002503412157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E632CAA1B1B3CE0D89B91BE82E80A32A1273DDB6A8DB93C2ABB6E7B773AA0BA "Click to enlarge")

## Contact Information Suggestion

When a user taps an input component whose **ContentType** is **PHONE\_NUMBER**, if the form contains an input component whose **ContentType** is **PERSON\_FULL\_NAME** or contains two input components whose **ContentType** is **PERSON\_LAST\_NAME** and **PERSON\_FIRST\_NAME** respectively that have been filled, contacts information will be recommenced based on the input name information.

## License Plate Information Suggestion

SmartFill supports license plate number filling suggestions since version 5.1.0(18).

If a form requires license plate number input, related suggestions can be obtained from the license plate information of the device owner stored in recent forms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/_UarbGviR76sEytzlAVsmA/en-us_image_0000002503412167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED571E17F995BE5588B515CB9E6C1B5C857F7351BBAC806386625DDF2E937792 "Click to enlarge")

## Passport Information Suggestion

SmartFill supports passport information filling suggestions since version 5.1.0(18).

In the scenario where a form contains an input component whose **ContentType** is **COUNTRY\_ADDRESS** (nationality), **PASSPORT\_NUMBER** (passport number), **VALIDITY** (expiration date), or **ISSUE\_AT** (issuance place), if a component requires name input is tapped, passport information can be obtained from recent forms to offer suggestions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Bqg2vGTgS5yB0M6-BTlh9w/en-us_image_0000002470332190.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3B113425E38F18A7F5D60A88B3BA6A022434E2FC1F6EB48AED9D04708C7CD2F "Click to enlarge")

## Invoice Title Suggestion

SmartFill supports invoice title information filling suggestions since version 5.1.0(18).

In the scenario where a form contains an input component whose **ContentType** is **ORGANIZATION** (organization name) and also an input component whose **ContentType** is **TAX\_ID**, suggestions can be made. If the former component (**ORGANIZATION**) is tapped, suggestions can be made either based on the data obtained from Account Kit or based on the user input. Then suggestions for the component with **ContentType** set to **TAX\_ID** will be provided based on the organization name input. If only one of the components exists, suggestions will not be available.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/KjdgrAcYQG6Am7WSafKkJw/en-us_image_0000002470332196.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E701453982A7E1641F2CD55BE5DAF4AD3E2819827B00BA0F60D12F7A5DB61023 "Click to enlarge")

#### Recent Forms

Previously filled form information can be saved in your app or atomic service for later filling suggestions.

## Saving Recent Forms

When a user fills a form, input components with the **ContentType** attribute set will trigger recent form saving, asking the user whether to save the input. If the user confirms, they will be then asked whether to enable SmartFill, so that forms can be filled in with a single tap later.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/h4xzEr98SfiMeje54QFvog/en-us_image_0000002506214604.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9448DB01FDFCCDCC6B7D6BA9E2190BCD7ECBEBF9F00A17DF4451A953B742D0E1 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/VzCI-5MOTnanzeVYmJWxhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DAC48B5E45B16EBB1A4133BA5DA913A182DFDB7BB9692E08E506F8BAFA7C358)

-   When a user switches or exits a page in a form for which SmartFill is enabled, the [requestAutoSave](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-autofillmanager#autofillmanagerrequestautosave) API is called to show the saving page, asking the user whether to save the input in a pop-up. You can also actively call this API to save recent forms.
-   After the user taps the button to confirm saving of recent forms on the displayed page, if the SmartFill function has not been enabled, the user will be further prompted to enable this function. Only by enabling the function will recent forms be saved.
-   If the user ignores saving of recent forms, the same app will not ask the user again within 24 hours. If saving of recent forms is ignored for five times on the same device, the user will be prompted to choose whether they don't want to be asked again.

## Updating Recent Forms

In the scenario where a form contains an input component whose **ContentType** is **PERSON\_FULL\_NAME** as well as another input component with the **ContentType** attribute set, if a user enters a name that already exists but other input information is different from recent form information saved for the name, the user will be asked whether to update the saved input or save the current input as a new record.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/QKcBIbAUR62cQxK9oTTZnA/en-us_image_0000002503412159.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C9C372EF36944A881DE8053E630661B1DA73B39C4DFA9B016218C5180D05796 "Click to enlarge")

## Adding or Modifying Recent Forms Manually

A user can manage recent forms under **Smart fill** or **Personal info**. They can either add new records or modify or delete existing records. If a lock screen password is set for the device, the user needs to enter the password to check recent forms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/zDwBbzvkR6OzEoDLyB_D1w/en-us_image_0000002537934803.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=523BFD9CC23ED49D0421A9DA20D8F094D189DB91A87F6BDD42FD5BC72E24D319 "Click to enlarge")

#### Data Synchronization with Cloud Space Service

Data is synchronized across multiple devices under the same HUAWEI ID through the cloud space service.

## Data Synchronization Across Multiple Devices with Cloud Space Service

After a user signs in to their HUAWEI ID, SmartFill is enabled under **Cloud**, and recent form data can be synchronized between multiple devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/lMtHW4QbS56hmU2-4QWI4g/en-us_image_0000002533071225.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D413F86AAC0341E35DFEBCAD7A20ABF9EA9B53B038C3DF7DE49C3E647B0658 "Click to enlarge")
