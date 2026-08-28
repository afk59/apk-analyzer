# How do I specify the target OS architecture during HarmonyOS build?

**Question**

In webrtc gn, **binary\_prefix** is used to determine the architecture of the build tool. How do I set the target architecture for HarmonyOS?

**Answer**

You can use **\-target** to set the target OS architecture. **\--target aarch64-linux-ohos** and **\--target arm-linux-ohos** correspond to the 64-bit and 32-bit architectures, respectively.
