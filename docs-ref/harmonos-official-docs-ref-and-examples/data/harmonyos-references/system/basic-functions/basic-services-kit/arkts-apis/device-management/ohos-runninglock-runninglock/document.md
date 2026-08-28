# @ohos.runningLock (RunningLock)

The **runningLock** module provides APIs for creating, querying, holding, and releasing running locks. A running lock enables the proximity sensor to turn on or off the screen, or prevents the device from entering sleep mode when the screen is off. For details about the running lock types, see [RunningLockType](#runninglocktype).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/cbT55c4rQnCSnVnQCwKKPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=025E38D257D8C59A85B0FD5E2337551BA73DAD3983472217A255369DF82A1AF7)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {runningLock} from '@kit.BasicServicesKit';

#### runningLock.isSupported9+

isSupported(type: RunningLockType): boolean

**API description**: Checks whether the system supports the running lock of a specified type.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the running lock. The value must be an enum. |

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the specified type of the running lock is supported, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

try {
    let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL);
    console.info('BACKGROUND type supported: ' + isSupported);
} catch(err) {
    console.error('check supported failed, err: ' + err);
}

#### runningLock.create9+

create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

**API description**: Creates a running lock. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **RunningLock** object. The value must be a string. |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the **RunningLock** object. The value must be an enum. |
| callback | AsyncCallback<[RunningLock](#runninglock)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and data is the created **RunningLock** object. Otherwise, **err** is an error object. **AsyncCallback** has encapsulated an API of the **RunningLock** class. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**Example**

runningLock.create('running\_lock\_test', runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});

#### runningLock.create9+

create(name: string, type: RunningLockType): Promise<RunningLock>

**API description**: Creates a running lock. This API uses a promise to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **RunningLock** object. The value must be a string. |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the **RunningLock** object. The value must be an enum. |

**Returns**

| Type | Description |
| :-- | :-- |
| Promise<[RunningLock](#runninglock)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**Example**

runningLock.create('running\_lock\_test', runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/VoCkWPg_S9WFfvfjLa0fWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C36B712F919C95329D2235FF5D08C8661DB4825CC95615185B8E1CA6F99ACC8B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [runningLock.isSupported](#runninglockissupported9) instead.

**API description**: Checks whether the system supports the running lock of a specified type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the running lock. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the query result obtained, where the value **true** indicates that the specified type of the running lock is supported and **false** indicates the opposite. Otherwise, **err** is an error object. |

**Example**

runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND, (err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('BACKGROUND lock support status: ' + data);
    } else {
        console.error('check BACKGROUND lock support status failed, err: ' + err);
    }
});

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/jxR26g_BQHKqj03uLNv47g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0D0BB9FEC571FE876E325B7120D501EF365E03EA231CB8B2FCBB0E18863E1F9)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [runningLock.isSupported](#runninglockissupported9) instead.

**API description**: Checks whether the system supports the running lock of a specified type. This API uses a promise to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the running lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the specified type of the running lock is supported, and the value **false** indicates the opposite. |

**Example**

runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND)
.then((data: boolean) => {
    console.info('BACKGROUND lock support status: ' + data);
})
.catch((err: Error) => {
    console.error('check BACKGROUND lock support status failed, err: ' + err);
});

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/fAA90fsdQKeJtWPUCKVVXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC1145C673D9F6AF1FD7BC78D4B990741346AFCCF7E9A84FBDA01F56028952BF)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [runningLock.create](#runninglockcreate9) instead.

**API description**: Creates a running lock. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **RunningLock** object. |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the **RunningLock** object to be created. |
| callback | AsyncCallback<[RunningLock](#runninglock)\> | Yes | Callback used to return the result. If a lock is successfully created, **err** is **undefined** and **data** is the created **RunningLock**. Otherwise, **err** is an error object. |

**Example**

runningLock.createRunningLock('running\_lock\_test', runningLock.RunningLockType.BACKGROUND, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9_71muVAQo2VOP4kiso8sQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=272C9A800C3E1C0FF7517B143EF0ED274707B6DC0091146B0084D73B43414C5D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [runningLock.create](#runninglockcreate9) instead.

**API description**: Creates a running lock. This API uses a promise to return the result.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **RunningLock** object. |
| type | [RunningLockType](#runninglocktype) | Yes | Type of the **RunningLock** object to be created. |

**Returns**

| Type | Description |
| :-- | :-- |
| Promise<[RunningLock](#runninglock)\> | Promise used to return the result. |

**Example**

runningLock.createRunningLock('running\_lock\_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});

#### RunningLock

Defines a **RunningLock** object.

#### \[h2\]hold9+

hold(timeout: number): void

**API description**: Holds a running lock.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | 
Duration for locking and holding the **RunningLock** object, in ms.

The value must be a number:

**\-1**: The lock is permanently held and needs to be released automatically.

**0**: The lock is released 3 seconds after the timer expires by default.

\> 0: The lock is released based on the input value after the timer expires.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 201 | If the permission is denied. |

**Example**

// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static holdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.hold(500);
            console.info('hold running lock success');
        } else {
            runningLock.create('running\_lock\_test', runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.hold(500);
                        console.info('hold running lock success');
                    } catch(err) {
                        console.error('hold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}

#### \[h2\]unhold9+

unhold(): void

**API description**: Releases this running lock.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | If the permission is denied. |

**Example**

// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static unholdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.unhold();
            console.info('unhold running lock success');
        } else {
            runningLock.create('running\_lock\_test', runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.unhold();
                        console.info('unhold running lock success');
                    } catch(err) {
                        console.error('unhold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}

#### \[h2\]isHolding9+

isHolding(): boolean

**API description**: Checks whether this running lock is being held.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the **RunningLock** object is held; and the value **false** indicates that the **RunningLock** object is released. |

**Example**

// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static isHoldingRunningLock(): void {
        if (RunningLockTest.recordLock) {
            let isHolding = RunningLockTest.recordLock.isHolding();
            console.info('check running lock holding status: ' + isHolding);
        } else {
            runningLock.create('running\_lock\_test', runningLock.RunningLockType.PROXIMITY\_SCREEN\_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    let isHolding = lock.isHolding();
                    console.info('check running lock holding status: ' + isHolding);
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}

#### \[h2\]lock(deprecated)

lock(timeout: number): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/zPGyhLYMR3C0B2C4j68Z_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3786DF3D6406F4CF661E2D4F167B7C8E8D08526E1E008A193FF874AEF50832F7)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [RunningLock.hold](#hold9) instead.

**API description**: Locks a running lock.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | Duration for locking and holding the **RunningLock** object, in ms. |

**Example**

runningLock.createRunningLock('running\_lock\_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.lock(500);
    console.info('create running lock and lock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});

#### \[h2\]unlock(deprecated)

unlock(): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JzOBUlygRg-K0-x92HKMlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFFC561D0EF020CB8F5FFBFEC67CBC72F83A830D1464596142D83A7A3F394DCD)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [RunningLock.unhold](#unhold9) instead.

**API description**: Releases this running lock.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Required permission**: ohos.permission.RUNNING\_LOCK

**Example**

runningLock.createRunningLock('running\_lock\_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.unlock();
    console.info('create running lock and unlock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});

#### \[h2\]isUsed(deprecated)

isUsed(): boolean

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/bz9GubrOR4ubFrChz2httw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F02E3F6FB405FA8033FBE6EBB46B82B2DB88C8DD217359B80795B3ADBC19334)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [RunningLock.isHolding](#isholding9) instead.

**API description**: Checks whether this running lock is used.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the **RunningLock** object is held; and the value **false** indicates that the **RunningLock** object is released. |

**Example**

runningLock.createRunningLock('running\_lock\_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    let isUsed = lock.isUsed();
    console.info('check running lock used status: ' + isUsed);
})
.catch((err: Error) => {
    console.error('check running lock used status failed, err: ' + err);
});

#### RunningLockType

Enumerates the types of **RunningLock** objects.

**System capability**: SystemCapability.PowerManager.PowerManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BACKGROUND(deprecated) | 1 | 
A lock that prevents the system from entering sleep mode when the screen is off.

**NOTE**

This parameter is supported since API version 7 and deprecated since API version 10.

 |
| PROXIMITY\_SCREEN\_CONTROL | 2 | A lock that enables the proximity sensor and turns on or off the screen based on the distance between the sensor and the obstacle. |
