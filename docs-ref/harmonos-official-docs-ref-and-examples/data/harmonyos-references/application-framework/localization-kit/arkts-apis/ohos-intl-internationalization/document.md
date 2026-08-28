# @ohos.intl (Internationalization)

The **intl** module provides basic i18n capabilities, such as time and date formatting, number formatting, and string sorting, through the standard i18n APIs defined in ECMA 402.

The [i18n](../ohos-i18n-internationalization/document.md) module provides enhanced i18n capabilities through supplementary interfaces that are not defined in ECMA 402. It works with the intl module to provide a complete suite of i18n capabilities.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/wVCTR-rmT3WVcONRJL0lNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1541EE9C538DAAEA886572C40BEDABDA5DAE8E761E9ED80988150EBCAF2B6F46)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module are based on the [CLDR](https://cldr.unicode.org) internationalization database. The processing results of the APIs may be adjusted as the CLDR standard evolves. For example, the return value of the [number formatting API](#numberformat) is used only for UI display. Do not hardcode the return value or make assumptions about the return value. Otherwise, version compatibility problems may occur. API version 12 corresponds to [CLDR 42](https://cldr.unicode.org/index/downloads/cldr-42). For details about data changes, see the official CLDR documentation.
    
-   Since API version 11, some APIs of this module are supported in ArkTS widgets.
    
-   Since API version 12, the APIs of this module are supported in atomic services.
    

#### Modules to Import

import { intl } from '@kit.LocalizationKit';

#### Locale(deprecated)

#### \[h2\]Attributes

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) instead.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| language | string | No | No | Language associated with the locale, for example, **zh**. The value complies with the ISO 639 standard. |
| script | string | No | No | Script type of the language, for example, **Hans**. The value complies with the Unicode ISO 15924 standard. |
| region | string | No | No | Country/region associated with the locale, for example, **CN**. The value complies with the ISO 3166 standard. |
| baseName | string | No | No | Locale information, which consists of the language, script, and country/region, for example, **zh-Hans-CN**. |
| caseFirst | string | No | No | 
Whether case is taken into account for the locale's collation rules. The value can be:

**upper**: Uppercase letters come first.

**lower**: Lowercase letters come first.

**false**: The default collation rules of the locale are used.

 |
| calendar | string | No | No | 

Calendar for the locale. The value can be:

The value can be any of the following: **buddhist**, **chinese**, **coptic**, **dangi**, **ethioaa**, **ethiopic**, **gregory**, **hebrew**, **indian**, **islamic**, **islamic-umalqura**, **islamic-tbla**, **islamic-civil**, **islamic-rgsa**, **iso8601**, **japanese**, **persian**, **roc**, or **islamicc**.

For details about their meanings, see Table 1 in [Calendar Setting](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-calendar).

 |
| collation | string | No | No | 

Collation rules for the locale. The value can be:

**big5han**: Pinyin sorting for Latin letters.

**compat**: compatibility sorting, only for Arabic.

**dict**: dictionary-style sorting, only for Singhalese.

**direct**: binary code point sorting.

**ducet**: sorting according to the Unicode collation element table.

**eor**: sorting according to the European collation rules.

**gb2312**: Pinyin sorting, only for Chinese.

**phonebk**: phone book-style sorting.

**phonetic**: phonetic sorting.

**pinyin**: Pinyin sorting.

**reformed**: reformed sorting, only for Swedish.

**searchjl**: special sorting for Korean initial consonant search.

**stroke**: stroke sorting for Chinese.

**trad**: traditional-style sorting, for example, Spanish.

unihan: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.

zhuyin: Zhuyin sorting, only for Chinese.

 |
| hourCycle | string | No | No | 

Time system for the locale. The value can be:

"h11", "h12", "h23", or "h24".

For details about their display effects, see [Table 5](#appendix).

 |
| numberingSystem | string | No | No | 

Numbering system for the locale. The value can be:

**adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.

 |
| numeric | boolean | No | No | 

Whether to use special sorting rules for digits. The value **true** means to use special sorting rules for digits, and the value **false** means the opposite.

The default value is **false**.

 |

#### \[h2\]constructor(deprecated)

constructor()

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [i18n.System.getSystemLocaleInstance](../ohos-i18n-internationalization/document.md#getsystemlocaleinstance20) instead.

Creates a **Locale** object.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// The current system locale is used by the default constructor.
let locale = new intl.Locale();
// Return the current system locale ID.
let localeID = locale.toString();

#### \[h2\]constructor(deprecated)

constructor(locale: string, options?: LocaleOptions)

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.Locale.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/Locale) instead.

Creates a **Locale** object.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Yes | Locale information, which consists of the language, script, and country/region. |
| options | [LocaleOptions](#localeoptionsdeprecated) | No | Options for creating the **Locale** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a zh-CN locale object.
let locale = new intl.Locale('zh-CN');
let localeID = locale.toString(); // localeID = 'zh-CN'

#### \[h2\]toString(deprecated)

toString(): string

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.Locale.toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/toString) instead.

Obtains the string that represents a **Locale** object.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| string | String that represents the **Locale** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create an en-GB locale object.
let locale = new intl.Locale('en-GB');
let localeID = locale.toString(); // localeID = 'en-GB'

#### \[h2\]maximize(deprecated)

maximize(): Locale

This API is supported since API version 68 and deprecated since API version 20. You are advised to use [Intl.Locale.maximize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/maximize) instead.

Maximizes locale information by supplementing the missing script and country/region information.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [Locale](#localedeprecated) | **Locale** object with the script and country/region information. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a zh locale object.
let locale = new intl.Locale('zh');
// Supplement the locale object's script and region.
let maximizedLocale = locale.maximize();
let localeID = maximizedLocale.toString(); // localeID = 'zh-Hans-CN'

// Create an en-US locale object.
locale = new intl.Locale('en-US');
// Supplement the locale object's script.
maximizedLocale = locale.maximize();
localeID = maximizedLocale.toString(); // localeID = 'en-Latn-US'

#### \[h2\]minimize(deprecated)

minimize(): Locale

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.Locale.minimize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/minimize) instead.

Minimizes locale information by removing the script and country/region information.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [Locale](#localedeprecated) | **Locale** object without the script and country/region information. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a zh-Hans-CN locale object.
let locale = new intl.Locale('zh-Hans-CN');
// Remove the locale object's script and region.
let minimizedLocale = locale.minimize();
let localeID = minimizedLocale.toString(); // localeID = 'zh'

// Create an en-US locale object.
locale = new intl.Locale('en-US');
// Remove locale object's region.
minimizedLocale = locale.minimize();
localeID = minimizedLocale.toString(); // localeID = 'en'

#### LocaleOptions(deprecated)

This API is supported since API version 6 and is deprecated since API version 20. Taking calendar as an example, you are advised to use [Intl.LocaleOptions.calendar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale/calendar) instead.

Options for initializing the **Locale** object. Since API version 9, the **LocaleOptions** attribute is changed from mandatory to optional.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| calendar | string | No | Yes | 
Calendar parameter. The value can be:

"buddhist", "chinese", "coptic", "dangi", "ethioaa", "ethiopic", "gregory", "hebrew", "indian", "islamic", "islamic-umalqura", "islamic-tbla", "islamic-civil", "islamic-rgsa", "iso8601", "japanese", "persian", "roc", or "islamicc".

 |
| collation | string | No | Yes | 

Collation rules for the locale. The value can be:

**big5han**: Pinyin sorting for Latin letters.

**compat**: compatibility sorting, only for Arabic.

**dict**: dictionary-style sorting, only for Singhalese.

**direct**: binary code point sorting.

**ducet**: sorting according to the Unicode collation element table.

**eor**: sorting according to the European collation rules.

**gb2312**: Pinyin sorting, only for Chinese.

**phonebk**: phone book-style sorting.

**phonetic**: phonetic sorting.

**pinyin**: Pinyin sorting.

**reformed**: reformed sorting, only for Swedish.

**searchjl**: special sorting for Korean initial consonant search.

**stroke**: stroke sorting for Chinese.

**trad**: traditional-style sorting, for example, Spanish.

unihan: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.

zhuyin: Zhuyin sorting, only for Chinese.

 |
| hourCycle | string | No | Yes | 

Hour cycle. The value can be:

"h11", "h12", "h23", or "h24".

 |
| numberingSystem | string | No | Yes | 

Numbering system. The value can be:

**adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.

 |
| numeric | boolean | No | Yes | Whether to treat numeric characters as numbers for sorting. The value true means to treat numeric characters as numbers for sorting, and the value **false** means to treat numeric characters as ordinary characters for sorting. For example, when this parameter is set to **true**, comparing the string **21** with the string **123** is equivalent to comparing the number 21 with the number 123. The default value is **false**. |
| caseFirst | string | No | Yes | 

Whether case is taken into account for the locale's collation rules. The value can be:

**upper**: Uppercase letters come first.

**lower**: Lowercase letters come first.

**false**: The default collation rules of the locale are used.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/X-Ha4ZkuTLemOFhSC2fPtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B54F6C2C7B24CD14F665F8675737554C434C17736ED824FF88D169BBAF0D0CFF)

-   For details about **calendar**, see Table 1 in [Calendar Setting](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/i18n-calendar).

#### DateTimeFormat(deprecated)

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) instead.

Performs date and time formatting.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor(deprecated)

constructor()

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) instead.

Creates a **DateTimeOptions** object for the specified locale.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a DateTimeFormat object using the current system locale ID.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat();

#### \[h2\]constructor(deprecated)

constructor(locale: string | Array<string>, options?: DateTimeOptions)

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) instead.

Creates a **DateTimeOptions** object for the specified locale.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Array<string> | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [DateTimeOptions](#datetimeoptionsdeprecated) | No | 
Options for creating the **DateTimeOptions** object.

If no options are set, the default values of **year**, **month**, and **day** are **numeric**.

 |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a DateTimeFormat object with locale ID being zh-CN, dateStyle being full, and timeStyle being medium.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('zh-CN', { dateStyle: 'full', timeStyle: 'medium' });

// Create a DateTimeFormat object with a locale ID array. The locale ID ban is invalid and therefore locale ID zh is used.
formatter = new intl.DateTimeFormat(\['ban', 'zh'\], { dateStyle: 'full', timeStyle: 'medium' });

#### \[h2\]format(deprecated)

format(date: Date): string

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.DateTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format) instead.

Formats the date and time.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

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

import { intl } from '@kit.LocalizationKit';

let date: Date = new Date(2021, 11, 17, 3, 24, 0); // The date and time is 2021.12.17 03:24:00.
// Create a DateTimeFormat object with the locale ID being en-GB.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDate: string = formatter.format(date); // formattedDate "17/12/2021"

// Create a DateTimeFormat object with locale ID being en-GB, dateStyle being full, and timeStyle being medium.
formatter = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
formattedDate = formatter.format(date); // formattedDate "Friday, 17 December 2021, 03:24:00"

#### \[h2\]formatRange(deprecated)

formatRange(startDate: Date, endDate: Date): string

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.DateTimeFormat.formatRange](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/formatRange) instead.

Formats date and time ranges.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startDate | Date | Yes | Start date and time. Note: The month starts from **0**. For example, **0** indicates January. |
| endDate | Date | Yes | End date and time. Note: The month starts from **0**. For example, **0** indicates January. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | A string containing the formatted date and time ranges. |

**Example**

import { intl } from '@kit.LocalizationKit';

let startDate: Date = new Date(2021, 11, 17, 3, 24, 0); // The date and time is 2021.12.17 03:24:00.
let endDate: Date = new Date(2021, 11, 18, 3, 24, 0);
// Create a DateTimeFormat object with the locale ID being en-GB.
let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB');
let formattedDateRange: string = formatter.formatRange(startDate, endDate); // formattedDateRange = '17/12/2021 - 18/12/2021'

#### \[h2\]resolvedOptions(deprecated)

resolvedOptions(): DateTimeOptions

This API is supported since API version 6 and deprecated since API version 20. You are advised to use [Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions) instead.

Obtains the options for creating a **DateTimeOptions** object.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [DateTimeOptions](#datetimeoptionsdeprecated) | Options for the **DateTimeOptions** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

let formatter: intl.DateTimeFormat = new intl.DateTimeFormat('en-GB', { dateStyle: 'full', timeStyle: 'medium' });
// Obtain the options of the DateTimeFormat object.
let options: intl.DateTimeOptions = formatter.resolvedOptions();
let dateStyle: string | undefined = options.dateStyle; // dateStyle = 'full'
let timeStyle: string | undefined = options.timeStyle; // timeStyle = 'medium'

#### DateTimeOptions(deprecated)

This API is supported since API version 6 and is deprecated since API version 20. You are advised to use **Intl.DateTimeFormatOptions** or **Intl.ResolvedDateTimeFormatOptions** instead. For details, see [Intl.DateTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) and [Intl.DateTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/resolvedOptions).

Defines the options for a **DateTimeOptions** object. Since API version 9, the **DateTimeOptions** attribute is changed from mandatory to optional.

**Widget capability**: Since API version 11, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| locale | string | No | Yes | 
Valid locale ID, for example, **zh-Hans-CN**.

The default value is the current system locale.

 |
| dateStyle | string | No | Yes | 

Date display format. The value can be:

"long", "short", "medium", "full", or "auto".

For details about their display effects, see [Table 1](#appendix).

 |
| timeStyle | string | No | Yes | 

Time display format. The value can be:

"long", "short", "medium", "full", or "auto".

For details about their display effects, see [Table 2](#appendix).

 |
| hourCycle | string | No | Yes | 

Hour cycle. The value can be:

"h11", "h12", "h23", or "h24".

For the display effects when **dateStyle** or **timeStyle** is not set, see [Table 5](#appendix).

For the display effects when **dateStyle** or **timeStyle** is not set, see [Table 6](#appendix).

 |
| timeZone | string | No | Yes | Time zone in use. The value is a valid IANA time zone ID. |
| numberingSystem | string | No | Yes | 

Numbering system. The value can be:

**adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.

 |
| hour12 | boolean | No | Yes | 

Whether to use the 12-hour clock. The value **true** means to use the 12-hour clock, and the value **false** means the opposite.

If both **hour12** and **hourCycle** are set, **hourCycle** does not take effect.

If **hour12** and **hourCycle** are not set and the 24-hour clock is turned on, the default value of **hour12** is **false**.

 |
| weekday | string | No | Yes | 

Week display format. The value can be:

"long", "short", "narrow", or "auto".

For details about their display effects, see [Table 4](#appendix).

 |
| era | string | No | Yes | 

Epoch display format. The value can be:

"long", "short", "narrow", or "auto".

For details about their display effects, see [Table 9](#appendix).

 |
| year | string | No | Yes | 

Year display format. The value can be:

"numeric" or "2-digit".

For details about their display effects, see [Table 3](#appendix).

 |
| month | string | No | Yes | 

Month display format. The value can be:

"numeric", "2-digit", "long", "short", "narrow", or "auto".

For details about their display effects, see [Table 7](#appendix).

 |
| day | string | No | Yes | 

Day display format. The value can be:

"numeric" or "2-digit".

 |
| hour | string | No | Yes | 

Hour display format. The value can be:

"numeric" or "2-digit".

 |
| minute | string | No | Yes | 

Minute display format. The value can be:

"numeric" or "2-digit".

 |
| second | string | No | Yes | 

Second display format. The value can be:

"numeric" or "2-digit".

 |
| timeZoneName | string | No | Yes | 

Localized representation of a time zone name. The value can be:

"long", "short", or "auto".

For details about their display effects, see [Table 8](#appendix).

 |
| dayPeriod | string | No | Yes | 

Time period display format. The value can be:

"long", "short", "narrow", or "auto".

For details about their display effects, see [Table 10](#appendix).

 |
| localeMatcher | string | No | Yes | 

Locale matching algorithm. The value can be:

\- **lookup**: exact match.

\- "best fit": best match.

 |
| formatMatcher | string | No | Yes | 

Format matching algorithm. The value can be:

\- **basic**: exact match.

\- "best fit": best match.

 |

#### NumberFormat

Performs standard number formatting.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor8+

constructor()

Creates a **NumberFormat** object for the current system locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object using the current system locale ID.
let formatter: intl.NumberFormat = new intl.NumberFormat();

#### \[h2\]constructor

constructor(locale: string | Array<string>, options?: NumberOptions)

Creates a **NumberFormat** object based on the specified locale and options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Array<string> | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [NumberOptions](#numberoptions) | No | Options for creating the **NumberFormat** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with locale ID being en-GB, style being decimal, and notation being scientific.
let formatter: intl.NumberFormat = new intl.NumberFormat('en-GB', { style: 'decimal', notation: 'scientific' });

#### \[h2\]format

format(num: number): string

Formats a number.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| num | number | Yes | Number to be formatted. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted number. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a NumberFormat object with a locale ID array. The locale ID en-GB is valid and therefore is used.
let formatter: intl.NumberFormat = new intl.NumberFormat(\['en-GB', 'zh'\], { style: 'decimal', notation: 'scientific' });
let formattedNumber: string = formatter.format(1223); // formattedNumber = 1.223E3
let options: intl.NumberOptions = {
  roundingPriority: 'lessPrecision',
  maximumFractionDigits: 3,
  maximumSignificantDigits: 3
}
formatter = new intl.NumberFormat('en', options);
let result: string = formatter.format(1.23456); // result = 1.23

#### \[h2\]formatRange18+

formatRange(startRange: number, endRange: number): string

Formats a number range.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| startRange | number | Yes | Start number. |
| endRange | number | Yes | End number. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted number range. |

**Example**

import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat('en-US', { style: 'unit', unit: 'meter' });
let formattedRange: string = formatter.formatRange(0, 3); // formattedRange: 0–3 m

#### \[h2\]resolvedOptions

resolvedOptions(): NumberOptions

Obtains the options for creating a **NumberFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [NumberOptions](#numberoptions) | Options for creating the **NumberFormat** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

let formatter: intl.NumberFormat = new intl.NumberFormat(\['en-GB', 'zh'\], { style: 'decimal', notation: 'scientific' });
// Obtain the options of the NumberFormat object.
let options: intl.NumberOptions = formatter.resolvedOptions();
let style: string | undefined = options.style; // style = 'decimal'
let notation: string | undefined = options.notation; // notation = 'scientific'

#### NumberOptions

Options for creating the **NumberFormat** object. Since API version 9, the **NumberOptions** attribute is changed from mandatory to optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| locale | string | No | Yes | 
Valid locale ID, for example, **zh-Hans-CN**.

The default value is the current system locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| currency | string | No | Yes | 

Currency unit. The value must comply with the [ISO-4217 standard](https://www.iso.org/iso-4217-currency-codes.html), for example, EUR, CNY, and USD.

From API version 12, a three-digit number is supported, for example, **978**, **156**, or **840**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| currencySign | string | No | Yes | 

Currency unit symbol. The value can be **standard** or **accounting**.

The default value is **standard**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 19](#appendix).

 |
| currencyDisplay | string | No | Yes | 

Currency display mode. The value can be **symbol**, **narrowSymbol**, **code**, or **name**.

The default value is **symbol**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 20](#appendix).

 |
| unit | string | No | Yes | 

Unit name, for example, **meter**, **inch**, or **hectare**.

The combination units supported since API version 18 are as follows: beat-per-minute, body-weight-per-second, breath-per-minute, foot-per-hour, jump-rope-per-minute, meter-per-hour, milliliter-per-minute-per-kilogram, rotation-per-minute, step-per-minute, and stroke-per-minute.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| unitDisplay | string | No | Yes | 

Display format of units. The value can be **long**, **short**, or **narrow**.

The default value is **short**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 21](#appendix).

 |
| unitUsage8+ | string | No | Yes | 

Application scenario of units. The value can be any of the following: "default\*\*, **area-land-agricult**, **area-land-commercl**, **area-land-residntl**, **length-person**, **length-person-small**, **length-rainfall**, **length-road**, **length-road-small**, **length-snowfall**, **length-vehicle**, **length-visiblty**, **length-visiblty-small**, **length-person-informal**, **length-person-small-informal**, **length-road-informal**, **speed-road-travel**, **speed-wind**, **temperature-person**, **temperature-weather**, **volume-vehicle-fuel**, **elapsed-time-second**, **size-file-byte**, or **size-shortfile-byte**.

The default value is **default**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 22](#appendix).

 |
| signDisplay | string | No | Yes | 

Number sign display format. The value can be:

\- "auto": automatically determines whether to display the plus or minus sign.

\- "never": do not display the plus or minus sign.

\- "always": always displays the plus or minus sign.

\- "exceptZero": displays the plus or minus sign for all values except 0.

Default value: **"auto"**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| compactDisplay | string | No | Yes | 

Compact display format. The value can be **long** or **short**.

The default value is **short**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 18](#appendix).

 |
| notation | string | No | Yes | 

Number notation. The value can be **standard**, **scientific**, **engineering**, or **compact**.

The default value is **standard**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 17](#appendix).

 |
| localeMatcher | string | No | Yes | 

Locale matching algorithm. The value can be **lookup** or **best fit**.

The default value is **best fit**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| style | string | No | Yes | 

Number display format. The value can be **decimal**, **currency**, **percent**, or **unit**.

The default value is **decimal**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| numberingSystem | string | No | Yes | 

Numbering system. The value can be:

**adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.

The default value is the default numbering system of the locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| useGrouping | boolean | No | Yes | 

Whether to enable grouping for display. The value **true** means to enable grouping for display, and the value **false** means the opposite.

The default value is **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 16](#appendix).

 |
| minimumIntegerDigits | number | No | Yes | 

Minimum number of digits allowed in the integer part of a number. The value ranges from **1** to **21**.

The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 11](#appendix).

 |
| minimumFractionDigits | number | No | Yes | 

Minimum number of digits in the fraction part of a number. The value ranges from **0** to **20**.

The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 12](#appendix).

 |
| maximumFractionDigits | number | No | Yes | 

Maximum number of digits in the fraction part of a number. The value ranges from **1** to **21**.

The default value is **3**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 13](#appendix).

 |
| minimumSignificantDigits | number | No | Yes | 

Minimum number of the least significant digits. The value ranges from **1** to **21**.

The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 14](#appendix).

 |
| maximumSignificantDigits | number | No | Yes | 

Maximum number of the least significant digits. The value ranges from **1** to **21**.

The default value is **21**.

**Atomic service API**: This API can be used in atomic services since API version 12.

For details about their display effects, see [Table 15](#appendix).

 |
| roundingPriority18+ | string | No | Yes | 

Rounding priority used when both the maximum number of fraction digits and the maximum number of valid digits are set. The value can be **auto**, **morePrecision**, or **lessPrecision**. The value **morePrecision** indicates that the maximum number of fraction digits is used. The value **lessPrecision** indicates that the maximum number of valid digits is used.

The default value is **auto**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| roundingIncrement18+ | number | No | Yes | 

Rounding increment. The value can be **1**, **2**, **5**, **10**, **20**, **25**, **50**, **100**, **200**, **250**, **500**, **1000**, **2000**, **2500**, or **5000**.

The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| roundingMode18+ | string | No | Yes | 

Rounding mode. The value can be:

\- **ceil**: rounding up.

\- **floor**: rounding down.

\- **expand**: rounding away from 0.

\- **trunc**: rounding toward 0.

\- **halfCeil**: half-rounding up; that is, rounding up when the decimal number is greater than or equal to half of the increment, and rounding down otherwise.

\- **halfFloor**: half-rounding down; that is, rounding up when the decimal number is greater than half of the increment, and rounding down otherwise.

\- **halfExpand**: half-rounding away from 0; that is, rounding away from 0 when the decimal number is greater than or equal to half of the increment, and rounding toward 0 otherwise.

\- **halfTrunc**: half-rounding toward 0; that is, rounding away from 0 when the decimal number is greater than half of the increment, and rounding toward 0 otherwise.

\- "halfEven": half-rounding to the nearest even number; that is, rounding away from 0 when the decimal number is greater than half of the increment, rounding toward 0 when the decimal number is less than half of the increment, and rounding to the nearest even number when the decimal number is exactly half of the increment.

The default value is **halfExpand**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### Collator8+

Performs string collation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor8+

constructor()

Creates a **Collator** object for the current system locale.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a Collator object using the current system locale ID.
let collator = new intl.Collator();

#### \[h2\]constructor8+

constructor(locale: string | Array<string>, options?: CollatorOptions)

Creates a **Collator** object based on the specified locale and options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Array<string> | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [CollatorOptions](#collatoroptions8) | No | Options for creating a **Collator** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a Collator object with the locale ID being zh-CN, localeMatcher being lookup, and usage being sort.
let collator = new intl.Collator('zh-CN', {localeMatcher: 'lookup', usage: 'sort'});

#### \[h2\]compare8+

compare(first: string, second: string): number

Compares two strings based on the specified collation rules.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| first | string | Yes | First string to compare. |
| second | string | Yes | Second string to compare. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Comparison result.

\- If the value is a negative number, the first string comes before the second string.

\- If the value is **0**, the first and second strings are in the same sequence.

\- If the value is a positive number, the first string is comes after the second string.

 |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a Collator object with the locale ID being en-GB.
let collator = new intl.Collator('en-GB');
// Compare the sequence of the first and second strings.
let compareResult = collator.compare('first', 'second'); // compareResult = -1

#### \[h2\]resolvedOptions8+

resolvedOptions(): CollatorOptions

Obtains the options for creating a **Collator** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [CollatorOptions](#collatoroptions8) | Options for creating a **Collator** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

let collator = new intl.Collator('zh-Hans', { usage: 'sort', ignorePunctuation: true });
// Obtain the options of the Collator object.
let options = collator.resolvedOptions();
let usage = options.usage; // usage = 'sort'
let ignorePunctuation = options.ignorePunctuation; // ignorePunctuation = true

#### CollatorOptions8+

Defines the options for creating a **Collator** object.

Since API version 9, the attributes in **CollatorOptions** are optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| localeMatcher | string | No | Yes | 
Locale matching algorithm. The options are as follows:

**lookup**: fuzzy match.

**best fit**: exact match.

The default value is **best fit**.

 |
| usage | string | No | Yes | 

Purpose of comparison. The options are as follows:

\- **sort**: sorting.

\- **search**: search for matched strings.

The default value is **sort**.

 |
| sensitivity | string | No | Yes | 

Differences in the strings that lead to non-zero return values. The options are as follows:

\- **base**: Different letters are considered unequal, for example, 'a' ≠ 'b', 'a' = 'á', 'a' = 'A'.

\- **accent**: Different letters or same letters with different pronunciations are considered unequal, for example, 'a' ≠ 'b', 'a' ≠ 'á', 'a' = 'A'.

\- **case**: Different letters or same letters with different cases are considered unequal, for example, 'a' ≠ 'b', 'a' = 'á', 'a' ≠ 'A'.

\- **variant**: Different letters, pronunciations, other distinguishing marks, or cases are all considered unequal, for example, 'a' ≠ 'b', 'a' ≠ 'á', 'a' ≠ 'A'.

The default value is **variant**.

 |
| ignorePunctuation | boolean | No | Yes | 

Whether to ignore punctuation. The value **true** means to ignore punctuation, and the value **false** means the opposite.

The default value is **false**.

 |
| collation | string | No | Yes | 

Collation rules for the locale. The value can be:

**big5han**: Pinyin sorting for Latin letters.

**compat**: compatibility sorting, only for Arabic.

**dict**: dictionary-style sorting, only for Singhalese.

**direct**: binary code point sorting.

**ducet**: sorting according to the Unicode collation element table.

**eor**: sorting according to the European collation rules.

**gb2312**: Pinyin sorting, only for Chinese.

**phonebk**: phone book-style sorting.

**phonetic**: phonetic sorting.

**pinyin**: Pinyin sorting.

**reformed**: reformed sorting, only for Swedish.

**searchjl**: special sorting for Korean initial consonant search.

**stroke**: stroke sorting for Chinese.

**trad**: traditional-style sorting, for example, Spanish.

unihan: radical-stroke sorting for Han characters, only for Chinese, Japanese, and Korean.

**zhuyin**: Zhuyin sorting, only for Chinese.

The default value is **default**.

 |
| numeric | boolean | No | Yes | 

Whether numeric sorting is used. The options are as follows:

\- **true**: Numeric sorting is used. For example, '1' < '2' < '10' < '11'.

\- **false**: Numeric sorting is not used. For example, '1' < '10' < '11' < '2'.

The default value is **false**.

 |
| caseFirst | string | No | Yes | 

Whether case is taken into account for the locale's collation rules. The value can be:

**upper**: Uppercase letters come first.

**lower**: Lowercase letters come first.

\- **false**: The default collation rules of the locale are used.

The default value is **false**.

 |

#### PluralRules(deprecated)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules) instead.

Obtains the plural rule type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor(deprecated)

constructor()

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules) instead.

Creates a **PluralRules** object to obtain the singular-plural type of numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object using the current system locale ID.
let pluralRules = new intl.PluralRules();

#### \[h2\]constructor(deprecated)

constructor(locale: string | Array<string>, options?: PluralRulesOptions)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.PluralRules.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules) instead.

Creates a **PluralRules** object to obtain the singular-plural type of numbers.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Array<string> | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [PluralRulesOptions](#pluralrulesoptionsdeprecated) | No | Options for creating a **PluralRules** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-CN, localeMatcher being lookup, and type being cardinal.
let pluralRules: intl.PluralRules = new intl.PluralRules('zh-CN', { localeMatcher: 'lookup', type: 'cardinal' });

#### \[h2\]select(deprecated)

select(n: number): string

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.PluralRules.select](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/select) instead.

Obtains the singular-plural type of the specified number.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| n | number | Yes | Number for which the singular-plural type is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
Singular-plural type. The value can be any of the following: **zero**, **one**, **two**, **few**, **many**, **others**.

For details about the meanings of different values, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

 |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a PluralRules object with the locale ID being zh-Hans.
let zhPluralRules = new intl.PluralRules('zh-Hans');
// Determine the singular-plural type corresponding to number 1 in locale zh-Hans.
let plural = zhPluralRules.select(1); // plural = 'other'

// Create a PluralRules object with the locale ID being en-US.
let enPluralRules = new intl.PluralRules('en-US');
// Determine the singular-plural type corresponding to number 1 in locale en-US.
plural = enPluralRules.select(1); // plural = 'one'

#### PluralRulesOptions(deprecated)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.PluralRulesOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules) instead.

Defines the options for creating a **PluralRules** object. Since API version 9, the **PluralRulesOptions** attribute is changed from mandatory to optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| localeMatcher(deprecated) | string | No | Yes | 
This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.localeMatcher** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Locale matching algorithm. The value can be **lookup** or **best fit**.

The default value is **best fit**.

 |
| type(deprecated) | string | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.type** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Collation type. The value can be **cardinal** or **ordinal**.

The default value is **cardinal**.

The value **cardinal** indicates a cardinal number and the value **ordinal** indicates an ordinal number.

 |
| minimumIntegerDigits(deprecated) | number | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.minimumIntegerDigits** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Minimum number of digits allowed in the integer part of a number. The value ranges from **1** to **21**.

The default value is **1**.

 |
| minimumFractionDigits(deprecated) | number | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.minimumFractionDigits** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Minimum number of digits in the fraction part of a number. The value ranges from **0** to **20**.

The default value is **0**.

 |
| maximumFractionDigits(deprecated) | number | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.maximumFractionDigits** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Maximum number of digits in the fraction part of a number. The value ranges from **1** to **21**.

The default value is **3**.

 |
| minimumSignificantDigits(deprecated) | number | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.maximumFractionDigits** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Minimum number of the least significant digits. The value ranges from **1** to **21**.

The default value is **1**.

 |
| maximumSignificantDigits(deprecated) | number | No | Yes | 

This parameter is supported since API version 8 and is deprecated since API version 20. You are advised to use **Intl.PluralRulesOptions.maximumSignificantDigits** instead. For details, see [Intl.PluralRules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules/PluralRules#options).

Maximum number of the least significant digits. The value ranges from **1** to **21**.

The default value is **21**.

 |

#### RelativeTimeFormat(deprecated)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat) instead.

Formats the relative time.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

#### \[h2\]constructor(deprecated)

constructor()

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat) instead.

Creates a **RelativeTimeFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object using the current system locale ID.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat();

#### \[h2\]constructor(deprecated)

constructor(locale: string | Array<string>, options?: RelativeTimeFormatInputOptions)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat.constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat) instead.

Creates a **RelativeTimeFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locale | string | Array<string> | Yes | Locale ID or locale ID array. If the input is a locale ID array, the first valid locale ID is used. |
| options | [RelativeTimeFormatInputOptions](#relativetimeformatinputoptionsdeprecated) | No | Options for creating a **RelativeTimeFormat** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN, localeMatcher being lookup, and style being long.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN', {
  localeMatcher: 'lookup',
  numeric: 'always',
  style: 'long'
});

#### \[h2\]format(deprecated)

format(value: number, unit: string): string

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat.format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/format) instead.

Formats a relative time.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Value to format. |
| unit | string | Yes | 
Unit of the relative time.

The value can be any of the following: **year**, **quarter**, month\*\*, **week**, **day**, **hour**, **minute**, or **second**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Relative time after formatting. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being zh-CN.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('zh-CN');
// Obtain the localized representation (in unit of quarter) of number 3 in locale zh-CN.
let formatResult: string = formatter.format(3, 'quarter'); // formatResult = '3 quarters later'

#### \[h2\]formatToParts(deprecated)

formatToParts(value: number, unit: string): Array<object>

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat.formatToParts](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts) instead.

Formats the relative time

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Value to format. |
| unit | string | Yes | 
Unit of the relative time.

The value can be any of the following: **year**, **quarter**, month\*\*, **week**, **day**, **hour**, **minute**, or **second**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<object> | to parts. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en and numeric being auto.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en', { numeric: 'auto' });
let parts: Array<object> = formatter.formatToParts(10, 'seconds'); // parts = \[ {type: 'literal', value: 'in'}, {type: 'integer', value: 10, unit: 'second'}, {type: 'literal', value: 'seconds'} \]

#### \[h2\]resolvedOptions(deprecated)

resolvedOptions(): RelativeTimeFormatResolvedOptions

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormat.resolvedOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions) instead.

Defines the formatting options for a **RelativeTimeFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

**Return value**

| Type | Description |
| :-- | :-- |
| [RelativeTimeFormatResolvedOptions](#relativetimeformatresolvedoptionsdeprecated) | Options for the **RelativeTimeFormat** object. |

**Example**

import { intl } from '@kit.LocalizationKit';

// Create a RelativeTimeFormat object with the locale ID being en-GB.
let formatter: intl.RelativeTimeFormat = new intl.RelativeTimeFormat('en-GB', { style: 'short' });
// Obtain the options of the RelativeTimeFormat object.
let options: intl.RelativeTimeFormatResolvedOptions = formatter.resolvedOptions();
let style: string = options.style; // style = 'short'

#### RelativeTimeFormatInputOptions(deprecated)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat#options) instead.

Defines the configuration options for a **RelativeTimeFormat** object.

Since API version 9, the attributes in **RelativeTimeFormatInputOptions** are optional.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| localeMatcher | string | No | Yes | 
Locale matching algorithm. The value can be **lookup** or **best fit**.

The default value is **best fit**.

 |
| numeric | string | No | Yes | 

Format of the output result. It determines whether numeric values are used to represent relative dates or times in the formatting result. The value can be **always** or **auto**.

The default value is **always**.

For details about their display effects, see [Table 23](#appendix).

 |
| style | string | No | Yes | 

Length of an internationalized message. The value can be **long**, **short**, or **narrow**.

The default value is **long**.

For details about their display effects, see [Table 24](#appendix).

 |

#### RelativeTimeFormatResolvedOptions(deprecated)

This API is supported since API version 8 and deprecated since API version 20. You are advised to use [Intl.RelativeTimeFormatOptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions#return_value) instead.

Represents the formatting options for the **RelativeTimeFormat** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.I18n

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| locale | string | No | No | Locale ID, including the language, script, and region. |
| numeric | string | No | No | 
Format of the output result. It determines whether numeric values are used to represent relative dates or times in the formatting result. The value can be **always** or **auto**.

For details about their display effects, see [Table 23](#appendix).

 |
| style | string | No | No | 

Length of an internationalized message. The value can be **long**, **short**, or **narrow**.

For details about their display effects, see [Table 24](#appendix).

 |
| numberingSystem | string | No | No | 

Numbering system. The value can be:

**adlm**, **ahom**, **arab**, **arabext**, **bali**, **beng**, **bhks**, **brah**, **cakm**, **cham**, **deva**, **diak**, **fullwide**, **gong**, **gonm**, **gujr**, **guru**, **hanidec**, **hmng**, **hmnp**, **java**, **kali**, **khmr**, **knda**, **lana**, **lanatham**, **laoo**, **latn**, **lepc**, **limb**, **mathbold**, **mathdbl**, **mathmono**, **mathsanb**, **mathsans**, **mlym**, **modi**, **mong**, **mroo**, **mtei**, **mymr**, **mymrshan**, **mymrtlng**, **newa**, **nkoo**, **olck**, **orya**, **osma**, **rohg**, **saur**, **segment**, **shrd**, **sind**, **sinh**, **sora**, **sund**, **takr**, **talu**, **tamldec**, **telu**, **thai**, **tibt**, **tirh**, **vaii**, **wara**, or **wcho**.

 |

#### Appendix

**Date and Time Formatting Options**

The following tables use 13:04:00 and 00:25:00 on September 17, 2021 and locales **zh-CN** and **en** as examples to illustrate the values and display results of [DateTimeOptions](#datetimeoptionsdeprecated).

**Table 1** Date display format (dateStyle)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| full | Complete date display, including the year, month, day, and week. | Friday, September 17, 2021 | Friday, September 17, 2021 |
| long | Long date display, including the year, month, and day. | September 17, 2021 | September 17, 2021 |
| short | Short date display, including the year, month, and day. | 2021/9/17 | 9/17/21 |
| medium | Medium date display, including the year, month, and day. | September 17, 2021 | Sep 17, 2021 |

**Table 2** Time display format (timeStyle)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| full | Complete time display, including the time zone and time accurate to seconds. | 13:04:00 China Standard Time | 13:04:00 China Standard Time |
| long | Long time display, including the time zone expressed in the format of GMT + time zone offset and time accurate to seconds. | GMT+8 13:04:00 | 13:04:00 GMT+8 |
| short | Short time display, including hour and minute. | 13:04 | 13:04 |
| medium | Medium time display, including hour, minute, and second. | 13:04:00 | 13:04:00 |

**Table 3** Year display format (year)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| numeric | Complete year | 2021 | 2021 |
| 2-digit | 2-digit year display | 21 | 21 |

**Table 4** Weekday display format (weekday)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| long | Long weekday display | Friday | Friday |
| short | Short weekday display. | Fri. | Fri |
| narrow | Narrow weekday display. | 5 | F |

**Table 5** Hour cycle format (hourCycle)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 00:25:00 for Locale zh-CN |
| :-- | :-- | :-- | :-- |
| h11 | Use of 0 to 11 to indicate the hour | 1:04 p.m. | 0:25 a.m. |
| h12 | Use of 1 to 12 to indicate the hour | 1:04 p.m. | 12:25 a.m. |
| h23 | Use of 0 to 23 to indicate the hour | 13:04 | 00:25 |
| h24 | Use of 1 to 24 to indicate the hour | 13:04 | 24:25 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zSozJunuRAeZrkR1AZXp0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57448CEA3F17D104D7D1C9F0B2E2C3AA458A34C392787F44C2B4D38037ECC7BE)

The preceding table shows the display effect for different values of **hourCycle** when **dateStyle** or **timeStyle** is not set.

**Table 6** Hour cycle format (hourCycle)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 00:25:00 for Locale zh-CN |
| :-- | :-- | :-- | :-- |
| h11 | Use of 1 to 24 to indicate the hour | 13:04 | 24:25 |
| h12 | Use of 1 to 12 to indicate the hour | 1:04 p.m. | 12:25 a.m. |
| h23 | Use of 0 to 11 to indicate the hour | 1:04 | 0:25 |
| h24 | Use of 0 to 23 to indicate the hour | 13:04 | 0:25 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Sd_jiup8TrKFNS6HX_seUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3AB5AA0295FA13AECCB7D9C1BB9F33BE4B869FEAEFD2278023EF7F519A39BC3)

The preceding table shows the display effect for different values of **hourCycle** when **dateStyle** or **timeStyle** is set.

**Table 7** Month format (month)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| numeric | Display of the month as a number | 9 | 9 |
| 2-digit | Display of the month in two digits | 09 | 09 |
| long | Long month display | September | September |
| short | Short month display | 9 | Sep |
| narrow | Narrow month display | 9 | S |

**Table 8** Localized representation of time zone names (timeZoneName)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| long | Long time zone name | China Standard Time (CST) | China Standard Time |
| short | Short time zone name | GMT+8 | GMT+8 |

**Table 9** Era display format (era)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| long | Long epoch display | Common Era | Anno Domini |
| short | Short epoch display | Common Era | AD |
| narrow | Narrow epoch display | Common Era | A |

**Table 10** Time period format (dayPeriod)

| Value | Description | 2021-09-17 13:04:00 for Locale zh-CN | 2021-09-17 13:04:00 for Locale en |
| :-- | :-- | :-- | :-- |
| long | Long time period display | p.m. | in the afternoon |
| short | Short time period display | p.m. | in the afternoon |
| narrow | Narrow time period display | p.m. | in the afternoon |

**Number Formatting Options**

You can use **NumberOptions** to configure number formatting options, including minimum number of integer digits, minimum and maximum numbers of fraction digits, minimum and maximum numbers of significant digits, use of grouping for display, number notation, compact display, rounding mode, rounding priority, rounding increment, number display format, and numeral system. Supported number display formats include decimal, percent, currency, and unit.

The following uses **123000.123** as an example to show the parameter values and corresponding display effects.

**Table 11** Minimum number of integer digits (minimumIntegerDigits)

| Value | Display Effect |
| :-- | :-- |
| 6 | 123,000.123 |
| 7 | 0,123,000.123 |

**Table 12** Minimum number of decimal places (minimumFractionDigits)

| Value | Display Effect |
| :-- | :-- |
| 3 | 123,000.123 |
| 4 | 123,000.1230 |

**Table 3** Maximum number of fraction digits (maximumFractionDigits)

| Value | Display Effect |
| :-- | :-- |
| 3 | 123,000.123 |
| 2 | 123,000.12 |

**Table 14** Minimum number of significant digits (minimumSignificantDigits)

| Value | Display Effect |
| :-- | :-- |
| 9 | 123,000.123 |
| 10 | 123,000.1230 |

**Table 15** Maximum number of significant digits (maximumSignificantDigits)

| Value | Display Effect |
| :-- | :-- |
| 9 | 123,000.123 |
| 8 | 123,000.12 |

**Table 16** Use of grouping for display (useGrouping)

| Value | Display Effect |
| :-- | :-- |
| true | 123,000.123 |
| false | 123000.123 |

**Table 7** Number notation (notation)

| Value | Display Effect |
| :-- | :-- |
| standard | 123,000.123 |
| scientific | 1.230001E5 |
| engineering | 123.000123E3 |
| compact | 123K |

**Table 18** Compact display (compactDisplay)

| Value | Display Effect |
| :-- | :-- |
| short | 123K |
| long | 123 thousand |

**Currency Formatting Options**

Assume that the currency unit is USD and the value is **\-12300**.

**Table 19** Currency sign (currencySign)

| Value | Display Effect |
| :-- | :-- |
| standard | \-US$12,300.00 |
| accounting | (US$12,300.00) |

**Table 20** Currency display (currencyDisplay)

| Value | Display Effect |
| :-- | :-- |
| symbol | \-US$12,300.00 |
| narrowSymbol | \-$12,300.00 |
| code | \-USD 12,300.00 |
| name | \-12,300.00 US dollars |

**Unit Formatting Options**

Assume that the unit name is **hectare** and the value is **\-12300**.

**Table 21** Unit display (unitDisplay)

| Value | Display Effect |
| :-- | :-- |
| long | \-12,3000 hectares |
| short | \-12,300 ha |
| narrow | \-12,300ha |

**Table 22** Unit usage (unitUsage)

| Value | Display Effect |
| :-- | :-- |
| Unspecified | \-12,300 ha |
| default | \-47.491 sq mi |
| area-land-agricult | \-30,393.962 ac |

**Relative Time Formatting Options**

The following uses the relative time **1 day ago** and locale IDs **fr-FR** and **en-GB** as an example.

**Table 11** Numeric representation (numeric)

| Value | Description | Display Effect (fr-FR) | Display Effect (en-GB) |
| :-- | :-- | :-- | :-- |
| always | Use of a number to indicate the relative time | il y a 1 jour | 1 day ago |
| auto | Use of a phrase or value based on the locale ID to indicate the relative time | hier | yesterday |

**Table 24** Relative time style (style)

| Value | Description | Display Effect (fr-FR) | Display Effect (en-GB) |
| :-- | :-- | :-- | :-- |
| long | Long relative time display | il y a 1 jour | 1 day ago |
| short | Short relative time display | il y a 1 j | 1 day ago |
| narrow | Narrow relative time display | \-1 j | 1 day ago |
