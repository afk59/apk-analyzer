# Getting Started

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Q4liBCPTTU6wOQTAofiudQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C29E541DF8C0077C68C7FD3DB43DD8E8EC977599D18D9876E01F18BAC825A64E)

You cannot install and start ohpm-repo as the **root** user on Linux or macOS. Install and run it as a non-root user.

#### How to Install

1.  Ensure that Node.js 18.x is installed and that environment variables are properly configured. For details about how to install Node.js, visit the [Node.js website](https://nodejs.org/download/release/latest/).
    
2.  Download the ohpm-repo tool package from the [Download Center](https://developer.huawei.com/consumer/en/download/ohpm-repo), and verify its integrity by following the instructions in **Tool integrity**.
    
3.  Decompress the ohpm-repo tool package.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/1BMeD4xFTqu3wN786EFZ-A/en-us_image_0000002500908780.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B1042A9DF2A72154F79F5D702E23D066F77D39B1AE9B68BDD4715FC2A65AA06)
    
4.  Set the path of the **bin** directory in the directory where the ohpm-repo tool package is decompressed to the [system environment variable](../faqs/document.md#section24117279211) **path**, and run the following command to query the version number:
    
    ohpm-repo -v
    
    If the version number (for example, 2.0.0) is displayed, the installation package is decompressed properly. If an error is reported, rectify the fault by referring to [FAQs](../faqs/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/vEJSU8AsQOOPag8mPY1CLA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFECAB264A1C2F1FA6A1752AAC5AF85C7D528823B76BE3218C01935867FBADF2)
    
    For Linux and macOS, you are advised to use Bash or Zsh. If other shell types are used, the environment variables of the ohpm-repo deployment root directory [deploy\_root](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_deploy_root) are written to the .bashrc file by default.
    
5.  Before starting ohpm-repo, go to the **conf** directory where the ohpm-repo tool package is decompressed and open the **config.yaml** [configuration file](../setting-the-configuration-file/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/WQ8HpGR4Qb-l3VWojh9cQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=641CBA87353766DF2D9377D28D113D9161E59E6E8C52C0356814C725FA31FFD7)
    
    **Methods of modifying the configuration file after ohpm-repo is started successfully:**
    
    -   If a configuration file is specified when you run the **install** command for the initial setup of ohpm-repo, locate and modify that file, then rerun the **install** command to apply the modified configuration, followed by the **start** command to launch ohpm-repo.
    -   If no configuration file is specified when you run the **install** command for the initial setup of ohpm-repo, the default configuration file in the **conf** directory under the ohpm-repo extraction path is used. Modify this file, then rerun the **install** and **start** commands to apply the configuration and launch ohpm-repo.
    
6.  Check the [listen](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_listen) configuration. The default value is **localhost:8088**, indicating that only the local IP address can be listened on. If you want other hosts to access the system using the IP address or domain name, you are advised to change the value of **listen** to the IP address of the host where ohpm-repo is deployed.
    
    listen: <_IP address of the host where ohpm-repo is deployed_\>:8088
    
7.  Check the [deploy\_root](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_deploy_root) configuration. If it is not configured, the default address is used. The path cannot be set to the root directory where ohpm-repo is decompressed.
8.  Check the [db](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_db) and [store](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store) configurations. **db** is the configuration option of metadata storage, and **store** is the configuration option of file storage. **db** supports FileDB local storage and MySQL database storage. **store** supports file storage, SFTP storage, and custom storage. **db** and **store** cannot be used together randomly and must comply with the mapping in Table 1. By default, **db** is set to the FileDB local storage, and **store** is set to the file storage.
    
    **Table 1** Mapping of db and store configurations
    | 
    db: Metadata Storage
    
     | 
    
    Corresponding store Type
    
     |
    | :-- | :-- |
    | 
    
    FileDB
    
     | 
    
    File storage
    
     |
    | 
    
    MySQL
    
     | 
    
    File storage, SFTP storage, custom storage
    
     |
    
9.  Check whether [store.config.server](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store) is configured to specify the download address of the ohpm-repo repository. If this parameter is not set, the default value is used. For details, see [en-us\_topic\_0000002500908752.html#EN-US\_TOPIC\_0000002500908752\_\_en-us\_topic\_0000001745376470\_li922300957171146](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_li922300957171146). You must set this parameter if the value of **host** in [listen](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_listen) is **0.0.0.0** and the local host has multiple network interfaces. In such cases, you are advised to change the value of **host** to the specific IP address/domain name of the local host. For example, if the value of **listen** is **0.0.0.0:8088**, set **server** to **http://<_IP address/domain name of the deployment host_\>:8088**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/deR7400iS5yFEnbLzniTCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97C71CFD01A594202E59873270F1A53F30552D9C8481591E7198D882D1803714)
    
    -   Use the IP address of the reverse proxy server if it is configured for the **ohpm-repo** service.
    -   If ohpm-repo is started in multi-instance mode, a reverse proxy server must be configured. A unified download address is required for multiple instances.
    -   For details about the configurations in the **config.yaml** file, see [Setting the Configuration File](../setting-the-configuration-file/document.md).
    
10.  Go to the **bin** directory where the ohpm-repo tool package is decompressed and run the **install** command:
     
     ohpm-repo install
     
     The following is an output example:
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/Tv5QpRIYTEy44uMIzaee5w/en-us_image_0000002501068638.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2173D85310ED7523CA8B2DD1BCED391BB016660ACE8499A2D7000DF31EF0F694 "Click to enlarge")
     
11.  After the installation is successful, you must update environment variables of the deployment directory based on the displayed information. The update method varies with the operating system — Windows or Linux/macOS.
     
     -   Windows: Close the current window and open a new window.
     -   Linux or macOS: Run the reload command in the CLI. If the shell is Bash, run the **_source ~/.bashrc_** or **_. ~/.bashrc_** command. If the shell is Zsh, run the **_source ~/.zshrc_** or **_. ~/.zshrc_** command.
     

#### How to Start

After installation, go to the **bin** directory in the directory where the ohpm-repo tool package is decompressed and run the following command to start ohpm-repo:

ohpm-repo start

If the startup is successful, the following log information is displayed:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/nCt-279mRh6wjG2jyFzpXA/en-us_image_0000002532668671.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA8407BD36DAC02D757BF2E38799D5CD5CB40F9D0F88E496426FA668082A46EF "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/C3gLff_9S1mlzDOj4gwr1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=557833D693C6DDD56192835C088D1D9FDCDF908A8BC9EFD3CDE6CB23CEC6F63E)

When ohpm-repo is started for the first time, an administrator account is created by default. The account name is _**admin**_ and the password is _**12345Qq!**_. You need to change the password upon first login, and then log in to the system again.

#### Obtaining Third-Party Libraries from ohpm-repo

You can configure the private repository for all projects. For example, run the following command:

ohpm config set registry <_Configured ohpm-repo service address_\>/repos/ohpm
ohpm install

Alternatively, configure the **\--registry** parameter on the CLI. For example, run the following command:

ohpm install @ohos/lottie --registry <_Configured ohpm-repo service address_\>/repos/ohpm

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/NK8U8cExTLSaU9rzW5I3Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B42CE99CF073BAFC54783F7C896193C275ED011F37258B18AC7A97743B93DA3)

<_**Configured ohpm-repo service address**_\> indicates the value of **[store.config.server](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store)** in the configuration file. For example, if **[store.config.server](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store)** is set to **http://127.0.0.1:8088**, then the value of **registry** is **http://127.0.0.1:8088/repos/ohpm**. If **[store.config.server](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store)** is not set, the default value is used.

#### Publishing Third-Party Libraries to ohpm-repo

The third-party libraries contain static shared packages (HARs) and dynamic shared packages (HSPs), which can be published using the ohpm CLI tool or web page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/h7FASPF1TI-IulJbxAiYvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=706F24D45791AD1FC0C1316944023D42C1CE949AD134A8D43D2D228EF8854EFA)

Since the ohpm CLI tool 1.3.0 and ohpm-repo 1.1.0, HSPs can be published to ohpm-repo as .tgz files. In earlier versions, only HARs in .har files can be published.

## Publishing with the CLI Tool

1.  Run the following command to use the ssh-keygen tool to generate a public key and a private key:
    
    ssh-keygen -m PEM -t RSA -b 4096 -f <your\_key\_path>
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/n3ZbLi-pSfKjVuGnLX8-zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06E415B925AC2BF38E3F6893C7B162C3C19E413C0FF64AED6DCD6DE49E13ADDF)
    
    -   **<_your\_key\_path_\>**: name and storage path of the public key and private key. If only the name is contained, the current working path of the CLI is used as the storage directory.
    -   The OHPM package manager supports only encryption key authentication. Enter the password when generating the public and private keys.
    
    Example:
    
    ssh-keygen -m PEM -t RSA -b 4096 -f D:\\path\\my\_key\_path
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/khtpp0LhRx-9yPhoyIhH9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01E097BA3371D72FF1C96D969D640D6F867A6F36D7BC241FDF8010588E334174)
    
    The public key and private key are stored in the **path** directory of drive D, named **my\_key\_path.pub** and **my\_key\_path**, respectively.
    

2.  Log in to the ohpm-repo management address, click **PersonalCenter** in the upper-right corner of the home page and choose **Security manage**, add a public key, and paste the content of the public key file (**<_your\_key\_path_\>.pub**) to the public key text box.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/4OAj3FZ9RsS7w5RInjdRUA/en-us_image_0000002532748645.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D740562DACD1F50F63AC062029BAC5C51FE27420D5C5D2CDD7DC4787BD615F55 "Click to enlarge")
    

3.  Open the CLI tool and run the following command to set the private key path:
    
    ohpm config set key\_path <your\_key\_path>
    

4.  Log in to the ohpm-repo management address, click **PersonalCenter** in the upper-right corner of the home page, and copy the publish ID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/-NjeK7YgTwi2GRflgS2Y1g/en-us_image_0000002532668667.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22ADE2CF061F5B5288E369DA8D1A1B8CFFC4F9BF37E4BC4305F5619A0769EDFF "Click to enlarge")
    

5.  Run the following command to configure the publish ID in the **.ohpmrc** file:
    
    ohpm config set publish\_id <your\_publish\_id>
    

6.  Publish static shared packages (HARs) and dynamic shared packages (HSPs) of third-party libraries in different ways.
    
    -   Static shared packages (HAR packages)
        
        Run the **ohpm publish <_HAR package path_\>** command to publish HAR packages, where **<_HAR package path_\>** must be a specified path pointing to a file with .har extension. Example:
        
        ohpm config set publish\_registry <_ohpm-repo management address_\>/repos/ohpm
        ohpm publish demo.har
        
        You can also run the following command with **\--publish\_registry** configured:
        
        ohpm publish demo.har --publish\_registry <_ohpm-repo management address_\>/repos/ohpm
        
    
    -   Dynamic shared packages (HSPs)
        
        The dynamic shared packages (HSPs) cannot be directly published in ohpm-repo. You must first convert them to .tgz packages. For details, see [Building an HSP Module](../../developing-and-publishing-shared-packages/developing-a-dynamic-shared-package/document.md#section67683213597). The publishing process of .tgz packages is the same as that of HAR packages.
        
        To publish a .tgz package, run the **ohpm publish <_.tgz package path_\>** command, where **<_.tgz package path_\>** is the path to a file with .tgz extension. Example:
        
        ohpm config set publish\_registry <_ohpm-repo management address_\>/repos/ohpm
        ohpm publish demo.tgz
        
        You can also run the following command with **\--publish\_registry** configured:
        
        ohpm publish demo.tgz --publish\_registry <_ohpm-repo management address_\>/repos/ohpm
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/49xUutSwTV-etNBM14sTDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D987E42AC6FAA72742FF9D705BD2B99ED3C50C7707CEB2D99C5F7AAE22D19A36)
    
    -   Check [Developing and Referencing Shared Packages](../../developing-and-publishing-shared-packages/document.md) to find more information about how to develop HAR and HSP packages, how to convert HSPs to .tgz packages, and how to convert .tgz to .har.
    -   The rules for the ohpm-repo management address are as follows:
        -   If **host** in **listen** is not **0.0.0.0**, use the full value of **[listen](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_listen)** as the ohpm-repo management address. For example, if **listen** is **_localhost_:8088**, set the management address to **http://_localhost_:8088**.
        -   If **host** in **listen** is **0.0.0.0**, replace it with the IP address/domain name of the server where ohpm-repo is deployed. For example, if **listen** is **0.0.0.0:8088**, set the ohpm-repo management address to **http://<_IP address/domain name of the server where ohpm-repo is deployed_\>:8088**.
    

## Publishing on Web Pages

On the web page, log in to the ohpm-repo management address as an administrator. Go to **PersonalCenter** > **Repository manage**, and choose **Manage Third-Party Packages** > **Upload package** to upload a third-party package. The package name extension must be .har or .tgz.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/95GP2oXdR0SH31PF5fd1ZA/en-us_image_0000002501068630.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2A1EF10C0EDFAE09FB44CF6BB6C682B200309FB78A1C59B7372CAE2FDC5AD62 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/EhWCJ75XS22nNEFf-eppXg/en-us_image_0000002501068616.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=282CB2E716C2FB4058F9FAE7D5D593FC866B4E240F4363E33D1922A38C49E194 "Click to enlarge")
