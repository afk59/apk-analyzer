# Process Model

#### Overview

Processes serve as the fundamental units for resource allocation in the system and form the basis of the operating system's architecture. This topic describes the process model and thread model of the system from the perspective of an entire application.

#### Process Model

## Basic Process Types

For a complex application with multiple [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) components and various ExtensionAbility components (such as [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) and [ShareExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-shareextensionability) shown in Figure 1), the following process types may be present at the runtime:

-   **Main process**: By default, all UIAbility components within the same application (identified by the same bundle name) run in a single, dedicated process known as the main process ("Main Process1" shown in Figure 1).
    
-   **ExtensionAbility process**: All ExtensionAbility components of the same type within the same application (identified by the same bundle name) run in their own dedicated process (for example, "FormExtensionAbility Process" and "Process for other ExtensionAbility types" shown in Figure 1).
    
    For ExtensionAbility components that inherit from [UIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiextensionability), each instance can be configured to run in its own separate process. For example, each ShareExtensionAbility instance can be set to run in its own process. For details, see [UIExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiextensionability).
    
-   **Render process**: When a **Web** component in the application is running, the system allocates a dedicated Render process for rendering ("Render Process" shown in Figure 1).
    

**Figure 1** Basic process types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/KCj1Nm0vQTqMqVNroUrOTw/en-us_image_0000002537764364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BA2A2BF13ED2AE67DC0BF38AFBAFE4BBEBD6D4AE047A24BDFC16C2FAA9841CE)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-kBEwntPTxSzQkVTX2nNmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4473DA9FAAD84177CB0A40B68F720D025F8DA66C9F15A9B86ED31E925CCEFB02)

-   Process names follow no fixed rules and are not directly related to process types. They should not be used for service logic judgments. For example, in an application named **com.example.myapplication**, an [InputMethodExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inputmethod-extension-ability) may run in a separate process typically named **com.example.myapplication:input**. However, this name is not fixed, and the process with this name is not necessarily the input method process, nor is the input method process necessarily named this way.
-   A single process can contain multiple AbilityStage instances, and a single AbilityStage can contain multiple Ability instances. The lifecycle of a process is closely related to the lifecycle of Ability instances. A process will only be destroyed after all Ability instances within it have exited. In other words, to exit a process, you must first exit all Ability instances within it.

## Other Process Types

On 2-in-1 and tablet devices, the following special process types are supported for the UIAbility:

-   **Module-independent process**: For applications with multiple HAPs where each HAP's service logic is relatively independent, you can configure the **isolationMode** field in the [module.json5](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#tags-in-the-configuration-file) file to **isolationOnly** (run only in an independent process) or **isolationFirst** (prefer to run in an independent process). This way, all UIAbility instances within that HAP will run in a unified, separate process. For example, UIAbilityC in Figure 2 runs in "Main Process2" instead of "Main Process1".
-   **Dynamically specified process**: When UIAbility instances within the same HAP need to be dynamically allocated to different processes based on runtime conditions (for example, each process can support up to five instances), you can set the **isolationProcess** field under UIAbility in the **module.json5** file to **true**. When starting a UIAbility instance, the system calls the [onNewProcessRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#onnewprocessrequest11) callback of the [master process](../../ability-kit-terminology/document.md#master-process). You can return a custom string in this callback. If the string matches an existing process, that process is reused; otherwise, a new process is created. For example, "Main Process3" and "Main Process4" in Figure 2 are multiple processes for UIAbilityD.
-   **Statically specified process**: When UIAbility or EmbeddedUIExtensionAbility components within the same application need to run in different processes, you can set the **process** field under the [abilities](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities) or [extensionAbilities](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#extensionabilities) tag in the **module.json5** file to different strings. When the system starts a UIAbility or an EmbeddedUIExtensionAbility, it assigns a process based on this string. If multiple UIAbility components and multiple EmbeddedUIExtensionAbility components of the same application have the same string configured for their **process** field, these components all run within the same process. This is illustrated by "Main Process5" in Figure 2.
-   **Child process**: If you want to use multiple processes for background tasks, create child processes using [childProcessManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-childprocessmanager) APIs. The lifecycle of a child process follows that of its parent process; when the parent process terminates, the child process also terminates. For example, "ArkTS Child Process" and "Native Child Process" in Figure 2 are child processes created by the main process. Child processes do not support creating further child processes.

**Figure 2** Other process types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8JA-aH_cSUW-QxbD-I9j6g/en-us_image_0000002537924304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061916Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6613B6357E191C1792509D45002B2C0B89B2631A59687A8A978753EF9E7D7007)

#### Thread Model

After the system creates an application process, it automatically creates a main thread and enters the message loop. All application components run on the main thread.

In addition to the main thread, if an application has complex, time-consuming logic to handle, you can create[Worker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-worker) threads or submit tasks to the [TaskPool](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-taskpool).
