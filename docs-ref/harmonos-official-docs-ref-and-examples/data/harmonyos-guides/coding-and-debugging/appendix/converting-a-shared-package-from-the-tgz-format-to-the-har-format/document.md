# Converting a Shared Package from the .tgz Format to the .har Format

Shared packages created in versions earlier than DevEco Studio 3.1 Release are managed with npm and come in .tgz format. To manage these packages with ohpm, you must convert them to .har format as follows:

1.  Decompress the package in .tgz format with a capable file compression tool. For example, on Windows 10/11 or macOS, you can use the system-provided tar tool from the command line.
    
    tar -xvf <tar package path> -C <extract path>
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/l9AkVfevQPq1zQW--6DCjg/en-us_image_0000002500909928.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58B48B39CC72D693D1C3660A1AF233FCF67821549D2B2F2C10A119392E28AC4A)
    
    The decompressed files are stored in the **package** folder in the decompression path.
    
2.  Modify the **package.json** file in the **package** folder to change it into an **oh-package.json5** file. For details, see [Manually Migrating a Historical Project](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V14/ide-ohpm-historical-project-migration-V14#section62481731185412).
3.  Use the file compression tool in step 1 to compress the **package** folder into a .har file.
    
    tar -cvzf <tar package path> package
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/jtYqNyaqRo-KVo5VpkxZ6g/en-us_image_0000002532669841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C60475730AA9A96DEFA5A816A8825A0B89B5E61B1D9BBFE7D5440866582CD77F)
    

Now the .har file can be installed and released using ohpm.
