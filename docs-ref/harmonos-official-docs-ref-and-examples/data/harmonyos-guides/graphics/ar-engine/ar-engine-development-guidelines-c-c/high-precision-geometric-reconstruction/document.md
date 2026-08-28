# High-Precision Geometric Reconstruction

#### Overview

AR Engine supports this capability since version 6.0.0(20).

This section describes how to use the high-precision geometric reconstruction of AR Engine to identify cube objects or embedded cube spaces in a space and calculate the length, width, height, and volume of the identified objects or spaces. This capability can be used to measure the volume of a cube and the size of an embedded space.

**Figure 1** Dense point cloud drawing  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/c-t7ou_kQDmMYaOoL5M5FA/en-us_image_0000002500306262.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7348B4A5B9D116C95889E572381FD546A7D99A2E1DB5C15EE9B2F580924A232D)

**Figure 2** Volume measurement  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/a2uKll9vSN2HQwoybsaTcg/en-us_image_0000002532306153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=119C11312274EB4A65C3FB48EE52838D238C451739F6E9FE3EAD63C822B8C939)

**Figure 3** Space recognition  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/M_skaSMcTGyvDKK5F6p53Q/en-us_image_0000002532146181.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB3DA4D0230FE33CB8C4134958182559A96723EE1A9D4F850C749FC195126F79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/41UWX0tDRPCUtVKxaja7rQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062047Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22300BA4F7E72D0316CEE1D57E7E8702E102A291406B5BF9414FDAA3449B9F73)

This feature only provides functionality and does not constitute a guarantee of product quality or any commitment. For details, please refer to [AR Engine High-Precision Geometric Reconstruction Limitations and Disclaimer](../../appendix/document.md#section68356131976).

AR Engine capabilities involved in this section:

-   Motion tracking
-   Environment tracking (point cloud recognition)
-   High-precision geometric reconstruction

#### API Description

The following lists APIs related to high-precision geometric reconstruction. For details about these APIs, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section17136162216547)

 | 

Obtains the high-precision geometric reconstruction object data of the current frame.

 |
| 

[HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section1099254315514)

 | 

Obtains the set high-precision geometric reconstruction mode.

 |
| 

[HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section1569718841012)

 | 

Sets the high-precision geometric reconstruction mode.

 |
| 

[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section7554459949)

 | 

Obtains the cube data in the recognized high-precision geometric reconstruction object data.

 |
| 

[HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section383013458212)

 | 

Obtains the cube count in the recognized high-precision geometric reconstruction object data.

 |
| 

[HMS\_AREngine\_ARSemanticDense\_Release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section390280482)

 | 

Releases a high-precision geometric reconstruction object.

 |

#### Development Procedure

## Declaring Native APIs

For details, please refer to [Declaring Native APIs](../placing-ar-objects/document.md#section1557014318265) in **Placing AR Objects**.

## Creating a UI

Create a UI, **ARSemanticDense.ets**, for setting the high-precision geometric reconstruction mode.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARSemanticDense.ets.
import { display} from '@kit.ArkUI';

@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense();
}

@Component
struct ARSemanticDense {
  pageInfo: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = display.getDefaultDisplaySync().rotation;
  @State volume: string = '';

  build() {
    NavDestination() {
      Column() {
        Button('Enable dense point cloud recognition', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 0).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
            });
          })

        Button('Enable volume measurement', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 1).catch((error: BusinessError) => {
              console.error(\`\[pushDestinationByName\]failed. Code: ${error.code}.\`);
            });
          })

        Button('Enable space measurement', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfo.pushDestinationByName('ARSemanticDenseRender', 2).catch((error: BusinessError) => {
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

Create **ARSemanticDenseRender.ets**, use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to load the camera preview, and periodically trigger the rendering of each frame.

// Refer to the sample code ARSample/entry/src/main/ets/pages/ARSemanticDenseRender.ets.
import { display } from '@kit.ArkUI';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARSemanticDenseRenderBuilder() {
  ARSemanticDenseRender();
}

@Component
struct ARSemanticDenseRender {
  pageInfo: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private xComponentId: string = 'ARSemanticDense';
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private interval: number = -1;
  private inputInterval: number = -1;
  private getCubeInfoInterval: number = -1;
  private isUpdate: boolean = false;
  private semanticDenseMode: number = 0;
  @State showPage: boolean = true;
  @State rotation: number = display.getDefaultDisplaySync().rotation;
  @State volume: string = '';

  build(): void {
    NavDestination() {
      RelativeContainer() {

        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .opacity(0.2)
          .width('100%')
          .height('100%')
          .zIndex(0.1)
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.xComponentId);
                if (this.semanticDenseMode != 0) {
                  this.volume = arEngineDemo.getVolume(this.xComponentId);
                }
              }
            }, 33) // Set the frame rate to 30 fps (refreshing a frame every 33 ms).
          })
          .onDestroy(() => {
            if (this.interval !== -1) {
              clearInterval(this.interval);
              this.interval = -1;
            }

            if (this.inputInterval !== -1) {
              clearInterval(this.inputInterval);
              this.inputInterval = -1;
            }

            if (this.getCubeInfoInterval !== -1) {
              clearInterval(this.getCubeInfoInterval);
              this.getCubeInfoInterval = -1;
            }
          })

        Text(this.volume)
          .fontColor(Color.Red)
          .fontSize(14)
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Bottom },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array(\[1,this.rotation, 2, this.semanticDenseMode\]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(async () => {
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
      this.semanticDenseMode = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

## Importing AR Engine

For details, please refer to [Importing AR Engine](../placing-ar-objects/document.md#section183721115521) in **Placing AR Objects**.

## Creating an AR Session and Setting the High-Precision Geometric Reconstruction Mode

AREngine\_ARSession \*arSession = nullptr;
// Create an AR session.
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);
AREngine\_ARConfig \*arConfig = nullptr;
// Create an AR session configurator.
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);
// Set the volume recognition option for the high-precision geometric reconstruction mode.
HMS\_AREngine\_ARConfig\_SetSemanticDenseMode(arSession, arConfig, ARENGINE\_SEMANTIC\_DENSE\_MODE\_CUBE\_VOLUME);
// Set the configurator for the AR session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

## Obtaining the High-Precision Geometric Reconstruction Information in the Current Environment

Create a frame object and call the [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section17136162216547) function to obtain the high-precision geometric reconstruction information in the current environment, which also includes the dense point cloud and cube data.

AREngine\_ARFrame \*arFrame = nullptr;
// Create an AR single-frame object.
HMS\_AREngine\_ARFrame\_Create(arSession, &arFrame);
AREngine\_ARSemanticDenseData \*arSemanticDense = nullptr;
// Obtain the dense point cloud information of the current frame.
HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData(arSession, arFrame, &arSemanticDense);

## Obtaining the Cube Data in the High-Precision Geometric Reconstruction Information

1\. Call the [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section7554459949) function to obtain the cube data in the current environment. For details about the cube data structure, please refer to [AREngine\_ARSemanticDenseCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata).

AREngine\_ARSemanticDenseCubeData \*semanticDenseCubeData = nullptr;
HMS\_AREngine\_ARSemanticDense\_AcquireCubeData(arSession, arSemanticDense, &semanticDenseCubeData);

2\. Call the [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#section383013458212) function to obtain the number of cubes in the current environment. If the number is greater than 0, you can obtain the data of a single cube for drawing and volume calculation.

int64\_t cubeDataSize = 0;
HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize(arSession, arSemanticDense, &cubeDataSize);

## Drawing Relevant Geometric Information

1\. Draw cubes through the obtained [AREngine\_ARSemanticDenseCubeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata) object.

// Determine the obtained cube data and quantity.
if (semanticDenseCubeData != nullptr && cubeDataSize > 0) {
    // Draw cubes.
    mCubeRenderer.Draw(projectionMat, viewMat, arSession, semanticDenseCubeData);
}
