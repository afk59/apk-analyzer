# Capabilities

AR Engine is an engine for building augmented reality (AR) apps on HarmonyOS devices, providing spatial computing capabilities such as motion tracking, environment tracking, and hit testing.

With these capabilities, apps can merge the virtual world with the real world, offering users a new visual experience and way of interaction.

AR Engine provides three capabilities: motion tracking, environment tracking, and hit testing.

#### Motion Tracking

AR Engine acquires camera data from the device, combines it with image features and the inertial measurement unit (IMU) sensor, calculates the device's position (translation along the x, y, and z axes) and pose (rotation around the x, y, and z axes) to achieve 6 degrees of freedom (6DoF) motion tracking.

**Figure 1** 6DoF motion tracking (the red arrows indicate the device's movement directions)  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/MoZruCANTIepgxfZNBob6w/en-us_image_0000002500426108.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45AC5F09F137829A690C75D6E4BADF012292B16575EF15ED86D0C1C4CE0000A9 "Click to enlarge")

#### Environment Tracking

AR Engine implements environment tracking by detecting and tracking planes and semantics around the device, and supports plane detection, plane semantics, target semantics, depth estimation, environmental mesh scanning, image tracking, and high-precision geometric reconstruction.

-   Plane detection
    
    AR Engine detects both horizontal and vertical planes (such as the floor and wall) and recognizes plane boundaries, so that apps can place virtual objects on these planes.
    
    **Figure 2** Plane detection (horizontal plane on the left and vertical plane on the right)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/joDZbzV_RgmiSwSQ7iMGYQ/en-us_image_0000002500426110.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E588F66A6671F058046BD46E211F87BCBAAB8A31F7B1BC50F8E3A6E2ABBF0408 "Click to enlarge")
    
-   Plane semantics
    
    AR Engine detects 11 types of planes: wall, floor, seat, table, ceiling, door, window, bed, plane space, cube volume, and cube space volume. Specifically, the plane space, cube volume, and cube space volume types are supported only in high-precision geometric reconstruction mode.
    
    **Figure 3** Plane semantics (the blue plane indicates the floor and the green plane indicates the table)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ta1rZTJzRVSbUF8kizG3og/en-us_image_0000002532146197.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0ACD84B9679D2D9C629B2E7FB6E1CAA1EFE2AF2640E3C7A66507423B0313E789 "Click to enlarge")
    
-   Target semantics
    
    AR Engine detects the shape of a target object on a plane, and supports the detection of rectangles and circles.
    
    **Figure 4** Object semantics (rectangle on the left and circle on the right)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/gi9_8t0mRHGNVljasHqjLA/en-us_image_0000002500306274.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EE51D25FC9004D32FB4F74E6A7ABDA6AAE33FB582D90B28F321A2F516C2866D "Click to enlarge")
    
-   Depth estimation
    
    This feature supports the continuous output of depth information of the surrounding environment relative to the device. By utilizing this depth information, a more natural and seamless fusion of virtual and real world experiences can be achieved. The depth information provided by this feature refers to the depth values from the device's camera to various points within the displayed scene, with each pixel containing its respective depth value. It also provides confidence data, enabling you to choose depth information that is either denser or more precise, depending on the needs of your app.
    
    **Figure 5** Depth rendering  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/VvQSqiXFSJuc6GzzMdZoLg/en-us_image_0000002500306276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF267C6DBDBFA2A501075BD02A39F119443CE50B77C2534C151C169EC21F833D)
    
-   Environmental mesh scanning
    
    This feature calculates and outputs the mesh data for the current image environment in real time, which can be used for the purposes of object occlusion.
    
    With the environmental mesh capability, a virtual object can be placed on any reconstructable surface, in addition to the horizontal and vertical planes. The reconstructed environment mesh can be used to implement virtual and physical occlusion and hit detection, so that virtual roles can accurately understand the 3D space around them, helping to achieve better immersive AR experience.
    
    **Figure 6** Environmental mesh scanning  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/ixMbOXreQcqlvLRrdkw_uw/en-us_image_0000002500306268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68EF299423580E0287928D82C97F37BB139450B222D0D19DDC10F9D0CBF2F660)
    
-   Image tracking
    
    AR Engine comes equipped with image recognition and tracking capabilities, detecting whether images provided by users exist in the setting, and outputting the image poses after recognition.
    
    With the image recognition and tracking features, AR effects can be applied to images in real-world settings, such as posters and covers. If a group of reference images are provided and they appear within the camera's field of view, AR Engine will track the images in real time to provide enriching and interactive perception.
    
    **Figure 7** Image tracking
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/TLGVzl0GTJ6RqF5GY15Z1w/en-us_image_0000002532306161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4198D961F82EC73928046DE1A356FA31239C68CE569C14C2CFA2142C631AA2E3)
    
-   High-precision geometric reconstruction
    
    AR Engine identifies cube objects or embedded cube spaces in a space and calculate the length, width, height, and volume of the identified objects or spaces. Volume measurement can be used to measure the volume of a cube and the size of an embedded space.
    
    High-precision geometric reconstruction supports dense point cloud drawing, volume measurement, and space recognition.
    
    **Figure 8** Dense point cloud drawing  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/lVJYt5ipTgSPG2vDd_BUXA/en-us_image_0000002532146193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37D402D8B119042390A611BD4C78209D784C6D336151EEBBCE279A27FEEC9FD8)
    
    **Figure 9** Volume measurement  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/14APanjlSrGIY3mAowWOuw/en-us_image_0000002532306157.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D80FF470F858073F0592353C12A9F14D94F579E3C73B1484BE255874CF40022)
    
    **Figure 10** Space recognition  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/0TM1dsB4RN-a3TFkBnDeLQ/en-us_image_0000002532306165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69C3C5D3243D014E49C0CB508AB4EF75B2A0F1DCA40BA95D112960902F9EBC15)
    

#### Hit testing

AR Engine uses the hit testing technology to map points of interest (POIs) on the device screen to POIs in the real environment. It casts a ray from a POI in the real environment pointing to the camera position, and returns the intersection where the ray meets a plane (or feature point). With hit testing, users can select POIs in the real environment by tapping on the device screen, to interact with virtual objects.

**Figure 11** Hit testing  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Tr_W51FPQVCTdRfTBa7zxQ/en-us_image_0000002532146189.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C98089BC8989558931CE965F7838FFFEB5B6B2B5B3BD135DA8CA7052925D5513 "Click to enlarge")

#### Use Case

These capabilities allow for development of apps featuring advanced AR capabilities, such as placing AR objects, offering users a new way to interact that seamlessly bridges the virtual and real worlds.

-   AR object placement: This capability utilizes the camera to create a virtual world and enables users to place virtual objects within it, making it ideal for use cases such as virtual home decoration.
-   Plane semantic recognition: You can perform semantic recognition for a detected plane, which can be wall, floor, seat, table, ceiling, door, window, or bed.
-   Target shape recognition: You can perform shape recognition for a detected target object, which can be a rectangle or circle.
-   Mesh scanning: Using the camera, the app can build an AR virtual world by reconstructing the mesh of the surrounding environment. This allows for virtual-physical occlusion and collision detection, enabling users to place virtual objects seamlessly within the virtual world. This enhances the immersive AR experience by sensing the surrounding 3D spatial environment.
-   Depth estimation: The app can continuously capture depth information of the surrounding environment through the camera. This provides a 3D environment perception capability. This technology can be applied in scenarios such as measurement, volume estimation, and scene reconstruction to obtain spatial object depth information. Based on this data, various spatial computation tasks, like calculating object volumes, can be accomplished.
-   Image tracking: By analyzing environmental data captured by the camera, the app can continuously check for an input target image in the scene. Once the image is detected, the app outputs the image pose.
    
    AR Engine comes equipped with image recognition and tracking capabilities, detecting whether images provided by users exist in the setting, and outputting the image poses after recognition.
    
    With the image recognition and tracking features, AR effects can be applied to images in real-world settings, such as posters and covers. If a group of reference images are provided and they appear within the camera's field of view, AR Engine will track the images in real time to provide enriching and interactive perception.
    
-   High-precision geometric reconstruction: The app can identify cube objects or embedded cube spaces in a space by using the camera to obtain the surrounding environment information and calculate the length, width, height, and volume of the identified objects or spaces. Volume measurement can be used to measure the volume of a cube and the size of an embedded space.
