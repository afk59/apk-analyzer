# How do I use ohpm in the CLI?

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/7TTtQSfuSY-qZtM7SNPcQw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D452AFC1B9E8431199B8A487778997897181B41DF4D47C368B2956EC8C50B5D)

Make sure Node.js 18 or later has been installed, and environment variables have been configured.

The default decompression path for ohpm is as follows: **_<DevEco Studio installation directory>_\\tools\\ohpm** or **_<command line tools installation directory>_/command-line-tools/ohpm**.

**Symptom 1**

After ohpm is installed on Windows, the ohpm commands do not work in the CLI.

**Solution 1**

1.  On Windows, right-click **This PC** and choose **Properties** > **Advanced system settings** > **Environment Variables** > **Path**, click **Edit** to add the **bin** directory generated after the ohpm package is decompressed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/9IF2AWMuRCmh66QOkfMzzg/en-us_image_0000002229604141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA1E2A55A259EE871AEE6A30015C09511C9E86FBF82643311EAD5F9915122AF4 "Click to enlarge")
    
2.  After the variable is added, restart the CLI and run the **ohpm -v** command to check the ohpm version. If the terminal outputs the version number information (for example, 1.0.0), the operation is successful.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/mY3Kp9QRSmKwv9UTH83f6Q/en-us_image_0000002194318368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29C9F5FD2C93C1980F79ECCA8DC56995084420DCDAA47BE9FE6A1F71E481729D)
    

**Symptom 2**

After ohpm is installed on Linux or macOS, the ohpm commands do not work in the CLI.

**Solution 2**

In the configuration file, add the path to the **bin** folder in the ohpm directory to the **PATH** environment variable. The following uses the macOS Zsh command line tool as an example.

1.  Open the terminal and edit the **~/.zshrc** file.
    
    vi ~/.zshrc
    
2.  At the end of the file, add the following line to add the aforementioned **bin** directory (**/home/tctAdmin/ohpm/bin** in this example) to the **PATH** environment variable:
    
    export PATH="/home/tctAdmin/ohpm/bin:$PATH"
    
3.  Save the **~/.zshrc** file and exit the editor.
4.  Run the following command to make the changes take effect, or close the current CLI and open a new CLI:
    
    source ~/.zshrc
    
5.  Run the **ohpm -v** command to check the ohpm version number. If the terminal outputs the version number information (for example, 1.0.0), the operation is successful.
    
    ohpm -v
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/bUQejOFlT96oiMDsb7Nzjg/en-us_image_0000002194318372.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11965A6C92FC2880DAD7BB38A01DD667F8710C82DDE82200C2DFEED21DB0A9F7)
