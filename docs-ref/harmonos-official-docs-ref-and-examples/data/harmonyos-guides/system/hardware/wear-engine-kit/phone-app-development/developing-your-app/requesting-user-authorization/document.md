# Requesting User Authorization

To protect user privacy, the Wear Engine APIs need user authorization to work. It is recommended that you perform the operations in this section when users call Wear Engine's open capabilities for the first time.

#### Applying for Wearable Device Permissions

Your app can only access data upon user authorization on the HUAWEI ID sign-in screen and authorization screen. Users can select the data range to be authorized and grant only some data permissions.

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/9MV25McCTneHLajq3uBX4g/en-us_image_0000002155046632.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6681BD0FCF395FB1279E161A98BFA7EB44063AAD1D21E3E62F6F77FF628D2F7 "Click to enlarge")  

1.  Call the [getAuthClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section17606835182712) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [AuthClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section876918413377) object.
2.  Define the authorization request class [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section12513135291215).
3.  Call the [requestAuthorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section172541457203810) method to request authorization from users. An authorization screen will display for users to grant the permissions. (The sign-in screen will display first if a user has not signed in to their HUAWEI ID.) You can use the APIs properly only after obtaining the user authorization. Otherwise, error code **201** will be reported.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/giStY20AQG6T8ObH7U9qgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BED4870A9823286245A8679A35081B8B1FA101BC17F355E1AA49AA3577A67800)
    
    -   Ensure that the permissions requested have been approved after [applying for integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md). Otherwise, error code **1008500004** will be reported.
    -   This API can be called for multiple times. If the requested permissions have been granted, the authorization screen will no longer display and the API will return the granted permissions.
    -   You can obtain the permissions requested by your app based on the [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section12513135291215) object in the input parameter. For details about the types of permissions required, please refer to [the permission description in Step 3](../../getting-started/applying-for-integrating-wear-engine/document.md#en-us_topic_0000001073008985_li5158124634712).
    -   The authorization result is returned through the [AuthorizationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1536013509131) object.
    
    // Before using Wear Engine, import the **wearEngine** and related modules.
    import { wearEngine } from '@kit.WearEngine';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Step 1: Obtain the **AuthClient** object.
    let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
    
    // Step 2: Define the permission request class based on the permissions that require user authorization.
    let request: wearEngine.AuthorizationRequest = {
      permissions: \[wearEngine.Permission.USER\_STATUS\]
    }
    
    // Step 3: Request user authorization.
    authClient.requestAuthorization(request).then(result => {
      console.info(\`Succeeded in requesting authorize, authorized permissions is ${result.permissions}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to request authorize. Code is ${error.code}, message is ${error.message}\`);
    })
    

#### Querying User Authorization Results

This API is used to query the app permissions granted by a user. If the required permissions are not granted, request authorization from the user by referring to [Applying for Wearable Device Permissions](#en-us_topic_0000001073917086_section7157142771512). You are advised to use this API to check whether the required permissions have been granted before requesting user authorization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/pNZdrqsGR-itJmQNekVloQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F836E0B65F34538277C7285FD5A5B00A4225892035A37501D34C5C70C16C655)

Ensure that the permissions have been approved after [applying for integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md). Otherwise, error code **1008500004** will be reported.

1.  Call the [getAuthClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section17606835182712) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [AuthClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section876918413377) object.
2.  Call the [getAuthorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section36125238476) method to query the granted permissions.
    
    // Before using Wear Engine, import the **wearEngine** and related modules.
    import { wearEngine } from '@kit.WearEngine';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Step 1: Obtain the **AuthClient** object.
    let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
    
    // Step 2: Call the API to query granted permissions.
    authClient.getAuthorization().then(result => {
      console.info(\`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}\`);
    })
