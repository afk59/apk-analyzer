# Developing an Hvigor Plugin

Hvigor allows you to develop your own plugin, where you can define the build logic and share it with others.

With Hvigor, you can implement plugins with the **hvigorfile.ts** script or based on a TypeScript project.

For details about plugin development practices, see [Customizing the Hvigor Plugin](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-custom-hvigor-plugin).

#### Developing a Plugin with the hvigorfile Script

You can quickly develop a plugin by editing the **hvigorfile.ts** file in your project or module directory. However, note that the plugins created this way cannot be reused or shared across projects.

Since DevEco Studio 6.0.2 Beta1, code editing features such as code completion, code generation, and code refactoring are supported for build script writing. For details, see [Editor Basics](../../../coding-and-debugging/writing-code/editor-basics/document.md), [Code Generation/Completion](../../../coding-and-debugging/writing-code/code-generation-completion/document.md), and [Code Refactoring](../../../coding-and-debugging/writing-code/code-refactoring/document.md).

To create build scripts, you are advised to place them under the **scripts** directory of the project or module to keep them separate from the app code, as shown in the example below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/NRjvXVg9R7e1mWcTmQTqrQ/en-us_image_0000002532670045.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=259EC1B030665BA5ABD194374CA2EBCFCF8F993F697DCEFB30F1CEBB38F039DC)

The following example demonstrates plugin development with a project-level **hvigorfile.ts** script.

1.  Import module dependencies. For details about more APIs, see [Using APIs for Extending Your Build](../using-apis-for-extending-your-build/document.md).
    
    // Project-level hvigorfile.ts
    import { appTasks } from '@ohos/hvigor-ohos-plugin';
    import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';
    
2.  Write the plugin code to implement the **HvigorPlugin** API.
    
    // Project-level hvigorfile.ts
    function customPlugin(): HvigorPlugin {
      return {
        pluginId: 'customPlugin',
        apply(node: HvigorNode) {
          // Plugin code.
          console.log('hello customPlugin!');
        }
      }
    }
    
3.  Add the custom plugin the export declaration.
    
    // Project-level hvigorfile.ts
    export default {
      system: appTasks,
      plugins:\[
        customPlugin()  // Custom plugin
      \]
    }
    
4.  Run Hvigor commands.
    
    Execute the **apply** method of the plugin when the Hvigor lifecycle is configured.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ZfFPRfiRTiK6dK_vk4F1Ig/en-us_image_0000002532670041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC01EFDFF3FAE5EFF905EB5D52B21CD90CE70B314A0636605B0F1308A85F9453)
    

#### Developing a Plugin Based on a TypeScript Project

The plugin code developed based on a TypeScript project can be reused and shared across projects. Therefore, this development mode is recommended.

## Initializing the TypeScript Project

1.  Create an empty directory.
    
    Run the **cd** command to go to the empty directory.
    
2.  Install TypeScript with the Node Package Manager (npm).
    
    // Install TypeScript globally.
    npm install typescript -g
    
3.  Initialize the nmp project.
    
    Run the following command and configure the project as instructed. After initialization, the **package.json** file is generated.
    
    // Initialize the nmp project.
    npm init
    
4.  Generate a TypeScript configuration file.
    
    Run the following command to generate a **tsconfig.json** file:
    
    // Initialize the TypeScript configuration file.
    tsc --init
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4yoxXk-7Rsuqecfh4lPhpw/en-us_image_0000002517845484.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A3067A05D206F2157D0D3EF70DB80735782AAEA621704D3453AAB51250ABA05)
    
5.  Delete the **verbatimModuleSyntax** field.
    
    Check the **tsconfig.json** file for the presence of the **verbatimModuleSyntax** field. If it exists and is set to **true**, it will prevent the use of ESM syntax and cause a compilation error. Therefore, you need to delete this field.
    

## Developing a Plugin

1.  Configure the npm image repository address, which is used to install the **@ohos/hvigor** plugin.
    
    Create an .npmrc file in your project directory and configure the following information:
    
    registry=https://repo.huaweicloud.com/repository/npm/
    @ohos:registry=https://repo.harmonyos.com/npm/
    
2.  Declare the dependency on hvigor.
    
    Add hvigor information to **devDependencies** in the **package.json** file.
    
    "devDependencies": {
        "@ohos/hvigor": "5.2.2"
    }
    
3.  Install dependencies.
    
    Run the following command to install dependencies:
    
    npm install
    
4.  Write the plugin code.
    
    Create the **custom-plugin.ts** file in the **src/plugin** directory and write the plugin code. For details about more APIs, see [Using APIs for Extending Your Build](../using-apis-for-extending-your-build/document.md).
    
    import type { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
    
    export function customPlugin(): HvigorPlugin {
      return {
        pluginId: 'customPlugin',
        apply(node: HvigorNode) {
          console.log('hello customPlugin!');
        }
      }
    }
    
5.  Export the plugin.
    
    Create an **index.ts** file and declare the export of plugin methods in it. Since .ts files are ultimately compiled into .js files, the .js file needs to be exported.
    
    export { customPlugin } from './src/plugin/custom-plugin.js';
    

## Publishing the Plugin

The TypeScript project, as an npm project in essence, is published in the same way as an npm project. For details, see the npm official documentation.

The process for publishing an npm package is as follows:

1.  Configure the registry.
    
    Open the .npmrc file in the project directory and configure the image repository where you want to publish.
    
    registry=\[npm image repository address\]
    
2.  Generate an AccessToken.
    
    Run the following command to register and log in to the npm repository. The token information is automatically generated in the .npmrc file in the project directory.
    
    npm login
    
3.  Compile the npm package.
    
    tsc
    
    If the following error is reported during the compilation, check whether [verbatimModuleSyntax is deleted](#li88369101451) during project initialization.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/q2IVOv02Td-rqGdwbQlOlw/en-us_image_0000002517685932.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1CB08ABF78099408A91E5C7E73269337CB2585DC064BFD3E2CA56BF31F5FFD3)
    
4.  Publish the npm package.
    
    Run the following command to package the npm project and publish it to the image repository:
    
    npm publish
    

## Using the Plugin

1.  Add the dependency.
    
    In the **hvigor/hvigor-config.json5** file of the project, add the custom plugin to **dependencies**. The dependencies support offline plugin configuration.
    
    "dependencies": {
      "custom-plugin": "1.0.0"   // Add the custom plugin.
    }
    
2.  Install dependencies.
    
    -   Method 1: Click **Sync Now** in the upper right corner of the editing area or choose **File** > **Sync and Refresh Project**. DecEvo Studio automatically installs the plugin based on the dependency configuration in **hvigor-config.json5**.
    -   Method 2: Run the following hvigorw command. The command line tool automatically installs the plugin.
        
        hvigorw --sync
        
    
3.  Import the plugin.
    
    Determine the **hvigorfile.ts** file where the node of the plugin is located, and import the plugin.
    
    import { customPlugin } from 'custom-plugin';
    
4.  Use the plugin.
    
    Add the custom plugin to **plugins** in **export default**.
    
    export default {
      system: appTasks, // Take the project-level hvigorfile.ts as an example.
      plugins:\[
        customPlugin()  // Add the custom plugin.
      \]
    }
