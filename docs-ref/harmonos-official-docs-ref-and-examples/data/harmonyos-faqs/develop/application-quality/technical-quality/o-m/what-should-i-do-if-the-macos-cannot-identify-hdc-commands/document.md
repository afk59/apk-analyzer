# What should I do if the MacOS cannot identify hdc commands?

1.  Solution for problems related to environment variables:
    1.  Click the apple icon on the top left of the screen and choose **System Settings** > **Users & Groups**.
    2.  Hold down the **Ctrl** key, click the user account name in the left pane, and select **Advanced Options**.
    3.  Select **/bin/bash** from the **Login Shell** drop-down list to set **bash** as the default shell.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/0mFAby7HQ-Ogg7e_kDBnwQ/en-us_image_0000002194318532.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062535Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=899FBA1033BEBF5DE7101B667CBA1C271E894A074738DBE6C2E5584CFAF11A00 "Click to enlarge")
        
2.  Solution for problems not related to environment variables:
    
    1.  Open the terminal and input **cd ~**.
    2.  Run the **sudo vim.bash\_profile** command to edit the file.
    3.  Input the following at the bottom of the file:
        
        export PATH=${PATH}:Sdk/default/base/toolchains
        
        Press **Esc** to exit, and input **:wq** to save the settings and exit.
        
    4.  Run the **source.bash\_profile** command to load environment variables.
    5.  Run **hdc -v**. If the version information is displayed, the hdc command can be used.
    
    **Reference**
    
    [FAQs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#faqs)
