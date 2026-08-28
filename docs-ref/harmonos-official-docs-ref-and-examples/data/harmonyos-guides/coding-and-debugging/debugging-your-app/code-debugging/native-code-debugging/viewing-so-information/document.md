# Viewing .so Information

In the native code debugging window, click **Layout Settings** ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ehV1kllFSGi3dR7sTXH9fg/en-us_image_0000002533435023.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13C87C6B3021E60BB7BCA1B41B1DD66B8856AD18D293E235CBE960154690D0F9) and select **Modules** to open the **Modules** pane.

During native debugging, the **Modules** window lists and displays information about the .so files used by the app. You can click the properties to sort them in ascending or descending order, with string matching search supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/cxp6FKlgQj-S60n3OU9jiw/en-us_image_0000002501831802.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062151Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B6A35C300EE87C2999A65C3D06102AF2831063BF9E2B50652D8A6F1504B7E46)

-   Loading symbol table files
    
    If symbols are not loaded, right-click the module and select **Load Modules** to load a local .so file containing symbol information. After successful loading, the **Symbol Status** column will display **Symbols Loaded**.
    
    To restore the symbols to their initial states, right-click the module and choose **Reset Modules**.
    
-   Mapping source code paths
    
    The default path of the loaded symbol table file is its compile-time location. If this does not match your local source file path, associate the source files. Specifically, right-click the module, choose **Set Source Mapping**, and select the local source directory. After successful mapping, the **Source Root Path** column will show the mapped path.
    
    To revert to the default path, right-click the module and select **Reset Source Mappings**.
