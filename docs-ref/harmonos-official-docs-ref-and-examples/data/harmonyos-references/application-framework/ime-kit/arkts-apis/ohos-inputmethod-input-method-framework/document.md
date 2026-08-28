# @ohos.inputMethod (Input Method Framework)

The **inputMethod** module is oriented to common foreground applications (third-party applications and system applications such as Notes, Messaging, and Settings). It provides input method control and management capabilities, including displaying or hiding the soft keyboard, switching between input methods, and obtaining the list of all input methods.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/pJOOnH4vTFqevfoEnAKbyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45FBDAC9C3D6A6446F45192B4ABF70E0D7B188547EDDA5069FE761293A3959E2)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { inputMethod } from '@kit.IMEKit';

#### Constant

Provides the constants.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| MAX\_TYPE\_NUM8+ | number | 128 | Maximum number of supported input methods. |

#### InputMethodProperty8+

Describes the input method application attributes.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name9+ | string | Yes | No | Mandatory. Name of the input method package. |
| id9+ | string | Yes | No | Mandatory. Unique identifier of an input method extension in an app. **id** and **name** form a globally unique identifier of the input method extension. |
| label9+ | string | Yes | Yes | 
Optional.

\- When **InputMethodProperty** is used as the input parameter of an API for switching or querying, you do not need to set this field. You can use name and ID to uniquely specify an input method extension.

\- When **InputMethodProperty** is used as the return value of an API for querying (for example, [getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)), this field indicates the name of the input method extension displayed externally. Use the label configured for the InputMethodExtensionAbility. If no label is configured, the label of the application entry ability is automatically used. If no label is configured for the application entry ability, the label configured in **AppScope** is automatically used.

 |
| labelId10+ | number | Yes | Yes | 

Optional.

\- When **InputMethodProperty** is used as the input parameter of an API for switching or querying, you do not need to set this field. You can use name and ID to uniquely specify an input method extension.

\- When **InputMethodProperty** is used as the return value of an API for querying (for example, [getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)), this field indicates the resource ID of the **label** field.

 |
| icon9+ | string | Yes | Yes | 

Optional.

\- When **InputMethodProperty** is used as the input parameter of an API for switching or querying, you do not need to set this field. You can use name and ID to uniquely specify an input method extension.

\- When **InputMethodProperty** is used as the return value of an API for querying (for example, [getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)), this field indicates the input method icon data, which can be obtained through icon ID.

 |
| iconId9+ | number | Yes | Yes | 

Optional.

\- When **InputMethodProperty** is used as the input parameter of an API for switching or querying, you do not need to set this field. You can use name and ID to uniquely specify an input method extension.

\- When **InputMethodProperty** is used as the return value of an API for querying (for example, [getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)), this field indicates the resource ID of the **icon** field.

 |
| enabledState20+ | [EnabledState](#enabledstate15) | Yes | Yes | 

Optional.

\- When **InputMethodProperty** is used as the input parameter of an API for switching or querying, you do not need to set this field. You can use name and ID to uniquely specify an input method extension.

\- When **InputMethodProperty** is used as the return value of an API for querying (for example, [getCurrentInputMethod](#inputmethodgetcurrentinputmethod9)), this field indicates whether the input method is enabled.

 |
| extra9+ | object | No | Yes | 

Extra information about the input method. This parameter is reserved and currently has no specific meaning.

\- API version 10 and later: optional

\- API version 9: mandatory

 |
| packageName(deprecated) | string | Yes | No | 

Name of the input method package. Mandatory.

**Note**: This API is supported since API version 8 and deprecated since API version 9. You are advised to use **name** instead.

 |
| methodId(deprecated) | string | Yes | No | 

Unique ID of the input method. Mandatory.

**Note**: This API is supported since API version 8 and deprecated since API version 9. You are advised to use **id** instead.

 |

#### CapitalizeMode20+

Enumerates the modes of capitalizing the first letter of a text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The first letter is not capitalized. |
| SENTENCES | 1 | The first letter of each sentence is capitalized. |
| WORDS | 2 | The first letter of each word is capitalized. |
| CHARACTERS | 3 | All letters are capitalized. |

#### inputMethod.getController9+

getController(): InputMethodController

Obtains an [InputMethodController](#inputmethodcontroller) instance.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodController](#inputmethodcontroller) | **InputMethodController** instance. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

#### inputMethod.getDefaultInputMethod11+

getDefaultInputMethod(): InputMethodProperty

Obtains the default input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodProperty](#inputmethodproperty8) | Default input method. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();

#### inputMethod.getSystemInputMethodConfigAbility11+

getSystemInputMethodConfigAbility(): ElementName

Obtains the information about the input method configuration page ability.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [ElementName](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Element name of the input method configuration page ability. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { bundleManager } from '@kit.AbilityKit';

let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();

#### inputMethod.getSetting9+

getSetting(): InputMethodSetting

Obtains an [InputMethodSetting](#inputmethodsetting8) instance.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodSetting](#inputmethodsetting8) | **InputMethodSetting** instance. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800007 | input method setter error. Possible cause: create InputMethodSetting object failed. |

**Example**

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

#### inputMethod.switchInputMethod9+

switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void

Switches to another input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ZF7yASuDS8eSr0eOKR1mbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A56BF25A141F933826F71A82A63A3EEE2027F701C27B8A7A5300070A7C7CD42A)

-   In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | [InputMethodProperty](#inputmethodproperty8) | Yes | Target input method. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/cmgpMb_1STKghVXrySQFMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EE5604133FE08A116C6A114DD6D313F77293C8BE47C795281F02ADA9B54AC4A)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.switchInputMethod9+

switchInputMethod(target: InputMethodProperty): Promise<boolean>

Switches to another input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pND8wSAxSBSJ4H3quBKAdw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=228FF8B9C79BDC8969B193B81EBDAC1A15A2BDE9E792A613542B48AAB91A9EDC)

-   In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | [InputMethodProperty](#inputmethodproperty8) | Yes | Target input method. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the switching is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
inputMethod.switchInputMethod(currentIme).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching input method.');
  } else {
    console.error('Failed to switch input method.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}\`);
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/GpflRVCuSAmuRx9hVnIToA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA23016A9F5FB9169C4E6FBB3BBCC5327DC73DAA0F335C662D482CFA39FED43B)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.getCurrentInputMethod9+

getCurrentInputMethod(): InputMethodProperty

Obtains the current input method. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodProperty](#inputmethodproperty8) | **InputmethodProperty** instance of the current input method. |

**Example**

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();

#### inputMethod.switchCurrentInputMethodSubtype9+

switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void

Switches to another subtype of this input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/yCiTPh9gQimKU7FpA297-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FD7A8D8B491F98BFC4533F72132B6607B440B3707F7DBB690F19A591553B7B8)

-   In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT\_IME\_ABILITY** permission is required.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype) | Yes | Target input method subtype. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let extra: Record<string, string> = {}
inputMethod.switchCurrentInputMethodSubtype({
  id: "ServiceExtAbility",
  label: "",
  name: "com.example.keyboard",
  mode: "upper",
  locale: "",
  language: "",
  icon: "",
  iconId: 0,
  extra: extra
}, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching currentInputMethodSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodSubtype');
  }
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/u3yab2WjQuSpcUuVYkuXCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FEE3F4437B4A1C09C5044CF19FE7E62434008E66AD84ED9B70E95D9F2D89F8F)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.switchCurrentInputMethodSubtype9+

switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>

Switches to another subtype of this input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/DS9tjfjHT9aa6pnJL-484Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAB387CC84B7B3C441E84A8F5BFF1C99AEE4D693E06FA220EB4927BE9A57F09A)

-   In API version 9, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   In API version 10, this API can only be called by system applications and the current input method application, and the **ohos.permission.CONNECT\_IME\_ABILITY** permission is required.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype) | Yes | Target input method subtype. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the switching is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let extra: Record<string, string> = {}
inputMethod.switchCurrentInputMethodSubtype({
  id: "ServiceExtAbility",
  label: "",
  name: "com.example.keyboard",
  mode: "upper",
  locale: "",
  language: "",
  icon: "",
  iconId: 0,
  extra: extra
}).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching currentInputMethodSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodSubtype.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/g2wWPeN1RgaQtcDu-zVWwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFD0F090D091636B08270DE561144474977B73D1F7549DA5975E413CDCCA32FC)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.getCurrentInputMethodSubtype9+

getCurrentInputMethodSubtype(): InputMethodSubtype

Obtains the current input method subtype.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype) | Current input method subtype. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';

let currentImeSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();

#### inputMethod.switchCurrentInputMethodAndSubtype9+

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void

Switches to a specified subtype of a specified input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/J3pQUKvsQLSDf1encnXdeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F492090AA6178C976C424FB5A2C471EEDA081F6ECAC73E83F3960ACEB3CA1650)

-   In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | Yes | Target input method. |
| inputMethodSubtype | [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype) | Yes | Target input method subtype. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in switching currentInputMethodAndSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodAndSubtype.');
  }
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/LTJFhUVOQOa0F8a31TYO3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A3AC10B5C9BE0F1B26867819A4CC81E48C4ADB3D0957FCA58F1882D28A8068D)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.switchCurrentInputMethodAndSubtype9+

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>

Switches to a specified subtype of a specified input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/LIuwuamsToivYPhGwtqBUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0294739D73761782741C903E7B66BF47A7F7653A6DF396A0D9A22FCF3353FF1A)

-   In API versions 9 and 10, this API can only be called by system applications granted the **ohos.permission.CONNECT\_IME\_ABILITY** permission.
-   Since API version 11, this API can only be called by the current input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | Yes | Target input method. |
| inputMethodSubtype | [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype) | Yes | Target input method subtype. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the switching is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in switching currentInputMethodAndSubtype.');
  } else {
    console.error('Failed to switchCurrentInputMethodAndSubtype.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}\`);
});

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/z74Nd75bQIubeIb8tSVFhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75A96049EEA7464C2F8EE8F04607564F6459EAC4C25FE839286EFD6DEEF01C03)

In API version 11, the error code 201 permissions check fails. is removed.

#### inputMethod.getInputMethodController(deprecated)

getInputMethodController(): InputMethodController

Obtains an [InputMethodController](#inputmethodcontroller) instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/oh8bMyckSheycfCXSX2kDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DFAEB8DE7C467386E54A5A175898A40208A511333F363E420D4DE1F3679A4E7)

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getController](#inputmethodgetcontroller9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodController](#inputmethodcontroller) | Current **InputMethodController** instance. |

**Example**

let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();

#### inputMethod.getInputMethodSetting(deprecated)

getInputMethodSetting(): InputMethodSetting

Obtains an [InputMethodSetting](#inputmethodsetting8) instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/WWySejm5R4uZ8LZd9ieA4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91FA43C6044FD12E1831BFCFCA37FDDA44D5B7CA4E4CAA6242F7E682C5D1C037)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getSetting](#inputmethodgetsetting9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodSetting](#inputmethodsetting8) | **InputMethodSetting** instance. |

**Example**

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();

#### inputMethod.setSimpleKeyboardEnabled20+

setSimpleKeyboardEnabled(enable: boolean): void

Enables or disables the simple keyboard.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether to enable the simple keyboard. The value **true** means that the simple keyboard is enabled; the value **false** means the opposite.

The native edit box takes effect when it is focused next time, while the self-drawing component takes effect when the input method is attached by calling [attach](#attach10) next time.

 |

**Example**

  let enable: boolean = false;
  inputMethod.setSimpleKeyboardEnabled(enable);

#### inputMethod.onAttachmentDidFail22+

onAttachmentDidFail(callback: Callback<AttachFailureReason>): void

Subscribes to attachment failure events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[AttachFailureReason](#attachfailurereason22)\> | Yes | Callback used to return the reason for attachment failure. This callback is only invoked when the attachment failure is triggered by the registrant's process. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
  (reason: inputMethod.AttachFailureReason): void => {
    console.info(\`Attachment failed with reason: ${reason}.\`);
  if (reason === inputMethod.AttachFailureReason.CALLER\_NOT\_FOCUSED) {
    console.info(\`Failure reason is CALLER\_NOT\_FOCUSED.\`);
  }
  };
inputMethod.onAttachmentDidFail(attachmentDidFailCallback);

#### inputMethod.offAttachmentDidFail22+

offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void

Unsubscribes from attachment failure events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | Callback<[AttachFailureReason](#attachfailurereason22)\> | No | Callback used for unsubscription, which must be the same as that passed by the subscription API. If no parameter is specified, all callback functions for this event will be unsubscribed from. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
  (reason: inputMethod.AttachFailureReason): void => {
    console.info(\`Attachment failed with reason: ${reason}.\`);
  if (reason === inputMethod.AttachFailureReason.CALLER\_NOT\_FOCUSED) {
    console.info(\`Failure reason is CALLER\_NOT\_FOCUSED.\`);
  }
  };
inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
inputMethod.offAttachmentDidFail(attachmentDidFailCallback);

#### TextInputType10+

Enumerates the text input types.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | \-1 | None. |
| TEXT | 0 | Text. |
| MULTILINE | 1 | Multi-line. |
| NUMBER | 2 | Number. |
| PHONE | 3 | Phone number. |
| DATETIME | 4 | Date. |
| EMAIL\_ADDRESS | 5 | Email address. |
| URL | 6 | URL. |
| VISIBLE\_PASSWORD | 7 | Password. |
| NUMBER\_PASSWORD11+ | 8 | Numeric password. |
| SCREEN\_LOCK\_PASSWORD20+ | 9 | Lock screen password. |
| USER\_NAME20+ | 10 | Username. |
| NEW\_PASSWORD20+ | 11 | New password. |
| NUMBER\_DECIMAL20+ | 12 | Number with a decimal point. |
| ONE\_TIME\_CODE20+ | 13 | Verification code. |

#### EnterKeyType10+

Enumerates the function types represented by the Enter key of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSPECIFIED | 0 | Not specified. |
| NONE | 1 | None. |
| GO | 2 | Go. |
| SEARCH | 3 | Search. |
| SEND | 4 | Send. |
| NEXT | 5 | Next. |
| DONE | 6 | Done. |
| PREVIOUS | 7 | Previous. |
| NEWLINE12+ | 8 | Line break. |

#### KeyboardStatus10+

Enumerates the soft keyboard states of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | None. |
| HIDE | 1 | Hidden. |
| SHOW | 2 | Shown. |

#### Direction10+

Enumerates the directions of cursor movement of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| CURSOR\_UP | 1 | Upward. |
| CURSOR\_DOWN | 2 | Downward. |
| CURSOR\_LEFT | 3 | Leftward. |
| CURSOR\_RIGHT | 4 | Rightward. |

#### ExtendAction10+

Describes the type of the extended edit action on the text box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SELECT\_ALL | 0 | Select all. |
| CUT | 3 | Cut. |
| COPY | 4 | Copy. |
| PASTE | 5 | Paste. |

#### FunctionKey10+

Describes the type of the input method function key.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enterKeyType | [EnterKeyType](#enterkeytype10) | No | No | Function type represented by the Enter key of the input method. |

#### InputAttribute10+

Describes the attributes of the edit box, including the text input type and Enter key function type.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| textInputType | [TextInputType](#textinputtype10) | No | No | Enumerates the text input types. |
| enterKeyType | [EnterKeyType](#enterkeytype10) | No | No | Function type represented by the Enter key. |
| placeholder20+ | string | No | Yes | 
Placeholder information set for the edit box.

\- When placeholder information is set for the edit box, the length cannot exceed 255 characters (a placeholder longer than 255 characters will be automatically truncated to 255 characters). It is used to prompt or guide users to enter temporary text or symbols. (For example, the placeholder prompts whether the input item is mandatory.)

\- If no placeholder is set for the edit box, the value is an empty string by default.

\- This field is provided for the input method application when [attach](#attach10) is called.

 |
| abilityName20+ | string | No | Yes | 

Ability name set for the edit box.

\- If the ability name is set for the edit box, the length cannot exceed 127 characters. (A name longer than 127 characters will be automatically truncated to 127 characters.)

\- If the ability name is not set for the edit box, the value is an empty string by default.

\- This field is provided for the input method application when [attach](#attach10) is called.

 |

#### TextConfig10+

Describes the configuration of the edit box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| inputAttribute | [InputAttribute](#inputattribute10) | No | No | Edit box attribute. |
| cursorInfo | [CursorInfo](#cursorinfo10) | No | Yes | Cursor information. |
| selection | [Range](#range10) | No | Yes | Text selection range. |
| windowId | number | No | Yes | 
ID of the window where the edit box is located. The value must be an integer.

You are advised to call [getWindowProperties()](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowproperties9) to obtain the window ID.

 |
| newEditBox20+ | boolean | No | Yes | Whether the edit box is new. The value **true** means the edit box is new; the value **false** means the opposite. |
| capitalizeMode20+ | [CapitalizeMode](#capitalizemode20) | No | Yes | Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first letter is not capitalized by default. |

#### CursorInfo10+

Represents the cursor information.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | Horizontal coordinate of the cursor, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen. |
| top | number | No | No | Vertical coordinate of the cursor, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen. |
| width | number | No | No | Width of the cursor, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen. |
| height | number | No | No | Height of the cursor, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen. |

#### Range10+

Describes the range of the selected text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | No | Index of the first selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length. |
| end | number | No | No | Index of the last selected character in the text box. The value is an integer greater than or equal to 0, and cannot exceed the actual text length. The **end** value must be greater than the **start** value. |

#### Movement10+

Describes the direction in which the cursor moves when the text is selected.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| direction | [Direction](#direction10) | No | No | Direction in which the cursor moves when the text is selected. |

#### InputWindowInfo10+

Describes the window information of the input method keyboard.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the input method keyboard window. |
| left | number | No | No | Horizontal coordinate of the upper left corner of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen. |
| top | number | No | No | Vertical coordinate of the upper left corner of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen. |
| width | number | No | No | Width of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the width of the current screen. |
| height | number | No | No | Height of the input method keyboard window, in px. The value must be an integer. The minimum value is 0 and the maximum value is the height of the current screen. |

#### EnabledState15+

Indicates whether the input method is enabled.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| DISABLED | 0 | Disabled. |
| BASIC\_MODE | 1 | Basic mode. |
| FULL\_EXPERIENCE\_MODE | 2 | Full experience mode. |

#### RequestKeyboardReason15+

Enumerates the reasons for requesting the keyboard.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The keyboard request is triggered for no reason. |
| MOUSE | 1 | The keyboard request is triggered by a mouse operation. |
| TOUCH | 2 | The keyboard request is triggered by a touch operation. |
| OTHER | 20 | The keyboard request is triggered by other reasons. |

#### MessageHandler15+

Represents a custom communication object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/bL5vArD7RH6HP8-qMq0Vyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8600B7B17EB25309EDDF98FE73200AFD2894E601201FB40CA03D920B12123E7)

You can register this object to receive custom communication data sent by the input method application. When the custom communication data is received, the [onMessage](#onmessage15) callback in this object is triggered.

This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated15) callback of the penultimate registered object is triggered.

If this object is unregistered, its [onTerminated](#onterminated15) callback will be triggered.

#### \[h2\]onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

Receives custom data sent by the input method application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/5Kg_BKVfSMybZvAKMvfhtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E6FD19983953F566F15E9E6B63C7AFAA21DD2A5C44FF6A944133124912DA0D9)

This callback is triggered when the registered MeesageHandler receives custom communication data sent by the input method application.

The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgId | string | Yes | Identifier of the received custom communication data. |
| msgParam | ArrayBuffer | No | Message body of the received custom communication data. |

**Example**

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
inputMethodController.recvMessage(messageHandler);

#### \[h2\]onTerminated15+

onTerminated(): void

Listens for MessageHandler termination.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/90uOHSOwSf6LRmE2M0A61g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16C9EE7FA914DEF1EEDA2204DAC6F0DF977591BAB86B13ABE672CE62E8789BE1)

When an application registers a new MessageHandler object, the **OnTerminated** callback of the previous registered MessageHandler object is triggered.

When an application unregisters a MessageHandler object, the **OnTerminated** callback of the current registered MessageHandler object is triggered.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Example**

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
inputMethodController.recvMessage(messageHandler);

#### SetPreviewTextCallback17+

type SetPreviewTextCallback = (text: string, range: Range) => void

Callback triggered when the input method framework needs to display the text preview.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text preview. |
| range | [Range](#range10) | Yes | Describes the range of the selected text. |

#### AttachFailureReason22+

Enumerates the reasons for attachment failure.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| CALLER\_NOT\_FOCUSED | 0 | The caller does not belong to the application of the focused window. |
| IME\_ABNORMAL | 1 | The input method application is abnormal. |
| SERVICE\_ABNORMAL | 2 | The input method framework service is abnormal. |

#### InputMethodController

In the following API examples, you must first use [getController](#inputmethodgetcontroller9) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance.

#### \[h2\]attach10+

attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void

Attaches a self-drawing component to the input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/XM8-7odoS8iZAtFnsx8Yrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE6626AF1D188664109778B0F128C5EC7DD898FCCD9D9BCB9D3C3C602CCC7C4F)

An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.

If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowfocusable9), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window).

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | Yes | 
Whether to start the input method keyboard after the self-drawing component is attached to the input method.

\- **true** means to start the input method keyboard.

\- **false** means not to start the input method keyboard.

 |
| textConfig | [TextConfig](#textconfig10) | Yes | Configuration of the edit box. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to attach, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in attaching the inputMethod.');
});

#### \[h2\]attach10+

attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>

Attaches a self-drawing component to the input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/OgLXMGcoTcOQijhkSFrxUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC42F6A81773BC6A8C893E4A772E2F2BD1CC1AF562D2303B019135CB5EC39A67)

An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.

If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowfocusable9), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window).

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | Yes | 
Whether to start the input method keyboard after the self-drawing component is attached to the input method.

\- **true** means to start the input method keyboard.

\- **false** means not to start the input method keyboard.

 |
| textConfig | [TextConfig](#textconfig10) | Yes | Configuration of the edit box. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to attach, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]attach15+

attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>

Attaches a self-drawing component to the input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Ng4wNPzZRs2eI7ta5NKzTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28DD371F851866858A33F597EFB59CF5B440C098BB4E65316E90744EA06765B8)

An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.

If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#setwindowfocusable9), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window).

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| showKeyboard | boolean | Yes | 
Whether to start the input method keyboard after the self-drawing component is attached to the input method.

\- **true** means to start the input method keyboard.

\- **false** means not to start the input method keyboard.

 |
| textConfig | [TextConfig](#textconfig10) | Yes | Configuration of the edit box. |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason15) | Yes | Reason for requesting the keyboard. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().attach(true, textConfig, requestKeyboardReason).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to attach, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]discardTypingText20+

discardTypingText(): Promise<void>

Discards the text that is being typed. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/8j2aQ_v-R32sjAnHvaJ8Pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCA25D9F3B6BE1348756898F311762A27D15A1B9C32E89DCFC8094644CA4FA80)

This API can be called after the edit box is attached to an input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800015 | the other side does not accept the request. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().discardTypingText().then(() => {
  console.info('Succeeded discardTypingText.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to discardTypingText, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]showTextInput10+

showTextInput(callback: AsyncCallback<void>): void

Enters the text editing mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/9oA4X_tZSlKvg0rKOQI_Sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EA35CA749899A66B3FB96CBF3F302D2346034F5E2FC3C1E7A86588F0A39D79C)

After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to showTextInput, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in showing the inputMethod.');
});

#### \[h2\]showTextInput10+

showTextInput(): Promise<void>

Enters the text editing mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ZyrD1rnOSSO_FUmxDVKLYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4D1ECFECF9394149BE2AC02D7C231E9BE680DF463761DBA4E21063F0CBF3A1B)

After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput().then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to showTextInput, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]showTextInput15+

showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>

Enters the text editing mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/aAYuVplHQ4Cst7Wrkyzizg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51BF0B7C1F3795BCB66AE8DA29DC40F1E661FE546417D553755668ADCF9806B0)

After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason15) | Yes | Reason for requesting the keyboard. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().showTextInput(requestKeyboardReason).then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to showTextInput, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]hideTextInput10+

hideTextInput(callback: AsyncCallback<void>): void

Exits the text editing mode. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/zz96QLwiToq6so_utwkoew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=610659A63AEF2774DA05BA3BF4D25912FF4E74E14FEA1F9505930F924846632F)

If the soft keyboard is displayed when this API is called, it will be hidden.

Calling this API does not detach the edit box from the input method. The edit box can call [showTextInput](#showtextinput10) again to reenter the text editing mode.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to hideTextInput, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in hiding text input.');
});

#### \[h2\]hideTextInput10+

hideTextInput(): Promise<void>

Exits the text editing mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/KUF8OPPjQ2eZUic7pvJ4hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FC6D9A3EB9483BCDB024CCDAE4DED2904209EE034F69FF7094B6EF274A38447)

If the soft keyboard is displayed when this API is called, it will be hidden.

Calling this API does not detach the edit box from the input method. The edit box can call [showTextInput](#showtextinput10) again to reenter the text editing mode.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput().then(() => {
  console.info('Succeeded in hiding inputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to hideTextInput, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]detach10+

detach(callback: AsyncCallback<void>): void

Detaches the self-drawing component from the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to detach, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in detaching inputMethod.');
});

#### \[h2\]detach10+

detach(): Promise<void>

Detaches the self-drawing component from the input method. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach().then(() => {
  console.info('Succeeded in detaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to detach, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]setCallingWindow10+

setCallingWindow(windowId: number, callback: AsyncCallback<void>): void

Sets the window to be avoided by the input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/zKhQyJfvQ2OAOPBGoFsAag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A911CF4EC8B5E05E4737D21A463CD3004330E4CB59D97C7A2C0A7C4CF160218)

After the window ID of the application bound to the input method is passed in the API, the input method window will not cover the window holding the application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Window ID of the application bound to the input method. The value must be an integer. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting callingWindow.');
});

#### \[h2\]setCallingWindow10+

setCallingWindow(windowId: number): Promise<void>

Sets the window to be avoided by the input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/TvW-yg4MQaOSnISQHy47TQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=454E604ACBA9A165C5FB2951ACA7630B5929236991DD0D3C4F8B76D0EFA79368)

After the window ID of the application bound to the input method is passed in the API, the input method window will not cover the window holding the application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| windowId | number | Yes | Window ID of the application bound to the input method. The value must be an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId).then(() => {
  console.info('Succeeded in setting callingWindow.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]updateCursor10+

updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void

Updates the cursor information in this edit box. This API can be called to notify the input method of the cursor changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cursorInfo | [CursorInfo](#cursorinfo10) | Yes | Cursor information. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to updateCursor, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in updating cursorInfo.');
});

#### \[h2\]updateCursor10+

updateCursor(cursorInfo: CursorInfo): Promise<void>

Updates the cursor information in this edit box. This API can be called to notify the input method of the cursor changes. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cursorInfo | [CursorInfo](#cursorinfo10) | Yes | Cursor information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo).then(() => {
  console.info('Succeeded in updating cursorInfo.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to updateCursor, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]changeSelection10+

changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void

Updates the information about the selected text in this edit box, to notify the input method when the selected text content or text range changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | All input text. |
| start | number | Yes | Start position of the selected text. The value is an integer greater than or equal to 0. |
| end | number | Yes | End position of the selected text. The value is an integer greater than or equal to 0. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('text', 0, 5, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to changeSelection, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in changing selection.');
});

#### \[h2\]changeSelection10+

changeSelection(text: string, start: number, end: number): Promise<void>

Updates the information about the selected text in this edit box, to notify the input method when the selected text content or text range changes. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | All input text. |
| start | number | Yes | Start position of the selected text. The value is an integer greater than or equal to 0. |
| end | number | Yes | End position of the selected text. The value is an integer greater than or equal to 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('test', 0, 5).then(() => {
  console.info('Succeeded in changing selection.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to changeSelection, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]updateAttribute10+

updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void

Updates the attribute information of this edit box. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attribute | [InputAttribute](#inputattribute10) | Yes | Attribute information. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to updateAttribute, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in updating attribute.');
});

#### \[h2\]updateAttribute10+

updateAttribute(attribute: InputAttribute): Promise<void>

Updates the attribute information of this edit box. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attribute | [InputAttribute](#inputattribute10) | Yes | Attribute information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute).then(() => {
  console.info('Succeeded in updating attribute.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to updateAttribute, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]stopInputSession9+

stopInputSession(callback: AsyncCallback<boolean>): void

Ends this input session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/kTBsOUqYSUa8Cgcy6QwVmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4606F9952BCBE316B4975E7578F6171091B821A250E3BF96EECC7AF873E03D88)

This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to stopInputSession, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
});

#### \[h2\]stopInputSession9+

stopInputSession(): Promise<boolean>

Ends this input session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Y1X3X8i-Ql2-LM0QUTvrNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B00B6EED9135F82C9A6010EB7980E6AE07CE944B0ACC13B3C1653C0D4F248E67)

This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to stopInputSession, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]showSoftKeyboard9+

showSoftKeyboard(callback: AsyncCallback<void>): void

Shows the soft keyboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/0q0msSSWSTe0ejV5WtzIAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5B302AC5C7FDEEDD5E1EEAE570E5B013922EA215D81A1DCC6F299B8E528CD0E)

This API can be called only when the edit box is attached to the input method. That is, it can be called to show the soft keyboard only when the edit box is focused.

**Required permissions**: ohos.permission.CONNECT\_IME\_ABILITY (for system applications only)

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in showing softKeyboard.');
  } else {
    console.error(\`Failed to show softKeyboard, ${err.code}, message: ${err.message}\`);
  }
});

#### \[h2\]showSoftKeyboard9+

showSoftKeyboard(): Promise<void>

Shows the soft keyboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/E1De-faoQYSBKqTvk8ymYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=851F3136A357640B9EB8D17676E50E94FA04FE7B68274B1773D9FDC522F2DA8A)

This API can be called only when the edit box is attached to the input method. That is, it can be called to show the soft keyboard only when the edit box is focused.

**Required permissions**: ohos.permission.CONNECT\_IME\_ABILITY (for system applications only)

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard().then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]hideSoftKeyboard9+

hideSoftKeyboard(callback: AsyncCallback<void>): void

Hides the soft keyboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/xeJ3l2OETk-Dg4Q1ZPNdCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A2C374418D9073E53D408ECEF50D04E3F86B588C89AD65625B8C6942596FC0A)

This API can be called only when the edit box is attached to the input method. That is, it can be called to hide the soft keyboard only when the edit box is focused.

**Required permissions**: ohos.permission.CONNECT\_IME\_ABILITY (for system applications only)

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in hiding softKeyboard.');
  } else {
    console.error(\`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}\`);
  }
})

#### \[h2\]hideSoftKeyboard9+

hideSoftKeyboard(): Promise<void>

Hides the soft keyboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/vaC6wrVdRJa6oy08y0rO_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4EA92BBEB049F5423130F03B89F5927D3BBBEF0196ACC08E58BC21B2EB22F6A)

This API can be called only when the edit box is attached to the input method. That is, it can be called to hide the soft keyboard only when the edit box is focused.

**Required permissions**: ohos.permission.CONNECT\_IME\_ABILITY (for system applications only)

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard().then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]sendMessage15+

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

Sends the custom communication to the input method application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ByIrAfKETdmG7XbkNTyTTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A57CC8E4B481740A122394857B34ABCD3144E2AA63FA704470CA368E569F8BED)

This API can be called only when the edit box is attached to the input method and enter the edit mode, and the input method application is in full experience mode.

The maximum length of **msgId** is 256 B, and the maximum length of **msgParam** is 128 KB.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgId | string | Yes | Identifier of the custom data to be sent to the input method application. |
| msgParam | ArrayBuffer | No | Message body of the custom data to be sent to the input method application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800014 | the input method is in basic mode. |
| 12800015 | the other side does not accept the request. |
| 12800016 | input method client is not editable. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputMethod.getController().sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to send message, code: ${err.code}, message: ${err.message}\`);
});

#### \[h2\]recvMessage15+

recvMessage(msgHandler?: MessageHandler): void

Registers or unregisters MessageHandler.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/I2uYu50OR-WevOUa-j2pgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1670D7B766F8481BFBB892FD44D67AC51357D3710AB37BDBF80DA25DF2178419)

The [MessageHandler](#messagehandler15) object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated15) callback of the penultimate registered object is triggered.

If no parameter is set, unregister [MessageHandler](#messagehandler15). Its [onTerminated](#onterminated15) callback will be triggered.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgHandler | [MessageHandler](#messagehandler15) | No | 
This object receives custom communication data from the input method application through [onMessage](#onmessage15) and receives a message for terminating the subscription to this object through [onTerminated](#onterminated15).

If no parameter is set, unregister [MessageHandler](#messagehandler15). Its [onTerminated](#onterminated15) callback will be triggered.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.recvMessage(messageHandler);
// Unregister the MessageHandler.
inputMethodController.recvMessage();

#### \[h2\]stopInput(deprecated)

stopInput(callback: AsyncCallback<boolean>): void

Ends this input session. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/PmRtMm3kTxaYQ7GSGTmUzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87F53262D8E1C6C097FCD666CE6983C58E1C499A119740A2EF5EFDFB21D1E87C)

This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [stopInputSession](#stopinputsession9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to stopInput, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
});

#### \[h2\]stopInput(deprecated)

stopInput(): Promise<boolean>

Ends this input session. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/vPpqM3xPSkm_CeJV2ZZvXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBCDBD4B06146C765B8A0324F9C731FB914F6AC8A2632E99B607BD836880FFCA)

This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [stopInputSession](#stopinputsession9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to stopInput, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]on('insertText')10+

on(type: 'insertText', callback: (text: string) => void): void

Enables listening for the text insertion event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'insertText'**. |
| callback | (text: string) => void | Yes | 
Callback used to return the text to be inserted.

The application needs to operate the content in the edit box based on the text content returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

function callback1(text: string): void {
  console.info(\`Succeeded in getting callback1, data: ${text}\`);
}

function callback2(text: string): void {
  console.info(\`Succeeded in getting callback2, data: ${text}\`);
}

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
// Register a callback.
inputMethodController.on('insertText', callback1);
inputMethodController.on('insertText', callback2);
// Cancel only callback1 of insertText.
inputMethodController.off('insertText', callback1);
// Cancel all callbacks of insertText.
inputMethodController.off('insertText');

#### \[h2\]off('insertText')10+

off(type: 'insertText', callback?: (text: string) => void): void

Disables listening for the text insertion event of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'insertText'**. |
| callback | (text: string) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onInsertTextCallback: Callback<string> = (text: string): void => {
  console.info(\`Succeeded in subscribing insertText: ${text}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('insertText', onInsertTextCallback);
inputMethodController.off('insertText');

#### \[h2\]on('deleteLeft')10+

on(type: 'deleteLeft', callback: (length: number) => void): void

Enables listening for the leftward delete event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'deleteLeft'**. |
| callback | (length: number) => void | Yes | 
Callback used to return the length of the text to be deleted leftward.

The application needs to operate the content in the edit box based on the length returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('deleteLeft', (length: number) => {
  console.info(\`Succeeded in subscribing deleteLeft, length: ${length}\`);
});

#### \[h2\]off('deleteLeft')10+

off(type: 'deleteLeft', callback?: (length: number) => void): void

Disables listening for the leftward delete event.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'deleteLeft'**. |
| callback | (length: number) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onDeleteLeftCallback: Callback<number> = (length: number): void => {
  console.info(\`Succeeded in subscribing deleteLeft, length: ${length}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteLeft', onDeleteLeftCallback);
inputMethodController.off('deleteLeft');

#### \[h2\]on('deleteRight')10+

on(type: 'deleteRight', callback: (length: number) => void): void

Enables listening for the rightward delete event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'deleteRight'**. |
| callback | (length: number) => void | Yes | 
Callback used to return the length of the text to be deleted rightward.

The application needs to operate the content in the edit box based on the length returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('deleteRight', (length: number) => {
  console.info(\`Succeeded in subscribing deleteRight, length: ${length}\`);
});

#### \[h2\]off('deleteRight')10+

off(type: 'deleteRight', callback?: (length: number) => void): void

Disables listening for the rightward delete event.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at deleteRight. |
| callback | (length: number) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onDeleteRightCallback: Callback<number> = (length: number): void => {
  console.info(\`Succeeded in subscribing deleteRight, length: ${length}\`);
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteRight', onDeleteRightCallback);
inputMethodController.off('deleteRight');

#### \[h2\]on('sendKeyboardStatus')10+

on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void

Enables listening for the soft keyboard status event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'sendKeyboardStatus'**. |
| callback | (keyboardStatus: [KeyboardStatus](#keyboardstatus10)) => void | Yes | 
Callback used to return the soft keyboard status.

The application needs to perform operations based on the soft keyboard state returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(\`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}\`);
});

#### \[h2\]off('sendKeyboardStatus')10+

off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void

Disables listening for the input method soft keyboard status event of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'sendKeyboardStatus'**. |
| callback | (keyboardStatus: [KeyboardStatus](#keyboardstatus10)) => void | No | Callback used for disable listening. If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onSendKeyboardStatus: Callback<inputMethod.KeyboardStatus> = (keyboardStatus: inputMethod.KeyboardStatus): void => {
  console.info(\`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendKeyboardStatus', onSendKeyboardStatus);
inputMethodController.off('sendKeyboardStatus');

#### \[h2\]on('sendFunctionKey')10+

on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void

Enables listening for the function key sending event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'sendFunctionKey'**. |
| callback | (functionKey: [FunctionKey](#functionkey10)) => void | Yes | 
Callback used to return the function key information sent by the input method.

The application needs to perform operations based on the function key information returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
  console.info(\`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}\`);
});

#### \[h2\]off('sendFunctionKey')10+

off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void

Disables listening for the function key sending event of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'sendFunctionKey'**. |
| callback | (functionKey: [FunctionKey](#functionkey10)) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onSendFunctionKey: Callback<inputMethod.FunctionKey> = (functionKey: inputMethod.FunctionKey): void => {
  console.info(\`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendFunctionKey', onSendFunctionKey);
inputMethodController.off('sendFunctionKey');

#### \[h2\]on('moveCursor')10+

on(type: 'moveCursor', callback: (direction: Direction) => void): void

Enables listening for the cursor movement event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'moveCursor'**. |
| callback | (direction: [Direction](#direction10)) => void | Yes | 
Callback used to return the cursor movement direction.

The application needs to change the cursor position based on the cursor movement direction returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
  console.info(\`Succeeded in subscribing moveCursor, direction: ${direction}\`);
});

#### \[h2\]off('moveCursor')10+

off(type: 'moveCursor', callback?: (direction: Direction) => void): void

Disables listening for the cursor movement event of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'moveCursor'**. |
| callback | (direction: [Direction](#direction10)) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onMoveCursorCallback: Callback<inputMethod.Direction> = (direction: inputMethod.Direction): void => {
  console.info(\`Succeeded in subscribing moveCursor, direction: ${direction}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('moveCursor', onMoveCursorCallback);
inputMethodController.off('moveCursor');

#### \[h2\]on('handleExtendAction')10+

on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void

Enables listening for the extended action handling event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'handleExtendAction'**. |
| callback | (action: [ExtendAction](#extendaction10)) => void | Yes | 
Callback used to return the extended action type.

The application needs to perform operations based on the extended action type returned in the callback.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
  console.info(\`Succeeded in subscribing handleExtendAction, action: ${action}\`);
});

#### \[h2\]off('handleExtendAction')10+

off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void

Disables listening for the extended action handling event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'handleExtendAction'**. |
| callback | (action: [ExtendAction](#extendaction10)) => void | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onHandleExtendActionCallback: Callback<inputMethod.ExtendAction> = (action: inputMethod.ExtendAction): void => {
  console.info(\`Succeeded in subscribing handleExtendAction, action: ${action}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('handleExtendAction', onHandleExtendActionCallback);
inputMethodController.off('handleExtendAction');

#### \[h2\]on('selectByRange')10+

on(type: 'selectByRange', callback: Callback<Range>): void

Enables listening for the select-by-range event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'selectByRange'**. |
| callback | Callback<[Range](#range10)\> | Yes | 
Callback used to return the range of the text to be selected.

The application needs to select the text based on the range returned in the callback.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
  console.info(\`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}\`);
});

#### \[h2\]off('selectByRange')10+

off(type: 'selectByRange', callback?: Callback<Range>): void

Disables listening for the select-by-range event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'selectByRange'**. |
| callback | Callback<[Range](#range10)\> | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onSelectByRangeCallback: Callback<inputMethod.Range> = (range: inputMethod.Range): void => {
  console.info(\`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByRange', onSelectByRangeCallback);
inputMethodController.off('selectByRange');

#### \[h2\]on('selectByMovement')10+

on(type: 'selectByMovement', callback: Callback<Movement>): void

Enables listening for the select-by-cursor-movement event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'selectByMovement'**. |
| callback | Callback<[Movement](#movement10)\> | Yes | 
Callback used to return the direction in which the cursor moves.

The application needs to select the text based on the direction returned in the callback.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});

#### \[h2\]off('selectByMovement')10+

off(type: 'selectByMovement', callback?: Callback<Movement>): void

Disables listening for the select-by-cursor-movement event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'selectByMovement'**. |
| callback | Callback<[Movement](#movement10)\> | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let onSelectByMovementCallback: Callback<inputMethod.Movement> = (movement: inputMethod.Movement): void => {
  console.info(\`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByMovement', onSelectByMovementCallback);
inputMethodController.off('selectByMovement');

#### \[h2\]on('getLeftTextOfCursor')10+

on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void

Enables listening for the event of obtaining the length of text deleted leftward. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getLeftTextOfCursor'**. |
| callback | (length: number) => string | Yes | Callback used to obtain the text of the specified length deleted leftward. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('getLeftTextOfCursor', (length: number) => {
  console.info(\`Succeeded in subscribing getLeftTextOfCursor, length: ${length}\`);
  let text: string = "";
  return text;
});

#### \[h2\]off('getLeftTextOfCursor')10+

off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void

Disables listening for the event of obtaining the length of text deleted leftward. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getLeftTextOfCursor'**. |
| callback | (length: number) => string | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

let getLeftTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(\`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}\`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getLeftTextOfCursor', getLeftTextOfCursorCallback);
inputMethodController.off('getLeftTextOfCursor');

#### \[h2\]on('getRightTextOfCursor')10+

on(type: 'getRightTextOfCursor', callback: (length: number) => string): void

Enables listening for the event of obtaining the length of text deleted rightward. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getRightTextOfCursor'**. |
| callback | (length: number) => string | Yes | Callback used to obtain the text of the specified length deleted rightward. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('getRightTextOfCursor', (length: number) => {
  console.info(\`Succeeded in subscribing getRightTextOfCursor, length: ${length}\`);
  let text: string = "";
  return text;
});

#### \[h2\]off('getRightTextOfCursor')10+

off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void

Disables listening for the event of obtaining the length of text deleted rightward. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getRightTextOfCursor'**. |
| callback | (length: number) => string | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

let getRightTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(\`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}\`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getRightTextOfCursor', getRightTextOfCursorCallback);
inputMethodController.off('getRightTextOfCursor');

#### \[h2\]on('getTextIndexAtCursor')10+

on(type: 'getTextIndexAtCursor', callback: () => number): void

Enables listening for the event of obtaining the index of text at the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getTextIndexAtCursor'**. |
| callback | () => number | Yes | Callback used to obtain the index of text at the cursor. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**Example**

inputMethod.getController().on('getTextIndexAtCursor', () => {
  console.info(\`Succeeded in subscribing getTextIndexAtCursor.\`);
  let index: number = 0;
  return index;
});

#### \[h2\]off('getTextIndexAtCursor')10+

off(type: 'getTextIndexAtCursor', callback?: () => number): void

Disables listening for the event of obtaining the index of text at the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'getTextIndexAtCursor'**. |
| callback | () => number | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

let getTextIndexAtCursorCallback: () => number = (): number => {
  console.info(\`Succeeded in unsubscribing getTextIndexAtCursor.\`);
  let index: number = 0;
  return index;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getTextIndexAtCursor', getTextIndexAtCursorCallback);
inputMethodController.off('getTextIndexAtCursor');

#### \[h2\]on('setPreviewText')17+

on(type: 'setPreviewText', callback: SetPreviewTextCallback): void

Subscribes to the event for text preview operations in an input method application. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/-q4SRZLQQmSUhnTVz1yyIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD92399A2E7A50EEEF99406AFB3647AA965E468F5703170383DC5B594C40AE19)

To use the text preview function, you need to subscribe to this event before calling [attach](#attach10) and subscribe to this event together with [on('finishTextPreview')](#onfinishtextpreview17).

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setPreviewText'**. |
| callback | [SetPreviewTextCallback](#setpreviewtextcallback17) | Yes | Callback used to return the result. It is used to receive and return the text preview. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(\`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}\`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(\`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(\`SetPreviewTextCallback1 subscribed to setPreviewText\`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(\`SetPreviewTextCallback2 subscribed to setPreviewText\`);
// Cancel only the callback1 of setPreviewText.
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(\`SetPreviewTextCallback1 unsubscribed from setPreviewText\`);
// Cancel all callbacks of setPreviewText.
inputMethodController.off('setPreviewText');
console.info(\`All callbacks unsubscribed from setPreviewText\`);

#### \[h2\]off('setPreviewText')17+

off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void

Unsubscribes from the event for text preview operations in an input method application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setPreviewText'**. |
| callback | [SetPreviewTextCallback](#setpreviewtextcallback17) | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(\`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}\`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(\`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(\`SetPreviewTextCallback1 subscribed to setPreviewText\`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(\`SetPreviewTextCallback2 subscribed to setPreviewText\`);
// Cancel only the callback1 of setPreviewText.
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(\`SetPreviewTextCallback1 unsubscribed from setPreviewText\`);
// Cancel all callbacks of setPreviewText.
inputMethodController.off('setPreviewText');
console.info(\`All callbacks unsubscribed from setPreviewText\`);

#### \[h2\]on('finishTextPreview')17+

on(type: 'finishTextPreview', callback: Callback<void>): void

Subscribes to the event of finishing text preview. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/0yeC-GThQTuQuzjBtI-kDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0643D94E999E5E09C458B05E16119F6B01223B7B4ECD90550D7CCE8BD349D23F)

To use the text preview function, you need to subscribe to this event before calling [attach](#attach10) and subscribe to this event together with [on('setPreviewText')](#onsetpreviewtext17).

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'finishTextPreview'**. |
| callback | Callback<void> | Yes | Callback used to return the result. It is used to process the logic of finishing text preview. Return type: void |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(\`FinishTextPreviewCallback1: finishTextPreview event triggered\`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(\`FinishTextPreviewCallback2: finishTextPreview event triggered\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(\`FinishTextPreviewCallback1 subscribed to finishTextPreview\`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(\`FinishTextPreviewCallback2 subscribed to finishTextPreview\`);
// Cancel only the callback1 of finishTextPreview.
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(\`FinishTextPreviewCallback1 unsubscribed from finishTextPreview\`);
// Cancel all callbacks of finishTextPreview.
inputMethodController.off('finishTextPreview');
console.info(\`All callbacks unsubscribed from finishTextPreview\`);

#### \[h2\]off('finishTextPreview')17+

off(type: 'finishTextPreview', callback?: Callback<void>): void

Unsubscribes from the event of finishing text preview. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'finishTextPreview'**. |
| callback | Callback<void> | No | 
Callback used for disable listening, which must be the same as that passed by the **on** API.

If this parameter is not specified, listening will be disabled for all callbacks corresponding to the specified type.

 |

**Example**

import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(\`FinishTextPreviewCallback1: finishTextPreview event triggered\`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(\`FinishTextPreviewCallback2: finishTextPreview event triggered\`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(\`FinishTextPreviewCallback1 subscribed to finishTextPreview\`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(\`FinishTextPreviewCallback2 subscribed to finishTextPreview\`);
// Cancel only the callback1 of finishTextPreview.
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(\`FinishTextPreviewCallback1 unsubscribed from finishTextPreview\`);
// Cancel all callbacks of finishTextPreview.
inputMethodController.off('finishTextPreview');
console.info(\`All callbacks unsubscribed from finishTextPreview\`);

#### InputMethodSetting8+

In the following API examples, you must first use [getSetting](#inputmethodgetsetting9) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

#### \[h2\]on('imeChange')9+

on(type: 'imeChange', callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

Enables listening for the input method and subtype change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'imeChange'**. |
| callback | (inputMethodProperty: [InputMethodProperty](#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)) => void | Yes | Callback used to return the input method attributes and subtype. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';

inputMethod.getSetting()
  .on('imeChange', (inputMethodProperty: inputMethod.InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => {
    console.info(\`Succeeded in subscribing imeChange: inputMethodProperty.name: ${inputMethodProperty.name} \` +
      \`, inputMethodSubtype.id: ${inputMethodSubtype.id}\`);
  });

#### \[h2\]off('imeChange')9+

off(type: 'imeChange', callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

Disables listening for the input method and subtype change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listening type. The value is fixed at **'imeChange'**. |
| callback | (inputMethodProperty: [InputMethodProperty](#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)) => void | No | Callback used to return the input method attributes and subtype. |

**Example**

inputMethod.getSetting().off('imeChange');

#### \[h2\]listInputMethodSubtype9+

listInputMethodSubtype(inputMethodProperty: InputMethodProperty, callback: AsyncCallback<Array<InputMethodSubtype>>): void

Obtains all subtypes of a specified input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | Yes | Input method. |
| callback | AsyncCallback<Array<[InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)\>> | Yes | Callback used to return all subtypes of the specified input method. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty,
  (err: BusinessError, data: Array<InputMethodSubtype>) => {
    if (err) {
      console.error(\`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in listing inputMethodSubtype.');
  });

#### \[h2\]listInputMethodSubtype9+

listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>

Obtains all subtypes of a specified input method. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputMethodProperty | [InputMethodProperty](#inputmethodproperty8) | Yes | Input method. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)\>> | Promise used to return all subtypes of the specified input method. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodProperty: inputMethod.InputMethodProperty = {
  name: 'com.example.keyboard',
  id: 'propertyId',
  packageName: 'com.example.keyboard',
  methodId: 'propertyId',
}
let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listInputMethodSubtype(inputMethodProperty).then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing inputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]listCurrentInputMethodSubtype9+

listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void

Obtains all subtypes of this input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)\>> | Yes | Callback used to return all subtypes of the current input method. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
inputMethodSetting.listCurrentInputMethodSubtype((err: BusinessError, data: Array<InputMethodSubtype>) => {
  if (err) {
    console.error(\`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in listing currentInputMethodSubtype.');
});

#### \[h2\]listCurrentInputMethodSubtype9+

listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>

Obtains all subtypes of this input method. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md#inputmethodsubtype)\>> | Promise used to return all subtypes of the current input method. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

inputMethodSetting.listCurrentInputMethodSubtype().then((data: Array<InputMethodSubtype>) => {
  console.info('Succeeded in listing currentInputMethodSubtype.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getInputMethods9+

getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void

Obtains a list of activated or deactivated input methods. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/39inMIMBQfeUKpE5o-t_Lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF5D35EF010E4CF09616B9054804827E359F7E43957CD4A6D8473BAF0B38B1A0)

An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.

The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to return a list of activated input methods. The value **true** means to return a list of activated input methods, and **false** means to return a list of deactivated input methods. |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Yes | Callback used to return a list of activated or deactivated input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true, (err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(\`Failed to getInputMethods, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting inputMethods.');
});

#### \[h2\]getInputMethods9+

getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>

Obtains a list of activated or deactivated input methods. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/op-LOVrTQxy39s01-acKjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3E25656D7D1F55F6FC054B8ADA470F0875B98B5151315681D9056903CE89BEB)

An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.

The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to return a list of activated input methods. The value **true** means to return a list of activated input methods, and **false** means to return a list of deactivated input methods. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise used to return a list of activated or deactivated input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethods(true).then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting inputMethods.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to getInputMethods, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getInputMethodsSync11+

getInputMethodsSync(enable: boolean): Array<InputMethodProperty>

Obtains a list of activated or deactivated input methods. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/7rOn_1jSQJ6YlyFGq61f4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F652D8C816878ACF9FFF016EBB68E6176CCADC00E96AD95F7678EA74DF2C5958)

An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.

The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | Whether to return a list of activated input methods. The value **true** means to return a list of activated input methods, and **false** means to return a list of deactivated input methods. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[InputMethodProperty](#inputmethodproperty8)\> | List of activated or deactivated input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);

#### \[h2\]getAllInputMethods11+

getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void

Obtains a list of all input methods. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Yes | Callback used to return a list of all input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(\`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting all inputMethods.');
});

#### \[h2\]getAllInputMethods11+

getAllInputMethods(): Promise<Array<InputMethodProperty>>

Obtains a list of all input methods. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise used to return a list of all input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getAllInputMethods().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in getting all inputMethods.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getAllInputMethodsSync11+

getAllInputMethodsSync(): Array<InputMethodProperty>

Obtains a list of all input methods. This API returns the result synchronously.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[InputMethodProperty](#inputmethodproperty8)\> | List of all input methods. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();

#### \[h2\]showOptionalInputMethods(deprecated)

showOptionalInputMethods(callback: AsyncCallback<boolean>): void

Displays a dialog box for selecting an input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/mNP5DdOIQdiOPI1R5QZPpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2CFAE3B7C6BC3DC0E479FF8117408309787C779B144DFDA613FEBFFC5EF9F86)

This API is supported since API version 9 and deprecated since API version 18.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(\`Failed to showOptionalInputMethods.\`);
  }
});

#### \[h2\]showOptionalInputMethods(deprecated)

showOptionalInputMethods(): Promise<boolean>

Displays a dialog box for selecting an input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/R7WXMMt7TNeexl4K8PgkWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CB9AC72B599B7DDDD1BE5AF8B4352CCD6F0FA933C49338A8970CD5D9EFD95AC)

This API is supported since API version 9 and deprecated since API version 18.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().showOptionalInputMethods().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in showing optionalInputMethods.');
  } else {
    console.error(\`Failed to showOptionalInputMethods.\`);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]listInputMethod(deprecated)

listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void

Obtains a list of installed input methods. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/17WvXqDYRNqdnU8V1-yZEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1091652B901CB91E4031EA9203E840B3099CCD1B1A9183EB3EF4F2A3E4EC166D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getInputMethods](#getinputmethods9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Yes | Callback used to return the list of installed input methods. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
  if (err) {
    console.error(\`Failed to listInputMethod, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in listing inputMethod.');
});

#### \[h2\]listInputMethod(deprecated)

listInputMethod(): Promise<Array<InputMethodProperty>>

Obtains a list of installed input methods. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/sDI-RJH8QGWAeTeqZyqy9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C57851F745412A5CBBDB54C13D35077EB9A2507A4F075EF45B992FF137F6492)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getInputMethods](#getinputmethods9-1) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[InputMethodProperty](#inputmethodproperty8)\>> | Promise used to return the list of installed input methods. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().listInputMethod().then((data: Array<inputMethod.InputMethodProperty>) => {
  console.info('Succeeded in listing inputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to listInputMethod, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]displayOptionalInputMethod(deprecated)

displayOptionalInputMethod(callback: AsyncCallback<void>): void

Displays a dialog box for selecting an input method. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/-ACDo2lrSc-ofMAbw2oy9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32706D59E555E2B6651B522C66240B21603BD3E2CBF0AD21CB8824AA395BF396)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [inputmethodlistdialog](../ohos-inputmethodlist-input-method-list/document.md#inputmethodlistdialog) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in displaying optionalInputMethod.');
});

#### \[h2\]displayOptionalInputMethod(deprecated)

displayOptionalInputMethod(): Promise<void>

Displays a dialog box for selecting an input method. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/iQg0ErLSRHSIgRZtnv8e9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AD37F0FF699DFACF27829B942963C1A07A8519CF06ECD8895B444EE352928EB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [inputmethodlistdialog](../ohos-inputmethodlist-input-method-list/document.md#inputmethodlistdialog) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().displayOptionalInputMethod().then(() => {
  console.info('Succeeded in displaying optionalInputMethod.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getInputMethodState15+

getInputMethodState(): Promise<EnabledState>

Obtains the input method state. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[EnabledState](#enabledstate15)\> | Promise used to return the result. **EnabledState.DISABLED** indicates that the input method is disabled, **EnabledState.BASIC\_MODE** indicates that the input method is in basic mode, and **EnabledState.FULL\_EXPERIENCE\_MODE** indicates that the input method is in full experience mode. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800004 | not an input method application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getSetting().getInputMethodState().then((status: inputMethod.EnabledState) => {
  console.info(\`Succeeded in getInputMethodState, status: ${status}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getInputMethodState, code: ${err.code}, message: ${err.message}\`);
})
