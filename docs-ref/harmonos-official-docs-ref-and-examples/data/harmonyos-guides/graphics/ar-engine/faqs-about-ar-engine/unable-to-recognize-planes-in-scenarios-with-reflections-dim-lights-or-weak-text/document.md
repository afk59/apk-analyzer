# Unable to Recognize Planes In Scenarios with Reflections, Dim Lights, or Weak Textures (Where There Is Little Color Variation in the Input Images)

#### Problem

During the usage of the environment tracking capability, if the input images contain reflections or weak textures (where there is little color variation in the input images), or the environment is dim, the number of detected point clouds may decrease or be zero, and the time to detect planes may be longer or planes may not be generated.

1.  Reflections: specular surface, smooth marble floor, etc.
    
    **Figure 1** Specular surface  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/wuvRmLj7TwaVHYRti5u1Pg/en-us_image_0000002500426100.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08CDC240EA1FAC4B6E9671A856DC91E1EAB633BB4D55C75858A6443FF001B076 "Click to enlarge")
    
2.  Dim light: roads at night, or scenarios where the camera is blocked
    
    **Figure 2** Road at night
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/nQu7fJl_SoOnvLOQ8rrwjA/en-us_image_0000002500426104.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6E4781822FF9F0383E8FC5E81EF963CA195BE46136F42FDC0939B9ED6166D1B "Click to enlarge")
    
3.  Weak textures: solid-color cabinets, tables, and walls
    
    **Figure 3** Wall
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Sv2QyX4TQQ6FSvAB1I0B-Q/en-us_image_0000002532306151.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=609E46272A9C86390958FF97B6BC71428DE7BC28581863E08579D0C5709BE6F7 "Click to enlarge")
    
    **Figure 4** Solid-color table
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/jFsH1xliRReALmfWwYPA6g/en-us_image_0000002532146183.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21DC62DF26711C5331C039E18CDF4F6D83AB588F90D0082F22563564B3D29570 "Click to enlarge")
    

#### Possible Causes

AR Engine calculates the feature points on a plane based on the input image data. If the input image data contains reflections, dim lights, or weak textures, AR Engine can obtain only a few points after calculation. As the plane is generated based on the identified point cloud, the plane generation takes a long time or even fails.

#### Procedure

When your app consistently fails to obtain the point cloud or plane data, prompt users to move the camera to avoid reflections, dim lights, or weak textures that continuously appear in the image.
