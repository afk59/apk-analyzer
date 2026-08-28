# Navigation and Other Capabilities Provided by the Map App

#### Use Cases

Starting from 5.0.3(15), the following functions are supported: opening the map app home screen, as well as launching the map app for place search, place details viewing, route planning, and navigation. Starting from 6.0.1(21), the function of initiating ride hailing in the map app is supported.

This section describes how to implement the following capabilities:

-   Opening the home screen of the map app
-   Launching the map app for place search
-   Launching the map app to view place details
-   Launching the map app to plan routes
-   Launching the map app for navigation
-   Launching the map app for ride hailing

#### API Description

The map app functions are called using the [openMapHomePage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1117619561413), [openMapTextSearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section2098315915160), [openMapPoiDetail](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section14159526181316), [openMapRoutePlan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1765318218173), [openMapNavi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section16894648175), and [openMapTaxi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section147354416415) APIs in the [petalMaps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps) namespace. For more information about the APIs, please refer to [petalMaps (Starting the Map App)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps).

| 
API Description

 | 

Description

 |
| :-- | :-- |
| 

[TextSearchParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section810823717266)

 | 

Parameters for text search.

 |
| 

[PoiDetailParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1555293218278)

 | 

Parameters for POI details.

 |
| 

[RoutePlanParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section491624219261)

 | 

Parameters for route planning.

 |
| 

[NaviParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section7249174522611)

 | 

Parameters for navigation.

 |
| 

[TaxiParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1625316256212)

 | 

Parameters for ride hailing.

 |
| 

[openMapHomePage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1117619561413)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context)): Promise<void>

 | 

Opens the home screen of the map app.

 |
| 

[openMapTextSearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section2098315915160)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), textSearchParams: [TextSearchParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section810823717266)): Promise<void>

 | 

Launches the map app for place search.

 |
| 

[openMapPoiDetail](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section14159526181316)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), poiDetailParams: [PoiDetailParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1555293218278)): Promise<void>

 | 

Launches the map app to view place details.

 |
| 

[openMapRoutePlan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1765318218173)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), routePlanParams: [RoutePlanParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section491624219261)): Promise<void>

 | 

Launches the map app to plan routes.

 |
| 

[openMapNavi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section16894648175)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), naviParams: [NaviParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section7249174522611)): Promise<void>

 | 

Launches the map app for navigation.

 |
| 

[openMapTaxi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section147354416415)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), taxiParams: [TaxiParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1625316256212)): Promise<void>

 | 

Opens the ride hailing screen of the map app.

 |

#### Coordinate Systems Used by the Map App

Sites in the Chinese mainland, Hong Kong (China), and Macao (China) use the GCJ02 coordinate system, and sites in Taiwan (China) use the WGS84 coordinate system.

Sites outside China use the WGS84 coordinate system. For details about coordinate conversion, please refer to [Coordinate Rectification](../map-calculation-tools/coordinate-rectification/document.md).

#### Development Procedure

Import required modules.

import { petalMaps } from '@kit.MapKit'

## Opening the Home Screen of the Map App

Call [openMapHomePage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1117619561413) to open the home screen of the map app.

try {
  await petalMaps.openMapHomePage(this.getUIContext().getHostContext());
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}

**Figure 1** Opening the home screen of the map app

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/i8_WNNoRRCq_iOFAyT3ZCg/en-us_image_0000002510921742.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD239EA4E9017CAD31E600561A67083AB4D49B981AC4A29A0260A42380686CA7 "Click to enlarge")

## Launching the Map App for Place Search

Call [openMapTextSearch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section2098315915160) and pass in the search target name to launch the map app for place search.

try {
  let params: petalMaps.TextSearchParams = {
  destinationName: 'Cloud Park'
  };
  await petalMaps.openMapTextSearch(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}

**Figure 2** Launching the map app for place search

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/F0u4RMU2Qh2UxOa3E4-Kgg/en-us_image_0000002511082168.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4078A5D9128061A26F2F2B64CDC1C2322C48BBC718B18DBCC88FCE653DF12AB "Click to enlarge")

## Launching the Map App to View Place Details

Call [openMapPoiDetail](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section14159526181316) and pass in the longitude and latitude of a place to launch the map app to view details of the place.

try {
  let params: petalMaps.PoiDetailParams = {
    destinationPosition: {
      latitude: 32.02065982629459,
      longitude: 118.788899213002
    },
    destinationPoiId: '563233191438217472'
  };
  await petalMaps.openMapPoiDetail(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}

**Figure 3** Launching the map app to view place details

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/MkbF3QpJQ5iUni76SKzDuQ/en-us_image_0000002546452193.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=194713BF328DE6EBF04F9F60D6DE87EC32F1AC00EC482FD8BF8DF5EA9CB66955 "Click to enlarge")

## Launching the Map App to Plan Routes

Call [openMapRoutePlan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section1765318218173) and pass in the longitude and latitude of a destination to launch the map app to plan routes.

try {
  let params: petalMaps.RoutePlanParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapRoutePlan(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}

**Figure 4** Launching the map app to plan routes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/20-jZGZyRMGyo_RyRPBq_Q/en-us_image_0000002514932686.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B56632C7FCBBEB7CE9283FABED1FD8E542CE57BB871CBFC29B7E54C322563D9B "Click to enlarge")

## Launching the Map App for Navigation

Call [openMapNavi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section16894648175) and pass in the longitude and latitude of a destination to launch the map app for navigation.

try {
  let params: petalMaps.NaviParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapNavi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}

**Figure 5** Launching the map app for navigation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/hPThJaw0T6GH8KqHOPCPjg/en-us_image_0000002514932830.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBA0AA39D0C817C2ED0EC688ADA2E510B57A3C3C9BBF223F338A97EA3CFDA8FE "Click to enlarge")

## Opening the Ride Hailing Screen of the Map App

Call [openMapTaxi](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-petal-maps#section147354416415) and pass in the longitude and latitude of a destination to launch the map app for ride hailing.

try {
  let params: petalMaps.TaxiParams = {
    destinationPosition: {
      latitude: 31.983015468224288,
      longitude: 118.78058590757131
    }
  };
  await petalMaps.openMapTaxi(this.getUIContext().getHostContext(), params);
} catch (e) {
  console.error(\`code:${e.code}, message:${e.message}\`);
}
