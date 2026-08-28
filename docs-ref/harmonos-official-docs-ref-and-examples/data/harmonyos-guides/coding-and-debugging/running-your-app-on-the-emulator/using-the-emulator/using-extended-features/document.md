# Using Extended Features

#### Battery Emulation

You can emulate different battery states on an emulator. On the extensions menu bar, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/OZKnIvV6TXC-lN3qfVr3xg/en-us_image_0000002532668783.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=557A84441CCB5B19082ADD8EFBBA75AC9CD5E993440D96404FBB137126E57441) to open the battery emulation page. On this page, you can manually enter a value or drag the slider to change the battery percentage. You can also click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/qWIolXuMRa2zD714MrCVCA/en-us_image_0000002501068730.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=309E9D2B6687675318E50D8011B2A4BFFB4C148EB695673D117E1CE4C31A9516) to switch the battery between charging and discharging states. The battery has the following three charging states:

-   ENABLE: The charging option is enabled. In this state, the battery is being charged and not fully charged.
-   NONE: The charging option is disabled. In this state, charging stops.
-   FULL: The charging option is enabled, and the battery level is 100% (fully charged).

In the app, you can query the remaining battery level and charging state of the emulator through the [@ohos.batteryInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-battery-info) module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/547lixSUQe6_kOepJAZeiw/en-us_image_0000002500908904.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50BB12E615311D2F795101BCBC6B8176D342F28323987E24F1CA5B8593CE615A "Click to enlarge")

#### GPS Positioning

The emulator supports the device location emulation. You can open the extensions menu and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/pZJi4AGPSJGZ45goLHuvLA/en-us_image_0000002532668777.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5306FF586B1DF36848E75EFE20C44669D1F15C312F728A63AF3FB78D213B693) to set the location. The emulator supports the following modes:

-   **Manual**: On this tab, you can manually enter the longitude, latitude, altitude, and azimuth of a location, or click the drop-down list box of **City** to select the target city.
-   **Replay**: On this tab, you can import continuous location information within a period of time. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/qdwV6KtuRuKvbnqYhrWqcQ/en-us_image_0000002532668807.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=400E3FE23288856ABBE6EBB09EBB608F359B7D775EDBB5DE3855EE88416342FC) to import a local GPX file, and then click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ebDlANhJR2qNhAlYQr7MvA/en-us_image_0000002532668771.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53467509FD3195EB3AB633033593214F45F925B083D78CE3EAA936FBF3696303) to start emulating the track in the GPX file. In addition, you can select different replay rates to change the moving speed.
-   **Scenario**: On this tab, you can use the preset GPX files if no local GPX file is available. Preset GPX files provided in the emulator cover the following scenarios: outdoor running, outdoor cycling, and driving navigation. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/SwFv1UwsRl-PIW7YLIIckQ/en-us_image_0000002532668797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDF11B21660EB0543FBE53871E3E59C7C1ABD54B023EA74EF57B8B2B9B83C7A6) to start track emulation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/eOU9625VQpi9XuHBUrd9bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4EB5EA293D3676810CCEF5A5D35BC197B7A0895AF33A7601F297B32198115E9)
    
    Currently, scenario simulation is supported only in the Chinese mainland.
    

In the app, you can obtain the location information of the emulator through the [@ohos.geoLocationManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager) module.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/LU5iUnzRTIe5EXDdHDUCCQ/en-us_image_0000002501068726.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DA043F98755CC2767B9619FA979F601E621634F21EF782F96CAED7CCBFD1183 "Click to enlarge")

#### Virtual Sensor

The emulator provides virtual sensors to emulate the capabilities of hardware sensors. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/sW-ny3dRTKCFNQK0nMFtkg/en-us_image_0000002500908874.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A5FDCB6B7632C2C71055B199AC34062D4D0EFEF8111566074D8B803FB9DD8E8) on the extension menu to open the **Activate Virtual sensor emulation** page. On this page, you can adjust different sensors to test your app and use the [@ohos.sensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-sensor) module to monitor changes of sensor values. The emulator provides the following virtual sensors:

-   Pedometer sensor: Measures step count. Corresponding sensor ID: **PEDOMETER**.
-   Ambient temperature sensor: Measures ambient temperature. Corresponding sensor ID: **AMBIENT\_TEMPERATURE**.
-   Humidity sensor: Measures humidity levels. Corresponding sensor ID: **HUMIDITY**.
-   Ambient light sensor: Measures light intensity. Corresponding sensor ID: **AMBIENT\_LIGHT**.

You can adjust values by dragging the sliders or entering them directly into the text boxes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/n7nP8f4GS6qyphGuRzpe_A/en-us_image_0000002500908890.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D24DD23E2D3C9F8D8E1C0E808C593FC2DB9132BCE183A4CC8737338CD25583E)

#### Network Proxy

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Fr7MI4ZNQLao9CbqL7V-NQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=201D4C3BA46FC3159E10AB04D65BF97DDAF91E9259328B8A8A53943E3E759D23)

Currently, this feature is available only in the Chinese mainland.

The emulator can proxy network requests to a proxy server, which then forwards requests to the target server. In this way, the following development scenarios are met:

-   You are on the intranet and want to access the Internet by setting a proxy.
-   You have configured the network proxy in DevEco Studio and want to avoid reconfiguring it in the emulator.
-   You need to proxy network requests to third-party packet capture tools for easy request information viewing.

You can open the extension menu and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/0XFy7vVkTq6RC0UVmt7s9w/en-us_image_0000002501068714.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DCC72E634CF9C59A3E00269A976348B5B6955267E7042968DE28BAD86EDD91B) to configure the proxy. The emulator provides the following proxy modes:

-   **Use DevEco Studio Proxy**: Reads and applies the network proxy configuration from DevEco Studio. The configuration is located in **DevEco Studio** > **Preferences**/**Settings** (**File** > **Settings** on Windows) > **Appearance & Behavior** > **System Settings** > **HTTP Proxy** (the emulator does not support the **no proxy for** option under **HTTP Proxy**). No repeated configuration is required in the emulator. Meanwhile, the emulator listens for changes to the proxy configuration in DevEco Studio to synchronize the proxy settings. If DevEco Studio uses automatic proxy mode or SOCKS proxy, the emulator does not support it and will switch to the **No proxy** mode.
-   **No proxy**: Does not use a proxy. Network requests are sent directly to the target server.
-   **Manual proxy configuration**: Requires you to configure the proxy server information to proxy network requests to the proxy server.

You need to click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Cf_IqEdaTDqDObppGUxAbg/en-us_image_0000002532748747.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B8EE657403D39125D6B746B2469383E9800B7FCE5FF4BC3099BFECDFF368132) for the above proxy configuration to take effect. You can also click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/1DUTdkDcRta8BKp5VniCXA/en-us_image_0000002532748753.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62F52CD460495668390D3AB08FF50E3B840F53B1F784B0C532A9EDCBAB5497DD) to verify the current proxy configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/tvUc0Vu4SYejZNLKws1HEQ/en-us_image_0000002501068738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22A15E21E3B7438C858E561BC01B74713D2CBC9F1D2083E78306D117BCC6B5C0 "Click to enlarge")

#### Shake

The emulator can emulate the Shake operation performed by the user on the device. Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/3eQXL_AmTvGl-qJWQcFuxA/en-us_image_0000002501068718.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CAD290D7F03E02A44CA88CBBCCC415676867F5EC3C933540CD6B66CAF535124) on the toolbar to emulate a 1-second shake. Your app can listen for changes in the accelerometer via the [@ohos.sensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-sensor) module. When the change in acceleration reaches the preset threshold, the service logic for the Shake feature is triggered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/mDIT_t74T5-x48mK39S0iA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=751590F8AE7EF26F92B7265EC7B5F55C7C039B52418D3B8CC0AB370F527C4DDF)

Currently, Shake is available only on phones and tablets.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Xq1IGSh0T8GHY7oyhJG52g/en-us_image_0000002501068744.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=653E14E25AE79625BEECB922F7349AB788FF24B8B9D40514FDBFF2A4D64F4DB0 "Click to enlarge")

#### Audio Input

Currently, the Emulator supports only the audio input capability provided by Audio Kit. You can use the microphone on the local computer to transmit audio data to the emulator. Procedure:

1.  Ensure that the local computer is connected to a microphone.
2.  Have your app call the APIs (such as **AudioCapturer** and **OHAudio**) provided by Audio Kit to start receiving audio data.
3.  Use the local microphone for audio input.

When the app on the emulator calls related APIs, the audio stream information in the following table is recommended to ensure clear and smooth audio quality.

| 
Audio Stream Information

 | 

Recommended Configuration

 |
| :-- | :-- |
| 

samplingRate

 | 

48000 Hz

 |
| 

channels

 | 

2

 |
| 

sampleFormat

 | 

Signed 16-bit integer

 |
| 

encodingType

 | 

PCM encoding

 |

#### Camera

Since DevEco Studio 5.1.0 Release, the Emulator supports the preview and photo-taking capabilities provided by Camera Kit. You can use the camera on the local computer to implement photo-taking and preview functionalities in the emulator.

1.  Ensure that your computer has an available local camera (excluding those connected via USB).
2.  The app calls the API provided by Camera Kit to display the shooting screen and take photos via the computer's camera.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/jEidrJACRl2AYGKeiamAvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F7BF6C00939AB138B66EEF8B202C69FE0C7B9ED391B4D715CED48CE2EFA56E0)
    
    When developing camera functionalities using the emulator, use the following [camera configuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#profile): RGBA\_8888 format and 1280 × 720 resolution.
    

#### Crown

The wearable emulator can emulate the crown functionalities.

-   Clicking the crown with the mouse: navigates to the watch face or home screen based on the current page.
-   Double-clicking the crown with the mouse: accesses the multitasking management page.
-   Scrolling the mouse wheel on the screen: emulates the crown rotation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/frtseRfORN6FSaXFkuiaig/en-us_image_0000002532668803.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE71420BDB02E3B09FBBB64F2B1C50248C8A9A9971FA209C7809084303D65956 "Click to enlarge")
