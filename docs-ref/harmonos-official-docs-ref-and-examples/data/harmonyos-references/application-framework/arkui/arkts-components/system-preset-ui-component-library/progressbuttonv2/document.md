# ProgressButtonV2

The **ProgressButtonV2** component is a text-based download button with a progress indicator that shows the download progress.

This component is implemented based on [state management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v2). Compared with [state management V1](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage download button data and states with greater flexibility, leading to faster UI updates.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/SzHh_9l9RDqCGKZ5QT9iWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B3C51B479FDD7127116F25F51F73CD1A148C9E12629E8D286A3B67D39729BD2)

-   This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ColorMetrics, LengthMetrics, ProgressButtonV2,  ProgressButtonV2Color } from '@kit.ArkUI';

#### ProgressButtonV2

ProgressButtonV2({progress: number, content: ResourceStr, progressButtonWidth?: LengthMetrics, onClicked: ClickCallback, isEnabled: boolean, colorOptions?: ProgressButtonColorOptions, progressButtonRadius?: LengthMetrics})

Creates a text-based download button with a progress indicator that shows the download progress.

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| progress | number | Yes | 
@Require

@Param

 | 

Current download progress.

The value ranges from 0 to 100. Values less than 0 are adjusted to **0**, and values greater than 100 are capped at **100**.

Default value: **0**

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | 

@Require

@Param

 | Button text. |
| progressButtonWidth | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | 

@Param

@Once

 | 

Width of the button.

Default value: **44vp**

 |
| onClicked | [ClickCallback](#clickcallback) | Yes | @Param | Callback invoked when the button is clicked. |
| isEnabled | boolean | Yes | @Param | 

Whether the button can be clicked.

**true**: The button can be clicked.

**false**: The button cannot be clicked.

 |
| colorOptions | [ProgressButtonV2Color](#progressbuttonv2color) | No | @Param | Color options for the button. |
| progressButtonRadius18+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Corner radius of the button. It cannot be set in percentage.

Value range: \[0, height/2\]

Default value: height/2

If an invalid value is set, the default value is used.

 |

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ClickCallback

type ClickCallback = () => void

Callback invoked when the button is clicked.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

#### ProgressButtonV2Color

Defines the color options for the download button.

**Decorator type**: @ObservedV2

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| progressColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 
Color of the progress indicator.

Default value: **#330A59F7**

Decorator type: @Trace

 |
| borderColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Border color of the button.

Default value: **#330A59F7**

Decorator type: @Trace

 |
| textColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Text color of the button.

Default value: system default value **#CE000000**

Decorator type: @Trace

 |
| backgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Background color of the button.

Default value: **$r('sys.color.ohos\_id\_color\_foreground\_contrary')**

Decorator type: @Trace

 |

#### \[h2\]constructor

constructor(options: ProgressButtonV2ColorOptions);

A constructor used to create a **ProgressButtonV2Color** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ProgressButtonV2ColorOptions](#progressbuttonv2coloroptions) | Yes | Color settings. |

#### ProgressButtonV2ColorOptions

Provides options for customizing the color of the download button.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| progressColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 
Color of the progress indicator.

Default value: **#330A59F7**

 |
| borderColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Border color of the button.

Default value: **#330A59F7**

 |
| textColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Text color of the button.

Default value: system default value **#CE000000**

 |
| backgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | Yes | 

Background color of the button.

Default value: **$r('sys.color.ohos\_id\_color\_foreground\_contrary')**

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

This example demonstrates how to create a simple download button with a progress indicator that shows the loading status of a text file.

import { LengthMetrics, ProgressButtonV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local progressIndex: number = 0;
  @Local textState: string = 'Download';
  @Local buttonWidth: LengthMetrics = LengthMetrics.vp(200);
  @Local isRunning: boolean = false;
  @Local enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButtonV2({
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            isEnabled: this.enableState,
            onClicked: () => {
              if (this.textState && !this.isRunning && this.progressIndex < 100) {
                this.textState = 'Continue';
              }
              this.isRunning = !this.isRunning;
              let timer = setInterval(() => {
                if (this.isRunning) {
                  if (this.progressIndex === 100) {
                    clearInterval(timer);
                  } else {
                    this.progressIndex++;
                    if (this.progressIndex === 100) {
                      this.textState = 'Completed';
                      this.enableState = false;
                    }
                  }
                } else {
                  clearInterval(timer);
                }
              }, 20);
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 });
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/MHj0tbsBQzaRU8uZZCD0NA/en-us_image_0000002537765984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAEC8E9512172A7A3D427A9864BD05D916C701AF38165552587F3EF13B4C3CD1)
