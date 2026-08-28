# MapArc

#### Use Cases

This section describes how to draw a MapArc on a map and use the [MapArcParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section943619551002) class to set MapArc parameters such as its position, width, and color.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/1wQ9gro5R7GLNzRXRsMaaA/en-us_image_0000002546025143.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D241F140477BB8A5E731D8E87EC9CADDBEACD6F52D1F4BC3F2C90681AF14CECA "Click to enlarge")

#### API Description

The MapArc adding function is mainly provided by [MapArcParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section943619551002), [addArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section123390488448), and [MapArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-maparc). For more information about the APIs, please refer to [MapArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-maparc).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MapArcParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section943619551002)

 | 

MapArc parameters.

 |
| 

[addArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section123390488448)(params: [mapCommon.MapArcParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section943619551002)): [MapArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-maparc)

 | 

Adds a MapArc.

 |
| 

[MapArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-maparc)

 | 

MapArc. This API supports updating and querying MapArc attributes.

 |

#### Development Procedure

## Adding a MapArc

1.  Import required modules.
    
    import { map, mapCommon, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a MapArc. Create initialization parameters in the **callback** method, and create a MapArc.
    
    @Entry
    @Component
    struct MapArcDemo {
      private TAG = "OHMapSDK\_MapArcDemo";
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapArc?: map.MapArc;
    
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 34.757975,
              longitude: 113.665412
            },
            zoom: 6
          }
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            if (!this.mapController) {
              console.error(this.TAG, "mapController is null");
              return;
            }
            // Set MapArc parameters.
            let mapArcParams: mapCommon.MapArcParams = {
              // Coordinates of the MapArc start point. 
              startPoint: {
                latitude: 39.913138,
                longitude: 116.415112
              },
              // Coordinates of the MapArc end point. 
              endPoint: {
                latitude: 28.239473,
                longitude: 112.954094
              },
              // Coordinates of the MapArc center point. 
              centerPoint: {
                latitude: 33.86970399048567,
                longitude: 112.08633528544145
              },
              width: 10,
              color: 0xffff0000,
              visible: true,
              zIndex: 100
            };
            // Add a MapArc. 
            try {
              this.mapArc = await this.mapController.addArc(mapArcParams);
            } catch (e) {
              console.error(\`Failed to create the MapArc. code: ${e.code}; message: ${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({
              mapOptions: this.mapOptions,
              mapCallback: this.callback
            })
              .width('100%')
              .height('100%');
          }.width('100%')
        }.height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/B8Fd5zbpTh2GmcE8V_3f-A/en-us_image_0000002514545566.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24BFB9CDCCFCC0BEF7D9C0836A77BADA400DB21334F9876FF2FEADAB17DC5304 "Click to enlarge")
