# Screen Recording

During app development, you can use the screen recording feature to capture the app's running state and demonstrate its functional effects to others through the screen recording files.

#### Constraints

-   Before starting screen recording, unlock the device screen if a lock screen password is set. The screen recording app cannot be started when the screen is locked.
-   If a lock screen password is set, keep the screen unlocked during screen recording. If the screen is locked during screen recording, the screen recording app will exit.
-   The Emulator does not support this feature.

#### Using DevEco Studio

1.  Connect to a real device, and run an app on the device.
2.  On DevEco Studio, open the **Log** tab page.
3.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/AIGNwEMATKKymPMa7W1mwg/en-us_image_0000002500910732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ADFC56156DD71541085E794CB15E85CCA487276CED438F8DB707547749386E3 "Click to enlarge") on the toolbar on the left to start screen recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/GYwd3KCWQCazVrwHbZ8kbA/en-us_image_0000002532750597.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=557AB200828827E7AECD0A0A4410B6BDF6A40C7AABE754615BEC3D150F3B3947)
    
4.  Select the save path for the screen recording file. You can use the default path or [set a custom path](#section89111791511).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/dQ2vO5gUQliKcrQiglohjg/en-us_image_0000002501070578.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26E1A131D11A2B714CA6BC15C9D6E2338BB8D9477AFFABBB0DB6554B8F01B4C1)
    
5.  After the path is selected, click **Start Recording**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/kQHlHvkpQLqUedbnRZadKw/en-us_image_0000002501070574.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9C62EF3A7FBA00B68F1E811742B82805D723FA9917DE9D25758C350ACBA64C2 "Click to enlarge")
    
6.  When the recording is complete, click **Stop Recording**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/geKJkzteRbGCilxSxPq2iA/en-us_image_0000002532750599.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56C298F9DAC40BD05BCBBD7B28E17B35D9F86287FA337C151F60C00E1214F109 "Click to enlarge")
    
7.  A dialog box is displayed to indicate that the screen recording file is saved in the selected path, from which you can play the recording with a system media player or open the folder containing the file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/OGGMKoA8QNGfWay7R_bN3g/en-us_image_0000002532670647.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E60CE0F1DF2943A0B3D25009CFC018F357379266870E4A5D790A543F4F5D7785 "Click to enlarge")
    

#### Setting a Custom Path for Screen Recording

1.  Click the **Log** tab at the bottom and choose **HiLog** > **Settings** > **Record Screen**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/3SGs0sEbTKuOk2ANRvKvcA/en-us_image_0000002532670645.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B447B9D2A450D920F85620ECF17E24866D2CAAD044626411560C893FC981CEF5)
    
2.  In the dialog box that is displayed, select a custom path. After the path is set and **Use the selected path and auto-generated file name as defaults and don't ask again** is selected, the system automatically uses this path and a timestamp-based file name for saving the recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/CRJHrmVtSUycl7My5QI7VA/en-us_image_0000002500910736.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0EAA9CD647AA718BC4A600173057FEC1BD271BAA886C3F1B3DE0BC3CD6B739B)
    

#### Using Commands

You can use hdc, a command line tool primarily used for debugging, to record the screen. For details about hdc, see [hdc](../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).

1.  Start screen recording.
    
    hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility --ps "CustomizedFileName" "test.mp4"   // Set the name of the screen recording file to test.mp4.
    
2.  Stop screen recording.
    
    hdc shell aa start -b com.huawei.hmos.screenrecorder -a com.huawei.hmos.screenrecorder.ServiceExtAbility
    
3.  Obtain the path to the screen recording file, which will be used as the value of **{RecordFile}** later.
    
    hdc shell mediatool query test.mp4 -u
    
    -   If the query result contains the **uri** field, the screen recording file indicated on the third line of the return value cannot be directly downloaded, which means the file path cannot be directly used as the value of **{RecordFile}**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0BQ8w6UXSv6YTrFg2vtQ5A/en-us_image_0000002532670649.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5670F4CAB61439C5922A57D3F165F6B1612378B4366524EBB41FDE828FA33D7)
        
        In this case, run the following command with the value of **uri** to save the file to a path on which you have the download permission, for example, **/data/local/tmp**:
        
        hdc shell mediatool recv "file://media/Photo/2/VID\_1736853237\_001/test.mp4" /data/local/tmp
        
        The second line in the command output is the value of **{RecordFile}**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/h6XtwdIlSbq_W3eVQCKIHg/en-us_image_0000002501070576.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FB6C83F9D8522757DDEEFF7A8008D9CD0F6140C6764B8619AB663D96812FE37)
        
    
    -   If the query result does not contain the **uri** field, the second line of the return value is the desired value of **{RecordFile}**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/6H5D6afoTQ-WxgujaSYySA/en-us_image_0000002500910734.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062152Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB274859D7459E33DDF66D78110C7EC0C758A6F2082AF2D2309EBCD8AD3E971F)
        
    
4.  Run the following command with the value of **{RecordFile}** obtained in the previous step to download the screen recording file to the local device:
    
    hdc file recv {RecordFile} d:\\test.mp4
