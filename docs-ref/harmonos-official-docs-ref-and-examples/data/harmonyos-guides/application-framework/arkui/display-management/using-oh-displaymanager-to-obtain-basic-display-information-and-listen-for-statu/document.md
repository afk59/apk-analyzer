# Using OH\_DisplayManager to Obtain Basic Display Information and Listen for Status Changes (C/C++)

#### When to Use

The [OH\_DisplayManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-displaymanager) module provides functions for you to obtain the display information and listen for display status changes and folded/unfolded state changes. Applications can adapt to different UIs based on the information and changes.

-   The display information that can be obtained includes the resolution, physical pixel density, logical pixel density, refresh rate, size, orientation, and rotation angle of the display.
    
-   The display status changes include changes of the rotation, resolution, and refresh rate of the display.
    
-   The folded/unfolded state changes indicate whether the device is in the folded or unfolded state. A function is also provided for you to check whether a device is foldable.
    

#### Basic Concepts

-   Density DPI: physical pixel density, that is, the number of physical pixels per inch of the display.
    
-   Density pixels: logical pixel density, which indicates the scaling coefficient of the physical pixels and logical pixels. It is calculated by dividing the physical pixel density by 160.
    

#### Available APIs

The following table lists the common APIs. For more API description, see [OH\_DisplayManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-displaymanager).

| Name | Description |
| :-- | :-- |
| OH\_NativeDisplayManager\_GetDefaultDisplayRotation(NativeDisplayManager\_Rotation \*displayRotation) | Obtains the rotation angle of the default display. |
| OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*\*cutoutInfo) | Obtains the cutout information of the default display. |
| OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(NativeDisplayManager\_CutoutInfo \*cutoutInfo) | Destroys the cutout information of the default display. |
| OH\_NativeDisplayManager\_IsFoldable() | Checks whether the device is foldable. |
| OH\_NativeDisplayManager\_RegisterDisplayChangeListener( OH\_NativeDisplayManager\_DisplayChangeCallback displayChangeCallback, uint32\_t \*listenerIndex) | Registers a listener for status changes (such as rotation, refresh rate, DPI, and resolution changes) of the display. |
| OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(uint32\_t listenerIndex) | Cancels the listening for status changes of the display. |
| OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener( OH\_NativeDisplayManager\_FoldDisplayModeChangeCallback displayModeChangeCallback, uint32\_t \*listenerIndex) | Registers a listener for folded/unfolded state changes of the display. |
| OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(uint32\_t listenerIndex) | Cancels the listening for folded/unfolded state changes of the display. |

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
target\_link\_libraries(entry PUBLIC libnative\_display\_manager.so )

#### Including Header Files

#include <window\_manager/oh\_display\_info.h>
#include <window\_manager/oh\_display\_manager.h>
#include <hilog/log.h>

#### Obtaining Display Information

1.  Call **OH\_NativeDisplayManager\_GetDefaultDisplayRotation** to obtain the rotation angle of the default display.
    
    static napi\_value GetDefaultDisplayRotation(napi\_env env, napi\_callback\_info info)
    {
        NativeDisplayManager\_Rotation displayRotation;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_GetDefaultDisplayRotation(&displayRotation);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            napi\_value rotation;
            napi\_create\_int32(env, displayRotation, &rotation);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "rotation=%{public}d", displayRotation);
            return rotation;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                "GetDefaultDisplayRotation errCode=%{public}d", errCode);
            return errorCode;
        }
    }
    
2.  Call **OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo** to obtain the cutout information of the default display. Call **OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo** to destroy the cutout information.
    
    static napi\_value CreateDefaultDisplayCutoutInfo(napi\_env env, napi\_callback\_info info)
    {
        NativeDisplayManager\_CutoutInfo \*cutOutInfo = NULL;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_CreateDefaultDisplayCutoutInfo(&cutOutInfo);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "GetDefaultCutoutInfo errCode=%{public}d", errCode);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            if (cutOutInfo != NULL && cutOutInfo->boundingRectsLength != 0) {
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "GetDefaultCutoutInfo cutOutInfo length=%{public}d", cutOutInfo->boundingRectsLength);
                for (int i = 0; i < cutOutInfo->boundingRectsLength; i++) {
                    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                        "cutOutInfo\[%{public}d\]=\[%{public}d %{public}d %{public}d %{public}d\]",
                        i, cutOutInfo->boundingRects\[i\].left, cutOutInfo->boundingRects\[i\].top,
                        cutOutInfo->boundingRects\[i\].width, cutOutInfo->boundingRects\[i\].height);
                }
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall left rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.left.left, cutOutInfo->waterfallDisplayAreaRects.left.top,
                    cutOutInfo->waterfallDisplayAreaRects.left.width, cutOutInfo->waterfallDisplayAreaRects.left.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall top rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.top.left, cutOutInfo->waterfallDisplayAreaRects.top.top,
                    cutOutInfo->waterfallDisplayAreaRects.top.width, cutOutInfo->waterfallDisplayAreaRects.top.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall right rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.right.left, cutOutInfo->waterfallDisplayAreaRects.right.top,
                    cutOutInfo->waterfallDisplayAreaRects.right.width, cutOutInfo->waterfallDisplayAreaRects.right.height);
                OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
                    "cutOutInfo waterfall bottom rect=\[%{public}d %{public}d %{public}d %{public}d\]",
                    cutOutInfo->waterfallDisplayAreaRects.bottom.left,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.top,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.width,
                    cutOutInfo->waterfallDisplayAreaRects.bottom.height);
            }
            napi\_value boundingRectsLength;
            napi\_create\_int32(env, cutOutInfo->boundingRectsLength, &boundingRectsLength);
            OH\_NativeDisplayManager\_DestroyDefaultDisplayCutoutInfo(cutOutInfo);
            return boundingRectsLength;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            return errorCode;
        }
    }
    

#### Listening for Display Status Changes

Call **OH\_NativeDisplayManager\_RegisterDisplayChangeListener** to register a listener for display status changes, including the rotation, resolution, refresh rate, and DPI changes. Call **OH\_NativeDisplayManager\_UnregisterDisplayChangeListener** to cancel the listening for the display status changes.

void DisplayChangeCallback(uint64\_t displayId)
{
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "DisplayChangeCallback displayId=%{public}lu.", displayId);
}

static napi\_value RegisterDisplayChangeListener(napi\_env env, napi\_callback\_info info)
{
    uint32\_t listenerIndex;
    NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_RegisterDisplayChangeListener(
        DisplayChangeCallback, &listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "RegisterDisplayChangeListener listenerIndex =%{public}d errCode=%{public}d.", listenerIndex, errCode);
    if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
        napi\_value registerIndex;
        napi\_create\_int32(env, listenerIndex, &registerIndex);
        return registerIndex;
    } else {
        napi\_value errorCode;
        napi\_create\_int32(env, errCode, &errorCode);
        return errorCode;
    }
}

static napi\_value UnregisterDisplayChangeListener(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = { nullptr };

    uint32\_t listenerIndex;
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_get\_value\_uint32(env, args\[0\], &listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "UnregisterDisplayChangeListener listenerIndex =%{public}d.", listenerIndex);
    NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_UnregisterDisplayChangeListener(listenerIndex);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest",
        "UnregisterDisplayChangeListener errCode=%{public}d.", errCode);
    napi\_value errorCode;
    napi\_create\_int32(env, errCode, &errorCode);
    return errorCode;
}

#### Listening for Folded/Unfolded State Changes

1.  Call **OH\_NativeDisplayManager\_IsFoldable** to check whether a device is foldable.
    
    static napi\_value IsFoldable(napi\_env env, napi\_callback\_info info)
    {
        bool isFoldDevice = OH\_NativeDisplayManager\_IsFoldable();
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "IsFoldable isFoldDevice =%{public}d.", isFoldDevice);
        napi\_value isFold;
        napi\_get\_boolean(env, isFoldDevice, &isFold);
        return isFold;
    }
    
2.  Call **OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener** to register a listener for folded/unfolded state changes of the display. Call **OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener** to cancel the listening for the folded/unfolded state changes.
    
    void FoldDisplayModeChangeCallback(NativeDisplayManager\_FoldDisplayMode displayMode)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "displayMode=%{public}d.", displayMode);
    }
    
    static napi\_value RegisterFoldDisplayModeChangeListener(napi\_env env, napi\_callback\_info info)
    {
        uint32\_t listenerIndex = 0;
        NativeDisplayManager\_ErrorCode errCode = OH\_NativeDisplayManager\_RegisterFoldDisplayModeChangeListener(
            FoldDisplayModeChangeCallback, &listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "listenerIndex =%{public}d errCode=%{public}d.",
            listenerIndex, errCode);
        if (errCode == NativeDisplayManager\_ErrorCode::DISPLAY\_MANAGER\_OK) {
            napi\_value registerIndex;
            napi\_create\_int32(env, listenerIndex, &registerIndex);
            return registerIndex;
        } else {
            napi\_value errorCode;
            napi\_create\_int32(env, errCode, &errorCode);
            return errorCode;
        }
    }
    
    static napi\_value UnregisterFoldDisplayModeChangeListener(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\] = { nullptr };
        uint32\_t listenerIndex;
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        napi\_get\_value\_uint32(env, args\[0\], &listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "listenerIndex =%{public}d.", listenerIndex);
        NativeDisplayManager\_ErrorCode errCode =
            OH\_NativeDisplayManager\_UnregisterFoldDisplayModeChangeListener(listenerIndex);
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "DMSTest", "errorCode=%{public}d", errCode);
        napi\_value errorCode;
        napi\_create\_int32(env, errCode, &errorCode);
        return errorCode;
    }
    

#### Registering Functions

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"getDisplayRotation", nullptr, GetDefaultDisplayRotation, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"getCutoutInfo", nullptr, CreateDefaultDisplayCutoutInfo, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerDisplayChange", nullptr, RegisterDisplayChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"unregisterDisplayChange", nullptr, UnregisterDisplayChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"checkIsFoldDevice", nullptr, IsFoldable, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerFoldDisplayModeChange", nullptr, RegisterFoldDisplayModeChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"unregisterFoldDisplayModeChange", nullptr, UnregisterFoldDisplayModeChangeListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

#### Registering Modules

static napi\_module displayModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "nativedisplay",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&displayModule);
}

static napi\_module displayModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "nativedisplay",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&displayModule);
}

#### Calling the Functions in the index.ets File

private callGetDisplayRotation(): void {
  this.promptAction.openToast({ message: 'Call getDisplayRotation' }).catch((error: Error) => {
    console.error(\`callGetDisplayRotation error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`get rotation value is: ${displayNapi.getDisplayRotation()}\`);
  });
}

private callFoldableCallback(): void {
  this.promptAction.openToast({ message: 'Call register displayMode' }).catch((error: Error) => {
    console.error(\`callFoldableCallback error ${JSON.stringify(error)}\`);
  }).then(() => {
    let registerIndex = displayNapi.registerFoldDisplayModeChange();
    console.info(\`register foldable value is: ${registerIndex}\`);
    console.info(\`unregister foldable value is: ${displayNapi.unregisterFoldDisplayModeChange(registerIndex)}\`);
  });
}

private callGetCutoutInfo(): void {
  this.promptAction.openToast({ message: 'Call getCutoutInfo' }).catch((error: Error) => {
    console.error(\`callGetCutoutInfo error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`cutoutInfo length is: ${displayNapi.getCutoutInfo()}\`);
  });
}

private callDealListenCallback(): void {
  this.promptAction.openToast({ message: 'Call register change' }).catch((error: Error) => {
    console.error(\`callDealListenCallback error ${JSON.stringify(error)}\`);
  }).then(() => {
    let registerIndex = displayNapi.registerDisplayChange();
    console.info(\`register display change value is: ${registerIndex}\`);
    console.info(\`unregister display change value is: ${displayNapi.unregisterDisplayChange(registerIndex)}\`);
  });
}

private callDealFoldableDevice(): void {
  this.promptAction.openToast({ message: 'Call dealFoldableDevice' }).catch((error: Error) => {
    console.error(\`callDealFoldableDevice error ${JSON.stringify(error)}\`);
  }).then(() => {
    console.info(\`fold device is: ${displayNapi.checkIsFoldDevice()}\`);
  });
}
