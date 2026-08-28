# Running a Lite Wearable App via the Simulator

The Simulator provided by DevEco Studio can run and debug HarmonyOS apps on lite wearables, supporting both signed and unsigned HAPs.

#### Procedure

1.  Select **Huawei Lite Wearable Simulator** from the device dropdown in the upper-right corner of DevEco Studio.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/SYbw5SWPTPif40FRN6YUGA/en-us_image_0000002532669953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90F24B3A67C5933F6AC82BC79C896E9B395AC75CFF1B533821BEB2CF0F1D4942)
    
2.  Click **Run** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/HE4PWowBQfi_GGW2-Vxbvg/en-us_image_0000002501069892.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA47482971725C82A7FC8D8434FEED84F7EE6BFAEAE19E33D879D877494911E0) or **Debug** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/A_Ttr6ZbRK2NYe3uA0vZBg/en-us_image_0000002500910044.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=904E7AEA8FCF9BA9E395E7E6059DCEF8521384A5409687D42B3B4F9B785F2410). In the dialog box displayed, set the device shape and resolution, and click **OK** to run or debug the app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/tzjZ-GoATYSWTX9yhy02aQ/en-us_image_0000002501069878.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64360677BEA0C9C9820D24A34CAC635524824D88B5709F5BC1C52BAFB7E217D2 "Click to enlarge")
    
3.  DevEco Studio begins compilation, building, and installation. Upon completion, the app can run on the Simulator.

#### Supported Features

In the Simulator screen, click **More** above the device to expand additional features.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/4mFOq8KISFOJbq_gPJf7MA/en-us_image_0000002532669959.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06E529DF5C6D989EC496FC5D015C60281E00967492D383820486A8D961E78F6B)

## Screen

-   **Turn screen on**: Controls the screen on/off.
-   **Keep screen on**: Controls whether the screen remains on. When disabled, the screen will automatically turn off after the timeout period, and the **Turn screen on** switch will also be disabled. After turning the screen on, you must enable **Keep screen on** to keep the screen awake.
-   **Brightness adjustment mode**: Adjusts the screen brightness.
    -   **Manual**: Adjust by dragging the slider or entering a brightness value.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/OtGpRjlUSRSFhPfSog1ciw/en-us_image_0000002532669969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0272D957FFB84900C67B5B97B74638FC58F1A07869F02BC42C3DE63251FE69BC)
        
    -   **Automatic**: Adjust automatically.
-   **Resolution**: Adjusting resolution is not supported in run or debug mode. To change it, stop the current session and select a new resolution by following the [operation steps](#section1332819367496).

## Sensor

The Simulator provides virtual sensors to emulate hardware capabilities. On this page, you can adjust various sensors to test your app. Use the [@system.sensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-sensor) module to listen for changes in sensor values and the [@system.geolocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-location) module to listen for geographic location changes. The following virtual sensors are available:

-   **On-body status**: indicates whether the device is being worn.
-   **Barometer**: Measures the ambient air pressure in Pascals (Pa).
-   **Heart rate**: Measures the user's heart rate. Adjust the value by dragging the slider or entering it directly.
-   **Step count**: Tracks the number of walking steps. Adjust the value by dragging the slider or entering it directly.
-   **Geographic location**: Simulates the device's geographical position by allowing you to input longitude and latitude.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/K0Gd8YReQK2YkW7BN9fGPw/en-us_image_0000002501069888.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D49A2A9186529FCE766CD36EFBEE1A6B1F15B614FDB7BBC4DDEDD86B7F24651)

## Battery

The Simulator allows you to simulate different battery states, including three charging states. You can also change the battery level manually by entering a value or dragging the slider. In your app, use the [@system.battery](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-battery) module to query the simulated device's battery level and charging state.

-   **Not charging**
-   **Charging**
-   **Wireless charging**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/fCjHpxEZTBavTDJum0HI8Q/en-us_image_0000002532669957.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=807CCF6246056F8FCFBC6DD631C6A348922A28EFE98977EAF409742C3F4F89D9)

## Device Settings

You can change the device's language and region. This is only supported in run mode, not in debug mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/I7bSgIMdScWwdmrO9ywsgw/en-us_image_0000002501069882.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC594FB0CB6DB42257E33CAE49ED5A8A8FEA1148EACDCCF4F35B2D5F62853DE8)

## Debugging

-   **Screen coordinate system**: When enabled, moving the cursor over the watch face will display the screen coordinates.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/HEkCn2EORWWJsoElVa0whA/en-us_image_0000002532749919.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18FC73BD4F3BD9CF30F34D9D163687F693ED9B071C04B17E1DFC11932D483D25 "Click to enlarge")
    
-   **Show device mask**: When disabled, the color of the crown around the watch face fades.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/EQUZf5rsSwyDNLdnoLWd4g/en-us_image_0000002532669961.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B52A79AF34725E93450EAEAABA68BC252EC7F00798AA34050D958A991CB2B97 "Click to enlarge")
