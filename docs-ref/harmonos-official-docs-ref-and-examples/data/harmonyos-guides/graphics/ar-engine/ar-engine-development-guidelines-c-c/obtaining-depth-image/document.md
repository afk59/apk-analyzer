# Obtaining Depth Image

#### Overview

AR Engine supports this capability since version 5.0.5(17).

AR Engine's depth estimation feature utilizes algorithms to generate depth image data (an image representing the distance of object surface from the camera) and depth confidence map information, providing 3D environmental perception capabilities. This technology can be applied in scenarios such as measurement, volume estimation, and scene reconstruction to obtain spatial object depth information. Based on this data, various spatial computation tasks, like calculating object volumes, can be accomplished.

**Figure 1** Depth rendering  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/OmwLJYVtRIKju4XPZs1p0g/en-us_image_0000002500306270.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92E26DB05B1CD9029A80D91C25E96851768C78C4EDF3D375B799FA5B0DE62B70)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/hyP4N3BMQuWaXWJjcr3USA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05DC85D93AF4C7B3B24EEFB40E55F6E3827560A11BCFC418127E7D92918A7FCA)

This feature only provides functionality and does not constitute a guarantee of product quality or any commitment. For details, please refer to [AR Engine Depth Estimation Technology Limitations and Disclaimer](../../appendix/document.md#section1854314717219).

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (plane detection)

#### API Description

The following lists APIs used for AR depth estimation. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine).

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

Creates an [AREngine\_ARFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gaf35f728a1179ef54a3eba9f1cf021719) object and stores the pointer in _\*_**outFrame**.

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

[HMS\_AREngine\_ARConfig\_SetDepthMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section12608229155413)

 | 

Sets the depth mode.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section138574584154)

 | 

Obtains the depth image of the current frame.

 |
| 

[HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section4424501286)

 | 

Obtains the confidence information corresponding to the depth image of the current frame.

 |
| 

[HMS\_AREngine\_ARImage\_GetNativeBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section367418528228)

 | 

Obtains the NativeBuffer data of the current frame's image object.

 |

#### Development Procedure

This section provides only the key development steps. Click [here](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp) to access the complete demo code.

## Declaring Native APIs

For details, please refer to [Declaring Native APIs](../placing-ar-objects/document.md#section1557014318265) in **Placing AR Objects**.

## Creating a UI

Create a UI interface, **ARDepth.ets**, to allow users to choose whether to enable depth rendering.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARDepth.ets.
@Builder
export function ARDepthBuilder() {
  ARDepth();
}

@Component
struct ARDepth {
  pageInfo: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button('Disable depth rendering', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 0); // 0 indicates that rendering is disabled.
          })

        Button('Enable depth rendering', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushPathByName('ARDepthRender', 1); // 1 indicates that rendering is enabled.
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

Create **ARDepthRender.ets**, use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to load the camera preview, and periodically trigger the rendering of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARDepthRender.ets.
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARDepthRenderBuilder() {
  ARDepthRender();
}

@Component
struct ARDepthRender {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private isUpdate: boolean = true;
  private params: number = 0;
  private xComponentId = 'ARDepth';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State distance: string = '';
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // Update the calculation result of each frame by calling the native API update of AR Engine.
                arEngineDemo.update(this.xComponentId);
                this.distance = arEngineDemo.getDistance(this.xComponentId);
              }
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })

        Text(this.distance)
          .fontColor(Color.Yellow)
          .fontSize(24)
          .textShadow({
            radius: 10,
            color: Color.Black,
            offsetX: 0,
            offsetY: 0
          })
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Bottom },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[0, this.params, 1, this.rotation\]);
      arEngineDemo.start(this.xComponentId, config);
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
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
      this.params = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

}

Also configure routing for navigation between pages. For detailed page routing configurations, please refer to [Component Navigation (Navigation) (Recommended)](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md).

## Importing AR Engine

For details, please refer to [Importing AR Engine](../placing-ar-objects/document.md#section183721115521) in **Placing AR Objects**.

## Creating an AR Session

Create an AR session and enable depth mode.

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Enable depth mode.
HMS\_AREngine\_ARConfig\_SetDepthMode(arSession, arConfig, ARENGINE\_DEPTH\_MODE\_AUTOMATIC);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

## Obtaining the Depth Image in the Current Environment

Call [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section138574584154) to obtain depth information from the current environment. The result is stored in **depthImage**.

AREngine\_ARFrame \*arFrame = nullptr;
// Create an AR single-frame object.
HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
AREngine\_ARImage \*depthImage = nullptr;
// Obtain the depth image.
HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits(arSession, arFrame, &depthImage);
// Obtain the nativeBuffer of the depth image.
OH\_NativeBuffer\* depthBuffer;
HMS\_AREngine\_ARImage\_GetNativeBuffer(arSession, depthImage, &depthBuffer);

## Obtaining the Depth Confidence Map of the Current Depth Image

Call [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section4424501286) to obtain the depth confidence map of the current depth image.

AREngine\_ARFrame \*arFrame = nullptr;
// Create an AR single-frame object.
HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
AREngine\_ARImage \*depthConfidenceImage = nullptr;
// Obtain the depth confidence map.
HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage(arSession, arFrame, &depthConfidenceImage);
// Obtain the nativeBuffer of the depth confidence map.
OH\_NativeBuffer\* depthConfidenceBuffer;
HMS\_AREngine\_ARImage\_GetNativeBuffer(arSession, depthConfidenceImage, &depthConfidenceBuffer);

## Obtaining the Values of the Depth Image and Depth Confidence Map

The depth image and depth confidence map are wrapped as the [AREngine\_ARImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gabfee13b0076f2f00b7efdef2717add59) object, which can be used to obtain the corresponding depth image and depth confidence map.

AREngine\_ARImageFormat format;
// Obtain the data format of the current frame.
HMS\_AREngine\_ARImage\_GetFormat(arSession, depthImage, &format);
int32\_t depthWidth;
// Obtain the depth image width.
HMS\_AREngine\_ARImage\_GetWidth(arSession, depthImage, &depthWidth);
int32\_t depthHeight;
// Obtain the depth image height.
HMS\_AREngine\_ARImage\_GetHeight(arSession, depthImage, &depthHeight);
uint8\_t \*depthData = nullptr;
int32\_t depthLength = 0;
// Obtain the depth image data.
HMS\_AREngine\_ARImage\_GetPlaneData(arSession, depthImage, 0, (const uint8\_t \*\*)&depthData, &depthLength);

## Destroying the Depth Image and Depth Confidence Map When Finished

HMS\_AREngine\_ARImage\_Release(depthImage);
HMS\_AREngine\_ARImage\_Release(depthConfidenceImage);
