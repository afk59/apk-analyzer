# Why does a third-party dependency library of a C/C++ project fail to be packaged into the HAP?

**Symptom**

The HAP generated does not contain the third-party .so file, on which the C/C++ project depends.

**Solution**

Currently, DevEco Studio has restrictions on the addressing mode of third-party .so files in C/C++ projects. If a third-party .so file is not packaged into the HAP, change the import mode of the .so file.

1.  Define an alias (for example, **jsbind\_shared\_lib\_tracing**), indicating the third-party .so file to be imported.
2.  Use **SHARED IMPORT** to dynamically import the third-party .so file.
3.  Use **IMPORTED\_LOCATION** to define the location of the imported .so file.
4.  Declare the defined three-party .so file to the target. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/QlG6KpIASnCwUaiJaz-DYg/en-us_image_0000002194318404.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13EFE1AC34B5D9D779D783916909DCD89573B16E6063AF54C02F5BA1B2CAA979) 
5.  Generate a HAP again and check that the third-party .so file is packaged into the HAP.
