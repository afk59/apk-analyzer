# Interface (AVScreenCaptureRecorder)

AVScreenCaptureRecorder is a class for screen capture management. It provides APIs for screen capture. Before calling any API in AVScreenCaptureRecorder, you must use [createAVScreenCaptureRecorder()](../functions/document.md#mediacreateavscreencapturerecorder12) to create an AVScreenCaptureRecorder instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/m1W_IbyHTmGJ4064K0Gw4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13A0C469D2FF050B064781D023B6C45D6ECBD891238D369791872A6AB7183D10)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### init12+

init(config: AVScreenCaptureRecordConfig): Promise<void>

Initializes screen capture and sets screen capture parameters. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [AVScreenCaptureRecordConfig](../interfaces-others/document.md#avscreencapturerecordconfig12) | Yes | Screen capture parameters to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Create a file.
let filesDir = '/data/storage/el2/base/haps';
let file = fs.openSync(filesDir + '/screenCapture.mp4', fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);

let avCaptureConfig: media.AVScreenCaptureRecordConfig = {
    fd: file.fd, // Before passing in an FD to this parameter, the file (generally an MP4 file) must be created by the caller and granted with the write permissions.
    frameWidth: 640,
    frameHeight: 480
    // Add other parameters.
};

if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.init(avCaptureConfig).then(() => {
    console.info('Succeeded in initializing avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to init avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### startRecording12+

startRecording(): Promise<void>

Starts screen recording. Before using this API, you must call [init](#init12). This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the startRecording method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.startRecording().then(() => {
    console.info('Succeeded in starting avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to start avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### stopRecording12+

stopRecording(): Promise<void>

Stops screen recording. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the stopRecording method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.stopRecording().then(() => {
    console.info('Succeeded in stopping avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to stop avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### skipPrivacyMode12+

skipPrivacyMode(windowIDs: Array<number>): Promise<void>

During screen capture, the application can exempt its privacy windows from security purposes. This API uses a promise to return the result.

For example, if a user enters a password in this application during screen capture, the application will not display a black screen.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowIDs | Array<number> | Yes | IDs of windows that require privacy exemption, including the main window IDs and subwindow IDs. For details about how to obtain window properties, see [getWindowProperties](../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the skipPrivacyMode method.
if (avScreenCaptureRecorder != undefined) {
  let windowIDs = \[\];
  avScreenCaptureRecorder.skipPrivacyMode(windowIDs).then(() => {
    console.info('Succeeded in skipping privacy mode');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to skip privacy mode. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### setMicEnabled12+

setMicEnabled(enable: boolean): Promise<void>

Enables or disables the microphone. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to enable the microphone. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the setMicEnabled method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.setMicEnabled(true).then(() => {
    console.info('Succeeded in setting microphone enabled.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set microphone enabled. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### setPickerMode22+

setPickerMode(pickerMode: PickerMode): Promise<void>

Sets the display mode of the picker. The setting takes effect the next time the picker is displayed. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pickerMode | [PickerMode](../enums/document.md#pickermode22) | Yes | 
Picker mode.

It defines the content type displayed in the picker. The options are as follows:

\- **SCREEN\_ONLY**: Displays only a list of screens.

\- **WINDOW\_ONLY**: Displays only a list of windows.

\- **SCREEN\_AND\_WINDOW**: Displays both screens and windows. It is the default value.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the setPickerMode method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.setPickerMode(media.PickerMode.WINDOW\_ONLY).then(() => {
    console.info('Succeeded in setting picker mode.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set picker mode. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### excludePickerWindows22+

excludePickerWindows(excludedWindows: Array<number>): Promise<void>

Sets the list of windows to be hidden in the picker. The setting takes effect the next time the picker is displayed. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| excludedWindows | Array<number> | Yes | List of windows to be hidden in the picker. For details about how to obtain window properties, see [getWindowProperties](../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let excludedWindows: Array<number> = \[101, 102, 103\];

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the excludePickerWindows method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.excludePickerWindows(excludedWindows).then(() => {
    console.info('Succeeded in excluding picker windows.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to exclude picker windows. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### presentPicker22+

presentPicker(): Promise<void>

Displays the Picker once more after the screen capture starts, allowing for dynamic updates to the recording source, such as changing the window or screen being recorded. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/1OuwTOdeQEWthUshNjXzTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6E99A8878A8A8E47D37D1A593AAB39D29353AE2E6A44E9A70E22BA212236743)

-   The ongoing capture process remains uninterrupted while updating the recording source.
-   Following the dynamic update of the recording source through the Picker, the capture proceeds with the newly selected source.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the presentPicker method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.presentPicker().then(() => {
    console.info('Succeeded in presenting picker avScreenCaptureRecorder.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to present picker avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### release12+

release(): Promise<void>

Releases this AVScreenCaptureRecorder instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the release method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.release().then(() => {
    console.info('Succeeded in releasing avScreenCaptureRecorder');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}\`);
  });
}

#### on('stateChange')12+

on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void

Subscribes to screen capture state changes. An application can subscribe to only one screen capture state change event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'stateChange'** in this case. |
| callback | Callback<[AVScreenCaptureStateCode](../enums/document.md#avscreencapturestatecode12)\> | Yes | Callback invoked when the event is triggered. [AVScreenCaptureStateCode](../enums/document.md#avscreencapturestatecode12) indicates the new state. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the on method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.on('stateChange', (state: media.AVScreenCaptureStateCode) => {
      console.info('avScreenCaptureRecorder stateChange to ' + state);
  });
}

#### on('error')12+

on(type: 'error', callback: ErrorCallback): void

Subscribes to AVScreenCaptureRecorder errors. You can handle the errors based on the application logic. An application can subscribe to only one AVScreenCaptureRecorder error event. When the application initiates multiple subscriptions to this event, the last subscription is applied.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'error'** in this case. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | Yes | Callback invoked when the event is triggered. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permission denied. |
| 5400103 | IO error. Return by ErrorCallback. |
| 5400105 | Service died. Return by ErrorCallback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the on method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.on('error', (err: BusinessError) => {
    console.error(\`avScreenCaptureRecorder error: Code: ${err.code}, message: ${err.message}\`);
  });
}

#### off('stateChange')12+

off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void

Unsubscribes from screen capture state changes. You can specify a callback to cancel the specified subscription.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'stateChange'** in this case. |
| callback | Callback<[AVScreenCaptureStateCode](../enums/document.md#avscreencapturestatecode12)\> | No | Callback used for unsubscription. [AVScreenCaptureStateCode](../enums/document.md#avscreencapturestatecode12) indicates the new state. If this parameter is not specified, the last subscription is canceled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the off method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.off('stateChange');
}

#### off('error')12+

off(type: 'error', callback?: ErrorCallback): void

Unsubscribes from AVScreenCaptureRecorder errors. You can specify a callback to cancel the specified subscription.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'error'** in this case. |
| callback | [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback) | No | Callback used for unsubscription. If this parameter is not specified, the last subscription is canceled. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Initialize avScreenCaptureRecorder.
let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in creating avScreenCaptureRecorder');
  } else {
    console.error('Failed to create avScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(\`createAVScreenCaptureRecorder catchCallback, error message:${error.message}\`);
});

// Other processes.

// Call the off method.
if (avScreenCaptureRecorder != undefined) {
  avScreenCaptureRecorder.off('error');
}
