# @ohos.systemDateTime (System Time and Time Zone)

The **systemTime** module provides system time and time zone features. You can obtain the system time and time zone by using the following APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/-74gs_KxSIW9pHR8lRaH8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C78A6047C8E9CD1DE1CD4F3958258B6205A2BD27CBF71BE7421806A6EEAFD0CB)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { systemDateTime } from '@kit.BasicServicesKit';

#### TimeType10+

Enumerates the types of time to obtain.

**System capability**: SystemCapability.MiscServices.Time

| Name | Value | Description |
| :-- | :-- | :-- |
| STARTUP | 0 | Number of milliseconds elapsed since system startup, including the deep sleep time. |
| ACTIVE | 1 | Number of milliseconds elapsed since system startup, excluding the deep sleep time. |

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/7BzREsQyTgK9JNAotpfOTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D92A40852D256580312CA887C0C2499B88CA7B5707D963FA5465A4272E5DE3A4)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getTime10+](#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the time elapsed since the Unix epoch. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting currentTime : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/2sKT6F-US_eW_pXnKrPWHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF220F0D6BC9785D60E9B78F4F52DB90E8AE1AB161CA122EFEAC71A4BFD1FE3A)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getTime10+](#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the time elapsed since the Unix epoch, in milliseconds. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting currentTime : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since the Unix epoch. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/7g90vM4WREOca0tdHf7m4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6DD47AA5D4CACA152329FC73612F73E7A423A226F94118089DA8E5861816A28)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getTime10+](#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the timestamp that has elapsed since the Unix epoch. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime().then((time: number) => {
    console.info(\`Succeeded in getting currentTime : ${time}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/YgqYpVDpT5qs-Np3v9L_Cg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B9C4BDB1883EA826106EE6CF04B21510000F27F77D1EC23EFF16C9ADB753BF3)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real active time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/cT3rIrZaRxmTikeNJHc64g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6163CCDC8A50D6C617B5C6DCE7F76187B1D85715ADF4A42212843EE4BFD29EA)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real active time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Tiulp4e7QTSW_-nRJQ_9nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F39EAAD8FBF84FBF86ED83E92A49C078AFE10A551B7960922FBA13FE42145B98)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the time elapsed since system startup, excluding the deep sleep time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(\`Succeeded in getting real active time : ${time}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/5uxPjdoaReenFsjeejz5rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=604F2A84E53F1FE6B9366B7C875A89ADC84DABE6C10486193B52D71215FBD30F)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealTime(deprecated)

getRealTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bnxN65igSNaxKo_LfMjesQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31E9C6358456DC7ACFC344B8A6A03F592BC30FFFDA251DA882D1C6DB4DB7974D)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getRealTime(deprecated)

getRealTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since system startup, including the deep sleep time. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/kDqY-M17Tl-XBeCGQJ9TVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35D88B1F0395DBD813E458C0CF35DEB58D4DC657B0699DC7D143D0C8B3897A88)

This API is supported since API version 9 and deprecated since API version 12. You are advised to use [systemDateTime.getUptime10+](#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the time elapsed since system startup, including the deep sleep time. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime().then((time: number) => {
    console.info(\`Succeeded in getting real time : ${time}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getTime10+

getTime(isNanoseconds?: boolean): number

Obtains the time elapsed since the Unix epoch. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNanoseconds | boolean | No | 
Whether the time to return is in nanoseconds.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

The default value is **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Time elapsed since the Unix epoch. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getTime(true)
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get time. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getUptime10+

getUptime(timeType: TimeType, isNanoseconds?: boolean): number

Obtains the time elapsed since system startup. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeType | [TimeType](#timetype10) | Yes | Type of the time to be obtained. The value can only be STARTUP or ACTIVE. |
| isNanoseconds | boolean | No | 
Whether the time to return is in nanoseconds.

\- **true** means that the return result is in nanoseconds (ns).

\- **false** means that the return result is in milliseconds (ms).

The default value is **false**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Time elapsed since system startup. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification

failed.This error code was added due to missing issues.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getUptime(systemDateTime.TimeType.ACTIVE, false);
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get uptime. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getDate(deprecated)

getDate(callback: AsyncCallback<Date>): void

Obtains the current system date. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/zg4zhdkkQXmNL1P0FJhMmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47E12382ECA8B1F6F061D67A07612975B632A72AECBEBA23C520E7EEE1B8786A)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use the **new Date()** method described in [How do I convert a string in time format to a Date object](https://gitcode.com/openharmony/docs/blob/weekly_20251117/en/application-dev/faqs/faqs-arkui-arkts.md#how-do-i-convert-a-string-in-time-format-to-a-date-object-api-version-9) instead, which returns the **Date** instance object.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Date> | Yes | Callback used to return the current system date. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.error(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting date : ${date}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getDate(deprecated)

getDate(): Promise<Date>

Obtains the current system date. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/1YUFN8X3RsK15Ht1XPaqlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB4ED4B1336F6C985CCB25BBC72B0A6A8EDBD07A68641131936871AFD7C7DB2C)

This API is supported since API version 9 and deprecated since API version 10. You are advised to use the **new Date()** method described in [How do I convert a string in time format to a Date object](https://gitcode.com/openharmony/docs/blob/weekly_20251117/en/application-dev/faqs/faqs-arkui-arkts.md#how-do-i-convert-a-string-in-time-format-to-a-date-object-api-version-9) instead, which returns the **Date** instance object.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Date> | Promise used to return the current system date. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.System error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate().then((date: Date) => {
    console.info(\`Succeeded in getting date : ${date}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getTimezone

getTimezone(callback: AsyncCallback<string>): void

Obtains the system time zone. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the system time zone. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.error(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in get timezone : ${data}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getTimezone

getTimezone(): Promise<string>

Obtains the system time zone. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the system time zone. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone().then((data: string) => {
    console.info(\`Succeeded in getting timezone: ${data}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
}

#### systemDateTime.getTimezoneSync10+

getTimezoneSync(): string

Obtains the system time zone in synchronous mode.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| string | System time zone. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timezone: string = systemDateTime.getTimezoneSync();
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
}

#### Supported System Time Zones

The following table lists the supported system time zones and the respective offset (unit: h) between each time zone and time zone 0.

| Time Zone | Offset |
| :-- | :-- |
| Antarctica/McMurdo | 12 |
| America/Argentina/Buenos\_Aires | \-3 |
| Australia/Sydney | 10 |
| America/Noronha | \-2 |
| America/St\_Johns | \-3 |
| Africa/Kinshasa | 1 |
| America/Santiago | \-3 |
| Asia/Shanghai | 8 |
| Asia/Nicosia | 3 |
| Europe/Berlin | 2 |
| America/Guayaquil | \-5 |
| Europe/Madrid | 2 |
| Pacific/Pohnpei | 11 |
| America/Godthab | \-2 |
| Asia/Jakarta | 7 |
| Pacific/Tarawa | 12 |
| Asia/Almaty | 6 |
| Pacific/Majuro | 12 |
| Asia/Ulaanbaatar | 8 |
| America/Mexico\_City | \-5 |
| Asia/Kuala\_Lumpur | 8 |
| Pacific/Auckland | 12 |
| Pacific/Tahiti | \-10 |
| Pacific/Port\_Moresby | 10 |
| Asia/Gaza | 3 |
| Europe/Lisbon | 1 |
| Europe/Moscow | 3 |
| Europe/Kiev | 3 |
| Pacific/Wake | 12 |
| America/New\_York | \-4 |
| Asia/Tashkent | 5 |

#### systemDateTime.getAutoTimeStatus21+

getAutoTimeStatus(): boolean

Obtains the switch status of the automatic time setting. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Switch status of the automatic time setting.

\- **true**: The automatic time setting is on.

\- **false**: The automatic time setting is off.

 |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md) and [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 13000001 | Network connection error or OS error. Possible causes: 1.System memory is insufficient; 2.Calls the underlying system interface failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch(e) {
  let error = e as BusinessError;
  console.error(\`Failed to get autotime status. message: ${error.message}, code: ${error.code}\`);
}
