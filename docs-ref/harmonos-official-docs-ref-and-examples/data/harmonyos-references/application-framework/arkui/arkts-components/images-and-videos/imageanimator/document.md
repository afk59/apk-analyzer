# ImageAnimator

The **ImageAnimator** component enables images to be played a frame-by-frame basis. The list of images to be played as well as the duration of each image can be configured.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/g4k-bKz2TJqTIKwLp7aNJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0515B389CD70B7AFEB381E8E3D578BF1287F248E0EDD0461EC6D74D0C686C209)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

ImageAnimator()

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]images

images(value: Array<ImageFrameInfo>)

Sets image frame information. Dynamic update is not supported.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[ImageFrameInfo](#imageframeinfo)\> | Yes | 
Image frame information. The information of each frame includes the path, size, position, and playback duration of an image. For details, see [ImageFrameInfo](#imageframeinfo).

Default value: **\[\]**

Note: If the input array is too large, memory usage may increase. Therefore, as the controller of memory usage, be sure to assess potential memory consumption before passing in the data to avoid issues such as insufficient memory.

 |

#### \[h2\]state

state(value: AnimationStatus)

Sets the playback state of the animation.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AnimationStatus](../../common-definitions/enums/document.md#animationstatus) | Yes | 
Playback state of the animation.

Default value: **AnimationStatus.Initial**

 |

#### \[h2\]duration

duration(value: number)

Sets the playback duration. This attribute does not take effect when a separate duration is set for any of the image frames.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Playback duration.

If the value is **0**, no image is played.

If the display duration allocated per image is shorter than a single frame interval, playback anomalies may occur.

If it is set to a negative value, the default value is used.

The value change takes effect only at the start of the next cycle.

Unit: ms

Default value: **1000**

 |

#### \[h2\]reverse

reverse(value: boolean)

Sets the playback direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Playback direction.

The value **false** indicates that images are played from the first one to the last one, and **true** indicates that images are played from the last one to the first one.

Default value: **false**

 |

#### \[h2\]fixedSize

fixedSize(value: boolean)

Sets whether the image size is fixed at the component size.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the image size is fixed at the component size.

**true**: The image size is fixed at the component size. In this case, the width, height, top, and left attributes of the image are invalid.

**false**: The width, height, top, and left attributes of each image must be set separately. If the image size does not match the component size, the image will not be stretched.

Default value: **true**

 |

#### \[h2\]preDecode(deprecated)

preDecode(value: number)

Sets the number of images to be pre-decoded.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/GtZTK4-ZQo-fdz-WW-17vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07DCC5D404ABA435B32B8A2359588E9984B4A38ABFA7DF8D8FEF58677A312666)

This API is supported since API version 7 and deprecated since API version 9. Currently, no substitute is available.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Number of images to be pre-decoded. For example, the value **2** indicates that two images following the currently playing one are pre-decoded.

Default value: **0**

 |

#### \[h2\]fillMode

fillMode(value: FillMode)

Sets the status before and after execution of the animation in the current playback direction. The status after execution of the animation is jointly determined by the **fillMode** and **reverse** attributes. For example, if **fillMode** is set to **Forwards**, the target will retain the state defined by the last keyframe encountered during execution. In this case, if **reverse** is set to **false**, the target will retain the state defined by the last keyframe encountered in the forward direction, that is, the last image; if **reverse** is set to **true**, the target will retain the state defined by the last keyframe encountered in the backward direction, that is, the first image.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [FillMode](../../common-definitions/enums/document.md#fillmode) | Yes | 
Status before and after execution of the animation in the current playback direction.

Default value: **FillMode.Forwards**

 |

#### \[h2\]iterations

iterations(value: number)

Sets the number of times that the animation is played.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
By default, the animation is played once. The value **\-1** indicates that the animation is played for an unlimited number of times. Values less than **\-1** are treated as the default value. When the value is a floating-point number, it is rounded down.

Default value: **1**

 |

#### \[h2\]monitorInvisibleArea17+

monitorInvisibleArea(monitorInvisibleArea: boolean)

Sets whether the component should automatically pause or resume based on its visibility, using the system's [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange) event.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| monitorInvisibleArea | boolean | Yes | 
Whether the component should automatically pause or resume based on its visibility, using the system's [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange) event.

With the value **true**, when the component's [AnimationStatus](../../common-definitions/enums/document.md#animationstatus) is **Running**, the component automatically pauses once it becomes invisible and resumes playback if it becomes visible again, based on the **onVisibleAreaChange** event.

With the value **false**, the pause and playback of the component are not affected by **onVisibleAreaChange**.

Default value: **false**

**NOTE**

When this parameter is dynamically changed from **true** to **false**, the component will resume from its last paused state based on the current [AnimationStatus](../../common-definitions/enums/document.md#animationstatus).

Changes to this property do not affect the custom [state](#state) value.

 |

#### ImageFrameInfo

Image frame information set.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | string | [Resource](../../common-definitions/basic-types/document.md#resource)9+ | [PixelMap](../image-analysis-types/document.md#pixelmap)12+ | No | No | 
Image path. The image format can be .jpg, .jpeg, .svg, .png, .bmp, .webp, .ico, or .heif. The [Resource](../../common-definitions/basic-types/document.md#resource) type is supported since API version 9, and the [PixelMap](../image-analysis-types/document.md#pixelmap) type is supported since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| width | number | string | No | Yes | 

Image width. When the value is a string, it can represent a numeric value with or without units, for example, **"2"** or **"2px"**.

Default value: **0**

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| height | number | string | No | Yes | 

Image height. When the value is a string, it can represent a numeric value with or without units, for example, **"2"** or **"2px"**.

Default value: **0**

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| top | number | string | No | Yes | 

Vertical coordinate of the image relative to the upper left corner of the component. When the value is a string, it can represent a numeric value with or without units, for example, **"2"** or **"2px"**.

Default value: **0**

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| left | number | string | No | Yes | 

Horizontal coordinate of the image relative to the upper left corner of the component. When the value is a string, it can represent a numeric value with or without units, for example, **"2"** or **"2px"**.

Default value: **0**

Unit: vp

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| duration | number | No | Yes | 

Playback duration of each image frame, in milliseconds.

Default value: **0**

Negative numbers are not supported. Setting negative values will cause the image to stay in the current frame for a long time, affecting normal playback.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onStart

onStart(event: () => void)

Triggered when the animation starts to play.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the animation starts to play. |

#### \[h2\]onPause

onPause(event: () => void)

Triggered when the animation playback is paused.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the animation playback is paused. |

#### \[h2\]onRepeat

onRepeat(event: () => void)

Triggered when the animation playback is repeated.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the animation playback is repeated. |

#### \[h2\]onCancel

onCancel(event: () => void)

Triggered when the animation playback returns to the initial state.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the animation playback returns to the initial state. |

#### \[h2\]onFinish

onFinish(event: () => void)

Triggered when the animation playback completes or stops.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback triggered when the animation playback completes or stops. |

#### Example

## Example 1: Playing an Animation Using Images of the Resource Type

This example demonstrates how to play an animation using the **ImageAnimator** component with images of the Resource type.

// xxx.ets
@Entry
@Component
struct ImageAnimatorExample {
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images(\[
          {
            // Replace $r('app.media.img1') with the image resource file you use.
            src: $r('app.media.img1')
          },
          {
            // Replace $r('app.media.img2') with the image resource file you use.
            src: $r('app.media.img2')
          },
          {
            // Replace $r('app.media.img3') with the image resource file you use.
            src: $r('app.media.img3')
          },
          {
            // Replace $r('app.media.img4') with the image resource file you use.
            src: $r('app.media.img4')
          }
        \])
        .duration(4000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start')
        })
        .onPause(() => {
          console.info('Pause')
        })
        .onRepeat(() => {
          console.info('Repeat')
        })
        .onCancel(() => {
          console.info('Cancel')
        })
        .onFinish(() => {
          console.info('Finish')
          this.state = AnimationStatus.Stopped
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused // Display the image of the current frame.
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped // Display the image of the initial frame.
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1 // The animation is played for an unlimited number of times.
        }).margin(5)
      }
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/m6cvgZeZR6Ka0kpCnPQFyw/en-us_image_0000002568685437.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC8250149C01F1886EBE4E2A156796819D5F645EC1EF172787593496161FD8EE)

## Example 2: Playing an Animation Using Images of the PixelMap Type

This example demonstrates how to play an animation using the **ImageAnimator** component with images of the PixelMap type.

// xxx.ets
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageAnimatorExample {
  imagePixelMap: Array<PixelMap> = \[\];
  @State state: AnimationStatus = AnimationStatus.Initial;
  @State reverse: boolean = false;
  @State iterations: number = 1;
  @State images: Array<ImageFrameInfo> = \[\];

  async aboutToAppear() {
    // Replace $r('app.media.1') with the image resource file you use.
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.1')));
    // Replace $r('app.media.2') with the image resource file you use.
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.2')));
    // Replace $r('app.media.3') with the image resource file you use.
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.3')));
    // Replace $r('app.media.4') with the image resource file you use.
    this.imagePixelMap.push(await this.getPixmapFromMedia($r('app.media.4')));
    this.images.push({ src: this.imagePixelMap\[0\] });
    this.images.push({ src: this.imagePixelMap\[1\] });
    this.images.push({ src: this.imagePixelMap\[2\] });
    this.images.push({ src: this.imagePixelMap\[3\] });
  }

  build() {
    Column({ space: 10 }) {
      ImageAnimator()
        .images(this.images)
        .duration(2000)
        .state(this.state)
        .reverse(this.reverse)
        .fillMode(FillMode.None)
        .iterations(this.iterations)
        .width(340)
        .height(240)
        .margin({ top: 100 })
        .onStart(() => {
          console.info('Start');
        })
        .onPause(() => {
          console.info('Pause');
        })
        .onRepeat(() => {
          console.info('Repeat');
        })
        .onCancel(() => {
          console.info('Cancel');
        })
        .onFinish(() => {
          console.info('Finish');
          this.state = AnimationStatus.Stopped;
        })
      Row() {
        Button('start').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Running;
        }).margin(5)
        Button('pause').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Paused; // Display the image of the current frame.
        }).margin(5)
        Button('stop').width(100).padding(5).onClick(() => {
          this.state = AnimationStatus.Stopped; // Display the image of the initial frame.
        }).margin(5)
      }

      Row() {
        Button('reverse').width(100).padding(5).onClick(() => {
          this.reverse = !this.reverse;
        }).margin(5)
        Button('once').width(100).padding(5).onClick(() => {
          this.iterations = 1;
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.iterations = -1; // The animation is played for an unlimited number of times.
        }).margin(5)
      }
    }.width('100%').height('100%')
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    });
    await imageSource.release();
    return createPixelMap;
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/8IIltvVBSwKeWQByI9q9NQ/en-us_image_0000002568765447.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64C8A89B7AE86334E00C3874D0D9832DD617A32DDAC989917DCC533C3357AAE1)

## Example 3: Enabling Automatic Pause on Invisibility

This example demonstrates how to use [monitorInvisibleArea](#monitorinvisiblearea17) to automatically pause the **ImageAnimator** component when it becomes invisible and resume playback when it becomes visible again. This behavior is controlled based on the component's [state](#state) being set to **AnimationStatus.Running**.

@Entry
@Component
struct ImageAnimatorAutoPauseTest {
  scroller: Scroller = new Scroller();
  @State state: AnimationStatus = AnimationStatus.Running;
  @State reverse: boolean = false;
  @State iterations: number = 100;
  @State preCallBack: string = 'Null';
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Scroll(this.scroller) {
        Column() {
          ImageAnimator()
            .images(\[
              {
                // Replace $r('app.media.Clouds') with the image resource file you use.
                src: $r('app.media.Clouds')
              },
              {
                // Replace $r('app.media.landscape') with the image resource file you use.
                src: $r('app.media.landscape')
              },
              {
                // Replace $r('app.media.sky') with the image resource file you use.
                src: $r('app.media.sky')
              },
              {
                // Replace $r('app.media.mountain') with the image resource file you use.
                src: $r('app.media.mountain')
              }
            \])
            .borderRadius(10)
            .monitorInvisibleArea(true)
            .clip(true)
            .duration(4000)
            .state(this.state)
            .reverse(this.reverse)
            .fillMode(FillMode.Forwards)
            .iterations(this.iterations)
            .width(340)
            .height(240)
            .margin({ top: 100 })
            .onStart(() => {
              this.preCallBack = 'Start';
              console.info('ImageAnimator Start');
            })
            .onPause(() => {
              this.preCallBack = 'Pause';
              console.info('ImageAnimator Pause');
            })
            .onRepeat(() => {
              console.info('ImageAnimator Repeat');
            })
            .onCancel(() => {
              console.info('ImageAnimator Cancel');
            })
            .onFinish(() => {
              console.info('ImageAnimator Finish');
            })
          ForEach(this.arr, (item: number) => {
            Text(item.toString())
              .width('90%')
              .height(150)
              .backgroundColor(0xFFFFFF)
              .borderRadius(15)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .margin({ top: 10 })
          }, (item: string) => item)
        }.width('100%')
      }
      .scrollable(ScrollDirection.Vertical) // The scrollbar scrolls in the vertical direction.
      .scrollBar(BarState.On) // The scrollbar is always displayed.
      .scrollBarColor(Color.Gray) // The scrollbar color is gray.
      .scrollBarWidth(10) // The scrollbar width is 10.
      .friction(0.6)
      .edgeEffect(EdgeEffect.None)
      .onWillScroll((xOffset: number, yOffset: number, scrollState: ScrollState) => {
        console.info(xOffset + ' ' + yOffset);
      })
      .onScrollEdge((side: Edge) => {
        console.info('To the edge');
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
      })

      Text('Last triggered callback (Pause/Start):' + this.preCallBack)
        .margin({ top: 60, left: 20 })
    }.width('100%').height('100%').backgroundColor(0xDCDCDC)
  }
}
