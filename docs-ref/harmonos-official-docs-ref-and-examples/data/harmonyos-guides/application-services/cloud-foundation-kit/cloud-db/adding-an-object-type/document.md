# Adding an Object Type

You need to create an object type in AppGallery Connect.

#### Prerequisites

You have [enabled Cloud DB](../../getting-started/enabling-cloud-db/document.md).

#### Procedure

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project for which you want to create an object type.
3.  Go to **Serverless** > **Cloud DB**.
4.  Click **Add** on the **Object Type** tab page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/up1zTsKZSxym-Iqg8d2YGw/en-us_image_0000002474214397.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FB1F78BAA5EE2ED999BD325D49E462870E79F2A244E28A11C635BDD2C14491D)
    
5.  Set **Object Type Name** to **BookInfo**, and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/PWJQ_CZrSlaCiItQ_H3Ykg/en-us_image_0000002440774556.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7C0E15006A39AAA1E3665ACC9521F0C3470417CFB3FF9235F6B30FFC338B4DA)
    
6.  Click **+Add Field** to add the following fields, and click **Next**.
    
    | 
    Field
    
     | 
    
    Type
    
     | 
    
    Primary Key
    
     | 
    
    Not Null
    
     | 
    
    Encrypt
    
     | 
    
    Default Value
    
     |
    | :-- | :-- | :-- | :-- | :-- | :-- |
    | 
    
    id
    
     | 
    
    Integer
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    bookName
    
     | 
    
    String
    
     | 
    
    –
    
     | 
    
    ✓
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    author
    
     | 
    
    String
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    price
    
     | 
    
    Double
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    borrowerId
    
     | 
    
    Integer
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    borrowerName
    
     | 
    
    String
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     |
    | 
    
    borrowerTime
    
     | 
    
    Date
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     | 
    
    –
    
     |
    
7.  Click the plus sign (+) to add an index named **bookName**, and click **Next**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bFuzXikOTDu_3uNxe1IgHg/en-us_image_0000002440774548.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4711EA8FA5F42BE6FAF54EEDE20E2D6612CF4D39EEE2A145AA8A8F6CF35092E2)
    
8.  Set role permissions as follows and click **OK**.
    
    | 
    Role
    
     | 
    
    query
    
     | 
    
    upsert
    
     | 
    
    delete
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- | :-- | :-- |
    | 
    
    Everyone
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    All users, including authenticated and non-authenticated users.
    
    This role has the query permission by default and can be granted the upsert and delete permissions. For example, if the **upsert** permission is selected for this role, this role can write data to the object type.
    
    However, you are not advised to grant the upsert and delete permissions to the **Everyone** role.
    
    If **Encrypt** is selected for fields of the object type, the full-process encryption function is enabled. In this case, the **Everyone** role does not have the query, upsert, and delete permissions, and the role's permissions cannot be modified.
    
     |
    | 
    
    Authenticated user
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    Users who have passed the AppGallery Connect sign-in authentication.
    
    This role has the query permission by default and can be granted the upsert and delete permissions. For example, if the **upsert** permission is selected for this role, this role can write data to the object type.
    
    If **Encrypt** is selected for fields of the object type, the full-process encryption function is enabled. In this case, the **Authenticated user** role does not have the query, upsert, and delete permissions, and the role's permissions cannot be modified.
    
     |
    | 
    
    Data creator
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    Authenticated users who create data.
    
    This role has all permissions by default and can customize the permissions. For example, if the **upsert** permission is selected for this role, this role can write data to the object type.
    
    Each data record has a corresponding creator (namely an app user). Data creators can upsert or delete the data created only by themselves.
    
    The information about data creators is stored in the system table of data records.
    
     |
    | 
    
    Administrator
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    ✓
    
     | 
    
    App developers who access Cloud DB through AppGallery Connect or Function as a Service (FaaS).
    
    This role has all permissions by default and can customize the permissions. For example, if the **upsert** permission is selected for this role, this role can write data to the object type.
    
    An administrator can manage and configure the permissions of other roles.
    
     |
    
9.  The created object types are displayed in the object type list.
10.  Select the created object type **BookInfo** and click **Export**. If no object type is selected, all object types will be exported by default.
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/HVKNSj1tQjuvrnAKzn39cA/en-us_image_0000002474214393.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A97B67C16AB4E7266181058D0ED5E83E752AB15BB7E1060175A75407DA26DD3)
     
11.  Set the file format to **JSON** and click **OK**. This file will be used when you [import an object type file](../importing-an-object-type-file/document.md).
     
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Lub-xGK1S1aAsQ234sYXpg/en-us_image_0000002474214405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD38ADD6E79F704A3EE733190F5E662EB8BC25CBC2D035AAAE95656D988E6E7C)
