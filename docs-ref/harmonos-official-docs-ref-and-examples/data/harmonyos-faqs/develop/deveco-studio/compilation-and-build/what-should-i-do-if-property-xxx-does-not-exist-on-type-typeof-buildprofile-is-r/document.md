# What should I do if "Property xxx does not exist on type 'typeof BuildProfile'." is reported during compilation?

**Symptom 1**

The custom parameter **BuildProfile** is used without exception occurring at compile time, but the build fails and "Property xxx does not exist on type 'typeof BuildProfile'" is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/M-frwRzSQ6WMJ3w4UALJIw/en-us_image_0000002229604165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F37E67C8B0034C766EA6BB308261E7DC2A63AEA5AE346DF08DE03A56A3F6526)

**Solution**

Check whether the key values of the custom parameters configured under **targets** > **buildProfileFields** in **build-profile.json5** of the current module are the same. If not, set the same key values for all **buildProfileFields** in **targets**.

The following example shows an incorrect configuration that causes the compilation error:

"targets": \[
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName1": "default1"
          }
        }
      }
    }
  }
\]

Change the key values of all **buildProfileFields** in **targets** to the same. For example, change the key values to **targetName**.

**Symptom 2**

The custom parameter **BuildProfile** used is marked red by the compiler, and the build fails with "Property xxx does not exist on type 'typeof BuildProfile'." reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/mpfX3vKESgmLIkzNJPHiaw/en-us_image_0000002194318396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E60F9D84D9A2767D1B4B802E18B21571C9AA54EEAE3ED47FC1D38B1B7C0044C)

**Solution**

Check the **build-profile.json5** file of the current module and ensure that the custom parameters have been added to **buildProfileFields**.
