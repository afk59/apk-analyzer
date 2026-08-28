# Camera Controller (ArkTS)

Starting from API version 20, the camera framework introduces a camera controller to enhance live streaming with features like beautification and background blur.

The camera controller is designed for live streaming and video calls and currently works only with the front camera in video mode, supporting up to 1080p resolution at 30fps.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call [isControlCenterSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-controlcenterquery#iscontrolcentersupported20) to check whether the current device and scenario support the camera controller.
    
    function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
      let isSupported: boolean = videoSession.isControlCenterSupported();
      return isSupported;
    }
    
3.  Call [getSupportedEffectTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-controlcenterquery#getsupportedeffecttypes20) to query the effect types supported by the camera controller on the current device and in the current scenario.
    
    function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
      let effectTypes: Array<camera.ControlCenterEffectType> = \[\];
      effectTypes = videoSession.getSupportedEffectTypes();
      return effectTypes;
    }
    
4.  Call [enableControlCenter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-controlcenter#enablecontrolcenter20) to enable or disable the camera controller, if it is supported.
    
    function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
      let isSupported: boolean = videoSession.isControlCenterSupported();
      if (isSupported) {
        videoSession.enableControlCenter(enable);
      }
    }
    
5.  Once the camera controller is enabled, the **Video effects** icon is displayed in the status bar.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/7SbmwP_3RJmvCiN6UkfrOw/en-us_image_0000002568764903.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97F97729A0CABAAAC177C400D0DFE62BBF9E20394062F66359C4687FBD33EC33)
    
6.  You can tap the **Video effects** icon to go to the secondary screen, where you can adjust effects like **Beautification** and **Background blur**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/U8rZoINWScW89Wd_ymlcBg/en-us_image_0000002537765178.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062039Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C93056F3A0CCF6A4C21431C82A7491DCA33001C22EBA2398B6F5480F027ADAD3)
    

#### Status Listening

Applications can listen for the enabled status of the camera controller's effects.

Register the [controlCenterEffectStatusChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videosession#oncontrolcentereffectstatuschange20) callback to track changes in the enabled status of each effect.

When the enabled status of an effect in the camera controller changes, the callback returns the [ControlCenterStatusInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#controlcenterstatusinfo20) parameter.

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`controlCenterEffectStatusChange: ${status}\`);
}

function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
  videoSession.on('controlCenterEffectStatusChange', callback);
}
