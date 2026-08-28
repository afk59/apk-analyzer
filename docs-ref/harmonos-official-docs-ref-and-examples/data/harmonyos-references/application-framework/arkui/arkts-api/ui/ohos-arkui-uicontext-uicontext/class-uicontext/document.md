# Class (UIContext)

Implements a **UIContext** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/5hX-T8JtROWDG2WpX7SSDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40C0432B7BADF7B359518E01EA2604562034CE02986A6CFA556CC1EA35FF9971)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
    
-   The following APIs must be called through a corresponding UIContext instance. There are three ways to obtain a **UIContext** instance: (1) using the [getUIContext()](../../../window-manager/ohos-window-window/interface-window/document.md#getuicontext10) method from ohos.window; (2) using the built‑in method [getUIContext()](../../../../arkts-components/custom-components/custom-component-built-in-apis/document.md#getuicontext) of a custom component; (3) using static methods of the UIContext class such as [getCallingScopeUIContext](#getcallingscopeuicontext22). In this document, the **UIContext** instance is represented by **uiContext**.
    

**Example**

The following example illustrates the three ways to obtain a UIContext instance.

// The three approaches return identical UIContext instances.
// index.ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Button")
          .onClick(()=>{
            // Obtain using the built-in component method
            this.getUIContext()
            // Obtain using a static method of the UIContext class
            let uiContext = UIContext.getCallingScopeUIContext();
            // Additional logic
          })
    }
  }
}

// EntryAbility.ets
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Obtain using ohos.window
    windowStage.getMainWindowSync().getUIContext()
    // Additional logic
  }
}

#### constructor22+

constructor()

Construct a **UIContext** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/rL88dQAQQ1GywexVxAws2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E322B3E2DD4D3CB60A7D953DEE7CB4B684F27D98ADE884FAA38413F975261F2)

A **UIContext** object created using the constructor points to an ambiguous UI context, meaning it is not bound to any specific UI instance. The unique ID of such a UIContext instance is -1.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

function GetUIContextByAtomicInterface(): UIContext {
  let callingScopeUIContext = UIContext.getCallingScopeUIContext();
  if (callingScopeUIContext) {
    hilog.info(0x00, 'testTag', \`Get UIContext of calling scope.\`)
    return callingScopeUIContext;
  }
  let allContexts = UIContext.getAllUIContexts();
  let length = allContexts.length;
  if (length === 1) {
    hilog.info(0x00, 'testTag', \`Get UIContext of unique UI instance.\`)
    return allContexts\[0\];
  }
  let lastFocusedUIContext = UIContext.getLastFocusedUIContext();
  if (lastFocusedUIContext) {
    hilog.info(0x00, 'testTag', \`Get UIContext of last focused instance.\`)
    return lastFocusedUIContext;
  }
  let lastForegroundUIContext = UIContext.getLastForegroundUIContext();
  if (lastForegroundUIContext) {
    hilog.info(0x00, 'testTag', \`Get UIContext of last foregrounded instance.\`)
    return lastForegroundUIContext;
  }
  if (length !== 0) {
    hilog.info(0x00, 'testTag', \`Get UIContext with maximum instanceId.\`)
    return allContexts\[length - 1\];
  }
  hilog.info(0x00, 'testTag', \`Get UIContext of undefined calling scope.\`)
  return new UIContext();
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    let uiContext = this.getUIContext();
    hilog.info(0x00, 'testTag', \`aboutToAppear UIContext: ${uiContext.getId()}\`)
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let resolvedUIContext = UIContext.resolveUIContext();
          let contextByAtomicInterface = GetUIContextByAtomicInterface();
          hilog.info(0x00, 'testTag',
            \`UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}, contextByAtomicInterface: ${contextByAtomicInterface.getId()}\`);
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### getCallingScopeUIContext22+

static getCallingScopeUIContext(): UIContext | undefined

Obtains the UIContext of this [calling scope](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#basic-concepts). This API returns **undefined** if the calling scope is ambiguous.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/KH0UzmFaSQ6JbziA0mTvCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A479A33DF9672B74FF5A6572DE84F3593A01AD296EFEE4F10AA4057DBA22772)

The returned UIContext object may point to a destroyed UI instance, which usually occurs when an asynchronous task is dispatched from an instance that has already been destroyed. As such, you are advised to verify its validity via the [isAvailable](#isavailable20) API.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| UIContext | undefined | UIContext of the current [calling scope](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#basic-concepts). Returns **undefined** if the calling scope is ambiguous. |

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getCallingScopeUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### getLastFocusedUIContext22+

static getLastFocusedUIContext(): UIContext | undefined

Obtains the UIContext of the UI instance that most recently switched to the focused state.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| UIContext | undefined | UIContext of the UI instance that most recently switched to the focused state. Returns **undefined** if the most recently focused instance has been destroyed or if no instance has ever been focused. |

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getLastFocusedUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### getLastForegroundUIContext22+

static getLastForegroundUIContext(): UIContext | undefined

Obtains the UIContext of the UI instance that most recently switched to the foreground state.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| UIContext | undefined | UIContext of the UI instance that most recently switched to the foreground state. Returns **undefined** if the most recently foreground UI instance has been destroyed or if no UI instance has ever been in the foreground. |

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContext = UIContext.getLastForegroundUIContext();
          hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### getAllUIContexts22+

static getAllUIContexts(): UIContext\[\]

Obtains all currently valid UIContext instances.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| UIContext\[\] | Array of all currently valid UIContext instances. Returns an empty array if no valid UIContext instance exists. |

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          let uiContexts = UIContext.getAllUIContexts();
          hilog.info(0x00, 'testTag', \`There are ${uiContexts.length} UIContext(s)\`);
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### resolveUIContext22+

static resolveUIContext(): ResolvedUIContext

Obtains a UIContext instance along with its resolution strategy using a predefined priority order.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/ilOGG9z8Qg6NNtvDHY4LNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C38D6FD095A1E1D3E2B242191C60C1E6AFCD934F69E92DC43FD046EC1335D1D0)

This API resolves and returns a UIContext instance together with the strategy used to determine it,

based on the following priority rules (in order):

1.  UIContext in the current calling scope.
2.  If only one UI instance exists, its UIContext is returned.
3.  If a UI instance has switched to the focused state, and the most recently focused UI instance has not been destroyed, the UIContext of that most recently focused instance is returned.
4.  If a UI instance has switched to the foreground state, and the most recently foreground UI instance has not been destroyed, the UIContext of that most recently foreground instance is returned.
5.  If multiple UI instances exist, the UIContext with the largest unique instance ID is returned.
6.  If none of the above conditions are met, an invalid UIContext instance is returned.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ResolvedUIContext](../class-resolveduicontext/document.md) | UIContext instance along with its resolution strategy. |

**Example**

import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('click').onClick(() => {
        let resolvedUIContext = UIContext.resolveUIContext();
        hilog.info(0x00, 'testTag', \`UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}\`);
      })
    }
    .width(UIContext.resolveUIContext().px2vp(100))
    .height('100%')
  }
}

#### isAvailable20+

isAvailable(): boolean

Checks whether the UI instance corresponding to this **UIContext** object is valid. The **UIContext** object can be obtained using the [getUIContext](../../../window-manager/ohos-window-window/interface-window/document.md#getuicontext10) API. A UI instance is considered valid when the backend UI instance exists. UIContext objects created using **new UIContext()** have no corresponding UI instance. After multiple [loadContent](../../../window-manager/ohos-window-window/interface-window/document.md#loadcontent9) operations, old UI instances become invalid. In multi-window scenarios, when a window is closed, its UI instance becomes invalid. In summary, a UIContext object is invalid when it has no corresponding backend UI instance.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the UI instance corresponding to the current **UIContext** object is valid. The value **true** means that the UI instance is valid, and **false** means the opposite. |

**Example**

import { UIContext } from '@kit.ArkUI'

@Entry
@Component
struct UIContextCompare {
  @State result1: string = ""
  @State result2: string = ""

  build() {
    Column() {
      Text("getUIContext() result: " + this.result1)
        .fontSize(20)
        .margin(10)

      Text("new UIContext() result: " + this.result2)
        .fontSize(20)
        .margin(10)

      Divider().margin(20)

      Button("getUIContext()")
        .width("70%")
        .height(50)
        .margin(10)
        .onClick(() => {
          try {
            const ctx: UIContext = this.getUIContext();
            const available: boolean = ctx.isAvailable();
            this.result1 = \`Status: ${available} (Valid UI instance)\`;
            console.info("getUIContext test:", available);
          } catch (e) {
            this.result1 = "Error: " + (e instanceof Error ? e.message : String(e));
          }
        })

      Button("new UIContext()")
        .width("70%")
        .height(50)
        .margin(10)
        .onClick(() => {
          try {
            const ctx: UIContext = new UIContext();
            const available: boolean = ctx.isAvailable();
            this.result2 = \`Status: ${available} (Invalid UI instance)\`;
            console.info("new UIContext test:", available);
          } catch (e) {
            this.result2 = "Error: " + (e instanceof Error ? e.message : String(e));
          }
        })
    }
    .width("100%")
    .height("100%")
    .padding(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/4OukN8_zRnGuKs-wa0J3NQ/en-us_image_0000002568765053.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9E89677476FB19C52005D520F74E35821CA5408DDD5D0267F83F57D4BB0DA03)

#### getFont

getFont(): Font

Obtains a **Font** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Font](../class-font/document.md) | **Font** object. |

**Example**

See the example for [Font](../class-font/document.md).

#### getComponentUtils

getComponentUtils(): ComponentUtils

Obtains the **ComponentUtils** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ComponentUtils](../class-componentutils/document.md) | **ComponentUtils** object. |

**Example**

For the complete example, see [Example 1: Obtaining the ComponentUtils Object](../../ohos-arkui-componentutils-componentutils/document.md#example-1-obtaining-the-componentutils-object).

#### getUIInspector

getUIInspector(): UIInspector

Obtains the **UIInspector** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [UIInspector](../class-uiinspector/document.md) | **UIInspector** object. |

**Example**

See the example for [UIInspector](../class-uiinspector/document.md).

#### getUIObserver11+

getUIObserver(): UIObserver

Obtains the **UIObserver** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [UIObserver](../class-uiobserver/document.md) | **UIObserver** object. |

**Example**

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
    this.getUIContext().getUIObserver().on('navDestinationUpdate', (info) => {
      console.info('NavDestination state update', JSON.stringify(info));
    });
  }

  aboutToDisappear() {
    this.getUIContext().getUIObserver().off('navDestinationUpdate');
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

#### getId22+

getId(): number

Obtains the unique ID of a UI instance object. In multi-instance scenarios, you can use this unique ID to distinguish between different UI instance objects for easier management.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unique ID of the backend instance. The value range is \[-1, +∞). |

**Example**

@Entry
@Component
struct Index{
  build(){
    Column()
      .width("100%")
      .height("100%")
      .onClick(()=>{
      console.info(\`id:${this.getUIContext()?.getId()}\`);
    })
  }
}

#### getMediaQuery

getMediaQuery(): MediaQuery

Obtains a **MediaQuery** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaQuery](../class-mediaquery/document.md) | **MediaQuery** object. |

**Example**

See the [mediaquery Example](../../ohos-mediaquery-media-query/document.md#example).

#### getRouter

getRouter(): Router

Obtains a **Router** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Router](../class-router/document.md) | **Router** object. |

**Example**

See the example for [pushUrl](../class-router/document.md#pushurl).

#### getPromptAction

getPromptAction(): PromptAction

Obtains a **PromptAction** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PromptAction](../class-promptaction/document.md) | **PromptAction** object. |

**Example**

See the example for [PromptAction](../class-promptaction/document.md).

#### getOverlayManager12+

getOverlayManager(): OverlayManager

Obtains the **OverlayManager** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [OverlayManager](../class-overlaymanager/document.md) | **OverlayManager** instance obtained. |

**Example**

See the example for [OverlayManager](../class-overlaymanager/document.md).

#### setOverlayManagerOptions15+

setOverlayManagerOptions(options: OverlayManagerOptions): boolean

Sets the parameters for [OverlayManager](../class-overlaymanager/document.md). This API initializes the parameters of the **OverlayManager** before using its capabilities, including properties such as whether to render the overlay root node. It must be called before **getOverlayManager** and takes effect only once.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [OverlayManagerOptions](../interfaces-others/document.md#overlaymanageroptions15) | Yes | Parameters for **OverlayManager**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the setting is successful.

Returns **true** if the setting is successful; returns **false** otherwise.

 |

**Example**

See the example for [OverlayManager](../class-overlaymanager/document.md).

#### getOverlayManagerOptions15+

getOverlayManagerOptions(): OverlayManagerOptions

Obtains the current parameters of [OverlayManagerOptions](../interfaces-others/document.md#overlaymanageroptions15).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [OverlayManagerOptions](../interfaces-others/document.md#overlaymanageroptions15) | Current **OverlayManagerOptions** object. |

**Example**

See the example for [OverlayManager](../class-overlaymanager/document.md).

#### animateTo

animateTo(value: AnimateParam, event: () => void): void

Adds transition animations for state changes in closure code.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/KGpIapIuTuy7_AUxD2tBqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DE458855FB0457BE33CBE3A0C847D2B7C6333A912E9C39F630C7AFAFFD9E066)

-   Avoid using **animateTo** in **aboutToAppear** or **aboutToDisappear**.
-   When **animateTo** is called in [aboutToAppear](../../../../arkts-components/custom-components/custom-component-lifecycle/document.md#abouttoappear), the component's build method is not executed yet, and internal components are not created. This means the animation has no initial values to work with and will not function as expected.
-   During execution of [aboutToDisappear](../../../../arkts-components/custom-components/custom-component-lifecycle/document.md#abouttodisappear), the component is being destroyed, so animations should not be used.
-   When a component appears or disappears, animation effects can be added through [component transition](../../../../arkts-components/animation/component-transition-transition/document.md).
-   For properties that component transitions do not support, refer to [Example 2: Enabling a Component to Disappear After the Animation](../../../../arkts-components/animation/explicit-animation-animateto/document.md#example-2-enabling-a-component-to-disappear-after-the-animation), which uses **animateTo** to achieve the effect of the component disappearing after the animation finishes.
-   In certain scenarios, using animateTo with [state management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-state-management-overview#state-management-v2) may produce unexpected results. For details, see [Using animateTo Failed in State Management V2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-local#using-animateto-failed-in-state-management-v2).
-   When a UIAbility switches from the foreground to the background, any limited iteration animations that are currently running will end immediately, thereby triggering the [onFinish animation completion callback](../../../../arkts-components/animation/explicit-animation-animateto/document.md#animateparam).
-   If transition animations are turned off in Developer options, animations end on the current frame, and the **onFinish** callback is executed immediately. Avoid placing timing‑dependent functional logic inside this callback.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [AnimateParam](../../../../arkts-components/animation/explicit-animation-animateto/document.md#animateparam) | Yes | Animation settings. |
| event | () => void | Yes | Closure function that displays the animation. The system automatically inserts the transition animation if the state changes in the closure function. |

**Example**

// xxx.ets
@Entry
@Component
struct AnimateToExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  private flag: boolean = true;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn("no uiContext");
      return;
    }
  }

  build() {
    Column() {
      Button('change size')
        .width(this.widthSize)
        .height(this.heightSize)
        .margin(30)
        .onClick(() => {
          if (this.flag) {
            this.uiContext?.animateTo({
              duration: 2000,
              curve: Curve.EaseOut,
              iterations: 3,
              playMode: PlayMode.Normal,
              onFinish: () => {
                console.info('play end');
              }
            }, () => {
              this.widthSize = 150;
              this.heightSize = 60;
            });
          } else {
            this.uiContext?.animateTo({}, () => {
              this.widthSize = 250;
              this.heightSize = 100;
            });
          }
          this.flag = !this.flag;
        })
      Button('stop rotating')
        .margin(50)
        .rotate({ x: 0, y: 0, z: 1, angle: this.rotateAngle })
        .onAppear(() => {
          // The animation starts when the component appears.
          this.uiContext?.animateTo({
            duration: 1200,
            curve: Curve.Friction,
            delay: 500,
            iterations: -1, // The value -1 indicates that the animation is played for an unlimited number of times.
            playMode: PlayMode.Alternate,
            expectedFrameRateRange: {
              min: 10,
              max: 120,
              expected: 60,
            }
          }, () => {
            this.rotateAngle = 90
          });
        })
        .onClick(() => {
          this.uiContext?.animateTo({ duration: 0 }, () => {
            // The value of this.rotateAngle is 90 before the animation. In an animation with a duration of 0, changing the property stops any previous animations for that property and applies the new value immediately.
            this.rotateAngle = 0;
          });
        })
    }.width('100%').margin({ top: 5 })
  }
}

#### getSharedLocalStorage12+

getSharedLocalStorage(): LocalStorage | undefined

Obtains the **LocalStorage** instance shared by this stage.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Model restriction**: This API can be used only in the stage model.

**Return value**

| Type | Description |
| :-- | :-- |
| [LocalStorage](../../../../arkts-components/state-management-and-rendering-control/state-management-with-application-level-variables/document.md#localstorage9) | undefined | **LocalStorage** instance if it exists; **undefined** if it does not exist. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  storage: LocalStorage = new LocalStorage();

  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', this.storage);
  }
}

// Index.ets

@Entry
@Component
struct SharedLocalStorage {
  localStorage = this.getUIContext().getSharedLocalStorage();

  build() {
    Row() {
      Column() {
        Button("Change Local Storage to 47")
          .onClick(() => {
            this.localStorage?.setOrCreate("propA", 47);
          })
        Button("Get Local Storage")
          .onClick(() => {
            console.info(\`localStorage: ${this.localStorage?.get("propA")}\`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### getHostContext12+

getHostContext(): Context | undefined

Obtains the context of this ability.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Model restriction**: This API can be used only in the stage model.

**Return value**

| Type | Description |
| :-- | :-- |
| [Context](../types/document.md#context12) | undefined | Context of the ability. The context type depends on the ability type. For example, if this API is called in a page within a UIAbility window, the returned context type is [UIAbilityContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1). If this API is called in a page within an ExtensionAbility window, the returned context type is [ExtensionContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md). If the ability context does not exist, **undefined** is returned. |

**Example**

@Entry
@Component
struct Index {
  uiContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Text("cacheDir='"+this.uiContext?.getHostContext()?.cacheDir+"'")
          .fontSize(25)
          .border({ color:Color.Red, width:2 })
          .padding(50)
        Text("bundleCodeDir='"+this.uiContext?.getHostContext()?.bundleCodeDir+"'")
          .fontSize(25)
          .border({ color:Color.Red, width:2 })
          .padding(50)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### getFrameNodeById12+

getFrameNodeById(id: string): FrameNode | null

Obtains a FrameNode on the component tree based on the component ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [Component ID](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../../arkui/framenode/document.md) | null | FrameNode of the component or **null** if no matching component is found. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/OhKy89moRG69N2no-jxbsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0C2FA1A5B94CCE6BA8AD29ADDFB5B190F7E4DD0317FFE1336CDB68E3EF5CE08)

The **getFrameNodeById** API searches for a node with a specific ID by traversing the tree, which can lead to poor performance. To deliver better performance, use the [getAttachedFrameNodeById](#getattachedframenodebyid12) API.

**Example**

See [Example of Obtaining the Root Node](../../arkui/framenode/document.md#example-of-obtaining-the-root-node).

#### getAttachedFrameNodeById12+

getAttachedFrameNodeById(id: string): FrameNode | null

Obtains the FrameNode attached to the current window based on its component ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [Component ID](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../../arkui/framenode/document.md) | null | FrameNode of the component or **null** if no matching component is found. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/EwI80cj3TNSm4h2bKr4PPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=758B344C7017D1DEF19BFA210BEE03E75BBB747CB9ED93151C157BBA4AC6AC9C)

**getAttachedFrameNodeById** can only obtain nodes that are currently rendered on the screen.

**Example**

@Entry
@Component
struct MyComponent {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let node = this.getUIContext().getAttachedFrameNodeById("HelloWorld");
          console.info(\`Find HelloWorld Tag:${node!.getNodeType()} id:${node!.getUniqueId()}\`);
        })
    }
    .height('100%')
    .width('100%')
  }
}

#### getFrameNodeByUniqueId12+

getFrameNodeByUniqueId(id: number): FrameNode | null

Obtains the FrameNode of a component on the component tree using its **uniqueId**. The return value depends on the type of component associated with the **uniqueId**.

1.  If the **uniqueId** corresponds to a built-in component, the associated FrameNode is returned.
2.  If the **uniqueId** corresponds to a custom component: If the component has rendered content, its root node is returned, with the type **Common**; if the component has no rendered content, the FrameNode of its first child component is returned.
3.  If the **uniqueId** does not correspond to any component, **null** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Unique ID of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [FrameNode](../../arkui/framenode/document.md) | null | FrameNode of the component or **null** if no matching component is found. |

**Example**

import { UIContext, FrameNode } from '@kit.ArkUI';

@Entry
@Component
struct MyComponent {
  aboutToAppear() {
    let uniqueId: number = this.getUniqueId();
    let uiContext: UIContext = this.getUIContext();
    if (uiContext) {
      let node: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
    }
  }

  build() {
    // ...
  }
}

#### getPageInfoByUniqueId12+

getPageInfoByUniqueId(id: number): PageInfo

Obtains the router or navigation destination page information corresponding to the node that matches the specified **uniqueId**.

1.  If the node that matches the specified **uniqueId** is in a page, the router information (**routerPageInfo**) is returned.
2.  If the node that matches the specified **uniqueId** is in a **NavDestination** component, the navigation destination page information (**navDestinationInfo**) is returned.
3.  If the node that matches the specified **uniqueId** does not have the corresponding router or navigation destination page information, **undefined** is returned.
4.  Modal dialog boxes are not contained within any pages. If the node that matches the specified **uniqueId** is in a modal dialog box, for example, on a modal page constructed by [CustomDialog](../../../../arkts-components/dialog-boxes/custom-dialog-box-customdialog/document.md), [bindSheet](../../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#bindsheet), or [bindContentCover](../../../../arkts-components/universal-attributes/transition/modal-transition/document.md#bindcontentcover), **undefined** is returned for **routerPageInfo**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Unique ID of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PageInfo](../interfaces-others/document.md#pageinfo12) | Router or navigation destination page information corresponding to the specified node. |

**Example**

import { UIContext, PageInfo } from '@kit.ArkUI';

@Entry
@Component
struct PageInfoExample {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

  build() {
    Column() {
      Navigation(this.pageInfos) {
        NavDestination() {
          MyComponent()
        }
      }.id('navigation')
    }
  }
}

@Component
struct MyComponent {
  @State content: string = '';

  build() {
    Column() {
      Text('PageInfoExample')
      Button('click').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        const uniqueId: number = this.getUniqueId();
        const pageInfo: PageInfo = uiContext.getPageInfoByUniqueId(uniqueId);
        console.info('pageInfo: ' + JSON.stringify(pageInfo));
        console.info('navigationInfo: ' + JSON.stringify(uiContext.getNavigationInfoByUniqueId(uniqueId)));
      })
      TextArea({
        text: this.content
      })
      .width('100%')
      .height(100)
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}

#### getNavigationInfoByUniqueId12+

getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined

Obtains the navigation information corresponding to the node that matches the specified **uniqueId**.

1.  If the node that matches the specified **uniqueId** is in a **Navigation** component, the navigation information is returned.
2.  If the node that matches the specified **uniqueId** does not have the corresponding navigation information, **undefined** is returned.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | number | Yes | Unique ID of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| observer.[NavigationInfo](../../ohos-arkui-observer-observer/document.md#navigationinfo12) | undefined | Navigation information corresponding to the specified node. |

**Example**

See the example of [getPageInfoByUniqueId](#getpageinfobyuniqueid12).

#### showAlertDialog

showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void

Shows an alert dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/kw8Qo6tBRKm9Mu6EyoTUYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A461C5756432C8DD91872FD76872AE6B29E64A9BDC06924EE07C1AF14FC3B83)

The **showAlertDialog** with [showInSubWindow](../../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#alertdialogparam) set to **true** cannot be used in the input method window. For details, see the [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1) description.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AlertDialogParamWithConfirm](../../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#alertdialogparamwithconfirm) | [AlertDialogParamWithButtons](../../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#alertdialogparamwithbuttons) | [AlertDialogParamWithOptions](../../../../arkts-components/dialog-boxes/alert-dialog-box-alertdialog/document.md#alertdialogparamwithoptions10) | Yes | Shows an **AlertDialog** component in the given settings. |

**Example**

@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext()

  build() {
    Column() {
      Button('showAlertDialog')
        .onClick(() => {
          this.uiContext.showAlertDialog(
            {
              title: 'title',
              message: 'text',
              autoCancel: true,
              alignment: DialogAlignment.Bottom,
              offset: { dx: 0, dy: -20 },
              gridCount: 3,
              confirm: {
                value: 'button',
                action: () => {
                  console.info('Button-clicking callback');
                }
              },
              cancel: () => {
                console.info('Closed callbacks');
              }
            }
          );
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/07dYRcU5QJ-kjkSYobKiSw/en-us_image_0000002537765328.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DCCFC519EDE6A75169E1CCBBE29235ECA7C64BED8E2EC633051ABF322481D81)

#### showActionSheet

showActionSheet(value: ActionSheetOptions): void

Shows an action sheet in the given settings.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ActionSheetOptions](../../../../arkts-components/dialog-boxes/action-sheet-actionsheet/document.md#actionsheetoptions) | Yes | Parameters of the action sheet. |

**Example**

@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext()

  build() {
    Column() {
      Button('showActionSheet')
        .onClick(() => {
          this.uiContext.showActionSheet({
            title: 'ActionSheet title',
            message: 'message',
            autoCancel: true,
            confirm: {
              value: 'Confirm button',
              action: () => {
                console.info('Get ActionSheet handled');
              }
            },
            cancel: () => {
              console.info('ActionSheet canceled');
            },
            alignment: DialogAlignment.Bottom,
            offset: { dx: 0, dy: -10 },
            sheets: \[
              {
                title: 'apples',
                action: () => {
                  console.info('apples');
                }
              },
              {
                title: 'bananas',
                action: () => {
                  console.info('bananas');
                }
              },
              {
                title: 'pears',
                action: () => {
                  console.info('pears');
                }
              }
            \]
          });
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/wMdFKRVGQ0O4YQ0FaY0itA/en-us_image_0000002537925268.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A6F339DB48C34C34EAB1B01F01B5EAA0DB48FF23A0D190FE4517C9BF7E0CB38)

#### showDatePickerDialog

showDatePickerDialog(options: DatePickerDialogOptions): void

Shows a date picker dialog box in the given settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/_5xGPU9aQC2Nj71v6lnGvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E975AAA54829AA20C6629DD1D5D27E76505913971F09CF867E87F621E566E5E)

showDatePickerDialog does not support subwindows (showInSubwindow is set to true) in the input method type window. For details, see the restrictions of the input method framework [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [DatePickerDialogOptions](../../../../arkts-components/dialog-boxes/date-picker-dialog-box-datepickerdialog/document.md#datepickerdialogoptions) | Yes | Parameters of the date picker dialog box. |

**Example**

// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date("2010-1-1");

  build() {
    Row(){
      Column() {
        Button("DatePickerDialog")
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date("2000-1-1"),
              end: new Date("2100-12-31"),
              selected: this.selectedDate,
              showTime: true,
              useMilitaryTime: false,
              dateTimeOptions: { hour: "numeric", minute: "2-digit" },
              onDateAccept: (value: Date) => {
                // Use the setFullYear method to set the date when the OK button is touched. In this way, when the date picker dialog box is displayed again, the selected date is the date last confirmed.
                this.selectedDate = value;
                console.info("DatePickerDialog:onDateAccept()" + value.toString());
              },
              onCancel: () => {
                console.info("DatePickerDialog:onCancel()");
              },
              onDateChange: (value: Date) => {
                console.info("DatePickerDialog:onDateChange()" + value.toString());
              },
              onDidAppear: () => {
                console.info("DatePickerDialog:onDidAppear()");
              },
              onDidDisappear: () => {
                console.info("DatePickerDialog:onDidDisappear()");
              },
              onWillAppear: () => {
                console.info("DatePickerDialog:onWillAppear()");
              },
              onWillDisappear: () => {
                console.info("DatePickerDialog:onWillDisappear()");
              }
            })
          })
      }.width('100%')
    }.height('100%')
  }
}

#### showTimePickerDialog

showTimePickerDialog(options: TimePickerDialogOptions): void

Shows a time picker dialog box in the given settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/JBEAth-GRL6StFDOW8b0YQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B9197E09DAD180B60B0F2B892164C9EC102241B7A8973D9D4FD81CC0EE59FC9)

showTimePickerDialog with showInSubwindow set to true cannot be used in the input method type window. For details, see the restrictions of the input method framework [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TimePickerDialogOptions](../../../../arkts-components/dialog-boxes/time-picker-dialog-box-timepickerdialog/document.md#timepickerdialogoptions) | Yes | Parameters of the time picker dialog box. |

**Example**

// xxx.ets

class SelectTime{
  selectTime: Date = new Date('2020-12-25T08:30:00');
  hours(h:number,m:number){
    this.selectTime.setHours(h, m);
  }
}

@Entry
@Component
struct TimePickerDialogExample {
  @State selectTime: Date = new Date('2023-12-25T08:30:00');

  build() {
    Column() {
      Button('showTimePickerDialog')
        .margin(30)
        .onClick(() => {
          this.getUIContext().showTimePickerDialog({
            selected: this.selectTime,
            onAccept: (value: TimePickerResult) => {
              // Set selectTime to the time when the OK button is clicked. In this way, when the dialog box is displayed again, the selected time is the time when the operation was confirmed last time.
              let time = new SelectTime();
              if(value.hour && value.minute){
                time.hours(value.hour, value.minute);
              }
              console.info("TimePickerDialog:onAccept()" + JSON.stringify(value));
            },
            onCancel: () => {
              console.info("TimePickerDialog:onCancel()");
            },
            onChange: (value: TimePickerResult) => {
              console.info("TimePickerDialog:onChange()" + JSON.stringify(value));
            }
          });
        })
    }.width('100%').margin({ top: 5 })
  }
}

#### showTextPickerDialog

showTextPickerDialog(options: TextPickerDialogOptions): void

Shows a text picker dialog box in the given settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/uSXOZnpKSWGGTZPEnvVDFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=921AB9833E009645FE2372BFEA85A97FA3B3F8FDC1353A0840AA515F6158528F)

showTextPickerDialog with showInSubwindow set to true cannot be used in the input method type window. For details, see the restrictions of the input method framework [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextPickerDialogOptions](../../../../arkts-components/dialog-boxes/text-picker-dialog-box-textpickerdialog/document.md#textpickerdialogoptions) | Yes | Parameters of the text picker dialog box. |

**Example**

// xxx.ets

class SelectedValue{
  select: number = 2;
  set(val: number){
    this.select = val;
  }
}
class SelectedArray{
  select: number\[\] = \[\];
  set(val: number\[\]){
    this.select = val;
  }
}
@Entry
@Component
struct TextPickerDialogExample {
  @State selectTime: Date = new Date('2023-12-25T08:30:00');
  private fruits: string\[\] = \['apple1', 'orange2', 'peach3', 'grape4', 'banana5'\];
  private select: number  = 0;
  build() {
    Row(){
      Column() {
        Button('showTextPickerDialog')
          .margin(30)
          .onClick(() => {
            this.getUIContext().showTextPickerDialog({
              range: this.fruits,
              selected: this.select,
              onAccept: (value: TextPickerResult) => {
                // Set select to the index of the item selected when the OK button is touched. In this way, when the text picker dialog box is displayed again, the selected item is the one last confirmed.
                let selectedVal = new SelectedValue();
                let selectedArr = new SelectedArray();
                if (value.index){
                  value.index instanceof Array?selectedArr.set(value.index) : selectedVal.set(value.index);
                }
                console.info("TextPickerDialog:onAccept()" + JSON.stringify(value));
              },
              onCancel: () => {
                console.info("TextPickerDialog:onCancel()");
              },
              onChange: (value: TextPickerResult) => {
                console.info("TextPickerDialog:onChange()" + JSON.stringify(value));
              }
            });
          })
      }.width('100%').margin({ top: 5 })
    }.height('100%')
  }
}

#### showTextPickerDialog20+

showTextPickerDialog(style: TextPickerDialogOptions|TextPickerDialogOptionsExt): void

Shows a text picker dialog box in the given settings. This API extends **showTextPickerDialog** by adding support for the **TextPickerDialogOptionsExt** parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/XVIrqTndQsKVW_HqreX6aQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEF207FCE4DA10AA89B080D3CA931DF68258934247DA81279F9187550C51003E)

showTextPickerDialog with showInSubwindow set to true cannot be used in the input method type window. For details, see the restrictions of the input method framework [createPanel](../../../../../ime-kit/arkts-apis/ohos-inputmethodengine-input-method-service/document.md#createpanel10-1).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [TextPickerDialogOptions](../../../../arkts-components/dialog-boxes/text-picker-dialog-box-textpickerdialog/document.md#textpickerdialogoptions)| [TextPickerDialogOptionsExt](../../../../arkts-components/dialog-boxes/text-picker-dialog-box-textpickerdialog/document.md#textpickerdialogoptionsext20) | Yes | Parameters of the text picker dialog box. |

#### createAnimator

createAnimator(options: AnimatorOptions): AnimatorResult

Creates an **Animator** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](../../ohos-animator-animator/document.md#animatoroptions) | Yes | Animator options. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AnimatorResult](../../ohos-animator-animator/document.md#animatorresult) | Animator result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { AnimatorOptions, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Create the main window and set the home page for this ability.
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      let uiContext = windowStage.getMainWindowSync().getUIContext();
      let options:AnimatorOptions = {
        duration: 1500,
        easing: "friction",
        delay: 0,
        fill: "forwards",
        direction: "normal",
        iterations: 3,
        begin: 200.0,
        end: 400.0
      };
      uiContext.createAnimator(options);
    });
  }
}

#### createAnimator18+

createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

Creates an **AnimatorResult** object for animations. Compared to the previous [createAnimator](#createanimator) API, this API adds support for the [SimpleAnimatorOptions](../../ohos-animator-animator/document.md#simpleanimatoroptions18) type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [AnimatorOptions](../../ohos-animator-animator/document.md#animatoroptions) | [SimpleAnimatorOptions](../../ohos-animator-animator/document.md#simpleanimatoroptions18) | Yes | Animator options. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AnimatorResult](../../ohos-animator-animator/document.md#animatorresult) | Animator result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { SimpleAnimatorOptions, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Create the main window and set the home page for this ability.
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      let uiContext = windowStage.getMainWindowSync().getUIContext();
      let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
      uiContext.createAnimator(options);
    });
  }
}

#### runScopedTask

runScopedTask(callback: () => void): void

Executes the specified callback in this UI context.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

@Entry
@Component
struct Index {
  uiContext = this.getUIContext();

  build() {
    Row() {
      Column() {
        Button("run task").onClick(()=>{
          this.uiContext.runScopedTask(()=>{
            // do something
          })
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### setKeyboardAvoidMode11+

setKeyboardAvoidMode(value: KeyboardAvoidMode): void

Sets the avoidance mode for the virtual keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [KeyboardAvoidMode](../enums/document.md#keyboardavoidmode11) | Yes | 
Keyboard avoidance mode.

Default value: KeyboardAvoidMode.OFFSET

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/xe3825MbT6KnQgdK-9qQSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A5B404B01C94952207771E3DD78D8382D2193A2A7C78E9B7BFA41BAF4EAE403)

With **KeyboardAvoidMode.RESIZE**, the page is resized to prevent the virtual keyboard from obstructing the view. Regarding components on the page, those whose width and height are set in percentage are resized with the page, and those whose width and height are set to specific values are laid out according to their settings. With **KeyboardAvoidMode.RESIZE**, **expandSafeArea(\[SafeAreaType.KEYBOARD\],\[SafeAreaEdge.BOTTOM\])** does not take effect.

With **KeyboardAvoidMode.NONE**, keyboard avoidance is disabled, and the page will be covered by the displayed keyboard.

**setKeyboardAvoidMode** only affects page layouts. It does not apply to popup components, including the following: **Dialog**, **Popup**, **Menu**, **BindSheet**, **BindContentCover**, **Toast**, **OverlayManager**. For details about the avoidance mode of popup components, see [CustomDialogControllerOptions](../../../../arkts-components/dialog-boxes/custom-dialog-box-customdialog/document.md#customdialogcontrolleroptions).

**Example**

See [Example 4: Setting the Keyboard Avoidance Mode to Resize](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-4-setting-the-keyboard-avoidance-mode-to-resize), [Example 5: Setting Keyboard Avoidance Mode to Offset](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-5-setting-keyboard-avoidance-mode-to-offset), and [Example 6: Switching Avoidance Modes](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-6-switching-avoidance-modes).

// EntryAbility.ets
import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        uiContext.setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
      });
    }
}

#### getKeyboardAvoidMode11+

getKeyboardAvoidMode(): KeyboardAvoidMode

Obtains the avoidance mode for the virtual keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyboardAvoidMode](../enums/document.md#keyboardavoidmode11) | Avoidance mode for the virtual keyboard. |

**Example**

See [Example 4: Setting the Keyboard Avoidance Mode to Resize](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-4-setting-the-keyboard-avoidance-mode-to-resize), [Example 5: Setting Keyboard Avoidance Mode to Offset](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-5-setting-keyboard-avoidance-mode-to-offset), and [Example 6: Switching Avoidance Modes](../../../../arkts-components/universal-attributes/layout-and-borders/safe-area/document.md#example-6-switching-avoidance-modes).

// EntryAbility.ets
import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        let KeyboardAvoidMode = uiContext.getKeyboardAvoidMode();
        console.info("KeyboardAvoidMode:", JSON.stringify(KeyboardAvoidMode));
      });
    }
}

#### getAtomicServiceBar11+

getAtomicServiceBar(): Nullable<AtomicServiceBar>

Obtains an **AtomicServiceBar** object, which can be used to set the properties of the atomic service menu bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| Nullable<[AtomicServiceBar](../interface-atomicservicebar/document.md)\> | Returns the **AtomicServerBar** type if the service is an atomic service; returns **undefined** type otherwise. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    console.info('Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        console.info('Get AtomServiceBar Successfully.');
      } else {
        console.error('Get AtomicServiceBar failed.');
      }
    });
  }
}

#### getDragController11+

getDragController(): DragController

Obtains the **DragController** object, which can be used to create and initiate dragging.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [DragController](../class-dragcontroller/document.md) | **DragController** object. |

**Example**

See the example for [DragController](../class-dragcontroller/document.md).

#### keyframeAnimateTo11+

keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void

Generates a key frame animation. For details about how to use this API, see [keyframeAnimateTo](../../../../arkts-components/animation/keyframe-animation-keyframeanimateto/document.md).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | [KeyframeAnimateParam](../../../../arkts-components/animation/keyframe-animation-keyframeanimateto/document.md#keyframeanimateparam) | Yes | Overall animation parameter of the keyframe animation. |
| keyframes | Array<[KeyframeState](../../../../arkts-components/animation/keyframe-animation-keyframeanimateto/document.md#keyframestate)\> | Yes | List of all keyframe states. |

**Example**

// xxx.ets
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct KeyframeDemo {
  @State myScale: number = 1.0;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
  }

  build() {
    Column() {
      Circle()
        .width(100)
        .height(100)
        .fill("#46B1E3")
        .margin(100)
        .scale({ x: this.myScale, y: this.myScale })
        .onClick(() => {
          if (!this.uiContext) {
            console.error("no uiContext, keyframe failed");
            return;
          }
          this.myScale = 1;
          // Configure the keyframe animation to play three times.
          this.uiContext.keyframeAnimateTo({
              iterations: 3,
              expectedFrameRateRange: {
                min: 10,
                max: 120,
                expected: 60,
              }
            }, \[
            {
              // The first keyframe animation lasts for 800 ms, during which the scale attribute changes from 1 to 1.5.
              duration: 800,
              event: () => {
                this.myScale = 1.5;
              }
            },
            {
              // The second keyframe animation lasts for 500 ms, during which the scale attribute changes from 1.5 to 1.
              duration: 500,
              event: () => {
                this.myScale = 1;
              }
            }
          \]);
        })
    }.width('100%').margin({ top: 5 })
  }
}

#### getFocusController12+

getFocusController(): FocusController

Obtains a [FocusController](../class-focuscontroller/document.md) object, which can be used to control the focus.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [FocusController](../class-focuscontroller/document.md) | **FocusController** object. |

**Example**

See the example for [FocusController](../class-focuscontroller/document.md).

#### getFilteredInspectorTree12+

getFilteredInspectorTree(filters?: Array<string>): string

Obtains the component tree and component attributes. This API has a long processing time and is intended for testing scenarios only.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filters | Array<string> | No | 
List of component attributes used for filtering. Currently, only the following filter fields are supported:

**"id"**: unique ID of the component.

**"src"**: source of the resource.

**"content"**: information or data contained in the element, component, or object.

**"editable"**: whether the component is editable.

**"scrollable"**: whether the component is scrollable.

**"selectable"**: whether the component is selectable.

**"focusable"**: whether the component is focusable.

**"focused"**: whether the component is currently focused.

If **filters** includes one or more fields, unspecified fields will be filtered out from the results. If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out.

The following filter field is supported since API version 20:

**"isLayoutInspector"**: whether the component tree contains [custom components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components). If **filters** is omitted or does not contain **"isLayoutInspector"**, the returned component tree will not include custom component details.

Other filter fields are used only in testing scenarios.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | JSON string of the component tree and component attributes. For details about each field in the component, see the return value description of [getInspectorInfo](../../arkui/framenode/document.md#getinspectorinfo12). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |

**Example**

uiContext.getFilteredInspectorTree(\['id', 'src', 'content'\]);

// xxx.ets
import { UIContext } from '@kit.ArkUI';
@Entry
@Component
struct ComponentPage {
  loopConsole(inspectorStr: string, i: string) {
    console.info(\`InsTree ${i}| type: ${JSON.parse(inspectorStr).$type}, ID: ${JSON.parse(inspectorStr).$ID}\`);
    if (JSON.parse(inspectorStr).$children) {
      i += '-';
      for (let index = 0; index < JSON.parse(inspectorStr).$children.length; index++) {
        this.loopConsole(JSON.stringify(JSON.parse(inspectorStr).$children\[index\]), i);
      }
    }
  }

  build() {
    Column() {
      Button('content').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        let inspectorStr = uiContext.getFilteredInspectorTree(\['content'\]);
        console.info(\`InsTree : ${inspectorStr}\`);
        inspectorStr = JSON.stringify(JSON.parse(inspectorStr));
        this.loopConsole(inspectorStr, '-');
      })
      Button('isLayoutInspector').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        let inspectorStr = uiContext.getFilteredInspectorTree(\['isLayoutInspector'\]);
        console.info(\`InsTree : ${inspectorStr}\`);
        inspectorStr = JSON.stringify(JSON.parse(inspectorStr).content);
        this.loopConsole(inspectorStr, '-');
      })
    }
    .width('100%')
    .height('100%')
  }
}

When the **"content"** filter field is passed, the returned JSON string has the following structure:

InsTree : {"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":\[{"$type":"Column","$ID":15,"type":"build-in","$rect":"\[0.00, 72.00\],\[720.00,1208.00\]","$debugLine":"","$attrs":{},"$children":\[{"$type":"Button","$ID":16,"type":"build-in","$rect":"\[293.00, 72.00\],\[427.00,132.00\]","$debugLine":"","$attrs":{}},{"$type":"Button","$ID":18,"type":"build-in","$rect":"\[237.00, 132.00\],\[484.00,192.00\]","$debugLine":"","$attrs":{}}\]}\]}\\
InsTree -| type: root, ID: undefined
InsTree --| type: Column, ID: 15
InsTree ---| type: Button, ID: 16
InsTree ---| type: Button, ID: 18

Since API version 20, when the **"isLayoutInspector"** filter field is passed, the returned JSON string structure includes an outer layer with **"type"** and **"content"** fields, where **"content"** contains the original JSON structure (as returned without this field), and the return value structure includes custom components. This JSON string structure is as follows:

InsTree : {"type":"root","content":{"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":\[{"$type":"JsView","$ID":13,"type":"custom","state":{"observedPropertiesInfo":\[\],"viewInfo":{"componentName":"ComponentPage","id":14,"isV2":false,"isViewActive\_":true}},"$rect":"\[0.00, 72.00\],\[720.00,1208.00\]","$debugLine":"{\\"$line\\":\\"(0:0)\\"}","viewTag":"ComponentPage","$attrs":{"viewKey":"13"},"$children":\[{"$type":"Column","$ID":15, "type":"build-in","$rect":"\[0.00, 72.00\],\[720.00,1208.00\]","$debugLine":"","$attrs":{ ...
InsTree -| type: root, ID: undefined
InsTree --| type: JsView, ID: 13
InsTree ---| type: Column, ID: 15
InsTree ----| type: Button, ID: 16
InsTree ----| type: Button, ID: 18

#### getFilteredInspectorTreeById12+

getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string

Obtains the attributes of the specified component and its child components. This API has a long processing time and is intended for testing scenarios only.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [ID](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target component. |
| depth | number | Yes | Number of layers of child components. If the value is **0**, the attributes of the specified component and all its child components are obtained. If the value is **1**, only the attributes of the specified component are obtained. If the value is **2**, the attributes of the specified component and its level-1 child components are obtained. The rest can be deduced by analogy. |
| filters | Array<string> | No | 
List of component attributes used for filtering. Currently, only the following filter fields are supported:

**"id"**: unique ID of the component.

**"src"**: source of the resource.

**"content"**: information or data contained in the element, component, or object.

**"editable"**: whether the component is editable.

**"scrollable"**: whether the component is scrollable.

**"selectable"**: whether the component is selectable.

**"focusable"**: whether the component is focusable.

**"focused"**: whether the component is currently focused.

If **filters** includes one or more fields, unspecified fields will be filtered out from the results. If **filters** is not provided or is an empty array, none of the aforementioned fields will be filtered out.

Other filter fields are used only in testing scenarios.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | JSON string of the attributes of the specified component and its child components. For details about each field in the component, see the return value description of [getInspectorInfo](../../arkui/framenode/document.md#getinspectorinfo12). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |

**Example**

uiContext.getFilteredInspectorTreeById('testId', 0, \['id', 'src', 'content'\]);

import { UIContext } from '@kit.ArkUI';
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Text("Hello World")
        .fontSize(20)
        .id("TEXT")
      Button('getFilteredInspectorTreeById').onClick(() => {
        const uiContext: UIContext = this.getUIContext();
        try {
          let inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, \["id", "src"\]);
          console.info(\`result1: ${inspectorStr}\`);
          inspectorStr = JSON.stringify(JSON.parse(inspectorStr)\['$children'\]\[0\]);
          console.info(\`result2: ${inspectorStr}\`);
          inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, \["src"\]);
          inspectorStr = JSON.stringify(JSON.parse(inspectorStr)\['$children'\]\[0\]);
          console.info(\`result3: ${inspectorStr}\`);
        } catch(e) {
          console.error(\`getFilteredInspectorTreeById error: ${e}\`);
        }
      })
    }
    .width('100%')
    .height('100%')
  }
}

This JSON string structure is as follows:

result1: {"$type":"root","width":"1260.000000","height":"2720.000000","$resolution":"3.250000","$children":\[{"$type":"Text","$ID":6,"type":"build-in","$rect":"\[457.00, 123.00\],\[804.00,199.00\]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}\]}
result2: {"$type":"Text","$ID":6,"type":"build-in","$rect":"\[457.00, 123.00\],\[804.00,199.00\]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}
result3: {"$type":"Text","$ID":6,"type":"build-in","$rect":"\[457.00, 123.00\],\[804.00,199.00\]","$debugLine":"","$attrs":{"isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}

To obtain the component specified by the **id** parameter in the **getFilteredInspectorTreeById** API, you must first convert the API's result into a JSON object (as demonstrated in the sample code), and then extract the first item from the **$children** array. A comparison between **result2** and **result3** reveals that, if the **filters** parameter is changed from **\["id", "src"\]** to **\["src"\]**, the **$attrs** property obtained does not contain the **id** key.

#### getCursorController12+

getCursorController(): CursorController

Obtains a [CursorController](../class-cursorcontroller/document.md) object, which can be used to control the cursor.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [CursorController](../class-cursorcontroller/document.md) | **CursorController** object. |

**Example**

See the example for [CursorController](../class-cursorcontroller/document.md).

#### getContextMenuController12+

getContextMenuController(): ContextMenuController

Obtains a [ContextMenuController](../class-contextmenucontroller/document.md) object, which can be used to control menus.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ContextMenuController](../class-contextmenucontroller/document.md) | **ContextMenuController** object. |

#### getMeasureUtils12+

getMeasureUtils(): MeasureUtils

Obtains a **MeasureUtils** object for text calculation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [MeasureUtils](../class-measureutils/document.md) | Text metrics, such as text height and width. |

**Example**

See the example for [MeasureUtils](../class-measureutils/document.md).

#### getComponentSnapshot12+

getComponentSnapshot(): ComponentSnapshot

Obtains a **ComponentSnapshot** object, which can be used to obtain a component snapshot.

For typical use cases (for example, long screenshots) and best practices of component snapshots, see [Using Component Snapshot (ComponentSnapshot)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-uicontext-component-snapshot).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ComponentSnapshot](../class-componentsnapshot/document.md) | **ComponentSnapshot** object. |

**Example**

See the example for [ComponentSnapshot](../class-componentsnapshot/document.md).

#### vp2px12+

vp2px(value : number) : number

Converts a value in units of vp to a value in units of px.

Conversion formula: px value = vp value × pixel density

Pixel density: effective pixel density of the current window, which is the virtual screen density [VirtualScreenConfig](../../../display-management/ohos-display-display/document.md#virtualscreenconfig16).density.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/RsstpBALTzapIlXw7mGOhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41B89DF57612B181EE04C1C3FF7A751527A2CC5C2F7E9678F446E5AC4E81E97A)

1.  **getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.
    
2.  When a UI instance has not been created yet, the **vp2px** API in [Pixel Units](../../../../arkts-components/common-definitions/pixel-units/document.md) uses the default screen's virtual pixel ratio for conversion. In such scenarios, if you need to replace this API with a UIContext-based one, refer to [Replacing Pixel Unit Conversion APIs with UIContext APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#replacing-pixel-unit-conversion-apis-with-uicontext-apis).
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().vp2px(50),
          centerY: this.getUIContext().vp2px(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### px2vp12+

px2vp(value : number) : number

Converts a value in units of px to a value in units of vp.

Conversion formula: vp value = px value/pixel density

Pixel density: effective pixel density of the current window, which is the virtual screen density [VirtualScreenConfig](../../../display-management/ohos-display-display/document.md#virtualscreenconfig16).density.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/gNUC4HD6QeCCLtPLzYe-IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B5110A78ACE0DF29C8976F7BA75D1C73190F42A5FFDE7E438134C18E94D7B54)

1.  **getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.
    
2.  When a UI instance has not been created yet, the **px2vp** API in [Pixel Units](../../../../arkts-components/common-definitions/pixel-units/document.md) uses the default screen's virtual pixel ratio for conversion. In such scenarios, if you need to replace this API with a UIContext-based one, refer to [Replacing Pixel Unit Conversion APIs with UIContext APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#replacing-pixel-unit-conversion-apis-with-uicontext-apis).
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2vp(50),
          centerY: this.getUIContext().px2vp(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### fp2px12+

fp2px(value : number) : number

Converts a value in units of fp to a value in units of px.

Conversion formula: px value = fp value × pixel density × font scale factor

Pixel density: effective pixel density of the current window, which is the virtual screen density [VirtualScreenConfig](../../../display-management/ohos-display-display/document.md#virtualscreenconfig16).density.

Font scale factor: system font scaling coefficient ([Configuration.fontScale](../../../../arkts-components/common-definitions/basic-types/document.md#configuration)).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/3SY0xABrSqeG9oNhzyKd9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AC2565E48B21E5599DC8CD191007AC7BD14D646F84762961B85D152678F3F6F)

**getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().fp2px(50),
          centerY: this.getUIContext().fp2px(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### px2fp12+

px2fp(value : number) : number

Converts a value in units of px to a value in units of fp.

Conversion formula: fp value = px value/pixel density/font scale factor

Pixel density: effective pixel density of the current window, which is the virtual screen density [VirtualScreenConfig](../../../display-management/ohos-display-display/document.md#virtualscreenconfig16).density.

Font scale factor: system font scaling coefficient ([Configuration.fontScale](../../../../arkts-components/common-definitions/basic-types/document.md#configuration)).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/P5K2lIusTGeRp2uzvIi6bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42B88B0CC0C65A5C5700BA7EDE1618401C77CCF618C70F7B7536A2409CDECB4E)

**getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2fp(50),
          centerY: this.getUIContext().px2fp(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### lpx2px12+

lpx2px(value : number) : number

Converts a value in units of lpx to a value in units of px.

Conversion formula: px value = lpx value × (actual screen width/logical width), where the logical width is configured using [designWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#pages)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/5BUcAnD-S1K_0FQeLC5h6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6BCE41618DC756D6EAB6DD4C444B1E6F8588B5DB0DAB95BCC0E5FFC118AA529B)

**getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().lpx2px(50),
          centerY: this.getUIContext().lpx2px(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### px2lpx12+

px2lpx(value : number) : number

Converts a value in units of px to a value in units of lpx.

Conversion formula: lpx value = px value/(actual screen width/logical width), where the logical width is configured using [designWidth](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#pages)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/JcyG71lLRaqGI2O56DE6hQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B59E591469792A1088EFA9C02A4A2E5120C21E78DBEA8F448111BE1EEB83367)

**getUIContext** must be called after windowStage.[loadContent](../../../window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9) to ensure the UIContext is initialized before this API is called. Otherwise, accurate results cannot be guaranteed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Value to convert.

Value range: (-∞, +∞)

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Value after conversion.

Value range: (-∞, +∞)

 |

**Example**

@Entry
@Component
struct MatrixExample {
  build() {
    Column({ space: 100 }) {
      Text('Hello1')
        .textAlign(TextAlign.Center)
        .width(100)
        .height(60)
        .backgroundColor(0xAFEEEE)
        .borderWidth(1)
        .rotate({
          z: 1,
          angle: 90,
          centerX: this.getUIContext().px2lpx(50),
          centerY: this.getUIContext().px2lpx(30)
        })
    }.width('100%')
    .height('100%')
  }
}

#### getWindowName12+

getWindowName(): string | undefined

Obtains the name of the window where this instance is located.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | undefined | Name of the window where the current instance is located. If the window does not exist, **undefined** is returned. |

**Example**

import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  aboutToAppear() {
    const windowName = this.getUIContext().getWindowName();
    console.info('WindowName ' + windowName);
    const currWindow = window.findWindow(windowName);
    const windowProperties = currWindow.getWindowProperties();
    console.info(\`Window width ${windowProperties.windowRect.width}, height ${windowProperties.windowRect.height}\`);
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### getWindowWidthBreakpoint13+

getWindowWidthBreakpoint(): WidthBreakpoint

Obtains the width breakpoint value of the window where this instance is located. The specific value is determined by the vp value of the window width. For details, see [WidthBreakpoint](../../../../arkts-components/common-definitions/enums/document.md#widthbreakpoint13).

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [WidthBreakpoint](../../../../arkts-components/common-definitions/enums/document.md#widthbreakpoint13) | Width breakpoint value of the window where the current instance is located. If the window width is 0 vp, **WIDTH\_XS** is returned. |

**Example**

import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text('test')
            .fontSize(30)
        }
        .onClick(() => {
          let uiContext: UIContext = this.getUIContext();
          let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
          console.info(\`Window widthBp: ${widthBp}\`);
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### getWindowHeightBreakpoint13+

getWindowHeightBreakpoint(): HeightBreakpoint

Obtains the height breakpoint value of the window where this instance is located. The specific value is determined based on the window aspect ratio. For details, see [HeightBreakpoint](../../../../arkts-components/common-definitions/enums/document.md#heightbreakpoint13).

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [HeightBreakpoint](../../../../arkts-components/common-definitions/enums/document.md#heightbreakpoint13) | Height breakpoint value of the window where the current instance is located. If the window aspect ratio is 0, **HEIGHT\_SM** is returned. |

**Example**

import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text('test')
            .fontSize(30)
        }
        .onClick(() => {
          let uiContext: UIContext = this.getUIContext();
          let heightBp: HeightBreakpoint = uiContext.getWindowHeightBreakpoint();
          let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
          console.info(\`Window heightBP: ${heightBp}, widthBp: ${widthBp}\`);
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### postFrameCallback12+

postFrameCallback(frameCallback: FrameCallback): void

Registers a callback that is executed when the next frame is rendered.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| frameCallback | [FrameCallback](../class-framecallback/document.md) | Yes | Callback to be executed for the next frame. |

**Example**

import {FrameCallback } from '@kit.ArkUI';

class MyFrameCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('Invoke postFrameCallback')
        .onClick(() => {
          this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
        })
    }
  }
}

#### postDelayedFrameCallback12+

postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void

Registers a callback to be executed on the next frame after a delay.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| frameCallback | [FrameCallback](../class-framecallback/document.md) | Yes | Callback to be executed for the next frame. |
| delayTime | number | Yes | Delay time, in milliseconds. If a **null**, **undefined**, or value less than 0 is passed in, it will be treated as **0**. |

**Example**

import {FrameCallback } from '@kit.ArkUI';

class MyFrameCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onFrame(frameTimeNanos: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('Invoke postDelayedFrameCallback')
        .onClick(() => {
          this.getUIContext().postDelayedFrameCallback(new MyFrameCallback("delayTask"), 5);
        })
    }
  }
}

#### requireDynamicSyncScene12+

requireDynamicSyncScene(id: string): Array<DynamicSyncScene>

Requests the dynamic sync scene of a component for customizing related frame rate configuration.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | [Component ID](../../../../arkts-components/universal-attributes/basic-attributes/component-id/document.md) of the target node. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<DynamicSyncScene> | **DynamicSyncScene** object array. |

**Example**

import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
  private scenes: SwiperDynamicSyncScene\[\] = \[\];

  build() {
    Column() {
      Text("Animation "+ JSON.stringify(this.ANIMATION))
      Text("Gesture "+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(()=>{
          this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene\[\];
        })
      }

      Button("set frame")
        .onClick(() => {
          this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

            if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
              scenes.setFrameRateRange(this.ANIMATION);
            }

            if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
              scenes.setFrameRateRange(this.GESTURE);
            }
          });
        })
    }
  }
}

#### openBindSheet12+

openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>

Creates a sheet whose content is as defined in **bindSheetContent** and displays the sheet. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/R8sX7HV7TVuKwls2N8C__w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A462517D3A8F5B8D4A03F9FB494229CFD2B55F1235BFEB1AB480EA6C6177F56)

1.  When calling this API, if no valid value is provided for **targetId**, you won't be able to set **SheetOptions.preferType** to **POPUP** or **SheetOptions.mode** to **EMBEDDED**.
    
2.  Since [updateBindSheet](#updatebindsheet12) and [closeBindSheet](#closebindsheet12) depend on **bindSheetContent**, you need to maintain the passed **bindSheetContent** yourself.
    
3.  Setting **SheetOptions.UIContext** is not supported.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bindSheetContent | [ComponentContent<T>](../../arkui/componentcontent/document.md) | Yes | Content to display on the sheet. |
| sheetOptions | [SheetOptions](../../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#sheetoptions) | No | 
Style of the sheet.

**NOTE**

1\. **SheetOptions.uiContext** cannot be set. Its value is fixed to the **UIContext** object of the current instance.

2\. If **targetId** is not passed in, **SheetOptions.preferType** cannot be set to **POPUP**; if **POPUP** is set, it will be replaced with **CENTER**.

3\. If **targetId** is not passed in, **SheetOptions.mode** cannot be set to **EMBEDDED**; the default mode is **OVERLAY**.

4\. For the default values of other attributes, see [SheetOptions](../../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#sheetoptions).

 |
| targetId | number | No | ID of the component to be bound. If this parameter is not set, no component is bound. If the ID does not exist, the error code 120004 is returned. Returns error code 401 if **undefined** is passed in. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Sheet Error Codes](../../../../error-codes/ui/sheet-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120002 | The bindSheetContent already exists. |
| 120004 | The targetId does not exist. |
| 120005 | The node of targetId is not in the component tree. |
| 120006 | The node of targetId is not a child of the page node or NavDestination node. |

**Example**

import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })
      })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
      })
  }
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}

#### updateBindSheet12+

updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean ): Promise<void>

Updates the style of the sheet corresponding to the provided **bindSheetContent**. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/dRy1eKriTSCmR5x60Cjx3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EBEB73C61F3DA17098DD90C61C615729AA19B31BA4F9C74839F1DDE6ACB7746)

**SheetOptions.UIContext**, **SheetOptions.mode**, and callback functions cannot be updated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bindSheetContent | [ComponentContent<T>](../../arkui/componentcontent/document.md) | Yes | Content to display on the sheet. |
| sheetOptions | [SheetOptions](../../../../arkts-components/universal-attributes/transition/sheet-transition/document.md#sheetoptions) | Yes | 
Style of the sheet.

**NOTE**

**SheetOptions.UIContext** and **SheetOptions.mode** cannot be updated.

 |
| partialUpdate | boolean | No | 

Whether to update the sheet in incremental mode.

Default value: **false**

**NOTE**

1\. **true**: incremental update, where the specified properties in **SheetOptions** are updated, and other properties stay at their current value.

2\. **false**: full update, where all properties except those specified in **SheetOptions** are restored to default values.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Sheet Error Codes](../../../../error-codes/ui/sheet-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120003 | The bindSheetContent cannot be found. |

**Example**

import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })
      })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
      })
  }
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}

#### closeBindSheet12+

closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>

Closes the sheet corresponding to **bindSheetContent**. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/OSH2J9OdSeSfsGkN9ZTZMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DDF90B68382A6EF3C98D2D5C10C78D542FA047E65AC82C031F292755218CA80)

Closing a sheet using this API will not invoke the **shouldDismiss** callback.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bindSheetContent | [ComponentContent<T>](../../arkui/componentcontent/document.md) | Yes | Content to display on the sheet. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [Sheet Error Codes](../../../../error-codes/ui/sheet-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120003 | The bindSheetContent cannot be found. |

**Example**

import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";

  constructor(text: string) {
    this.text = text;
  }
}

let contentNode: ComponentContent<Params>;
let gUIContext: UIContext;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
    Button('Update BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.updateBindSheet(contentNode, {
          backgroundColor: Color.Pink,
        }, true)
          .then(() => {
            console.info('updateBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
          })
      })

    Button('Close BindSheet')
      .fontSize(20)
      .onClick(() => {
        gUIContext.closeBindSheet(contentNode)
          .then(() => {
            console.info('closeBindSheet success');
          })
          .catch((err: BusinessError) => {
            console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
          })
      })
  }
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';

  aboutToAppear() {
    gUIContext = this.getUIContext();
    contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            let uiContext = this.getUIContext();
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: Color.Green,
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error: ' + err.code + ' ' + err.message);
              })
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}

#### isFollowingSystemFontScale13+

isFollowingSystemFontScale(): boolean

Checks whether this UI context follows the system font scale settings.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the current UI context follows the system font scale settings.

**true**: The current UI context follows the system font scale settings.

**false**: The current UI context does not follow the system font scale settings.

 |

**Example**

Refer to the [configuration tag](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#configuration) and set the value of **fontSizeScale** to **"followSystem"**.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('isFollowingSystemFontScale').onClick(() => {
        console.info('isFollowingSystemFontScale', this.getUIContext().isFollowingSystemFontScale());
      });
    }
  }
}

#### getMaxFontScale13+

getMaxFontScale(): number

Obtains the maximum font scale of this UI context.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum font scale of the current UI context. |

**Example**

Refer to the [configuration tag](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#configuration) and set the value of **fontSizeMaxScale** to **"1.75"**.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('getMaxFontScale').onClick(() => {
        console.info('getMaxFontScale', this.getUIContext().getMaxFontScale().toFixed(2));
      });
    }
  }
}

#### bindTabsToScrollable13+

bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void

Binds a **Tabs** component with a scrollable container, which can be a [List](../../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../../arkts-components/scroll-and-swipe/scroll/document.md), [Grid](../../../../arkts-components/scroll-and-swipe/grid/document.md), or [WaterFlow](../../../../arkts-components/scroll-and-swipe/waterflow/document.md) component. This way, scrolling the scrollable container triggers the display and hide animations of the tab bar for all **Tabs** components that are bound to it – scrolling up triggers the hide animation, and scrolling down triggers the show animation. A **TabsController** instance can be bound with multiple **Scroller** instances, and conversely, a **Scroller** instance can be bound with multiple **TabsController** instances.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/U_8ZegRwRme2fewHUdDAVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBEDC6C3F43D920A62E1719C773D0D03656A1F50F0B4CC4FA59364260AC1B38C)

When multiple scrollable containers are bound to the same **Tabs** component, scrolling any of the bound containers will trigger the appearance and disappearance animations of the tab bar. In addition, when any scrollable container reaches the bottom, the tab bar immediately triggers the appearance animation. Therefore, avoid scrolling multiple scrollable containers simultaneously whenever possible.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tabsController | [TabsController](../../../../arkts-components/navigation-and-switching/tabs/document.md#tabscontroller) | Yes | Controller of the target **Tabs** component. |
| scroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target scrollable container. |

**Example**

@Entry
@Component
struct TabsExample {
  private arr: string\[\] = \[\];
  private parentTabsController: TabsController = new TabsController();
  private childTabsController: TabsController = new TabsController();
  private listScroller: Scroller = new Scroller();
  private parentScroller: Scroller = new Scroller();
  private childScroller: Scroller = new Scroller();

  aboutToAppear(): void {
    for (let i = 0; i < 20; i++) {
      this.arr.push(i.toString());
    }
    let context = this.getUIContext();
    context.bindTabsToScrollable(this.parentTabsController, this.listScroller);
    context.bindTabsToScrollable(this.childTabsController, this.listScroller);
    context.bindTabsToNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
  }

  aboutToDisappear(): void {
    let context = this.getUIContext();
    context.unbindTabsFromScrollable(this.parentTabsController, this.listScroller);
    context.unbindTabsFromScrollable(this.childTabsController, this.listScroller);
    context.unbindTabsFromNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
  }

  build() {
    Tabs({ barPosition: BarPosition.End, controller: this.parentTabsController }) {
      TabContent() {
        Tabs({ controller: this.childTabsController }) {
          TabContent() {
            List({ space: 20, initialIndex: 0, scroller: this.listScroller }) {
              ForEach(this.arr, (item: string) => {
                ListItem() {
                  Text(item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Gray)
                }
              }, (item: string) => item)
            }
            .scrollBar(BarState.Off)
            .width('90%')
            .height('100%')
            .contentStartOffset(56)
            .contentEndOffset(52)
          }.tabBar(SubTabBarStyle.of('Top tab'))
        }
        .width('100%')
        .height('100%')
        .barOverlap (true) // Make the tab bar overlap the TabContent component. This means that when the tab bar is hidden upwards or downwards, the area it occupies will not appear empty.
        .clip (true) // Clip any child components that extend beyond the Tabs component's boundaries, preventing accidental touches on the tab bar when it is hidden.
      }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'Scroller linked with TabsControllers'))

      TabContent() {
        Scroll(this.parentScroller) {
            List({ space: 20, initialIndex: 0, scroller: this.childScroller }) {
              ForEach(this.arr, (item: string) => {
                ListItem() {
                  Text(item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(Color.Gray)
                }
              }, (item: string) => item)
            }
            .scrollBar(BarState.Off)
            .width('90%')
            .height('100%')
            .contentEndOffset(52)
            .nestedScroll({ scrollForward: NestedScrollMode.SELF\_FIRST, scrollBackward: NestedScrollMode.SELF\_FIRST })
        }
        .width('100%')
        .height('100%')
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Vertical)
        .edgeEffect(EdgeEffect.Spring)
      }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'Nested Scroller linked with TabsController'))
    }
    .width('100%')
    .height('100%')
    .barOverlap (true) // Make the tab bar overlap the TabContent component. This means that when the tab bar is hidden upwards or downwards, the area it occupies will not appear empty.
    .clip (true) // Clip any child components that extend beyond the Tabs component's boundaries, preventing accidental touches on the tab bar when it is hidden.
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/VBELyHwKQjud_1suPbmOlA/en-us_image_0000002568685045.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B27338F0813AF5B6681C9124736CD9040FE9608D74A7AB0E8E4CF0B8AC80A06)

#### unbindTabsFromScrollable13+

unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void

Unbinds a **Tabs** component from a scrollable container.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tabsController | [TabsController](../../../../arkts-components/navigation-and-switching/tabs/document.md#tabscontroller) | Yes | Controller of the target **Tabs** component. |
| scroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target scrollable container. |

**Example**

See the example for [bindTabsToScrollable](#bindtabstoscrollable13).

#### bindTabsToNestedScrollable13+

bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

Binds a **Tabs** component with a nested scrollable container, which can be a [List](../../../../arkts-components/scroll-and-swipe/list/document.md), [Scroll](../../../../arkts-components/scroll-and-swipe/scroll/document.md), [Grid](../../../../arkts-components/scroll-and-swipe/grid/document.md), or [WaterFlow](../../../../arkts-components/scroll-and-swipe/waterflow/document.md) component. This way, scrolling the parent or child component triggers the display and hide animations of the tab bar for all **Tabs** components that are bound to it – scrolling up triggers the hide animation, and scrolling down triggers the show animation. A **TabsController** instance can be bound with multiple nested **Scroller** instances, and conversely, a nested **Scroller** instance can be bound with multiple **TabsController** instances.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tabsController | [TabsController](../../../../arkts-components/navigation-and-switching/tabs/document.md#tabscontroller) | Yes | Controller of the target **Tabs** component. |
| parentScroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target parent scrollable container. |
| childScroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target child scrollable container, which is a nested child component of the component corresponding to **parentScroller**. |

**Example**

See the example for [bindTabsToScrollable](#bindtabstoscrollable13).

#### unbindTabsFromNestedScrollable13+

unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

Unbinds a **Tabs** component from a nested scrollable container.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| tabsController | [TabsController](../../../../arkts-components/navigation-and-switching/tabs/document.md#tabscontroller) | Yes | Controller of the target **Tabs** component. |
| parentScroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target parent scrollable container. |
| childScroller | [Scroller](../../../../arkts-components/scroll-and-swipe/scroll/document.md#scroller) | Yes | Controller of the target child scrollable container, which is a nested child component of the component corresponding to **parentScroller**. |

**Example**

See the example for [bindTabsToScrollable](#bindtabstoscrollable13).

#### enableSwipeBack18+

enableSwipeBack(enabled: Optional<boolean>): void

Sets whether to enable the horizontal swipe-to-go-back gesture within the application.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Circle

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | Optional<boolean> | Yes | 
Whether to enable the horizontal swipe-to-go-back gesture.

Default value: **true**.

**true**: The horizontal swipe-to-go-back gesture is enabled.

**false**: The horizontal swipe-to-go-back gesture is disabled.

 |

**Example**

@Entry
@Component
struct Index {
  @State isEnable: boolean = true;

  build() {
    RelativeContainer() {
      Button(\`enable swipe back: ${this.isEnable}\`).onClick(() => {
        this.isEnable = !this.isEnable;
        this.getUIContext().enableSwipeBack(this.isEnable);
      })
    }
    .height('100%')
    .width('100%')
  }
}

#### getTextMenuController16+

getTextMenuController(): TextMenuController

Obtains a [TextMenuController](../class-textmenucontroller/document.md) object, which can be used to control the context menu on selection.

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [TextMenuController](../class-textmenucontroller/document.md) | Obtained **TextMenuController** object. |

**Example**

See the example for [TextMenuController](../class-textmenucontroller/document.md).

#### createUIContextWithoutWindow17+

static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext) : UIContext | undefined

Creates a UI instance that does not depend on a window and returns its UI context. The created UI instance is a singleton.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/kfxXFisgTjemOsqPdfVs-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AA63D23C653ED60CDFC5C99F35AE73487C1925CB9A589D527683B1749A46AB2)

The returned UI context can only be used to create [custom nodes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-node). It cannot be used for other UI operations.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | common.[UIAbilityContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | common.[ExtensionContext](../../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md) | Yes | Context corresponding to [UIAbility](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) or [ExtensionAbility](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| UIContext | undefined | Context of the created UI instance, or **undefined** if creation fails. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [API Call Error Codes](../../../../error-codes/ui/api-call-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. The number of parameters is incorrect.

2\. Invalid parameter type of context.

 |
| 100001 | Internal error. |

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let uiContext : UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
  }

  // ......
}

#### destroyUIContextWithoutWindow17+

static destroyUIContextWithoutWindow(): void

Destroys the UI instance created using [createUIContextWithoutWindow](#createuicontextwithoutwindow17).

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    let uiContext : UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
    UIContext.destroyUIContextWithoutWindow();
  }

  // ......
}

#### dispatchKeyEvent15+

dispatchKeyEvent(node: number | string, event: KeyEvent): boolean

Dispatches a key event to the specified component. To ensure predictable behavior, the target component must be within the subtree of the dispatching component.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| node | number | string | Yes | ID or unique ID of the target component. |
| event | [KeyEvent](../../../../arkts-components/universal-events/basic-input-events/key-event/document.md#keyevent) | Yes | **KeyEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the key event was successfully dispatched to the specified component.

The value **true** means the dispatch was successful, and **false** means the dispatch failed.

 |

**Example**

@Entry
@Component
struct Index {
  build() {
    Row() {
      Row() {
        Button('Button1').id('Button1').onKeyEvent((event) => {
          console.info("Button1");
          return true;
        })
        Button('Button2').id('Button2').onKeyEvent((event) => {
          console.info("Button2");
          return true;
        })
      }
      .width('100%')
      .height('100%')
      .id('Row1')
      .onKeyEventDispatch((event) => {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Button1');
        return context.dispatchKeyEvent('Button1', event);
      })

    }
    .height('100%')
    .width('100%')
    .onKeyEventDispatch((event) => {
      if (event.type == KeyType.Down) {
        let context = this.getUIContext();
        context.getFocusController().requestFocus('Row1');
        return context.dispatchKeyEvent('Row1', event);
      }
      return true;
    })
  }
}

#### setPixelRoundMode18+

setPixelRoundMode(mode: PixelRoundMode): void

Sets the pixel rounding mode for this page.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [PixelRoundMode](../../../../arkts-components/common-definitions/enums/document.md#pixelroundmode18) | Yes | 
Pixel rounding mode.

Default value: **PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH**.

 |

**Example**

// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
        uiContext.setPixelRoundMode(PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH);
      });
    }
}

#### getPixelRoundMode18+

getPixelRoundMode(): PixelRoundMode

Obtains the pixel rounding mode for this page.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelRoundMode](../../../../arkts-components/common-definitions/enums/document.md#pixelroundmode18) | Pixel rounding mode of the current page. |

**Example**

// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {

      windowStage.loadContent('pages/Index', (err, data) => {
        let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
        console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
      });
    }
}

#### setResourceManagerCacheMaxCountForHSP21+

static setResourceManagerCacheMaxCountForHSP(count: number): void

Sets the maximum number of cached HSP resource management objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/w0IMX0ZpQO-fScbkfx9mFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02C28A2D244B024BDA48FC1C278AE343AC73E597EEFC7AA7829B299E91201E8F)

If the upper limit of the cache is set too high, the memory overhead may be too large. You are advised to set it properly.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| count | number | Yes | Number of cached resources. The value is a non-negative integer. |

**Error codes**

For details about the error codes, see UI Context Error Codes.

| ID | Error Message |
| :-- | :-- |
| 100101 | The parameter is less than 0. |
| 100102 | The parameter value cannot be a floating point number. |
| 100103 | The function cannot be called from a non main thread. |

**Example**

// EntryAbility.ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { UIContext, window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
        return;
      }
      UIContext.setResourceManagerCacheMaxCountForHSP(5);
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
}

#### getMagnifier22+

getMagnifier(): Magnifier

Obtains a [Magnifier](../class-magnifier/document.md) object, which can be used to control the display and hiding of a magnifier.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [Magnifier](../class-magnifier/document.md) | **Magnifier** object, which can be used to control the display and hiding of a magnifier. |

**Example**

See the example of the [bind](../class-magnifier/document.md#bind) API in [Magnifier](../class-magnifier/document.md).
