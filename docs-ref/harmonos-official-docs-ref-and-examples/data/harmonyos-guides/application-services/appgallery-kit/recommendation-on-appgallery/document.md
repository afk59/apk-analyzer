# Recommendation on AppGallery

#### Use Cases

-   Adding an atomic service widget to the home screen
    
    You can call the [loadService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section16879449144620) API provided by AppGallery Kit to load a page, on which users can tap the **Add to home screen** button to add an atomic service widget to the home screen.
    

-   Displaying an app details page
    1.  You can call the [loadProduct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section144826162913) API provided by AppGallery Kit to load an app details page on AppGallery. On the details page, users can tap the **INSTALL** button to download and install the app.
    2.  You can use a deep link to display an app details page on AppGallery. By constructing a deep link that redirects users to AppGallery, when the relevant API is called by the target app or when users tap the link on a web page, the details page of the app will be displayed, where users can tap **INSTALL** to download and install the app.
    3.  You can use a link of App Linking to display an app details page on AppGallery. By constructing a link that redirects users to AppGallery, when the relevant API is called by the target app or when users tap the link on a web page, the details page of the app will be displayed, where users can tap **INSTALL** to download and install the app.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/gAUCck8PQhWd1cA_BPwPUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D90E1F16348DC95FCDEC9EA26A67CC222482A62676525CE80C262F36BCCCED2)
        
        You can call the **loadProduct()** API to open AppGallery in an app and download the recommended app. Alternatively, you can use App Linking to open AppGallery on a web page and download the recommended app.
        
-   Adding an app shortcut to the home screen
    1.  You can call the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API provided by AppGallery Kit to check whether a shortcut can be added to the home screen. If so, the authentication result and the result's validity period will be returned.
    2.  After obtaining the authentication result through the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API, you can call the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API provided by AppGallery Kit within the result's validity period to create a shortcut and display a confirmation pop-up for users. The shortcut can be added to the home screen after users confirm the operation.
-   Displaying the app review page
    1.  You can use a deep link to open the app review submission page on AppGallery. By constructing a deep link that redirects users to AppGallery, when the relevant API is called by the target app or when users tap the link on a web page, the app review submission page will be displayed on the details page, where users can rate and comment your app.
    2.  You can use a link of App Linking to open the app review submission page on AppGallery. By constructing a link that redirects users to AppGallery, when the relevant API is called by the target app or when users tap the link on a web page, the app review submission page will be displayed on the details page, where users can rate and comment your app.

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"></td></tr><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%">&nbsp;&nbsp;</td></tr><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p><span><img height="495.050339" originheight="709" originwidth="320" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/bLiUt1ibQtm0YythXd0oFQ/en-us_image_0000002371732737.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=85043A3CAFBFAA6D3B6B010F42EC20E37FC28A3B3D385B6A20BAA4FBD46B4240" title="Click to enlarge" width="223.44"></span></p></td><td class="nocellnorowborder" style="border: none;" valign="top" width="33.33333333333333%"><p><span><img height="489.89020500000004" originheight="1280" originwidth="576" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/tM6_LoYFQp6dwL_LfY1n-w/en-us_image_0000002371732693.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=5C4D5157943EAAB073832EDFE230E7446CA42C47F1EE52BA437193AC29B9DB16" title="Click to enlarge" width="220.44750000000002"></span></p></td><td class="cell-norowborder" style="border: none;" valign="top" width="33.33333333333333%"><p><span><img height="499.209914" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/RdYNG-XkSAmGlU-GI1Zyxw/en-us_image_0000002337734752.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=458094D3F7D4BDCE39F79F33366066C8F10AEE9532F70C7C9172B7B995DA1A4F" title="Click to enlarge" width="225.83400000000003"></span></p></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p><span><img height="487.28274" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/JmTs-0dCQE-dpTLZ9LIXhQ/en-us_image_0000002371652841.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=4E74533BF0018289EA29B01AE8602CF6E9C430C0D28C3A86407457734DB14A4C" title="Click to enlarge" width="220.44750000000002"></span></p></td><td class="row-nocellborder" style="border: none;" valign="top" width="33.33333333333333%"><p><span><img height="489.50716500000004" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/mpzL61fKSrmFFcR67yeZgg/en-us_image_0000002371732729.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062058Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=A0407C13750D60197E30846C9390C29227CAD5B900A5581F4049783591BBDA52" title="Click to enlarge" width="221.44500000000002"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="33.33333333333333%">&nbsp;&nbsp;</td></tr></tbody></table>

#### Service Process

## Adding an Atomic Service Widget to the Home Screen and Displaying an App Details Page

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/4NXpsuMaQ8K9fbTC2j8YIA/en-us_image_0000002337894540.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6FB1AB451917D5C83940F3E090FB9CA954E56B05BDDD0E7BCDAA399AAC0C04D "Click to enlarge")

1.  A user requests to access the app details page.
2.  Your app calls the **loadProduct** API of AppGallery Kit.
3.  The relevant API of AppGallery Kit obtains the passed information and generates a page.
4.  The generated page is displayed to the user.

## Adding an App Shortcut to the Home Screen

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/wrVwLec3RhWUPrAZXvTuSA/en-us_image_0000002337894496.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBD108B01952B2491B9FF05778003740C802890D978871D157BC47436069BA70 "Click to enlarge")

1.  Your app calls the **checkPinShortcutPermitted** API to check whether a shortcut can be added to the home screen.
2.  AppGallery Kit obtains the shortcut information passed by your app and generates a result.
3.  AppGallery Kit returns the result and validity period to your app.
4.  If allowed, your app displays to the user an entry for adding the shortcut.
5.  The user attempts to add the shortcut.
6.  Call the **requestNewPinShortcut** API to request to create a shortcut.
7.  AppGallery Kit loads the shortcut information and displays a pop-up for user confirmation.
8.  The user determines whether to add the shortcut to the home screen.
9.  After the user agrees, AppGallery Kit processes the request.
10.  AppGallery Kit returns the result to your app.

## Displaying an App Review Page Through a Deep Link

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/IMlh2vKHQO2mLT6zPrUDPw/en-us_image_0000002371732681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6A85CB905835D937F4F445F742CC08CC0D139990D2DF0F84F8E04B0566434B0 "Click to enlarge")

1.  A user requests to access the review submission page to rate and comment the app.
2.  The app redirects the user to the review submission page on AppGallery by constructing a deep link.
3.  AppGallery parses the parameters in the deep link and displays the app details page (in full-screen mode).
4.  The app displays the review submission page in a simi-modal or lightweight window.
5.  The app displays the review submission page to the user.

## Displaying an App Review Page Through a Link of App Linking

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/jcqqn6mPTnS5whekiFjT3A/en-us_image_0000002337894532.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD74A2CB51E9692805E72718715BD21543BFF7DB663FB18CAD6BEFA8E7FBC4FC "Click to enlarge")

1.  A user requests to access the review submission page to rate and comment the app.
2.  The app redirects the user to the review submission page on AppGallery by constructing a link of App Linking.
3.  AppGallery parses the parameters in the link of App Linking and displays the app details page (in full-screen mode).
4.  The app displays the review submission page in a simi-modal or lightweight window.
5.  The app displays the review submission page to the user.

#### Restrictions

The Recommendation on AppGallery function does not support the Emulator. Use a real device for debugging. If you use this service in the Emulator, the message "Unable to load content. Tap the screen to retry." will be displayed.

#### API Description

The Recommendation on AppGallery function provides the **loadService**, **loadProduct**, **checkPinShortcutPermitted**, and **requestNewPinShortcut** APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[loadService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section16879449144620)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), want: [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want), callback?: [ServiceViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351)): void

 | 

Loads a page for adding an atomic service widget to the home screen.

 |
| 

[loadProduct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section144826162913)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), want: [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want), callback?: [ProductViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418)): void

 | 

Loads an app details page.

 |
| 

[checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), shortcutId: string, want: [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want), labelResName: string, iconResName: string): Promise<[CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199)\>

 | 

Verifies the home screen shortcut through static resources.

 |
| 

[checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section41029172212)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), shortcutId: string, want: [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want), label: string, foregroundIcon: string, backgroundIcon: string): Promise<[CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199)\>

 | 

Verifies the home screen shortcut through custom resources.

 |
| 

[requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext), tid: string): Promise<void>

 | 

Creates a home screen shortcut.

 |

#### Development Procedure

## Adding an Atomic Service Widget to the Home Screen

1.  Import the **productViewManager** module and related common modules.
    
    import { productViewManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct atomic service widget parameters.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is an object of the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) type. Pass the link for adding an atomic service to the home screen to attributes of the object.
    -   The third parameter is optional and can contain four attributes: [onError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351), [onReceive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351), [onAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351), and [onDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351). [onError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351) is a callback that returns error information when the page for adding an atomic service widget fails to be loaded. [onReceive](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351) is a callback used to receive the result of adding an atomic service widget to the home screen. [onAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351) is a callback which will be called when the page for adding an atomic service widget to the home screen is successfully displayed. [onDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section428319231351) is a callback which will be called when the page for adding an atomic service widget to the home screen is successfully closed.
        
        @Entry
        @Component
        struct LoadServiceView {
          @State message: string = 'Display details page on AppGallery';
        
          build() {
            Row() {
              Column() {
                Button(this.message)
                  .fontSize(24)
                  .fontWeight(FontWeight.Bold)
                  .onClick(() => {
                    const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
                    const wantParam: Want = {
          // Enter the link for adding an atomic service widget to the home screen.
                      uri: 'xxx'
                    }
                    const callback: productViewManager.ServiceViewCallback = {
                      onReceive: (data: productViewManager.ServiceViewReceiveData) => {
                        hilog.info(0x0001, 'TAG', \`loadService onReceive.result is ${data.result}, msg is ${data.msg}, formInfo is ${JSON.stringify(data.formInfo)}\`);
                      },
                      onError: (error: BusinessError) => {
                        hilog.error(0, 'TAG', \`loadService onError.code is ${error.code}, message is ${error.message}\`)
                      },
                      onAppear: () => {
                        hilog.info(0, 'TAG', \`loadService onAppear.\`);
                      },
                      onDisappear: () => {
                        hilog.info(0, 'TAG', \`loadService onDisappear.\`);
                      }
                    }
                  })
              }
              .width('100%')
            }
            .height('100%')
          }
        }
        
    
3.  Call [productViewManager.loadService](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section16879449144620) by passing the parameters constructed in step 2.
    
    // Call **loadService** to load the page for adding an atomic service widget to the home screen.
    productViewManager.loadService(uiContext, wantParam, callback);
    

## Displaying an App Details Page

-   **Method 1: through the loadProduct API**

1.  Import the **productViewManager** module and related common modules.
    
    import { productViewManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct parameters of the app details page.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is an object of the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) type. Two attributes can be passed: **bundleName** (which indicates the name of the app package to be loaded) and **skExposure** (which is of the [SKExposure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1346915243448) type and indicates the registered attribute source information passed to the app attribution service).
    -   The third parameter is optional and can contain three attributes: [onError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418), [onAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418), and [onDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418). [onError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418) is a callback that returns error information when the app details page fails to be loaded. [onAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418) is a callback that is triggered when the app details page is successfully displayed. [onDisappear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1744815172418) is a callback that is triggered when the app details page is closed.
        
        @Entry
        @Component
        struct LoadProductView {
          @State message: string = 'Display details page on AppGallery';
        
          build() {
            Row() {
              Column() {
                Button(this.message)
                  .fontSize(24)
                  .fontWeight(FontWeight.Bold)
                  .onClick(() => {
                    const exposureData: productViewManager.SKExposure = {
                      adTechId: '20\*\*\*\*e8',
                      campaignId: '123456',
                      destinationId: '10\*\*\*\*\*\*',
                      mmpIds: \['2f\*\*\*\*5', '2f7\*\*\*5'\],
                      serviceTag: '123\*\*\*2',
                      nonce: '123\*\*\*2',
                      timestamp: 1705536488,
                      signature: 'MEQCIEQlmZ\*\*\*\*zKBSE8QnhLTIHZZZ\*\*\*\*ZpRqRxHss65Ko\*\*\*\*JgJKjdrWdkL\*\*\*\*juEx2RmFS7da\*\*\*\*ZRVZ8RyMyUXg=='
                    };
                    const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext
                    const wantParam: Want = {
                      parameters: {
            // Mandatory. Enter the name of the app package to be loaded, for example, **com.huawei.hmsapp.books**.
                        bundleName: 'com.xxx',
            // Optional. Registered attribute source information passed to the app attribution service.
                        skExposure: exposureData
                      }
                    }
                    const callback: productViewManager.ProductViewCallback = {
                      onError: (error: BusinessError) => {
                        hilog.error(0, 'TAG',
                          \`loadProduct onError.code is ${error.code}, message is ${error.message}\`)
                      },
                      onAppear: () => {
                        hilog.info(0, 'TAG', \`loadProduct onAppear.\`);
                      },
                      onDisappear: () => {
                        hilog.info(0, 'TAG', \`loadProduct onDisappear.\`);
                      }
                    }
                  })
                  .width('100%')
              }
              .height('100%')
            }
          }
        }
        
    
3.  Call [loadProduct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section144826162913) by passing the parameters constructed in step 2.
    
    // Call **loadProduct** to display the app details page.
    productViewManager.loadProduct(uiContext, wantParam, callback);
    

-   **Method 2: through a deep link**
    
    Construct a deep link by combining the base URL with **bundleName** (package name) of the app whose details page needs to be displayed. The format is as follows:
    
    store://appgallery.huawei.com/app/detail?id= + bundleName
    
    The app calls the [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability-2) method to display the details page of the target app on AppGallery.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common, Want } from '@kit.AbilityKit';
    
    // Display the app details page on AppGallery.
    function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
      let want: Want = {
        action: 'ohos.want.action.appdetail', // Implicitly set **action** to **ohos.want.action.appdetail**.
        uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName, // **bundleName** indicates the name of the app package for which you want to launch the app details page.
      };
      context.startAbility(want).then(() => {
        hilog.info(0x0001, 'TAG', "Succeeded in starting Ability successfully.")
      }).catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG', \`Failed to startAbility.Code: ${error.code}, message is ${error.message}\`);
      });
    }
    
    @Entry
    @Component
    struct StartAppGalleryDetailAbilityView {
      @State message: string = 'Display details page on AppGallery';
    
      build() {
        Row() {
          Column() {
            Button(this.message)
              .fontSize(24)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
                // Set the value of **bundleName**, for example, **com.huawei.hmsapp.books**.
                const bundleName = 'xxxx';
                startAppGalleryDetailAbility(context, bundleName);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
    Use a deep link on a web page to display the details page of an app on AppGallery:
    
    <html lang="en">
      <head>
        <meta charset="UTF-8">
      </head>
      <body>
        <div>
          <button type="button" onclick="openDeepLink()">Display app details page</button>
        </div>
      </body>
    </html>
    <script>
      function openDeepLink() {
        window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx')
      }
    </script>
    

-   **Method 3: through App Linking**
    
    Construct a link of App Linking by combining the base URL with **bundleName** (package name) of the app whose details page needs to be displayed. The format is as follows:
    
    https://appgallery.huawei.com/app/detail?id= + bundleName
    
    The app calls the [openlink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12) API to redirect users to a page specified by the link of App Linking:
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      build() {
        Button('start app linking', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            // Configure different app package names to display details pages of different apps, for example, **bundleName: 'com.huawei.hmsapp.books'**.
            let bundleName: string = 'xxxx';
            let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName;
            // Display the app details page of the specified package name on AppGallery using App Linking as the preferred mode.
            context.openLink(link, { appLinkingOnly: false })
              .then(() => {
                hilog.info(0x0001, 'TAG', 'openlink success.');
              })
              .catch((error: BusinessError) => {
                hilog.error(0x0001, 'TAG', \`openlink failed. Code: ${error.code}, message is ${error.message}\`);
              });
          })
      }
    }
    
    Open a link of App Linking on a web page:
    
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>Redirection example</title>
      </head>
      <body>
        <a href='https://appgallery.huawei.com/app/detail?id=bundleName'>App Linking redirection example</a>
      </body>
    </html>
    

## Adding an App Shortcut to the Home Screen

-   **Method 1: through static resources**

1.  Import the **productViewManager** module and related common modules.
    
    import { productViewManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct parameters for verifying the home screen shortcut through the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is the shortcut ID constructed by the app. The value is a string containing a maximum of 63 bytes.
    -   The third parameter is an object of the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) type. You need to pass **bundleName**, **moduleName**, and **abilityName** of the target app that will be launched after the user taps the shortcut.
    -   The fourth parameter is the label resource index name of the shortcut displayed on the home screen.
    -   The fifth parameter is the icon file resource index name of the shortcut displayed on the home screen.
    
    const uiContext =this.getUIContext().getHostContext() as common.UIAbilityContext;
    const shortcutId = "id\_test1"; // Corresponds to **shortcutId** configured in the **shortcuts** tag, for example, **"shortcutId": "id\_test1"**.
    const labelResName = "shortcut"; // Corresponds to the label resource index name configured in the **shortcuts** tag, for example, **"label": "$string:shortcut"**.
    const iconResName = "aa\_icon"; // Corresponds to the icon resource index name configured in the **shortcuts** tag, for example, **"icon": "$media:aa\_icon"**.
    const want: Want = {            // Corresponds to **want** configured in the **shortcuts** tag.
      bundleName: "com.example.appgallery.kit.demo",
      moduleName: "entry",
      abilityName: "EntryAbility",
      parameters: {
        testKey: "testValue"
      }
    };
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/aNU-BQOoQ0GNNlkOe9k8Jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=592C3C36F5A97E759A1F8D12AC906A3DC8801655B240E5FD4448D2A4E60C40C6)
    
    You need to [create a static app shortcut](../../../getting-started/development-fundamentals/typical-scenarios-development/creating-a-static-shortcut-of-the-application/document.md) in advance, and the second, third, fourth, and fifth parameters should be consistent with the configurations in the [shortcuts](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#shortcuts) tag.
    
    If a verification parameter changes, a new **tid** will be generated each time. Otherwise, the previous **tid** and the remaining time before expiration (specified by **expired**) will be returned.
    
3.  Call the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API by passing parameters constructed in step 2 in sequence, and save the asynchronously returned result [CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199).
    
    try {
      let checkShortcutResult: productViewManager.CheckShortcutResult;
      productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, labelResName, iconResName)
        .then((result: productViewManager.CheckShortcutResult) => {
          hilog.info(0x0001, 'TAG', \`checkPinShortcutPermitted success result is ${JSON.stringify(result)}\`);
          checkShortcutResult = result;
        }).catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG',
          \`checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}\`);
      })
    } catch (err) {
      hilog.error(0x0001, 'TAG', \`checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}\`);
    }
    
4.  Construct parameters for creating a home screen shortcut through the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is the value of the **tid** attribute in [CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199) obtained from step 3.
    
    const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const tid = checkShortcutResult.tid;
    
5.  Call the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API by passing parameters constructed in step 4 in sequence.
    
    try {
      productViewManager.requestNewPinShortcut(uiContext, tid)
        .then(() => {
          hilog.info(0x0001, 'TAG', \`requestNewPinShortcut success.\`);
        }).catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG', \`requestNewPinShortcut error. code is ${error.code}, message is ${error.message}\`);
      })
    } catch (err) {
      hilog.error(0x0001, 'TAG', \`requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/2RM6KDsXQRODhgcotuZnxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F430ECE655C7C38AAC604E7BE139CD5430B5A2015EF1791F3CA9BDE709CCBEC1)
    
    Once a shortcut is successfully added to the home screen, the original **tid** in the verification result will become invalid, and a new **tid** will be generated if the shortcut is added again.
    
    To improve user experience, you are advised to call the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API in advance. After a user taps the button for adding the shortcut to the home screen, call the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API to process the request.
    
    It is not recommended to call these two APIs consecutively to process the request after the user taps the button for adding the shortcut to the home screen.
    

-   **Method 2: through custom resources**

1.  Import the **productViewManager** module and related common modules.
    
    import { productViewManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import type { common, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct parameters for verifying the home screen shortcut through the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is the shortcut ID constructed by the app. The value is a string containing a maximum of 63 bytes.
    -   The third parameter is an object of the [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-want) type. You need to pass **bundleName**, **moduleName**, and **abilityName** of the target app that will be launched after the user taps the shortcut.
    -   The fourth parameter is the shortcut name displayed on the home screen.
    -   The fifth parameter is the sandbox address for the icon of the shortcut displayed on the home screen. The icon must be in PNG or WebP format and should not exceed 100 KB.
    -   The sixth parameter is reserved as an empty string and cannot be used for now.
    
    const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const shortcutId = \`${Date.now()}\`;
    const want: Want = {
      bundleName: "com.example.appgallery.kit.demo",
      moduleName: "entry",
      abilityName: "EntryAbility",
      parameters: {
        testKey: "testValue"
      }
    }
    const label = "shortcut";
    const foregroundIcon = uiContext.filesDir + "/icon.png";
    const backgroundIcon = "";
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/fTg2-tgPRpyTcpKZ89iv0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A326C5ECB65B4F94C41013637700B056BF5FA4D8468FC6D2D084185E7B0C5138)
    
    The sixth parameter **backgroundIcon** is an empty string, as background-layer icons are not currently supported.
    
    If a verification parameter changes, a new **tid** will be generated each time. Otherwise, the previous **tid** and the remaining time before expiration (specified by **expired**) will be returned.
    
3.  Call the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section41029172212) API by passing parameters constructed in step 2 in sequence, and save the asynchronously returned result [CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199).
    
    try {
      let checkShortcutResult: productViewManager.CheckShortcutResult;
      productViewManager.checkPinShortcutPermitted(uiContext, shortcutId, want, label, foregroundIcon, backgroundIcon)
        .then((result: productViewManager.CheckShortcutResult) => {
          hilog.info(0x0001, 'TAG', \`checkPinShortcutPermitted success result is ${JSON.stringify(result)}\`)
          checkShortcutResult = result;
        }).catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG',
          \`checkPinShortcutPermitted error. code is ${error.code}, message is ${error.message}\`);
      })
    } catch (err) {
      hilog.error(0x0001, 'TAG', \`checkPinShortcutPermitted failed, code is ${err.code}, message is ${err.message}\`);
    }
    
4.  Construct parameters for creating a home screen shortcut through the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API.
    
    -   The first parameter is the obtained [UIAbilityContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) of the current page.
    -   The second parameter is the value of the **tid** attribute in [CheckShortcutResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section1548317391199) obtained from step 3.
    
    const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const tid = checkShortcutResult.tid;
    
5.  Call the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API by passing parameters constructed in step 4 in sequence.
    
    try {
      productViewManager.requestNewPinShortcut(uiContext, tid)
        .then(() => {
          hilog.info(0x0001, 'TAG', \`requestNewPinShortcut success.\`);
        }).catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG', \`requestNewPinShortcut error. code is ${error.code}, message is ${error.message}\`);
      })
    } catch (err) {
      hilog.error(0x0001, 'TAG', \`requestNewPinShortcut failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/BeYS1DYhSoeBYoocXrrWNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=221F4CE5F340F7C476A77A5ADCAA28F365CDA91C5AA2E28B57882A97D57D5972)
    
    Once a shortcut is successfully added to the home screen, the original **tid** in the verification result will become invalid, and a new **tid** will be generated if the shortcut is added again.
    
    To improve user experience, you are advised to call the [checkPinShortcutPermitted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section5665513519) API in advance. After a user taps the button for adding the shortcut to the home screen, call the [requestNewPinShortcut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-productviewmanager#section2891132652315) API to process the request.
    
    It is not recommended to call these two APIs consecutively to process the request after the user taps the button for adding the shortcut to the home screen.
    

## Displaying an App Review Page Through a Deep Link

Construct a deep link by combining **bundleName** and **action**. **bundleName** represents the package name of the app for which the review submission page needs to be launched, while **action** should be implicitly set to **write-review**, which indicates that the review submission page will be launched after the details page is displayed. The format is as follows:

store://appgallery.huawei.com/app/detail?id= + bundleName + &action=write-review

The app calls the [startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability) method to display the app review page on AppGallery.

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common, Want } from '@kit.AbilityKit';

// Launch a specified review submission page on AppGallery through a deep link.
function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
  let want: Want = {
    action: 'ohos.want.action.appdetail', // Implicitly set **action** to **ohos.want.action.appdetail**.
    uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review'// **bundleName** indicates the package name of the app for which the review submission page needs to be launched, and **action** should be implicitly set to **write-review**, indicating that the review submission page will be launched after the details page is displayed.
  };
  context.startAbility(want).then(() => {
    hilog.info(0x0001, 'TAG', "Succeeded in starting Ability successfully.")
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, 'TAG', \`Failed to startAbility. Code: ${error.code}, message is ${error.message}\`);
  });
}

@Entry
@Component
struct StartAppGalleryDetailAbilityView {
  @State message: string = 'Launch review submission page on AppGallery through a deep link'

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            // Set the value of **bundleName**, for example, **com.huawei.hmsapp.books**.
            const bundleName = 'xxxx';
            startAppGalleryDetailAbility(context, bundleName);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Use a deep link on a web page to display the review submission page of an app on AppGallery:

<html lang="en">
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
    <div>
      <button type="button" onclick="openDeepLink()">Use deep link to launch review submission page on AppGallery</button>
    </div>
  </body>
</html>
<script>
  function openDeepLink() {
    window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx&action=write-review')
  }
</script>

## Displaying an App Review Page Through a Link of App Linking

Construct a link of App Linking by including **bundleName** and **action**. **bundleName** represents the package name of the app for which the review submission page needs to be launched, while **action** should be implicitly set to **write-review**, which indicates that the review submission page will be launched after the details page is displayed. The format is as follows:

https://appgallery.huawei.com/app/detail?id= + bundleName + &action=write-review

The app calls the relevant API to redirect users to a page specified by the link of App Linking:

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Button('start app linking', { type: ButtonType.Capsule, stateEffect: true })
      .width('87%')
      .height('5%')
      .margin({ bottom: '12vp' })
      .onClick(() => {
        let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
        // Configure different app package names to display review pages of different apps, for example, **bundleName: 'com.huawei.hmsapp.books'**.
        let bundleName: string = 'xxxx';
        let link: string = 'https://appgallery.huawei.com/app/detail?id=' + bundleName + '&action=write-review';
        // Display the app review page of the specified package name on AppGallery using App Linking as the preferred mode.
        context.openLink(link, { appLinkingOnly: false })
          .then(() => {
            hilog.info(0x0001, 'TAG', 'openlink success.');
          })
          .catch((error: BusinessError) => {
            hilog.error(0x0001, 'TAG', \`openlink failed. Code: ${error.code}, message is ${error.message}\`);
          });
      })
  }
}

Open a link of App Linking on a web page:

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Redirection example</title>
  </head>
  <body>
    <a href='https://appgallery.huawei.com/app/detail?id=bundleName&action=write-review'>Launch the review submission page on AppGallery through a link of App Linking.</a>
  </body>
</html>
