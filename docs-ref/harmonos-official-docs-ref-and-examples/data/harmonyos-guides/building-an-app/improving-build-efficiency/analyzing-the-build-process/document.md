# Analyzing the Build Process

Build Analyzer can visualize important information in the build process for you to analyze and check performance and memory issues.

#### Accessing Build Analyzer

By default, Build Analyzer generates a report each time an app build task is created and displays the report in the **Build Analyzer** window.

After app build is complete, you can open the **Build Analyzer** window in any of the following ways:

-   Choose **Build** > **Build Analyzer**.
-   On the **Build Output** tab in the **Build** window, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Q8lJAPybTn-JmdfIQFA1tA/en-us_image_0000002532749757.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F82FD7B4466ADD61164284196EFE4EB338A42F59DD2C6F90935F565F13671BF) on the left panel.
-   After the build is successful, click the link below the log on the **Build Output** tab page in the **Build** window.

#### Viewing the Build History

You can find a list of historical build records in the **Build History** pane on the left of Build Analyzer. These records, including the historical build data of the current project and [imported log data](#section26761217305), are presented in a chronological order for easy tracking. Click any record to view its overview and visualized graphs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/oU7uqvCXQn6r_-cCXJVOgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0A7CFD421E8EDADD0157426C4DF8994D2EEE285DCBC79FBC5B404DD9E32015E)

The historical build data of the current project is stored in the **./hvigor/report** directory. If the number of build records exceeds 10, the earliest record will be automatically deleted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/WdZGyeuRTYOQlsQE2-AdFA/en-us_image_0000002501069750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=133F02B80CAFBBE4A9E9415D39DF880E5569F14F91EE4C23993BE391843CEE7D)

#### Viewing the Build Task Timeline Graph

When you open Build Analyzer for the first time after the build is complete, the build analysis overview is displayed, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/1pYERnIHR1eNUyWN2ZhJGA/en-us_image_0000002532669807.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE8361F04C672969AFDF8463A2C95CE6581745A1EF8A9BD7F43639377CC0E307)

To view the build task timeline graph, choose **Tasks** from the drop-down list box. The build history, build task timeline graph, build logs, and log details are displayed in different blocks on the page, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/y9jeaclhRQiU1TwqoFdT5g/en-us_image_0000002501069738.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98A05808F5454BD7E4EAD875CD9D9DA57200AC6C735789F84E9A5B2E59E026E2)

Each build task occupies a certain length in the graph based on the proportion of each task duration to the total build duration. You can adjust the time range to view specific tasks and their durations.

By default, build subtasks in the graph are collapsed. You can click nodes in **Build TimeLine** to expand the build duration graphs of subtasks.

The graph is associated with log information. You can click the task information in the graph to view the corresponding log and log details. Similarly, when you click a log, the information displayed in the graph changes accordingly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/Eejqpl16Qji2cPNe1CV7fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4368DB6C83CB91FFE046464FD40F6BBD7DC3C8CF846DBDA5C0398F75EBDAB7D9)

Build Analyzer does not display all tasks in a build operation. Instead, it preferentially displays the tasks that account for a great proportion of the total build duration.

Log information of each build is displayed by log level (Info, Debug, Warn, and Error), and log search is supported.

After you click a log, the information displayed in the upper graph and the **Details** block on the right changes accordingly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/6ICdhVxIQuK845NL_eHWnw/en-us_image_0000002532749763.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFAC0FD6AC9735A53B47B3D03AAA2FE9D5EE82F13C4C105717BADEFB65DF6ECB)

#### Viewing the Build Task Proportion Graph

To analyze how build time is distributed among tasks, you can use the build task proportion graph. To view this graph: On the **Overview** page, click the links below **Common views into this build**; alternatively, switch to the **Tasks** page and specify how you want to group the tasks. Tasks are grouped by modules, service categories, targets, targets within the same module, service categories within the same module, and service categories within the same target. Tasks in the chart are sorted by duration proportion in descending order. You can click a subtask to view its execution details.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/aDsvziruQhKmhnRO5o_GTQ/en-us_image_0000002500909898.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=493C917B7FF78420913631A0E0E7CE586EB5791BFD78B0E9235A32776235963E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/_TvbqPXcQFmmxYyg0q0t-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B15DC548C72423D2AD70F3B079B060CDDD391DE6AD9D583A2BF00E03DDBA530E)

1\. Due to the existence of parallel threads, the duration sum of all task types may be longer than the actual total build duration.

2\. In the pie chart, **configuration** indicates the proportion of tasks that are not recorded.

#### Viewing the Memory Usage Curve of the Build Process

To analyze the memory usage during the build process, you need to [set the build analysis mode to Advanced](#section207890565217) and enable memory monitoring. After the build is complete, a memory usage curve chart is generated. This feature is supported since DevEco Studio 5.1.1 Beta1.

Click **Memory Usage During Build** under **Common views into this build** on the overview page, or select **Tasks** and **Memory Usage** from the drop-down list to view the memory usage curve.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/nuzSRPhCRninfUhBCE-0og/en-us_image_0000002501069740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2398BA3F735979FD9E6C294C57297CD448D915F3F2F7A50BBEBFF7904A03667)

#### Exporting Logs

To export build logs, click **Export Report**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/PacOOIKRRVq_zgUaK21xog/en-us_image_0000002500909890.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06B9E2CB893396A82A7C2D679E32269AA586C342A4A1155B2FEE6EF2102C6A2C)

The exported report includes:

-   HTML file that analyzes and records statistics about this build
-   **build.log** file
-   **daemon.log** file
-   **report.json** file that records build task duration details
-   **report-monitor.json** file that records memory usage during the build process

#### Importing Logs

In Build Analyzer, you can directly access the build logs of historical or other projects by importing them. To do so, click **Upload** and upload the desired **report.json** file. Once uploaded, the file is stored in the **./hvigor/report/upload** directory of the project, and a record of it appears in the **Build History** pane. Be aware that the **upload** directory can contain a maximum of 10 files. If the number of files exceeds this limit, the system will automatically remove the oldest file to make room for the new one.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/7gfguglHR5SvsAsnu9r7VQ/en-us_image_0000002532749761.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC8D44D40CD397FE5077738EF6DFD39E58F745D89B0628F33956B0C1840E3DED)

#### Setting the Build Analysis Mode

Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and set **Use build analysis mode**.

-   If you select this parameter, the options are as follows:
    -   **Normal** (default value): indicates that only simple event tracking data is recorded for analysis.
    -   **Advanced**: indicates that detailed event tracking data is recorded for analysis. (You are advised to use Node.js 18 if selecting this option.)
    -   **Ultrafine**: indicates the ultra-fine mode. Compared with the **Advanced** mode, this mode records more detailed trace data during ArkTS compilation. However, enabling this mode may prolong the compilation and build time. This mode is supported since DevEco Studio 6.0.0 Beta1.
-   If you deselect this parameter, no build data is recorded for analysis.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/gJilxBbYSaWfGyM76E-Cjg/en-us_image_0000002532669815.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D5EB8D8CCD55ECA7889A7C63A281FA977CC16C7744F717B28E3102E7FD1B1D8)

#### Generating a Build Visualization HTML File

-   Generate a build visualization HTML file through the command line. For example, to generate a build visualization HTML file for a HAP module, use the following command:
    
    hvigorw assembleHap --analyze=normal --config properties.hvigor.analyzeHtml=true
    

-   Generate a build visualization HTML file by setting the **properties.hvigor.analyzeHtml** field in the [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md) file to **true**.
    
    {
      "modelVersion": "6.0.2",
      "dependencies": {
      },
      "execution": {
      },
      "logging": {
      },
      "debugging": {
      },
      "nodeOptions": {
      },
      "properties": {
        "hvigor.analyzeHtml": true  // Generate a build visualization HTML file.
      }
    }
    
    Execute the build again, for example, by running the following command:
    
    hvigorw assembleHap --analyze=normal
    

After the preceding commands are executed, the corresponding HTML file is generated in the **.hvigor/report** directory of the project. The file can be opened in a browser.
