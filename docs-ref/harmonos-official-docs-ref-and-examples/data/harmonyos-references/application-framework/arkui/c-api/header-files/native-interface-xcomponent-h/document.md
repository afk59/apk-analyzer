# native\_interface\_xcomponent.h

#### Overview

Declares the APIs for accessing Native XComponent features.

**File to include**: <ace/xcomponent/native\_interface\_xcomponent.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 8

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Sample**: [NativeXComponentSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeXComponentSample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeXComponent\_HistoricalPoint](../../structs/oh-nativexcomponent-historicalpoint/document.md) | OH\_NativeXComponent\_HistoricalPoint | Represents a historical touch point. |
| [OH\_NativeXComponent\_TouchPoint](../../structs/oh-nativexcomponent-touchpoint/document.md) | OH\_NativeXComponent\_TouchPoint | Describes the touch point of the touch event. |
| [OH\_NativeXComponent\_TouchEvent](../../structs/oh-nativexcomponent-touchevent/document.md) | OH\_NativeXComponent\_TouchEvent | Describes the touch event. |
| [OH\_NativeXComponent\_MouseEvent](../../structs/oh-nativexcomponent-mouseevent/document.md) | OH\_NativeXComponent\_MouseEvent | Describes the mouse event. |
| [OH\_NativeXComponent\_Callback](../../structs/oh-nativexcomponent-callback/document.md) | OH\_NativeXComponent\_Callback | Registers callbacks for the surface lifecycle and touch event. |
| [OH\_NativeXComponent\_MouseEvent\_Callback](../../structs/oh-nativexcomponent-mouseevent-callback/document.md) | OH\_NativeXComponent\_MouseEvent\_Callback | Registers callbacks for the mouse event. |
| [OH\_NativeXComponent\_ExpectedRateRange](../../structs/oh-nativexcomponent-expectedraterange/document.md) | OH\_NativeXComponent\_ExpectedRateRange | Defines the expected frame rate range. |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) | OH\_NativeXComponent | Provides an encapsulated **OH\_NativeXComponent** instance. |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) | OH\_NativeXComponent\_KeyEvent | Provides an encapsulated **OH\_NativeXComponent\_KeyEvent** instance. |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md) | OH\_NativeXComponent\_ExtraMouseEventInfo | Provides an encapsulated instance of extended mouse event information. |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) | OH\_ArkUI\_SurfaceHolder | Provides an encapsulated **OH\_ArkUI\_SurfaceHolder** instance. |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) | OH\_ArkUI\_SurfaceCallback | Defines surface lifecycle callback functions. |
| [NativeWindow](../../structs/ohnativewindow/document.md) | OHNativeWindow | Provides an encapsulated **NativeWindow** instance. |
| [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) | ArkUI\_XComponentSurfaceConfig | Defines the surface configuration for the **XComponent**, which specifies whether the **XComponent**'s surface should be treated as opaque during rendering. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [anonymous](#anonymous) | \- | Enumerates the API access states. |
| [ArkUI\_XComponent\_ImageAnalyzerState](#arkui_xcomponent_imageanalyzerstate) | ArkUI\_XComponent\_ImageAnalyzerState | Enumerates the AI image analyzer error codes of the XComponent. |
| [OH\_NativeXComponent\_TouchEventType](#oh_nativexcomponent_toucheventtype) | OH\_NativeXComponent\_TouchEventType | Enumerates the touch event types. |
| [OH\_NativeXComponent\_TouchPointToolType](#oh_nativexcomponent_touchpointtooltype) | OH\_NativeXComponent\_TouchPointToolType | Enumerates the touch point tool types. |
| [OH\_NativeXComponent\_EventSourceType](#oh_nativexcomponent_eventsourcetype) | OH\_NativeXComponent\_EventSourceType | Enumerates the touch event source types. |
| [OH\_NativeXComponent\_MouseEventAction](#oh_nativexcomponent_mouseeventaction) | OH\_NativeXComponent\_MouseEventAction | Enumerates the mouse event actions. |
| [OH\_NativeXComponent\_MouseEventButton](#oh_nativexcomponent_mouseeventbutton) | OH\_NativeXComponent\_MouseEventButton | Enumerates the mouse event buttons. |
| [OH\_NativeXComponent\_TouchEvent\_SourceTool](#oh_nativexcomponent_touchevent_sourcetool) | OH\_NativeXComponent\_TouchEvent\_SourceTool | Enumerates the source tool types of touch events. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| OH\_NATIVE\_XCOMPONENT\_OBJ ("**NATIVE\_XCOMPONENT\_OBJ**") | Native **XComponent** instance. |
| OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER 10 | Maximum number of identifiable touch points in a touch event. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_NativeXComponent\_GetXComponentId(OH\_NativeXComponent\* component, char\* id, uint64\_t\* size)](#oh_nativexcomponent_getxcomponentid) | Obtains the ID of ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_GetXComponentSize(OH\_NativeXComponent\* component, const void\* window, uint64\_t\* width, uint64\_t\* height)](#oh_nativexcomponent_getxcomponentsize) | Obtains the size of the surface held by the ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_GetXComponentOffset(OH\_NativeXComponent\* component, const void\* window, double\* x, double\* y)](#oh_nativexcomponent_getxcomponentoffset) | Obtains the offset of the surface held by the XComponent relative to the upper left corner of its parent component. |
| [int32\_t OH\_NativeXComponent\_GetTouchEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_TouchEvent\* touchEvent)](#oh_nativexcomponent_gettouchevent) | Obtains the touch event scheduled by the ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointToolType(OH\_NativeXComponent\* component, uint32\_t pointIndex, OH\_NativeXComponent\_TouchPointToolType\* toolType)](#oh_nativexcomponent_gettouchpointtooltype) | Obtains the ArkUI XComponent touch point tool type. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointTiltX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltX)](#oh_nativexcomponent_gettouchpointtiltx) | Obtains the angle between the Y-Z plane of the ArkUI XComponent touch point and the x-axis. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointTiltY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltY)](#oh_nativexcomponent_gettouchpointtilty) | Obtains the angle between the X-Z plane of the ArkUI XComponent touch point and the y-axis. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointWindowX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowX)](#oh_nativexcomponent_gettouchpointwindowx) | Obtains the x-coordinate of the touch point relative to the upper left corner of the application window where the ArkUI XComponent is located. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointWindowY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowY)](#oh_nativexcomponent_gettouchpointwindowy) | Obtains the y-coordinate of the touch point relative to the upper left corner of the application window where the ArkUI XComponent is located. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointDisplayX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayX)](#oh_nativexcomponent_gettouchpointdisplayx) | Obtains the x-coordinate of the touch point relative to the upper left corner of the screen where the ArkUI XComponent is located. |
| [int32\_t OH\_NativeXComponent\_GetTouchPointDisplayY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayY)](#oh_nativexcomponent_gettouchpointdisplayy) | Obtains the y-coordinate of the touch point relative to the upper left corner of the screen where the ArkUI XComponent is located. |
| [int32\_t OH\_NativeXComponent\_GetHistoricalPoints(OH\_NativeXComponent\* component, const void\* window, int32\_t\* size, OH\_NativeXComponent\_HistoricalPoint\*\* historicalPoints)](#oh_nativexcomponent_gethistoricalpoints) | Obtains the historical touch point data for the touch event of an **OH\_NativeXComponent** instance. Some input devices report touch points at very high frequencies (up to 1 ms intervals). However, since UI updates typically do not require such high-frequency updates, the system consolidates touch events and reports them once per frame. All touch points collected during the current frame are preserved as historical touch points for applications that need direct access to this raw data. |
| [int32\_t OH\_NativeXComponent\_GetMouseEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_MouseEvent\* mouseEvent)](#oh_nativexcomponent_getmouseevent) | Obtains the mouse event scheduled by the ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_RegisterCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_Callback\* callback)](#oh_nativexcomponent_registercallback) | Registers a callback for the [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_RegisterMouseEventCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_MouseEvent\_Callback\* callback)](#oh_nativexcomponent_registermouseeventcallback) | Registers a mouse event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_GetExtraMouseEventInfo(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExtraMouseEventInfo\*\* extraMouseEventInfo)](#oh_nativexcomponent_getextramouseeventinfo) | Obtains extended mouse event information from this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_GetMouseEventModifierKeyStates (OH\_NativeXComponent\_ExtraMouseEventInfo\* extraMouseEventInfo, uint64\_t\* keys)](#oh_nativexcomponent_getmouseeventmodifierkeystates) | Obtains the state of modifier keys from an [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_RegisterFocusEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registerfocuseventcallback) | Registers a focus event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_RegisterKeyEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registerkeyeventcallback) | Registers a key event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_RegisterBlurEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registerblureventcallback) | Registers a blur event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_GetKeyEvent(OH\_NativeXComponent\* component, OH\_NativeXComponent\_KeyEvent\*\* keyEvent)](#oh_nativexcomponent_getkeyevent) | Obtains the key event scheduled by the ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventAction(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyAction\* action)](#oh_nativexcomponent_getkeyeventaction) | Obtains the action of the specified key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventCode(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyCode\* code)](#oh_nativexcomponent_getkeyeventcode) | Obtains the key code of the specified key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventSourceType(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_EventSourceType\* sourceType)](#oh_nativexcomponent_getkeyeventsourcetype) | Obtains the source type of the specified key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventDeviceId(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* deviceId)](#oh_nativexcomponent_getkeyeventdeviceid) | Obtains the device ID of the specified key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventTimestamp(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* timestamp)](#oh_nativexcomponent_getkeyeventtimestamp) | Obtains the timestamp of the specified key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventModifierKeyStates(OH\_NativeXComponent\_KeyEvent\* keyEvent, uint64\_t\* keys)](#oh_nativexcomponent_getkeyeventmodifierkeystates) | Obtains the state of modifier keys from a key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventNumLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isNumLockOn)](#oh_nativexcomponent_getkeyeventnumlockstate) | Obtains the state of the NumLock key from a key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventCapsLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isCapsLockOn)](#oh_nativexcomponent_getkeyeventcapslockstate) | Obtains the state of the CapsLock key from a key event. |
| [int32\_t OH\_NativeXComponent\_GetKeyEventScrollLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isScrollLockOn)](#oh_nativexcomponent_getkeyeventscrolllockstate) | Obtains the state of the ScrollLock key from a key event. |
| [int32\_t OH\_NativeXComponent\_SetExpectedFrameRateRange(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExpectedRateRange\* range)](#oh_nativexcomponent_setexpectedframeraterange) | Sets the expected frame rate range. |
| [int32\_t OH\_NativeXComponent\_RegisterOnFrameCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, uint64\_t timestamp, uint64\_t targetTimestamp))](#oh_nativexcomponent_registeronframecallback) | Registers the display update callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables the callback for each frame. |
| [int32\_t OH\_NativeXComponent\_UnregisterOnFrameCallback(OH\_NativeXComponent\* component)](#oh_nativexcomponent_unregisteronframecallback) | Deregisters the display update callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and disables the callback for each frame. |
| [int32\_t OH\_NativeXComponent\_AttachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)](#oh_nativexcomponent_attachnativerootnode) | Attaches the UI component created through the native API of ArkUI to this **OH\_NativeXComponent** instance. |
| [int32\_t OH\_NativeXComponent\_DetachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)](#oh_nativexcomponent_detachnativerootnode) | Detaches the native component of ArkUI from this **OH\_NativeXComponent** instance. |
| [int32\_t OH\_NativeXComponent\_RegisterUIInputEventCallback(OH\_NativeXComponent \*component, void (\*callback)(OH\_NativeXComponent \*component, ArkUI\_UIInputEvent \*event,ArkUI\_UIInputEvent\_Type type),ArkUI\_UIInputEvent\_Type type)](#oh_nativexcomponent_registeruiinputeventcallback) | Registers a UI input event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables this callback to be invoked when a UI input event is received. Currently, only axis events are supported. |
| [int32\_t OH\_NativeXComponent\_RegisterOnTouchInterceptCallback(OH\_NativeXComponent\* component, HitTestMode (\*callback)(OH\_NativeXComponent\* component, ArkUI\_UIInputEvent\* event))](#oh_nativexcomponent_registerontouchinterceptcallback) | Registers a custom event intercept callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables this callback to be invoked during hit testing. UI input–related operations are not supported on event objects received through this callback. For full functionality, use the [NODE\_ON\_TOUCH\_INTERCEPT](../native-node-h/document.md#arkui_nodeeventtype) event on native nodes instead. |
| [int32\_t OH\_NativeXComponent\_SetNeedSoftKeyboard(OH\_NativeXComponent\* component, bool needSoftKeyboard)](#oh_nativexcomponent_setneedsoftkeyboard) | Sets whether the soft keyboard is required for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [int32\_t OH\_NativeXComponent\_RegisterSurfaceShowCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registersurfaceshowcallback) | Registers a surface display callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. This callback is invoked after the application is switched to the foreground. |
| [int32\_t OH\_NativeXComponent\_RegisterSurfaceHideCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registersurfacehidecallback) | Registers a surface hiding callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. This callback is invoked after the application is switched to the background. |
| [int32\_t OH\_NativeXComponent\_GetTouchEventSourceType(OH\_NativeXComponent\* component, int32\_t pointId, OH\_NativeXComponent\_EventSourceType\* sourceType)](#oh_nativexcomponent_gettoucheventsourcetype) | Obtains the touch event source type of an ArkUI XComponent instance. |
| [OH\_NativeXComponent\* OH\_NativeXComponent\_GetNativeXComponent(ArkUI\_NodeHandle node)](#oh_nativexcomponent_getnativexcomponent) | Obtains a pointer of the [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) type based on the specified component instance created by the native API. |
| [int32\_t OH\_NativeXComponent\_GetNativeAccessibilityProvider(OH\_NativeXComponent\* component, ArkUI\_AccessibilityProvider\*\* handle)](#oh_nativexcomponent_getnativeaccessibilityprovider) | Obtains the accessibility provider handle for an ArkUI XComponent. |
| [int32\_t OH\_NativeXComponent\_RegisterKeyEventCallbackWithResult(OH\_NativeXComponent\* component, bool (\*callback)(OH\_NativeXComponent\* component, void\* window))](#oh_nativexcomponent_registerkeyeventcallbackwithresult) | Registers a key event callback with a return value for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. The callback must return a result (**true** or **false**). If the callback returns **true**, the event will not be further propagated. If it returns **false**, the event will continue to be processed according to the normal event handling flow. |
| [int32\_t OH\_ArkUI\_XComponent\_StartImageAnalyzer(ArkUI\_NodeHandle node, void\* userData, void (\*callback)(ArkUI\_NodeHandle node, ArkUI\_XComponent\_ImageAnalyzerState statusCode, void\* userData))](#oh_arkui_xcomponent_startimageanalyzer) | Starts AI image analysis for this XComponent instance. Before calling this API, make sure the AI image analyzer is enabled. |
| [int32\_t OH\_ArkUI\_XComponent\_StopImageAnalyzer(ArkUI\_NodeHandle node)](#oh_arkui_xcomponent_stopimageanalyzer) | Stops AI image analysis for this XComponent instance. |
| [OH\_ArkUI\_SurfaceHolder\* OH\_ArkUI\_SurfaceHolder\_Create(ArkUI\_NodeHandle node)](#oh_arkui_surfaceholder_create) | Creates an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) object for an **XComponent**. |
| [void OH\_ArkUI\_SurfaceHolder\_Dispose(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](#oh_arkui_surfaceholder_dispose) | Disposes of an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) object. |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_SetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, void\* userData)](#oh_arkui_surfaceholder_setuserdata) | Stores custom data in an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [void\* OH\_ArkUI\_SurfaceHolder\_GetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](#oh_arkui_surfaceholder_getuserdata) | Obtains the custom data stored in an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [OH\_ArkUI\_SurfaceCallback\* OH\_ArkUI\_SurfaceCallback\_Create()](#oh_arkui_surfacecallback_create) | Creates an [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) object. |
| [void OH\_ArkUI\_SurfaceCallback\_Dispose(OH\_ArkUI\_SurfaceCallback\* callback)](#oh_arkui_surfacecallback_dispose) | Disposes of an [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) object. |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](#oh_arkui_surfacecallback_setsurfacecreatedevent) | Sets the creation callback event in the surface lifecycle callbacks. |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height))](#oh_arkui_surfacecallback_setsurfacechangedevent) | Sets the size change callback event in the surface lifecycle callbacks. |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](#oh_arkui_surfacecallback_setsurfacedestroyedevent) | Sets the destruction callback event in the surface lifecycle callbacks. |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)](#oh_arkui_surfaceholder_addsurfacecallback) | Adds a surface lifecycle callback to an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)](#oh_arkui_surfaceholder_removesurfacecallback) | Removes a previously added surface lifecycle callback from an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [OHNativeWindow\* OH\_ArkUI\_XComponent\_GetNativeWindow(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)](#oh_arkui_xcomponent_getnativewindow) | Obtains the **NativeWindow** instance associated with an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [int32\_t OH\_ArkUI\_XComponent\_SetAutoInitialize(ArkUI\_NodeHandle node, bool autoInitialize)](#oh_arkui_xcomponent_setautoinitialize) | Sets whether the **XComponent** component needs to automatically initialize the surface. |
| [int32\_t OH\_ArkUI\_XComponent\_Initialize(ArkUI\_NodeHandle node)](#oh_arkui_xcomponent_initialize) | Initializes the surface held by the **XComponent** component. |
| [int32\_t OH\_ArkUI\_XComponent\_Finalize(ArkUI\_NodeHandle node)](#oh_arkui_xcomponent_finalize) | Destroys the surface held by the **XComponent** component. |
| [int32\_t OH\_ArkUI\_XComponent\_IsInitialized(ArkUI\_NodeHandle node, bool\* isInitialized)](#oh_arkui_xcomponent_isinitialized) | Checks whether the surface held by the **XComponent** component is initialized. |
| [int32\_t OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange(ArkUI\_NodeHandle node, OH\_NativeXComponent\_ExpectedRateRange range)](#oh_arkui_xcomponent_setexpectedframeraterange) | Sets the expected frame rate range for the XComponent. |
| [int32\_t OH\_ArkUI\_XComponent\_RegisterOnFrameCallback(ArkUI\_NodeHandle node,void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp))](#oh_arkui_xcomponent_registeronframecallback) | Registers a frame callback function for the XComponent. |
| [int32\_t OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback(ArkUI\_NodeHandle node)](#oh_arkui_xcomponent_unregisteronframecallback) | Unregisters the frame callback function for the XComponent. |
| [int32\_t OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard(ArkUI\_NodeHandle node, bool needSoftKeyboard)](#oh_arkui_xcomponent_setneedsoftkeyboard) | Sets whether the soft keyboard is required for the XComponent. |
| [ArkUI\_AccessibilityProvider\* OH\_ArkUI\_AccessibilityProvider\_Create(ArkUI\_NodeHandle node)](#oh_arkui_accessibilityprovider_create) | Creates an [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance for this **XComponent** instance. |
| [void OH\_ArkUI\_AccessibilityProvider\_Dispose(ArkUI\_AccessibilityProvider\* provider)](#oh_arkui_accessibilityprovider_dispose) | Disposes of the [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance created using [OH\_ArkUI\_AccessibilityProvider\_Create](#oh_arkui_accessibilityprovider_create). |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceShow)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](#oh_arkui_surfacecallback_setsurfaceshowevent) | Sets a surface display callback for this [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. This callback is invoked when the application window has moved from the background to the foreground. |
| [void OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent(OH\_ArkUI\_SurfaceCallback\* callback, void (\*onSurfaceHide)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))](#oh_arkui_surfacecallback_setsurfacehideevent) | Sets a surface hiding callback for this [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. This callback is invoked when the application window has moved from the foreground to the background. |
| [ArkUI\_XComponentSurfaceConfig\* OH\_ArkUI\_XComponentSurfaceConfig\_Create()](#oh_arkui_xcomponentsurfaceconfig_create) | Creates an [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object for an **XComponent**. |
| [void OH\_ArkUI\_XComponentSurfaceConfig\_Dispose(ArkUI\_XComponentSurfaceConfig\* config)](#oh_arkui_xcomponentsurfaceconfig_dispose) | Disposes of an [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object. |
| [void OH\_ArkUI\_XComponentSurfaceConfig\_SetIsOpaque(ArkUI\_XComponentSurfaceConfig\* config, bool isOpaque)](#oh_arkui_xcomponentsurfaceconfig_setisopaque) | Sets whether the surface held by the **XComponent** should be treated as opaque during rendering, regardless of the actual pixel transparency. |
| [int32\_t OH\_ArkUI\_SurfaceHolder\_SetSurfaceConfig(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, ArkUI\_XComponentSurfaceConfig \*config)](#oh_arkui_surfaceholder_setsurfaceconfig) | Sets the surface configuration for the [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const uint32\_t OH\_XCOMPONENT\_ID\_LEN\_MAX = 128 | 
Maximum length of the ArkUI XComponent ID.

**Since**: 8

 |
| const uint32\_t OH\_MAX\_TOUCH\_POINTS\_NUMBER = 10 | 

Maximum number of identifiable touch points in a touch event.

**Since**: 8

 |
| OH\_NATIVE\_XCOMPONENT\_MAX\_TOUCH\_POINTS\_NUMBER 10 | 

Maximum number of supported touch points.

**Since**: 8

 |

#### Enum Description

#### \[h2\]anonymous

enum anonymous

**Description**

Enumerates the API access states.

**Since**: 8

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS = 0 | Success. |
| OH\_NATIVEXCOMPONENT\_RESULT\_FAILED = -1 | Failure. |
| OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER = -2 | Invalid parameter. |

#### \[h2\]ArkUI\_XComponent\_ImageAnalyzerState

enum ArkUI\_XComponent\_ImageAnalyzerState

**Description**

Enumerates the AI image analyzer error codes of the XComponent.

**Since**: 18

| Value | Description |
| :-- | :-- |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_FINISHED = 0 | AI image analysis is complete. |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_DISABLED = 110000 | AI image analysis is disabled. |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_UNSUPPORTED = 110001 | The device does not support AI image analysis. |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_ONGOING = 110002 | AI image analysis is in progress. |
| ARKUI\_XCOMPONENT\_AI\_ANALYSIS\_STOPPED = 110003 | AI image analysis has been stopped. |

#### \[h2\]OH\_NativeXComponent\_TouchEventType

enum OH\_NativeXComponent\_TouchEventType

**Description**

Enumerates the touch event types.

**Since**: 8

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_DOWN = 0 | The touch event is triggered when a finger is pressed. |
| OH\_NATIVEXCOMPONENT\_UP = 1 | The touch event is triggered when a finger is lifted. |
| OH\_NATIVEXCOMPONENT\_MOVE = 2 | The touch event is triggered when a finger is moved on the screen. |
| OH\_NATIVEXCOMPONENT\_CANCEL = 3 | The event is triggered when a touch event is canceled. |
| OH\_NATIVEXCOMPONENT\_UNKNOWN = 4 | Invalid touch type. |

#### \[h2\]OH\_NativeXComponent\_TouchPointToolType

enum OH\_NativeXComponent\_TouchPointToolType

**Description**

Enumerates the touch point tool types.

**Since**: 9

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_UNKNOWN = 0 | Unknown tool type. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_FINGER = 1 | Finger. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_PEN = 2 | Stylus. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_RUBBER = 3 | Rubber. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_BRUSH = 4 | Brush. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_PENCIL = 5 | Pencil. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_AIRBRUSH = 6 | Air brush. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_MOUSE = 7 | Mouse. |
| OH\_NATIVEXCOMPONENT\_TOOL\_TYPE\_LENS = 8 | Lens. |

#### \[h2\]OH\_NativeXComponent\_EventSourceType

enum OH\_NativeXComponent\_EventSourceType

**Description**

Enumerates the touch event source types.

**Since**: 9

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_UNKNOWN = 0 | Unknown source type. |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_MOUSE = 1 | Source that generates a mouse multi-click event. |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_TOUCHSCREEN = 2 | Source that generates a touchscreen multitouch event. |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_TOUCHPAD = 3 | Source that generates a touchpad multitouch event. |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_JOYSTICK = 4 | Source that generates a joystick multitouch event. |
| OH\_NATIVEXCOMPONENT\_SOURCE\_TYPE\_KEYBOARD = 5 | 
Source that generates a key event.

**Since**: 10

 |

#### \[h2\]OH\_NativeXComponent\_MouseEventAction

enum OH\_NativeXComponent\_MouseEventAction

**Description**

Enumerates the mouse event actions.

**Since**: 9

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_MOUSE\_NONE = 0 | Invalid mouse event. |
| OH\_NATIVEXCOMPONENT\_MOUSE\_PRESS = 1 | Mouse button press. |
| OH\_NATIVEXCOMPONENT\_MOUSE\_RELEASE = 2 | Mouse button release. |
| OH\_NATIVEXCOMPONENT\_MOUSE\_MOVE = 3 | Mouse movement. |
| OH\_NATIVEXCOMPONENT\_MOUSE\_CANCEL = 4 | 
Mouse button canceling.

**Since**: 18

Note: Mouse button canceling is typically triggered in the following scenarios:

1\. Component focus loss: A currently focused **XComponent** loses focus due to a system event (such as pop-up interruption or app switching).

2\. Event interruption: During a mouse operation, a higher-priority event occurs (such as a system-level gesture or forced event stream recycling), causing the current mouse operation to be forcibly terminated.

3\. Abnormal state exit: In scenarios such as component destruction or abnormal rendering environment, unfinished mouse events are marked as canceled.

 |

#### \[h2\]OH\_NativeXComponent\_MouseEventButton

enum OH\_NativeXComponent\_MouseEventButton

**Description**

Enumerates the mouse event buttons.

**Since**: 9

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_NONE\_BUTTON = 0 | No button. |
| OH\_NATIVEXCOMPONENT\_LEFT\_BUTTON = 0x01 | Left mouse button. |
| OH\_NATIVEXCOMPONENT\_RIGHT\_BUTTON = 0x02 | Right mouse button. |
| OH\_NATIVEXCOMPONENT\_MIDDLE\_BUTTON = 0x04 | Middle mouse button. |
| OH\_NATIVEXCOMPONENT\_BACK\_BUTTON = 0x08 | Back button on the left of the mouse. |
| OH\_NATIVEXCOMPONENT\_FORWARD\_BUTTON = 0x10 | Forward key on the left of the mouse. |

#### \[h2\]OH\_NativeXComponent\_TouchEvent\_SourceTool

enum OH\_NativeXComponent\_TouchEvent\_SourceTool

**Description**

Enumerates the source tool types of touch events.

**Since**: 10

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_UNKNOWN = 0 | Unknown source tool. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_FINGER = 1 | Finger. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_PEN = 2 | Pen. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_RUBBER = 3 | Eraser. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_BRUSH = 4 | Brush. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_PENCIL = 5 | Pencil. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_AIRBRUSH = 6 | Airbrush. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_MOUSE = 7 | Mouse pointer. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_LENS = 8 | Lens. |
| OH\_NATIVEXCOMPONENT\_SOURCETOOL\_TOUCHPAD = 9 | Touchpad. |

#### Function Description

#### \[h2\]OH\_NativeXComponent\_GetXComponentId()

int32\_t OH\_NativeXComponent\_GetXComponentId(OH\_NativeXComponent\* component, char\* id, uint64\_t\* size)

**Description**

Obtains the ID of ArkUI XComponent.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| char\* id | Pointer to the character buffer for storing the ID of the [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. Note that null terminators will be attached to the character buffer, so the size of the character buffer should be at least one unit greater than the length of the real ID. The recommended size is \[[OH\_XCOMPONENT\_ID\_LEN\_MAX](#variables) + 1\]. |
| uint64\_t\* size | Pointer to the length of the ID, used to receive the length information of the ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetXComponentSize()

int32\_t OH\_NativeXComponent\_GetXComponentSize(OH\_NativeXComponent\* component, const void\* window, uint64\_t\* width, uint64\_t\* height)

**Description**

Obtains the size of the surface held by the ArkUI XComponent.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| const void\* window | Handle to the **NativeWindow** instance. |
| uint64\_t\* width | Pointer to the width of the current surface. Unit: vp. |
| uint64\_t\* height | Pointer to the height of the current surface. Unit: vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetXComponentOffset()

int32\_t OH\_NativeXComponent\_GetXComponentOffset(OH\_NativeXComponent\* component, const void\* window, double\* x, double\* y)

**Description**

Obtains the offset of the surface held by the XComponent relative to the upper left corner of its parent component.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| const void\* window | Handle to the **NativeWindow** instance. |
| double\* x | Pointer to the x-coordinate of the current surface relative to the upper left corner of the **XComponent**'s parent component. Unit: vp. |
| double\* y | Pointer to the y-coordinate of the current surface relative to the upper left corner of the **XComponent**'s parent component. Unit: vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchEvent()

int32\_t OH\_NativeXComponent\_GetTouchEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_TouchEvent\* touchEvent)

**Description**

Obtains the touch event scheduled by the ArkUI XComponent.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| const void\* window | Handle to the **NativeWindow** instance. |
| [OH\_NativeXComponent\_TouchEvent](../../structs/oh-nativexcomponent-touchevent/document.md)\* touchEvent | Pointer to the current touch event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointToolType()

int32\_t OH\_NativeXComponent\_GetTouchPointToolType(OH\_NativeXComponent\* component, uint32\_t pointIndex,OH\_NativeXComponent\_TouchPointToolType\* toolType)

**Description**

Obtains the ArkUI XComponent touch point tool type.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| [OH\_NativeXComponent\_TouchPointToolType](#oh_nativexcomponent_touchpointtooltype)\* toolType | Pointer to the tool type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointTiltX()

int32\_t OH\_NativeXComponent\_GetTouchPointTiltX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltX)

**Description**

Obtains the angle between the Y-Z plane of the ArkUI XComponent touch point and the x-axis.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* tiltX | Pointer to the angle between the Y-Z plane of the touch point and the x-axis. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointTiltY()

int32\_t OH\_NativeXComponent\_GetTouchPointTiltY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* tiltY)

**Description**

Obtains the angle between the X-Z plane of the ArkUI XComponent touch point and the y-axis.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* tiltY | Pointer to the angle between the X-Z plane of the touch point and the y-axis. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointWindowX()

int32\_t OH\_NativeXComponent\_GetTouchPointWindowX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowX)

**Description**

Obtains the x-coordinate of the touch point relative to the upper left corner of the application window where the ArkUI XComponent is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* windowX | Pointer to the x-coordinate of the touch point relative to the upper left corner of the application window. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if the component, windowX, or native XComponent is a null pointer.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointWindowY()

int32\_t OH\_NativeXComponent\_GetTouchPointWindowY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* windowY)

**Description**

Obtains the y-coordinate of the touch point relative to the upper left corner of the application window where the ArkUI XComponent is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* windowY | Pointer to the y-coordinate of the touch point relative to the upper left corner of the application window. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if the component, windowY, or native XComponent is a null pointer.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointDisplayX()

int32\_t OH\_NativeXComponent\_GetTouchPointDisplayX(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayX)

**Description**

Obtains the x-coordinate of the touch point relative to the upper left corner of the screen where the ArkUI XComponent is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* displayX | Pointer to the x-coordinate of the touch point relative to the upper left corner of the screen. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if the component, displayX, or native XComponent is a null pointer.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchPointDisplayY()

int32\_t OH\_NativeXComponent\_GetTouchPointDisplayY(OH\_NativeXComponent\* component, uint32\_t pointIndex, float\* displayY)

**Description**

Obtains the y-coordinate of the touch point relative to the upper left corner of the screen where the ArkUI XComponent is located.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| uint32\_t pointIndex | Pointer to the index of the touch point. |
| float\* displayY | Pointer to the y-coordinate of the touch point relative to the upper left corner of the screen. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if the component, displayY, or native XComponent is a null pointer.

 |

#### \[h2\]OH\_NativeXComponent\_GetHistoricalPoints()

int32\_t OH\_NativeXComponent\_GetHistoricalPoints(OH\_NativeXComponent\* component, const void\* window,int32\_t\* size, OH\_NativeXComponent\_HistoricalPoint\*\* historicalPoints)

**Description**

Obtains the historical touch point data for the touch event of an **OH\_NativeXComponent** instance. Some input devices report touch points at very high frequencies (up to 1 ms intervals). However, since UI updates typically do not require such high-frequency updates, the system consolidates touch events and reports them once per frame. All touch points collected during the current frame are preserved as historical touch points for applications that need direct access to this raw data.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| const void\* window | Handle to the **NativeWindow** instance. |
| int32\_t\* size | Length of the historical touch point array. |
| [OH\_NativeXComponent\_HistoricalPoint](../../structs/oh-nativexcomponent-historicalpoint/document.md)\*\* historicalPoints | Pointer to the historical touch point array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetMouseEvent()

int32\_t OH\_NativeXComponent\_GetMouseEvent(OH\_NativeXComponent\* component, const void\* window, OH\_NativeXComponent\_MouseEvent\* mouseEvent)

**Description**

Obtains the mouse event scheduled by the ArkUI XComponent.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| const void\* window | Handle to the **NativeWindow** instance. |
| [OH\_NativeXComponent\_MouseEvent](../../structs/oh-nativexcomponent-mouseevent/document.md)\* mouseEvent | Pointer to the current mouse event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterCallback()

int32\_t OH\_NativeXComponent\_RegisterCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_Callback\* callback)

**Description**

Registers a callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [OH\_NativeXComponent\_Callback](../../structs/oh-nativexcomponent-callback/document.md)\* callback | Pointer to the surface lifecycle and touch event callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterMouseEventCallback()

int32\_t OH\_NativeXComponent\_RegisterMouseEventCallback(OH\_NativeXComponent\* component, OH\_NativeXComponent\_MouseEvent\_Callback\* callback)

**Description**

Registers a mouse event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [OH\_NativeXComponent\_MouseEvent\_Callback](../../structs/oh-nativexcomponent-mouseevent-callback/document.md)\* callback | Pointer to the mouse event callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetExtraMouseEventInfo()

int32\_t OH\_NativeXComponent\_GetExtraMouseEventInfo(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExtraMouseEventInfo\*\* extraMouseEventInfo)

**Description**

Obtains extended mouse event information from this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md)\*\* extraMouseEventInfo | Address of a pointer to the [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md) type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetMouseEventModifierKeyStates()

int32\_t OH\_NativeXComponent\_GetMouseEventModifierKeyStates(OH\_NativeXComponent\_ExtraMouseEventInfo\* extraMouseEventInfo, uint64\_t\* keys)

**Description**

Obtains the state of modifier keys from an [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_ExtraMouseEventInfo](../../structs/oh-nativexcomponent-extramouseeventinfo/document.md)\* extraMouseEventInfo | Pointer to the extended mouse event information instance. |
| uint64\_t\* keys | Address of a 64-bit unsigned integer to receive the modifier key press state information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterFocusEventCallback()

int32\_t OH\_NativeXComponent\_RegisterFocusEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a focus event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the focus event callback. - **window**: handle to the **NativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterKeyEventCallback()

int32\_t OH\_NativeXComponent\_RegisterKeyEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a key event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the key event callback. - **window**: handle to the **NativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterBlurEventCallback()

int32\_t OH\_NativeXComponent\_RegisterBlurEventCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a blur event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the blur event callback. - **window**: handle to the **NativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEvent()

int32\_t OH\_NativeXComponent\_GetKeyEvent(OH\_NativeXComponent\* component, OH\_NativeXComponent\_KeyEvent\*\* keyEvent)

**Description**

Obtains the key event scheduled by the ArkUI XComponent.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\*\* keyEvent | Pointer to the current key event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventAction()

int32\_t OH\_NativeXComponent\_GetKeyEventAction(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyAction\* action)

**Description**

Obtains the action of the specified key event.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to an [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) instance. |
| [OH\_NativeXComponent\_KeyAction](../native-xcomponent-key-event-h/document.md#oh_nativexcomponent_keyaction)\* action | Pointer to the key event action. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventCode()

int32\_t OH\_NativeXComponent\_GetKeyEventCode(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_KeyCode\* code)

**Description**

Obtains the key code of the specified key event.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to an [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) instance. |
| [OH\_NativeXComponent\_KeyCode](../native-xcomponent-key-event-h/document.md#oh_nativexcomponent_keycode)\* code | Pointer to the key code of the key event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventSourceType()

int32\_t OH\_NativeXComponent\_GetKeyEventSourceType(OH\_NativeXComponent\_KeyEvent\* keyEvent, OH\_NativeXComponent\_EventSourceType\* sourceType)

**Description**

Obtains the source type of the specified key event.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to an [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) instance. |
| [OH\_NativeXComponent\_EventSourceType](#oh_nativexcomponent_eventsourcetype)\* sourceType | Pointer to the source type of the key event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventDeviceId()

int32\_t OH\_NativeXComponent\_GetKeyEventDeviceId(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* deviceId)

**Description**

Obtains the device ID of the specified key event.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to an [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) instance. |
| int64\_t\* deviceId | Pointer to the device ID of the key event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventTimestamp()

int32\_t OH\_NativeXComponent\_GetKeyEventTimestamp(OH\_NativeXComponent\_KeyEvent\* keyEvent, int64\_t\* timestamp)

**Description**

Obtains the timestamp of the specified key event.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to an [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md) instance. |
| int64\_t\* timestamp | Pointer to the timestamp of the key event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventModifierKeyStates()

int32\_t OH\_NativeXComponent\_GetKeyEventModifierKeyStates(OH\_NativeXComponent\_KeyEvent\* keyEvent, uint64\_t\* keys)

**Description**

Obtains the state of modifier keys from a key event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to the key event. |
| uint64\_t\* keys | Address of a 64-bit unsigned integer to receive the modifier key press state information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventNumLockState()

int32\_t OH\_NativeXComponent\_GetKeyEventNumLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isNumLockOn)

**Description**

Obtains the state of the NumLock key from a key event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to the key event. |
| bool\* isNumLockOn | Pointer to a boolean variable to receive the state of the NumLock key. **true**: NumLock is enabled. **false**: NumLock is disabled. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventCapsLockState()

int32\_t OH\_NativeXComponent\_GetKeyEventCapsLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isCapsLockOn)

**Description**

Obtains the state of the CapsLock key from a key event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to the key event. |
| bool\* isCapsLockOn | Pointer to a boolean variable to receive the state of the CapsLock key. **true**: CapsLock is enabled. **false**: CapsLock is disabled. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetKeyEventScrollLockState()

int32\_t OH\_NativeXComponent\_GetKeyEventScrollLockState(OH\_NativeXComponent\_KeyEvent\* keyEvent, bool\* isScrollLockOn)

**Description**

Obtains the state of the ScrollLock key from a key event.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent\_KeyEvent](../../structs/oh-nativexcomponent-keyevent/document.md)\* keyEvent | Pointer to the key event. |
| bool\* isScrollLockOn | Pointer to a boolean variable to receive the state of the ScrollLock key. **true**: ScrollLock is enabled. **false**: ScrollLock is disabled. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_SetExpectedFrameRateRange()

int32\_t OH\_NativeXComponent\_SetExpectedFrameRateRange(OH\_NativeXComponent\* component, OH\_NativeXComponent\_ExpectedRateRange\* range)

**Description**

Sets the expected frame rate range.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [OH\_NativeXComponent\_ExpectedRateRange](../../structs/oh-nativexcomponent-expectedraterange/document.md)\* range | Pointer to the expected frame rate information object of the [OH\_NativeXComponent\_ExpectedRateRange](../../structs/oh-nativexcomponent-expectedraterange/document.md) type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterOnFrameCallback()

int32\_t OH\_NativeXComponent\_RegisterOnFrameCallback(OH\_NativeXComponent\* component,void (\*callback)(OH\_NativeXComponent\* component, uint64\_t timestamp, uint64\_t targetTimestamp))

**Description**

Registers the display update callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables the callback for each frame.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, uint64\_t timestamp, uint64\_t targetTimestamp) | Pointer to the display update callback. - **timestamp**: time when the current frame arrives, in nanoseconds. - **targetTimestamp**: expected arrival time of the next frame, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_UnregisterOnFrameCallback()

int32\_t OH\_NativeXComponent\_UnregisterOnFrameCallback(OH\_NativeXComponent\* component)

**Description**

Deregisters the display update callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and disables the callback for each frame.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_AttachNativeRootNode()

int32\_t OH\_NativeXComponent\_AttachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)

**Description**

Attaches the UI component created through the native API of ArkUI to this **OH\_NativeXComponent** instance.

**Since**: 12

**Deprecated from**: 20

**Substitute**: [OH\_ArkUI\_NodeContent\_AddNode](../native-node-h/document.md#oh_arkui_nodecontent_addnode)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) root | Pointer to the component instance created through the native API. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_DetachNativeRootNode()

int32\_t OH\_NativeXComponent\_DetachNativeRootNode(OH\_NativeXComponent\* component, ArkUI\_NodeHandle root)

**Description**

Detaches the native component of ArkUI from this **OH\_NativeXComponent** instance.

**Since**: 12

**Deprecated from**: 20

**Substitute**: [OH\_ArkUI\_NodeContent\_RemoveNode](../native-node-h/document.md#oh_arkui_nodecontent_removenode)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) root | Pointer to the component instance created through the native API. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterUIInputEventCallback()

int32\_t OH\_NativeXComponent\_RegisterUIInputEventCallback(OH\_NativeXComponent \*component,void (\*callback)(OH\_NativeXComponent \*component, ArkUI\_UIInputEvent \*event,ArkUI\_UIInputEvent\_Type type),ArkUI\_UIInputEvent\_Type type)

**Description**

Registers a UI input event callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables this callback to be invoked when a UI input event is received. Currently, only axis events are supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) \*component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent \*component, ArkUI\_UIInputEvent \*event,ArkUI\_UIInputEvent\_Type type) | Pointer to the UI input event callback. - **event**: pointer to the UI input event. |
| [ArkUI\_UIInputEvent\_Type](../ui-input-event-h/document.md#arkui_uiinputevent_type) type | Type of the current UI input event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterOnTouchInterceptCallback()

int32\_t OH\_NativeXComponent\_RegisterOnTouchInterceptCallback(OH\_NativeXComponent\* component, HitTestMode (\*callback)(OH\_NativeXComponent\* component, ArkUI\_UIInputEvent\* event))

**Description**

Registers a custom event intercept callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance and enables this callback to be invoked during hit testing. UI input–related operations are not supported on event objects received through this callback. For full functionality, use the [NODE\_ON\_TOUCH\_INTERCEPT](../native-node-h/document.md#arkui_nodeeventtype) event on native nodes instead.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| HitTestMode (\*callback)(OH\_NativeXComponent\* component, ArkUI\_UIInputEvent\* event) | Pointer to the custom event intercept callback. - **event**: pointer to the UI input event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_SetNeedSoftKeyboard()

int32\_t OH\_NativeXComponent\_SetNeedSoftKeyboard(OH\_NativeXComponent\* component, bool needSoftKeyboard)

**Description**

Sets whether the soft keyboard is required for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| bool needSoftKeyboard | Whether the soft keyboard is required for the current [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. **true** if the soft keyboard is required, **false** otherwise. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterSurfaceShowCallback()

int32\_t OH\_NativeXComponent\_RegisterSurfaceShowCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a surface display callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. This callback is invoked after the application is switched to the foreground.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the surface display callback. - **window**: handle to the **NativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterSurfaceHideCallback()

int32\_t OH\_NativeXComponent\_RegisterSurfaceHideCallback(OH\_NativeXComponent\* component, void (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a surface hiding callback for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. This callback is invoked after the application is switched to the background.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| void (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the surface hiding callback. - **window**: handle to the **NativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetTouchEventSourceType()

int32\_t OH\_NativeXComponent\_GetTouchEventSourceType(OH\_NativeXComponent\* component, int32\_t pointId, OH\_NativeXComponent\_EventSourceType\* sourceType)

**Description**

Obtains the touch event source type of an ArkUI XComponent instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| int32\_t pointId | ID of the touch point. The touch event source type can be correctly returned only when the ID passed in is the ID of the touch point that triggers the touch event. Otherwise, **OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER** is returned. |
| [OH\_NativeXComponent\_EventSourceType](#oh_nativexcomponent_eventsourcetype)\* sourceType | Pointer to the touch event source type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_FAILED](#anonymous) if any other error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_GetNativeXComponent()

OH\_NativeXComponent\* OH\_NativeXComponent\_GetNativeXComponent(ArkUI\_NodeHandle node)

**Description**

Obtains a pointer of the [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) type based on the specified component instance created by the native API.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the component instance created through the native API. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |

#### \[h2\]OH\_NativeXComponent\_GetNativeAccessibilityProvider()

int32\_t OH\_NativeXComponent\_GetNativeAccessibilityProvider(OH\_NativeXComponent\* component, ArkUI\_AccessibilityProvider\*\* handle)

**Description**

Obtains the accessibility provider handle for an ArkUI XComponent.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\*\* handle | Pointer to an [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_FAILED](#anonymous) if any other error occurs.

 |

#### \[h2\]OH\_NativeXComponent\_RegisterKeyEventCallbackWithResult()

int32\_t OH\_NativeXComponent\_RegisterKeyEventCallbackWithResult(OH\_NativeXComponent\* component, bool (\*callback)(OH\_NativeXComponent\* component, void\* window))

**Description**

Registers a key event callback with a return value for this [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. The callback must return a result (**true** or **false**). If the callback returns **true**, the event will not be further propagated. If it returns **false**, the event will continue to be processed according to the normal event handling flow.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md)\* component | Pointer to an [OH\_NativeXComponent](../../structs/oh-nativexcomponent/document.md) instance. |
| bool (\*callback)(OH\_NativeXComponent\* component, void\* window) | Pointer to the key event callback. - **window**: handle to the **NativeWindow** instance. If the callback returns **true**, the event will not be further propagated. If it returns **false**, the event will continue to be processed according to the normal event handling flow. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS](#anonymous) if the operation is successful.

Returns [OH\_NATIVEXCOMPONENT\_RESULT\_BAD\_PARAMETER](#anonymous) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_StartImageAnalyzer()

int32\_t OH\_ArkUI\_XComponent\_StartImageAnalyzer(ArkUI\_NodeHandle node, void\* userData,void (\*callback)(ArkUI\_NodeHandle node, ArkUI\_XComponent\_ImageAnalyzerState statusCode, void\* userData))

**Description**

Starts AI image analysis for this XComponent instance. Before calling this API, make sure the AI image analyzer is enabled.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |
| void\* userData | Pointer to the data that you need to obtain when the callback function is executed. |
| void (\*callback)(ArkUI\_NodeHandle node, ArkUI\_XComponent\_ImageAnalyzerState statusCode, void\* userData) | Callback function triggered when the AI image analysis status is updated. - **statusCode**: one of the input parameters of the callback function, indicating the current image analysis status. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_StopImageAnalyzer()

int32\_t OH\_ArkUI\_XComponent\_StopImageAnalyzer(ArkUI\_NodeHandle node)

**Description**

Stops AI image analysis for this XComponent instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_Create()

OH\_ArkUI\_SurfaceHolder\* OH\_ArkUI\_SurfaceHolder\_Create(ArkUI\_NodeHandle node)

**Description**

Creates an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) object for an **XComponent**.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the XComponent instance created through the native API. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* | Pointer to the created [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) object. |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_Dispose()

void OH\_ArkUI\_SurfaceHolder\_Dispose(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)

**Description**

Disposes of an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) object.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_SetUserData()

int32\_t OH\_ArkUI\_SurfaceHolder\_SetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, void\* userData)

**Description**

Stores custom data in an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| void\* userData | Pointer to the custom data to be stored. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_GetUserData()

void\* OH\_ArkUI\_SurfaceHolder\_GetUserData(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)

**Description**

Obtains the custom data stored in an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Custom data. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_Create()

OH\_ArkUI\_SurfaceCallback\* OH\_ArkUI\_SurfaceCallback\_Create()

**Description**

Creates an [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) object.

**Since**: 19

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* | Pointer to the created [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) object. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_Dispose()

void OH\_ArkUI\_SurfaceCallback\_Dispose(OH\_ArkUI\_SurfaceCallback\* callback)

**Description**

Disposes of an [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) object.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the target [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent()

void OH\_ArkUI\_SurfaceCallback\_SetSurfaceCreatedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))

**Description**

Sets the creation callback event in the surface lifecycle callbacks.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the surface lifecycle callback. |
| void (\*onSurfaceCreated)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | Callback event triggered when the surface is created. - **surfaceHolder**: pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent()

void OH\_ArkUI\_SurfaceCallback\_SetSurfaceChangedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height))

**Description**

Sets the size change callback event in the surface lifecycle callbacks.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the surface lifecycle callback. |
| void (\*onSurfaceChanged)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, uint64\_t width, uint64\_t height) | Callback event triggered when the surface size changes. - **surfaceHolder**: pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. - **width**: new width of the surface after the size change. Unit: vp. - **height**: new height of the surface after the size change. Unit: vp. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent()

void OH\_ArkUI\_SurfaceCallback\_SetSurfaceDestroyedEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))

**Description**

Sets the destruction callback event in the surface lifecycle callbacks.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the surface lifecycle callback. |
| void (\*onSurfaceDestroyed)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder) | Callback event triggered when the surface is destroyed. - **surfaceHolder**: pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback()

int32\_t OH\_ArkUI\_SurfaceHolder\_AddSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)

**Description**

Adds a surface lifecycle callback to an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the new callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback()

int32\_t OH\_ArkUI\_SurfaceHolder\_RemoveSurfaceCallback(OH\_ArkUI\_SurfaceHolder\* surfaceHolder,OH\_ArkUI\_SurfaceCallback\* callback)

**Description**

Removes a previously added surface lifecycle callback from an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the callback to be removed. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_GetNativeWindow()

OHNativeWindow\* OH\_ArkUI\_XComponent\_GetNativeWindow(OH\_ArkUI\_SurfaceHolder\* surfaceHolder)

**Description**

Obtains the **NativeWindow** instance associated with an [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NativeWindow](../../structs/ohnativewindow/document.md)\* | **NativeWindow** instance associated with the [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_XComponent\_SetAutoInitialize()

int32\_t OH\_ArkUI\_XComponent\_SetAutoInitialize(ArkUI\_NodeHandle node, bool autoInitialize)

**Description**

Sets whether the **XComponent** component needs to automatically initialize the surface.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the **XComponent** component instance. |
| bool autoInitialize | 
Whether the **XComponent** component needs to automatically initialize the surface. If **autoInitialize** is **true**, the **OnSurfaceCreated** callback will be triggered when the component is attached to the tree, and the **OnSurfaceDestroyed** callback will be triggered when the component is detached from the tree. If the value is **false**, the component does not need to automatically initialize the surface.

The default value of **autoInitialize** is **true**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_Initialize()

int32\_t OH\_ArkUI\_XComponent\_Initialize(ArkUI\_NodeHandle node)

**Description**

Initializes the surface held by the **XComponent** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the **XComponent** component instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID](../native-type-h/document.md#arkui_errorcode) if the surface held by the **XComponent** component has been initialized.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_Finalize()

int32\_t OH\_ArkUI\_XComponent\_Finalize(ArkUI\_NodeHandle node)

**Description**

Destroys the surface held by the **XComponent** component.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the **XComponent** component instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

Returns [ARKUI\_ERROR\_CODE\_XCOMPONENT\_STATE\_INVALID](../native-type-h/document.md#arkui_errorcode) if the surface held by the **XComponent** component has been destroyed.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_IsInitialized()

int32\_t OH\_ArkUI\_XComponent\_IsInitialized(ArkUI\_NodeHandle node, bool\* isInitialized)

**Description**

Checks whether the surface held by the **XComponent** component is initialized.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Pointer to the **XComponent** component instance. |
| bool\* isInitialized | Whether the surface held by the **XComponent** component is initialized. **true**: The surface is initialized. **false**: The surface is not initialized. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange()

int32\_t OH\_ArkUI\_XComponent\_SetExpectedFrameRateRange(ArkUI\_NodeHandle node, OH\_NativeXComponent\_ExpectedRateRange range)

**Description**

Sets the expected frame rate range for the XComponent.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |
| [OH\_NativeXComponent\_ExpectedRateRange](../../structs/oh-nativexcomponent-expectedraterange/document.md) range | Expected frame rate information object of the [OH\_NativeXComponent\_ExpectedRateRange](../../structs/oh-nativexcomponent-expectedraterange/document.md) type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_RegisterOnFrameCallback()

int32\_t OH\_ArkUI\_XComponent\_RegisterOnFrameCallback(ArkUI\_NodeHandle node,void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp))

**Description**

Registers a frame callback function for the XComponent.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |
| void (\*callback)(ArkUI\_NodeHandle node, uint64\_t timestamp, uint64\_t targetTimestamp) | Pointer to the frame callback function. - **timestamp**: time when the current frame arrives, in nanoseconds. - **targetTimestamp**: expected arrival time of the next frame, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback()

int32\_t OH\_ArkUI\_XComponent\_UnregisterOnFrameCallback(ArkUI\_NodeHandle node)

**Description**

Unregisters the frame callback function for the XComponent.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard()

int32\_t OH\_ArkUI\_XComponent\_SetNeedSoftKeyboard(ArkUI\_NodeHandle node, bool needSoftKeyboard)

**Description**

Sets whether the soft keyboard is required for the XComponent.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |
| bool needSoftKeyboard | Whether the soft keyboard is required. **true** if the soft keyboard is required, **false** otherwise. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityProvider\_Create()

ArkUI\_AccessibilityProvider\* OH\_ArkUI\_AccessibilityProvider\_Create(ArkUI\_NodeHandle node)

**Description**

Creates an [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance for this **XComponent** instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | XComponent instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\* | Pointer of the [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) type. |

#### \[h2\]OH\_ArkUI\_AccessibilityProvider\_Dispose()

void OH\_ArkUI\_AccessibilityProvider\_Dispose(ArkUI\_AccessibilityProvider\* provider)

**Description**

Disposes of the [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance created using [OH\_ArkUI\_AccessibilityProvider\_Create](#oh_arkui_accessibilityprovider_create).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\* provider | [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) instance created using [OH\_ArkUI\_AccessibilityProvider\_Create](#oh_arkui_accessibilityprovider_create). |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent()

void OH\_ArkUI\_SurfaceCallback\_SetSurfaceShowEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceShow)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))

**Description**

Sets a surface display callback for this [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. This callback is invoked when the application window has moved from the background to the foreground.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the target [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. |
| onSurfaceShow | Pointer to the surface display callback. - **surfaceHolder**: pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent()

void OH\_ArkUI\_SurfaceCallback\_SetSurfaceHideEvent(OH\_ArkUI\_SurfaceCallback\* callback,void (\*onSurfaceHide)(OH\_ArkUI\_SurfaceHolder\* surfaceHolder))

**Description**

Sets a surface hiding callback for this [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. This callback is invoked when the application window has moved from the foreground to the background.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md)\* callback | Pointer to the target [OH\_ArkUI\_SurfaceCallback](../../structs/oh-arkui-surfacecallback/document.md) instance. |
| onSurfaceHide | Pointer to the surface hiding callback. - **surfaceHolder**: pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |

#### \[h2\]OH\_ArkUI\_XComponentSurfaceConfig\_Create()

ArkUI\_XComponentSurfaceConfig\* OH\_ArkUI\_XComponentSurfaceConfig\_Create()

**Description**

Creates an [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object for an **XComponent**.

**Since**: 22

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md)\* | Pointer to the created [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object. |

#### \[h2\]OH\_ArkUI\_XComponentSurfaceConfig\_Dispose()

void OH\_ArkUI\_XComponentSurfaceConfig\_Dispose(ArkUI\_XComponentSurfaceConfig\* config)

**Description**

Disposes of an [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md)\* config | Pointer to the target [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) object. |

#### \[h2\]OH\_ArkUI\_XComponentSurfaceConfig\_SetIsOpaque()

void OH\_ArkUI\_XComponentSurfaceConfig\_SetIsOpaque(ArkUI\_XComponentSurfaceConfig\* config, bool isOpaque)

**Description**

Sets whether the surface held by the **XComponent** should be treated as opaque during rendering, regardless of the actual pixel transparency.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md)\* config | Pointer to the target [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) instance. |
| bool isOpaque | Whether the surface held by the **XComponent** should be treated as opaque during rendering. **true** if the surface should be treated as opaque, **false** otherwise. The default value is **false**, which means pixel opacity of the surface content will be applied during rendering. |

#### \[h2\]OH\_ArkUI\_SurfaceHolder\_SetSurfaceConfig()

int32\_t OH\_ArkUI\_SurfaceHolder\_SetSurfaceConfig(OH\_ArkUI\_SurfaceHolder\* surfaceHolder, ArkUI\_XComponentSurfaceConfig \*config)

**Description**

Sets the surface configuration for the [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md)\* surfaceHolder | Pointer to the target [OH\_ArkUI\_SurfaceHolder](../../structs/oh-arkui-surfaceholder/document.md) instance. |
| [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) \*config | Pointer to the target [ArkUI\_XComponentSurfaceConfig](../../structs/arkui-xcomponentsurfaceconfig/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
