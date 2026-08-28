# Build System Lifecycle

This topic provides a brief overview of the structure and lifecycle of the Hvigor compilation and build system. It starts with the definition of project structure in Hvigor, followed by an explanation of the task, and finally discusses the build lifecycle of Hvigor and how it works with the hvigor-ohos-plugin to complete the automated compilation and build process.

#### Project Structure Definition

Hvigor parses the project into a two-level tree structure, where the project itself is the root node, and each module within the project is represented as a leaf node. In this structure, modules are not allowed to contain other modules. In Hvigor, both projects and modules are collectively referred to as nodes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/EnO4wZV4S3eHwXtk3NDafg/en-us_image_0000002532749943.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE2CCD1ED97721D58C059D40D45AA5B6BCE54D3B4BF592BC724C329CC903F0CA)

During the [initialization phase](#section19246144681710) of the build, a tree structure representing the project structure is constructed using configurations from the [hvigorconfig.ts](#section810245135914) file and the project-level **build-profile.json5** file, both of which can be used to [configure multiple modules](../../configuring-your-build/managing-modules/document.md#section99251918477).

#### Hvigor Script Files

During the build [lifecycle](#section8207184919159), Hvigor uses two script files to complete the registration of plug-ins, tasks, and lifecycle hooks:

-   **hvigorconfig.ts**: This file is unique to the project and only exists in the root directory. It is not a required build file and does not exist by default, but you can create it if needed. This file is parsed and executed early in the Hvigor lifecycle and can be used to manipulate certain data at the very beginning of the hvigor lifecycle.
-   **hvigorfile.ts**: This file is present in every node and is a required file for the build. In this file, you can register plug-ins, tasks, and lifecycle hooks, among other operations.

#### Tasks and Task Dependency Graph

Hvigor automates project builds based on tasks, which outline the steps required to build the project. Tasks can perform a variety of operations, such as source code compilation, packaging, or signing. The execution logic for each task is provided by a plug-in, which can be the default task logic provided by [hvigor-ohos-plugin](#section199818016213) or a custom logic created by you.

It is important to note that tasks have dependencies. Before executing any task, Hvigor constructs a task dependency graph, where all tasks form a directed acyclic graph (DAG). In the following example diagram, task dependencies are represented by arrows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Y-6Sa-WXTyyIeU7I74_i0w/en-us_image_0000002532669993.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1685605F86A4FC30E0D8306AF3E28F73105850F3A81ACF09A89F6B387B39C5EC)

Both hvigor-ohos-plugin and the build scripts in the **hvigorfile.ts** file affect the task dependency graph through the task dependency mechanism.

#### hvigor-ohos-plugin

hvigor-ohos-plugin is the default build plugin that provides service logic support for task completion, such as HAP, HAR, and HSP packaging services for Hvigor. The execution logic of each task is provided by different plugins in the module.

## Relationship Between Hvigor and hvigor-ohos-plugin

As mentioned in [Overview](../document.md), Hvigor provides task registration, orchestration, and configuration management as part of its task management mechanism. It controls the execution process of tasks, but does not include the specific service logic of each task. The specific logic is provided by hvigor-ohos-plugin.

The following figure shows the relationship between Hvigor and hvigor-ohos-plugin. Hvigor accepts task registration, orchestrates the task execution sequence, and calls the plugins in hvigor-ohos-plugin in sequence to execute tasks. If you have customized and registered a task logic plugin, Hvigor will also call your customized plugin to complete the build process.

During the build, hvigor-ohos-plugin registers the task with Hvigor, and Hvigor calls the corresponding plugins according to the [task dependency graph](#section194191858161220) to perform the respective tasks. After completing compilation, packaging, signing, and other tasks, Hvigor finishes the build.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/jWcZsgVCQc-F8NoRyPQTtg/en-us_image_0000002501069910.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1CED52EBF7135415791E48E152F7E05800E36B4DC361FFEE8BEAF5562C55A36)

#### Hvigor Lifecycle

The Hvigor lifecycle illustrates the complete build process, which include three sequential phases: initialization, configuration, and execution.

## Initialization

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/AygnomVvSyKAcTOq8uLINw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A3B048CF0038AB9E1BF30BF4E7267A317224E4AE6FB1146C51184BCAC61E058)

This phase aims to initialize the build parameters of the project and construct a tree-shaped data model of the project structure, where each node is an [HvigorNode](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md#section14832104719474) object.

1.  Based on the command parameters and the configuration in the **hvigor-config.json5** file, set the Hvigor build parameters and construct the **hvigor** and **hvigorConfig** objects.
    -   The **hvigor** object persists throughout the entire build lifecycle, from creation until the build is completed.
    -   The **hvigorConfig** object represents the project structure in hvigor, serving as a simple configuration object for adding or removing nodes and storing node descriptors (**NodeDescriptor** instances).
2.  Using the **build-profile.json5** file in the project's root directory, create a [rootNodeDescriptor](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md#section1914012226435) instance, and initialize the [NodeDescriptor](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md#section1914012226435) instances of all modules in the project through the **modules** field.
3.  Execute the **hvigorconfig.ts** file in the project's root directory, where you can use the related APIs of Hvigor to register hooks for the lifecycle or perform other processing at the start of the build.
4.  Construct the **HvigorNode** instance for each node based on the node descriptors.

## Configuration

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MEkCzyamQRS3Ejw-zHBiZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98864F20BFB059C4D3567E4DA7D1EF61364F9AF482D2C885B03E7A22235D3E77)

This phase aims to load plug-ins, tasks, and DAGs into the nodes after they have been fully loaded.

1.  Execute the **hvigorfile.ts** file in each node, add plugins to each node (register tasks to Hvigor), execute the **apply** method of the plugin, and set up plugin contexts.
2.  Based on the plugins and tasks loaded in the previous step, construct the DAG according to their execution dependencies.

## Execution

-   Execute selected tasks.
-   The dependency between tasks determines the order of task execution.
-   Tasks can be executed concurrently.

## Lifecycle and Hooks

Throughout the Hvigor lifecycle, the following multiple hooks are available for you to use, facilitating the invocation of certain logic at the appropriate times.

In the figure below, all the green-marked frames represent available hooks. For details about how to use each hook, see [Basic Build Capability](../../expanding-build-capabilities/using-apis-for-extending-your-build/basic-build-capability/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/n1h7QeXQQSSzFbKmKeoRtQ/en-us_image_0000002532749939.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062154Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34A6F46CB2B9D413D79554C37F4AB7B869D2235535532B2DAD5A626CBDD03D7C)
