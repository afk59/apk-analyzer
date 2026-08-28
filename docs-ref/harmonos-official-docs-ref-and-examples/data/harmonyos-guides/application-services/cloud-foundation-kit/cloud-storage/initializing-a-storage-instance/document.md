# Initializing a Storage Instance

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Prerequisites

You have [enabled Cloud Storage](../../getting-started/enabling-cloud-storage/document.md).

#### Procedure

Call [cloudStorage.bucket](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudstorage#section1286815320203) to initialize a storage instance. Instances can be initialized in either of the following ways:

-   Initializing the default instance
    
    import { cloudStorage } from '@kit.CloudFoundationKit';
    
    let bucket: cloudStorage.StorageBucket = cloudStorage.bucket(); // Start an asynchronous task to query the default cloud-side instance.
    
    If you choose to initialize the default Cloud Storage instance, an asynchronous task will be started to query the default cloud-side instance. Therefore, when multiple cloud storage operations are involved, you are advised to perform initialization only for the first operation and reuse the initialized cloud storage instance for all subsequent operations, rather than reinitializing it each time.
    
    // Initialize the Cloud Storage instance only once.
    let bucket: cloudStorage.StorageBucket = cloudStorage.bucket(); 
    bucket.list(...); 
    bucket.uploadFile(...);
    
    Not recommended:
    
    // Initialize the Cloud Storage instance multiple times.
    cloudStorage.bucket().list(...);
    cloudStorage.bucket().uploadFile(...);
    
-   Initializing a specified instance
    
    import { cloudStorage } from '@kit.CloudFoundationKit';
    
    let bucket: cloudStorage.StorageBucket = cloudStorage.bucket('bucket001-ki6tc'); // Specify the **bucket001-ki6tc** instance.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/0xjrk4LPQoeD0XbOh1zlDg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE5116F9EC83D6450349C8B8E38663CCB7A780FEF4E38E3F1E57D82DCA3D5B92)
    
    If you choose to initialize a specified Cloud Storage instance, ensure that the instance exists on the cloud; otherwise, subsequent operations will result in an error indicating that the instance cannot be found. Create a storage instance on the cloud. For details, please refer to [Managing Storage Instances](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-storage-manage-bucket-0000001281294006).
