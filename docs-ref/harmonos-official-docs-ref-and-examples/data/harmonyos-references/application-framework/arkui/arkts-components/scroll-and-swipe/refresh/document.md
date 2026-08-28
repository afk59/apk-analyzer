# Refresh

The **Refresh** component is a container that provides the pull-to-refresh feature.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ljc3se7eTYaCgSs2hyWRWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57848DAFC48E6C30CDF2A79014BA3D06C9E216A192285DCC0469A7D686D26A4E)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Since API version 12, this component provides linkage with a vertically scrolling [Swiper](../swiper/document.md) and [Web](../../../javascript-components/javascript-compatible-web-like-development-paradigm-arkui-full/basic-components/web/document.md) components. When the [loop](../swiper/document.md#loop) attribute of [Swiper](../swiper/document.md) is set to **true**, the **Refresh** component cannot provide linkage with [Swiper](../swiper/document.md).
    
-   When the **Refresh** component is nested with a [List](../list/document.md) component whose content size is smaller than the component itself, and there are other components in between, gestures may be intercepted by the intermediate components, preventing the pull-to-refresh effect. In such cases, set the [alwaysEnabled](../scrollable-component-common-apis/document.md#edgeeffectoptions11) parameter to **true** to allow [List](../list/document.md) to respond to gestures and drive the **Refresh** component through nested scrolling for the pull-to-refresh effect. For details, see [Example 9: Implementing Pull-to-Refresh in the Non-Full-Screen Scenario](#example-9-implementing-pull-to-refresh-in-the-non-full-screen-scenario).
    
-   The component has been bound with gestures to implement functions such as follow-up scrolling. If you need to add custom gestures, refer to [Gesture Blocking Enhancement](../../gesture-handling/gesture-control/gesture-blocking-enhancement/document.md).
    
-   Pull-to-refresh cannot be triggered by mouse click-and-drag operations.
    

#### Child Components

This component supports only one child component.

Since API version 11, this component's child component moves down with the pull-down gesture.

#### APIs

Refresh(value: RefreshOptions)

Creates a **Refresh** container.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [RefreshOptions](#refreshoptions) | Yes | Parameters of the **Refresh** component. |

#### RefreshOptions

Defines the options of the **Refresh** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| refreshing | boolean | No | No | 
Whether the component is being refreshed. The value **true** means that the component is being refreshed, and **false** means the opposite.

Default value: **false**

This parameter supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| offset(deprecated) | number | string | No | Yes | 

Distance from the pull-down starting point to the top of the component.

Default value: **16**.

Unit: vp.

If the type is string, the pixel unit must be explicitly specified, for example, **'10px'**; if the unit is not specified, for example, **'10'**, the default unit vp is used.

Note: This API is supported since API version 8 and deprecated since API version 11. No substitute is provided.

**NOTE**

The value range of **offset** is \[0vp, 64vp\]. If the value is greater than 64 vp, the value 64 vp will be used. The value cannot be a percentage or a negative number.

 |
| friction(deprecated) | number | string | No | Yes | 

Coefficient of friction, which indicates the **<Refresh>** component's sensitivity to the pull-down gesture. The value ranges from 0 to 100.

Default value: **62**

\- **0** indicates that the **Refresh** component is not responsive to the pull-down gesture.

\- **100** indicates that the **Refresh** component is highly responsive to the pull-down gesture.

\- A larger value indicates higher responsiveness of the **Refresh** component to the pull-down gesture.

**NOTE**

This API is supported since API version 8 and deprecated since API version 11. You are advised to use [pullDownRatio](#pulldownratio12) instead.

 |
| builder10+ | [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) | No | Yes | 

Custom content in the refreshing area.

**NOTE**

In API version 10 and earlier versions, there is a height limit of 64 vp on custom components. This restriction is removed since API version 11.

When a custom component is set with a fixed height, it will be displayed below the refreshing area at that fixed height; when the custom component does not have a height set, its height will adapt to the height of the refreshing area, which may result in the height of the custom component changing to 0 along with the refreshing area. To maintain the intended layout, configure a minimum height constraint for a custom component, which ensures that the component's height does not fall below a certain threshold. For details about how to apply this constraint, see [Example 3](#example-3-customizing-the-refreshing-area-content-with-builder).

Since API version 12, use **refreshingContent** instead of **builder** for customizing the content of the refreshing area, to avoid animation interruptions caused by the destruction and re-creation of the custom component during the refreshing process.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| promptText12+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Custom text displayed at the bottom of the refreshing area.

**NOTE**

When setting the text, follow the constraints on the **Text** components. If you are using **builder** or **refreshingContent** to customize the content displayed in the refreshing area, the text set with **promptText** will not be displayed.

When **promptText** is set and effective, the [refreshOffset](#refreshoffset12) attribute defaults to 96 vp.

The maximum font scale factor for the custom text, as specified by [maxFontScale](../../text-and-input/text/document.md#maxfontscale12), is 2.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| refreshingContent12+ | [ComponentContent](../../../arkts-api/ui/arkui/componentcontent/document.md) | No | Yes | 

Custom content in the refreshing area.

**NOTE**

If this parameter and the **builder** parameter are set at the same time, the **builder** parameter does not take effect.

When a custom component is set with a fixed height, it will be displayed below the refreshing area at that fixed height; when the custom component does not have a height set, its height will adapt to the height of the refreshing area, which may result in the height of the custom component changing to 0 along with the refreshing area. To maintain the intended layout, configure a minimum height constraint for a custom component, which ensures that the component's height does not fall below a certain threshold. For details about how to apply this constraint, see [Example 4](#example-4-customizing-the-refreshing-area-content-with-refreshingcontent).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

**Supplementary Notes**

-   If neither **builder** nor **refreshingContent** is set, the pull-down displacement effect is implemented by adjusting the [translate](../../universal-attributes/visual-effects/transformation/document.md#translate) attribute of the child component. During the pull-down process, the [onAreaChange](../../universal-events/component-change-events/component-area-change-event/document.md#onareachange) event of the child component is not triggered, and any changes made to the [translate](../../universal-attributes/visual-effects/transformation/document.md#translate) attribute of the child component do not take effect.
-   When **builder** or **refreshingContent** is set, the pull-down displacement effect is implemented by adjusting the position of the child component relative to the **Refresh** component. During the pull-down process, the [onAreaChange](../../universal-events/component-change-events/component-area-change-event/document.md#onareachange) event of the child component can be triggered. However, if the [position](../../universal-attributes/layout-and-borders/location/document.md#position) attribute is set for the child component, the position of the child component relative to the **Refresh** component is fixed, preventing the child component from moving down with the pull gesture.
-   If the width and height of a custom component set by **builder** are not specified, its dimensions will adapt to the child components. If the width is specified but the height is not, the height of the component is automatically adjusted according to the pull-down distance. If a custom component set by **refreshingContent** does not have a specified height, its height will also adapt to the pull-down distance. In such cases, as the pull-down distance increases, the height of the custom component will increase accordingly. When the custom component's height is set to a fixed value or reaches its maximum height limit, further increases in the pull-down distance will cause the spacing between the custom component and the top boundary of the **Refresh** component to widen.

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]refreshOffset12+

refreshOffset(value: number)

Sets the minimum pull-down offset required to trigger a refresh. If the distance pulled down is less than the value specified by this attribute, releasing the gesture does not trigger a refresh.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Pull-down offset, in vp.

Default value: 96 vp when [promptText](#refreshoptions) is set and 64 vp when [promptText](#refreshoptions) is not set.

If the value specified is 0 or less than 0, the default value is used.

 |

#### \[h2\]pullToRefresh12+

pullToRefresh(value: boolean)

Sets whether to initiate a refresh when the pull-down distance exceeds the value of [refreshOffset](#refreshoffset12).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to initiate a refresh when the pull-down distance exceeds the value of [refreshOffset](#refreshoffset12). The value **true** means to initiate a refresh, and **false** means the opposite.

Default value: **true**

 |

#### \[h2\]pullDownRatio12+

pullDownRatio(ratio: [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number>)

Sets the pull-down ratio.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ratio | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Pull-down ratio. A larger value indicates higher responsiveness to the pull-down gesture. The value **0** indicates that the pull-down does not follow the gesture, and **1** indicates that the pull-down follows the gesture proportionally.

If this parameter is not set or is set to **undefined**, a dynamic pull-down ratio is used. That is, the larger the pull-down distance, the smaller the ratio.

The value ranges from 0 to 1. A value less than 0 is handled as **0**, and a value greater than 1 is handled as **1**.

 |

#### \[h2\]maxPullDownDistance20+

maxPullDownDistance(distance: Optional<number>)

Sets the maximum pull-down distance.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| distance | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Maximum pull-down distance. The minimum value for the maximum pull-down distance is 0. Values less than 0 are treated as **0**. If this value is less than the refresh offset (**refreshOffset**), the refresh action will not be triggered when the pull-down gesture is released.

If set to **undefined** or **null**, this parameter is considered not set.

Default value: **undefined**.

Unit: vp

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onStateChange

onStateChange(callback: (state: RefreshStatus) => void)

Called when the refresh status changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [RefreshStatus](#refreshstatus) | Yes | Refresh status. |

#### \[h2\]onRefreshing

onRefreshing(callback: () => void)

Called when the component starts refreshing.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback triggered when the component enters the refresh state. |

#### \[h2\]onOffsetChange12+

onOffsetChange(callback: Callback<number>)

Called when the pull-down distance changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/TA6qIskWQx2b7cAya4e1Aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A74389582859AC5934FDBB249A3B6C09599C27411829F003DEB320352EBFD7F)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<number> | Yes | 
Pull-down distance.

Unit: vp

 |

#### RefreshStatus

Enumerates the states of a refresh operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Inactive | 0 | The component is not pulled down. This is the default value. |
| Drag | 1 | 
The component is being pulled down, but the pull-down distance is shorter than the refresh threshold.

If you release the component, it enters the **Inactive** state. If you continue to pull down the component and the pull-down distance exceeds the refresh threshold, the component enters the **OverDrag** state.

 |
| OverDrag | 2 | 

The component is being pulled down, and the pull-down distance exceeds the refresh threshold.

If you release the component, the component enters the **Refresh** state. If you swipe upward and the pull-down distance is less than the refresh threshold, the component enters the **Drag** state.

 |
| Refresh | 3 | The pull-down ends, and the component rebounds to the minimum length required to trigger the refresh and enters the refreshing state. |
| Done | 4 | The refresh is complete, and the component returns to the initial state (at the top). |

#### Example

## Example 1: Using the Default Refreshing Style

This example implements a **Refresh** component with its refreshing area in the default style.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State arr: String\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];

  build() {
    Column() {
      Row() {
        Button('Refresh').onClick(() => {
          this.isRefreshing = true;
        })
        Button('Stop').onClick(() => {
          this.isRefreshing = false;
        })
      }

      Refresh({ refreshing: $$this.isRefreshing }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
      .backgroundColor(0x89CFF0)
      .refreshOffset(64)
      .pullToRefresh(true)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/sLsrt8c4R-uBt58MS3UxIA/en-us_image_0000002537765558.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC5AE2BA2124AAD9B47D239620E11C7AEDB198FD43850B3870D35ECD07113B38)

## Example 2: Setting the Text Displayed in the Refreshing Area

This example shows how to set the text displayed in the refreshing area using the [promptText](#refreshoptions) parameter.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State promptText: string = "Refreshing...";
  @State arr: string\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing, promptText: this.promptText }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text(item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .pullToRefresh(true)
      .refreshOffset(96)
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Lu-VdWvxSuymy53QBZSMsQ/en-us_image_0000002537925498.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBD396210AE5F1CF31BDFE04877650943575DF77B5EA2C812A641958D02D06C3)

## Example 3: Customizing the Refreshing Area Content with builder

This example shows how to customize the content displayed in the refreshing area using the [builder](#refreshoptions) parameter.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State arr: String\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];

  @Builder
  customRefreshComponent() {
    Stack() {
      Row() {
        LoadingProgress().height(32)
        Text("Refreshing...").fontSize(16).margin({ left: 20 })
      }
      .alignItems(VerticalAlign.Center)
    }
    .align(Alignment.Center)
    .clip(true)
    // Set a minimum height constraint to ensure that the height of the custom component does not fall below the specified minHeight when the height of the refreshing area changes.
    .constraintSize({ minHeight: 32 })
    .width('100%')
  }

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing, builder: this.customRefreshComponent() }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .pullToRefresh(true)
      .refreshOffset(64)
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/elHgSrg0S8S6aLq-6NR5hQ/en-us_image_0000002568685275.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA6CE9208BC59D030A912C4C19A9D379316A9FE9560022B2488B86C6F6191EE6)

## Example 4: Customizing the Refreshing Area Content with refreshingContent

This example shows how to customize the content displayed in the refreshing area using the [refreshingContent](#refreshoptions) parameter.

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

class Params {
  refreshStatus: RefreshStatus = RefreshStatus.Inactive;

  constructor(refreshStatus: RefreshStatus) {
    this.refreshStatus = refreshStatus;
  }
}

@Builder
function customRefreshingContent(params: Params) {
  Stack() {
    Row() {
      LoadingProgress().height(32)
      Text("refreshStatus: " + params.refreshStatus).fontSize(16).margin({ left: 20 })
    }
    .alignItems(VerticalAlign.Center)
  }
  .align(Alignment.Center)
  .clip(true)
  // Set a minimum height constraint to ensure that the height of the custom component does not fall below the specified minHeight when the height of the refreshing area changes.
  .constraintSize({ minHeight: 32 })
  .width('100%')
}

@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State arr: String\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];
  @State refreshStatus: RefreshStatus = RefreshStatus.Inactive;
  private contentNode?: ComponentContent<Object> = undefined;
  private params: Params = new Params(RefreshStatus.Inactive);

  aboutToAppear(): void {
    let uiContext = this.getUIContext();
    this.contentNode = new ComponentContent(uiContext, wrapBuilder(customRefreshingContent), this.params);
  }

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing, refreshingContent: this.contentNode }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .pullToRefresh(true)
      .refreshOffset(96)
      .onStateChange((refreshStatus: RefreshStatus) => {
        this.refreshStatus = refreshStatus;
        this.params.refreshStatus = refreshStatus;
        // Update the content of the custom component.
        this.contentNode?.update(this.params);
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fOMVc_ZNQyus468gkNaEYg/en-us_image_0000002568765285.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D9F0AF5A18F40CB26236EC409D6533F1C5E604050ABB017ECA1FA946F16B7A3)

## Example 5: Implementing the Maximum Pull-down Distance

This example shows how to use the [pullDownRatio](#pulldownratio12) attribute and the [onOffsetChange](#onoffsetchange12) event to implement the maximum pull-down distance.

// xxx.ets
import { ComponentContent } from '@kit.ArkUI';

@Builder
function customRefreshingContent() {
  Stack() {
    Row() {
      LoadingProgress().height(32)
    }
    .alignItems(VerticalAlign.Center)
  }
  .align(Alignment.Center)
  .clip(true)
  // Set a minimum height constraint to ensure that the height of the custom component does not fall below the specified minHeight when the height of the refreshing area changes.
  .constraintSize({ minHeight: 32 })
  .width('100%')
}

@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State arr: String\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];
  @State maxRefreshingHeight: number = 100.0;
  @State ratio: number = 1;
  private contentNode?: ComponentContent<Object> = undefined;

  aboutToAppear(): void {
    let uiContext = this.getUIContext();
    this.contentNode = new ComponentContent(uiContext, wrapBuilder(customRefreshingContent));
  }

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing, refreshingContent: this.contentNode }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString());
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .pullDownRatio(this.ratio)
      .pullToRefresh(true)
      .refreshOffset(64)
      .onOffsetChange((offset: number) => {
        // The closer to the maximum distance, the smaller the pull-down ratio.
        this.ratio = 1 - Math.pow((offset / this.maxRefreshingHeight), 3);
      })
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/2YKJig1HSR-2UBHuUufBaw/en-us_image_0000002537765560.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1B8A10B9CC75E5C08F43A6EC8A428CE33B03500C8AE177E867BA313F3E36A85)

## Example 6: Implementing Pull-Down-to-Refresh and Pull-Up-to-Load-More

This example demonstrates how to combine the **Refresh** component with the [List](../list/document.md) component to implement pull-down-to-refresh and pull-up-to-load-more features.

// xxx.ets
@Entry
@Component
struct ListRefreshLoad {
  @State arr: Array<number> = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\];
  @State refreshing: boolean = false;
  @State refreshOffset: number = 0;
  @State refreshState: RefreshStatus = RefreshStatus.Inactive;
  @State isLoading: boolean = false;

  @Builder
  refreshBuilder() {
    Stack({ alignContent: Alignment.Bottom }) {
      // The Progress component is displayed based on the refresh state.
      // It is only shown when the refresh state is Drag or Refresh.
      if (this.refreshState != RefreshStatus.Inactive && this.refreshState != RefreshStatus.Done) {
        Progress({ value: this.refreshOffset, total: 64, type: ProgressType.Ring })
          .width(32).height(32)
          .style({ status: this.refreshing ? ProgressStatus.LOADING : ProgressStatus.PROGRESSING })
          .margin(10)
      }
    }
    .clip(true)
    .height('100%')
    .width('100%')
  }

  @Builder
  footer() {
    Row() {
      LoadingProgress().height(32).width(48)
      Text("Loading")
    }.width('100%')
    .height(64)
    .justifyContent(FlexAlign.Center)
    // The component is hidden when not in the loading state.
    .visibility(this.isLoading ? Visibility.Visible : Visibility.Hidden)
  }

  build() {
    Refresh({ refreshing: $$this.refreshing, builder: this.refreshBuilder() }) {
      List() {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(80)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor(0xFFFFFF)
          }.borderWidth(1)
        }, (item: string) => item)

        ListItem() {
          this.footer();
        }
      }
      .onScrollIndex((start: number, end: number) => {
        // Trigger new data loading when the end of the list is reached.
        if (end >= this.arr.length - 1) {
          this.isLoading = true;
          // Simulate new data loading.
          setTimeout(() => {
            for (let i = 0; i < 10; i++) {
              this.arr.push(this.arr.length);
            }
            this.isLoading = false;
          }, 700)
        }
      })
      .scrollBar(BarState.Off)
      // Enable the effect used when the scroll boundary is reached.
      .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .onOffsetChange((offset: number) => {
      this.refreshOffset = offset;
    })
    .onStateChange((state: RefreshStatus) => {
      this.refreshState = state;
    })
    .onRefreshing(() => {
      // Simulate data refreshing.
      setTimeout(() => {
        this.refreshing = false;
      }, 2000)
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/6u8l86W4TPyHRmXbSrELww/en-us_image_0000002537925500.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=365385C35198DAD56D36DA59834B13DAE35599F90A34C7F19F2AE9203DE74FDD)

## Example 7: Setting the Maximum Pull-Down Distance

This example demonstrates how to set the maximum pull-down distance using the [maxPullDownDistance](#maxpulldowndistance20) attribute, supported since API version 20.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false
  @State arr: string\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\]

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing }) {
        List() {
          ForEach(this.arr, (item: string) => {
            ListItem() {
              Text('' + item)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
            }
          }, (item: string) => item)
        }
        .onScrollIndex((first: number) => {
          console.info(first.toString())
        })
        .width('100%')
        .height('100%')
        .alignListItem(ListItemAlign.Center)
        .scrollBar(BarState.Off)
      }
      .maxPullDownDistance(150)
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus)
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value)
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false
        }, 2000)
        console.info('onRefreshing test')
      })
      .backgroundColor(0x89CFF0)
      .refreshOffset(64)
      .pullToRefresh(true)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/L9QavpjUTr6CzF8koYAyLw/en-us_image_0000002568685277.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD96FB14FF69FD7C010AA75D6BD2138C5DCCEE935F3E5FA4E6B26D18A6D9C428)

## Example 8: Disabling Pull-to-Refresh

This example demonstrates how to disable pull-to-refresh using the [pullDownRatio](#pulldownratio12) attribute.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State ratio: number | undefined = undefined;
  @State arr: string\[\] = \['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'\];

  build() {
    Column() {
      Row() {
        Button('Disable Pull-to-Refresh').onClick(() => {
          this.ratio = 0
        })
        Button('Enable Pull-to-Refresh').onClick(() => {
          this.ratio = undefined
        })
      }
      Refresh({ refreshing: $$this.isRefreshing }) {
          List() {
            ForEach(this.arr, (item: string) => {
              ListItem() {
                Text('' + item)
                  .width('70%')
                  .height(80)
                  .fontSize(16)
                  .margin(10)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: string) => item)
          }
          .onScrollIndex((first: number) => {
            console.info(first.toString());
          })
          .width('100%')
          .height('100%')
          .alignListItem(ListItemAlign.Center)
          .scrollBar(BarState.Off)
      }
      .backgroundColor(0x89CFF0)
      .refreshOffset(64)
      .pullToRefresh(true)
      .pullDownRatio(this.ratio)
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
        console.info('onRefreshing test');
      })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/IMWXv8iwR_-haoLV7h0zhw/en-us_image_0000002568765287.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E08F113CAD87692B534C7975A69D5EF6B709CF4344EF0B1745B5E397ABE3A19)

## Example 9: Implementing Pull-to-Refresh in the Non-Full-Screen Scenario

You can set the **alwaysEnabled** parameter in the [edgeEffect](../scrollable-component-common-apis/document.md#edgeeffect11) attribute to implement the pull-to-refresh effect of the **Refresh** component when the screen is not full.

// xxx.ets
@Entry
@Component
struct RefreshExample {
  @State isRefreshing: boolean = false;
  @State alwaysEnabled: boolean = false;

  build() {
    Column() {
      Refresh({ refreshing: $$this.isRefreshing }) {
        Column() {
          List() {
            ListItem() {
              Text('alwaysEnabled:' + this.alwaysEnabled)
                .width('70%')
                .height(80)
                .fontSize(16)
                .margin(10)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
                .onClick(() => {
                  this.alwaysEnabled = !this.alwaysEnabled;
                })
            }
          }
          .width('100%')
          .height('100%')
          .alignListItem(ListItemAlign.Center)
          .scrollBar(BarState.Auto)
          // If the content size of the List component is smaller than the component size and alwaysEnabled is set to false, the List component does not respond to gestures. In this case, the gestures are responded by the Column component, and the pull-to-refresh effect is not generated.
          // If alwaysEnabled is set to true, the List component responds to gestures and drives the Refresh component to trigger pull-down refresh through nested scrolling.
          .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: this.alwaysEnabled })
        }
        .gesture(
          PanGesture({ direction: PanDirection.Vertical })
        )
      }
      .onStateChange((refreshStatus: RefreshStatus) => {
        console.info('Refresh onStatueChange state is ' + refreshStatus);
      })
      .onOffsetChange((value: number) => {
        console.info('Refresh onOffsetChange offset:' + value);
      })
      .onRefreshing(() => {
        setTimeout(() => {
          this.isRefreshing = false;
        }, 2000)
      })
      .backgroundColor(0x89CFF0)
      .refreshOffset(64)
      .pullToRefresh(true)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/94XwBPs5SnK2ihtLW2I3Bw/en-us_image_0000002537765562.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EABBDCA76A042473867B18D6DE2E508CC9166ACD2231D2E09FEC8201FAA07F9)
