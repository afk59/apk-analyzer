# How are the processes of an application started?

-   Every application has a maximum of three types of processes: main process, ExtensionAbility process, and render process. All these processes are created and managed by the system.
-   The main process runs all UIAbility components, pages, and service logic of an application. It can have multiple UIAbility instances.
-   An application contains one or more modules. Modules are classified as Ability or Library. A module of the Ability type is built into a Harmony Ability Package (HAP) file, and a module of the Library type is built into a Harmony Archive (HAR) file or a Harmony Shared Package (HSP).
-   HAP can be classified into two types: Entry and Feature. In the same application, only one HAP of the Entry type is provided for the same device type, and it is the entry module of the application.
-   The process startup sequence is as follows:
    1.  The system service starts the main process of the application through the incubation process and creates the corresponding running environment.
    2.  The application requests system services based on specific requirements.
    3.  The system starts other processes required by the application.
-   The module startup sequence is as follows:
    1.  The system starts the entry module of the application. When the module is loaded, an AbilityStage instance is created for initialization.
    2.  After initialization, the corresponding entry UIAbility is started.
    3.  After the UIAbility is loaded, a WindowStage class instance is generated and bound to the UIAbility. The WindowStage serves as the window manager in an application process. Through the WindowStage, the UIAbility manages a window and loads the first ArkUI page in the window for representation on the device.

**Reference**

[Stage Model Development Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/stage-model-development-overview)
