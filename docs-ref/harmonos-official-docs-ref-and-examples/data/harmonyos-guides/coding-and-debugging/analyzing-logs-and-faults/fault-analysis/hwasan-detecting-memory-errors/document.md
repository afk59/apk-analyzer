# HWASan: Detecting Memory Errors

Hardware-Assisted Address Sanitizer (HWASan) is a memory error detection tool similar to [ASan](../asan-detecting-memory-errors/document.md). Compared with ASan, HWASan uses significantly less memory, making it more suitable for system-wide sanitization.

#### Constraints

-   HWASan is only available for hardware with AArch64 architecture.
-   ASan, TSan, UBSan, and HWASan cannot be enabled simultaneously; only one of these sanitizers can be active at a time.

#### Enabling HWASan

## Method 1

Choose **Run** > **Edit Configurations** > **Diagnostics** and select **Hardware-Assisted Address Sanitizer**.

## Method 2

1.  In the **AppScope/app.json5** file of the project, add the HWASan configuration.
    
    "hwasanEnabled": true
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/iCTUmZCNTlKNAuOiC4CHGA/en-us_image_0000002532750163.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF3D121AB141DD49FE760B0F3A8B5AC353A311AC7B1C3B1E6B61577632DC80DA)
    
2.  In the module where HWASan needs to be enabled, add build parameters to enable HWASan instrumentation. Specifically, in the **build-profile.json5** file of the module, add the following:
    
    "arguments": "-DOHOS\_ENABLE\_HWASAN=ON"
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/mcv09qBWTb6HDWcG7-aJNQ/en-us_image_0000002532750161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F963B6DD20BFB9346411ABA2BFF3E4F228164A96745F91AB817658B8C91207CA)
    

#### Using HWASan

1.  Run or debug the app.
2.  When a memory error occurs, the HWASan log information will be displayed. You can click the link in the information to go to the code that causes the memory error. For details about the description of each field in the log, see [HWASan Log Specifications](../../../../system/debugging-tools/performance-analysis-kit/fault-detection/address-sanitizer-detection/document.md#hwasan-log-specifications); for details about detectable error types, see [Detectable Error Types](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-hwasan-detection#section207321025115510).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/hQwKzyBtRKu0Rew2ospu7Q/en-us_image_0000002500910296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9924687671958B7426159D0F2FDC114A1B414085B74C0894ACDF41FDFE46DBA)
    
3.  If it is a release app and there is no source code available locally, you can use the AnalyzeStackTrace feature. Provide the .so file for which you want to analyze the stack trace; the analysis result will give you the source code addresses.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/scBnbM-mRU2t9LeODlksJw/en-us_image_0000002501070144.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EC020090DE5526C179CCD9DD29C8100A5EAF0C08CEEAF0DB6ECC79436DDF704)
