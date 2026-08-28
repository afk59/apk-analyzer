# Map Screenshot

This section describes how to implement the map screenshot function.

A map screenshot is a captured image of the visible region on a map, including map elements, overlays, and logos.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ENuOUtWLRPGSqvpB4xeimQ/en-us_image_0000002515124978.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90E86202485967373BC021E43F8664301ECC7165E2A61A64EF981571AB3F0EE5 "Click to enlarge")

#### API Description

The following table describes the map screenshot API, which is provided by [snapshot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section4803202315197). For more information about the APIs, please refer to [snapshot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section4803202315197).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[snapshot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section4803202315197)(): Promise<[image.PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)\>

 | 

Takes map screenshots.

 |

#### Development Procedure

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    import { image } from '@kit.ImageKit';
    
2.  Call the [snapshot](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section4803202315197) method to take a screenshot of the current map screen.
    
    @Entry
    @Component
    struct HuaweiMapDemo {
      private mapOptions?: mapCommon.MapOptions;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapController?: map.MapComponentController;
      @State image?: image.PixelMap = undefined;
    
      aboutToAppear(): void {
        // Map initialization parameters used to set the coordinates of the map center point and zoom level.
        this.mapOptions = {
          position: {
            target: {
              latitude: 39.9,
              longitude: 116.4
            },
            zoom: 10
          }
        };
    
        // Map initialization callback.
        this.callback = async (err, mapController) => {
          if (!err) {
            // Obtain **mapController** to operate the map.
            this.mapController = mapController;
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
              .width('100%')
              .height('50%');
    
            Scroll(new Scroller()) {
              Column() {
                Image(this.image)
                  .objectFit(ImageFit.Auto)
                  .border({ width: 1, color: Color.Red }).width("100%")
                Button ("Get Screenshot")
                  .margin({ left: 10 })
                  .fontSize(12)
                  .onClick(async () => {
                    if (this.mapController) {
                      let pixelMap = await this.mapController.snapshot();
                      this.image = pixelMap;
                    }
                  });
              }
            }.width('70%').height("50%")
          }.width('100%')
        }.height('100%')
      }
    }
