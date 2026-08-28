# Module Description

In the stage model, a window stage or window can use the [loadContent](../../../window-manager/ohos-window-window/interface-window/document.md#loadcontent9) API to load pages, create a UI instance, and render page content to the associated window. Naturally, UI instances and windows are associated on a one-by-one basis. Some global UI APIs are executed in the context of certain UI instances. When calling these APIs, you must identify the UI context, and consequently UI instance, by tracing the call chain. If these APIs are called on a non-UI page or in some asynchronous callback, the current UI context may fail to be identified, resulting in API execution errors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/qmUo64HCTgyvK7BcSDl_Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DD23B6A33DF719243540B5DA55D8B6C204327551303A0E8295E9F7C0918983D)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   You can preview how this component looks on a real device, but not in DevEco Studio Previewer.
    

#### Modules to Import

import {
  AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager,
  PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MeasureUtils, FrameCallback,
  OverlayManagerOptions, TargetInfo, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, Magnifier
} from "@kit.ArkUI";

**System capability**: SystemCapability.ArkUI.ArkUI.Full
