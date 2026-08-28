# Local Test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/W4W6rG19T86JoOqU_PZ6tw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B5C815F2FC528828551D2B5B7500298A8D45E68C72BC58AAB18007E1CF11AE4)

Currently, testing of C/C++ methods and system APIs is not supported.

#### Creating a Local Test Case

1.  Open the .ets file of the HAP, HAR, or HSP module to be tested in the project directory, move the cursor to any position in the code, and then right-click the code and choose **Show Context Actions** > **Create Local Test**, or press **Alt+Enter** (**Option+Enter** on macOS) and click **Create Local Test** in the dialog box displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/LKCoNK3LSBSNaJ2VCIwB-g/en-us_image_0000002500910558.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=812A9D504FB4EBEB40860CD794453BBAC7663E8320EE690016488DE886909D07)
    
2.  In the **Create Local Test** dialog box, set the following parameters:
    
    -   **Testing library**: test type. The default value is **DECC-ArkTSUnit**.
    -   **ArkTS name**: name of the created test file, which contains test cases. The test file name must be unique in the project directory, and allows only letters, digits, underscores (\_), and dots (.).
    -   **Destination package**: location where the test file is stored. You are advised to store it in the **test** directory of the module to be tested.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/dK4C8udeRamrk566JwCmUg/en-us_image_0000002500910544.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0602ADF50891DD380054142BA49C973DA8FD2D36F9A5D93FCD1692BAD5EA2FB)
    
3.  DevEco Studio automatically generates the corresponding test class in the **test** directory. In the test class, DevEco Studio generates test case templates for involved methods. You need to develop test code that complies with your service logic. For details, see [JsUnit User Guide](../../../../../system/debugging-tools/test-kit/automated-test-framework-user-guides/jsunit-user-guide/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/sFkFcXdpRROZPxxIeEvsCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC17B6BA9EC83FED976C65EB91E8DA924A19C7612F26D6B3B4DF91CB59D920C1)
    
    You can also create a test case under the **test** directory and add the corresponding test class to the **List.test.ets** file.
    

#### Running Local Test Cases

## Performing Local Tests in Running Mode

You can run all test cases in a project directory (**test**), run test cases from a file (such as **Index.test.ets**), run all tests associated with a test suite (**describe**), and run a specific test method (**it**). The test entries are as follows:

<table id="table8849024115311" style="border-style: none;"><tbody><tr id="EN-US_TOPIC_0000002532669727__row1084920245537"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p2084932419536"><span><img originheight="443" originwidth="499" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/xhsuJBgcTGi7BksloFL1Qw/en-us_image_0000002500910548.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=034224F1874AE7AADECEB36E2DF5F08C8C168B443A582CF4F6E560822EA732B9"></span></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p48491324125312"><span><img originheight="434" originwidth="466" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/04lj6d9oQWq9BvoskZPHDg/en-us_image_0000002532670471.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=175E9E5BCAF297F4C2EBA391BA56598502A7C852CF4E8BD88E711E982CD42103"></span></p></td></tr><tr id="EN-US_TOPIC_0000002532669727__row168495245531"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p108491924115318">Directory entry</p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p14849142411534">Test file entry</p></td></tr><tr id="EN-US_TOPIC_0000002532669727__row88495249531"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p13849132419537"><span><img originheight="172" originwidth="504" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/jrNtTXTsS1GBcUTYkhhYfQ/en-us_image_0000002532670455.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=BD21F9D30E03D51DD2DB1D8175FE0D5E956F93DE81C2EE7E268E45449CD9553D"></span></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p1985018244535"><span><img originheight="172" originwidth="467" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/TuuLpyUHS_eW4ykj8RpwGw/en-us_image_0000002500910562.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062153Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=1C340132EDC04C0515E8BC4450E841E3956C0D5C19A0DA56FA32C1008ADCD600"></span></p></td></tr><tr id="EN-US_TOPIC_0000002532669727__row1885072411535"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p1485092465312">Test suite entry</p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="EN-US_TOPIC_0000002532669727__p1085015248538">Method entry</p></td></tr></tbody></table>

The following uses a test file as an example. In the project directory, right-click the target file and choose **Run '_test file name_'** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/VXXd8Cr9SSGwtSH9vrRM6w/en-us_image_0000002500910550.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B90BF5968B88E405814D8D5F64B2D643130DBA30FD03E88F34DD20736E5C6D61)

You can also perform a local test as follows:

-   Choose **Run** > **Run '****_test name_****'**.
-   In the upper right corner of DevEco Studio, select a test task and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/_S8dzc9fTkKgPpiL_zl77g/en-us_image_0000002501070408.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62AF1EBD1E7C5A45AC4641957F20D8BC71AD0D5E44C53B974529F6A8E2530630) on the right.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/UuYRxFffTh-I7TCmsVXgVA/en-us_image_0000002532670461.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6520F3589D53DCF83B3C501BB7C02608C68F0DC3E11C3E7BBD35DDC818B47AF)
    

View the test result after the test is complete.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/eFkVAUVxS6aUiwsHoBWWWQ/en-us_image_0000002532750423.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CB189020B8B6DE06265F85FEA5BFF6E8F683C73DD0A9BD89DA83E353589B103)

## Performing Local Tests in Debug Mode

Compared with the running mode, the debug mode provides breakpoint management. When a breakpoint is hit, you can perform single stepping, step-in, step-out, and stop-over operations as required. You can also view the thread stacks, variables, and expressions to quickly locate faults.

The following uses a test file as an example. After adding breakpoints, right-click the target file in the project directory and choose **Debug 'Test file name'** from the shortcut menu to perform a test task in debug mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/CzOz5grpS0G5CB_inqQs1A/en-us_image_0000002532750413.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14A6EA0ECB1A2EF95FEBB6C59283813DE066F61771BF924AFC99B9D92DC4FA7C)

When a breakpoint is hit, the **Debug** window is displayed. You can perform breakpoint management and basic debugging in this window. When a breakpoint is hit, you can view the variables and stack information of the current thread.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/rUWSbEeXRA-GlEaK8U_6UQ/en-us_image_0000002500910546.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEB7FFABE350FA05F3023309B157362CAAADDA6B3382AAEC8D5E36A9FF0012F8)

Right-click in the code editor window. The shortcut menu shows the functions specific to the debug mode, including **Evaluate Expression**, **Run to Cursor**, **Force Run to Cursor**, **Add to Watches**, and **Add Inline Watch**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/oi7u03kxSMuLAFFZi-V3Sg/en-us_image_0000002500910566.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4DB207A0215DBB2C882816B78179E0B105DD838E2D6BB4E0362402861842EFB)

After the test is complete, view the test result on the console.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/fDs39KrSRX2M9F6Oyvkr8A/en-us_image_0000002532750425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E3A0B155733B5BED597EEB09C1BC60F633A2009ADC19EC6005BFB6FB774F4CC)

## Performing Local Tests with Code Coverage

DevEco Studio provides the code coverage for local tests. Currently, only ArkTS projects are supported.

You can specify the specific files to be included in or excluded from the coverage statistics. For details, see [Filtering Files for Coverage Test](../../black-box-test-with-coverage/document.md#section13756446154).

As with test cases without coverage, test cases with coverage can also be started from various entries. For example, to start a test case from a test file, use either of the following methods:

-   Method 1: In the project directory, right-click a file and choose > **Run '_Test file name_' with Coverage** from the shortcut menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/0PliyqUmQH6nq3OixMXrxQ/en-us_image_0000002532670485.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F25D0742DAEDB91F796ED85353B00482A3701EB8C21DE3C814D40665D8E81AA)
    

-   Method 2: In the upper right corner of DevEco Studio, select a test task and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/H7reDbSkS7S0mPuRkb_mtA/en-us_image_0000002532750427.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1D42BCF4E3EAF19D3471D341BA6B4996B1191FBC16948D6A3E868C49F505358) on the right.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Kq1EnFfIR4a3KI_xeiGZdQ/en-us_image_0000002532670475.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABB8B51EA332D12385B2B0CC35BA952B0EF88740680CCDD1CC4985FB7E2C7FC3)
    

After the test starts, the build process begins, and the **Cover** tab appears at the bottom. Once the build is complete, the **Cover** tab will automatically open. After the test task is finished, the path to the test report will be printed on the tab page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/NWcoEFiHQeO5mpFsbBniqw/en-us_image_0000002532750417.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D530FDF5D2EF22D3D9A0D6BEDDDBD587C8BD4983FBBC5A66D4BB200841F92FA4)

Click the path link to open the report and view the code coverage details. For details about the coverage rate, see [Viewing Coverage Reports](../../black-box-test-with-coverage/document.md#section10394362109).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/mFOVt3sfSeeNcvqKC3jXaQ/en-us_image_0000002500910552.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=110165615EA8D7A5B001D233E8583E1130CE1FA1C985C07DBD18FF26430AC04A)

On the **Cover** tab page, you can click the rerun button to re-execute the test case based on the previous settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/saX9Zu0aTemB-VPXrwrkMw/en-us_image_0000002532750437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F416BBBFAF832A048081CD7F6B2CD058E5EAE61028F808EE9CE9EC18F6111EF)

#### (Optional) Customizing a Test Case Task

By default, test cases can be run directly. To customize a test case task, perform the following steps:

1.  Choose **Run** > **Edit Configurations** from the main menu on the toolbar.
2.  On the **Run/Debug Configurations** page, click **+** and choose **Local Test** from the drop-down list.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ERDpKYjOTkKX1VTl2IBw0w/en-us_image_0000002532670453.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39C9A6853C94C99A10EBE3C83A266B099AB17D0BDFF55589B792114009570925)
    
3.  Set parameters for the task, and click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/wCxd1DnaRCmolF6SAsFG2w/en-us_image_0000002532750421.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=164A572D73E8F3CBC056561A8D6878E1C73D96111658EA3F5B2F1C25C206EABC)
    

#### Running Local Tests from the CLI

Run the following command in the root directory of the project to perform the local test:

hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}

-   **module**: module on which the test is performed. By default, the test cases of all modules are performed.
-   **coverage**: whether to generate a coverage report. The default value is **true**. Two reports are generated in the **_<module-path>_/.test/default/outputs/test/reports** directory, one in HTML format (**index.html**) and the other in JSON format (**coverageReport.json**). For details, see [Viewing Coverage Reports](../../black-box-test-with-coverage/document.md#section10394362109).
-   **scope**: test case, in the format of {suiteName}#{methodName}, or test suite, in the format of {suiteName} for execution. By default, all cases of the current module are executed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/-HTpNJ8TTJqFOUgEUWRbmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02BB68F6655CDE1969393384F190A0B05B22CFD922759E8060DF535F76754905)

-   Multiple values of **module** and **scope** can be specified, separated by commas (,).
-   The command cannot be executed on Linux.

Path of the test result file: <module-path>/.test/default/intermediates/test/coverage\_data/test\_result.txt
