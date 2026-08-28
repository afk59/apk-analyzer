# Deploying an Emulator Offline

If you are using a computer without Internet access, set up the development environment by following the instructions below.

**On a computer with Internet access**

Download and install DevEco Studio, then download the required emulator image. For details, see [Creating an Emulator](../managing-the-emulator/creating-an-emulator/document.md).

For example, to download a phone image on a Windows computer and specify the save path as **D:\\Sdk**, the actual full image path would be **D:\\Sdk\\system-image\\HarmonyOS-xxx\\phone\_all\_x86**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/zIP3LgpES6Kx4nSOifPL6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C85F5208AD1656AC27759A246CB601D498F5E53169F2AA3992FC16BEE3299812)

If the save path is not specified, use the default path. For details, see [Creating an Emulator](../managing-the-emulator/creating-an-emulator/document.md).

**On a computer without Internet access**

1.  Copy DevEco Studio and the emulator image files to the offline computer. The subfolder path for the image files (such as **system-image\\HarmonyOS-xxx\\phone\_all\_x86**) must be consistent between the computers with and without Internet access.
    
    Create a directory (such as **D:\\No-network\\Sdk**) on the offline computer to store the copied image files. Under this directory, create the folder hierarchy **system-image\\HarmonyOS-xxx\\phone\_all\_x86**, and copy all files from the **phone\_all\_x86** folder on the computer with Internet access to this corresponding path on the offline computer.
    
2.  Create an emulator on the offline computer. During creation, change the image path to the one used in the previous step (such as **D:\\No-network\\Sdk**). For specific steps, see [Creating an Emulator](../managing-the-emulator/creating-an-emulator/document.md). Once created successfully, the emulator is ready for use.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/JV8VN8FgQiuCAkz7oadScw/en-us_image_0000002507705952.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB6241BE1CE9070B446689C97829DA7BFBEC5FF8B1BEF83F3EEB7DC0A29C7556)
