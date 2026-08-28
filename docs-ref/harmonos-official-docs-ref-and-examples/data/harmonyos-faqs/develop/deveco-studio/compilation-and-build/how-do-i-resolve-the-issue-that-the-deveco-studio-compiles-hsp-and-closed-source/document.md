# How do I resolve the issue that the DevEco Studio compiles HSP and closed-source HAR files slowly because the emit process takes a long time to generate a declaration file?

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/gmJ8IVfvR-WzE3otBr0EMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45352E2D299EB8A3B9BCF0D805308A83696B1BE2614ED3107D864E7716B4FDE2)

Note: This solution is a workaround and this issue will be resolved in the future. You are advised to use this solution only when the system is blocked.

This solution is used to reduce the time for generating a declaration file.

Modify the **ets\_checker.js** file (stored in **_SDK path_\\default\\base\\ets\\build-tools\\ets-loader\\lib\\ets\_checker.js**) and edit the **processBuildHap** function.

1.  Generate the **sourceFile**, and then traverse the files to generate the declaration file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Ut5RjgnjTUyy3vLcmgwStQ/en-us_image_0000002229603953.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92395DFA5386FFB342EC849C221536542B27AC49B56A903D74FE1394CCDB7A23 "Click to enlarge")
    
2.  Modify the **getEmitOutput** function to **getFileEmitOutput** for obtaining the declaration file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/yDoi78SHQzi2fLsScfVh-Q/en-us_image_0000002194318168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF7DD6A5B06DEA63EEAB8B14D360E0FC4829CA1542ACE4A3EB776C9422E1F6D3 "Click to enlarge")
