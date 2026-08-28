# What should I do if no ASan log is generated when an entry module references a local library?

**Symptom**

When an entry module references a local library and the ASan option is selected, no ASan log is generated.

**Solution**

When an entry module references a local C++ library, set **arguments** to **\-DOHOS\_ENABLE\_ASAN=ON** in the **build-profile.json5** file of the library module, so that the .so file is compiled in ASan mode.

{
  // ...
      "arguments": "-DOHOS\_ENABLE\_ASAN=ON",
      // ...
    }
  },
  // ...
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/rajhHBo9Tieh4rWg9w7rqw/en-us_image_0000002194318360.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062623Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62EC7A901EF4749D251241B0E40E869B99AE5F6245D748111897B8E196BD8411)
