# Why does macOS activity monitor show high memory usage of the Emulator?

After you configure the emulator memory to 4 GB and use it for a period of time, you may find that the emulator process occupies more than 6 GB memory in Activity Monitor (as shown in the following figure). Note that 6.49 GB in the figure does not represent the physical memory (**Dirty** memory) actually used by the Emulator process, but the **phys\_footprint** memory occupied by the Emulator process. In macOS, the **phys\_footprint** memory is much higher than the **Dirty** memory for virtualization platforms (such as emulators).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/r1V3k1VsSLu6EvbySl8bxg/en-us_image_0000002229758733.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DBF5F1B426731D21003C6C272D4791E13A729387D30AEFCB96F85018DCFDC72 "Click to enlarge")

To view the **Dirty** memory, open the activity monitor, view the process ID (PID) of the Emulator, and run the **footprint -vmObjectDirty PID** command.
