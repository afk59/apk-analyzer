# Previewing an ArkTS/JS App/Atomic Service

The Previewer supports both live preview and dynamic preview for apps/atomic services developed in ArkTS or JS.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/bIiNCgXnRgqniGM553pi_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FC2250A4BA123DC7539308FFF2D01D14576D3347C52FC8EA2D2D8676D0368F4)

-   The Previewer supports ArkTS projects for Phone, Tablet, 2in1, Car, Wearable, and TV devices, as well as JS projects for LiteWearable and Wearable devices.
-   Before using the Previewer, make sure the OpenGL version on your computer is 3.2 or later.
-   The ability lifecycle does not run during previews.
-   Since DevEco Studio 6.0.0 Beta3 onwards, previews are available when HAPs/HSPs reference HSPs, but not when HARs reference HSPs. Preview them directly within the HSPs or [set the mock implementation](../mocking-preview-data/document.md) for the HSPs.
-   During previews, files in the **resources** directory cannot be accessed with a relative or absolute path.
-   Components cannot be dragged on the preview canvas.
-   Previews are not available for APIs of certain modules, such as **Ability**, **App**, and **MultiMedia**.
-   Previews are not available for the following components: **RichText**, **Web**, **Video**, and **XComponent**.
-   Calling the C++ library is not supported.
-   The Previewer does not show any menu bar for a HAR, regardless of whether it is used in an app or an atomic service. However, on a real device, a menu bar is shown for the HAR in an atomic service. Keep in mind this difference when you are developing a HAR.

-   **Live preview**: During UI code development, if you add or delete UI components, the Previewer will refresh the layout and display the effect immediately after you have saved the changes by pressing **Ctrl+S**. If you modify the attributes of a component, the Previewer refreshes the layout and displays the effect in subseconds. (This feature is available for ArkTS components.) Data binding is supported in certain cases, for example, where the variable is decorated by @State. The live preview feature is enabled by default. If you do not need it, disable it by clicking the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/YCVtRV_SQAmv82Ks-YLfxg/en-us_image_0000002501070040.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F73A7200301FC6A78605026538858B03FDD6431CA1F1F01FC935CE80D1815566) button in the upper right corner of the Previewer.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-WephvZJTymUxNA2apnyzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8C4EFCBEF98E4738192E26FCE758E3C489D2229EE82F6DDDAB55285646AC11E)
    
    Live previews are not available for changes made to a configuration file (for example, **main\_pages.json** or **form\_config.json**) under **resources/base/profile**. To see the results of these changes, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/7nUa3fI5TfOthegcHpbVRg/en-us_image_0000002532750065.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C57BD997D76122EF3E1F04ACA49DE5734A21568CB92526690F81F78CF25A0E4).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/TI9BIKpwQdi03wzqZZEc4g/en-us_image_0000002500910196.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00DC71E0C22EDE5444341F97F3DFA04A8F6A56021DE7AF49C8BB6A6BA1B3E437 "Click to enlarge")
    
-   **Dynamic preview**: In the Previewer, you can interact with your app/atomic service UI just as you would on a real device, including touching, navigating through pages, and swiping.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/KsBWHsZPSXqlA8Gn5Qceng/en-us_image_0000002501070044.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC74388E1C57F991EF78810685D3EA7A21BD4DF4E2E3A10928B5470C5F258F2D "Click to enlarge")
    

In this example, an ArkTS app/atomic service is being previewed.

1.  Create or open an ArkTS app/atomic service project. In this example, a local ArkTS demo project is being opened.
2.  In the project directory, open any .ets file (.hml/.css/.js file for a JS project).
3.  You can open the Previewer in either of the following ways:
    
    -   On the menu bar, choose **View** > **Tool Windows** > **Previewer**.
    -   On the toolbar in the upper right corner of the editing window, click **Previewer**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/0HEDaLhFTQOWxO_eonEVqQ/en-us_image_0000002532750067.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95DCF1A6073415109FA02E7899F10CE16DAB78CAEE2CFD82CA3971E9DB8036C0 "Click to enlarge")
    
4.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Ai-hid07TL2dVDwQYSLshg/en-us_image_0000002500910200.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E735327AE561540DE7FBB783F3830D235AF2CDA6963C84A268FCDF0D02342B19) to stop the preview.
