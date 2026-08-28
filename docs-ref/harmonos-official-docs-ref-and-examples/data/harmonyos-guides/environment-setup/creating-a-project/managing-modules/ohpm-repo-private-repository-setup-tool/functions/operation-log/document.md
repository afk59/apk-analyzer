# Operation Log

The **Operation Log** page displays all operations performed on the ohpm-repo management page and logs recorded when commands including **publish**, **unpublish**, and **dist-tags** are executed using the ohpm CLI tool. The **Operation Log** page consists of two parts. The first part is the filtering criteria, and the second part is the data that meets the filtering criteria.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/WDn25lfxRriG-qnJoJjxtw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC559A146489E864B580EC54F8E0927859009A72F205AB35731A331C24B4BC05)

Operation logs are cleaned every other day. By default, operation logs generated within 100 days are retained. You can set the data retention period by setting the [operation\_log\_retention](../../setting-the-configuration-file/document.md#li38847353322) configuration item in the **config.yaml** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/v4Fp9q9CQ4G7hpWnCH0G-w/en-us_image_0000002500908770.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E071771E88244167912CB19537A0AF5338198864BF9EE1CF241A522BEC6FBA9A "Click to enlarge")

Data filtering: There are five types of data filtering for operation logs: user type, event type, operation type, operation time range, and user name of the operation object.

-   **User Type**: There are two types of users: **Admin User** and **Common User**. If you select **Common User**, only the operation logs of the common user are displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/sl_mkHxkThW5gat7APfHvg/en-us_image_0000002532668683.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C390FBF8EDF5A1A7F53A10E80C8223566B7E2AFDFFABA631276370AF602BEA1)
    
-   **Type Event**: There are six event types, including **User manage**, **Manage Repo**, **Package permissions**, **Cert Management**, **Organization Management**, and **System Setup**. You can select an event type to filter logs.
    
    -   For example, if **Type Event** is set to **Add user** in **User manage**, only the logs whose **Type Event** is **Add user** are displayed on the **Operation Log** page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Vh_LPnpsR7ajaJX0yO1N_A/en-us_image_0000002532668677.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DADE8985894DE44283371F921DD109C72A5A5F2B4F8120EAD73EDF8993CC5B66 "Click to enlarge")
        
    -   For details about **Type Event**, see the following table. When a level-1 event type is selected, all level-2 and level-3 event types are automatically included. When a level-2 event type is selected, all level-3 event types are automatically included.
        
        | 
        Level-1 Event Type
        
         | 
        
        Level-2 Event Type
        
         | 
        
        Level-3 Event Type
        
         |
        | :-- | :-- | :-- |
        | 
        
        User manage
        
         | 
        
        Add user
        
         | 
        
        \-
        
         |
        | 
        
        Delete User
        
         | 
        
        \-
        
         |
        | 
        
        Change User Role
        
         | 
        
        \-
        
         |
        | 
        
        Reset User Password
        
         | 
        
        \-
        
         |
        | 
        
        Manage Repo
        
         | 
        
        Repo
        
         | 
        
        Add Repo
        
         |
        | 
        
        Delete Repo
        
         |
        | 
        
        Update Repo
        
         |
        | 
        
        Publish
        
         |
        | 
        
        Unpublished
        
         |
        | 
        
        Batch Unpublished
        
         |
        | 
        
        Uplink
        
         | 
        
        Update Uplink Proxy
        
         |
        | 
        
        Add Uplink
        
         |
        | 
        
        Update Uplink
        
         |
        | 
        
        Delete Uplink
        
         |
        | 
        
        Tag
        
         | 
        
        Add Tag
        
         |
        | 
        
        Update Tag
        
         |
        | 
        
        Delete Tag
        
         |
        | 
        
        Permission management
        
         | 
        
        Edit Package Visibility
        
         |
        | 
        
        Add Package Whitelist User
        
         |
        | 
        
        Delete Whitelist User
        
         |
        | 
        
        Package permissions
        
         | 
        
        Add Package Owner
        
         | 
        
        \-
        
         |
        | 
        
        Delete Package Owner
        
         | 
        
        \-
        
         |
        | 
        
        Transfer Package Ownership
        
         | 
        
        \-
        
         |
        | 
        
        Add Package Maintainer
        
         | 
        
        \-
        
         |
        | 
        
        Delete Package Maintainer
        
         | 
        
        \-
        
         |
        | 
        
        Cert Management
        
         | 
        
        Certify
        
         | 
        
        Add Public Key
        
         |
        | 
        
        Delete Public Key
        
         |
        | 
        
        Access Token
        
         | 
        
        Create Access Token
        
         |
        | 
        
        Delete Access Token
        
         |
        | 
        
        Organization Management
        
         | 
        
        Organization
        
         | 
        
        Add Organization
        
         |
        | 
        
        Update Organization
        
         |
        | 
        
        Delete Organization
        
         |
        | 
        
        Organization Member
        
         | 
        
        Add Organization Member
        
         |
        | 
        
        Delete Organization Member
        
         |
        | 
        
        Organization Admin
        
         | 
        
        Add Organization Admin
        
         |
        | 
        
        Delete Organization Admin
        
         |
        | 
        
        System Setup
        
         | 
        
        Update oh-package.json5 Rule
        
         | 
        
        \-
        
         |
        | 
        
        Reset System Secret Key
        
         | 
        
        \-
        
         |
        | 
        
        update system security config
        
         | 
        
        \-
        
         |
        
    
    -   **Operation Result**: Select **Success** or **Failed** for filtering. If you select **Failed**, the following information is displayed on the **Operation Log** page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/5OhJDDT3RoG2Qdl8JBfHRQ/en-us_image_0000002532748631.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C2A941EFF2A707FD52D2101B7A7556E1113C523F8F41359FA719CC5577235B5 "Click to enlarge")
        
    -   Operation time range: Select an operation time range for filtering. If you select **2025-8-18** to **2025-8-25**, the following information is displayed on the **Operation Log** page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/HFpNs-zgSquhC3XzoJJRzg/en-us_image_0000002501068634.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27210AAF121ADA41554F3B6614B9193BB446831DC300B366C744FA682DBC1EF7 "Click to enlarge")
        
    -   **User Name**: Enter the user name of the operation object for filtering. For example, if you enter **user**, the following information is displayed on the **Operation Log** page.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/y8xYZ-JXTs6SMGvNuWqYFw/en-us_image_0000002500908776.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A190094A09935B033F3B6CDEBFFDE9FB643F2045F66A6D3CCA1C67AF38D24B4 "Click to enlarge")
