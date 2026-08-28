# Setting the Configuration File

The **config.yaml** file is a key configuration file for ohpm-repo. You can use it to modify the default parameter settings, start the plugin, and extend functionality. This file is located in the **conf** directory under the directory where the ohpm-repo tool package is decompressed. ohpm-repo reads this file by default when running the **install** command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/7iqLF_64T1eJyayFepbGyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=526842303134726738D02BD599504197D45C4C12D0DC7CC5D905AE99BD4CB30F)

**Methods of modifying the configuration file after ohpm-repo is started successfully:**

-   A configuration file is specified when you run the **install** command before starting ohpm-repo for the first time: Find the specified configuration file, modify the file content, run the **install** command again to specify the modified configuration file, and then run the **start** command to start ohpm-repo.
-   No configuration file is specified when you run the **install** command before starting ohpm-repo for the first time: By default, use the configuration file in the **conf** directory in the path where the ohpm-repo package is decompressed. Modify the file content and run the **install** and **start** commands again.

#### Default Settings

\##### server configuration section #####
listen: localhost:8088        # You are advised to change it to a specific IP address or domain name.
# listen:
# - localhost:8088            # Listen to the loopback address of the local host.
# - http://localhost:8088     # Listen to the loopback address of the local host.
# - 0.0.0.0:8088              # Listen to all addresses of the local host (INADDR\_ANY).
# The protocol can be HTTP or HTTPS. The default protocol is HTTP.
# port: 1-65535 (Windows)/1024-65535 (Linux or macOS)

#Optional (mandatory when the listen value is an HTTPS address)
https\_key: ''                 # Path of the key used by the HTTPS service (If this parameter is not set, the default value '' is used.)
https\_cert: ''                 # Path of the crt used by the HTTPS service (If this parameter is not set, the default value '' is used.)

##### server deploy root section #####
deploy\_root: ''                # Installation root directory. Only absolute paths are supported, and the directory must exist.

##### server numeric limit section #####
max\_package\_size: 500          # Maximum size of a package to be uploaded, (0, 500\] in MB. If this parameter is not set or set to 0, the default value 500 is used.
max\_extract\_size: 800          # Maximum size of a package after decompression, in MB. If this parameter is not set or set to 0, the default value 800 is used.
max\_extract\_file\_num: 30000    # Maximum number of files after decompression. If this parameter is not set or set to 0, the default value 30000 is used.
user\_rate\_limit: 100           # User access frequency control, (0, 10000\] in times/h. If this parameter is not set or set to 0, the default value 100 is used.
fetch\_timeout: 60              # Request/response timeout interval, (0, 3600\] in seconds. If this parameter is not set or set to 0, the default value 60 is used.
keep\_alive\_timeout: 60         # Timeout interval for keeping a TCP connection, (0, 3600\] in seconds. If this parameter is not set or set to 0, the default value 60 is used.
api\_timeout: 60                # API timeout interval, (0, 3600\] in seconds. If this parameter is not set or set to 0, the default value 60 is used.
upload\_api\_timeout: 300        # Timeout interval for the third-party package upload API, (0, 3600\] in seconds. If this parameter is not set or set to 0, the default value 300 is used.
upload\_lock\_hour: 24           # Period within which a new third-party package with the same name cannot be uploaded, after all versions of a third-party package are removed, (0, 168\] in hours. If this parameter is not set or set to 0, the default value 24 is used.
upload\_max\_times: 100          # Maximum upload times of a single user within 24 hours, (0, 100000\]. If this parameter is not set or set to 0, the default value 100 is used.
operation\_log\_retention: 100   # Duration for storing operation logs in the database, in days. If this parameter is not set or set to 0, the default value 100 is used.

##### metadata storage section #####
## The data storage type can be either filedb or mysql. Only one type can be configured.
db:                         # The value must be a YAML array.
  type: filedb
  config:                   # If you want to change the storage path and retain the old data, migrate the data files from the old path to the new path.
    path: ./db              # Local data storage path. If this parameter is not set, the default value <deploy\_root>/db is used.

#db:                        # The value must be a YAML array.
#  type: mysql
#  config:
#    host: "localhost"      # Database host address
#    port: 3306             # Database port (0,65535\]
#    username: tctAdmin         # Database user name
#    password: "password"   # Database user password (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
#    database: "repo"       # Database name

##### storage section #####
## The file storage type can be fs, sftp, or custom. Only one type can be selected.

store:                               # The value must be a YAML array.
  type: fs
  config:                            # If you want to change the storage path after uploading resources, migrate the data from the old path to the new path.
    path: ./storage                  # Storage path of the published third-party library. If this parameter is not set, the default value <deploy\_root>/storage is used.
    #server: http://localhost:8088   # Address for downloading the repository. If this parameter is not set, the default value is used.

# If the file storage type is set to sftp, a maximum of three SFTP servers can be configured.
#store:                               # The value must be a YAML array.
#  type: sftp                         # The type of store can be sftp only when the type of db is mysql.
#  config:
#    location:
#      -
#        name: test\_one\_sftp          # Host name, which must be unique.
#        host: "localhost"            # Host address
#        port: 22                     # Host port (0,65535\]
#        read\_username: "read"        # Name of the user with read permission on the host
#        read\_password: "password"    # Password of the user with read permission on the host (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
#        write\_username: "write"      # Name of the user with write permission on the host
#        write\_password: "password"   # Password of the user with write permission on the host (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
#        path: /source22              # File path relative to the SFTP root directory. The path must start with a slash (/) and the path folder must exist.
#      -
#        name: test\_two\_sftp
#        host: "localhost"
#        port: 24
#        read\_username: "read"
#        read\_password: "password"
#        write\_username: "write"
#        write\_password: "password"
#        path: /source24
#    #server: http://localhost:8088   # Address for downloading the repository. If this parameter is not set, the default value is used.

#store:
#  type: custom                                            # custom is a custom storage plugin type. For details about the development process of the custom storage plugin, see the [guide document](../appendix/storage-plug-in-customization/document.md).
#  config:
#    export\_name: CustomStorage                            # Class name of the export plugin
#    plugin\_path: plugins/CustomStorage.js                 # Absolute path of the plugin or a path relative to the ohpm-repo software package. You are advised to place the plugin in the plugins directory of the software package.
#    custom\_field: "test"                                  # Customized field. Obtain the value of the customized field by introducing the getStorageConfigInfo method of libs/common/getStorageConfigInfo.js.
#    #server: http://localhost:8088                        # Address for downloading the repository. If this parameter is not set, the default value is used.

##### use\_reverse\_proxy section #####
# The options are true and false. The default value is false. If a reverse proxy is used, set this to true. The client IP address will be obtained from the x-forwarded-for field in the request header.
use\_reverse\_proxy: false

##### uplink section #####
uplink\_cache\_path: ./uplink      # Cache path. If this parameter is not set, the default value <deploy\_root>/uplink is used.
uplink\_cache\_time: 168           # Time for caching remote package metadata, in hours. The default value is **168**. The value range is (0, 8760\].

##### log section #####
logs\_path: ./logs                # Log path. If this parameter is not set, the default value <deploy\_root>/logs is used.

##### log level section #####
# Log level: The log levels are all, trace, debug, info, warn, error, fatal, mark, and off in ascending order.
# For run, operate, and access log files, if the log level is not configured or is incorrectly configured, the default log level info is used.
loglevel\_run: info
loglevel\_operate: info
loglevel\_access: info

##### auth plugin section #####
# (Optional) Configuration of the custom authentication plugin
#auth\_plugin:
#  name: CustomAuth              # Name of the authentication plugin
#  path: plugins/CustomAuth.js   # Absolute path of the plugin or path relative to the ohpm-repo software package. You are advised to place the plugin in the plugins directory of the software package.

##### fieldCheck plugin section #####
# (Optional) Custom metadata rule check plugin configuration.
#field\_check\_plugin:
#  config\_file\_path:  plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json  # Absolute path of the field check configuration file or path relative to the ohpm-repo software package. You are advised to save the file to the plugins/fieldCheckPlugin directory of the software package.
#  check\_func\_dir: plugins/fieldCheckPlugin                                          # Absolute path of the directory where the field check function file is located or path relative to the ohpm-repo software package. You are advised to set the directory to the plugins/fieldCheckPlugin folder.

\##### content check plugin #####
\# (Optional) Configuration of the package content rule check plugin
#content\_check\_plugin:
 # (Required for the check) The environment variables must contain the ark\_disasm executable file and tar command line tool.
 # Check scope: uploaded bytecode HAR and HSP
\#  name: 'OHMUrlCheck'

##### Level of check logs for compatibility fields such as compatibleSdkVersion #####
# The options are close, info, warn, and error. The default value is warn.
compability\_log\_level: warn

##### Allowing removal of packages dependent by other components #####
# The options are true and false. The default value is false.
allow\_remove\_depended\_packages: false

#### Configuration Options

## listen

The value is in three-segment format, that is, **<proto>://<host>:<port>**, where **<proto>** is optional. The default value of **<proto>** is **http**. Example:

-   (By default) Listen to the loopback address of the local host:
    
    listen: localhost:8088
    # Or listen: http://localhost:8088
    
-   (Recommended) Listen to a specific address:
    
    listen: https://<_IP address of the host where ohpm-repo is deployed_\>:8088
    
-   Listen on all addresses. (If you choose to listen on all addresses, **server** in the [store](#en-us_topic_0000001745376470_store) configuration option must be configured.)
    
    listen: 0.0.0.0:8088
    # Or listen: http://0.0.0.0:8088
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cen0butBQh2feD-Nv1MJ6w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89893375ADB49831998E6F35706DD7FA73F80F998C18CDF27E43682C1B4C82C5)

You are advised to set **listen** to a specific address. **proto** supports HTTP and HTTPS protocols. The default protocol is HTTP. To ensure the security of the ohpm-repo link, you are advised to use HTTPS. If you choose to use HTTPS, you must complete the [https](#en-us_topic_0000001745376470_https) configuration.

## https

If you configure [listen](#en-us_topic_0000001745376470_listen) to use HTTPS, you must configure **https\_key** and **https\_cert**.

-   **https\_key**: private key file of the SSL certificate
-   **https\_cert**: SSL certificate file

Configurations for reference:

https\_key: ./ssl/server.key
https\_cert: ./ssl/server.crt

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/WZQN19Z9S0OYlVHhDN2WqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E701E5BE80FDC1D0BE7E625886BB0ADA0224981C117F9D5D35CA2370EC7D8AB)

In the production environment, you must use certificates issued by a trusted CA to avoid browser security warnings caused by self-signed certificates.

## deploy\_root

Deployment directory of ohpm-repo, which stores file data generated during running

-   If the **<deploy\_root>** field is empty, the default path is as follows:
    
    Windows: **~/AppData/Roaming/Huawei/ohpm-repo**
    
    Others: **~/ohpm-repo**
    
-   If the **<_deploy\_root_\>** field is not empty, the path must be an **absolute path** and the folder to which the path points **must exist**.
    
-   The path cannot be set to the root directory where the ohpm-repo installation package is decompressed.

Configurations for reference:

deploy\_root: ''

## Server

Service-related configurations:

-   **max\_package\_size**: maximum size of a package to be uploaded, in MB. If this parameter is not set or set to **0**, the default value **500** is used. The value range is (0, 500\].
-   **max\_extract\_size**: maximum size of a package after decompression, in MB. If this parameter is not set or set to **0**, the default value 800 is used.
-   **max\_extract\_file\_num**: maximum number of files after decompression. If this parameter is not set or set to **0**, the default value **30000** is used.
-   **user\_rate\_limit**: user access frequency control, in times/s. If this parameter is not set or set to **0**, the default value **100** is used. The value range is (0, 10000\].
-   **fetch\_timeout**: request/response timeout interval, in seconds, for requesting uplink data when [uplink](#en-us_topic_0000001745376470_uplink) is used. If this parameter is not set or set to **0**, the default value **60** is used. The value range is (0, 3600\].
-   **keep\_alive\_timeout**: timeout interval for maintaining a TCP connection, in seconds. If this parameter is not set or set to **0**, the default value **60** is used. The value range is (0, 3600\].
-   **api\_timeout**: API request/response timeout interval, in seconds. If this parameter is not set or set to **0**, the default value **60** is used. The value range is (0, 3600\].
-   **upload\_api\_timeout**: request/response timeout interval for the third-party package upload API, in seconds. If this parameter is not set or set to **0**, the default value **60** is used. The value range is (0, 3600\].
-   **upload\_lock\_hour**: period within which a new third-party package with the same name cannot be uploaded, after all versions of a third-party package are removed, in hours. If this parameter is not set or set to **0**, the default value **24** is used. The value range is (0, 168\].
-   **upload\_max\_times**: maximum upload times of a single user within 24 hours. If this parameter is not set or set to **0**, the default value **100** is used. The value range is (0, 100000\].
-   **operation\_log\_retention**: duration for storing operation logs in the database, in days. If this parameter is not set or set to **0**, the default value **100** is used.

Configurations for reference:

max\_package\_size: 500
max\_extract\_size: 800
max\_extract\_file\_num: 30000
user\_rate\_limit: 100
fetch\_timeout: 60
keep\_alive\_timeout: 60
api\_timeout: 60
upload\_api\_timeout: 300
upload\_lock\_hour: 24
upload\_max\_times: 100
operation\_log\_retention: 100   

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/rlEkBwSsT6KXOTXIfwbemQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=389057987539F412DCEBCA52E953B8A58D29F8A4A82224F0F70AC513B890977E)

**db** is the configuration option of metadata storage, and **store** is the configuration option of file storage. **db** supports FileDB local storage and MySQL database storage. **store** supports file storage, SFTP storage, and custom storage. **db** and **store** cannot be used together randomly and must comply with the mapping in Table 1.

**Table 1** Mapping of db and store configurations
| 
db: Metadata Storage

 | 

**Corresponding store Type: Third-party File Storage**

 |
| :-- | :-- |
| 

FileDB

 | 

File storage

 |
| 

MySQL (supported since ohpm-repo 1.1.0)

 | 

File storage, SFTP storage (supported since ohpm-repo 1.1.0), custom storage (supported since ohpm-repo 2.2.0)

 |

## db

Stores data such as user information and running status generated during the running of ohpm-repo. FileDB local disk storage and MySQL database storage are supported.

**Local disk storage**

By default, local disks are used for storage. The configuration is as follows:

-   **type**: storage plugin name, which is **filedb**.
-   **config**: plugin configuration. The options are as follows:
    -   **path**: address for storing database files. The default value is **./db**. The path can be either relative or absolute. If a relative path is used, it is resolved based on [deploy\_root](#en-us_topic_0000001745376470_关于-deploy_root).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/AiWcSQhVQNCJ4P5V0hhZDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=768A2A20AD7AB4CF24BBA5D7C2B40107D961C1415F8AD414790A5E996832D7C0)

If you want to change the storage path of database files and retain the old data, migrate the data files from the old path to the new path.

Configurations for reference:

db:                
  type: filedb     
  config:
    path: ./db     

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BKYROq9YROG8Htp0jEs_-w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC7BFCF55DC8A54FFE8C8A76E9EDFD516A253E075B1B71A6E74BEA29E2815D0C)

To prevent potential security risks, you are advised to use a database account with non-highest permissions for connection.

## store

Stores resource files such as third-party libraries and metadata. Local disk storage, SFTP storage, and custom plugin storage are supported.

**Local disk storage**

By default, local disks are used to store files. The configuration is as follows:

-   **type**: plugin name, which is **fs**.
-   **config**: plugin configuration. The options are as follows:
    -   **path**: storage root directory path. The default value is **./storage**. The path can be either relative or absolute. If a relative path is used, it is resolved based on [deploy\_root](#en-us_topic_0000001745376470_关于-deploy_root).
    -   **server**: address for downloading the repository content. If **host** in **[listen](#en-us_topic_0000001745376470_listen)** is **0.0.0.0** and the local host has multiple network interfaces, this option is mandatory.
        -   The format of **server** is as follows: <_**proto** in [listen](#en-us_topic_0000001745376470_listen)_\>://<_host_\>:<_**port** in [listen](#en-us_topic_0000001745376470_listen)_\>.
        -   If the value of **host** in **[listen](#en-us_topic_0000001745376470_listen)** is not **0.0.0.0**, **server** uses the full value of **listen** by default. For example, if the value of **listen** is **127.0.0.1:8088**, the default value of **server** is **http://127.0.0.1:8088**.
        -   If **host** in **[listen](#en-us_topic_0000001745376470_listen)** is set to **0.0.0.0**, the default value of **host** in **server** is determined as follows: If the local host has only one network interface, the default value is the IPv4 address of the network interface. If the local host has multiple network interfaces, the default value is the IPv4 address of the first detected network interface. In this case, you are advised to manually change the value of **host** to the correct local IP address or domain name. For example, if **listen** is **0.0.0.0:8088**, set **server** to **http://<_local IP address_/_domain name_\>:8088**.
        -   If the ohpm-repo service needs to be accessed through the reverse proxy, this field must be set to the domain name of the reverse proxy server, and **[use\_reverse\_proxy](#section1074004784011)** must be set to **true**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/WwRaGioJTdCxUXr_UfWq2w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96D375A46F79C72DF95D6F7AF9895C5E2D0AC30326E22642119EFAD6FB45B6E8)

If you want to change the storage path after uploading resources, you need to migrate the data in the old path to the new path.

Configurations for reference:

store:
  type: fs
  config:
    path: ./storage
    #server: http://localhost:8088

**SFTP storage**

SFTP can be used to store files only when MySQL is used to store data. The specific configuration is as follows:

-   **type**: plugin name, which is **sftp**.
-   **config**: plugin configuration.
    -   **location**: A maximum of three SFTP services can be configured. The value must be a YAML array. The detailed configuration is as follows:
        -   **name**: SFTP service name, which must be unique.
        -   **host**: address of the SFTP service host.
        -   **port**: SFTP service port.
        -   **read\_username**: name of the user with read permission.
        -   **read\_password**: password of the user with read permission. (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
        -   **write\_username**: name of the user with write permission.
        -   **write\_password**: password of the user with write permission. (Set this parameter to plaintext, which will be converted into ciphertext in the deployment directory.)
        -   **path**: file path relative to the SFTP root directory. The path must start with a slash (/) and the folder to which the path points must exist.
    -   **server**: address for downloading the repository content. If **host** in **[listen](#en-us_topic_0000001745376470_listen)** is **0.0.0.0** and the local host has multiple network interfaces, this option is mandatory.
        -   The format of **server** is as follows: <_**proto** in [listen](#en-us_topic_0000001745376470_listen)_\>://<_host_\>:<_**port** in [listen](#en-us_topic_0000001745376470_listen)_\>.
        -   If the value of **host** in **[listen](#en-us_topic_0000001745376470_listen)** is not **0.0.0.0**, **server** uses the full value of **listen** by default. For example, if the value of **listen** is **127.0.0.1:8088**, the default value of **server** is **http://127.0.0.1:8088**.
        -   If **host** in **[listen](#en-us_topic_0000001745376470_listen)** is set to **0.0.0.0**, the default value of **host** in **server** is determined as follows: If the local host has only one network interface, the default value is the IPv4 address of the network interface. If the local host has multiple network interfaces, the default value is the IPv4 address of the first detected network interface. In this case, you are advised to manually change the value of **host** to the correct local IP address or domain name. For example, if **listen** is **0.0.0.0:8088**, set **server** to **http://<_local IP address_/_domain name_\>:8088**.
        -   If the ohpm-repo service needs to be accessed through the reverse proxy, this field must be set to the domain name of the reverse proxy server, and **[use\_reverse\_proxy](#section1074004784011)** must be set to **true**.

Configurations for reference:

store:                               
  type: sftp                         
  config:
    location:
      - 
        name: test\_one\_sftp          
        host: "localhost"           
        port: 22                     
        read\_username: "read"   
        read\_password: "password" 
        write\_username: "write"   
        write\_password: "password" 
        path: /source22
      -
        name: test\_two\_sftp
        host: "localhost"
        port: 24
        read\_username: "read"
        read\_password: "password"
        write\_username: "write"
        write\_password: "password"
        path: /source24
    #server: http://localhost:8088

**Custom storage**

Custom plugins are used for storage. The specific configuration is as follows:

-   **type**: plugin name, which is **custom**. **custom** is a custom storage plugin type. For details about the custom storage plugin development process, see [Storage Plugin Customization](../appendix/storage-plug-in-customization/document.md).
-   **config**: plugin configuration. The options are as follows:
    -   **export\_name**: class name of the export plugin to be written.
    -   **plugin\_path**: an absolute path of the plugin or a path relative to the ohpm-repo software package. You are advised to place the plugin in the **plugins** directory of the software package.
    -   **custom\_field**: user-defined field. You can obtain the value of the user-defined field by using the getStorageConfigInfo method of **libs/common/getStorageConfigInfo.js** in the decompressed package of ohpm-repo.
    -   **server**: address for downloading packages from the local repository.
        -   If the value of **host** in **[listen](#en-us_topic_0000001745376470_listen)** is not **0.0.0.0**, **server** uses the full value of **listen** by default. For example, if the value of **listen** is **127.0.0.1:8088**, the default value of **server** is **http://127.0.0.1:8088**.
        -   If **host** in [listen](#en-us_topic_0000001745376470_listen) is set to **0.0.0.0**, the default value of **host** in **server** is **localhost**, for example, **http://localhost:8088**. You are advised to manually change the value of **host** to the IP address/domain name of the local host. For example, if the value of **listen** is **0.0.0.0:8088**, set **server** to **http://<_Local IP address/domain name_\>:8088**.
        -   If the ohpm-repo service needs to be accessed through the reverse proxy, this field must be set to the domain name of the reverse proxy server. When ohpm-repo is deployed in multi-instance mode, a reverse proxy server must be configured, and [use\_reverse\_proxy](#section1074004784011) must be set to **true**.

Configurations for reference:

store:
  type: custom                                            
  config:
    export\_name: "MyStorage"                              
    plugin\_path: "plugins/storagePlugin/MyStorage.js"        
    custom\_field: "test"                                  
    #server: http://localhost:8088

## use\_reverse\_proxy

-   **use\_reverse\_proxy**: whether to use the reverse proxy. The options are **true** and **false**. The default value is **false**. If a reverse proxy is used, **use\_reverse\_proxy** must be set to **true**, and the client IP address will be obtained from the x-forwarded-for field in the request header.

use\_reverse\_proxy: false

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/32PSMhXOQnCDO5IyP8-pUw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58F2E6C94B825C17E139E71E03890A9FE01E94706F55A406599489F3E88A7D2C)

When **use\_reverse\_proxy** is set to **true**, be sure to update the **x-forwarded-for** value in your reverse proxy configuration. This update is only necessary at the outermost proxy if there is a chain of proxies involved. Skipping the update could incur the risk of **x-forwarded-for** data manipulation. Here's how you can update **x-forwarded-for** in your reverse proxy configuration:

proxy\_set\_header x-forwarded-for $remote\_addr

## uplink

-   **uplink\_cache\_path**: path for caching the remote package. The default value is **./uplink**. The path can be either relative or absolute. If a relative path is used, it is resolved based on [deploy\_root](#en-us_topic_0000001745376470_关于-deploy_root).
-   **uplink\_cache\_time**: time for caching remote package **metadata**, in hours. The default value is **168**. The value range is (0, 8760\].

Configurations for reference:

uplink\_cache\_path: ./uplink
uplink\_cache\_time: 168

## logs

-   **logs\_path**: location for storing logs. The default value is **./logs**. The path can be either relative or absolute. If a relative path is used, it is resolved based on [deploy\_root](#en-us_topic_0000001745376470_关于-deploy_root).

Configurations for reference:

logs\_path: ./logs 

## loglevel

Custom log level. The configuration is as follows:

-   **loglevel\_run**: storage level of run log files. The default level is **info**. Only logs whose levels are higher than the specified level are stored in run log files.
-   **loglevel\_operate**: storage level of operate log files. The default level is **info**. Only logs whose levels are higher than the specified level are stored in operate log files.
-   **loglevel\_access**: storage level of access log files. The default level is **info**. Only logs whose levels are higher than the specified level are stored in access log files.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/zuHYo4shSLKnLQE7WpYztQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43F81D7638B133FB85503F7F66B6AA661265B1EBB11C1B8DDEBCA251ADB71BC4)

-   The log levels are all, trace, debug, info, warn, error, fatal, mark, and off in ascending order.
-   For run, operate, and access log files, if the log level is not configured or is incorrectly configured, the default log level **info** is used.

Configurations for reference:

loglevel\_run: info
loglevel\_operate: info
loglevel\_access: info

## auth\_plugin

ohpm-repo 2.3.0 and later versions support custom authentication plugins (the ohpm CLI 1.8.0 or later is required), allowing you to develop custom authentication plugins to connect to your own user information system. For details about the process of developing a custom authentication plugin, see the [instructions for developing a custom authentication plugin](../appendix/authentication-plug-in-customization/document.md).

Parameter description:

-   **name**: plugin name, which is the implementation class name defined in the **CustomAuth.js** plugin file. If the implementation class is CustomAuth, set this parameter to **CustomAuth**.
-   **path**: storage path of the compiled **CustomAuth.js** plugin file. The value can be an absolute path or a relative path. The base of the relative path is the root directory where the ohpm-repo tool package is decompressed.

Example configuration (disabled by default):

#auth\_plugin:
#  name: CustomAuth              
#  path: plugins/CustomAuth.js   

## field\_check\_plugin

Since version 5.1.3, ohpm-repo supports custom metadata validation rules, allowing you to create customized validation rules for specific fields in **oh-package.json5**. For details about how to develop the custom metadata rule check plugin, see [Custom Metadata Rule Check Plugin Configuration](../appendix/custom-metadata-validation-rule-plugin/configuration/document.md).

Parameter description:

-   **config\_file\_path**: path of the field check configuration file. The value can be an absolute path or a relative path. The baseline of the relative path is the root directory where ohpm-repo is decompressed. You are advised to save the file to the **plugins/fieldCheckPlugin** directory of the software package. The default value is **plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json**.
-   **check\_func\_dir**: directory where the field validation function file is stored. The value can be an absolute path or a relative path. The base path of the relative path is the root directory where ohpm-repo is decompressed. You are advised to set the directory to the **plugins/fieldCheckPlugin** folder. The default value is **plugins/fieldCheckPlugin**.

Example configuration (disabled by default):

#field\_check\_plugin:
#  config\_file\_path:  plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json   
#  check\_func\_dir: plugins/fieldCheckPlugin                                           

## content\_check\_plugin

Since version 5.2.0, ohpm-repo supports consistency checks for the OHMUrl version in third-party library bytecode files. This feature verifies that the OHMUrl version number in the **module.abc** file within the bytecode HAR package matches the actual version number in the HAR package's metadata. It will block the upload of packages with inconsistent versions to prevent potential runtime crashes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/WlOduQ6KS-edOtschgKXmA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062136Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE99C01DB605BA7D3CBD989E0F0C3294BC1D49C62156EBA6CC8B740EDE531D15)

The consistency check relies on the ark\_disasm tool and the system's built-in tar extraction utility. The ark\_disasm tool, which is used to disassemble the **module.abc** file, is included in the command-line tools package. Please download the [command-line tools](https://developer.huawei.com/consumer/en/download/command-line-tools-for-hmos) and add the path to the ark\_disasm tool (default path: **command-line-tools/sdk/default/openharmony/toolchains**) as well as the path to the tar utility to your system environment variables. (For Linux and macOS, ensure the path to the bsdtar utility is added to your system environment variables.) If you encounter any errors related to ark\_disasm during the third-party library upload process, please contact the administrator to ensure your DevEco Studio version is compatible with the ark\_disasm tool.

Parameter description:

-   **name**: fixed to **OHMUrlCheck**.

Example configuration (disabled by default):

#content\_check\_plugin:
#  name: 'OHMUrlCheck'     

## compability\_log\_level

-   **compability\_log\_level**: level of check logs for compatibility fields such as **compatibleSdkVersion**. The options are **close**, **info**, **warn**, and **error**. The default value is **warn**. The reference configuration is as follows:

compability\_log\_level: warn

## allow\_remove\_depended\_packages

-   **allow\_remove\_depended\_packages**: indicates whether to allow removal of packages dependent by other components. The options are **true** and **false**. The default value is **false**. The reference configuration is as follows:

allow\_remove\_depended\_packages: false

#### About deploy\_root

**_deploy\_root_** is the deployment directory of ohpm-repo, which can be configured through the **<[deploy\_root](#en-us_topic_0000001745376470_deploy_root)\>** field in the configuration file.
