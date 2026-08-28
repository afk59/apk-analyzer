# Terminal Environment Variables

During the execution of commands such as **hvigor** and **ohpm** within the terminal in DevEco Studio, the built-in environment variables are used by default, eliminating the need for additional configuration.

Configure the built-in environment variables in DevEco Studio as follows:

Choose **File** > **Settings** (**DevEco Studio** > **Preferences/Settings** on macOS) > **Tools** > **Terminal** and select the following options to enable the built-in environment variables:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/13Nhe8TxT-KHrtC4PZWzkA/en-us_image_0000002532750131.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93E558E45E8FA9B0ABEB3BC3B62FAE707A5FFE735480009E6EEAD1F98B064913)

In addition to the built-in environment variables, you can configure the **PATH** environment variable in the local system. If both are configured, the following priority rule applies:

-   Windows: The built-in environment variables take effect.
-   macOS: The effective variables are determined by the shell in use.
    -   For Bash, the built-in variables take effect.
    -   For Zsh, the local environment variables take effect.
