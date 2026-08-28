# ProgressButton

The **ProgressButton** component is a text-based download button with a progress indicator that shows the download progress.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/VC9ul5PASi2ceFHEQQDaiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF9B3DA57D0D0AD90D400DE1BF8037AD92CB3B7D6FE35FD5FB124A2347138D3B)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ProgressButton } from '@kit.ArkUI';

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### ProgressButton

ProgressButton({progress: number, content: ResourceStr, progressButtonWidth?: Length, clickCallback: () => void, enable:

boolean, colorOptions?: ProgressButtonColorOptions, progressButtonRadius?: LengthMetrics})

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| progress | number | Yes | @Prop | 
Current download progress.

The value ranges from 0 to 100. Values less than 0 are adjusted to **0**, and values greater than 100 are capped at **100**.

Default value: **0**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| content | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | @Prop | 

Button text.

The default value is an empty string.

Note: The text is truncated with an ellipsis (...) if it exceeds the maximum display width of the component. The Resource type is supported since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| progressButtonWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | \- | 

Button width, in vp.

The value must be greater than or equal to 44 vp.

The default value is **44vp**. If the provided value is not of the Resource type and is either less than the default value or invalid, the system will automatically use the default value. If the provided value is of the Resource type but is less than the default value, the system will automatically use the default value. If the provided value is invalid, the button width will be 100% of the container width.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| clickCallback | () => void | Yes | \- | 

Callback invoked when the button is clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| enable | boolean | Yes | @Prop | 

Whether the button can be clicked.

**true**: The button can be clicked.

**false**: The button cannot be clicked.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| colorOptions18+ | [ProgressButtonColorOptions](#progressbuttoncoloroptions18) | No | @Prop | 

Color options of the button.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| progressButtonRadius18+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Prop | 

Corner radius of the button. It cannot be set in percentage.

Value range: \[0, height/2\]

Default value: height/2

If the value is less than 0, the value **0** is used. If the value is invalid, the default value is used. If the input parameter is **undefined**, the default value is used. When using LengthMetrics.vp, you are advised to provide a specific numeric value. Passing **null** or **undefined** will result in an exception.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ProgressButtonColorOptions18+

Defines the color options for the download button.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| progressColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Color of the progress indicator.

Default value: **#330A59F7**

 |
| borderColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Border color of the button.

Default value: **#330A59F7**

 |
| textColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Text color of the button.

Default value: system default value **#CE000000**

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the button.

Default value: **$r('sys.color.ohos\_id\_color\_foreground\_contrary')**

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Creating a Download Button with a Progress Indicator

This example demonstrates how to create a simple download button with a progress indicator that shows the loading status of a text file.

import { ProgressButton } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State progressIndex: number = 0;
  @State textState: string = 'Download';
  @State buttonWidth: number = 200;
  @State isRunning: boolean = false;
  @State enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButton({
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            enable: this.enableState,
            clickCallback: () => {
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
              }, 20)
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/S11Th-pAT-2WR0-2UFMu0w/en-us_image_0000002537765984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D7CDB3A136CEF47D9E67AD9EAE555AD077C8C43311B82A438F73EE037005179)

## Example 2: Implementing a Download Button with Custom Colors

This example shows how to implement a download button with custom colors.

import { ProgressButton } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State progressIndex: number = 0;
  @State textState: string = 'Download';
  @State buttonWidth: number = 200;
  @State isRunning: boolean = false;
  @State enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButton({
            // Set the color options of the download button.
            colorOptions: {
              progressColor: Color.Orange,
              borderColor: Color.Black,
              textColor: Color.Blue,
              backgroundColor: Color.Pink
            },
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            enable: this.enableState,
            clickCallback: () => {
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
              }, 20)
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/xnIY81PMTmGxAJdhrzRfUA/en-us_image_0000002537925924.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E8F418595203385BB4F93AA081D9859F18AA2AC4A4F446F7A23A892A61E38E8)

## Example 3: Implementing a Download Button with Custom Corner Radius

This example shows how to implement a download button with custom corner radius.

import { ProgressButton, LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State progressIndex: number = 0;
  @State textState: string = 'Download';
  @State buttonWidth: number = 200;
  @State isRunning: boolean = false;
  @State enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButton({
            progressButtonRadius: LengthMetrics.vp (8), // Set the custom corner radius to 8 vp.
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            enable: this.enableState,
            clickCallback: () => {
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
              }, 20)
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/5QiU9sy4SQGmnd8TNQAWJw/en-us_image_0000002568685701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68826FC694E2892CD466C3D364DF221211E75FC59764F065EC63714760A910E7)
