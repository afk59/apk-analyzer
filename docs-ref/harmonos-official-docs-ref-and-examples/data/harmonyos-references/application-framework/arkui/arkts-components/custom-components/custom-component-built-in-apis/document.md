# Custom Component Built-in APIs

Custom component built-in APIs are APIs predefined on the base class of custom components in the ArkUI framework. You can call these APIs on the instance of a custom component to obtain information, such as the UI context, about the instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/VVsCLBiLTdi-h_A9oe78OA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6A8CDF80357B39C7E52BCEB9326EFD78DC9139859990AA791A5A97EC84AF1E3)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### getUIContext

getUIContext(): UIContext

Obtains the **UIContext** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [UIContext](#uicontext) | **UIContext** instance obtained. If this API is used in an asynchronously called callback method, or if the initial call of this API does not occur in the current page, the API call may occur after the custom component is destroyed, returning **undefined**. |

#### UIContext

type UIContext = UIContext

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md) | **UIContext** instance obtained. |

**Example**

import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uiContext: UIContext = this.getUIContext();
  }

  build() {
    // ...
  }
}

#### getUniqueId12+

getUniqueId(): number

Obtains the unique ID of this component. This unique ID is assigned by the system to each component. If this API is called before the component's corresponding node is created or after it has been destroyed, an invalid unique ID, which is **\-1**, will be returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unique ID of the current Component. |

**Example**

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uniqueId: number = this.getUniqueId();
  }

  build() {
    // ...
  }
}

#### queryNavDestinationInfo

queryNavDestinationInfo(): NavDestinationInfo | undefined;

Queries the **NavDestination** information of this custom component. This API has effect only when the component is contained within a **NavDestination** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [NavDestinationInfo](#navdestinationinfo) | undefined | **NavDestinationInfo** instance obtained. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Component
export struct NavDestinationExample {
  build() {
    NavDestination() {
      MyComponent()
    }
  }
}

@Component
struct MyComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined

  aboutToAppear() {
    // this refers to the custom node MyComponent and searches for the nearest parent node of the NavDestination type from this node upwards.
    this.navDesInfo = this.queryNavDestinationInfo();
    console.info('get navDestinationInfo: ' + JSON.stringify(this.navDesInfo));
  }

  build() {
    // ...
  }
}

#### queryNavDestinationInfo18+

queryNavDestinationInfo(isInner: Optional<boolean>): NavDestinationInfo | undefined

Queries the information about the nearest **NavDestination** component in the navigation stack for a custom component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isInner | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to search inward for the nearest **NavDestination** component in the navigation stack.

**true**: Search inward.

**false**: Search outward.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [NavDestinationInfo](#navdestinationinfo) | undefined | **NavDestinationInfo** instance obtained. |

**Example**

// Index.ets
@Entry
@Component
struct NavigationExample {
  pageInfo: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPath({ name: 'pageOne' }); // Push the navigation destination page specified by name to the navigation stack.
          })
      }
    }.title('NavIndex')
  }
}

// PageOne.ets
import { uiObserver } from '@kit.ArkUI';

@Builder
export function PageOneBuilder() {
  PageOneComponent()
}

@Component
export struct PageOneComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined;
  @State text: string = '';
  build() {
    NavDestination() {
      Column() {
        Button('Search Inward')
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            // Search inward for the NavDestination information for PageOne.
            this.navDesInfo = this.queryNavDestinationInfo(true);
            this.text = JSON.stringify(this.navDesInfo?.name).toString();
          })
        Text('The NavDestination component found inward is:' + this.text)
          .width('80%')
          .height(50)
          .margin(50)
          .fontSize(20)
        MyComponent()
      }.width('100%').height('100%')
    }
    .title('pageOne')
  }
}

@Component
struct MyComponent {
  navDesInfo: uiObserver.NavDestinationInfo | undefined;
  @State text: string = '';

  build() {
    Column() {
      Button('Search Outward')
        .width('80%')
        .height(40)
        .margin(20)
        .onClick(() => {
          // Search outward for the NavDestination information for PageOne.
          this.navDesInfo = this.queryNavDestinationInfo(false);
          this.text = JSON.stringify(this.navDesInfo?.name).toString();
        })
      Text('The NavDestination component found outward is:' + this.text)
        .width('80%')
        .height(50)
        .margin(50)
        .fontSize(20)
    }
  }
}

// route\_map.json
{
  "routerMap": \[
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    }
  \]
}

#### NavDestinationInfo

type NavDestinationInfo = NavDestinationInfo

Defines a **NavDestinationInfo** object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [NavDestinationInfo](../../../arkts-api/ui/ohos-arkui-observer-observer/document.md#navdestinationinfo) | **NavDestinationInfo** instance obtained. |

#### queryNavigationInfo12+

queryNavigationInfo(): NavigationInfo | undefined

Queries the **Navigation** information of this custom component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [NavigationInfo](#navigationinfo12) | undefined | **NavigationInfo** instance obtained. |

**Example**

// index.ets
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct MainPage {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      // ...
    }.id("NavigationId")
  }
}

@Component
export struct PageOne {
  pathStack: NavPathStack = new NavPathStack();

  aboutToAppear() {
    // this refers to the custom node PageOne and searches for the nearest parent node of the Navigation type from this node upwards.
    let navigationInfo: uiObserver.NavigationInfo | undefined = this.queryNavigationInfo();
    console.info('get navigationInfo: ' + JSON.stringify(navigationInfo));
    if (navigationInfo !== undefined) {
      this.pathStack = navigationInfo.pathStack;
    }
  }

  build() {
    NavDestination() {
      // ...
    }.title('PageOne')
  }
}

#### NavigationInfo12+

type NavigationInfo = NavigationInfo

Defines a **NavigationInfo** object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [NavigationInfo](../../../arkts-api/ui/ohos-arkui-observer-observer/document.md#navigationinfo12) | **NavigationInfo** instance obtained. |

#### queryRouterPageInfo12+

queryRouterPageInfo(): RouterPageInfo | undefined;

Obtains a **RouterPageInfo** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [RouterPageInfo](#routerpageinfo12) | undefined | **RouterPageInfo** instance obtained. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let info: uiObserver.RouterPageInfo | undefined = this.queryRouterPageInfo();
  }

  build() {
    // ...
  }
}

#### RouterPageInfo12+

type RouterPageInfo = RouterPageInfo

Defines a **RouterPageInfo** object.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 12.

| Type | Description |
| :-- | :-- |
| [RouterPageInfo](../../../arkts-api/ui/ohos-arkui-observer-observer/document.md#routerpageinfo) | **RouterPageInfo** instance obtained. |

#### getDialogController18+

getDialogController(): PromptActionDialogController | undefined

Obtains a **PromptActionDialogController** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PromptActionDialogController](#promptactiondialogcontroller18) | undefined | **PromptActionDialogController** instance obtained. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent } from '@kit.ArkUI';

class Params {
  text: string = "";
  constructor(text: string) {
    this.text = text;
  }
}

@ComponentV2
struct MyComponent {
  build() {
    Column() {
      Button('Close Dialog')
        .onClick(() => {
          let ctrl: PromptActionDialogController = this.getDialogController();
          if (ctrl != undefined) {
            ctrl.close();
          }
        })
    }
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({ bottom: 36 })
    MyComponent()
  }.backgroundColor('#FFF0F0F0')
}

@Entry
@ComponentV2
struct Index {
  @Local message: string = "hello";

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('click me')
          .fontSize(20)
          .onClick(() => {
            let ctx = this.getUIContext();
            let promptAction = ctx.getPromptAction();
            promptAction.openCustomDialog(new ComponentContent(ctx, wrapBuilder(buildText), new Params(this.message)))
              .catch((err: BusinessError) => {
                console.error("openCustomDialog error: " + err.code + " " + err.message);
              })
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}

#### PromptActionDialogController18+

type PromptActionDialogController = promptAction.DialogController

Defines a custom dialog box controller, which can be used to control a custom dialog box, including actions such as closing the dialog box. For details, see [promptAction.DialogController](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#dialogcontroller18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [promptAction.DialogController](../../../arkts-api/ui/ohos-promptaction-prompt/document.md#dialogcontroller18) | Instance of **promptAction.DialogController**. |
