# How do I generate a QR code with a logo?

1.  Use the **Canvas** component to draw the QR code image and logo image.
    
    Canvas(this.context)
      .width(300)
      .height(300)
      .onReady(() => {
        this.createQRCode();
      })
    
2.  Call the **createBarcode** API to generate the barcode image pixelMap. Then, call the **drawImage** API to draw the barcode image pixelMap. Finally, call the **drawImage** API again to draw the logo and overlay it on the barcode image.
    
    let options: generateBarcode.CreateOptions = {
      scanType: scanCore.ScanType.QR\_CODE,
      height: this.QRCodeWidth,
      width: this.QRCodeWidth
    };
    generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
      this.pixelMap = pixelMap;
      this.context.drawImage(this.pixelMap, 0, 0, 300, 300, 0, 0, 300, 300);
      this.context.drawImage(this.img, 0, 0, 80, 80, 110, 110, 80, 80);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '\[generateBarcode\]', 'promise error : %{public}s', JSON.stringify(error));
    })
    

The sample code is as follows:

import { image } from '@kit.ImageKit';
import { generateBarcode, scanCore } from '@kit.ScanKit';
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined;
  private setting: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.setting);
  private img: ImageBitmap = new ImageBitmap('common/startIcon.png');
  private QRCodeWidth: number = 300;
  private QRCodeHeight: number = 300;

  aboutToAppear(): void {
    let sdkApiVersionInfo: number = deviceInfo.sdkApiVersion;
    // The API version is greater than or equal to API18.
    if(sdkApiVersionInfo >= 18){
      this.QRCodeWidth = this.getUIContext().vp2px(this.QRCodeWidth);
      this.QRCodeHeight = this.getUIContext().vp2px(this.QRCodeHeight);
    }
  }

  createQRCode() {
    this.pixelMap = undefined;
    let content: string = 'helloWorld';
    let options: generateBarcode.CreateOptions = {
      scanType: scanCore.ScanType.QR\_CODE,
      height: this.QRCodeWidth,
      width: this.QRCodeWidth
    };
    generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
      this.pixelMap = pixelMap;
      this.context.drawImage(this.pixelMap, 0, 0, 300, 300, 0, 0, 300, 300);
      this.context.drawImage(this.img, 0, 0, 80, 80, 110, 110, 80, 80);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '\[generateBarcode\]', 'promise error : %{public}s', JSON.stringify(error));
    })
  }

  build() {
    Column() {
      Canvas(this.context)
        .width(300)
        .height(300)
        .onReady(() => {
          this.createQRCode();
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Start)
    .justifyContent(FlexAlign.Start)
  }
}
