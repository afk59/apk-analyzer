# PointAnnotation

#### Use Cases

This section describes how to add PointAnnotations to a map to identify locations such as stores and buildings, and provide location details with information windows.

This function allows you to:

-   Set icons, texts, and collision rule.
-   Add tap events.

A [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) has a default style and can be customized. The following describes some basic functions. For details about other functions, please refer to [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/b98p4wT1QSOz2l9ZZUONZQ/en-us_image_0000002514547962.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4BCB55A17E88EE1D19E97984A7699C386261690A9007EF06FA94D3F86D606DC "Click to enlarge")

#### API Description

The PointAnnotation adding function is mainly provided by [PointAnnotationParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section161194598375), [addPointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1899064804520), [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation), [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section636111479397), and [off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section5365154710393). For more information about the APIs, please refer to [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[PointAnnotationParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section161194598375)

 | 

PointAnnotation parameters.

 |
| 

[addPointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1899064804520)(params: [mapCommon.PointAnnotationParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section161194598375)): Promise<[PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation)\>

 | 

Adds a PointAnnotation on the map.

 |
| 

[PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation)

 | 

PointAnnotation. This API supports updating and querying PointAnnotation attributes.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section636111479397)(type: 'pointAnnotationClick', callback: Callback<[PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation)\>): void

 | 

Sets a listener for PointAnnotation tap events.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section5365154710393)(type: 'pointAnnotationClick', callback?: Callback<[PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation)\>): void

 | 

Cancels listening for PointAnnotation tap events.

 |

#### Development Procedure

## Adding a PointAnnotation

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a PointAnnotation. Create initialization parameters in the **callback** method, and create a PointAnnotation.
    
    @Entry
    @Component
    struct PointAnnotationDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapEventManager?: map.MapEventManager;
      private pointAnnotation?: map.PointAnnotation;
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 32.020750,
              longitude: 118.788765
            },
            zoom: 14
          }
        };
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            this.mapEventManager = this.mapController.getEventManager();
            let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
              // Define the anchor for the icon of a PointAnnotation.
              position: {
                latitude: 32.020750,
                longitude: 118.788765
              },
              // Define whether to support deduplication when the PointAnnotation name is the same as a map POI name.
              repeatable: true,
              // Define the collision rule of the PointAnnotation. 
              collisionRule: mapCommon.CollisionRule.NAME,
              // Define PointAnnotation titles. The minimum length of the array is 1 and the maximum length is 3.
              titles: \[{
                // Define the title content.
                content: "Nanjing Confucius Temple",
                // Define the title text color.
                color: 0xFF000000,
                // Define the title text font size.
                fontSize: 15,
                // Define the title stroke color.
                strokeColor: 0xFFFFFFFF,
                // Define the title stroke width.
                strokeWidth: 2,
                // Define the title text font style.
                fontStyle: mapCommon.FontStyle.ITALIC
              }\],
              // Define an icon for the PointAnnotation. The icon is stored in **resources/rawfile**.
              icon: "",
              // Define whether to display the icon for the PointAnnotation. 
              showIcon: true,
              // Define the horizontal position of the anchor of the PointAnnotation. 
              anchorU: 0.5,
              // Define the vertical position of the anchor of the PointAnnotation. 
              anchorV: 1,
              // Define the display attribute of the PointAnnotation. If it is set to **true**, the PointAnnotation remains visible after collision. 
              forceVisible: false,
              // Define the collision priority. A larger value indicates a lower priority.
              priority: 3,
              // Define the minimum zoom level for PointAnnotation display. 
              minZoom: 2,
              // Define the maximum zoom level for PointAnnotation display. 
              maxZoom: 20,
              // Define whether the PointAnnotation is visible.
              visible: true,
              // Define the overlay level attribute of the PointAnnotation.
              zIndex: 10
            }
    
            // Create a PointAnnotation.
            try {
              this.pointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
            } catch (e) {
              console.error(\`Failed to create the PointAnnotation. code: ${e.code}; message: ${e.message}\`);
            }
          } else {
            console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
          }
        };
      }
      build() {
        Stack() {
          Column() {
            MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
          }.width('100%')
        }.height('100%')
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/nWAyENveTCaaLY4rEoy4Pw/en-us_image_0000002511015340.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1E246079AA22F7D9270C45EF72D4A013FDC6E6524F5E9FD7EBDCBFBC78743C0 "Click to enlarge")
    
3.  Modify the attributes of the PointAnnotation.
    
    // Set the zoom level of the PointAnnotation to a value ranging from 3 to 14.
    this.pointAnnotation.setZoom(3,14);
    // Set the collision priority of the PointAnnotation to **10**.
    this.pointAnnotation.setPriority(10);
    

## Setting a Listener for PointAnnotation Tap Events

let callback = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`pointAnnotationClick: ${pointAnnotation.getId()}\`);
};
this.mapEventManager.on("pointAnnotationClick", callback);

## Setting an Animation for a PointAnnotation

Call the [setAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-basepriorityoverlay#section688810310374) method of [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) to set the animation.

Call the [startAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-basepriorityoverlay#section15532754163419) method of [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) to start the animation.

let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
// Set the duration of a single animation.
animation.setDuration(3000);
// Set a listener for animation start events.
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
animation.on("animationStart", callbackStart);
// Set a listener for animation end events. 
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationEnd", callbackEnd);
// Set the status after the animation ends.
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
// Set the animation replay mode.
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
// Set an animation interpolator.
animation.setInterpolator(Curve.Linear);
// Set the number of times the animation is replayed.
animation.setRepeatCount(100);
this.pointAnnotation.setAnimation(animation);
this.pointAnnotation.startAnimation();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/vAwMJ2QiRgCrZ0_yXZPcQg/en-us_image_0000002510855542.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A14FB65EF0A078E6E01809DA78BA386D139584E7EF982CE05FF48ABA12F5B03E "Click to enlarge")

## Setting an Animation for the PointAnnotation Title

Call the [setTitleAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation#section884818504399) method of [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) to set the title animation.

Call the [startTitleAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation#section108531150183916) method of [PointAnnotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-pointannotation) to start the title animation.

let animation: map.FontSizeAnimation = new map.FontSizeAnimation(15, 45);
// Set the duration of a single animation.
animation.setDuration(3000);
// Set a listener for animation start events.
let callbackStart = () => {
  console.info("animationStart", \`callback\`);
};
animation.on("animationStart", callbackStart);
// Set a listener for animation end events. 
let callbackEnd = () => {
  console.info("animationEnd", \`callback\`);
};
animation.on("animationEnd", callbackEnd);
// Set the status after the animation ends.
animation.setFillMode(map.AnimationFillMode.FORWARDS);
// Set the animation replay mode.
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
// Set an animation interpolator.
animation.setInterpolator(Curve.Linear);
// Set the number of times the animation is replayed.
animation.setRepeatCount(100);
this.pointAnnotation.setTitleAnimation(animation);
this.pointAnnotation.startTitleAnimation();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/YZWsDfJEQoqE0eaX4Y6uWg/en-us_image_0000002542464547.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6013C8F94DC5E20513A210B6B656E2DADBC58B56C146C3D5AACF4B16EC5621E8 "Click to enlarge")
