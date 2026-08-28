# White Balance Settings (ArkTS)

Starting from API version 20, you can configure white balance effects. White balance is a color correction technique used by cameras to produce different visual effects in photos. Currently, white balance is supported for the following scenarios: photo capture ([PhotoSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-photosession)), video recording ([VideoSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videosession)), and the camera secure mode ([SecureSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-securesession)).

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Set white balance. Two methods are provided for setting white balance.
    
    -   Method 1: Use [isWhiteBalanceModeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalancequery#iswhitebalancemodesupported20) to check whether a specific white balance mode is supported. Then, call [setWhiteBalanceMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalance#setwhitebalancemode20) and [getWhiteBalanceMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalance#getwhitebalancemode20) to set and obtain the white balance mode. Note that you can only view the currently set white balance mode. The available white balance modes include automatic, manual, cloudy, incandescent, fluorescent, and daylight. If both a white balance mode and a white balance value are set, only one takes effect, with the white balance mode taking precedence by default.
        
        function isWhiteBalanceModeSupported(session: camera.PhotoSession | camera.VideoSession): boolean {
           let status: boolean = false;
           let whiteBalanceMode: camera.WhiteBalanceMode | undefined = undefined;
           try {
              let mode: camera.WhiteBalanceMode = camera.WhiteBalanceMode.DAYLIGHT;
              status = session.isWhiteBalanceModeSupported(mode);
              if(status){
                 session.setWhiteBalanceMode(mode);
              }
              whiteBalanceMode = session.getWhiteBalanceMode();
           } catch (error) {
              let err = error as BusinessError;
              console.error(\`The isWhiteBalanceModeSupported call failed. error code: ${err.code}\`);
           }
           return status;
        }
        
    -   Method 2: Call [getWhiteBalanceRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalancequery#getwhitebalancerange20) to obtain the range of white balance values supported by the device. Then, call [setWhiteBalance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalance#setwhitebalance20) and [getWhiteBalance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-whitebalance#getwhitebalance20) to set and obtain the white balance value. Note that you can only view the currently set white balance value.
        
        function getWhiteBalanceRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
           let range: Array<number> = \[\];
           try {
              range = session.getWhiteBalanceRange();
              let whiteBalance: number = 3000;
              if(whiteBalance >= range\[0\] && whiteBalance <= range\[1\]) {
                 session.setWhiteBalance(whiteBalance);
              }
              whiteBalance = session.getWhiteBalance();
           } catch (error) {
             let err = error as BusinessError;
             console.error(\`The getWhiteBalanceRange call failed. error code: ${err.code}\`);
           }
           return range;
        }
