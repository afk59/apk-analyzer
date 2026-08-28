# Obtaining Command Line Tools

The Command Line Tools package includes codelinter (code check tool), hstack (stack parsing tool), hvigorw (command line build tool), ohpm (third-party dependency management tool), and a series of tools contained in the SDK. This topic describes how to use the codelinter, hstack, and hvigorw. For details about how to use the tools contained in the SDK, see [Command Line Tools](../../system/debugging-tools/debugging-commands/about-this-kit/document.md).

#### Obtaining Command Line Tools

Go to [Download Center](https://developer.huawei.com/consumer/en/download/command-line-tools-for-hmos) to download the Command Line Tools, and verify the integrity by following the instructions in **Tool Integrity**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/4VVfyN7FTti6KTbJYTJccQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FC27D073650134675C973168406D6CCD82074A9CFE0F0D2EFDF2A80261890A4)

Since the HarmonyOS SDK is embedded in DevEco Studio, there is no need for separate downloads or configurations.

#### Setting Environment Variables

Decompress the Command Line Tools package. Tools such as codelinter and hstack are located in the **bin** directory under **Command Line Tools**. You must add this directory to the **PATH** environment variable.

## Windows

After decompressing the Command Line Tools package, add the **${_Command Line Tools decompression path_}\\command-line-tools\\bin** directory to the system or user **PATH** variable. Then, open the CLI again.

The figure below shows an example path when the Command Line Tools package is decompressed to the root directory of drive D.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/vY8NfT53Qe-WKon-Yh7SoA/en-us_image_0000002532670513.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5593D37856AC5953C6134643FB1CA4A7B928E41C3549E12F64FD63EDD03468C)

## macOS/Linux

1.  Decompress the downloaded command line tool to the local PC.
2.  Start the terminal tool and run the following command:
    
    echo $SHELL 
    
    -   If the command output is **/bin/bash**, open the **.bash\_profile** file.
        
        vi ~/.bash\_profile
        
    -   If the command output is **/bin/zsh**, open the **.zshrc** file.
        
        vi ~/.zshrc
        
3.  Press **i** to enter Insert mode.
4.  Enter the following content to add the environment variable to **PATH**. Replace the path with the actual storage path of the command line tool.
    
    export PATH=${Command Line Tools decompression path}/command-line-tools/bin:$PATH  
    
5.  Press **Esc** to exit the edit mode, enter **:wq**, and press **Enter** to save the settings.
6.  Run the following command for the environment variable to take effect.
    -   If the **.bash\_profile** file is opened in [Step 2](#en-us_topic_0000001169160500_en-us_topic_0000001056725590_li56571525162613), run the following command:
        
        source ~/.bash\_profile
        
    -   If the **.zshrc** file is opened in [Step 2](#en-us_topic_0000001169160500_en-us_topic_0000001056725590_li56571525162613), run the following command:
        
        source ~/.zshrc
        

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/nKj4ohHDTmWYi9Q2in4K4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92E3B21B7FB1608C81C5669A27FBB71AC36C3EB951419966F681EA92BDDF27DD)

To verify whether the configuration is successful, run the related commands. For example, run the **codelinter -v** command to check whether the codelinter tool version can be obtained correctly.
