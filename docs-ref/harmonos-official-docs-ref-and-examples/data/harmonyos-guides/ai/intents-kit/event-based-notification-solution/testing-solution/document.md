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

1.  Event sharing: You can sign in to your app to [obtain the SID provided by the cloud-side event](../integration-solution/document.md#section2151759161514), trigger event push, and synchronize the event content to Huawei Cloud. For details, please refer to [Integration Solution](../integration-solution/document.md).
    
    Example: A travel app integrates the flight reminder feature of Intents Kit. When a user purchases a ticket through the app, this action triggers your cloud to call the **service-events/notify** API (https://insightintent-simenv.cloud.huawei.com/open-ability/v2/service-events/notify). If the API successfully pushes the user's flight event to Huawei Cloud, it indicates a successful response.
    
2.  Widget rendering: Tap any service in the Celia Suggestions widget on the home screen and return to the home screen. This operation will force the Celia Suggestions widget to refresh through the cloud. The conditions for widget rendering are adjusted based on the event's effective time. For specific widget rendering conditions and styles, please refer to the scenario description document for the specific feature (provided by Huawei after you have determined the feature you want to develop).
    
    Example: Flight reminders are triggered 24 hours prior to departure. For a flight scheduled for 20:00 on August 15, data becomes accessible at 20:00 on August 14.
    
3.  Intent call: Tap the template widget in the Celia Suggestions widget. If the target page of the test app is displayed in both cold start and warm start modes, the intent call process is correct.
    
    Example: Tapping the template widget in the Celia Suggestions widget will a user navigate to the ticket purchase details page.
