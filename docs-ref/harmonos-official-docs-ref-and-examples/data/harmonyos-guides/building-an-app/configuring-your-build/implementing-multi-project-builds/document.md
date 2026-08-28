# Implementing Multi-project Builds

It is a common place for a large app to be split into modules and then developed by different teams. To accommodate this development mode and facilitate collaboration across teams, support for multi-project builds is provided. Through a multi-project build, you can have multiple projects for a single app, each project being a module of the app. After each project is built into a HAP, you can then pack all of the HAPs into an App Pack for release to AppGallery.

1.  In the project-level **build-profile.json5** file of each project, set **multiProjects** to **true**.
    
    {
      "app": {
        "multiProjects": true,
      }
    }
    
2.  Prepare the HAP packing tool **app\_packing\_tool.jar**, which is located in **$_DevEco Studio installation path_/sdk/default/openharmony/toolchains/lib**.
3.  In the directory where the HAP packing tool is located, run the following command to pack multiple HAPs. For details about how to use the packing tool, see [Packing Tool](../../../system/debugging-tools/debugging-commands/packing-and-unpacking-tools/packing-tool/document.md#multi-project-packing-command).
    
    java -jar app\_packing\_tool.jar --mode multiApp --hap-list D:\\project\\MyApplication\\1.hap,D:\\project\\MyApplication1\\2.hap --out-path D:\\project\\final.app
    
    -   **hap-list**: list of HAP file paths, separated by commas (,).
    -   **out-path**: path where the generated App Pack will be saved, for example, **D:\\project\\final.app**.
