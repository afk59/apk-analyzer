# Setting the Overlay Order of Map Elements

#### Use Cases

This section describes how to set the overlay order of map elements.

Set the display order of map elements from bottom to top, so that later elements will cover earlier ones.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/BNxPcU0PTluelonYxWPhnA/en-us_image_0000002545994257.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A300FFF91D7AC8096E7E60FA51056F3AAFF7F26568FB068FCF0F6BF89BF089B "Click to enlarge")

**Table 1** Layering order of map elements
| 
Enumerations

 | 

Enumerated Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

OVERLAY

 | 

1

 | 

Overlays, including the [MapCircle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcircle#section46461317478), [MapPolygon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolygon), [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline), [MapArc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-maparc), [ImageOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-imageoverlay), and [TraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-traceoverlay).

 |
| 

POI

 | 

2

 | 

Base map [POI](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section1155919456273)s.

 |
| 

CUSTOM\_POI

 | 

3

 | 

Overlays that support collision, including the [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) and [Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble).

 |
| 

MARKER

 | 

4

 | 

Markers, including the [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker) and [ClusterOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-clusteroverlay).

 |

#### API Description

The function of setting the layering order of map elements is provided by [MapElementType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17215821103111) and [setDisplayOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section10934934202319). For more information about the APIs, please refer to [setDisplayOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section10934934202319).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.MapElementType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17215821103111)

 | 

Map element type.

 |
| 

[setDisplayOrder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section10934934202319)(types: Array<[mapCommon.MapElementType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section17215821103111)\>): void

 | 

Sets the layering order of map elements.

 |

#### Development Procedure

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Set the overlay order of map elements.
    
    @Entry
    @Component
    struct MarkerDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapEventManager?: map.MapEventManager;
      private marker?: map.Marker;
      private bubble?: map.Bubble;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.984410259206815,
              longitude: 118.26625379397866
            },
            zoom: 10
          }
        };
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            this.mapEventManager = this.mapController.getEventManager();
            // Marker initialization parameters.
            let markerOptions: mapCommon.MarkerOptions = {
              position: {
                latitude: 31.984410259206815,
                longitude: 118.26625379397866
              },
              rotation: 0,
              visible: true,
              zIndex: 0,
              alpha: 1,
              anchorU: 0.5,
              anchorV: 1,
              clickable: true,
              draggable: true,
              flat: false
            };
            // Create a Marker.
            try {
              this.marker = await this.mapController.addMarker(markerOptions);
            } catch (e) {
              console.error(\`Failed to create the Marker. code: ${e.code}; message: ${e.message}\`);
            }
            let bubbleOptions: mapCommon.BubbleParams = {
              // Bubble position. 
              positions: \[\[{
                latitude: 32.384410259206815,
                longitude: 118.26625379397866
              }\]\],
              // Set icons. Icons for four directions must be provided and stored in **resources/rawfile**. 
              icons: \[
                'speed\_limit\_10.png',
                'speed\_limit\_20.png',
                'speed\_limit\_30.png',
                'speed\_limit\_40.png'
              \],
              // Define the display attribute of the Bubble. If it is set to **true**, the Bubble remains visible after collision. 
              forceVisible: true,
              // Define the Bubble collision priority. A larger value indicates a lower priority.
              priority: 3,
              // Define the minimum zoom level for Bubble display. 
              minZoom: 2,
              // Define the maximum zoom level for Bubble display. 
              maxZoom: 20,
              // Define whether the Bubble is visible.
              visible: true,
              // Define the overlay level attribute of the Bubble. 
              zIndex: 1
            }
            // Add a Bubble.
            try {
              this.bubble = await this.mapController.addBubble(bubbleOptions);
            } catch (e) {
              console.error(\`Failed to create the Bubble. code: ${e.code}; message: ${e.message}\`);
            }
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
              // Image of the ImageOverlay.
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
              await this.mapController?.addImageOverlay(imageOverlayParams);
            } catch (e) {
              console.error(\`Failed to create the ImageOverlay. code: ${e.code}; message: ${e.message}\`);
            }
    
            // Set the elements in the following order: overlays at the bottom layer, followed by POIs, overlays that support collision, and markers at the topmost. 
            let mapElementTypeArr: Array<mapCommon.MapElementType> = \[
              mapCommon.MapElementType.OVERLAY,
              mapCommon.MapElementType.POI,
              mapCommon.MapElementType.CUSTOM\_POI,
              mapCommon.MapElementType.MARKER\];
            this.mapController.setDisplayOrder(mapElementTypeArr);
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        }
      }
    
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
          }.width('100%')
        }.height('100%')
      }
    }
