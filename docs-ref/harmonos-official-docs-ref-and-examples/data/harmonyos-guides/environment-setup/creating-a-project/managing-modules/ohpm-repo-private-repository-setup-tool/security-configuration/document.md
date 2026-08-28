# Security Configuration

This section lists the recommended security configuration items designed to enhance the security and reliability of ohpm-repo. You can adopt these configurations as needed.

#### Principle of Least Privilege for Startup

To reduce risks and improve system stability and maintainability, ohpm-repo must be started and deployed as a non-root user.

#### Encrypted Connection and Listening IP Address

By default, the value of **listen** is **http://localhost:8088**, indicating that the HTTP protocol is used and the listening IP address is **localhost**. For more secure data transmission, you are advised to set the [listening IP address](../setting-the-configuration-file/document.md#li146761718065) to the IP address of a specific host and use HTTPS as the communication protocol. Alternatively, you can use HTTPS [reverse proxy](../setting-the-configuration-file/document.md#li1128831818389) on ohpm-repo. When the [custom authentication plugin](../appendix/authentication-plug-in-customization/document.md) or [custom storage plugin](../appendix/storage-plug-in-customization/document.md) is used, you are advised to use HTTPS as the communication protocol if network communication is involved.

listen: https://<_IP address of the host where ohpm-repo is deployed_\>:8088

#### Multi-Instance Deployment

ohpm-repo stores third-party packages of private repositories. To prevent data loss and ensure high availability of ohpm-repo, you are advised to use [MySQL](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_li1552633682171146) for [metadata storage](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_db), [custom storage plugins](../setting-the-configuration-file/document.md#li620610378133) for [package data storage](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_store), and [deploy multiple ohpm-repo instances](../deployment-guide/multi-instance-deployment/document.md) through load balancing.

**MySQL storage**

-   **type**: plugin name. Set this parameter to **mysql**.
-   **config**: plugin configuration. The options are as follows:
    -   **host**: address of the database host
    -   **port**: database port
    -   **username**: database username
    -   **password**: database user password (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
    -   **database**: database name

Configurations for reference:

db:                         
  type: mysql
  config:
    host: "localhost"
    port: 3306
    username: "tctAdmin"
    password: "password"
    database: "repo"

**Custom storage**

Use custom plugins for storage. The specific configuration is as follows:

-   **type**: [type of the custom storage plugin](../appendix/storage-plug-in-customization/document.md). Set it to **custom**.
-   **config**: plugin configuration. The options are as follows:
    -   **export\_name**: class name of the export plugin to be written.
    -   **plugin\_path**: an absolute path of the plugin or a path relative to the ohpm-repo software package. You are advised to place the plugin in the **plugins** directory of the software package.
    -   **custom\_field**: user-defined field. You can obtain its value by using the **getStorageConfigInfo** method of **libs/common/getStorageConfigInfo.js** in the decompressed package of ohpm-repo.
    -   **server**: address for downloading packages from the local repository
        -   If the value of **host** in the [listen](../setting-the-configuration-file/document.md) configuration option is not **0.0.0.0**, **server** uses the complete format of **listen** by default. For example, if the value of **listen** is **127.0.0.1:8088**, the default value of **server** is **https://127.0.0.1:8088**.
        -   If **host** in [listen](../setting-the-configuration-file/document.md) is set to **0.0.0.0**, the value of **host** in **server** is **localhost**, for example, **https://localhost:8088**. You are advised to manually change the value of **host** to the IP address/domain name of the local host. For example, if the value of **listen** is **0.0.0.0:8088**, set **server** to **https://<_Local IP address/domain name_\>:8088**.
        -   If the ohpm-repo service needs to be accessed through the reverse proxy, set this field to the domain name of the reverse proxy server. When ohpm-repo is deployed in multi-instance mode, be sure to configure a reverse proxy server, and set [use\_reverse\_proxy](../setting-the-configuration-file/document.md#section1074004784011) to **true**.

Configurations for reference:

store:
  type: custom                                            
  config:
    export\_name: "MyStorage"                              
    plugin\_path: "plugins/storagePlugin/MyStorage"        
    custom\_field: "test"                                  
    #server: https://localhost:8088

#### Anonymous Access Prohibition

By default, all package information in the ohpm-repo repository is accessible and downloadable by any user. To prevent unauthorized access, choose **System setting** > **System safety** on the ohpm-repo management page and disable the anonymous access feature (enabled by default). After the feature is disabled, only users [with read-only or read-write access tokens](../functions/authentication-management/document.md#li168806431480) specified in the .ohpmrc file can access the packages you upload to ohpm-repo.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/OWMoySnnTNaTYTSuh8ejHA/en-us_image_0000002501068626.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80A3BD5D72436E648F2B14A452FF43F0065BD556CD52284E50F24FF375B518C9 "Click to enlarge")

#### Access Rate Limiting

To prevent malicious users from excessively accessing the repository, set the [user\_rate\_limit](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_server) option, which enforces a default limit of 100 requests per second per user, with a configurable range of (0, 10000\].

user\_rate\_limit: 100

#### Upload Frequency Control

To prevent malicious users from frequently releasing third-party packages, set the [upload\_max\_times](../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_server) option, which limits the maximum number of uploads per user within a 24-hour period. By default, the value is 100. You can modify this value (to **1000**, for example) within the range (0, 100000\] based on operational requirements.

upload\_max\_times: 1000
