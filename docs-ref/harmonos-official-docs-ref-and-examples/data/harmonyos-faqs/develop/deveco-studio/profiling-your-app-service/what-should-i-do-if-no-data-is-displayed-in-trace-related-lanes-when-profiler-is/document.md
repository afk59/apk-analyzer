# What should I do if "No Data" is displayed in trace-related lanes when Profiler is used to record data on macOS?

**Symptom**

When the Profiler is used to record data on macOS, trace-related lanes may display "No Data".

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/JSklXi3NT26EJDkrc5IHgQ/en-us_image_0000002516464433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062624Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=988B99FC4575C0B5F947BDEF5ED3BC936DA689F56910486B0DD2CD5BAD270E5E "Click to enlarge")

**Possible Causes**

The chip of the current macOS model does not support **trace\_streamer** parsing. As a result, "No Data" is displayed in trace-related lanes when data is recorded.

**Root Cause Verification**

You can perform the following steps to verify:

1.  Find the directory where **trace\_streamer.exe** is located in the DevEco Studio installation directory on macOS.
2.  Use the command line tool to run the **trace\_streamer.exe 1.htrace -e 1.db** command to parse a trace file.
3.  If the command output is **zsh: bad CPU type in executable**, the current macOS chip does not support **trace\_streamer** parsing.

**Solution**

The provided **trace\_streamer.exe** binary file is for the x86 architecture. If macOS uses the ARM architecture, the parsing is not supported. This issue can be resolved by installing Rosetta.
