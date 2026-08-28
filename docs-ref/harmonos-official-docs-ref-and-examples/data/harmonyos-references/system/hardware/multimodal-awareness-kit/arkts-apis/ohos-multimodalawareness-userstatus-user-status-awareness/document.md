# @ohos.multimodalAwareness.userStatus (User Status Awareness)

The **UserStatus** module, designed for user state awareness, empowers the system to perceive specific conditions of users, such as determining their age group.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/EKUrVvIHRKGa-5aCQF61jA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62E8098EF27CAA8569E7E068E483B8599857CE8C7BBE07BBB168A226ACC12C74)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { userStatus } from '@kit.MultimodalAwarenessKit';

#### UserAgeGroup

Enumerates the user age groups, for example, child or adult.

**System capability**: SystemCapability.MultimodalAwareness.UserStatus

| Name | Value | Description |
| :-- | :-- | :-- |
| OTHERS | 0 | Adult. |
| CHILD | 1 | Child. |

#### UserClassification

Defines the user age group detection result.

**System capability**: SystemCapability.MultimodalAwareness.UserStatus

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ageGroup | [UserAgeGroup](#useragegroup) | No | Yes | User age group, for example, child or adult. |
| confidence | float | No | Yes | Confidence of the detection result. The value is a floating point number ranging from 0 to 1. A larger value indicates a higher confidence. |

#### userStatus.on('userAgeGroupDetected')

on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void

Enables the age group detection function.

When the function is enabled, the application can recommend content based on the age group detection result.

**System capability**: SystemCapability.MultimodalAwareness.UserStatus

**Device behavior differences**: This API can be called on phones. If it is called on other devices, error code **801** is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zxhW__1lTHS6K-XbLg9GfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75A3CF0633D9931526E4A9BAFBF1FE2A8516DC8563DDFCB00BC3625742921AD1)

This API is supported only on some phones. Error code **801** is returned if it is called on unsupported phones.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **userAgeGroupDetected** indicates the event of enabling age group detection. |
| callback | Callback<[UserClassification](#userclassification)\> | Yes | Callback used to return the detection result. |

**Error codes**

For details about the error codes, see [User Status Awareness Error Codes](../../error-codes/user-status-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 33900001 | 
Service exception. Possible causes:

1\. System error, such as a null pointer and container-related exception.

2\. Node-API invocation exception, such as invalid Node-API status.

 |
| 33900002 | 

Subscription failed. Possible causes:

1\. Callback registration failed.

2\. Failed to bind the native object to the JS wrapper.

3\. Node-API invocation exception, such as invalid Node-API status.

4\. IPC request exception.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    userStatus.on('userAgeGroupDetected', (data: userStatus.UserClassification) => {
        console.info('callback succeeded, ageGroup:' + data.ageGroup + ", confidence:" + data.confidence);
    });
    console.info("on succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed on and err code is " + error.code);
}

#### userStatus.off('userAgeGroupDetected')

off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void

Disables the age group detection function.

**System capability**: SystemCapability.MultimodalAwareness.UserStatus

**Device behavior differences**: This API can be called on phones. If it is called on other devices, error code **33900003** is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ZcuoSAeJQPeIcvD38bFovw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062410Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DE4E42DAB5D246D50ABB890F30F0CDC347A5D97861D816275836F866B05672C)

This API is supported only on some phones. Error code **33900003** is returned if it is called on unsupported phones.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **userAgeGroupDetected** indicates the event of enabling age group detection. |
| callback | Callback<[UserClassification](#userclassification)\> | No | Callback used to return the detection result. |

**Error codes**

For details about the error codes, see [User Status Awareness Error Codes](../../error-codes/user-status-awareness-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. Function can not work correctly due to limited device capabilities. |
| 33900001 | 
Service exception. Possible causes:

1\. System error, such as a null pointer and container-related exception.

2\. Node-API invocation exception, such as invalid Node-API status.

 |
| 33900003 | 

Unsubscription failed. Possible causes:

1\. Callback failure.

2\. Node-API invocation exception, such as invalid Node-API status.

3\. IPC request exception.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    userStatus.off('userAgeGroupDetected');
    console.info("off succeeded");
} catch (err) {
    let error = err as BusinessError;
    console.error("Failed off and err code is " + error.code);
}
