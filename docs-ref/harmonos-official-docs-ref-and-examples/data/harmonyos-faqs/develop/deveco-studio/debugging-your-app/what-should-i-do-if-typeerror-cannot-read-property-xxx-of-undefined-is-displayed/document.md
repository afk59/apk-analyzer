# What should I do if "TypeError: Cannot read property xxx of undefined " is displayed during runtime?

**Symptom**

When you start debugging or run a C++ application or service, "error: install parse native so failed" is displayed during HAP installation, or "TypeError: Cannot read property xxx of undefined" is displayed during HAP running.

**Solution**

Make sure the ABI type configured for the C++ project matches that supported by the device. To do so, perform the following steps:

Typical scenario:

In 4.1.3.400 and later versions, the default value of the **abiFilters** field is **arm64-v8a**. By default, only the arm64-v8a ABI type is built. If the device does not support the 64-bit ABI type, the built package cannot run on the device. In this case, manually configure the value of **abiFilters** in **buildOption/externalNativeOptions** of **build-profile.json5** based on the AbI type supported by the device.

// HarmonyOS project
"buildOption": {
  "externalNativeOptions": {
    "abiFilters": \["arm64-v8a", "x86\_64"\]
  },
}
// OpenHarmony project
"buildOption": {
  "externalNativeOptions": {
    "abiFilters": \["arm64-v8a", "x86\_64", "armeabi-v7a"\]
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/L_h85V6cR723sFkWaYEYVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C41EBD6EAAB0EEC6EF550F296500FA5BF0B8F60EECBFF9EC5C3D0171BF16E25)

-   If the project has a dependent HSP or HAR module, make sure the ABI types configured for all modules that contain C++ code include the ABI type supported by the device.
-   If the project depends on a third-party library that includes .so files, make sure the appropriate ABI directory for your device, such as **arm64-v8a** or **x86\_64**, is present in the **oh\_modules/_third-party-library_/libs** directory.
-   For HarmonyOS applications, the SO files of the **armeabi-v7a** architecture are not supported in DevEco Studio NEXT Developer Beta1 (5.0.3.200) and later versions.

Common scenario:

1.  Connect the device to DevEco Studio.
2.  Open the CLI and go to the hdc directory: **_DevEco Studio installation directory_/sdk/default/openharmony/toolchains**.
3.  Run the following command to obtain the list of ABI types supported by the device, which include one or more of the following: default, armeabi, arm64-v8a, x86, and x86\_64.
    
    hdc shell
    param get const.product.cpu.abilist
    
4.  Depending on the obtained list, modify the **abiFilters** settings in the [Module-level Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-hvigor-build-profile-V5#section11914746114811).
    
    -   If the list includes only **default**, run the following command to check whether the **lib64** folder exists:
        
        cd /system/
        ls
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/I2YKCsswQTixJ4rRBkRHpA/en-us_image_0000002434852810.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A529F4270D47C43B07F4CCDF861CB8E5294B7A924F3DC95DB9FEA98AC709A27E)
        
        -   If the **lib64** folder exists, add the arm64-v8a type to **abiFilters**.
        -   If the **lib64** folder does not exist, add the armeabi type to **abiFilters**.
        
    -   If the list includes one or more of the following, add at least one of them to **abiFilters**: armeabi, arm64-v8a, x86, and x86\_64.
