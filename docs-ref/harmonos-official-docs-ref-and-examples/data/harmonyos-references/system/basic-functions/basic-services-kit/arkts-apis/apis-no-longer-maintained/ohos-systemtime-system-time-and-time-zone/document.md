# @ohos.systemTime (System Time and Time Zone)

The **systemTime** module provides system time and time zone features. You can use the APIs of this module to set and obtain the system time and time zone.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/CXEv19n0Tluv7j4KZzoE_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18B1F4E46630C1780343ACB2C46953E89EB784FC1306CED48AB4B059F033A5DB)

-   The APIs of this module are no longer maintained since API version 9. You are advised to use [@ohos.systemDateTime (system time and time zone)](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md).
-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { systemTime } from '@kit.BasicServicesKit';

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/LxwDI6RwSbmQwHZLl4U31w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6968EAC2DB6175D7A1E45FCBAA0D44740FBD5DDE23F2428CE4B9ED1D1FB24A0B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getTime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the time elapsed since the Unix epoch. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting currentTime: ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Bj7kTZfISh2o7udu3f9G6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFB09C039477E4CD044E7A6CBD3464305A9644B809139FB5FDD5DDEA8DC04640)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getTime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the time elapsed since the Unix epoch. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting currentTime : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getCurrentTime8+(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since the Unix epoch. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/4xcN2YkERXq9fl0OAtDVsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECA891D9AF3FDBD4CC073815B754E50A9184F92A71C9325EDE09FFCD8E0A484B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getTime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegettime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

The default value is false.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the time elapsed since the Unix epoch. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getCurrentTime().then((time: number) => {
    console.info(\`Succeeded in getting currentTime : ${time}\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get currentTime. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_yt3TNzNRW6bdIAPPPOyfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FAEBB6673E5F11E1D482F03CA995956A2AD8389E4C17AA6DCF26701E5E8E7E6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real active time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/asd9uRaTRpGKre-aSsuI4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7214BE5050776EBBB1D2321784F4986971A209293DD54958EE8F2B1AB3004954)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real active time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealActiveTime8+(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/bQ7fjLKORsqXCM8h6u0mMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A751BE8DE0228810A13A3B2C886BD850F3BF7DD453E4B36B39520B181BBA4EC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the time elapsed since system startup, excluding the deep sleep time. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealActiveTime().then((time: number) => {
    console.info(\`Succeeded in getting real active time : ${time}\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real active time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/8NhCH2tXRluiS_ow37BqVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=158AA10445A742806F911E9BA58919196CA5F3CF2B17E1B986588DC6C5BC6EC8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | Yes | 
Whether the time to return is in nanoseconds.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealTime8+(deprecated)

getRealTime(callback: AsyncCallback<number>): void

Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Zb-CXCE7SRSfAqByGzcbVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DA6826C233C134C5EF4C8A36085B1505E00F000E3EACBDD3793AF8FF8E73803)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting real time : ${time}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getRealTime8+(deprecated)

getRealTime(isNano?: boolean): Promise<number>

Obtains the time elapsed since system startup, including the deep sleep time. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/z8Y-_9gSSb-Fd64E1Q-BIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C73B036C55E2F9063B45122922953AAEFD396E1B253767AF69BC9F00BD96D5B8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getUptime](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegetuptime10) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isNano | boolean | No | 
Whether the time to return is in nanoseconds. The default value is **false**.

The default value is false.

\- **true**: The result is in nanoseconds.

\- **false**: The result is in milliseconds.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the time elapsed since system startup, including the deep sleep time. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getRealTime().then((time: number) => {
    console.info(\`Succeeded in getting real time : ${time}\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get real time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getDate8+(deprecated)

getDate(callback: AsyncCallback<Date>): void

Obtains the current system date. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/RaryzjM-TVeT_M56adMtLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82E966252238EB190DD3FF824EA98C3508416C1E30045EC929B3BD718FCF2635)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use the **new Date()** method described in [How do I convert a string in time format to a Date object](https://gitcode.com/openharmony/docs/blob/weekly_20251117/en/application-dev/faqs/faqs-arkui-arkts.md#how-do-i-convert-a-string-in-time-format-to-a-date-object-api-version-9) instead, which returns the **Date** instance object.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Date> | Yes | Callback used to return the current system date. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.info(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting date : ${date}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getDate8+(deprecated)

getDate(): Promise<Date>

Obtains the current system date. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/3fHAhcL2S_2QV0cvr4VhBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92ACDB3E0663ED8279E069F98255D3331350BC1EA810C3E29342C511F455A39E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use the **new Date()** method described in [How do I convert a string in time format to a Date object](https://gitcode.com/openharmony/docs/blob/weekly_20251117/en/application-dev/faqs/faqs-arkui-arkts.md#how-do-i-convert-a-string-in-time-format-to-a-date-object-api-version-9) instead, which returns the **Date** instance object.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Date> | Promise used to return the current system date. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getDate().then((date: Date) => {
    console.info(\`Succeeded in getting date : ${date}\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get date. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getTimezone8+(deprecated)

getTimezone(callback: AsyncCallback<string>): void

Obtains the system time zone. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/YD9c8t99QB-DahDb2jQJ_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D344D1B59A72E8798480A4EF675E641D449B8E872CF1063C1F4BB773AD9FA548)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getTimezone](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegettimezone) instead.

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the system time zone. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone((error: BusinessError, data: string) => {
    if (error) {
      console.info(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in getting timezone : ${data}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.getTimezone8+(deprecated)

getTimezone(): Promise<string>

Obtains the system time zone. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/qwGnM_jSQa-qbIloTrgoiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC4F733E22E1B23F79D8357685DCA85373BE2D7FF64035B753C12AD72ED41EE8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [systemDateTime.getTimezone](../../others/ohos-systemdatetime-system-time-and-time-zone/document.md#systemdatetimegettimezone-1) instead.

**System capability**: SystemCapability.MiscServices.Time

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the system time zone. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.getTimezone().then((data: string) => {
    console.info(\`Succeeded in getting timezone: ${data}\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to get timezone. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setTime(deprecated)

setTime(time : number, callback : AsyncCallback<void>) : void

Sets the system time. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/AUCaSg0kRrCiworUiz-VUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B84C1D19AF3B89B70DB82AC72A66D64686CBB1A9D091A5D8146438ABC1BF4CF4)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| time | number | Yes | Timestamp to set, in milliseconds. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Set the system time to 2021-01-20 02:36:25.
let time = 1611081385000;
try {
  systemTime.setTime(time, (error: BusinessError) => {
    if (error) {
      console.info(\`Failed to setting time. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in setting time\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setTime(deprecated)

setTime(time : number) : Promise<void>

Sets the system time. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/2c2-jcj0QNazq3hlRJFV4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8D0F18AA08793F8A7CEC1C8AA2F9A9C80A52292255128EA1184ECDBCBE7A727)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| time | number | Yes | Timestamp to set, in milliseconds. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Set the system time to 2021-01-20 02:36:25.
let time = 1611081385000;
try {
  systemTime.setTime(time).then(() => {
    console.info(\`Succeeded in setting time.\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to setting time. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set time. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setDate(deprecated)

setDate(date: Date, callback: AsyncCallback<void>): void

Sets the system date. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/diWp0vVyQN-bzGn7OgtELw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CDE6768E6FF69C2D8174A4B5DA2F24D92B88ED136ACE8F9D3C39C0D2C5E2105)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | Yes | Target date to set. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date, (error: BusinessError) => {
    if (error) {
      console.info(\`Failed to setting date. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in setting date.\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set date. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setDate(deprecated)

setDate(date: Date): Promise<void>

Sets the system date. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/i4GEJm09Qk-gDyt-gLyDJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A22E0C9BDB276CC57D03127755553DD7AA0283C776FA3A0143674BA5EB559E0C)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | Yes | Target date to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let date = new Date();
try {
  systemTime.setDate(date).then(() => {
    console.info(\`Succeeded in setting date.\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to setting date. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set date. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string, callback: AsyncCallback<void>): void

Sets the system time zone. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Asm4LVw4TTqcB3XdOczwnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D63A6DA35780D5711D0C5FDFCEAFFE8D0035310B334A83053236BD6E6E776FCB)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME\_ZONE

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timezone | string | Yes | System time zone to set. For details, see [Supported System Time Zones](#supported-system-time-zones). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai', (error: BusinessError) => {
    if (error) {
      console.info(\`Failed to setting timezone. message: ${error.message}, code: ${error.code}\`);
      return;
    }
    console.info(\`Succeeded in setting timezone.\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set timezone. message: ${error.message}, code: ${error.code}\`);
}

#### systemTime.setTimezone(deprecated)

setTimezone(timezone: string): Promise<void>

Sets the system time zone. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/5XKnPpJvSVezFWFA12yjzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CE4E63CB18230B0AB62DC4C3A74EFD338E121EA3D4F539A46F616411CCA60BF)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_TIME\_ZONE

**System capability**: SystemCapability.MiscServices.Time

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timezone | string | Yes | System time zone to set. For details, see [Supported System Time Zones](#supported-system-time-zones). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Time and Time Zone Service Error Codes](../../../error-codes/time-and-time-zone-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| \-1 | Parameter check failed, permission denied, or system error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemTime.setTimezone('Asia/Shanghai').then(() => {
    console.info(\`Succeeded in setting timezone.\`);
  }).catch((error: BusinessError) => {
    console.info(\`Failed to setting timezone. message: ${error.message}, code: ${error.code}\`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.info(\`Failed to set timezone. message: ${error.message}, code: ${error.code}\`);
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
