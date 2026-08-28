# Initializing Database Access

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [imported an object type file](../importing-an-object-type-file/document.md).

#### Procedure

1.  Configure the cloud database.
    
    Add the network permission to the **entry/src/main/module.json5** file.
    
    "requestPermissions": \[
      {
        "name": "ohos.permission.INTERNET"
      }
    \]
    
2.  (Optional) If database operations (such as adding or deleting data) require users to sign in to the app, you need to perform the following operations:
    1.  [Obtain user credentials via AuthProvider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section136610231214).
    2.  Pass the obtained credentials when calling the [cloudCommon.init()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section15555111210233) method for initialization.
3.  In the service code, use the **QuickStartDemo** class of the Cloud DB zone created in AppGallery Connect to initialize **DatabaseZone**.
    
    import { cloudDatabase } from '@kit.CloudFoundationKit';
    
    let databaseZone = cloudDatabase.zone('QuickStartDemo');
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/VL2MEo91S8W88O2_Gh5f9Q/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AEA18750EB1306B5C2A4859097200B9DD3EC09DA2EF8D5399AC9C185032493D)
    
    -   The input parameter received by the **cloudDatabase.zone** method is **cloudDBZoneName**, which indicates the Cloud DB zone name. For details, please refer to [Adding a Cloud DB Zone](../adding-a-cloud-db-zone/document.md).
    -   You can create a maximum of four Cloud DB zones. If more than four Cloud DB zones are created, Cloud DB access will fail.
    
4.  To use database query methods, you can use classes (**BookInfo** as an example) to initialize **DatabaseQuery**.
    
    import { BookInfo } from 'xx/BookInfo'; // _xx_ is the relative path to the **BookInfo** file.
    
    let condition = new cloudDatabase.DatabaseQuery(BookInfo);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/vYbhS2tCRgK3P_l_X9fwiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8990220E0220E7E55087D7BF6CA4C6767F597B546BC31B8F2D47751AF3741465)
    
    You can create **databaseZone** and **condition** objects, which will be used in each query, by referring to this section. The following code will not describe the creation process again.
