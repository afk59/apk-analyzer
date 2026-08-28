# How do I remove the error "Cannot read properties of undefined(reading 'XXX')"?

Rectify the fault based on the value of _XXX_. If the fault persists, refer to the final solution.

-   **Scenario 1:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'setEnabled')" is displayed.
    
    **Cause Analysis**
    
    The **hvigorfile.ts** file contains the following code:
    
    import { hvigor, getHvigorNode } from "@ohos/hvigor"
    import { hapTasks} from '@ohos/hvigor-ohos-plugin';
    // Problem Code
    getHvigorNode(\_\_filename).getTaskByName('XXX').setEnabled(false);
    export default {
        system: hapTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
        plugins: \[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
    }
    
    **Solution**
    
    1.  Ensure that the specified task is a task in the current **HvigorNode**.
        
        For example, if the error occurs in **hvigorfile.ts** of the entry module, valid _XXX_ values include the following: **default@SignHap**, **default@CollectDebugSymbol**, and **assembleHap**, as shown in the following figure.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/BaxzSfMaTlOer4rF5A61bg/en-us_image_0000002289418625.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0344C793EA0E6DADD325186FADFF7787EE84F4BD27EDE41E1F93D5A86B28ACE)
        
    2.  Use **getTaskByName** only in the Hvigor configuration phase or later phases, including **beforeNodeEvaluate**, **afterNodeEvaluate**, **nodesEvaluated**, **taskGraphResolved**, and **buildFinished**.
    
    **Reference**
    
    [Lifecycle and Hooks](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-life-cycle#section746253616316)
    
-   **Scenario 2:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'isSO')" is displayed.
    
    **Solution**
    
    Upgrade DevEco Studio to 5.1.0.840 or later.
    
-   **Scenario 3:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'getPluginId')" is displayed.
    
    **Solution**
    
    Set the value of **system** in the **export default** object in **hvigorfile.ts** to **appTasks**, **hapTasks**, **hspTasks**, or **harTasks**.
    
    import { harTasks } from '@ohos/hvigor-ohos-plugin';
    
    export default {
        system: harTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
        plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
    }
    
-   **Scenario 4:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'getNeedExecTargetServiceList')" is displayed.
    
    **Solution**
    
    Set the **type** field in **module.json5** of the module to match the **system** field of the **export default** object in **hvigorfile.ts**. For the mappings of the two fields, see the following table.
    
    **Table 1**
    | 
    type Field in module.json5
    
     | 
    
    system Field of the export default Object in hvigorfile.ts
    
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
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'app')" is displayed.
    
    **Solution**
    
    Ensure that the **AppScope/app.json5** file exists in the project directory.
    
-   **Scenario 6:**
    
    **Symptom**
    
    When a unit test is performed in the Linux environment, the error "Cannot read properties of undefined(reading 'toString')" occurs.
    
    **Solution**
    
    Currently, unit tests are not supported in the Linux environment.
    
-   **Scenario 7:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'kind')" is displayed.
    
    **Solution**
    
    Check whether the ArkTS code contains the following negative example:
    
    // Incorrect writing: empty array 
    class w {
      public a: \[\]\[\] = \[\]
      test() {
        console.log("1", this.a\[0\])
      }
    }
    
    // Correct writing
    class w {
      public a: string\[\]\[\] = \[\]
      test() {
        console.log("1", this.a\[0\])
      }
    }
    
-   **Scenario 8:**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'getltem')" is displayed.
    
    **Solution**
    
    Add **.domStorageAccess(true)** to the controller that loads the WebView.
    
-   **Scenario 9**
    
    **Symptom**
    
    During compilation and build, the error message "Cannot read properties of undefined(reading 'clear')" is displayed.
    
    **Cause Analysis**
    
    Configure the following content in the **hvigor/hvigor-config.json5** file in the project root directory to open the stack.
    
    {
      "debugging": {
        "stacktrace": true
        /\* Disable stacktrace compilation. Value: \[ true | false \]. Default: false \*/
      },
    }
    
    Check whether the stack content is as follows.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ACGFgJI3RnquBXTTQqTLlw/en-us_image_0000002289305561.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2D82862A0099F9799B40999D90CA2D71AE00DFD11AB4792C7EAB5569C217534)
    
    **Solution**
    
    Check whether DevEco Studio is using third-party plugins such as security hardening plugins. If yes, disable them and check whether the issue persists. If it persists, refer to the final solution.
    
-   **Scenario 10**
    
    **Symptom**
    
    During the HAP coverage test, the error message "Error Message: Cannot read properties of undefined (reading 'module')" is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/YMrLQZebT2q_c3-VEbogqA/en-us_image_0000002523012117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F017D5092B9274635544E0A1028E309EEAE3B97ED19B4947B68226460E452E12)
    
    **Possible Causes**
    
    The **build-profile.json5** file of the HAP and HSP modules in the project contains **ohosTest**, but the **ohosTest** directory does not exist. As a result, the **ohosTest** information of the module fails to be obtained during the build.
    
    **Solution**
    
    Check all modules of the project. If **ohosTest** is configured in targets in the **build-profile.json5** file, ensure that the **src/ohosTest** directory and the corresponding directory structure exist in the module. If **ohosTest** is not required, delete **ohosTest** from targets.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/n8GNwsgMSGytvkUUPHoLjg/en-us_image_0000002490972342.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062619Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1178F7AC276CE20F3790D5BA1FADB2E5DFA75DB547859096BFC5ABE44F5AF5FA)
    
-   **Final Solution:**
    
    If none of the preceding solutions work, open the stack and check the code based on the stack information.
    
    To open the stack, configure the following content in the **hvigor/hvigor-config.json5** file in the root directory of the project:
    
    {
      "debugging": {
        "stacktrace": true
        /\* Disable stacktrace compilation. Value: \[ true | false \]. Default: false \*/
      },
    }
    
    Check the **hvigorconfig.ts** and **hvigorfile.ts** files first, and then check other files.
    
    If no problem is found in the preceding files, submit a trouble ticket to us in time.
