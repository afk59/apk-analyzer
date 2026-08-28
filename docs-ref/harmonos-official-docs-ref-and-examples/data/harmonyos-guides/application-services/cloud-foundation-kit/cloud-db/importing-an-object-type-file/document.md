# Importing an Object Type File

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

-   You have [added an object type](../adding-an-object-type/document.md).
-   You have [added a Cloud DB zone](../adding-a-cloud-db-zone/document.md).

#### Procedure

1.  Name the exported [JSON file](../adding-an-object-type/document.md#en-us_topic_0000001518866308_li0821548919) **schema.json** and copy it to the **AppScope/resources/rawfile** or **entry/src/main/resources/rawfile** directory of the DevEco Studio project. During compilation and build, resource files in the **AppScope** directory are merged into the module's resource files. For details, please refer to [Resource Categories](../../../../getting-started/resource-categories-and-access/document.md#resource-categories).
2.  Create the **BookInfo.ets** file in the code project based on the object type **BookInfo** created in AppGallery Connect. The sample code in the file is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/IRCW5Hf5R6upIz2atRbKVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=951466CF7A8F46731967DE764BF75DA32D74C1874B7AB3A7C82BCC659E14503F)
    
    The mapping between types of fields created in AppGallery Connect and ArkTS data types is as follows:
    
    -   String and Text: string
    -   Boolean: boolean
    -   Byte and ByteArray: Uint8Array
    -   Short, Integer, Long, Float, Double, IntAutoIncrement, and LongAutoIncrement: number
    -   Date: Date
    
    import { cloudDatabase } from '@kit.CloudFoundationKit';
    
    class BookInfo extends cloudDatabase.DatabaseObject{
      public naturalbase\_ClassName(): string {
        return "BookInfo";
      }
      public id: number | undefined;
      public bookName: string | undefined;
      public author: string | undefined;
      public price: number | undefined;
      public borrowerId: number | undefined;
      public borrowerName: string | undefined;
      public borrowerTime: Date | undefined;
    }
    
    export { BookInfo };
