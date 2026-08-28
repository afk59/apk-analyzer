# ClusterOverlay

#### Use Cases

This section describes how to implement clustering based on map data.

You can zoom to adapt the clustering effect. The clustering icon can be tapped. This function supports the following capabilities:

-   Cluster ClusterItems by distance.
-   Draw the default icon of a ClusterOverlay.
-   Draw a [custom icon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section252017318496) for a ClusterOverlay.
-   Listen for tap events of a ClusterOverlay.
-   Add a single ClusterItem to a ClusterOverlay.
-   Delete ClusterOverlays.
-   Redraw ClusterOverlays when the map is moved.

Starting from 5.0.3(15), the function of listening for ClusterOverlay tap events is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/PZgggxOEQUOwY1KWd-P9Yg/en-us_image_0000002514389600.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CA09A62AA0C20AFFA64F6F9BA2258E32B11104B29F0C37D55A39BF504E2401A "Click to enlarge")

#### API Description

The ClusterOverlay function is mainly provided by [ClusterOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section693971514320), [addClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section879947112414), and [ClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-clusteroverlay). For more information about the APIs, please refer to [ClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-clusteroverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[ClusterOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section693971514320)

 | 

ClusterOverlay parameters.

 |
| 

[addClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section879947112414)(params: [mapCommon.ClusterOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section693971514320)): Promise<[ClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-clusteroverlay)\>

 | 

Clustering API, which supports the ClusterOverlay capability.

 |
| 

[ClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-clusteroverlay)

 | 

ClusterOverlay. This API supports updating and querying ClusterOverlay attributes.

 |

#### Development Procedure

1.  Import required modules.
    
    import { map, mapCommon, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a ClusterOverlay.
    
    @Entry
    @Component
    struct ClusterOverlayDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
    
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.98,
              longitude: 118.7
            },
            zoom: 7
          }
        }
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            // Generate items to be clustered.
            let clusterItem1: mapCommon.ClusterItem = {
              position: {
                latitude: 31.98,
                longitude: 118.7
              }
            };
            let clusterItem2: mapCommon.ClusterItem = {
              position: {
                latitude: 32.99,
                longitude: 118.9
              }
            };
            let clusterItem3: mapCommon.ClusterItem = {
              position: {
                latitude: 31.5,
                longitude: 118.7
              }
            };
            let clusterItem4: mapCommon.ClusterItem = {
              position: {
                latitude: 30,
                longitude: 118.7
              }
            };
            let clusterItem5: mapCommon.ClusterItem = {
              position: {
                latitude: 29.98,
                longitude: 117.7
              }
            };
            let clusterItem6: mapCommon.ClusterItem = {
              position: {
                latitude: 31.98,
                longitude: 120.7
              }
            };
            let clusterItem7: mapCommon.ClusterItem = {
              position: {
                latitude: 25.98,
                longitude: 119.7
              }
            };
            let clusterItem8: mapCommon.ClusterItem = {
              position: {
                latitude: 30.98,
                longitude: 110.7
              }
            };
            let clusterItem9: mapCommon.ClusterItem = {
              position: {
                latitude: 30.98,
                longitude: 115.7
              }
            };
            let clusterItem10: mapCommon.ClusterItem = {
              position: {
                latitude: 28.98,
                longitude: 122.7
              }
            };
            let array: Array<mapCommon.ClusterItem> = \[
              clusterItem1,
              clusterItem2,
              clusterItem3,
              clusterItem4,
              clusterItem5,
              clusterItem6,
              clusterItem7,
              clusterItem8,
              clusterItem9,
              clusterItem10
            \]
            for(let index = 0; index < 100; index++){
              array.push(clusterItem1)
            }
            for(let index = 0; index < 10; index++){
              array.push(clusterItem2)
            }
            // Generate the input parameters of the ClusterOverlay. Set the cluster distance to 100 vp.
            let clusterOverlayParams: mapCommon.ClusterOverlayParams = { 
              distance: 100,
              clusterItems: array
            };
            try {
              // Call **addClusterOverlay** to generate a ClusterOverlay.
              await this.mapController.addClusterOverlay(clusterOverlayParams);
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
              .height('100%');
          }.width('100%')
        }.height('100%')
      }
    }
    
3.  Listen for ClusterOverlay tap events.
    
    let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
      console.info("markerClusterClick", \`callback1 markerClusterInfo\`);
    };
    // Add listening.
    clusterOverlay.on("markerClusterClick", callback1);
    // Cancel listening. 
    clusterOverlay.off("markerClusterClick", callback1);
