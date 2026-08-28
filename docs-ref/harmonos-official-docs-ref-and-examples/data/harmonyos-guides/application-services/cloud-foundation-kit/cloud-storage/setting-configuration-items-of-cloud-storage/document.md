# Setting Configuration Items of Cloud Storage

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Procedure

1.  Add the network permission to the **entry/src/main/module.json5** file.
    
    "requestPermissions": \[
      {
        "name": "ohos.permission.INTERNET"
      }
    \]
    
2.  (Optional) If Cloud Storage operations (such as uploading or downloading files) require users to sign in to the app, you need to perform the following operations:
    1.  [Obtain user credentials via AuthProvider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section136610231214).
    2.  Pass the obtained credentials when calling the [cloudCommon.init()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section15555111210233) method for initialization.
3.  (Optional) Customize initialization parameters.
    
    To customize initialization parameters used by APIs of Cloud Storage, such as the network type or task mode, refer to the following configuration.
    
    -   To configure the network type used by APIs of Cloud Storage, use [StorageOptions.network](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section1772621115138). If no network type is configured, the default value **request.agent.Network.ANY** will be used.
        
        import { cloudCommon } from '@kit.CloudFoundationKit';
        import { request } from '@kit.BasicServicesKit';
        
        // Set Cloud Storage to use only the Wi-Fi network.
        cloudCommon.init({
          storageOptions: {
            network: request.agent.Network.WIFI
          }  
        })
        
    -   To configure the working mode of Cloud Storage upload and download tasks, use [StorageOptions.mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudcommon#section1772621115138). If no mode is configured, the default value **request.agent.Mode.BACKGROUND** will be used.
        
        import { cloudCommon } from '@kit.CloudFoundationKit';
        import { request } from '@kit.BasicServicesKit';
        
        // Set the Cloud Storage upload and download tasks to the foreground mode.
        cloudCommon.init({
          storageOptions: {
            mode: request.agent.Mode.FOREGROUND
          }
        })
