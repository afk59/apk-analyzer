# How Do I Implement the Barcode Scanning Box on a Custom UI?

**Problem**

The code scanning box is not displayed on the scanning UI.

**Solution**

1.  Use ArkTS to draw the scanning box in the real-time scanning UI.
2.  Determine whether the barcode image is within the scanning box based on the obtained barcode image location information. Ensure that the location information of the scanning box and barcode image uses the same unit, for example, px or vp.
3.  If the barcode is not within the scanning box, call the [customScan.rescan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section19244173211169) API in the callback of [customScan.start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913) to scan again.

Sample code (for reference only):

import { customScan, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// For example, the width and height are set for XComponent as follows: cameraWidth = 1080px, cameraHeight = 1920px.
let cameraWidth = 1080;
let cameraHeight = 1920;
// When the custom scanning box is at the center of the screen, with the size 800 px x 800 px, the coordinates of barcode scanning box relative to XComponent are as follows: left: 140 px; top: 560 px; right: 940 px; bottom: 1360 px.
let scanBoxWidth = 800;
let scanBoxHeight = 800;
let scanBox: scanBarcode.ScanCodeRect = {
  left: (cameraWidth - scanBoxWidth) / 2,
  top: (cameraHeight - scanBoxHeight) / 2,
  right: (cameraWidth + scanBoxWidth) / 2,
  bottom: (cameraHeight + scanBoxHeight) / 2
}

// Set parameters for ViewControl.
let viewControl: customScan.ViewControl = {
  width: cameraWidth,
  height: cameraHeight,
  surfaceId: '123' // Mock data, which needs to be obtained from the component.
};
try {
  customScan.start(viewControl, (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
    if (error) {
      // Scanning failed.
      return;
    }
    if (result && result.length > 0) {
      for (let i = 0; i < result.length; i++) {
        // For example, scanCodeRect data is { left: 150px, top: 400px, right: 450px, bottom: 700px }.
        const scanCodeRect: scanBarcode.ScanCodeRect | undefined = result\[i\].scanCodeRect;
        if (scanCodeRect) {
          // Determine whether the barcode image is within the scanning box.
          if (scanCodeRect.left >= scanBox.left && scanCodeRect.top >= scanBox.top &&
            scanCodeRect.right <= scanBox.right &&
            scanCodeRect.bottom <= scanBox.bottom) {
            // If scanning is successful and the barcode is within the scanning box, process the scanning result based on service needs.
          } else {
            // If the barcode is not in the scanning box, scan again.
            try {
              customScan.rescan();
              break;
            } catch (error) {
              hilog.error(0x0001, '\[Scan Sample\]', \`Failed to rescan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        }
      }
    }
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
}
