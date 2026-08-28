# @ohos.i18n (Internationalization)

This module provides system-related and enhanced [i18n](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-l10n) capabilities, such as locale management, phone number formatting, and calendar, through supplementary i18n APIs that are not defined in [ECMA 402](https://dev.ecma-international.org/publications-and-standards/standards/ecma-402/). The [intl](../ohos-intl-internationalization/document.md) module provides basic i18n capabilities through the standard i18n APIs defined in ECMA 402. It works with the **i18n** module to provide a complete suite of i18n capabilities. The terms used in the APIs are defined as follows:

-   Pattern string, which is a string consisting of [Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and custom text enclosed by single quotation marks.
-   Skeleton string: a string that consists of [Unicode date field symbols](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) and does not support custom text.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/-UDaz83nT7iUHtLOExEigA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=756B1208D0F532E57EB1377CE515084BFD13445DF19AF3F0420FD3774916DC67)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module are based on the [CLDR](https://cldr.unicode.org) internationalization database. The processing results of the APIs may be adjusted as the CLDR standard evolves. For example, the return value of the [date and time formatting API](#simplenumberformat18) is used only for UI display. Do not hardcode the return value or make assumptions about the return value. Otherwise, version compatibility problems may occur. API version 12 corresponds to [CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42). For details about data changes, see the official CLDR documentation.
    
-   Since API version 11, some APIs of this module are supported in ArkTS widgets.
    

#### Modules to Import

import { i18n } from '@kit.LocalizationKit';

#### System9+

Provides system attribute configuration functions, including translating language and country/region names, obtaining the list of supported languages and countries/regions, and obtaining the system language and region.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getDisplayCountry9+

static getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string

Obtains the country/region display name in the specified language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| country | string | Yes | Valid country/region code. For details, see [System Locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works). |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value **true** means to display the text in title case format, and the value **false** means to display the text in the default case format of the locale. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Country/region display name in the specified language. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Description**

The error message of 890001 is subject to the actual error.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let displayCountry: string = i18n.System.getDisplayCountry('CN', 'en-GB'); // displayCountry = 'China'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.getDisplayCountry failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getDisplayLanguage9+

static getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string

Obtains the language display name in the specified language.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | Valid language ID. For details, see [System Locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works). |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value **true** means to display the text in title case format, and the value **false** means to display the text in the default case format of the locale. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Language display name in the specified language. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Obtain the display name of Chinese in English.
  let displayLanguage: string = i18n.System.getDisplayLanguage('zh', 'en-GB'); // displayLanguage = 'Chinese'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.getDisplayLanguage failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getSystemLanguages9+

static getSystemLanguages(): Array<string>

Obtains the list of system languages.

Since API version 11, this API is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of system languages. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// systemLanguages = \[ 'ug', 'bo', 'zh-Hant', 'en-Latn-US', 'zh-Hans' \]
let systemLanguages: Array<string> = i18n.System.getSystemLanguages();

#### \[h2\]getSystemCountries9+

static getSystemCountries(language: string): Array<string>

Obtains the list of countries/regions supported for the specified language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | [Valid language ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works). |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of countries/regions supported for the specified language. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Description**

The error message of 890001 is subject to the actual error.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // systemCountries = \[ 'ZW', 'YT', 'YE', ..., 'ER', 'CN', 'DE' \]
  let systemCountries: Array<string> = i18n.System.getSystemCountries('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.getSystemCountries failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]isSuggested9+

static isSuggested(language: string, region?: string): boolean

Checks whether a language is a suggested language in the specified region. It can be used for region-based language recommendation or language-based region recommendation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | [Valid language ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), for example, **zh**. |
| region | string | No | 
[Valid country/region code](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), for example, **CN**.

The default value is the country/region of the SIM card.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether a language is a suggested language. The value **true** indicates that the language is a suggested language of the region, the the value false indicates the opposite. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Description**

The error message of 890001 is subject to the actual error.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let isSuggestedCountry: boolean = i18n.System.isSuggested('zh', 'CN'); // isSuggestedCountry = true
  isSuggestedCountry = i18n.System.isSuggested('en'); // Check whether a language is a suggested language for the current system region.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.isSuggested failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getSystemLanguage9+

static getSystemLanguage(): string

Obtains the current system language. To listen for system language changes, enable listening for [COMMON\_EVENT\_LOCALE\_CHANGED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_locale_changed). For details, see [System Language and Region](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-system-language-region#how-to-develop).

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Language ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.System.getSystemLanguage(); // If the system language is simplified Chinese, then systemLanguage is 'zh-Hans'.

#### \[h2\]getSystemRegion9+

static getSystemRegion(): string

Obtains the current system country/region. To listen for system region changes, enable listening for [COMMON\_EVENT\_LOCALE\_CHANGED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_locale_changed). For details, see [System Language and Region](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-system-language-region#how-to-develop).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Country/region ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let systemRegion: string = i18n.System.getSystemRegion(); // If the system region is China, then systemRegion is CN.

#### \[h2\]getSystemLocale(deprecated)

static getSystemLocale(): string

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [System.getSystemLocaleInstance](#getsystemlocaleinstance20) instead.

Obtains the current system locale.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Locale ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let systemLocale: string = i18n.System.getSystemLocale(); // If the system language is simplified Chinese and the system region is China, then systemLocale is zh-Hans-CN.

#### \[h2\]getSystemLocaleInstance20+

static getSystemLocaleInstance(): Intl.Locale

Obtains the current system locale. To listen for system locale changes, enable listening for [COMMON\_EVENT\_LOCALE\_CHANGED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_locale_changed). For details, see [System Language and Region](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-system-language-region#how-to-develop).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [Intl.Locale](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | System locale. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let systemLocale: Intl.Locale = i18n.System.getSystemLocaleInstance();

#### \[h2\]is24HourClock9+

static is24HourClock(): boolean

Checks whether the 24-hour clock is used. To listen for system time format changes, enable listening for [COMMON\_EVENT\_TIME\_CHANGED](../../../../system/basic-functions/basic-services-kit/arkts-apis/process-and-thread-communication/system-common-events/document.md#common_event_time_changed). For details, see [User Preference](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-user-preferences#how-to-develop).

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the 24-hour clock is used. The value **true** indicates that the 24-hour clock is used, the the value **false** means the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.System.is24HourClock(); // If the 24-hour clock is used, then is24HourClock is true.

#### \[h2\]getPreferredLanguageList9+

static getPreferredLanguageList(): Array<string>

Obtains the list of preferred languages.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of preferred languages. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.System.getPreferredLanguageList();

#### \[h2\]getFirstPreferredLanguage9+

static getFirstPreferredLanguage(): string

Obtains the first language in the preferred language list.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | First language in the preferred language list. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.System.getFirstPreferredLanguage();

#### \[h2\]setAppPreferredLanguage11+

static setAppPreferredLanguage(language: string): void

Sets the preferred language of the application. Resources are loaded in the preferred language when the application is launched. If the preferred language is set to **default**, the application's language will be the same as the system language, and the setting will take effect upon cold starting of the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | [Valid language ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works) or **default**. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  i18n.System.setAppPreferredLanguage('zh');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.setAppPreferredLanguage failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getAppPreferredLanguage9+

static getAppPreferredLanguage(): string

Obtains the preferred language of an application.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Preferred language of the application. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let appPreferredLanguage: string = i18n.System.getAppPreferredLanguage();

#### \[h2\]getUsingLocalDigit9+

static getUsingLocalDigit(): boolean

Checks whether use of local digits is enabled.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether use of local digits is enabled. The value **true** indicates that use of local digits is enabled, and the value **false** indicates the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let usingLocalDigit: boolean = i18n.System.getUsingLocalDigit();

#### \[h2\]getSimplifiedLanguage15+

static getSimplifiedLanguage(language?: string): string

Obtains the simplified representation of a language. For example, the simplified representation of **en-Latn-US** is **en**, and that of **en-Latn-GB** is **en-GB**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | No | [Valid language ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works). The default value is the system language. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
If **language** is not passed, the application checks for dialects supported by the system based on the system language and locale. If such a dialect is found, the simplified representation of the dialect is returned. Otherwise, the simplified representation of the system language is returned.

If **language** is passed, the simplified representation of the specified language is returned.

 |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // simplifiedLanguage = 'zh'
  let simplifiedLanguage: string = i18n.System.getSimplifiedLanguage('zh-Hans-CN');
  // Obtain the simplified representation of the current system language.
  let simplifiedSystemLanguage: string = i18n.System.getSimplifiedLanguage();
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.getSimplifiedLanguage failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getTemperatureType18+

static getTemperatureType(): TemperatureType

Obtains the temperature unit of the system.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [TemperatureType](#temperaturetype18) | Temperature unit. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let temperatureType: i18n.TemperatureType = i18n.System.getTemperatureType();

#### \[h2\]getTemperatureName18+

static getTemperatureName(type: TemperatureType): string

Obtains the name of a temperature unit.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [TemperatureType](#temperaturetype18) | Yes | Temperature unit. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Name of the temperature unit, which can be **celsius**, **fahrenheit**, and **kelvin**. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Description**

The error message of 890001 is subject to the actual error.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // temperatureName = 'celsius'
  let temperatureName: string = i18n.System.getTemperatureName(i18n.TemperatureType.CELSIUS);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call System.getTemperatureName failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getFirstDayOfWeek18+

static getFirstDayOfWeek(): WeekDay

Obtains the first day of a week in the system settings.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [WeekDay](#weekday18) | Start day of a week. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let firstDayOfWeek: i18n.WeekDay = i18n.System.getFirstDayOfWeek();

#### TemperatureType18+

Enumerates temperature units.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

| Name | Value | Description |
| :-- | :-- | :-- |
| CELSIUS | 1 | Celsius. |
| FAHRENHEIT | 2 | Fahrenheit. |
| KELVIN | 3 | Kelvin. |

#### WeekDay18+

Enumerates the first day of a week. The value ranges from Monday to Sunday.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

| Name | Value | Description |
| :-- | :-- | :-- |
| MON | 1 | Monday. |
| TUE | 2 | Tuesday. |
| WED | 3 | Wednesday. |
| THU | 4 | Thursday. |
| FRI | 5 | Friday. |
| SAT | 6 | Saturday. |
| SUN | 7 | Sunday. |

#### i18n.isRTL

isRTL(locale: string): boolean

Checks whether a language is an RTL language. For an RTL language, [UI mirroring](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-ui-design#ui-mirroring) is required.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether a language is an RTL language. The value **true** indicates that the language is an RTL language, and the value **false** indicates the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isZhRTL: boolean = i18n.isRTL('zh-CN'); // Since Chinese is not written from right to left, false is returned.
let isArRTL: boolean = i18n.isRTL('ar-EG'); // Since Arabic is written from right to left, true is returned.

#### i18n.getCalendar8+

getCalendar(locale: string, type? : string): Calendar

Obtains the **Calendar** object for the specified locale and calendar type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [Locale ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |
| type | string | No | 
Calendar. The value can be buddhist, chinese, coptic, ethiopic, hebrew, gregory, indian, islamic\_civil, islamic\_tbla, islamic\_umalqura, japanese, or persian.

The default value is the default calendar of the locale. For details about the meanings and application scenarios of different values, see [Calendar Setting](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-calendar) .

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Calendar](#calendar8) | **Calendar** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans', 'chinese'); // Obtain the Calendar object for the Chinese lunar calendar.

#### EntityRecognizer11+

Provides entity recognition capabilities, which can be used to obtain the type and start and end positions of an entity in the text. Currently, supported entities include phone numbers, and date and time.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor11+

constructor(locale?: string)

Creates an **entityRecognizer** object. This object is used to recognize entities in the text for the specified locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | No | 
[Locale ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region, for example, **zh-Hans-CN**.

The default value is the current system locale.

 |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let entityRecognizer: i18n.EntityRecognizer = new i18n.EntityRecognizer('zh-CN');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call new i18n.EntityRecognizer failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]findEntityInfo11+

findEntityInfo(text: string): Array<EntityInfoItem>

Obtains entity information in the **text** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[EntityInfoItem](#entityinfoitem11)\> | List of entities in the text. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let entityRecognizer: i18n.EntityRecognizer = new i18n.EntityRecognizer('zh-CN');
  let phoneNumberText: string = 'If you have any questions, call us by phone 12345678.';
  // phoneNumberEntity\[0\].type = 'phone\_number', phoneNumberEntity\[0\].begin = 8, phoneNumberEntity\[0\].end = 19
  let phoneNumberEntity: Array<i18n.EntityInfoItem> = entityRecognizer.findEntityInfo(phoneNumberText);
  let dateText: string = 'Let's have dinner on December 1, 2023.';
  // dateEntity\[0\].type = 'date', dateEntity\[0\].begin = 2, dateEntity\[0\].end = 12
  let dateEntity: Array<i18n.EntityInfoItem> = entityRecognizer.findEntityInfo(dateText);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call EntityRecognizer.findEntityInfo failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### EntityInfoItem11+

Defines a list of entities.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | string | No | No | Entity type. The value can be **phone\_number** or **date**. **phone\_number** indicates that the entity is a phone number, and **date** indicates that the entity is a date. |
| begin | number | No | No | Start position of the entity in the input string. |
| end | number | No | No | End position of the entity the input string. |

#### Calendar8+

Provides calendar management capabilities, such as calendar name retrieval and date calculation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]setTime8+

setTime(date: Date): void

Sets the date and time for a **Calendar** object based on the input **Date** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | Yes | Date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let date: Date = new Date(2021, 10, 7, 8, 0, 0); // The date and time is 2021.11.07 08:00:00.
calendar.setTime(date);

#### \[h2\]setTime8+

setTime(time: number): void

Sets the date and time for a **Calendar** object based on the input timestamp.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| time | number | Yes | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix epoch. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
calendar.setTime(10540800000);

#### \[h2\]set8+

set(year: number, month: number, date:number, hour?: number, minute?: number, second?: number): void

Sets the year, month, day, hour, minute, and second for this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| year | number | Yes | Year to set. |
| month | number | Yes | Month to set. Note: The month starts from **0**. For example, **0** indicates January. |
| date | number | Yes | Day to set. |
| hour | number | No | Hour to set. The default value is the current system time. |
| minute | number | No | Minute to set. The default value is the current system time. |
| second | number | No | Second to set. The default value is the current system time. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // Set the date and time to 2021.11.1 08:00:00.

#### \[h2\]setTimeZone8+

setTimeZone(timezone: string): void

Sets the time zone of this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timezone | string | Yes | Valid time zone ID, for example, Asia/Shanghai. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');

#### \[h2\]getTimeZone8+

getTimeZone(): string

Obtains the time zone ID of this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Time zone ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTimeZone('Asia/Shanghai');
let timezone: string = calendar.getTimeZone(); // timezone = 'Asia/Shanghai'

#### \[h2\]getFirstDayOfWeek8+

getFirstDayOfWeek(): number

Obtains the first day of a week for this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | First day of a week. The value **1** indicates Sunday, and the value **7** indicates Saturday. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'gregory');
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 1

#### \[h2\]setFirstDayOfWeek8+

setFirstDayOfWeek(value: number): void

Sets the first day of a week for this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Start day of a week. The value **1** indicates Sunday, and the value **7** indicates Saturday. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setFirstDayOfWeek(3);
let firstDayOfWeek: number = calendar.getFirstDayOfWeek(); // firstDayOfWeek = 3

#### \[h2\]getMinimalDaysInFirstWeek8+

getMinimalDaysInFirstWeek(): number

Obtains the minimum number of days in the first week for this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Minimum number of days in the first week of a year. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 1

#### \[h2\]setMinimalDaysInFirstWeek8+

setMinimalDaysInFirstWeek(value: number): void

Sets the minimum number of days in the first week for this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Minimum number of days in the first week of a year. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setMinimalDaysInFirstWeek(3);
let minimalDaysInFirstWeek: number = calendar.getMinimalDaysInFirstWeek(); // minimalDaysInFirstWeek = 3

#### \[h2\]get8+

get(field: string): number

Obtains the values of the calendar attributes in this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | Calendar attributes. The following table lists the supported attribute values. |

| Name | Description |
| :-- | :-- |
| era | Era, for example, AD or BC. |
| year | Year. |
| month | Month. Note: The month starts from **0**. For example, **0** indicates January. |
| date | Date. |
| hour | Wall-clock hour. |
| hour\_of\_day | Hour of day. |
| minute | Minute. |
| second | Second. |
| millisecond | Millisecond. |
| week\_of\_year | Week of year. Note that the algorithm for calculating the first week of a year varies according to regions. For example, the first seven days in a year are the first week. |
| year\_woy | Year used with the week of year field. |
| week\_of\_month | Week of month. |
| day\_of\_week\_in\_month | Day of week in month. |
| day\_of\_year | Day of year. |
| day\_of\_week | Day of week. |
| milliseconds\_in\_day | Milliseconds in day. |
| zone\_offset | Fixed time zone offset in milliseconds (excluding DST). |
| dst\_offset | DST offset in milliseconds. |
| dow\_local | Localized day of week. |
| extended\_year | Extended year, which can be a negative number. |
| julian\_day | Julian day. |
| is\_leap\_month | Whether a month is a leap month. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Value of the calendar attribute. For example, if the year of the internal date of the current **Calendar** object is 1990, **get('year')** returns **1990**. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 10, 1, 8, 0, 0); // Set the date and time to 2021.11.1 08:00:00.
let hourOfDay: number = calendar.get('hour\_of\_day'); // hourOfDay = 8

#### \[h2\]getDisplayName8+

getDisplayName(locale: string): string

Obtains calendar display name in the specified language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Calendar display name in the specified language. For example, **buddhist** is displayed as **Buddhist Calendar** if the locale is **en-US**. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('en-US', 'buddhist');
let calendarName: string = calendar.getDisplayName('zh'); // calendarName = 'Buddhist'

#### \[h2\]isWeekend8+

isWeekend(date?: Date): boolean

Checks whether a given date is a weekend in this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | No | 
Date and time. Note: The month starts from **0**. For example, **0** indicates January.

The default value is current date of the **Calendar** object.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the specified date is a weekend, and the value **false** indicates the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.set(2021, 11, 11, 8, 0, 0); // Set the time to 2021.12.11 08:00:00.
let isWeekend: boolean = calendar.isWeekend(); // isWeekend = true
let date: Date = new Date(2011, 11, 6, 9, 0, 0); // The date and time is 2011-12-06 09:00:00.
isWeekend = calendar.isWeekend(date); // isWeekend = false

#### \[h2\]add11+

add(field: string, amount: number): void

Performs addition or subtraction on the calendar attributes of this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | 
Calendar attribute. The value can be any of the following: **year**, **month**, **week\_of\_year**, **week\_of\_month**, **date**, **day\_of\_year**, **day\_of\_week**, **day\_of\_week\_in\_month**, **hour**, **hour\_of\_day**, **minute**, **second**, **millisecond**.

For details about the values, see [get](#get8).

 |
| amount | number | Yes | Addition or subtraction amount. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.set(2021, 11, 11, 8, 0, 0); // Set the date and time to 2021.12.11 08:00:00.
  calendar.add('year', 8); // 2021 + 8
  let year: number = calendar.get('year'); // year = 2029
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call Calendar.add failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getTimeInMillis11+

getTimeInMillis(): number

Obtains the timestamp of this **Calendar** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unix timestamp, which indicates the number of milliseconds that have elapsed since the Unix epoch. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
calendar.setTime(5000);
let millisecond: number = calendar.getTimeInMillis(); // millisecond = 5000

#### \[h2\]compareDays11+

compareDays(date: Date): number

Compares the current date of this **Calendar** object with the specified date for the difference in the number of days.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | Yes | Date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Difference in the number of days. A positive number indicates that the calendar date is earlier, and a negative number indicates the opposite.

The value is accurate to milliseconds. If the value is less than one day, it is considered as one day.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
  calendar.setTime(5000);
  let date: Date = new Date(6000);
  let diff: number = calendar.compareDays(date); // diff = 1
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call Calendar.compareDays failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### PhoneNumberFormat8+

Provides phone number management capabilities, such as phone number validity verification, formatting, and home location retrieval.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor8+

constructor(country: string, options?: PhoneNumberFormatOptions)

Creates a **PhoneNumberFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| country | string | Yes | Country/region to which the phone number to be formatted belongs. |
| options | [PhoneNumberFormatOptions](#phonenumberformatoptions8) | No | Options for **PhoneNumberFormat** object initialization. The default value is **NATIONAL**. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let option: i18n.PhoneNumberFormatOptions = { type: 'E164' };
let phoneNumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);

#### \[h2\]isValidNumber8+

isValidNumber(phoneNumber: string): boolean

Checks whether the phone number is valid for the country/region in the **PhoneNumberFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number to be checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the phone number is valid. The value **true** indicates that the phone number is valid, and the value **false** indicates the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let isValidNumber: boolean = formatter.isValidNumber('158\*\*\*\*2312'); // isValidNumber = true

#### \[h2\]format8+

format(phoneNumber: string): string

Formats a phone number.

**Description**

Formatting dialed phone numbers is supported since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number to be formatted. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted phone number. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let formatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
// formattedPhoneNumber = '158 \*\*\*\* 2312'
let formattedPhoneNumber: string = formatter.format('158\*\*\*\*2312');

// Format the phone number being dialed.
let option: i18n.PhoneNumberFormatOptions = { type: 'TYPING' };
let typingFormatter: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', option);
let phoneNumber: string = '130493';
let formatResult: string = '';
for (let i = 0; i < phoneNumber.length; i++) {
  formatResult += phoneNumber.charAt(i);
  formatResult = typingFormatter.format(formatResult); // formatResult = '130 493'
}

#### \[h2\]getLocationName9+

getLocationName(phoneNumber: string, locale: string): string

Obtains the home location of a phone number.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. To obtain the home location of a number in other countries/regions, you need to prefix the number with **00** and the country code. |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Home location of the phone number. If the number is invalid, an empty string is returned. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let phonenumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
let locationName: string = phonenumberFormat.getLocationName('158\*\*\*\*2345', 'zh-CN'); // locationName = 'Zhanjiang, Guangdong Province'
let locName: string = phonenumberFormat.getLocationName('0039312\*\*\*\*789', 'zh-CN'); // locName = 'Italy'

#### PhoneNumberFormatOptions8+

Options for **PhoneNumberFormat** object initialization.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | string | No | Yes | 
Type of the phone number. The value can be **E164**, **INTERNATIONAL**, **NATIONAL**, **RFC3966**, or **TYPING**.

\- In API version 8, **type** is mandatory.

\- In API version 9 or later, **type** is optional.

\- In API version 12 or later, TYPING is supported, which indicates that the dialed number is formatted in real time.

 |

#### UnitInfo8+

Defines the measurement unit information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| unit | string | No | No | Name of the measurement unit, for example, **meter**, **inch**, or **cup**. |
| measureSystem | string | No | No | Measurement system. The value can be **SI**, **US**, or **UK**. |

#### i18n.getInstance8+

getInstance(locale?: string): IndexUtil

Creates an **IndexUtil** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | No | 
[System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region.

The default value is the current system locale.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [IndexUtil](#indexutil8) | **IndexUtil** object created based on the specified locale ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');

#### IndexUtil8+

Provides index management capabilities, such as obtaining the locale index list and text index values.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getIndexList8+

getIndexList(): Array<string>

Obtains the index list of the current locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Index list of the current locale. The first and last elements are **...**. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
// indexList = \[ '...', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
//              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '...' \]
let indexList: Array<string> = indexUtil.getIndexList();

#### \[h2\]addLocale8+

addLocale(locale: string): void

Adds the index list of a new locale to the index list of the current locale to form a composite list.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
indexUtil.addLocale('en-US');

#### \[h2\]getIndex8+

getIndex(text: string): string

Obtains the index of the **text** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Index of the **text** object. If no proper index is found, an empty string is returned. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
let index: string = indexUtil.getIndex('hi'); // index = 'H'

#### i18n.getLineInstance8+

getLineInstance(locale: string): BreakIterator

Obtains a **BreakIterator** object. The **BreakIterator** object maintains an internal break iterator that can be used to access various line break points.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | 
[System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region.

The generated [BreakIterator](#breakiterator8) object calculates the positions of line breaks based on the rules of the specified locale.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [BreakIterator](#breakiterator8) | **BreakIterator** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');

#### BreakIterator8+

Provides text line breaking capabilities, such as obtaining, moving, and identifying break points.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]setLineBreakText8+

setLineBreakText(text: string): void

Sets the text to be processed by the **BreakIterator** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.'); // Set the text to be processed.

#### \[h2\]getLineBreakText8+

getLineBreakText(): string

Obtains the text processed by the **BreakIterator** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Text being processed by the **BreakIterator** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let breakText: string = iterator.getLineBreakText(); // breakText = 'Apple is my favorite fruit.'

#### \[h2\]current8+

current(): number

Obtains the position of the break iterator in the text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the break iterator in the text. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let currentPos: number = iterator.current(); // currentPos = 0

#### \[h2\]first8+

first(): number

Moves the break iterator to the first line break point, which is always at the beginning of the processed text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Offset of the first line break point in the processed text. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let firstPos: number = iterator.first(); // firstPos = 0

#### \[h2\]last8+

last(): number

Moves the break iterator to the last line break point, which is always the next position after the end of the processed text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Offset of the last line break point in the processed text. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let lastPos: number = iterator.last(); // lastPos = 27

#### \[h2\]next8+

next(index?: number): number

Moves the break iterator backward by the specified number of line break points.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | No | 
Number of line break points for moving the break iterator. The value is an integer.

A positive number means to move the break iterator backward, and a negative number means to move the break iterator forward.

The default value is **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Position of the break iterator in the text after movement.

The value **\-1** is returned if the position of the break iterator is outside of the processed text after movement.

 |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(); // pos = 6
pos = iterator.next(10); // pos = -1

#### \[h2\]previous8+

previous(): number

Moves the break iterator foreward by one line break point.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Position of the break iterator in the text after movement.

The value **\-1** is returned if the position of the break iterator is outside of the processed text after movement.

 |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.first(); // pos = 0
pos = iterator.next(3); // pos = 12
pos = iterator.previous(); // pos = 9

#### \[h2\]following8+

following(offset: number): number

Moves the line break iterator to the line break point after the specified position.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Offset of the line break point. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Position of the break iterator in the text after movement. The value **\-1** is returned if the position of the break iterator is outside of the processed text after movement. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let pos: number = iterator.following(0); // pos = 6
pos = iterator.following(100); // pos = -1
pos = iterator.current(); // pos = 27

#### \[h2\]isBoundary8+

isBoundary(offset: number): boolean

Checks whether the specified position is a line break point.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Specified position in the text. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the specified position is a line break point. The value **true** indicates that the specified position is a line break point, and the value **false** indicates the opposite.

If **true** is returned, the break iterator is moved to the position specified by **offset**. Otherwise, the break iterator is moved to the text line break point after the position specified by **offset**, which is equivalent to calling **following**.

 |

**Example**

import { i18n } from '@kit.LocalizationKit';

let iterator: i18n.BreakIterator = i18n.getLineInstance('en');
iterator.setLineBreakText('Apple is my favorite fruit.');
let isBoundary: boolean = iterator.isBoundary(0); // isBoundary = true;
isBoundary = iterator.isBoundary(5); // isBoundary = false;

#### i18n.getTimeZone

getTimeZone(zoneID?: string): TimeZone

Obtains the **TimeZone** object corresponding to the specified time zone ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| zoneID | string | No | Time zone ID. The default value is the system time zone. |

**Return value**

| Type | Description |
| :-- | :-- |
| [TimeZone](#timezone) | **TimeZone** object corresponding to the time zone ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');

#### TimeZone

Provides time zone management capabilities, such as time zone name translation, offset retrieval, and transition rule retrieval.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getID

getID(): string

Obtains the ID of the specified **TimeZone** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | Time zone ID corresponding to the **TimeZone** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneID: string = timezone.getID(); // timezoneID = 'Asia/Shanghai'

#### \[h2\]getDisplayName

getDisplayName(locale?: string, isDST?: boolean): string

Obtains time zone display name in the specified language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | No | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. The default value is the current system locale. |
| isDST | boolean | No | Whether DST information is displayed. The value **true** indicates that DST information is displayed, and the value **false** indicates the opposite. The default value is **false**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Time zone display name in the specified language. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let timezoneName: string = timezone.getDisplayName('zh-CN', false); // timezoneName = 'China Standard Time'

#### \[h2\]getRawOffset

getRawOffset(): number

Obtains the raw offset of the specified time zone.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Raw offset of the time zone, in milliseconds. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getRawOffset(); // offset = 28800000

#### \[h2\]getOffset

getOffset(date?: number): number

Obtains the offset of the specified time zone at the specified time.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | number | No | Specified time, in milliseconds. The default value is the system time. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Time zone offset, in milliseconds. When the DST is used, the time zone offset is the raw time zone offset plus the DST offset. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.getTimeZone('Asia/Shanghai');
let offset: number = timezone.getOffset(1234567890); // offset = 28800000

#### \[h2\]getAvailableIDs9+

static getAvailableIDs(): Array<string>

Obtains the list of time zone IDs supported by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of time zone IDs supported by the system. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// ids = \['America/Adak', 'America/Anchorage', 'America/Bogota', 'America/Denver', 'America/Los\_Angeles', 'America/Montevideo', 'America/Santiago', 'America/Sao\_Paulo', 'Asia/Ashgabat', 'Asia/Hovd', 'Asia/Jerusalem', 'Asia/Magadan', 'Asia/Omsk', 'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Yerevan', 'Atlantic/Cape\_Verde', 'Australia/Lord\_Howe', 'Europe/Dublin', 'Europe/London', 'Europe/Moscow', 'Pacific/Auckland', 'Pacific/Easter', 'Pacific/Pago-Pago'\]
let ids: Array<string> = i18n.TimeZone.getAvailableIDs();

#### \[h2\]getAvailableZoneCityIDs9+

static getAvailableZoneCityIDs(): Array<string>

Obtains the list of time zone city IDs supported by the system.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of time zone city IDs supported by the system. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// cityIDs = \['Auckland', 'Magadan', 'Lord Howe Island', 'Tokyo', 'Shanghai', 'Hovd', 'Omsk', 'Ashgabat', 'Yerevan', 'Moscow', 'Tel Aviv', 'Dublin', 'London', 'Praia', 'Montevideo', 'Brasília', 'Santiago', 'Bogotá', 'Easter Island', 'Salt Lake City', 'Los Angeles', 'Anchorage', 'Adak', 'Pago Pago'\]
let cityIDs: Array<string> = i18n.TimeZone.getAvailableZoneCityIDs();

#### \[h2\]getCityDisplayName9+

static getCityDisplayName(cityID: string, locale: string): string

Obtains time zone city display name in the specified language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cityID | string | Yes | Time zone city ID. |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Time zone city display name in the specified language. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let displayName: string = i18n.TimeZone.getCityDisplayName('Shanghai', 'zh-CN'); // displayName = 'Shanghai (China)'

#### \[h2\]getTimezoneFromCity9+

static getTimezoneFromCity(cityID: string): TimeZone

Creates a **TimeZone** object corresponding to the specified time zone city.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cityID | string | Yes | Time zone city ID. The value must be a time zone city ID supported by the system. |

**Return value**

| Type | Description |
| :-- | :-- |
| TimeZone | **TimeZone** object corresponding to the specified time zone city ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timezone: i18n.TimeZone = i18n.TimeZone.getTimezoneFromCity('Shanghai');

#### \[h2\]getTimezonesByLocation10+

static getTimezonesByLocation(longitude: number, latitude: number): Array<TimeZone>

Creates an array of **TimeZone** objects corresponding to the specified location.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| longitude | number | Yes | Longitude. The value range is \[-180, 179.9). A positive value is used for east longitude and a negative value is used for west longitude. |
| latitude | number | Yes | Latitude. The value range is \[-90, 89.9). A positive value is used for north latitude and a negative value is used for south latitude. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[TimeZone](#timezone)\> | **TimeZone** objects corresponding to the specified location. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Description**

The error message of 890001 is subject to the actual error.

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let timezoneArray: Array<i18n.TimeZone> = i18n.TimeZone.getTimezonesByLocation(-118.1, 34.0);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call TimeZone.getTimezonesByLocation failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getZoneRules20+

getZoneRules(): ZoneRules

Obtains the time zone transition rules. For details about the time zone transition logic, see [DST Transition](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-dst-transition).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [ZoneRules](#zonerules20) | Time zone transition rule, including the transition time and the offset before and after the transition. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let tzId: string = 'America/Tijuana';
let timeZone: i18n.TimeZone = i18n.getTimeZone(tzId);
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // Obtain the nextTransition object for time zone transition after May 13, 2025.
zoneOffsetTransition.getMilliseconds(); // Timestamp of the transition point: 1762074000000
zoneOffsetTransition.getOffsetAfter(); // Post-transition offset: -28800000
zoneOffsetTransition.getOffsetBefore(); // Pre-transition offset: -25200000
// Format the timestamp of the transition point.
let dateTimeFormat: Intl.DateTimeFormat = new Intl.DateTimeFormat('en-US', {
  timeZone: tzId,
  dateStyle: 'long',
  timeStyle: 'long',
  hour12: false
});
let dateFormat: string =
  dateTimeFormat.format(new Date(zoneOffsetTransition.getMilliseconds())); // November 2, 2025, 1:00:00 PST

#### ZoneRules20+

Queries the time zone transition rule.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]nextTransition20+

nextTransition(date?: number): ZoneOffsetTransition

Obtains the **nextTransition** object for the specified time.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | number | No | Timestamp of next transition. It is measured as the number of milliseconds from 00:00:00 on January 1, 1970 (UTC) to the specified time, which defaults to the current system time. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ZoneOffsetTransition](#zoneoffsettransition20) | **ZoneOffsetTransition** object for next transition. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// Obtain the time zone of Tijuana.
let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
// Obtain the time zone transition rule of Tijuana.
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
// Obtain the next time zone transition for Tijuana after May 13, 2025.
let zoneOffsetTransition: i18n.ZoneOffsetTransition = zoneRules.nextTransition(date.getTime());

#### ZoneOffsetTransition20+

Parses the time zone transition rule.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getMilliseconds20+

getMilliseconds(): number

Obtains the timestamp of the time zone transition point.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Timestamp of the time zone transition point. It is measured as the number of milliseconds from 00:00:00 on January 1, 1970 (UTC) to the time zone transition point, for example, 1762074000000. If the [raw offset](#getrawoffset) remains unchanged and DST is not used, **0** is returned. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // Obtain the nextTransition object for time zone transition after May 13, 2025.
zoneOffsetTransition.getMilliseconds(); // Timestamp of the transition point: 1762074000000

#### \[h2\]getOffsetAfter20+

getOffsetAfter(): number

Obtains the offset after the time zone transition.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Post-transition offset, that is, the time difference between the post-transition time and UTC, measured in ms. For example, **\-28800000** indicates that the time after the transition is 28800000 ms (8 hours) later than UTC. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // Obtain the nextTransition object for time zone transition after May 13, 2025.
zoneOffsetTransition.getOffsetAfter(); // Post-transition offset: -28800000

#### \[h2\]getOffsetBefore20+

getOffsetBefore(): number

Obtains the offset before the time zone transition.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| number | Pre-transition offset, that is, the time difference between the pre-transition time and UTC, measured in ms. For example, **\-25200000** indicates that the pre-transition time is 25200000 ms (7 hours) slower than UTC. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let timeZone: i18n.TimeZone = i18n.getTimeZone('America/Tijuana');
let zoneRules: i18n.ZoneRules = timeZone.getZoneRules();
let date = new Date(2025, 4, 13);
let zoneOffsetTransition: i18n.ZoneOffsetTransition =
    zoneRules.nextTransition(date.getTime()); // Obtain the nextTransition object for time zone transition after May 13, 2025.
zoneOffsetTransition.getOffsetBefore(); // Pre-transition offset: -25200000

#### Transliterator9+

Provides text transliteration capabilities, such as obtaining the supported language IDs and transliterating text.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getAvailableIDs9+

static getAvailableIDs(): string\[\]

Obtains a list of IDs supported by the **Transliterator** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | List of IDs supported by the **Transliterator** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// A total of 742 IDs are supported. One ID is comprised of two parts separated by a hyphen (-) in the format of source-destination. For example, in \*\*ids = \["Han-Latin","Latin-ASCII", "Amharic-Latin/BGN","Accents-Any", ...\]\*\*, \*\*Han-Latin\*\* indicates conversion from Chinese to Latin, and \*\*Amharic-Latin\*\* indicates conversion from Amharic to Latin.
// For more information, see ISO-15924.
let ids: string\[\] = i18n.Transliterator.getAvailableIDs();

#### \[h2\]getInstance9+

static getInstance(id: string): Transliterator

Creates a **Transliterator** object based on the specified ID.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | ID supported by the **Transliterator** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Transliterator](#transliterator9) | **Transliterator** object. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');

#### \[h2\]transform9+

transform(text: string): string

Converts the input text from the source format to the target format.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Text after conversion. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
let wordArray: string\[\] = \['China', 'Germany', 'US', 'France"\]
for (let i = 0; i < wordArray.length; i++) {
  let transliterateLatn: string =
    transliterator.transform(wordArray\[i\]); // transliterateLatn: 'zhōng guó', 'dé guó', 'měi guó', 'fǎ guó'
}

// Chinese transliteration and tone removal
transliterator = i18n.Transliterator.getInstance('Any-Latn;Latin-Ascii');
let transliterateAscii: string = transliterator.transform ('China'); // transliterateAscii = 'zhong guo'

// Chinese surname pronunciation
transliterator = i18n.Transliterator.getInstance('Han-Latin/Names');
let transliterateNames: string = transliterator.transform('Teacher Shan'); // transliterateNames = 'shàn lǎo shī'
transliterateNames = transliterator.transform('Long Sun No Taboo'); // transliterateNames = 'zhǎng sūn wú jì'

#### Unicode9+

Provides character attribute management capabilities, such as checking whether a character is a space, digit, or letter.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]isDigit9+

static isDigit(ch: string): boolean

Checks whether the input character is a digit.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a digit, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isDigit: boolean = i18n.Unicode.isDigit('1'); // isDigit = true

#### \[h2\]isSpaceChar9+

static isSpaceChar(ch: string): boolean

Checks whether the input character is a space.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a space, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isSpacechar: boolean = i18n.Unicode.isSpaceChar('a'); // isSpacechar = false

#### \[h2\]isWhitespace9+

static isWhitespace(ch: string): boolean

Checks whether the input character is a whitespace.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a white space, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isWhitespace: boolean = i18n.Unicode.isWhitespace('a'); // isWhitespace = false

#### \[h2\]isRTL9+

static isRTL(ch: string): boolean

Checks whether the input character is of the right to left (RTL) language.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is of the RTL language, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isRtl: boolean = i18n.Unicode.isRTL('a'); // isRtl = false

#### \[h2\]isIdeograph9+

static isIdeograph(ch: string): boolean

Checks whether the input character is an ideographic character.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character an ideographic character, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isIdeograph: boolean = i18n.Unicode.isIdeograph('a'); // isIdeograph = false

#### \[h2\]isLetter9+

static isLetter(ch: string): boolean

Checks whether the input character is a letter.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character a letter, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isLetter: boolean = i18n.Unicode.isLetter('a'); // isLetter = true

#### \[h2\]isLowerCase9+

static isLowerCase(ch: string): boolean

Checks whether the input character is a lowercase letter.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character a lowercase letter, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isLowercase: boolean = i18n.Unicode.isLowerCase('a'); // isLowercase = true

#### \[h2\]isUpperCase9+

static isUpperCase(ch: string): boolean

Checks whether the input character is an uppercase letter.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character an uppercase letter, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let isUppercase: boolean = i18n.Unicode.isUpperCase('a'); // isUppercase = false

#### \[h2\]getType9+

static getType(ch: string): string

Obtains the type of the input character.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Type of the input character. |

The following table lists only the common types. For more details, see the Unicode Standard.

| Name | Value | Description |
| :-- | :-- | :-- |
| U\_UNASSIGNED | U\_UNASSIGNED | Non-category for unassigned and non-character code points. |
| U\_GENERAL\_OTHER\_TYPES | U\_GENERAL\_OTHER\_TYPES | Same as **U\_UNASSIGNED**. |
| U\_UPPERCASE\_LETTER | U\_UPPERCASE\_LETTER | Uppercase letter. |
| U\_LOWERCASE\_LETTER | U\_LOWERCASE\_LETTER | Lowercase letter. |
| U\_TITLECASE\_LETTER | U\_TITLECASE\_LETTER | Title case letter. |
| U\_MODIFIER\_LETTER | U\_MODIFIER\_LETTER | Modifier letter. |
| U\_OTHER\_LETTER | U\_OTHER\_LETTER | Letters other than the uppercase letter, lowercase letter, title case letter, and modifier letter. |
| U\_NON\_SPACING\_MARK | U\_NON\_SPACING\_MARK | Non-spacing mark, such as the accent symbol **'** and the variable symbol **#**. |
| U\_ENCLOSING\_MARK | U\_ENCLOSING\_MARK | Enclosing mark, for example, a circle or a box. |
| U\_COMBINING\_SPACING\_MARK | U\_COMBINING\_SPACING\_MARK | Spacing mark, for example, the vowel symbol **\[\]**. |
| U\_DECIMAL\_DIGIT\_NUMBER | U\_DECIMAL\_DIGIT\_NUMBER | Decimal number. |
| U\_LETTER\_NUMBER | U\_LETTER\_NUMBER | Letter and number (including Roman numeral). |
| U\_OTHER\_NUMBER | U\_OTHER\_NUMBER | Other numbers, which are used as encryption symbols, marker symbols, or non-Arabic numerals, such as **@**, **#**, **(1)**, and **①**. |
| U\_SPACE\_SEPARATOR | U\_SPACE\_SEPARATOR | Space separator, for example, a space character, uninterrupted space character, or space character with a fixed width. |
| U\_LINE\_SEPARATOR | U\_LINE\_SEPARATOR | Line separator. |
| U\_PARAGRAPH\_SEPARATOR | U\_PARAGRAPH\_SEPARATOR | Paragraph separator. |
| U\_CONTROL\_CHAR | U\_CONTROL\_CHAR | Control character. |
| U\_FORMAT\_CHAR | U\_FORMAT\_CHAR | Format character. |
| U\_PRIVATE\_USE\_CHAR | U\_PRIVATE\_USE\_CHAR | Privately used character, for example, a company logo. |
| U\_SURROGATE | U\_SURROGATE | Surrogate, which is used to represent supplementary characters in UTF-16. |
| U\_DASH\_PUNCTUATION | U\_DASH\_PUNCTUATION | Dash punctuation. |
| U\_START\_PUNCTUATION | U\_START\_PUNCTUATION | Start punctuation, for example, the left parenthesis. |
| U\_END\_PUNCTUATION | U\_END\_PUNCTUATION | End punctuation, for example, the right parenthesis. |
| U\_INITIAL\_PUNCTUATION | U\_INITIAL\_PUNCTUATION | Initial punctuation, for example, the left double quotation mark or left single quotation mark. |
| U\_FINAL\_PUNCTUATION | U\_FINAL\_PUNCTUATION | Final punctuation, for example, the right double quotation mark or right single quotation mark. |
| U\_CONNECTOR\_PUNCTUATION | U\_CONNECTOR\_PUNCTUATION | Connector punctuation. |
| U\_OTHER\_PUNCTUATION | U\_OTHER\_PUNCTUATION | Other punctuations. |
| U\_MATH\_SYMBOL | U\_MATH\_SYMBOL | Mathematical symbol. |
| U\_CURRENCY\_SYMBOL | U\_CURRENCY\_SYMBOL | Currency symbol. |
| U\_MODIFIER\_SYMBOL | U\_MODIFIER\_SYMBOL | Modifier symbol. |
| U\_OTHER\_SYMBOL | U\_OTHER\_SYMBOL | Other symbols. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let unicodeType: string = i18n.Unicode.getType('a'); // unicodeType = 'U\_LOWERCASE\_LETTER'

#### I18NUtil9+

Internationalization utility class, which provides the capabilities of unit conversion, date sequence retrieval, time segment name retrieval, region matching, and path localization.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]unitConvert9+

static unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string

Converts one measurement unit into another and formats the unit based on the specified locale and style.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fromUnit | [UnitInfo](#unitinfo8) | Yes | Measurement unit to be converted. |
| toUnit | [UnitInfo](#unitinfo8) | Yes | Measurement unit to be converted to. |
| value | number | Yes | Value of the measurement unit to be converted. |
| locale | string | Yes | [Locale ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |
| style | string | No | 
Style used for formatting. The value can be **long**, **short**, or **narrow**. The default value is **short**.

For details about the meaning or display effect of different values, see [Number and Unit of Measurement Formatting](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-numbers-weights-measures).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String converted to the measurement unit after formatting. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let fromUnit: i18n.UnitInfo = { unit: 'cup', measureSystem: 'US' };
let toUnit: i18n.UnitInfo = { unit: 'liter', measureSystem: 'SI' };
let convertResult: string =
  i18n.I18NUtil.unitConvert(fromUnit, toUnit, 1000, 'en-US', 'long'); // convertResult = '236.588 liters'

#### \[h2\]getDateOrder9+

static getDateOrder(locale: string): string

Obtains the sequence of the year, month, and day in the specified locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [Locale ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Sequence of the year, month, and day in the locale. **y** indicates the year, **L** indicates the month, and **d** indicates the day. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let order: string = i18n.I18NUtil.getDateOrder('zh-CN'); // order = 'y-L-d'

#### \[h2\]getTimePeriodName11+

static getTimePeriodName(hour:number, locale?: string): string

Obtains the localized expression of the specified time in the specified locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hour | number | Yes | Specified time, for example, **16**. |
| locale | string | No | 
[System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. for example, **zh-Hans-CN**.

The default value is the current system locale.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Localized expression of the specified time in the specified locale. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let name: string = i18n.I18NUtil.getTimePeriodName(2, 'zh-CN'); // name = 'a.m.'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getTimePeriodName failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getBestMatchLocale12+

static getBestMatchLocale(locale: string, localeList: string\[\]): string

Obtains the locale that best matches a region from the specified locale list.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | [Locale ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), for example, **zh-Hans-CN**. |
| localeList | string\[\] | Yes | List of locale IDs. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | ID of the locale that best matches a region. If no matching locale is found, an empty string is returned. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let matchedLocaleId: string = i18n.I18NUtil.getBestMatchLocale('zh-Hans-CN',
    \['en-Latn-US', 'en-GB', 'zh-Hant-CN', 'zh-Hans-MO'\]); // matchedLocaleId = 'zh-Hans-MO'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getBestMatchLocale failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getThreeLetterLanguage12+

static getThreeLetterLanguage(locale: string): string

Converts a language code from two letters to three letters.

For example, the two-letter language code of Chinese is **zh**, and the corresponding three-letter language code is **zho**. For details, see [ISO 639](https://www.iso.org/iso-639-language-code).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | Two-letter code of the language to be converted, for example, **zh**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Language code after conversion. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let language: string = i18n.I18NUtil.getThreeLetterLanguage('zh') // language = 'zho'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getThreeLetterLanguage failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getThreeLetterRegion12+

static getThreeLetterRegion(locale: string): string

Converts a region code from two letters to three letters.

For example, the two-letter region code of China is **CN**, and the corresponding three-letter region code is **CHN**. For details, see [ISO 3166](https://www.iso.org/iso-3166-country-codes.html).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | Two-letter country/region code to be converted, for example, **CN**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Region code after conversion . |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let region: string = i18n.I18NUtil.getThreeLetterRegion('CN') // region = 'CHN'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getThreeLetterRegion failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getUnicodeWrappedFilePath20+

static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: Intl.Locale): string

Localizes a file path for the specified locale.

For example, **/data/out/tmp** is changed to **tmp/out/data/** after localization.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path to mirror, for example, **/data/out/tmp**. |
| delimiter | string | No | Path delimiter. The default value is **/**. |
| locale | [Intl.Locale](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | File path after localization. If the specified locale object corresponds to an RTL language, the processed file path contains a direction control character to ensure that the file path is displayed in mirror mode. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let path: string = '/data/out/tmp';
  let delimiter: string = '/';
  let locale: Intl.Locale = new Intl.Locale('ar');
  let mirrorPath: string =
    i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, locale); // mirrorPath is displayed as tmp/out/data/.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getUnicodeWrappedFilePath failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getUnicodeWrappedFilePath(deprecated)

static getUnicodeWrappedFilePath(path: string, delimiter?: string, locale?: intl.Locale): string

This API is supported since API version 18 and deprecated since API version 20. You are advised to use [getUnicodeWrappedFilePath](#getunicodewrappedfilepath20).

Localizes a file path for the specified locale.

For example, **/data/out/tmp** is changed to **tmp/out/data/** after localization.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path to mirror, for example, **/data/out/tmp**. |
| delimiter | string | No | Path delimiter. The default value is **/**. |
| locale | [intl.Locale](../ohos-intl-internationalization/document.md#localedeprecated) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | File path after localization. If the specified locale object corresponds to an RTL language, the processed file path contains a direction control character to ensure that the file path is displayed in mirror mode. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let path: string = '/data/out/tmp';
  let delimiter: string = '/';
  let locale: intl.Locale = new intl.Locale('ar');
  let mirrorPath: string =
    i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, locale); // mirrorPath is displayed as tmp/out/data/.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call I18NUtil.getUnicodeWrappedFilePath failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### Normalizer10+

Provides the text normalization capabilities.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]getInstance10+

static getInstance(mode: NormalizerMode): Normalizer

Obtains a **Normalizer** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [NormalizerMode](#normalizermode10) | Yes | Text normalization mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Normalizer](#normalizer10) | **Normalizer** object for text normalization. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]normalize10+

normalize(text: string): string

Normalizes input strings.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Input text. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Normalized strings. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
  let normalizedText: string = normalizer.normalize('\\u1E9B\\u0323'); // normalizedText = 'ẛ̣'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call Normalizer.getInstance failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### NormalizerMode10+

Enumerates text normalization modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Value | Description |
| :-- | :-- | :-- |
| NFC | 1 | NFC. |
| NFD | 2 | NFD. |
| NFKC | 3 | NFKC. |
| NFKD | 4 | NFKD. |

#### HolidayManager11+

Provides holiday data parsing capabilities, such as determining holidays and obtaining the holiday list of a specified year.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor11+

constructor(icsPath: String)

Creates a **HolidayManager** object for parsing holiday data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| icsPath | String | Yes | Path of the **.ics** file with the read permission granted for applications. iCalendar is a standard Internet calendar format for storing calendar data. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager = new i18n.HolidayManager('/system/lib/US.ics');
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.HolidayManager failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]isHoliday11+

isHoliday(date?: Date): boolean

Determines whether the specified date is a holiday.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | No | 
Date and time. Note: The month starts from **0**. For example, **0** indicates January.

The default value is the current date.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the specified date is a holiday, and **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let isHoliday: boolean = holidayManager.isHoliday();
  isHoliday = holidayManager.isHoliday(new Date(2023, 5, 25)); // The date is 2023.06.25.
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call holidayManager.isHoliday failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]getHolidayInfoItemArray11+

getHolidayInfoItemArray(year?: number): Array<[HolidayInfoItem](#holidayinfoitem11)\>

Obtains the holiday information list of the specified year.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| year | number | No | 
Specified year, for example, 2023.

The default value is the current year.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[HolidayInfoItem](#holidayinfoitem11)\> | Holiday information list. |

**Error codes**

For details about the error codes, see [ohos.i18n Error Codes](../../error-codes/i18n-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  // Replace /system/lib/US.ics with the actual ICS file path.
  let holidayManager: i18n.HolidayManager = new i18n.HolidayManager('/system/lib/US.ics');
  let holidayInfoItemArray: Array<i18n.HolidayInfoItem> = holidayManager.getHolidayInfoItemArray(2023);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call holidayManager.getHolidayInfoItemArray failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### HolidayInfoItem11+

Represents the holiday information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| baseName | string | No | No | Holiday name. |
| year | number | No | No | Year of the holiday. |
| month | number | No | No | Month of the holiday. |
| day | number | No | No | Day of the holiday. |
| localNames | Array<[HolidayLocalName](#holidaylocalname11)\> | No | Yes | Local names of the holiday. |

#### HolidayLocalName11+

Represents the name of a holiday in different languages.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| language | string | No | No | Language, for example, **ar**, **en**, or **tr**. |
| name | string | No | No | Local name of a holiday. For example, the Turkish name of Sacrifice Feast is Kurban Bayrami. |

#### i18n.getSimpleDateTimeFormatByPattern20+

getSimpleDateTimeFormatByPattern(pattern: string, locale?: Intl.Locale): SimpleDateTimeFormat

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatBySkeleton](#i18ngetsimpledatetimeformatbyskeleton20), see the examples in [SimpleDateTimeFormat.format](#format18).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pattern | string | Yes | Valid pattern, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter also supports custom text enclosed in single quotation marks (''). |
| locale | [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleDateTimeFormat](#simpledatetimeformat18) | **SimpleDateTimeFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.getSimpleDateTimeFormatByPattern failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### i18n.getSimpleDateTimeFormatByPattern(deprecated)

getSimpleDateTimeFormatByPattern(pattern: string, locale?: intl.Locale): SimpleDateTimeFormat

This API is supported since API version 18 and deprecated since API version 20. You are advised to use [getSimpleDateTimeFormatByPattern](#i18ngetsimpledatetimeformatbypattern20).

Obtains a **SimpleDateTimeFormat** object based on the specified pattern string. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatBySkeleton](#i18ngetsimpledatetimeformatbyskeletondeprecated), see the examples in [SimpleDateTimeFormat.format](#format18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pattern | string | Yes | Valid pattern, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter also supports custom text enclosed in single quotation marks (''). |
| locale | [intl.Locale](../ohos-intl-internationalization/document.md#localedeprecated) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleDateTimeFormat](#simpledatetimeformat18) | **SimpleDateTimeFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.getSimpleDateTimeFormatByPattern failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### i18n.getSimpleDateTimeFormatBySkeleton20+

getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleDateTimeFormat

Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatByPattern](#i18ngetsimpledatetimeformatbypattern20), see the examples in [SimpleDateTimeFormat.format](#format18).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| skeleton | string | Yes | Valid skeleton, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter does not support custom text. |
| locale | [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleDateTimeFormat](#simpledatetimeformat18) | **SimpleDateTimeFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.getSimpleDateTimeFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### i18n.getSimpleDateTimeFormatBySkeleton(deprecated)

getSimpleDateTimeFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleDateTimeFormat

This API is supported since API version 18 and deprecated since API version 20. You are advised to use [getSimpleDateTimeFormatBySkeleton](#i18ngetsimpledatetimeformatbyskeleton20).

Obtains a **SimpleDateTimeFormat** object based on the specified skeleton. For details about the difference between the objects obtained by this API and [getSimpleDateTimeFormatByPattern](#i18ngetsimpledatetimeformatbypatterndeprecated), see the examples in [SimpleDateTimeFormat.format](#format18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| skeleton | string | Yes | Valid skeleton, which supports free combinations of field patterns in [Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table). This parameter does not support custom text. |
| locale | [intl.Locale](../ohos-intl-internationalization/document.md#localedeprecated) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleDateTimeFormat](#simpledatetimeformat18) | **SimpleDateTimeFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.getSimpleDateTimeFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### SimpleDateTimeFormat18+

Performs date and time formatting.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]format18+

format(date: Date): string

Formats the date and time.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| date | Date | Yes | Date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | A string containing the formatted date and time. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale : Intl.Locale = new Intl.Locale("zh-Hans-CN");
  let date: Date = new Date(2024, 11, 13); // Set the date to 2024.12.13.

  let formatterWithText: i18n.SimpleDateTimeFormat =
    i18n.getSimpleDateTimeFormatByPattern("'month('M')'", locale);
  let formattedDate: string = formatterWithText.format(date); // formattedDate = 'month(12)'

  let patternFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatByPattern('yMd', locale);
  formattedDate = patternFormatter.format(date); // formattedDate = '20241213'

  let skeletonFormatter: i18n.SimpleDateTimeFormat = i18n.getSimpleDateTimeFormatBySkeleton('yMd', locale);
  formattedDate = skeletonFormatter.format(date); // formattedDate = '2024/12/13'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call SimpleDateTimeFormat.format failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### i18n.getSimpleNumberFormatBySkeleton20+

getSimpleNumberFormatBySkeleton(skeleton: string, locale?: Intl.Locale): SimpleNumberFormat

Obtains a **SimpleNumberFormat** object based on the specified skeleton.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| skeleton | string | Yes | Valid skeleton. For details about the supported characters and their meanings, see [Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html#number-skeletons). |
| locale | [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleNumberFormat](#simplenumberformat18) | **SimpleNumberFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8900001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call SimpleDateTimeFormat.getSimpleNumberFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### i18n.getSimpleNumberFormatBySkeleton(deprecated)

getSimpleNumberFormatBySkeleton(skeleton: string, locale?: intl.Locale): SimpleNumberFormat

This API is supported since API version 18 and deprecated since API version 20. You are advised to use [getSimpleNumberFormatBySkeleton](#i18ngetsimplenumberformatbyskeleton20).

Obtains a **SimpleNumberFormat** object based on the specified skeleton.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| skeleton | string | Yes | Valid skeleton. For details about the supported characters and their meanings, see [Number Skeletons](https://unicode-org.github.io/icu/userguide/format_parse/numbers/skeletons.html#number-skeletons). |
| locale | [intl.Locale](../ohos-intl-internationalization/document.md#localedeprecated) | No | **Locale** object. The default value is the current system locale. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SimpleNumberFormat](#simplenumberformat18) | **SimpleNumberFormat** object. |

**Error codes**

For details about the error codes, see [i18n Error Codes](../../error-codes/i18n-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 890001 | Invalid parameter. Possible causes: Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let locale: intl.Locale = new intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call SimpleDateTimeFormat.getSimpleNumberFormatBySkeleton failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### SimpleNumberFormat18+

Formats a number based on the specified skeleton string.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]format18+

format(value: number): string

Formats a number.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Number to be formatted. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted number. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let locale: Intl.Locale = new Intl.Locale('zh-Hans-CN');
  let formatter: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('%', locale);
  let formattedNumber: string = formatter.format(10); // formattedNumber = '10%'
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call SimpleNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### StyledNumberFormat18+

Performs rich text number formatting.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor(deprecated)

constructor(numberFormat: intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

This API is supported since API version 18 and deprecated since API version 20. You are advised to use [constructor](#constructor20) instead.

Creates a **NumberFormat** object for rich text display.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| numberFormat | [intl.NumberFormat](../ohos-intl-internationalization/document.md#numberformat) | [SimpleNumberFormat](#simplenumberformat18) | Yes | **NumberFormat** object. |
| options | [StyledNumberFormatOptions](#stylednumberformatoptions18) | No | Configuration options of the **NumberFormat** object. The default value is the default text style. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n, intl } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // Create a StyledNumberFormat object through intl.NumberFormat.
  let numFmt: intl.NumberFormat = new intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // Create a StyledNumberFormat object through SimpleNumberFormat.
  let locale: intl.Locale = new intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]constructor20+

constructor(numberFormat: Intl.NumberFormat | SimpleNumberFormat, options?: StyledNumberFormatOptions)

Creates a **NumberFormat** object for rich text display.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| numberFormat | [Intl.NumberFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat) | [SimpleNumberFormat](#simplenumberformat18) | Yes | **NumberFormat** object. |
| options | [StyledNumberFormatOptions](#stylednumberformatoptions18) | No | Configuration options of the **NumberFormat** object. The default value is the default text style. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // Create a StyledNumberFormat object through Intl.NumberFormat.
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });

  // Create a StyledNumberFormat object through SimpleNumberFormat.
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call i18n.StyledNumberFormat failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### \[h2\]format18+

format(value: number): StyledString

Formats a number as a rich text object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Number to be formatted. |

**Return value**

| Type | Description |
| :-- | :-- |
| [StyledString](../../../arkui/arkts-components/text-and-input/styled-string/document.md#styledstring) | Rich text object after formatting. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

try {
  let integerTextStyle: TextStyle = new TextStyle({ fontColor: Color.Red });
  let decimalTextStyle: TextStyle = new TextStyle({ fontColor: Color.Brown });
  let fractionTextStyle: TextStyle = new TextStyle({ fontColor: Color.Blue });
  let unitTextStyle: TextStyle = new TextStyle({ fontColor: Color.Green });

  // Create a StyledNumberFormat object through Intl.NumberFormat.
  let numFmt: Intl.NumberFormat = new Intl.NumberFormat('zh', { style: 'unit', unit: 'percent' });
  let styledNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(numFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedNumber.getString () is 1,234.568%. In the formatted number, 1,234 is in red, . in brown, 568 in blue, and % in green.
  let formattedNumber: StyledString = styledNumFmt.format(1234.5678);

  // Create a StyledNumberFormat object through SimpleNumberFormat.
  let locale: Intl.Locale = new Intl.Locale('zh');
  let simpleNumFmt: i18n.SimpleNumberFormat = i18n.getSimpleNumberFormatBySkeleton('percent', locale);
  let styledSimpleNumFmt: i18n.StyledNumberFormat = new i18n.StyledNumberFormat(simpleNumFmt, {
    integer: integerTextStyle,
    decimal: decimalTextStyle,
    fraction: fractionTextStyle,
    unit: unitTextStyle
  });
  // formattedSimpleNumber.getString () is 1,234.5678%. In the formatted number, '1,234' is in red, . in brown, 5678 in blue, and % in green.
  let formattedSimpleNumber: StyledString = styledSimpleNumFmt.format(1234.5678);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(\`call StyledNumberFormat.format failed, error code: ${err.code}, message: ${err.message}.\`);
}

#### StyledNumberFormatOptions18+

Represents optional configuration items for the **NumberFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| integer | [TextStyle](../../../arkui/arkts-components/text-and-input/styled-string/document.md#textstyle) | No | Yes | Text style for the integer part. The default value is the default text style. |
| decimal | [TextStyle](../../../arkui/arkts-components/text-and-input/styled-string/document.md#textstyle) | No | Yes | Text style for the decimal point. The default value is the default text style. |
| fraction | [TextStyle](../../../arkui/arkts-components/text-and-input/styled-string/document.md#textstyle) | No | Yes | Text style for the fraction part. The default value is the default text style. |
| unit | [TextStyle](../../../arkui/arkts-components/text-and-input/styled-string/document.md#textstyle) | No | Yes | Text style for the unit. The default value is the default text style. |

#### i18n.getDisplayCountry(deprecated)

getDisplayCountry(country: string, locale: string, sentenceCase?: boolean): string

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [System.getDisplayCountry](#getdisplaycountry9) instead.

Obtains the localized name of the specified country/region.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| country | string | Yes | Specified country. |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value **true** means to display the text in title case format, and the value **false** means to display the text in the default case format of the locale. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Localized script for the specified country. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let countryName: string = i18n.getDisplayCountry('zh-CN', 'en-GB', true); // countryName = 'China'
countryName = i18n.getDisplayCountry('zh-CN', 'en-GB'); // countryName = 'China'

#### i18n.getDisplayLanguage(deprecated)

getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [System.getDisplayLanguage](#getdisplaylanguage9) instead.

Obtains the localized script for the specified language.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | Specified language. |
| locale | string | Yes | [System locale](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-locale-culture#how-it-works), which consists of the language, script, and country/region. |
| sentenceCase | boolean | No | Whether to use sentence case to display the text. The value **true** means to display the text in title case format, and the value **false** means to display the text in the default case format of the locale. The default value is **true**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Localized script for the specified language. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let languageName: string = i18n.getDisplayLanguage('zh', 'en-GB', true); // languageName = 'Chinese'
languageName = i18n.getDisplayLanguage('zh', 'en-GB'); // languageName = 'Chinese'

#### i18n.getSystemLanguage(deprecated)

getSystemLanguage(): string

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [System.getSystemLanguage](#getsystemlanguage9) instead.

Obtains the system language.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | System language ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.getSystemLanguage();

#### i18n.getSystemRegion(deprecated)

getSystemRegion(): string

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [System.getSystemRegion](#getsystemregion9) instead.

Obtains the system region.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | System region ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let region: string = i18n.getSystemRegion();

#### i18n.getSystemLocale(deprecated)

getSystemLocale(): string

This API is supported since API version 7 and is deprecated since API version 9. You are advised to use [System.getSystemLocale](#getsystemlocaledeprecated) instead.

Obtains the system locale.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | System locale ID. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let locale: string = i18n.getSystemLocale();

#### i18n.is24HourClock(deprecated)

is24HourClock(): boolean

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [System.is24HourClock](#is24hourclock9) instead.

Checks whether the 24-hour clock is used.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the 24-hour clock is used, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let is24HourClock: boolean = i18n.is24HourClock();

#### i18n.set24HourClock(deprecated)

set24HourClock(option: boolean): boolean

This API is supported since API version 7 and is deprecated since API version 9. The substitute API is available only for system applications.

Sets the 24-hour clock.

**Permission required**: ohos.permission.UPDATE\_CONFIGURATION

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| option | boolean | Yes | Whether to enable the 24-hour clock. The value **true** means to enable the 24-hour clock, and the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the setting is successful, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// Set the system time to the 24-hour clock.
let success: boolean = i18n.set24HourClock(true);

#### i18n.addPreferredLanguage(deprecated)

addPreferredLanguage(language: string, index?: number): boolean

This API is supported since API version 8 and is deprecated since API version 9. The substitute API is available only for system applications.

Adds a preferred language to the specified position on the preferred language list.

**Permission required**: ohos.permission.UPDATE\_CONFIGURATION

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| language | string | Yes | Preferred language to add. |
| index | number | No | Position to which the preferred language is added. The default value is the length of the preferred language list. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the operation is successful, and **false** otherwise. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// Add zh-CN to the preferred language list.
let language: string = 'zh-CN';
let index: number = 0;
let success: boolean = i18n.addPreferredLanguage(language, index);

#### i18n.removePreferredLanguage(deprecated)

removePreferredLanguage(index: number): boolean

This API is supported since API version 8 and is deprecated since API version 9. The substitute API is available only for system applications.

Removes a preferred language from the specified position on the preferred language list.

**Permission required**: ohos.permission.UPDATE\_CONFIGURATION

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Position of the preferred language to delete. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { i18n } from '@kit.LocalizationKit';

// Delete the first preferred language from the preferred language list.
let index: number = 0;
let success: boolean = i18n.removePreferredLanguage(index);

#### i18n.getPreferredLanguageList(deprecated)

getPreferredLanguageList(): Array<string>

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [System.getPreferredLanguageList](#getpreferredlanguagelist9) instead.

Obtains the list of preferred languages.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of preferred languages. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.getPreferredLanguageList();

#### i18n.getFirstPreferredLanguage(deprecated)

getFirstPreferredLanguage(): string

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [System.getFirstPreferredLanguage](#getfirstpreferredlanguage9) instead.

Obtains the first language in the preferred language list.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | First language in the preferred language list. |

**Example**

import { i18n } from '@kit.LocalizationKit';

let firstPreferredLanguage: string = i18n.getFirstPreferredLanguage();

#### Util(deprecated)

#### \[h2\]unitConvert(deprecated)

unitConvert(fromUnit: UnitInfo, toUnit: UnitInfo, value: number, locale: string, style?: string): string

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [unitConvert](#unitconvert9) instead.

Converts one measurement unit into another and formats the unit based on the specified locale and style.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fromUnit | [UnitInfo](#unitinfo8) | Yes | Measurement unit to be converted. |
| toUnit | [UnitInfo](#unitinfo8) | Yes | Measurement unit to be converted to. |
| value | number | Yes | Value of the measurement unit to be converted. |
| locale | string | Yes | Locale ID used for formatting, for example, **zh-Hans-CN**. |
| style | string | No | Style used for formatting. The value can be **long**, **short**, or **narrow**. The default value is **short**. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String obtained after formatting based on the measurement unit specified by **toUnit**. |

#### Character(deprecated)

#### \[h2\]isDigit(deprecated)

isDigit(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isDigit](#isdigit9) instead.

Checks whether the input character is a digit.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a digit, and **false** otherwise. |

#### \[h2\]isSpaceChar(deprecated)

isSpaceChar(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isSpaceChar](#isspacechar9) instead.

Checks whether the input character is a space.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a space, and **false** otherwise. |

#### \[h2\]isWhitespace(deprecated)

isWhitespace(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isWhitespace](#iswhitespace9) instead.

Checks whether the input character is a whitespace.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is a white space, and **false** otherwise. |

#### \[h2\]isRTL(deprecated)

isRTL(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isRTL](#isrtl9) instead.

Checks whether the input character is of the right to left (RTL) language.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character is of the RTL language, and **false** otherwise. |

#### \[h2\]isIdeograph(deprecated)

isIdeograph(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isIdeograph](#isideograph9) instead.

Checks whether the input character is an ideographic character.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character an ideographic character, and **false** otherwise. |

#### \[h2\]isLetter(deprecated)

isLetter(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isLetter](#isletter9) instead.

Checks whether the input character is a letter.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character a letter, and **false** otherwise. |

#### \[h2\]isLowerCase(deprecated)

isLowerCase(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isLowerCase](#islowercase9) instead.

Checks whether the input character is a lowercase letter.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character a lowercase letter, and **false** otherwise. |

#### \[h2\]isUpperCase(deprecated)

isUpperCase(ch: string): boolean

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [isUpperCase](#isuppercase9) instead.

Checks whether the input character is an uppercase letter.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** if the input character an uppercase letter, and **false** otherwise. |

#### \[h2\]getType(deprecated)

getType(ch: string): string

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [getType](#gettype9) instead.

Obtains the type of the input character.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | string | Yes | Input character. If the input is a string, only the type of the first character is checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Type of the input character. |
