# Redirecting to an App in a Specific Way Through a Cross-Platform Link

#### Use Case

The cross-platform link capability is supported since version 6.0.0(20).

It enables app redirection on HarmonyOS devices in a specified way. After tapping a cross-platform link, users will be redirected to a HarmonyOS preview page, a details page on AppGallery, a custom URL, a deep link, or another specified page.

Cross-platform links are primarily used to send app promotional information directly to users, for example, distributing product campaigns or app promotional activities through SMS messages, emails, or social media.

#### Prerequisites

You have [enabled App Linking](../getting-started/enabling-app-linking/document.md).

#### Development Process

| 
Party

 | 

Procedure

 |
| :-- | :-- |
| 

Target app

 | 

Cloud-side development

 | 

[Enable App Linking](../getting-started/enabling-app-linking/document.md).

 |
| 

Cloud-side development

 | 

[Request a URL prefix](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_section17487350112015) in AppGallery Connect, [add a trusted URL format](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_section95571012226), and [create a cross-platform link](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_section759794318231).

 |
| 

App-side development

 | 

[Configure a cross-platform link in the module.json5 file](#en-us_topic_0000002447485937_en-us_topic_0000002442949429_section2446143184813).

 |
| 

App-side development

 | 

[Process the link passed by the caller app](#en-us_topic_0000002447485937_en-us_topic_0000002442949429_section1620481746).

 |
| 

Caller app

 | 

App-side development

 | 

Open the target app through the [UIAbilityContext.openLink() API](#en-us_topic_0000002447485937_en-us_topic_0000002442949429_section10388164920620) or [system browser/ArkWeb](#en-us_topic_0000002447485937_en-us_topic_0000002442949429_section3736124874513).

 |

#### Configuring the Cross-Platform Link Capability for the Target App

## Requesting a URL Prefix

A URL prefix refers to a part of a cross-platform link, which follows the format of **https://_Domain name_**. Before creating a cross-platform link, you need to request a URL prefix.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project to which your HarmonyOS app belongs. (Ensure that all versions of the app across different platforms are contained within the same project.)
3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **URL prefixes** tab, and click **New URL prefix**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/XrQ4Py7XTGyrM9oDIbtcnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E297518F6F54877CE6A0EE5CBBEDB65401CEE9472C44DEA9855253730953E4D1)
    
    If the **URL prefixes** tab is not displayed, click **Custom configuration** on the right and select the tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/3cKXEClSTfuFtcLy5kr2Vw/en-us_image_0000002453987861.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCC2A744981AAE346204DF3865AC534D24FD44FF4C75F518DB082156915B7B67)
    
4.  Set a prefix for the free domain name provided by AppGallery Connect. The prefix must be unique and contain only lowercase letters and digits. Then click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/CKb3Eb7tRTKrNd_YutQKig/en-us_image_0000002420389376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5A57AA212F7AEC9337F806BF70EA0854E751B9923238F3BF91A7E8F7CCFFEA6)
    
5.  View the complete domain name displayed after it is verified.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/JriUTkk4Ru6GqqvSKvPwYQ/en-us_image_0000002420549712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6621F9F943F7148D277CD689C7456C814317F42223822BCCCC552A0CF51B3089)
    

## Adding a Trusted URL Format

Before creating a cross-platform link, you need to add a trusted URL format to define the format of deep links and custom URLs. Once configured, redirection is restricted to URLs that match the trusted format, helping prevent website spoofing.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project to which your HarmonyOS app belongs. (Ensure that all versions of the app across different platforms are contained within the same project.)
3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **URL trustlist** tab, and click **New trusted URL format**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/o0wdxo6JRRqBr5tceOH21w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41C653C521732345909367B707253408473FD0F036D6EA14DB11A1A95611D63B)
    
    If the **URL trustlist** tab is not displayed, click **Custom configuration** on the right and select the tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/9dFa8A_IRIm_Z5U-QjvSbw/en-us_image_0000002454122849.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDA5077B46A20D4ED513A19484817650516B0F7354F47FF9B5125DB7E280EDCB)
    
4.  Add a trusted URL format using regular expressions, and then click **Release** in the upper right corner.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/TCJ8RY7fSNKLEgNaTb3Lpw/en-us_image_0000002454122921.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B55F2773A6610005B979AF8B5811E5A89AEC2943A4F98EF33548ED90AE6EC69)
    

## Creating a Cross-Platform Link

Configure the cross-platform link to implement redirection in a specified way.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project to which your HarmonyOS app belongs. (Ensure that all versions of the app across different platforms are contained within the same project.)
3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **Cross-platform links** tab, and click **New cross-platform link**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/R52BFEjTQEudN8x1xg5y5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00C872204F7F6B8501E36CD50EB68192D0C1865FC589467672BB2E098622560B)
    
    If the **Cross-platform links** tab is not displayed, click **Custom configuration** on the right and select the tab.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/ePeYSL-pR3yl2TbH5vJkbg/en-us_image_0000002454007969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4168011E2D41B0B08DA25388BA9026766367B624A27C0D1277F7D29F0D7218A6)
    
4.  Set a short link and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ctBdxc7IRS2aud7IZUAdBA/en-us_image_0000002454008361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5D5389371C3CA9E5BE9112C513E947D4A221B035EEEA6ED29F406943737F8BB)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    URL prefix
    
     | 
    
    Prefix of a cross-platform link. If you have not requested a URL prefix, [request one](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_section17487350112015).
    
    You can set a character string as the short link suffix for the cross-platform link in the text box under **URL prefix**. A default suffix is automatically generated by AppGallery Connect. You can change the default suffix to a custom one, but ensure that the custom suffix is unique.
    
     |
    | 
    
    Link preview
    
     | 
    
    Short link to be sent to users through the cross-platform link capability.
    
     |
    
5.  Set a deep link and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4SGwoR3HQhGK7tJdCP8rQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DB7B4573FFE339200D41847CAB246227864159B52A8B69DD27FE7D48C0B27E0)
    
    -   The domain name in the deep link must follow the trusted URL format.
    -   The deep link destination cannot be set to an executable file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/JuHugSHtQaC6hnhfPuHelg/en-us_image_0000002505900284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAC724DC94A6121224DEB126E08AABA2E725959B6BBD49F037065091EAA0DF8F)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Link name
    
     | 
    
    Custom name of the cross-platform link.
    
     |
    | 
    
    Default deep link
    
     | 
    
    URL of the in-app content to be opened.
    
    If **HarmonyOS deep link (API ≥ 12)** is not set, this link will be opened by default.
    
     |
    | 
    
    HarmonyOS deep link (API ≥ 12)
    
     | 
    
    Optional. If specified, this link will be opened preferentially on a HarmonyOS platform.
    
     |
    
6.  Set the cross-platform link behavior for HarmonyOS and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/4d1EdMI3RMGAjEopmzTY3Q/en-us_image_0000002420691118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6160F96BAE0D6880DA37C425184FE5ECB3EAF9337A7CBBF5506271FC6E7691E5)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Link behavior for HarmonyOS (API ≥ 12)
    
     | 
    
    1.  Select **Open in app**, and users will be redirected to the content specified by the deep link in the HarmonyOS app after tapping the cross-platform link.
    2.  Select or add a HarmonyOS app for which you want to configure the deep link.
    
     |
    | 
    
    Redirect a user not installing the app to
    
     | 
    
    If a user has not installed the HarmonyOS app, the user will be directed to the app details page on HUAWEI AppGallery or a custom URL.
    
    CAUTION:
    
    If **Custom URL** is selected for **Redirect a user not installing the app to**, do not enter a URL that targets an executable file.
    
    
    
    
    
     |
    
7.  (Optional) On the **Set tracing parameters** page, set ad tracking parameters to track ad and traffic performance.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/hSvBSObXR-yiGOY9XL_fnA/en-us_image_0000002420691950.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AD5D5DA41C04C7B7703B50B99DC642769E691586736D94B4DD21B33AA675DF0)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Campaign source
    
     | 
    
    Ad channel, for example, **Huawei**. You can also customize a value.
    
     |
    | 
    
    Campaign medium
    
     | 
    
    Identifier of an ad medium, for example, **pic** or **email**.
    
     |
    | 
    
    Campaign name
    
     | 
    
    Name of a campaign, for example, **New Year promotion**.
    
     |
    
8.  (Optional) Set social meta tags to track sharing on social media and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/pp_BHwZ3Sze_7iW-fF-pWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770F39AF9D87B35F5C281E987884AC711E68C87C3B1342270F61731C934A8917)
    
    Learn about the configuration effect by referring to [Social Meta Tags](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-applinking-socialdescription-0000001055261926).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/vXJthyGuQYmkmHYIqhdOfw/en-us_image_0000002420852706.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C9F734568365A4601D2FBA784A8DE827D226CEE63A1F299696BF9B8B29BB398)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Title
    
     | 
    
    Title to be displayed when a cross-platform link is shared on social media.
    
     |
    | 
    
    Image URL
    
     | 
    
    URL of the image to be displayed when a cross-platform link is shared on social media.
    
     |
    | 
    
    Description
    
     | 
    
    Description to be displayed when a cross-platform link is shared on social media.
    
     |
    
9.  (Optional) Set the preview page to divert a user to a proper position.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/nRdMRcc2Q6GVbE9CWzGQhw/en-us_image_0000002476578365.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAC5B4BE0A6FBBA18ADA25DD4F3F1A8F1242E8C75BD54F6B0FC2AEA04E69B816)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Preview page
    
     | 
    
    Indicates whether to display the preview page when a user taps the cross-platform link and the app is not installed.
    
    -   If this check box is selected and the app is not installed, when a user taps the cross-platform link, the preview page will be displayed before the user is diverted to the app details page on AppGallery.
    -   By default, this check box is not selected. When a user who has not installed the app taps the cross-platform link, they will be preferentially diverted to the app details page on AppGallery based on the browser type.
        
        NOTE:
        
        Currently, only HUAWEI Browser supports this function.
        
    
     |
    | 
    
    Preview page information source
    
     | 
    
    Source of information displayed on the preview page. This parameter is available only when **Preview page** is selected.
    
    -   **Social meta tag**: Information on the preview page comes from social meta tags.
    -   **App information on app store**: Information on the preview page comes from the app information configured in AppGallery Connect.
    
     |
    
10.  After all settings are complete, click **Release** in the upper right corner. Your released cross-platform links are listed on the **Cross-platform links** tab page.
     -   Click the QR code icon or **Download QR code** in the **Operation** column of a cross-platform link to download the QR code image of the link.
         
         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/1_jfU5WpQEmmgFIT8CtPVw/en-us_image_0000002454427413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A2355CF20A7C8AC372724CC340DAA633B0DB9EEC02A6E44D7A9F5826A53B3A8)
         
         Click **View details** in the **Operation** column of a cross-platform link to view the link details, including the deep link, HarmonyOS app package name, and short link.
         
         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-M1oeZfZSJ2V577X5ZyubA/en-us_image_0000002420710504.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7ADB3468490D55C535D2D38E4063084A8E71905CADC505B8086FBE622198690)
         

## (Optional) Archiving a Cross-Platform Link

After creating a cross-platform link, you can archive it if you no longer want to manage it but still want to preserve its long-term usability for users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/yiKnmnfHRQGr1JYXx2OR6w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECA2CA583FCB69BD9BF4AF4C6B850C9DF75B8D32CC669AAEAB232DC635BD55BD)

-   A cross-platform link will be hidden after being archived for seven days, and you will be unable to view the link or cancel the archiving in AppGallery Connect.
-   By default, archived cross-platform links remain valid for one year since the archiving time. Exercise caution when archiving links.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project to which your HarmonyOS app belongs.
3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **Cross-platform links** tab, and archive the created cross-platform links.
    
    -   Archiving a single cross-platform link: In the cross-platform link list, click **Archive** in the **Operation** column of the link to be archived.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Z_GOMlmWRNqaDqGqquOJ3A/en-us_image_0000002454411005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C16270E52193E117C47D10AE49715B6A351F43E8BBAD85820996F42F7C2E3F0)
        
    -   Batch archiving: Select multiple links to be archived in the list and select **Archive** from the **Batch operation** drop-down list in the upper right corner.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/GDt6-wkNT7mG1H_X23rM4Q/en-us_image_0000002421055170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78C027E91EF75E9C4149D1FB0199FF53FF9C5BC29435D9A2BE4F5380DEACB994)
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/-EWZcMI1Tii2d5NcIIAmdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE2AC720869854FC5CB544359B979EA13CFFE2303BD6E7E5DBC9840A44E6B61F)
    
    You can filter links by time to view cross-platform links archived in the last seven days. To restore an archived link, you can click **Unarchive** in the **Operation** column.
    

## Configuring a Cross-Platform Link in the module.json5 File

Configure the following information in the [module.json5 file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of your HarmonyOS app to receive a cross-platform link and obtain the data passed through the link.

-   The **entities** list must contain **entity.system.browsable**.
-   The **actions** list must contain **ohos.want.action.viewData**.
-   The **uris** list must contain an element whose **scheme** is **https** and **host** is the domain name of the cross-platform link. The optional attributes include **path**, **pathStartWith**, and **pathRegex**. For details, please refer to [Description of uris](../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-a-specified-application/application-link-description/document.md#description-of-uris).
-   **domainVerify** must be set to **true**, indicating that domain name verification is enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/V8Twy9aCR--2_Fr4MRQNbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05FB222FE04A6488EF437D1577D4BD7F1410AD1826179D128572B331121E6C83)

By default, the **skills** section contains a **skill** object, which is used to mark the app entry. The app redirection link cannot be configured in the **skill** object. Instead, you need to create an independent **skill** object.

If multiple redirection scenarios are involved, create different **skill** objects in the **skills** section. Otherwise, the configuration cannot take effect.

For example, the configuration below is required when the domain name of the cross-platform link is **example.drcn.agconnect.link**.

{
  "module": {
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        // Set **exported** to **true**. If **exported** is set to **false**, only authorized system apps can start the target app.
        "exported": true,
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home"
            \]
          },
          {
            "entities": \[
              // **entities** must contain **entity.system.browsable**.
              "entity.system.browsable"
            \],
            "actions": \[
              // **actions** must contain **ohos.want.action.viewData**.
              "ohos.want.action.viewData"
            \],
            "uris": \[
              {
                // **scheme** must be set to **https**.
                "scheme": "https",
                // **host** must be set to the domain name of the cross-platform link.
                "host": "example.drcn.agconnect.**link**",
                // **path** is optional, which indicates the short link suffix of the cross-platform link, for example, **AIYx** in **example.drcn.agconnect.link/AIYx**.
                // If the app supports only specific paths, provide those paths here to prevent unsupported paths from triggering the app.
                "path": "AIYx"
              }
            \],
            // **domainVerify** must be set to **true**.
           "domainVerify": true
          }
          // If other redirection capabilities are involved, such as push message– and NFC-based redirection, add a **skill** object to prevent conflicts with App Linking.
        \]
      }
    \]
  }
}

## Processing the Link Passed by the Caller App

Add the following code to the [onCreate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) or [onNewWant()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onnewwant) lifecycle callback of the HarmonyOS app's ability (for example, **EntryAbility**) to process the passed link.

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { url } from '@kit.ArkTS';
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Obtain the passed link information from **want**.
    // For example, the passed URL is **https://example.drcn.agconnect.link/AIYx**. You can perform subsequent processing based on your service requirements.
    let uri = want?.uri;
    if (uri) {
      try {
        let urlObject = url.URL.parseURL(want?.uri);
        if (urlObject.toString() === "https://example.drcn.agconnect.link/AIYx"){
          // ...
        }
        // ...
      } catch (error) {
        hilog.error(0x0000, 'testTag', \`Failed to parse url.\`);
      }
    }
  }
}

To start a specified **UIAbility** page component based on link parameters, please refer to [Starting a Specified Page of UIAbility](../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md#starting-a-specified-page-of-uiability).

#### Implementing App Redirection from the Caller App

## Starting the App by Calling the UIAbilityContext.openLink() API

The caller app calls the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API, with **appLinkingOnly** set to **false** or not set. This ensures that the target app is started in the method of preferentially opening the app in App Linking mode.

1.  Add the **GlobalContext.ets** file to the **entry/src/main/ets/common** directory to initialize and obtain the app context.
    
    import { common } from '@kit.AbilityKit';
    
    export class GlobalContext {
      private static context: common.UIAbilityContext;
    
      public static initContext(context: common.UIAbilityContext): void {
        GlobalContext.context = context;
      }
    
      public static getContext(): common.UIAbilityContext {
        return GlobalContext.context;
      }
    }
    
2.  Import **GlobalContext** to the **entry/src/main/ets/entryability/EntryAbility.ets** file and use **GlobalContext.initContext(this.context)** in the **onCreate** method to initialize the global app context.
3.  In the **entry/src/main/ets/pages/Index.ets** file, call the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to configure the cross-platform link.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { GlobalContext } from '../common/GlobalContext';
    
    @Entry
    @Component
    struct Index {
      build() {
        Button('start link', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let context = GlobalContext.getContext();
            // Set **link** to the actual URL for redirection.
            let link: string = "https://example.drcn.agconnect.link/AIYx";
            context.openLink(link, { appLinkingOnly: false })
              .then(() => {
                hilog.info(0x0000, 'testTag', \`Succeeded in opening link.\`);
              })
              .catch((error: BusinessError) => {
                hilog.error(0x0000, 'testTag', \`Failed to open link, code: ${error.code}, message: ${error.message}\`);
              })
          })
      }
    }
    
4.  Install the caller app and tap the redirection button in the app.
    
    Currently, the target app has not been installed. If a matching app is available, tapping the link will redirect to a HarmonyOS preview page, an app details page on AppGallery, a custom URL, or other pages, depending on the method specified during [cross-platform link creation](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_section759794318231). If no app matches, the system attempts to access the app content in a browser.
    
5.  Install the target app. The content details page specified by the deep link will be displayed when the app is launched for the first time.

## Starting the App Through the System Browser or ArkWeb

ArkWeb deeply integrates App Linking. When a user taps a cross-platform link in the system browser or on an embedded web page in an app that integrates ArkWeb, the target app is preferentially started through App Linking if a matching app is available. However, there are certain restrictions:

-   If the [link behavior for HarmonyOS](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_li1761311182013) is configured for the cross-platform link, the HarmonyOS preview page will be displayed, prompting users to open or download the app.
-   If only [a deep link](#en-us_topic_0000002414086764_en-us_topic_0000002409550078_li13663141012470) is configured for the cross-platform link, the content details page specified by the deep link will be displayed.
