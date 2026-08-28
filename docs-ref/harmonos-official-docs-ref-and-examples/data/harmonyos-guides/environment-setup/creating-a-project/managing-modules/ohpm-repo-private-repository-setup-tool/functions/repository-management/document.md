# Repository Management

The repository management service manages repository information, including permissions of all packages in the repository, package publishing/unpublishing, and uplinks.

#### Managing Repositories

Since version 5.3.0, ohpm-repo supports multi-repository configuration and allows permission editing for each repository.

Repository permissions are divided into read and write permissions. When attempting to download, publish, unpublish a package, or edit package tags, a user must have both the corresponding repository-level permission and the [specific package-level permission](../package-permission-management/document.md). Neither alone is sufficient.

| 
Repository Permission Type

 | 

Prerequisites

 | 

Available Operation

 | 

Typical Scenario

 |
| :-- | :-- | :-- | :-- |
| 

Read

 | 

1\. The target resource is publicly readable.

2\. The target resource is authorized readable and the user has been added to the authorized read whitelist.

 | 

-   Downloading packages

 | 

Developers obtain dependencies.

 |
| 

Write

 | 

1\. The target resource is publicly writable.

2\. The target resource is authorized writable and the user has been added to the authorized write whitelist.

 | 

-   Downloading packages
-   Publishing packages
-   Unpublishing packages
-   Editing package tags

 | 

Maintainers update the repository content.

 |

The **Repository manage** page displays the information about all owned repositories. You can perform the following operations:

1.  Managing third-party packages in ohpm-repo
2.  Editing repository information
3.  Deleting a repository
4.  Adding a repository

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/qm-l5IkeQ4qYNJwAC1ru-Q/en-us_image_0000002532748779.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83124791EF7C59078C6358358191ED0ADE398B7642891FD28FC0BA4D479DA3C8 "Click to enlarge")

## Managing Third-party Packages

The **Manage ohpm warehouse's third-party packages** page consists of two main sections: **Permission management** and **On and off shelf**.

## **Managing Permissions**

Since version 5.3.0, ohpm-repo supports package-level access permission configuration. System administrators can manage permissions for all packages in a repository, including configuring package visibility, whitelists, and managing owners. Packages can be searched by name using fuzzy matching.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/bLUIaLrrQpCHNqHuD_nYhA/en-us_image_0000002532668821.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C76FB5C59AA20F86FC63A99D692FF258CCCF5E2A16F7301C548A749C2B20E5CC "Click to enlarge")

-   Area 1: package visibility configuration area. The default value of **Permission Type** is **Publicly Readable**. When **Permission Type** is set to **Authorization Readable**, you can configure the whitelist in area 2. **Publicly Readable**: All users can download and view the package. **Authorization Readable**: Only users added to the read whitelist can download the package.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/vJKo-mxTSEqDk1Q3ovcmyA/en-us_image_0000002500908914.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7BBF549FBCB5E849315C4439B7EDC10CAA574821261971F7EBD9CB81F28D141 "Click to enlarge")
    

-   Area 2: whitelist configuration area. Users in the whitelist have the permission to download and view packages. Package owners and maintainers are automatically added to the whitelist and cannot be removed. You can click the **Add user** or **Delete** buttons to add a user to or remove a user from the whitelist.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/E6Ax97TBSgG866RdPEyffw/en-us_image_0000002500908910.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3079B5644FA6CB20B5B07829254850DF4FB732C7C7A4807EC5F573CC07C0F0E0 "Click to enlarge")
    

-   Area 3: owner management area. Package owners have permissions to download, publish, unpublish packages, and edit package tags. Owners can be added or deleted. A package must always have at least one owner; the last remaining owner cannot be deleted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/1LGoF1eHS9WbDsme5ET4GQ/en-us_image_0000002532668817.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC1ADA9A6CF39108BE77C0469D4B68BDEDFD0157CE99884C6E1A7AB5637124E6 "Click to enlarge")
    

## **Publishing and Unpublishing Packages**

Click the **Manage ohpm warehouse's third-party packages** button to enter the repository details panel, which displays all packages uploaded to ohpm-repo. This section includes four functions: uploading packages, unpublishing a package, batch unpublishing packages, and searching for packages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7CG8R3o-Syu3gHAD_UXJ9g/en-us_image_0000002532748789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F53DC0E6B75E2BE797A73D6D65E1E75240E5CA1733FDD16F7CD4A2DAAD29BC97 "Click to enlarge")

-   Area 1: package upload area. Click **Upload Package** to upload a specified package file or select a local third-party package file to upload it to the repository. The following figure shows the page effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/GzQBjhF8T1uRy2bPeKJFnA/en-us_image_0000002501068756.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80164CFA897EA9A05507FEA50F6CB110175E6F57B16D1772E121934C0226ECAB "Click to enlarge")
    
-   Area 2: package unpublishing area. Click **UnPublish** on the right of a specified package and enter the reason for unpublishing to unpublish the package. The following figure shows the page effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/8lWBuyT7T6GgY_nLdoFfAw/en-us_image_0000002501068758.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AC023F6E7FC211163115EE35AC819870EDA484D60332CC2139C16A838C0D3C2 "Click to enlarge")
    
-   Area 3: batch unpublishing area. Select the check boxes on the left of the packages and click **Batch unPublish** to unpublish the selected packages in batches. You can change the number of data items shown on each page at the bottom of the page to unpublish more packages in batches at a time.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/uk5LPNvwQ-elLlKVKJiZVg/en-us_image_0000002532748783.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B69DE741311F4AFD20F3D7D45ABC3E93AEF71F6B8489793B0718E7DAE4CA85BA "Click to enlarge")
    
-   Area 4: data filtering area. Click the funnel icon next to the list title to filter package data, by name, version, publisher, author, publish time, and more. For example, to filter for packages whose name contains 3, whose version number is 2.0.0 or later, and whose publisher is accessToken1, the data filtering result is as follows:
    
    \- **Name**: Search for packages by package name. Fuzzy search is supported.
    
    \- **Version**: Search for packages by version number range. You can enter the minimum version number and maximum version number.
    
    \- **Publisher**: Search for packages by publisher name. Fuzzy search is supported.
    
    \- **Author**: Search for packages by package author. Fuzzy search is supported.
    
    \- **PublishTime**: Search for packages by publish time range is supported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/dBFy_KOETsS0Yq4Eg29qOQ/en-us_image_0000002501068764.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=250956BA113D94E5F53A2E630D706B6D2DBA9F8FD83644E4B088DC0364514744 "Click to enlarge")
    

## Editing Repository Information

Click the edit icon of a specified repository to enter its information editing page, where you can modify the name, uplink, read policy, authorized read whitelist, write policy, authorized write whitelist, publishing policy, and description of the repository.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/ViLcnlFZRdOXCXEJi78fOw/en-us_image_0000002500908920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FA0500F1E765F65504F4B8C3A8747E86384E0DF466852C07A4971493FA8C35E "Click to enlarge")

-   **Name**: name of the repository, which cannot be modified if the repository has published packages, or if an authorized read or write whitelist has been configured.
-   **Uplink**: proxy repository address. You can select an option from the drop-down list. The options available are the uplink repositories configured in the [uplinks](#en-us_topic_0000001792256181_uplinks) panel of the repository management page.
-   **Read Policy**: The options are **Publicly Readable** and **Authorization Readable**. When **Read Policy** is set to **Publicly Readable**, all users have the read permission on the repository, allowing them to access package information and download packages within the repository. When **Read Policy** is set to **Authorization Readable**, only users in the authorized read whitelist have the read permission on the repository. In this case, **Authorization Readable Whitelist** becomes available and must be configured, and **Write Policy** is automatically set to **Authorization Writable** and cannot be modified. The system administrators have read and write permissions to the repository by default.
-   **Authorization Readable Whitelist**: must be configured when **Read Policy** is set to **Authorization Readable**. You can add users to the whitelist. A maximum of 200 users can be added. You can search for user names and add them one by one, or add user names in batches by separating them with commas (,).
-   **Write Policy**: The options are **Publicly Writable** and **Authorization Writable**. When **Write Policy** is set to **Publicly Writable**, all users have the write permission on the repository, allowing them to download, publish, unpublish packages, and edit package tags within the repository. When **Write Policy** is set to **Authorization Writable**, the **Authorization Writable Whitelist** configuration item is displayed. Only users in the whitelist have the write permission on the repository. Users with the write permission have the read permission by default. The system administrators have the read and write permissions on the repository by default.
-   **Authorization Writable Whitelist**: must be configured when **Write Policy** is set to **Authorization Writable**. You can add users to the whitelist. A maximum of 200 users can be added. You can search for user names and add them one by one, or add user names in batches by separating them with commas (,).
-   **Deploy Policy**: The options are **Disable Redeploy** and **Allow Redeploy**. In the **Disable Redeploy** mode, if you try to publish the same package version to the repository repeatedly, the system displays an error message indicating that the third-party library already has this version. This ensures the uniqueness of the version. In the **Allow Redeploy** mode, you can publish the same package version repeatedly. The new package will overwrite the old one. This mode is applicable to scenarios where continuous updates are required. You can select a proper publishing policy as required. **The overwriting operation is irreversible. Exercise caution when performing this operation.**

## Deleting a Repository

You can click the delete icon to delete the selected repository. Deletion is prohibited if the repository contains published packages, or if it is the last remaining repository.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/CJyXth0LQj-mnybxvnN-bg/en-us_image_0000002500908918.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD12222F28A646AE98BA241562611E4D2AA9423861C7DB24E161464FF81DB951 "Click to enlarge")

## Creating a Repository

You can click the **+** icon to create a repository. During creation, you can edit the name, uplink, read policy, write policy, publish policy, and description of the repository. **Read Policy** defaults to **Publicly Readable**, **Write Policy** defaults to **Publicly Writable**, and **Deploy Policy** defaults to **Disable Redeploy**. A maximum of 20 repositories can be created. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/bOIItBRSRTazgVECWRN4Hw/en-us_image_0000002500908916.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=466BD852FA267ACE60C10114A2CEAFD0A0870A634DBEDE8E4137AE3DA824F086 "Click to enlarge")

#### Using Uplinks

The uplink function allows the current repository to obtain all packages of the configured uplink repository. If a third-party package that does not exist in the current repository is downloaded from a repository configured with an uplink repository, the package will be downloaded via the uplink repository instead. If a proxy is required for accessing the uplink repository, configure the required proxy information. The **uplinks** page is shown in the figure below:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/WhSvGNihT72WjIdnNgJ0Kg/en-us_image_0000002501068754.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85538FFAA6B150600AC5D0AFF3B5798A649928FB2B2CF5B3C27757F57BFCA1B9 "Click to enlarge")

1.  Click **Add** to create an uplink repository. After adding an uplink repository, you must go to **Repository manage** > **Warehouse** > **Edit** to apply the configuration so that this function takes effect. Only one uplink repository can be configured for ohpm-repo at a time. You are not advised to set the uplink repository address to the address of another ohpm-repo. Otherwise, repository A may be configured with uplink repository B, and repository B may be configured with uplink repository A, causing cyclic search. The following figure shows the page effect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/1fqI-87kR9ScIF-jFAMaCw/en-us_image_0000002532668815.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D9380844BA0775D934D6933333DB8DB13C219D4BB604A6EB21729581A969F2F "Click to enlarge")
    
2.  Click **Edit** to modify the configured uplink repository information, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/v4c49wXKTYibw5BqcfCeqA/en-us_image_0000002532748787.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89B0EDE9E498D06815300D658B0ABB2A2D2E55CBB7450CEE97094A371FE9893F "Click to enlarge")
    
3.  Click **Delete** to delete the configured uplink repository, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ii5E1vRKT8KmfEBpOxWniw/en-us_image_0000002501068762.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3258E54416E0448F639846D2352A6EDA51AA33A418098F84F670518F3F9B5E66 "Click to enlarge")
    
4.  ohpm-repo may need to access the configured uplink repository through a proxy. Therefore, ohpm-repo provides the proxy function. Click **Config proxy** to add proxy information, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/9789eI2PRVy0PUZneDws_w/en-us_image_0000002532668819.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBEFF89417DDB3138D0F9D134F9EFB825744D7010345C4D46C2E70DEF84919ED "Click to enlarge")
