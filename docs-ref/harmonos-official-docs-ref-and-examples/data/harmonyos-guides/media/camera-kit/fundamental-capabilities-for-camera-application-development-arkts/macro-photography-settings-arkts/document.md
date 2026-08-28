# Macro Photography Settings (ArkTS)

Starting from API version 19, you can configure macro photography. This feature allows the camera to focus closely and capture detailed images of small objects through optimized optical design and algorithms.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call [isMacroSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-macroquery#ismacrosupported19) to check whether the current device supports macro photography.
    
    let isSupported: boolean = photoSession.isMacroSupported();
    
3.  Call [enableMacro](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-macro#enablemacro19) to enable or disable macro photography.
    
    function EnableMacro(photoSession: camera.PhotoSession): void {
       let isSupported: boolean = photoSession.isMacroSupported();
       if (isSupported) {
          photoSession.enableMacro(true);
       }
    }
    

#### Status Listening

Starting from API version 20, you can listen for macro photography status changes.

Call [on('macroStatusChanged')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-photosession#onmacrostatuschanged20) to listen for the macroStatusChanged event to track changes in macro photography.

function callback(err: BusinessError, macroStatus: boolean): void {
   if (err !== undefined && err.code !== 0) {
      console.error(\`Callback Error, errorCode: ${err.code}\`);
      return;
   }
   console.info(\`Macro state: ${macroStatus}\`);
}

// Register a callback.
function registerMacroStatusChanged(photoSession: camera.PhotoSession): void {
   photoSession.on('macroStatusChanged', callback);
}

// Stop the listening.
function unregisterMacroStatusChanged(photoSession: camera.PhotoSession): void {
   photoSession.off('macroStatusChanged');
}
