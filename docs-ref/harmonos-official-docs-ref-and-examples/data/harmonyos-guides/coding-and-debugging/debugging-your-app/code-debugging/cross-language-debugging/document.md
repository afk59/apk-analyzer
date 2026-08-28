# Cross-Language Debugging

DevEco Studio supports cross-language debugging for both C++ and ArkTS, allowing you to debug these two languages simultaneously. The overall operation experience is consistent with single-language debugging, eliminating the need to manually add breakpoints in the respective languages.

1.  Connect DevEco Studio to a device. If the device to connect is a real device, sign your app/atomic service first. For details, see [Signing Your App/Atomic Service](../../../configuring-a-debug-signature/document.md).
2.  On the menu bar, choose **Run** > **Edit Configurations**, select the module (for example, **entry**) under **Application** in the left pane, select the **Debugger** tab in the right pane, and then set **Debug type** to **Dual (ArkTS/JS + Native)**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/hJ5K5O5IQNmk_iG6HNMPAQ/en-us_image_0000002532750605.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B21857EA32D01006FFCA526B1B4B95007DEDA8735A74BEB8006B4C0E0844D9A)
    
3.  When the code debugging execution reaches the point where ArkTS calls a C++ method, click **Step Into** to navigate to the first line of the corresponding C++ method.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/GQHe5gN9RJK7owNMLuMjnw/en-us_image_0000002500910742.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=494A20D5DB6D0B110964036A254224612C7B719BB43A875C7DB33D5CA79E208E)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/0g-jgzuITCWWgLHuq_hGAA/en-us_image_0000002500910740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F958EB46947ECC8850599C6F2C30B6A263297A5E9674FACB872C6BCD3AD2419C)
    
4.  After stepping into the C++ code, you can view the C++ call stack in the **Frames** panel. To view the corresponding ArkTS call stack, right-click within the **Frames** panel and check **Show ArkTS Stack Frame**. Clicking any stack entry will then navigate you directly to the matching line of ArkTS code.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ilmcgCguTkWJfK0Ks77n0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90F61215EC4970608699B7B2A0F7C69499DEA7214D38C217F29632B1C690A075)
    
    DevEco Studio 6.0.0 Beta3 and later support ArkTS variable viewing. Other operations related to variables are not currently supported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/aEd-0UawTWSsFnLDyf3dmQ/en-us_image_0000002501070584.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5416D5AD2609FC79BD6AEB33EC12F6F8CC11E068E71070885DE59825129442EC)
    
5.  If there is a breakpoint in the code after the ArkTS call the C++ method, clicking **Resume** will return you to the next ArkTS breakpoint, allowing you to continue debugging the ArkTS code.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ucSm777aSCWrFb-er0QXKQ/en-us_image_0000002532670653.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=068FFC2B5ED79679A198A784DB794543EB9A0A70D59CAF52F80C707882D9695B)
