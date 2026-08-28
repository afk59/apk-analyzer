# MassPointOverlay

#### Use Cases

A MassPointOverlay can be added for bulk display of point data. The MassPointOverlay can process a wide range of points, from dozens to hundreds of thousands. This section describes how to draw a MassPointOverlay on a map.

Starting from 6.0.0(20), the MassPointOverlay function is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/zB9ONnJjTMu45OBCtqiE9w/en-us_image_0000002545996415.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=340EBEF2FC443ACAB9D6047BD6A5808B94DDBE2028BD8CEE2C1C1E4CC162E9B5 "Click to enlarge")

#### API Description

The MassPointOverlay functions are mainly provided by [MassPointOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1423475535919), [addMassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section18441352614), and [MassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-masspointoverlay). For more information about the APIs, please refer to [MassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-masspointoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MassPointOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1423475535919)

 | 

MassPointOverlay parameters.

 |
| 

[addMassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section18441352614)(params: mapCommon.[MassPointOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1423475535919)): Promise<[MassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-masspointoverlay)\>

 | 

Adds a MassPointOverlay.

 |
| 

[MassPointOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-masspointoverlay)

 | 

MassPointOverlay object.

 |

#### Development Procedure

## Adding a MassPointOverlay

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Draw a MassPointOverlay.
    
    @Entry
    @Component
    struct MassPointOverlayDemo {
      private TAG = 'OHMapSDK\_MassPointOverlayDemo';
      private mapOption?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private massPointOverlay?: map.MassPointOverlay;
      @State currentTimestamp: number = 0;
      @State mapHeight: string = '65%'
      @State mapWidth: string = '100%'
      aboutToAppear(): void {
        this.mapOption = {
          position: {
            target: {
              latitude: 32.11111,
              longitude: 118.11111
            },
            zoom: 9
          },
          scaleControlsEnabled: true
        }
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let items: mapCommon.MassPointItem\[\] = \[\];
            for (let i = 0; i < 1000; i++) {
              // Save mass points to **items**.
              items.push({
                itemId: 'test' + i,
                position: {
                  longitude: 118.11111 + Math.random() \* 1 - 0.5,
                  latitude: 32.11111 + Math.random() \* 1 - 0.5
                },
                snippet: 'test' + i,
                title: 'test' + i
              })
            }
            let params: mapCommon.MassPointOverlayParams = {
              id: 'test',
              items: items,
              // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file within the **rawfile** folder.
              icon: 'icon/maps\_blue\_dot.png'
            }
            try {
              this.massPointOverlay = await this.mapController?.addMassPointOverlay(params);
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
            MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback, })
              .width(this.mapWidth)
              .height(this.mapHeight);
          }.width('100%')
        }.height('100%')
      }
    }
    

## MassPointOverlay Tap Events

// Initialize the event listener manager of the map component.
let mapEventManager = this.mapController?.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(\`overlayId:${overlay.getId()},item :${JSON.stringify(item)}\`);
}
// Start listening for MassPointOverlay tap events.
mapEventManager.on('massPointOverlayClick', massCallback);
// Stop specific listening for MassPointOverlay tap events by passing the corresponding callback.
mapEventManager.off('massPointOverlayClick', massCallback);
// Stop all listening for MassPointOverlay tap events. No callback needs to be passed.
mapEventManager.off('massPointOverlayClick');
