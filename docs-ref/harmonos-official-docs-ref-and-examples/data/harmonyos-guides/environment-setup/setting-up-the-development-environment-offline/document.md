# Setting Up the Development Environment Offline

If you are using a computer without Internet access, set up the development environment by following the instructions below.

#### Installing hypium

As the project-level **oh-package.json5** file in the project templates has Hypium configured as a dependency by default, you need to install Hypium. If you have other dependencies configured, you can follow similar steps to install them.

On the computer that has Internet access, create an empty folder (for example, **third\_library**) and in it create the **oh-package.json5** file. Add Hypium under **dependencies** in the file. The sample code is as follows:

{
  "dependencies": {
    "@ohos/hypium": "1.0.18"
  }
}

[Configure environment variables](../../coding-and-debugging/appendix/setting-up-the-proxy/document.md#en-us_topic_0000001056725590_li1012418311835). Then open the [CLI](../../command-line-tools/obtaining-command-line-tools/document.md#section21298572437) and run the **ohpm install** command. The **oh\_modules** folder and the **oh-package-lock.json5** file are automatically generated.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Dwiu6ueLS8W5VE-9Ap2Aog/en-us_image_0000002501070502.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26C2A27652061D905A3C142BA96CCEA395871DED3781846EAA89268281BD7AA1)

Copy the **oh\_modules** folder and the **oh-package-lock.json5** file to the root directory of the project on the computer where Internet access is denied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/owTYBvB1Sd-ElIMhRG6sOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=463948284779B9CCFE7A399794995D59120A5A3E9C2FEF51BB29531ED8D823AB)

The ohpm versions must be consistent across environments with or without Internet access; otherwise, the **oh-package-lock.json5** file may not take effect due to version mismatch.

#### Installing a Third-Party Library

You can install a third-party library using either of the following methods:

-   Method 1: Use [ohpm-repo](../creating-a-project/managing-modules/ohpm-repo-private-repository-setup-tool/document.md) to set up a private repository, publish the required third-party library dependency to that repository, and replace the value of **registry** in the [.ohpmrc](../../command-line-tools/using-ohpm/ohpmrc/document.md#en-us_topic_0000001792216397_%E6%96%87%E4%BB%B6) file with the private repository address.
-   Method 2: On the computer that has Internet access, create an empty folder (for example, **third\_library**) and in it create the **oh-package.json5** file. Add the third-party library dependency to the dependencies in the file:
    
    {
      "dependencies": {
        "@ohos/hypium": "1.0.17",
        "@ohos/lottie": "^2.0.0" 
      }
    }
    
    Open the CLI and run the **ohpm install** command. The **oh\_modules** folder and the **oh-package-lock.json5** file are automatically generated.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/wNt4BB2xTp-KRhPEqyobUg/en-us_image_0000002500910660.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3AAD4C4668F081D41729789585189566E148FD250ADF58902277FDC850953CC5)
    
    Copy the **oh\_modules** folder and the **oh-package-lock.json5** file to the root directory of the project on the computer without Internet access.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/yLRJPUNWSX2B_wj_4k6HZQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D341D24EBA50547EF9083B2C3ED70E78274E6486C058217CDD618783338B6B5)
    
    When using method 2, ensure that the ohpm versions are consistent across environments with or without Internet access; otherwise, the **oh-package-lock.json5** file may not take effect due to version mismatch.
    

#### Deploying an Emulator

For details, see [Deploying an Emulator Offline](../../coding-and-debugging/running-your-app-on-the-emulator/deploying-an-emulator-offline/document.md).
