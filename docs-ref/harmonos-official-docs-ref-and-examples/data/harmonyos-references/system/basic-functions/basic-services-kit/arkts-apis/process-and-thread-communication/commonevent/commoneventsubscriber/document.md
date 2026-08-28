# commonEventSubscriber

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/-TUstbU1T6G5UpdUDMpsIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC3EA0D5F7221A7849F1D3086A9F9BDA95E6FB0A06743CC59ADB7C8B76722D4B)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### CommonEventSubscriber

The **CommonEventSubscriber** module provides APIs for describing the common event subscriber.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

## How to Use

Before using the **CommonEventSubscriber** module, you must obtain a **subscriber** object by calling **commonEventManager.createSubscriber**.

import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define a subscriber to save the created subscriber object for subsequent subscription and unsubscription.
let subscriber: commonEventManager.CommonEventSubscriber | null = null;
// Subscriber information.
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    events: \['event'\]
};
// Create a subscriber.
subscriber = commonEventManager.createSubscriberSync(subscribeInfo);

#### \[h2\]getCode

getCode(callback: AsyncCallback<number>): void

Obtains the result code (number type) of an ordered common event. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.getCode((err: BusinessError, code: number) => {
  if (err) {
    console.error(\`Failed to get code. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting code, code is ${JSON.stringify(code)}\`);
});

#### \[h2\]getCode

getCode(): Promise<number>

Obtains the result code (number type) of an ordered common event. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

subscriber.getCode().then((code: number) => {
  console.info(\`Succeeded in getting code, code is ${JSON.stringify(code)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get code. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getCodeSync10+

getCodeSync(): number

Obtains the result code (number type) of an ordered common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| number | Result code of an ordered common event. |

**Example**

let code: number = subscriber.getCodeSync();
console.info(\`Succeeded in getting code, code is ${JSON.stringify(code)}\`);

#### \[h2\]setCode

setCode(code: number, callback: AsyncCallback<void>): void

Sets the result code (number type) of an ordered common event. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setCode(1, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set code. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in setting code.\`);
});

#### \[h2\]setCode

setCode(code: number): Promise<void>

Sets the result code (number type) of an ordered common event. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setCode(1).then(() => {
  console.info(\`Succeeded in setting code.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set code. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setCodeSync10+

setCodeSync(code: number): void

Sets the result code (number type) of an ordered common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

try {
  subscriber.setCodeSync(1);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`Failed to set code. Code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]getData

getData(callback: AsyncCallback<string>): void

Obtains the result data (string type) of an ordered common event. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

// Obtain the result data (string type) of an ordered common event.
subscriber.getData((err: BusinessError, data: string) => {
  if (err) {
    console.error(\`Failed to get data. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting data, data is ${JSON.stringify(data)}\`);
});

#### \[h2\]getData

getData(): Promise<string>

Obtains the result data (string type) of an ordered common event. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Example**

subscriber.getData().then((data: string) => {
  console.info(\`Succeeded in getting data, data is ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get data. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getDataSync10+

getDataSync(): string

Obtains the result data (string type) of an ordered common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| string | Result data of an ordered common event. |

**Example**

let data: string = subscriber.getDataSync();
console.info(\`Succeeded in getting data, data is ${data}\`);

#### \[h2\]setData

setData(data: string, callback: AsyncCallback<void>): void

Sets the result data (string type) of an ordered common event. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Result data of an ordered common event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setData('publish\_data\_changed', (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set data. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in setting data.\`);
});

#### \[h2\]setData

setData(data: string): Promise<void>

Sets the result data (string type) of an ordered common event. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Result data of an ordered common event. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setData('publish\_data\_changed').then(() => {
  console.info(\`Succeeded in setting data.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set data. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setDataSync10+

setDataSync(data: string): void

Sets the result data (string type) of an ordered common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Result data of an ordered common event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

try {
  subscriber.setDataSync('publish\_data\_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`Failed to set data. Code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]setCodeAndData

setCodeAndData(code: number, data: string, callback:AsyncCallback<void>): void

Sets the result code and data of an ordered common event. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |
| data | string | Yes | Result data of an ordered common event. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setCodeAndData(1, 'publish\_data\_changed', (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to set code and data. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in setting code and data.\`);
});

#### \[h2\]setCodeAndData

setCodeAndData(code: number, data: string): Promise<void>

Sets the result code and data of an ordered common event. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |
| data | string | Yes | Result data of an ordered common event. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.setCodeAndData(1, 'publish\_data\_changed').then(() => {
  console.info(\`Succeeded in setting code and data.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to set code and data. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setCodeAndDataSync10+

setCodeAndDataSync(code: number, data: string): void

Sets the result code and data of an ordered common event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Result code of an ordered common event. |
| data | string | Yes | Result data of an ordered common event. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

try {
  subscriber.setCodeAndDataSync(1, 'publish\_data\_changed');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`Failed to set code and data. Code is ${err.code}, message is ${err.message}\`);
}

#### \[h2\]isOrderedCommonEvent

isOrderedCommonEvent(callback: AsyncCallback<boolean>): void

Checks whether the current common event is an ordered common event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the common event is an ordered one; returns **false** if the common event is an unordered one. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.isOrderedCommonEvent((err: BusinessError, isOrdered:boolean) => {
  if (err) {
    console.error(\`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`isOrderedCommonEvent ${JSON.stringify(isOrdered)}\`);
});

#### \[h2\]isOrderedCommonEvent

isOrderedCommonEvent(): Promise<boolean>

Checks whether the current common event is an ordered common event. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if the common event is an ordered one; returns **false** if the common event is an unordered one. |

**Example**

subscriber.isOrderedCommonEvent().then((isOrdered:boolean) => {
  console.info(\`isOrderedCommonEvent ${JSON.stringify(isOrdered)}\`);
}).catch((err: BusinessError) => {
  console.error(\`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isOrderedCommonEventSync10+

isOrderedCommonEventSync(): boolean

Checks whether the current common event is an ordered common event.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the common event is an ordered one; returns **false** if the common event is an unordered one. |

**Example**

let isOrdered: boolean = subscriber.isOrderedCommonEventSync();
console.info(\`isOrderedCommonEventSync ${JSON.stringify(isOrdered)}\`);

#### \[h2\]isStickyCommonEvent

isStickyCommonEvent(callback: AsyncCallback<boolean>): void

Checks whether a common event is a sticky one. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the common event is a sticky one; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.isStickyCommonEvent((err: BusinessError, isSticky:boolean) => {
  if (err) {
    console.error(\`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`isStickyCommonEvent ${JSON.stringify(isSticky)}\`);
});

#### \[h2\]isStickyCommonEvent

isStickyCommonEvent(): Promise<boolean>

Checks whether a common event is a sticky one. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if the common event is a sticky one; returns **false** otherwise. |

**Example**

subscriber.isStickyCommonEvent().then((isSticky:boolean) => {
  console.info(\`isStickyCommonEvent ${JSON.stringify(isSticky)}\`);
}).catch((err: BusinessError) => {
  console.error(\`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]isStickyCommonEventSync10+

isStickyCommonEventSync(): boolean

Checks whether a common event is a sticky one.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the common event is a sticky one; returns **false** otherwise. |

**Example**

let isSticky: boolean = subscriber.isStickyCommonEventSync();
console.info(\`isStickyCommonEventSync ${JSON.stringify(isSticky)}\`);

#### \[h2\]abortCommonEvent

abortCommonEvent(callback: AsyncCallback<void>): void

Aborts an ordered common event. This API is used with [finishCommonEvent](#finishcommonevent9). After the abort, the common event is not sent to the next subscriber. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.abortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to abort common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in aborting common event.\`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in finishing common event.\`);
});

#### \[h2\]abortCommonEvent

abortCommonEvent(): Promise<void>

Aborts this ordered common event. This API is used with [finishCommonEvent](#finishcommonevent9). After the abort, the common event is not sent to the next subscriber. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

subscriber.abortCommonEvent().then(() => {
  console.info(\`Succeeded in aborting common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to abort common event. Code is ${err.code}, message is ${err.message}\`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(\`Succeeded in finishing common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]abortCommonEventSync10+

abortCommonEventSync(): void

Aborts this ordered common event synchronously. This API is used with [finishCommonEvent](#finishcommonevent9). After the abort, the common event is not sent to the next subscriber.

**System capability**: SystemCapability.Notification.CommonEvent

**Example**

subscriber.abortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(\`Succeeded in finishing common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]clearAbortCommonEvent

clearAbortCommonEvent(callback: AsyncCallback<void>): void

Clears the abort state of an ordered common event. Use this API together with [finishCommonEvent](#finishcommonevent9), and the common event can be passed to the next subscriber. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.clearAbortCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in clearing abort common event.\`);
});
subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in finishing common event.\`);
});

#### \[h2\]clearAbortCommonEvent

clearAbortCommonEvent(): Promise<void>

Clears the abort state of this ordered common event. Use this API together with [finishCommonEvent](#finishcommonevent9), and the common event can be passed to the next subscriber. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

subscriber.clearAbortCommonEvent().then(() => {
  console.info(\`Succeeded in clearing abort common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}\`);
});
subscriber.finishCommonEvent().then(() => {
  console.info(\`Succeeded in finishing common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]clearAbortCommonEventSync10+

clearAbortCommonEventSync(): void

Clears the abort state of this ordered common event. Use this API together with [finishCommonEvent](#finishcommonevent9), and the common event can be passed to the next subscriber.

**System capability**: SystemCapability.Notification.CommonEvent

**Example**

subscriber.clearAbortCommonEventSync();
subscriber.finishCommonEvent().then(() => {
  console.info(\`Succeeded in finishing common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getAbortCommonEvent

getAbortCommonEvent(callback: AsyncCallback<boolean>): void

Checks whether this ordered common event should be aborted. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. Returns **true** if the ordered common event is in the abort state; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.getAbortCommonEvent((err: BusinessError, abortEvent: boolean) => {
  if (err) {
    console.error(\`Failed to get abort common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}\`);
});

#### \[h2\]getAbortCommonEvent

getAbortCommonEvent(): Promise<boolean>

Checks whether this ordered common event should be aborted. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. Returns **true** if the ordered common event is in the abort state; returns **false** otherwise. |

**Example**

subscriber.getAbortCommonEvent().then((abortEvent: boolean) => {
  console.info(\`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get abort common event. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getAbortCommonEventSync10+

getAbortCommonEventSync(): boolean

Checks whether this ordered common event should be aborted.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the ordered common event is in the abort state; returns **false** otherwise. |

**Example**

let abortEvent: boolean = subscriber.getAbortCommonEventSync();
console.info(\`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}\`);

#### \[h2\]getSubscribeInfo

getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void

Obtains the subscriber information. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[CommonEventSubscribeInfo](../commoneventsubscribeinfo/document.md)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.getSubscribeInfo((err: BusinessError, subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  if (err) {
    console.error(\`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}\`);
});

#### \[h2\]getSubscribeInfo

getSubscribeInfo(): Promise<CommonEventSubscribeInfo>

Obtains the subscriber information. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CommonEventSubscribeInfo](../commoneventsubscribeinfo/document.md)\> | Promise used to return the result. |

**Example**

subscriber.getSubscribeInfo().then((subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
  console.info(\`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getSubscribeInfoSync10+

getSubscribeInfoSync(): CommonEventSubscribeInfo

Obtains the subscriber information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| [CommonEventSubscribeInfo](../commoneventsubscribeinfo/document.md) | Subscriber information. |

**Example**

let subscribeInfo1 = subscriber.getSubscribeInfoSync();
console.info(\`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo1)}\`);

#### \[h2\]finishCommonEvent9+

finishCommonEvent(callback: AsyncCallback<void>): void

Finishes this ordered common event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |

**Example**

subscriber.finishCommonEvent((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`Succeeded in finishing common event.\`);
});

#### \[h2\]finishCommonEvent9+

finishCommonEvent(): Promise<void>

Finishes this ordered common event. This API uses a promise to return the result.

**System capability**: SystemCapability.Notification.CommonEvent

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

subscriber.finishCommonEvent().then(() => {
  console.info(\`Succeeded in finishing common event.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to finish common event. Code is ${err.code}, message is ${err.message}\`);
});
