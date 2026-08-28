# Introduction to Device Interconnectivity

For API 6.0.0(20) and later versions, cross-device photographing, document scanning, image selector, video selector, and image and video selector are supported. For versions earlier than API 6.0.0(20), only cross-device photographing, document scanning, and image selector are supported.

Device Interconnectivity enables a tablet or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/v4MtRk2DR9O3N6htogJnBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=511372756B9B6DCD07E706AF9121F4BF055000056FBFC2521B300B181BBC8856)

This section details how to use the photographing function. The operations relating to scanning and gallery functions are similar to the photographing operations.

A user may need to take some photos as material when using a rich text editing app (such as a memo or note app, or an email app) on a tablet or a 2-in-1 device. However, it can be inconvenient to use the current device to take photos. In this case, the user can leverage the photographing capability of Device Interconnectivity to specify a tablet or a phone in the app on the current device and open the camera of the tablet or phone to take photos. A phone or tablet is more suitable for photo-taking thanks to its mobility, support for easy framing, and powerful camera capabilities. The photos taken can be quickly sent back to the rich text editing app on the tablet or 2-in-1 device, helping the user efficiently design documents with images and text.

If there are multiple phones or tablets on the same network, the user can select different devices for photo-taking.

#### Operations Mechanism

Based on the distributed collaboration framework, the [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) (camera device list component) and [CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417) (dialog box component showing remote camera status) components are provided for cross-device photographing scenarios. Your apps only need to call the two components to implement cross-device photographing, rather than focusing on details such as data transmission and command control in distributed scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tVqulaQvRJGNru9NYVSN1Q/en-us_image_0000002394951637.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58C105DEDB06EEB2AB97197A51D18A9EA191D54BE8161E4410041CFB21FFBC8C "Click to enlarge")

The above figure shows the process of using the photographing capability of Device Interconnectivity.

1.  **Cross-device automatic link establishment based on the distributed collaboration framework of the system**
    
    Through the distributed collaboration framework of the system, the local device (2-in-1 device/tablet) is automatically connected to the remote device (phone/tablet) if the same account is signed in on both devices. The system automatically completes the processes such as device discovery, connection, and authentication, provides information about available remote devices supporting the camera function to your app, and displays the information through the [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) component.
    
    When one or two devices are available, the device information is directly displayed. When more than two devices are available, a submenu is automatically created to display the information in layering structure.
    
    | 
    Only One or Two Devices Are Available
    
     | 
    
    More Than Two Devices Are Available
    
     |
    | :-- | :-- |
    | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/0wyVq0VCQ4mCcNnx0C4Hqw/en-us_image_0000002453060049.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C73B57A2B5BBA809CCDB10DB92A5F1769F5576A247BE03B3019C2BAD47F970DD)
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/4NTkivqqS--C_sGdZPlSrQ/en-us_image_0000002419501080.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB2C087DEEE423D054C46D48A766A72C2EC67010A29807976B14858F45FA176B)
    
     |
    
2.  **User's operation in the app on the local device to wake up the camera**
    1.  A user selects a remote device through [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) in the app. The app initiates a cross-device photographing request through the distributed collaboration framework to wake up the camera on the corresponding remote device.
    2.  The system wakes up the camera on the remote device and displays the camera preview screen. The user can directly take photos.
    3.  The distributed collaboration framework sends the shooting status information of the remote device to the [CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417) component in real time. The [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) component displays the information on the app for the user to check.
        
        The status can be: photo-taking on the remote device, image importing, collaboration failed, Wi-Fi not enabled on the local device, or Wi-Fi or Bluetooth not enabled on both devices.
        
        | 
        Photo-Taking on the Remote Device
        
         | 
        
        Image Importing
        
         | 
        
        Collaboration Failed
        
         | 
        
        Wi-Fi Not Enabled on the Local Device
        
         | 
        
        Wi-Fi or Bluetooth Not Enabled on Both Devices
        
         |
        | :-- | :-- | :-- | :-- | :-- |
        | 
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/qq826467TUi7dqiXG6tpvg/en-us_image_0000002419537890.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F79F9429EEF0079A64685610E8F0B7405CAC454A6B5F63A068537C4FA076AF5 "Click to enlarge")
        
         | 
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/YTZfZBWiS1qlZ9FMklgOag/en-us_image_0000002453096813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDEDC55050B09FABDF92076526C1011C15328FFF3A9BF0263D437B002E215F6B "Click to enlarge")
        
         | 
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/LxBdmGsRQ-qSTGdHOFeTdg/en-us_image_0000002452936913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5644CE37227CCCCB415A2E7E21D14912CF4B43DF36044A7DCA2C59694AC0133C "Click to enlarge")
        
         | 
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/0hCFkKGQQbO2k8enYblVmw/en-us_image_0000002419378050.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D76E6F48759E2A9EBC492E507581BA540214C4FF24414B3C4481015DD094DE0 "Click to enlarge")
        
         | 
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Cj-RfdblT62A_7vUqoOoTA/en-us_image_0000002419537894.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0589320BDE626E31EB57C7ACF8587CB2D2D80EB16BF9A90482A530D75C53DA24 "Click to enlarge")
        
         |
        
        If the collaboration is failed, Wi-Fi on the local device is not enabled, or Wi-Fi or Bluetooth on both devices is not enabled, the user needs to enable the Wi-Fi or Bluetooth on the corresponding device as prompted and touch [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) again to trigger the process.
        
3.  **User's photo-taking with the remote device**
    1.  The user uses the remote device to take photos and confirm the photos, which are then sent back to the app on the local device.
    2.  Camera on the remote device is automatically closed, and the device returns to its original state.
