# ASan: Detecting Memory Errors

To achieve optimal performance of C/C++, the compiler and OS (Windows, Linux, and macOS) runtime framework do not perform security detection on memory operations. This is where Address Sanitizer (ASan) comes into the picture. ASan is integrated in DevEco Studio to detect C/C++ out-of-bounds addresses, and display error stack details and problematic code lines in **FaultLog**.

#### Constraints

-   Once enabled for any module in an app, ASan must also be enabled for the entry module. If ASan is not enabled for the entry module, the app exits unexpectedly during startup and a CPP crash error is thrown.
-   ASan, TSan, UBSan, and HWASan cannot be enabled simultaneously; only one of these sanitizers can be active at a time.

#### Enabling ASan

You can enable ASan in either of the following ways:

## Method 1

1.  Choose **Run** > **Edit Configurations** > **Diagnostics** and select **Address Sanitizer**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/saQ8q6AgRPSctrG4GtG4gA/en-us_image_0000002532670083.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=559A0BB5F90A99C79A9C5A21C8A4027240D4B7C52F17BC958F24FA5514B38456)
    
2.  If a local library is referenced, set **arguments** to **\-DOHOS\_ENABLE\_ASAN=ON** in the **build-profile.json5** file of the library module. This allows the .so file to be compiled in ASan mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/k9Y8nAv-SCSJlhdJ3fviaA/en-us_image_0000002500910162.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DB2911AF552CBF3ECBE77F5692FD73A92F44319C2E3D1FBF14BDC0767E2C2C7)
    

## Method 2

1.  In the **AppScope/app.json5** file of the project, add the ASan configuration.
    
     "asanEnabled": true
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/B7sC7HiGRx2JS64zR_mDIg/en-us_image_0000002532750033.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A69FCA584DC16C4CBB97EF221EC203F984D25B84F8AF5BF481261DE765F8EC83)
    
2.  Add build parameters to enable ASan instrumentation for the module.
    
    In the module where ASan needs to be enabled, add build parameters to enable ASan instrumentation. Specifically, in the **build-profile.json5** file of the module, add the following:
    
    "arguments": "-DOHOS\_ENABLE\_ASAN=ON"
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/56U4og4pQce5nQiUMlKjkg/en-us_image_0000002501070006.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F58BC9DE1CEF82DE54EC11B20C3978BCC0748927D03FCE7BE1D259935AD45042)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/o_I7wf9ASNeSxSCgYQ7Chg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=942A22D04892975031F8EC09D813928A14AA7CBD8466ACEF41E0EF9DD835FED4)
    
    Leaving this parameter unspecified will not cause errors. However, in this case, aside from a few memory errors that include **malloc** and **free** functions, ASan will not be able to detect other memory errors that require instrumentation for detection.
    

#### Configuring Parameters (Optional)

Configure **ASAN\_OPTIONS** to define behavior of ASan at runtime, including setting the detection level, output format, and the detail level of memory error reports. **ASAN\_OPTIONS** can be configured in the **app.json5** file or under **Run/Debug Configurations**. The configuration in **app.json5** takes precedence. If both methods are used, the settings in **app.json5** prevail. For details about how to configure **ASAN\_OPTIONS** and common parameters, see [Configuring Parameters](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-asan-detection#section1496994494018).

#### Using ASan

1.  Run or debug the app.
2.  When a memory error occurs, the ASan log information will be displayed. You can click the link in the information to go to the code that causes the memory error. For details about the description of each field in the log, see [ASan Log Specifications](../../../../system/debugging-tools/performance-analysis-kit/fault-detection/address-sanitizer-detection/document.md#asan-log-specifications); for details about detectable error types, see [Detectable Error Types](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-asan-detection#section12508111110451).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/FwoeNjbITGC_NSsxDuGPjw/en-us_image_0000002532670077.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EA15BDE6031BFE48E22FEC117F0DF035157DB58F0F78996A1ABA980D629F2CF "Click to enlarge")
