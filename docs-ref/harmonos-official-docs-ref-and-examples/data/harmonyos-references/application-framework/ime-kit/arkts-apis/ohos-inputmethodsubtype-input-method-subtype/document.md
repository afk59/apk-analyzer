# @ohos.InputMethodSubtype (Input Method Subtype)

The **InputMethodSubtype** module provides APIs for managing the attributes of input method subtypes. The input method subtype allows the input method to switch to a specific mode or language, for example, the Chinese or English keyboard.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/oSsnD10uRvKivRKVxjxlAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2033F8ECDD0809093CC2CB3BCF401DE62222EDE6A92B656EACE1B086E836F059)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { InputMethodSubtype } from '@kit.IMEKit';

#### InputMethodSubtype

Defines the attributes of input method subtypes.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| label | string | Yes | Yes | Optional. Label of the input method subtype. |
| labelId10+ | number | Yes | Yes | Optional. Label ID of the input method subtype. |
| name | string | Yes | No | Mandatory. Bundle name of the application to which the input method subtype belongs. |
| id | string | Yes | No | Mandatory. ID of the input method subtype. |
| mode | 'upper' | 'lower' | Yes | Yes | Optional. Mode of the input method subtype, including **upper** (uppercase) and **lower** (lowercase). |
| locale | string | Yes | No | Mandatory. Locale of the input method subtype. |
| language | string | Yes | No | Mandatory. Language of the input method subtype. |
| icon | string | Yes | Yes | Optional. Icon of the input method subtype. It can be obtained by using **iconId**. This parameter is reserved. |
| iconId | number | Yes | Yes | Optional. Icon ID of the input method subtype. |
| extra | object | No | Yes | 
Mandatory. Extra information of the input method subtype.

**NOTE**

\- This parameter is optional since API version 10.

\- This parameter is reserved and currently has no specific meaning.

 |
