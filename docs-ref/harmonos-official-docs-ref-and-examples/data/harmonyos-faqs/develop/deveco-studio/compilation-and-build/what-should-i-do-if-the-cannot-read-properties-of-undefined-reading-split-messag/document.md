# What should I do if the "Cannot read properties of undefined (reading 'split')" message is displayed during compilation?

-   Scenario 1:
    
    **Symptom**
    
    DevEco Studio displays the "TypeError: Cannot read properties of undefined (reading 'split')" message due to a mismatch between DevEco Studio and SDK versions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lKQSBiRDTPKCfiEl8cyMwQ/en-us_image_0000002264138776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C894B8C8660D39C2073CC19C74300694F941F6CE3403CFA96332D50743C963BF)
    
    **Solution**
    
    1.  Visit the [HUAWEI Developers website](https://developer.huawei.com/consumer/en/download/) to download and install the latest DevEco Studio.
    2.  Open the project with the latest DevEco Studio.
    3.  Follow the onscreen instructions for project migration.
        
        -   Click **Migrate Assistant**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5gg4PXgjTdG3KkqywQnJWQ/en-us_image_0000002264083104.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE2B307207567DB8DEA4E046CD7A0BB2E641971D5BCA9E67CB7970A25E834D09)
        
        -   Select the target version from the version list.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/rWeVmZX7QJqV-9p1gp4REQ/en-us_image_0000002264081160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A83971C003D4EBCA844EA4908BF3A8C3DAB8D95F0F770BB9CB487EFA511598C)
        
        -   Complete the project migration process.
        
-   Scenario 2:
    
    **Symptom**
    
    The "Error: Cannot read properties of undefined (reading 'split')" message appears when external module dependencies are referenced in the code but are not declared in the project-level **build-profile.json5** file. Although these dependencies may be correctly declared in the module-level **oh-package.json5** file, the project-level build configuration does not recognize them, resulting in the error.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/XHGKNN6BTWKGbi3uIdnkDg/en-us_image_0000002264140556.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1A5106DDE84CEE9567803B8E94264046850E5C469AED3022FDBB57C9E1144DC)
    
    **Solution**
    
    1.  Check the dependencies referenced in the involved module and make sure they are correctly declared in the **modules** field of the **build-profile.json5** file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/gdMlw8FJTHO7cYRNi6bNeA/en-us_image_0000002264140648.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=379EB51CD54BE66CECE51DB4EC37C1A250B01315F4B7241016BB471192AC3DEA)
        
    2.  Open the **oh-package.json5** of the involved module and make sure the dependencies are listed under **dependencies**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/3DTVg-OcReyLHZJziqwnFw/en-us_image_0000002298773813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFED3D9A9DF5436377C44FEF1C7D0259718073A4599ED973A64420D74430E380)
        
    3.  After making sure the dependencies are correctly declared, delete the **oh\_modules** cache directory from the project and recompile the project.
        
-   Scenario 3:
    
    **Symptom**
    
    The "Error: Cannot read properties of undefined (reading 'split')" message appears when a HAP depends on a bytecode HAR for compilation, but the module alias used in the import statement does not match the alias declared in **dependencies**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/f_9Wu1bSTper-NqJsX_xSA/en-us_image_0000002264083960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7EB0B43461E5C85AF738C49BDDCF57188A3F226F1D72316DAFA311B9B88E5868)
    
    **Solution**
    
    Make sure the module alias used in the import statement matches the alias declared in **dependencies**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5VGhCS1tQ0aCBjOyuIZvlQ/en-us_image_0000002298661041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74FB466FF02EB7824EFA90AFC47CD81CAE4C7BBEA40CD368774719DB7E86EE53)
    
-   Scenario 4:
    
    **Symptom**
    
    A dependency referenced by a bytecode HAR is declared under **devDependencies**. However, the Hvigor build system does not collect the dependencies declared under **devDependencies** during compilation, causing a failure due to missing dependencies.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/bRZCWSDlT8yjpJZ-X3ntZQ/en-us_image_0000002264141304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F0D55B45395456A895BF8316C8C2A502FF3084F9F5D05F8E856AB8845D6B5A1)
    
    **Solution**
    
    Move the referenced dependency from **devDependencies** to **dependencies**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Vws94RueTjmSoRvUrZBHhw/en-us_image_0000002264084432.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86116108BC2DCBEB597EBFBC96F5EE034261FD0AD950D7C6CA01057474874489)
