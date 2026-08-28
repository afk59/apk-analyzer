# Testing Solution

Intents Kit allows you to perform testing on real devices. After completing code development, you can test a function on a HarmonyOS NEXT device before officially launching the function on AppGallery, laying a foundation for function optimization. Real-device testing consists of three steps: providing basic information, preparing an environment, and conducting joint debugging and verification.

#### Providing Basic Information

To conduct testing, send an email to **hagservice@huawei.com** or contact Huawei's Intents Kit representative, providing the information about the app to be tested to Huawei.

| 
**No.**

 | 

**Basic Information**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

1

 | 

App name

 | 

Name of the app to be released on AppGallery.

 |
| 

2

 | 

App package name

 | 

Package name of the app to be released on AppGallery.

 |
| 

3

 | 

Intent name

 | 

Name of the intent you want to integrate. Provide the name in both Chinese and English.

 |
| 

4

 | 

App icon

 | 

App icon. The requirements are as follows:

Background of the icon: non-transparent

Aspect ratio and dimensions: 1:1 and 72 x 72 px

Maximum size: 1 MB

Format: PNG, JPG, or JPEG

 |
| 

5

 | 

App ID

 | 

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/), click **Development and services**, select the target project, go to **Project settings**, and obtain the app ID in the **App information** area on the **General information** tab page.

 |
| 

6

 | 

Client ID

 | 

Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/), click **Development and services**, select the target project, go to **Project settings**, and obtain the client ID next to **OAuth 2.0 client ID** in the **App information** area on the **General information** tab page.

 |
| 

7

 | 

HUAWEI ID (UID)

 | 

Obtain the UID by referring to [Appendix A: How to Obtain the UID of a HUAWEI ID](../../appendix-a-how-to-obtain-the-uid-of-a-huawei-id/document.md).

 |

#### Preparing an Environment

Prepare a mobile phone running HarmonyOS NEXT whose version must be Developer Beta 3 or later. Then perform the following operations in sequence:

1.  Ensure that the device is connected to the network and the device time is the same as the actual Beijing time.
2.  Tap the Celia Suggestions widget on the home screen. Before you tap it, the widget displays "Welcome to Celia Suggestions". Tap the widget to open Celia's privacy agreement page and agree to the privacy agreement. If you have agreed to the Celia privacy agreement, skip this step.
    
3.  Enable the developer debug mode: Go to **Settings**, tap the device model, tap the software version for seven consecutive times on the **About** screen, and tap **Enable** when the "Enable Developer options?" message is displayed.
    
4.  Press and hold the power button to wake up Celia and drag Celia from half-screen mode to full-screen mode. Tap the icon in the upper left corner to return to the previous screen and tap the avatar in the upper right corner. On the **My settings** screen, select **Settings** > **Network settings**. On the **Network settings** screen displayed, enable **Automatic updates**.
    
5.  Scroll down on the screen displayed in the previous step, tap **Personalized recommendations**, and enable **Personalized recommendations** on the screen displayed.
    
6.  Go to **Settings** > **System** > **Developer options** > **InsightIntent debugging**, and enable **InsightIntent debugging** on the screen displayed. If **On** is displayed below **Actual device model** and the package name of the test app is displayed below **Supported test apps**, you have successfully switched to the real device mode.
    
    Tip: If after **InsightIntent debugging** is enabled, the device does not show **On** below **Actual device model** for a long time or shows **On** below **Actual device model** but without a package name, you can try the following steps:
    
    1.  Sign out of your HUAWEI ID, sign in again, and enable **InsightIntent debugging** again.
    2.  Tap the avatar in the upper right corner of Celia Chat, go to **Settings** > **Manage service** > **Deactivate service**, and tap **Deactivate service**. Then return to the home screen and tap the Celia Suggestions widget again. The widget showing "Welcome to Celia Suggestions" will be refreshed to one with service recommendations. Finally, enable **InsightIntent debugging** again.
7.  After all the preceding steps are complete, start joint debugging.

#### Conducting Joint Debugging and Verification

1.  Intent sharing: Verify that you can successfully trigger intent sharing in the test app. This involves triggering the [shareIntent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-arkts-api-insightintent#section144826162913) API call through operations within the test app and ensuring that the intent sharing is successful.
    
    \[Example\] A music app integrates the music resume feature of Intents Kit. When a user plays a song, the music app will call the system API [shareIntent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-arkts-api-insightintent#section144826162913). The music app developer can confirm through logs that the [shareIntent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/intents-arkts-api-insightintent#section144826162913) API call was successful, indicating successful intent sharing for the music app.
    
2.  Widget rendering: Tap any service in the Celia Suggestions widget on the home screen and return to the home screen. This operation will force the Celia Suggestions widget to refresh. After the refresh, the template widget created using the intent data shared in the previous step will be displayed. You can refer to the scenario description document for the specific style of the feature-specific widget.
    
    \[Suggestion\] Repeat the steps of intent sharing and widget rendering can trigger the refresh of text and image elements on the widget.
    
3.  Intent call: Tap the template widget in the Celia Suggestions widget. If the target page of the test app is displayed, the intent call process is correct.
    1.  Tip: During the verification of an intent call, both cold start and warm start scenarios of the test app should be verified. The final target page in both scenarios should be consistent with the expected page.
    2.  If the widget is not rendered properly, you can perform the following steps to display the widget:
        1.  Ensure that you have enabled the personalized recommendation function by referring to [5](#li11955153025619) and enabled Intents Kit debugging by referring to [6](#li1467622075715). Then render the widget.
        2.  Re-trigger intent sharing, and after the API returns **success**, reconnect the charging cable, turn off the phone screen, wait for 8 minutes, and then re-execute the widget rendering step.

#### Habit-based Recommendation Combing Both the Device Side and the Cloud Side

If your development involves habit-based recommendations combined with cloud searches, prioritize joint debugging of habit-based recommendations on the device to ensure that the logic for intent sharing and calls in the test app is correct. After completing the backend API development, you need to verify that the output parameters meet the cloud-side API specifications of Intents Kit. Once these steps are completed, you can contact Huawei's Intents Kit team and provide your backend API documentation. Huawei personnel will assist you with the joint debugging.
