# What should I do if the memory usage is too high during compilation?

**Symptom**

During compilation and build, memory or CPU usage is too high, resulting in issues such as slow response in DevEco Studio.

**Solution**

-   During hvigor build, memory usage during compilation can be reduced by decreasing cached data in memory and reducing the number of threads.
    
    You can set the following code in the **hvigor-config.json5** file.
    
    {
      "modelVersion": "0.0.1",
      "dependencies": {},
      "properties": {
        // Set to 0, indicating that the memory cache configuration is not enabled. The default value is 4, and the lower the value, the less cached data in memory
        "hvigor.pool.cache.capacity": 0,
        // The default configuration is -1 CPU cores, including ohos.arkCompile.maxSize4. The smaller the value, the less memory it occupies
        "hvigor.pool.maxSize" : 5,
        // The default configuration value is 5, and the smaller the value, the less memory it occupies
        "ohos.arkCompile.maxSize": 3,
        // The default configuration value is true, indicating that the memory cache is turned on and occupies more memory. The configuration is false, and the memory cache is turned off and occupies less memory
        "hvigor.enableMemoryCache": false
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/99ffcofiRqq4YZzE-QktIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B289C81733AF725E068570A36A959755058F8C3B4A57A92EC15481F5E0FB1827)
    
    After the values of **hvigor.pool.maxSize** and **ohos.arkCompile.maxSize** are set to smaller numbers and **hvigor.enableMemoryCache** is set to **false**, the compilation time may increase.
    

-   If the preceding modifications do not yield expected results, you can compile in a non-parallel mode.
    
    -   On the menu bar, choose **File** > **Settings** > **Build, Execution, Deployment** > **Build Tools** > **Hvigor**, and deselect **Execute tasks in parallel mode**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/AKpmdZ6yTjesRgTqE_LiRw/en-us_image_0000002229758673.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08BB7382F42F63B2FD690B84D8D191134EE0ABB7679793958C72F4D2CCA82E7F)
        
    -   Add **\--no-parallel** to the end of the command line. The following is an example:
        
        hvigorw assembleHap --no-parallel
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/pGpaTf-YTRqT7zMfu1iiyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062618Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B92BF4718BB943A11030FD930C5986D28C9609C2C9855E6996BE4A6082B9592)
    
    Using the non-parallel mode for compilation can reduce memory usage, but it may also lead to an increase in compilation time.
