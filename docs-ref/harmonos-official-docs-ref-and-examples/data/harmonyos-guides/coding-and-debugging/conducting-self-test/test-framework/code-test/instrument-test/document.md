# Instrument Test

#### Creating an ArkTS Test Case

## Creating a Default Test Case

1.  Open the .ets file of the HAP, HAR, or HSP module to be tested in the project directory, move the cursor to any position in the code, and then right-click the code and choose **Show Context Actions** > **Create Instrument Test**, or press **Alt+Enter** (**Option+Enter** on macOS) and click **Create Instrument Test** in the dialog box displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/du_yFmRCRV-M9SrRLhJsNA/en-us_image_0000002532750253.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7161FAB2198D51FDB6144C7503D2ECF9D0C79DC7BA2C3FB744E129FFCC6FC11)
    
2.  In the **Create Instrument Test** dialog box, set the following parameters:
    
    -   **Testing library**: test type. The default value is **DECC-ArkTSUnit** for an ArkTS project and **DECC-JSUnit** for a JS project.
    -   **ArkTS name**: name of the created test file, which contains test cases. The test file name must be unique in the project directory, and allows only letters, digits, underscores (\_), and dots (.).
    -   **Destination package**: location where the test file is stored. You are advised to store it in the **test** directory of the module to be tested.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/FdAxCCruSNOM_mCI_IpvQQ/en-us_image_0000002532750239.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D621DAC4965CAD97CC700233E38822E79F179CD79C49AEC3030C9612DA04700E)
    
3.  DevEco Studio automatically generates the corresponding test class in the **ohosTest/ets/test** directory. In the test class, DevEco Studio generates the case template of the corresponding method. You need to develop the specific test code based on the service logic. For details, see [arkXtest User Guide](../../../../../system/debugging-tools/test-kit/automated-test-framework-user-guides/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/7W-tfU98TUiDmgh9QthHzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C690CB50502D2AFBDEAE286EF03FEFB94122AFD01C5ECAC3A18A6D85ADD1FC8)
    
    -   You can also manually create a test case under **ohosTest\\ets\\test** and add the corresponding test class to the **List.test.ets** file. All the files in the **ohosTest\\ets\\test** directory must end with **.test.ets**. Otherwise, "Error: Test files must end with '.test.ets'." will be displayed when the files are executed. If this occurs, click **Fix**. DevEco Studio automatically corrects the file names in the directory.
    -   If it is your first time to run UiTest on a HarmonyOS device, run the **hdc -n shell param set persist.ace.testmode.enabled 1** command to enable UiTest capabilities.
    

## Defining Custom Ability and Resources

Since 5.0.3.403, the **ohosTest** directory in newly created projects and modules no longer includes the **testability**, **testrunner**, and resources directories by default. (These directories are retained in existing projects.) If new projects require the use of abilities or resources, you need to create them manually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/ynYquEHBThO1-g_s68ogKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=431FA2BDC4161F0E6CDC68AF274E267EC426088360197E6257B792572F4DB585)

To use ability capabilities, you must also create the **testrunner** directory and the **OpenHarmonyTestRunner.ets** file.

<table id="table988904811377" style="border-style: none;"><caption><b>Table 1 </b><strong>Comparison of the ohosTest directory between new and old versions</strong></caption><tbody><tr id="EN-US_TOPIC_0000002501069634__row988912488371"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002501069634__p1788911489371"><strong>New version</strong></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002501069634__p178891248123711"><strong>Old version</strong></p></td></tr><tr id="EN-US_TOPIC_0000002501069634__row118891748203717"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002501069634__p28898483379"><span><img originheight="182" originwidth="208" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/CeEg_WBpTGG913rwegRdmQ/en-us_image_0000002500910384.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=F081D940872C7D356535FCC39F953E9A0E279758AB51B4A1EC73B4B5C4835A18"></span></p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002501069634__p1788919487371"><span><img originheight="324" originwidth="288" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/fTBssSQIS32gdIYbCAiJOQ/en-us_image_0000002532750235.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=11C0893945B3208E8DDE52F9A957451A0B89E400CB1FB3351E49BA193355D2F3"></span></p></td></tr></tbody></table>

1.  Create the following directories or files. Example file contents can be found in the corresponding module's **build/{_productName_}/intermediates/src/ohosTest** directory after [executing instrument test cases](#section1574003717165). _**productName**_ refers to the currently active product, which can be viewed by clicking ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/iQW1l3ToQLmIxes8x4pHYQ/en-us_image_0000002532750215.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6520EE1DE397039F92CC4E97A4196C96D3AAC600EBCC55B191B2C67BF95F2A1) in the upper right corner of DevEco Studio.
    
    -   **testability** > **TestAbility.ets**
    -   **testability** > **pages** > **Index.ets**
    -   **testrunner** > **OpenHarmonyTestRunner.ets**
    -   **resources** > **base** > **element** > **color.json**
    -   **resources** > **base** > **element** > **string.json**
    -   **resources** > **base** > **profile** > **test\_pages.json**
    
2.  Add the ability configuration fields **mainElement**, **pages**, and **abilities** to the **module.json5** file. For details about the fields, see [module.json5 Configuration File](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md).
    
    {
      "module": {
        "name": "entry\_test",
        "type": "feature",
        "description": "$string:module\_test\_desc",
        "mainElement": "TestAbility",                                   // Corresponds to the ability name in the abilities section below.
        "deviceTypes": \[
          "phone",
          "tablet",
          "2in1"
        \],
        "deliveryWithInstall": true,
        "installationFree": false,
        "pages": "$profile:test\_pages",                                 // Corresponds to the test\_pages.json file under resources > base > profile.
        "abilities": \[                                                  // Configuration of the ability to add.
          {
            "name": "TestAbility",
            "srcEntry": "./ets/testability/TestAbility.ets",
            "description": "$string:TestAbility\_desc",
            "icon": "$media:icon",    // Ensure that the referenced resources exist.
            "label": "$string:TestAbility\_label",
            "exported": true,
            "startWindowIcon": "$media:icon",
            "startWindowBackground": "$color:start\_window\_background"
          }
        \]
      }
    }
    

#### Running a Test Case

## Performing Local Tests in Running Mode

Before running test cases, connect the device and your PC, build your project into a signed HAP, and install and run the HAP on the device or Emulator. For details, see [Running Your App on a Local Real Device](../../../../running-your-app-on-a-local-real-device/document.md) or [Running Your App on the Emulator](../../../../running-your-app-on-the-emulator/document.md).

You can run all test cases in a project directory (**test**), run test cases from a file (such as **Ability.test.ets**), run all tests associated with a test suite (**describe**), and run a specific test method (**it**).

-   To run test cases in a project directory, right-click the project directory and choose **Run '****_test file name_****'** from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ec00yNvnSxetmCl8_3eNmA/en-us_image_0000002532750237.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E511DD0086FD7BD45B62D22E8C527913CE047E51E0929C67BCBF822F27A50B2)
    
-   To run test cases from a file, open the file and click the green button on the left of the test suite.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/9tNMhBpPRcmw3UsPUK3KXA/en-us_image_0000002501070232.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D244D669FC60B39E84816E44FDA16C1387022075818906F3045FD53ABC428A38)
    
-   To perform an instrument test based on custom configuration, [create a test case task](#section65264166107) and perform either of the following operations:
    -   Choose **Run** > **Run '****_test name_****'**.
    -   In the upper right corner of DevEco Studio, select a test task and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/-CWNURGiQjCqWmmU70oT9Q/en-us_image_0000002532670291.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFB3511EDFD0033BE9EF05FF426541CF4FC35DA13DD7B20C561A688355615905) on the right.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/wZSqv9LCSsmQZ_X9ZAd6_Q/en-us_image_0000002532670289.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70F88D2906A2CA54F801CC44C79E024D0AED63AAD356CB39F25D628E0CDADE5D)
        

View the test result after the test is complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/1uUxqmplT_mmnI5cFttCEA/en-us_image_0000002532750225.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EF9E3FBEEFA69D53A5EE137FA69348BE8931BDC8AE8B616530C92D77BD124F2)

## Performing Instrument Tests in Debug Mode

Compared with the running mode, the debug mode provides breakpoint management. When a breakpoint is hit, you can perform single stepping, step-in, step-out, and stop-over operations as required. You can also view the thread stacks, variables, and expressions to quickly locate faults.

The following uses a test file as an example. After adding breakpoints, right-click the target file in the project directory and choose **Debug 'Test file name'** from the shortcut menu to perform a test task in debug mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/uwEU4au_QxaT_UuHkj3UHw/en-us_image_0000002501070196.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=685BB36A6B53D3BC086B18FDDFCEB3519D86A4B60753106093F673C3412B38C5)

When a breakpoint is hit, the **Debug** window is displayed. You can perform breakpoint management and basic debugging in this window. When a breakpoint is hit, you can view the variables and stack information of the current thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/R2tInDaJQGSLDoBZ5pLODw/en-us_image_0000002500910386.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=496AF3488DF2688ECEDC79DCCDE0DF4D9B58222B7CE00479F6DC247AF93956AE)

Right-click in the code editor window. The shortcut menu shows the functions specific to the debug mode, including **Evaluate Expression**, **Run to Cursor**, **Force Run to Cursor**, **Add to Watches**, and **Add Inline Watch**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/8kV3qVtYTViGd8SsfM8RLg/en-us_image_0000002500910348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=465AC25C2908F0B8826D4DF4C46D25ED5D357C9901F8D43A6DAAEAC7072B3F6B)

After the test is complete, view the test result on the console.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/weYwg-a4QVePHsthZm67yQ/en-us_image_0000002500910346.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90CC7E5B0BCF6AC5CF51FF79F1E6EA87DE23BE59B12516503AF89B47D9FC07F7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/AqFScg0bQHSIPZpN4Er0hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF86D1D9DA7CC1582F8748BD3BDACDBDF8D94FD7DE11030A02A78400C8C5017F)

You can set the type of code to be debugged in DevEco Studio. For details, see [Setting the Debug Type](#section0164586312).

## Performing Instrument Tests with Code Coverage

DevEco Studio provides the code coverage for instrument tests.

You can specify the specific files to be included in or excluded from the coverage statistics. For details, see [Filtering Files for Coverage Test](../../black-box-test-with-coverage/document.md#section13756446154).

You can run all test cases in a project directory (**test**), run test cases from a file (such as **Ability.test.ets**), run all tests associated with a test suite (**describe**), and run a specific test method (**it**).

To run test cases from a file, use either of the following methods:

-   Method 1: In the project directory, right-click a file and choose > **Run '_Test file name_' with Coverage** from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/R7R7YMT4TuKvTBsrqluLEA/en-us_image_0000002501070206.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DC4F426721FFE45D67829414F66C47C99240ABB4709AB4AAB73F720A06791B9)
    
-   Method 2: In the upper right corner of DevEco Studio, select a test task and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/9JAYtDukSCKZsZVyfLVnVA/en-us_image_0000002501070202.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6943FFE9C0B7AD64F75EC61D87DBD03A6B6D3C3C027FD238E1F4490237BA1088) on the right.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/IhxcszzsSZ6_JI3lJH_Wzg/en-us_image_0000002501070222.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3812BE5117D20CB20DEE7FF82F0E17BC2EA6177104A2E184979597F11D545295)
    

After the test starts, the build process begins, and the **Cover** tab appears at the bottom. Once the build is complete, the **Cover** tab will automatically open. After the test task is finished, the path to the test report will be printed on the tab page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/s34uI1xORZyRkbENlsa64w/en-us_image_0000002532670305.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8A97A02DB740717C60161CDF1C839435C195953B1239469FC552DFB19BD3BB9)

Click the path link to open the report and view the ArkTS code coverage details. For details about the coverage rate, see [Viewing Coverage Reports](../../black-box-test-with-coverage/document.md#section10394362109).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/U5pK_N_QTOSuO-JFNkfXRw/en-us_image_0000002532750259.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32D607F83E799D4A1E3393D28E8D96865E88CC5711F0AD1288CD1A6AA3E16DAC)

On the **Cover** tab page, you can click the rerun button to re-execute the test case based on the previous settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/KW6Og7ctQDiXd-L0Wzdayg/en-us_image_0000002532670303.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F0C9296E1A9EE02B7309F0EC39AEAC9D684EB8AB3102B39D54EB0F7CED3068B)

#### (Optional) Customizing a Test Case Task

By default, test cases can be directly executed. To customize a test case task, perform the following steps:

1.  Choose **Run** > **Edit Configurations** from the main menu on the toolbar.
2.  On the **Run/Debug Configurations** page, click **+** and choose **Instrument Test** from the drop-down list.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ftGe9lLlSVSt748-yhbU0w/en-us_image_0000002501070230.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD00C04735B879CBDA5B846796DD5312A5E3BE32D1FA5A2050B8951A63240035)
    
3.  Set parameters, and click **OK**.
    
    -   If the module depends on a HAP, set the HAP installation mode in advance to **Keep Application Data**. This way, the HAP will be installed in overwrite mode, ensuring that the app/atomic service cache data is retained.
    -   When your project involves HAP/HSP modules that directly depend on other HSP modules (for example, an entry module depending on an HSP module) or indirectly depend on other modules (for example, an entry module depending on an HAR module, which then depends on an HSP module), you must install both the module packages and all their dependencies on the device during testing. In this case, you can select **Auto Dependencies**, which ensures that all required dependencies are automatically installed on the device. This feature is enabled by default for convenience.
    -   If UI testing is not involved, select **Only OhosTest Package**. This ensures that only the OhosTest package is sent to the device, omitting the HAP/HSP package. As a result, the time taken for package deployment is significantly shortened.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/bSUeQC_-TnOLsW6vIfTkdg/en-us_image_0000002501070218.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9A7F5951B5BBEB93FAD4DE4ECC2A3BFF5A1C04A566C08EBD3A7327E7AD7AA6D)
    

## Filtering Test Cases

1.  Set a filter parameter for your test cases via the second parameter of **it()** when writing test cases. This parameter is used to add annotations to a test case. The default value **0** indicates that the test case has no annotation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/AQLrApv2RNKs-gjInkSMVw/en-us_image_0000002501070220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=982CE7ED9D2B188DC27732BD2FFAD7E83D169A37C4AE2CCD46A373E807C126C0)
    
2.  On the **Run/Debug Configurations** page, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/L7pyuxn8SO2S2FY09xD5_g/en-us_image_0000002500910370.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D3FB6D69E85F83661DA57C463B8EA9DF577214CDC9427C06FAAB0F3E22C299C) in **Test Args** and add command line parameters in the **Test Args** dialog box displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/QU8etGyMQDam9hT95zv05A/en-us_image_0000002532670295.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD5DB82F681608E436982010BD5C3CE7D8152666F15CBE3056A0623D069A7118)
    
    For example, set **level** to **1** and **size** to **medium**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/IcbqiwiuSN2ksjlNeMBbQQ/en-us_image_0000002501070216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CA8A9A33DDD00AA45B8D1D0BF73B64502A814B9237E6DF752337DB00D5ECC68)
    
    **Table 2** Parameter description
    | 
    Key
    
     | 
    
    Description
    
     | 
    
    Value Range
    
     |
    | :-- | :-- | :-- |
    | 
    
    level
    
     | 
    
    Level of the test case.
    
     | 
    
    0 to 4, for example, **\-s level 1**.
    
     |
    | 
    
    size
    
     | 
    
    Granularity of the test case.
    
     | 
    
    **small**, **medium**, or **large**, for example, **\-s size small**.
    
     |
    | 
    
    testType
    
     | 
    
    Type of the test case.
    
     | 
    
    **function**, **performance**, **power**, **reliability**, **security**, **global**, **compatibility**, **user**, **standard**, **safety**, or **resilience**, for example, **\-s testType function**.
    
     |
    
3.  Run the test cases. Only the test cases that match the filter criteria will be executed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/n-hjljgJQdKt_TXvSwesMA/en-us_image_0000002501070204.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD91D47D0FA4EB6419391E5CB515412B6DB4DCD242BFC9B2932EBD544E9D76AE)
    

## Setting the Debug Type

Choose **Run** > **Edit Configurations**. In the **Run/Debug Configurations** dialog box, select **Instrument Test**, click the **Debugger** tab, and set **Debug type**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/GwW-IPTRQC6VCz2Sx4Q1hg/en-us_image_0000002501070198.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6871AE7184AB3684F733A7A7A8148B7BB8C11DC7B269BB326A951AA37948B0C7)

By default, the debug type is **Detect Automatically**. The table below describes the debug types.

| 
Debug Type

 | 

Code Type

 |
| :-- | :-- |
| 

Detect Automatically

 | 

Code automatically detected. The debugger is selected based on the programming languages involved in the project module and its dependent modules.

If a native module is detected, both the **PandaDebugger** and **Native** debug windows are displayed; if no native module is detected, only the **PandaDebugger** debug window is displayed.

 |
| 

ArkTS/JS

 | 

ArkTS/JS. The **PandaDebugger** debug window is displayed.

 |
| 

Native

 | 

C++. The **Native** debug window is displayed.

 |
| 

Dual(ArkTS/JS + Native)

 | 

ArkTS/JS and C/C++. Both the **PandaDebugger** and **Native** debug windows are displayed.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/71onz-41QueY0opURwvkzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEE57E75D1CD2C9E8C4269D4DEF950988A6623B43D9B7DC4BE99E14D096DB50F)

When debugging C++ code, ensure that the [Address Sanitizer](#section8352185341915) configuration of the current module is the same as that of all dependent HSP modules. Otherwise, the breakpoint of the C++ code may fail to be entered.

## ASan Detection

In instrument tests, you can run ASan detection for C/C++ methods. For details about ASan, see [ASan](../../../../analyzing-logs-and-faults/fault-analysis/asan-detecting-memory-errors/document.md). This feature does not apply to JavaScript.

1.  In the **Run/Debug Configurations** window, select an instrument test, click the **Diagnostics** tab, and select **Address Sanitizer**. Then both the test package and the source package will have ASan enabled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/xCnm2HOSTvufPknZupG9dw/en-us_image_0000002532670293.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=366158C7F72FAEDFE3FE1005AAE1385089DE89A8F87035EA371266693E60B8A4)
    
2.  If a local library is referenced, set **arguments** to **\-DOHOS\_ENABLE\_ASAN=ON** in the **build-profile.json5** file of the library module. This allows the .so file to be compiled in ASan mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/WXHS-Q6kSm2pqdg_xXtjbQ/en-us_image_0000002532750249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C95C46B14C0777E473E4C4831837EE3BCAB83A887DBECCBE2CEE533158C67BC8)
    
3.  Execute test cases.
4.  When a memory error occurs, the ASan log information will be displayed. You can click the link in the information to go to the code that causes the memory error.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Ww1TSrpzRZGGr9qnwWim3A/en-us_image_0000002532670299.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18753718F835BB718950D3422BF0AC5424D3A763EE79180311796017545A2928)
    

#### Testing C++ Code

As of DevEco Studio 6.0.0 Beta5, support for testing C++ code has been added, including the ability to run or debug C++ test code and collect code coverage statistics for C++.

Since the C++ test shared library (.so) cannot be executed directly on the device, it must be launched via Node-API from ArkTS/JS code to run the C/C++ test cases.

## Running C++ Test Code

1.  To create a C++ test directory, right-click the **ohosTest** directory and choose **New** > **C/C++ File(Napi)** from the shortcut menu. This will generate the C++ test directory under **ohosTest**. Taking the **entry** module as an example, the resulting directory structure is as follows:
    
    -   **src > ohosTest > cpp > types**: a collection of C++ API description files.
    -   **src > ohosTest > cpp > types > libentry\_test > index.d.ts**: file that describes the C++ API behavior, such as the API name, input parameters, and output parameters.
    -   **src > ohosTest > cpp > types > libentry\_test > oh-package.json5**: configuration of the entry to the .so third-party package declaration file and third-party package names.
    -   **src > ohosTest > cpp > CMakeLists.txt**: CMake configuration file, which provides CMake build scripts.
    -   **src > ohosTest > cpp > napi\_init.cpp**: file that defines C++ APIs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/y0Yuh1XZQlW9elMKMEGAFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7088BD645E07BAE0EC072578DD2FB23D1B6AFC60AA81B444E9EFE837A8A6FD3)
    
    The C++ test directory generated by DevEco Studio does not include a C++ testing framework. You need to select and use an open-source testing framework.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/glZmCL5ET02VJoHhjxc_ng/en-us_image_0000002532670307.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B54037D50707CDD07C58589598A15638853BAC938762851646A1F9657D6C2AF6)
    
2.  Launch the C++ test via ArkTS test cases. The example is as follows:
    
    // ArkTS test file Ability.test.ets
    import entryTest from 'libentry\_test.so';
    export default function abilityTest() {
      describe('ActsAbilityTest', () => {
        ...
        it('testNative', 0, () => {
          hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
          let result = entryTest.runNativeTest();
          hilog.info(0x0000, 'testTag', '%{public}s', result)
          expect(result).assertContain("ended");
        })
      })
    }
    
3.  Run the testNative test cases and check the test results.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ncuJYRYjRjK7JL76zrw26A/en-us_image_0000002500910382.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2BF3DD4DAB9469F8CC1815F21C2E5CAA1F1F0C0B833C106D49CBBB15A9BEEDE)
    

## Collecting Code Coverage

DevEco Studio does not collect C++ code coverage by default and needs to be enabled as follows:

1.  Add the following code to **CMakeLists.txt** in the test directory to enable coverage compilation instrumentation.
    
    // For versions earlier than DevEco Studio 6.0.2 Beta1.
    set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    set(CMAKE\_C\_FLAGS "${CMAKE\_C\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    
    // For DevEco Studio 6.0.2 Beta1 and later versions, OHOS\_TEST\_COVERAGE is true in coverage mode and false in debug/run mode.
    if(OHOS\_TEST\_COVERAGE)
      set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
      set(CMAKE\_C\_FLAGS "${CMAKE\_C\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    endif()
    
2.  In the **RunNativeTest** method of the **napi\_init.cpp** file, call the **\_\_llvm\_profile\_write\_file** method to save the coverage data to the **c++\_coverage.profraw** file under the **/data/storage/el2/base** path on the device. This path and file name cannot be modified. Example code is as follows:
    
    extern "C" {
        void \_\_llvm\_profile\_set\_filename(char \*);
        int \_\_llvm\_profile\_write\_file(void);
    }
    
    static napi\_value RunNativeTest(napi\_env env, napi\_callback\_info info)
    {
        char filename\[256\];
        snprintf(filename, sizeof(filename), "/data/storage/el2/base/c++\_coverage.profraw"); // Coverage report file path and file name, which cannot be changed.
        \_\_llvm\_profile\_set\_filename(filename);
        // Start the test.
        ...
        // End the test and save the data.
         \_\_llvm\_profile\_write\_file();
        ...
    }
    
3.  Right-click the ArkTS test file and choose **Run '_Test file name_' with Coverage** from the shortcut menu to run the coverage test.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/rbtfsCxrTuav3opltNjI-g/en-us_image_0000002501070194.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71C36FFEEAADF2C960109E3FDEA31D4539708515517D81D65A40EB71CC2ECFDD)
    
    After the test starts, the build process begins, and the **Cover** tab appears at the bottom. Once the build is complete, the **Cover** tab will automatically open. After the test task is finished, the path to the test report will be printed on the tab page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/iSqsFQ4ETDWwXXSdtweQXA/en-us_image_0000002532750217.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C62771192A4DE519F171F84174CB3D645930DDA44C08E5511CE689520C884FE)
    
    Click the link to open the report and view details of C++ code coverage.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/w2dJ-0S-TtCjlnyBZ7--Wg/en-us_image_0000002501070208.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF81ECAB00E2DACD718B433FA1FB842F6B52C5E55497B3F1BC9881071F19FA10)
    

#### Running Instrument Tests from the CLI

Run the following command in the root directory of the project to perform the instrument test:

hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}

-   **module**: module on which the test is performed. By default, the test cases of all modules are performed.
-   **coverage**: whether to generate a coverage report. The default value is **true**. Two reports are generated in the **_<module-path>_/.test/default/outputs/ohosTest/reports** directory, one in HTML format (**index.html**) and the other in JSON format (**coverageReport.json**). For details, see [Viewing Coverage Reports](../../black-box-test-with-coverage/document.md#section10394362109).
    
    If C++ code coverage testing is enabled, a coverage report will be generated at the path: **<_module-path_\>/.test/default/outputs/ohosTest/cpp\_reports/index.html**.
    
-   **scope**: test case, in the format of {suiteName}#{methodName}, or test suite, in the format of {suiteName} for execution. By default, all cases of the current module are executed.
-   **ohos-debug-asan**: whether to enable ASan detection. The default value is **false**. This field is supported since DevEco Studio 5.1.1 Beta1.
    
    ASan log path: **<_module-path_\>/.test/default/intermediates/ohosTest/coverage\_data**
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/HCR8xU3nTMignWW1xUeWzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D61F795972AE3D24F4DC94FA6EA0F5D0794C1189199C09138E2121ED8808AA63)

-   When you run tests via the CLI, the **product** parameter cannot be configured and defaults to **default**.
-   Multiple values of **module** and **scope** can be specified, separated by commas (,).

Path of the test result file: <module-path>/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
