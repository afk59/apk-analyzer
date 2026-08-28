# What should I do if the message "tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes" is displayed when the application UI generates a plug-in and decompresses the .apk file?

**Symptom**

When the application UI generation plug-in is used in the Windows environment, after the configuration items (Install Package Path, SDK Path, and Git Bash Path) are selected and **Next** is clicked, the message "tar.exe: Tool-small extra data: Need at least 4 bytes, but only found 1 bytes" is displayed on the execution terminal of the application UI generation plug-in.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/4n8ANUr8Sh6c55i69hrUkQ/en-us_image_0000002541924407.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062625Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56310F817B770D9CAC13D70B4861FD5833268A7CDD9C0F6B7D65EF345FFFF937)

**Possible Causes**

The built-in **C:/Windows/System32/tar.exe** of the Windows operating system does not support APK file decompression.

**Solution**

1\. Ensure that the system is installed with a tool that can decompress APK files. (APK files are compressed in ZIP format by default. That is, ensure that the system is installed with a tool that can decompress ZIP files.)

2\. Open the "C:/Users/_user name_/AppData/Local/Huawei/_DevEco Studio cache directory_/ui-generation/sim-sdk" directory. Replace _user name_ in the path with the user name used on the computer, and replace _DevEco Studio cache directory_ with the cache directory of the DevEco Studio version in use. For example, if the current DevEco Studio version name starts with **DevEco Studio6.1.xx**, replace _DevEco Studio cache directory_ with **DevEcoStudio6.1**.

3\. Modify the "C:/Users/_user name_/AppData/Local/Huawei/_DevEco Studio cache directory_/ui-generation/sim-sdk/apk\_unzip\_all.sh" file and replace the decompression tool **/c/Windows/System32/tar** with the decompression tool installed. Replace the contents in the file with the following contents:

if \[ "${uu\_names: 0: 5}" == "MINGW" \] || \[ "${uu\_names: 0: 6}" == "CYGWIN" \];then
    mkdir -p $unzipfile
    #/c/Windows/System32/tar -xf $dir\_or\_file -C $unzipfile
    # Use the installed decompression tool to replace the **tar** command.
    unzip -q $dir\_or\_file -d $unzipfile
else
    unzip -q $dir\_or\_file -d $unzipfile
fi

4\. After the replacement is complete, clear the historical conversion cache "C:/Users/_user name_/AppData/Local/Huawei/_DevEco Studio cache directory_/ui-generation/build" and execute the conversion logic again. Check whether the conversion logic can be successfully executed.
