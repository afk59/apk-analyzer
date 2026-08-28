# TSan: Detecting Thread Errors

ThreadSanitizer (TSan) is a tool for detecting data races. It consists of a compiler instrumentation module and a runtime library. When TSan is enabled, it can reduce performance by 5 to 15 times and increase memory usage by 5 to 10 times.

#### Function Description

## Use Scenarios

TSan provides the following detections:

-   Data race detection
    
    Data races occur when two or more threads access the same memory location simultaneously without proper synchronization, with at least one of the threads writing. Data races are one of the main causes of unpredictable behavior in multi-threaded programs.
    

-   Lock error detection
    
    TSan can detect the following errors related to locks:
    
    -   Deadlock: Two or more threads are waiting for each other to release a lock, preventing the program from continuing execution.
    -   Double unlock: A thread attempts to unlock a lock that has already been unlocked.
    -   Unlock without holding a lock: A thread attempts to unlock a lock that it does not hold.

-   Condition Variable Error Detection
    
    Condition variables are used for communication and synchronization between threads. Common errors include:
    
    -   Waiting without holding lock: A thread calls wait without holding the associated lock.
    -   Signaling without holding lock: A thread calls **signal** or **broadcast** without holding the associated lock.

## Error Reports

When TSan detects an error, it generates a detailed report, including:

-   Error type: for example, data race and deadlock.
-   Memory address: involved memory address.
-   Thread information: thread ID and stack trace of the thread creation involved.
-   Source code location: source code location and stack trace for each memory access.
-   Context information: access type (read/write) and access size.

#### Constraints

-   TSan is only available for API version 12 and later versions.
-   ASan, TSan, UBSan, and HWASan cannot be enabled simultaneously; only one of these sanitizers can be active at a time.
-   Enabling TSan could lead to significant virtual memory allocation, which potentially impacts other memory-intensive features, such as GPU-based graphics rendering.
-   TSan does not support static linking with the libc or libc++ libraries.

#### Enabling TSan

You can enable TSan in either of the following ways:

## Method 1

1.  Choose **Run** > **Edit Configurations** > **Diagnostics** and select **Thread Sanitizer**.
    
2.  If a local library is referenced, set **arguments** to **\-DOHOS\_ENABLE\_TSAN=ON** in the **build-profile.json5** file of the library module. This allows the .so file to be compiled in TSan mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/1rI1-7rFR5W2gVS-qyBfbQ/en-us_image_0000002532670343.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B2722DA1850788E9A69629708B59FEBB9F679AABFD905EF95CE52192B37EA5A)
    

## Method 2

1.  In the **AppScope/app.json5** file of the project, add the TSan configuration.
    
     "tsanEnabled": true
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/9JfpviFtTyCrpQNAsDjOQQ/en-us_image_0000002501070262.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBD194B69425B5C327D1338320294E5479C617529B2E75D1621EA88BD1946E10)
    
2.  Add build parameters to enable TSan instrumentation for the module.
    
    In the module where TSan needs to be enabled, add build parameters to enable TSan instrumentation. Specifically, in the **build-profile.json5** file of the module, add the following:
    
    "arguments": "-DOHOS\_ENABLE\_TSAN=ON"
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Lx8t7SBeSmGy1ncmXwXDfg/en-us_image_0000002532670337.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F580EF18DEE9603143B868B74B5EDBECE9F32FAAF584CB29790E9A8035BE137C)
    

#### Using TSan

1.  Run or debug the app.
2.  When a thread error occurs, the TSan log information will be displayed. You can click the link in the information to go to the code that causes the thread error.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/fzOpIKbcSReu4oBDefJzWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83730380DB4E23126C41DCED41EBEBF6F51764D76A1CB5738EFE3A6B6D10CB4B)
    
    When the **call\_once** API is used, TSan might report false positives. To suppress incorrect reporting, you can place **\_\_attribute\_\_((no\_sanitize("thread")))** before the declaration of the function that uses the API.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/0TlPu4cvT6GxG5HbpmUFtg/en-us_image_0000002500910420.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE352AC0CBBACA73277D609FB8A620ADF4D494188B7082F4C6BC6F5F1ACBAAD3)
    
3.  If it is a release app and there is no source code available locally, you can use the AnalyzeStackTrace feature. Provide the .so file for which you want to analyze the stack trace; the analysis result will give you the source code addresses.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Yj4RfBAXTSW36qgJgvabCw/en-us_image_0000002532670335.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FEE8F98F6524DCA022682FD82A142B3469460284A89EF2C4ED6C38D4F68FCE3 "Click to enlarge")
