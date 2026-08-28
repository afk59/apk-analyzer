# Device Security Mode Query (C/C++)

#### Use Cases

Device Security Kit provides the capability of querying the system security mode. By calling the API provided by Device Security Kit, your app can check the current security mode (common or Secure Shield) of the device and provide differentiated services accordingly.

-   Common mode: This is the default mode of the operating system and applies to most users.
-   Secure Shield mode: This is a system-level security mode provided for users with high security requirements. This mode restricts basic device capabilities to enhance security and effectively defend against targeted attacks on the remote attack surface.
    
    In the Secure Shield mode, the operating system prohibits apps from requesting executable anonymous memory.
    
    Apps must adapt to the system security mode by disabling the just-in-time (JIT) compilation function or switching to interpreted execution.
    

#### Development Procedure

1.  Import and link the shared library of the device security mode in **CMakeLists.txt**.
    
    find\_library(dsm-lib libdevice\_security\_mode.z.so)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so ${dsm-lib})
    
2.  Import the header file of the device security mode.
    
    #include <DeviceSecurityKit/device\_security\_mode.h>
    
3.  Call the API to query the current security mode of a device.
    
    int32\_t IsSecureShieldModeOn(void)
    {
        DSM\_DeviceSecurityMode mode = HMS\_DSM\_GetDeviceSecurityMode();
        return mode & DSM\_SECURE\_SHIELD\_MODE;
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/y2_zr868TkqJJfpo9IOPLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65C64709EFFF7A26C855A4756F12DE0E6684B85DDCB0D9FAAD052F59ECF74CF7)

If the ArkWeb component is used in your app, you need to evaluate the compatibility of web features by referring to [Using Secure Shield Mode](../../../../application-framework/arkweb/managing-cyber-security-and-privacy-for-the-web-component/using-secure-shield-mode/document.md).
