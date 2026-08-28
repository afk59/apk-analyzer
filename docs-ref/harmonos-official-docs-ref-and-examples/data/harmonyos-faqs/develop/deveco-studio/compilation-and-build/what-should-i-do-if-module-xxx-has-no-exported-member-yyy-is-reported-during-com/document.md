# What should I do if "Module 'xxx' has no exported member 'yyy'" is reported during compilation?

**Symptom**

The stage model project fails to be compiled and built. "Module 'xxx' has no exported member 'yyy'" is reported, where the **yyy** symbol is exported from the **x.js** file using **export \* from 'x.js'** syntax.

**Solution**

During compilation and build of the stage model project, the syntax of the .js file is not checked. Therefore, when using **export \* from 'x.js'** to export symbols, the error message "Module 'xxx' has no exported member 'yyy'" is displayed.

Try the following methods:

-   Method 1 (recommended): Use syntax to explicitly re-export symbols from the **x.js** file.
    
    export { yyy } from 'x.js'
    

-   Method 2: Create a .d.ts file of the specific **x.js** file and do not specify the file name extension during reference.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/KugXINsVQ7KGnYWC-hwkxg/en-us_image_0000002229758485.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C120AC0F7A29F0FF6AC3CFF202151D7EB63F77191F0628D19440E47603A2C75)
