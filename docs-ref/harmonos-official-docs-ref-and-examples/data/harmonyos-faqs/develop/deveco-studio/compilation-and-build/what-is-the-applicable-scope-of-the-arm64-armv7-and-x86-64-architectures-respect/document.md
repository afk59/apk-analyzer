# What is the applicable scope of the ARM64, ARMv7, and x86\_64 architectures respectively?

**Symptom**

The created Native C++ project supports three architectures by default: ARM64, ARMv7, and x86\_64. What are the applicable scopes of these architectures?

In the DevEco Studio 3.1.1 release, the Emulator supports only ARM64.

In the DevEco Studio Next Preview1, the Next real device supports only ARM64.

Are there ARMv7 and x86\_64 SDKs? In which scenarios are these two architectures used?

**Solution**

ARM64: 64-bit ARM architecture, which is applicable to modern mobile devices and embedded systems, such as smartphones, tablets, and IoT devices.

ARMv7: 32-bit ARM architecture, which is applicable to early mobile devices and low-power IoT devices.

x86\_64: 64-bit x86 architecture, which is applicable to desktop computers, servers, and VMs based on x86 processors. You do not need to provide the ARMv7 and x86\_64 versions.
