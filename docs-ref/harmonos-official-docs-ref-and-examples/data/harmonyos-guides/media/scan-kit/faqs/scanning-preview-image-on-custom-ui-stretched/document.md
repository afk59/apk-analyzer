# Scanning Preview Image on Custom UI Stretched

**Problem**

The width and height of [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) do not match those of [ViewControl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section8604949165313). As a result, the preview page of the custom scanning UI is stretched.

**Solution**

Ensure that the width-height ratio of ViewControl is the same as that of XComponent. Currently, the supported resolution ratios are 16:9, 4:3, and 1:1.

For example, if **width** is set to **1080(px)** and **height** is set to **1920(px)** in XComponent, set **width** to **1080** and **height** to **1920** for ViewControl.

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is px.
  @State cameraHeight: number = 1920;
  // Set the preview stream width. The default unit is px.
  @State cameraWidth: number = 1080;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'onLoad is called')
          // Obtain surfaceId of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, 'viewControl', \`onLoad surfaceId: ${surfaceId}\`);
          // Set parameters for ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '\[Scan Sample\]',
                \`Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}\`);
            }).catch((error: BusinessError) => {
              hilog.error(0x0001, '\[Scan Sample\]',
                \`Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}\`);
            })
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight + 'px')
        .width(this.cameraWidth + 'px')
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
