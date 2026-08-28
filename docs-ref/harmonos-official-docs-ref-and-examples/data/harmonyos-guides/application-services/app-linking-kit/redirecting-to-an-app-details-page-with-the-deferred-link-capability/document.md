# Redirecting to an App Details Page with the Deferred Link Capability

#### Use Case

The deferred link capability is supported since version 5.0.3(15).

If a user to whom an app link is shared has not installed the app, the deferred link capability enables the system to obtain the previously tapped link when the app is opened for the first time by calling the deferred link API. Once the link is obtained, the corresponding app details page, instead of the app home page, will be directly displayed, enhancing user experience and the link conversion rate.

#### Mechanism

## One-Time Use

The deferred link can be obtained only once. After it is obtained, the system deletes the link from the cache. Subsequent calls will return an empty response.

## Cache

-   Validity period: The maximum cache duration of a link is 10 minutes. The link will be automatically deleted once this period expires.
-   Maximum number of cached links: The system can cache up to 50 links. The earliest cached link will be automatically deleted once this limit is exceeded.

#### Prerequisites

1.  You have [configured an app link based on App Linking](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md) for the target app.
2.  This capability applies only to HarmonyOS apps with API version 15 or later.

#### Restrictions

Only the app links that pass the domain name verification of App Linking are supported. For details, please refer to [Creating an Associated Website Domain Name for Your App in AppGallery Connect](../starting-an-app-with-the-app-link-capability-of-app-linking/document.md#en-us_topic_0000002415444457_section1101111611317). It is advised that the deferred link API be called after the privacy agreement is signed upon the first launch. This ensures that the domain name verification is successful at that time.

#### Development Procedure

1.  Configure the target app to obtain the deferred link.
    1.  Add the following code to the entry page file **Index.ets**. When the app is opened for the first time, the [deferredLink.popDeferredLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/applinking-deferredlink-api#section15555111210233) API is called to obtain the app link tapped previously by the user.
        
        import { deferredLink } from '@kit.AppLinkingKit';  
        import { hilog } from '@kit.PerformanceAnalysisKit';
        
        @Entry
        @Component
        struct Index {
        pageStack: NavPathStack = new NavPathStack();
           build() {
              Column() {
                 Navigation(this.pageStack) {
                    Button("Obtain deferred link").onClick(() => {
                       // When the app is opened for the first time, obtain the app link tapped previously by the user.
                       deferredLink.popDeferredLink().then((link: string) => {
                          hilog.info(0x0000, 'testTag', \`Succeeded in getting deferred link, result: ${link}\`);
                       }).catch(() => {
                         // Unknown error.
                          hilog.error(0x0000, 'testTag', \`Failed to get deferred link.\`);
                       })
                    })
                    // ...
                 }
                 // ...
              }
           }
        }
        
    2.  Configure the service logic for redirecting the link to the details page.
        
        import { deferredLink } from '@kit.AppLinkingKit';
        import { hilog } from '@kit.PerformanceAnalysisKit';
        import { url } from '@kit.ArkTS';
        
        @Entry
        @Component
        struct Index {
          pageStack: NavPathStack = new NavPathStack();
          build() {
            Column() {
              Navigation(this.pageStack) {
                Button("Obtain deferred link").onClick(() => {
                  // When the app is opened for the first time, obtain the app link tapped previously by the user.
                  deferredLink.popDeferredLink().then((link: string) => {
                    hilog.info(0x0000, 'testTag', \`Succeeded in getting deferred link, result: ${link}\`);
                    // If the link is successfully obtained, it can redirect to the details page based on the service logic that you define.
                    if (link) {
                      // Configure the service logic for redirecting the link to the details page.
                      // For example, the passed URL is **<https://www.example.com/product?pageName=productDetail>**.
                      // Parse the **query** parameter from the link. You can perform subsequent processing based on your service requirements.
                      try {
                        let urlObject = url.URL.parseURL(link);
                        let pageName = urlObject.params.get('pageName');
                        this.pageStack.pushPath({ name: pageName });
                      } catch (error) {
                        hilog.error(0x0000, 'testTag', \`Failed to parse url.\`);
                      }
                    }
                  }).catch(() => {
                    // Unknown error.
                    hilog.error(0x0000, 'testTag', \`Failed to get deferred link.\`);
                  })
                })
                // ...
              }
              // ...
            }
          }
        }
        
2.  Implement the redirection from the caller app to the target app.
    
    The caller app passes the link of the target app through the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to start the target app.
    
    The **UIAbilityContext.openLink()** API provides two methods for starting the target app.
    
    -   Method 1: Open the app only in App Linking mode.
        
        In this method, **appLinkingOnly** is set to **true**. If an app is matched, that app is directly opened. If no app matches, an exception is thrown.
        
        This method applies to scenarios where you have implemented exception handling for target app launch failure. For example, if the caller app integrates ArkWeb, the link can be opened through ArkWeb if the target app is unavailable.
        
    -   Method 2: Preferentially open the app in App Linking mode.
        
        In this method, **appLinkingOnly** is set to **false** or not set. If an app is matched, that app is directly opened. If no app matches, the system attempts to access the app content in a browser.
        
        This method applies to scenarios where you have not implemented exception handling for target app launch failure. If the target app is unavailable, the link is opened through the system browser.
        
    
    This section describes method 1, in order to check whether the App Linking configuration is correct. The following is an example.
    
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
    3.  In the **entry/src/main/ets/pages/Index.ets** file, call the [UIAbilityContext.openLink()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to open the app.
        
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
                // Open the app only in App Linking mode.
                context.openLink(link, { appLinkingOnly: true })
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
    
    If the target app is not installed, a system exception is thrown.
    
4.  Install the target app and redirect to the details page of the app based on the deferred link obtained.
