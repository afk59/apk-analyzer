# What should I do if "App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime." is reported during compilation?

**Symptom**

DevEco Studio compilation fails and "App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime." is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/oq3jUBB7RPiLztC1XszKOg/en-us_image_0000002229604181.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=871410C20DBEEA85C55C16C14EBD4B6AF011B15B801C0B4D917AE0797E6FA28A)

**Solution**

Modify the **build-profile.json5** file, log in to your HUAWEI ID, and sign the file again.

1.  In the **build-profile.json5** file in the root directory, change **"runtimeOS": "OpenHarmony"** to **"runtimeOS": "HarmonyOS"**.
2.  Choose **File** > **Project Structure** > **Signing Configs** to configure signing.
3.  Select **Support HarmonyOS** and **Automatically generate signature**.
4.  Click **Sign In**.
5.  Log in to your HUAWEI ID and enter your mobile number and verification code as prompted.
