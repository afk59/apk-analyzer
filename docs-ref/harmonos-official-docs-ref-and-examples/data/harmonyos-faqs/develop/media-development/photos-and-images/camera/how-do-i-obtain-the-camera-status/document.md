# How do I obtain the camera status?

Set a callback to obtain the camera status.

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
const context = AppStorage.get("context") as UIContext;
let cameraManager = camera.getCameraManager(context.getHostContext()!);
cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
  console.log(\`camera : ${cameraStatusInfo.camera.cameraId}\`);
  console.log(\`status: ${cameraStatusInfo.status}\`);
});

CameraStatus

**CameraStatus** is an enum that indicates the camera statuses.

**Reference**

[CameraStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#camerastatus)
