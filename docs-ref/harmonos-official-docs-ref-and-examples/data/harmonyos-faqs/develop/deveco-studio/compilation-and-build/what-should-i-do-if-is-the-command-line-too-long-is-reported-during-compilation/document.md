# What should I do if "(is the command line too long?)" is reported during compilation?

**Symptom**

During native project compilation, the following warning and error are reported:

Warning: The length of the project directory exceeds 250 characters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/W6s5rG4lSRO4f4HnCnKSxw/en-us_image_0000002194158988.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98BFAF4DE9C0B1AF9DFAA49A5FDEC5EF517DAD9A790A0BBB9DE7A7005EB7ED5C "Click to enlarge")

Error: "(is the command line too long?)".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/bjhDZ22mRWOcbTs35vrxSQ/en-us_image_0000002194318604.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7F0F84107F760D48EBC6149D1BA520F5B69863E169043B8524C4DD9536FCAFE)

**Solution**

**CMAKE\_OBJECT\_PATH\_MAX** defaults to **250**. It is a variable used in CMake to limit the path length of the object file. It is used to avoid problems caused by the compiler or operating system due to long paths when the build system is generated. If the actual path length of the object file in the project exceeds this value, the compilation will fail and an error will be reported. Theoretically, there is no maximum limit on **CMAKE\_OBJECT\_PATH\_MAX** in CMake. However, the operating system and toolchain have restrictions on the path length. For details, see the operating system and toolchain documentation.

You need to set the value of **CMAKE\_OBJECT\_PATH\_MAX** in the **CMakeLists.txt** file of the project based on the actual path length of the object file. Do as follows:

-   Method 1: Add a file name length to the default value of **CMAKE\_OBJECT\_PATH\_MAX**.
    
    In the example, the length of the warning file **TextMeasureCache.cpp.obj** is 24 characters. Add **24** to the default value **250**, that is, **set(CMAKE\_OBJECT\_PATH\_MAX 274)**.
    
-   Method 2: Calculate the value of **CMAKE\_OBJECT\_PATH\_MAX** based on the actual path length of the object file.
    
    Calculation formula: **CMAKE\_OBJECT\_PATH\_MAX** = Total path length - Directory length + 32. Subtracting the length of the directory part is because CMake converts the directory path into a hash value, and only the length of the file name needs to be calculated.
    
    -   The total path length is the sum of the object file directory length and object file length, which is 297 characters in the figure below.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/1cFUy_v_Q-Kw3lfS5d8d1w/en-us_image_0000002229604381.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45FF3A4784A1141C1C7A53BFD2DABA5D190DC4637842009A2A800F2BC9D8592F "Click to enlarge")
        
    -   Object file directory length: In the example, the length of **\_\_/\_\_/\_\_/\_\_/\_\_/third-party/rn/ReactCommon/react/renderer/textlayoutmanager** is 74 characters.
    -   Number of characters in the CMake hash value: The length of the hash value converted by CMake from a long path is fixed at **32**.
    
    The calculation result is as follows: CMAKE\_OBJECT\_PATH\_MAX = 297 – 74 + 32 = 255. Configure **set(CMAKE\_OBJECT\_PATH\_MAX 255)**.
    
-   Method 3: If the same error persists after **CMAKE\_OBJECT\_PATH\_MAX** is set, save the project in a directory with a shorter path.
