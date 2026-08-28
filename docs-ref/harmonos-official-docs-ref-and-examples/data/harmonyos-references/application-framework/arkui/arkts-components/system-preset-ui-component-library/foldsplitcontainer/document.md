# FoldSplitContainer

**FoldSplitContainer** is a layout container designed to manage regions for two-panel and three-panel arrangements on a foldable device across various states, including the expanded state, the semi-folded state, and the folded state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/FodPni_uQWq3uwsaCgkO4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1087648D170271E1947538B25E41C30CE57AB5D946F37E887D1BE027CBEB7961)

-   This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.
    
-   By default, a two-panel layout is used when the window width is less than or equal to 600 vp. When the window width exceeds 600 vp, an extended area is supported alongside the top-bottom split layout. A semi-folded state layout can be triggered when the window width is greater than 600 vp and the device is in a horizontal, half-folded posture. In the semi-folded layout, visual avoidance for the screen crease area is applied, and the extended area cannot span across the crease. The extended area can also be configured not to display in the semi-folded state. For details, see [Example](#example)
    

#### Modules to Import

import { FoldSplitContainer } from '@kit.ArkUI';

#### Child Components

Not supported

#### FoldSplitContainer

FoldSplitContainer({primary: Callback<void>, secondary: Callback<void>, extra?: Callback<void>, expandedLayoutOptions: ExpandedRegionLayoutOptions, hoverModeLayoutOptions: HoverModeRegionLayoutOptions, foldedLayoutOptions: FoldedRegionLayoutOptions, animationOptions?: AnimateParam | null, onHoverStatusChange?: OnHoverStatusChangeHandler})

Creates a **FoldSplitContainer** component to manage regions for two-panel and three-panel arrangements on a foldable device across various states, including the expanded state, the semi-folded state, and the folded state.

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| primary | Callback<void> | Yes | @BuilderParam | Callback function for the primary region. |
| secondary | Callback<void> | Yes | @BuilderParam | Callback function for the extra region. |
| extra | Callback<void> | No | @BuilderParam | Callback function for the extra region. If this parameter is not provided, there is no corresponding region. |
| expandedLayoutOptions | [ExpandedRegionLayoutOptions](#expandedregionlayoutoptions) | Yes | @Prop | Layout information for the expanded state. |
| hoverModeLayoutOptions | [HoverModeRegionLayoutOptions](#hovermoderegionlayoutoptions) | Yes | @Prop | Layout information for the semi-folded state. |
| foldedLayoutOptions | [FoldedRegionLayoutOptions](#foldedregionlayoutoptions) | Yes | @Prop | Layout information for the folded state. |
| animationOptions | [AnimateParam](../../animation/explicit-animation-animateto/document.md#animateparam) | null | No | @Prop | Animation settings. The value **null** indicates that the animation is disabled. |
| onHoverStatusChange | [OnHoverStatusChangeHandler](#onhoverstatuschangehandler) | No | \- | Callback function triggered when the foldable device enters or exits the semi-folded state. |

#### ExpandedRegionLayoutOptions

Layout information for the expanded state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isExtraRegionPerpendicular | boolean | No | Yes | 
Whether the extra region extends perpendicularly through the entire component from top to bottom. The value **true** means that the extra region extends perpendicularly through the entire component from top to bottom, and **false** means the opposite. This setting takes effect only when **extra** is effective.

Default value: **true**.

 |
| verticalSplitRatio | number | No | Yes | 

Height ratio between the primary and extra regions.

Default value: [PresetSplitRatio](#presetsplitratio).LAYOUT\_1V1

 |
| horizontalSplitRatio | number | No | Yes | 

Width ratio between the primary and extra regions. This setting takes effect only when **extra** is effective.

Default value: [PresetSplitRatio](#presetsplitratio).LAYOUT\_3V2

 |
| extraRegionPosition | [ExtraRegionPosition](#extraregionposition) | No | Yes | 

Position information of the extra region. This setting takes effect only when **isExtraRegionPerpendicular** is set to **false**.

Default value: **ExtraRegionPosition.top**.

 |

#### HoverModeRegionLayoutOptions

Layout information for the semi-folded state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| showExtraRegion | boolean | No | Yes | 
Whether to display the extra region in the half-folded state. The value **true** means to display the extra region in the half-folded state, and **false** means the opposite.

Default value: **false**.

 |
| horizontalSplitRatio | number | No | Yes | 

Width ratio between the primary and extra regions. This setting takes effect only when **extra** is effective.

Default value: [PresetSplitRatio](#presetsplitratio).LAYOUT\_3V2

 |
| extraRegionPosition | [ExtraRegionPosition](#extraregionposition) | No | Yes | 

Position information of the extra region. This setting takes effect only when **showExtraRegion** is set to **true**.

Default value: **ExtraRegionPosition.top**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bV_Q4rxbROy7POpgHnHfgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16710A0BC451A52CBA8E15E787ADC97F651F44C3365E1620FF4D1C3591D2A7BB)

1.  In the semi-folded state, there is an avoidance area. Layout calculations must take the impact of this avoidance area into account.
2.  In the semi-folded state, the upper half of the screen is used for display, and the lower half is used for interaction.

#### FoldedRegionLayoutOptions

Provides the layout information of the folded state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| verticalSplitRatio | number | No | Yes | Height ratio between the primary and extra regions. Default value: [PresetSplitRatio](#presetsplitratio).LAYOUT\_1V1 |

#### OnHoverStatusChangeHandler

type OnHoverStatusChangeHandler = (status: HoverModeStatus) => void

Implements a handler for the **onHoverStatusChange** event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| status | [HoverModeStatus](#hovermodestatus) | Yes | Callback function triggered when the foldable device enters or exits the semi-folded state. |

#### HoverModeStatus

Provides information about the device or application's folding, rotation, and window state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| foldStatus | [display.FoldStatus](../../../arkts-api/display-management/ohos-display-display/document.md#foldstatus10) | No | No | Fold status of the device. |
| isHoverMode | boolean | No | No | Whether the application is in the hover state. The value **true** means that the application is in the hover state, and **false** means the opposite. |
| appRotation | number | No | No | Rotation angle of the application. |
| windowStatusType | [window.WindowStatusType](../../../arkts-api/window-manager/ohos-window-window/enums/document.md#windowstatustype11) | No | No | Window mode. |

#### ExtraRegionPosition

Provides the position information of the extra region.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP | 1 | The extra region is in the upper half of the component. |
| BOTTOM | 2 | The extra region is in the lower half of the component. |

#### PresetSplitRatio

Enumerates the split ratios.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LAYOUT\_1V1 | 1 | 1:1. |
| LAYOUT\_3V2 | 1.5 | 3:2. |
| LAYOUT\_2V3 | 0.6666666666666666 | 2:3. |

#### Example

## Example 1: Setting Up a Two-Panel Layout

This example demonstrates how to control the region for a two-panel layout on a foldable screen across different states: folded, expanded, and hover.

import { FoldSplitContainer } from '@kit.ArkUI';

@Entry
@Component
struct TwoColumns {
  @Builder
  privateRegion() {
    Text("Primary")
      .backgroundColor('rgba(255, 0, 0, 0.1)')
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .height('100%')
      .width('100%')
  }

  @Builder
  secondaryRegion() {
    Text("Secondary")
      .backgroundColor('rgba(0, 255, 0, 0.1)')
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .height('100%')
      .width('100%')
  }

  build() {
    RelativeContainer() {
      FoldSplitContainer({
        primary: () => {
          this.privateRegion()
        },
        secondary: () => {
          this.secondaryRegion()
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}

| Folded | Expanded | Semi-folded |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/WuL3BoTuRiOuxBMkqTPwVg/en-us_image_0000002568685691.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=573ED3F713BFEF34FD926EF474A9E289F062F2914A534D8608DA1B316C31DE39) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/NKNOQLfrTZuo84FxEAIu5g/en-us_image_0000002568765701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8140104977DD50D8CE2B88AF9052C379FBE5C4D71BC239A5CC6B151ECADA486) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/uFS4sKmES7ubxqRMxpVVfg/en-us_image_0000002537765976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53CA167735C60C1DE6D9B55F8359EB16761BB1854602B709D764E8FF3B1E083A) |

## Example 2: Setting Up a Three-Panel Layout

This example demonstrates how to control the region for a three-panel layout on a foldable screen across different states: folded, expanded, and hover.

import { FoldSplitContainer } from '@kit.ArkUI';

@Entry
@Component
struct ThreeColumns {
  @Builder
  privateRegion() {
    Text("Primary")
      .backgroundColor('rgba(255, 0, 0, 0.1)')
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .height('100%')
      .width('100%')
  }

  @Builder
  secondaryRegion() {
    Text("Secondary")
      .backgroundColor('rgba(0, 255, 0, 0.1)')
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .height('100%')
      .width('100%')
  }

  @Builder
  extraRegion() {
    Text("Extra")
      .backgroundColor('rgba(0, 0, 255, 0.1)')
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .height('100%')
      .width('100%')
  }

  build() {
    RelativeContainer() {
      FoldSplitContainer({
        primary: () => {
          this.privateRegion()
        },
        secondary: () => {
          this.secondaryRegion()
        },
        extra: () => {
          this.extraRegion()
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}

| Folded | Expanded | Semi-folded |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/y2MYnvjPQje0jv66mhJxCw/en-us_image_0000002537925916.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=065BE0BAA57553F58A93C71B3E01AD910E8F3347A6B15D77D478A644B6B2BF8A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/mxmkK0FGRZypcrX1u4IsdQ/en-us_image_0000002568685693.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21E4469B36A77FD5FC8A6315855D46CC8AABDECE4E47E3519863BF0596DF843F) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/WlsPo58jSc2Gg4YTIXv7RA/en-us_image_0000002568765703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EA8F3BA7BD86E6F3BD87E12E8C7179EF47FC714CFB3E61C0C4986C7FAA3A283) |

## Example 3: Setting Layout Information in Expanded State

This example illustrates how to configure **ExpandedRegionLayoutOptions** to set the layout information for a foldable screen when it is in the expanded state.

import {
  FoldSplitContainer,
  PresetSplitRatio,
  ExtraRegionPosition,
  ExpandedRegionLayoutOptions,
  HoverModeRegionLayoutOptions,
  FoldedRegionLayoutOptions
} from '@kit.ArkUI';

@Component
struct Region {
  @Prop title: string;
  @BuilderParam content: () => void;
  @Prop compBackgroundColor: string;

  build() {
    Column({ space: 8 }) {
      Text(this.title)
        .fontSize("24fp")
        .fontWeight(600)

      Scroll() {
        this.content()
      }
      .layoutWeight(1)
      .width("100%")
    }
    .backgroundColor(this.compBackgroundColor)
    .width("100%")
    .height("100%")
    .padding(12)
  }
}

const noop = () => {
};

@Component
struct SwitchOption {
  @Prop label: string = ""
  @Prop value: boolean = false
  public onChange: (checked: boolean) => void = noop;

  build() {
    Row() {
      Text(this.label)
      Blank()
      Toggle({ type: ToggleType.Switch, isOn: this.value })
        .onChange((isOn) => {
          this.onChange(isOn);
        })
    }
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width("100%")
  }
}

interface RadioOptions {
  label: string;
  value: Object | undefined | null;
  onChecked: () => void;
}

@Component
struct RadioOption {
  @Prop label: string;
  @Prop value: Object | undefined | null;
  @Prop options: Array<RadioOptions>;

  build() {
    Row() {
      Text(this.label)
      Blank()
      Column({ space: 4 }) {
        ForEach(this.options, (option: RadioOptions) => {
          Row() {
            Radio({
              group: this.label,
              value: JSON.stringify(option.value),
            })
              .checked(this.value === option.value)
              .onChange((checked) => {
                if (checked) {
                  option.onChecked();
                }
              })
            Text(option.label)
          }
        })
      }
      .alignItems(HorizontalAlign.Start)
    }
    .alignItems(VerticalAlign.Top)
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width("100%")
  }
}

@Entry
@Component
struct Index {
  @State expandedRegionLayoutOptions: ExpandedRegionLayoutOptions = {
    horizontalSplitRatio: PresetSplitRatio.LAYOUT\_3V2,
    verticalSplitRatio: PresetSplitRatio.LAYOUT\_1V1,
    isExtraRegionPerpendicular: true,
    extraRegionPosition: ExtraRegionPosition.TOP
  };
  @State foldingRegionLayoutOptions: HoverModeRegionLayoutOptions = {
    horizontalSplitRatio: PresetSplitRatio.LAYOUT\_3V2,
    showExtraRegion: false,
    extraRegionPosition: ExtraRegionPosition.TOP
  };
  @State foldedRegionLayoutOptions: FoldedRegionLayoutOptions = {
    verticalSplitRatio: PresetSplitRatio.LAYOUT\_1V1
  };

  @Builder
  MajorRegion() {
    Region({
      title: "Folded state settings",
      compBackgroundColor: "rgba(255, 0, 0, 0.1)",
    }) {
      Column({ space: 4 }) {
        RadioOption({
          label: "Vertical split ratio in folded state",
          value: this.foldedRegionLayoutOptions.verticalSplitRatio,
          options: \[
            {
              label: "1:1",
              value: PresetSplitRatio.LAYOUT\_1V1,
              onChecked: () => {
                this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_1V1
              }
            },
            {
              label: "2:3",
              value: PresetSplitRatio.LAYOUT\_2V3,
              onChecked: () => {
                this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_2V3
              }
            },
            {
              label: "3:2",
              value: PresetSplitRatio.LAYOUT\_3V2,
              onChecked: () => {
                this.foldedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_3V2
              }
            },
            {
              label: "Not set",
              value: undefined,
              onChecked: () => {
                this.foldedRegionLayoutOptions.verticalSplitRatio = undefined
              }
            }
          \]
        })
      }
      .constraintSize({ minHeight: "100%" })
    }
  }

  @Builder
  MinorRegion() {
    Region({
      title: "Semi-folded state settings",
      compBackgroundColor: "rgba(0, 255, 0, 0.1)"
    }) {
      Column({ space: 4 }) {
        RadioOption({
          label: "Horizontal split ratio in semi-folded state",
          value: this.foldingRegionLayoutOptions.horizontalSplitRatio,
          options: \[
            {
              label: "1:1",
              value: PresetSplitRatio.LAYOUT\_1V1,
              onChecked: () => {
                this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_1V1
              }
            },
            {
              label: "2:3",
              value: PresetSplitRatio.LAYOUT\_2V3,
              onChecked: () => {
                this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_2V3
              }
            },
            {
              label: "3:2",
              value: PresetSplitRatio.LAYOUT\_3V2,
              onChecked: () => {
                this.foldingRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_3V2
              }
            },
            {
              label: "Not set",
              value: undefined,
              onChecked: () => {
                this.foldingRegionLayoutOptions.horizontalSplitRatio = undefined
              }
            },
          \]
        })

        SwitchOption({
          label: "Show extra region in semi-folded state",
          value: this.foldingRegionLayoutOptions.showExtraRegion,
          onChange: (checked) => {
            this.foldingRegionLayoutOptions.showExtraRegion = checked;
          }
        })

        if (this.foldingRegionLayoutOptions.showExtraRegion) {
          RadioOption({
            label: "Extra region location in semi-folded state",
            value: this.foldingRegionLayoutOptions.extraRegionPosition,
            options: \[
              {
                label: "Top",
                value: ExtraRegionPosition.TOP,
                onChecked: () => {
                  this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
                }
              },
              {
                label: "Bottom",
                value: ExtraRegionPosition.BOTTOM,
                onChecked: () => {
                  this.foldingRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
                }
              },
              {
                label: "Not set",
                value: undefined,
                onChecked: () => {
                  this.foldingRegionLayoutOptions.extraRegionPosition = undefined
                }
              },
            \]
          })
        }
      }
      .constraintSize({ minHeight: "100%" })
    }
  }

  @Builder
  ExtraRegion() {
    Region({
      title: "Expanded state settings",
      compBackgroundColor: "rgba(0, 0, 255, 0.1)"
    }) {
      Column({ space: 4 }) {
        RadioOption({
          label: "Horizontal split ratio in expanded state",
          value: this.expandedRegionLayoutOptions.horizontalSplitRatio,
          options: \[
            {
              label: "1:1",
              value: PresetSplitRatio.LAYOUT\_1V1,
              onChecked: () => {
                this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_1V1
              }
            },
            {
              label: "2:3",
              value: PresetSplitRatio.LAYOUT\_2V3,
              onChecked: () => {
                this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_2V3
              }
            },
            {
              label: "3:2",
              value: PresetSplitRatio.LAYOUT\_3V2,
              onChecked: () => {
                this.expandedRegionLayoutOptions.horizontalSplitRatio = PresetSplitRatio.LAYOUT\_3V2
              }
            },
            {
              label: "Not set",
              value: undefined,
              onChecked: () => {
                this.expandedRegionLayoutOptions.horizontalSplitRatio = undefined
              }
            },
          \]
        })

        RadioOption({
          label: "Vertical split ratio in expanded state",
          value: this.expandedRegionLayoutOptions.verticalSplitRatio,
          options: \[
            {
              label: "1:1",
              value: PresetSplitRatio.LAYOUT\_1V1,
              onChecked: () => {
                this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_1V1
              }
            },
            {
              label: "2:3",
              value: PresetSplitRatio.LAYOUT\_2V3,
              onChecked: () => {
                this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_2V3
              }
            },
            {
              label: "3:2",
              value: PresetSplitRatio.LAYOUT\_3V2,
              onChecked: () => {
                this.expandedRegionLayoutOptions.verticalSplitRatio = PresetSplitRatio.LAYOUT\_3V2
              }
            },
            {
              label: "Not set",
              value: undefined,
              onChecked: () => {
                this.expandedRegionLayoutOptions.verticalSplitRatio = undefined
              }
            }
          \]
        })

        SwitchOption({
          label: "Show extra region perpendicularly,"
          value: this.expandedRegionLayoutOptions.isExtraRegionPerpendicular,
          onChange: (checked) => {
            this.expandedRegionLayoutOptions.isExtraRegionPerpendicular = checked;
          }
        })

        if (!this.expandedRegionLayoutOptions.isExtraRegionPerpendicular) {
          RadioOption({
            label: "Extra region location in expanded state",
            value: this.expandedRegionLayoutOptions.extraRegionPosition,
            options: \[
              {
                label: "Top",
                value: ExtraRegionPosition.TOP,
                onChecked: () => {
                  this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.TOP
                }
              },
              {
                label: "Bottom",
                value: ExtraRegionPosition.BOTTOM,
                onChecked: () => {
                  this.expandedRegionLayoutOptions.extraRegionPosition = ExtraRegionPosition.BOTTOM
                }
              },
              {
                label: "Not set",
                value: undefined,
                onChecked: () => {
                  this.expandedRegionLayoutOptions.extraRegionPosition = undefined
                }
              },
            \]
          })
        }
      }
      .constraintSize({ minHeight: "100%" })
    }
  }

  build() {
    Column() {
      FoldSplitContainer({
        primary: () => {
          this.MajorRegion()
        },
        secondary: () => {
          this.MinorRegion()
        },
        extra: () => {
          this.ExtraRegion()
        },
        expandedLayoutOptions: this.expandedRegionLayoutOptions,
        hoverModeLayoutOptions: this.foldingRegionLayoutOptions,
        foldedLayoutOptions: this.foldedRegionLayoutOptions,
      })
    }
    .width("100%")
    .height("100%")
  }
}

| Folded | Expanded | Semi-folded |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/j8PLd6C8TleCyeq1vZJpPw/en-us_image_0000002537765978.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32A4F98842A4DBA5210B3F2C8E4019444593BF62B062A3EC819BA721D9367110) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/f-k_Xt1tTsOS1liONpTq-Q/en-us_image_0000002537925918.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4D57BD73D6CE531986CD7955A96F5CE04F54A041C4E58FF8A0E9731F2A9443A) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/25zA8zuSR_yA5KgBGF9rnQ/en-us_image_0000002568685695.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0454820F781705549F81EC54F52F137EA6E02F5AB6F591FFEE3A125DE1A955B) |
| \- | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/AFot1iSGQZ6kLUcdn1Cnng/en-us_image_0000002568765705.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74250ED15E5EEF4A16AF933FC531E00F5E04D8346385DC7295DD783A23BEC735) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/loZEbETbTVWESA-at5d_8w/en-us_image_0000002537765980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=880DEF56EFC2AD6282E8AD794E490695F2F2B029372C43B6CBB102C11A1A2CC6) |
| \- | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/mFVNrnIiSfqAOpMrtOixXw/en-us_image_0000002537925920.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E71E4A948A3475AE5A088693ACC17BA7E021A62DE2A08ADF573210D3FE17EEA7) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/IPAIQXGTTTOH7lkzNBwnEw/en-us_image_0000002568685697.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACAB7A0C5717900CEC1A590181B7A1C920C2544F62692B081E10355CAC9E6307) |
