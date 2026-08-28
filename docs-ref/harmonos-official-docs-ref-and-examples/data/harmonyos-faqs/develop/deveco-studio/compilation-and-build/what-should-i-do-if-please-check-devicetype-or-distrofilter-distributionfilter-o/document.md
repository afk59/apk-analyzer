# What should I do if "please check deviceType or distroFilter/distributionFilter of the module" is reported during compilation?

**Symptom**

One of the following errors is reported during compilation in HarmonyOS DevEco Studio:

-   Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/mJpqfKcfTK-Mx9_kpsf48Q/en-us_image_0000002229604261.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4703AA0C356DD6602B1BFCF132951D967E1BF9495CE06ADB9C2CA0030C5C959)
    
-   Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0-bFiPN1Qn-DzBEVovFI3Q/en-us_image_0000002194158880.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E356D3DC46576DCC00062D420B8DF8F52B5EFF5273C8A342793D0939E125D122)
    
-   Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Om4_3zhXQ8uJ_DyIoCQcPg/en-us_image_0000002194318488.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FB8639920F863A4A1081E0880F9A9627DD4162D65B93D60BDF28A948AF96216)
    
-   Module: (xxx) and Module: (xxx) have the same ability name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/GOqriGdARqav5GaGBC_2wA/en-us_image_0000002194318492.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51B6FCAC8D3E403916C272AC753D746696E81C8B365CCB0EEA8D1BB31AE79E3C)
    

**Solution**

-   Modify the project configuration by referring to [Logic for Checking HAP Uniqueness](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-verification-rule) to ensure that the project meets the logic for checking HAP uniqueness during packaging.
-   If only one device type exists in the project, ensure that the products corresponding to **applyToProducts** of different targets of the same module in the project-level **build-profile.json5** file are different.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/AKr5qGpdTdyjkmY8jMY8JQ/en-us_image_0000002194158884.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E64DCD30CC841FDD1D0D2CB8D9D992B15288064FD161EC3B16AAFBEEFC4E96D)
