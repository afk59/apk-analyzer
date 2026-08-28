# Enabling Parallel Build

Most projects contain multiple subprojects. Some subprojects are independent of each other, meaning no status sharing among them. In most cases, parallel build can effectively reduce the overall build time for multiple subprojects. However, in specific cases where there are mutual dependencies between subprojects, there may not be significant reduction in the build time. The actual time saved depends on your project structure and the dependencies between subprojects.

Parallel build is enabled in Hvigor by default. You can manage the settings using the following methods:

-   Using the menu bar of DevEco Studio
    -   Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select or deselect **Execute tasks in parallel mode(may require larger heap size)**.
-   Using commands
    -   Run the following command (replace **<task>** with the actual task name):
        
        // Enable parallel build.
        hvigorw <task> --parallel
        // Disable parallel build.
        hvigorw <task> --no-parallel
        
    -   Configure **execution.parallel** in [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md).
