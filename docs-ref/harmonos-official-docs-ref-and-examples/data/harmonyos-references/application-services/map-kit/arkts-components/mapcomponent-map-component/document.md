# MapComponent (Map Component)

Provides map components. You need to provide **mapOptions** and a callback that can be used to obtain a **MapComponentController** object.

**Start version**: 4.1.0(11)

#### Module Import

import { MapComponent } from '@kit.MapKit';

#### MapComponent

The **MapComponent** API provides map components and obtains **MapComponentController** objects through callbacks.

**Decorator type**: @Component

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

mapOptions

 | 

[mapCommon.MapOptions](../../arkts-apis/mapcommon-map-attribute-model/document.md#section816451553012)

 | 

No

 | 

No

 | 

Map initialization parameters.

 |
| 

mapCallback

 | 

AsyncCallback<[map.MapComponentController](../../arkts-apis/map-map-display/mapcomponentcontroller/document.md)\>

 | 

No

 | 

No

 | 

Callback function that returns [map.MapComponentController](../../arkts-apis/map-map-display/mapcomponentcontroller/document.md).

 |

**Example**:

import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct HuaweiMapDemo {
  private TAG = "HuaweiMapDemo";
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;

  aboutToAppear(): void {
    // Map initialization parameters used to set the coordinates of the map center point and zoom level.
    this.mapOptions = {
      position: {
        target: {
          latitude: 39.9,
          longitude: 116.4
        },
        zoom: 10
      }
    };

    // Map initialization callback.
    this.callback = async (err, mapController) => {
      if (!err) {
        // Obtain **mapController** to operate the map.
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, \`on-mapLoad\`);
        }
        this.mapEventManager.on("mapLoad", callback);
      }
    };
  }

  build() {
    Stack() {
      // Call the **MapComponent** component to initialize the map.
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%')
    }.height('100%')
  }
}

#### \[h2\]build

build(): void

Default constructor of a struct. This method cannot be directly called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

#### \[h2\]customInfoWindow

@BuilderParam customInfoWindow: customInfoWindowCallback

Custom information window.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

customInfoWindow

 | 

[customInfoWindowCallback](#section1038016522147)

 | 

Yes

 | 

Custom information window.

 |

**Example**:

import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { customInfoWindowCallback } from '@hms.core.map.MapComponent';

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
          // Set an information window title.
          title: "Custom Information Window",
        };
        await this.mapController?.addMarker(markerOptions);
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
          .height('100%')
      }.width('100%')
    }.height('100%')
  }

  // Custom information window BuilderParam.
  @BuilderParam customInfoWindow: customInfoWindowCallback = this.customInfoWindowBuilder;

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
        .border({
          width: 3,
          color: Color.Black,
          radius: 25,
          style: BorderStyle.Dashed
        })
    }
  }
}

#### customInfoWindowCallback

type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void

Callback of a custom information window.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

markerDelegate

 | 

[map.MarkerDelegate](../../arkts-apis/map-map-display/markerdelegate/document.md)

 | 

Yes

 | 

Marker for a delegate object.

 |
