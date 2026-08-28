# MvtOverlay

#### Use Cases

An MvtOverlay can be added to overlay vector data onto the base map. You can use MvtOverlays to add additional features, such as the global or regional weather condition, to the base map.

Starting from 6.0.0(20), the MvtOverlay function is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/WKOxFw3eQxanJhDbQmvsWQ/en-us_image_0000002514395388.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59A031AC48912335078FA96CECF7946091459932550931ACEC21B9FAB444642D "Click to enlarge")

#### API Description

The MvtOverlay functions are mainly provided by [MvtOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17301232184), [addMvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section10177450104116), and [MvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mvtoverlay). For more information about the APIs, please refer to [MvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mvtoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MvtOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17301232184)

 | 

MvtOverlay parameters.

 |
| 

[addMvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section10177450104116)(params: [mapCommon.MvtOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17301232184)): [MvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mvtoverlay)

 | 

Adds an MvtOverlay.

 |
| 

[MvtOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mvtoverlay)

 | 

MvtOverlay object. You can add and delete MvtOverlays.

 |

#### Development Procedure

An MvtOverlay can be drawn by loading from an online source or a local file.

## Online Download

1.  Before drawing an MvtOverlay by downloading an online source, you need to configure the network access permission in the **module.json5** file of your app.
    
    {
      "module" : {
        // ...
        "requestPermissions":\[
          {
            // Allow your app to use the Internet.
            "name": "ohos.permission.INTERNET",
            "usedScene": {
              "when": "always"
            }
          }
        \]
      }
    }
    
2.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
3.  Draw an MvtOverlay.
    
    The MvtOverlay supports data sources in the common vector tile format (PBF/MVT). The default values of **sourceLayer**, **fillColor**, and **fillOpacity** of the **layers** parameter in the [MvtOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17301232184) class can be manually set or obtained from vector data.
    
    @Entry
    @Component
    struct MvtOverlayDemo {
      private TAG = 'OHMapSDK\_MvtOverlayDemo';
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 35.899780,
              longitude: 107.766172
            },
            zoom: 6
          },
          scaleControlsEnabled: true
        }
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let params: mapCommon.MvtOverlayParams = {
              source: {
                // Set the URL of the MvtOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
                tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
                minZoom: 2,
                maxZoom: 15
              },
              layers: \[{
                id: 'layer-map',
                type: mapCommon.MvtLayerType.FILL,
                // MvtOverlay name.
                sourceLayer: 'XX',
                paint: {
                  fillColor: {
                    operator: mapCommon.Operator.GET,
                    args: 'fill'
                  },
                  fillOpacity: {
                    operator: mapCommon.Operator.GET,
                    args: 'fill-opacity'
                  }
                }
              }\]
            }
            try {
              this.mapController?.addMvtOverlay(params);
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
              .height('100%')
          }.width('100%')
        }.height('100%')
      }
    }
    

## Local Loading

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a local MvtOverlay.
    
    @Entry
    @Component
    struct MvtOverlayDemo {
      private TAG = 'OHMapSDK\_MvtOverlayDemo';
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 35.899780,
              longitude: 107.766172
            },
            zoom: 6
          },
          scaleControlsEnabled: true
        }
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let params: mapCommon.MvtOverlayParams = {
              source: {
                // Obtain the MvtOverlay based on the coordinates. You need to implement the **tileProvider** method to obtain the MvtOverlay data locally.
                tileProvider: this.tileProviderMethod,
                minZoom: 2,
                maxZoom: 15
              },
              layers: \[{
                id: 'layer-map',
                type: mapCommon.MvtLayerType.FILL,
                // MvtOverlay name.
                sourceLayer: 'XX',
                paint: {
                  fillColor: {
                    operator: mapCommon.Operator.GET,
                    args: 'fill'
                  },
                  fillOpacity: {
                    operator: mapCommon.Operator.GET,
                    args: 'fill-opacity'
                  }
                }
              }\]
            }
            try {
              this.mapController?.addMvtOverlay(params);
            } catch (e) {
              console.error(this.TAG, \`code:${e.code}, message:${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      // Implement the **tileProviderMethod** method to load MvtOverlay resources from the local project.
      private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
        return new Promise((resolve, reject) => {});
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
              .width('100%')
              .height('100%')
          }.width('100%')
        }.height('100%')
      }
    }
