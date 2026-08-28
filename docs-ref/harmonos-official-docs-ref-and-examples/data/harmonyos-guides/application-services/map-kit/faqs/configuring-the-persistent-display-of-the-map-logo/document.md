# Configuring the Persistent Display of the Map Logo

**Symptom**

The map logo is hidden.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/oYlOZNUbQ-S2Gdh2cD8gIQ/en-us_image_0000002485000176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB23BAE3B0CBB8DF4980AE474BA21E9FAD3B4512E2A93AC01A3A0F0C5604148D "Click to enlarge")

**Possible causes**

The map logo is blocked by a control or page during development.

**Solution**

The map logo's persistent display is mandatory. It should not be hidden or obscured. Refer to the following code to implement automatic map logo collision avoidance.

import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapKitAppDemo {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;
  private TAG = 'MapKitAppDemo';
  @State isShowSheet: boolean = true;

  @Builder
  Panel() {
    Column() {
      Row() {
        Text() {
          SymbolSpan($r('sys.symbol.magnifyingglass'))
            .fontSize(24)
            .fontColor(\[Color.Gray\])
        }

        TextInput()
          .layoutWeight(1)
          .backgroundColor('#33b1afaf')
          .borderRadius(24)
          .margin({ left: 8, right: 8 })
      }
      .backgroundColor(Color.White)
      .width('100%')
    }
    .borderRadius(10)
    .padding({
      top: 8,
      left: 8,
      right: 8,
      bottom: 4
    })
    .width('100%')
  }

  aboutToAppear() {
    // Map initialization parameters used to set the coordinates of the map center point and zoom level.
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.979227,
          longitude: 118.762245
        },
        zoom: 17
      }
    };

    // Map initialization callback.
    this.callback = async (err, mapController) => {
      if (!err) {
        // Obtain **mapController** to operate the map.
        this.mapController = mapController;
        // Return the event listener manager of the map component.
        this.mapEventManager = this.mapController.getEventManager();
        let callback = () => {
          console.info(this.TAG, \`on-mapLoad\`);
        }
        this.mapEventManager?.on('mapLoad', callback);
      } else {
        console.error(\`Failed to initialize the map. Code: ${err.code}; message: ${err.message}\`);
      }
    }
  }

  aboutToDisappear(): void {
    this.mapEventManager?.off('mapLoad');
    this.mapController?.clear();
  }

  private bindSheetOptions() {
    let bindSheetOptions = {
      // Heights of the semi-modal dialog box in its three different states.
      detents: \[100, 300, 500\],
      // Allow user interaction on the page where the semi-modal dialog box is located.
      enableOutsideInteractive: true,
      maskColor: Color.Transparent,
      backgroundColor: Color.White,
      blurStyle: BlurStyle.Thick,
      showClose: false,
      preferType: SheetType.CENTER,
      onAppear: () => {
        this.mapController?.setPadding({
          bottom: 358
        })
      },
      onHeightDidChange: (height: number) => {
        // Set the bottom margin of the map dynamically to avoid covering the logo.
        this.mapController?.setPadding({
          bottom: height + 8
        })
      }
    } as BindOptions
    return bindSheetOptions;
  }

  build() {
    Stack() {
      Column() {
        // Call the **MapComponent** component to initialize the map.
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .width('100%')
          .height('100%')
        Column()
          .bindSheet(this.isShowSheet, this.Panel(), this.bindSheetOptions())
          .visibility(this.isShowSheet ? Visibility.Visible : Visibility.None)
          .justifyContent(FlexAlign.Start)
      }
    }
    .height('100%')
    .width('100%')
  }
}

The following figure illustrates the effects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/7BsgR6AORP2cLe3KTcvcTw/en-us_image_0000002485160138.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062113Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D46EBE7EA65A97982EF65442005BB27BF2CD544F69988942AEBC868ABEB464C "Click to enlarge")
