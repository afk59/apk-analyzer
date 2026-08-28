# What should I do if Hot Reload is not supported after code modification?

**Symptom**

During the hot reload process, if the current code changes are not supported by hot reload, the console will display an error message, requesting reinstallation and restart.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/dz5RT1emSD2brJUb6gcqkw/en-us_image_0000002194318220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=970C536AA6A64690C209B573B5A6F53D9495715F54A4EB5E3613C6DE42EB15E6 "Click to enlarge")

**Solution**

This issue occurs when the code changes exceed the supported range. For details about the range of supported code changes, see [Constraints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hot-reload#section995453874915).

**Common unsupported code scenarios**

-   Addition or modification of member variables and functions in **struct Index** decorated by **@Entry**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/NDdytyWTQJmDia9313BTUw/en-us_image_0000002229604013.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61ACB0371202077E5EA664B330CFC24E078EED3DA393F05038892A5E4C52C72A "Click to enlarge")
    
-   Addition of class member functions in the **@Entry** file
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/o1cyUVGcSVCFanvQxaTEWw/en-us_image_0000002194158608.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18D3BB6C9AC504A0591F245923D82C85555948E6CCEB7DC9145FEEC7AB4D7C6D "Click to enlarge")
    
-   Modification of the enums in the **@Entry** file
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/JUrOf0f1TfOPpcXNFoyxsw/en-us_image_0000002194158604.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA600ED8BE5D01919FB741A0173BDD2242DCDEED15046BFBAE5F7E5366800B4F "Click to enlarge")
    
-   Addition and modification of a module that is not imported
    
    If a code file is not imported at the start of the hot reload, adding imports for this file during hot reload is not supported. For example, if **TestC.ets** is not imported in **Index.ets** at the start of the hot reload, adding **import _xxx_ from './TestC.ets';** will not be supported during hot reload.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/YrrBHIkcR7Gf50F9vTUcKQ/en-us_image_0000002229604005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4E44660254C7507939E8426BBABF11972E532625DAE2F399DCC66E3458BE0DC "Click to enlarge")
    
    If an import statement is dimmed before hot reload, the file will not be compiled and will be treated as an unloaded module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/q1fXyogdRru1xyAH03OJ9Q/en-us_image_0000002194318228.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E655DE5BAAA893D094E47BE32DF3549BF16D784CF39BC68992CF46AAD7F8237A "Click to enlarge")
    
-   Modification of top-level closure variables (though addition and deletion are supported)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/NOa2Nje2S2WLlG-bRX26GA/en-us_image_0000002229758481.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20F50C48F3A165594CEB9047C5285794E870A7BEA860FB24A2852549963FD352 "Click to enlarge")
    
-   Placement of class inheritance classes and inherited classes in the **@Entry** file. You are advised to write **class** in a non-@Entry file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/8zxhwBR6SfmNg-3poQcZpg/en-us_image_0000002229604009.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02EADD09E3F204D5C26BE2755C808EB6692F366BE5234119094CC880F2223CAB "Click to enlarge")
    
-   Modification of most decorators in the @Entry file
    
    Currently, hot reload does not support the modification of most decorators. The @Styles decorator can be added and modified in the @Entry file. The @Builder decorator can be modified but cannot be added. The @State decorator cannot be added or modified.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/-kQHePoHQj2eilZUd69zqA/en-us_image_0000002229758473.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7A39EC26B42F48BB3DCB427239A26DA9F47DE016F593D5B1E39B43D280D3F98 "Click to enlarge")
    
-   Addition and modification of custom components in other structs inside the @Entry file
    
    It is recommended that you import these components instead.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/RXbXiQ1ZQyucQNF6ZrXdcA/en-us_image_0000002194318224.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3661A8B4D7E2671CC9BC71FA9BF6ECAA9CC3683B0AFF8F8D99293BEBD14CEE96 "Click to enlarge")
    
-   Addition and modification of classes or functions with the same name as @State decorated variables in the @Entry file
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/nyE2ap8vQe-YCJ1KtLDlmw/en-us_image_0000002194318216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA0D2F5A520A53B11E28B348F9648D9A70975DAEC522D96E634DFBAB570C58B9 "Click to enlarge")
    
-   Modification of non-ETS or non-TS code files
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/i8t-ko1sTn-1YabaW14rbA/en-us_image_0000002229758489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00D4570EFCC70772C926B913DBC969193F9A8013E71B1EEFFB521A6C79A3D354 "Click to enlarge")
    
-   Modification of Worker thread files
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/D-d1m0pLQhaY-pJr9RXYKA/en-us_image_0000002194158612.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5147B3C7CCB7B75860E0C93AAE1619ED223453A5BE989271455ED042DC12A0D "Click to enlarge")
