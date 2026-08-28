# MapCircle

#### Use Cases

This section describes how to draw a MapCircle on a map.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/8ErKK4I2Rkuaq9WNJgDwkg/en-us_image_0000002511014404.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D15C45D212D4AFD24C1B28EE75BEC37B2616FD39422A91CF911E5250A7913702 "Click to enlarge")

#### API Description

The MapCircle adding function is mainly provided by [MapCircleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section5282124803117), [addCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section8212148102813), and [MapCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcircle). For more information about the APIs, please refer to [MapCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcircle).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MapCircleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section5282124803117)

 | 

MapCircle parameters.

 |
| 

[addCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section8212148102813)(options: [mapCommon.MapCircleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section5282124803117)): Promise<[MapCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcircle)\>

 | 

Adds a MapCircle to a map. The longitude and latitude of the center and the radius are specified for the MapCircle to indicate the surrounding area of a location.

 |
| 

[MapCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcircle)

 | 

MapCircle. This API supports updating and querying MapCircle attributes.

 |

#### Development Procedure

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a MapCircle. Create initialization parameters in the **callback** method, and create a MapCircle.
    
    @Entry
    @Component
    struct MapCircleDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapCircle?: map.MapCircle;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 39.918,
              longitude: 116.397
            },
            zoom: 14
          }
        };
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            // MapCircle initialization parameters.
            let mapCircleOptions: mapCommon.MapCircleOptions = {
              center: {
                latitude: 39.918,
                longitude: 116.397
              },
              radius: 500,
              clickable: true,
              fillColor: 0xFFFFC100,
              strokeColor: 0xFFFF0000,
              strokeWidth: 10,
              visible: true,
              zIndex: 15
            }
            // Create a MapCircle.
            try {
              this.mapCircle = await this.mapController.addCircle(mapCircleOptions);
            } catch (e) {
              console.error(\`Failed to create the MapCircle. code: ${e.code}; message: ${e.message}\`);
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/5tH3YzJLQ5OeQoSmsBxRNw/en-us_image_0000002542494709.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9C9E050A5303B00AC89AE12FF5F08F0863E91720903ED7AF4060C13815C237D "Click to enlarge")
