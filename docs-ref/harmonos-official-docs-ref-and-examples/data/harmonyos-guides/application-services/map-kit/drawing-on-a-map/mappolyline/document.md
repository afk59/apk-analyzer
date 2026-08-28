# MapPolyline

#### Use Cases

This section describes how to draw a MapPolyline on a map, and set the segment colors, enable gradient, and draw the texture for the MapPolyline.

Starting from 5.0.3(15), the function of drawing the texture for the MapPolyline is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/hGOYVX0SSGudeRJ6du3IZg/en-us_image_0000002514381418.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=808BBFD454D9EF396FC4CF9A18AC9F247368C59FBA9152BFF367C94248A71600 "Click to enlarge")

#### API Description

The MapPolyline adding function is mainly provided by [MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153), [addPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section6818109112812), and [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline). For more information about the APIs, please refer to [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153)

 | 

MapPolyline parameters.

 |
| 

[addPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section6818109112812)(options: [mapCommon.MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153)): Promise<[MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline)\>

 | 

Adds a MapPolyline to a map.

 |
| 

[MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline)

 | 

MapPolyline. This API supports updating and querying MapPolyline attributes.

 |

#### Development Procedure

## Adding a MapPolyline

1.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    import { AsyncCallback } from '@kit.BasicServicesKit';
    
2.  Add a MapPolyline. Create initialization parameters in the **callback** method, and create a [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline).
    
    @Entry
    @Component
    struct MapPolylineDemo {
      private mapOptions?: mapCommon.MapOptions;
      private mapController?: map.MapComponentController;
      private callback?: AsyncCallback<map.MapComponentController>;
      private mapPolyline?: map.MapPolyline;
    
      aboutToAppear(): void {
        // Map initialization parameters.
        this.mapOptions = {
          position: {
            target: {
              latitude: 31.98,
              longitude: 118.78
            },
            zoom: 14
          }
        };
        this.callback = async (err, mapController) => {
          if (!err) {
            this.mapController = mapController;
    
            // MapPolyline initialization parameters.
            let polylineOption: mapCommon.MapPolylineOptions = {
              points: \[
                { longitude: 118.78, latitude: 31.975 },
                { longitude: 118.78, latitude: 31.982 },
                { longitude: 118.79, latitude: 31.985 }
              \],
              clickable: true,
              startCap: mapCommon.CapStyle.BUTT,
              endCap: mapCommon.CapStyle.BUTT,
              geodesic: false,
              jointType: mapCommon.JointType.BEVEL,
              visible: true,
              width: 10,
              zIndex: 10,
              gradient: false
            }
            // Create a MapPolyline.
            try {
              this.mapPolyline = await this.mapController.addPolyline(polylineOption);
            } catch (e) {
              console.error(\`Failed to create the MapPolyline. code: ${e.code}; message: ${e.message}\`);
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/pHC2DFeAS-SuzDR98miNEg/en-us_image_0000002514541580.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19E816A1F161A759DBDC11466596AFEA63FD9972B316B86362BFDA6232BCD170 "Click to enlarge")
    

## Setting the Colors of MapPolyline Segments

Method 1: During MapPolyline creation, set the color values of the MapPolyline segments in the **colors** attribute of [MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153).

let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[{longitude:118.78,latitude:31.975}, {longitude:118.78,latitude:31.982}, {longitude:118.79,latitude:31.985}\],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.BEVEL,
  visible: true,
  width: 10,
  zIndex: 10,
  // Set the color. 
  colors: \[0xffffff00, 0xff000000\],
  gradient: false
};

Method 2: Call the [setColors](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline#section205821994815)() method of [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline).

let colors = \[0xffffff00, 0xff000000\];
this.mapPolyline.setColors(colors);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/rVaPzeOVRAaQLm7Tk0dYMg/en-us_image_0000002545981753.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AD316688F284795A5FDAA641F582995BA46940F0C5ABA3618569AF400372F4A "Click to enlarge")

## Enabling Gradient for a MapPolyline

Method 1: Set the **gradient** attribute of [MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153) to **true**.

let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[{longitude:118.78,latitude:31.975}, {longitude:118.78,latitude:31.982}, {longitude:118.79,latitude:31.985}\],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.BEVEL,
  visible: true,
  width: 10,
  zIndex: 10,
  colors: \[0xffffff00, 0xff000000\],
  // Enable gradient for the MapPolyline. 
  gradient: true
};

Method 2: Call the [setGradient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline#section690415431896)() method of [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline).

this.mapPolyline.setGradient(true);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ZZISr9ECQ1yGYrjaEgbz2w/en-us_image_0000002514384398.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3288BA12A4D98BE0C2AC2B3CCCEAC60A8A0E9FF5F8764D42DB8D8551BB1E5EF7 "Click to enlarge")

## Drawing Texture

Method 1: During MapPolyline creation, set the **customTexture** attribute of [MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153).

let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[
    { latitude: 32.220750, longitude: 118.788765 },
    { latitude: 32.120750, longitude: 118.788765 },
    { latitude: 32.020750, longitude: 118.788765 },
    { latitude: 31.920750, longitude: 118.788765 },
    { latitude: 31.820750, longitude: 118.788765 }
  \],
  clickable: true,
  jointType: mapCommon.JointType.DEFAULT,
  width: 20,
  // The icon must be stored in the **resources/rawfile** directory.
  customTexture: "icon/naviline\_arrow.png"
}

Method 2: Call the [setCustomTexture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline#section18866126111212) method of [MapPolyline](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mappolyline).

await this.mapPolyline.setCustomTexture("icon/naviline\_arrow.png");

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/hRPwyBeMRga2e16nkG1_nw/en-us_image_0000002546024455.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D49A426D65E2653D96728E28F113FD177E97674F652EB0860F401F2A9F34FD4B "Click to enlarge")

## Setting Textures for Segments of a MapPolyline

You can set the MapPolyline segment textures through the **customTextures** and **customTextureIndexes** attributes of [MapPolylineOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section113246334153) during MapPolyline creation.

import { image } from '@kit.ImageKit';

// Store images in an array.
let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
// Icons are stored in **resources/rawfile**. The passed value **icon/img.png** indicates the relative path of the icon file within **resources/rawfile**.
customTextures.push('icon/img.png');
customTextures.push('icon/img\_1.png');
let cusIndexNumber: Array<number> = new Array();
// The length of the **cusIndexNumber** array must be the same as the number of MapPolyline points. The array element content corresponds to the subscripts of **customTextures**. Images are stored from the second element in the array.
cusIndexNumber.push(0, 0, 1);
// MapPolyline initialization parameters.
let polylineOption: mapCommon.MapPolylineOptions = {
  points: \[
    { longitude: 118.78, latitude: 31.975 },
    { longitude: 118.78, latitude: 31.982 },
    { longitude: 118.79, latitude: 31.985 }\],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  jointType: mapCommon.JointType.BEVEL,
  width: 30,
  // The icon must be stored in the **resources/rawfile** directory.
  customTextures: customTextures,
  customTextureIndexes: cusIndexNumber
};
let mapPolyline = await this.mapController.addPolyline(polylineOption);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Z28THg0fR8G2AUkKtln5pQ/en-us_image_0000002514544706.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062112Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE952BB5F37BB8930989953C6D32DF5ABCAB90727747A9A2BB13C8F47EC7C2AC "Click to enlarge")
