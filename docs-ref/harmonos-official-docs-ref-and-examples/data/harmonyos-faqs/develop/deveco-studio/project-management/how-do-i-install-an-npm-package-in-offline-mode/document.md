# How do I install an npm package in offline mode?

Prerequisites

-   A PC with Internet access is available.
-   A PC in the offline environment with Node.js installed is available.
-   The PC in the offline environment has the Verdaccio tool installed.

1.  On the PC with Internet access, use npm-pack-all to package all dependencies into .tgz files.
    1.  Install npm-pack-all: **npm install -g npm-pack-all**.
        
        This will also install the husky package, which is a dependency for npm-pack-all.
        
    2.  Download the required dependencies: **npm install -g _bundleName_**. The following figure uses webpack as an example, that is, **npm install -g webpack**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/GzXikcLmQ_KKKdEVIcCKeA/en-us_image_0000002229758193.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A20D3438BE89C3BB01AB9EBE2D012453B4B7C9B8A037960BD2CF2FD482FF5A92)
        
    3.  Run the **cd C:\\Users\\_User name_\\AppData\\Roaming\\npm\\node\_modules\\_bundleName_** (for example, webpack) command to go to the global npm package path, and then run the **npm-pack-all** command to create a .tgz file.
2.  Transfer the .tgz file to the PC in the offline environment. Then, run the **npm install _XXXX_.tgz** command on that PC to install the .tgz file.
3.  After successfully installing the .tgz file, configure the npm registry path on the offline PC to the local path.
    1.  On the PC in the offline environment, run the **verdaccio** command.
    2.  After the command is executed successfully, a local npm server is set up. In a new CLI, run the **npm config set registry http://127.0.0.1:4873** command to set the npm registry. Then, run the **npm config get registry** command to check whether the setting is successful.![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/sFJE9azsReiBl5lJCMsg6w/en-us_image_0000002194317944.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66F9A17A840128CD4695D5CF011C445A383AB1F549BC1971D2ACD2FB1B3EDADF)
4.  With the local npm server set up, you can update your project's npm dependencies even in the offline environment.
    1.  Go to the project directory and run **npm install** to install or update npm dependencies.
    2.  Note: If the error message "404 Not Found 'xxx'" is displayed during the installation, the required dependencies are missing. In this case, you will need to copy the missing dependency files from an online environment and follow the same process as described above.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/0_TsX-rKSm6_vjncPD5cLg/en-us_image_0000002229603725.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=435353819A263C2CC6B86D936A2CA3CB9521879BFFB4497271BB8E5C84D66FC0 "Click to enlarge")
