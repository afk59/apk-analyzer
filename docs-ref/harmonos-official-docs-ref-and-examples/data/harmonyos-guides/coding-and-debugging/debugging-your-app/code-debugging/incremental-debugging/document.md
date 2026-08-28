# Incremental Debugging

For large apps, the process of rebuilding, pushing packages, and installing after each code modification can be time-consuming. To address this issue, incremental debugging is provided in both DevEco Studio and command line. After code is modified, the debugger can identify code differences and build and push only the incremental package for debugging.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/yxZR5byARJqNZFuV88SUAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2705F62E5EE3E33E5B89B5011C87830BAAF0A43B3C20FB68BF1DB4FB7FE2671B)

Incremental debugging of C++ code is available for projects developed using API version 11 or later based on the stage model. Incremental debugging of ArkTS code, specifically for modifications to resource files, is available for projects developed using API version 12 or later based on the stage model.

#### Incremental Debugging in DevEco Studio

## Debugging C++ Code

1.  On the toolbar, select the device to be debugged and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/KPygRHrpQ_2yeXR1vlRhbQ/en-us_image_0000002532750263.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E07C48BB46CFC0BF686B383AF2615D6D054FB6F8F3CF2754EB94F149827B9A20) **Run** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/YqZ3RH6NTZWwOZTP3L7amQ/en-us_image_0000002501070238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83EA2252CEE8F4283706602CA9956E0C2459CC8E30ECC0ED98C11851FE240993) **Debug**.
2.  After modifying the C++ code, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Rx203xAfS6CQMS2FDej_cg/en-us_image_0000002501070240.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B65E4BA7B1178C22A6C0BE042BAEE32207AAE1DF2F9F3B1BC8FAA9E15E1CCCAF) **Apply Changes**.
    
    Then, DevEco Studio initiates an incremental build task, building an incremental package in HQF format. Once the incremental package is built, it will be pushed and installed on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/s-APvsetRPqB63sdA5a1vQ/en-us_image_0000002532750267.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82280C46EA4B98484E4D03166B9751B76D5514A6B5AD1BE4691840FB14A0322E)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/mrJ0cFL5Sw6pYTd6Nv_irg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB8189A1019035D8D07C1A8D0D01384FD6BFD1AF72C59929AAFB95C05AA48E51)
    
    The **Apply Changes** feature does not support the creation and deletion of code files, modifications to decorator-related code, or addition of new references using **import** statements.
    

## Debugging rawfile/resfile Resource Files

Incremental debugging of resource files in the **rawfile** folder is supported since DevEco Studio 5.1.0 Release.

1.  On the toolbar, select the device to be debugged and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/jqlWT0YwQVWUXosag_jR2A/en-us_image_0000002532750269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02202A61BC9D5369A7D618FB97ED2A4C331113553B1F9D290B9C6F6E60781D87) **Run** or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/epsyrJsiQX-TzmfOO6-HdQ/en-us_image_0000002500910392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48663352D360CF52D9D717F21429857EC8B192DA4AA2A51FE693D7293A89A651) **Debug**.
2.  Add or modify resource files in the **rawfile** or **resfile** folder under **resources** of the project directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/VrNL13liRLOHPtQlyWWQqA/en-us_image_0000002532670319.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6768018CD83A3D2163A42B48EB6144D731E60E32C4F9B20ECE341B7E3CAB1297)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/pMrcIEacQq2qWdvURf7qcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84E8EAE706BDB780E432956886C7938D270E1E190FC559D48ABD691B3A20BC3C)
    
    Currently, incremental debugging of **resfile** and **rawfile** resources is limited to the resource files that are explicitly called in the code.
    
3.  Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/IiLfqB_xRcS593VneBN44g/en-us_image_0000002501070244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F187A996F5ACE03E58A6CA5D43ADEA282ED475E2EBD167989ABA34E287EFF4F2) **Apply Changes** to push the incremental package to the device.
    
    Then, DevEco Studio initiates an incremental build task, building an incremental package in HQF format. Once the incremental package is built, it will be pushed and installed on the device.
    

#### Incremental Debugging on Command Lines

## Building an .hqf Package Using hvigorw

1.  Check for the **build/config/buildConfig.json** file in the target module and its dependent modules. If the file does not exist, run the project in DevEco Studio to generate it.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ITsmLHGbSmOvGb1lRbhvTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7E79ADB51A051309C8A685FA9D670DCB982496E35EB9BD45E8FE5773A91B73B)
    
    If you have performed step 1, skip steps 2 and 3.
    
2.  Based on the required modules for running and their products and targets, write commands to execute the HAP or HSP build tasks. For example, if the **entry** module depends on the HSP module **library**:
    
    hvigorw --mode module -p module=entry@default,library@default -p product=default assembleHap assembleHsp --info --no-daemon
    
    For details about how to use the commands, see [hvigorw](../../../../command-line-tools/using-hvigorw/document.md).
    
3.  Run the hdc commands to install the HAP and HSP modules. For details about how to use the hdc tool, see [hdc](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
    
    $ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
    $ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
    $ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
    $ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
    $ hdc shell rm -rf data/local/tmp/99c24fdc44694c05be12491d0a48e139
    $ hdc shell aa start -a {abilityName} -b {bundleName}
    
    -   **abilityName**: ability name of the app.
    -   **bundleName**: bundle name of the app.
    
4.  If any resource file in the **rawfile** or **resfile** folder of the HAP/HSP module has been modified, create a **changedFileList.json** file in the **build/default/intermediates/patch/default** directory of the module, and list the modified files in the created file. If any resource file for the HAR module has been modified, list the modified files in the module that depends on that HAR module. The following is an example:
    
    {
      "resources": {
        "resFile": \[
          {
            "filePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources\\\\resfile\\\\test.txt",
            "resourcePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources"
          }
        \],
        "rawFile": \[
          {
            "filePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources\\\\rawfile\\\\test.txt",
            "resourcePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources"
          }
        \]
      }
    }
    
5.  After modifying the C++ code, run the .hqf packing command. Once the command execution is completed, you can find the corresponding products **entry-default-signed.hqf** and **library-default-signed.hqf** in the **build/default/outputs/default** output directories of the **entry** and **library** modules.
    
    hvigorw --mode module -p module=entry@default,library@default -p product=default assembleDevHqf --info --no-daemon
    
6.  Run the hdc command to install the .hqf package.
    
    $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
    $ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
    $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
    $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
    

## Building an .hqf Package Using the SDK Tool

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/DLKsWKVBRjqF5IwFoWu9MA/en-us_image_0000002532670313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D994DF45236BFC205D0AF1AC756643BD7A6FC8E923F7482AD16FAEB2D0B7D2B4 "Click to enlarge")

1.  Perform a full build of the app and install the app on the device.
    
    hdc bm install {hap\_path} // Use this command when the HAP is on the computer, where hap\_path refers to the path of the HAP.
    hdc shell bm install -p {hap\_path}  // Use this command when the HAP is on the target device.
    
2.  Use an independent build process to identify the .so files for building an incremental .hqf package. Based on the ABI compilation environment (which can be checked in the [abiFilters](../../../../building-an-app/configuring-your-build/configuring-for-c-builds/document.md#section0721057575) field of **build-profile.json5**), gather them into a specific directory. As shown in the example below, when the compilation environment is arm64-v8a, the files are gathered in the **change\_test** directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/u9f2XyzjRhipjilUXv0_Hg/en-us_image_0000002500910398.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A453DB0B321016B2EF9DBC118A5DBAA099903C828B0731A51EE3C99AED682ADE)
    
3.  (Optional) Modify resource files. If any resource file in the **rawfile** or **resfile** folder of the HAP/HSP module has been modified, create a **changedFileList.json** file in the **build/default/intermediates/patch/default** directory of the module, and list the modified files in the created file. If any resource file of the HAR module has been modified, list the modified files in the module that depends on that HAR module. The following is an example:
    
    {
      "resources": {
        "resFile": \[
          {
            "filePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources\\\\resfile\\\\test.txt",
            "resourcePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources"
          }
        \],
        "rawFile": \[
          {
            "filePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources\\\\rawfile\\\\test.txt",
            "resourcePath": "D:\\\\MyApplication\\\\entry\\\\src\\\\main\\\\resources"
          }
        \]
      }
    }
    
4.  Prepare a signature file consistent with the installed app.
    
    You can obtain the corresponding signature file from the project's **build-profile.json5** file.
    
5.  Prepare a **patch.json** file. The following is an example:
    
    {
        "app" : {
            "bundleName" : "com.ohos.quickfix",
            "versionCode" : 1000000, // App version
            "versionName" : "1.0.0",
            "patchVersionCode" : 1000000, // Patch version number. Each time you perform incremental debugging, increment the patch version number by 1 to make sure it is always be greater than the previous one.
            "patchVersionName" : "1000000"  // The value must match the patch version number.
        },
        "module" : {
            "name" : "entry",
            "type" : "patch",
            "deviceTypes" : \[
                "phone",
                "tablet"
            \],
            "originalModuleHash" : "" // SHA-256 value of the HAP to be fixed; leave it empty
        }
    }
    
6.  In the directory where the [HQF packing tool](../../../../system/debugging-tools/debugging-commands/packing-and-unpacking-tools/packing-tool/document.md#hqf-packing-command) is installed, which is **_DevEco Studio installation directory_\\sdk\\default\\openharmony\\toolchains\\lib** by default, run the following packing command:
    
    java -jar app\_packing\_tool.jar --mode hqf --json-path D:\\MyApplication\\entry\\patch.json --lib-path D:\\MyApplication\\entry\\change\_test --resources-path D:\\MyApplication\\entry\\src\\main\\resources --out-path entry-default-unsigned.hqf --force true
    
    In the preceding command, modify settings of the following parameters and keep the other parameters as they are:
    
    -   **json-path**: (mandatory) path to the **patch.json** file, which contains incremental package information. For details, see [Step 5](#li13802124619204).
    
    -   **lib-path**: path to the .so file to be packed. For details, see [Step 2](#li13802194642015). Note that the ABI compilation environment cannot be included in the path.
    -   **resources-path**: path to the **resources** folder that contains resources to be packed, including the **rawfile** and **resfile** folders.
    
    -   **out-path**: output path for the .hqf package.
    
7.  In the directory where the signing tool is installed, which is **_DevEco Studio installation directory_\\sdk\\default\\openharmony\\toolchains\\lib** by default, run the following signing command:
    
    java -jar hap-sign-tool.jar sign-app -keyAlias "OpenHarmony Application Release" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "OpenHarmonyApplication.cer" -profileFile "ohos\_provision\_release.p7b" -inFile "entry-default-unsigned.hqf" -keystoreFile "OpenHarmony.p12" -outFile "entry-default-signed.hqf" -keyPwd "123456Abc" -keystorePwd "123456Abc"
    
    In the preceding command, modify settings of the following parameters and keep the other parameters as they are:
    
    -   **keyAlias**: key alias.
    -   **appCertFile**: debug certificate file in .cer format.
    -   **profileFile**: debug profile file in .p7b format.
    -   **inFile**: .hqf file to sign.
    -   **keystoreFile**: keystore file in .p12 format.
    -   **outFile**: .hqf file that carries the signature information, generated after the signing.
    -   **keyPwd**: key password.
    -   **keystorePwd**: keystore password.
    
8.  Install the incremental .hqf package.
    
    $ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
    $ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
    $ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
    

#### FAQs

## Failed to Use Incremental Debugging of DevEco Studio

**Symptom**

If the .so file is modified and packed by using other development tools, the incremental debugging feature of DevEco Studio 4.1 Canary2 does not work.

**Solution**

In DevEco Studio 4.1 Canary2, if the native file exceeds 16 KB, the LLDB debugger holds the file handle by default when a breakpoint is hit. As a result, the file cannot be modified or saved during debugging.

To resolve this issue, use either of the following methods:

-   Method 1: Run the following command to disable the source code caching mechanism for the LLDB debugger. This will prevent the LLDB debugger from retaining file handles.
    
    settings set use-source-cache false 
    
-   Method 2: Upgrade DevEco Studio to 5.1.0 Beta1.
