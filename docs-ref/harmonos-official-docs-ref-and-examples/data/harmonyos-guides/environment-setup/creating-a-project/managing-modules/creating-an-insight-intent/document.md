# Creating an Insight Intent

In DevEco Studio you can create an insight intent to help your app understand user intents and provide services rightly where they are needed.

#### Constraints

-   Insight intents can be created only in projects of API version 11 or later.
-   Insight intents can be created only for HAPs in projects in the stage model.

#### Procedure

1.  Right-click a module or a file in a module and choose **New** > **Insight Intent** from the shortcut menu. In the displayed dialog box, set the following fields:
    
    -   **Intent domain**: domain of the insight intent.
    -   **Source entry name**: name of the entry code file for the insight intent.
    -   **Intent Settings**: additional settings of the insight intent. The following uses MusicDomain as an example:
        
        -   **PlayMusic**: whether to enable the insight intent for playing a specified song. By default, enabling this option requires a linked UIAbility. In **Ability name**, specify the ability to link.
        -   **PlayMusicList**: whether to enable the insight intent for playing a specified playlist. By default, enabling this option requires a linked UIAbility. In **Ability name**, specify the ability to link.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/08DN6LxGQBmvjIAV-zjSBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF66BDBCD886BCACB30A6E86B029A9C699BC238F26BABF38DE373A575FFCC353)
        
        **PlayMusic** and **PlayMusicList** cannot be disabled at the same time.
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/QcrgHNw_TFqtAU1wMZS_yg/en-us_image_0000002532750571.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70B0F3E0CEA4313D5A17DF634FD45ADD14AF08AEA640F2B635D9F961121DB519)
    
2.  When you have finished, click **Finish**. The entry code file is generated under **entry** > **src** > **main** > **ets** > **insightintents**. In the **insight\_intent.json** file generated under **entry** > **src** > **main** > **resource** > **base** > **profile**, you can check the configuration of the created insight intent.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jANnq_oTQJqBmQa3ySiwWA/en-us_image_0000002500910702.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0905021EAD9C7DE09CD50701AD2E1C21224313E1A8D5995F2833264BCA92B06)
