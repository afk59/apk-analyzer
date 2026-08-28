# navigationInfoMgr (Navigation Information Management)

This module provides a set of map navigation functions, including sending navigation commands (such as starting or ending navigation), navigation updates (such as POI information), and navigation metadata (turn-by-turn information, TBT information for short) to maps, for navigation hop and dashboard/AR-HUD display.

**Start version**: 4.1.0(11)

#### Module Import

import { navigationInfoMgr } from '@kit.CarKit';

#### NavigationStatus

Defines the navigation status information, including the map status, navigation type, destination, waypoints, route, map, and theme.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

status

 | 

[MapStatus](#section66501518181418)

 | 

No

 | 

No

 | 

Map status.

 |
| 

naviType

 | 

[NaviType](#section12883193118184)

 | 

No

 | 

No

 | 

Navigation type.

 |
| 

destLocation

 | 

[Location](#section546213416209)

 | 

No

 | 

No

 | 

Destination. The destination information varies according to **status**:

When **status** is set to **MapStatus.NAVIGATION**, this parameter indicates the destination address.

When **status** is set to **MapStatus.POI**, this parameter indicates the POI information.

When **status** is set to **MapStatus.CRUISE**, this parameter indicates the cruise information.

When **status** is set to **MapStatus.IDLE**, this parameter is meaningless.

When **status** is set to **MapStatus.ROUTE**, this parameter indicates the destination address.

When **status** is set to **MapStatus.UNAVAILABLE**, this parameter is meaningless.

 |
| 

passPoint

 | 

[Location](#section546213416209)\[\]

 | 

No

 | 

No

 | 

Array of waypoints.

 |
| 

routeIndex

 | 

number

 | 

No

 | 

No

 | 

Route number, which is an integer greater than or equal to 0.

 |
| 

routePreference

 | 

[RoutePreference](#section1697318441154)\[\]

 | 

No

 | 

No

 | 

Route preference.

 |
| 

theme

 | 

[ThemeType](#section129109467221)

 | 

No

 | 

No

 | 

Map theme color.

 |
| 

customData

 | 

String

 | 

No

 | 

No

 | 

Custom data.

 |

#### MapStatus

Enumerated values of the map status.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

IDLE

 | 

0

 | 

The map is in idle state. This is the default value when the map app is not started.

 |
| 

NAVIGATION

 | 

1

 | 

The map is in navigation mode.

 |
| 

CRUISE

 | 

2

 | 

The map is in cruise mode.

 |
| 

POI

 | 

3

 | 

The map is in point of interest (POI) selection mode.

 |
| 

ROUTE

 | 

4

 | 

The map is in route selection mode.

 |
| 

UNAVAILABLE

 | 

5

 | 

The map service is not available. This value is used when the map app cannot provide services due to an internal error.

 |

#### NaviType

Enumerated values of the navigation type.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

DRIVING

 | 

0

 | 

Driving.

 |
| 

MOTORCYCLE

 | 

1

 | 

Motorcycle.

 |
| 

CYCLING

 | 

2

 | 

Cycling.

 |
| 

WALKING

 | 

3

 | 

Walking.

 |

#### Location

Geographical location information.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Address name, which can contain 0 to 1024 bytes.

 |
| 

coordType

 | 

[LocationCoordType](#section18414131420206)

 | 

No

 | 

No

 | 

Geodetic coordinate system.

 |
| 

longitude

 | 

number

 | 

No

 | 

No

 | 

Longitude of the destination. This parameter is used together with **coordType**. The value ranges from –180 to 180.

 |
| 

latitude

 | 

number

 | 

No

 | 

No

 | 

Latitude of the destination. This parameter is used together with **coordType**. The value ranges from –90 to 90.

 |
| 

altitude

 | 

number

 | 

No

 | 

No

 | 

Altitude of the destination, in meters. The default value is **0**.

 |

#### LocationCoordType

Enumerated values of the geodetic coordinate system.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

GCJ02

 | 

0

 | 

China geodetic coordinate system.

 |
| 

WGS84

 | 

1

 | 

World geodetic coordinate system.

 |

#### RoutePreference

Enumerated values of route preference.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTELLIGENT\_RECOMMENDATION

 | 

0

 | 

Recommend routes smartly.

 |
| 

HIGHWAY\_FIRST

 | 

1

 | 

Take highways in priority.

 |
| 

AVOID\_HIGHWAY

 | 

2

 | 

Avoid highways.

 |
| 

AVOID\_CONGESTION

 | 

3

 | 

Avoid traffic jams.

 |
| 

LESS\_CHARGE

 | 

4

 | 

Minimize tolls.

 |
| 

MAIN\_ROAD\_FIRST

 | 

5

 | 

Take main roads in priority.

 |
| 

TIME\_FIRST

 | 

6

 | 

Minimize travel time when selecting routes.

 |

#### ThemeType

Enumerated values of the map theme color.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

LIGHT

 | 

0

 | 

The map uses the light theme.

 |
| 

DARK

 | 

1

 | 

The map uses the dark theme.

 |

#### NavigationMetadata

Defines the navigation data, including the navigation turn mode, distance to the next turn, current road name, and next road name.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
**Name**

 | 

**Type**

 | 

Read-only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

naviTurnMode

 | 

number

 | 

No

 | 

No

 | 

Navigation turn mode. The value is a hexadecimal number ranging from 0 to 3E7. For details, please refer to [naviTurnMode](../appendixes/naviturnmode/document.md).

 |
| 

segmentLeftDis

 | 

number

 | 

No

 | 

No

 | 

Distance to the next turn, in meters.

 |
| 

currentRoadName

 | 

string

 | 

No

 | 

No

 | 

Current road name, which can contain 0 to 1024 bytes.

 |
| 

nextRoadName

 | 

string

 | 

No

 | 

No

 | 

Next road name, which can contain 0 to 1024 bytes.

 |
| 

intersectionView

 | 

string

 | 

No

 | 

No

 | 

Intersection zoom-in view.

The value is a Base64-encoded byte value of an image.

 |
| 

viewWidth

 | 

number

 | 

No

 | 

No

 | 

Width of an intersection zoom-in view, in pixels.

 |
| 

viewHeight

 | 

number

 | 

No

 | 

No

 | 

Height of an intersection zoom-in view, in pixels.

 |
| 

trafficLane

 | 

string

 | 

No

 | 

No

 | 

Traffic lane. They are ordered from left to right. Regarding communication, traffic lanes are parsed by four-character hexadecimal unit, with each unit representing one lane line. Multiple lane lines can be transmitted as needed. The icon codes are enumerated values, and please refer to [trafficLane](../appendixes/trafficlane/document.md) for specifics.

 |
| 

cameraSpeedLimitValid

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the speed camera alerts function is enabled. The value **true** indicates yes and **false** indicates no.

 |
| 

cameraSpeedLimit

 | 

number

 | 

No

 | 

No

 | 

Speed limit enforced by speed camera, in m/s.

 |
| 

naviSpeedLimitValid

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether navigation speed limit is enabled. The value **true** indicates yes and **false** indicates no.

 |
| 

naviSpeedLimit

 | 

number

 | 

No

 | 

No

 | 

Navigation speed limit, in m/s.

 |
| 

currentSpeed

 | 

number

 | 

No

 | 

No

 | 

Current speed, in m/s.

 |
| 

naviBearing

 | 

number

 | 

No

 | 

No

 | 

Bearing relative to true north.

 |
| 

totalLeftDis

 | 

number

 | 

No

 | 

No

 | 

Total remaining distance, in meters.

 |
| 

remainingTime

 | 

number

 | 

No

 | 

No

 | 

Remaining time, in minutes.

 |
| 

customData

 | 

Record<string, Object>

 | 

No

 | 

Yes

 | 

Custom navigation metadata.

**Start version**: 5.0.0(12)

 |

#### SystemNavigationListener

System navigation listener callback.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

#### \[h2\]onQueryNavigationInfo

onQueryNavigationInfo(query: QueryType, args: Record<string, Object>): Promise<ResultData>

Returns the query result when an app receives a query request from the system.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

query

 | 

[QueryType](#section5929173314151)

 | 

Yes

 | 

Query command.

 |
| 

args

 | 

Record<string, Object>

 | 

Yes

 | 

Additional parameters for the **query** parameter.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ResultData](#section268420482562)\>

 | 

Navigation information query result, which is returned through a promise.

 |

**Example**:

For details, please refer to the example in [registerSystemNavigationListener](#section66695411419).

#### \[h2\]onReceiveNavigationCmd

onReceiveNavigationCmd(command: CommandType, args: Record<string, Object>): Promise<ResultData>

Returns the command execution result when an app receives a command from the system.

This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

command

 | 

[CommandType](#section1255014591510)

 | 

Yes

 | 

Command that the system service requires your app to execute.

 |
| 

args

 | 

Record<string, Object>

 | 

Yes

 | 

Command parameter. The value varies according to **command**:

When **command** is set to **START\_NAVIGATION**, the value is **destLocation**, indicating the navigation destination of the **Location** type.

When **command** is set to **START\_MAP\_LAYER** or **STOP\_MAP\_LAYER**, the value is **mapLayerDisplayId**, indicating the display ID of the screen where a map layer is started.

When **command** is set to **CHANGE\_THEME**, the value is **newTheme**, indicating the new theme that your app is instructed to use, for example, switching between dark and light.

When **command** is set to **SEARCH\_POI**, the value is **address**, indicating the address that your app is instructed to search for.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ResultData](#section268420482562)\>

 | 

Command sending result, which is returned through a promise.

 |

**Example**:

For details, please refer to the example in [registerSystemNavigationListener](#section66695411419).

#### QueryType

Enumerated values of the navigation information query type.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NAVIGATION\_STATUS

 | 

navigationStatus

 | 

Queries the navigation status. The data ([NavigationStatus](#section153711644737)) is returned through a callback.

 |
| 

NAVIGATION\_METADATA

 | 

navigationMetadata

 | 

Queries the TBT navigation information. The data ([NavigationMetadata](#section12118327148)) is returned through a callback.

 |

#### CommandType

Enumerated values of the command type.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

START\_NAVIGATION

 | 

startNavigation

 | 

Starts navigation.

 |
| 

STOP\_NAVIGATION

 | 

stopNavigation

 | 

Stops navigation.

 |
| 

GO\_HOME

 | 

goHome

 | 

Navigates home.

 |
| 

GO\_TO\_COMPANY

 | 

goToCompany

 | 

Navigates to the office.

 |
| 

START\_MAP\_LAYER

 | 

startMapLayer

 | 

Starts a map layer on another screen.

 |
| 

STOP\_MAP\_LAYER

 | 

stopMapLayer

 | 

Stops a map layer on another screen.

 |
| 

ZOOM\_IN\_MAP

 | 

zoomInMap

 | 

Zooms in on the map.

 |
| 

ZOOM\_OUT\_MAP

 | 

zoomOutMap

 | 

Zooms out on the map.

 |
| 

CHANGE\_THEME

 | 

changeTheme

 | 

Changes the theme.

 |
| 

START\_UPDATE\_NAVIGATION\_STATUS

 | 

startUpdateNavigationStatus

 | 

Starts the navigation status update.

**Start version**: 5.0.0(12)

 |
| 

STOP\_UPDATE\_NAVIGATION\_STATUS

 | 

stopUpdateNavigationStatus

 | 

Stops the navigation status update.

**Start version**: 5.0.0(12)

 |
| 

SEARCH\_POI

 | 

searchPOI

 | 

Searches for POIs.

**Start version**: 5.1.0(18)

 |

#### ResultData

Navigation information query result or command sending result.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

code

 | 

number

 | 

No

 | 

No

 | 

Result code. Result code 0 means the operation was successful. Any non-zero code indicates a failure, with the specific value passed from the third-party map app.

 |
| 

message

 | 

string

 | 

No

 | 

No

 | 

Result message, depending on the result code.

For result code 0, the result message could be "execute success" or other similar content indicating an operation success.

For any non-zero code, the result message could be "execute fail" or other similar content indicating an operation failure.

The actual value depends on the value passed from the map app.

 |
| 

data

 | 

{ \[key: string\]: object }

 | 

No

 | 

No

 | 

Additional information. Your app can return the information to the system in the form of key-value pairs as required.

 |

#### getNavigationController

getNavigationController(): NavigationController

Controller used to obtain the navigation information service.

**System capability**: SystemCapability.CarService.NavigationInfo

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NavigationController](#section5525718748)

 | 

Controller of the navigation information service.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { navigationInfoMgr } from '@kit.CarKit';

let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();

#### NavigationController

Controller of the navigation information service.

**System capability**: SystemCapability.CarService.NavigationInfo

**Start version**: 4.1.0(11)

#### \[h2\]updateNavigationStatus

updateNavigationStatus(navigationStatus: NavigationStatus): void

Sets the navigation status, including the map status, navigation type, destination, waypoints, route, map, and theme.

**System capability**: SystemCapability.CarService.NavigationInfo

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

navigationStatus

 | 

[NavigationStatus](#section153711644737)

 | 

Yes

 | 

Navigation status, including the map status, navigation type, destination, waypoints, route, map, and theme.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |
| 

1003810001

 | 

Invalid parameter value.

 |
| 

1003810002

 | 

The total size of all parameters exceeds the limit.

 |

**Example**:

import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

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

#### \[h2\]updateNavigationMetadata

updateNavigationMetadata(navigationMetadata: NavigationMetadata): void

Sets the navigation data, including the navigation turn mode, distance to the next turn, current road name, and next road name.

**System capability**: SystemCapability.CarService.NavigationInfo

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

navigationMetadata

 | 

[NavigationMetadata](#section12118327148)

 | 

Yes

 | 

Navigation data, including the navigation turn mode, distance to the next turn, current road name, and next road name.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |
| 

1003810001

 | 

Invalid parameter value.

 |
| 

1003810002

 | 

The total size of all parameters exceeds the limit.

 |

**Example**:

import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Set the data attributes.
let data: navigationInfoMgr.NavigationMetadata = {
  naviTurnMode: 0x0001,
  segmentLeftDis: 100,
  currentRoadName: 'currentRoad',
  nextRoadName: 'nextRoad',
  intersectionView: 'intersectionView',
  viewWidth: 960,
  viewHeight: 450,
  trafficLane: '0001',
  cameraSpeedLimitValid: false,
  cameraSpeedLimit: 120,
  naviSpeedLimitValid: true,
  naviSpeedLimit: 80,
  currentSpeed: 75,
  naviBearing: 90.00000000000000,
  totalLeftDis: 1546,
  remainingTime: 5,
  customData: { 'sample': 'sampleData' }
};

try {
  // Obtain **NavigationController**.
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.updateNavigationMetadata(data);
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`update navigation metadata error, error code: ${e?.code}\`);
}

#### \[h2\]registerSystemNavigationListener

registerSystemNavigationListener(listener: SystemNavigationListener): void

Registers a listener for system navigation information and commands. This method needs to be called when your app is started.

**System capability**: SystemCapability.CarService.NavigationInfo

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[SystemNavigationListener](#section12455103872013)

 | 

Yes

 | 

Listener for system navigation information and commands.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |
| 

1003810001

 | 

Invalid parameter value.

 |

**Example**:

import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Implement the **SystemNavigationListener** API.
class Listener implements navigationInfoMgr.SystemNavigationListener {
  // Implement the **onQueryNavigationInfo** method.
  onQueryNavigationInfo(query: navigationInfoMgr.QueryType, args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
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
  // Obtain **NavigationController**.
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.registerSystemNavigationListener(new Listener());
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`register system navigation listener error, error code: ${e?.code}\`);
}

#### \[h2\]unregisterSystemNavigationListener

unregisterSystemNavigationListener(): void

Unregisters a listener for system navigation information and commands.

**System capability**: SystemCapability.CarService.NavigationInfo

**Device behavior differences**: This API is supported on phones. On other devices, it returns error code 801.

**Required permission**: ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**Start version**: 4.1.0(11)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

801

 | 

Capability not supported.

 |

**Example**:

import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Obtain **NavigationController**.
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.unregisterSystemNavigationListener();
} catch (e) {
  // Obtain the error code for an API call exception and handle the exception.
  hilog.error(0x0000, 'testTag', \`unregister system navigation listener error, error code: ${e?.code}\`);
}
