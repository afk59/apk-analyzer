# Using Extension Debugging

You can debug the [ExtensionAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md) lifecycle functions in either of the following ways:

-   Debug the app in wait-for-debugger mode.
-   Specify the currently running or being debugged ability as an ExtensionAbility by modifying the run/debug configuration.

#### Debugging the App at Startup

1.  Debug the project as instructed in [Debugging an App at Startup](../debugging-an-app-at-startup/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/aIfoXb8UQbSENV0Rax68AA/en-us_image_0000002501070418.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8FC5C529A59F43DE7E4B3A327A9A9DFCEBEC77F32E8EB9C048CB33E75750789)
    
2.  Set breakpoints in the lifecycle of the ExtensionAbility.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Gfm95brDTfakfu5gzKW-Fw/en-us_image_0000002532750447.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4851EAAE3F1CE6BA380B20A693CC91FD96F633441CACB9F4FF826FF18A158E6)
    
3.  Wait for the ExtensionAbility lifecycle function code to be called to hit the breakpoints.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/iUVQgCiXSICX_JPCNdjmrg/en-us_image_0000002532750443.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8572283C4C2EF1EC1DA37E9EFD83E56E60AD1273A801C3AACFF29363985E340A)
    

#### Modifying the Run Configuration

1.  In the **Run/Debug Configurations** window, set **Launch Options** to **Specified Ability**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Rc6xrOqPTHas60BImdQ6HQ/en-us_image_0000002501070426.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AD01E5D31061C0561D4EE7ACAA926F766B75D8D74E1E19119B3E84089645A86)
    
2.  Select the ExtensionAbility you want to debug.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/xnvwA62gTsOLvR0FPeY5uw/en-us_image_0000002532670493.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D46E16954FD41DFA5694983DA082B6C7096030403C4FFD8F13C414DCD3820C1)
    
3.  Click **OK** to save the configuration and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/vYkuH7y8Rc6L_tZi4BvQzQ/en-us_image_0000002532670497.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CB061EABB72275ECC7EDE6EA3F6A2279F3B3045DA550EACDAF5018B679C8D5E) to start debugging. This will hit the lifecycle function breakpoints in the ExtensionAbility.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/nqjOMIUmS8aiIqAFTZpWpg/en-us_image_0000002501070424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F9CAE4CB98146E59D49CA1CBF677A494E81FA2E9B6E339952EE45E741C2EAD4)
