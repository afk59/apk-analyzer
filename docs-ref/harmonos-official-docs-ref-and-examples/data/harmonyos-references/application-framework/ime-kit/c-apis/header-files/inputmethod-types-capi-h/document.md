# inputmethod\_types\_capi.h

#### Overview

Defines the types related to the input method.

**File to include**: <inputmethod/inputmethod\_types\_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](../../modules/inputmethod/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [InputMethod\_KeyboardStatus](#inputmethod_keyboardstatus) | InputMethod\_KeyboardStatus | Keyboard status. |
| [InputMethod\_EnterKeyType](#inputmethod_enterkeytype) | InputMethod\_EnterKeyType | Enter key type. |
| [InputMethod\_Direction](#inputmethod_direction) | InputMethod\_Direction | Moving direction. |
| [InputMethod\_ExtendAction](#inputmethod_extendaction) | InputMethod\_ExtendAction | Type of the extended edit action on the text box. |
| [InputMethod\_TextInputType](#inputmethod_textinputtype) | InputMethod\_TextInputType | Text input type. |
| [InputMethod\_CommandValueType](#inputmethod_commandvaluetype) | InputMethod\_CommandValueType | Private data type. |
| [InputMethod\_ErrorCode](#inputmethod_errorcode) | InputMethod\_ErrorCode | Error code of the input method. |
| [InputMethod\_RequestKeyboardReason](#inputmethod_requestkeyboardreason) | InputMethod\_RequestKeyboardReason | Reason for requesting the keyboard. |

#### Enum Description

#### \[h2\]InputMethod\_KeyboardStatus

enum InputMethod\_KeyboardStatus

**Description**

Enumerates the keyboard status.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_KEYBOARD\_STATUS\_NONE = 0 | NONE. |
| IME\_KEYBOARD\_STATUS\_HIDE = 1 | Invisible. |
| IME\_KEYBOARD\_STATUS\_SHOW = 2 | Visible. |

#### \[h2\]InputMethod\_EnterKeyType

enum InputMethod\_EnterKeyType

**Description**

Enumerates the Enter key types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_ENTER\_KEY\_UNSPECIFIED = 0 | Unspecified. |
| IME\_ENTER\_KEY\_NONE = 1 | NONE. |
| IME\_ENTER\_KEY\_GO = 2 | Go. |
| IME\_ENTER\_KEY\_SEARCH = 3 | Search. |
| IME\_ENTER\_KEY\_SEND = 4 | Send. |
| IME\_ENTER\_KEY\_NEXT = 5 | Next. |
| IME\_ENTER\_KEY\_DONE = 6 | Done. |
| IME\_ENTER\_KEY\_PREVIOUS = 7 | Previous. |
| IME\_ENTER\_KEY\_NEWLINE = 8 | Line break. |

#### \[h2\]InputMethod\_Direction

enum InputMethod\_Direction

**Description**

Enumerates the moving directions.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_DIRECTION\_NONE = 0 | NONE. |
| IME\_DIRECTION\_UP = 1 | Upward. |
| IME\_DIRECTION\_DOWN = 2 | Downward. |
| IME\_DIRECTION\_LEFT = 3 | Leftward. |
| IME\_DIRECTION\_RIGHT = 4 | Rightward. |

#### \[h2\]InputMethod\_ExtendAction

enum InputMethod\_ExtendAction

**Description**

Enumerates the types of the extended edit action on the text box.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_EXTEND\_ACTION\_SELECT\_ALL = 0 | Select all. |
| IME\_EXTEND\_ACTION\_CUT = 3 | Cut. |
| IME\_EXTEND\_ACTION\_COPY = 4 | Copy. |
| IME\_EXTEND\_ACTION\_PASTE = 5 | Paste. |

#### \[h2\]InputMethod\_TextInputType

enum InputMethod\_TextInputType

**Description**

Enumerates the text input types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_TEXT\_INPUT\_TYPE\_NONE = -1 | NONE. |
| IME\_TEXT\_INPUT\_TYPE\_TEXT = 0 | Text. |
| IME\_TEXT\_INPUT\_TYPE\_MULTILINE = 1 | Multi-line. |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER = 2 | Number. |
| IME\_TEXT\_INPUT\_TYPE\_PHONE = 3 | Phone number. |
| IME\_TEXT\_INPUT\_TYPE\_DATETIME = 4 | Date. |
| IME\_TEXT\_INPUT\_TYPE\_EMAIL\_ADDRESS = 5 | Email address. |
| IME\_TEXT\_INPUT\_TYPE\_URL = 6 | URL. |
| IME\_TEXT\_INPUT\_TYPE\_VISIBLE\_PASSWORD = 7 | Password. |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER\_PASSWORD = 8 | Numeric password. |
| IME\_TEXT\_INPUT\_TYPE\_SCREEN\_LOCK\_PASSWORD = 9 | Lock screen password. |
| IME\_TEXT\_INPUT\_TYPE\_USER\_NAME = 10 | Username. |
| IME\_TEXT\_INPUT\_TYPE\_NEW\_PASSWORD = 11 | New password. |
| IME\_TEXT\_INPUT\_TYPE\_NUMBER\_DECIMAL = 12 | Decimal number. |
| IME\_TEXT\_INPUT\_TYPE\_ONE\_TIME\_CODE = 13 | Verification code. **Since**: 20 |

#### \[h2\]InputMethod\_CommandValueType

enum InputMethod\_CommandValueType

**Description**

Enumerates the private data types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_COMMAND\_VALUE\_TYPE\_NONE = 0 | NONE. |
| IME\_COMMAND\_VALUE\_TYPE\_STRING = 1 | String. |
| IME\_COMMAND\_VALUE\_TYPE\_BOOL = 2 | Boolean. |
| IME\_COMMAND\_VALUE\_TYPE\_INT32 = 3 | 32-bit signed integer. |

#### \[h2\]InputMethod\_ErrorCode

enum InputMethod\_ErrorCode

**Description**

Enumerates the input method error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IME\_ERR\_OK = 0 | Success. |
| IME\_ERR\_UNDEFINED = 1 | Undefined error. |
| IME\_ERR\_PARAMCHECK = 401 | Parameter check failed. |
| IME\_ERR\_PACKAGEMANAGER = 12800001 | Package management error. |
| IME\_ERR\_IMENGINE = 12800002 | Input method application error. |
| IME\_ERR\_IMCLIENT = 12800003 | Text box client error. |
| IME\_ERR\_CONFIG\_PERSIST = 12800005 | Configuration persistence failed. This error code is reported when the configuration fails to be saved. |
| IME\_ERR\_CONTROLLER = 12800006 | Input method controller error. |
| IME\_ERR\_SETTINGS = 12800007 | Input method setter error. |
| IME\_ERR\_IMMS = 12800008 | Input method manager service error. |
| IME\_ERR\_DETACHED = 12800009 | Text box unbound. |
| IME\_ERR\_NULL\_POINTER = 12802000 | Null pointer. |
| IME\_ERR\_QUERY\_FAILED = 12802001 | Query failed. |

#### \[h2\]InputMethod\_RequestKeyboardReason

enum InputMethod\_RequestKeyboardReason

**Description**

Enumerates the reasons for requesting the keyboard.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| IME\_REQUEST\_REASON\_NONE = 0 | No reason. |
| IME\_REQUEST\_REASON\_MOUSE = 1 | Mouse operation. |
| IME\_REQUEST\_REASON\_TOUCH = 2 | Touch operation. |
| IME\_REQUEST\_REASON\_OTHER = 20 | Other reasons. |
