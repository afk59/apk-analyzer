# Frontend page

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/yxO0Vo6mSKCfuWN_EbqLcA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F64D2DE383D0F1D0BC7B15DF31130729FA83B31BB7D5B29398AB9835911885A0)

An anti-replay attack mechanism is added for interfaces since ohpm-repo 5.0.2. Ensure that time is synchronized between the server where ohpm-repo is deployed and the client that accesses the ohpm-repo management page. If an error message indicating that the request is invalid is displayed, rectify the fault by referring to [FAQs](../../faqs/document.md#section15971414154116).

After ohpm-repo is started, you can access the ohpm-repo page using a browser. The access path is **http://_<Deployment server IP address>_:_<Listening port>_** or **https://_<Deployment server IP address>_:_<Listening port>_**. **http** or **https** indicates the network protocol of ohpm-repo, **_<Deployment server IP address>_** is the IP address of the server where ohpm-repo is deployed, and **_<Listening port>_** is the listening port. All these can be configured in the [listen](../../setting-the-configuration-file/document.md#en-us_topic_0000001745376470_listen) option of the ohpm-repo configuration file.

For example, deploy ohpm-repo on the server whose IP address is **192.168.10.10**. If you do not know the IP address of the ohpm-repo server, run the **ifconfig** command on Linux or macOS, or run the **ipconfig** command on Windows to view the IP address. In addition, set **listen** in the ohpm-repo configuration file to **0.0.0.0:8088**. The URL for accessing the ohpm-repo page is **http://192.168.10.10:8088**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ATiQTSJbSv6_v0ccGV-D8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB9E08D93E0B36CAC35C27CDF596A420EF41B04ACA8C646D28B8F88D8364B582)

The default administrator account is automatically created for ohpm-repo. The account name is **admin** and the password is **12345Qq!**. To ensure the ohpm-repo account security, you are forced to change the password upon the first login. Set a new password and log in again.

#### Home Page

The home page displays the package information stored in ohpm-repo and provides the search function, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/DyxSqdrCTQ2TMzM_fmkOEw/en-us_image_0000002501068656.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEB8057FDFBB99719BC48731B9CA60B48BAE8A0CB0A29A0D4DA51C28D7CC91F4 "Click to enlarge")

-   Area 1: search area. The search function supports two-level filtering. You can select the target repository from the drop-down menu, then perform a fuzzy search for package names within the selected repository.
-   Area 2: login and registration area. Users can log in to and register with the system. After login, users can access the background management page through this area.
-   Area 3: package list area, which displays all packages that meet the search criteria. Click the summary of a package in the list to go to the package details page and view more information about the package. If ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/8rLSmNP0TFGqJWnms03RbA/en-us_image_0000002532668715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=232BE460D850AE2BDEA6FDB32B1C0FD733B82B8F76DCB9CBD4DD04E0A9F0CDC4 "Click to enlarge") is displayed before the package name, you do not have the permission to access the package.

#### Package Details Page

The package details page displays the detailed information about the current package. The information mainly comes from the internal files of the package and records the package version information and number of downloads. The following figure shows the page effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/b_8JkA1GRe-JfsNIWY6MpQ/en-us_image_0000002532668709.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062137Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8793E092E7B0C10B8137FD89738D419E46A7A2183A156728A4EF4BF554F7144E "Click to enlarge")

-   Area 1: area for displaying basic package information, which is obtained from the **oh-package.json5** file of the package.
-   Area 2: tab page area. You can select different tabs to display more information about the package.
    -   **Describe**: displays the content of the **README.md** file of the package. The file records the introduction to the package by the developer.
    -   **Dependency**: records package dependency information.
    -   **Dependent**: records the information about dependent packages.
    -   **Versions**: records all current version information and tag information of the package in ohpm-repo. You can click the version list to view the package information of the corresponding version and the upload time of different version packages and their number of downloads in the last week.
    -   **ChangesLog**: displays the content of the **CHANGELOG.md** file of the package. The file records the update logs of the package.
-   Area 3: tab details area, which displays details about the selected tab.
-   Area 4: area for displaying additional information about the package, including the contributor (obtained from the **author** field in the **oh-package.json5** file), uploader (user who uploads the package to the ohpm-repo), and downloads statistics (displayed only on the details page of the latest package version). The downloads statistics cover the weekly downloads data of all versions in the last year. You can click different positions in the weekly downloads data curve to obtain the weekly downloads data in a specified period.
