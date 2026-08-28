# How Do I Scan Barcodes Continuously on the Custom Scanning UI (customScan.rescan)?

**Problem**

After a barcode is scanned and a code value is obtained on the custom scanning UI, how do I implement the function of continue scanning barcodes?

**Solution**

Call customScan.[rescan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section19244173211169) to trigger scanning again in customScan.[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913)(viewControl, callback) using a callback instead of a promise.

Example:

import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode } from '@kit.ScanKit';

@Entry
@Component
struct Index {
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
      try {
  // Trigger scanning again. To trigger scanning again without restarting the camera, call the **rescan** API in the asynchronous callback of the **start** API.
        customScan.rescan();
      } catch (error) {
        hilog.error(0x0001, '\[Scan Sample\]', \`Failed to rescan. Code: ${error.code}, message: ${error.message}\`);
      }
    }

  build() {
  }
}
