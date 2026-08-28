# Obtaining the Device Pose

#### Overview

AR Engine supports this capability since version 5.0.0(12).

The device pose describes the position and orientation of an object in the real world. AR Engine provides 6DoF pose computation in the world coordinate system, including the object's position (translation along the x, y, and z axes) and orientation (rotation around the x, y, and z axes). AR Engine allows for obtaining the pose of a device at any time in the space in real time.

#### World Coordinate System and Pose

The device pose is typically represented in the world coordinate system, which describes the absolute position of objects in real physical spaces, with its positive directions shown in the figure.

**Figure 1** World coordinate system  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/lB4udp1tRVOYPixmVyCOWw/en-us_image_0000002500426118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF340A331E99FD6B4C15E38CE61CA58A8C64EA6F063682EEE65C32116D8C79BA)

AR Engine will automatically initialize the world coordinate system.

In AR Engine, the device pose is described by a 7-dimensional vector, which consists of the rotation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/xDiKGM6sS0GGVDP0CZxTYw/en-us_formulaimage_0000002532306169.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5DC552466FD2DF3D9F214D26A2F3D0D2BF1723719D5385EF39E825531D5E4AC) and the translation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/O_pxnT0KRQKc93HUafe3nQ/en-us_formulaimage_0000002532306171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9CD28A4622014BBF9B5028941B3F7A91007F8CC3BEB3FE7B3BA54B4C3058598). The rotation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/_lcezmmPSbeQ8j6j-4A2lQ/en-us_formulaimage_0000002500306278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=462423E598FD6FC7A2F1021483529F4A805BFB70A8F4E1BDA9198AE15B0D417D) is a quaternion that describes the device's rotation state relative to the coordinate origin, while the translation component ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ba5h-DJKQOePhs2NDbwQ4w/en-us_formulaimage_0000002500306280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCDF16110C395D392F413652870FC0063EE2EDB1DE4ABF8B31F6F263A9ABC2F9) is a three-dimensional vector that describes the device's translation state relative to the coordinate origin, as shown in the following figure.

**Figure 2** Rotational and translational changes of the device pose  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/7BZmjp4UQhaMppvhd0FOdA/en-us_image_0000002532306167.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97E62A68F271F6C425E92854DAAE0742A72B1A79A62E22C6C5650BC3A140DA4B)

With rotation components and translation components, a device's pose state in space at any given moment can be described.

#### Importing AR Engine

For details, please refer to [Importing AR Engine](../managing-ar-sessions/document.md#section1410827131110) in **Managing AR Sessions**.

#### Creating an AR Session

Create an AR session by referring to [Managing AR Sessions](../managing-ar-sessions/document.md).

#### Obtaining the Current Device Pose

1.  Create an empty pose variable **cameraPose**.
    
    AREngine\_ARPose \*cameraPose = nullptr;
    HMS\_AREngine\_ARPose\_Create(arSession, nullptr, 0, &cameraPose);
    
2.  Obtain the camera pose at the current moment and store it in **cameraPose**.
    
    // Create an AREngine\_ARFrame object.
    AREngine\_ARFrame \*arFrame = nullptr;
    HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
    // Update the result of the current frame to arFrame.
    HMS\_AREngine\_ARSession\_Update(arSession, arFrame);
    // Obtain the camera parameter object of the current frame.
    AREngine\_ARCamera \*arCamera = nullptr;
    HMS\_AREngine\_ARFrame\_AcquireCamera(arSession, arFrame, &arCamera);
    // Obtain the camera pose information at the current time.
    HMS\_AREngine\_ARCamera\_GetPose(arSession, arCamera, cameraPose);
    

3.  Obtain different components of the camera pose from cameraPose, including the translation component and rotation component.
    
    float poseRaw\[7\] = { 0.0f };
    HMS\_AREngine\_ARPose\_GetPoseRaw(arSession, cameraPose, poseRaw, 7);
