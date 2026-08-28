# How do I resolve the "The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'." error?

**Symptom**

The **tag** keyword is not allowed for the **version** field in the **oh-package.json5** file.

**Possible Causes**

When the value of the **version** field in the **oh-package.json5** file is configured using **parameterFile**, the relevant parameter in the **parameterFile** configuration file incorrectly contains the **tag** keyword.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2zOV5ekCRwuV8jMeGEJWNQ/en-us_image_0000002229604173.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4C39A9169C8B8360F53BC5BFC0DAE710D5DF714925B0CDF93624A46E4A880F1)

**Solution**

Identify the parameter referenced in the value of the **version** field in the **oh-package.json5** file, and update its value in the corresponding **parameterFile** configuration file to a valid value that does not contain the **tag** keyword.
