# Creating an Emulator

When Internet access is available, follow the steps below to create an emulator. For offline environments, refer to the instructions in [Deploying an Emulator Offline](../../deploying-an-emulator-offline/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/BKZ2d0gPQMW45RflF8RjBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46A38E3B84A8329A3244D879A9F9A260AF7556DA520088A8D876C0F125A9A11D)

On macOS, you may observe in the activity monitor that the memory occupied by the emulator process exceeds the configured value. However, the **Memory** metric displayed in the activity monitor does not reflect the actual physical memory consumed by the emulator process. For more details, see [Why does macOS activity monitor show high memory usage of the Emulator](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-app-running-23).

#### Procedure

1.  Choose **Tools** > **Device Manager** from the menu bar, and click **Edit** in the lower right-corner to set the storage path (**Local Emulator Location**) of the emulator instance. On macOS, emulator instances are stored in **~/.Huawei/Emulator/deployed** by default. On Windows, emulator instances are stored in **C:\\Users\\_xxx_\\AppData\\Local\\Huawei\\Emulator\\deployed** by default.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/nt6G9AaMS9SDXv0DZMYpSA/en-us_image_0000002532668713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4803D4277A11DA5449E65CADAD6C3253A458661ADA65E6D9E7D447D8B72B6E9B "Click to enlarge")
    
2.  On the **Local Emulator** tab, click **New Emulator** in the lower-right corner to create an emulator.
    
    On the emulator configuration page, you can select a default device template. If this is your first time using the device, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/IJ7HRlFVQaGRvlWmyI_5ng/en-us_image_0000002532668705.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88F3365DE6F83651FF27769F6D033FECCEC8954838B7FD2AEBF09AE4B32ED2D8) on the right of the device to download the emulator image. You can also update or delete the emulator image for different devices on this page. Click **Edit** to set the path for storing the image files. By default, these files are stored in **~/Library/Huawei/Sdk** for macOS and **C:\\Users\\_xxx_\\AppData\\Local\\Huawei\\Sdk** for Windows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/UY6r9TMNQKGC7aSHNqZIGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D70BAE8A262BC44C4CF9D287EBA56B523521503E706D9BB7AB828031DA8660)
    
    If the configuration page is not properly displayed, for example, the device list is empty, close DevEco Studio and clear the cache corresponding to the DevEco Studio version in the **~/Library/Huawei** (**C:\\Users\\_xxx_\\AppData\\Local\\Huawei** for Windows) directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/73qGjHjTTJOCGHk2U7x74g/en-us_image_0000002532668699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABAB415A1E76300B758A3FD22F15C7E4175289B27926E791CD3E40B8BC982FA0)
    
3.  Click **Next**. Verify the name, memory, and storage space of the emulator to be created, and then click **Finish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/amnAcKRDRgOyUyW9Oj8RQQ/en-us_image_0000002500908806.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B21C05F973BE044EF765A26A0FA7E744BFD9285F4B7C30602E80452FD53B9ADE)
    
4.  On the **Device Manager** page, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/W3EPmZvNQXCwj27-fvbpsA/en-us_image_0000002532668695.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9463A16D9E2ACBAF675E7AF48B9C80A9EDE2245AEB5F925E9E451258E9BA800) to start the emulator.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/vy8h88E9ROiuhKWLqJVCQw/en-us_image_0000002500908774.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB4476DF1FB31E062D646EC1992E8B3BA60EDD3F17CF6D2929FDBCC4C2354106 "Click to enlarge")
    
5.  Choose **Run** > **Run '_Module name_'** or click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/eWya6boFRHCBSrhc86G4RA/en-us_image_0000002500908772.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=925CE6803FEB12B142BD1B852C7EABB017093335740CAF56F320A349910BF204) in DevEco Studio.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/QKbbPoiJQv2AxLO2Vw33Mw/en-us_image_0000002501068658.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBDF56613B39FD58E5C6BEA3A3E365EA33C502336287FBAA34B74F952A303FD8)
    
6.  Once DevEco Studio has finished building and deploying the app/atomic service, the app/atomic service can run on the emulator.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/V8i29kRNTYiHuaF08M3TLg/en-us_image_0000002532668681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81B62C7061C575CD9184377102B73C0C0100CA0393AB31A1B8D810FBE7DC3663)
