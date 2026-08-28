# Redirecting to an App Download Page Through Direct Access to AppGallery

#### Use Case

The capability of direct access to AppGallery is supported since version 5.0.3(15).

After configuring the app link based on App Linking, you can create a link to the app download page on AppGallery. Tapping the passed app link will redirect users to the specified in-app content if the app is installed, or the app download page on AppGallery if it is not installed.

#### Mechanism

## Link Effectiveness Mechanism

A direct link to AppGallery does not take effect immediately. Generally, it takes 24 hours to become effective. However, in some cases, it might take 48 hours.

#### Prerequisites

1.  You have [configured an app link based on App Linking](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md) for the target app.
2.  The target HarmonyOS app must have been released. For details, please refer to [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230).

#### Restrictions

Only the app links that pass the domain name verification of App Linking are supported. For details, please refer to [Creating an Associated Website Domain Name for Your App in AppGallery Connect](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section1101111611317).

#### Development Procedure

1.  Configure the capability of directly accessing AppGallery for the target app.
    1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
    2.  Click the project to which the target app belongs.
    3.  In the navigation tree on the left, choose **Grow** > **App Linking**, click the **App links (applicable to API 12 or later)** tab, and click **Configure direct link** in the **Operation** column.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/1TyddIa-Sh-Xwe7Yl1BVNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CA7BF480F44BB5171E1FA6EC5361BE8B8295490B81C8D362C8F49E3A1D9D0AE)
        
        The direct link to AppGallery can be configured only when the release status of the [associated domain name created in AppGallery Connect](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section1101111611317) is **Successful**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/mLd1l8WWRSq4EPFqOFrlUg/en-us_image_0000002505731790.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64F6DCD980752182A9927CF4FB63E14F32BBAE6ED82C9009ACFE2180EF946C88)
        
    4.  On the configuration page, select a released app associated with the domain name from the **Associated app** drop-down list to configure a direct link to AppGallery for the app.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/63L9_yKSSQ-YhTLdnEN7Gg/en-us_image_0000002451705878.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EED273D16DCF6BBA3B900F9EF3C58C326134B87B5E029C4A564FEB133D06504)
        
        -   You can click **Add app** to configure direct links to AppGallery for multiple apps. No additional apps can be added if all released apps associated with the domain name are configured with a link to AppGallery.
        -   You can configure **Direct link** based on the following rules.
            
            | 
            Path
            
             | 
            
            Matching Rule
            
             |
            | :-- | :-- |
            | 
            
            path
            
             | 
            
            Exact matching
            
             |
            | 
            
            pathStartWith
            
             | 
            
            Prefix matching
            
             |
            | 
            
            pathRegex
            
             | 
            
            Regular expression matching
            
             |
            
            -   If **path**, **pathStartWith**, and **pathRegex** are all not configured when you [configure the associated domain name in the module.json5 file](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section13808113610362), one of the following matching rules must be configured:
                
                **pathRegex**: matching path **.\***
                
                **path**: Enter a path for exact matching. The path cannot start with a slash (/), or contain double slashes (//) or duplicate dots (..). Valid characters include letters (a-z and A-Z), digits (0-9), slashes (/), dots (.), underscores (\_), and hyphens (-).
                
            -   (Not recommended) If **pathRegex** is set to **.\*** when you [configure the associated domain name in the module.json5 file](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section13808113610362), the following matching rules can be configured here:
                
                **pathRegex**: matching path **.\***
                
                **path**: Enter a path for exact matching. The path cannot start with a slash (/), or contain double slashes (//) or duplicate dots (..). Valid characters include letters (a-z and A-Z), digits (0-9), slashes (/), dots (.), underscores (\_), and hyphens (-).
                
            -   In other scenarios, you need to configure the path matching rules based on those set when you [configure the associated domain name in the module.json5 file](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section13808113610362).
        -   You can click **Delete link** to delete a direct link to the download page of the app on AppGallery.
        
    5.  After the configuration is complete, click **Release** on the top of the page, and the **App links (applicable to API 12 or later)** tab page is displayed.
        
        If the value of **AppGallery direct link configured** is **Yes**, as shown in the following figure, the link is successfully configured.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Q1R2eWDUQ26EAzKqki_9jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B56E633BF036E983B1458D7672CA2A3B538A5EDBFF760F6C6E8A4A56815570F1)
        
        After the link is configured, it takes 24 to 48 hours for the link to take effect. Please wait patiently.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/mmAJ98qyRx-w8jwQ4jtd1A/en-us_image_0000002537531827.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062100Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D01CA476CB94F5880820943E56A2A11E3149C1E219C1C25C00CCB41CCA8C8A7)
        
2.  Implement the redirection from the caller app.
    
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
    3.  In the **entry/src/main/ets/pages/Index.ets** file, call the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to configure the redirection link.
        
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
                let link: string = "https://www.example.com/product?pageName=productDetail";
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
        
3.  Install the caller app and tap the redirection button in the app.
    
    The target app is not installed. If a matching app is available, tapping the link will redirect to the app download page on AppGallery. If no app matches, the system attempts to access the app content in a browser.
    
4.  After the target app is installed, tap the redirection button in the caller app to directly open the target app.

#### FAQs

## If the target app is not installed, will the app download page on AppGallery be displayed when ArkWeb is used to start the target app?

If the system browser or ArkWeb is used to start a target app that is not installed, the app download page on AppGallery will not be displayed. You need to implement the redirection to AppGallery based on your service requirements. For details, please refer to [Redirecting from an ArkWeb Page to the Specified Application](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-web-app-jump-and-pull-up#section37419543116) in _Redirecting and Starting Between Web Pages and Applications_.

## Which services support App Linking Kit's capability of direct access to AppGallery?

The following services support the capability:

Huawei Share, Tap to Transfer, SMS, MeeTime, and other services that support the **UIAbilityContext.openLink()** API.

The following services do not support the capability:

Browser and code scanning (The capability is under planning for code scanning and will take effect automatically after rollout. No adaptation is required.)

## How many path rules (**path**, **pathStartWith**, or **pathRegex**) can be configured for a direct link to AppGallery?

Each app supports only one path rule.
