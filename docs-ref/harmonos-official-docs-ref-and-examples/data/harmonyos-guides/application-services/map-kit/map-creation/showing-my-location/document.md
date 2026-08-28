# Showing My Location

#### Use Cases

Starting from version 6.0.1(21), the function of changing the stacking order of the **my-location** layer relative to overlays is supported.

This section describes how to enable the **my-location** function. This function shows a user's current location when the user opens the map. The following figure shows the effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/in3L9QfPTW-iXudEzLNhIA/en-us_image_0000002545846359.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BCB5D566AB7A272AA6FFABA5BA6DA7DBB1DB4399D0D76164153ACFF25D65758 "Click to enlarge")

#### API Description

The **my-location** function is mainly implemented by methods of [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller). For details about the APIs and their usage, please refer to [setMyLocationEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section201759451313).

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[setMyLocationEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section201759451313)(myLocationEnabled: boolean): void

 | 

Sets whether to enable the **my-location** layer function. By default, the continuous location capability of the system is used to display user locations. After the function is enabled, the my-location icon is displayed in the lower right corner of the map by default. When a user taps the **my-location** icon, the user's current location will be displayed in the center of the screen as a blue dot.

 |
| 

[setMyLocationControlsEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section3464719101814)(enabled: boolean): void

 | 

Sets whether to enable the **my-location** icon. If the **my-location** layer function is disabled, the system does not respond when the icon is tapped.

 |
| 

[setMyLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1165002535516)(location: [geoLocationManager.Location](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#location)): void

 | 

Sets the coordinates of **my-location**.

If you do not use the default location function provided by Map Kit, you can obtain the user's location through [Location Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/location-api) and send it to Map Kit.

 |
| 

[setMyLocationStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section126791641317)(style: [mapCommon.MyLocationStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section3713124215275)): Promise<void>

 | 

Sets the style of **my-location**.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section9264124723916)(type: 'myLocationButtonClick', callback: Callback<void>): void

 | 

Listens for **my-location** icon tap events.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section19268134715398)(type: 'myLocationButtonClick', callback?: Callback<void>): void

 | 

Cancels listening for **my-location** tap events.

 |

#### Development Procedure

## Enabling the **my-location** Icon

1.  Before enabling the **my-location** icon, ensure that your app can obtain user location information.
    
    Apply for the **ohos.permission.LOCATION** and **ohos.permission.APPROXIMATELY\_LOCATION** permissions. You need to declare the required permissions in the _module.json5_ configuration file. For details, please refer to [Declaring Permissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    
    {
      "module" : {
        // ...
        "requestPermissions":\[
          {
            // Allow an app running in the foreground to obtain the location information.
            "name" : "ohos.permission.LOCATION",
            // The reason needs to be created in **/resources/base/element/string.json**.
            "reason": "$string:location\_permission",
            "usedScene": {
              "abilities": \[
                "EntryAbility"
              \],
              "when":"inuse"
            }
          },
          {
            // Allow an app to obtain the approximate device location.
            "name" : "ohos.permission.APPROXIMATELY\_LOCATION",
            // The reason needs to be created in **/resources/base/element/string.json**.
            "reason": "$string:approximately\_location\_permission",
            "usedScene": {
              "abilities": \[
                "EntryAbility"
              \],
              "when":"inuse"
            }
          }
        \]
      }
    }
    
2.  Initialize the map and obtain an object of the map operation class [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller). Call the [setMyLocationEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section201759451313) method of the **mapController** object to enable the **my-location** function.
    
    It is advised to enable the **my-location** function after user authorization is obtained.
    
    import { abilityAccessCtrl, bundleManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
    import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    
    @Entry
    @Component
    struct LocationDemo {
      private mapOptions?: mapCommon.MapOptions;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapController?: map.MapComponentController;
      private mapEventManager?: map.MapEventManager;
    
      aboutToAppear(): void {
        // Map initialization parameters used to set the coordinates of the map center point and zoom level.
        this.mapOptions = {
          position: {
            target: {
              latitude: 39.9,
              longitude: 116.4
            },
            zoom: 10
          }
        };
    
        // Map initialization callback.
        this.callback = async (err, mapController) => {
          if (!err) {
            // Obtain **mapController** to operate the map.
            this.mapController = mapController;
            this.mapEventManager = this.mapController.getEventManager();
            let permission = await this.checkPermissions()
            if (!permission) {
              this.requestPermissions()
            // Enable the **my-location** icon.
              this.mapController?.setMyLocationControlsEnabled(true);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
    
      // Call the checkAccessToken() method to check whether the location permission has been granted to the app. . 
      async checkPermissions(): Promise<boolean> {
        const permissions: Array<Permissions> = \['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY\_LOCATION'\];
        for (let permission of permissions) {
          let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
          if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION\_GRANTED) {
            // Enable the **my-location** layer. **mapController** is an object of the map operation class.
            this.mapController?.setMyLocationEnabled(true);
            // Enable the **my-location** icon.
            this.mapController?.setMyLocationControlsEnabled(true);
            return true;
          }
        }
        return false;
      }
    
      // If the location permission is not granted, dynamically apply for authorization from the user.
      requestPermissions(): void {
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
          \['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY\_LOCATION'\])
          .then((data: PermissionRequestResult) => {
            // Enable the **my-location** layer.
            this.mapController?.setMyLocationEnabled(true);
          })
          .catch((err: BusinessError) => {
            console.error(\`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}\`);
          })
      }
    
      async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
        let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
        let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION\_DENIED;
    
        // Obtains **accessTokenID** of the app.
        let tokenId: number = 0;
        let bundleInfo: bundleManager.BundleInfo =
          await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION);
        console.info('Succeeded in getting Bundle.');
        let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
        tokenId = appInfo.accessTokenId;
    
        // Check whether the app has been granted the permission.
        grantStatus = await atManager.checkAccessToken(tokenId, permission);
        console.info('Succeeded in checking access token.');
        return grantStatus;
      }
    
      build() {
        Stack() {
          // Call the **MapComponent** component to initialize the map.
          MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%');
        }.height('100%')
      }
    }
    
3.  Check whether the **my-location** function is successfully enabled.
    
    The **my-location** icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Rbzj0VBRTnuvrkhU1KRZfg/en-us_image_0000002517280081.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4782EA59C0E6D3A6D8BD70F3C865F94A0E818B7E5A4BF8750F2773D39F5C5761) is displayed in the lower right corner of the map by default. Tap the **my-location** icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/nOyjrY-eSTq8YitsRyDTyQ/en-us_image_0000002517280079.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7067E174602065AB2E0440B1E603DF257232770C4653952DEF7A681D245AE35E), and then the current location is displayed in the center of the screen as a blue dot, as shown in the following figure. The effect varies depending on the obtained user location.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4epHyHsuRAe3bxVhzQNx-Q/en-us_image_0000002514366502.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=531034C0346EC6500BD69DB8C4E61A4FAF5E801331AB8EA67CCC8EBB3200D373 "Click to enlarge")
    
4.  Obtain the coordinates of the user's location and set the user's location.
    
    By default, Map Kit uses the continuous location capability of the system. If you want to customize the display frequency or accuracy, call the [geoLocationManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager) API to obtain the user location coordinates (which is in the WGS84 coordinate system). User authorization is a must if your app needs to access the device location information. For details, please refer to [geoLocationManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager).
    
    The following example only shows the one-time location result. After the user's coordinates are obtained, call [setMyLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1165002535516) of the **mapController** object to set the user location. The [setMyLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1165002535516) API uses the WGS84 coordinate system.
    
    // Introduce the @kit.LocationKit module. 
    import { geoLocationManager } from '@kit.LocationKit';
    // ...
    
    // Obtain the coordinates of user locations.
    let location = await geoLocationManager.getCurrentLocation();
    
    // Set user locations. 
    this.mapController.setMyLocation(location);
    

## Listening for my-location Icon Tap Events

Call the [on('myLocationButtonClick')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section9264124723916) method to set the **myLocationButtonClick** event listener. After the listening function is enabled, the tap event of the **my-location** icon needs to be set. If no tap event is set, Map Kit executes the default after-tap event, that is, the map moves to the current user location.

let callback = () => {
  console.info("myLocationButtonClick", \`myLocationButtonClick\`);
};
this.mapEventManager.on("myLocationButtonClick", callback);

## Disabling the **my-location** Icon

Determine whether to display the **my-location** icon.

this.mapController.setMyLocationControlsEnabled(false);

## Customizing the Location Icon Style

Call the mapController.[setMyLocationStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section126791641317) method to set the user location icon style. The following figure shows the effect.

let style: mapCommon.MyLocationStyle = {
  anchorU: 0.5,
  anchorV: 0.5,
  radiusFillColor: 0xffff0000,
  // Set **icon** to a custom icon resource when required. 
  // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file within the **rawfile** folder.
  icon: 'test.png'
};
await this.mapController.setMyLocationStyle(style);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/3ptbkdrQSJ-ysfWwC_mkww/en-us_image_0000002545846401.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70CDED1CCF2B1D14889F5152D16787D3C305ED76E5226BCBCAF687C388082784 "Click to enlarge")

## Changing the Stacking Order of the my-location Layer Relative to Overlays

Call the mapController.[changeMyLocationLayerOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section16251915293) method to change the stacking order of the **my-location** layer relative to overlays. The following figure shows the effect.

// **true**: The **my-location** layer is below overlays.
this.mapController?.changeMyLocationLayerOrder(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/mUaD7AP1Rxm7rJkMefIAKw/en-us_image_0000002545966395.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3E5F26931B8942910931FE3495BC097525F841253913AACC19D0C6A4FBCEDBF "Click to enlarge")
