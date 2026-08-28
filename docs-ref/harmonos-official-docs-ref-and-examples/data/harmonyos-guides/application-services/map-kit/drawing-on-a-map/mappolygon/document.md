# MapPolygon

#### Use Cases

This section describes how to draw a MapPolygon on a map.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/xOUuDqMNS1myXWIYjWCGBA/en-us_image_0000002514386286.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8AF291F85D1F165674A8190275FC24B78AAA77272E0E6A174289ACE6A40080D7 "Click to enlarge")

#### API Description

The MapPolygon adding function is mainly provided by [MapPolygonOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1615694815308), [addPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1825517119280), and [MapPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolygon). For more information about the APIs, please refer to [MapPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolygon).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MapPolygonOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1615694815308)

 | 

MapPolygon parameters.

 |
| 

[addPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1825517119280)(options: [mapCommon.MapPolygonOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1615694815308)): Promise<[MapPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolygon)\>

 | 

Adds a MapPolygon to a map.

 |
| 

[MapPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolygon)

 | 

MapPolygon. This API supports updating and querying MapPolygon attributes.

 |

#### Development Procedure

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a MapPolygon. Create initialization parameters in the **callback** method, and create a MapPolygon.
    
    @Entry
    @Component
    struct MapPolygonDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapPolygon?: map.MapPolygon;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.98,
              longitude: 118.78
            },
            zoom: 14
          }
        };
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            // MapPolygon initialization parameters. 
            let polygonOptions: mapCommon.MapPolygonOptions = {
              points: \[
                { longitude: 118.78, latitude: 31.975 },
                { longitude: 118.78, latitude: 31.985 },
                { longitude: 118.79, latitude: 31.985 },
                { longitude: 118.79, latitude: 31.975 }
              \],
              clickable: true,
              fillColor: 0xff00DE00,
              geodesic: false,
              strokeColor: 0xff000000,
              jointType: mapCommon.JointType.DEFAULT,
              strokeWidth: 10,
              visible: true,
              zIndex: 10
            }
            // Create a MapPolygon.
            try {
              this.mapPolygon = await this.mapController.addPolygon(polygonOptions);
            } catch (e) {
              console.error(\`Failed to create the MapPolygon. code: ${e.code}; message: ${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
          }.width('100%')
        }.height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/9uwNFHBMS5qq9Rr90u2PnA/en-us_image_0000002546027165.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F89D6E7460E1A6A1236B0857CDFC01FA709487B9C7160BDBDD779A4045D0AC70 "Click to enlarge")
