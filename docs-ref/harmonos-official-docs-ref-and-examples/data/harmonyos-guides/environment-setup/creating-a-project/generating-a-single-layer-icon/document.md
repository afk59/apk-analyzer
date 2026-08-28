# Generating a Single-Layer Icon

With the Image Asset feature on DevEco Studio, you can generate device- and screen density–specific icons and easily locate these icons in the directories.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/KmfjIoaCSd64ukgZ5Bb2lQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06AF536F253FA79BFAB80B49065D84DB2E85BB344771405C5487D0CEA0715439)

Currently, the Image Asset feature can be used to generate single-layer icons for phone, tablet, and 2-in-1 device apps.

Two types of icons can be generated with Image Asset:

-   **Icon**: app icon displayed on the home screen and **Settings** screen.
-   **Start window icon**: icon on the startup screen.

1.  Right-click a module or file in the project directory and choose **New** > **Image Asset** from the shortcut menu to access the icon configuration page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/C5YNV2_4SpuSrtM_beOwVg/en-us_image_0000002532669847.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=380397170222B60B8DAB4329E53F2894EC3D4BB2ABD4FFB2808A3F840A762103 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/nz1A-JA_RDGBujpNbhcnwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D4747EE06435BEC842A20A881457096D9EC353B3647387105A994475F6FA006)
    
    If you use Image Asset in a module-level directory (entry or other modules), icons of the **Icon and start window icon** type are generated. These can be used to configure the **icon** and **startWindowIcon** fields in the **module.json5** file. If you use Image Asset in a project-level directory (such as **AppScope**), only an icon of the **Icon** type is generated, which can be used to configure the **icon** field in the **app.json5** file.
    
2.  Follow the onscreen instructions to set the fields.
    
    -   **Device**: type of device on which the icon takes effect.
    -   **Icon Type**: icon type.
    -   **Name**: icon name. The name can contain a maximum of 128 characters, including letters, digits, and underscores (\_).
    -   **Foreground Layer**: foreground of the icon. It includes the following options:
        -   **Path**: path to the foreground image. To ensure the icon clarity, use images with the size of 1024 px × 1024 px.
        -   **Trim**: whether to adjust the spacing between the icon image and the borders and to remove the redundant transparent area around the image.
        -   **Resize**: scale factor of the image.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/1IuMbGjzTfi6K1NKEzA7OA/en-us_image_0000002532669851.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F814D7C2DD48CEC5A79588A02D355C8CCB6F3E84C8E253C2C5DA3121B31B205)
    
    -   **Background Layer**: background of the icon. It includes the following options:
        -   **Asset Type**: type of the background. Available options are **Color** and **Image**.
        -   **Color**: color of the background.
        -   **Path**: path to the background image. To ensure the icon clarity, use images with the size of 1024 px × 1024 px.
        -   **Trim**: whether to adjust the spacing between the icon image and the borders and to remove the redundant transparent area around the image.
        -   **Resize**: scale factor of the image.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ZmsjD1j6T6W2aBek8yWAqQ/en-us_image_0000002501069784.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=095B8F75334232BA3FC6B77F5C5F86B4EFCE57C9613E691C684ECC0B0627C003)
    
3.  Click **Next** to confirm the save path and size information. By default, the icon is saved to the **resources** directory. Once you have confirmed the settings, click **Finish** to generate the icon.
    
    **icon.png** is the icon displayed on the home screen, and **icon\_start window.png** is the icon displayed on the splash screen. **Size** specifies the icon dimensions. The correspondence between each size designation and its target device DPI range is as follows:
    
    -   **sdpi**: small-scale dots per inch (SDPI), applicable for devices with a DPI range of (0, 120\].
    -   **mdpi**: medium-scale dots per inch (MDPI), applicable for devices with a DPI range of (120, 160\].
    -   **ldpi**: large-scale dots per inch (LDPI), applicable for devices with a DPI range of (160, 240\].
    -   **xldpi**: extra-large-scale dots per inch (XLDPI), applicable for devices with a DPI range of (240, 320\].
    -   **xxldpi**: extra-extra-large-scale dots per inch (XXLDPI), applicable for devices with a DPI range of (320, 480\].
    -   **xxxldpi**: extra-extra-extra-large-scale dots per inch (XXXLDPI), applicable for devices with a DPI range of (480, 640\].
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/dEDOyJQiTIugSYUtOLljqA/en-us_image_0000002501069786.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=064C9BFEDD1B36183E047BA95108E7F1842753C03AFA510AC08ABA6954E77DC7)
    
4.  To use the new icon as the app icon displayed on the home screen or **Settings** screen, set the **icon** field in the **module.json5** file to the new icon name. To use the new icon as the icon for the startup screen, set the **startWindowIcon** field in the same file to the new icon name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/lTbvLUc2QLiagWWeOBxzSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54CD437FE69FF20D418E86DAE9276B9500E6752ACBF0C2651F162FA56F75C33F)
    
    -   Once the preceding fields are updated, the system will preferentially search for resources from the matching qualifier directories, namely, the different size icon files generated in step [3](#en-us_topic_0000002166648820_li094548151616), based on the current device state. For details, see [Matching Resources](../../../getting-started/resource-categories-and-access/document.md).
    -   If the **icon** field is not configured in the **module.json5** file, the system uses the icon configured in the **icon** field in the **app.json5** file.
