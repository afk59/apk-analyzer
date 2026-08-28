# TileOverlay

#### Use Cases

This section describes how to add a TileOverlay. You can use your own TileOverlay data by either loading it from an online source or a local file. The TileOverlay can be transformed in response to map operations such as panning, zooming, and rotating. The TileOverlay layer is positioned directly above the base map (that is, the TileOverlay layer occludes only the base map but no other layers). The order in which the TileOverlay is added does not affect the overlay relationship of other layers.

You can use TileOverlays to add additional features, such as the indoor information of a shopping mall or details about a scenic spot, to the base map. This capability is applicable to the scenario where you have the map of a specific region and want to overlay it onto the corresponding region on Huawei map.

Starting from 5.0.3(15), the TileOverlay function is supported.

Starting from 6.0.0(20), **TileOverlayOptions** is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/L7CMYtKIT9OogEjKEjKJMw/en-us_image_0000002542523021.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAE51667FDFDE4E14E051B2A4AE5EB817FC989432CE8E65676790FEEE47540AF "Click to enlarge")

#### API Description

The TileOverlay functions are mainly provided by [TileOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section3168172982513), [TileOverlayOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section849136102717), [addTileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section169060253532), and [TileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-tileoverlay). For more information about the APIs, please refer to [TileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-tileoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[TileOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section3168172982513)

 | 

TileOverlay parameters.

 |
| 

[TileOverlayOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section849136102717)

 | 

TileOverlay parameters.

 |
| 

[addTileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section169060253532)(params: [mapCommon.TileOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section3168172982513) | [mapCommon.TileOverlayOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section849136102717)): [TileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-tileoverlay)

 | 

Adds a TileOverlay to a map.

 |
| 

[TileOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-tileoverlay)

 | 

TileOverlay. This API supports updating and querying TileOverlay attributes.

 |

#### Development Procedure

A TileOverlay can be drawn by loading from an online source or a local file.

## Online Download

1.  Import required modules.
    
    import { map, mapCommon, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a TileOverlay. Set the URL of the online TileOverlay.
    
    @Entry
    @Component
    struct TileOverlayDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private tileOverlay?: map.TileOverlay;
    
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 48.893478,
              longitude: 2.334595
            },
            zoom: 7
          }
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let params: mapCommon.TileOverlayOptions = {
              // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
              // Replace it with your own URL.
              tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
              // Set the transparency.
              transparency: 0.5,
              // Enable the TileOverlay fade-in effect.
              fadeIn: true
            };
            try {
              this.tileOverlay = this.mapController?.addTileOverlay(params);
            } catch (e) {
              console.error(\`code:${e.code}, message:${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
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
    
2.  Add a TileOverlay.
    
    @Entry
    @Component
    struct TileOverlayDemo {
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private tileOverlay?: map.TileOverlay;
    
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 48.893478,
              longitude: 2.334595
            },
            zoom: 7
          },
          scaleControlsEnabled: true
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let tileOverlayOption: mapCommon.TileOverlayOptions = {
              // Obtain the TileOverlay based on the coordinates. You need to implement the **tileProvider** method to obtain the TileOverlay data locally.
              tileProvider: this.tileProviderMethod,
              // Fade-in and fade-out effect (**true**: enabled; **false**: disabled).
              fadeIn: false,
              // Transparency (the value ranges from 0 to 1).
              transparency: 0.5,
              // Visibility (**true**: visible; **false**: invisible).
              visible: true
            }
            if (this.mapController !== undefined) {
              try {
                this.tileOverlay = this.mapController.addTileOverlay(tileOverlayOption);
              } catch (e) {
                console.error(\`code:${e.code}, message:${e.message}\`);
              }
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      private tileProviderMethod(x: number, y: number, z: number): Promise<ArrayBuffer> {
        return new Promise((resolve, reject) => {});
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
    

## Caching TileOverlay Data

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a TileOverlay.
    
    @Entry
    @Component
    struct TileOverlayDemo {
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private tileOverlay?: map.TileOverlay;
    
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 48.87278,
              longitude: 2.33016
            },
            zoom: 4
          },
          scaleControlsEnabled: true
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let options: mapCommon.TileOverlayOptions = {
              // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
              // Replace it with your own URL.
              tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
              // Whether to enable disk caching (**true**: yes; **false**: no).
              diskCacheEnabled: true,
              // Disk cache size, in KB. The default value is **20480**.
              diskCacheSize: 20480,
              // Path of the sandbox for storing disk cache.
              diskCachePath: this.getUIContext().getHostContext()?.databaseDir
            };
            if (this.mapController !== undefined) {
              try {
                this.tileOverlay = this.mapController.addTileOverlay(options);
              } catch (e) {
                console.error(\`code:${e.code}, message:${e.message}\`);
              }
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      aboutToDisappear(): void {
        if (this.tileOverlay) {
          this.tileOverlay.remove();
          // Clear the memory cache.
          this.tileOverlay.clearTileCache();
          // Clear the disk and memory caches.
          this.tileOverlay.clearDiskCache();
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
