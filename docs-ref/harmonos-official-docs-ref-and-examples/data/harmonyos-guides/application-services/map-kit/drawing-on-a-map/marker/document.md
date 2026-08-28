# Marker

#### Use Cases

This section describes how to add Markers to specified locations on a map to identify locations such as stores and buildings.

Markers are used to mark any location in the map, such as the user location, vehicle location, and store location. The Marker function provided by Map Kit encapsulates a large number of triggering events, such as tap events, long-press events, and drag events.

Markers have default styles and can be customized. Given the extensive feature set, the following only showcases the use of a few fundamental functions.

Starting from 5.1.1(19), the function of controlling the visibility of the Marker text is supported.

Starting from 6.0.0(20), the function of generating a Marker icon through a custom component is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/VOcNCtAkT1aab63JN58kCg/en-us_image_0000002545851145.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7F4914FC5FE690988D269BAC251D81B5516D7792CE22D14F87A6C0E9BFC301C "Click to enlarge")

#### API Description

The Marker adding function is mainly provided by [MarkerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section559041743210), [addMarker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section0810361284), and [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker). For more information about the APIs, please refer to [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MarkerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section559041743210)

 | 

Marker parameters.

 |
| 

[addMarker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section0810361284)(options: [mapCommon.MarkerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section559041743210)): Promise<[Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker)\>

 | 

Adds a Marker on the map.

 |
| 

[Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker)

 | 

Marker. This API supports updating and querying Marker attributes.

 |

#### Development Procedure

## Adding Markers

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a Marker. Create initialization parameters in the **callback** method, and create a [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker).
    
    @Entry
    @Component
    struct MarkerDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapEventManager?: map.MapEventManager;
      private marker?: map.Marker;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.984410259206815,
              longitude: 118.76625379397866
            },
            zoom: 15
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
                longitude: 118.76625379397866
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/IZggKVLiRveBgnzYKbgtRQ/en-us_image_0000002545972659.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4379CCBAB3199F0F105807A99289548E928B06B405840D716EC528C16E08453E "Click to enlarge")
    
3.  Modify the attributes of the added Marker.
    
    // Set the Marker so that it can be dragged.
    this.marker.setDraggable(true);
    // Set the Marker anchor.
    this.marker.setMarkerAnchor(1.0, 1.0);
    

## Customizing a Marker

Change the default Marker icon to a custom icon in [MarkerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section559041743210).

let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file within the **rawfile** folder.
  icon: 'test.png'
};
this.marker = await this.mapController.addMarker(markerOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/wjp6vC_8QOOC3Gb18JB14g/en-us_image_0000002545974245.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B50FDEE106C80DA539C5D4738C8A5366F515DD062A1B9B5E36AEE11EDB5BFA04 "Click to enlarge")

## Controlling the Visibility of the Marker Text

You can use the [setAnnotationVisible](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker#section6403556152318) method to control the visibility of the Marker text and use the [isAnnotationVisible](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker#section7880311173111) method to obtain its visibility status.

// Marker initialization parameters.
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  annotations: \[{
    // Define the title content.
    content: "text",
    fontStyle: 1,
    strokeWidth: 3,
    fontSize: 15
  }\]
};
// Create a Marker.
this.marker = await this.mapController.addMarker(markerOptions);
// Hide the Marker text
this.marker.setAnnotationVisible(false);
// Check whether the Marker text is visible.
let isAnnotationVisible: boolean = this.marker.isAnnotationVisible();
console.info(\`isAnnotationVisible is: \` + isAnnotationVisible);

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Before hiding the Marker text</span></div></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>After hiding the Marker text</span></div></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><span><img height="843.324405" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/-4IrUNkKQjySL0bTG6nNMg/en-us_image_0000002514536924.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=77C4000D586C890CD6BC66413BA997C12253C476531D9728663C6CD2EFE8B647" title="Click to enlarge" width="381.48190500000004"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p><span><img height="842.3199890000001" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/0JH1QH-uS1qph9nCzpAvUQ/en-us_image_0000002546016921.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=033C46EBBB77493C8B8CFA0A15EBF5BD9BAE726E6ACE05708D24A74E437E4C7F" title="Click to enlarge" width="381.045"></span></p></td></tr></tbody></table>

## Collision Detection

You can configure the Marker's collision rule by setting the **collisionRule** attribute in [MarkerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section559041743210).

let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  rotation: 0,
  visible: true,
  zIndex: 0,
  alpha: 1,
  anchorU: 0.5,
  anchorV: 1,
  clickable: true,
  draggable: true,
  flat: false,
  // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file within the **rawfile** folder.
  icon: 'icon.png',
  annotations:  \[{
    // Define the title content.
    content: "Test",
    fontStyle: 1,
    strokeWidth: 3,
    fontSize: 15
  }\],
  // Configure the collision rule to include icons and their name labels in collision detection.
  collisionRule: mapCommon.CollisionRule.ALL,
  annotationPosition: mapCommon.TextPosition.TOP
};
this.marker = await this.mapController.addMarker(markerOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/oEOrSeRAQPq38C67bPKvYg/en-us_image_0000002546018089.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E3805F81BFBCE578FEB2538BACC8877FDF0C3E5FFFA83B699EA2455B63B0077 "Click to enlarge")

## Setting a Listener for Marker Tap Events

let callback = (marker: map.Marker) => {
  console.info(\`on-markerClick marker = ${marker.getId()}\`);
};
this.mapEventManager.on("markerClick", callback);

## Setting a Listener for Marker Drag Events

To listen for Marker drag events, perform the following steps:

1.  Set the drag attribute of a [Marker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-marker) to **true**.
2.  Call the [on(type: 'markerDragStart' , callback: Callback<Marker>)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section19294747123912) method to listen for the Marker drag start event.
3.  Call the [on(type: 'markerDrag' , callback: Callback<Marker>)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section103026476395) method to listen for the Marker drag process.
4.  Call the [on(type: 'markerDragEnd' , callback: Callback<Marker>)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapeventmanager#section13310124719393) method to listen for the Marker drag end event.

// Set the Marker so that it can be dragged.
this.marker.setDraggable(true);

// Listen for Marker drag start events.
let markerCallback = (marker: map.Marker) => {
  console.info(\`on-markerDragStart marker = ${marker.getId()}\`);
};
this.mapEventManager.on("markerDragStart", markerCallback);

// Listen for Marker drag events.
let markerDragCallback = (marker: map.Marker) => {
  console.info(\`on-markerDrag marker = ${marker.getId()}\`);
};
this.mapEventManager.on("markerDrag", markerDragCallback);

// Listen for Marker drag end events.
let markerDragEndCallback = (marker: map.Marker) => {
  console.info(\`on-markerDragEnd marker = ${marker.getId()}\`);
};
this.mapEventManager.on("markerDragEnd", markerDragEndCallback);

## Adding an Information Window

// Add an information window. 
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  }
};
this.marker = await this.mapController?.addMarker(markerOptions);
// Set the title of the information window.
this.marker.setTitle ('Nanjing');
// Set the subtitle of the information window.
this.marker.setSnippet('East China');
// Set the Marker to be tappable.
this.marker.setClickable(true);
// Set the anchor location of the information window.
this.marker.setInfoWindowAnchor(1, 1);
// Set the information window to be visible. The information window will be displayed after the Marker is tapped.
this.marker.setInfoWindowVisible(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/UdA1QTm3SRaBEKeJNk64gw/en-us_image_0000002542367861.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5455B9E76A98B692FF28D0FACF5065992157E45F06714A2C51E37068B23C1F8 "Click to enlarge")

## Customizing an Information Window

@Entry
@Component
struct MarkerDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.120750,
          longitude: 118.788765
        },
        zoom: 15
      }
    }

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.120750,
            longitude: 118.788765
          },
          clickable: true,
          // Set the information window title. The information window will be displayed after the Marker is tapped.
          title: "Marker"
        };
        await this.mapController?.addMarker(markerOptions);
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
          // Customize an information window.
          customInfoWindow: this.customInfoWindow
        })
          .width('100%')
          .height('100%');
      }.width('100%')
    }.height('100%')
  }
  // Custom information window BuilderParam.
  @BuilderParam customInfoWindow: ($$: map.MarkerDelegate) => void = this.customInfoWindowBuilder;
  // Custom information window Builder.
  @Builder
  customInfoWindowBuilder($$: map.MarkerDelegate) {
    if ($$.marker) {
      Text($$.marker.getTitle())
        .width("50%")
        .height(50)
        .backgroundColor(Color.Green)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .font({ size: 25, weight: 10, style: FontStyle.Italic })
        .border({ width: 3, color: Color.Black, radius: 25, style: BorderStyle.Dashed })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5Sd11c4LQzeyyx1Q9DWnbw/en-us_image_0000002542447915.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B20AC6AEB2158B348F9FAA9D5D0E30FAD48D29BAE534237B4A1AF9F500BB11E3 "Click to enlarge")

## Setting an Animation for a Marker

Markers support rotation, scaling, panning, transparency, image animation playback, and combined animation effects.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[AlphaAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-alphaanimation)

 | 

Animation class for controlling transparency.

 |
| 

[RotateAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-rotateanimation)

 | 

Animation class for controlling rotation.

 |
| 

[ScaleAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-scaleanimation)

 | 

Animation class for controlling scaling.

 |
| 

[TranslateAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-translateanimation)

 | 

Animation class for controlling panning.

 |
| 

[PlayImageAnimation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-playimageanimation)

 | 

Animation class that controls multiple images.

 |
| 

[AnimationSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-animationset)

 | 

Animation set.

 |

The sample code for the rotation animation effect is as follows:

import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MarkerDemo {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.020750,
          longitude: 118.788765
        },
        zoom: 11
      }
    }

    this.callback = async (err, mapController) => {
      if (!err) {
        // Build a **MarkerOptions** object.
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.020750,
            longitude: 118.788765
          }
        };
        // Create a Marker.
        let marker: map.Marker = await mapController.addMarker(markerOptions);
        // Build a **RotateAnimation** object.
        let animation = new map.RotateAnimation(0, 270);
        // Animation execution duration. 
        animation.setDuration(2000);

        // Animation end status.
        animation.setFillMode(map.AnimationFillMode.BACKWARDS);

        // Animation replay mode.
        animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

        // Number of times an animation is replayed.
        animation.setRepeatCount(100);

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

        // Set the animation.
        marker.setAnimation(animation);
        // Start the animation.
        marker.startAnimation();
      } else {
        console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
      }
    }
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
      }.width('100%')
    }.height('100%')
  }
}

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/__L2YcwgRlmtahzAETiMpw/en-us_image_0000002545978923.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19B403E8D844280069B5396B4D7FAD204452DCF472337F83E7D5B76DE188F9D7 "Click to enlarge")

## Playing Image Animations

import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct MarkerDemo {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 32.020750,
          longitude: 118.788765
        },
        zoom: 11
      }
    }

    this.callback = async (err, mapController) => {
      if (!err) {
        // Build a **MarkerOptions** object.
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.020750,
            longitude: 118.788765
          },
        };
        let images: Array<ResourceStr | image.PixelMap> = \[
          // The icons must be stored in the **resources/rawfile** directory.
          'icon/avocado.png',
          'icon/20231027.png',
          // The icon must be stored in the **resources/base/media** directory.
          $r('app.media.maps\_blue\_dot')
        \]
        let mContext = this.getUIContext().getHostContext();
        if (mContext) {
          const fileData: Uint8Array = await mContext?.resourceManager?.getRawFileContent('icon/icon.png');
          let imageSource: image.ImageSource =
            image.createImageSource(fileData.buffer.slice(0, fileData.buffer.byteLength));
          let pixelMap: PixelMap = await imageSource.createPixelMap();
          images.push(pixelMap);
        }
        // Create a Marker.
        let marker: map.Marker = await mapController.addMarker(markerOptions);
        // Build a **PlayImageAnimation** object.
        let animation: map.PlayImageAnimation = new map.PlayImageAnimation();
        // Add an image.
        await animation.addImages(images)
        // Animation execution duration. 
        animation.setDuration(3000);

        // Animation end status. 
        animation.setFillMode(map.AnimationFillMode.BACKWARDS);

        // Animation replay mode.
        animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

        // Number of times an animation is replayed.
        animation.setRepeatCount(100);

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
        // Set the animation.
        marker.setAnimation(animation);
        // Start the animation.
        marker.startAnimation();
      } else {
        console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
      }
    }
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
      }.width('100%')
    }.height('100%')
  }
}

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/vyVwvVSnTsOupYlcmsb7oA/en-us_image_0000002546019481.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB0A1CC0B3ED65C9B47B2B59ECDAD9563211FD3F8A18C7823432F3A3D4DDDADF "Click to enlarge")

## Generating a Marker Icon Through a Custom Component

Generate a Marker icon through a custom component.

import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MarkerDemo {
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private marker?: map.Marker;
  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          latitude: 32.120750,
          longitude: 118.788765
        },
        zoom: 14
      },
      scaleControlsEnabled: true
    }
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // Build a **MarkerOptions** object.
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 32.120750,
            longitude: 118.788765
          },
          // Custom component.
          iconBuilder: () => {
            this.renderBuilder();
          }
        };
        this.marker = await this.mapController?.addMarker(markerOptions);
      }
    }
  }
  @Builder
  renderBuilder() {
    Stack({ alignContent: Alignment.Center }) {
      // Replace the resource image with your own one. Save your image in the **resources/base/media** directory.
      Image($r('app.media.iconbuilder'))
        .syncLoad(true)
    }
    .height(50)
    .width(50)
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
          .width('100%')
          .height('100%');
      }.width('100%')
    }.height('100%')
  }
}

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gS5pqUSvRnGFjKfFEYhEfg/en-us_image_0000002514380090.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=575AF5EAF0E14B39D13370366F2F1994EC1FBD200D29038A52B323DBC0053B1A "Click to enlarge")
