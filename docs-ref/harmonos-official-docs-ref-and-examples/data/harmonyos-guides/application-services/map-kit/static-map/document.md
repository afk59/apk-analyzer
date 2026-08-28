# Static Map

#### Use Cases

This section describes how to use the static map function. The static map function returns a map image. You can embed the map as an image into your app or atomic service. This function allows you to specify the requested map location and image size.

**Figure 1** Static Map

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/BUFQiJmqQuSMZmjbGuH3IQ/en-us_image_0000002546036719.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E40CB3E7D13C6F2823A612249C263712E2AF7C0E66FF88FE4349498EF000D5C "Click to enlarge")

#### API Description

The following table describes static map APIs. The static map function is mainly provided by methods in the [staticMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap) namespace. For more information about the APIs, please refer to [staticMap (Static Map)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[StaticMapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1555293218278)

 | 

Static map attributes.

 |
| 

[getMapImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1117619561413)(options: [StaticMapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1555293218278)): Promise<[image.PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)\>

 | 

Creates a static map based on the provided parameters.

 |
| 

[getMapImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1068516421577)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), options: [StaticMapOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1555293218278)): Promise<[image.PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)\>

 | 

Creates a static map based on the provided parameters. The context can be passed.

 |

#### Development Procedure

1.  Import required modules.
    
    import { staticMap } from '@kit.MapKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create static map initialization parameters. Call the [getMapImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-staticmap#section1117619561413) method to obtain a static map. The result is shown in the following figure.
    
    @Entry
    @Component
    struct StaticMapDemo {
      @State image?: PixelMap = undefined;
    
      build() {
        Column() {
          this.buildDemoUI();
        }.width('100%')
        .margin({ bottom: 48 })
        .backgroundColor(0xf2f2f2)
        .height('100%')
      }
    
      @Builder
      buildDemoUI() {
        // Display the obtained static map.
        Image(this.image)
          .width('100%')
          .fitOriginalSize(false)
          .border({ width: 1 })
          .borderStyle(BorderStyle.Dashed)
          .objectFit(ImageFit.Contain)
          .height("90%")
    
        Row() {
          Button("getStaticMap")
            .fontSize(12)
            .onClick(async () => {
              // Set Markers of the static map. 
              let markers: Array<staticMap.StaticMapMarker> = \[{
                location: {
                  latitude: 50,
                  longitude: 126.3
                },
                font: 'statics',
                defaultIconSize: staticMap.IconSize.TINY
              }\];
    
              // Set the static map drawing path.
              let path: staticMap.StaticMapPath = {
                locations: \[
                  {
                    latitude: 50,
                    longitude: 126
                  },
                  {
                    latitude: 50.3,
                    longitude: 126
                  },
                  {
                    latitude: 50.3,
                    longitude: 126.3
                  },
                  {
                    latitude: 49.7,
                    longitude: 126
                  },
                  {
                    latitude: 50,
                    longitude: 126
                  }
                \],
                width: 3
              };
    
              // Assemble static map parameters. 
              let option: staticMap.StaticMapOptions = {
                location: {
                  latitude: 50,
                  longitude: 126
                },
                zoom: 10,
                imageWidth: 1024,
                imageHeight: 1024,
                scale: 1,
                markers: markers,
                path: path
              };
    
              try {
              // Obtain the static map.
                this.image = await staticMap.getMapImage(option);
                console.info("Succeeded in getting image.");
              } catch (error) {
                const err: BusinessError = error as BusinessError;
                console.error(\`Failed in getting image, code: ${err.code}, message: ${err.message}\`);
              }
            })
        }.margin({ top: 12 })
      }
    }
    
    **Figure 2** Calling the getMapImage method to obtain a static map  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8dMqRGb6RmCyEJwWw57UfA/en-us_image_0000002517200111.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D054AC447469A53CA5324A4812D136AA7665F368C714B1E944F2422940E608A "Click to enlarge")
