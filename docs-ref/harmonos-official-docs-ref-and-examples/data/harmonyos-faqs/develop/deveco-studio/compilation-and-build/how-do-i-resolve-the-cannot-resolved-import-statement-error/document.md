# How do I resolve the "Cannot resolved import statement" error?

**Symptom**

The error message "Cannot resolved import statement" is displayed during compilation.

**Possible Causes**

When a file is imported, the case is inconsistent. (When the file is imported to a single folder, the **index.ets** file (lowercase) is addressed by default, but only the **index.ets** file (uppercase) exists in the folder.)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/7QhMsMVKRdC6ysGE1sKhGQ/en-us_image_0000002194318384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062620Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18A490B3E88B779E3553C3955616356F4347866B7A84B8A158120D06BB3A07AF)

**Solution**

Check the actual file name in the directory. Ensure that the case matches what is specified in the import statement.
