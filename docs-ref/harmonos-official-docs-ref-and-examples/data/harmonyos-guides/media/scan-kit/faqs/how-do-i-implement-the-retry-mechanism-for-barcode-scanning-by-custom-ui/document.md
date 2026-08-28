# How Do I Implement the Retry Mechanism for Barcode Scanning by Custom UI?

**Problem**

After customScan.[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245) is successfully called and customScan.[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913) is called to start camera streams, the internal error 1000500001 is reported.

**Solution**

You can implement the retry mechanism for starting camera streams.

In the mechanism, you will stop and then release camera streams by calling customScan.[stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915) and customScan.[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917) respectively, and then restart camera streams by calling customScan.[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245) and customScan.[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913).

Sample code (for reference only):

import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State viewControl: customScan.ViewControl = {
    width: 1080,
    height: 1080,
    surfaceId: ''
  };
  private retryScanTimes = 0;
  private options: scanBarcode.ScanOptions = {
    scanTypes: \[scanCore.ScanType.ALL\],
    enableMultiMode: true,
    enableAlbum: true
  };
  private customScanCallbackScan: AsyncCallback<scanBarcode.ScanResult\[\]> =
    (error: BusinessError, result: scanBarcode.ScanResult\[\]) => {
      if (error && error.code !== 0) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`An error is returned by customScan.start->CallbackScan. Code: ${error.code}\`);
        // start callback, which is triggered to restart camera streams when the internal error 1000500001 is reported.
        if (error.code === scanCore.ScanErrorCode.INTERNAL\_ERROR) {
          this.retryCamera(error);
        }
      } else {
        hilog.info(0x0001, '\[Scan Sample\]', \`customScan start callbackScan result size: ${result.length}\`)
}
      // Barcode recognition processing logic.
      // ...
    }

  // Restart camera streams.
  retryCamera(error: BusinessError) {
    if (this.retryScanTimes < 3 && error.code === scanCore.ScanErrorCode.INTERNAL\_ERROR) {
      this.retryScanTimes++;
      let timeId = setTimeout(async () => {
        hilog.info(0x0001, '\[Scan Sample\]',
          \`Retry camera start. Times: ${this.retryScanTimes}.\`);
        // Stop and release camera streams.
        await this.releaseCamera();
        // Restart camera streams.
        this.startCamera();
        hilog.info(0x0001, '\[Scan Sample\]', 'Retry camera end.');
        clearTimeout(timeId);
      }, 100)
    }
  }

  // Start camera streams.
  startCamera() {
    try {
      customScan.init(this.options);
      hilog.info(0x0001, '\[Scan Sample\]', 'customScan->init end');
      try {
        customScan.start(this.viewControl, this.customScanCallbackScan);
        hilog.info(0x0001, '\[Scan Sample\]', 'customScan->start end');
      } catch (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to customScan->start. Code: ${error.code}, message: ${error.message}\`);
      }
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to customScan->init. Code: ${error.code}, message: ${error.message}\`);
    }
  }

  // Stop and release camera streams.
  async releaseCamera() {
    try {
      await customScan.stop();
      hilog.info(0x0001, '\[Scan Sample\]', 'customScan->stop end');
      try {
        await customScan.release();
        hilog.info(0x0001, '\[Scan Sample\]', 'customScan->release end');
      } catch (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to customScan->release. Code: ${error.code}, message: ${error.message}\`);
      }
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to customScan->stop. Code: ${error.code}, message: ${error.message}\`);
    }
  }

  build() {
  }
}
