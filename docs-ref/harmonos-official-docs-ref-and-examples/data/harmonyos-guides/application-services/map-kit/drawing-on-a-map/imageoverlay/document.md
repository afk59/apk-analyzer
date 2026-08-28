# ImageOverlay

#### Use Cases

An ImageOverlay is an image fixed on a map. This section describes how to add an ImageOverlay to a map.

An ImageOverlay is a special overlay positioned between the base map and the base map label layer. It does not obscure the map label information. You can use the [ImageOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section12537418218) class to set an image. The image will dynamically transform along with any panning, zooming, or rotating actions performed on the map.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/tl0BbsykSDKG_rV8JrKVzw/en-us_image_0000002545989829.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D1D4AEF04CC419C5B6FD527C2D935E931F3D9E3881A6DE7E2A24233C6692F5E "Click to enlarge")

#### API Description

The ImageOverlay adding function is mainly provided by [ImageOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section12537418218), [addImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1177619539267), and [ImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-imageoverlay). For more information about the APIs, please refer to [ImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-imageoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ImageOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section12537418218)

 | 

ImageOverlay parameters.

 |
| 

[addImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1177619539267)(params: [mapCommon.ImageOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section12537418218)): Promise<[ImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-imageoverlay)\>

 | 

Adds an ImageOverlay on the map.

 |
| 

[ImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-imageoverlay)

 | 

ImageOverlay. This API supports updating and querying ImageOverlay attributes.

 |

#### Development Procedure

1.  Import required modules.
    
    import { map, mapCommon, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add an ImageOverlay.
    
    @Entry
    @Component
    struct ImageOverlayDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapEventManager?: map.MapEventManager;
    
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 32.2,
              longitude: 118.2
            },
            zoom: 10
          }
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            this.mapEventManager = this.mapController.getEventManager();
            let imageOverlayParams: mapCommon.ImageOverlayParams = {
              // Range of the ImageOverlay. 
              bounds: {
                southwest: {
                  latitude: 32,
                  longitude: 118
                },
                northeast: {
                  latitude: 32.4,
                  longitude: 118.4
                }
              },
              // Image of the ImageOverlay. The icon must be stored in the **resources/rawfile** directory.
              image: 'icon/icon.png',
              transparency: 0.3,
              zIndex: 101,
              anchorU: 0.5,
              anchorV: 0.5,
              clickable: true,
              visible: true,
              bearing: 0
            };
            // Add an ImageOverlay.
            try {
              let imageOverlay = await this.mapController?.addImageOverlay(imageOverlayParams);
            } catch (e) {
              console.error(\`Failed to create the ImageOverlay. code: ${e.code}; message: ${e.message}\`);
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
            })
              .width('100%')
              .height('100%');
          }.width('100%')
        }.height('100%')
      }
    }
    
3.  Set a listener for ImageOverlay tap events.
    
    let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay: map.ImageOverlay) => {
      console.info("imageOverlay callback");
    }
    // Enable the listener for ImageOverlay tap events.
    this.mapEventManager.on("imageOverlayClick", imageOverlayCallback);
    // Disable the listener for ImageOverlay tap events.
    this.mapEventManager.off("imageOverlayClick", imageOverlayCallback);
