# Compilation and Building FAQs

#### Memory usage is too high during compilation

**Symptom**

During compilation and build, memory or CPU usage is too high, resulting in issues such as slow response in DevEco Studio.

**Solution**

-   During hvigor build, memory usage during compilation can be reduced by decreasing cached data in memory and reducing the number of threads.
    
    You can add configurations to **hvigor-config.json5**.
    
    "properties": {
      // Setting to 0 means no memory cache configuration is enabled; the default value is 4; the smaller the value, the less data cached in the memory.
      "hvigor.pool.cache.capacity": 0,
      // The default value is the number of CPU cores minus 1, including ohos.arkCompile.maxSize; the smaller the value, the less memory used.
      "hvigor.pool.maxSize" : 5,
      // The default value is 5; the smaller the value, the less memory used.
      "ohos.arkCompile.maxSize": 3,
      // The default value true enables memory cache, which results in more memory used; the value false means the opposite.
      "hvigor.enableMemoryCache": false
    },
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/RjmyYD-4Q6y5LX8MEQIrgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FE4E93EE84E99168F235F08AD9E90BD97FE31D08EACD00441F8D1ACAD98751B)
    
    After the values of **hvigor.pool.maxSize** and **ohos.arkCompile.maxSize** are set to smaller numbers and **hvigor.enableMemoryCache** is set to **false**, the compilation time may increase.
    

-   If the preceding modifications do not yield significant results, you can compile in a non-parallel mode.
    
    -   On the menu bar, choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and deselect **Execute tasks in parallel mode (may require larger heap size)**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ckJwB4LzQeisxmeWumn6Jg/en-us_image_0000002501611980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B95D709215FE6FDF6142A8AEEAA64E626CCBD45801B12FA842065FF3C2D2D75)
        
    -   In the pipeline scenario, add **\--no-parallel** at the end of the command line. The following is an example:
        
        hvigorw assembleHap --no-parallel
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/W1nXx2J8RPuyv3kVjg-kWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=638AB2D39B82909297CADE4FAF958ACEB4EC69AADC2C9B4DA3D3236691F7090C)
    
    Using the non-parallel mode for compilation will reduce memory usage, but it may also lead to an increase in compilation time.
    

#### Build error occurs: "Cannot read properties of undefined(reading 'XXX')"

Rectify the fault based on the value of _XXX_. If the fault persists, refer to the final solution.

-   **Scenario 1:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'setEnabled')" occurs.
    
    **Cause Analysis**
    
    The **hvigorfile.ts** file contains the following code:
    
    import { hvigor, getHvigorNode } from "@ohos/hvigor"
    import { hapTasks} from '@ohos/hvigor-ohos-plugin';
    // Problematic code
    getHvigorNode(\_\_filename).getTaskByName('XXX').setEnabled(false);
    export default {
        system: hapTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
        plugins: \[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
    }
    
    **Solution**
    
    1.  Ensure that the specified task is a task in the current **HvigorNode**.
        
        For example, if the error occurs in **hvigorfile.ts** of the entry module, valid task names include the following: **default@SignHap**, **default@CollectDebugSymbol**, and **assembleHap**, as shown in the following figure.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/r_ej6fshRnmEiJwUqyI0FQ/en-us_image_0000002500910576.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6590635B13DA505242D418007A2F8075DA5848DAB3C895AFC9CD929E938BD9AF)
        
    2.  Use **getTaskByName** only in the [Hvigor configuration phase](../../overview/build-system-lifecycle/document.md#section746253616316) or later lifecycle phases, including **beforeNodeEvaluate**, **afterNodeEvaluate**, **nodesEvaluated**, **taskGraphResolved**, and **buildFinished**.
-   **Scenario 2:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'isSO')" occurs.
    
    **Solution**
    
    Upgrade DevEco Studio to 5.1.0.840 or later.
    
-   **Scenario 3:**
    
    **Symptom**
    
    During the compilation and build process, an error "Cannot read properties of undefined(reading 'getPluginId')" occurs.
    
    **Solution**
    
    Set **system** in the **export default** object in **hvigorfile.ts** to **appTasks**, **hapTasks**, **hspTasks**, or **harTasks**.
    
    import { appTasks } from '@ohos/hvigor-ohos-plugin';
    
    export default {
        system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
        plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
    }
    
-   **Scenario 4:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'getNeedExecTargetServiceList')" occurs.
    
    **Solution**
    
    Set the **type** field in **module.json5** of the module to match the **system** field of the **export default** object in **hvigorfile.ts**. For the corresponding mappings between **type** and **system**, refer to the table below.
    
    **Table 1**
    | 
    type in module.json5
    
     | 
    
    system of the export default object in hvigorfile.ts
    
     |
    | :-- | :-- |
    | 
    
    entry
    
     | 
    
    hapTasks
    
     |
    | 
    
    feature
    
     | 
    
    hapTasks
    
     |
    | 
    
    shared
    
     | 
    
    hspTasks
    
     |
    | 
    
    har
    
     | 
    
    harTasks
    
     |
    
-   **Scenario 5:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'app')" occurs.
    
    **Solution**
    
    Ensure that the **AppScope/app.json5** file exists in the project directory.
    
-   **Scenario 6:**
    
    **Symptom**
    
    When a unit test is performed in the Linux environment, the error "Cannot read properties of undefined(reading 'toString')" occurs.
    
    **Solution**
    
    Currently, unit tests are not supported in the Linux environment.
    
-   **Scenario 7:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'kind')" occurs.
    
    **Solution**
    
    Refer to the following code examples:
    
    // Negative example: empty array
    class w {
      public a: \[\]\[\] = \[\]
      test() {
        console.log("1", this.a\[0\])
      }
    }
    // Positive example
    class w {
      public a: string\[\]\[\] = \[\]
      test() {
        console.log("1", this.a\[0\])
      }
    }
    
-   **Scenario 8:**
    
    **Symptom**
    
    During the compilation and build process, the error "Cannot read properties of undefined(reading 'clear')" occurs.
    
    **Cause Analysis**
    
    Configure the following content in the **hvigor/hvigor-config.json5** file in the project root directory to open the stack.
    
    "debugging": {
      "stacktrace": true                /\* Disable stacktrace compilation. Value: \[ true | false \]. Default: false \*/
    },
    
    Check whether the stack content is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/P0Y6T70JSWqQgiKpDPT0ag/en-us_image_0000002500910522.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8087BD4524777CFB7A55F64256FDFC6C949A96D0FD6919496744702B5E78D10)
    
    **Solution**
    
    If your DevEco Studio is using third-party plugins, such as security hardening plugins, disable them and check whether the issue persists. If the issue persists, refer to the final solution.
    
-   **Final solution**
    
    If none of the preceding solutions work, open the stack and check the code based on the stack information.
    
    To open the stack, add the following content to the **hvigor/hvigor-config.json5** file in the project root directory:
    
    "debugging": {
      "stacktrace": true                /\* Disable stacktrace compilation. Value: \[ true | false \]. Default: false \*/
    },
    
    Check the **hvigorconfig.ts** and **hvigorfile.ts** files first, and then check other files.
    
    If no problem is found in the preceding files, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
    

#### Build error occurs: "Duplicated files found in module xxx. This may cause unexpected errors at runtime"

**Symptom**

During the compilation and build process, an error occurs: "Duplicated files found in module xxx. This may cause unexpected errors at runtime".

The error occurs when there are different versions of an .so file with the same name. For example, if you copy the .so file from the **har** module's product to the **libs** directory of the **entry** module, then there is a **libhar.so** file in both the **har** module and the **entry** module. In this case, if you configure the **entry** module to depend on the **har** module, the build of the entry module will result in an error.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/a28_OrcPQY6P6yedSGp0dA/en-us_image_0000002532750439.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3D20A2AA78C0076D8C28587BFD5630D6F7E9F9C2074FECDF3DFB39174F3B57E)

**Solution**

Use configurations such as **select**, **pickFirsts**, and **pickLasts** to choose the .so files to be used. **select** provides precise selection capabilities for native products, with a higher priority than **excludes**, **pickFirsts**, and other configuration items. **pickFirsts** and **pickLasts** pack the .so file with the highest priority. The priority order refers to the order of dependency collection, and the later it is collected, the higher the priority.

For details, see [Configuring for C++ Builds](../../configuring-your-build/configuring-for-c-builds/document.md).

Based on the preceding example, you can add a **select** configuration in the **entry** module's **build-profile.json5** file to choose the .so file from the **har** module, set **package** to the **"har"**, and **include** to **"libhar.so"**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/QZh7bRfDQaqIyckhRUpe6Q/en-us_image_0000002532670429.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20CBF8422A756AEA7B58862AB9D3323D6A40C48E045C38A0F90B06E378D17D88)

#### Build error occurs: "input module releaseType is different"

**Symptom**

When an App Pack is packaged, the message "input module releaseType is different" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jLQ2u1vJS16auUz1NvnUDg/en-us_image_0000002532670479.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C51C3F4789E8C8D700D4A3395408F64127D85D8F5140C14410455694876D72E9)

**Solution**

According to the module names indicated in the error message, check whether the **apiReleaseType** fields are consistent between the modules.

The **apiReleaseType** field is automatically generated by the compilation and build tool and is saved in the **module.json** file of the HAP/HSP. As shown in the figure below, first confirm whether this field is consistent between the modules. If there is an inconsistency, you need to repackage each module of the app with the same version of the SDK, and then package the App Pack.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/MxOYotHvQBmn_hY3EB7foQ/en-us_image_0000002532670381.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86DC8E144C28C02EE81DD1CF34892D65CCC79115EA9253FB8F762939C82095C7)

#### Build error occurs: "debug is different"

**Symptom**

When an App Pack is packaged, the message "debug is different" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/EBmBVSCARc6Y9qv4bMAaFQ/en-us_image_0000002500910456.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A19DC5453214CBEB6E896C098ABF6B5A021842C871BF1B36AB031197526C6971)

**Solution**

Based on the module names indicated in the error message, check whether the **debug** fields are consistent between modules, especially between local modules and externally referenced modules.

1\. The **debug** field is automatically generated by the compilation and build tool and saved in the **module.json** file of the HAP/HSP, as shown in the figure below. First, confirm whether the fields are consistent across all modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/vDV0nBfxR5u6KQfd2b8jnA/en-us_image_0000002532670397.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A75B9D0876DBD376521226D0CEFE70164A03F03C9EB8C28A8D68827C8011954)

2\. Set **Build Mode**, based on which the compilation and build tool generates the **debug** flag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Vfcxgfh4QlWGyl9e5KAmUA/en-us_image_0000002534099411.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C54BB2ECCE83EE582A299AA945B7F7570741389154D16A8631F1853D7860D79)

#### Build error occurs: "proxy data is duplicated"

**Symptom**

When an App Pack is packaged, the message "uri datashareproxy://bundleName/\*\* in proxy data is duplicated" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/i2VleYZoRIiHnYd9Lyn0eQ/en-us_image_0000002500910490.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42B78737CF99876A4C6D209587237D75AAF6711F0A94327F461AE025819E95C3)

**Solution**

The **proxyData** field lists the data proxies provided by the module and is only allowed to be configured in entry and feature modules. The URIs configured in different **proxyData** configurations must not be duplicated. In light of this, if the preceding issue occurs, check whether the **proxyData** configurations with the same URI is configured between modules.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/uCx4koi2QHC8EAaLzUwpBg/en-us_image_0000002500910472.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C3CA7DA80C35C6BE04D66FAAC7E711650432BE076F993EB2005A1EA9D96AAEF)

#### Compilation error occurs: "Init keystore failed: parseAlgParameters failed: ObjectIdentifier()"

**Symptom**

During compilation and build, an error occurs: "Init keystore failed: parseAlgParameters failed: ObjectIdentifier()".

hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details:   Init keystore failed: parseAlgParameters failed: ObjectIdentifier() -- data isn't an object ID (tag = 48)   Detail: Please check the message from tools

**Analysis**

Using a higher version of JDK to generate a key pair (.p12), and then using a lower version of JDK to execute the signing command, can lead to incompatibility, causing the .p12 file to fail to parse, and the signing to fail.

**Scenarios**

1.  When DevEco Studio generates a key pair, it uses the pre-installed JDK 17 by default. If a lower version JDK is used for signing locally, an error will occur.
2.  If a key pair is generated locally using a higher version of JDK, and signing is done through DevEco Studio, an error will occur since the pre-installed JDK 17 is lower than the locally used JDK.

**Solution**

Check the JDK version currently in use and the version used to generate the key pair, and use a JDK version that matches for executing the signing command.

#### Compilation error occurs: "generate SignerBlock failed"

**Symptom**

During compilation and build, an error occurs: message: generate SignerBlock failed.

hap-sign-tool: error: {errorcode:0,message:generate SignerBlock failed}

**Analysis**

The public and private key pair used for signing does not match. In this case, if you sign with the private key, verification with the public key will fail. Ensure that the private key (**keyalias**) and public key (**appCertPath**) are used in pairs.

**Scenarios**

1.  When the signing material is generated locally, the correct certificate signing request (.csr file) corresponding to **keyalias** is not exported. As a result, the public key does not match the private key corresponding to **keyalias** when the certificate is generated.
2.  The **keyalias** or **appCertPath** file is incorrect.

**Solution**

Select the correct, paired **keyalias** and **appCertPath** files.

#### Error message "java.io.IOException: DerValue.getOID, not an OID 49" is displayed during compilation

**Symptom**

During the compilation and build process, the error message "java.io.IOException: DerValue.getOID, not an OID 49" is displayed.

hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: java.io.IOException: DerValue.getOID, not an OID 49 Detail: Please check the message from tools

**Possible Cause**

The certificate file fails to parse, and the certificate's OID could not be found.

**Scenarios**

1.  The certificate has been tampered with.
2.  The **appCertPath** parameter has a non-certificate file passed in.

**Solution**

Make sure the certificate is correct.

#### Erro message "JS heap out of memory" is displayed during compilation

**Symptom**

The error message "JS heap out of memory" is displayed during compilation and build.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/zUKmkO_pQKmeRJ9JS3ApWw/en-us_image_0000002532750319.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16CFD177126E1DFBE4B6B0EAF4849A52A0858AC09593460D20BB307E8802637E)

**Solution**

The memory for running Hvigor is insufficient. When Hvigor of version 3.1.0 or later is used, modify the maximum memory for running Hvigor. Do as follows:

Select **Enable the Daemon for tasks**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/jvAF0GwwQFCr_TFAtO78vg/en-us_image_0000002533541757.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC68013C2B41795EE2BB11FE032C750B52B98A962582A8716B3B3B2EC0958048)

Set the value of **maxOldSpaceSize** in **hvigor-config.json5** to a larger value (for example, **8192**) based on the project size.

"nodeOptions": {
  "maxOldSpaceSize": 8192
}

#### Error message "JS heap out of memory" is displayed during compilation on Linux

**Symptom**

In a Linux environment, the system has 64 GB of memory. The hvigorw script is configured with **\--max-old-space-size=40960**. During the compilation and build process, an error "JS heap out of memory" occurs even though the actual memory usage has not reached the configured limit (for example, only around 20 GB is used).

FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
Writing Node.js report to file: report.20200512.172528.47517.24.011.json
Node.js report completed
1: 0xa295e0 node::Abort() \[node\]
2: 0x9782df node::FatalError(char const\*, char const\*) \[node\]
3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate\*, char const\*, bool) \[node\]
4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate\*, char const\*, bool) \[node\]
5: 0xd3a3b5 \[node\]
6: 0xd74f27 \[node\]
7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() \[node\]
8: 0xd481b9 v8::internal::Heap::MarkCompact() \[node\]
9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) \[node\]
10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) \[node\]
11: 0xd4aebf v8::internal::Heap::HandleGCRequest() \[node\]
12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() \[node\]
13: 0x104b803 v8::internal::Runtime\_StackGuard(int, unsigned long\*, v8::internal::Isolate\*) \[node\]
14: 0x13a5a99 \[node\]
Aborted (core dumped)

**Cause**

As a parameter related to the kernel's virtual memory subsystem, **vm.max\_map\_count** controls the maximum number of memory mapping areas that a process can have. It is commonly used to limit the number of files a process can open, especially in cases where a large number of memory-mapped files are used.

On Linux, the default value of **vm.max\_map\_count** is usually a relatively small number, such as **65530**. However, for some apps that require a large number of memory mappings or for specific use cases, you may need to increase the value of this parameter to allow for more memory mapping areas.

**Solution**

Change the value of **vm.max\_map\_count**.

-   Temporary modification:
    
    sysctl -w vm.max\_map\_count=new\_value
    
-   Permanent modification: Edit the **/etc/sysctl.conf** file and add or modify the following line:
    
    Vm.max\_map\_count=new\_value
    
    Save the file and run the following command to apply the changes:
    
    sysctl -p
    

#### Erro message "Cannot find module XXX or its corresponding type declarations" is displayed during compilation

-   **Scenario 1:**
    
    **Symptom**
    
    When the native file **(.so)** is referenced during stage model project compilation, the error message "Cannot find module _XXX_ or its corresponding type declarations." is displayed.
    
    **Solution**
    
    During compilation and build of the current stage model project, the syntax of the symbols exported from the native file (**.so**) is verified. If a native file (**.so**) without the corresponding declaration file (**.d.ts**) is referenced, the syntax verification tool reports an error message indicating that the corresponding declaration file cannot be found.
    
    If a similar problem occurs, perform the following to troubleshoot:
    
    1.  Create the **types/lib**_xxx_ directory in the corresponding **cpp** directory, add the **index.d.ts** file to the directory to declare the native type symbol, and add the **oh-package.json5** configuration file for the verification tool module querying.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/tLQL3yIbSuail9aBCSrjmw/en-us_image_0000002532670393.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC30EEF78655AC86E456E379B0A72BB2C24C940F0454684776D5A21D0C9FBCDA)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/LG8qyoV7TESYj5NBfgF0Jw/en-us_image_0000002532670433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF4EB238C087B49306E484BD23D52BCF8B221A103C97ACBF60BCA45B18FCC6FC)
        
    2.  Add the local dependency of the native module to **oh-package.json5** in the module referenced by the native module, and click **Sync Now** to synchronize the project as prompted. The following figure uses the entry module as an example to describe how to reference a native module.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/jCZY33KLSVWSKslrialT5w/en-us_image_0000002532750367.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1E99DD1D0192DCDD3BB10C952A67EEE73F3FB8BB6F55615756D56F2A0BDB046)
        

-   Scenario 2:
    
    **Symptom**
    
    When a third-party package is referenced, the build fails and the error message "Cannot find module '_xxx_' or its corresponding type declarations" is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/9fMErwQBRsCkYCjOeKMeRA/en-us_image_0000002501070374.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E566E07B5866F5F90E58A0169463CACDC38C5352DF2AC6BC8BF5E7F232039A52)
    
    **Solution**
    
    Open the **oh-package.json5** file of the corresponding module or project to check whether the third-party package has been installed. If the third-party package has not been installed, run **ohpm install** to install it. If the third-party package has been installed, check whether the **main** field is correctly configured. If the entry file is not configured or incorrectly configured, configure it correctly.
    
-   Scenario 3:
    
    **Symptom**
    
    The referenced package path is obfuscated. In the code, the path is directly concatenated to the end of the referenced package. As a result, the module cannot be referenced and an error is reported.
    
    Sample code:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/wZYHd0uWSROPGFatr51jkQ/en-us_image_0000002500910454.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49A2BDE16E4F5DB03196942953B14CE33C9E77393CC9DC1572FF9815A12F7090)
    
    It is referenced in the code as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/gb61VuAvTWepSwvzC99J9g/en-us_image_0000002532670451.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A18C215BB8A70F3B8B6E91DC3B4B6772BF60E3F75479BEBCCB7C193A73DFD480) In this case, the module cannot be found. As a result, an error is reported.
    
    **Solution**
    
    Change the reference mode to the recommended one.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/R4FJn84GSfyGRAYQ2x54IQ/en-us_image_0000002501070392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=757B89AFC94EC59DCE4B84FC94925830E6D2811AB4EBBC2BF097AB497C333CD7)
    
-   Scenario 4:
    
    **Symptom**
    
    The referenced module **oh\_package.json5** is incorrectly configured. The **ohpm install** command is executed and the dependency is successfully installed. However, an error message is displayed, indicating that the module cannot be found.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/TwwRCJ2_Ti6k4P61iMlvTQ/en-us_image_0000002500910586.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD88449207C702D9047FAA3AB853652EFC2624389E9DE9FFF770F10C41DF8BF8)
    
    The **types** field is incorrectly configured in the **oh\_package.json5** file of the referenced module.
    
    This field takes precedence over the **main** field. In other words, if the value configured in the **types** field does not exist, an error message is displayed, indicating that the module cannot be found.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/v4vM0VXPRCCXjoh8ZVq8GQ/en-us_image_0000002501070368.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E26D27A38134C6C4FDF955C229E8D59950BAC3563F1979AE786AE1D22CCA5DAB)
    
    **Solution**
    
    If the package does not contain the **d.ets** declaration, this field can be deleted. If the configured value does not exist or is incorrect, an error is reported.
    
-   Scenario 5:
    
    **Symptom**
    
    The name of the module referenced in **dependencies** of **oh\_package.json5** is different from that imported in actual use.
    
    For example, a module is referenced in **oh\_package.json5** as follows:
    
    "dependencies": {   "har": "file:../har" }
    
    However, in the actual code, the value followed by the **import** field is not **har** as configured in **dependencies**, such as **HAR** in uppercase. (Currently, this issue occurs only on Linux.)
    
    **Solution**
    
    Change the name of the module referenced in **dependencies** of **oh\_package.json5** to the same as that imported in actual use.
    
-   Scenario 6:
    
    **Symptom**
    
    The value of the **main** field in **oh\_package.json5** of the referenced module is inconsistent with the actual file name.
    
    **Solution**
    
    Change the case of the **main** field to be the same as that of the actual file name.
    
-   Scenario 7:
    
    **Symptom**
    
    The stage model project fails to be built, with the message "Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations".
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2KDpkDBvRpWwzyqr6gb_cA/en-us_image_0000002500910506.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62504D61F2A2DCACA69E0D5813CAC57E22696FAB940C7EA440C2ACFFAF8203A3)
    
    **Solution**
    
    This issue occurs when the project references a **.d.ts** declaration file that does not have the corresponding implementation file.
    
    1.  Search for **rollup\_plugin\_ignore\_empty\_module\_placeholder** in the **build** directory to locate the intermediate file where the error is reported, and find the corresponding project file based on the intermediate file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/H-KHyZmMRJiCWgJJqHAt6A/en-us_image_0000002532670449.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18FD097C3B5D3BE7AF637209018815D18C56CBC56F1CE924308423E55FA52FE5)
        
        Enter **rollup\_plugin\_ignore\_empty\_module\_placeholder** in the text box to locate the intermediate file where the error is reported.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lnXbEdyHQj2mdxHsFN5-mA/en-us_image_0000002501070316.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B5ED7D8574F4EFFE650B5CB41475865A63C5CF9D971A7E007BE4B20A307EEC5)
        
    
    2.  Explicitly declare a symbolic type reference by adding **type** to the reference type file:
        
        export type {T} from './type';
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YH_1ctx8RKyYl4kZT-MdrA/en-us_image_0000002532750453.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAEC22B3436C14F08105B334481EE0BAA6D22E04013923F25C8AFE326220D2A0)
        
    
    3.  In addition, check whether value type symbols are referenced from **d.ts/d.ets**. Do not declare value variables in the declaration file.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/omaS_nSJTGOT6gXwj5hJ_g/en-us_image_0000002532670415.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73B1661E14AA613E846E4E8E6774F537655D642B6CE19B41F7DDA6F12DE28FAB)
        

#### Erro message "Module 'xxx' has no exported member 'yyy'" is displayed during compilation

**Symptom**

The stage model project fails to be compiled and built. The error message "Module '_xxx_' has no exported member '_yyy_'" is displayed, where the _yyy_ symbol is exported from the _x_**.js** file using **export \* from '**_x_**.js'**.

**Solution**

During compilation and build of the stage model project, the syntax of the .js file is not checked. Therefore, when using **export \* from 'x.js'** to export symbols from an **x.js** file, "Module 'xxx' has no exported member 'yyy'" is reported where the symbol is referenced.

If a similar problem occurs, perform the following to troubleshoot:

-   Method 1 (recommended): Use the symbol explicit export syntax to re-export symbols from the _x_**.js** file.
    
    export { yyy } from 'x.js'
    

-   Method 2: Add a declaration file (**.d.ts**) of the _x_**.js** file and do not specify the file name extension during reference.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/PUU5oXvLTeWP4Janv6O73A/en-us_image_0000002532750455.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A2D8FF31BAAE7F98F6B0AC88DBC807BC3E7857DFEE432FA044E96E24A53B133)
    

#### Erro message "Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded" is displayed during compilation

**Symptom**

The stage model project fails to be compiled and built, and the message "ERROR: Could not load ${_file1_} (imported by ${_file2_}): Maximum call stack size exceeded" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/OGjRzGcmS8mE8_UVrH4Fig/en-us_image_0000002532670501.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3C36A61225D13357100AEFD92259EE7F8AAD665EE162E36683C35BF9583CC69)

**Solution**

This problem occurs because **file1** is the code outside the current project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/i6bED-H_Tz-988DP7htqIQ/en-us_image_0000002500910578.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C62C140EE74C78FCCD15AE50FCA652429580ECE4F177888A5F9A1984389E9110)

Create a **Static Library** module, migrate the code outside the project to the **Static Library** module, and reference **HAR** using **HAP** to implement cross-module reference.

#### Error message "Failed to get a resolved OhmUrl by filepath xx" is displayed during compilation

-   **Scenario 1:**
    
    **Symptom**
    
    When the dependency of a third-party package is configured in **devDependencies**, if the source code references the API in the dependency, the compilation fails. In the following example, the third-party package **@hms-security/ucs-appauth** depends on **@network/gr** in **devDependencies**. When the source code uses the API of **@network/grs**, the compilation fails and the error message "ArkTS:ERROR Failed to get a resolved OhmUrl by filepath _xxx_" is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/eNgZBxL3QGej4vJW8QOWGQ/en-us_image_0000002532750459.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B134BD91143DBDF9BFEF47FF6F2CF659B670A7B98932092C0027EBF138AE2E6)
    
    **Cause Analysis**
    
    1.  Find the source code file in yellow. The warning messages for dependencies are displayed.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/IRsWcOKxTe-qJKNNhex8UA/en-us_image_0000002500910504.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E97CAAA90D67C995F5F0D8F9B7D9C02C2FDA38D91FE8762118AFBE5F32347BA "Click to enlarge")
        
    2.  Go to the **oh-package.json5** file in the package and check whether the dependencies are configured in **devDependencies**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/BVX_QFyzQY6MkVCA2gLhOw/en-us_image_0000002532750419.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2920C0B8E31F13E607301ADF12D627AEAADD6842CDC51B4480A45802DAF2456F)
        
    
    **Solution**
    
    -   Provide an improvement suggestion to the package development team: Runtime dependencies cannot be configured in **devDependencies**.
    -   Import the third-party packages in **devDependencies** to the dependency upper layer.
    

-   **Scenario 2:**
    
    **Symptom**
    
    Compilation fails with the error message "ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/sjs0vo4cREuh43Fri5OEMQ/en-us_image_0000002532750335.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE7DB3371262BB542EA1CB94657346681CAE02D1297510A5A1F9AF9BC12D5DDE)
    
    **Cause Analysis**
    
    Check whether the **srcPath** path specified by field **modules** in the **build-profile.json5** file of the project directory is different from the actual path and whether the path uses incorrect letter cases.
    
    **Solution**
    
    Change the value of **srcPath** in field **modules** in the **build-profile.json5** file of the project directory to the actual path.
    
-   **Scenario 3:**
    
    **Symptom**
    
    Project A references a module of project B using relative paths. This reference causes an error.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/BgK5wO2PTI-a5aIdbNNa1g/en-us_image_0000002500910528.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D985AE494D4F4DC39ACA7BB7DC2818E1F506CFF6991B802A9C6965E871EC31B)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/e9BsujwYR9qQhGLzNsF8dw/en-us_image_0000002500910538.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=208691AEF8CE2063E6DF8BBC4DBAE2575A0363308C6FCF4D0A2FD4763CE2FF92)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SlDYxujaSN2fCxMwIWd-ng/en-us_image_0000002532670447.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA53C064134AA06D9CDF9BD0F8EC46D1ADE071C31B8EF2E9B28249B61369E8BD)**Solution**
    
    -   Transfer the HAR of project B to project A as a module reference for project A.
    -   Package the HAR of project B in advance and reference the module using **.har** in project A.
    -   Upload the module to the repository and reference it using the version number.
-   **Scenario 4**
    
    **Symptom**
    
    Compilation fails with the error message "Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx."
    
    **Solution**
    
    If the module containing **hvigor\_ignore\__xxxxx_** is a HAR module, check the **oh\_package.json5** file for the presence of **"packageType": "InterfaceHar"**. If it exists, remove it.
    
-   **Scenario 5**
    
    **Symptom**
    
    Compilation fails with the error message "Failed to get a resolved OhmUrl for 'xxx' imported by 'yyy'."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0AwPNcFDQ9uXIz6KqoG6fA/en-us_image_0000002501070354.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=618973F72B0A3A853155FBF266C1C223AA36A9D04ADE36623CBAB4C8B8EA80A8 "Click to enlarge")
    
    **Cause Analysis**
    
    1.  Check whether the module where yyy is located is a [bytecode HAR](../../configuring-your-build/building-a-har/document.md#section16598338112415). If the value of **useNormalizedOHMUrl** in the project-level **build-profile.json5** file is **true** (the default value is **false**), the bytecode HAR is built by default.
    2.  If the module where _yyy_ is located is a bytecode HAR, check whether the dependency _xxx_ is configured under **dependencies** in the project-level **oh\_package.json5** file but not in the module-level **oh\_package.json5** file of the yyy module.
    
    **Solution**
    
    -   Add the dependency _xxx_ to **dependencies** in the **oh\_package.json5** file of the _yyy_ module.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/uVPoePVCSLG0Ca2bX_NYBQ/en-us_image_0000002501070352.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F3B6119164F84B4E00672A5208DCFADCB1764F39492FBFC802AA5937CB71F2B "Click to enlarge")
        
    -   Change the _yyy_ module to a non-bytecode HAR, add the **byteCodeHar** field to the module-level **build-profile.json5** file, and set the field to **false**.
        
        "buildOption": { 
          "arkOptions": { 
            "byteCodeHar": false
          }
        }
        
-   **Scenario 6**
    
    Ensure that the current DevEco Studio version matches the SDK version. Choose **Help > About DevEco Studio** and **Help > About HarmonyOS SDK** to check the DevEco Studio and SDK versions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/l0tvZmoRTrWhUMCPFVZ6Aw/en-us_image_0000002500910590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=612024C17EA58626947515B5E7A2FDB42BBD0316C45CA7F9F3BAE4AE40706E1E)
    
-   **Scenario 7**
    
    **Symptom**
    
    The error message "ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx" is accompanied with the message "ERROR: ArkTS:ERROR failed to execute es2ab."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/UFO4cZ-oTJuZVmLT4mxDcA/en-us_image_0000002532750385.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02D124B2DC317D6F241DCEBA8D9C913276C7E2EDA6766121BD8FB8E36A920FD4)
    
    **Solution**
    
    The project references a non-standard module directory (that is, the directory does not contain the module description file **module.json5**). Create a **Static Library** module and migrate the code in **utils/common** to the **Static Library** module, and reference **HAR** using **HAP** to implement cross-module reference.
    

#### Error message "Property 'xxx' does not exist on type 'typeof BuildProfile'." is displayed during compilation

**Symptom 1**

The user-defined parameter **BuildProfile** is used. No exception occurs in the compilation phase, but the compilation fails, with the message "Property _xxx_ does not exist on type 'typeof BuildProfile'."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/QZhhLmFmTMePP0iXmPysyg/en-us_image_0000002501070394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=456628751BC9E7A829ED96A0C7061478F52000591277591E6B8863F6E9004FBD)

**Solution**

Check whether the key values of user-defined parameters configured in **targets** > **buildProfileFields** in **build-profile.json5** of the current module are the same. If they are different, change them to the same.

The following is an example of **incorrect** configuration that causes the compilation error:

"targets": \[
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName1": "default1"
          }
        }
      }
    }
  },
\]

Change all the key values of **buildProfileFields** in **targets** to the same. The following is an example:

"targets": \[
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            **"targetName"**: "default1"
          }
        }
      }
    }
  },
\]

**Symptom 2**

The custom parameter **BuildProfile** used is marked red by the compiler, and the build fails with "Property xxx does not exist on type 'typeof BuildProfile'." reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/PenCVT0MRtiiZWvTnMizyw/en-us_image_0000002532750325.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E2362A17DC532598DFBE80E3F0CC2B058696F7186047B16D0C326EF3E8F0496)

**Solution**

Ensure that the user-defined parameter is added to **buildProfileFields** in **build-profile.json5** of the current module.

#### PC stuttering occurs due to C++ project compilation

**Symptom**

For a C++ project with a large amount of code, the CPU usage is high during C++ compilation. As a result, the computer may freeze or respond slowly.

**Solution**

If a similar problem occurs, perform the following to troubleshoot:

Open the **build-profile.json5** file in the module and add the following configuration to **arguments**: Change the values of **compile** and **link** based on the CPU configuration of the computer. You are advised to set the sum of the values of **compile** and **link** to half of the number of CPU cores. For example, if the CPU has eight cores, set both **compile** and **link** to **2**.

"arguments": "-DCMAKE\_JOB\_POOL\_COMPILE:STRING=compile -DCMAKE\_JOB\_POOL\_LINK:STRING=link -DCMAKE\_JOB\_POOLS:STRING=compile=2;link=2",

It should be noted that if the values of **compile** and **link** are changed, the compilation duration may increase.

#### Error message "A 'undefined symbol' error has occurred" is displayed during C++ compilation

**Symptom**

During compilation of a HarmonyOS C++ project, the error message "A 'undefined symbol' error has occurred" is displayed.

**Solution**

The "undefined symbol" error typically indicates that the linker cannot find the definition of a specific symbol. This issue often occurs when source files are not compiled or linked correctly, or when the necessary library files are missing. To locate and rectify this issue, perform the following steps:

1\. Make sure all source files are included in the CMake build.

Check your **CMakeLists.txt** file to ensure that all relevant source files are included in the project.

Example **CMakeLists.txt**:

cmake\_minimum\_required(VERSION 3.10) 
project(MyProject)  
set(CMAKE\_CXX\_STANDARD 17)  
include\_directories(${CMAKE\_CURRENT\_SOURCE\_DIR}                    
                    ${CMAKE\_CURRENT\_SOURCE\_DIR}/include)  
# Add all source files.
add\_library(myProgram SHARED main.cpp myLibrary.cpp) 

2\. Confirm the symbol definitions in the source files.

Make sure symbols are correctly defined in all relevant source files. For example, check whether **myLibrary.cpp** includes the definition of **myFunction**.

**myLibrary.cpp**

#include "myLibrary.h" 
void myFunction() {     
// Function implementation
}

**myLibrary.h**

#ifndef MY\_LIBRARY\_H
#define MY\_LIBRARY\_H 
void myFunction();  
#endif 

3\. Check the compilation and linking order.

Make sure all source files and library files are compiled and linked in the correct order. CMake and Ninja usually handle this order issue, but problems may arise during manual compilation.

4\. Clean and regenerate build files.

Sometimes, build files may become corrupted or symbol definitions may be lost. Try cleaning the build directory and regenerating the build files:

hvigorw clean 1 

Alternatively, manually delete the .cxx directory from the module.

5\. Check library paths and linker flags.

If using third-party libraries, make sure the library paths and linker flags are correctly configured in the **CMakeLists.txt** file. Sample code:

cmake\_minimum\_required(VERSION 3.10) 
project(MyProject)  
set(CMAKE\_CXX\_STANDARD 17)  
# Ensure that the header file of the involved third-party library is added.
include\_directories(${PATH\_TO\_EXTERNAL\_LIBRARY}
                    ${PATH\_TO\_EXTERNAL\_LIBRARY}/include)  
# Add a source file.
add\_library(myProgram SHARED main.cpp myLibrary.cpp)  
# Link the third-party library.
target\_link\_libraries(myProgram PUBLIC /path/to/external/library) 

6\. Enable verbose compilation and linking output.

To understand the detailed compilation and linking process, you can enable more verbose output. Add the following to the **CMakeLists.txt** file:

set(CMAKE\_VERBOSE\_MAKEFILE ON)

7\. Check the Ninja output logs.

By default, Ninja generates a **.ninja\_log** file containing detailed information about the build process. You can check this log file to identify issues that occur during the build process.

cat {module}/.cxx/default/default/arm64-v8a/.ninja\_log 

Check the log file for the source file or header file containing the symbols.

8\. Use the nm tool to check symbols.

Inspect the symbols in the target file and library file to ensure that the symbol definitions exist.

You can do so with the nm tool in the SDK: **sdk/default/openharmony/native/llvm/bin/llvm-nm**.

Check the target file.

nm myLibrary.o | grep myFunction 

Check the third-party library file.

nm /path/to/external/library | grep myFunction

**Conclusion**

By following the above steps, you can locate and resolve the "error: undefined symbol" issue. When compiling a C++ project with CMake, Ninja, and LLVM, ensure that all source files and library files are correctly included in the project and that the compilation and linking options are correctly configured. If the issue persists, consult the compilation and linking output logs for clues to help you identify the specific cause.

#### Error message "A 'unknown type name' error has occurred" is displayed during C++ compilation

**Symptom**

During compilation of a HarmonyOS C++ project, the error message "A 'unknown type name' error has occurred" is displayed.

**Solution**

This error occurs when the compiler cannot recognize a certain type. This may be due to the type not being defined, the relevant header file not being included, or the path to the included header file being incorrect. To locate and rectify this issue, perform the following steps:

1.  Check for included header files.
    
    Make sure all necessary header files are correctly included in the source file. For example, if you are using a custom type or a type provided by a library, be sure to include the relevant header file in the file where the type is used.
    
    **Example**
    
    // main.cpp
    #include "myLibrary.h" 
    int main() {
         MyType obj;
         // Use a custom type.
         return 0;
    }
    
    // myLibrary.h
    #ifndef MY\_LIBRARY\_H
    #define MY\_LIBRARY\_H
    class MyType {
    public:
         MyType() {}
         void doSomething();
    };
    #endif
    
2.  Verify header file paths.
    
    Make sure the search paths for header files are correctly set in the **CMakeLists.txt** file. You can add header file directories using **include\_directories**.
    
    Example **CMakeLists.txt**:
    
    cmake\_minimum\_required(VERSION 3.10) 
    project(MyProject)  
    set(CMAKE\_CXX\_STANDARD 17)  
    # Add a header file directory.
    include\_directories(${CMAKE\_SOURCE\_DIR}/include)  
    # Add a source file.
    add\_library(myProgram SHARED src/main.cpp src/myLibrary.cpp) 
    
3.  Clean and regenerate build files.
    
    Sometimes, build files may become corrupted or symbol definitions may be lost. Try cleaning the build directory and regenerating the build files:
    
    hvigorw clean
    
    Alternatively, manually delete the .cxx directory from the module.
    
4.  Enable verbose compilation output.
    
    To understand the detailed compilation process, you can enable more verbose output. Add the following to the **CMakeLists.txt** file:
    
    set(CMAKE\_VERBOSE\_MAKEFILE ON) 
    
5.  Check the compilation output logs.
    
    By default, Ninja generates a **.ninja\_log** file containing detailed information about the build process. You can check this log file to identify issues that occur during the build process.
    
    cat .cxx/default/default/arm64-v8a/.ninja\_log
    
6.  Use CMake's **message** function for debugging.
    
    Add the **message** function in the **CMakeLists.txt** file to print some debug information to ensure that paths and variables are correctly set.
    
    **Example**
    
    message(STATUS "Source directory: ${CMAKE\_SOURCE\_DIR}") 
    message(STATUS "Include directories: ${CMAKE\_INCLUDE\_PATH}") 
    
7.  If the error-causing API is a system API, check the initial version in the corresponding API reference to confirm whether the API is available in the current version.

**Conclusion**

By following the above steps, you can locate and resolve the "error: unknown type name" issue. When compiling a C++ project with CMake, Ninja, and LLVM, it is crucial to ensure that all header files are correctly included and that the correct header file paths are set. If the issue persists, consult the compilation output logs for clues to help you identify the specific cause.

#### Compilation fails due to JDK version mismatch

**Symptom**

HarmonyOS apps or atomic services fail to be built in command line mode, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/_CEpRsYhRhSVO-VF4q41mQ/en-us_image_0000002501070410.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7083909735CE409587956BE15C2BF095C9CFB50654F10FC6F9D62A5A456CFA67)

**Solution**

This problem is caused by a mismatch in the JDK version. To fix it, install JDK 17 as follows:

1.  Download and install JDK 17.
2.  Change the value of **JAVA\_HOME** to **JDK 17**. For Linux, see [Configuring the JDK](../../../command-line-tools/setting-up-a-pipeline/document.md#section195447475220).

#### Solution to LABEL\_VALUE\_ERROR

**Symptom**

The **LABEL\_VALUE\_ERROR** message is displayed during project synchronization or building.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/bpMBrimCSbqy3j5twnkL_A/en-us_image_0000002500910588.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2D9F415A622AF0FBD061E65AF83D9002ED0EEF763586176C6A576DF9779FDE0)

**Solution**

Set the **label** field in the **config.json** file to the resource reference mode.

1.  Choose **resources** > **base** > **element** and add the corresponding character string to the **string.json** file.
2.  Reference the string resource again in the **config.json** file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/umSIqa36SsOPkNBP2tub6w/en-us_image_0000002500910582.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=619E5493A4C5E4B1291108D6835C02294B7FFF3EE0482FCE4EB846EF5971FA8A)
    

#### Error message "Schema validate failed" is displayed due to missing start window information of an app/atomic service

**Symptom**

An error occurs during project synchronization or build, and the error message "Schema validate failed" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/gVPvKZikRte-y9QSX_ZtNw/en-us_image_0000002500910460.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78E0C5CFF36B0A36CE53277C6DA5CDEFF2FD19850685B72315D04200AFBB7C27)

**Solution**

During app/atomic service development, you can set the icon and background color of the startup window. The startup window settings are automatically configured when you create a project. If you accidentally delete a required field, the system generates an error to alert you and prevent misconfiguration. The following describes how to reset the startup page information. You can customize the icon and background color of the startup page.

To improve the cold start performance of your app/atomic service, you can set the icon and background color on the startup window as follows:

1.  Right-click **resources** > **base** > **element** and choose **New** > **Element Resource File** from the shortcut menu to create a resource file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/fbL_gWQiTVC7nfDRyWBDsA/en-us_image_0000002532670369.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88556603BCD8EE87CC8E1B0F6BDA8D9F053DA187E9D25687BBAFEA9CE98D1586)
    
2.  In the dialog box displayed, name the file, for example, **color**, and set **Root element** to **color**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/gjSi9wfGS6mgl-EbqlDbxg/en-us_image_0000002501070364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=536B718D252C580C40FBEB8C2980AF8FBF0D00FD3B67FF3514F75455412838FE)
    
    After the creation is complete, the **color.json** file shown below is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Mvlb5oj4Rj2RiT4lj6EtWQ/en-us_image_0000002501070304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F95B8F62656A4D25050A39AFBFA0936BBACCFA1448D16368193CA425D3711FD9)
    
3.  Copy the **color.json** file created in [2](#li124901748185712) to the **ohosTest** > **resources** > **base** > **element** directory of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/opTiwEmrQryeiPErcA25aA/en-us_image_0000002532750381.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE12346AE8EC231B4FCB34AD88221A7E791DC5CBE5E1A8887596180A9BEBCEAE)
    
4.  Add the **startWindowIcon** and **startWindowBackground** fields to the abilities array in the **src** \> **main** \> **module.json5** file of the module. If any field is missing, the error message "ERROR: Schema validate failed" is reported. The **startWindowIcon** field is used to index the icon resource in **resources** \> **base** \> **media** of the module, and the **startWindowBackground** field is used to index the color in **resources** \> **base** \> **element** > **color.json**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UD5l2sOvSP6Jo0xlwqjUSw/en-us_image_0000002500910584.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A4057C697D40C7B08000648AC9EBE4294812AEF303D9BCC30750AD02B9562DC)
    
5.  Add the **startWindowIcon** and **startWindowBackground** fields to the abilities array in the **src** > **ohosTest** > **module.json5** file. The **startWindowIcon** field is used to index the icon resource in **resources** \> **base** \> **media** of module **ohosTest**, and the **startWindowBackground** field is used to index the color in **resources** \> **base** \> **element** > **color.json**.

#### Error message "Schema validate failed" is displayed during compilation

**Symptom**

An error occurs during DevEco Studio compilation, and the error message "Schema validate failed" is displayed.

**Solution**

The cause is that some fields are missing or spelled incorrectly in the configuration file. Locate the fault based on the error details.

For example, if **name** in the **abilities** tag in **module.json5** is misspelled to **nam**, the following error information is displayed:

	 Detail: Please check the following fields.
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'srcEntrance' },
  message: "must have required property 'srcEntrance'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'required',
  params: { missingProperty: 'name' },
  message: "must have required property 'name'",
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'oneOf',
  params: { passingSchemas: null },
  message: 'must match exactly one schema in oneOf',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'enum',
  params: {
    allowedValues: \[
      'priority',
      'name',
      'srcEntrance',
      'srcEntry',
      'launchType',
      'description',
      'icon',
      'label',
      'permissions',
      'metadata',
      'visible',
      'exported',
      'skills',
      'backgroundModes',
      'continuable',
      'startWindowIcon',
      'startWindowBackground',
      'removeMissionAfterTerminate',
      'orientation',
      'supportWindowMode',
      'maxWindowRatio',
      'minWindowRatio',
      'maxWindowWidth',
      'minWindowWidth',
      'maxWindowHeight',
      'minWindowHeight',
      'excludeFromMissions'
    \]
  },
  message: 'must be equal to one of the allowed values',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 
{
  instancePath: 'module.abilities\[0\]',
  keyword: 'propertyNames',
  params: { propertyName: 'nam' },
  message: 'property name must be valid',
  location: 'D:/MyApplication/entry/src/main/module.json5:15:8'
} 

Below are the keywords in the preceding error information:

-   **instancePath**: location of the error in the file. **'module.abilities\[0\]'** indicates the first **abilities** in the **module.json5** file.
-   **keyword**: optional configuration property of the erroneous field, such as **'required'**, **'oneOf'**, **'enum'**, and **'propertyNames'** in this example.
    -   **required**: indicates that the field is mandatory but has not been configured, likely due to its absence or a misspelling.
    -   **oneOf**: indicates that the current configuration does not meet the **oneOf** requirement. As indicated by **instancePath**, the error lies with the **abilities** tag. To address this, in DevEco Studio, press and hold **Ctrl** and click **abilities** to go to the corresponding **module.json** file. You can see that one of the following two groups must be configured. A further check reveals that a spelling error has led to the **name** property not being configured.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Vuk5GIKJQmKxqZB-Cj6IGA/en-us_image_0000002532670467.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B5A71D1AECE1436AD72A22C59103B3E5AC0178910DCFAB508277FD07C41FA22)
        
    -   **enum**: lists all configurable properties in the tag. You can determine the correct spelling of the properties based on the enumerated values.
    -   **propertyNames**: indicates that there is a spelling error in the field. For example, **propertyName:'nam'** indicates that **nam** is an incorrect property name.
-   **params**: detailed information corresponding to different keywords. For example, if **keyword** is **required**, **params** with **missingProperty: 'name'** indicates that the **name** property is missing.
-   **message**: instructions on what needs to be corrected. For example, if **keyword** is **required**, **message** might state that the **name** property must be configured.
-   **location**: specific location of the error, which takes you to the error in the code upon a click.

#### Error message "No available entry module found" is displayed during compilation

**Symptom**

An error occurs during DevEco Studio compilation, and the error message "No available entry module found" is displayed.

**Solution**

The dependent entry module needs to be configured in the feature module. During compilation, DevEco Studio checks whether the entry module on which the feature module depends exists. If an error similar to above is reported, the possible causes are as follows:

1.  In the **build-profile.json5** file of the feature module, the name configured for the **entryModules** field is different from the actual name of the entry module. In this case, modify the value of **entryModules** to the name of the entry module.
2.  In the **modules** field of the project-level **build-profile.json5** file, the feature module is placed before the entry module. Since DevEco Studio configures modules from front to back during compilation, if the entry module is not read or configured when the feature module is configured, an error indicating that the entry module does not exist is reported. Place the feature module after the dependent entry module in the **modules** field.

#### Error message "keystore password was incorrect" is displayed during compilation

**Symptom**

What Do I Do If an Error Message "ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109." Is Displayed During DevEco Studio Compilation? Details: Init keystore failed: keystore password was incorrect" error information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/usp-WT1qQAmKgBduUNk6LA/en-us_image_0000002532670407.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C6C48CAD813B26D8B33AB9587F6B1A404D49691557E39563880F7DA710E32E4)

**Possible Cause**

The password of the keystore (.p12) is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/XXyK_HE2ROyWAc0DDHBcew/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D73C911B578AD6EC03157A0FC28CE3A91325BC4AD2C13AAD351C832BE410F7D)

**storePassword** and **keyPassword** are customized by the developer when the **.p12** file is created. Remember the passwords. The **build-profile.json5** file of the DevEco Studio project contains the ciphertext of the password. However, the signing tool requires the plaintext of the password. Therefore, the value in the **build-profile.json5** file cannot be directly used in the signing tool.

**Common Scenarios**

1.  Incorrect password.
2.  An actual password is required in the command line, but a ciphertext password is entered by mistake.
3.  The key (**keyAlias**) password is mixed up with the keystore (.p12) password.

**Solution**

The cause is that the signature password in the signature file is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/XYNbQUj2QQOuiBk2MUfKQw/en-us_image_0000002532750359.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94B4874F0580C4100FD5D8A1231DD5A29379E64BB6C251ABF3B7F058050367BA)

Developers can solve this problem by re-signing.

1\. Choose **File** > **Project Structure** > **Project** > **Signing Configs**.

2\. Select **Automatically generate signature**, wait for re-signing, and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/-YL09KtmTFK6brfnKqzPiw/en-us_image_0000002533542955.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46E7C15B79242C8D3423DF295B8F564DE0D207E9BC700E03CB495BB42CBD55A0)

#### Error message "please check deviceType or distroFilter of the module" is displayed during compilation

**Symptom**

An error occurs during DevEco Studio compilation. One of the following messages is displayed:

-   Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/N5pxz4eFRV-Be4oeChOizQ/en-us_image_0000002500910574.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27807DDF6105FDC1C5609B02E792B6AEBCB95CC0C4655B590F56E0A3ED2603AC)
    
-   Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/N6JGpnkfR1ytLH9mSukFcQ/en-us_image_0000002532670457.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75896B116672D580BED6CDA2D22F7E1A5187EBBA76FC26F5056EAF25917128C1)
    
-   Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/ohw4V3c4RyuP3CiPuFEKkg/en-us_image_0000002532670465.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9080441A584F02FED7E9661583F43EBF40DFCC6569220BA766FEE39A1AE2DF8)
    
-   Module: (xxx) and Module: (xxx) have the same ability name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/s2V9qxg-QDqo-HEPfCOGKg/en-us_image_0000002532670387.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA886ED0D045C723E2DFA475B9848DB9BCB3C2B0BF03BC5413FFB2401F395FCF)
    

**Solution**

Modify the project to ensure that it meets the HAP uniqueness verification logic during packaging. For details, see [Logic for Checking HAP Uniqueness](../../configuring-your-build/understanding-the-logic-for-checking-hap-uniqueness/document.md).

#### Error message "Failed to generate test project build system" is displayed during compilation

**Symptom**

During multi-module native build, the error message "Failed to generate test project build system." is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/GYh_BnVhRim-1aQ3mD1rGA/en-us_image_0000002500910556.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAB1B3B02F9C3C79E46467ECE7DB55B3769FAAF84DE41E817EB85583B9E9E32C)

**Solution**

Delete the **.c**_xx_ folder under the module that reports the error, select the module to be built, and run the **Make Module** **${**_moduleName_**}** command to build the module separately. Do not build multiple modules at the same time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/411MzPaMQ36fFzcTGG2vtA/en-us_image_0000002500910488.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA700A7B1631F2716D6008A9B22C77215A0284136473C37BE4DBAADBB710A0EB)

#### Third-party dependency library of a C/C++ project is not packaged into the HAP

**Symptom**

When a C/C++ project depends on a third-party **so.** file, the third-party **so.** file is not packaged into the HAP file after it is generated.

**Solution**

Currently, DevEco Studio has limited addressing modes for third-party **so.** files in C/C++ projects. If third-party **so.** files are not packaged into HAP, modify the **so.** file import mode.

1.  Define an alias (for example, **jsbind\_shared\_lib\_tracing**), indicating the third-party **so.** file to be imported.
2.  Use **SHARED IMPORT** to define the **so.** file import mode as dynamic import.
3.  Use **IMPORTED\_LOCATION** to specify the location where the **so.** file is imported.
4.  Declare the defined three-party **so.** file to the target.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/hKPXPINaRiKr4vhfjpfhPA/en-us_image_0000002500910518.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABD38E560623C35B1909A67BC746F53407151C20D2B4F8FEDC51C0F38BED434B)
    
5.  Generate a HAP again and ensure that the third-party **.so** file is packaged into the HAP.

#### Files in the src/main/cpp directory of the Static Library module are not packaged into the HAR

**Symptom**

Click **Build** > **Make Module ${**_libraryName_**}** to compile and build the HAR, files in the **cpp** directory are not displayed in the build product.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/kqalwnRuSVeXXWEETAWbCg/en-us_image_0000002501070412.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F7C2D8A3B0D100D0702FE40048F890764BDCF1FAE2623988D5626521782044E)

**Solution**

When Hvigor 2.5.0-s or later is used for HAR compilation and build, only the local dependencies specified in **dependencies** in the current module are included in the **.har** file. The dependencies specified in **devDependencies** are not included.

Move the corresponding local dependency to **dependencies** and recompile it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/tQZAbwxmTu2ph_AIjIC6LQ/en-us_image_0000002532750379.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6C7C75B58C6DE400A90CFEB6FD8DE172D7970E43B85115D5D05AB2D78A359F1)

#### Error message "ArkTS:WARN: For details about ArkTS syntax errors" is displayed during compilation

**Symptom**

During project build, the error message "ArkTS:WARN: For details about ArkTS syntax errors, see FAQs" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ijj3DuIBT3yGM7Ccpky9-Q/en-us_image_0000002501070384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7DC6D4AD8397FBDC117DD80AD0071028F7A05D0C90CFF360E939D5768E76CB7)

**Solution**

Check the error message for specific ArkTS syntax rule violations, which are enclosed in brackets, such as (arkts-no-var). Then, refer to the [TypeScript to ArkTS Cookbook](../../../getting-started/learning-arkts/migration-from-typescript-to-arkts/typescript-to-arkts-cookbook/document.md#use-let-instead-of-var) and modify your code to comply with the ArkTS syntax specifications.

#### Error message "ninja: error: mkdir(xxx): No such file or directory" is displayed during compilation

**Symptom**

An error is reported during native project compilation, and the following warning and error message are displayed:

A warning message is generated indicating that the length of the project directory exceeds 250 characters. For example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/yCD2E_oMQBCs_zbodqXaFA/en-us_image_0000002501070400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2040079DFB0F2BA99BB5F5210ECFFAA627E4D46F7684C10E34BD50A7DCB67715 "Click to enlarge")

The compilation error message "ninja: error: mkdir(_xxx_): No such file or directory" is displayed, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/eCyYpwMrTn2_s06mNzxhhQ/en-us_image_0000002501070390.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACC365537BDBF48A7AA4A6BDD7563C7E766640AA4E613DC5EB93B0CE1CCD120F "Click to enlarge")

**Solution**

The default value of **CMAKE\_OBJECT\_PATH\_MAX** is **250**. If the actual path length of the object file in the project exceeds this limit, a compilation error is reported.

You need to set **CMAKE\_OBJECT\_PATH\_MAX** in **CMakeLists.txt** based on the actual path length of the object file. The procedure is as follows:

-   Method 1: Add a file name length to the default value of **CMAKE\_OBJECT\_PATH\_MAX**.
    
    In the example, the warning message file is **TextMeasureCache.cpp.obj**, whose name contains 24 characters. Add 24 to the default value **250**, that is, configure it to **set(CMAKE\_OBJECT\_PATH\_MAX 274)**.
    
-   Method 2: Calculate the value of **CMAKE\_OBJECT\_PATH\_MAX** based on the actual path length of the object file.
    
    Calculation formula: **CMAKE\_OBJECT\_PATH\_MAX** = Total path length – Length of the directory in the object file + Number of characters in the CMake hash value (fixed at 32)
    
    -   Total path length = Length of the object file directory + Length of the object file. In the following example, the total length of the object file directory and object file is 297 characters.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/FOJTXysdSt6VpOspKRGC3A/en-us_image_0000002532750371.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57F22AF2A162E85F8955F71148FC247053ED38AC95D71DC5D9FDE93D82DCA1E2 "Click to enlarge")
        
    -   Length of the directory in the object file: In the example, the length of **\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager** is 74 characters. Replace it with the actual length.
    -   Number of characters in the CMake hash value: length of the hash value when CMake converts a long path to a hash value. The value is fixed at 32.
    
    Therefore, in this example, **CMAKE\_OBJECT\_PATH\_MAX** = 297 - 74 + 32 = 255, that is, set it to **set(CMAKE\_OBJECT\_PATH\_MAX 255)**.
    

#### Error message "(is the command line too long?)" is displayed during compilation

**Symptom**

An error is reported during native project compilation, and the following warning and error message are displayed:

A warning message is generated indicating that the length of the project directory exceeds 250 characters. For example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/vc3aJsSTQKeIJMMbNoVD0Q/en-us_image_0000002532750411.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C2A0C1AC4B14E0FD5C3F5CD19C9B9738472903EA386CF88C82A6BAC12001972 "Click to enlarge")

The compilation error message "(is the command line too long?)" is displayed, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/GAro4kPdTEmqeFITMVDi6A/en-us_image_0000002500910560.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6632BDDBF39FB2C9BA1651F0F04686276D1C9D1E62E8A1B7E6665AEFA020765C)

**Solution**

The default value of **CMAKE\_OBJECT\_PATH\_MAX** is **250**. If the actual path length of the object file in the project exceeds this limit, a compilation error is reported.

You need to set **CMAKE\_OBJECT\_PATH\_MAX** in **CMakeLists.txt** based on the actual path length of the object file. The procedure is as follows:

-   Method 1: Add a file name length to the default value of **CMAKE\_OBJECT\_PATH\_MAX**.
    
    In the example, the warning message file is **TextMeasureCache.cpp.obj**, whose name contains 24 characters. Add 24 to the default value **250**, that is, configure it to **set(CMAKE\_OBJECT\_PATH\_MAX 274)**.
    
-   Method 2: Calculate the value of **CMAKE\_OBJECT\_PATH\_MAX** based on the actual path length of the object file.
    
    Calculation formula: **CMAKE\_OBJECT\_PATH\_MAX** = Total path length – Length of the directory in the object file + Number of characters in the CMake hash value (fixed at 32)
    
    -   Total path length = Length of the object file directory + Length of the object file. In the following example, the total length of the object file directory and object file is 297 characters.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/EhliOHxNRFWjHSLwZyeaTw/en-us_image_0000002532670459.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=283A0F6E44B35BCFDF052F7DEF2C3E223FE59B2B43790752BCC85EED8015D62B "Click to enlarge")
        
    -   Length of the directory in the object file: In the example, the length of **\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager** is 74 characters. Replace it with the actual length.
    -   Number of characters in the CMake hash value: length of the hash value when CMake converts a long path to a hash value. The value is fixed at 32.
    
    Therefore, in this example, **CMAKE\_OBJECT\_PATH\_MAX** = 297 - 74 + 32 = 255, that is, set it to **set(CMAKE\_OBJECT\_PATH\_MAX 255)**.
    
-   Method 3: If the error persists after **CMAKE\_OBJECT\_PATH\_MAX** is correctly configured, change the project storage path to a shorter directory.
    
    After **CMAKE\_OBJECT\_PATH\_MAX** is correctly configured, CMake converts the long path into a 32-character hash value to shorten the path length. If the converted path is still too long, change the project storage path to a shorter directory.
    

#### Error message "CMake Error: The following variables are used in this project, but they are set to NOTFOUND" is displayed during compilation

**Symptom**

When **find\_path** is used in a native project, the following error information is displayed:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/1aP_9jg2QF2WfN9hEJSBOA/en-us_image_0000002532750327.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61F0E4142D191F6A84BC4504FA78C42A8E75791A8A467CD31E44A334A79528F4 "Click to enlarge")

**Solution**

In the CMake cross-compilation configuration file (**ohos.toolchain.cmake**) provided by the OpenHarmony SDK, the search path is restricted to **CMAKE\_SYSROOT**.

If you need to add a search path, use the **list** API to add a custom path in **CMakeLists.txt**. For example, add **D:demo** to the search path.

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

After the path is added, you can use **find\_path** to search files in the **D:demo** directory.

#### Error message "Unknown resource name" is displayed during compilation

-   Scenario 1

**Symptom**

In a project, module A references module B. When module A is compiled, an error message "Unknown resource name '_xxxx_'" is displayed, indicating that the resources of module B cannot be found.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/mGRcrXUpRymIKoNN9CGR8Q/en-us_image_0000002532670505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=319EA5F6DDD04EA04EFA8231819235D1C77B9EBDB79124498827125C865C1D41 "Click to enlarge")

**Solution**

Ensure that the following conditions are met:

1.  Resources must be stored in the **resource/base** directory.
2.  Module B has been installed.
3.  Module A references the resources of module B by the defined module name instead of the relative path.

-   Scenario 2

**Symptom**

The method of referencing a module is incorrect. If the code of another module is referenced, an error message is displayed, indicating that the resource cannot be found.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/RoMy1pO7QPChyxJLcwfVcg/en-us_image_0000002500910526.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E83332BFDA23B768CF73A217248E9874A873A52DADC35AD3282D647A1D5BA0AC)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/PwMzrJ45Sh2APwFKNVe23g/en-us_image_0000002501070326.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8088E0E5A9C63074CD995E17E128BA811388700B8C430AEDC4B34C72C57D60BF)

**Solution**

Add the module under **dependencies** in the **oh\_package.json5** module.

An example is provided as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/3Qpck6hkTmelPOoBNLQCxA/en-us_image_0000002532750331.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7396FA731664ED9FC52BAC2F4DB327DFD5DE68173763B41AC2CBF153BAE4BB79)

-   Scenario 3

**Symptom**

HSP A applies for a permission that references resources. When all components that depend on HSP A are built, an error message is displayed, indicating that the resources referenced by HSP A cannot be found.

**Solution**

Manually configure the corresponding resource in the referencing party.

#### Error message "ERROR: Task xxx was not found in the project xxx'" is displayed during compilation

**Symptom**

When the build command is manually executed on the CLI, the build fails and the error message "ERROR: Task xxx was not found in the project xxx" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/x1Zr7uYDSImtO2GSVUs79w/en-us_image_0000002532750365.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=216C06AF51441EA94E34AD6495A79A7B582FC14B661FF2FF5D9FC7F476AD178E)**Cause Analysis**

1.  Run the **hvigorw tasks** command to check whether the corresponding command exists.
2.  Check whether the **type** field in **module.json5** of the corresponding project matches the command execution module. As shown in the preceding figure, the **assembleHar** command is used to package the HAR module in the project. If the **type** field in **module.json5** is not **har**, the preceding error message is displayed.

**Solution**

1.  Run the correct command.
2.  Check the **type** field in **module.json5** of the corresponding project and run the corresponding command.

#### Error message "The reason and usedScene attributes are mandatory for user\_grant permissions" is displayed during compilation

**Symptom**

DevEco Studio compilation fails, and the error message "The reason and usedScene attributes are mandatory for user\_grant permissions" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/2qerskDxSyeCnQTyXK_iDg/en-us_image_0000002532750451.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADC4260BA39D0344B9088AAA19C7F1DDC107F639574EEE9DD3153D16B710B07E "Click to enlarge")

**Cause**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule is added: In an app package, the permission list **requestPermissions** under the module of all **Entry.hap** and **Feature.hap** must be specified. (**requestPermissions** can be left empty by default. If it is not empty, the **name** field is mandatory. For the **user\_grant** permission, the **reason** and **usedScene** fields are mandatory.)

**Solution**

Go to the corresponding **module.json5** file and supplement the **reason** and **usedScene** fields under **requestPermissions**. The following is an example:

"requestPermissions": \[
  {
    "name": "ohos.permission.READ\_IMAGEVIDEO",
    "reason": "$string:module\_desc",
    "usedScene": {
      "abilities": \[
        "EntryAbility"
      \],
      "when": "inuse"
    }
  }
\]

#### Error message "Only one default card can be configured in the form\_config.json file" is displayed during compilation

**Symptom**

DevEco Studio compilation fails, and the error message "Only one default card can be configured in the form\_config.json file" is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/VCUl5XTJRm633jAg18mFzw/en-us_image_0000002532750395.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=877014A80941D2AFA7F2227172DE3EE7E106DC805D4E9504B36A8CB21734C5CC "Click to enlarge")

**Cause**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule is added: In the widget configuration file, **isDefault** cannot be left empty. Each UIAbility has only one default widget.

**Solution**

Go to the corresponding **module.json5** file, select the default widget, and set the **isDefault** field of other widgets to **false**.

#### Error message "In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty" is displayed during compilation

**Symptom**

DevEco Studio compilation fails, and the error message "In the form\_config.json file, if the value of the updateEnabled field is true, the updateDuration and scheduleUpdateTime fields cannot be both empty." is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/lnyL0Nf0SMK-FDskghMk7A/en-us_image_0000002500910502.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73C83BA1948D860167CFC899F8AE9BECAEF5D982D4A4115B993906ED85C41F4B "Click to enlarge")

**Cause**

In DevEco Studio NEXT Developer Preview2 and later versions, the following rule is added: **updateEnabled** in the widget configuration file cannot be left empty. If **updateEnabled** is set to **true**, you can select either **updateDuration** or **scheduledUpdateTime** and configure it. If both **updateDuration** and **scheduledUpdateTime** are configured, **updateDuration** takes effect first.

**Solution**

Open the **module.json5** file and set **updateEnabled** to **false** or add **updateDuration** and **scheduledUpdateTime** as required.

#### Error message "The path XX is not writable. Please choose a new location" is displayed during compilation

**Symptom**

When DevEco Studio is opened directly from a .dmg file on macOS, any attempt to build a project results in the error message "The path XX is not writable. Please choose a new location."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/A9sOwXiaSJ2MCPNlIrprew/en-us_image_0000002501070416.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F13F0FDD633D055FD72ED0AF4022D3F4258826192517C52E547B73FF6F0E7F03)

**Cause**

Opening DevEco Studio from the .dmg file launches it in read-only mode, and the files built into DevEco Studio do not have write permissions.

**Solution**

Drag DevEco-Studio.app to **Applications** and install DevEco Studio by following the onscreen instructions.

#### Error message "Property 'XX' does not exist on type 'typeof BuildProfile' is displayed during compilation

**Symptom**

The external interface provided by the local HSP module uses a custom parameter **BuildProfileFileds**, which is not defined in the HAP, and the HAP references this interface, causing the compilation to fail with the message "Property 'XX' does not exist on type 'typeof BuildProfile'".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FU9LVxWtRyWEJcqo5jn8qg/en-us_image_0000002501070396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F818024FBE0D476C9F032AB9CE6B130DD8E231DACB7ACF0F2B50D0D682DDDBE)

**Solution**

You can resolve this issue in two ways:

-   Configure the same custom parameter **BuildProfileFileds** in the HAP as in the HSP.
-   Configure the same custom parameter **BuildProfileFields** (as defined in the HSP) in the project-level **build-profile.json5** file. This way, the custom parameter in the HSP takes effect globally.

#### Error Message "The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match" Is Displayed During Compilation

**Symptom**

Error message "The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match" is displayed during compilation

**Solution**

When [useNormalizedOHMUrl](../../configuration-files/project-level-build-profile-json5-file/document.md#section13181758123312) is set to **true**, the ohmurl uses a new method of concatenation and parsing. As such, it cannot be mixed with the old ohmurl; otherwise, it cannot be recognized at runtime.

You can resolve this issue in two ways:

-   Modify the **useNormalizedOHMUrl** field in the project-level **build-profile.json5** file of the problematic dependency package to be consistent with the current project. Then, regenerate the dependency package and replace the original one (the default value for **useNormalizedOHMUrl** is **false**).
    
    {
      "app": {
        "products": \[
          {
             "buildOption": {
               "strictMode": {
                 "useNormalizedOHMUrl": true
               }
             }
          }
        \]
      }
    }
    
-   If there are many dependency packages with inconsistent **useNormalizedOHMUrl** values, you are advised to change the value of **useNormalizedOHMUrl** in the project-level **build-profile.json5** and replace other inconsistent dependency packages.

If the issue persists, the HSP is a local package. In this case, import the HSP by adding it to **modules** in the project-level **build-profile.json5** file. The following is an example:

"modules": \[
  {
    name: "hsp",   // HSP dependency
    srcPath: "../MyApplication\_stageB/hsp",   // Absolute or relative path of the HSP dependency
  }
\]

#### How to configure dynamic dependencies in oh-package.json5

In the **oh-package.json5** file:

-   **dependencies**: third-party libraries to be imported to the code, that is, production dependencies used in build and runtime phases.
-   **devDependencies**: development dependencies that participate only in the development or testing phases of the project.
-   **dynamicDependencies**: HSP modules that are dynamically imported. This field is used when the HSP module needs to be dynamically loaded.

The following is an example. For details, see [oh-package.json5](../../../command-line-tools/using-ohpm/oh-package-json5/document.md) and [Adding Dependencies](../../configuring-your-build/adding-dependencies/document.md).

{
  "name": "parameter-test",
  "version": "@param:version", 
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  },
  "parameterFile": '.parameterFile/parameterFile.json5' // Enable parameterization and specify the path of the parameterization configuration file.
}

#### Unable to execute .abc files due to SDK and image version mismatch

**Symptom**

When the SDK version does not match the image version, the app may crash, resulting in a JS crash error.

**Solution**

Use a matching SDK and image version.

To view the SDK version:

Go to the **sdk** directory in the DevEco Studio installation path, and execute the following command: **{sdk.dir}/openharmony/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version**

#### Error message "Could not resolve 'xxx' from" is displayed when the 'xxx' directory exists

**Symptom**

The error message "Could not resolve '_xxx_' from" is displayed during compilation, but the _xxx_ directory exists and contains an **Index** file.

**Cause**

When referencing a directory, the compiler automatically concatenates a lowercase **index** file, but the directory contains an uppercase **Index** file. During compilation in a case-sensitive environment, the **index** file cannot be found, resulting in an error.

**Solution**

When referencing a directory, explicitly specify the reference to the **Index** file in the directory, for example, **xxx/Index**.

#### User directory does not contain an .npmrc file

**Symptom**

During an attempt to create a project, the error message "Error: The hvigor depends on the npmrc file. Configure the npmrc file first." is displayed.

**Cause**

There is no .npmrc file in the user directory.

**Solution**

Create an .npmrc file in your user directory and configure the following information:

registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/

#### Error message "Error: 'icon' value \`$media:icons\` invalid value." is displayed during compilation

**Symptom**

The error message "Error: 'icon' value \`$media:icons\` invalid value" is displayed during compilation.

ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref \`$media:icons\` don\`t be defined.
Error: 'icon' value \`$media:icons\` invalid value.
at D:\\project\\process\_profile\\default\\module.json
Detail: Please check the message from tools.

**Possible Cause**

When a referenced resource does not exist, the file path indicated by the compilation error is the build directory.

**Common Scenarios**

1.  The resource file is not added.
2.  The resource file is deleted accidentally.

**Solution**

Search globally for the resource ID indicated by the error to check whether the erroneous resource exists.

#### Error message "Error: cJSON\_Parse failed, please check the JSON file." is displayed during compilation

**Symptom**

The error message "Error: cJSON\_Parse failed, please check the JSON file" is displayed during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/j47LP-MQRXmX50oYIOe6xQ/en-us_image_0000002532670437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F244F7D3203BAF8B4C60673D9BB603FAFAD6FC7F0FCDAC898AD7FD48A406BCA "Click to enlarge")

**Possible Cause**

The **module.json** file format is invalid.

**Common Scenarios**

1\. There is an extra comma (,) at the end of the JSON file.

2\. The root element is not enclosed in curly braces ({}).

**Solution**

Verify the format of the JSON file indicated by the error.

#### Error message "Error: the name 'XXX' can only contain \[a-zA-Z0-9\_\]." is displayed during compilation

**Symptom**

The error message "Error: the name 'XXX' can only contain \[a-zA-Z0-9\_\]" is displayed during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/aXSrERO6TZa0vEzWTeIeKg/en-us_image_0000002500910484.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F694E02FC5DF6123602CEE080F6944E4B4C9DA9FCB46C8C18E275FB55C553697)

**Solution**

Verify the file name. The file name can contain only uppercase letters, lowercase letters, digits, and underscores (\_).

#### There are errors with require statements in third-party packages

**Symptom**

An error is reported during compilation when a third-party package is imported.

**Possible Cause**

Some third-party packages are migrated from npm and were originally developed for a Node environment. The **require** syntax may not be fully supported by ArkCompiler, leading to runtime errors.

**Scenario 1**

// Module/src/test.json
{a: 1, b: 2}
//use.js
let test = require("Module/src/test.json")

Change the code as follows:

// Module/src/test.js
module.exports = {a: 1, b: 2}
//use.js
let test = require("Module/src/test")

**Scenario 2**

// Module/package.json
...
main: "./src"
...
// use.js
let module = require("Module")

Change the code as follows:

// Module/package.json
...
main: "./src/index.js"
...
// use.js
let module = require("Module")

**Scenario 3**

The following warning message is displayed during compilation:

Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node\_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning

**Solution**

Modify the **preferBuiltins** field in the **rollup.config.js** file.

plugins: \[ 
  resolve({ 
    preferBuiltins: false,    // true or false
    mainFields: \['module', 'main'\], 
    extensions
  })
\];

**Scenario 4**

import {Buffer} from 'buffer'

Change the code as follows:

import {Buffer} from 'buffer/'

#### Error message "Indexed access is not supported for fields(arkts-no-props-by-index)" is displayed during compilation

**Symptom**

Dynamically accessing fields of a class or interface results in a compilation error with the message: "Indexed access is not supported for fields (arkts-no-props-by-index)."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/OFlkbj4OQSaKh3ZIBmWA7w/en-us_image_0000002532750355.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E188B7FFD2999169EF1B4DCE2CF0F8A4C466F8CC63FE64E0734032FB540274F0)

**Solution**

Modify the code.

getValue(breakpoint: string): T {
    return Reflect.get(this.options, breakpoint) as T;
}

#### Error message "Declaration merging is not supported(arkts-no-decl-merging)" or "Cannot redeclare block-scoped variable 'xxx'" is displayed during compilation

**Symptom**

When the same variable or type such as interface or enum is declared in different files, DevEco Studio does not report an error, but an error is reported during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Y2DPWd8aTf6AMQ-ohZaP-w/en-us_image_0000002501070406.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57F70C3593D8729336FDEABE861B0DE7F8D2A8058281C6C04F103409CA2E6387)

**Solution**

If a file does not contain the **export** keyword, it is considered part of the global namespace, effectively making two files act as if they are the same file. To resolve the issue, add the **export** keyword to make the file an independent namespace, or add the declared content to a custom namespace.

#### Error message "The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary" is displayed during compilation

**Symptom**

Error message "The inferred type of 'xxx' cannot be named without a reference to 'xxx'. This is likely not portable. A type annotation is necessary" is displayed during compilation.

**Cause**

The original files do not specify types. As a result, the .d.ts file generated by the HSP lack type annotations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/JpqSDsC4QdygEXieQFyQ3A/en-us_image_0000002501070318.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3157A9CCBDAD2173CAB58EC6D2381D803586F1276CEE3E4A6406FB7EE9C8BEE9 "Click to enlarge")

**Solution**

Add type annotations at the location where the error occurs.

#### Error messages "arkts-no-any-unknown" and "Cannot find module 'xx' or its corresponding type declarations" are displayed during compilation

**Symptom**

The error messages "arkts-no-any-unknown" and "Cannot find module 'xx' or its corresponding type declarations" are displayed during compilation.

**Cause**

Case sensitivity causes module resolution failures, typically when the two errors shown in the figure occur together.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/e45TlUDqQLyFHlAWiqCwkg/en-us_image_0000002532670489.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48E049D41E005CE35373B98A05139442571E5E9BC2CE29340BDA56FE862EDD9E)

**Solution**

Resolve the case sensitivity issue in the references.

#### Error message "ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted" is displayed during compilation

**Symptom**

The error message "ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted" is displayed during compilation.

**Cause**

The security settings on macOS add a quarantine flag (com.apple.quarantine) to executable files downloaded from the Internet. As a result, the SDK executable file, which is obtained through downloading from the Internet, cannot be executed.

**Solution**

Execute the command to remove the com.apple.quarantine flag from the executable file.

xattr -d com.apple.quarantine /path/to/es2abc

#### Error message "Cannot add xxxx items to index" is displayed during compilation

**Symptom**

The error message "Cannot add xxxx items to index" is displayed during compilation.

**Cause**

There is a function within the compiled file that contains a large number of object literals, array literals, and strings, causing the number of items to exceed the limit (65536).

**Solution**

Check the relevant files and split the functions that have the aforementioned causes.

#### Error message "resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'" is displayed during compilation initialization

**Symptom**

After DevEco Studio is upgraded to version 5.0.3.403, sometimes the following error message is displayed when opening a historical project: resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/9JwmkQHVTLKGm46FAE7-1w/en-us_image_0000002500910452.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4595274117AA8E6A0C2BA64641AD860F533BF9168E80697B77D18954B8C4CF87)

**Cause**

During initialization, there is a conflict in log writing because the **build-log** file in the .hvigor directory is in use.

**Solution**

-   Method 1: Click **Sync Now** at the top of the editor window.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/bhy-ma1HRI6xHijs0Ny03w/en-us_image_0000002501070376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFDB74346AFE9EAA9A289905C42A3C306877E9A86F239D4EBCA028BEFB9BD23A)
    
-   Method 2: Choose **File** > **Sync and Refresh Project** from the toolbar.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/aN-Xso52SDuOGLKfkvCjYg/en-us_image_0000002500910564.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=388796CD07DAD317B15A577D052CA9A1975944B8B4FA5B16BC0E64B2D91FB91B)
    
-   Method 3: If the issue persists, manually delete the .hvigor directory in the project directory and restart the sync.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ucPUc_reRb6ZQJVQ3Sduww/en-us_image_0000002532750337.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23F430A07CCDB56CB5D9F5FC2DB79E47E9003B66AD4B76C119D016E83CE3A852)
    

#### When the dynamic library is loaded on macOS, the signing is intercepted

**Symptom**

On macOS, the following instrumentation configuration is added to the **build-profile.json** file for development in DevEco Studio, but the instrumentation function does not take effect.

"transformLib": "<Dynamic library path relative to the root path of the module, starting with ./>"

**Judgment and Verification**

1.  Go to the directory where es2abc is located in the **sdk** directory: \[DevEco Studio installation directory\]/Contents/sdk/default/openharmony/ets/build-tools/ets-loader/bin/ark/build-mac/bin
2.  Execute the following command:
    
    ./es2abc --merge-abc --transform-lib <Dynamic library path> <Test JS file path>
    
3.  If an error message similar to the following is displayed, the reason may be that es2abc and the dynamic library file do not belong to the same signature group.
    
    os::library\_loader::Load error: dlopen(..., 0x0001): 
    tried: '...' (code signature in <...> '...' not valid for use in process: mapped file has no cdhash, completely unsigned? Code has to be at least ad-hoc signed.)
    
4.  Run the following commands to view the signature group information of es2abc and the dynamic library file. If one file has signature information and the other does not, or if both have signature information but the **TeamIdentifier** property values in the signature information are different, the issue is caused by inconsistent signature groups.
    
    codesign -dv --verbose=1 <es2abc path>
    codesign -dv --verbose=1 <Dynamic library path>
    

**Solution**

Run the following command to replace the signature of the es2abc file with the same user signature as the dynamic library file.

codesign --remove-signature <es2abc path>
codesign -s - -v <es2abc path>
