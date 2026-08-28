# What should I do if "Hyper-V not enabled" is reported when the Emulator is started on a Windows PC?

**Symptom 1**

When starting the Emulator, if Hyper-V is not enabled, or if the Emulator is used in a virtual environment, "Hyper-V not enabled." is reported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/vPL_4eGuQRq46JoncRhQlA/en-us_image_0000002394049758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=786B86AAE1FF96B9001CE20D72DBC66FA69A45307BEAEAE113758048B87DD165)

**Solution**

1.  Ensure that the [Working Environment](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-emulator-requirements) of the Emulator meets the requirements.
2.  If the CPU supports virtualization, choose **Control Panel** > **Programs** > **Programs and Features** > **Turn Windows features on or off** (for Windows 11, go to **System** > **Optional features** > **Related settings** > **More Windows features**), select **Hyper-V**, **Windows Hypervisor Platform**, and **Virtual Machine Platform**, click **OK**, and restart the PC. If the issue persists, open the CLI as an administrator, run the **bcdedit /set hypervisorlaunchtype auto** command, and restart the PC.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/cYA4DoKnR6eciTryOw4m5g/en-us_image_0000002394210146.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC2687DE8E011C6BE6FA53080D671C829C19C3485184F5BD253A98871BA8F4D3 "Click to enlarge")
    
3.  If the error persists, open the CLI as an administrator, run the following command, and restart the computer.
    
    bcdedit /set hypervisorlaunchtype auto
    
4.  If the issue persists, choose **Task Manager** > **Performance**. If **Virtualization** is disabled or not enabled, it is disabled in the BIOS. In this case, go to the BIOS settings page based on the mainboard model of the computer and enable the virtualization feature.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/JG4_GlnnQQOxHT-IVJG6ag/en-us_image_0000002427649925.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F11C8022FE1634E50EC80A2334C20DBE6D6D66B70A95AE8F3F89ECE9E31201A "Click to enlarge")
    

If you encounter other problems during the installation and startup of Hyper-V, refer to related documents based on the system version. For more information about Hyper-V installation, see [Install Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/Install-Hyper-V?f=255&amp;MSPPError=-2147217396&amp;tabs=powershell&amp;pivots=windows), [System requirements for Hyper-V on Windows and Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/host-hardware-requirements?pivots=windows).
