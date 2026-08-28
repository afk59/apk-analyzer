# FlowFieldOverlay

#### Use Cases

A FlowFieldOverlay can be added to overlay data onto the base map for displaying real-time wind field and ocean current information.

Starting from 6.0.0(20), the FlowFieldOverlay function is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/4WB2YNr0QbezmUDrVkhmEw/en-us_image_0000002514556320.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71044610FECFEBC835B28D9AF94EEEF674AFBA8BFDF3304FB02FA05DFB3DD5C7 "Click to enlarge")

#### API Description

The FlowFieldOverlay functions are mainly provided by [FlowFieldOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1920897172416), [addFlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section7516202017439), and [FlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-flowfieldoverlay). For more information about the APIs, please refer to [FlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-flowfieldoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[FlowFieldOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1920897172416)

 | 

FlowFieldOverlay parameters.

 |
| 

[addFlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section7516202017439)(params: mapCommon.[FlowFieldOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1920897172416)): Promise<[FlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-flowfieldoverlay)\>

 | 

Adds a FlowFieldOverlay.

 |
| 

[FlowFieldOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-flowfieldoverlay)

 | 

FlowFieldOverlay object.

 |

#### Development Procedure

## Adding a FlowFieldOverlay

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Draw a FlowFieldOverlay.
    
    @Entry
    @Component
    struct MapFlowFieldOverlayDemo {
      private TAG = "OHMapSDK\_MapFlowFieldOverlayDemo";
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private fieldOverlay?: map.FlowFieldOverlay;
    
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 31.984410259206815,
              longitude: 118.76625379397866
            },
            zoom: 4
          },
          scaleControlsEnabled: true
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let params: mapCommon.FlowFieldOverlayParams = {
              // The value of **data** must be in JSON format and complies with the GRIB2 specification. Set **data** by referring to flow field data format.
              data:
              \`\[{
                "header": {
                  "parameterUnit": "m.s-1",
                  "parameterNumber": 2,
                  "dx": 10,
                  "dy": 20,
                  "parameterNumberName": "U-component-wind",
                  "la2": -90,
                  "la1": 90,
                  "parameterCategory": 2,
                  "lo1": 0,
                  "lo2": 359.75,
                  "ny": 4,
                  "nx": 4,
                  "numberPoints": 16
                },
                "data": \[2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2\]
              }, {
                "header": {
                  "parameterUnit": "m.s-1",
                  "parameterNumber": 3,
                  "dx": 4,
                  "dy": 4,
                  "parameterNumberName": "U-component-wind",
                  "la2": -90,
                  "la1": 90,
                  "parameterCategory": 2,
                  "lo1": 0,
                  "lo2": 359.75,
                  "ny": 4,
                  "nx": 4,
                  "numberPoints": 16
                },
                "data": \[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1\]
              }\]\`,
              style: {
                count: 10000,
                color: 0xff0000ff,
                maxSpeed: 100,
                speedFactor: 1
              }
            };
    
            try {
              this.fieldOverlay = await this.mapController?.addFlowFieldOverlay(params);
            } catch (e) {
              console.error(this.TAG, \`code:${e.code}, message:${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
              .width('100%')
              .height('100%');
          }.width('100%')
        }.height('100%')
      }
    }
    

## Flow Field Data Format Reference

The value of **data** in the [FlowFieldOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1920897172416) class is in JSON format and complies with the GRIB2 specification. GRIB2 is a binary data format defined by the World Meteorological Organization (WMO), primarily used for storing and transmitting meteorological and climate data.

\[
// **header** indicates the overall information of **data**, and **data** indicates the zonal velocity.
  {"header":{},"data":\[\]},
  // **header** indicates the overall information of **data**, and **data** indicates the meridional velocity.
  {"header":{},"data":\[\]}
\]

The following is an example of wind field data.

\[{
  "header": {
    "parameterUnit": "m.s-1",   // Wind speed unit.
    "parameterNumber": 2,       // Wind direction. The value **2** indicates the U-component (zonal), and the value **3** indicates the V-component (meridional).
    "dx": 10,                   // Zonal spacing, that is, the longitude value occupied by each grid cell. The value is an integer.
    "dy": 20,                   // Meridional spacing, that is, the latitude value occupied by each grid cell. The value is an integer.
    "parameterNumberName": "U-component-wind",   // Name for the U-component of the wind.
    "la2": -90,                 // Latitude range start value. The value of la2 must be less than that of la1.
    "la1": 90,                  // Latitude range end value. The value of la2 must be less than that of la1.
    "parameterCategory": 2,     // Data category.
    "lo1": 0,                   // Longitude range start value. The value of lo1 must be less than that of lo2.
    "lo2": 359.75,              // Longitude range end value. The value of lo1 must be less than that of lo2.
    "nx": 4,                    // Number of zonal grid cells. The value is an integer.
    "ny": 4,                    // Number of meridional grid cells. The value is an integer.
    "numberPoints": 16          // Number of wind speed data points, that is, the number of data records in **data**.
  },
  // Zonal velocity. The number of data records must be equal to the value of **numberPoints**.
  "data": \[2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2\]
}, {
  "header": {
    "parameterUnit": "m.s-1",   // Wind speed unit.
    "parameterNumber": 3,       // Wind direction. The value **2** indicates the U-component (zonal), and the value **3** indicates the V-component (meridional).
    "dx": 4,                    // Zonal spacing, that is, the longitude value occupied by each grid cell. The value is an integer.
    "dy": 4,                    // Meridional spacing, that is, the latitude value occupied by each grid cell. The value is an integer.
    "parameterNumberName": "V-component-wind",   // Name for the V-component of the wind.
    "la2": -90,                 // Latitude range start value. The value of la2 must be less than that of la1.
    "la1": 90,                  // Latitude range end value. The value of la2 must be less than that of la1.
    "parameterCategory": 2,     // Data category.
    "lo1": 0,                   // Longitude range start value. The value of lo1 must be less than that of lo2.
    "lo2": 359.75,              // Longitude range end value. The value of lo1 must be less than that of lo2.
    "nx": 4,                    // Number of zonal grid cells. The value is an integer.
    "ny": 4,                    // Number of meridional grid cells. The value is an integer.
    "numberPoints": 16          // Number of wind speed data points, that is, the number of data records in **data**.
  },
  // Zonal velocity. The number of data records must be equal to the value of **numberPoints**.
  "data": \[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1\]
}\]
