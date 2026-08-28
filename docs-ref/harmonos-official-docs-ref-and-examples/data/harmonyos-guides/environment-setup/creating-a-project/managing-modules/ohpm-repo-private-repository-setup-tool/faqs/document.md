# FAQs

#### Obtaining and Upgrading ohpm-repo

-   Obtain the latest ohpm-repo tool package from the [Download Center](https://developer.huawei.com/consumer/en/download/ohpm-repo).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/WgSfduwJS3S_7M3B3DrE2w/en-us_image_0000002501068710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBFBA590842A8D8D0C6CF20A5511D0D19B270E809695710B2C7C69EE4431FFD2 "Click to enlarge")
    
-   Upgrading ohpm-repo: Before the upgrade, back up data. For details, see [Version Upgrade](../appendix/version-upgrade/document.md).

#### Modifying the Configuration File After ohpm-repo Is Started and Making the Modification Take Effect

-   **Version 1.0.1**: Stop the current ohpm-repo service, modify the configuration file in the **conf** directory in the root directory of the decompressed ohpm-repo package, and run the **start** command again.
-   **Version 1.1.0**: Stop the current ohpm-repo service, modify the configuration file in the **conf** directory in the deployment root directory, and run the **start** command again.
-   **Version 2._X_._X_**: Stop the current ohpm-repo service and perform differentiated processing based on whether the configuration file is specified during the previous ohpm-repo startup.
    -   A configuration file is specified when you run the **install** command: Find the specified configuration file, modify the file content, run the **install** command again to specify the modified configuration file, and then run the **start** command to start ohpm-repo.
    -   No configuration file is specified when you run the **install** command: The configuration file in the **conf** directory in the decompressed package is used by default. In this case, modify the default configuration file, run the **install** command without specifying the configuration file, and then run the **start** command to start ohpm-repo.

#### ohpm-repo Deployment Directory and ohpm-repo Decompression Directory

-   **ohpm-repo decompression directory**: **<_binary\_root_\>**. It is the root directory where the ohpm-repo tool package is decompressed and stores the content of the decompressed ohpm-repo package.
    
-   **ohpm-repo deployment directory**: **<_deploy\_root_\>**. This directory stores data generated during ohpm-repo running, including configuration files, log files, and encryption components. The configuration method of the ohpm-repo deployment directory varies according to the version.
    
-   -   ohpm-repo 1.0.1: The ohpm-repo deployment directory cannot be customized. Only the default path can be used.
    -   ohpm-repo 1.1.0: When running the **ohpm-repo start** or **ohpm-repo deploy** command, you can set the **\--deploy\_root** parameter to specify the deployment directory of ohpm-repo. If this parameter is not configured, the default directory is used.
    -   ohpm-repo 2._X_._X_:
        -   Method 1: Set the **\--deploy\_root** parameter in the configuration file to specify the deployment directory of ohpm-repo and run the **ohpm-repo install** command for the setting to take effect.
        -   Method 2: Run the **ohpm-repo deploy** command to deploy multiple instances. You can set the **\--deploy\_root** parameter to specify the deployment directory of ohpm-repo. If this parameter is not configured, the default directory is used.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/_sCxsYv5Qka5pHcBtmmiCw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=878C6D3B34E764B473D2ED52A4507144986DE2E3F2C7289474F4B761F5FEA6AE)
    
    Default path of the ohpm-repo deployment directory:
    
    -   Windows: **~/AppData/Roaming/Huawei/ohpm-repo**
    -   Linux or macOS: **~/ohpm-repo**
    
    Do not place the ohpm-repo deployment directory and the ohpm-repo decompression directory in the **same directory**.
    

#### ohpm-repo Permission Management

## Account Permissions: System Administrator and Common User

1.  **Account registration**
    
    There are two types of accounts registered with ohpm-repo: user and administrator. When ohpm-repo is started for the first time, an administrator account is created by default. The account name is admin and the password is 12345Qq!.
    
    -   Click **Register** on the ohpm-repo management page to add a user.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/_VNQZmHSR9yVzTDWgUgzkA/en-us_image_0000002532668795.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41FE1D1D1C53C6411E33ABD2AA9AA65A4808D51C91C60B98A8B87B4D775F10E1 "Click to enlarge")
        
    -   Log in with any administrator account, and you can add users and manage existing users (such as deleting users, changing user types, and resetting passwords) on the ohpm-repo user management page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/5WQ4HERORYewMhRNTRw3PQ/en-us_image_0000002501068728.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=531D4D9EEAF4ADAFDF7EEED61E37F0707CB4DE8BC3C18A18E63D5D255DB4D6B6 "Click to enlarge")
        
2.  **Account permission description**
    -   System administrator: Multiple system administrators are allowed.
        -   User management: Create a user, edit the user type, and change the types and passwords of other users.
        -   Repository management: Edit repositories, manage third-party packages (packages can be directly published on the ohpm-repo management page), edit the uplink repository, and configure proxy information.
        -   System setting: Add the **oh-package.json5** check rules, reset system key, and add the anonymization configuration.
        -   Organization management: View information about all organizations, edit or delete managed organizations, and edit the administrators of all organizations.
        -   Operation log: All user operations can be recorded.
        -   Authentication management: Support public and private key authentication and access token authentication.
        -   Package permission management: Configure fine-grained permissions for individual third-party packages, including defining package owners, maintainers, and viewers.
    -   Common user: Multiple common users are allowed.
        -   Organization management: View the list of organizations to which the user belongs, and edit or delete the managed organization information.
        -   Authentication management: Support public and private key authentication and access token authentication.
        -   Package permission management: Configure fine-grained permissions for individual third-party packages, including defining package owners, maintainers, and viewers.

## Organization Permissions: Organization Members and Organization Administrators

1.  **Creating an organization and editing organization permissions**
    -   Adding and deleting an organization: Log in to the system as a system administrator. On the organization management page, click **Add** to create an organization. The current system administrator becomes the administrator of the organization by default. Click **Delete** to delete an organization.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/Thxeu6IcTDKvAy27UhDuaQ/en-us_image_0000002532748751.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D24404DA0C58D9AE57AC4802F292B534298CEFD6C41E3ED9EDBEC6EFA8F2866 "Click to enlarge")
        
    -   Adding and deleting an organization member: Log in to the organization administrator account. On the organization management page, click **Details** of the organization to which a user is to be added. On the member page, click **Add member** to add a member to the organization or click **Delete** to delete a member from the organization.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/JzWJWihqT2ya2Dn5reUi1Q/en-us_image_0000002500908878.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=885ECA587EE93E5660E763E90CC499CD7B076C83E24C6EFBACD7753562CF443F "Click to enlarge")
        
    -   Adding and deleting an organization administrator: Log in to the system as a system administrator. On the **Organize manage** page, click **Edit** for the organization to which you want to add a user. On the organization administrator editing page, click **Add group admin** to add an organization administrator or click **Delete** to delete an organization administrator.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/rls0wufdSiWWxd4Hg9D8Mw/en-us_image_0000002532668769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F4C491A14660D11BC0A54011E1EBF75B0E23EF9EAF489BC2F43B2FA73C2B94C "Click to enlarge")
        
2.  **Organization permission description**
    -   Organization user: Multiple organization users are allowed.
        -   Package upload: Third-party packages with the organization can be uploaded.
        -   Package removal: Third-party packages uploaded by members can be removed.
    -   Organization administrator: Multiple organization administrators are allowed.
        -   Package upload: Third-party packages with the organization can be uploaded.
        -   Package removal: Packages uploaded by all members of an organization can be removed.
        -   Organization editing: Edit the organization to which the administrator belongs, delete the organization, and change the permissions of the organization administrator.
        -   Organization member editing: Add or delete organization members.

## Managing Permissions for Uploading and Uninstalling Packages

Third-party packages can be classified into packages that belong to an organization and packages that do not belong to any organization. You can use ohpm-repo and the ohpm CLI tool to upload and remove packages.

-   Uploading and removing packages using repository management on the ohpm-repo management page: Only the system administrator has this permission. For organization package management, system administrators can publish and unpublish all packages within their organization. For non-organization package management, system administrators can publish and unpublish all non-organization packages (note: only a single user can upload all versions of non-organization packages).
-   Uploading and removing packages using the ohpm CLI tool: When configuring the .ohpmrc file, the authentication information identifies a unique user regardless of whether public/private key authentication or access token authentication is used. The user can upload and remove all packages from the organization to which the user belongs and upload and remove all packages that do not belong to any organization.

#### Metadata and Third-Party Package Data Management of ohpm-repo

## Introduction to Metadata and Third-Party Package Data

The ohpm-repo data consists of two parts:

-   Metadata: user data generated during the running of ohpm-repo and description of the uploaded package. You can configure storage by using the **db** option in the configuration file.
-   Third-party package data: After ohpm-repo is started up, the third-party packages are released to ohpm-repo through the ohpm-repo management page and ohpm CLI tool. You can configure storage for package file data of the third-party packages by using the **store** option in the configuration file.

## Storage Modes of Metadata and Third-Party Package Data

-   Metadata can be stored in local files (FileDB) and MySQL databases (MySQL).
-   Third-party package data can be stored in local files (file storage), SFTP servers (SFTP storage), and custom plug-ins (custom storage, including various cloud storages).
    
    The storage modes of metadata and third-party package data cannot be combined randomly. The following figure shows the matching rules and supported ohpm-repo versions.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/8E1yl1uCShWRyzeuBpQnaw/en-us_image_0000002500908886.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C41682252285D906EEDEDC656F9E18F30A3B46E3C63FB175A360A57D14727A0B "Click to enlarge")
    
    If the storage locations of metadata and package data need to be changed, you can follow the data migration guide to change the storage locations.
    

#### ohpm-repo Authentication Modes

When ohpm-repo runs commands that need to modify ohpm-repo database content, such as **publish**, **unpublish**, and **dist-tags**, read-write permission is required.

In ohpm-repo 5.0.5 and later versions, if anonymous access is disabled for ohpm-repo, ohpm must authenticate via either the standard AccessToken authentication or a customized AccessToken authentication method when executing the **install**, **info**, and **update** commands. To pass the authentication and obtain read permissions, you need to correctly configure the read-write or read-only AccessToken information.

## Authentication Modes

-   **Certificate authentication**: The encrypted SSH certificate is embedded for identity authentication. A password is required to obtain read-write permission.
-   **Access token authentication (for connecting to user data in the database)**: Access token is a new authentication mechanism introduced in ohpm-repo 2.1.0 (the ohpm CLI tool of 1.6.0 or later is required). You can generate a token on the ohpm-repo page and add it to the configuration file of the ohpm client. When interacting with ohpm-repo, the client automatically attaches a token for identity authentication, achieving password-free authentication. Configure the read-only AccessToken to obtain the read permission, or configure the read-write access token to obtain the read and write permissions.
-   **Customized access token authentication (for connecting to custom user data)**: Access token is a new authentication mechanism introduced in ohpm-repo 2.3.0 (which requires the ohpm CLI tool of 1.8.0 or later). If you do not want to store user data in the configured **db** storage path, you can [implement a custom authentication plugin](../appendix/authentication-plug-in-customization/document.md) to connect to the custom user data. The validity of the access token is authenticated by the customized user data. Configure the read-only AccessToken to obtain the read permission, or configure the read-write access token to obtain the read and write permissions.

## Authentication Failure FAQs

## publish/unpublish/dist-tags Command Fails to Be Executed Using Certificate Authentication

-   **Symptom**: The error message "ERROR: Publish failed, detail: The "key\_path" is empty - configure "key\_path" in the .ohpmrc file" is displayed.
-   **Cause analysis**: The certificate authentication parameters are not correctly configured.
-   **Solution**:
    -   Ensure that the public and private key files generated by the ssh-keygen tool are in pairs.
    -   Ensure that the public key information is configured on the ohpm-repo management page and parameters such as **publish\_id**, **publish\_registry**, and **key\_path** are configured in the .ohpmrc configuration file of ohpm.

## When Certificate Authentication Is Used and the ohpm publish XX.har Command Is Executed on the Git Bash Terminal to Publish Packages to ohpm-repo, the Error Message "The content of private key in the key\_path error" Is Displayed

-   **Symptom**: When the **ohpm publish** command is executed on the Git Bash terminal, the error message "The content of private key in the key\_path error" is displayed, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lDm21hshQaCx7CQHgsVv7A/en-us_image_0000002500908872.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C09CAFDF6D0EA1F8EB8DCF7557F71BEC9BD052C987CD9CE58413BBEAC4E805A1 "Click to enlarge")
    
-   **Cause analysis**: When the **ohpm publish** command is used to upload a package, if SSH certificate password authentication is used, the program must read the password entered by the user through the TTY stream. If the Git version is too early, the Git Bash carried in the Git will be lost. As a result, the TTY stream is lost.
-   **Solution**:
    -   Method 1: Download and install the latest version of Git from the Git official website, and use the Git Bash terminal carried in the latest version to perform operations.
    -   Method 2: Add the **git-bash.config** file to the **etc** directory in the current Git installation directory and add the **MSYS=enable\_pcon** configuration to the **git-bash.config** file. Open the Git Bash terminal again and run the **ohpm publish** command.

## publish/unpublish/dist-tags Command Fails to Be Executed Using Access Token Authentication

-   **Symptom**: The error message "ERROR: Publish failed, detail: The "key\_path" is empty - configure "key\_path" in the .ohpmrc file" is displayed.
-   **Cause analysis**: The access token is not correctly configured or the current tool version does not support this function.
-   **Solution**:
    -   Upgrade ohpm-repo and ohpm to ohpm-repo2.1.0 and ohpm 1.6.0 or later, respectively, as the access token function is supported by these versions.
    -   If access token is incorrectly configured in the .ohpmrc file, perform the following steps:
        -   Add //<ip>:<port>/repos/ohpm/:\_auth=<token> to the .ohpmrc configuration file of the OHPM client.
        -   _//<ip>:<port>/repos/ohpm/_ indicates the publish registry URL without the protocol name, and **<_token_\>** indicates the generated token.
        -   Use the ohpm client to run commands such as **publish**.

#### Publishing HSPs in an Application to ohpm-repo

1.  If you want to publish HSPs in an application to ohpm-repo, ensure that the software of the specified version is installed.
    -   **ohpm-cli**: version 1.3.0 or later
    -   **DevEco Studio**: version 4.1.0 or later
    -   **ohpm-repo**: version 1.1.0 or later
2.  The HSPs in an application cannot be directly published to ohpm-repo. You must convert them into .tgz files and upload them to ohpm-repo.
3.  You can obtain the .tgz files in either of the following ways:
    -   If DevEco Studio is used, click **Release** to obtain the .tgz package. For details, see [Developing a Dynamic Shared Package](../../developing-and-publishing-shared-packages/developing-a-dynamic-shared-package/document.md).
    -   If you have obtained the .hsp and .har files of a package, run the **tar** command in the directory where the two files are located to generate the .tgz file.
        
        // Pack the libhsp.har and libhsp.hsp files to generate the libhsp.tgz file.
        tar -czvf libhsp.tgz libhsp.har libhsp.hsp
        

#### An Error Is Reported When the ohpm-repo Command Is Executed

## When the ohpm-repo install or ohpm-repo start Command Is Executed, the Error Message "server install failed: YAMLException: bad indentation of a mapping entry" Is Displayed

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/dAvfHWD2Q_KeWV21uXWP5Q/en-us_image_0000002500908882.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6368517811F5924099CB780092D7C22161BFD09E148DBB9CC090055F49FC1A28 "Click to enlarge")

The indentation format configured in the **config.yaml** configuration file of ohpm-repo is incorrect, and the error location is displayed in the error information.

## After the ohpm-repo <command> Command Is Executed, an Error Message Is Displayed, Indicating that ohpm-repo Does Not Exist or <command> Does Not Exist

-   **ohpm-repo does not exist**: The path of the **bin** directory in the directory where the ohpm-repo tool package is decompressed is not configured in the system environment variable **path**. You must manually add the [system environment variable](#section24117279211), or go to the **bin** directory and add **./** before the command, that is, run **./ohpm-repo _<command>_** to make the command take effect.
-   **<command> does not exist**: Check whether the current ohpm-repo version is 2._X_._X_. Some commands, such as **install** and **remove\_instance**, exist only in versions later than 2.0.0.

## After ohpm-repo Is Started, No Information Is Displayed or the Page Cannot Be Opened When You Access the ohpm-repo Management Page Based on the listen Value in the Configuration File

-   **Possible cause 1**: The browser is incompatible with ohpm-repo. After ohpm-repo is started, the ohpm-repo management page is not displayed. The possible cause is that the browser used by the current user is incompatible with ohpm-repo. Download the browser of the latest version and enter the **listen** value again.
-   **Possible cause 2**: The ohpm-repo service is not started. Run the **ohpm-repo install** and **ohpm-repo start** commands to start the ohpm-repo service.
-   **Possible cause 3**: The address for accessing the ohpm-repo management page is incorrect. Enter the **listen** value configured in the ohpm-repo configuration file **config.yaml** in the address box of the browser.

## When the Domain Name and Port Number of Host A Are Used to Access the ohpm-repo Service Deployed on Host A from Host B, the Package Description Page Fails to Be Opened

-   **Symptom**: The following error information is displayed:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/EL6rzaDwTUSOY0C4810q-A/en-us_image_0000002532668785.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E3673EADE5F0CCFDD49D40191A58DBB2DDFC4A820C7A922043BA812689E9147 "Click to enlarge")
    
-   **Cause analysis**: The server is not configured on the host where ohpm-repo is deployed. The default server is used. The host is a local host and cannot be accessed on other hosts.
-   **Solution**: Modify the configuration file of host A where ohpm-repo is deployed and add the **store.config.server** configuration. You are advised to manually change the value of **host** to the IP address/domain name of the local host. For example, if the value of **listen** is **0.0.0.0:8088**, set **server** to **http://<_Local IP address/domain name_\>:8088**.

## When ohpm-repo install Is Executed, the Error Message "fail to initialize encryption component: Error: invalid crypto component." Is Displayed

-   **Symptom**: The following error information is displayed:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/u73zOGRVSJmdlcak1rmb9w/en-us_image_0000002500908866.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA8DC08987E06664513213FC1CA64E2CAF5C34749D6CB2C7FA38D4A8B544AF68 "Click to enlarge")
    
-   **Cause analysis**: In the root directory deploy\_root for ohpm-repo deployment, the **meta** file of the encryption component is damaged and invalid. In ohpm-repo, the uplink proxy address information and the public key information for certificate authentication are encrypted and stored using the meta encryption component.
-   **Solution**:
    -   If the problem is caused by version upgrade, obtain the **meta** file of the previous version and replace the **meta** file of the current version.
    -   If the **meta** file is damaged due to other reasons, perform the following steps:
        1.  Clear the content in the **publickey** and **uplinkproxy** tables in the database. (Back up the database before performing operations to prevent development from being affected by data deletion by mistake.)
        2.  Delete the damaged **meta** file.
        3.  Run the **ohpm-repo install** command again to generate a new **meta** file.
        4.  On the ohpm-repo management page, reconfigure the **uplink** proxy information.
        5.  On the ohpm-repo management page, reconfigure the public key data for certificate authentication.

#### An Error Is Reported When ohpm publish XX.har Is Executed to Publish Packages to ohpm-repo

## Error: connect ECONNREFUSED ::1:8089

-   **Symptom**: In the configuration file, the value of **store.config.server** is **http://Localhost:8089**, and the value of **host** is **localhost**. When ohpm executes the **publish** command, the following error message is displayed:
    
    ohpm ERROR request to http://Localhost:8089/repos/ohpm/Login failed, reason: connect ECONNREFUSED ::1:8089
    
-   **Cause**: According to the **listen** value **::1:8089** at the end of the error message, **localhost** is parsed as **::1** instead of **127.0.0.1**. Because the priority of IPv6 is higher than that of IPv4, **localhost** is parsed as **::1** (**127.0.0.1** corresponds to IPv6).
-   **Solution**:
    -   Method 1: Set the parsing priority of IPv4 to be higher than that of IPv6.
    -   Method 2: Change the value of **localhost** in **server** to **127.0.0.1**.

## Error: The content of private key in the key\_path error

-   **Symptom**: When ohpm executes the **publish** command, the following error message is displayed:
    
    The content of private key in the key\_path error.
    
-   **Solution**: The entered password is incorrect. Enter the correct password or reconfigure the key.

## Error: HttpCode 400 Group does not exist!

-   **Symptom**: When ohpm executes the **publish** command, the following error message is displayed:
    
    HttpCode 400 Group does not exist!
    
-   **Solution**: Some third-party packages contain the organization name. Only the user who releases a package can publish the package in the organization. The error information indicates that the third-party package has an organization name, but the organization has been not created. In ohpm, the package is named in the format of **@<_group_\>/<_package\_name_\>**, where **<_group_\>** indicates the organization name. Open the ohpm-repo management page and add an organization to publish the package.

## Error: HttpCode 400 You are not a developer of the group!

-   **Symptom**: When ohpm executes the **publish** command, the following error message is displayed:
    
    HttpCode 400 You are not a developer of the group!
    

-   **Solution**: Some third-party packages contain the organization name. Only the user who releases a package can publish the package in the organization. The error information indicates that an administrator account has added the organization of the package, but the current account is not a member of the organization. In ohpm, package names follow the format of **@_<group>_/_<package\_name>_**, where **_<group>_** indicates the organization name. Identify the owner account of the organization **_<group>_**. Use the owner account to log in to the ohpm-repo management page, access the organization details page, and add the account that will publish the packages as a member of the organization. Then the member can publish packages under the organization name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/vpYvuRMLQLG7ffPHlizmAA/en-us_image_0000002501068720.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3BE30646658ABAC9091B7BDF09490B2AE597CA881E3175B7848A946E75B4B8A "Click to enlarge")
    

## Error: ohpm ERROR: HttpCode 404 Not Found

-   **Symptom**: When ohpm executes the **publish** command, the following error message is displayed:
    
    ohpm ERROR: HttpCode 404 Not Found
    
-   **Solution**: **publish\_registry** in the ohpm configuration file is incorrectly configured: The port is not configured or the path is incomplete. The correct configuration is as follows:
    
    publish\_registry = http://localhost:8089/repos/ohpm
    

## Error: Same ohpm package is exists!

-   **Symptom**: When ohpm executes the **publish** command, the error message "Same ohpm package is exists!" is displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/qcSam3PMToav5m46N_vMFA/en-us_image_0000002501068732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24DC51732E34DDA2AF63E282061EF1BFF5170E93314596D748803546A475A690 "Click to enlarge")
    
-   **Cause analysis**: When a third-party library that does not belong to any organization needs to be upgraded, only the original user that published the package can upgrade the library.
-   **Solution**: Upgrade a package as the original user that published the package. If different users need to upgrade an uploaded package, the package name must contain the organization name.

## Error: Request Entity Too Large

-   **Symptom**: When ohpm executes the **publish** command, the error message "Request Entity Too Large" is displayed.
-   **Cause analysis**: When the Nginx is used as the reverse proxy server, the size of the sent package exceeds the value specified by **client\_max\_body\_size** in the Nginx configuration. By default, the value is set to **1** (in MB) in the Nginx.
-   **Solution**: Change the value of **client\_max\_body\_size** in the Nginx to a size that matches the package to be released.

## Error: The packageType is no equals the exists packageType!

-   **Symptom**: When ohpm executes the **publish** command, the error message "The packageType is no equals the exists packageType!" is displayed.
-   **Cause analysis**: The package to be uploaded is a HAR package, but an HSP file with the same name already exists in the repository. HAR and HSP packages must have unique names within the same repository.
-   **Solution**:
    -   Method 1: Change the name of the package to be uploaded to a name different from that of the uploaded .hsp package.
    -   Method 2: Remove all uploaded .hsp packages with the same name, and then upload HAR packages with the same name. (After the packages are removed, uploading third-party packages with the same name will be restricted and locked for a period of time to prevent abuse.) You can set the **upload\_lock\_hour** parameter in the **config.yaml** file to adjust the lock period.

#### An Error Is Reported When ohpm install XX.har Is Executed to Download Packages from ohpm-repo

## After an Uplink Is Configured for ohpm-repo, the install Command Fails to Download the Package from the Repository Configured for the Uplink

-   When an uplink is added, check whether the new uplink is selected in **Repository manage**. In the following figure, the new uplink is not selected and the **uplink** area is empty.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/qqjKuBLRTDyU_1RI7dv7zQ/en-us_image_0000002532748743.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CC47ADB391ED74B49AF1474762729C2B3497336F4A52744165D2966828DA6A7 "Click to enlarge")
    
-   If the required third-party package exists in the new uplink but cannot be downloaded, you may need to configure a proxy for the uplink. The configuration location is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/z3ssQwRVSoipTDCs2VXjEQ/en-us_image_0000002532748759.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CADA79C858E9224A48409E9EF14BE351A48BE4442859A7B339CC274B0476AD22 "Click to enlarge")
    

#### An Error Is Reported When the ohpm-repo Management Page Is Accessed

## When the ohpm-repo Management Page Is Accessed, an Error Message indicating that the Request Is Invalid Is Displayed

-   **Symptom**: When a user accesses the ohpm-repo management page, an error message is displayed, indicating that the request is invalid.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/qCXhecVaSuiBvu0VUn5CrQ/en-us_image_0000002532748739.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B27F43A81DC2149B7F09BF15EC08D4CFF7A9D049B976E853809B57B032FE4557 "Click to enlarge")
    

-   **Cause analysis**: In ohpm-repo 5.0.2, the anti-replay attack mechanism is added for interfaces. This mechanism verifies the timestamps in all data modification requests in ohpm-repo. If the difference between the timestamp carried in a request and the current time of the server exceeds 1 minute (earlier or later), the system rejects the request and returns an error indicating that the request is invalid.
-   **Solution**: To ensure the normal running of the system, ensure that the time of the server is the same as that of the client.

## Accessing the ohpm-repo Management Page Results in the "The encryption component is invalid" Error

-   **Symptom**: When a user opens the ohpm-repo management page and accesses the **uplink** proxy configuration page on the repository management page or accesses the certificate authentication configuration page on the authentication management page, an error message indicating that the encryption component is invalid is displayed, and the configured information is cleared.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pZBX0sz8Qg-9CzkNsEncfg/en-us_image_0000002532748731.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C01E4CFFC71213873D9E6EAA33E16F4F142A4F06AD5B15F86DDD27EBE6716F1 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/w1geyrpVShC1_Ul7NKpRmw/en-us_image_0000002532668781.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFB6D00E0C11F0DB0EC6A6A4AAD838BDB7C7607CEB3B8B8233405BE23CFA11A4 "Click to enlarge")
    
-   **Cause**: The address information of the **uplink** proxy and the public key information for certificate authentication must be encrypted. The encryption component is the **meta** file in the root directory **deploy\_root** for ohpm-repo deployment. If the **meta** file for encryption is different from that for decryption, data decryption fails.
-   **Solution**:
    -   If the problem is caused by version upgrade, obtain the **meta** file of the previous version and replace the **meta** file of the current version to ensure the consistency of the encryption component.
    -   If decryption using the **meta** file fails due to other reasons, perform the following steps:
        1.  Clear the content in the **publickey** and **uplinkproxy** tables in the database. (Back up the database before performing operations to prevent development from being affected by data deletion by mistake.)
        2.  Delete the **meta** file of the failed decryption.
        3.  Run the **ohpm-repo install** command again to generate a new **meta** file.
        4.  On the ohpm-repo management page, reconfigure the **uplink** proxy information.
        5.  On the ohpm-repo management page, reconfigure the public key data for certificate authentication.

## Accessing the ohpm-repo Management Page Results in the "System configuration error. Contact your administrator." Error

-   **Symptom**: When a user opens the ohpm-repo management page, an "Illegal request" error is displayed, and the ohpm-repo runtime log reports an error: "verify reverse proxy usage: set "use\_reverse\_proxy" to false in config.yaml if not used, or refresh "x-forwarded-for" in Nginx if it is."
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LR4D9pfOSCyccG7w2zKhkg/en-us_image_0000002532668775.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A597E33D1A7CBF89E1C1D8D4566A9A269FC892454A193D13875BE303034B57D0)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/mxdLZt1dSs2EsdUF7Piocw/en-us_image_0000002501068724.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F8DFB73483D73BED18341AC9915DD83A9B8FFB4E2406DA1D5ABAB261EDB927B "Click to enlarge")
    

-   **Cause analysis**: ohpm-repo 5.0.7 adds the [use\_reverse\_proxy](../setting-the-configuration-file/document.md#section1074004784011) configuration item to the configuration file to determine whether a reverse proxy is used. If **use\_reverse\_proxy** is set to **true** but a reverse proxy is not used, or if the **x-forwarded-for** value is not updated when the reverse proxy is configured, the **x-forwarded-for** value obtained from the request header is empty, leading to the error.
-   **Solution**: Ensure that **use\_reverse\_proxy** is set to **true** only if a reverse proxy is being used. In addition, be sure to update the **x-forwarded-for** value in your proxy configuration (this update is only necessary at the outermost proxy if there is a chain of proxies involved). The configuration command is **proxy\_set\_header x-forwarded-for $remote\_addr**.

#### Configuring Environment Variables for the ohpm-repo Tool

## Windows

1.  In the search box on the taskbar or **Start** menu, search for **environment variables** and select **Edit the system environment variables**.
2.  In the opened **System Properties** window, click the **Environment Variables...** button at the bottom right.

3.  In the **Environment Variables** window, locate and select the **Path** variable under the system variables section, then click **Edit...**.
4.  In the **Edit environment variable** window, click **New**, then enter the full path to the **bin** directory under the directory where the ohpm-repo tool package is decompressed.
5.  Click **OK** on all open windows to save the changes.
6.  Reopen the CLI and run the [ohpm-repo commands](../related-commands/document.md).

## Linux and macOS

1.  Open the CLI and run the following command to edit the **.bashrc** file:
    
    vim ~/.bashrc
    
2.  Press **i** to enter the insert mode (**\-- INSERT --** is displayed at the bottom).
3.  Navigate to the end of the file, create a new line, and add the following content:
    
    export PATH="$PATH:\[Specified path\]"  // Replace \[Specified path\] with the path of the bin directory under the directory where the ohpm-repo tool package is decompressed.
    
4.  Press **Esc** to exit the insert mode, enter **:wq**, and press **Enter** to save the modifications and exit.
5.  Run the following command to apply the configuration changes. The [ohpm-repo commands](../related-commands/document.md) are now ready for use.
    
    **source** ~/.bashrc
