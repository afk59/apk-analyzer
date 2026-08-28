# Map Location Change

#### Use Cases

The Huawei map's movement functionality is implemented by simulating camera movements. This camera, referred to as the map camera, allows you to control the visible area of a map by changing its position, as shown in the following figures.

This section describes the attributes of the map camera and how to move the camera.

<table style="border-style: none;"><tbody><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 1 </b>Before moving the camera</span></div><p><span><img height="692.36076" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/b2PjGFZWSvq6w_93hRxK6g/en-us_image_0000002514526868.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=A14C81F462667CB86582B8B7FA26E89760DCF090238648FFEB984B3FEA5CAF97" title="Click to enlarge" width="313.21500000000003"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 2 </b>After moving the camera</span></div><p><span><img height="692.325781" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/GjRD3l3-T0Ch3sUDMBqZlg/en-us_image_0000002545846825.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=9DDAC95496397FF626E2C31CACBB8E1762B3CDC4E6A0EE8480FF3FB8E72A34BD" title="Click to enlarge" width="313.21500000000003"></span></p></td></tr></tbody></table>

#### API Description

You can call the [moveCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section141021341974), [animateCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section6163175355113), and [animateCameraStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section972910185717) methods in the [map](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map) namespace to implement map camera movement. You can create the input parameter [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate) for these methods using methods described in the following table.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[zoomTo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-zoomto)(zoom: number): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Sets the zoom level of a map.

 |
| 

[zoomOut](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-zoomout)(): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Zooms out on a map by 1 level.

 |
| 

[zoomIn](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-zoomin)(): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Zooms in on a map by 1 level.

 |
| 

[zoomBy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-zoomby)(amount: number, focus?: [mapCommon.MapPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section123881566186)): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Zooms in or out on a map by a specified value with the specified pixel point as the center.

 |
| 

[scrollBy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-scrollby)(x: number, y: number): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Moves the map center point by pixel.

 |
| 

[newLatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-newlatlngbounds-1#section1925622842414)(bounds: [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section96341159111320), padding?: number): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Sets the longitude and latitude ranges of a map, and the padding between the map region and map edges.

 |
| 

[newLatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-newlatlngbounds-1#section275119019112)(bounds: [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section96341159111320), width: number, height: number, padding: number): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Sets the longitude and latitude ranges of a map, the height and width of the longitude and latitude rectangle range, and the padding between the map region and map edges.

 |
| 

[newLatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-newlatlngbounds-1#section268618619820)(bounds: [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section96341159111320), padding: [mapCommon.Padding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section144591344648)): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Sets the longitude and latitude ranges of a map, and the padding between the map region and the four map edges.

 |
| 

[newLatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-newlatlng)(latLng: [mapCommon.LatLng](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section20691173773810), zoom?: number): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Sets the map center and zoom level.

 |
| 

[newCameraPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-newcameraposition)(cameraPosition: [mapCommon.CameraPosition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section105031244194712)): [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate)

 | 

Updates the map status.

 |

#### Development Procedure

## Moving the Camera

1.  Initialize the map and obtain an object of the map operation class [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller). For details, please refer to [Displaying a Map](../../map-creation/displaying-a-map/document.md).
2.  Import required modules.
    
    import { MapComponent, mapCommon, map } from '@kit.MapKit';
    
3.  Call the [moveCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section141021341974), [animateCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section6163175355113), and [animateCameraStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section972910185717) methods of [MapComponentController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller) to move the map camera.
    
    You can move the map camera in animation or non-animation mode.
    
    -   When moving the camera in animation mode, you can set the duration of the animation.
    -   Camera movement in non-animation mode is transient.
    
    // Create a **CameraUpdate** object. 
    let cameraPosition: mapCommon.CameraPosition = {
      target: {
        latitude: 32.0,
        longitude: 118.0
      },
      zoom: 10,
      tilt: 0,
      bearing: 0
    };
    let cameraUpdate = map.newCameraPosition(cameraPosition);
    // Move the map camera in non-animation mode.
    this.mapController.moveCamera(cameraUpdate);
    
    // Move the map camera in animation mode.
    this.mapController.animateCamera(cameraUpdate, 1000);
    
    // Move the map camera in animation mode and return the animation result.
    let animateResult = await this.mapController.animateCameraStatus(cameraUpdate, 1000);
    
    <table style="border-style: none;"><tbody><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 3 </b>Before moving the camera</span></div><p><span><img height="829.0391410000001" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/xOkJkWpEQTioqGL-imc4WQ/en-us_image_0000002545966909.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=084F2E3752A41AC29779D5B4960E73F48D08FABE11D5D5C8AADA3C78D1F7D2FF" title="Click to enlarge" width="375.06"></span></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><div class="fignone"><span class="figcap"><b>Figure 4 </b>After moving the camera</span></div><p><span><img height="831.259576" originheight="2688" originwidth="1216" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/czgYbNZ-RA6i9p6HtP_Wyg/en-us_image_0000002514367046.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062112Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=C49976A3EDAD3BFC6A551D038A4D8A1642D6C3FF5EC82EBCC01FBD961905800E" title="Click to enlarge" width="376.0575"></span></p></td></tr></tbody></table>
    
4.  You can also create a [CameraUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-cameraupdate) object using either of the following methods:
    
    // Method 1: Increase the camera zoom level by 1 and retain other attribute settings.
    let cameraUpdate = map.zoomIn();
    
    // Method 2: Decrease the camera zoom level by 1 and retain other attribute settings.
    let cameraUpdate1 = map.zoomOut();
    
    // Method 3: Set the camera zoom level to a specified value and retain other attribute settings.
    let zoom1 = 8.0;
    let cameraUpdate2 = map.zoomTo(zoom1);
    
    // Method 4:
    // a. Increase or decrease the camera zoom level by a specified value.
    // b. Move the camera to the specified center point and increase or decrease the camera zoom level. 
    // The left vertex of the screen is used as the (0, 0) point. A positive value of **positionX** indicates that the visible region moves rightwards, while a negative value indicates that the visible region moves leftwards.
    // A positive value of **positionY** indicates that the visible region moves downwards, while a negative value indicates that the visible region moves upwards. 
    let point: mapCommon.MapPoint = {
      positionX: 31,
      positionY: 118
    };
    let amount = 2.0;
    let cameraUpdate3 = map.zoomBy(amount, point);
    
    // Method 5: Set the longitude, latitude, and map zoom level of the camera.
    // a. Specify only the longitude and latitude of the camera to move the center point.
    // b. Specify the longitude, latitude, and map zoom level of the camera. You can call this API to move the camera to the center point and zoom in or out the camera.
    let latLng: mapCommon.LatLng = {
      latitude: 31.5,
      longitude: 118.9
    };
    let zoom2 = 10;
    let cameraUpdate4 = map.newLatLng(latLng, zoom2);
    
    // Method 6: Set the visible region of the camera.
    let latLngBounds: mapCommon.LatLngBounds = {
      northeast: {
        latitude: 32.5,
        longitude: 119.9
      },
      southwest: {
        latitude: 31.5,
        longitude: 118.9
      }
    };
    // Set the longitude and latitude ranges of the map, and set the padding between the map region and map edges to 5 pixels.
    let cameraUpdate5 = map.newLatLngBounds(latLngBounds, 5);
    // Method 7: Set the visible region of the camera.
    // Set the longitude and latitude ranges of the map. Set the width and height of the rectangular area defined by latitude and longitude to 1000 pixels and 1000 pixels, respectively, and set the padding between the map area and edges to 100 pixels.
    let cameraUpdate6 = map.newLatLngBounds(latLngBounds, 1000, 1000, 100);
    // Method 8: Set the longitude and latitude range of the map. Set the padding between the map area and the left, top, right, and bottom edges to 5, 6, 7, and 8 pixels, respectively. 
    let paddings: mapCommon.Padding = {
      left:5,
      top: 6,
      right: 7,
      bottom: 8
    };
    let cameraUpdate7 = map.newLatLngBounds(latLngBounds, paddings);
    
    // Method 9: Scroll the camera by a specified number of pixels. 
    let x = 100.0;
    let y = 100.0;
    let cameraUpdate8 = map.scrollBy(x, y);
    

## Setting the Preferred Minimum and Maximum Camera Zoom Levels

// Set the preferred minimum zoom level. The value ranges from 2 to 20.
this.mapController.setMinZoom(6); 
// Set the preferred maximum zoom level. The value ranges from 2 to 20.
this.mapController.setMaxZoom(14);

## Setting the Bounds of the Map Camera

Map Kit allows you to set the map camera bounds. You can call the [setLatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-map-mapcomponentcontroller#section14990184514712) API to specify [LatLngBounds](https://developer.huawei.com/consumer/en/doc/harmonyos-references/map-common#section96341159111320) to constrain the camera target, preventing it from moving outside the defined area when users pan the map. If this parameter is set to **null**, the map camera bounds will be cleared.

let bounds: mapCommon.LatLngBounds = {
  northeast: {
    latitude: 31,
    longitude: 118
  },
  southwest: {
    latitude: 30,
    longitude: 113
  }
};
this.mapController.setLatLngBounds(bounds);
