# TraceOverlay

#### Use Cases

This section describes how to draw a TraceOverlay on a map.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/VvVGam-EQ9ev1NoqwYs6eQ/en-us_image_0000002514550246.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35DF5DDCA24393D76079DCC31F619E213BBB97EA772721F8E43E0246164B32F2 "Click to enlarge")

#### API Description

The TraceOverlay drawing function is provided by [TraceOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section202444375510), [addTraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section188905329242), [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker#section166747193469), and [TraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-traceoverlay). For more information about the APIs, please refer to [TraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-traceoverlay).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[TraceOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section202444375510)

 | 

TraceOverlay parameters.

 |
| 

[addTraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section188905329242)(params: [mapCommon.TraceOverlayParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section202444375510), markers?: Array<[Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker#section166747193469)\>): Promise<[TraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-traceoverlay)\>

 | 

Draws a TraceOverlay.

 |
| 

[Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker#section166747193469)

 | 

A group of TraceOverlay markers.

 |
| 

[TraceOverlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-traceoverlay)

 | 

TraceOverlay. This API supports functions including pausing and deleting TraceOverlays.

 |

#### Development Procedure

1.  Import required modules.
    
    import { mapCommon, map, MapComponent } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Draw a TraceOverlay.
    
    @Entry
    @Component
    struct TraceOverlayDemo {
      private TAG = "OHMapSDK\_TraceOverlayDemo";
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.99227173519985,
              longitude: 118.7622219990476
            },
            zoom: 16
          },
          scaleControlsEnabled: true
        }
    
        this.callback = async (err, mapController) => {
          console.info(this.TAG, "mapCallback err=" + JSON.stringify(err) +
            "; mapController=" + JSON.stringify(mapController));
          if (!err) {
            this.mapController = mapController;
            // Parameters of Marker1. 
            let markerOptions1: mapCommon.MarkerOptions = {
              position: {
                latitude: 31.99227173519985,
                longitude: 118.7622219990476
              },
              icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
              anchorU: 0.5,
              anchorV: 1,
              visible: true
            };
            // Create Marker 1. 
            let markerBoy1 = await this.mapController.addMarker(markerOptions1);
            let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
            boyImages1.setDuration(1000);
            let resourceArray: Array<Resource> = new Array();
            // Replace the resource images with your own ones. Save your images in the **resources/base/media** directory.
            resourceArray.push($r("app.media.side\_0"));
            resourceArray.push($r("app.media.side\_1"));
            resourceArray.push($r("app.media.side\_2"));
            resourceArray.push($r("app.media.side\_3"));
            resourceArray.push($r("app.media.side\_4"));
            resourceArray.push($r("app.media.side\_5"));
            resourceArray.push($r("app.media.side\_6"));
            resourceArray.push($r("app.media.side\_7"));
            resourceArray.push($r("app.media.side\_8"));
            resourceArray.push($r("app.media.side\_9"));
            resourceArray.push($r("app.media.side\_10"));
            resourceArray.push($r("app.media.side\_11"));
            resourceArray.push($r("app.media.side\_12"));
            resourceArray.push($r("app.media.side\_13"));
            resourceArray.push($r("app.media.side\_14"));
            resourceArray.push($r("app.media.side\_15"));
            resourceArray.push($r("app.media.side\_16"));
            resourceArray.push($r("app.media.side\_17"));
            resourceArray.push($r("app.media.side\_18"));
            resourceArray.push($r("app.media.side\_19"));
            resourceArray.push($r("app.media.side\_20"));
            await boyImages1.addImages(resourceArray);
            boyImages1.setRepeatCount(-1);
    
            // Add an animation for Marker 1. 
            markerBoy1.setAnimation(boyImages1);
            markerBoy1.startAnimation();
    
            // Parameters of Marker 2. 
            let markerOptions2: mapCommon.MarkerOptions = {
              position: {
                latitude: 31.99227173519985,
                longitude: 118.7622219990476
              },
              icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
              anchorU: 0.5,
              anchorV: 1,
              visible: false
            };
            // Create Marker 2.
            let markerBoy2 = await this.mapController.addMarker(markerOptions2);
            let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
            boyImages2.setDuration(1000);
            let resourceArray2: Array<Resource> = new Array();
            // Replace the resource images with your own ones. Save your images in the **resources/base/media** directory.
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_000"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_001"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_002"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_003"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_004"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_005"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_006"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_007"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_008"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_009"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_010"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_011"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_012"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_013"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_014"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_015"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_016"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_017"));
            resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_018"));
            await boyImages2.addImages(resourceArray2);
            boyImages2.setRepeatCount(-1);
            // Add an animation for Marker 2. 
            markerBoy2.setAnimation(boyImages2);
            markerBoy2.startAnimation();
    
            let points: Array<mapCommon.LatLng> = new Array();
            points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
            points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
            points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
            points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
            points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
            points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
            points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
            points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
            points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
            points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
            points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
            points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
            points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
            points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
            points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
            points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
            points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
            points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
            points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
            points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
            points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
            points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
            points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
            points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
            points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });
    
            // Input parameters of the TraceOverlay. 
            let traceOptions: mapCommon.TraceOverlayParams = {
              // Trajectory points. 
              points: points,
              // Trajectory animation duration. 
              animationDuration: 5000,
              // Indicates whether the camera follows the animation path.
              isMapMoving: true,
              // Trajectory color. 
              color: 0xAAFFAA00,
              // Trajectory width.
              width: 20,
              // Trajectory animation callback (index for trajectory point callback).
              animationCallback: (pointIndex) => {
                // Change to cycling.
                if (pointIndex === 10) {
                  markerBoy1.setVisible(false);
                  markerBoy2.setVisible(true);
                }
              }
            }
            let markers: Array<map.Marker> = new Array();
            markers.push(markerBoy1, markerBoy2);
            // Add a trajectory point animation.
            try {
              let traceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);
            } catch (e) {
              console.error(\`Failed to create the TraceOverlay. code: ${e.code}; message: ${e.message}\`);
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
