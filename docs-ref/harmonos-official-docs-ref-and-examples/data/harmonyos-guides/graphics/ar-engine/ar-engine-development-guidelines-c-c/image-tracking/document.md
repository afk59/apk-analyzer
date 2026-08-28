# Image Tracking

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how to recognize and track the pose information of 2D images, and provides instructions on how to detect whether the input image exists in the scene and, once recognized, output its pose data.

**Figure 1** Image tracking

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/YXwIsyHOStuWTNyEAki9Tw/en-us_image_0000002500426102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F8AF5B3AAA1655D50DFA380D70F149655871F674A45BC2B8EDC8D26D2D96111)

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)

#### API Description

The following lists APIs used for AR image tracking. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3)

 | 

Creates an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARSession\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga1d1cacf372a8011a439f0e4e76994259)

 | 

Updates the computation result of AR Engine.

 |
| 

[HMS\_AREngine\_ARSession\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga6394ae995148abbe3d00082817bf320a)

 | 

Configures an [AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650) session.

 |
| 

[HMS\_AREngine\_ARFrame\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gadfcb9589137a39c5afcb217e18853a9d)

 | 

Creates an [AREngine\_ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in **\*outFrame**.

 |
| 

[HMS\_AREngine\_ARSession\_SetDisplayGeometry](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3f23bf747def8303c3fb261a9e9a2286)

 | 

Sets the display height and width (in pixels). Ensure that the height and width you set here are consistent with those of the display view. A mismatch will result in a camera preview failure.

 |
| 

[HMS\_AREngine\_ARSession\_SetCameraGLTexture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac697e4be36db63ed6098f154aa9ac01c)

 | 

Sets the OpenGL texture for storing the camera preview stream data.

 |
| 

[HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[HMS\_AREngine\_ARTrackableList\_AcquireItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab1782eeeeddc01b77a140af915cb351c)

 | 

Obtains the object at a specified index from the trackable object list.

 |
| 

[HMS\_AREngine\_ARPlane\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gabbb03027afb984be8542d00d2eebd063)

 | 

Obtains the pose information for the conversion from the plane's local coordinate system to the world coordinate system.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireCamera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga5295c975a0ff3d633a1dde5a8eb70863)

 | 

Obtains the camera parameter object of the current frame.

 |
| 

[HMS\_AREngine\_ARPose\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gafb471f39563ca1a4947d4f87c77e24e2)

 | 

Allocates and initializes a new pose object.

 |
| 

[HMS\_AREngine\_ARCamera\_GetPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga00df108c4ba187967a10e9c4d2e27d3a)

 | 

Obtains the pose of the current camera object in the AR world space.

 |
| 

[HMS\_AREngine\_ARAugmentedImageDatabase\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section4108822184411)

 | 

Creates an empty tracking image database.

 |
| 

[HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section0315115618403)

 | 

Adds an image to the image database and outputs the index of the image.

 |
| 

[HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c)

 | 

Obtains the list of all trackable objects of the specified type.

 |
| 

[HMS\_AREngine\_ARTrackableList\_GetSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9729d4436f3d969286f31b33d07513e)

 | 

Obtains the number of trackable objects in the list.

 |
| 

[HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section498975343520)

 | 

Obtains the pose information of the center point of a tracking image in the world coordinate system.

 |
| 

[HMS\_AREngine\_ARAugmentedImage\_GetExtendX](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section917593011382)

 | 

Obtains the estimated value on the X axis based on the center point of the image (coordinate origin) and the physical image width (unit: m).

 |
| 

[HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section9630192711390)

 | 

Obtains the estimated value on the Z axis based on the center point of the image (coordinate origin) and the physical image width (unit: m).

 |
| 

[HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section6536162875117)

 | 

Serializes the feature database. After images are added, the feature database can be serialized into a buffer. You can save the buffer for future use.

 |
| 

[HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section1619582764511)

 | 

Deserializes the feature database. You can deserialize the buffer data generated or saved last time into the feature database and use the feature database directly.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp) to access the complete demo code.

## Declaring Native APIs

For details, please refer to [Declaring Native APIs](../placing-ar-objects/document.md#section1557014318265) in **Placing AR Objects**.

## Creating a UI

Start by creating an initial UI page, **ARImage.ets**, and add two buttons: one for adding a local image (**ARImageByAdd.ets**) and the other for reading from the local database (**ARImageByDatabase.ets**). Also configure routing for navigation between pages. For detailed page routing configurations, please refer to [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARImage.ets.
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Builder
export function ARImageBuilder() {
  ARImage();
}

@Component
struct ARImage {
  pageInfo: NavPathStack = new NavPathStack();
  private imagePathArray: string\[\] = \[\];

  build(): void {
    NavDestination() {
      Column() {
        Button('Select local image', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {

            try {
              let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
              photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
              photoOption.maxSelectNumber = 50;
              photoOption.isEditSupported = false;
              let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

              let photoResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoOption);
              if (photoResult.photoUris.length > 0 && photoResult.photoUris\[0\].length > 0) {
                this.imagePathArray = photoResult.photoUris;
                this.pageInfo.pushDestinationByName('ARImageByAdd', this.imagePathArray).catch((error: BusinessError) => {
                  console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
                });
              }
            } catch (error) {
              const err: BusinessError = error as BusinessError;
              console.error(\`Failed to select by photoPicker. Code: ${err.code}, message is ${err.message}.\`);
            }
          })

        Button('Load local database', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushDestinationByName('ARImageByDatabase', null).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
            });
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

Create **ARImageByAdd.ets** for selecting images, use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to load the camera preview, and periodically trigger the rendering of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARImageByAdd.ets.
import { taskpool } from '@kit.ArkTS';
import { BusinessError, deviceInfo, emitter } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARImageByAddBuilder() {
  ARImageByAdd();
}

@Component
struct ARImageByAdd {
  pageInfo: NavPathStack = new NavPathStack();
  private imageAddFailedNumbers: number = 0;
  private imageAddNumbers: number = 0;
  private imagePathList: string\[\] = \[\];
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId = 'ARImage';
  @State addImageLog: string = '';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State imageTotalNumbers: number = 0;
  @State private isImageAddComplete: boolean = false;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;
  @State showPage: boolean = true;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            console.info(\`XComponent onLoad ${this.xComponentId}.\`);
            this.interval = setInterval(() => {
              if (!this.isUpdate || !this.isImageAddComplete || this.imageAddNumbers === 0) {
                return;
              }
              arEngineDemo.update(this.xComponentId);
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            console.info(\`XComponent onDestroy ${this.xComponentId}.\`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })

        Text ('Progress of adding images: ' +
        this.imageTotalNumbers.toString() + '/' + this.imagePathList.length.toString() + '\\n ' +
        'Number of images added successfully: ' +
        this.imageAddNumbers + ' \\n' +
        'Number of images that failed to add: ' +
        this.imageAddFailedNumbers + '\\n' + this.addImageLog)
          .width(300)
          .textAlign(TextAlign.Center)
          .fontColor(Color.Red)
          .visibility(!this.isImageAddComplete ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
      }
    }
    .onBackPressed(() => {
      console.error('Failed to onBackPressed.');
      return false;
    })
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[1, this.rotation\]);
      arEngineDemo.start(this.xComponentId, config);

      try {
        console.info(\`Image path length: ${this.imagePathList.length}.\`);
        this.RegisterAddImageCallback();
        taskpool.execute(addImage, this.xComponentId, this.imagePathList, errcode).then(() => {
          console.info('Add image task complete.');
          emitter.emit('checkAddImageResult');
        })
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(\`Failed to promise options error. Code: ${err.code}, message is ${err.message}.\`);
      }
    })
    .onWillDisappear(() => {
      if (this.imageAddNumbers > 0) {
        arEngineDemo.saveImageDataBaseToLocal(this.xComponentId, this.context.filesDir);
      }
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.xComponentId);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.imagePathList = context.pathInfo.param as string\[\];
    })
    .hideTitleBar(true)
    .hideBackButton(false)
    .hideToolBar(true)
  }

  private ShowDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: 'Warning',
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY
            .animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: \[{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: 'Exit',
        action: () => {
          console.info('Callback when the second button is clicked')
          this.pageInfo.pop();
        }
      }\]
    })
  }

  private RegisterAddImageCallback(): void {
    emitter.on('addImage', (data: emitter.EventData) => {
      if (data.data?.addImageReason === 0) {
        this.imageAddNumbers++;
        console.info(\`Succeeded in adding image, image numbers: ${this.imageAddNumbers}.\`);
      } else {
        this.imageAddFailedNumbers++;
        this.addImageLog += 'Name of the failed image:' +
          data.data?.imageName + '\\n' +
          'Failure cause:' +
          errcode.get(data.data?.addImageReason) + '\\n';
        console.error(\`Failed to add image, image numbers: ${this.imageAddFailedNumbers}.\`);
      }
      this.imageTotalNumbers++;
    })

    emitter.on('checkAddImageResult', () => {
      if (this.imageAddNumbers === 0 && this.isUpdate) {
        this.showPage = false;
        this.ShowDialog('Please add a valid image.');
      }
      emitter.off('addImage');
      this.isImageAddComplete = true;
      emitter.off('checkAddImageResult');
    })
  }
}

let errcode: Map<number, string> = new Map<number, string>(\[\[0, 'success'\], \[1, 'size not match'\],
  \[2, 'too bright or too dark'\], \[3, 'image color is relatively single'\], \[4, 'other error'\]\]);

// Execute the image addition task asynchronously.
@Concurrent
async function addImage(componentId: string, imagePathList: string\[\],
  errcode: Map<number, string>): Promise<void> {
  for (let index = 0; index < imagePathList.length; index++) {
    const imagePath: string = imagePathList\[index\];
    let file: fileIo.File;
    try {
      file = fileIo.openSync(imagePath, fileIo.OpenMode.READ\_ONLY);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to open image. Code is ${err.code}, message is ${err.message}\`);
      this.addFailedImageCounts += 1;
      continue
    }
    let imageName: string = file.name;
    const imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
    try {
      fileIo.closeSync(file);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(\`Failed to closeSync. Code is ${err.code}, message is ${err.message}.\`);
      imageSourceApi.release();
      continue;
    }
    const imageInfo: image.ImageInfo = imageSourceApi.getImageInfoSync();
    if (!imageInfo) {
      console.error(\`Failed to obtain the image pixel map information.\`);
      imageSourceApi.release();
      continue;
    }
    const opts: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
      desiredSize: { width: imageInfo.size.width, height: imageInfo.size.height }
    }
    const pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync(opts);
    if (!pixelMap) {
      console.error('Failed to create pixelMap.');
      imageSourceApi.release();
      continue;
    }
    const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
    await pixelMap.readPixelsToBuffer(readBuffer);
    await pixelMap.release();

    let result: number = arEngineDemo.initImage(componentId, imageInfo.size.width, imageInfo.size.height, readBuffer);
    if (errcode.has(result) === false) {
      console.error('Failed to add image, break.');
      imageSourceApi.release();
      break;
    }
    if (result !== 0) {
      console.error(\`Failed to Add image, reason is: ${errcode.get(result)}, imageName is: ${imageName}.\`);
    }
    let eventData: emitter.EventData = {
      data: {
        'addImageReason': result,
        'imageName': imageName,
      }
    }
    emitter.emit('addImage', eventData);
    imageSourceApi.release();
  }
}

Create **ARImageByDatabase.ets** for loading the local database, loading the camera preview, and periodically triggering the rendering of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARImageByDatabase.ets.
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARImageByDatabaseBuilder() {
  ARImageByDatabase();
}

@Component
struct ARImageByDatabase {
  pageInfo: NavPathStack = new NavPathStack();
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId = 'ARImage';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;
  @State showPage: boolean = true;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            console.info(\`XComponent onLoad ${this.xComponentId}.\`);
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.xComponentId);
              }
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            console.info(\`XComponent onDestroy ${this.xComponentId}.\`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[1, this.rotation\]);
      arEngineDemo.start(this.xComponentId, config);

      arEngineDemo.setPath(this.xComponentId, this.context.filesDir);

      let imageCountInDatabase: number = arEngineDemo.getImageCount(this.xComponentId);
      console.info(\`ImageCountInDatabase: ${imageCountInDatabase}.\`);
      if (imageCountInDatabase <= 0) {
        this.ShowDialog('Please add a valid image.');
      }
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.xComponentId);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  ShowDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: 'Warning',
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: \[{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
            value: 'Exit',
        action: () => {
          console.info('Callback when the second button is clicked.');
          this.pageInfo.pop();
        }
      }\]
    })
  }
}

Also configure routing for navigation between pages. For detailed page routing configurations, please refer to [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).

## Importing AR Engine

For details, please refer to [Importing AR Engine](../placing-ar-objects/document.md#section183721115521) in **Placing AR Objects**.

## Creating an AR Session

Create an AR session and set **ARType** to image tracking.

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Set ARType to ARENGINE\_TYPE\_IMAGE.
HMS\_AREngine\_ARConfig\_SetARType(arSession, arConfig, ARENGINE\_TYPE\_IMAGE);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

## Creating a Tracking Image Database and Add Images

1\. Call [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section4108822184411) to create a tracking image database.

// Create a tracking image database.
AREngine\_ARAugmentedImageDatabase \*mDataBase = nullptr;
HMS\_AREngine\_ARAugmentedImageDatabase\_Create(&mDataBase);

2\. Call [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section0315115618403) to add an image to the database. Save the failure result to **reason**.

// Add an image to the database.
AREngine\_ARAddAugmentedImageReason reason = ARENGINE\_ADD\_AUGMENTED\_IMAGE\_REASON\_NONE;
AREngine\_ARAugmentedImageSource image;
uint32\_t outputIndex = 0;
// Construct image based on the input image. For details, see the sample code.
auto addRet = HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage(mDataBase, &image, &outputIndex, &reason);

## Identifying Trackable Images in the Environment

Call [HMS\_AREngine\_ARSession\_GetAllTrackables](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gac5b39338f95317671d8de6d4f409cf9c) to detect all tracking images in the current environment. The result is stored in **augmentList**.

AREngine\_ARTrackableList \*augmentList = nullptr;
HMS\_AREngine\_ARTrackableList\_Create(arSession, &augmentList);
HMS\_AREngine\_ARSession\_GetAllTrackables(arSession, ARENGINE\_TRACKABLE\_AUGMENTED\_IMAGE, augmentList);

## Obtaining the Number of Trackable Images in the Environment

Call [HMS\_AREngine\_ARTrackableList\_GetSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gad9729d4436f3d969286f31b33d07513e) to obtain the number of planes. The result is stored in **augmentSize**.

int32\_t augmentSize = 0;
HMS\_AREngine\_ARTrackableList\_GetSize(arSession, augmentList, &augmentSize);

In the app environment, there may be zero, one, or more trackable images.

**augmentSize** = **0**: no trackable image in the current environment

**augmentSize** = **1**: one trackable image in the current environment

**augmentSize** > **1**: more than one trackable image in the current environment

## Example of Obtaining Tracking Images

When one or more tracking images are detected, traversing **augmentList** can obtain all tracking images.

for (int i = 0; i < augmentSize; ++i) {
    // Traverse all trackable objects and process them as required.
}

Create and obtain a tracking object for the _i_th tracking image, and convert it into a tracking image object [AREngine\_ARAugmentedImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section68491824155217).

AREngine\_ARTrackable \*augment = nullptr;
HMS\_AREngine\_ARTrackableList\_AcquireItem(arSession, augmentList, i, &augment);
AREngine\_ARAugmentedImage \*arImage = reinterpret\_cast<AREngine\_ARAugmentedImage\*>(augment);

## Obtaining the Pose Information of the Center Point of a Tracking Image in the World Coordinate System

Call [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section498975343520) to obtain the pose information of the center point of a tracking image. For details about pose information, please refer to [Obtaining the Device Pose](../obtaining-the-device-pose/document.md).

AREngine\_ARPose \*imagePose = nullptr;
HMS\_AREngine\_ARPose\_Create(arSession, nullptr, 0, &imagePose);
HMS\_AREngine\_ARAugmentedImage\_GetCenterPose(arSession, arImage, imagePose);

## Obtaining the Width of a Tracking Image

Call [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section917593011382) to obtain the estimated value on the X axis based on the center point of the image (coordinate origin) and the physical image width (unit: m).

float extent\_x;
HMS\_AREngine\_ARAugmentedImage\_GetExtendX(arSession, arImage, &extent\_x);

Call [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section9630192711390) to obtain the estimated value on the Z axis based on the center point of the image (coordinate origin) and the physical image width (unit: m).

float extent\_z;
HMS\_AREngine\_ARAugmentedImage\_GetExtendZ(arSession, arImage, &extent\_z);
