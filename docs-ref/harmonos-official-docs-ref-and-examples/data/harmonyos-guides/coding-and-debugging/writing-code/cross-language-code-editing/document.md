# Cross-language Code Editing

#### Generating a Glue Code Function Framework

Cross-language code editing allow you to use Node-API to encapsulate the APIs exposed to ArkTS or JS.

1.  Make sure the **napi\_init.cpp** file exists in the **entry** > **src** > **main** > **cpp** directory of the current C++ project. If the file does not exist, create one as follows: Place the caret at the name of a function or class (whose parameters must be of the bool, int, string, void, float, double, std::array, or std::vector type) in the header file (in .hpp, .hxx, .hh, or .h format), right-click, and choose **Generate** > **NAPI** from the shortcut menu to generate the glue code framework file **napi\_init.cpp**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ne45wO5NSaijQ11BmfW6fg/en-us_image_0000002501069986.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0997CDBD4C2726B2E490B861E0FFCA4728E8BAE550B50B30A1465F5C64FE71D0 "Click to enlarge")
    
2.  When the **napi\_init.cpp** file is in the preceding location, place the caret at the function or class to be invoked in the header file, right-click, and choose **Generate** > **NAPI** from the shortcut menu. The corresponding function or class will be registered in the **napi\_property\_descriptor** field of the **napi\_init.cpp** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_dD_n2DYQiGLR1FQsfqCQg/en-us_image_0000002532750019.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F204E8B6AC0DF92DD88CCEF649EE3C453E21A831FD57615D1CA107E6084284B5)
    
3.  Add the corresponding implementation code to the TODO position in the **napi\_init.cpp** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/5AaDurt9S1y8ywGUcspSqA/en-us_image_0000002532670069.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44150585EAB698B92BC7DD5EC8FDACC4B9E3837C0A7C3B208E52DCAAB2FC9439)
    

#### Quickly Generating Function Definitions Across Languages

The **Generate native implementation** feature is supported in cross-language .d.ts files, allowing for the one-click generation of corresponding function definitions in C++ files.

To use this feature, hover the cursor over the name of an undefined function. In the popup window, click **Generate native implementation**, or click the red light bulb icon that appears on the page and select **Generate native implementation**, to create the function definition.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/7uaq1LgwR-KXlI49DiLIGA/en-us_image_0000002500910142.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4FA5E323344EDA3DDF84EEF59BBAABB515B31078ECC847FA1AB3E3467B0A686)
