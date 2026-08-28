# Hop to Walking Navigation upon Vehicle Exit

Navigation data can be transferred from a specified map app on the head unit to a user's phone for walking navigation.

#### Use Cases

Hop to walking navigation upon vehicle exit: Before a user exits the vehicle, the navigation on the head unit's map app has not yet ended. After the user exits the vehicle, the navigation data on the head unit can be transferred to the phone to initiate walking navigation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/qJtqS4uUTOa1-WeGSt3D1A/en-us_image_0000002513576769.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57294762CCD61BD403FED3C4FF4D231D856C9501F4178D0930BFD05C5476CC92 "Click to enlarge")

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[registerSystemNavigationListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-navigationinfomgr#section66695411419)

 | 

Registers a listener for system navigation information and commands.

 |
| 

[unregisterSystemNavigationListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-navigationinfomgr#section1567066181615)

 | 

Unregisters a listener for system navigation information and commands.

 |

#### Development Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/Z-vmi4rNQUqm-4Y1vIH0mQ/en-us_image_0000002513586269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02E4A73391AAA77B622CA1986392F2FEFB154F953B70D6EC8CADD0A5E6CABD4B "Click to enlarge")

#### Development Procedure

1.  Configure the capabilities.
    
    For details, please refer to [Configuring Capabilities](../../getting-started/document.md#section239110365269). In the scenario of hop to walking navigation upon vehicle exit, set **name** in the metadata to **carHopCapability** and **value** to **getOffCarNavi**. The sample code is as follows:
    
    "metadata": \[
      {
        "name": "carHopCapability",
        "value": "getOffCarNavi"
      }
    \]
    
2.  Import required modules.
    
    import { navigationInfoMgr } from '@kit.CarKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
3.  Listen to system navigation information and commands.
    
    Register a listener for system navigation information and commands so that the map app can receive system commands. After the user exits the vehicle, the system sends the **START\_NAVIGATION** command to the map app. The map app can start the walking navigation task after receiving the command.
    
    // Implement the **SystemNavigationListener** API.
    class Listener implements navigationInfoMgr.SystemNavigationListener {
      // Implement the **onQueryNavigationInfo** method.
      onQueryNavigationInfo(query: navigationInfoMgr.QueryType, args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
        // Return navigation information to the system.
        return new Promise(resolve => {
          let ret: navigationInfoMgr.ResultData = {
            code: 1001,
            message: 'message test1',
            data: args
          }
          resolve(ret);
        })
      }
    
      // Implement the **onReceiveNavigationCmd** method.
      onReceiveNavigationCmd(command: navigationInfoMgr.CommandType, args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
        if (command == navigationInfoMgr.CommandType.START\_NAVIGATION) {
          // The map app processes the logic of automatically initiating walking navigation after the user gets off the vehicle.
          if (args !== undefined && args !== null) {
            // Obtain the navigation type.
            let naviType: navigationInfoMgr.NaviType = args\['naviType'\] as navigationInfoMgr.NaviType;
            // The navigation type is walking.
            if (naviType === navigationInfoMgr.NaviType.WALKING) {
              let destPoi: string = args\['destPoi'\] as string;
              // Obtain the destination name.
              let destLocationName: string = args\['destName'\] as string;
              // Obtain the destination latitude.
              let destLatitude: string = destPoi?.split(',')\[0\].toString();
              // Obtain the destination longitude.
              let destLongitude: string = destPoi?.split(',')\[1\].toString();
              // Initiate walking navigation based on **destLocationName**, **destLatitude**, and **destLongitude**.
              // ...
            }
          }
        }
        return new Promise(resolve => {
          let ret: navigationInfoMgr.ResultData = {
            code: 1002,
            message: 'message test2',
            data: args
          }
          resolve(ret);
        })
      }
    }
    
    try {
      // Obtain the **NavigationController** instance.
      let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
      // Register a listener for system navigation information and commands.
      navInfoController.registerSystemNavigationListener(new Listener());
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`register system navigation listener, error code: ${e?.code}\`);
    }
    
4.  Unregister the listener.
    
    When exiting, the map app needs to unregister the listener to reduce unnecessary system resource consumption.
    
    try {
      // Obtain the **NavigationController** instance.
      let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
      // Unregister the listener for system navigation information and commands.
      navInfoController.unregisterSystemNavigationListener();
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`unregister system navigation listener error, error code: ${e?.code}\`);
    }
