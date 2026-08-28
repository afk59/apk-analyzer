# Bubble

#### Use Cases

This section describes how to add a Bubble to a specified position on a map.

You can use Bubbles to show speed and congestion information at a specified location on a road. This function allows you to:

-   Set icons for four directions. (The icons must have the same height and width.)
-   Set the icon collision rule.
-   Set the candidate coordinates segment for a Bubble, so that the Bubble can be displayed on the optimal position on the road after calculation.
-   Set the icon animation.
-   Add tap events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/pb-lrUweQiCZQ45j9FKF8g/en-us_image_0000002545988885.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B794708AB38CB1BEB8CB444FFED40D0B9A81AEFE97C58C12930D237858D5C6F1 "Click to enlarge")

#### API Description

The Bubble adding function is mainly provided by [BubbleParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section10348735114315), [addBubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1732020231338), and [Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble). For more information about the APIs, please refer to [Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[BubbleParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section10348735114315)

 | 

Bubble parameters.

 |
| 

[addBubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section1732020231338)(params: [mapCommon.BubbleParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section10348735114315)): Promise<[Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble)\>

 | 

Adds a Bubble on the map.

 |
| 

[Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble)

 | 

Bubble. This API supports updating and querying Bubble attributes.

 |

#### Development Procedure

## Add a Bubble.

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a Bubble. Create initialization parameters in the **callback** method, and create a Bubble.
    
    @Entry
    @Component
    struct BubbleDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private bubble?: map.Bubble;
    
      aboutToAppear(): void {
        this.mapOptions = {
          position: {
            target: {
              latitude: 39.918,
              longitude: 116.397
            },
            zoom: 14
          }
        };
    
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
            let bubbleOptions: mapCommon.BubbleParams = {
              // Bubble position. 
              positions: \[\[{ 
                latitude: 39.918,
                longitude: 116.397
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/kVfF2Q2ESgqcl-E65jJWrw/en-us_image_0000002546029131.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C45AFFD721C9E260FCCAD4158B5C82F7EAD49288A1CBD98DEF7D87A315568D52 "Click to enlarge")
    

## Setting a Listener for Bubble Tap Events

let callback = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback bubble = ${bubble.getId()}\`);
};
this.mapController?.on("bubbleClick", callback);

## Setting an Animation for a Bubble

[Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble) calls [setAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-basepriorityoverlay#section688810310374) to set the animation.

[Bubble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-bubble) calls [startAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-basepriorityoverlay#section15532754163419) to start the animation.

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
this.bubble.setAnimation(animation);
this.bubble.startAnimation();
