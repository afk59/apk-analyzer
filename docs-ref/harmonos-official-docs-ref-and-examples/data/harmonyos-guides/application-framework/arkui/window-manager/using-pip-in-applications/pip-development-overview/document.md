# PiP Development Overview

#### When to Use

The Picture in Picture (PiP) feature enables users to watch a video in a small window while they can operate the other part of the screen. PiP is mainly used in video playback, video meetings, and video calls.

The common use cases of PiP are as follows:

-   Video playback
-   Video calls
-   Video meetings
-   Live

The system provides three modes for developing the PiP feature.

-   [Using XComponent to develop PiP](../using-xcomponent-to-develop-pip-arkts/document.md): This mode is suitable for an application that uses the [Navigation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation) component to manage pages or an ability that has only one page. The application does not need to manage pages.
-   [Using typeNode to develop PiP](../using-typenode-to-develop-pip-arkts/document.md): This mode is applicable to all scenarios and is recommended. The application needs to manage pages.
-   [Using NDK APIs to develop PiP](../using-ndk-apis-to-develop-pip-c-c/document.md): This mode is applicable to applications that depend on NDK APIs. The application needs to manage pages.

#### Constraints

-   For security purposes, do not start a PiP window by calling the **startPiP** API when the application is running in the background. Instead, call the **setAutoStartEnabled(true)** API.

#### Available APIs

The following table lists the common ArkTS APIs for the PiP feature. For details, see [@ohos.PiPWindow (PiP Window)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

isPiPEnabled(): boolean

 | 

Checks whether the PiP feature is enabled.

 |
| 

create(config: PiPConfiguration): Promise<PiPController>

 | 

Creates a PiP controller.

 |
| 

create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>

 | 

Creates a PiP controller through typeNode.

 |
| 

startPiP(): Promise<void>

 | 

Starts a PiP window.

 |
| 

stopPiP(): Promise<void>

 | 

Stops a PiP window.

 |
| 

setAutoStartEnabled(enable: boolean): void

 | 

Sets whether to automatically enable the PiP feature when the application moves to the background. **true** to enable, **false** otherwise.

 |
| 

updateContentSize(width: number, height: number): void

 | 

Updates the media content size when the media content is switched.

 |
| 

on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void

 | 

Subscribes to PiP state events.

 |
| 

off(type: 'stateChange'): void

 | 

Unsubscribes from PiP state events.

 |
| 

on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void

 | 

Subscribes to PiP action events. The **on('controlEvent')** API is preferred.

 |
| 

off(type: 'controlPanelActionEvent'): void

 | 

Unsubscribes from PiP action events. The **off('controlEvent')** API is preferred.

 |
| 

updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void

 | 

Updates the PiP control status.

 |
| 

setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void

 | 

Sets the PiP component enabling status.

 |
| 

on(type: 'controlEvent', callback: CallBack<ControlEventParam>): void

 | 

Subscribes to PiP action events.

 |
| 

off(type: 'controlEvent', callback?: CallBack<ControlEventParam>): void

 | 

Unsubscribes from PiP action events.

 |

The following table lists the common NDK APIs for the PiP feature. For details, see [oh\_window\_pip.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-window-pip-h).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t OH\_PictureInPicture\_CreatePipConfig(PictureInPicture\_PipConfig\* pipConfig)

 | 

Creates a PiP configurator.

 |
| 

int32\_t OH\_PictureInPicture\_DestroyPipConfig(PictureInPicture\_PipConfig\* pipConfig)

 | 

Destroys a PiP configurator.

 |
| 

int32\_t OH\_PictureInPicture\_CreatePip(PictureInPicture\_PipConfig pipConfig, uint32\_t\* controllerId)

 | 

Creates a PiP controller.

 |
| 

int32\_t OH\_PictureInPicture\_DeletePip(uint32\_t controllerId)

 | 

Deletes a PiP controller.

 |
| 

int32\_t OH\_PictureInPicture\_StartPip(uint32\_t controllerId)

 | 

Starts a PiP window.

 |
| 

int32\_t OH\_PictureInPicture\_StopPip(uint32\_t controllerId)

 | 

Stops a PiP window.

 |
| 

int32\_t OH\_PictureInPicture\_UpdatePipContentSize(uint32\_t controllerId, uint32\_t width, uint32\_t height)

 | 

Updates the media content size when the media content is switched.

 |
| 

int32\_t OH\_PictureInPicture\_UpdatePipControlStatus(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, PictureInPicture\_PipControlStatus status)

 | 

Updates the PiP control status.

 |
| 

int32\_t OH\_PictureInPicture\_SetPipControlEnabled(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, bool enabled)

 | 

Sets the PiP component enabling status.

 |
| 

int32\_t OH\_PictureInPicture\_RegisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)

 | 

Subscribes to the completion of creating a PiP surface.

 |
| 

int32\_t OH\_PictureInPicture\_UnregisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback)

 | 

Unsubscribes from the completion of creating a PiP surface.

 |
| 

int32\_t OH\_PictureInPicture\_RegisterLifecycleListener(uint32\_t controllerId, WebPipLifeCycleCallback callback)

 | 

Subscribes to PiP state events.

 |
| 

int32\_t OH\_PictureInPicture\_UnregisterLifecycleListener(uint32\_t controllerId, WebPipLifeCycleCallback callback)

 | 

Unsubscribes from PiP state events.

 |
| 

int32\_t OH\_PictureInPicture\_RegisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)

 | 

Subscribes to PiP action events.

 |
| 

int32\_t OH\_PictureInPicture\_UnregisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback)

 | 

Unsubscribes from PiP action events.

 |
| 

int32\_t OH\_PictureInPicture\_RegisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)

 | 

Subscribes to PiP window size change events.

 |
| 

int32\_t OH\_PictureInPicture\_UnregisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback)

 | 

Unsubscribes from PiP window size change events.

 |

#### Interaction Modes

The PiP window provides the following interaction modes:

-   Touch: A touch will show the PiP controller if it is not already visible, and it will automatically disappear after 3 seconds of inactivity. If the PiP controller is visible, a touch will hide it.
-   Double-touch: A double-touch zooms in or zooms out the PiP window.
-   Drag: You can drag the PiP window to any position on the screen. If dragged to the left or right edge of the screen, the PiP window is automatically hidden, and a corresponding icon is displayed on the edge. A touch to the icon shows the PiP window again.
-   Drag to resize: You can resize the PiP window by dragging any of its four edges or four corners. The window size is constrained between a predefined minimum and maximum limit. If a drag action would cause the window to exceed these size limits or the screen boundaries, it smoothly snaps back to the nearest valid position.
-   Drag to delete: To delete a PiP window, simply drag it to the trash bin area at the bottom of the screen. Applications that request continuous tasks should proactively listen for the STOPPED event in the PiP lifecycle and stop the task or process accordingly.

The PiP controller provides the following functions:

-   Window control: includes **Close** and **Full-screen Window**. After users touch **Close**, the PiP window is closed. After users touch **Full-screen Window**, the original screen is restored.
-   Content control: The content control area varies according to the scenario and needs to be configured accordingly. The following figure shows the controllers in each scenario.

**Figure 1** Different forms of the PiP controller in different scenarios  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Rzccw_snQsi6sdqsfFaPYA/en-us_image_0000002497742070.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DEB8BDF9AD44DCD92FC0C0D9A154DDCFA430D6535255F1F183BEE3B1CBD520F "Click to enlarge")

#### Configuring Optional Components in the PiP Controller

When using the [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipwindowcreate) API to create a PiP controller instance, you can add a [PiPControlGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipcontrolgroup12) array to [PiPConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipconfiguration) to configure the PiP controller components.

-   In video playback, configure [VideoPlayControlGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#videoplaycontrolgroup12) to display optional controller components.
    
    **Figure 2** Optional controller components in video playback  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/dFwgBeHrRhifnlzQ2idXWQ/en-us_image_0000002529702005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E563E82FF446926B626DF43F73B04BCE88B4D681E1BC135813611F70A1A0967 "Click to enlarge")
    
-   In video calls, configure [VideoCallControlGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#videocallcontrolgroup12) to display optional controller components.
    
    **Figure 3** Optional controller components in video calls  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qf_ra9XbSVWpUtiqR_ZMrA/en-us_image_0000002529582039.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96FE13C655FE048A46EAB481C03AF347DCD50E98B223176A5C68D92AE59DE854 "Click to enlarge")
    
    If **VideoCallControlGroup** is not set, there is no button in video calls by default. You can touch any position in the PiP window to trigger a restoration (see the left figure). The right figure shows the PiP window when **VideoCallControlGroup** is set.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/xwTBUej6SH-S--RCTul2VA/en-us_image_0000002497902046.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FB6B613DA854D70BB6054D92A0869367D310A9C52DFC30D62FAB4A3882BFDB6 "Click to enlarge")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/KeRex6sWRJOeX0_dAbYKeQ/en-us_image_0000002497902044.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48C80D3D64FE7E9CA50008F58C5815A376FDAF77DC94F3993048D48CDAD9DBAC "Click to enlarge")
    
-   In video meetings, configure [VideoMeetingControlGroup](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#videomeetingcontrolgroup12) to display optional controller components. If **VideoMeetingControlGroup** is not set, there is no button in video meetings by default. You can click any position in the PiP window to trigger a restoration (same as that in video calls).
    
    **Figure 4** Optional controller components in video meetings
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/po0Xdco4QtmhT30F7KSBOw/en-us_image_0000002529702007.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA4145C3C1C907EBBB018A207171733D505CA1256EE37E085FB651268D3F5A56 "Click to enlarge")
    
-   In live scenarios, configure [VideoLiveControlGroup](https://gitee.com/openharmony/docs/blob/6ef3072be96ddb9e029f1ee7f303c27f4747b94a/en/application-dev/reference/apis-arkui/js-apis-pipWindow.md#videolivecontrolgroup12) to display optional controller components.
    
    **Figure 5** Optional controller components in live scenarios  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/6_918CdfQd29ggYAXP6qxA/en-us_image_0000002497742072.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3104ADAB559D029B1563A181D5BA2A37AB65420AE108F44F05582DDEA5B99588 "Click to enlarge")
    

#### Displaying the Custom UI at the Top

When using the [create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipwindowcreate) API to create a PiP controller instance, you can pass in the **customUIController** to [PiPConfiguration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pipwindow#pipconfiguration) to display the custom UI.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XD0tiUQNRK-5Y2jeyLf6Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BDC9BC18F94D6C76F6FA966C71215F542DC040323EA5A518D51713871A85C31)

The custom UI cannot respond to interaction events.

**Figure 6** Displaying the custom UI at the top of the PiP window  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/srQoj4yMSdGqoBtL-4Ls8Q/en-us_image_0000002497902042.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD3DEEB8F9E4A79AD5E381DCD01F134F23693EC66866DDB15E315B51B80AA525)

#### Updating the PiP Component Status

An application can update the PiP component status by calling the **updatePiPControlStatus** API. The following figure shows how to change the **VIDEO\_PLAY\_PAUSE** component to the paused state.

An application can set the PiP component enabling status by calling the **setPiPControlEnabled** API. The following figure shows how to change the **VIDEO\_PREVIOUS** component to the non-clickable state.

**Figure 7** Updating the PiP component status  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/aHJJmvRWT4WnpDxZ_dX0bQ/en-us_image_0000002497742068.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F236448D028AF7E10D9643A4A2A8E5C497B86A857C15946BD9790D952B460EEF "Click to enlarge")

**Figure 8** Setting the PiP component enabling status  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Z8gh21U1S2KtGzisoCLJ_g/en-us_image_0000002529582035.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95CD08DE3302EC6105E6F6CB2F51C7C83A19D0239F3E180BE055499BECF95191 "Click to enlarge")
