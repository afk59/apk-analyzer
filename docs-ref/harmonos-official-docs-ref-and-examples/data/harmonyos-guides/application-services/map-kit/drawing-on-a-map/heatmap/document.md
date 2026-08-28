# Heatmap

#### Use Cases

A heatmap layer can be added to display data distribution. The heatmap function visualizes the density and distribution of people or vehicles in a region with different colors. Heatmaps are well suited for visualizing data density in large-scale scenarios, such as pedestrian flow distribution and hotspot areas.

Starting from 6.0.0(20), the heatmap function is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/kmo1HZjGTZCrxDCiU0SrLA/en-us_image_0000002514554906.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D287DDFD9702C308E80109C169D85F2F9FA266CCCF738F5FF2D05A107A62079 "Click to enlarge")

#### API Description

The heatmap functions are mainly provided by [HeatmapParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section273113662417), [addHeatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section849314585910), and [Heatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-heatmap#section792365317339). For more information about the APIs, please refer to [Heatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-heatmap#section792365317339).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HeatmapParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section273113662417)

 | 

Heatmap parameters.

 |
| 

[addHeatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section849314585910)(params: [mapCommon.HeatmapParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section273113662417)): Promise<[Heatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-heatmap#section792365317339)\>

 | 

Adds a heatmap.

 |
| 

[Heatmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-heatmap#section792365317339)

 | 

Heatmap. You can modify and delete heatmaps, for example, setting the heatmap color and opacity.

 |

#### Development Procedure

1.  Import required modules.
    
    import { map, mapCommon, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a heatmap.
    
    @Entry
    @Component
    struct HeatMapDemo {
      private TAG = "OHMapSDK\_HeatMapDemo";
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
    
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 31.000000,
              longitude: 118.000000
            },
            zoom: 11
          }
        }
        this.callback = async (err, mapController) => {
          console.info(this.TAG, "mapCallback err=" + JSON.stringify(err) +
            "; mapController=" + JSON.stringify(mapController));
          if (!err) {
            this.mapController = mapController;
            let data: mapCommon.WeightedLatLng\[\] = \[\];
            for (let i = 0; i < 500; i++) {
              data.push({
                point: {
                  longitude: 118.000000 + Math.random() \* 1 - 0.25,
                  latitude: 31.000000 + Math.random() \* 1 - 0.25
                },
                intensity: 1
              });
            }
            let heatMapOptions: mapCommon.HeatmapParams = {
              id: 'heatmap0001',
              data:data,
              radius:20,
              intensity: {
                2: 1,
                5: 5,
                8: 10
              }
            }
            try {
              await this.mapController?.addHeatmap(heatMapOptions);
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
