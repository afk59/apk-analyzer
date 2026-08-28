# @ohos.arkui.observer (Observer)

Provides APIs for listening for UI component behavior changes. [UIObserver](../ohos-arkui-uicontext-uicontext/class-uiobserver/document.md) is recommended for component observation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/qT9JYKcJSI2D3VOiGbhi3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062226Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72B8222407817E4EFDFF8802956FBAAF475CF3AF024C7504B7D979C240698149)

-   The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   UIObserver can only listen for relevant information within the current process and does not support obtaining information in cross-process scenarios.
    

#### Modules to Import

import { uiObserver } from '@kit.ArkUI';

#### NavDestinationState

Describes the state of the **NavDestination** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ON\_SHOWN | 0 | 
The **NavDestination** component is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_HIDDEN | 1 | 

The **NavDestination** component is hidden.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_APPEAR12+ | 2 | 

The **NavDestination** component is attached to the component tree.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_DISAPPEAR12+ | 3 | 

The **NavDestination** component is detached from the component tree.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_WILL\_SHOW12+ | 4 | 

The **NavDestination** component is about to be displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_WILL\_HIDE12+ | 5 | 

The **NavDestination** component is about to be hidden.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_WILL\_APPEAR12+ | 6 | 

The **NavDestination** component is about to be mounted to the component tree.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_WILL\_DISAPPEAR12+ | 7 | 

The **NavDestination** component is about to be unmounted from the component tree.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ON\_ACTIVE17+ | 8 | 

The **NavDestination** component is active.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| ON\_INACTIVE17+ | 9 | 

The **NavDestination** component is inactive.

**Atomic service API**: This API can be used in atomic services since API version 17.

 |
| ON\_BACKPRESS12+ | 100 | 

The back button is pressed on the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ScrollEventType12+

Enumerates the scroll event types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SCROLL\_START | 0 | The scroll event starts. |
| SCROLL\_STOP | 1 | The scroll event ends. |

#### RouterPageState

Enumerates the states of a page during routing. **RouterPageState** is used in [RouterPageInfo](#routerpageinfo) as the callback parameter for passive observation via [routerPageUpdate](#uiobserveronrouterpageupdate11).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ABOUT\_TO\_APPEAR | 0 | The page is about to be displayed. |
| ABOUT\_TO\_DISAPPEAR | 1 | The page is about to be destroyed. |
| ON\_PAGE\_SHOW | 2 | The page is displayed. |
| ON\_PAGE\_HIDE | 3 | The page is hidden. |
| ON\_BACK\_PRESS | 4 | The page is returned. |

#### TabContentState12+

Enumerates the **TabContent** component states.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ON\_SHOW | 0 | The **TabContent** component is displayed. |
| ON\_HIDE | 1 | The **TabContent** component is hidden. |

#### NavDestinationInfo

Provides information about the **NavDestination** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| navigationId | [ResourceStr](../../../arkts-components/common-definitions/basic-types/document.md#resourcestr) | No | No | 
ID of the **Navigation** component that contains the target **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| name | [ResourceStr](../../../arkts-components/common-definitions/basic-types/document.md#resourcestr) | No | No | 

Name of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| state | [NavDestinationState](#navdestinationstate) | No | No | 

State of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| index12+ | number | No | No | 

Index of the **NavDestination** component in the navigation stack.

**Atomic service API**: This API can be used in atomic services since API version 12.

Value range: \[0, +∞)

 |
| param12+ | Object | No | Yes | 

Parameters of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| navDestinationId12+ | string | No | No | 

Unique ID of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mode15+ | [NavDestinationMode](../../../arkts-components/navigation-and-switching/navdestination/document.md#navdestinationmode11) | No | Yes | 

Mode of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |
| uniqueId15+ | number | No | Yes | 

Unique ID of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### NavigationInfo12+

Provides information about the **Navigation** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| navigationId | string | No | No | 
ID of the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| pathStack | [NavPathStack](../../../arkts-components/navigation-and-switching/navigation/document.md#navpathstack10) | No | No | 

Navigation controller of the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| uniqueId20+ | number | No | Yes | 

Unique ID of the **Navigation** component, which can be obtained through [queryNavigationInfo](../../../arkts-components/custom-components/custom-component-built-in-apis/document.md#querynavigationinfo12).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ScrollEventInfo12+

Provides the scroll event information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | 
ID of the scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| uniqueId | number | No | No | 

Unique ID of the scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| scrollEvent | [ScrollEventType](#scrolleventtype12) | No | No | 

Enumerates the scroll event types.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| offset | number | No | No | 

Current offset of the scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| axis20+ | [Axis](../../../arkts-components/common-definitions/enums/document.md#axis) | No | Yes | 

Scroll direction of the scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### ObserverOptions12+

Describes the observer options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | Component ID. |

#### RouterPageInfo

Provides the information contained in **RouterPageInfo**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | No | No | Context of the router page that invokes the lifecycle callback. |
| index | number | No | No | 
Position of the router page that invokes the lifecycle callback, in the navigation stack.

Value range: \[0, +∞)

 |
| name | string | No | No | Name of the page that invokes the lifecycle callback. |
| path | string | No | No | Path of the page that invokes the lifecycle callback. |
| state | [RouterPageState](#routerpagestate) | No | No | State of the router page that invokes the lifecycle callback. |
| pageId12+ | string | No | No | Unique ID of the router page that invokes the lifecycle callback. |

#### DensityInfo12+

Provides the information contained in the callback when the screen pixel density changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | No | No | Context corresponding to the page when the screen pixel density changes. |
| density | number | No | No | 
Screen pixel density after the change.

Value range: \[0, +∞)

 |

#### NavDestinationSwitchInfo12+

Provides the information about page switching of the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | No | No | Context information corresponding to **Navigation** component that triggers page switching. |
| from | [NavDestinationInfo](#navdestinationinfo) | [NavBar](../../../arkts-components/navigation-and-switching/navigation/document.md#navbar12) | No | No | Source page for page switching. |
| to | [NavDestinationInfo](#navdestinationinfo) | [NavBar](../../../arkts-components/navigation-and-switching/navigation/document.md#navbar12) | No | No | Destination page for page switching. |
| operation | [NavigationOperation](../../../arkts-components/navigation-and-switching/navigation/document.md#navigationoperation11) | No | No | Page switching operation type. |

#### NavDestinationSwitchObserverOptions12+

Provides the observer options for the page switching event of the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| navigationId | [ResourceStr](../../../arkts-components/common-definitions/basic-types/document.md#resourcestr) | No | No | ID of the target **Navigation** component. |

#### TextChangeEventInfo22+

Provides information about text changes in input fields.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | ID of the text input component. |
| uniqueId | number | No | No | Unique ID of the text input component. |
| content | string | No | No | Text content after the change. |

#### TabContentInfo12+

Provides the **TabContent** switching information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| tabContentId | string | No | No | 
ID of the **TabContent** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| tabContentUniqueId | number | No | No | 

Unique ID of the **TabContent** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| state | [TabContentState](#tabcontentstate12) | No | No | 

Enumerates the **TabContent** component states.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| index | number | No | No | 

Index of the **TabContent** component. The index is zero-based.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| id | string | No | No | 

ID of the **Tabs** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| uniqueId | number | No | No | 

Unique ID of the **Tabs** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| lastIndex22+ | number | No | Yes | 

Index of the previously focused **TabContent** component. The index is zero-based. This parameter is available only in the callback of [on('tabChange')](../ohos-arkui-uicontext-uicontext/class-uiobserver/document.md#ontabchange22).

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### WindowSizeLayoutBreakpointInfo22+

Provides information about window size layout breakpoint changes.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| widthBreakpoint | [WidthBreakpoint](../../../arkts-components/common-definitions/enums/document.md#widthbreakpoint13) | Yes | No | Layout breakpoint for window width. |
| heightBreakpoint | [HeightBreakpoint](../../../arkts-components/common-definitions/enums/document.md#heightbreakpoint13) | Yes | No | Layout breakpoint for window height. |

#### uiObserver.on('navDestinationUpdate')

on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void

Subscribes to status changes of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| callback | Callback<[NavDestinationInfo](#navdestinationinfo)\> | Yes | Callback used to return the result. It provides the current state of the **NavDestination** component. |

**Example**

// Index.ets
// Example usage of uiObserver.on('navDestinationUpdate', callback)
// uiObserver.off('navDestinationUpdate', callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    // Register a listener.
    uiObserver.on('navDestinationUpdate', (info) => {
      console.info(\`NavDestination state update ${JSON.stringify(info)}\`);
    });
  }

  aboutToDisappear() {
    // Unregister the listener.
    uiObserver.off('navDestinationUpdate');
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}

#### uiObserver.off('navDestinationUpdate')

off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void

Unsubscribes from status changes of the **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| callback | Callback<[NavDestinationInfo](#navdestinationinfo)\> | No | Callback used to return the result. It provides the current state of the **NavDestination** component. |

**Example**

See the example for [uiObserver.on('navDestinationUpdate')](#uiobserveronnavdestinationupdate).

#### uiObserver.on('navDestinationUpdate')

on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<NavDestinationInfo>): void

Subscribes to status changes of the **NavDestination** component. Compared with [uiObserver.on](#uiobserveronnavdestinationupdate), this API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component to observe.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| options | { navigationId: [ResourceStr](../../../arkts-components/common-definitions/basic-types/document.md#resourcestr) } | Yes | ID of the target **Navigation** component. |
| callback | Callback<[NavDestinationInfo](#navdestinationinfo)\> | Yes | Callback used to return the result. It provides the current state of the **NavDestination** component. |

**Example**

// Index.ets
// Example usage of uiObserver.on('navDestinationUpdate', navigationId, callback)
// uiObserver.off('navDestinationUpdate', navigationId, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    // Register a listener with the specified Navigation component ID.
    uiObserver.on('navDestinationUpdate', { navigationId: "testId" }, (info) => {
      console.info(\`NavDestination state update ${JSON.stringify(info)}\`);
    });
  }

  aboutToDisappear() {
    // Unregister the listener.
    uiObserver.off('navDestinationUpdate', { navigationId: "testId" });
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .id("testId")
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}

#### uiObserver.off('navDestinationUpdate')

off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void

Unsubscribes from status changes of the **NavDestination** component. Compared with [uiObserver.off](#uiobserveroffnavdestinationupdate), this API supports the **options** parameter, which enables you to specify the ID of the target **Navigation** component to observe.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationUpdate'** for **NavDestination** component status change events. |
| options | { navigationId: [ResourceStr](../../../arkts-components/common-definitions/basic-types/document.md#resourcestr) } | Yes | ID of the target **Navigation** component. |
| callback | Callback<[NavDestinationInfo](#navdestinationinfo)\> | No | Callback used to return the result. It provides the current state of the **NavDestination** component. |

**Example**

See the example for [uiObserver.on('navDestinationUpdate')](#uiobserveronnavdestinationupdate-1).

#### uiObserver.on('scrollEvent')12+

on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void

Listens for the start and end of scroll events of all scrollable components. Supported components include [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md), and [ArcList](../../../arkts-components/scroll-and-swipe/arclist/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'scrollEvent'** indicates the start and end of a scroll event. |
| callback | Callback<[ScrollEventInfo](#scrolleventinfo12)\> | Yes | Callback used to return the result. It returns the information about the scroll event. |

**Example**

See the example for [uiObserver.off('scrollEvent')](#uiobserveroffscrollevent12-1).

#### uiObserver.off('scrollEvent')12+

off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void

Unregisters the listener for the start and end of scroll events of all scrollable components. Supported components include [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md), and [ArcList](../../../arkts-components/scroll-and-swipe/arclist/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'scrollEvent'** indicates the start and end of a scroll event. |
| callback | Callback<[ScrollEventInfo](#scrolleventinfo12)\> | No | Callback used to return the result. It returns the information about the scroll event. |

**Example**

See the example for [uiObserver.off('scrollEvent')](#uiobserveroffscrollevent12-1).

#### uiObserver.on('scrollEvent')12+

on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void

Listens for the start and end of scroll events of a specific scrollable component identified by its ID. Supported components include [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md), and [ArcList](../../../arkts-components/scroll-and-swipe/arclist/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'scrollEvent'** indicates the start and end of a scroll event. |
| options | [ObserverOptions](#observeroptions12) | Yes | ID of the target scrollable component. |
| callback | Callback<[ScrollEventInfo](#scrolleventinfo12)\> | Yes | Callback used to return the result. It returns the information about the scroll event. |

**Example**

See the example for [uiObserver.off('scrollEvent')](#uiobserveroffscrollevent12-1).

#### uiObserver.off('scrollEvent')12+

off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void

Unregisters the listener for the start and end of scroll events of a specific scrollable component identified by its ID. Supported components include [List](../../../arkts-components/scroll-and-swipe/list/document.md), [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md), [Scroll](../../../arkts-components/scroll-and-swipe/scroll/document.md), [WaterFlow](../../../arkts-components/scroll-and-swipe/waterflow/document.md), and [ArcList](../../../arkts-components/scroll-and-swipe/arclist/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'scrollEvent'** indicates the start and end of a scroll event. |
| options | [ObserverOptions](#observeroptions12) | Yes | ID of the target scrollable component. |
| callback | Callback<[ScrollEventInfo](#scrolleventinfo12)\> | No | Callback used to return the result. It returns the information about the scroll event. |

**Example**

import { uiObserver } from '@kit.ArkUI'

@Entry
@Component
struct Index {
  scroller: Scroller = new Scroller();
  options: uiObserver.ObserverOptions = { id: 'testId' };
  private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7\]

  build() {
    Column() {
      Column() {
        Scroll(this.scroller) {
          Column() {
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
        .id('testId')
        .height('80%')
      }
      .width('100%')

      Row() {
        Button('UIObserver on')
          .onClick(() => {
            // Register a listener.
            uiObserver.on('scrollEvent', (info) => {
              console.info(\`scrollEventInfo ${JSON.stringify(info)}\`);
            });
          })
        Button('UIObserver off')
          .onClick(() => {
            // Unregister the listener.
            uiObserver.off('scrollEvent');
          })
      }

      Row() {
        Button('UIObserverWithId on')
          .onClick(() => {
            // Register a listener with the specified component ID.
            uiObserver.on('scrollEvent', this.options, (info) => {
              console.info(\`scrollEventInfo ${JSON.stringify(info)}\`);
            });
          })
        Button('UIObserverWithId off')
          .onClick(() => {
            // Unregister the listener.
            uiObserver.off('scrollEvent',this.options);
          })
      }
    }
    .height('100%')
  }
}

#### uiObserver.on('routerPageUpdate')11+

on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void

Subscribes to state changes of the page during routing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'routerPageUpdate'**, which indicates the state change event of the page during routing. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<[RouterPageInfo](#routerpageinfo)\> | Yes | Callback used to return the result. If **pageInfo** is passed, the current page state is returned. |

**Example**

// used in UIAbility
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { UIContext, window, uiObserver } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  private uiContext: UIContext | null = null;

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // Subscribe to the target events within the scope of the page under the ability context.
    uiObserver.on('routerPageUpdate', this.context, (info: uiObserver.RouterPageInfo) => {
      console.info(\`\[uiObserver\]\[abilityContext\] got info: ${JSON.stringify(info)}\`)
    })
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => {
      windowStage.getMainWindow((err: BusinessError, data) => {
        let windowInfo: window.Window = data;
        // Obtain a UIContext instance.
        this.uiContext = windowInfo.getUIContext();
        // Subscribe to the target events within the scope of the page under the UI context.
        uiObserver.on('routerPageUpdate', this.uiContext, (info: uiObserver.RouterPageInfo)=>{
          console.info(\`\[uiObserver\]\[uiContext\] got info: ${JSON.stringify(info)}\`)
        })
      })
    });
  }

  // ... other function in EntryAbility
}

#### uiObserver.off('routerPageUpdate')11+

off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void

Unsubscribes from state changes of the page during routing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is fixed at **'routerPageUpdate'**, which indicates the state change event of the page during routing. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<[RouterPageInfo](#routerpageinfo)\> | No | Target listener to unregister. |

**Example**

// used in UIAbility
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  // Before actual use, uiContext must be assigned a value. For details, see the example for uiObserver.on('routerPageUpdate').
  private uiContext: UIContext | null = null;

  onDestroy(): void {
    // Unregister all callbacks for the routerPageUpdate event under the current ability context.
    uiObserver.off('routerPageUpdate', this.context)
  }

  onWindowStageDestroy(): void {
    // Unregister all callbacks for the routerPageUpdate event under the UI context.
    if (this.uiContext) {
      uiObserver.off('routerPageUpdate', this.uiContext);
    }
  }

  // ... other function in EntryAbility
}

#### uiObserver.on('densityUpdate')12+

on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void

Listens for screen pixel density changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'densityUpdate'** for screen pixel density change events. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<[DensityInfo](#densityinfo12)\> | Yes | Callback used to return the result. It provides information about the changed screen pixel density. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State density: number = 0;
  @State message: string = 'Listener not registered';

  densityUpdateCallback = (info: uiObserver.DensityInfo) => {
    this.density = info.density;
    this.message = 'DPI after change:' + this.density.toString();
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Subscribe to Screen Pixel Density Changes')
        .onClick(() => {
          this.message = 'Listener registered'
          uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
    }
  }
}

#### uiObserver.off('densityUpdate')12+

off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void

Unregisters the listener for screen pixel density changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'densityUpdate'** for screen pixel density change events. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<[DensityInfo](#densityinfo12)\> | No | Target listener to unregister. If no parameter is provided, all listeners for the **densityUpdate** event under the current UI context are unregistered. |

import { uiObserver, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State density: number = 0;
  @State message: string = 'Listener not registered'

  densityUpdateCallback = (info: uiObserver.DensityInfo) => {
    this.density = info.density;
    this.message = 'DPI after change:' + this.density.toString();
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Subscribe to Screen Pixel Density Changes')
        .margin({ bottom: 10 })
        .onClick(() => {
          this.message = 'Listener registered'
          uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
      Button('Unsubscribe from Screen Pixel Density Changes')
        .onClick(() => {
          this.message = 'Listener not registered'
          uiObserver.off('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
    }
  }
}

#### uiObserver.on('willDraw')12+

on(type: 'willDraw', context: UIContext, callback: Callback<void>): void

Listens for drawing instruction dispatch in each frame.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event event. The value **'willDraw'** indicates whether drawing is about to occur. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  willDrawCallback = () => {
    console.info("willDraw instruction dispatched.");
  }
  build() {
    Column() {
      Button('Listen for Drawing Instruction Dispatch')
        .onClick(() => {
          uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
        })
    }
  }
}

#### uiObserver.off('willDraw')12+

off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void

Unregisters the listener for drawing instruction dispatch in each frame.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event event. The value **'willDraw'** indicates whether drawing is about to occur. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<void> | No | Target listener to unregister. |

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  willDrawCallback = () => {
    console.info("willDraw instruction dispatched.")
  }

  build() {
    Column() {
      Button('Listen for Drawing Instruction Dispatch')
        .margin({ bottom: 10 })
        .onClick(() => {
          uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
        })
      Button('Unregister Drawing Instruction Dispatch Listener')
        .onClick(() => {
          uiObserver.off('willDraw', this.getUIContext(), this.willDrawCallback);
        })
    }
  }
}

#### uiObserver.on('didLayout')12+

on(type: 'didLayout', context: UIContext, callback: Callback<void>): void

Listens for layout completion status in each frame.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'didLayout'** indicates whether the layout has been completed. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  didLayoutCallback = () => {
    console.info("Layout completed.");
  }
  build() {
    Column() {
      Button('Listen for Layout Completion')
        .onClick(() => {
          uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
    }
  }
}

#### uiObserver.off('didLayout')12+

off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void

Unregisters the listener for layout completion status in each frame.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **'didLayout'** indicates whether the layout has been completed. |
| context | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | Callback<void> | No | Target listener to unregister. |

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  didLayoutCallback = () => {
    console.info("Layout completed.")
  }

  build() {
    Column() {
      Button('Listen for Layout Completion')
        .margin({ bottom: 10 })
        .onClick(() => {
          uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
      Button('Unsubscribe from Layout Completion')
        .onClick(() => {
          uiObserver.off('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
    }
  }
}

#### uiObserver.on('navDestinationSwitch')12+

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void

Subscribes to **Navigation** component page switching events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationSwitch'** for **Navigation** component page switching events. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target scope for page switching events. |
| callback | Callback<[NavDestinationSwitchInfo](#navdestinationswitchinfo12)\> | Yes | Callback used to return the result. It provides page switching event information through **NavDestinationSwitchInfo**. |

**Example**

// EntryAbility.ets
// Example usage of uiObserver.on('navDestinationSwitch', UIAbilityContext, callback)
// uiObserver.off('navDestinationSwitch', UIAbilityContext, callback)
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, window } from '@kit.ArkUI';
import { hilog } from "@kit.PerformanceAnalysisKit";

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(\`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}\`)
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    uiObserver.on('navDestinationSwitch', this.context, callbackFunc);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    uiObserver.off('navDestinationSwitch', this.context, callbackFunc);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

// Index.ets
// Example usage of uiObserver.on('navDestinationSwitch', UIContext, callback)
// uiObserver.off('navDestinationSwitch', UIContext, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(\`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}\`)
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationSwitch', this.getUIContext(), callbackFunc)
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationSwitch', this.getUIContext(), callbackFunc)
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}

#### uiObserver.off('navDestinationSwitch')12+

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void

Unsubscribes from **Navigation** component page switching events.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationSwitch'** for **Navigation** component page switching events. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target scope for page switching events. |
| callback | Callback<[NavDestinationSwitchInfo](#navdestinationswitchinfo12)\> | No | Target listener to unregister. |

**Example**

See the example for [uiObserver.on('navDestinationSwitch')](#uiobserveronnavdestinationswitch12).

#### uiObserver.on('navDestinationSwitch')12+

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void

Subscribes to **Navigation** component page switching events. Compared with [uiObserver.on](#uiobserveronnavdestinationswitch12), this API supports the **observerOptions** parameter, which enables you to configure observation options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationSwitch'** for **Navigation** component page switching events. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target scope for page switching events. |
| observerOptions | [NavDestinationSwitchObserverOptions](#navdestinationswitchobserveroptions12) | Yes | Observer configuration options. |
| callback | Callback<[NavDestinationSwitchInfo](#navdestinationswitchinfo12)\> | Yes | Callback used to return the result. It provides page switching event information through **NavDestinationSwitchInfo**. |

**Example**

// EntryAbility.ets
// Example usage of uiObserver.on('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
// uiObserver.off('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { uiObserver, window } from '@kit.ArkUI';
import { hilog } from "@kit.PerformanceAnalysisKit"

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(\`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}\`)
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    uiObserver.on('navDestinationSwitch', this.context, {
      navigationId: "myNavId"
    }, callbackFunc);
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    uiObserver.off('navDestinationSwitch', this.context, {
      navigationId: "myNavId"
    }, callbackFunc);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

// Index.ets
// Example usage of uiObserver.on('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
// uiObserver.off('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
import { uiObserver } from '@kit.ArkUI';

@Component
struct PageOne {
  build() {
    NavDestination() {
      Text("pageOne")
    }.title("pageOne")
  }
}

function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
  console.info(\`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}\`)
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  PageBuilder(name: string) {
    PageOne()
  }

  aboutToAppear() {
    uiObserver.on('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
  }

  aboutToDisappear() {
    uiObserver.off('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
  }

  build() {
    Column() {
      Navigation(this.stack) {
        Button("push").onClick(() => {
          this.stack.pushPath({ name: "pageOne" });
        })
      }
      .id("myNavId")
      .title("Navigation")
      .navDestination(this.PageBuilder)
    }
    .width('100%')
    .height('100%')
  }
}

#### uiObserver.off('navDestinationSwitch')12+

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void

Unsubscribes from **Navigation** component page switching events. Compared with [uiObserver.off](#uiobserveroffnavdestinationswitch12), this API supports the **observerOptions** parameter, which enables you to configure observation options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'navDestinationSwitch'** for **Navigation** component page switching events. |
| context | [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | Yes | Context information, which is used to specify the target scope for page switching events. |
| observerOptions | [NavDestinationSwitchObserverOptions](#navdestinationswitchobserveroptions12) | Yes | Observer configuration options. |
| callback | Callback<[NavDestinationSwitchInfo](#navdestinationswitchinfo12)\> | No | Target listener to unregister. |

**Example**

See the example for [uiObserver.on('navDestinationSwitch')](#uiobserveronnavdestinationswitch12-1).

#### uiObserver.on('tabContentUpdate')12+

on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void

Subscribes to **TabContent** switch events. Unlike [on('tabChange')](../ohos-arkui-uicontext-uicontext/class-uiobserver/document.md#ontabchange22), this API does not support listening for the initial tab display event when the **Tabs** component is initialized.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| callback | Callback<[TabContentInfo](#tabcontentinfo12)\> | Yes | Callback used to return the result. It provides information about **TabContent** switch events through **TabContentInfo**. |

**Example**

import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(\`tabContentUpdate ${JSON.stringify(info)}\`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    // Register a listener.
    uiObserver.on('tabContentUpdate', callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listeners.
    uiObserver.off('tabContentUpdate', callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}

#### uiObserver.off('tabContentUpdate')12+

off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void

Unsubscribes from the **TabContent** switching event.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| callback | Callback<[TabContentInfo](#tabcontentinfo12)\> | No | Target listener to unregister. |

**Example**

See the example for [uiObserver.on('tabContentUpdate')](#uiobserverontabcontentupdate12).

#### uiObserver.on('tabContentUpdate')12+

on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void

Subscribes to **TabContent** page switching events for the specified **Tabs** component identified by its ID. Unlike [on('tabChange')](../ohos-arkui-uicontext-uicontext/class-uiobserver/document.md#ontabchange22), this API does not support listening for the initial tab display event when the **Tabs** component is initialized.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| options | [ObserverOptions](#observeroptions12) | Yes | ID of the target **Tabs** component. |
| callback | Callback<[TabContentInfo](#tabcontentinfo12)\> | Yes | Callback used to return the result. It provides information about **TabContent** switch events through **TabContentInfo**. |

**Example**

import { uiObserver } from '@kit.ArkUI';

function callbackFunc(info: uiObserver.TabContentInfo) {
  console.info(\`tabContentUpdate ${JSON.stringify(info)}\`);
}

@Entry
@Component
struct TabsExample {

  aboutToAppear(): void {
    // Register a listener with the specified tab ID.
    uiObserver.on('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  aboutToDisappear(): void {
    // Unregister the listeners.
    uiObserver.off('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
  }

  build() {
    Column() {
      Tabs() {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#00CB87')
        }.tabBar('green').id('tabContentId0')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar('blue').id('tabContentId1')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar('yellow').id('tabContentId2')

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92')
        }.tabBar('pink').id('tabContentId3')
      }
      .width(360)
      .height(296)
      .backgroundColor('#F1F3F5')
      .id('tabsId')
    }.width('100%')
  }
}

#### uiObserver.off('tabContentUpdate')12+

off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void

Unsubscribes from **TabContent** page switching events for the specified **Tabs** component identified by its ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. Set to **'tabContentUpdate'** for **TabContent** page switching events. |
| options | [ObserverOptions](#observeroptions12) | Yes | ID of the target **Tabs** component. |
| callback | Callback<[TabContentInfo](#tabcontentinfo12)\> | No | Target listener to unregister. |

**Example**

See the example for [uiObserver.on('tabContentUpdate')](#uiobserverontabcontentupdate12-1).
