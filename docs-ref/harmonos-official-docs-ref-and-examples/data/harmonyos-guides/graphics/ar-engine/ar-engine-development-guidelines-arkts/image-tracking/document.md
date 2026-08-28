# Image Tracking

#### Overview

AR Engine supports this capability since version 5.1.0(18).

This section describes how to recognize 2D images and track their pose information, and provides instructions on how to detect whether the input image exists in the scene and, once recognized, output its pose data.

**Figure 1** Image tracking

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/bJ7aC2EKSUW9TvzEE7dM_A/en-us_image_0000002532146187.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062046Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F64533B145CBBF0C85FD8405AAA7C2D7CF75C2447F36859F4F44B88F85742D2)

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)

#### API Description

Image recognition mainly depends on [ARAugmentedImageDatabase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1410345414514) and [ARImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section3211104815419). The following table lists the APIs related to image recognition. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-arkts-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[arEngine.createARAugmentedImageDatabase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section204881041154517)

 | 

Creates an augmented image database.

 |
| 

[ARAugmentedImageDatabase.deserialize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section11965134812716)

 | 

Deserializes the buffer of the augmented image database to a new augmented image database object.

 |
| 

[ARAugmentedImageDatabase.serialize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section18164121486)

 | 

Serializes the augmented image database into a buffer.

 |
| 

[ARAugmentedImageDatabase.addImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section9315052814)

 | 

Adds an image to the image database and outputs the index of the image.

 |
| 

[ARAugmentedImageDatabase.getImageCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section106577102812)

 | 

Obtains the number of images in the image database.

 |
| 

[ARAugmentedImageDatabase.getCapacity](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section87071617088)

 | 

The maximum number of images that can be added.

 |
| 

[ARAugmentedImageDatabase.getImageAddMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section121563216515)

 | 

Obtains the image adding mode.

 |
| 

[ARAugmentedImageDatabase.setImageAddMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section15149542135910)

 | 

Sets the image adding mode.

 |
| 

[ARAugmentedImageDatabase.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section72331823587)

 | 

Releases the memory occupied by the [ARAugmentedImageDatabase](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1410345414514) object.

 |
| 

[ARImage.release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1060545815466)

 | 

Releases the memory occupied by the [ARImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section3211104815419) camera video stream frame object.

 |
| 

[ARAugmentedImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arengine#section1570811755212)

 | 

Indicates a trackable augmented image object.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts) to access the complete demo code.

The AR Engine only outputs data for detected planes. To enhance observation, you can use either the Ark Graphics Platform (AGP) rendering engine or [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to draw the identified planes. For details about AGP, please refer to the [introduction to ArkGraphics 3D](../../../arkgraphics-3d/about-this-kit/document.md) and [AGP Engine](https://gitcode.com/openharmony/graphic_graphic_3d).

For any AR app built with ArkTS, it is first necessary to create an AR session [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519), to manage the system status of the AR Engine. For details about how to create an [ARViewContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section12681656121519) for an AR session, please refer to [Managing AR Sessions](../managing-ar-sessions/document.md).

## Creating a UI

Start by creating an initial UI page, **ARImage.ets**, and add two buttons: one for adding a local image (**ARImageByAdd.ets**) and the other for reading from the local database (**ARImageByDatabase.ets**). Also configure routing for navigation between pages. For detailed page routing configurations, please refer to [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).

## ARImage Page

// ARImage.ets
// Import the image module.
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Builder
export function ARImageBuilder(): void {
  ARImage();
}

@Component
struct ARImage {
  pageInfo: NavPathStack = new NavPathStack();

  // UI configuration.
  build(): void {
    NavDestination() {
      Column() {
        Button('Select local image', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {
            await this.chooseImageToTrack();
          })

        Button('Load local database', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.loadDatabaseToTrack();
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

  // Select the local image mode.
  private async chooseImageToTrack(): Promise<void> {
    try {
      let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
      photoOption.maxSelectNumber = 50; // Default
      photoOption.isEditSupported = false;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

      await photoPicker.select(photoOption).then((photoResult) => {
        if (photoResult.photoUris.length > 0 && photoResult.photoUris\[0\].length > 0) {
          this.pageInfo.pushDestinationByName('ARImageByAdd', photoResult.photoUris).catch((error: BusinessError) => {
            console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
          });
        }
      }).catch((error: BusinessError) => {
        // ...
      })
    } catch (error) {
      console.error(\`Failed to select by photoPicker. Code: ${error.code}.\`);
    }
  }

  // Load the local database.
  private loadDatabaseToTrack(): void {
    this.pageInfo.pushDestinationByName('ARImageByDatabase', null).catch((error: BusinessError) => {
      console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
    });
  }
}

## ARImageByAdd Page

Load the local image mode.

1.  The following are modules required for enabling image recognition for local images.
    
    // ARImageByAdd.ets
    
    import { arEngine, ARView, arViewController } from '@kit.AREngine';
    import { Node, Scene } from '@kit.ArkGraphics3D';
    import { collections } from '@kit.ArkTS';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo } from '@kit.CoreFileKit';
    import { image } from '@kit.ImageKit';
    
2.  Configure the page routing information, and define **dataBase**.
    
    // ARImageByAdd.ets
    
    // Page routing
    @Builder
    export function ARImageByAddBuilder(): void {
      ARImageByAdd();
    }
    
    let dataBase: arEngine.ARAugmentedImageDatabase;
    
3.  On the device UI, display the image addition status. If no images are available, display a pop-up prompt. Load the AR scene.
    
    // ARImageByAdd.ets
    
    @Component
    struct ARImageByAdd {
      pageInfo: NavPathStack = new NavPathStack();
      private imagePathArray: string\[\] = \[\];
      private isProgramExits: boolean = false;
      private isSaveDatabase: boolean = false;
      @State arContext?: arViewController.ARViewContext = undefined;
      @State context: Context = this.getUIContext().getHostContext() as Context;
      @State totalImageCounts: number = this.imagePathArray.length;
      @State addFailedImageCounts: number = 0;
      @State succeedImageCounts: number = 0;
      @State addFailedMessage: string\[\] = \[\];
    
      build(): void {
        NavDestination() {
          RelativeContainer() {
            Column() {
              Text(\`Image adding progress: ${this.succeedImageCounts + this.addFailedImageCounts} / ${this.totalImageCounts}\`)
              Text(\`Number of images added successfully: ${this.succeedImageCounts}\`)
              Text(\`Number of images that failed to add: ${this.addFailedImageCounts}\`)
    
              if (this.addFailedMessage) {
                ForEach(this.addFailedMessage, (item: string) => {
                  Text(\`${item}\`)
                    .fontColor(Color.Red)
                })
              }
            }
            .visibility(this.addFailedImageCounts + this.succeedImageCounts < this.totalImageCounts ? Visibility.Visible :
            Visibility.None)
            .foregroundColor(Color.Red)
            .zIndex(1)
            .alignRules({
              center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
              middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
            })
    
            if (this.arContext) {
              ARView({ context: this.arContext })
                .height('100%')
                .width('100%')
                .alignRules({
                  center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
                  middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
                })
            }
          }
        }
        // Create the database, load local cache, initialize the AR scene, and start the AR session.
        .onAppear(async () => {
          await arEngine.createARAugmentedImageDatabase()
            .then(async (arDataBase) => {
              dataBase = arDataBase;
    
              await this.addImage(dataBase).then(() => {
                if (this.addFailedImageCounts === this.totalImageCounts) {
                  this.ShowDialog('Please add a valid image.');
                }
                this.initARView();
              })
            })
            .catch((error: BusinessError) => {
              console.error(\`Failed to create AR Augmented Database.Code is ${error.code}, message is ${error.message}\`);
            });
        })
        .onWillDisappear(async () => {
          await this.stopARView();
        })
        .onShown(() => {
          this.resumeARView();
        })
        .onHidden(() => {
          this.pauseARView();
        })
        .onReady((context: NavDestinationContext) => {
          this.pageInfo = context.pathStack;
          this.imagePathArray = context.pathInfo.param as string\[\];
          this.totalImageCounts = this.imagePathArray.length;
        })
        .hideTitleBar(true)
        .hideBackButton(true)
        .hideToolBar(true)
      }
    
      // Initialize the AR scene and create an AR session.
      private initARView(): void {
        Scene.load().then((scene: Scene) => {
          let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
          viewContext.scene = scene;
          viewContext.callback = new ARViewCallbackImpl();
          viewContext.config = {
            type: arEngine.ARType.IMAGE,  // Use image tracking mode.
            planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL\_AND\_VERTICAL,
            powerMode: arEngine.ARPowerMode.NORMAL,
            semanticMode: arEngine.ARSemanticMode.NONE,
            poseMode: arEngine.ARPoseMode.GRAVITY,
            depthMode: arEngine.ARDepthMode.AUTOMATIC,
            meshMode: arEngine.ARMeshMode.DISABLED,
            focusMode: arEngine.ARFocusMode.AUTO
          }
          viewContext.init().then(() => {
            this.arContext = viewContext;
            console.info('Succeeded in initializing ARView.');
          }).catch((err: BusinessError) => {
            console.error(\`Failed to init ARView. Code is ${err.code}, message is ${err.message}.\`);
          })
        })
      }
    
      private async stopARView(): Promise<void> {
        if (!this.arContext) {
          return;
        }
        try {
          this.isProgramExits = true;
          if (this.isSaveDatabase) {
            SaveBufferToLocal(dataBase, this.context);
          }
    
          await dataBase.release();
          await this.arContext?.destroy();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(\`Failed to stop context. Code is ${err.code}, message is ${err.message}\`);
        }
      }
    
      private resumeARView(): void {
        // ...
      }
      private pauseARView(): void {
        // ...
      }
    
      // Execute the image addition task asynchronously.
      async addImage(dataBase: arEngine.ARAugmentedImageDatabase): Promise<void> {
        for (let index = 0; index < this.totalImageCounts; index++) {
          const imagePath: string = this.imagePathArray\[index\];
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
            console.error(\`Failed to closeSync. Code: ${err.code}.\`);
            this.addFailedImageCounts += 1;
            continue;
          }
          const imageInfo: image.ImageInfo = imageSourceApi.getImageInfoSync(0);
          if (!imageInfo) {
            console.error('Failed to obtain the image pixel map information.');
            this.addFailedImageCounts += 1;
            continue;
          }
          const opts: image.DecodingOptions = {
            editable: true,
            desiredPixelFormat: image.PixelMapFormat.RGBA\_8888,
            desiredSize: { width: imageInfo.size.width, height: imageInfo.size.height }
          }
          let pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync(opts);
    
          if (this.isProgramExits) {
            break;
          }
    
          await dataBase.addImage(imageName, pixelMap, 10).then((result: arEngine.ARAddAugmentedImageResult) => {
            console.info(\`The imageResult: ${result.index} ${result.stateReason}.\`);
            if (result.stateReason !== arEngine.ARAddAugmentedImageReason.NONE) {
              this.addFailedImageCounts += 1;
              this.addFailedMessage.push('Name of the failed image:' + imageName + 'Failure cause:' + errcode.get(result.stateReason) + ' ');
            } else {
              this.succeedImageCounts += 1;
            }
          }).catch(() => {
            this.addFailedImageCounts += 1;
          })
    
          await imageSourceApi.release();
          await pixelMap.release();
        }
      }
    
      // Customized pop-up prompt.
      ShowDialog(msg: string): void {
        this.getUIContext().showAlertDialog(
          {
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
                console.info('Callback when the second button is clicked.');
                this.pageInfo.pop();
                return;
              }
            }\]
          })
        }
      }
    
4.  Upon exiting the app, store image features in the local cache.
    
    // ARImageByAdd.ets
    
    async function SaveBufferToLocal(dataBase: arEngine.ARAugmentedImageDatabase, context: Context): Promise<void> {
      let filesDir: string = context.filesDir;
      let file: fileIo.File;
      try {
        file = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
      } catch (e) {
        // ...
      }
      let buf: ArrayBuffer;
      try {
        buf = await dataBase.serialize()
      } catch (error) {
        // ...
        return;
      }
      let writeLen: number = fileIo.writeSync(file.fd, buf);
      console.info(\`The length of buffer is: ${writeLen}\`);
      try {
        fileIo.closeSync(file);
      } catch (error) {
        // ...
      }
    }
    
5.  Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data. If the target image is recognized, a log is printed.
    
    // ARImageByAdd.ets
    
    class ARViewCallbackImpl extends arViewController.ARViewCallback {
      onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
        // ...
      }
    
      onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
        // ...
      }
    
      onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
        if (!ctx.session || !dataBase) {
          return;
        }
    
        let session: arEngine.ARSession = ctx.session; // Obtain the AR session.
    
        try {
          let imageNumber: number = dataBase.getImageCount();
          console.info(\`The number of images in the database is ${imageNumber}.\`);
    
          let imageCapacity: number = dataBase.getCapacity();
          console.info(\`The dataBase image capacity is: ${imageCapacity}.\`);
    
          let trackable: arEngine.ARTrackable\[\] = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED\_IMAGE);
    
          console.info(\`The image trackable size: ${trackable.length}.\`);
          for (let i = 0; i < trackable.length; ++i) {
            if (trackable\[i\].type === arEngine.ARTrackableType.AUGMENTED\_IMAGE) {
              let arimage: arEngine.ARAugmentedImage = trackable\[i\] as arEngine.ARAugmentedImage;
              if (arEngine.ARTrackingState.TRACKING !== arimage.state) {
                continue;
              }
              let centerPose: arEngine.ARPose = arimage.getPose();
              console.info(\`The image width: ${arimage.extendX}, height: ${arimage.extendZ}, pose: ${centerPose.getMatrix()}.\`);  // Print target image information.
            }
          }
    
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(\`Failed to got image count. Code is ${err.code}, message is ${err.message}\`);
        }
      }
    }
    
    // Reasons for image addition failure.
    const errcode: collections.Map<number, string> = new collections.Map<number, string>(\[
      \[0, 'success'\],
      \[1, 'size not match'\],
      \[2, 'too bright or too dark'\],
      \[3, 'image color is relatively single'\],
      \[4, 'other error'\]
    \])
    

## ARImageByDatabase Page

Load the local database.

1.  The following modules need to be imported to enable image recognition using the local database:
    
    // ARImageByDatabase.ets
    
    import { arEngine, ARView, arViewController } from '@kit.AREngine';
    import { Node, Scene } from '@kit.ArkGraphics3D';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo, ReadOptions } from '@kit.CoreFileKit';
    
2.  Configure the page routing information, and define **dataBase**.
    
    // ARImageByDatabase.ets
    
    // Page routing
    @Builder
    export function ARImageByDatabaseBuilder(): void {
      ARImageByDatabase();
    }
    
    let dataBase: arEngine.ARAugmentedImageDatabase;
    
3.  Load the AR scene and image database. If no available database is found, display a pop-up prompt.
    
    // ARImageByDatabase.ets
    
    @Component
    struct ARImageByDatabase {
      pageInfo: NavPathStack = new NavPathStack();
      @State arContext?: arViewController.ARViewContext = undefined;
      @State context: Context = this.getUIContext().getHostContext() as Context;
    
      build() {
        NavDestination() {
          RelativeContainer() {
            if (this.arContext) {
              ARView({ context: this.arContext })
                .height('100%')
                .width('100%')
                .alignRules({
                  center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
                  middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
                })
            }
          }
        }
        // Create the database, load local cache, initialize the AR scene, and start the AR session.
        .onAppear(() => {
          arEngine.createARAugmentedImageDatabase()
            .then((arDataBase) => {
              dataBase = arDataBase;
    
              try {
                let databaseBuffer: ArrayBuffer = ReadBuffer(this.context);
                dataBase.deserialize(databaseBuffer).then(() => {
                  this.initARView();
                })
              } catch (error) {
                const err: BusinessError = error as BusinessError;
                console.error(\`Failed to init context. Code is ${err.code}, message is ${err.message}.\`);
                this.ShowDialog('Please add a valid image.');
              }
            })
            .catch((error: BusinessError) => {
              console.error(\`Failed to create AR Augmented Database.Code is ${error.code}, message is ${error.message}\`);
            });
        })
        .onWillDisappear(async () => {
          await this.stopARView();
        })
        .onShown(() => {
          this.resumeARView();
        })
        .onHidden(() => {
          this.pauseARView();
        })
        .onReady((context: NavDestinationContext) => {
          this.pageInfo = context.pathStack;
        })
        .hideTitleBar(true)
        .hideBackButton(true)
        .hideToolBar(true)
      }
    
      // Initialize the AR scene and create an AR session.
      private initARView(): void {
        Scene.load().then((scene: Scene) => {
          let context: arViewController.ARViewContext = new arViewController.ARViewContext();
          context.scene = scene;
          context.callback = new ARViewCallbackImpl();
          context.config = {
            type: arEngine.ARType.IMAGE,  // Use image tracking mode.
            planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL\_AND\_VERTICAL,
            powerMode: arEngine.ARPowerMode.NORMAL,
            semanticMode: arEngine.ARSemanticMode.NONE,
            poseMode: arEngine.ARPoseMode.GRAVITY,
            depthMode: arEngine.ARDepthMode.AUTOMATIC,
            meshMode: arEngine.ARMeshMode.ENABLE
          }
          context.init().then(() => {
            this.arContext = context;
            console.info('Succeeded in initializing ARView.');
          }).catch((err: BusinessError) => {
            console.error(\`Failed to init context. Code is ${err.code}, message is ${err.message}.\`);
          })
        })
      }
    
      private async stopARView(): Promise<void> {
        if (!this.arContext) {
          return;
        }
        try {
          await dataBase.release();
          await this.arContext?.destroy();
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(\`Failed to stop context. Code is ${err.code}, message is ${err.message}\`);
        }
      }
    
      private resumeARView(): void {
        // ...
      }
      private pauseARView(): void {
        // ...
      }
    
      // Customized pop-up prompt.
      ShowDialog(msg: string): void {
        this.getUIContext().showAlertDialog(
          {
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
                console.info('Callback when the second button is clicked.');
                this.pageInfo.pop();
                return;
              }
            }\]
          })
        }
      }
    
4.  Method for reading local database cache files.
    
    // ARImageByDatabase.ets
    
    function ReadBuffer(context: Context): ArrayBuffer {
      let filesDir: string = context.filesDir;
      let srcFile: fileIo.File;
      try {
        srcFile = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
        const fileStat: fileIo.Stat = fileIo.statSync(srcFile.fd);
      // Read data from the source file and copy it to the destination file.
        let readSize: number = 0;
        let buf: ArrayBuffer = new ArrayBuffer(fileStat.size);
        let readOptions: ReadOptions = {
          offset: readSize,
          length: fileStat.size
        }
        let readLen: number = fileIo.readSync(srcFile.fd, buf, readOptions);
        console.info(\`The length of buffer is: ${readLen}.\`);
        fileIo.closeSync(srcFile);
        return buf;
      } catch (e) {
        // ...
      }
    }
    
5.  Call [ARViewCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section9396615174614) and use its [onFrameUpdate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-api-arviewcontroller#section52341758194715) method to update frame data. If the target image is recognized, a log is printed.
    
    // ARImageByDatabase.ets
    
    class ARViewCallbackImpl extends arViewController.ARViewCallback {
      onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
        // ...
      }
    
      onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
        // ...
      }
    
      onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
        if (!ctx.session || !dataBase) {
          return;
        }
    
        let session: arEngine.ARSession = ctx.session;
    
        try {
          let imageNumber: number = dataBase.getImageCount();
          console.info(\`The number of images in the database is ${imageNumber}.\`);
    
          let imageCapacity: number = dataBase.getCapacity();
          console.info(\`The dataBase image capacity = ${imageCapacity}.\`);
    
          let trackable: arEngine.ARTrackable\[\] = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED\_IMAGE);
    
          console.info(\`The image trackable size: ${trackable.length}.\`);
          for (let i = 0; i < trackable.length; ++i) {
            if (trackable\[i\].type === arEngine.ARTrackableType.AUGMENTED\_IMAGE) {
              let arimage: arEngine.ARAugmentedImage = trackable\[i\] as arEngine.ARAugmentedImage;
              if (arEngine.ARTrackingState.TRACKING !== arimage.state) {
                continue;
              }
              let centerPose: arEngine.ARPose = arimage.getPose();
              console.info(\`The image width: ${arimage.extendX}, height: ${arimage.extendZ}, pose: ${centerPose.getMatrix()}.\`);  // Print target image information.
            }
          }
    
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(\`Failed to got image count. Code is ${err.code}, message is ${err.message}.\`);
        }
      }
    }
