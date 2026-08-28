# What should I do if "ninja: error: mkdir(xxx): No such file or directory" is reported during compilation?

**Symptom**

During native project compilation, the following warning and error are reported:

Warning: The length of the project directory exceeds 250 characters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/mRnGY_G3QNqSeG2wbWAhuQ/en-us_image_0000002229604401.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F36CA2F5B3A7FB6456FC83125B4F166B21672C3C4E224591D1781CC48E9EA96D "Click to enlarge")

Error: "ninja: error: mkdir(xxx): No such file or directory". The sample code is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/KZcXt0IPQ1uJbDUjT2-KCg/en-us_image_0000002229758889.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45E7CB74DA30CF3586391983733407483D73CF4BA4A10E4CEA7769119351B767 "Click to enlarge")

**Solution**

The default size of **CMAKE\_OBJECT\_PATH\_MAX** is **250**. If the actual path length of the object file in the project exceeds 250 characters, a compilation error is reported.

You need to set the value of **CMAKE\_OBJECT\_PATH\_MAX** in the **CMakeLists.txt** file of the project based on the actual path length of the object file. The specific methods are as follows:

-   Method 1: Add a file name length to the default value of **CMAKE\_OBJECT\_PATH\_MAX**.
    
    In the example, the length of the warning file **TextMeasureCache.cpp.obj** is 24 characters. Add **24** to the default value **250**, that is, **set(CMAKE\_OBJECT\_PATH\_MAX 274)**.
    
-   Method 2: Calculate the value of **CMAKE\_OBJECT\_PATH\_MAX** based on the actual path length of the object file.
    
    Calculation formula: CMAKE\_OBJECT\_PATH\_MAX = Total path length – Length of the directory in the object file + Number of characters in the CMake hash value (fixed at 32).
    
    -   The total path length is the sum of the object file directory length and object file length. In the figure below, the sum of the two lengths is 297 characters.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/8Dnqxm--SImnn4zWNKeVfA/en-us_image_0000002194318624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDB56BD1B066ADA6CFD8E771FD5BDB9BF7A94100A3282815137EE98E87A5F9AD "Click to enlarge")
        
    -   Object file directory length: In the example, the length of **\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager** is 74 characters.
    -   Number of characters in the CMake hash value: The length of the hash value converted by CMake from a long path is fixed at **32**.
    
    The calculation result is as follows: CMAKE\_OBJECT\_PATH\_MAX = 297 – 74 + 32 = 255. Set **CMAKE\_OBJECT\_PATH\_MAX** to **255**.
