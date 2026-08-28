# Applying for the Formal Permission on Live View Kit

After you've fully debugged the live view function on the debugging devices and confirmed that the design solution and function experience comply with the [Live View Design Specifications](../../live-view-design-specifications/document.md), you can apply for the formal permission on Live View Kit. When receiving your application, we'll review the design solution and function experience of your app. You will receive the review result within seven working days.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/B9pmVlViT4qGvT3LwR6m7w/en-us_image_0000002543471705.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD354DCEDCF28CC1AF04007144F10385A1180401DAC1BA1E8A7502C88733D30C "Click to enlarge")
    
2.  Find the project for which you want to enable Live View Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Lp2L8ACDSaeAV0Wgl2gx_A/en-us_image_0000002511871780.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A85A005E3823B9A5A326252CDA9FBF8777310DF4E15637048C63BFB2A1393DA9 "Click to enlarge")
    
3.  Go to **Grow** > **Push Kit** > **Settings**, select the app for which you want to enable Live View Kit, and click **Apply** next to **Live view**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/mQCQcJhTQoy7WMA7LA3JuQ/en-us_image_0000002543471703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12DF69BE35D22AA3FC6113733FCA033F18D509F7279B28A732FFE17222DCA2B0 "Click to enlarge")
    
4.  On the **Live view** page that is displayed, click **Try now**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/_k9Zgf1OTFuLWfkm4zgKkA/en-us_image_0000002543471701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBCDF83A6855A8B716F53914BAC3BA9A731AF50A27BC15435896E0B7756B357F "Click to enlarge")
    
5.  The **Live view** page is displayed. If your app has 1000 or more monthly active users and has been released, click **Apply** next to the required application scenarios in the **Application scenarios** list to apply for the Live View Kit permission in these scenarios.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/02B7a-YqT4-ooRvSt56pgg/en-us_image_0000002511871784.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0D43F920E1B281516409601117E1D6DA5A7A4B9D5A4E9B9DF720933D4771FC6 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/qhRhEFSBQ6S8x5uE6jroPA/en-us_image_0000002543551715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00F3899DB0CAB9372AFF549933D876C04447A99D2D178C2931F4F8B7FAE27955 "Click to enlarge")
    
6.  Enter the scenario description, scenario integration solution, and remarks as instructed, and submit the application. Then wait for approval. For details, please refer to [Application Filling Requirements for Live View Kit](#section1942365192213).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/V1ayq9VBS3KuMC-VGGAnZQ/en-us_image_0000002511871786.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=789ECADBE8C770240F1AA3C0382B1C0D1DA8B18F053CCE7D30523BC11251CDC0 "Click to enlarge")
    

#### Application Filling Requirements for Live View Kit

## Scenario Description

You need to fill in descriptions about the integration scenario, message display timing, and main display nodes. The information you provide will be used for customer service inquiries and other purposes. Please describe it in detail.

Example:

Take the ride hailing scenario as an example. You can describe the scenario as follows:
**Integration scenario**: After a user hails a ride, display live view messages about the ride progress including pickup and trip updates.
**Display timing**: after a user submits an immediate ride-hailing order, or 30 minutes before the start of a scheduled ride-hailing order
**Display nodes**: Calling driver, Driver on the way, Driver arrives at pickup point, Heading to destination, Arrived at destination - pending payment, Arrived at destination - payment completed

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/D1KM917eQai4EFlYbasN2g/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45C76737D6531E0893261F5F6B8D946AA439B2A93708A17BA7FD2481A598B5CB)

If your app supports another app's mini program, you need to specify whether this mini program is involved in the application scenario you request. If the other app's mini program is involved, ensure that there won't be multiple apps pushing live view messages for a same task. You need to attach the following documents to your application:

-   Proof of alignment communication with the mini program client. Both parties need to specify how the mini program client processes the tasks generated by the mini program in your app. For example, the mini program client does not display live view messages for the tasks generated by the mini program.
-   Contingency plan for policy changes. You need to provide a contingency plan for mini program client policy changes, to ensure consistent user experience.

The communication proof and contingency plan must be provided case by case based on the application scenario and mini program. If other mini programs are added to an application scenario in future, you need to submit the alignment communication proof and corresponding contingency plan for the new mini programs offline.

## Integration Solution

Combine screenshots of the approved integration solution's live network performance (including the widget, capsule, and lock screen effects as well as display timing of each status node) and major special cases' implementation effects into a single image. The combined image cannot exceed 3 MB.

Your Live View Kit integration solution must meet the requirements specified in the "Live View Design Specifications". You can design the solution based on the templates.

**Self-check Before Application**

Before applying for the Live View Kit permission, you need to perform a self-check on the effect and user experience of the live view function, and provide the self-check result in remarks. If a self-check item has been completed, mark √ in \[ \].

-   \[ \] The uploaded screenshots meet the live view design specifications.
-   \[ \] Each live view activity has an end event.
-   \[ \] Live view messages are consistent with the event progress and information in your app.
-   \[ \] A same event has only one live view.
-   \[ \] Solutions for major special cases have been considered and provided.
-   \[ \] The live view function in the specific scenario has been tested and meets the rollout requirements.
-   \[ \] I agree to the live view management specifications. If the live view does not comply with the design specifications or violates the scenario requirements, Huawei can revoke the permission for the scenario \[_Scenario name_\].

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/LtwbzV9HRAG2gMrQ8XoDmQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062110Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72A2ADC988DE01331FBE761788D8780C866BFF337916C9EE85237E09CAA0024C)

The formal permission application involves solution review, testing, and acceptance. After the solution passes the review, you must cooperate in testing and acceptance by providing the acceptance method and version. The entire process takes about 15 business days. Please check the application result in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) or your mailbox.
