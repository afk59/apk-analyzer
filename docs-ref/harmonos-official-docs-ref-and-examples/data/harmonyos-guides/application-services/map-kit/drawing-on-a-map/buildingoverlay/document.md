# BuildingOverlay

#### Use Cases

This section describes how to draw a BuildingOverlay on a map.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/KdsyQ-wNTKSS529B_dXdgA/en-us_image_0000002514390206.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A866D45E4EFE6D3C10F687421440D0BA1E727EDF13A96E82E75DF24CF2416766 "Click to enlarge")

#### API Description

The BuildingOverlay adding function is mainly provided by [BuildingOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section316117228284), [addBuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section97851167710), and [BuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-buildingoverlay). For more information about the APIs, please refer to [BuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-buildingoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[BuildingOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section316117228284)

 | 

BuildingOverlay parameters.

 |
| 

[addBuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section97851167710)(params: [mapCommon.BuildingOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section316117228284)): Promise<[BuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-buildingoverlay)\>

 | 

Adds a BuildingOverlay to a map.

 |
| 

[BuildingOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-buildingoverlay)

 | 

BuildingOverlay. This API supports updating and querying BuildingOverlay attributes.

 |

#### Development Procedure

## Adding a BuildingOverlay

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a BuildingOverlay.
    
    @Entry
    @Component
    struct BuildingOverlayDemo {
      private TAG = "OHMapSDK\_BuildingOverlayDemo";
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private buildingOverlay?: map.BuildingOverlay;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.984794,
              longitude: 118.765865
            },
            zoom: 18
          },
          scaleControlsEnabled: true
        }
    
        this.callback = async (err, mapController) => {
          console.info(this.TAG, "addBuildingOverlay");
          if (!err) {
            this.mapController = mapController;
            let points: Array<mapCommon.LatLng> = \[
              {
                latitude: 31.984794,
                longitude: 118.765865
              },
              {
                latitude: 31.98468,
                longitude: 118.766076
              },
              {
                latitude: 31.98472,
                longitude: 118.766116
              },
              {
                latitude: 31.98463,
                longitude: 118.766292
              },
              {
                latitude: 31.984586,
                longitude: 118.766251
              },
              {
                latitude: 31.984536,
                longitude: 118.766344
              },
              {
                latitude: 31.984633,
                longitude: 118.766446
              },
              {
                latitude: 31.9848,
                longitude: 118.766285
              },
              {
                latitude: 31.984925,
                longitude: 118.766312
              },
              {
                latitude: 31.985282,
                longitude: 118.766661
              },
              {
                latitude: 31.985438,
                longitude: 118.766419
              },
              {
                latitude: 31.985801,
                longitude: 118.766755
              },
              {
                latitude: 31.985856,
                longitude: 118.766504
              },
              {
                latitude: 31.985785,
                longitude: 118.766434
              },
              {
                latitude: 31.985821,
                longitude: 118.766278
              },
              {
                latitude: 31.985897,
                longitude: 118.766311
              },
              {
                latitude: 31.985944,
                longitude: 118.766095
              },
              {
                latitude: 31.985909,
                longitude: 118.766069
              },
              {
                latitude: 31.985794,
                longitude: 118.765989
              },
              {
                latitude: 31.9857,
                longitude: 118.766029
              },
              {
                latitude: 31.985658,
                longitude: 118.766164
              },
              {
                latitude: 31.985647,
                longitude: 118.766271
              },
              {
                latitude: 31.985574,
                longitude: 118.766297
              },
              {
                latitude: 31.985458,
                longitude: 118.766285
              },
              {
                latitude: 31.985271,
                longitude: 118.766002
              },
              {
                latitude: 31.985219,
                longitude: 118.766002
              },
              {
                latitude: 31.985135,
                longitude: 118.766029
              },
              {
                latitude: 31.985093,
                longitude: 118.766083
              },
              {
                latitude: 31.985019,
                longitude: 118.766109
              },
              {
                latitude: 31.984978,
                longitude: 118.766083
              },
              {
                latitude: 31.984794,
                longitude: 118.765865
              }
            \];
            points.reverse();
            // BuildingOverlay parameters.
            let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
              {
                // BuildingOverlay range parameters (the points are drawn clockwise). 
                points: points,
                // Height of the BuildingOverlay.
                totalHeight: 51,
                // Height of the selected floor in the BuildingOverlay. 
                floorBottomHeight: 33,
                // Color of the BuildingOverlay's rooftop.
                topFaceColor: 0xffa4b8f7,
                // Color of the BuildingOverlay's lateral surface.
                sideFaceColor: 0x44a4b8f7,
                // Color of the selected floor in the BuildingOverlay. 
                floorColor: 0xff000000,
                // Floor from which the BuildingOverlay starts to be displayed.
                showLevel: 14,
                // Duration of the animation of the selected floor in the BuildingOverlay rising from the bottom.
                animationDuration: 5000,
                // Texture of the BuildingOverlay's lateral surface. Replace the resource image with your own one. Save your resource image in the **resources/base/media** directory.
                sideTexture: { image: $r("app.media.side\_tex"), height: 3, width: 3 },
                // Texture of the selected floor in the BuildingOverlay. Replace the resource image with your own one. Save your resource image in the **resources/base/media** directory.
                floorTexture: { image: $r("app.media.floor\_tex"), height: 3, width: 3 }
              };
            let cameraUpdate = map.newCameraPosition({
              target: {
                latitude: 31.984794,
                longitude: 118.765865
              },
              zoom: 18,
              tilt: 70
            });
            // Move the map camera to focus on the BuildingOverlay area. 
            this.mapController?.moveCamera(cameraUpdate);
            // Create a BuildingOverlay.
            try {
              this.buildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
            } catch (e) {
              console.error(\`Failed to create the BuildingOverlay. code: ${e.code}; message: ${e.message}\`);
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
              mapCallback: this.callback,
            }).width('100%').height('100%');
          }.width('100%')
        }.height('100%')
      }
    }
