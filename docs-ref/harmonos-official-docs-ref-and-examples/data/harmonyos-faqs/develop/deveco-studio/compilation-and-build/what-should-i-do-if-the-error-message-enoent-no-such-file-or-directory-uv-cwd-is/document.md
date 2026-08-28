# What should I do if the error message "ENOENT: no such file or directory, uv\_cwd" is displayed?

**Symptom**

When a project is rebuilt after being forcibly deleted and manually restored, an error message similar to the following is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/wIX_TaAcQNeKterLb3cRPg/en-us_image_0000002342994341.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B17CBBAFB111C01AAA6914BC9BC05B1B43941F16B6B007F6E6D2EE540C46E623)

**Possible Causes**

When the Node.js process is running, the **process.cwd()** method returns the current working directory of the process when the process is started or changed through **process.chdir()**. If the current working directory of the process is forcibly deleted (for example, the user manually deletes the project folder), all subsequent operations (such as file reading and directory traversal) that depend on the directory paths will fail and errors will be reported because the referenced directory does not exist.

**Solution 1**

Close all Node.js processes and rebuild the project.

On Linux:

pkill node

On macOS:

killall node

On Windows:

taskkill /F /IM node.exe

**Solution 2**

The no-daemon mode is recommended for pipeline packaging.

Change **\--daemon** to **\--no-daemon** when running hvigorw assemble app or hvigorw assemble hap.
