# @ohos.inputMethodEngine (Input Method Service)

The **inputMethodEngine** module is oriented to input method applications (including system and third-party input method applications). With the APIs of this module, input method applications are able to create soft keyboard windows, insert or delete characters, select text, and listen for physical keyboard events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/a90VKfjKRJuMVIkiL8wB-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93C8CEA960742884E4141D67C85F497FF37E7D7437C61F59A3ECA0A8741D2557)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { inputMethodEngine } from '@kit.IMEKit';

#### Constants

Provides the constant values of function keys, edit boxes, and the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| ENTER\_KEY\_TYPE\_UNSPECIFIED | number | 0 | No function is specified for the key. |
| ENTER\_KEY\_TYPE\_GO | number | 2 | Key that executes a command or navigates to a specific location. |
| ENTER\_KEY\_TYPE\_SEARCH | number | 3 | Key that initiates a search operation. |
| ENTER\_KEY\_TYPE\_SEND | number | 4 | Key that sends the text to its target. |
| ENTER\_KEY\_TYPE\_NEXT | number | 5 | Key that moves the focus to the next item in a sequence. |
| ENTER\_KEY\_TYPE\_DONE | number | 6 | Key that indicates that a task or input is complete. |
| ENTER\_KEY\_TYPE\_PREVIOUS | number | 7 | Key that moves the focus to the previous item in a sequence. |
| ENTER\_KEY\_TYPE\_NEWLINE12+ | number | 8 | Key that inserts a new line. |
| PATTERN\_NULL | number | \-1 | Any type of edit box. |
| PATTERN\_TEXT | number | 0 | Text edit box. |
| PATTERN\_NUMBER | number | 2 | Number edit box. |
| PATTERN\_PHONE | number | 3 | Phone number edit box. |
| PATTERN\_DATETIME | number | 4 | Date edit box. |
| PATTERN\_EMAIL | number | 5 | Email edit box. |
| PATTERN\_URI | number | 6 | URI edit box. |
| PATTERN\_PASSWORD | number | 7 | Password edit box. |
| PATTERN\_PASSWORD\_NUMBER11+ | number | 8 | Numeric password edit box. |
| PATTERN\_PASSWORD\_SCREEN\_LOCK11+ | number | 9 | Screen lock password edit box. |
| PATTERN\_USER\_NAME20+ | number | 10 | User name edit box. |
| PATTERN\_NEW\_PASSWORD20+ | number | 11 | New password edit box. |
| PATTERN\_NUMBER\_DECIMAL20+ | number | 12 | Edit box for numbers with decimal points. |
| PATTERN\_ONE\_TIME\_CODE20+ | number | 13 | Verification code edit box. |
| OPTION\_ASCII | number | 20 | ASCII values are allowed. |
| OPTION\_NONE | number | 0 | No input attribute is specified. |
| OPTION\_AUTO\_CAP\_CHARACTERS | number | 2 | Characters are allowed. |
| OPTION\_AUTO\_CAP\_SENTENCES | number | 8 | Sentences are allowed. |
| OPTION\_AUTO\_WORDS | number | 4 | Words are allowed. |
| OPTION\_MULTI\_LINE | number | 1 | Multiple lines are allowed. |
| OPTION\_NO\_FULLSCREEN | number | 10 | Half-screen style. |
| FLAG\_SELECTING | number | 2 | The edit box is being selected. |
| FLAG\_SINGLE\_LINE | number | 1 | The edit box allows only single-line input. |
| DISPLAY\_MODE\_PART | number | 0 | The edit box is displayed in half-screen mode. |
| DISPLAY\_MODE\_FULL | number | 1 | The edit box is displayed in full screen. |
| CURSOR\_UP9+ | number | 1 | The caret moves upward. |
| CURSOR\_DOWN9+ | number | 2 | The caret moves downward. |
| CURSOR\_LEFT9+ | number | 3 | The caret moves leftward. |
| CURSOR\_RIGHT9+ | number | 4 | The caret moves rightward. |
| WINDOW\_TYPE\_INPUT\_METHOD\_FLOAT9+ | number | 2105 | The input method is displayed in a floating window. |

#### inputMethodEngine.getInputMethodAbility9+

getInputMethodAbility(): InputMethodAbility

Obtains an [InputMethodAbility](#inputmethodability) instance for the input method. This API can be called only by an input method.

The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event, create/destroy an input method panel, and the like.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodAbility](#inputmethodability) | **InputMethodAbility** instance. |

**Example**

let InputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();

#### inputMethodEngine.getKeyboardDelegate9+

getKeyboardDelegate(): KeyboardDelegate

Obtains a [KeyboardDelegate](#keyboarddelegate) instance for the input method.

The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyboardDelegate](#keyboarddelegate) | **KeyboardDelegate** instance. |

**Example**

let KeyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.getKeyboardDelegate();

#### inputMethodEngine.getInputMethodEngine(deprecated)

getInputMethodEngine(): InputMethodEngine

Obtains an [InputMethodEngine](#inputmethodengine) instance for the input method.

The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/80f4V53zS9ODth3ppqYNIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12CDD52B16B4CD6C4B9C18A05CECF7C82EE262CFCAA4E7F9BDDB3A26CE83D07C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getInputMethodAbility](#inputmethodenginegetinputmethodability9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [InputMethodEngine](#inputmethodengine) | **InputMethodAbility** instance. |

**Example**

let InputMethodEngine: inputMethodEngine.InputMethodEngine = inputMethodEngine.getInputMethodEngine();

#### inputMethodEngine.createKeyboardDelegate(deprecated)

createKeyboardDelegate(): KeyboardDelegate

Obtains a [KeyboardDelegate](#keyboarddelegate) instance for the input method. The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and more.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/teY4Ui82Q4e6eYe0cYof7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7158345F82681BCF623ADC4C200056A43AAA6E01C0970B006B804BBF86B59DD3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getKeyboardDelegate](#inputmethodenginegetkeyboarddelegate9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [KeyboardDelegate](#keyboarddelegate) | **KeyboardDelegate** instance. |

**Example**

let keyboardDelegate: inputMethodEngine.KeyboardDelegate = inputMethodEngine.createKeyboardDelegate();

#### CommandDataType12+

type CommandDataType = number | string | boolean;

Defines the private data type, which varies depending on its function.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Type | Description |
| :-- | :-- |
| string | String. |
| number | Number. |
| boolean | Boolean. |

#### SizeChangeCallback15+

type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void

Callback triggered when the size of the input method panel changes.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [window.Size](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#size7) | Yes | Panel size. |
| keyboardArea | [KeyboardArea](#keyboardarea15) | No | Size of the keyboard area. |

#### InputMethodEngine

In the following API examples, you must first use [getInputMethodEngine](#inputmethodenginegetinputmethodenginedeprecated) to obtain an **InputMethodEngine** instance, and then call the APIs using the obtained instance.

#### \[h2\]on('inputStart')

on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

Enables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: [KeyboardController](#keyboardcontroller), textInputClient: [TextInputClient](#textinputclientdeprecated)) => void | Yes | Callback used to return the **KeyboardController** and **TextInputClient** instances. |

**Example**

inputMethodEngine.getInputMethodEngine()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let textInputClient: inputMethodEngine.TextInputClient = textClient;
    });

#### \[h2\]off('inputStart')

off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void

Disables listening for the input method binding event.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: [KeyboardController](#keyboardcontroller), textInputClient: [TextInputClient](#textinputclientdeprecated)) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodEngine()
  .off('inputStart',
    (kbController: inputMethodEngine.KeyboardController, textClient: inputMethodEngine.TextInputClient) => {
      console.info('delete inputStart notification.');
    });

#### \[h2\]on('keyboardShow'|'keyboardHide')

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyboardShow'** indicates the keyboard display event.

\- The value **'keyboardHide'** indicates the keyboard hiding event.

 |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

inputMethodEngine.getInputMethodEngine().on('keyboardShow', () => {
  console.info('inputMethodEngine keyboardShow.');
});
inputMethodEngine.getInputMethodEngine().on('keyboardHide', () => {
  console.info('inputMethodEngine keyboardHide.');
});

#### \[h2\]off('keyboardShow'|'keyboardHide')

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyboardShow'** indicates the keyboard display event.

\- The value **'keyboardHide'** indicates the keyboard hiding event.

 |
| callback | () => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodEngine().off('keyboardShow');
inputMethodEngine.getInputMethodEngine().off('keyboardHide');

#### InputMethodAbility

In the following API examples, you must first use [getInputMethodAbility](#inputmethodenginegetinputmethodability9) to obtain an **InputMethodAbility** instance, and then call the APIs using the obtained instance.

#### \[h2\]on('inputStart')9+

on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void

Enables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: [KeyboardController](#keyboardcontroller), inputClient: [InputClient](#inputclient9)) => void | Yes | Callback used to return instances related to input method operations. |

**Example**

inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
    });

#### \[h2\]off('inputStart')9+

off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void

Disables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStart'**. |
| callback | (kbController: [KeyboardController](#keyboardcontroller), inputClient: [InputClient](#inputclient9)) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('inputStart');

#### \[h2\]on('inputStop')9+

on(type: 'inputStop', callback: () => void): void

Enables listening for the input method unbinding event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStop'**. |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

inputMethodEngine.getInputMethodAbility().on('inputStop', () => {
  console.info('inputMethodAbility inputStop');
});

#### \[h2\]off('inputStop')9+

off(type: 'inputStop', callback: () => void): void

Disables listening for the input method stop event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'inputStop'**. |
| callback | () => void | Yes | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('inputStop', () => {
  console.info('inputMethodAbility delete inputStop notification.');
});

#### \[h2\]on('setCallingWindow')9+

on(type: 'setCallingWindow', callback: (wid: number) => void): void

Enables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setCallingWindow'**. |
| callback | (wid: number) => void | Yes | Callback used to return the window ID of the caller. |

**Example**

inputMethodEngine.getInputMethodAbility().on('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility setCallingWindow');
});

#### \[h2\]off('setCallingWindow')9+

off(type: 'setCallingWindow', callback: (wid:number) => void): void

Disables listening for the window invocation setting event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setCallingWindow'**. |
| callback | (wid:number) => void | Yes | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('setCallingWindow', (wid: number) => {
  console.info('inputMethodAbility delete setCallingWindow notification.');
});

#### \[h2\]on('keyboardShow'|'keyboardHide')9+

on(type: 'keyboardShow'|'keyboardHide', callback: () => void): void

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyboardShow'** indicates the keyboard display event.

\- The value **'keyboardHide'** indicates the keyboard hiding event.

 |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

inputMethodEngine.getInputMethodAbility().on('keyboardShow', () => {
  console.info('InputMethodAbility keyboardShow.');
});
inputMethodEngine.getInputMethodAbility().on('keyboardHide', () => {
  console.info('InputMethodAbility keyboardHide.');
});

#### \[h2\]off('keyboardShow'|'keyboardHide')9+

off(type: 'keyboardShow'|'keyboardHide', callback?: () => void): void

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyboardShow'** indicates the keyboard display event.

\- The value **'keyboardHide'** indicates the keyboard hiding event.

 |
| callback | () => void | No | Callback used to return the result. |

**Example**

inputMethodEngine.getInputMethodAbility().off('keyboardShow', () => {
  console.info('InputMethodAbility delete keyboardShow notification.');
});
inputMethodEngine.getInputMethodAbility().off('keyboardHide', () => {
  console.info('InputMethodAbility delete keyboardHide notification.');
});

#### \[h2\]on('setSubtype')9+

on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void

Enables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setSubtype'**. |
| callback | (inputMethodSubtype: [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md)) => void | Yes | Callback used to return the input method subtype. |

**Example**

import { InputMethodSubtype } from '@kit.IMEKit';

inputMethodEngine.getInputMethodAbility().on('setSubtype', (inputMethodSubtype: InputMethodSubtype) => {
  console.info('InputMethodAbility setSubtype.');
});

#### \[h2\]off('setSubtype')9+

off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void

Disables listening for the input method subtype setting event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'setSubtype'**. |
| callback | (inputMethodSubtype: [InputMethodSubtype](../ohos-inputmethodsubtype-input-method-subtype/document.md)) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('setSubtype', () => {
  console.info('InputMethodAbility delete setSubtype notification.');
});

#### \[h2\]on('securityModeChange')11+

on(type: 'securityModeChange', callback: Callback< SecurityMode>): void

Enables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'securityModeChange'**. |
| callback | Callback<[SecurityMode](#securitymode11)\> | Yes | Callback used to return the current security mode. |

**Example**

inputMethodEngine.getInputMethodAbility()
  .on('securityModeChange', (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(\`InputMethodAbility securityModeChange, security is ${securityMode}\`);
  });

#### \[h2\]off('securityModeChange')11+

off(type: 'securityModeChange', callback?: Callback< SecurityMode>): void

Disables listening for the security mode changes of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'securityModeChange'**. |
| callback | Callback<[SecurityMode](#securitymode11)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

let securityChangeCallback: (securityMode: inputMethodEngine.SecurityMode) => void =
  (securityMode: inputMethodEngine.SecurityMode) => {
    console.info(\`InputMethodAbility securityModeChange, security is ${securityMode}\`);
  };
let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
inputMethodAbility.on('securityModeChange', securityChangeCallback);
inputMethodAbility.off('securityModeChange', securityChangeCallback);

#### \[h2\]on('privateCommand')12+

on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;

Enables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'privateCommand'**. |
| callback | Callback<Record<string, [CommandDataType](#commanddatatype12)\>> | Yes | Callback used to return the private data sent to the input method application. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800010 | not the preconfigured default input method. |

**Example**

let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i :number = 0; i < record.length; i++) {
      console.info(\`private command key: ${i}, value: ${record\[i\]}\`);
    }
  }
inputMethodEngine.getInputMethodAbility().on('privateCommand', privateCommandCallback);

#### \[h2\]off('privateCommand')12+

off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void

Disables listening for the private data event of the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'privateCommand'**. |
| callback | Callback<Record<string, [CommandDataType](#commanddatatype12)\>> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800010 | not the preconfigured default input method. |

**Example**

let privateCommandCallback: (record: Record<string, inputMethodEngine.CommandDataType>) => void =
  (record: Record<string, inputMethodEngine.CommandDataType>) => {
    for (let i: number = 0; i < record.length; i++) {
      console.info(\`private command key: ${i}, value: ${record\[i\]}\`);
    }
  }

inputMethodEngine.getInputMethodAbility().off('privateCommand', privateCommandCallback);

#### \[h2\]on('callingDisplayDidChange')18+

on(type: 'callingDisplayDidChange', callback: Callback<number>): void

Enables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'callingDisplayDidChange'**. |
| callback | Callback<number> | Yes | Callback used to return the screen ID of the window corresponding to the edit box. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | capability not supported. |

**Example**

let callingDisplayDidChangeCallback: (num: number) => void = (num: number) => {
  console.info(\`display id: ${num}\`);
}
inputMethodEngine.getInputMethodAbility().on('callingDisplayDidChange', callingDisplayDidChangeCallback);

#### \[h2\]off('callingDisplayDidChange')18+

off(type: 'callingDisplayDidChange', callback?: Callback<number>): void

Disables listening for changes of the screen ID of the window associated with the edit box. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'callingDisplayDidChange'**. |
| callback | Callback<number> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('callingDisplayDidChange', (num: number) => {
  console.info('InputMethodAbility delete calling display  notification.');
});

#### \[h2\]on('discardTypingText')20+

on(type: 'discardTypingText', callback: Callback<void>): void

Subscribes to the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'discardTypingText'**.

\- **'discardTypingText'**: indicates subscribing to the event of discarding candidate words and sending the event to the input method.

 |
| callback | Callback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

inputMethodEngine.getInputMethodAbility().on('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});

#### \[h2\]off('discardTypingText')20+

off(type: 'discardTypingText', callback?: Callback<void>): void

Unsubscribes from the event of discarding candidate words and sends the event to the input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type, which is **'discardTypingText'**.

\- **'discardTypingText'**: indicates unsubscribing from the event of discarding candidate words and sending the event to the input method.

 |
| callback | Callback<void> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getInputMethodAbility().off('discardTypingText', () => {
  console.info('InputMethodAbility discard the typing text.');
});

#### \[h2\]getSecurityMode11+

getSecurityMode(): SecurityMode

Obtains the current security mode of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [SecurityMode](#securitymode11) | Security mode. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 12800004 | not an input method application. |

**Example**

let security: inputMethodEngine.SecurityMode = inputMethodEngine.getInputMethodAbility().getSecurityMode();
console.error(\`getSecurityMode, securityMode is : ${security}\`);

#### \[h2\]createPanel10+

createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void

Creates an input method panel. This API can be called only by the input method application in the [InputMethodExtensionAbility](../ohos-inputmethodextensionability-inputmethodextensionability/document.md#inputmethodextensionability) class. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Lvv_SlbvQVK2UIvHD3R09A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32418AF2C7B4A535D2B123D9C341BEBBF64D7926F56E511979799D1B069EE557)

Only one [SOFT\_KEYBOARD](#paneltype10) panel and one [STATUS\_BAR](#paneltype10) panel can be created for a single input method.

The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such as [window.createWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-fa#setting-the-child-window-of-an-application), [bindContextMenu](../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu8), and [CustomDialog](../../../arkui/arkts-components/dialog-boxes/custom-dialog-box-customdialog/document.md). You are advised to adopt alternative solutions to sub-windows, such as using a [dialog box](../../../arkui/arkts-components/dialog-boxes/dialog-box-dialog/document.md) or [bindMenu](../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindmenu), or set **showInSubwindow** to **false**.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current context of the input method. |
| info | [PanelInfo](#panelinfo10) | Yes | Information about the input method panel. |
| callback | AsyncCallback<[Panel](#panel10)\> | Yes | Callback used to return the result. If the operation is successful, the created input method panel is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT\_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG\_FIXED
}

if (!this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(\`Failed to createPanel. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      console.info('Succeed in creating panel.');
    })
}

#### \[h2\]createPanel10+

createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>

Creates an input method panel. This API can be called only by the input method application in the [InputMethodExtensionAbility](../ohos-inputmethodextensionability-inputmethodextensionability/document.md#inputmethodextensionability) class. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/VjYWBtc3QmC4hhkuPOvPWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=399C9796425138F1A2673B5BFECF9AEB325D9F025E314555BD138F4123244A60)

Only one [SOFT\_KEYBOARD](#paneltype10) panel and one [STATUS\_BAR](#paneltype10) panel can be created for a single input method.

The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such as [window.createWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-window-fa#setting-the-child-window-of-an-application), [bindContextMenu](../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindcontextmenu8), and [CustomDialog](../../../arkui/arkts-components/dialog-boxes/custom-dialog-box-customdialog/document.md). You are advised to adopt alternative solutions to sub-windows, such as using a [dialog box](../../../arkui/arkts-components/dialog-boxes/dialog-box-dialog/document.md) or [bindMenu](../../../arkui/arkts-components/universal-attributes/dialog-box-control/menu-control/document.md#bindmenu), or set **showInSubwindow** to **false**.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ctx | [BaseContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md) | Yes | Current context of the input method. |
| info | [PanelInfo](#panelinfo10) | Yes | Information about the input method panel. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Panel](#panel10)\> | Promise used to return the result. If the operation is successful, the created input method panel is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 12800004 | not an input method application. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT\_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG\_FIXED
}

if (this.context) {
  inputMethodEngine.getInputMethodAbility().createPanel(this.context, panelInfo)
    .then((panel: inputMethodEngine.Panel) => {
      console.info('Succeed in creating panel.');
    }).catch((err: BusinessError) => {
    console.error(\`Failed to create panel. Code is ${err.code}, message is ${err.message}\`);
  })
}

#### \[h2\]destroyPanel10+

destroyPanel(panel: Panel, callback: AsyncCallback<void>): void

Destroys the specified input method panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| panel | [Panel](#panel10) | Yes | Input method panel to destroy. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT\_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG\_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(\`Failed to create panel. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel, (err: BusinessError) => {
    if (err !== undefined) {
      console.error(\`Failed to destroy panel. Code is ${err.code}, message is ${err.message}\`);
      return;
    }
    console.info('Succeed in destroying panel.');
  })
}

#### \[h2\]destroyPanel10+

destroyPanel(panel: Panel): Promise<void>

Destroys the specified input method panel. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| panel | [Panel](#panel10) | Yes | Input method panel to destroy. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let panelInfo: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT\_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG\_FIXED
}

let inputPanel: inputMethodEngine.Panel | undefined = undefined;
if (this.context) {
  inputMethodEngine.getInputMethodAbility()
    .createPanel(this.context, panelInfo, (err: BusinessError, panel: inputMethodEngine.Panel) => {
      if (err) {
        console.error(\`Failed to create panel. Code is ${err.code}, message is ${err.message}\`);
        return;
      }
      inputPanel = panel;
      console.info('Succeed in creating panel.');
    })
}

if (inputPanel) {
  inputMethodEngine.getInputMethodAbility().destroyPanel(inputPanel).then(() => {
    console.info('Succeed in destroying panel.');
  }).catch((err: BusinessError) => {
    console.error(\`Failed to destroy panel. Code is ${err.code}, message is ${err.message}\`);
  });
}

#### KeyboardDelegate

In the following API examples, you must first use [getKeyboardDelegate](#inputmethodenginegetkeyboarddelegate9) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance.

#### \[h2\]on('keyDown'|'keyUp')

on(type: 'keyDown'|'keyUp', callback: (event: KeyEvent) => boolean): void

Enables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyDown'** indicates the keydown event.

\- The value **'keyUp'** indicates the keyup event.

 |
| callback | (event: [KeyEvent](#keyevent)) => boolean | Yes | Callback used to return the key information. If the event is consumed by the event subscriber, **true** is returned. Otherwise, **false** is returned. |

**Example**

inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(\`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}\`);
  console.info(\`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}\`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(\`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}\`);
  console.info(\`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}\`);
  return true;
});

#### \[h2\]off('keyDown'|'keyUp')

off(type: 'keyDown'|'keyUp', callback?: (event: KeyEvent) => boolean): void

Disables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type.

\- The value **'keyDown'** indicates the keydown event.

\- The value **'keyUp'** indicates the keyup event.

 |
| callback | (event: [KeyEvent](#keyevent)) => boolean | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyUp notification.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyDown notification.');
  return true;
});

#### \[h2\]on('keyEvent')10+

on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void

Enables listening for a keyboard event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'keyEvent'**. |
| callback | (event: [InputKeyEvent](../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md#keyevent)) => boolean | Yes | 
Callback used to return the result. The input parameter is the key event information and the return value is of the Boolean type.

\- Input parameter: [InputKeyEvent](../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md#keyevent).

\- If the event is consumed by the event subscriber, **true** is returned. Otherwise, **false** is returned.

 |

**Example**

import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().on('keyEvent', (keyEvent: KeyEvent) => {
  console.info(\`inputMethodEngine keyEvent.action:${ keyEvent.action}\`);
  console.info(\`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}\`);
  console.info(\`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}\`);
  console.info(\`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}\`);
  return true;
});

#### \[h2\]off('keyEvent')10+

off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void

Disables listening for a keyboard event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'keyEvent'**. |
| callback | (event: [InputKeyEvent](../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keyevent-key-event/document.md#keyevent)) => boolean | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');

#### \[h2\]on('cursorContextChange')

on(type: 'cursorContextChange', callback: (x: number, y:number, height:number) => void): void

Enables listening for the cursor change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'cursorContextChange'**. |
| callback | (x: number, y: number, height: number) => void | Yes | 
Callback used to return the cursor information.

\- **x**: x coordinate of the top of the cursor.

\- **y**: y coordinate of the bottom of the cursor.

\- **height**: height of the cursor.

 |

**Example**

inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});

#### \[h2\]off('cursorContextChange')

off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void

Disables listening for cursor context changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'cursorContextChange'**. |
| callback | (x: number, y:number, height:number) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('delete cursorContextChange notification.');
});

#### \[h2\]on('selectionChange')

on(type: 'selectionChange', callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

Enables listening for the text selection change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'selectionChange'**. |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | Yes | 
Callback used to return the text selection information.

\- **oldBegin**: start of the selected text before the change.

\- **oldEnd**: end of the selected text before the change.

\- **newBegin**: start of the selected text after the change.

\- **newEnd**: end of the selected text after the change.

 |

**Example**

inputMethodEngine.getKeyboardDelegate()
  .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('selectionChange oldBegin:' + oldBegin);
    console.info('selectionChange oldEnd:' + oldEnd);
    console.info('selectionChange newBegin:' + newBegin);
    console.info('selectionChange newEnd:' + newEnd);
  });

#### \[h2\]off('selectionChange')

off(type: 'selectionChange', callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void

Disables listening for the text selection change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'selectionChange'**. |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getKeyboardDelegate()
  .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('delete selectionChange notification.');
  });

#### \[h2\]on('textChange')

on(type: 'textChange', callback: (text: string) => void): void

Enables listening for the text change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'textChange'**. |
| callback | (text: string) => void | Yes | Callback used to return the text content. |

**Example**

inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});

#### \[h2\]off('textChange')

off(type: 'textChange', callback?: (text: string) => void): void

Disables listening for the text change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'textChange'**. |
| callback | (text: string) => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});

#### \[h2\]on('editorAttributeChanged')10+

on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void

Enables listening for the edit box attribute change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'editorAttributeChanged'**. |
| callback | (attr: [EditorAttribute](#editorattribute)) => void | Yes | Callback used to return the changed edit box attribute. |

**Example**

inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
    console.info(\`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}\`);
  });

#### \[h2\]off('editorAttributeChanged')10+

off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void

Disables listening for the edit box attribute change event. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'editorAttributeChanged'**. |
| callback | (attr: [EditorAttribute](#editorattribute)) => void | No | Callback used for unsubscription. If this parameter is not specified, this API unregisters all callbacks for the specified type by default. |

**Example**

inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');

#### Panel10+

In the following API examples, you must first use [createPanel](#createpanel10) to obtain a **Panel** instance, and then call the APIs using the obtained instance.

#### \[h2\]setUiContent10+

setUiContent(path: string, callback: AsyncCallback<void>): void

Loads content from a page to this input method panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page from which the content will be loaded. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2', (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to setUiContent. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the content.');
});

#### \[h2\]setUiContent10+

setUiContent(path: string): Promise<void>

Loads content from a page to this input method panel. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page from which the content will be loaded. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.setUiContent('pages/page2/page2').then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to setUiContent. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setUiContent10+

setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void

Loads content from a page linked to LocalStorage to this input method panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page linked to LocalStorage. |
| storage | [LocalStorage](../../../arkui/arkts-components/state-management-and-rendering-control/state-management-with-application-level-variables/document.md#localstorage9) | Yes | Storage unit that provides storage for mutable and immutable state variables in the application. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to setUiContent. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in setting the content.');
});

#### \[h2\]setUiContent10+

setUiContent(path: string, storage: LocalStorage): Promise<void>

Loads content from a page linked to LocalStorage to this panel. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the page from which the content will be loaded. |
| storage | [LocalStorage](../../../arkui/arkts-components/state-management-and-rendering-control/state-management-with-application-level-variables/document.md#localstorage9) | Yes | Storage unit that provides storage for mutable and immutable state variables in the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let storage: LocalStorage = new LocalStorage();
storage.setOrCreate('storageSimpleProp', 121);
panel.setUiContent('pages/page2/page2', storage).then(() => {
  console.info('Succeeded in setting the content.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to setUiContent. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]resize10+

resize(width: number, height: number, callback: AsyncCallback<void>): void

Resizes this input method panel. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ES6gG2TVTYGqp-YdhCpbgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50BDCFA271BCC0EAAA2D76C31D5263DD65ECB3EAD338FEC8237B0A82C6C9DE11)

The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen height.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Target width of the panel, in px. The value is an integer greater than or equal to 0, and cannot be greater than the screen width. |
| height | number | Yes | Target height of the panel, in px. The value is an integer greater than or equal to 0, and cannot be greater than 0.7 times the screen height. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to resize panel. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in changing the panel size.');
});

#### \[h2\]resize10+

resize(width: number, height: number): Promise<void>

Resizes this input method panel. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/s69rCC94RI6ikh2Ia4dYwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56FAC2CE917F2A8D75DF82AA14B865CF416C096F376DF2B77C1ABAF21555CEAE)

The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen height.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Target width of the panel, in px. The value is an integer greater than or equal to 0, and cannot be greater than the screen width. |
| height | number | Yes | Target height of the panel, in px. The value is an integer greater than or equal to 0, and cannot be greater than 0.7 times the screen height. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.resize(500, 1000).then(() => {
  console.info('Succeeded in changing the panel size.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to resize panel. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]moveTo10+

moveTo(x: number, y: number, callback: AsyncCallback<void>): void

Moves this input method panel to the specified position. This API uses an asynchronous callback to return the result. This API does not work on panels in the [FLG\_FIXED](#panelflag10) state.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance to move along the horizontal axis, in px. A positive value indicates moving rightwards. The value must be an integer. |
| y | number | Yes | Distance to move along the vertical axis, in px. A positive value indicates moving downwards. The value must be an integer. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to move panel. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in moving the panel.');
});

#### \[h2\]moveTo10+

moveTo(x: number, y: number): Promise<void>

Moves this input method panel to the specified position. This API uses a promise to return the result. This API does not work on panels in the [FLG\_FIXED](#panelflag10) state.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Distance to move along the horizontal axis, in px. A positive value indicates moving rightwards. The value must be an integer. |
| y | number | Yes | Distance to move along the vertical axis, in px. A positive value indicates moving downwards. The value must be an integer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.moveTo(300, 300).then(() => {
  console.info('Succeeded in moving the panel.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to move panel. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]startMoving15+

startMoving(): void

Sends a command to start moving the window. The window can be moved only when the mouse is clicked.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**Example**

panel.startMoving();

#### \[h2\]getDisplayId15+

getDisplayId(): Promise<number>

Obtains the window ID. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. It returns **displayId** of the window. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.getDisplayId().then((result: number) => {
  console.info('get displayId:' + result);
}).catch((err: BusinessError) => {
  console.error(\`Failed to get displayId. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]show10+

show(callback: AsyncCallback<void>): void

Shows this input method panel. This API uses an asynchronous callback to return the result. It can be called when the input method is bound to the edit box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.show((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to show panel. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in showing the panel.');
});

#### \[h2\]show10+

show(): Promise<void>

Shows this input method panel. This API uses a promise to return the result. It can be called when the input method is bound to the edit box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.show().then(() => {
  console.info('Succeeded in showing the panel.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to show panel. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]hide10+

hide(callback: AsyncCallback<void>): void

Hides this panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.hide((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to hide panel. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in hiding the panel.');
});

#### \[h2\]hide10+

hide(): Promise<void>

Hides this panel. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.hide().then(() => {
  console.info('Succeeded in hiding the panel.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to hide panel. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]adjustPanelRect12+

adjustPanelRect(flag: PanelFlag, rect: PanelRect): void

Adjusts the panel rectangle. After the API is called, the adjust request is submitted to the input method framework, but the execution is not complete.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | Yes | Type of the state of the target panel. It can be **FLG\_FIXED** or **FLG\_FLOATING**. |
| rect | [PanelRect](#panelrect12) | Yes | Landscape rectangle and portrait rectangle of the target panel. For the panel of the fixed state, the height cannot exceed 70% of the screen height, and the width cannot exceed the screen width. For the panel of the floating state, the height cannot exceed the screen height, and the width cannot exceed the screen width. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |

**Example**

import { window } from '@kit.ArkUI';

let landscapeRect: window.Rect = {
  left: 100,
  top: 100,
  width: 400,
  height: 400
};

let portraitRect: window.Rect = {
  left: 200,
  top: 200,
  width: 300,
  height: 300
};

let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG\_FIXED;
let panelRect: inputMethodEngine.PanelRect = {
  landscapeRect: landscapeRect,
  portraitRect: portraitRect
};
panel.adjustPanelRect(panelFlag, panelRect);

#### \[h2\]adjustPanelRect15+

adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void

Adjusts the panel rectangle, and customizes the avoid area and touch area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/hMBGLrYgRTOLuOghb4lOcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ACFBFB328BE4F8D07058C578A438F0F53E5C4E54F997F747E64E7CF8F9B156E)

This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** state. This API is compatible with [adjustPanelRect](#adjustpanelrect12). If the input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes, [adjustPanelRect](#adjustpanelrect12) is called by default.

This API returns the result synchronously. The return only indicates that the system receives the setting request, not that the setting is complete.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | Yes | Type of the state of the target panel. It can be **FLG\_FIXED** or **FLG\_FLOATING**. |
| rect | [EnhancedPanelRect](#enhancedpanelrect15) | Yes | The target panel rectangle, avoid area, and touch area. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**Example**

import { window } from '@kit.ArkUI';

let landscapeRect1: window.Rect = {
  left: 300,
  top: 650,
  width: 2000,
  height: 500
};
let landscapeInputRegion: Array<window.Rect> = \[landscapeRect1\];

let portraitRect1: window.Rect = {
  left: 0,
  top: 1800,
  width: 1200,
  height: 800
}
let portraitInputRegion: Array<window.Rect> = \[portraitRect1\];

let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG\_FIXED;
let panelRect: inputMethodEngine.EnhancedPanelRect = {
  landscapeAvoidY: 650,
  landscapeInputRegion: landscapeInputRegion,
  portraitAvoidY: 1800,
  portraitInputRegion: portraitInputRegion,
  fullScreenMode: true
};
panel.adjustPanelRect(panelFlag, panelRect);

#### \[h2\]updateRegion15+

updateRegion(inputRegion: Array<window.Rect>): void

Updates the hot zone on the input method panel in the current state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/0mmQQM38Qnai3dQ0VsRbKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74B3C0F2AADE2D27F1B212179EE8FDFBE3E84F28A19B74C714E1296CFF6324C5)

This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** state.

This API returns the result synchronously. The return only indicates that the system has received the request for updating the hot zone, not that the hot zone has been updated.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputRegion | Array<[window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7)\> | Yes | 
Region for receiving input events.

\- The array size is limited to \[1, 4\].

\- The input hot zone is relative to the left vertex of the input method panel window.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let inputRegion: Array<window.Rect> = \[{
  left: 300,
  top: 650,
  width: 2000,
  height: 500
}\];
panel.updateRegion(inputRegion);

#### \[h2\]on('show')10+

on(type: 'show', callback: () => void): void

Enables listening for the show event of this panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'show'**. |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

panel.on('show', () => {
  console.info('Panel is showing.');
});

#### \[h2\]on('hide')10+

on(type: 'hide', callback: () => void): void

Enables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'hide'**. |
| callback | () => void | Yes | Callback used to return the result. |

**Example**

panel.on('hide', () => {
  console.info('Panel is hiding.');
});

#### \[h2\]on('sizeChange')12+

on(type: 'sizeChange', callback: SizeChangeCallback): void

Enables listening for the panel size change. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/7EnIOQr9Q92_W9MRHnorUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC80D2B5F3AB38412374FEA77FA232F5877524A703648032CF9E46E91F3F63E)

This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the panel layout.

-   This API is supported from API version 12 to 14. The callback function of this API contains only mandatory parameters of the [window.Size](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#size7) type.
-   Since API version 15, after the [adjustPanelRect](#adjustpanelrect15) API is called, an optional parameter of the [KeyboardArea](#keyboardarea15) type is added to the callback function of this API.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'sizeChange'**. |
| callback | [SizeChangeCallback](#sizechangecallback15) | Yes | Callback used to return the size of the soft keyboard panel, including the width and height. |

**Example**

import { window } from '@kit.ArkUI';

panel.on('sizeChange', (windowSize: window.Size) => {
  console.info(\`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}\`);
});

panel.on('sizeChange', (windowSize: window.Size, keyboardArea: inputMethodEngine.KeyboardArea) => {
  console.info(\`panel size changed, windowSize: ${windowSize.width}, ${windowSize.height}, \` +
    \`keyboardArea: ${keyboardArea.top}, ${keyboardArea.bottom}, ${keyboardArea.left}, ${keyboardArea.right}\`);
});

#### \[h2\]off('show')10+

off(type: 'show', callback?: () => void): void

Disables listening for the show event of this panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'show'**. |
| callback | () => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

panel.off('show');

#### \[h2\]off('hide')10+

off(type: 'hide', callback?: () => void): void

Disables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'hide'**. |
| callback | () => void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

panel.off('hide');

#### \[h2\]off('sizeChange')12+

off(type: 'sizeChange', callback?: SizeChangeCallback): void

Disables listening for the panel size change. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/f-PUhjuzTp2hVNYnBqQaug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEF309C1122B7F80EE3988EB761B1E8A6C68C35350620D4A7006FCD2D5CBD886)

This API applies only to the panels of the **SOFT\_KEYBOARD** type in the **FLG\_FIXED** or **FLG\_FLOATING** state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain the actual panel size to refresh the panel layout.

-   This API is supported from API version 12 to 14. The callback function of this API contains only mandatory parameters of the [window.Size](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#size7) type.
-   Since API version 15, after the [adjustPanelRect](#adjustpanelrect15) API is called, an optional parameter of the [KeyboardArea](#keyboardarea15) type is added to the callback function of this API.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type, which is **'sizeChange'**. |
| callback | [SizeChangeCallback](#sizechangecallback15) | No | Callback used to return the size of the soft keyboard panel, including the width and height. |

**Example**

import { window } from '@kit.ArkUI';

panel.off('sizeChange', (windowSize: window.Size) => {
  console.info(\`panel size changed, width: ${windowSize.width}, height: ${windowSize.height}\`);
});

#### \[h2\]changeFlag10+

changeFlag(flag: PanelFlag): void

Changes the state type ([PanelFlag](#panelflag10)) of this input method panel. This API only works for [SOFT\_KEYBOARD](#paneltype10) panels.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flag | [PanelFlag](#panelflag10) | Yes | Type of the state of the target panel. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

let panelFlag: inputMethodEngine.PanelFlag = inputMethodEngine.PanelFlag.FLG\_FIXED;
panel.changeFlag(panelFlag);

#### \[h2\]setPrivacyMode11+

setPrivacyMode(isPrivacyMode: boolean): void

Sets the input method panel to privacy mode. In privacy mode, screenshot and screen recording are blocked.

**Required permissions**: ohos.permission.PRIVACY\_WINDOW

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isPrivacyMode | boolean | Yes | 
Whether to set the input method panel to privacy mode.

\- **true**: privacy mode.

\- **false**: non-privacy mode.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permissions check fails. |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

let isPrivacyMode: boolean = true;
panel.setPrivacyMode(isPrivacyMode);

#### \[h2\]setImmersiveMode15+

setImmersiveMode(mode: ImmersiveMode): void

Sets the immersive mode of the input method application. You can only set the immersion mode to **NONE\_IMMERSIVE**, **LIGHT\_IMMERSIVE**, or **DARK\_IMMERSIVE**. **IMMERSIVE** cannot be set.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [ImmersiveMode](#immersivemode15) | Yes | Immersive mode. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |

**Example**

panel.setImmersiveMode(inputMethodEngine.ImmersiveMode.LIGHT\_IMMERSIVE);

#### \[h2\]getImmersiveMode15+

getImmersiveMode(): ImmersiveMode

Obtains the immersive mode of the input method application.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [ImmersiveMode](#immersivemode15) | Immersive mode. |

**Example**

let mode: inputMethodEngine.ImmersiveMode = panel.getImmersiveMode();

#### \[h2\]setImmersiveEffect20+

setImmersiveEffect(effect: ImmersiveEffect): void

Sets the immersive effect of the input method application.

-   Gradient mode and fluid light mode can be used only when the [immersive mode](#setimmersivemode15) is enabled.
-   The fluid light mode can be used only when the gradient mode is enabled.
-   If the gradient mode is disabled, the gradient height must be 0 px.
-   Only system applications can set the fluid light mode.
-   The current API can be called only after any of the following APIs is called:
    -   [adjustPanelRect](#adjustpanelrect12) (available since API version 12)
    -   [adjustPanelRect](#adjustpanelrect15) (available since API version 15)
    -   [resize](#resize10) (available since API version 10)

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [ImmersiveEffect](#immersiveeffect20) | Yes | Immersive effect. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | capability not supported. |
| 12800002 | input method engine error. Possible causes:1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800013 | window manager service error. |
| 12800020 | invalid immersive effect. 1.The gradient mode and the fluid light mode can only be used when the immersive mode is enabled. 2.The fluid light mode can only be used when the gradient mode is enabled. 3.When the gradient mode is not enabled, the gradient height can only be 0. |
| 12800021 | this operation is allowed only after adjustPanelRect or resize is called. |

**Example**

let effect: inputMethodEngine.ImmersiveEffect = {
  gradientHeight: 100,
  gradientMode: inputMethodEngine.GradientMode.LINEAR\_GRADIENT
}
panel.setImmersiveEffect(effect);

#### \[h2\]setKeepScreenOn20+

setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>

Sets to keep the screen always on. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/biTWYUk_QXqNgk4WX3Mu-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2520881411BDEF776E121E7E3877BFFE24B3D52C25F7FF9A6B0F0AFA58D6DC8C)

-   When the keyboard is displayed, the screen stays on. When the keyboard is hidden, the screen turns off.
-   You need to use this API properly. Set the attribute to **true** in necessary scenarios (for example, voice input) and reset this attribute to **false** after exiting necessary scenarios. In other scenarios, do not use this API.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isKeepScreenOn | boolean | Yes | Whether to keep the screen always on. The value **true** means that the screen is always on; the value **false** means the opposite. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800013 | window manager service error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

panel.setKeepScreenOn(true).then(() => {
  console.info(\`setKeepScreenOn success.\`);
}).catch((error: BusinessError) => {
  console.error(\`setKeepScreenOn failed, code: ${error.code}, message: ${error.message}\`);
})

#### \[h2\]getSystemPanelCurrentInsets21+

getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>

Obtains the offset area of the soft keyboard relative to the system panel under the current state of the specified screen (for example, folded or unfolded) and the current state of the input method keyboard (for example, floating or fixed). This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| displayId | number | Yes | Display ID of the screen where the input method keyboard is located. It can be obtained by calling [getDisplayId](#getdisplayid15). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SystemPanelInsets](#systempanelinsets21)\> | Promise used to return the offset area between the input method keyboard and the system panel. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800013 | window manager service error. |
| 12800017 | invalid panel type or panel flag. Possible causes: 1. Current panel's type is not SOFT\_KEYBOARD. 2. Panel's flag is not FLG\_FIXED or FLG\_FLOATING. |
| 12800022 | invalid displayId. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { inputMethodEngine } from '@kit.IMEKit';

let inputMethodAbility: inputMethodEngine.InputMethodAbility = inputMethodEngine.getInputMethodAbility();
let panelConfig: inputMethodEngine.PanelInfo = {
  type: inputMethodEngine.PanelType.SOFT\_KEYBOARD,
  flag: inputMethodEngine.PanelFlag.FLG\_FIXED
}
// The following logic needs to be executed in InputMethodExtensionAbility. this.context is the context of InputMethodExtensionAbility.
inputMethodAbility.createPanel(this.context, panelConfig).then( (panel: inputMethodEngine.Panel) =>{
  panel.getDisplayId().then((displayId: number) => {
    panel.getSystemPanelCurrentInsets(displayId).then((insets: inputMethodEngine.SystemPanelInsets) => {
      console.info(\`getSystemPanelCurrentInsets success, insets is { left: ${insets.left}, right: ${insets.right}, bottom: ${insets.bottom} }\`);
    }).catch((error: BusinessError) => {
      console.error(\`getSystemPanelCurrentInsets failed, code: ${error.code}, message: ${error.message}\`);
    })
  });
})

#### \[h2\]setSystemPanelButtonColor22+

setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>

Sets the color of the function buttons and their background color on the current panel. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fillColor | string|undefined | Yes | Color of the function buttons. The value can be \[#01000000, #FFFFFFFF\] or \[#000000, #FFFFFF\]. The value of the fully transparent alpha channel (**#00xxxxxx**) is not supported. |
| backgroundColor | string|undefined | Yes | Background color of the function buttons. The value can be \[#01000000, #FFFFFFFF\] or \[#000000, #FFFFFF\]. The value of the fully transparent alpha channel (#00xxxxxx) is not supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fillColor = "#FFFF00";
  let backgroundColor = "#0000FF";
  this.panel.setSystemPanelButtonColor(fillColor, backgroundColor).then(() => {
    console.info(\`setSystemPanelButtonColor success.\`);
  }).catch((error: BusinessError) => {
    console.error(\`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}\`);
  })
} catch (err) {
  let error = err as BusinessError;
  console.error(\`setSystemPanelButtonColor failed, code: ${error.code}, message: ${error.message}\`);
}

#### KeyboardController

You must first use [on('inputStart')](#oninputstart9) to obtain a **KeyboardController** instance, and then use this instance to call the following APIs.

#### \[h2\]hide9+

hide(callback: AsyncCallback<void>): void

Hides the keyboard. This API uses an asynchronous callback to return the result.

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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to hide. Code:${err.code}, message:${err.message}\`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});

#### \[h2\]hide9+

hide(): Promise<void>

Hides the keyboard. This API uses a promise to return the result.

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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hide().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to hide. Code:${err.code}, message:${err.message}\`);
});

#### \[h2\]hideKeyboard(deprecated)

hideKeyboard(callback: AsyncCallback<void>): void

Hides the keyboard. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/C9-jFu6TR3C_QioPDE0cQQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCA96D5D9B6453368AD8DECD7C4DCC807DB30681256374C52740FB43F9214C9E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hide](#hide9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in hiding keyboard.');
});

#### \[h2\]hideKeyboard(deprecated)

hideKeyboard(): Promise<void>

Hides the keyboard. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/sSn2kpEkS5WMlA94bgmy9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ACED42C059C82A5BD3603FE76C5B40D1FF7150545697DAA17171BDF58D96744)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hide](#hide9-1) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.hideKeyboard().then(() => {
  console.info('Succeeded in hiding keyboard.');
}).catch((err: BusinessError) => {
  console.info(\`Failed to hideKeyboard. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]exitCurrentInputType11+

exitCurrentInputType(callback: AsyncCallback<void>): void

Exits this input type. This API can be called only by the preconfigured default input method. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType((err: BusinessError) => {
  if (err) {
    console.error(\`Failed to exit current input type. Code:${err.code}, message:${err.message}\`);
    return;
  }
  console.info('Succeeded in exiting current input type.');
});

#### \[h2\]exitCurrentInputType11+

exitCurrentInputType(): Promise<void>

Exits this input type. This API can be called only by the preconfigured default input method. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800010 | not the preconfigured default input method. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

keyboardController.exitCurrentInputType().then(() => {
  console.info('Succeeded in exiting current input type.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to exit current input type. Code:${err.code}, message:${err.message}\`);
});

#### SecurityMode11+

Describes the security mode.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| BASIC | 0 | Basic access mode, where network access is restricted. |
| FULL | 1 | Full access mode, where network access is not restricted. |

#### ExtendAction10+

Describes the type of the extended edit action on the text box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SELECT\_ALL | 0 | Select all. |
| CUT | 3 | Cut. |
| COPY | 4 | Copy. |
| PASTE | 5 | Paste. |

#### Direction10+

Enumerates the directions of cursor movement of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| CURSOR\_UP | 1 | Upward. |
| CURSOR\_DOWN | 2 | Downward. |
| CURSOR\_LEFT | 3 | Leftward. |
| CURSOR\_RIGHT | 4 | Rightward. |

#### Range10+

Describes the range of the selected text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | No | Index of the first selected character in the text box. |
| end | number | No | No | Index of the last selected character in the text box. |

#### Movement10+

Describes the direction in which the cursor moves when the text is selected.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| direction | [Direction](#direction10) | No | No | Direction in which the cursor moves when the text is selected. |

#### MessageHandler15+

Represents a custom communication object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/V3QlMAfeSmeXYflF2YeV9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D726531394B4A67EFA0013C8E38A62C7BB1310C70E1269634965093AF388E827)

You can register this object to receive custom communication data sent by the edit box application attached to the input method application. When the custom communication data is received, the [onMessage](#onmessage15) callback in this object is triggered.

This object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated15) callback of the penultimate registered object is triggered.

If this object is unregistered, its [onTerminated](#onterminated15) callback will be triggered.

#### \[h2\]onMessage15+

onMessage(msgId: string, msgParam?: ArrayBuffer): void

Receives the custom data callback sent by the edit box application attached to the input method application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/9iag_m0ST_OQv4eVxstFtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F76243AF8E0624D08A77206D868514E0F19FFB40D9789D20EB241D1277C0B9A2)

This callback is triggered when the registered [MessageHandler](#messagehandler15) receives custom communication data sent by the edit box application attached to the input method application.

The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId** data is received, confirm it with the data sender.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgId | string | Yes | Identifier of the received custom communication data. |
| msgParam | ArrayBuffer | No | Message body of the received custom communication data. |

**Example**

inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });

#### \[h2\]onTerminated15+

onTerminated(): void

Listens for MessageHandler termination.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bobk26zqRPOEUclYsvLLYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12F6025169CC511FDFF31FF9F498917C9FD3B24D19FC411A7816B722F375D21A)

When an application registers a new [MessageHandler](#messagehandler15) object, the [onTerminated](#onterminated15) callback of the penultimate registered [MessageHandler](#messagehandler15) object is triggered.

When an application unregisters a new [MessageHandler](#messagehandler15) object, the [onTerminated](#onterminated15) callback of the registered [MessageHandler](#messagehandler15) object is triggered.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Example**

inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });

#### InputClient9+

You must first use [on('inputStart')](#oninputstart9) to obtain a **InputClient** instance, and then use this instance to call the following APIs.

#### \[h2\]sendKeyFunction9+

sendKeyFunction(action:number, callback: AsyncCallback<boolean>): void

Sends the function key. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | number | Yes | 
Action of the function key.

\- **0**: invalid key.

\- **1**: confirm key (Enter key).

 |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});

#### \[h2\]sendKeyFunction9+

sendKeyFunction(action: number): Promise<boolean>

Sends the function key. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | number | Yes | 
Action of the function key.

**0**: invalid key.

**1**: confirm key (Enter key).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the operation is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getForward9+

getForward(length:number, callback: AsyncCallback<string>): void

Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(\`Failed to getForward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});

#### \[h2\]getForward9+

getForward(length:number): Promise<string>

Obtains the specific-length text before the cursor. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the specific-length text before the cursor. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getForward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getForwardSync10+

getForwardSync(length:number): string

Obtains the specific-length text before the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Specific-length text before the cursor. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

let length: number = 1;
let text: string = inputClient.getForwardSync(length);
console.info(\`Succeeded in getting forward, text: ${text}\`);

#### \[h2\]getBackward9+

getBackward(length:number, callback: AsyncCallback<string>): void

Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(\`Failed to getBackward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});

#### \[h2\]getBackward9+

getBackward(length:number): Promise<string>

Obtains the specific-length text after the cursor. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the specific-length text after the cursor. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getBackward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getBackwardSync10+

getBackwardSync(length:number): string

Obtains the specific-length text after the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Specific-length text after the cursor. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(\`Succeeded in getting backward, text: ${text}\`);

#### \[h2\]deleteForward9+

deleteForward(length:number, callback: AsyncCallback<boolean>): void

Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to deleteForward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(\`Failed to deleteForward.\`);
  }
});

#### \[h2\]deleteForward9+

deleteForward(length:number): Promise<boolean>

Deletes the fixed-length text before the cursor. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the deletion is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to deleteForward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]deleteForwardSync10+

deleteForwardSync(length:number): void

Deletes the fixed-length text before the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

let length: number = 1;
inputClient.deleteForwardSync(length);

#### \[h2\]deleteBackward9+

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

Deletes the fixed-length text after the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(\`Failed to deleteBackward.\`);
  }
});

#### \[h2\]deleteBackward9+

deleteBackward(length:number): Promise<boolean>

Deletes the fixed-length text after the cursor. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the deletion is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]deleteBackwardSync10+

deleteBackwardSync(length:number): void

Deletes the fixed-length text after the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

let length: number = 1;
inputClient.deleteBackwardSync(length);

#### \[h2\]insertText9+

insertText(text:string, callback: AsyncCallback<boolean>): void

Inserts text. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to insert. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to insertText. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});

#### \[h2\]insertText9+

insertText(text:string): Promise<boolean>

Inserts text. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the insertion is successful, and **false** means the opposite. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to insertText. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]insertTextSync10+

insertTextSync(text: string): void

Inserts text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to insert. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800002 | input method engine error. Possible causes: 1.input method panel not created. 2.the input method application does not subscribe to related events. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

inputClient.insertTextSync('test');

#### \[h2\]getEditorAttribute9+

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[EditorAttribute](#editorattribute)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the attribute of the edit box. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(\`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}\`);
  console.info(\`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}\`);
});

#### \[h2\]getEditorAttribute9+

getEditorAttribute(): Promise<EditorAttribute>

Obtains the attribute of the edit box. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[EditorAttribute](#editorattribute)\> | Promise used to return the attribute of the edit box. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(\`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}\`);
  console.info(\`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getEditorAttributeSync10+

getEditorAttributeSync(): EditorAttribute

Obtains the attribute of the edit box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [EditorAttribute](#editorattribute) | Attribute information. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(\`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}\`);
console.info(\`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}\`);

#### \[h2\]moveCursor9+

moveCursor(direction: number, callback: AsyncCallback<void>): void

Moves the cursor. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | number | Yes | 
Direction in which the cursor moves.

\- **1**: upward.

\- **2**: downward.

\- **3**: leftward.

\- **4**: rightward. which cannot be less than 0.

 |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR\_UP, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to moveCursor. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in moving cursor.');
});

#### \[h2\]moveCursor9+

moveCursor(direction: number): Promise<void>

Moves the cursor. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | number | Yes | 
Direction in which the cursor moves.

\- **1**: upward.

\- **2**: downward.

\- **3**: leftward.

\- **4**: rightward. which cannot be less than 0.

 |

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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR\_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to moveCursor. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]moveCursorSync10+

moveCursorSync(direction: number): void

Moves the cursor.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | number | Yes | 
Direction in which the cursor moves.

\- **1**: upward.

\- **2**: downward.

\- **3**: leftward.

\- **4**: rightward. which cannot be less than 0.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR\_UP);

#### \[h2\]selectByRange10+

selectByRange(range: Range, callback: AsyncCallback<void>): void

Selects text based on the specified range. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | Yes | Range of the selected text. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the selection event is sent, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to selectByRange. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});

#### \[h2\]selectByRange10+

selectByRange(range: Range): Promise<void>

Selects text based on the specified range. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | Yes | Range of the selected text. |

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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to selectByRange. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]selectByRangeSync10+

selectByRangeSync(range: Range): void

Selects text based on the specified range.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| range | [Range](#range10) | Yes | Range of the selected text. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);

#### \[h2\]selectByMovement10+

selectByMovement(movement: Movement, callback: AsyncCallback<void>): void

Selects text based on the cursor movement direction. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | Yes | Direction in which the cursor moves when the text is selected. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the selection event is sent, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});

#### \[h2\]selectByMovement10+

selectByMovement(movement: Movement): Promise<void>

Selects text based on the cursor movement direction. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | Yes | Direction in which the cursor moves when the text is selected. |

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

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]selectByMovementSync10+

selectByMovementSync(movement: Movement): void

Selects text based on the cursor movement direction.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| movement | [Movement](#movement10) | Yes | Direction in which the cursor moves when the text is selected. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |

**Example**

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);

#### \[h2\]getTextIndexAtCursor10+

getTextIndexAtCursor(callback: AsyncCallback<number>): void

Obtains the index of the text where the cursor is located. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the text index is obtained, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
  if (err) {
    console.error(\`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});

#### \[h2\]getTextIndexAtCursor10+

getTextIndexAtCursor(): Promise<number>

Obtains the index of the text where the cursor is located. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getTextIndexAtCursorSync10+

getTextIndexAtCursorSync(): number

Obtains the index of the text where the cursor is located.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| number | Index of the text where the cursor is located. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

let index: number = inputClient.getTextIndexAtCursorSync();
console.info(\`Succeeded in getTextIndexAtCursorSync, index: ${index}\`);

#### \[h2\]sendExtendAction10+

sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void

Sends an extended edit action. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/JvoYPiBDRICy9x1b9ssQXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA50BF50DCB3755DDDDC7154A67646DAF352F504AA1478D93107B963CB22AD66)

The input method applications call this API to send extended edit actions to the edit box. The edit box listens for the corresponding event using [on('handleExtendAction')](../ohos-inputmethod-input-method-framework/document.md#onhandleextendaction10) for further processing.

When the edit box responds to the **PASTE** command of [ExtendAction](#extendaction10), the edit box application needs to apply for the [ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard) permission.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | [ExtendAction](#extendaction10) | Yes | Extended edit action to send. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
  if (err) {
    console.error(\`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in sending extend action.');
});

#### \[h2\]sendExtendAction10+

sendExtendAction(action: ExtendAction): Promise<void>

Sends an extended edit action. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/IXvmSvBuTgeBZMVkptt17Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E53B4ECDC6970B25297D6A1E67D63BB3F383198DCC357116A439FEE2A1F1A5E)

The input method applications call this API to send extended edit actions to the edit box. The edit box listens for the corresponding event using [on('handleExtendAction')](../ohos-inputmethod-input-method-framework/document.md#onhandleextendaction10) for further processing.

When the edit box responds to the **PASTE** command of [ExtendAction](#extendaction10), the edit box application needs to apply for the [ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard) permission.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | [ExtendAction](#extendaction10) | Yes | Extended edit action to send. |

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
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]sendPrivateCommand12+

sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>

Sends private data to the system component that needs to communicate with the input method application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/zjDGpupmQUS5-xxh0ft7Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60A9082ECD308A06A394FF765E6A7E2674B18DC60E30296971A3A2704BD66683)

-   The private data channel allows communication between the system preset input method application and specific system components (such as a text box or a home screen application). It is usually used to implement custom input on a specific device.
-   The total size of the private data is 32 KB, and the maximum number of private data records is 5.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| commandData | Record<string, [CommandDataType](#commanddatatype12)\> | Yes | Private data to send. |

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
| 12800010 | not the preconfigured default input method. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
  let record: Record<string, inputMethodEngine.CommandDataType> = {
    "valueString1": "abcdefg",
    "valueString2": true,
    "valueString3": 500,
  }
  textInputClient.sendPrivateCommand(record).then(() => {
  }).catch((err: BusinessError) => {
    if (err !== undefined) {
      console.error(\`sendPrivateCommand catch error: ${err.code} ${err.message}\`);
    }
  });
})

#### \[h2\]getCallingWindowInfo12+

getCallingWindowInfo(): Promise<WindowInfo>

Obtains information about the application window, in which the input box that starts an input method is located. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/dX1GCdwKQrmuHsjOe-EmEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7A7FDACB1303896558E44370B010A0B4DEB9EEFD13FB4C2021582682D60DDE5)

This API applies only to the input method applications that use [Panel](#panel10) as the soft keyboard window.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[WindowInfo](#windowinfo12)\> | Promise used to return the information obtained. |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800012 | the input method panel does not exist. |
| 12800013 | window manager service error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
  console.info(\`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}\`);
  console.info(\`windowInfo.status: ${windowInfo.status}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setPreviewText12+

setPreviewText(text: string, range: Range): Promise<void>

Sets the preview text. This API uses a promise to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Preview text to set. |
| range | [Range](#range10) | Yes | 
Range of the preview text.

\- If the value is { start: -1, end: -1 }, **text** replaces the entire text in the current preview area by default.

\- If **start** is equal to **end**, **text** is inserted into the cursor position specified by **start**.

\- If **start** is not equal to **end**, **text** replaces the text of the specified range.

\- If the values of **start** and **end** are negative values, a parameter error is returned.

\- If there is preview text in the text box, the value of **range** cannot exceed the range of the preview text. Otherwise, a parameter error is returned.

\- If there is no preview text in the text box, the value of **range** cannot exceed the text range of the text box. Otherwise, a parameter error is returned.

 |

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
| 12800011 | text preview not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewText('test', range).then(() => {
  console.info('Succeeded in setting preview text.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]setPreviewTextSync12+

setPreviewTextSync(text: string, range: Range): void

Sets the preview text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Preview text to set. |
| range | [Range](#range10) | Yes | 
Range of the preview text.

\- If the value is { start: -1, end: -1 }, **text** replaces the entire text in the current preview area by default.

\- If **start** is equal to **end**, **text** is inserted into the cursor position specified by **start**.

\- If **start** is not equal to **end**, **text** replaces the text of the specified range.

\- If the values of **start** and **end** are negative values, a parameter error is returned.

\- If there is preview text in the text box, the value of **range** cannot exceed the range of the preview text. Otherwise, a parameter error is returned.

\- If there is no preview text in the text box, the value of **range** cannot exceed the text range of the text box. Otherwise, a parameter error is returned.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**Example**

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);

#### \[h2\]finishTextPreview12+

finishTextPreview(): Promise<void>

Finishes the text preview. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/TOlLKBE5SqK0YDDAcTPIfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49ABA633FE41319B1DF4CB8C22D14FAAE8A65BF1B9CF80ACDDABCF041CC16548)

If there is preview text in the current text box, calling this API will display the preview text on the screen.

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
| 12800011 | text preview not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

inputClient.finishTextPreview().then(() => {
  console.info('Succeeded in finishing text preview.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]finishTextPreviewSync12+

finishTextPreviewSync(): void

Finishes the text preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/3H9pqmjnRhGT5wzR84WFAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C393C68E7B113444896A6D04612AEB312313879621786CC140F0E7C25A2B4517)

If there is preview text in the current text box, calling this API will display the preview text on the screen.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800011 | text preview not supported. |

**Example**

inputClient.finishTextPreviewSync();

#### \[h2\]sendMessage15+

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

Sends the custom communication to the edit box application attached to the input method application. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/L14GKLgJQ0eU2nM_9H5P4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=157B8B7D9CC174B88CE478EB99A5855E9D58A637C267252A3A297F01299DFB5E)

This API can be called only when the edit box is attached to the input method and enter the edit mode, and the input method application is in full experience mode.

The maximum length of **msgId** is 256 B, and the maximum length of **msgParam** is 128 KB.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgId | string | Yes | Identifier of the custom data to be sent to the edit box application attached to the input method application. |
| msgParam | ArrayBuffer | No | Message body of the custom data to be sent to the edit box application attached to the input method application. |

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
inputClient.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(\`Failed to send message. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]recvMessage15+

recvMessage(msgHandler?: MessageHandler): void;

Registers or unregisters MessageHandler.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/UfluMNM9Q4mgrTDdVphyfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3320C9F0EFA0907353F5745B4BE5D12605DE8B952B062AD9C985BA275792078F)

The [MessageHandler](#messagehandler15) object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](#onterminated15) callback of the penultimate registered object is triggered.

If no parameter is set, unregister [MessageHandler](#messagehandler15). Its [onTerminated](#onterminated15) callback will be triggered.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| msgHandler | [MessageHandler](#messagehandler15) | No | 
This object receives custom communication data from the edit box application attached to the input method application through [onMessage](#onmessage15) and receives a message for terminating the subscription to this object through [onTerminated](#onterminated15).

If no parameter is set, unregister [MessageHandler](#messagehandler15). Its [onTerminated](#onterminated15) callback will be triggered.

 |

**Error codes**

For details about the error codes, see [Input Method Framework Error Codes](../../error-codes/input-method-framework-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**Example**

inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });

#### \[h2\]getAttachOptions19+

getAttachOptions(): AttachOptions

Obtains the additional options for binding an input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| [AttachOptions](#attachoptions19) | Additional options for binding an input method. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/qLw9th3YTeiPqRbuY-SRyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE94AF47237F01042658FE61F4272F8AA4E1529F54872FAB0227B6A75E25DE94)

Error code 801 Capability not supported. is removed since API version 20.

**Example**

let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(\`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}\`);

#### \[h2\]on('attachOptionsDidChange')19+

on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void

Subscribes to the event indicating that the additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Additional option change event when the input method is bound. The value is fixed to **'attachOptionsDidChange'**. |
| callback | Callback<[AttachOptions](#attachoptions19)\> | Yes | Callback used to return the additional options for binding an input method. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/yNfDKWWfQCysHRjzVfTp2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2519E9D527CAD592A80A16F3A51672094F62C0628CB16A155E5FA1904D78CBDD)

Error code 801 Capability not supported. is removed since API version 20.

**Example**

let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(\`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered\`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(\`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange\`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(\`attachOptionsDidChange unsubscribed from attachOptionsDidChange\`);

#### \[h2\]off('attachOptionsDidChange')19+

off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void

Unsubscribes from the event indicating that additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Additional option change event when the input method is bound. The value is fixed to **'attachOptionsDidChange'**. |
| callback | Callback<[AttachOptions](#attachoptions19)\> | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type by default. |

**Example**

let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(\`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered\`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(\`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange\`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(\`attachOptionsDidChange unsubscribed from attachOptionsDidChange\`);

#### \[h2\]CapitalizeMode20+

Enumerates the modes of capitalizing the first letter of a text.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The first letter is not capitalized. |
| SENTENCES | 1 | The first letter of each sentence is capitalized. |
| WORDS | 2 | The first letter of each word is capitalized. |
| CHARACTERS | 3 | All letters are capitalized. |

#### \[h2\]EditorAttribute

Represents the attributes of the edit box.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enterKeyType | number | Yes | No | Function attributes of the edit box. For details, see [function key definitions in constants](#constants). |
| inputPattern | number | Yes | No | Text attribute of the edit box. For details, see [edit box definitions in constants](#constants). |
| isTextPreviewSupported12+ | boolean | No | No | 
Whether text preview is supported.

\- **true**: Supported.

\- **false**: Unsupported.

 |
| bundleName14+ | string | Yes | Yes | Name of the application package to which the edit box belongs. The value may be **""**. Handle this scenario when using the attribute. |
| immersiveMode15+ | [ImmersiveMode](#immersivemode15) | Yes | Yes | Immersive mode of the input method. |
| windowId18+ | number | Yes | Yes | ID of the window where the edit box is located. |
| displayId18+ | number | Yes | Yes | Screen ID of the window corresponding to the edit box. If window ID is not set, the screen ID of the focused window is used. |
| placeholder20+ | string | Yes | Yes | Placeholder information set for the edit box. |
| abilityName20+ | string | Yes | Yes | Ability name set for the edit box. |
| capitalizeMode20+ | [CapitalizeMode](#capitalizemode20) | Yes | Yes | Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first letter is not capitalized by default. |
| gradientMode20+ | [GradientMode](#gradientmode20) | Yes | Yes | Gradient mode. If this attribute is not specified or is set to an invalid value, the gradient mode is not used by default. |
| extraConfig22+ | [InputMethodExtraConfig](../ohos-inputmethod-extraconfig-input-method-extension-information/document.md#inputmethodextraconfig) | Yes | Yes | Extra information about the input method. |

#### KeyEvent

Represents the attributes of a key.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| keyCode | number | Yes | No | Key value. For details, see [KeyCode](../../../../system/basic-functions/input-kit/arkts-apis/ohos-multimodalinput-keycode-keycode/document.md#keycode). |
| keyAction | number | Yes | No | 
Key event type.

\- **2**: keydown event.

\- **3**: keyup event.

 |

#### PanelFlag10+

Enumerates the state types of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| FLG\_FIXED | 0 | Fixed state type. |
| FLG\_FLOATING | 1 | Floating state type. |
| FLAG\_CANDIDATE15+ | 2 | Candidate state type. |

#### PanelType10+

Enumerates the types of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SOFT\_KEYBOARD | 0 | Soft keyboard type. |
| STATUS\_BAR | 1 | Status bar type. |

#### PanelInfo10+

Describes the attributes of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [PanelType](#paneltype10) | No | No | Type of the panel. |
| flag | [PanelFlag](#panelflag10) | No | Yes | State type of the panel. |

#### PanelRect12+

Represents the size of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| landscapeRect | [window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | No | Size of the input method panel window in landscape mode. |
| portraitRect | [window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | No | Size of the input method panel window in portrait mode. |

#### EnhancedPanelRect15+

Indicates the size of the enhanced input method panel, including the custom avoid area and touch area.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| landscapeRect | [window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | Yes | 
Size of the input method panel window in landscape mode.

\- This attribute is mandatory when **fullScreenMode** is not set or is set to **false**.

 |
| portraitRect | [window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | Yes | 

Size of the input method panel window in portrait mode.

\- This attribute is mandatory when **fullScreenMode** is not set or is set to **false**.

 |
| landscapeAvoidY | number | No | Yes | 

Distance between the avoid line and the top of the panel in landscape mode, in px. The default value is **0**.

\- Other system components in the application avoid the input method panel area below the avoid line.

\- When the panel is fixed, the distance between the avoid line and the bottom of the screen cannot exceed 70% of the screen height.

 |
| landscapeInputRegion | Array<[window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7)\> | No | Yes | 

Region where the panel receives input events in landscape mode.

\- The array size is limited to \[1, 4\]. The default value is the panel size in landscape mode.

\- The input hot zone is relative to the left vertex of the input method panel window.

 |
| portraitAvoidY | number | No | Yes | 

Distance between the avoid line and the top of the panel in portrait mode, in px. The default value is **0**.

\- Other system components in the application avoid the input method panel area below the avoid line.

\- When the panel is fixed, the distance between the avoid line and the bottom of the screen cannot exceed 70% of the screen height.

 |
| portraitInputRegion | Array<[window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7)\> | No | Yes | 

Region where the panel receives input events in portrait mode.

\- The array size is limited to \[1, 4\]. The default value is the panel size in portrait mode.

\- The input hot zone is relative to the left vertex of the input method panel window.

 |
| fullScreenMode | boolean | No | Yes | 

Indicates whether to enable the full-screen mode. The default value is **false**.

\- If the value is **true**, **landscapeRect** and **portraitRect** are optional.

\- If the value is **false**, **landscapeRect** and **portraitRect** are mandatory.

 |

#### KeyboardArea15+

Represents the keyboard area on the panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| top | number | No | No | Distance between the upper boundary of the keyboard area and the upper boundary of the panel area, in pixels. The value is an integer. |
| bottom | number | No | No | Distance between the lower boundary of the keyboard area and the lower boundary of the panel area, in pixels. The value is an integer. |
| left | number | No | No | Distance between the left boundary of the keyboard area and the left boundary of the panel area, in pixels. The value is an integer. |
| right | number | No | No | Distance between the right border of the keyboard area and the right border of the panel area, in pixels. The value is an integer. |

#### AttachOptions19+

Defines additional options for binding an input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| requestKeyboardReason | [RequestKeyboardReason](#requestkeyboardreason19) | No | Yes | Reason for requesting the keyboard. This attribute is set by the edit box application. If this attribute is not set or is set to an invalid value, the keyboard will not be triggered by default. |
| isSimpleKeyboardEnabled20+ | boolean | No | Yes | 
Whether to enable the simple keyboard. This attribute is set by the edit box application. The value **true** means that the simple keyboard is enabled, and the value **false** means the opposite.

If this attribute is not set or is set to an invalid value, the simple keyboard is disabled by default.

 |

#### WindowInfo12+

Represents window information.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rect | [window.Rect](../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#rect7) | No | No | Rectangular area of the window. |
| status | [window.WindowStatusType](../../../arkui/arkts-api/window-manager/ohos-window-window/enums/document.md#windowstatustype11) | No | No | Window status type. |

#### ImmersiveMode15+

Enumerates the immersive modes of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE\_IMMERSIVE | 0 | The immersive mode is not used. |
| IMMERSIVE | 1 | The immersive mode is used. Its style is determined by the input method application. |
| LIGHT\_IMMERSIVE | 2 | Immersive style in light mode. |
| DARK\_IMMERSIVE | 3 | Immersive style in dark mode. |

#### RequestKeyboardReason19+

Enumerates the reasons for requesting keyboard input.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The keyboard request is triggered for no reason. |
| MOUSE | 1 | The keyboard request is triggered by a mouse operation. |
| TOUCH | 2 | The keyboard request is triggered by a touch operation. |
| OTHER | 20 | The keyboard request is triggered by other reasons. |

#### GradientMode20+

Enumerates the gradient modes of the input method.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The gradient mode is not used. |
| LINEAR\_GRADIENT | 1 | Linear gradient. |

#### ImmersiveEffect20+

Describes the immersive effect.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| gradientHeight | number | No | No | Gradient height, which cannot exceed 15% of the screen height. |
| gradientMode | [GradientMode](#gradientmode20) | No | No | Gradient mode. |

#### SystemPanelInsets21+

Defines the offset area between the input method soft keyboard and the system panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bottom | number | Yes | No | Distance between the bottom border of the keyboard area and the bottom border of the system panel area, in px. The value is an integer. |
| left | number | Yes | No | Distance between the left border of the keyboard area and the left border of the system panel area, in px. The value is an integer. |
| right | number | Yes | No | Distance between the right border of the keyboard area and the right border of the system panel area, in px. The value is an integer. |

#### TextInputClient(deprecated)

You must first use [on('inputStart')](#oninputstart) to obtain a **TextInputClient** instance, and then use this instance to call the following APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/U7dktHARQ_OCL2IUOMKE_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1BB87F2E0C8412E64AEC7AD79548B4A0D61034FDBF1EB15A9AD0D215E4A796A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [InputClient](#inputclient9) instead.

#### \[h2\]getForward(deprecated)

getForward(length:number, callback: AsyncCallback<string>): void

Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/QdxNu_XMQNe6O6OWiSZdJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EDBA4057E182EA52550598D68420893D47B63C6AA6A46036F8327D51C40365A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getForward](#getforward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(\`Failed to getForward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});

#### \[h2\]getForward(deprecated)

getForward(length:number): Promise<string>

Obtains the specific-length text before the cursor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/a4jFXiH-S8ezE7OD23OIKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD8E53B93EABE76756848F7BBC168665A90372BC37A920B52E4AA48B07027796)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getForward](#getforward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the specific-length text before the cursor. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getForward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getBackward(deprecated)

getBackward(length:number, callback: AsyncCallback<string>): void

Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/3nSt-wwSSSS3WkKNA87_6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20B47555547E124F7732829273509D4D00A301738994042376A2218B16C343A5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getBackward](#getbackward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(\`Failed to getBackward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});

#### \[h2\]getBackward(deprecated)

getBackward(length:number): Promise<string>

Obtains the specific-length text after the cursor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/KlPyT7TeSauOZrL5FX6d1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2159F857E7E69A65CF7FD280D95C4DFDBA975310B53A3C88477BFEC134257AD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getBackward](#getbackward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the specific-length text after the cursor. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length).then((text: string) => {
  console.info(\`'Succeeded in getting backward: ${text}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getBackward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]deleteForward(deprecated)

deleteForward(length:number, callback: AsyncCallback<boolean>): void

Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/E72Bt9tdRVCZpeWAmShmcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6585575E8A6147DB588E6CAF19FE216B01E0C711CF52223B1249530F02663FA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [deleteForward](#deleteforward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to deleteForward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to deleteForward.');
  }
});

#### \[h2\]deleteForward(deprecated)

deleteForward(length:number): Promise<boolean>

Deletes the fixed-length text before the cursor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/TAR88g6pTwKsI8tc3oREIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0B0CFE99AB16F0100EDA1C11BC652F0E67E1386EF92AC77C97A66A457C87707)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [deleteForward](#deleteforward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the deletion is successful, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete forward.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to deleteForward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]deleteBackward(deprecated)

deleteBackward(length:number, callback: AsyncCallback<boolean>): void

Deletes the fixed-length text after the cursor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/K12cxTlFQCeNa2K48FPh4g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B2927E990BCB14F2A8AAE657A7508EEEEF9EA2A5575D39B33D45CA082DD8427)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [deleteBackward](#deletebackward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
});

#### \[h2\]deleteBackward(deprecated)

deleteBackward(length:number): Promise<boolean>

Deletes the fixed-length text after the cursor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ryeQPlNBTRaJo-lvkPW6Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F32F3A9D640AAC3A7EC0119762AE86730262D9F30B086A4A7D28126367AE7586)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [deleteBackward](#deletebackward9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | Text length, which cannot be less than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the deletion is successful, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]sendKeyFunction(deprecated)

sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void

Sends the function key. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/4Q-AjPy_ReCaqzjCG4POdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94F09715D03091022D734F171579BBF5ACB5702DBCAF0640C1A7FCA13A0101B4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sendKeyFunction](#sendkeyfunction9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | number | Yes | 
Action of the function key.

\- **0**: invalid key.

\- **1**: confirm key (Enter key).

 |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});

#### \[h2\]sendKeyFunction(deprecated)

sendKeyFunction(action: number): Promise<boolean>

Sends the function key. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ThTvjtOoRLKr2QpGcc0Kfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B03700586A882CE64B9508BA7FEA51860C605359FE2DB9EDB76CC093F97CB65)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sendKeyFunction](#sendkeyfunction9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| action | number | Yes | 
Action of the function key.

**0**: invalid key.

**1**: confirm key (Enter key).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the setting is successful, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]insertText(deprecated)

insertText(text:string, callback: AsyncCallback<boolean>): void

Inserts text. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/H-eqJU-TS7SVVgjmPzvSsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=051B393A56F8C6D0C2BA9E976BE5047C708AE3F98AD12FADE3A17E9DE2E8049C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [insertText](#inserttext9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to insert. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(\`Failed to insertText. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});

#### \[h2\]insertText(deprecated)

insertText(text:string): Promise<boolean>

Inserts text. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ZKP6rCzIRwq9scpXlqC-zQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D702B55B2974F23C65507B5AB1976EE992349F973616C4323445E51A0EE501EB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [insertText](#inserttext9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to insert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means that the insertion is successful, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to insertText. Code is ${err.code}, message is ${err.message}\`);
});

#### \[h2\]getEditorAttribute(deprecated)

getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void

Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/CY4HVsgfQIeRQCVy8IUdlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7383B3D6B68F625140D204266B26BD9763C5EA218DFE6D1CA59815A63A53B1D8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getEditorAttribute](#geteditorattribute9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[EditorAttribute](#editorattribute)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the attribute of the edit box. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute((err: BusinessError,
  editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(\`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}\`);
    return;
  }
  console.info(\`editorAttribute.inputPattern: ${editorAttribute.inputPattern}\`);
  console.info(\`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}\`);
});

#### \[h2\]getEditorAttribute(deprecated)

getEditorAttribute(): Promise<EditorAttribute>

Obtains the attribute of the edit box. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VKWBVhkMTkG9Uu_JuLm02w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5927B1A2D5FC980B4C4C9A7C28200019BED5EA3A558F99323C1A536BC512E4C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [getEditorAttribute](#geteditorattribute9) instead.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[EditorAttribute](#editorattribute)\> | Promise used to return the attribute of the edit box. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(\`editorAttribute.inputPattern: ${editorAttribute.inputPattern}\`);
  console.info(\`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}}\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}\`);
});
