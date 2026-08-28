# @ohos.print (Print)

The **print** module provides APIs for basic print operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/KZqGWXeJQnq9P94wcppJZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F83A7C7A546CE5192F3B234EAA9C240CCF5FBECB2079402306EF75ACD047BA8)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { print } from '@kit.BasicServicesKit';

#### PrintTask

Implements event listeners for print jobs.

#### \[h2\]on

on(type: 'block', callback: Callback<void>): void

Subscribes to the block events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'block'**.

It means that the print job is blocked.

 |
| callback | Callback<void> | Yes | Callback used to notify the caller that the print job is blocked. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.on('block', () => {
        console.info('print state is block');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]on

on(type: 'succeed', callback: Callback<void>): void

Subscribes to the success events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'succeed'**.

It means that the print job is successful.

 |
| callback | Callback<void> | Yes | Callback used to notify the caller that the print job is successful. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.on('succeed', () => {
        console.info('print state is succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]on

on(type: 'fail', callback: Callback<void>): void

Subscribes to the failure events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'fail'**.

It means that the print job is failed.

 |
| callback | Callback<void> | Yes | Callback used to notify the caller that the print job is failed. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.on('fail', () => {
        console.info('print state is fail');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]on

on(type: 'cancel', callback: Callback<void>): void

Subscribes to the cancellation events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'cancel'**.

It means that the print job is canceled.

 |
| callback | Callback<void> | Yes | Callback used to notify the caller that the print job is canceled. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.on('cancel', () => {
        console.info('print state is cancel');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]off

off(type: 'block', callback?: Callback<void>): void

Unsubscribes from the block events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'block'**.

It means that the print job is blocked.

 |
| callback | Callback<void> | No | Callback used to unsubscribe from the block events of a specified print job. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.off('block', () => {
        console.info('unregister state block');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]off

off(type: 'succeed', callback?: Callback<void>): void

Unsubscribes from the success events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'succeed'**.

It means that the print job is successful.

 |
| callback | Callback<void> | No | Callback used to unsubscribe from the success events of a specified print job. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.off('succeed', () => {
        console.info('unregister state succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]off

off(type: 'fail', callback?: Callback<void>): void

Unsubscribes from the failure events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'fail'**.

It means that the print job is failed.

 |
| callback | Callback<void> | No | Callback used to unsubscribe from the failure events of a specified print job. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.off('fail', () => {
        console.info('unregister state fail');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### \[h2\]off

off(type: 'cancel', callback?: Callback<void>): void

Unsubscribes from the cancellation events of a print job. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Listening type.

The value is fixed at **'cancel'**.

It means that the print job is canceled.

 |
| callback | Callback<void> | No | Callback used to unsubscribe from the cancellation events of a specified print job. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.off('cancel', () => {
        console.info('unregister state cancel');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### PrintDocumentAdapter11+

Provides information about the document to print. This API must be implemented by a third-party application.

#### \[h2\]onStartLayoutWrite11+

onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number, writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void

Sends an empty PDF file descriptor to a third-party application. The third-party application updates the file with the new print attributes and then calls **writeResultCallback** to print the file.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| jobId | string | Yes | ID of the print job. |
| oldAttrs | [PrintAttributes](#printattributes11) | Yes | Old print attributes. |
| newAttrs | [PrintAttributes](#printattributes11) | Yes | New print attributes. |
| fd | number | Yes | PDF file descriptor sent to the API caller. |
| writeResultCallback | (jobId: string, writeResult: [PrintFileCreationState](#printfilecreationstate11)) => void | Yes | Callback used to print the updated file. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT\_FILE\_CREATED);
    };
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state == print.PrintDocumentAdapterState.PREVIEW\_DESTROY) {
            console.info('PREVIEW\_DESTROY');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_SUCCEED) {
            console.info('PRINT\_TASK\_SUCCEED');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_FAIL) {
            console.info('PRINT\_TASK\_FAIL');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_CANCEL) {
            console.info('PRINT\_TASK\_CANCEL');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_BLOCK) {
            console.info('PRINT\_TASK\_BLOCK');
        }
    }
}

#### \[h2\]onJobStateChanged11+

onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void

Registers a listener for print job state changes.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| jobId | string | Yes | ID of the print job. |
| state | [PrintDocumentAdapterState](#printdocumentadapterstate11) | Yes | New state of the print job. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyPrintDocumentAdapter implements print.PrintDocumentAdapter {
    onStartLayoutWrite(jobId: string, oldAttrs: print.PrintAttributes, newAttrs: print.PrintAttributes, fd: number,
        writeResultCallback: (jobId: string, writeResult: print.PrintFileCreationState) => void) {
        writeResultCallback(jobId, print.PrintFileCreationState.PRINT\_FILE\_CREATED);
    };
    onJobStateChanged(jobId: string, state: print.PrintDocumentAdapterState) {
        if (state == print.PrintDocumentAdapterState.PREVIEW\_DESTROY) {
            console.info('PREVIEW\_DESTROY');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_SUCCEED) {
            console.info('PRINT\_TASK\_SUCCEED');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_FAIL) {
            console.info('PRINT\_TASK\_FAIL');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_CANCEL) {
            console.info('PRINT\_TASK\_CANCEL');
        } else if (state == print.PrintDocumentAdapterState.PRINT\_TASK\_BLOCK) {
            console.info('PRINT\_TASK\_BLOCK');
        }
    }
}

#### print.print10+

print(files: Array<string>, callback: AsyncCallback<PrintTask>): void

Prints files. This API uses an asynchronous callback to return the result. To start the system print preview page, call the [print](#printprint11-1) API and pass in context.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | List of files to print. Images (in .jpg, .png, .gif, .bmp, or .webp format) and PDF files are supported. You should save the files to the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API. |
| callback | AsyncCallback<[PrintTask](#printtask)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

// Pass in the URIs of the files.
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\], (err: BusinessError, printTask: print.PrintTask) => {
    if (err) {
        console.error('print err ' + JSON.stringify(err));
    } else {
        printTask.on('succeed', () => {
            console.info('print state is succeed');
        })
        // ...
    }
})

#### print.print10+

print(files: Array<string>): Promise<PrintTask>

Prints files. This API uses a promise to return the result. To start the system print preview page, call the [print](#printprint11-1) API and pass in context.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | List of files to print. Images (in .jpg, .png, .gif, .bmp, or .webp format) and PDF files are supported. You should save the files to the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<[PrintTask](#printtask)\> | Print result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

// Pass in the URIs of the files.
let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
print.print(\[fileUri.getUriFromPath(filePath)\]).then((printTask: print.PrintTask) => {
    printTask.on('succeed', () => {
        console.info('print state is succeed');
    })
    // ...
}).catch((error: BusinessError) => {
    console.error('print err ' + JSON.stringify(error));
})

#### print.print11+

print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void

Prints files. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | List of files to be printed. Currently, the following file types are supported: ".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", and ".xml". You should save the files to the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API. |
| context | Context | Yes | UIAbilityContext used to start the system print UI. |
| callback | AsyncCallback<[PrintTask](#printtask)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("Print").width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print(\[fileUri.getUriFromPath(filePath)\], context, (err: BusinessError, printTask: print.PrintTask) => {
                        if (err) {
                            console.error('print err ' + JSON.stringify(err));
                        } else {
                            printTask.on('succeed', () => {
                                console.info('print state is succeed');
                            })
                            // ...
                        }
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}

#### print.print11+

print(files: Array<string>, context: Context): Promise<PrintTask>

Prints files. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| files | Array<string> | Yes | List of files to be printed. Currently, the following file types are supported: ".bm", ".bmp", ".doc", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".gif", ".jfif", ".jpe", ".jpeg", ".jpg", "pdf", ".pot", ".potm", ".potx", ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".png", ".rtf", ".txt", ".webp", ".wps", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltx", and ".xml". You should save the files to the application sandbox, obtain the sandbox URI through **fileUri.getUriFromPath**, and then pass this URI as a parameter to this API. |
| context | Context | Yes | UIAbilityContext used to start the system print UI. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<[PrintTask](#printtask)\> | Print result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("Print").width('90%').height(50).onClick(() => {
                    let filePath = '/data/storage/el2/base/haps/entry/files/test.pdf';
                    let context = this.getUIContext().getHostContext();
                    print.print(\[fileUri.getUriFromPath(filePath)\], context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error('print err ' + JSON.stringify(error));
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}

#### print.print11+

print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes, context: Context): Promise<PrintTask>

Prints a file. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| jobName | string | Yes | Name of the file to print, for example, **test.pdf**. The printer uses the [onStartLayoutWrite](#onstartlayoutwrite11) API to send the **fd** of the empty PDF file to the API caller. The API caller uses the new print attributes to update the file to print. |
| printAdapter | [PrintDocumentAdapter](#printdocumentadapter11) | Yes | [PrintDocumentAdapter](#printdocumentadapter11) API instance implemented by a third-party application. |
| printAttributes | [PrintAttributes](#printattributes11) | Yes | Print attributes. |
| context | Context | Yes | UIAbilityContext used to start the system print UI. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<[PrintTask](#printtask)\> | Print result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
    build() {
        Scroll() {
            Column({ space: 10 }) {
                Button("Print").width('90%').height(50).onClick(() => {
                    let jobName : string = "jobName";
                    let printAdapter : print.PrintDocumentAdapter | null = null;
                    let printAttributes : print.PrintAttributes = {
                        copyNumber: 1,
                        pageRange: {
                            startPage: 0,
                            endPage: 5,
                            pages: \[\]
                        },
                        pageSize: print.PrintPageType.PAGE\_ISO\_A3,
                        directionMode: print.PrintDirectionMode.DIRECTION\_MODE\_AUTO,
                        colorMode: print.PrintColorMode.COLOR\_MODE\_MONOCHROME,
                        duplexMode: print.PrintDuplexMode.DUPLEX\_MODE\_NONE
                    }
                    let context = this.getUIContext().getHostContext();

                    print.print(jobName, printAdapter, printAttributes, context).then((printTask: print.PrintTask) => {
                        printTask.on('succeed', () => {
                            console.info('print state is succeed');
                        })
                        // ...
                    }).catch((error: BusinessError) => {
                        console.error('print err ' + JSON.stringify(error));
                    })
                })
            }
            .justifyContent(FlexAlign.Center)
            .constraintSize({ minHeight: '100%' })
            .width('100%')
        }
        .height('100%')
    }
}

#### PrintAttributes11+

Defines the print attributes.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| copyNumber | number | No | Yes | Number of printed file copies. The default value is **1**. |
| pageRange | [PrintPageRange](#printpagerange11) | No | Yes | Page range of the file to print. |
| pageSize | [PrintPageSize](#printpagesize11) | [PrintPageType](#printpagetype11) | No | Yes | Page size of the file to print. |
| directionMode | [PrintDirectionMode](#printdirectionmode11) | No | Yes | Print direction mode. |
| colorMode | [PrintColorMode](#printcolormode11) | No | Yes | Color mode of the files to print. |
| duplexMode | [PrintDuplexMode](#printduplexmode11) | No | Yes | Duplex mode of the files to print. |

#### PrintPageRange11+

Defines the print range.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| startPage | number | No | Yes | Start page. The default value is **1**. |
| endPage | number | No | Yes | End page. The default value is the maximum number of pages of the file to be printed. |
| pages | Array<number> | No | Yes | Page range set of the file to print. The default value is empty. |

#### PrintPageSize11+

Defines the size of the printed page.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| id | string | No | No | Paper size ID. |
| name | string | No | No | Paper size name. |
| width | number | No | No | Page width, in millimeters. |
| height | number | No | No | Page height, in millimeters. |

#### PrintDirectionMode11+

Enumerates the print direction modes.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| DIRECTION\_MODE\_AUTO | 0 | Automatic. |
| DIRECTION\_MODE\_PORTRAIT | 1 | Portrait mode. |
| DIRECTION\_MODE\_LANDSCAPE | 2 | Landscape mode. |

#### PrintColorMode11+

Enumerates the color modes.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| COLOR\_MODE\_MONOCHROME | 0 | Black and white. |
| COLOR\_MODE\_COLOR | 1 | Color. |

#### PrintDuplexMode11+

Enumerates the duplex modes.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| DUPLEX\_MODE\_NONE | 0 | Simplex (single-sided). |
| DUPLEX\_MODE\_LONG\_EDGE | 1 | Duplex (double-sided) with flipping on long edge. |
| DUPLEX\_MODE\_SHORT\_EDGE | 2 | Duplex (double-sided) with flipping on short edge. |

#### PrintPageType11+

Enumerates the print page types.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PAGE\_ISO\_A3 | 0 | A3. |
| PAGE\_ISO\_A4 | 1 | A4. |
| PAGE\_ISO\_A5 | 2 | A5. |
| PAGE\_JIS\_B5 | 3 | B5. |
| PAGE\_ISO\_C5 | 4 | C5. |
| PAGE\_ISO\_DL | 5 | DL. |
| PAGE\_LETTER | 6 | Letter. |
| PAGE\_LEGAL | 7 | Legal. |
| PAGE\_PHOTO\_4X6 | 8 | 4 x 6 photo paper. |
| PAGE\_PHOTO\_5X7 | 9 | 5 x 7 photo paper. |
| PAGE\_INT\_DL\_ENVELOPE | 10 | International envelope DL. |
| PAGE\_B\_TABLOID | 11 | B Tabloid. |

#### PrintDocumentAdapterState11+

Enumerates the print job states.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PREVIEW\_DESTROY | 0 | The preview fails. |
| PRINT\_TASK\_SUCCEED | 1 | The print job is successful. |
| PRINT\_TASK\_FAIL | 2 | The print job is failed. |
| PRINT\_TASK\_CANCEL | 3 | The print job is canceled. |
| PRINT\_TASK\_BLOCK | 4 | The print job is blocked. |

#### PrintFileCreationState11+

Enumerates the print file creation status.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINT\_FILE\_CREATED | 0 | The print file is created successfully. |
| PRINT\_FILE\_CREATION\_FAILED | 1 | The print file fails to be created. |
| PRINT\_FILE\_CREATED\_UNRENDERED | 2 | The print file is successfully created but not rendered. |

#### PrinterState14+

Enumerates the printer states.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINTER\_ADDED | 0 | A new printer is added. |
| PRINTER\_REMOVED | 1 | The printer is removed. |
| PRINTER\_CAPABILITY\_UPDATED | 2 | The printer is updated. |
| PRINTER\_CONNECTED | 3 | The printer is connected. |
| PRINTER\_DISCONNECTED | 4 | The printer is disconnected. |
| PRINTER\_RUNNING | 5 | The printer is running. |

#### PrintJobState14+

Enumerates the print job states.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINT\_JOB\_PREPARE | 0 | The printer is prepared for the print job. |
| PRINT\_JOB\_QUEUED | 1 | The print job is on the print queue of the printer. |
| PRINT\_JOB\_RUNNING | 2 | The print job is being executed. |
| PRINT\_JOB\_BLOCKED | 3 | The print job is blocked. |
| PRINT\_JOB\_COMPLETED | 4 | The print job is complete. |

#### PrintJobSubState14+

Enumerates the print job substates.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINT\_JOB\_COMPLETED\_SUCCESS | 0 | The print job is successful. |
| PRINT\_JOB\_COMPLETED\_FAILED | 1 | The print job is failed. |
| PRINT\_JOB\_COMPLETED\_CANCELLED | 2 | The print job is canceled by user. |
| PRINT\_JOB\_COMPLETED\_FILE\_CORRUPTED | 3 | The print file is corrupted. |
| PRINT\_JOB\_BLOCK\_OFFLINE | 4 | The printer is offline. |
| PRINT\_JOB\_BLOCK\_BUSY | 5 | The printer is occupied by another process. |
| PRINT\_JOB\_BLOCK\_CANCELLED | 6 | The print job is canceled due to a block. |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_PAPER | 7 | The printer is out of paper. |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_INK | 8 | The printer is out of ink. |
| PRINT\_JOB\_BLOCK\_OUT\_OF\_TONER | 9 | The printer is out of toner. |
| PRINT\_JOB\_BLOCK\_JAMMED | 10 | The printer is in a paper jam. |
| PRINT\_JOB\_BLOCK\_DOOR\_OPEN | 11 | The printer door is open. |
| PRINT\_JOB\_BLOCK\_SERVICE\_REQUEST | 12 | Print service request. |
| PRINT\_JOB\_BLOCK\_LOW\_ON\_INK | 13 | The printer is low on ink. |
| PRINT\_JOB\_BLOCK\_LOW\_ON\_TONER | 14 | The printer is low on toner. |
| PRINT\_JOB\_BLOCK\_REALLY\_LOW\_ON\_INK | 15 | The printer is extremely low on ink. |
| PRINT\_JOB\_BLOCK\_BAD\_CERTIFICATE | 16 | The print certificate is incorrect. |
| PRINT\_JOB\_BLOCK\_DRIVER\_EXCEPTION20+ | 17 | The print driver is abnormal. |
| PRINT\_JOB\_BLOCK\_ACCOUNT\_ERROR | 18 | There is an error with the printer account. |
| PRINT\_JOB\_BLOCK\_PRINT\_PERMISSION\_ERROR | 19 | There is an error with the printer permission. |
| PRINT\_JOB\_BLOCK\_PRINT\_COLOR\_PERMISSION\_ERROR | 20 | There is an error with the color printing permission. |
| PRINT\_JOB\_BLOCK\_NETWORK\_ERROR | 21 | The printer fails to connect to the network. |
| PRINT\_JOB\_BLOCK\_SERVER\_CONNECTION\_ERROR | 22 | The printer fails to connect to the server. |
| PRINT\_JOB\_BLOCK\_LARGE\_FILE\_ERROR | 23 | There is an error with a large file printing. |
| PRINT\_JOB\_BLOCK\_FILE\_PARSING\_ERROR | 24 | There is an error with file parsing. |
| PRINT\_JOB\_BLOCK\_SLOW\_FILE\_CONVERSION | 25 | The file conversion is slow. |
| PRINT\_JOB\_RUNNING\_UPLOADING\_FILES | 26 | The file is uploading. |
| PRINT\_JOB\_RUNNING\_CONVERTING\_FILES | 27 | The file is converting. |
| PRINT\_JOB\_BLOCK\_FILE\_UPLOADING\_ERROR18+ | 30 | The file fails to be uploaded. |
| PRINT\_JOB\_BLOCK\_DRIVER\_MISSING20+ | 34 | The print driver is missing. |
| PRINT\_JOB\_BLOCK\_INTERRUPT20+ | 35 | The print job is interrupted. |
| PRINT\_JOB\_BLOCK\_PRINTER\_UNAVAILABLE20+ | 98 | The printer is unavailable. |
| PRINT\_JOB\_BLOCK\_UNKNOWN | 99 | There is an unknown error with the printer. |

#### PrintErrorCode14+

Enumerates the print error codes.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| E\_PRINT\_NONE | 0 | No error. |
| E\_PRINT\_NO\_PERMISSION | 201 | No permission. |
| E\_PRINT\_INVALID\_PARAMETER | 401 | Invalid parameters. |
| E\_PRINT\_GENERIC\_FAILURE | 13100001 | Printing failure. |
| E\_PRINT\_RPC\_FAILURE | 13100002 | RPC failure. |
| E\_PRINT\_SERVER\_FAILURE | 13100003 | Print service failure. |
| E\_PRINT\_INVALID\_EXTENSION | 13100004 | Invalid printer extension. |
| E\_PRINT\_INVALID\_PRINTER | 13100005 | Invalid printer. |
| E\_PRINT\_INVALID\_PRINT\_JOB | 13100006 | Invalid print job. |
| E\_PRINT\_FILE\_IO | 13100007 | Incorrect file input/output. |
| E\_PRINT\_TOO\_MANY\_FILES18+ | 13100010 | Excessive files. Maximum number: 99. |

#### ApplicationEvent14+

Enumerates print application events.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| APPLICATION\_CREATED | 0 | Starts the print application. |
| APPLICATION\_CLOSED\_FOR\_STARTED | 1 | Closes the print application by clicking **Start**. |
| APPLICATION\_CLOSED\_FOR\_CANCELED | 2 | Closes the print application by clicking **Cancel**. |

#### print.addPrinterToDiscovery14+

addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>

Adds a printer to the printer discovery list. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerInformation | [PrinterInformation](#printerinformation14) | Yes | The added printer. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Result of adding a printer to the printer discovery list. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOps'
};
print.addPrinterToDiscovery(printerInformation).then(() => {
    console.info('addPrinterToDiscovery success');
}).catch((error: BusinessError) => {
    console.error('addPrinterToDiscovery error : ' + JSON.stringify(error));
})

#### print.updatePrinterInDiscovery14+

updatePrinterInDiscovery(printerInformation: PrinterInformation): Promise<void>

Updates the printer capabilities to the printer discovery list. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerInformation | [PrinterInformation](#printerinformation14) | Yes | Printer whose capability is to be updated. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Result of updating the printer capabilities to the printer discovery list. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testPageSize : print.PrintPageSize = {
    id : 'ISO\_A4',
    name : 'iso\_a4\_210x297mm',
    width : 8268,
    height : 11692
};

let testCapability : print.PrinterCapabilities = {
    supportedPageSizes : \[testPageSize\],
    supportedColorModes : \[print.PrintColorMode.COLOR\_MODE\_MONOCHROME\],
    supportedDuplexModes : \[print.PrintDuplexMode.DUPLEX\_MODE\_NONE\],
    supportedMediaTypes : \['stationery'\],
    supportedQualities : \[print.PrintQuality.QUALITY\_NORMAL\],
    supportedOrientations : \[print.PrintOrientationMode.ORIENTATION\_MODE\_PORTRAIT\],
    options : 'testOptions'
};

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    capability : testCapability,
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOptions'
};
print.updatePrinterInDiscovery(printerInformation).then(() => {
    console.info('updatePrinterInDiscovery success');
}).catch((error: BusinessError) => {
    console.error('updatePrinterInDiscovery error : ' + JSON.stringify(error));
})

#### print.removePrinterFromDiscovery14+

removePrinterFromDiscovery(printerId: string): Promise<void>

Removes a printer from the printer discovery list. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerId | string | Yes | Printer to remove. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Result of removing a printer from the printer discovery list. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = 'testPrinterId';
print.removePrinterFromDiscovery(printerId).then(() => {
    console.info('removePrinterFromDiscovery success');
}).catch((error: BusinessError) => {
    console.error('removePrinterFromDiscovery error : ' + JSON.stringify(error));
})

#### print.getPrinterInformationById14+

getPrinterInformationById(printerId: string): Promise<PrinterInformation>

Obtains printer information based on the printer ID. This API uses a promise to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerId | string | Yes | Printer ID used to obtain information. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<[PrinterInformation](#printerinformation14)\> | Printer information obtained based on the printer ID. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = 'testPrinterId';
print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
    console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
}).catch((error: BusinessError) => {
    console.error('getPrinterInformationById error : ' + JSON.stringify(error));
})

#### PrinterInformation14+

Defines the printer information.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| printerId | string | No | No | Printer ID. |
| printerName | string | No | No | Printer name. |
| printerStatus | [PrinterStatus](#printerstatus14) | No | No | Printer state. |
| description | string | No | Yes | Printer description. |
| capability | [PrinterCapabilities](#printercapabilities14) | No | Yes | Printer capabilities. |
| uri | string | No | Yes | Printer URI. |
| printerMake | string | No | Yes | Printer model. |
| preferences18+ | [PrinterPreferences](#printerpreferences18) | No | Yes | Printer preferences. |
| alias18+ | string | No | Yes | Printer alias. |
| options | string | No | Yes | Printer details. |

#### PrinterCapabilities14+

Defines the printer capabilities.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| supportedPageSizes | Array<[PrintPageSize](#printpagesize11)\> | No | No | List of paper sizes supported by the printer. |
| supportedColorModes | Array<[PrintColorMode](#printcolormode11)\> | No | No | List of color modes supported by the printer. |
| supportedDuplexModes | Array<[PrintDuplexMode](#printduplexmode11)\> | No | No | List of single- and double-sided modes supported by the printer. |
| supportedMediaTypes | Array<string> | No | Yes | List of paper types supported by the printer. |
| supportedQualities | Array<[PrintQuality](#printquality14)\> | No | Yes | List of print quality supported by the printer. |
| supportedOrientations | Array<[PrintOrientationMode](#printorientationmode14)\> | No | Yes | List of print directions supported by the printer. |
| options | string | No | Yes | Printer capability details. |

#### PrintQuality14+

Enumerates the print qualities.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| QUALITY\_DRAFT | 3 | Draft |
| QUALITY\_NORMAL | 4 | Standard |
| QUALITY\_HIGH | 5 | High |

#### PrintOrientationMode14+

Enumerates the print directions.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| ORIENTATION\_MODE\_PORTRAIT | 0 | Portrait mode. |
| ORIENTATION\_MODE\_LANDSCAPE | 1 | Landscape mode. |
| ORIENTATION\_MODE\_REVERSE\_LANDSCAPE | 2 | Reverse landscape mode. |
| ORIENTATION\_MODE\_REVERSE\_PORTRAIT | 3 | Reverse portrait mode. |
| ORIENTATION\_MODE\_NONE | 4 | Adaptive mode. |

#### PrinterStatus14+

Enumerates the printer states.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINTER\_IDLE | 0 | The printer is idle. |
| PRINTER\_BUSY | 1 | The printer is busy. |
| PRINTER\_UNAVAILABLE | 2 | The printer is unavailable. |

#### PrinterPreferences18+

Defines the printer preferences.

**System capability**: SystemCapability.Print.PrintFramework

**Attributes**

| **Name** | **Type** | **Read-Only** | **Optional** | **Description** |
| :-- | :-- | :-- | :-- | :-- |
| defaultDuplexMode | [PrintDuplexMode](#printduplexmode11) | No | Yes | Default duplex mode. |
| defaultPrintQuality | [PrintQuality](#printquality14) | No | Yes | Default print quality. |
| defaultMediaType | string | No | Yes | Default paper type. |
| defaultPageSizeId | string | No | Yes | ID of the default paper size. The value can be a standard paper size defined by the International Organization for Standardization (ISO), for example, ISO\_A4, or a non-standard paper size defined in the system, for example, Custom.178 × 254 mm. |
| defaultOrientation | [PrintOrientationMode](#printorientationmode14) | No | Yes | Default print orientation. |
| borderless | boolean | No | Yes | Whether to print without margins. The value **true** means to print without margins, and **false** means the opposite. The default value is **false**. |
| options | string | No | Yes | Other fields in the printer preferences. The fields are queried from the printer or obtained from the printer driver and stored in the string in JSON format. |

#### PrinterEvent18+

Enumerates printer-related events.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| PRINTER\_EVENT\_ADDED | 0 | Printer added. |
| PRINTER\_EVENT\_DELETED | 1 | Printer deleted. |
| PRINTER\_EVENT\_STATE\_CHANGED | 2 | Printer state changed. |
| PRINTER\_EVENT\_INFO\_CHANGED | 3 | Printer information changed. |
| PRINTER\_EVENT\_PREFERENCE\_CHANGED | 4 | Printer preferences changed. |
| PRINTER\_EVENT\_LAST\_USED\_PRINTER\_CHANGED | 5 | The last used printer changed. |

#### DefaultPrinterType18+

Enumerates default printer types.

**System capability**: SystemCapability.Print.PrintFramework

| **Name** | **Value** | **Description** |
| :-- | :-- | :-- |
| DEFAULT\_PRINTER\_TYPE\_SET\_BY\_USER | 0 | The printer set by the user serves as the default printer. |
| DEFAULT\_PRINTER\_TYPE\_LAST\_USED\_PRINTER | 1 | The printer used last time serves as the default printer. |

#### print.getAddedPrinters18+

getAddedPrinters(): Promise<Array<string>>

Obtains the list of printers added to the system. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.getAddedPrinters().then((printers: string\[\]) => {
    console.info('getAddedPrinters success ' + JSON.stringify(printers));
    // ...
}).catch((error: BusinessError) => {
    console.error('failed to getAddedPrinters because ' + JSON.stringify(error));
})

#### PrinterChangeCallback18+

type PrinterChangeCallback = (event: PrinterEvent, printerInformation: PrinterInformation) => void

Defines a callback that takes the printer event and printer information as parameters.

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| event | [PrinterEvent](#printerevent18) | Yes | Printer event. |
| printerInformation | [PrinterInformation](#printerinformation14) | Yes | Printer information. |

#### print.on18+

on(type: 'printerChange', callback: PrinterChangeCallback): void

Registers a listener for the printer change events.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | 'printerChange' | Yes | Printer change event. |
| callback | [PrinterChangeCallback](#printerchangecallback18) | Yes | Callback to be invoked when the printer changes. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';

// Trigger this callback when an added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);

#### print.off18+

off(type: 'printerChange', callback?: PrinterChangeCallback): void

Unregisters the listener for printer state change events. This API uses a callback to return the result.

**Required permissions**: ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | 'printerChange' | Yes | Printer change event. |
| callback | [PrinterChangeCallback](#printerchangecallback18) | No | Callback to unregister. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { print } from '@kit.BasicServicesKit';

// Trigger this callback when an added printer is changed.
let onPrinterChange =
    (event: print.PrinterEvent, printerInformation: print.PrinterInformation) => {
        console.info('printerChange, event: ' + event + ', printerInformation: ' + JSON.stringify(printerInformation));
    };
print.on('printerChange', onPrinterChange);
print.off('printerChange');

#### print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>, callback: AsyncCallback<void>): void

Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| extensionList | Array<string> | Yes | List of [PrintExtensionAbilities](../ohos-app-ability-printextensionability-printextensionability/document.md) to be loaded. The list members are the bundle names of the applications with print extension abilities. An empty list indicates that all extension abilities are loaded. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Load all print extension abilities.
let extensionList: string\[\] = \[\];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string\[\] = \['com.myapplication.test'\];
print.startDiscoverPrinter(extensionList, (err: BusinessError) => {
    if (err) {
        console.error('failed to start Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start Discover Printer success');
    }
})

#### print.startDiscoverPrinter20+

startDiscoverPrinter(extensionList: Array<string>): Promise<void>

Discovers printers by specifying the extension list. The discovered printers contain the specified print extension abilities. If an empty extension list is specified, all extension abilities are loaded. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| extensionList | Array<string> | Yes | List of [PrintExtensionAbilities](../ohos-app-ability-printextensionability-printextensionability/document.md) to be loaded. The list members are the bundle names of the applications with print extension abilities. An empty list indicates that all extension abilities are loaded. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Load all print extension abilities.
let extensionList: string\[\] = \[\];
// Specify the bundle name of your applications to load required print extension abilities during printer discovery.
// let extensionList: string\[\] = \['com.myapplication.test'\];
print.startDiscoverPrinter(extensionList).then(() => {
    console.info('start Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to start Discovery because : ' + JSON.stringify(error));
})

#### print.stopDiscoverPrinter20+

stopDiscoverPrinter(callback: AsyncCallback<void>): void

Stops discovering printers. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter((err: BusinessError) => {
    if (err) {
        console.error('failed to stop Discover Printer because : ' + JSON.stringify(err));
    } else {
        console.info('stop Discover Printer success');
    }
})

#### print.stopDiscoverPrinter20+

stopDiscoverPrinter(): Promise<void>

Stops discovering printers. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.stopDiscoverPrinter().then(() => {
    console.info('stop Discovery success');
}).catch((error: BusinessError) => {
    console.error('failed to stop Discovery because : ' + JSON.stringify(error));
})

#### print.connectPrinter20+

connectPrinter(printerId: string, callback: AsyncCallback<void>): void

Connects to a printer by printer ID. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerId | string | Yes | Printer ID. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId: string = 'printerId\_32';
print.connectPrinter(printerId, (err: BusinessError) => {
    if (err) {
        console.error('failed to connect Printer because : ' + JSON.stringify(err));
    } else {
        console.info('start connect Printer success');
    }
})

#### print.connectPrinter20+

connectPrinter(printerId: string): Promise<void>

Connects to a printer by printer ID. This API uses a promise to return the result.

**Required permissions**: ohos.permission.MANAGE\_PRINT\_JOB or ohos.permission.PRINT

**System capability**: SystemCapability.Print.PrintFramework

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| printerId | string | Yes | Printer ID. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Error Codes of the Print Service](../../../error-codes/print-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | the application does not have permission to call this function. |

**Example**

import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId: string = 'printerId\_32';
print.connectPrinter(printerId).then(() => {
    console.info('start connect Printer success');
}).catch((error: BusinessError) => {
    console.error('failed to connect Printer because : ' + JSON.stringify(error));
})
