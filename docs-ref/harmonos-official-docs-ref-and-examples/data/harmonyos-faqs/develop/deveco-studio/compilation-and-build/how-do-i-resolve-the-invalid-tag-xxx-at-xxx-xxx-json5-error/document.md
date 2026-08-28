# How do I resolve the "Invalid tag 'xxx' at 'xxx/xxx.json5'." error?

**Symptom**

The "Invalid tag 'xxx' at 'xxx/xxx.json5'." error is reported during compilation.

**Possible Causes**

In the indicated **parameterFile** configuration file, the tag used for the parameter defined in the **oh-package.json5** file in the project root directory contains invalid characters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/9Fd_be3qT1-ZxU_NRmi4lQ/en-us_image_0000002229758505.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68E4711477EEDD0BD048919A911BC3AF024688788B62A7E628B3DA9DAD4545A7)

**Solution**

Make sure the tag starts with a letter or digit, contains a maximum of 60 characters consisting of only letters, digits, periods (.), hyphens (-), and underscores (\_), and is not **latest**.
