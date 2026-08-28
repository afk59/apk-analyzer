# Introduction

Hvigor supports flexible customization of build modes. When you create a project, DevEco Studio automatically creates the **debug**, **release**, and **test** build modes. Although the project-level **build-profile.json5** configuration file does not specify the **test** mode, this mode is automatically used when the test framework is used to start a test.

#### Specifying a Build Mode

## GUI-based Setting

To set **Build Mode** on the GUI, click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/EEscZ7p6QP-ptJ7eCqRilw/en-us_image_0000002532750293.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53B509C3CAC9C9D8FC8483DDF43D2C7A0314A3A9F8B70763774736AD2B464A31) icon in the upper right corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Ojl83W65QKaQFvtVUQ7vMA/en-us_image_0000002532750291.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B09CFF8FFE66B26BD2A1B564ED21E54CBD5AB9527CBD3D368CA48890F6D60E35)

There are three built-in options: **<Default>**, **debug**, and **release**.

If you have defined additional build modes in the **build-profile.json5** file, the corresponding options are displayed in the **Build Mode** drop-down list.

-   **<Default>**: default option. With this option, the release mode is used to build App Packs and the debug mode is used to build HAPs, HSPs, or HARs.
-   **debug**: The debug mode is used to build App Packs, HAPs, HSPs, or HARs, with the **debuggable** option in **buildOption** defaulting to **true**. In this case, the resulting build includes extensive debugging information such as variable names, function names, and line numbers, enabling direct debugging. However, this debugging information increases the app size and may lead to reduced runtime performance.
-   **release**: The release mode is used to build App Packs, HAPs, HSPs, or HARs, with the **debuggable** option in **buildOption** defaulting to **false**. In this case, the resulting build excludes extensive debugging information and contains only the necessary code and data for the app. This reduction in size, coupled with optimization in compiled bytecode, leads to improved runtime speed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Srr350GQSOeOE7-de-xbVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42A8078F3409DFB5E8C07D59C39128D8AE3D81A15060C6C0F8BB5EEE4CFF3988)

-   The build mode set from the DevEco Studio GUI or the CLI only indicates the name of the selected build mode. Whether the final build product is a debug app depends on the **debuggable** field in the **buildOption** configuration. For details, see [Module-level buildOption](../../../configuration-files/module-level-build-profile-json5-file/document.md#section1010733210421).
-   Lite wearable devices use standard JavaScript runtime. Therefore, the build product in release mode contains JavaScript source code; be mindful of code asset protection.

## CLI-based Setting

-   Use **\-p buildMode** to specify a build mode. For example, specify the **release** mode for building the HAP package of the entry module:
    
    hvigorw --mode module -p product=default -p module=entry@default -p buildMode=release assembleHap
    
-   Use **\-p debuggable=true** to specify the **debug** mode or **\-p debuggable=false** to specify the **release** mode. For example, specify the **release** mode for building the HAP package of the entry module:
    
    hvigorw --mode module -p product=default -p module=entry@default -p debuggable=false assembleHap
    

The default build mode is **release** for building APP Packs and **debug** for building HAPs, HSPs, or HARs.

#### Customizing a Build Mode

Hvigor supports custom build modes. Use the **buildOption** field to declare build options, and the **buildModeBinder** field to bind **target**, **buildOption**, and **buildMode**.

## Defining Build Options

**Project-level build-profile.json5 file:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buildModeSet

 | 

Object array

 | 

No

 | 

Build mode set. Multiple build modes can be configured.

 |
|    | 

name

 | 

String

 | 

Yes

 | 

Name of the build mode.

There are three built-in build modes, which do not require explicit configuration.

-   **debug**: recommended for development and debugging
-   **release**: recommended for packaging and release
-   **test**: recommended for running the ohosTest test suite
    
    NOTE:
    
    1\. The value is globally unique in the project and is case insensitive.
    
    2\. This parameter can be declared and defined only in the project-level **build-profile.json5** file.
    
    3\. For the same build mode, configurations will be overwritten based on the order in which they are applied. Specifically, the latter configuration will overwrite the former.
    
    4\. All the three modes are customizable.
    

 |
| 

buildOption

 | 

Object

 | 

No

 | 

Configuration used by the build mode. For details, see [Project-level buildOption](../../../configuration-files/project-level-build-profile-json5-file/document.md#section14222051575).

 |
| 

products

 | 

Object array

 | 

No

 | 

Product category. Multiple products can be configured. For details, see [Configuring Multiple Targets and Products](../../../configuring-your-build/configuring-multiple-targets-and-products/document.md).

 |
|    | 

buildOption

 | 

Object

 | 

No

 | 

Build configuration of the product. For details, see [Project-level buildOption](../../../configuration-files/project-level-build-profile-json5-file/document.md#section14222051575).

NOTE:

The **buildOption** settings specified for a product take precedence over those defined in **buildMode**. This means that, if the same **buildOption** is specified in both places, the configuration set for the product has a higher priority.

 |

**Module-level build-profile.json5 file**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

buildOption

 | 

Object

 | 

No

 | 

Configuration used by the build mode. For details, see [Module-level buildOption](../../../configuration-files/module-level-build-profile-json5-file/document.md#section1010733210421). The **name**, **debuggable**, and **copyFrom** fields cannot be configured.

 |
| 

buildOptionSet

 | 

Object array

 | 

No

 | 

Build option set, which defines available build options.

 |
|    | 

name

 | 

String

 | 

Yes

 | 

Name of **buildOption**.

The **buildOptionSet** configuration has a higher priority than the top-level standalone **buildOption** configuration in the file.

NOTE:

1.  The value is unique in a module and is case insensitive.
2.  For the same name, configurations will be overwritten based on the order in which they are applied. Specifically, the latter configuration will overwrite the former.
3.  Three built-in options are **default**, **debug**, and **release**.

 |
| 

copyFrom

 | 

String

 | 

No

 | 

Name of a predefined build option in the same module to copy from. This enables you to replicate an existing build option in the same module and then override its settings as needed.

NOTE:

1.  The build option for copying must be defined in the **build-profile.json5** file of the same module.
2.  If it is not, an error is generated, and the built-in default option is copied instead.

 |
| 

buildModeBinder

 | 

Object array

 | 

No

 | 

Mapping between the target and **buildOption** for a build mode.

 |
|    | 

buildModeName

 | 

String

 | 

Yes

 | 

Build mode for the mapping to be created.

NOTE:

1.  **buildModeName** cannot be defined at the module level. The name must be selected from **buildModeSet** at the project level.
2.  For the three built-in build modes (**debug**, **release**, and **test**), Hvigor allocates default bindings:
    -   **debug** mode: The **debug** build option is preferentially allocated, and the **default** build option is allocated to the test package (ohosTest).
    -   **release** mode: The **release** build option is preferentially allocated, and the **default** build option is allocated to the test package (ohosTest).
    -   **test** mode: The **default** build option is allocated to the test package (ohosTest), and the **debug** build option is allocated to the main package.

 |
| 

mappings

 | 

Object array

 | 

No

 | 

Array that manages the binding of build options to targets.

 |
|    | 

targetName

 | 

String

 | 

Yes

 | 

Target to be bound.

NOTE:

The value must be selected within the module.

 |
| 

buildOptionName

 | 

String

 | 

Yes

 | 

Name of the build option to be bound.

NOTE:

The value must be selected within the module.

 |
| 

targets

 | 

config

 | 

buildOption

 | 

Object

 | 

No

 | 

Configuration used by the build mode, which takes precedence over **buildOptionSet**. For details, see [Module-level buildOption](../../../configuration-files/module-level-build-profile-json5-file/document.md#section1010733210421). Note that the **name**, **debuggable**, and **copyFrom** fields cannot be configured.

 |

## Rules for Combining Build Options

1.  By default, a project supports three build modes: **debug**, **release**, and **test**.
2.  By default, a module supports three build options: **default**, **debug**, and **release**.
3.  If **buildModeBinder** does not define the mapping between the target and **buildOption**:
    -   **release** build mode: The target maps to the **release** option, but the **default** option is allocated to ohosTest.
    -   **debug**: The target maps to the **debug** option, but the **default** option is allocated to ohosTest.
    -   **test**: The target maps to the **debug** option, but the **default** option is allocated to ohosTest.
    -   Custom build mode: All targets map to the **default** option.
4.  The **buildOption** settings specified for a product in the project-level **build-profile.json5** file take precedence over those defined in **buildMode**. This means that, if the same **buildOption** is specified in both places, the configuration set for the product has a higher priority.
5.  The module-level **buildOption** value, as a common configuration, is inherited by each **buildOption** in **buildOptionSet**. If **copyFrom** is specified, inheritance occurs prior to copying. Consequently, the settings in **buildOptionSet** have a higher priority than the standalone **buildOption** configuration.
6.  You can use the module-level **buildModeBinder** to identify the unique **buildOption** corresponding to a target. **buildOption** configured in **targets** has a higher priority and is combined with the corresponding **buildOption** following the rules of inheritance and overwrite.
7.  Command line options have the highest priority. Based on the integrated configuration items, you can use command line options to overwrite a specific value.

## Inheritance and Overwrite of Build Options

The precedence of build options, from highest to lowest, is as follows: CLI-based configuration, **targets** configuration, **buildOptionSet** configuration, **buildOption** configuration, **products** configuration, **buildModeSet** configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ZwofDOu-Qqe_384W5z1Sfg/en-us_image_0000002532750289.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062155Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB8FD086648F1ED4064ECD77412353A9AE7C6870E29696FD92A73320DC2948EA)
