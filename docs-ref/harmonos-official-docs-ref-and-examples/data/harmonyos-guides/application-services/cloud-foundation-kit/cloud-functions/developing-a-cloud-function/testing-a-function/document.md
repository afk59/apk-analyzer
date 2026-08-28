# Testing a Function

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/7GlQXXQCTv29xm6epwxcQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BD41E168BB22245E571BFB9E462618D68D1BC16C28FA1EAF18CC9B7077CD924)

This section uses the latest function version as an example to describe the test method. To test a released function version, go to the **Function code** tab page on the details page of the function version and test the function version based on method 2.

You can test the created function in AppGallery Connect to check whether the function code can run properly. Go to the test page in either of the following ways:

-   Method 1: In the function list, click **Test** in the **Operation** column of a function, and test the function on the **Test function** page displayed on the right.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/gFMR4dZaQI-EMpwBDZ9_VA/en-us_image_0000002474214301.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B04C003089452107BB1AD332718B11274175BAF8185B3E2D35472873A5CB6CAE)
    
-   Method 2:
    1.  In the function list, click the name of a function to go to the function details page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/V6a37QimRNiAa7ALEK8a9w/en-us_image_0000002474214333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F04B985E9240B57A0ADC6F069237FAF2A014E207A5FAFA7C23D490E170FC018)
        
    2.  Click the **Function code** tab and click **Test**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/PXrwcBYdR1SszwfBLzzZRA/en-us_image_0000002440774512.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F63D399F9C62887EDF542EBF136DC8D46A2235449FEAFCB12AEE6223350DCD02)
        
    3.  On the **Test function** page displayed on the right, test the function using the default test event, a new test event, or a saved test event.
        -   Using the default test event
            
            Click **Test** to test the function.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/3H3TU_LAS8-bg2ZXPo2s9w/en-us_image_0000002440774488.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF925286077B8603ACE438BDF008B33AFE87388860A11F5064565F224303DA2F)
            
        -   Using a new test event
            
            To set the request body for calling the function, you can perform the following operations to set test parameters and save the configuration as a test event for future use:
            
            1.  Enter JSON-format event parameters in the **Event** text box and click **Save**. In the **Information** dialog box displayed, enter an event name and click **OK**.
                
                ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/pxNhXEuvS6OarzDGbDggdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBACAEAF65A33D26CD9665B7BE99E8D5746E0B21F8EDCAA18BA2DBEF80D90F03)
                
                The JSON object entered in the **Event** text box corresponds to the event format of the trigger and will be transparently transmitted to the function.
                
                ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/ngFNOsmFS1GV1N5j-k8oAQ/en-us_image_0000002474174509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6841F2849C1B13900F556340718A69455881ECDCB040FF9BAF4D3A7ED0427F4)
                
            2.  Click **Test**. The function will process the event and return the test result.
        -   Using a saved test event
            1.  On the **Test function** page, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/TA6_1-99RPunYic0Qlkt5w/en-us_image_0000002474174485.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41743B0DD04E639FB856A5EB099B4770C5890ECCAD74EBEF7CFFE743FA54A775) to expand the list of saved test events, click **Load** on the right of a saved event, and click **Test**. The function will process the event and return the test result.
                
                ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/bOrrbjbHRfGF8JdcSJPk7w/en-us_image_0000002440934368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBF943F0D19DCFBBDE795D8946F3E27C18D1C63AC748EC6645A2832B8E6D6076)
                
            2.  (Optional) Click **Delete** on the right of a saved event to delete it as needed.
                
                ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/x4PCInUGS6iEEXrvgj_6gg/en-us_image_0000002474174477.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BDFEAB7E43B6A79F13CE768369C1784CADB427698B4724AF1CD18E43283BD0B)
                
    4.  Check the test result.
        -   **Result**: displays the response result obtained after the test.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/TuRQaXkXQHWTb5TmcqKPUg/en-us_image_0000002440934376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21280CC24B5F9DCC01FD116576C398673D6288415FE2D92AB508867E87C73F5D)
            
        -   **Run logs**: displays logs generated by the logger API during function running. Logs of the DEBUG level or higher are supported. (The following is just an example.)
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/JtUT4ibXRSmVJPdnMFzRaQ/en-us_image_0000002474214373.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=047960EA17B9662C5C9F6DD34A5361E41CF3A251EA74138D3D3E050EC829A3D9)
            
        -   **Summary**: displays information about the test request.
            
            -   **Request ID**: ID of the test request, which is displayed as **X-Trace-ID** in background logs.
            -   **Duration**: E2E duration for function execution.
            -   **Version**: version of the tested function.
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/txVf5TTjQBa9W-bbyIU7eg/en-us_image_0000002440774476.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BCCAECA129E614703EFF8B257C04109DF6442C37A520BD13B2C73CBAA5B39D4)
            
    5.  To modify entry point file code of a function whose **Code input type** is **Edit code inline** during the test, directly modify the code in the code editor on the **Function code** tab page and then click **Submit** at the bottom of the page. After the function is updated successfully, you can click **Test** to test the modified code.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/YcfkjveMSPiRp722FH57-A/en-us_image_0000002440934356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0183E0B77126774DC45A3B04E5AD51F8E00F330CB44A71DB03CCF1FE7D8B169)
        
        To modify the code file of a function whose **Code input type** is **\*.zip file** during the test, you can modify the local code file, package the modified file, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/p_l7d5uST92SM1qOKyAT-g/en-us_image_0000002474214305.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA724AD62617BA11064039364FB4B471D61979ABBB9A550B810F62694F98B63D) to upload the packaged file, and click **Submit** at the bottom of the page. After the function is updated successfully, you can click **Test** to test the modified code.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ixeHRz_7S0W8ZyPCWpzqyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D7F56DD572CD61DEF1B55B5B732C9096D8CA5647CEB7DBAD36C0E2E1075E634)
        
        If a large amount of code is modified and the function memory setting needs to be changed, you can select a value from the **Memory (MB)** drop-down list box, and then upload the function deployment package.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Y0NGjiN4SCm8YrWmmNWghA/en-us_image_0000002474214353.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99805C18DABF20E4C8267D2B3C8242068C5CEEA2CA4E019AB5B0C84D3513F44F)
        
    6.  After the function is tested successfully, click **Export** on the **Function code** tab page to export the function deployment package. The exported package is named in _Function name_\__Function version_.zip format. You can view the function structure and file content in the package.
