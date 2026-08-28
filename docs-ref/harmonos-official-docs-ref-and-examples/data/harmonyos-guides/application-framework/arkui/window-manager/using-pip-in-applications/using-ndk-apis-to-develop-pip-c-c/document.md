# Using NDK APIs to Develop PiP (C/C++)

This topic uses video playback as an example to describe how to develop the PiP feature using NDK APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/k7s_U_0vT8KYLiT3uDzhWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09231539A5F0885310BBE6A31582E99D3F1E9AEFB4BA03522034395CE6F2719D)

-   Since API version 20, the NDK APIs can be used to develop the PiP feature.
-   The NDK APIs can be used to develop the PiP feature on phones, PCs/2-in-1 devices, and tablets.

#### Constraints

-   The PiP window content is rendered not through the XComponent Controller passed in, but via the component corresponding to the surfaceId obtained in the PiP start callback.
-   Similar to the typeNode implementation, the system does not cache pages. To perform page operations, applications must listen for the PiP lifecycle and execute corresponding actions at appropriate stages.
-   Automatic PiP launch is not supported.

#### How to Develop

The video player used in this section implements PiP through the following simplified workflow:

1.  Call **OH\_PictureInPicture\_CreatePipConfig** to create a PiP configurator, and set the initial configuration information in the configurator using **OH\_PictureInPicture\_SetPipMainWindowId**, **OH\_PictureInPicture\_SetPipTemplateType**, **OH\_PictureInPicture\_SetPipRect**, **OH\_PictureInPicture\_SetPipControlGroup**, and **OH\_PictureInPicture\_SetPipNapiEnv**.
2.  Create a PiP controller, and register lifecycle events and control event callbacks based on the returned controller ID. Specifically, call **OH\_PictureInPicture\_CreatePip** to create a PiP controller instance and cache the returned controller ID. Once the PiP controller is created, call **OH\_PictureInPicture\_DestroyPipConfig** to avoid memory leakage.
3.  Call **OH\_PictureInPicture\_RegisterStartPipCallback** to register the PiP start callback and render the video image based on the returned surface ID. You can register other callback functions as required.
4.  Call **OH\_PictureInPicture\_StartPip** to start PiP.
5.  Call **OH\_PictureInPicture\_UpdatePipContentSize** to update the media content size.
6.  Call **OH\_PictureInPicture\_StopPip** to stop PiP.
7.  Call **OH\_PictureInPicture\_UnregisterStartPipCallback** to unregister the PiP start callback to avoid memory leakage. Unregister other event callbacks that have been registered.

The following describes the files involved in the preceding steps and provide code examples.

For details about how to register the Node-API module, see [Node-API Development Specifications](../../../../../ndk-development/code-development/using-node-api/node-api-development-specifications/document.md).

This file is for reference only. Handle errors and log codes any way you like.

// napi\_init.cpp
#include "napi/native\_api.h"
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <string>
#include "window\_manager/oh\_window\_pip.h"
#include "hilog/log.h"
#include "js\_native\_api.h"
#include "napi/native\_api.h"
#include <cstdio>
#include "rawfile/raw\_file\_manager.h"

#define LOG\_MSG\_TAG "PiPMain"
#define LOG(format, ...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0xFF00, LOG\_MSG\_TAG, format, ##\_\_VA\_ARGS\_\_))
napi\_ref jsCallback;
napi\_env env\_;

napi\_ref jsLifecycleCallback;
napi\_env lifeEnv\_;
int32\_t g\_minValue = 0;
int32\_t g\_maxValue = 255;

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, int32\_t& value)
{
    return napi\_get\_value\_int32(env, jsValue, &value) == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, uint32\_t& value)
{
    return napi\_get\_value\_uint32(env, jsValue, &value) == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, int64\_t& value)
{
    return napi\_get\_value\_int64(env, jsValue, &value) == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, uint64\_t& value)
{
    int64\_t num;
    auto res = napi\_get\_value\_int64(env, jsValue, &num);
    if (res == napi\_ok) {
        value = static\_cast<uint64\_t>(num);
    }
    return res == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, double& value)
{
    return napi\_get\_value\_double(env, jsValue, &value) == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, bool& value)
{
    return napi\_get\_value\_bool(env, jsValue, &value) == napi\_ok;
}

inline bool ConvertFromJsNumber(napi\_env env, napi\_value jsValue, unsigned char& value)
{
    int32\_t num;
    if (napi\_get\_value\_int32(env, jsValue, &num) != napi\_ok) {
        return false;
    }
    if (num < g\_minValue || num > g\_maxValue) {
        return false; // Out of range.
    }
    value = static\_cast<unsigned char>(num);
    return true;
}

template<class T>
bool ConvertFromJsValue(napi\_env env, napi\_value jsValue, T& value)
{
    if (jsValue == nullptr) {
        return false;
    }
    using ValueType = std::remove\_cv\_t<std::remove\_reference\_t<T>>;
    if constexpr (std::is\_same\_v<ValueType, bool>) {
        return napi\_get\_value\_bool(env, jsValue, &value) == napi\_ok;
    } else if constexpr (std::is\_arithmetic\_v<ValueType>) {
        return ConvertFromJsNumber(env, jsValue, value);
    } else if constexpr (std::is\_same\_v<ValueType, std::string>) {
        size\_t len = 0;
        if (napi\_get\_value\_string\_utf8(env, jsValue, nullptr, 0, &len) != napi\_ok) {
            return false;
        }
        auto buffer = std::make\_unique<char\[\]>(len + 1);
        size\_t strLength = 0;
        if (napi\_get\_value\_string\_utf8(env, jsValue, buffer.get(), len + 1, &strLength) == napi\_ok) {
            value = buffer.get();
            return true;
        }
        return false;
    } else if constexpr (std::is\_enum\_v<ValueType>) {
        std::make\_signed\_t<ValueType> numberValue = 0;
        if (!ConvertFromJsNumber(env, jsValue, numberValue)) {
            return false;
        }
        value = static\_cast<ValueType>(numberValue);
        return true;
    }
    return false;
}

void PipStartPipCallback(uint32\_t controllerId, uint8\_t requestId, uint64\_t surfaceId)
{
    if (jsCallback) {
        napi\_value global = nullptr;
        napi\_get\_global(env\_, &global);
        size\_t argc = 1;
        std::string tStr = std::to\_string(surfaceId);
        const char\* cStr = tStr.c\_str();
        size\_t length = strlen(cStr);
        napi\_value str;
        napi\_status status = napi\_create\_string\_utf8(env\_, cStr, length, &str);
        napi\_value argv\[1\] = {str};
        napi\_value jsCallbackValue;
        
        napi\_value result = nullptr;
        if (!jsCallback) {
            LOG("js callback is invalid");
        }
        napi\_get\_reference\_value(env\_, jsCallback, &jsCallbackValue);
        napi\_call\_function(env\_, global, jsCallbackValue, argc, argv, &result);
    }
}

void LifecycleCallback(uint32\_t controllerId, PictureInPicture\_PipState state, int32\_t errcode)
{
    if (jsLifecycleCallback) {
        napi\_value global = nullptr;
        napi\_get\_global(lifeEnv\_, &global);
        size\_t argc = 1;
        napi\_value pipState = nullptr;
        napi\_create\_int32(lifeEnv\_, static\_cast<int32\_t> (state), &pipState);
        napi\_value argv\[1\] = {pipState};
        napi\_value jsCallbackValue;
        
        napi\_value result = nullptr;
        if (!jsCallback) {
            LOG("js callback is invalid");
        }
        napi\_get\_reference\_value(lifeEnv\_, jsLifecycleCallback, &jsCallbackValue);
        napi\_call\_function(lifeEnv\_, global, jsCallbackValue, argc, argv, &result);
    }
}

class PiPManager {
public:
    static napi\_value CreatePip(napi\_env env, napi\_callback\_info info);
    static napi\_value StartPip(napi\_env env, napi\_callback\_info info);
    static napi\_value RegisterStartPip(napi\_env env, napi\_callback\_info info);
    static napi\_value DeletePip(napi\_env env, napi\_callback\_info info);
    static napi\_value StopPip(napi\_env env, napi\_callback\_info info);
    static napi\_value RegisterLifecycleListener(napi\_env env, napi\_callback\_info info);
    static void getElement(napi\_env &env, uint32\_t size, napi\_value &controlGroupValue,
                PictureInPicture\_PipControlGroup controlGroup\[\]);
};

napi\_value PiPManager::CreatePip(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    napi\_value config = argv\[0\];

    napi\_value mainWindowIdValue = nullptr;
    napi\_value pipTemplateTypeValue = nullptr;
    napi\_value widthValue = nullptr;
    napi\_value heightValue = nullptr;
    napi\_value controlGroupValue = nullptr;
    napi\_value pipControllerIdValue = nullptr;
    
    uint32\_t controllerId = -1;
    uint32\_t mainWindowId = -1;
    PictureInPicture\_PipTemplateType pipTemplateType = PictureInPicture\_PipTemplateType::VIDEO\_PLAY;
    uint32\_t width = -1;
    uint32\_t height = -1;
    
    napi\_get\_named\_property(env, config, "mainWindowId", &mainWindowIdValue);
    napi\_get\_named\_property(env, config, "pipTemplateType", &pipTemplateTypeValue);
    napi\_get\_named\_property(env, config, "width", &widthValue);
    napi\_get\_named\_property(env, config, "height", &heightValue);
    napi\_get\_named\_property(env, config, "controlGroup", &controlGroupValue);
    napi\_get\_named\_property(env, config, "pipControllerId", &pipControllerIdValue);
    
    ConvertFromJsValue(env, mainWindowIdValue, mainWindowId);
    ConvertFromJsValue(env, pipTemplateTypeValue, pipTemplateType);
    ConvertFromJsValue(env, widthValue, width);
    ConvertFromJsValue(env, heightValue, height);
    ConvertFromJsValue(env, pipControllerIdValue, controllerId);
    
    uint32\_t size = 0;
    napi\_get\_array\_length(env, controlGroupValue, &size);
    PictureInPicture\_PipControlGroup controlGroup\[size\];

    PiPManager::getElement(env, size, controlGroupValue, controlGroup);
    
    napi\_value result = nullptr;
    PictureInPicture\_PipConfig pipConfig;
    OH\_PictureInPicture\_CreatePipConfig(&pipConfig);
    OH\_PictureInPicture\_SetPipMainWindowId(pipConfig, mainWindowId);
    OH\_PictureInPicture\_SetPipTemplateType(pipConfig, pipTemplateType);
    OH\_PictureInPicture\_SetPipRect(pipConfig, width, height);
    OH\_PictureInPicture\_SetPipControlGroup(pipConfig, controlGroup, size);
    OH\_PictureInPicture\_SetPipNapiEnv(pipConfig, env);
    int32\_t res = OH\_PictureInPicture\_CreatePip(pipConfig, &controllerId);
    OH\_PictureInPicture\_DestroyPipConfig(&pipConfig);
    napi\_create\_uint32(env, controllerId, &result);
    return result;
}

void PiPManager::getElement(napi\_env &env, uint32\_t size, napi\_value &controlGroupValue,
    PictureInPicture\_PipControlGroup controlGroup\[\])
{
    for (uint32\_t i = 0; i < size; i++) {
        napi\_value getElementValue = nullptr;
        napi\_get\_element(env, controlGroupValue, i, &getElementValue);
        PictureInPicture\_PipControlGroup controlType;
        if (ConvertFromJsValue(env, getElementValue, controlType)) {
            controlGroup\[i\] = controlType;
        }
        LOG("controlType: %{public}d", controlType);
    }
}

napi\_value PiPManager::StartPip(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    napi\_value controlIdValue = argv\[0\];
    uint32\_t controlId = -1;
    ConvertFromJsValue(env, controlIdValue, controlId);
    napi\_value resultValue = nullptr;
    int32\_t result = OH\_PictureInPicture\_StartPip(controlId);
    napi\_create\_uint32(env, result, &resultValue);
    return resultValue;
}

napi\_value PiPManager::RegisterStartPip(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    napi\_value controllerIdValue = argv\[0\];
    uint32\_t controlId = -1;
    napi\_status status = napi\_create\_reference(env, argv\[1\], 1, &jsCallback);
    env\_ = env;
    ConvertFromJsValue(env, controllerIdValue, controlId);
    napi\_value resultValue = nullptr;
    int32\_t result = OH\_PictureInPicture\_RegisterStartPipCallback(controlId, PipStartPipCallback);
    napi\_create\_uint32(env, result, &resultValue);
    return resultValue;
}

napi\_value PiPManager::DeletePip(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    uint32\_t controlId = -1;
    ConvertFromJsValue(env, argv\[0\], controlId);
    napi\_value resultValue = nullptr;
    int32\_t result = OH\_PictureInPicture\_DeletePip(controlId);
    napi\_create\_uint32(env, result, &resultValue);
    return resultValue;
}

napi\_value PiPManager::StopPip(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    uint32\_t controlId = -1;
    napi\_value resultValue = nullptr;

    ConvertFromJsValue(env, argv\[0\], controlId);
    uint32\_t result = OH\_PictureInPicture\_StopPip(controlId);
    napi\_create\_uint32(env, result, &resultValue);
    return resultValue;
}

napi\_value PiPManager::RegisterLifecycleListener(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    uint32\_t controlId = -1;
    napi\_status status = napi\_create\_reference(env, argv\[1\], 1, &jsLifecycleCallback);
    lifeEnv\_ = env;
    if (status != napi\_ok) {
        LOG("register failed %{public}d", status);
    }
    ConvertFromJsValue(env, argv\[0\], controlId);
    
    napi\_value resultValue = nullptr;
    int32\_t result = OH\_PictureInPicture\_RegisterLifecycleListener(controlId, LifecycleCallback);
    napi\_create\_uint32(env, result, &resultValue);
    return resultValue;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"createPip", nullptr, PiPManager::CreatePip, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"startPip", nullptr, PiPManager::StartPip, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerStartPip", nullptr, PiPManager::RegisterStartPip, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"deletePip", nullptr, PiPManager::DeletePip, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"stopPip", nullptr, PiPManager::StopPip, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"registerLifecycleListener", nullptr, PiPManager::RegisterLifecycleListener,
            nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};
extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Node-API interface declaration:

// Index.d.ts
export enum PiPControlGroup {
  VIDEO\_PLAY\_VIDEO\_PREVIOUS\_NEXT = 101,
  VIDEO\_PLAY\_FAST\_FORWARD\_BACKWARD = 102,
  VIDEO\_CALL\_MICROPHONE\_SWITCH = 201,
  VIDEO\_CALL\_HANG\_UP\_BUTTON = 202,
  VIDEO\_CALL\_CAMERA\_SWITCH = 203,
  VIDEO\_CALL\_MUTE\_SWITCH = 204,
  VIDEO\_MEETING\_HANG\_UP\_BUTTON = 301,
  VIDEO\_MEETING\_CAMERA\_SWITCH = 302,
  VIDEO\_MEETING\_MUTE\_SWITCH = 303,
  VIDEO\_MEETING\_MICROPHONE\_SWITCH = 304,
  VIDEO\_LIVE\_VIDEO\_PLAY\_PAUSE = 401,
  VIDEO\_LIVE\_MUTE\_SWITCH = 402,
}
export interface PiPConfig {
  mainWindowId: number;
  pipTemplateType: number;
  width: number;
  height: number;
  controlGroup: Array<PiPControlGroup>;
}
export declare const createPip: (config: PiPConfig) => number;
export declare const startPip: (controllerId: number) => number;
export declare const registerStartPip: (controllerId: number, jsCallback: Function) => number;
export declare const deletePip: (controllerId: number) => number;
export declare const stopPip: (controllerId: number) => number;
export declare const registerLifecycleListener: (controllerId: number, jsCallback: Function) => number;

**CMakeLists.txt** file, which is used to generate the corresponding library file.

\# CMakeLists.txt
# the minimum version of CMake.
cmake\_minimum\_required(VERSION 3.5.0)
set(CMAKE\_CXX\_STANDARD 17)
set(CMAKE\_CXX\_STANDARD\_REQUIRED ON)
project(MyApplication)
set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
if(DEFINED PACKAGE\_FIND\_FILE)
    include(${PACKAGE\_FIND\_FILE})
endif()
include\_directories(${NATIVERENDER\_ROOT\_PATH}
                    ${NATIVERENDER\_ROOT\_PATH}/include)
add\_library(entry SHARED napi\_init.cpp)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libace\_ndk.z.so libnative\_window\_manager.so libhilog\_ndk.z.so)

Example of the EntryAbility file:

// entryability/EntryAbility.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { PipManager } from '../nodefree/PipManager';
import { Logger } from '../util/LogUtil';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      AppStorage.setOrCreate('UIAbilityContext', this.context);
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR\_MODE\_NOT\_SET);
  }

  onDestroy(): void {
    Logger.info('testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    Logger.info('testTag', '%{public}s', 'Ability onWindowStageCreate');
    let windowClass: window.Window | undefined = undefined;
    let windowClassId: number = -1;

    windowStage.getMainWindow().then((window) => {
      if (window == null) {
        Logger.error('Failed to obtaining the window. Cause: The data is empty');
        return;
      }
      windowClass = window;
      windowClass.setUIContent('pages/Index');
      windowClassId = windowClass.getWindowProperties().id;
      AppStorage.setOrCreate('windowId', windowClassId);
      Logger.info('Succeeded in obtaining the window')

      let ctx = window.getUIContext();
      AppStorage.setOrCreate('UIContext', ctx);
      // Create a typeNode through the UIContext in the main window.
      PipManager.getInstance().makeTypeNode(ctx);
    }).catch((err: BusinessError) => {
      Logger.error(\`Failed to obtaining the window. Cause code: ${err.code}, message: ${err.message}\`);
    });
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        Logger.error('testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      Logger.info('testTag', 'Succeeded in loading the content.');
    });
  }
  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    Logger.info('testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    Logger.info('testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    Logger.info('testTag', '%{public}s', 'Ability onBackground');
  }
}

The AVPlayer is required for video playback in the example. For details, see [Using AVPlayer to Play Videos (ArkTS)](../../../../../media/media-kit/media-development-arkts/playback/using-avplayer-to-play-videos-arkts/document.md).

// model/AVPlayer.ets
// Simple implementation of the video player.
import media from '@ohos.multimedia.media';
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
import resourceManager from '@ohos.resourceManager';
import { Logger } from '../util/LogUtil';

export class AVPlayer {
  public avPlayer?: media.AVPlayer;
  private count: number = 0;
  private surfaceID: string; // The surfaceID parameter specifies the window used to display the video. Its value is obtained through the XComponent.
  public jumpNext: boolean = false;
  public type: number = 0; // Distinguish the player on the main screen from that in the PiP window.
  public state\_: string = ''
  public playStatus: boolean = true;

  constructor(surfaceID: string, type: number) {
    this.surfaceID = surfaceID;
    this.type = type
  }

  setSurfaceId(id: string) {
    if (this.avPlayer) {
      this.surfaceID = id;
      this.avPlayer.surfaceId = id;
    }
  }

  updatePlayStatus(status: boolean) {
    this.playStatus = status;
  }
  // Set AVPlayer callback functions.
  setAVPlayerCallback() {
    // Callback function for the seek operation.
    this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
      Logger.info(\`PipMain AVPlayer seek succeeded, seek time is ${seekDoneTime}\`);
    })
    // Callback function for errors. If an error occurs during the operation on the AVPlayer, reset() is called to reset the AVPlayer.
    this.avPlayer?.on('error', (err: BusinessError) => {
      Logger.error(\`PipMain Invoke avPlayer failed, code is ${err.code}, message is ${err.message}\`);
      this.avPlayer?.reset(); // Call reset() to reset the AVPlayer, which enters the idle state.
    })
    // Callback function for state changes.
    this.avPlayer?.on('stateChange', async (state, reason) => {
      if (!this.avPlayer) {
        return;
      }
      this.state\_ = state;
      switch (state) {
        case 'idle': // This state is reported upon a successful call of reset().
          Logger.info('AVPlayer state idle called.');
          if (!this.jumpNext) {
            this.avPlayer.release(); // Call release() to release the instance.
          } else {
            let uiContext: UIContext = AppStorage.get('UIAbilityContext') as UIContext;
            let context = uiContext.getHostContext() as common.UIAbilityContext;
            let fileDescriptor: resourceManager.RawFileDescriptor;
            fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
            // Assign a value to fdSrc to trigger the reporting of the initialized state.
            this.avPlayer.fdSrc = fileDescriptor;
          }
          break;
        case 'initialized': // This state is reported when the AVPlayer sets the playback source.
          Logger.info('initialized called.');
          this.avPlayer.surfaceId = this.surfaceID; // Set the window to display the video. This setting is not required when a pure audio asset is to be played.
          this.avPlayer.prepare().then(() => {
            Logger.info('AVPlayer prepare succeeded.');
          }, (err: BusinessError) => {
            Logger.error(\`Invoke prepare failed, code is ${err.code}, message is ${err.message}\`);
          });
          break;
        case 'prepared': // This state is reported upon a successful call of prepare().
          Logger.info('AVPlayer state prepared called.');
          this.avPlayer.play(); // Call play() to start playback.
          break;
        case 'playing': // This state is reported upon a successful call of play().
          Logger.info('AVPlayer state playing called.');
          this.jumpNext = false;
          this.count++;
          break;
        case 'paused': // This state is reported upon a successful call of pause().
          Logger.info('AVPlayer state paused called.');
          // this.avPlayer.play(); // Call play() again to start playback.
          break;
        case 'completed': // This state is reported upon the completion of the playback.
          Logger.info('AVPlayer state completed called.');
          this.playNext();
          ; // Call stop() to stop the playback.
          break;
        case 'stopped': // This state is reported upon a successful call of stop().
          Logger.info('AVPlayer state stopped called.');
          this.avPlayer.reset(); // Call reset() to reset the AVPlayer state.
          break;
        case 'released':
          Logger.info('AVPlayer state released called.');
          break;
        default:
          Logger.info('AVPlayer state unknown called.');
          break;
      }
    })
    this.avPlayer?.on('videoSizeChange', (width: number, height: number) => {
      Logger.info('videoSizeChange width:' + width + ' height:' + height);
      let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
    })
  }

  // The following demo shows how to use resourceManager to obtain the media file packed in the HAP file and play the media file by using the fdSrc attribute.
  async avPlayerFdSrc() {
    // Create an AVPlayer instance.
    Logger.info('avPlayerFdSrc');
    this.avPlayer = await media.createAVPlayer();

    // Set a callback function for state changes.
    this.setAVPlayerCallback();
    // Call getRawFd of the resourceManager member of UIAbilityContext to obtain the media asset URL.
    // The return type is {fd,offset,length}, where fd indicates the file descriptor address of the HAP file, offset indicates the media asset offset, and length indicates the duration of the media asset to play.

    let context = AppStorage.get('UIAbilityContext') as common.UIAbilityContext;
    let fileDescriptor = await context.resourceManager.getRawFd('640x360.mp4');
    Logger.info('getRawFd');
    // Assign a value to fdSrc to trigger the reporting of the initialized state.
    this.avPlayer.fdSrc = fileDescriptor;
  }

  async playNext() {
    if (this.avPlayer === null) {
      return;
    }
    this.jumpNext = true;
    this.avPlayer?.stop();
  }

  play() {
    if (this.state\_ === 'paused') {
      this.avPlayer?.play();
    }
  }

  pause() {
    if (this.state\_ === 'playing') {
      this.avPlayer?.pause();
    }
  }

  stopAvPlayer() {
    Logger.info('stopAvPlayer>>>')
    if (!this.avPlayer) {
      return;
    }
    this.avPlayer.stop();
    Logger.info('stopping>>>');
    this.avPlayer.reset();
  }
}

Application UI layout file, which is used to demonstrate the PiP feature.

// pages/Index.ets
// Application home screen
import { router } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      Scroll() {
        Flex({ direction: FlexDirection.Column }) {
          // ...
          this.featureButton('Implement PiP using NDK APIs (C++)', this.ndkImplement);
        }
      }
    }
    .hideBackButton(true)
    .titleMode(NavigationTitleMode.Mini)
    .backgroundColor('#FFF1F3F5')
    .mode(NavigationMode.Stack)
    .title('Sample Code for PiP')
  }

  @Builder
  featureButton(buttonText: string, callbackOnClick: () => void) {
    Button({ type: ButtonType.Normal }) {
      Row() {
        Column() {
          Text(buttonText)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .fontColor('#000000')
          Rect()
            .radius(1)
            .fill('#0A59F7')
            .height(2)
            .width(30)
        }
        .width('100%')
        .alignItems(HorizontalAlign.Start)
      }
      .width('100%')
    }
    .width('90%')
    .padding('5%')
    .margin({ top: '3%', bottom: '2%', right: '3%' })
    .backgroundColor('#FFFFFF')
    .borderRadius(20)
    .onClick(callbackOnClick)
  }

  // ...
  private ndkImplement = () => {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/NDKImplementPage' }, router.RouterMode.Standard)
  }
}

// pages/NDKImplementIndexPage.ets
// UI for demonstrating the PiP feature
import testNapi, {PiPConfig} from 'libentry.so';
import { PiPWindow } from '@kit.ArkUI';
import { AVPlayer } from '../model/NDKAVPlayer';
import { Logger } from '../util/LogUtil';

const TAG = 'PipMain';
export enum PiPControlGroup {
  VIDEO\_PLAY\_VIDEO\_PREVIOUS\_NEXT = 101,
  VIDEO\_PLAY\_FAST\_FORWARD\_BACKWARD = 102,
  VIDEO\_CALL\_MICROPHONE\_SWITCH = 201,
  VIDEO\_CALL\_HANG\_UP\_BUTTON = 202,
  VIDEO\_CALL\_CAMERA\_SWITCH = 203,
  VIDEO\_CALL\_MUTE\_SWITCH = 204,
  VIDEO\_MEETING\_HANG\_UP\_BUTTON = 301,
  VIDEO\_MEETING\_CAMERA\_SWITCH = 302,
  VIDEO\_MEETING\_MUTE\_SWITCH = 303,
  VIDEO\_MEETING\_MICROPHONE\_SWITCH = 304,
  VIDEO\_LIVE\_VIDEO\_PLAY\_PAUSE = 401,
  VIDEO\_LIVE\_MUTE\_SWITCH = 402,
}

@Entry
@Component
struct NDKImplementIndexPage {
  @State message: string = 'Hello World';
  mXComponentController: XComponentController | null = new XComponentController();
  private controllerId: number = -1;
  private contentWidth: number = 1920;
  private contentHeight: number = 1080;
  private pipType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO\_PLAY;
  private pipControlGroups: Array<PiPControlGroup> = \[\];
  player?: AVPlayer;
  surfaceId = '';

  changeSurface = (surfaceId: string) => {
    if(this.player) {
      this.player.setSurfaceId(surfaceId);
      return;
    }
    Logger.info(\`\[${TAG}\] change surface failed\`);
  }

  private onStateChange = (state: PiPWindow.PiPState) => {
    switch(state) {
      case PiPWindow.PiPState.ABOUT\_TO\_START:
        Logger.info(\`\[${TAG}\] ABOUT\_TO\_START\`);
        break;
      case PiPWindow.PiPState.STARTED:
        Logger.info(\`\[${TAG}\] STARTED\`);
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_STOP:
        Logger.info(\`\[${TAG}\] ABOUT\_TO\_STOP\`);
        break;
      case PiPWindow.PiPState.STOPPED:
        if (this.mXComponentController) {
          this.changeSurface(this.mXComponentController?.getXComponentSurfaceId());
        }
        Logger.info(\`\[${TAG}\] STOPPED\`);
        break;
      case PiPWindow.PiPState.ABOUT\_TO\_RESTORE:
        this.changeSurface(this.surfaceId);
        Logger.info(\`\[${TAG}\] ABOUT\_TO\_RESTORE\`);
        break;
      case PiPWindow.PiPState.ERROR:
        Logger.info(\`\[${TAG}\] ERROR\`);
        break;
      default:
        break;
    }
  }

  build() {
    RelativeContainer() {
      Row({ space: 20 }) {

        Button('Change Template Type')
          .bindMenu(\[
            {
              value: 'Video Playback',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO\_PLAY;
                this.pipControlGroups = \[PiPControlGroup.VIDEO\_PLAY\_VIDEO\_PREVIOUS\_NEXT\];
              }
            },
            {
              value: 'Call',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO\_CALL;
                this.pipControlGroups = \[PiPControlGroup.VIDEO\_CALL\_HANG\_UP\_BUTTON,
                  PiPControlGroup.VIDEO\_CALL\_CAMERA\_SWITCH, PiPControlGroup.VIDEO\_CALL\_MICROPHONE\_SWITCH\];
              }
            },
            {
              value: 'Meeting',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO\_MEETING;
                this.pipControlGroups = \[PiPControlGroup.VIDEO\_MEETING\_MICROPHONE\_SWITCH,
                  PiPControlGroup.VIDEO\_MEETING\_HANG\_UP\_BUTTON,
                  PiPControlGroup.VIDEO\_MEETING\_CAMERA\_SWITCH\];
              }
            },
            {
              value: 'Live',
              action: () => {
                this.pipType = PiPWindow.PiPTemplateType.VIDEO\_LIVE;
                this.pipControlGroups = \[PiPControlGroup.VIDEO\_LIVE\_VIDEO\_PLAY\_PAUSE,
                  PiPControlGroup.VIDEO\_LIVE\_MUTE\_SWITCH\];
              }
            }
          \])
      }
      .size({ width: '100%', height: 60 })
      .backgroundColor('#DDDDDD')
      .justifyContent(FlexAlign.SpaceAround)
      .alignRules({
        top: { anchor: '\_\_container\_\_', align: VerticalAlign.Top },
        middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
      })
      .id('pip\_type\_control')
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          if (this.mXComponentController) {
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
          }
          this.player = new AVPlayer(this.surfaceId, 1);
          this.player.avPlayerFdSrc();
        })
        .onDestroy(() => {
          Logger.info(\`\[${TAG}\] XComponent onDestroy\`);
        })
        .size({ width: '100%', height: '800px' })
        .margin({ top: 10 })
        .backgroundColor('#888888')
        .alignRules({
          bottom: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .id('x\_component')
        .size({ width: '100%', height: '800px' })
      Row({ space: 0 }) {
        Button('Create PiPController')
          .onClick(() => {
            let windowId: number | undefined = AppStorage.get('windowId');
            let config: PiPConfig = {
              mainWindowId: windowId as number,
              pipTemplateType: this.pipType,
              width: this.contentWidth,
              height: this.contentHeight,
              controlGroup: this.pipControlGroups
            }
            this.controllerId = testNapi.createPip(config);
            testNapi.registerStartPip(this.controllerId, this.changeSurface);
            testNapi.registerLifecycleListener(this.controllerId, this.onStateChange);
          })
        Button('Start PiP')
          .onClick(() => {
            testNapi.startPip(this.controllerId);
          })
      }
      .size({ width: '100%', height: 60 })
      .alignRules({
        top: { anchor: 'x\_component', align: VerticalAlign.Bottom },
        left: { anchor: '\_\_container\_\_', align: HorizontalAlign.Start }
      })
      .id('pip\_control')
      Row({ space: 0 }) {
        Button('Close PiP')
          .onClick(() => {
            testNapi.stopPip(this.controllerId);
          })
        Button('Delete PiPController')
          .onClick(() => {
            testNapi.deletePip(this.controllerId);
          })
      }
      .size({ width: '100%', height: 60 })
      .alignRules({
        top: { anchor: 'pip\_control', align: VerticalAlign.Bottom },
        left: { anchor: '\_\_container\_\_', align: HorizontalAlign.Start }
      })
    }
    .size({ width: '100%', height: '100%' })
  }
}

The following figure shows the schematic diagram of the preceding sample code.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/8k5QOQvsQvi95ngZD7KEJw/en-us_image_0000002529702003.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=528233CE8218B5837A72BED7A1310D4B8F5A6BB1E17D658DFADDA6BEF181A73E "Click to enlarge")
