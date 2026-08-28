# What should I do if an error occurs during the compilation after react-native-openharmony is upgraded?

**Symptom**

An error occurs during the compilation after **react-native-openharmony** is upgraded. The error information is similar to the following:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/6emgJpQtSc6LofzsZxF3zw/en-us_image_0000002304734606.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DBBE93B603AB896C169B1D4E0CD346C7E6858D141F6DA3EE3631A5CD765C9208)

**Possible Causes**

The cache of the earlier **react-native-openharmony** version still exists. As a result, some links cannot be found.

**Solution**

Delete the **.cxx** and **build** directories in the root directory of the module to be compiled, and then trigger the compilation again.
