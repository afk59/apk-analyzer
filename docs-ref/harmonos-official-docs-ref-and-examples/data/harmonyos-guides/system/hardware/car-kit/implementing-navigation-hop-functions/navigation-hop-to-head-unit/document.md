# Navigation Hop to Head Unit

#### Use Cases

Navigation data can be transferred to the head unit in the following common scenarios:

-   Tap for navigation hop: When a user is on a specific map screen (location selection, route planning, or driving navigation) on their phone, tapping the phone against a specified area on the vehicle's central display will transfer navigation data from the phone to the head unit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/vkLfhTM5T8mejNBp_mut4w/en-us_image_0000002513687533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10F59B6F97DCBD08155F6C049306B8C6B69CC3E9782D8078EBABDAA788BC7E79 "Click to enlarge")
    
-   Auto navigation hop upon vehicle entry: When a user enters the vehicle after initiating driving navigation on their phone's map app, navigation data will be automatically transferred from the phone to the head unit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/8gW6loxtQP6shGjnrJPVtA/en-us_image_0000002517892175.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F8554F4EBE590C89B47157926779C931A46D00E005DD0377C882240F40C0AF1 "Click to enlarge")
    
-   In-vehicle auto navigation hop: When a user is in the vehicle and initiates driving navigation on their phone's map app, navigation data will be automatically transferred from the phone to the head unit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/DrewV3PRTdCLu5qDh85x3Q/en-us_image_0000002513568407.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F098D12E4962DEABFD147D5BEBECCC288016EF9CF440963597E04F47F9AC511 "Click to enlarge")
    

#### API Description

The following table describes the APIs used for navigation data transfer to the head unit.

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

[on('smartMobilityEvent')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-smartmobilitycommon#section10205101163617)

 | 

Registers a smart mobility service event listener.

 |
| 

[updateNavigationStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-navigationinfomgr#section126311558181112)

 | 

Sets the navigation status, including the map status, navigation type, destination, waypoints, route, and theme.

 |
| 

[unregisterSystemNavigationListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-navigationinfomgr#section1567066181615)

 | 

Unregisters a listener for system navigation information and commands.

 |
| 

[off('smartMobilityEvent')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-smartmobilitycommon#section659872123616)

 | 

Unregisters a smart mobility service event listener.

 |

## SmartMobilityEvent Event Name Description

The following table describes the value of **eventName** in **SmartMobilityEvent**.

| 
Event Name

 | 

Description

 |
| :-- | :-- |
| 

hopSucceeded

 | 

Hop success event.

 |

#### Development Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/4FpBw_arSIq0cqPQunRqsQ/en-us_image_0000002513703149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DCF75D9584FBF878E1765630F1B54F0337BD7E23AE4FCCC9C75DFC4906ECB18 "Click to enlarge")

#### Development Procedure

1.  Configure the capabilities.
    
    For details, please refer to [Configuring Capabilities](../../getting-started/document.md#section239110365269). In the scenario of navigation hop to the head unit, set **name** in the metadata to **carHopCapability**. Set **value** according to the service scenarios.
    
    -   Tap for navigation hop: Set **value** to **carHopNavi**.
    -   Auto navigation hop upon vehicle entry: Set **value** to **getOnCarNavi**.
    -   In-vehicle auto navigation hop: Set **value** to **insideCarNavi**.
2.  Import required modules.
    
    import { navigationInfoMgr, smartMobilityCommon } from '@kit.CarKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
3.  Listen to system navigation information and commands.
    
    Since version 5.1.0(18), the **searchPOI** command is added to search for POI information.
    
    Register a listener for system navigation information and commands when the map app is opened. This listener enables the map app to receive system commands (for example, stop navigation) and execute corresponding service logic.
    
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
        // Receive and process system navigation commands.
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
      hilog.error(0x0000, 'testTag', \`register system navigation listener error, error code: ${e?.code}\`);
    }
    
4.  (Optional) Listen to smart mobility service events.
    
    Register a smart mobility service event listener for the map app to receive event notifications (such as a hop success event) from the smart mobility service and execute corresponding service logic.
    
    // Event callback function of the smart mobility service.
    const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
      hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
      if (event.eventName === 'hopSucceeded' && event.type === smartMobilityCommon.SmartMobilityType.CAR\_HOP) {
        // The map app processes a hop success event (such as exiting navigation).
        // ...
      }
    };
    
    try {
      // Service type.
      let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.CAR\_HOP\];
      // Obtain the **SmartMobilityAwareness** instance.
      let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
      // Register a smart mobility service event listener.
      awareness.on('smartMobilityEvent', types, callBack);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`register smart mobility event listener error, error code: ${e?.code}\`);
    }
    
5.  Set the system navigation status.
    
    Each time when a user selects a destination or waypoint on the map or changes the navigation information, the map app needs to set the navigation status and save the latest navigation status to Car Kit. The system then transfers the latest navigation status data to the head unit.
    
    // Set the destination.
    let location: navigationInfoMgr.Location = {
      name: 'location',
      coordType: navigationInfoMgr.LocationCoordType.GCJ02,
      longitude: 0.000000000000001,
      latitude: 1.000000000000001,
      altitude: 2.000000000000001,
    };
    // (Optional) Set waypoints.
    let passPoint0: navigationInfoMgr.Location = {
      name: 'passPoint0',
      coordType: navigationInfoMgr.LocationCoordType.GCJ02,
      longitude: 29.53851890563965,
      latitude: 16.50643920898438,
      altitude: 3.00015949516846,
    };
    let passPoint1: navigationInfoMgr.Location = {
      name: 'passPoint1',
      coordType: navigationInfoMgr.LocationCoordType.WGS84,
      longitude: 4.4445874651238,
      latitude: 5.55565329843751,
      altitude: 6.66641578943265,
    };
    // Set the navigation status attributes.
    let navigationStatus: navigationInfoMgr.NavigationStatus = {
      status: navigationInfoMgr.MapStatus.NAVIGATION,
      naviType: navigationInfoMgr.NaviType.DRIVING,
      destLocation: location,
      passPoint: \[passPoint0, passPoint1\],
      routeIndex: 101,
      customData: "customData",
      routePreference: \[
        navigationInfoMgr.RoutePreference.TIME\_FIRST,
        navigationInfoMgr.RoutePreference.MAIN\_ROAD\_FIRST
      \],
      theme: navigationInfoMgr.ThemeType.LIGHT
    };
    
    try {
      // Obtain **NavigationController**.
      let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
      navInfoController.updateNavigationStatus(navigationStatus);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`update navigation status error, error code: ${e?.code}\`);
    }
    
6.  Unregister listeners.
    
    When exiting, the map app needs to unregister listeners to reduce unnecessary system resource consumption.
    
    Unregister the listener for system navigation information and commands.
    
    try {
      // Obtain the **NavigationController** instance.
      let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
      // Unregister the listener for system navigation information and commands.
      navInfoController.unregisterSystemNavigationListener();
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`unregister system navigation listener error, error code: ${e?.code}\`);
    }
    
    Unregister the smart mobility service event listener. You can use either of the following methods:
    
    **Method 1**: **Do not pass the optional callback parameter. Then, all callbacks under the given type will be unregistered.**
    
    The sample code is as follows:
    
    try {
      // Service type.
      let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.CAR\_HOP\];
      // Obtain the **SmartMobilityAwareness** instance.
      let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
      // Unregister the smart mobility service event listener.
      awareness.off('smartMobilityEvent', types);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`unregister smart mobility event listener error, error code: ${e?.code}\`);
    }
    
    **Method 2**: **Pass the optional callback parameter. Then, only the specified callback will be unregistered.**
    
    The sample code is as follows:
    
    try {
      // Service type.
      let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.CAR\_HOP\];
      // Obtain the **SmartMobilityAwareness** instance.
      let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
      // Unregister the smart mobility service event listener. The callback is the one defined in step 4.
      awareness.off('smartMobilityEvent', types, callBack);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`unregister smart mobility event listener error, error code: ${e?.code}\`);
    }
