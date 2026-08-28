# @ohos.accessibility (Accessibility)

The **Accessibility** module implements the accessibility features, including obtaining the accessibility application list, accessibility application enabling state, and captions configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/DVZLFhQOQ2CH5vHk2JbtTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1899FCC246ACA0BDAE9B9DA1EFCE6B8A0C801C79FE016D7B5DC11FED3057DA91)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { accessibility } from '@kit.AccessibilityKit';

#### AbilityState

type AbilityState = 'enable' | 'disable' | 'install'

Enumerates the states of an accessibility application.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'enable' | The accessibility application is enabled. |
| 'disable' | The accessibility application is disabled. |
| 'install' | The accessibility application has been installed. |

#### AbilityType

type AbilityType = 'audible' | 'generic' | 'haptic' | 'spoken' | 'visual' | 'all'

Enumerates the types of accessibility applications.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'audible' | The accessibility application provides audible feedback. |
| 'generic' | The accessibility application provides generic feedback. |
| 'haptic' | The accessibility application provides haptic feedback. |
| 'spoken' | The accessibility application provides spoken feedback. |
| 'visual' | The accessibility application provides visual feedback. |
| 'all'9+ | All the preceding types. |

#### AccessibilityAbilityInfo

Provides information about an accessibility application.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id | string | Yes | No | Ability ID. |
| name | string | Yes | No | Ability name. |
| bundleName | string | Yes | No | Bundle name. |
| targetBundleNames9+ | Array<string> | Yes | No | Name of the target bundle. |
| abilityTypes | Array<[AbilityType](#abilitytype)\> | Yes | No | Accessibility application type. |
| capabilities | Array<[Capability](#capability)\> | Yes | No | Capabilities list of the accessibility application. |
| description | string | Yes | No | Description of the accessibility application. |
| eventTypes | Array<[EventType](#eventtype)\> | Yes | No | List of events that the accessibility application focuses on. |
| needHide12+ | boolean | Yes | No | Whether the auxiliary application is hidden in the list of installed extended services. The value **true** means the auxiliary application is hidden, and the value **false** means the opposite. |
| label12+ | string | Yes | No | Name of the application in the extended service list. |

#### Action

type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |

'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |

'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |

'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common'

Target actions supported by the application. The target actions for which parameters need to be set have been specified in the description of the following table.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'click' | Click. |
| 'longClick' | Long press. |
| 'scrollForward' | Scroll forward. |
| 'scrollBackward' | Scroll backward. |
| 'focus' | Obtain a focus. |
| 'clearFocus' | Clear a focus. |
| 'clearSelection' | Clear selection. Not supported yet. |
| 'accessibilityFocus' | Obtain an accessibility focus. |
| 'clearAccessibilityFocus' | Clear an accessibility focus. |
| 'cut' | Cut. |
| 'copy' | Copy. |
| 'paste' | Paste. |
| 'select' | Select. |
| 'setText' | Set text. You need to set the **setText** parameter. |
| 'delete' | Delete. Not supported yet. |
| 'setSelection' | Select. You need to set the **selectTextBegin**, **selectTextEnd** and **selectTextInForWard** parameters. |
| 'common' | Common actions used in auto-focusing and auto-broadcasting. |
| 'home' | Return to the home screen. |
| 'back' | Return to the previous screen. |
| 'recentTask' | Open a recent task. |
| 'notificationCenter' | Open the notification bar. |
| 'controlCenter' | Open the control center. |
| 'setCursorPosition' | Set cursor location. You need to set the **offset** parameter. |

#### Capability

type Capability = 'retrieve' | 'touchGuide' | 'keyEventObserver' | 'zoom' | 'gesture'

Enumerates the capabilities of an accessibility application.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'retrieve' | Capability to retrieve the window content. |
| 'touchGuide' | Capability of touch guide mode. |
| 'keyEventObserver' | Capability to filter key events. |
| 'zoom' | Capability to control the display zoom level. Not supported currently. |
| 'gesture' | Capability to perform gesture actions. |

#### CaptionsFontEdgeType8+

type CaptionsFontEdgeType = 'none' | 'raised' | 'depressed' | 'uniform' | 'dropShadow'

Enumerates the font edge types of captions.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

| Type | Description |
| :-- | :-- |
| 'none' | No effect. |
| 'raised' | Raised effect. |
| 'depressed' | Depressed effect. |
| 'uniform' | Uniform effect. |
| 'dropShadow' | Drop shadow effect. |

#### CaptionsFontFamily8+

type CaptionsFontFamily = 'default' | 'monospacedSerif' | 'serif' | 'monospacedSansSerif' |

'sansSerif' | 'casual' | 'cursive' | 'smallCapitals'

Enumerates the font families of captions.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

| Type | Description |
| :-- | :-- |
| 'default' | Default font family. |
| 'monospacedSerif' | Monospaced Serif fonts, which use the same width for each character. |
| 'serif' | Serif fonts. |
| 'monospacedSansSerif' | Monospaced Sans Serif fonts, which use the same width for each character. |
| 'sansSerif' | Sans Serif fonts. |
| 'casual' | Casual fonts. |
| 'cursive' | Cursive fonts. |
| 'smallCapitals' | Small caps fonts. |

#### CaptionsStyle8+

Describes the style of captions.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontFamily | [CaptionsFontFamily](#captionsfontfamily8) | No | No | Font family of captions. |
| fontScale | number | No | No | Font scale factor of captions, in percentage. The value ranges from 1 to 200. |
| fontColor | number | string | No | No | 
Font color of captions.

**number**: HEX format, used to represent colors defined in either the RGB or ARGB color models.

**string**: #rrggbb, #rrggbbaa, #rgb, or #rgba format.

Example: opaque red; number: 0xffff0000; string: '#ff0000', '#ff0000ff', '#f00', or '#f00f'

 |
| fontEdgeType | [CaptionsFontEdgeType](#captionsfontedgetype8) | No | No | Font edge type of captions. |
| backgroundColor | number | string | No | No | 

Background color of captions.

**number**: HEX format, used to represent colors defined in either the RGB or ARGB color models.

**string**: #rrggbb, #rrggbbaa, #rgb, or #rgba format.

Example: opaque red; number: 0xffff0000; string: '#ff0000', '#ff0000ff', '#f00', or '#f00f'

 |
| windowColor | number | string | No | No | 

Window color of captions.

**number**: HEX format, used to represent colors defined in either the RGB or ARGB color models.

**string**: #rrggbb, #rrggbbaa, #rgb, or #rgba format.

Example: opaque red; number: 0xffff0000; string: '#ff0000', '#ff0000ff', '#f00', or '#f00f'

 |

#### CaptionsManager8+

Implements configuration management for captions. Before calling any API of **CaptionsManager**, you must use the [accessibility.getCaptionsManager()](#accessibilitygetcaptionsmanagerdeprecated) API to obtain a **CaptionsManager** instance.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enabled | boolean | No | No | Whether to enable captions configuration. The value **true** indicates that the caption configuration is enabled, and **false** indicates the opposite. |
| style | [CaptionsStyle](#captionsstyle8) | No | No | Style of captions. |

#### \[h2\]on('enableChange')(deprecated)

on(type: 'enableChange', callback: Callback<boolean>): void;

Subscribes to the state changes of captions configuration. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/UlwmHD1oSPGQPxf-lpEmoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F01E002734679E9FA63D25C466C291F029FA4BA5FFBD0A2328B2D38C68780457)

This API is supported since API version 8 and deprecated since API version 12. Related features are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'enableChange'** in this API. |
| callback | Callback<boolean> | Yes | Callback invoked when the enabled status of captions configuration changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(\`subscribe caption manager enable state change, result: ${JSON.stringify(data)}\`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### \[h2\]on('styleChange')(deprecated)

on(type: 'styleChange', callback: Callback<CaptionsStyle>): void;

Subscribes to captions style changes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/VkfMmkG3SSiZcKk3d9IyWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2517C8A915C6B4BE5ADD5DB6B898043C9A0106C59FFBAABAC62C88C3F884AE42)

This API is supported since API version 8 and deprecated since API version 12. Related features are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'styleChange'** in this API. |
| callback | Callback<[CaptionsStyle](#captionsstyle8)\> | Yes | Callback invoked when the style of captions changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(\`subscribe caption manager style state change, result: ${JSON.stringify(data)}\`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### \[h2\]off('enableChange')(deprecated)

off(type: 'enableChange', callback?: Callback<boolean>): void;

Unsubscribes from the state changes of captions configuration. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/04nmAJpaRRSF2kHQbr6geg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAFDF12156E70DB2140D075AF776A596388EFDEDCD5F6108700C878AE58E8BA6)

This API is supported since API version 8 and deprecated since API version 12. Related features are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'enableChange'** in this API. |
| callback | Callback<boolean> | No | Callback used to unregister. The value must be the same as the value of **callback** in **on('enableChange')**. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(\`subscribe caption manager enable state change, result: ${JSON.stringify(data)}\`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('enableChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('enableChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### \[h2\]off('styleChange')(deprecated)

off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void;

Unsubscribes from the captions style changes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/xCEU09GzTKGLJ5wirFXCNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D4960CF7506305BB8152C35D20243B509D1CF942903109FB21CD7E79E7A86F6)

This API is supported since API version 8 and deprecated since API version 12. Related features are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'styleChange'** in this API. |
| callback | Callback<[CaptionsStyle](#captionsstyle8)\> | No | Callback used to unregister. The value must be the same as the value of **callback** in **on('styleChange')**. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: accessibility.CaptionsStyle) => void = this.eventCallback;
  eventCallback(data: accessibility.CaptionsStyle): void {
    console.info(\`subscribe caption manager style state change, result: ${JSON.stringify(data)}\`);
  }

  aboutToAppear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.on('styleChange', this.callback);
  }

  aboutToDisappear(): void {
    let captionsManager = accessibility.getCaptionsManager();
    captionsManager.off('styleChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### EventInfo

Describes a GUI change event.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [EventType](#eventtype) | No | No | Accessibility event type (mandatory). |
| windowUpdateType | [WindowUpdateType](#windowupdatetype) | No | Yes | Window update type. |
| bundleName | string | No | No | Name of the target application (mandatory). |
| componentType | string | No | Yes | Component type, for example, **Button** for the button component and **Image** for the image component. |
| pageId | number | No | Yes | ID of the page where the event occurs. The default value is **0**. |
| description | string | No | Yes | Event description. Set this parameter as required. |
| triggerAction | [Action](#action) | No | No | Action that triggers the event (mandatory). |
| textMoveUnit | [TextMoveUnit](#textmoveunit) | No | Yes | Text move granularity. |
| contents | Array<string> | No | Yes | Content list. Set this parameter as required. |
| lastContent | string | No | Yes | Latest content. Set this parameter as required. |
| beginIndex | number | No | Yes | Start index. The default value is **0**. |
| currentIndex | number | No | Yes | Current index. The default value is **0**. |
| endIndex | number | No | Yes | End index. The default value is **0**. |
| itemCount | number | No | Yes | Total number of items. The default value is **0**. |
| elementId12+ | number | No | Yes | Element ID of the component. The default value is **0**. |
| textAnnouncedForAccessibility12+ | string | No | Yes | Content for auto-broadcasting. Set the broadcast content based on the actual scenario. No special restrictions. |
| textResourceAnnouncedForAccessibility18+ | Resource | No | Yes | Content for auto-broadcasting. The value is a string of the **Resource** type. |
| customId12+ | string | No | Yes | Component ID for auto-focusing. |

#### \[h2\]constructor

constructor(jsonObject: Object)

Implements a constructor.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| jsonObject | Object | Yes | JSON object that contains the **type**, **bundleName**, and **triggerAction** fields. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

#### \[h2\]constructor11+

constructor(type: EventType, bundleName: string, triggerAction: Action)

Implements a constructor.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [EventType](#eventtype) | Yes | Accessibility event types. |
| bundleName | string | Yes | Target application name. |
| triggerAction | [Action](#action) | Yes | Action that triggers the event. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

let eventInfo = new accessibility.EventInfo('click', 'com.example.MyApplication', 'click');

#### EventType

type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' |

'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' |

'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' |

'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' |

'announceForAccessibilityNotInterrupt' | 'scrolling'

Accessibility event types.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'accessibilityFocus' | Event indicating that the accessibility focus is obtained. |
| 'accessibilityFocusClear' | Event indicating that the accessibility focus is cleared. |
| 'click' | Event of clicking a component. |
| 'longClick' | Event indicating that the component is long pressed. |
| 'select' | Event of selecting a component. |
| 'hoverEnter' | Event indicating that the hover enters a component. |
| 'hoverExit' | Event indicating that the hover exits a component. |
| 'focus' | Event indicating that the component obtains the focus. Not supported currently. |
| 'textUpdate' | Event indicating that the component text has been updated. |
| 'textSelectionUpdate' | Event indicating that the selected text has been updated. Not supported currently. |
| 'scroll' | Event of the scroll view. |
| 'requestFocusForAccessibility' | Event of the auto-focusing. |
| 'announceForAccessibility' | Event of the auto-broadcasting. |
| 'requestFocusForAccessibilityNotInterrupt'18+ | Event of the auto-focusing without interruption. |
| 'announceForAccessibilityNotInterrupt'18+ | Event of the auto-broadcasting without interruption. |
| 'scrolling'18+ | Event indicating that an item is scrolled out of the screen in the scrolling view. |

#### TextMoveUnit

type TextMoveUnit = 'char' | 'word' | 'line' | 'page' | 'paragraph'

Enumerates the movement units for traversing the node text.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'char' | The movement unit for traversing the node text is by character. |
| 'word' | The movement unit for traversing the node text is by word. |
| 'line' | The movement unit for traversing the node text is by line. |
| 'page' | The movement unit for traversing the node text is by page. |
| 'paragraph' | The movement unit for traversing the node text is by paragraph. |

#### WindowUpdateType

type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'

Window update type.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| :-- | :-- |
| 'add' | Window adding. |
| 'remove' | Window deletion. |
| 'bounds' | Window boundary change. |
| 'active' | Window activity change. |
| 'focus' | Window focus change. |

#### accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

Obtains the accessibility application list. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/6fUe_v3sTlSuylwutjyqvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B914C0AA38FECA6C220E911C94641EB404658584B539CE7645604A96E4719F69)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [accessibility.getAccessibilityExtensionList](#accessibilitygetaccessibilityextensionlist9) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityType | [AbilityType](#abilitytype) | Yes | Accessibility application type. |
| stateType | [AbilityState](#abilitystate) | Yes | Accessibility application status. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AccessibilityAbilityInfo](#accessibilityabilityinfo)\>> | Promise used to return the accessibility application list. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo\[\]) => {
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get accessibility extension list because ${JSON.stringify(err)}\`);
});

#### accessibility.getAbilityLists(deprecated)

getAbilityLists(abilityType: AbilityType, stateType: AbilityState,callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

Obtains the accessibility application list. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bup28plzSPOv6n5ZYF6v3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AC23071054B7ACE11F00BB5AEB5FE66BF22CC3CB1490B40EF768F20857596B8)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [accessibility.getAccessibilityExtensionList](#accessibilitygetaccessibilityextensionlist9-1) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityType | [AbilityType](#abilitytype) | Yes | Accessibility application type. |
| stateType | [AbilityState](#abilitystate) | Yes | Accessibility application status. |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](#accessibilityabilityinfo)\>> | Yes | Callback used to return the accessibility application list. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken';
let abilityState: accessibility.AbilityState = 'enable';

accessibility.getAbilityLists(abilityType, abilityState, (err: BusinessError, data: accessibility.AccessibilityAbilityInfo\[\]) => {
  if (err) {
    console.error(\`failed to get accessibility extension list because ${JSON.stringify(err)}\`);
    return;
  }
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
})

#### accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Promise<Array<AccessibilityAbilityInfo>>

Obtains the accessibility application list. This API uses a promise to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityType | [AbilityType](#abilitytype) | Yes | Accessibility application type. |
| stateType | [AbilityState](#abilitystate) | Yes | Accessibility application status. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AccessibilityAbilityInfo](#accessibilityabilityinfo)\>> | Promise used to return the accessibility application list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Parameter example**

| Accessibility Application Type/State | enable | disable | install |
| :-- | :-- | :-- | :-- |
| **audible** | Queries enabled accessibility applications with audible feedback. | Queries disabled accessibility applications with audible feedback. | Queries installed accessibility applications with audible feedback. |
| **generic** | Queries enabled accessibility applications with generic feedback. | Queries disabled accessibility applications with generic feedback. | Queries installed accessibility applications with generic feedback. |
| **haptic** | Queries enabled accessibility applications with haptic feedback. | Queries disabled accessibility applications with haptic feedback. | Queries installed accessibility applications with haptic feedback. |
| **spoken** | Queries enabled accessibility applications with spoken feedback. | Queries disabled accessibility applications with spoken feedback. | Queries installed accessibility applications with spoken feedback. |
| **visual** | Queries enabled accessibility applications with visual feedback. | Queries disabled accessibility applications with visual feedback. | Queries installed accessibility applications with visual feedback. |
| **all** | Queries all enabled accessibility applications. | Queries all disabled accessibility applications. | Queries all installed accessibility applications. |

**Example of querying all installed accessibility applications**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // Set the accessibility application type to 'all'.
let abilityState: accessibility.AbilityState = 'install'; // Set the accessibility application state to 'install'.

accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo\[\]) => {
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}\`);
});

// For example, install an accessibility application whose bundle name is com.example.myaccessibilityapp in the system.
// The log output is as follows:
// \[{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":\[\],
// "capabilities":\["retrieve","gesture"\],"description":"$string:MainAbility\_desc",
// "eventTypes":\["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"\],"targetBundleNames":\[\],"needHide":false}}\]

**Example of querying all enabled accessibility applications with voice feedback**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // Set the accessibility application type to 'spoken'.
let abilityState: accessibility.AbilityState = 'enable'; // Set the accessibility application state to 'enable'.

accessibility.getAccessibilityExtensionList(abilityType, abilityState).then((data: accessibility.AccessibilityAbilityInfo\[\]) => {
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}\`);
});

#### accessibility.getAccessibilityExtensionList9+

getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState, callback: AsyncCallback<Array<AccessibilityAbilityInfo>>): void

Obtains the accessibility application list. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityType | [AbilityType](#abilitytype) | Yes | Accessibility application type. |
| stateType | [AbilityState](#abilitystate) | Yes | Accessibility application status. |
| callback | AsyncCallback<Array<[AccessibilityAbilityInfo](#accessibilityabilityinfo)\>> | Yes | Callback used to return the accessibility application list. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Parameter example**

| Accessibility Application Type/State | enable | disable | install |
| :-- | :-- | :-- | :-- |
| **audible** | Queries enabled accessibility applications with audible feedback. | Queries disabled accessibility applications with audible feedback. | Queries installed accessibility applications with audible feedback. |
| **generic** | Queries enabled accessibility applications with generic feedback. | Queries disabled accessibility applications with generic feedback. | Queries installed accessibility applications with generic feedback. |
| **haptic** | Queries enabled accessibility applications with haptic feedback. | Queries disabled accessibility applications with haptic feedback. | Queries installed accessibility applications with haptic feedback. |
| **spoken** | Queries enabled accessibility applications with spoken feedback. | Queries disabled accessibility applications with spoken feedback. | Queries installed accessibility applications with spoken feedback. |
| **visual** | Queries enabled accessibility applications with visual feedback. | Queries disabled accessibility applications with visual feedback. | Queries installed accessibility applications with visual feedback. |
| **all** | Queries all enabled accessibility applications. | Queries all disabled accessibility applications. | Queries all installed accessibility applications. |

**Example of querying all installed accessibility applications**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // Set the accessibility application type to 'all'.
let abilityState: accessibility.AbilityState = 'install'; // Set the accessibility application state to 'install'.

accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo\[\]) => {
  if (err) {
    console.error(\`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
});

// For example, install an accessibility application whose bundle name is com.example.myaccessibilityapp in the system.
// The log output is as follows:
// \[{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":\[\],
// "capabilities":\["retrieve","gesture"\],"description":"$string:MainAbility\_desc",
// "eventTypes":\["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"\],"targetBundleNames":\[\],"needHide":false}}\]

**Example of querying all enabled accessibility applications with voice feedback**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // Set the accessibility application type to 'spoken'.
let abilityState: accessibility.AbilityState = 'enable'; // Set the accessibility application state to 'enable'.

accessibility.getAccessibilityExtensionList(abilityType, abilityState,(err: BusinessError, data: accessibility.AccessibilityAbilityInfo\[\]) => {
  if (err) {
    console.error(\`failed to get accessibility extension list, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
});

#### accessibility.getAccessibilityExtensionListSync12+

getAccessibilityExtensionListSync(abilityType: AbilityType, stateType: AbilityState): Array<AccessibilityAbilityInfo>

Query the list of accessibility applications in the current system, which can be queried by criteria.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abilityType | [AbilityType](#abilitytype) | Yes | Accessibility application type. |
| stateType | [AbilityState](#abilitystate) | Yes | Accessibility application status. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[AccessibilityAbilityInfo](#accessibilityabilityinfo)\> | Promise used to return the accessibility application list. |

**Parameter example**

| Accessibility Application Type/State | enable | disable | install |
| :-- | :-- | :-- | :-- |
| **audible** | Queries enabled accessibility applications with audible feedback. | Queries disabled accessibility applications with audible feedback. | Queries installed accessibility applications with audible feedback. |
| **generic** | Queries enabled accessibility applications with generic feedback. | Queries disabled accessibility applications with generic feedback. | Queries installed accessibility applications with generic feedback. |
| **haptic** | Queries enabled accessibility applications with haptic feedback. | Queries disabled accessibility applications with haptic feedback. | Queries installed accessibility applications with haptic feedback. |
| **spoken** | Queries enabled accessibility applications with spoken feedback. | Queries disabled accessibility applications with spoken feedback. | Queries installed accessibility applications with spoken feedback. |
| **visual** | Queries enabled accessibility applications with visual feedback. | Queries disabled accessibility applications with visual feedback. | Queries installed accessibility applications with visual feedback. |
| **all** | Queries all enabled accessibility applications. | Queries all disabled accessibility applications. | Queries all installed accessibility applications. |

**Example of querying all installed accessibility applications**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'all'; // Set the accessibility application type to 'all'.
let abilityState: accessibility.AbilityState = 'install'; // Set the accessibility application state to 'install'.
let data: accessibility.AccessibilityAbilityInfo\[\];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
} catch (error) {
  let err = error as BusinessError;
  console.error(\`error code: ${err.code}\`);
}

// For example, install an accessibility application whose bundle name is com.example.myaccessibilityapp in the system.
// The log output is as follows:
// \[{"id":"com.example.myaccessibilityapp/AccessibilityExtAbility","name":"AccessibilityExtAbility",
// "bundleName":"com.example.myaccessibilityapp","abilityTypes":\[\],
// "capabilities":\["retrieve","gesture"\],"description":"$string:MainAbility\_desc",
// "eventTypes":\["click","longClick","select","focus","textUpdate","hoverEnter","hoverExit","scroll",
// "textSelectionUpdate","accessibilityFocus","accessibilityFocusClear","requestFocusForAccessibility",
// "announceForAccessibility","announceForAccessibilityNotInterrupt",
// "requestFocusForAccessibilityNotInterrupt","scrolling"\],"targetBundleNames":\[\],"needHide":false}}\]

**Example of querying all enabled accessibility applications with voice feedback**:

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityType: accessibility.AbilityType = 'spoken'; // Set the accessibility application type to 'spoken'.
let abilityState: accessibility.AbilityState = 'enable'; // Set the accessibility application state to 'enable'.
let data: accessibility.AccessibilityAbilityInfo\[\];

try {
  data = accessibility.getAccessibilityExtensionListSync(abilityType, abilityState);
  console.info(\`Succeeded in get accessibility extension list, ${JSON.stringify(data)}\`);
} catch (error) {
  let err = error as BusinessError;
  console.error(\`error code: ${err.code}\`);
}

#### accessibility.getCaptionsManager(deprecated)

getCaptionsManager(): CaptionsManager

Obtains a **CaptionsManager** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/QKasGlEgTxewjL57NbcEAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA16E024D2343897D25671F289C3C75D0E7B9CCAA7A14E0A19AF790421A6D777)

This API is supported since API version 8 and deprecated since API version 12. Related features are no longer available in the system.

**System capability**: SystemCapability.BarrierFree.Accessibility.Hearing

**Return value**

| Type | Description |
| :-- | :-- |
| [CaptionsManager](#captionsmanager8) | Captions configuration. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

let captionsManager = accessibility.getCaptionsManager();

#### accessibility.on('accessibilityStateChange')

on(type: 'accessibilityStateChange', callback: Callback<boolean>): void

Subscribes to the state changes of the accessibility application. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](#accessibilitygetaccessibilityextensionlistsync12).

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'accessibilityStateChange'** in this API. |
| callback | Callback<boolean> | Yes | Callback invoked when the enabled status of accessibility application changes. The returned result indicates the global enabled status of the accessibility application. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

// When one or more accessibility applications have been installed in the system:
// 1. After the first application is enabled, the callback returns true.
// 2. If one or more applications have been enabled and the last enabled one is disabled, the callback returns false.
accessibility.on('accessibilityStateChange', (data: boolean) => {
  console.info(\`subscribe accessibility state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.on('touchGuideStateChange')

on(type: 'touchGuideStateChange', callback: Callback<boolean>): void

Subscribes to the state changes in touch guide mode. This API uses an asynchronous callback to return the result. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](#accessibilitygetaccessibilityextensionlistsync12).

**System capability**: SystemCapability.BarrierFree.Accessibility.Vision

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'touchGuideStateChange'** in this API. |
| callback | Callback<boolean> | Yes | Callback invoked when the enabling state of touch guide mode changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

// When one or more accessibility applications with touch guide mode (touchGuide is set in Capability) have been installed in the system:
// 1. After the first application is enabled, the callback returns true.
// 2. If one or more applications have been enabled and the last enabled one is disabled, the callback returns false.
accessibility.on('touchGuideStateChange', (data: boolean) => {
  console.info(\`subscribe touch guide state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.on('screenReaderStateChange')18+

on(type: 'screenReaderStateChange', callback: Callback<boolean>): void

Subscribes to the state changes of the screen reader. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'screenReaderStateChange'** in this API. |
| callback | Callback<boolean> | Yes | Callback invoked when the enabling state of screen reader changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

accessibility.on('screenReaderStateChange', (data: boolean) => {
  console.info(\`subscribe screen reader state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.on('touchModeChange')20+

on(type: 'touchModeChange', callback: Callback<string>): void

Subscribers to the single- or double-touch event changes in touch guide mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'touchModeChange'** in this API. |
| callback | Callback<string> | Yes | Callback to be invoked when the single- or double-touch event changes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(\`current touch mode: ${JSON.stringify(mode)}\`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### accessibility.off('accessibilityStateChange')

off(type: 'accessibilityStateChange', callback?: Callback<boolean>): void

Unsubscribes from the state changes of the accessibility application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'accessibilityStateChange'** in this API. |
| callback | Callback<boolean> | No | Callback used to unregister. The value must be the same as the value of **callback** in **accessibility.on('accessibilityStateChange')**. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('accessibilityStateChange', (data: boolean) => {
  console.info(\`Unsubscribe accessibility state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.off('touchGuideStateChange')

off(type: 'touchGuideStateChange', callback?: Callback<boolean>): void

Unsubscribes from the state changes in touch guide mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'touchGuideStateChange'** in this API. |
| callback | Callback<boolean> | No | Callback used to unregister. The value must be the same as the value of **callback** in **accessibility.on('touchGuideStateChange')**. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('touchGuideStateChange', (data: boolean) => {
  console.info(\`Unsubscribe touch guide state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.off('screenReaderStateChange')18+

off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void

Unsubscribes from the state changes of the screen reader. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'screenReaderStateChange'** in this API. |
| callback | Callback<boolean> | No | Callback used to unregister. The value must be the same as the value of **callback** in **accessibility.on('screenReaderStateChange')**. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

accessibility.off('screenReaderStateChange', (data: boolean) => {
  console.info(\`Unsubscribe screen reader state change, result: ${JSON.stringify(data)}\`);
});

#### accessibility.off('touchModeChange')20+

off(type: 'touchModeChange', callback?: Callback<string>): void

Unsubscribes from the single- or double-touch event changes in touch guide mode. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is set to **'touchModeChange'** in this API. |
| callback | Callback<string> | No | Callback used to unregister. The callback must be the same as that of [accessibility.on('touchModeChange')](#accessibilityontouchmodechange20). If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (mode: string) => void = this.eventCallback;
  eventCallback(mode: string): void {
    console.info(\`current touch mode: ${JSON.stringify(mode)}\`);
  }

  aboutToAppear(): void {
    accessibility.on('touchModeChange', this.callback);
  }

  aboutToDisappear(): void {
    accessibility.off('touchModeChange', this.callback);
  }

  build() {
    Column() {
    }
  }
}

#### accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(): Promise<boolean>

Checks whether an accessibility application is enabled. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/etkCg9XWTdKtqOCfIiwvPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D1A7351C4770865F1A1170572B1F02EEE6D8A38F9904DAA3D950B0DC7C9643F)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [accessibility.isOpenAccessibilitySync](#accessibilityisopenaccessibilitysync10) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if the accessibility application is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility().then((data: boolean) => {
  console.info(\`success data:isOpenAccessibility : ${JSON.stringify(data)}\`)
}).catch((err: BusinessError) => {
  console.error(\`failed to  isOpenAccessibility, Code is ${err.code}, message is ${err.message}\`);
});

#### accessibility.isOpenAccessibility(deprecated)

isOpenAccessibility(callback: AsyncCallback<boolean>): void

Checks whether an accessibility application is enabled. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/DkuafQ5dR9yKaZSWAs0EBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6C668F6578A8FADE074C8AD651D9A3A2702120953F1476191B6CC82868E50E6)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [accessibility.isOpenAccessibilitySync](#accessibilityisopenaccessibilitysync10) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the accessibility application is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenAccessibility((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(\`failed to isOpenAccessibility, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`success data:isOpenAccessibility : ${JSON.stringify(data)}\`);
});

#### accessibility.isOpenAccessibilitySync10+

isOpenAccessibilitySync(): boolean

Checks whether any accessibility application has been enabled in the system. To obtain information about accessibility applications in the system, use [accessibility.getAccessibilityExtensionListSync](#accessibilitygetaccessibilityextensionlistsync12).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether any accessibility application has been enabled in the system. Returns **true** if one or more accessibility applications are enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1. If no accessibility application is enabled, the system returns false.
// 2. If any accessibility application is enabled, the system returns true.
let status: boolean = accessibility.isOpenAccessibilitySync();

#### accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(): Promise<boolean>

Checks whether touch guide mode is enabled. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/LWaAfjzARU6TGhOEop8L9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82D55E90A4E5EC1C84F5B9596253900B0A47092032E61AA2C505FFA8D50A96B3)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [accessibility.isOpenTouchGuideSync](#accessibilityisopentouchguidesync10) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Vision

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if touch guide mode is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide().then((data: boolean) => {
  console.info(\`success data:isOpenTouchGuide : ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to  isOpenTouchGuide, Code is ${err.code}, message is ${err.message}\`);
});

#### accessibility.isOpenTouchGuide(deprecated)

isOpenTouchGuide(callback: AsyncCallback<boolean>): void

Checks whether touch guide mode is enabled. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/n1bKdDQDRDOeO_7pCIRS6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7C5EA1FA2A4E990A72649024FD60539584A82AB6D39EAC906B34FB14B6D0FA6)

This API is supported since API version 7 and deprecated since API version 10. You are advised to use [accessibility.isOpenTouchGuideSync](#accessibilityisopentouchguidesync10) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Vision

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if touch guide mode is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

accessibility.isOpenTouchGuide((err: BusinessError, data: boolean) => {
  if (err) {
    console.error(\`failed to isOpenTouchGuide, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`success data:isOpenTouchGuide : ${JSON.stringify(data)}\`);
});

#### accessibility.isOpenTouchGuideSync10+

isOpenTouchGuideSync(): boolean

Checks whether touch guide mode is enabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BarrierFree.Accessibility.Vision

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the touch guide mode is enabled. Returns **true** if touch guide mode is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isOpenTouchGuideSync();

#### accessibility.isScreenReaderOpenSync18+

isScreenReaderOpenSync(): boolean

Checks whether the screen reader mode is enabled.

**System capability**: SystemCapability.BarrierFree.Accessibility.Vision

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the screen reader is enabled. Returns **true** if the screen reader is enabled; returns **false** otherwise. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isScreenReaderOpenSync();

#### accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo): Promise<void>

Sends an accessibility event. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-dQxfl18R5-ibPgCG_YofQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A677445A2C5F09692567440B0BFAA619EF2E501A54597E439A6E18E240758FB)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [accessibility.sendAccessibilityEvent](#accessibilitysendaccessibilityevent9) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [EventInfo](#eventinfo) | Yes | Accessibility event. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo).then(() => {
  console.info(\`Succeeded in send event,eventInfo is ${eventInfo}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to sendEvent, Code is ${err.code}, message is ${err.message}\`);
});

#### accessibility.sendEvent(deprecated)

sendEvent(event: EventInfo, callback: AsyncCallback<void>): void

Sends an accessibility event. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/lrkx7UGfQoiSafnbQCfNPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F129C7F4C07D753230993360C336D44603580D5B81D57B211E7B58B429F65245)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [accessibility.sendAccessibilityEvent](#accessibilitysendaccessibilityevent9-1) instead.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [EventInfo](#eventinfo) | Yes | Accessibility event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, **err** that contains data is returned. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(\`failed to sendEvent, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in sendEvent, eventInfo is ${eventInfo}\`);
});

#### accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo): Promise<void>

Sends an accessibility event. This API uses a promise to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [EventInfo](#eventinfo) | Yes | Accessibility event. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo).then(() => {
  console.info(\`Succeeded in send event,eventInfo is ${eventInfo}\`);
}).catch((err: BusinessError) => {
  console.error(\`failed to send event , Code is ${err.code}, message is ${err.message}\`);
});

#### accessibility.sendAccessibilityEvent9+

sendAccessibilityEvent(event: EventInfo, callback: AsyncCallback<void>): void

Sends an accessibility event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [EventInfo](#eventinfo) | Yes | Accessibility event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation fails, **err** that contains data is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'click',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'click',
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(\`failed to send event, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in send event, eventInfo is ${eventInfo}\`);
});

**Example of auto-focusing:**

@Entry
@Component
struct Index {

  build() {
    Column() {
      // Add the ID attribute to the component to be focused. The uniqueness of the ID is ensured by the user.
      Button('Component to be focused').id('click')
    }
  }
}

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'requestFocusForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  customId: 'click' // ID of the component to be focused.
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(\`failed to send event, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in send event, eventInfo is ${eventInfo}\`);
});

**Example of resource-supported auto-broadcasting18+:**

import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let eventInfo: accessibility.EventInfo = ({
  type: 'announceForAccessibility',
  bundleName: 'com.example.MyApplication',
  triggerAction: 'common',
  textResourceAnnouncedForAccessibility: $r('app.string.ResourceName'),
});

accessibility.sendAccessibilityEvent(eventInfo, (err: BusinessError) => {
  if (err) {
    console.error(\`failed to send event, Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in send event, eventInfo is ${eventInfo}\`);
});

#### accessibility.getTouchModeSync20+

getTouchModeSync(): string

Queries the single- or double-touch mode.

**System capability**: SystemCapability.BarrierFree.Accessibility.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
Touch mode.

\- **singleTouchMode**: single-touch mode.

\- **doubleTouchMode**: double-touch mode.

\- **none**: The touch mode is disabled.

 |

import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    let touchMode: string = accessibility.getTouchModeSync();
    console.info(\`current touch mode: ${JSON.stringify(touchMode)}\`);
  }

  build() {
    Column() {
    }
  }
}
