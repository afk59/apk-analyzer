# How do I share an HSP in an application?

To share an HSP in an application, you must upload the HSP package to a private repository. Since HSPs cannot be directly published to a private repository, they must first be converted into .tgz files as follows:

1.  Set the build mode to **release**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/P5YzYOCeSra7ZGpouFto-Q/en-us_image_0000002215625442.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062537Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1BAD67EFE7DA806BC6074071B498723472763E30D1F4C5249A41FFF3D7142A3 "Click to enlarge")
    
2.  Select the root directory of the HSP and choose **Build** > **Make Module {_libraryName_}** to start the build.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/OJGCT8lMR3KW3sNv6f4_aA/en-us_image_0000002215465626.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062537Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E62B7257C6D97AD3398E7DF51DE8912ED9E2DA307C88A2CDC74ABD08DFBF26E "Click to enlarge")
    
3.  After the build is complete, the HSP is generated in the **build** directory, where the .tgz file is used for uploading to the private repository. For details, see [Publishing Third-Party Libraries to ohpm-repo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo-quickstart#en-us_topic_0000001792256157_将三方库发布到ohpm-repo).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/eZV09EA5RYCNYhfu1GCSMw/en-us_image_0000002250545457.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062537Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBE161B6763A8D41CA220AD5A574DA3C6FB799F425B71E997B8F9ECE06B4B11F "Click to enlarge")
    
4.  Upload the .tgz file to the repository. Then, use the **ohpm install** command to install the dependency into the project. Be sure to add the dependency in the **dependencies** field of the **oh-package.json5** file. Once installed, the shared methods of the HSP will be available for use in the application.

**Reference**

[Creating an HSP Module](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hsp#section7717162312546)
