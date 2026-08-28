# Log Analysis

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Q7SFYAahS_mESeLlRoxGhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3D1ABBD0F15992F11C91C5F2DA0BCF0DE7B56651C17D1C8868812146265DA9E)

For details about how to print logs, see [Using HiLog](../../../system/debugging-tools/performance-analysis-kit/log-printing/using-hilog-arkts/document.md).

You can choose **Log** > **HiLog** to view the real-time logs of all apps on a device. The default log information displayed in the **HiLog** window contains the following:

| 
Column 1

 | 

Column 2

 | 

Column 3

 | 

Column 4

 | 

Column 5

 | 

Column 6

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

Timestamp of the log.

 | 

Process ID and thread ID.

 | 

Service domain and tag of the log.

 | 

Application bundle name.

 | 

Level of the log.

 | 

Content of the log.

 |

You can filter logs by app bundle name, log level, and keyword, customize the log display format, export logs, and display the latest logs.

The buttons on the left of the **HiLog** window are described as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/LQaDs0-fSzu0qtJwXA-r2A/en-us_image_0000002532670411.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4CCD136AE97570F0C048451626F141E1892CCD506A6DD5BDCEC9F76B7C10492): goes to the previous page and stops automatic scrolling of the log window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/uFHeT0kFQ_24MWp-QeIKbQ/en-us_image_0000002501070336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E29021F1476E21EA467AEBC9A5C60D9BC8ADF893CD646CA348855931B9DB7A4B): goes to the next page and stops automatic scrolling of the log window. If the log window has reached the bottom, it automatically scrolls.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/bBTG-1KSSCOBVQtHflOrMw/en-us_image_0000002532750345.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CF9D61A205C91B825B0BAF6BD831F18EBAA8ABA447350017F5C35277C4EC4EE): adds line feeds when necessary. If this icon is not selected, logs are displayed line by line.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Arkrbvb2T3aAGJgG-0zK8w/en-us_image_0000002501070322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=600180B535C0A89F2D80A78F61C6CA7CB4A618D9228D0D5436D69893138BDAE9): automatically scrolls logs to the bottom of the window. If this icon is not selected, the window stays at the current log.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/idntMDYERoWFFFERD4HSyA/en-us_image_0000002532750329.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AF03F66F5610E008BAEE74CC61AE13D2B2FD9B2DA06E1EEB04C91A79205BBFD): starts reloading logs from the device log buffer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/UsYwcqBxTfqmc3Yrc2mLig/en-us_image_0000002532670367.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=451D4E2A9186A5ADB20BB4F3C50006C3A0A452F93CB855E46D5998FA7526DD17): clears the device cache and HiLog window logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/KC_Mhg-SRv2GLhr8L3Gg0g/en-us_image_0000002532670405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4546C7C7BC178D3825B316304A3BF5872BD5484A59E156E7CFE87020CA827FA9): takes a screenshot of the selected device and saves it locally.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/3Cj-SC5_ROahwJuu7T834A/en-us_image_0000002501070310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EAC900939D161962A4C82E8567EB5579A808DD49D0C240343F040D27BCE78EB): records the screen of the selected device and saves the recording locally.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/8R2QloJRSvKIbFuce-HaVw/en-us_image_0000002501070302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF90799FC1A21344CD51D5E99FC39983ECBBD5F9337EBE8680906D23BF9F7723): saves cached logs to a specified file for online logs, or to save the logs as an offline log file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/IBa7o44UQb6W2AnhVcOeaw/en-us_image_0000002500910494.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63CA0FB50B97D00678CBE51A13EBD1EE3F3966EE4F1B39E03D9DA5A702A1B81F): automatically selects and switches connected devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/DuSpVxfHTj-s7jNzPy45YQ/en-us_image_0000002532750303.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62323BA5D8FA001D7A627B5884E297C8710557F09B380338C0D1F8D6EB359B2B): switches the log view and customizes the log display format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/oBUQenmKQfqMDQWqDn6c3g/en-us_image_0000002501070308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61E1261B3E60D6A81665832C648B4DAE37E23F53763A7C6DBBDF1C5A3A1A48FD): closes the current log window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/EJbVs76BSc26DIw1IcyIIQ/en-us_image_0000002532670341.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CCE1545C61FADC5827A587B68287F2A81A4F93F32AD4B206B7EF9A4E4F406EA): goes to the online help document related to HiLog.

#### Filtering Logs

## Filtering Logs by Keyword

Enter the keyword in the HiLog search box. All logs containing the keyword are displayed.

You can click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/VOmokRJnSHOPuJcUEY_XRg/en-us_image_0000002501070328.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46C936733C73B6066667162DA159E06FF5E84024A166B8568FCC4F3C26179107 "Click to enlarge") button to specify whether the filter is case sensitive, and click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/TIRf0qXsTkiGbW6N_diCUw/en-us_image_0000002532750369.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B469E0021AD9084C683489CD0D236C992432A4FE3498136064EAEC428F02DF4B "Click to enlarge") button to specify whether to use a regular expression for filtering.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/hVB1AQ0_Rky4j7phN2qLIA/en-us_image_0000002532670375.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8354EFB34F72A37EEC557CBD14CC4AA7AAD68C90A5224C6942C1291991BDDAC9)

Since DevEco Studio 6.0.2 Beta1, you can use the logical operator & to concatenate multiple keywords for precise log searching. Note that spaces must be included before and after the & character.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/AUlgI46DQGe9s7laI19E5A/en-us_image_0000002501070292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F7BB34446F9E8A107F04A7FB452E5D88009984AD28ACC94339962AC71DE0E4B "Click to enlarge")

## Filtering Logs by Default Option

You can use the options provided by HiLog to filter logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/QUwu6CsWSEWJNY43bH1Kmg/en-us_image_0000002532670359.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=125C705C815F9635AAAB6AA10C8B8CF361A798FE8F363D9B95863A4E4B4D878A)

-   **All logs of selected app**: displays all logs based on the selected app.
-   **User logs of selected app**: displays only user logs of the selected app.

When **All logs of selected app** or **User logs of selected app** is selected, you can select a process from the process drop-down box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/UKIrSJlCS1ea70xZ6AMkIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08F1D137BAF0DF522CC8A28F48C744135FDC9567C988C710C7E84B460FCD4D31)

If USB debugging is not enabled when the device starts, some system apps may not register properly, and the HiLog list will not display these unregistered system apps. To view the logs from these apps, you can [filter logs by keywords](#section1264082914019) in HiLog or keep USB debugging enabled and restart the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/IW2tFauXSYyM4aeGJkC1dg/en-us_image_0000002500910444.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F22FA797A05055F606EE02974CACA96C4464D18AD9383CECB599EE4D0FCE6062)

You can also enter a PID or a keyword of the app name in the process drop-down box to search for the process to be filtered.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/v-z2-ae1QTKBGsigjABeCg/en-us_image_0000002500910436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=058837D2D1F5814AD6A881007EAB44795C104AB6AAFE96A27943DEC3FEE729C8)

## Filtering Logs by Log Level

HiLog provides logs of the following levels: **Debug**, **Info**, **Warn**, **Error**, and **Fatal**. You can specify the log level to filter, and the system displays logs of the specified level and higher levels.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/iDt8JEMQRRqTVWRhzpVHYw/en-us_image_0000002500910430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0554EE61C0FE9823676D364A54B511A04DD69E0462E93A448F37351AFE86F97)

For example, if you select the **Warn** level, logs of the **Warn**, **Error**, and **Fatal** levels are displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/DzJ_eKOrRCGXbwf8rrlimw/en-us_image_0000002500910426.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAD2CEBEE3D8D694F14588E5301C6F34129B490322EA4661F3EBAE937E5D273D)

## Filtering Logs by Custom Option

In addition to default filtering options, HiLog also allows you to customize and save filtering options for reuse.

To customize a filtering option, select **Config custom filter**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/rXJXW0J3TOmN0qwRkvjoCw/en-us_image_0000002532750351.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1B21760FE46594A28313C79D503B12F69D4ACB2BA8BAE8C6FDE8A42F279E3C2)

In addition to the filtering options described above, you can configure the following:

-   **Set to all projects**: Select this option to filter logs of the current project and all other projects.
-   **Package name**: Select this option to filter logs by app bundle name.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/HbOOebuCQeaF2__nrrClog/en-us_image_0000002500910450.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEDDDAA10450861BA0098ABCEF3A381EB1B458FB21C2EEA6EE78A51E804189A7)

After the configuration, the custom filtering option configured is automatically applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/HDHD7zKqTeyV3cdbZb7Fkw/en-us_image_0000002501070342.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D123C9FD7A38368AA3F02236022080B85EB706B23B49411000D43D8E0986997)

Now, the logs are filtered based on the specified keyword, log level, and custom filtering option.

#### Setting the Log Display Format

You can customize the log display format to filter out unnecessary information.

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/TWyAICRqTdinAR8IDfdfJA/en-us_image_0000002532670365.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C2A3117CF7D8215286112F1379DCA43B5984D70E8B2348183C54D071E061DA7) on the left, and set the log display format as required:

-   **Standard Views**: displays all information.
-   **Compact Views**: displays only the log levels and log information.
-   **Modify Views**: customizes the log display format in the **Hilog Format** window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/oSB6B_iATXakv5HGyxM9-g/en-us_image_0000002532670361.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9CAEE07683557AC9F9FFB23E0E60AA635A2EE1780E9EF319DF61612B5FBD778)

Customize the log display format in **Hilog Format**.

-   **Use as default view for new windows**: If you select this option, the customized log view will be used as the default log view. You can still change the log view as required.
-   **Show timestamp**: To display the log timestamp, select this option and set **Format**.
    
    **Format**: To display date and time, select **Datetime**; to display time only, select **Time**.
    
-   **Show process id**: To display the process ID, select this option.
    
    **include thread id**: To display the thread ID, select this option.
    
-   Show **domain/processname/tags**: You can check the following three options to determine whether to show the domain, process name, and tag.
    
    **Show domains**: To display the domain, select this option.
    
    **Show processnames**: To display the process name, select this option.
    
    **Show tags**: To display the tag, select this option.
    
    **Total column width**: Set the maximum width of the **domain/processname/tags** column. Excessively long information will be abbreviated in the column and displayed in full via a tooltip.
    
-   **Show package names**: To display the app bundle name, select this option and set **Package column width**.
    
    **Package column width**: Set the maximum width of the bundle name column. If the bundle name exceeds the maximum column width, complete bundle name is displayed in a tooltip.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KQWxUxKtRBGFJCVy0iJyqQ/en-us_image_0000002532750343.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69D07FB586CB64CDFD26B01980651EE54C6BDA8C2654B62DD84E39014C601778)

#### Wrapping Long Logs

If a log message cannot be displayed completely in the log window, you need to drag the scroll bar to view the log message. To wrap lines, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/LyZUCxc2TserP66QzgBlKg/en-us_image_0000002501070268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF86251C80EBECE96E38B9D4C6FE8500615B54503C52461E04E7C0B083A1B44C) **Soft-Wrap**.

**Figure 1** Line-wrapping disabled

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/qSvERj-HRE2lXzbJxCl8bw/en-us_image_0000002532750315.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C55901EDFE4DED3906C68AFDDEA97F8025C83DDB45BE4163BFEA59DF928A058F)

**Figure 2** Line-wrapping enabled

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/dF0NrZCnRyeVM_UB0s0oYg/en-us_image_0000002500910476.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A86CC1764F5D7BB154C55F3AD98909566D7EE43AC670736DF54C31676DDA2667)

#### Displaying the Latest Logs

HiLog displays logs in real time, with the newest entries appearing at the bottom of the window. To enable the view to automatically navigate to the latest logs, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/PHPN309BQVGuWoetpaC2Gw/en-us_image_0000002532750341.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6F01979F610309649D757105A9E207A204DFA002024D38D3C06D212DE1B8E03) **Scroll to End**. To stop the automatic scrolling and stay on the current line, just click on the **HiLog** window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/tyUbTdETTIOLJmCMWOD1sQ/en-us_image_0000002532670379.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=780C349171846C9510F0DF2A7FB949EC3C4777A6660BCE883B8EB44253706E23)

#### Exporting Logs

You can save the filtered logs to a file for further analysis.

Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sz04iB6HQgKOdn7FmHAkAA/en-us_image_0000002501070276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAD023F65E2E863E3322774742439A8AFA50885CF02B21638F08E24AB0B9D39C) **Export HiLog**. In the **Export HiLog To** dialog box, specify the directory for saving the logs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/FB8nbKaXR1W2SIfNRXgfCw/en-us_image_0000002532670357.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57A7CAE94FF8F38B2B0B56ABB8B4E5C6648BB944333962AF3504999EB437EFBF)

#### Clearing Logs

There are two log-related buffers: device log buffer and HiLog console buffer (buffer of the **HiLog** window).

The process for printing logs on HiLog is as follows:

1.  Apps output logs to the device log buffer.
2.  The Log component dumps the logs from the device log buffer to the HiLog console buffer.
3.  The **HiLog** window displays the logs stored in the HiLog console buffer based on the filtering criteria.

To clear logs, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/rXPLu_fRRXeo5gObvISzJg/en-us_image_0000002532750299.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A5494BA7A15566A6EF24C8934707F8A8ADB5B763847536617E7C75ECA12A4E3) **Clear All**. The device log buffer and HiLog window buffer, as well as the logs that have been printed, are cleared. Then, the **HiLog** window displays the logs that are newly output to the device log buffer after the clear operation. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/hcmw0aSET76GUjzkIFnIzA/en-us_image_0000002532670353.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A36BBC419F0755C6C08662EA9199A76894A104DCD57F5BC035D3CD1730F3FD0A)

#### Setting the HiLog Console Buffer Size

The logs displayed in the **HiLog** window are stored in the console buffer. The buffer size determines the maximum number of logs that can be displayed in this window. When the number of logs reaches the maximum, the earliest logs will be automatically cleared. You can set the size of the HiLog console buffer.

Choose **Settings** > **Buffer**. The buffer settings window is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/BNRN4Ja9RtqLZFSn2d5xeg/en-us_image_0000002532750307.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=362F9375D43ABD42B5824BB6382758B6447386E12544297AB0945836E045605A)

Select **Override console cycle buffer size** and enter the buffer size. The default buffer size is 4096 KB. If you change the buffer size, restart the **HiLog** window for the change to take effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/twMaArxjRzOS_jmKqeb97Q/en-us_image_0000002501070300.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2001DEB7A75C6370F5BCE1E451D43C67CA870318516B65E2AB829BA319F9369)

To restart the **HiLog** window, click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/TMuVgh-AR-OhX01lUN5Qlw/en-us_image_0000002532670373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04E01BC85BC6D923DFA2DEF3B3779B0AF8C5D50D1D4D698240047605479718D4) button in the lower part and then choose ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/VB2z_ImuQUexUJC97j2jZA/en-us_image_0000002532750295.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4400333842F55D85873F7B1C263037B7A207B4547BB0F6C148B0705C5220C5BA) > **Online Log** in the upper part.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Fema0p_8RnKLX75c7a476A/en-us_image_0000002532670339.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BE92B790AC6565EED61EEB05C6845432B751ECDA3335FF71666034F8CBE969E)

When the number of logs reaches the maximum, the earlier logs displayed in the upper part of the window are continuously cleared and keeps scrolling. To view the log information, right-click in the window and choose **Pause Output** from the shortcut menu to pause log printing. After viewing the log information, deselect **Pause Output** to resume log printing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/sqvTtJDwTb-cET-3TIpyUw/en-us_image_0000002501070296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6539C97945E66AAFB80007513C48265AA2F87E69B85F2B54C09FCA174667D068)

#### Setting the Device Log Buffer Size

To view the size of the device log buffer, run the **hdc shell hilog -g** command. The default buffer size is 256 KB.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Ae5eE6vEQWOov_JXh_AEgg/en-us_image_0000002532750357.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA86384B1AB2676B6EFC2A106F8B27FD28EF94F5401A87F6EA06E61912C6A3F8 "Click to enlarge")

To change the log buffer size, run the **hdc shell hilog -G** command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/VTXGE2oxTV6p8ErbPACyDQ/en-us_image_0000002500910498.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AB825E2577C8C131692CEB289FFAF804921C04D0A84E3F3A35291FE6191AB72 "Click to enlarge")

To set the buffer size for a certain type of logs, run the **hdc shell hilog -G** command with the parameter **\-t**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/34FV0Ek-RPqIM-9-G8FR7w/en-us_image_0000002500910464.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC932DF52E2DD5F7C90D0502594F1066403434CC1E270EFDCE29B5BDA08F838C "Click to enlarge")

Once the maximum device buffer size is reached, historical logs are saved to the **data/log/hilog** directory of the device. You can download historical logs from this directory for log analysis.

#### Viewing or Exporting Device Offline Logs

In DevEco Studio, you can view offline device logs located at **/data/log/hilog** from the offline log window, which displays the logs after they have been [parsed](../../../system/debugging-tools/debugging-commands/hilogtool/document.md) and formatted.

Click **New** in the upper left corner of the **HiLog** window, and then click **Offline Log** to open the offline log window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/pXMJdSLzSbGtympaP1dSnA/en-us_image_0000002500910486.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22DAE46F2456FCAD1952E867221BD3D931F91AF8690B3C0C0748DFA793FCF363)

The offline log window provides the same functionality as the online log window, except that the device drop-down list box only supports the selection of real devices and emulators.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6pSC8BQSS0WDfd5CLzaEUg/en-us_image_0000002532750339.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10EF7A2414DF43C36485BF91F4C75F4E9ED697A01E9AD701109BBA77A6EBCB5C)

Offline logs can be filtered by time, with the default time range being the 30 minutes before the window is opened. In addition to the displayed format, you can also enter time in yyyyMMddHHmm format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/1SmMMMAfSo-Fmt8egsTZQw/en-us_image_0000002532750297.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04045DAFAB13201EABA7259A3D9E4BFD96E073888D658D3F8847FA57C3BB9D58)

After you enter the time, the log file list will refresh, and clicking a file will download it from the device and automatically parse and output it to the offline log window.

The content of the latest log file continues to be updated until it reaches the specified size. If you reopen the offline log window or change the time setting, the list of logs refreshes, leading to the download and parsing of additional content from the latest log file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Hr3Nam0pT6KUPaDaUV7ayw/en-us_image_0000002501070290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A907FFB497D7421F89C0997338AE7E184C69328AD63602561A86E26B797CA63A "Click to enlarge")You can set the amount of text that can be output in the offline log window. For details, see [Setting the HiLog Console Buffer Size](#section106741332995). A smaller setting may result in failure to display all the logs of the selected file. The recommended buffer size is 6 MB (6144 KB).

If the logs are not fully displayed even after the buffer size is set, you can export them by clicking the save button on the toolbar on the left. This exports the original, parsed logs before they are formatted by DevEco Studio, and you can view the complete logs in the exported file.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/dbsKWktDSbaX--AA2hgsZg/en-us_image_0000002501070312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9886C2445CAA4AE77BAA9F6B31F5EB1BCE3E655812F55FFFF2DEB6A259D10E80)

#### Stopping an App

Since DevEco Studio 6.0.0 Beta5, you can right-click the HiLog window and choose **Force Stop App** to terminate the app process associated with the log. This feature is unavailable for system apps or those signed with a release certificate.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/V5ntXWyKQsiEh5-T_cuiUQ/en-us_image_0000002532750323.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6221823087CFA9A680CB2ADF00EA5BC6136EFC6F5A250C5147AB3CAA0D47CC0D)
