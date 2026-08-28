# native\_key\_event.h

#### Overview

Declares the APIs of **NativeKeyEvent**.

**File to include**: <arkui/native\_key\_event.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 14

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [NdkKeyEvent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NdkKeyEvent)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_KeyCode](#arkui_keycode) | ArkUI\_KeyCode | Enumerates the key codes for key events. |
| [ArkUI\_KeyEventType](#arkui_keyeventtype) | ArkUI\_KeyEventType | Enumerates the types of key events. |
| [ArkUI\_KeySourceType](#arkui_keysourcetype) | ArkUI\_KeySourceType | Enumerates the types of input devices that trigger key events. |
| [ArkUI\_KeyIntension](#arkui_keyintension) | ArkUI\_KeyIntension | Enumerates the intentions corresponding to key events. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_KeyEventType OH\_ArkUI\_KeyEvent\_GetType(const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_gettype) | Obtains the type of the specified key event. |
| [int32\_t OH\_ArkUI\_KeyEvent\_GetKeyCode(const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_getkeycode) | Obtains the key code from the specified key event. |
| [const char OH\_ArkUI\_KeyEvent\_GetKeyText(const ArkUI\_UIInputEvent event)](#oh_arkui_keyevent_getkeytext) | Obtains the key value from the specified key event. |
| [ArkUI\_KeySourceType OH\_ArkUI\_KeyEvent\_GetKeySource(const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_getkeysource) | Obtains the type of input device that triggers the specified key event. |
| [void OH\_ArkUI\_KeyEvent\_StopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)](#oh_arkui_keyevent_stoppropagation) | Stops the specified key event from bubbling upwards or downwards. |
| [ArkUI\_KeyIntension OH\_ArkUI\_KeyEvent\_GetKeyIntensionCode(const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_getkeyintensioncode) | Obtains the intention code associated with the specified key event. |
| [uint32\_t OH\_ArkUI\_KeyEvent\_GetUnicode(const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_getunicode) | Obtains the Unicode value of the specified key event. Non-space basic Latin characters in the 0x0021-0x007E range are supported. Characters with a value of 0 are not supported. In the case of key combination, this API returns the Unicode value of the key corresponding to the key event. |
| [void OH\_ArkUI\_KeyEvent\_SetConsumed(const ArkUI\_UIInputEvent\* event, bool isConsumed)](#oh_arkui_keyevent_setconsumed) | Sets whether the specified key event is consumed in the key event callback. |
| [void OH\_ArkUI\_KeyEvent\_Dispatch(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)](#oh_arkui_keyevent_dispatch) | Dispatches the specified key event to a specific node. |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsNumLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](#oh_arkui_keyevent_isnumlockon) | Obtains the state of the NumLock key when the specified key event occurs. |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsCapsLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](#oh_arkui_keyevent_iscapslockon) | Obtains the state of the CapsLock key when the specified key event occurs. |
| [ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsScrollLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)](#oh_arkui_keyevent_isscrolllockon) | Obtains the state of the ScrollLock key when the specified key event occurs. |

#### Enum Description

#### \[h2\]ArkUI\_KeyCode

enum ArkUI\_KeyCode

**Description**

Enumerates the key codes for key events.

**Since**: 14

| Value | Description |
| :-- | :-- |
| ARKUI\_KEYCODE\_UNKNOWN = -1 | Unknown key |
| ARKUI\_KEYCODE\_FN = 0 | Function (Fn) key |
| ARKUI\_KEYCODE\_VOLUME\_UP = 16 | Volume Up key |
| ARKUI\_KEYCODE\_VOLUME\_DOWN = 17 | Volume Down key |
| ARKUI\_KEYCODE\_POWER = 18 | Power key |
| ARKUI\_KEYCODE\_CAMERA = 19 | Camera key |
| ARKUI\_KEYCODE\_VOLUME\_MUTE = 22 | Speaker Mute key |
| ARKUI\_KEYCODE\_MUTE = 23 | Mute key |
| ARKUI\_KEYCODE\_BRIGHTNESS\_UP = 40 | Brightness Up key. |
| ARKUI\_KEYCODE\_BRIGHTNESS\_DOWN = 41 | Brightness Down key. |
| ARKUI\_KEYCODE\_0 = 2000 | Key 0 |
| ARKUI\_KEYCODE\_1 = 2001 | Key 1 |
| ARKUI\_KEYCODE\_2 = 2002 | Key 2 |
| ARKUI\_KEYCODE\_3 = 2003 | Key 3 |
| ARKUI\_KEYCODE\_4 = 2004 | Key 4 |
| ARKUI\_KEYCODE\_5 = 2005 | Key 5 |
| ARKUI\_KEYCODE\_6 = 2006 | Key 6 |
| ARKUI\_KEYCODE\_7 = 2007 | Key 7 |
| ARKUI\_KEYCODE\_8 = 2008 | Key 8 |
| ARKUI\_KEYCODE\_9 = 2009 | Key 9 |
| ARKUI\_KEYCODE\_STAR = 2010 | Key \* |
| ARKUI\_KEYCODE\_POUND = 2011 | Key # |
| ARKUI\_KEYCODE\_DPAD\_UP = 2012 | Up key on D-pad. |
| ARKUI\_KEYCODE\_DPAD\_DOWN = 2013 | Down key on D-pad. |
| ARKUI\_KEYCODE\_DPAD\_LEFT = 2014 | Left key on D-pad. |
| ARKUI\_KEYCODE\_DPAD\_RIGHT = 2015 | Right key on D-pad. |
| ARKUI\_KEYCODE\_DPAD\_CENTER = 2016 | Center key on D-pad. |
| ARKUI\_KEYCODE\_A = 2017 | Key A |
| ARKUI\_KEYCODE\_B = 2018 | Key B |
| ARKUI\_KEYCODE\_C = 2019 | Key C |
| ARKUI\_KEYCODE\_D = 2020 | Key D |
| ARKUI\_KEYCODE\_E = 2021 | Key E |
| ARKUI\_KEYCODE\_F = 2022 | Key F |
| ARKUI\_KEYCODE\_G = 2023 | Key G |
| ARKUI\_KEYCODE\_H = 2024 | Key H |
| ARKUI\_KEYCODE\_I = 2025 | Key I |
| ARKUI\_KEYCODE\_J = 2026 | Key J |
| ARKUI\_KEYCODE\_K = 2027 | Key K |
| ARKUI\_KEYCODE\_L = 2028 | Key L |
| ARKUI\_KEYCODE\_M = 2029 | Key M |
| ARKUI\_KEYCODE\_N = 2030 | Key N |
| ARKUI\_KEYCODE\_O = 2031 | Key O |
| ARKUI\_KEYCODE\_P = 2032 | Key P |
| ARKUI\_KEYCODE\_Q = 2033 | Key Q |
| ARKUI\_KEYCODE\_R = 2034 | Key R |
| ARKUI\_KEYCODE\_S = 2035 | Key S |
| ARKUI\_KEYCODE\_T = 2036 | Key T |
| ARKUI\_KEYCODE\_U = 2037 | Key U |
| ARKUI\_KEYCODE\_V = 2038 | Key V |
| ARKUI\_KEYCODE\_W = 2039 | Key W |
| ARKUI\_KEYCODE\_X = 2040 | Key X |
| ARKUI\_KEYCODE\_Y = 2041 | Key Y |
| ARKUI\_KEYCODE\_Z = 2042 | Key Z |
| ARKUI\_KEYCODE\_COMMA = 2043 | Key , |
| ARKUI\_KEYCODE\_PERIOD = 2044 | Key . |
| ARKUI\_KEYCODE\_ALT\_LEFT = 2045 | Left Alt key |
| ARKUI\_KEYCODE\_ALT\_RIGHT = 2046 | Right Alt key |
| ARKUI\_KEYCODE\_SHIFT\_LEFT = 2047 | Left Shift key |
| ARKUI\_KEYCODE\_SHIFT\_RIGHT = 2048 | Right Shift key |
| ARKUI\_KEYCODE\_TAB = 2049 | Tab key |
| ARKUI\_KEYCODE\_SPACE = 2050 | Space key |
| ARKUI\_KEYCODE\_SYM = 2051 | Symbol key |
| ARKUI\_KEYCODE\_EXPLORER = 2052 | Explorer key, which is used to start the explorer application |
| ARKUI\_KEYCODE\_ENVELOPE = 2053 | Email key, which is used to start the email application |
| ARKUI\_KEYCODE\_ENTER = 2054 | Enter key |
| ARKUI\_KEYCODE\_DEL = 2055 | Delete key |
| ARKUI\_KEYCODE\_GRAVE = 2056 | Key \` |
| ARKUI\_KEYCODE\_MINUS = 2057 | Key - |
| ARKUI\_KEYCODE\_EQUALS = 2058 | Key = |
| ARKUI\_KEYCODE\_LEFT\_BRACKET = 2059 | Key \[ |
| ARKUI\_KEYCODE\_RIGHT\_BRACKET = 2060 | Key \] |
| ARKUI\_KEYCODE\_BACKSLASH = 2061 | Key \\ |
| ARKUI\_KEYCODE\_SEMICOLON = 2062 | Key ; |
| ARKUI\_KEYCODE\_APOSTROPHE = 2063 | Key ' |
| ARKUI\_KEYCODE\_SLASH = 2064 | Key / |
| ARKUI\_KEYCODE\_AT = 2065 | Key @ |
| ARKUI\_KEYCODE\_PLUS = 2066 | Key + |
| ARKUI\_KEYCODE\_MENU = 2067 | Menu key |
| ARKUI\_KEYCODE\_PAGE\_UP = 2068 | Page Up key |
| ARKUI\_KEYCODE\_PAGE\_DOWN = 2069 | Page Down key |
| ARKUI\_KEYCODE\_ESCAPE = 2070 | ESC key. |
| ARKUI\_KEYCODE\_FORWARD\_DEL = 2071 | Forward Delete key |
| ARKUI\_KEYCODE\_CTRL\_LEFT = 2072 | Left Ctrl key |
| ARKUI\_KEYCODE\_CTRL\_RIGHT = 2073 | Right Ctrl key |
| ARKUI\_KEYCODE\_CAPS\_LOCK = 2074 | Caps Lock key |
| ARKUI\_KEYCODE\_SCROLL\_LOCK = 2075 | Scroll Lock key |
| ARKUI\_KEYCODE\_META\_LEFT = 2076 | Left Meta key |
| ARKUI\_KEYCODE\_META\_RIGHT = 2077 | Right Meta key |
| ARKUI\_KEYCODE\_FUNCTION = 2078 | Function key |
| ARKUI\_KEYCODE\_SYSRQ = 2079 | System Request/Print Screen key |
| ARKUI\_KEYCODE\_BREAK = 2080 | Break/Pause key |
| ARKUI\_KEYCODE\_MOVE\_HOME = 2081 | Move to Home key |
| ARKUI\_KEYCODE\_MOVE\_END = 2082 | Move to End key |
| ARKUI\_KEYCODE\_INSERT = 2083 | Insert key |
| ARKUI\_KEYCODE\_FORWARD = 2084 | Forward key |
| ARKUI\_KEYCODE\_MEDIA\_PLAY = 2085 | Play key |
| ARKUI\_KEYCODE\_MEDIA\_PAUSE = 2086 | Pause key |
| ARKUI\_KEYCODE\_MEDIA\_CLOSE = 2087 | Close key |
| ARKUI\_KEYCODE\_MEDIA\_EJECT = 2088 | Eject key |
| ARKUI\_KEYCODE\_MEDIA\_RECORD = 2089 | Record key |
| ARKUI\_KEYCODE\_F1 = 2090 | F1 key |
| ARKUI\_KEYCODE\_F2 = 2091 | F2 key |
| ARKUI\_KEYCODE\_F3 = 2092 | F3 key |
| ARKUI\_KEYCODE\_F4 = 2093 | F4 key |
| ARKUI\_KEYCODE\_F5 = 2094 | F5 key |
| ARKUI\_KEYCODE\_F6 = 2095 | F6 key |
| ARKUI\_KEYCODE\_F7 = 2096 | F7 key |
| ARKUI\_KEYCODE\_F8 = 2097 | F8 key |
| ARKUI\_KEYCODE\_F9 = 2098 | F9 key |
| ARKUI\_KEYCODE\_F10 = 2099 | F10 key |
| ARKUI\_KEYCODE\_F11 = 2100 | F11 key |
| ARKUI\_KEYCODE\_F12 = 2101 | F12 key |
| ARKUI\_KEYCODE\_NUM\_LOCK = 2102 | Number Lock key on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_0 = 2103 | Key 0 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_1 = 2104 | Key 1 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_2 = 2105 | Key 2 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_3 = 2106 | Key 3 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_4 = 2107 | Key 4 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_5 = 2108 | Key 5 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_6 = 2109 | Key 6 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_7 = 2110 | Key 7 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_8 = 2111 | Key 8 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_9 = 2112 | Key 9 on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_DIVIDE = 2113 | Key / on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_MULTIPLY = 2114 | Key \* on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_SUBTRACT = 2115 | Key - on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_ADD = 2116 | Key + on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_DOT = 2117 | Key . on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_COMMA = 2118 | Key , on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_ENTER = 2119 | Enter key on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_EQUALS = 2120 | Key = on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_LEFT\_PAREN = 2121 | Key ( on numeric keypad |
| ARKUI\_KEYCODE\_NUMPAD\_RIGHT\_PAREN = 2122 | Key ) on numeric keypad |
| ARKUI\_KEYCODE\_BUTTON\_A = 2301 | 
Joystick key A

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_B = 2302 | 

Joystick key B

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_X = 2304 | 

Joystick key X

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_Y = 2305 | 

Joystick key Y

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_L1 = 2307 | 

Joystick key L1

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_R1 = 2308 | 

Joystick key R1

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_L2 = 2309 | 

Joystick key L2

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_R2 = 2310 | 

Joystick key R2

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_SELECT = 2311 | 

Joystick key Select

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_START = 2312 | 

Joystick key Start

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_MODE = 2313 | 

Joystick key Mode

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_THUMBL = 2314 | 

Joystick key THUMBL

**Since**: 15

 |
| ARKUI\_KEYCODE\_BUTTON\_THUMBR = 2315 | 

Joystick key THUMBR

**Since**: 15

 |

#### \[h2\]ArkUI\_KeyEventType

enum ArkUI\_KeyEventType

**Description**

Enumerates the types of key events.

**Since**: 14

| Value | Description |
| :-- | :-- |
| ARKUI\_KEY\_EVENT\_UNKNOWN = -1 | Unknown type. |
| ARKUI\_KEY\_EVENT\_DOWN = 0 | Key press. |
| ARKUI\_KEY\_EVENT\_UP = 1 | Release of a key. |
| ARKUI\_KEY\_EVENT\_LONG\_PRESS = 2 | Long press of a key. |
| ARKUI\_KEY\_EVENT\_CLICK = 3 | Click of a key. |

#### \[h2\]ArkUI\_KeySourceType

enum ArkUI\_KeySourceType

**Description**

Enumerates the types of input devices that trigger key events.

**Since**: 14

| Value | Description |
| :-- | :-- |
| ARKUI\_KEY\_SOURCE\_UNKNOWN = 0 | Unknown type. |
| ARKUI\_KEY\_SOURCE\_TYPE\_MOUSE = 1 | Mouse. |
| ARKUI\_KEY\_SOURCE\_TYPE\_KEYBOARD = 4 | Keyboard. |
| ARKUI\_KEY\_SOURCE\_TYPE\_JOYSTICK = 5 | 
Game controller.

**Since**: 15

 |

#### \[h2\]ArkUI\_KeyIntension

enum ArkUI\_KeyIntension

**Description**

Enumerates the intentions corresponding to key events.

**Since**: 14

| Value | Description |
| :-- | :-- |
| ARKUI\_KEY\_INTENSION\_UNKNOWN = -1 | Unknown intention. |
| ARKUI\_KEY\_INTENSION\_UP = 1 | Upward. |
| ARKUI\_KEY\_INTENSION\_DOWN = 2 | Downward. |
| ARKUI\_KEY\_INTENSION\_LEFT = 3 | Leftward. |
| ARKUI\_KEY\_INTENSION\_RIGHT = 4 | Rightward. |
| ARKUI\_KEY\_INTENSION\_SELECT = 5 | Select. |
| ARKUI\_KEY\_INTENSION\_ESCAPE = 6 | Return. |
| ARKUI\_KEY\_INTENSION\_BACK = 7 | Back. |
| ARKUI\_KEY\_INTENSION\_FORWARD = 8 | Forward. |
| ARKUI\_KEY\_INTENSION\_MENU = 9 | Menu. |
| ARKUI\_KEY\_INTENSION\_HOME = 10 | Home page. |
| ARKUI\_KEY\_INTENSION\_PAGE\_UP = 11 | Previous. |
| ARKUI\_KEY\_INTENSION\_PAGE\_DOWN = 12 | Next. |
| ARKUI\_KEY\_INTENSION\_ZOOM\_OUT = 13 | Zoom out. |
| ARKUI\_KEY\_INTENSION\_ZOOM\_IN = 14 | Zoom in. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_PLAY\_PAUSE = 100 | Play. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_FAST\_FORWARD = 101 | Fast-forward. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_FAST\_PLAYBACK = 103 | Fast playback. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_NEXT = 104 | Play the next media asset. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_PREVIOUS = 105 | Play the previous media asset. |
| ARKUI\_KEY\_INTENTION\_MEDIA\_MUTE = 106 | Mute. |
| ARKUI\_KEY\_INTENTION\_VOLUME\_UP = 107 | Volume up. |
| ARKUI\_KEY\_INTENTION\_VOLUME\_DOWN = 108 | Volume down. |
| ARKUI\_KEY\_INTENTION\_CALL = 200 | Answer a call. |
| ARKUI\_KEY\_INTENTION\_CAMERA = 300 | Take a photo. |

#### Function Description

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetType()

ArkUI\_KeyEventType OH\_ArkUI\_KeyEvent\_GetType(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the type of the specified key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_KeyEventType](#arkui_keyeventtype) | Key event type. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetKeyCode()

int32\_t OH\_ArkUI\_KeyEvent\_GetKeyCode(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the key code from the specified key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | Key code. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetKeyText()

const char \*OH\_ArkUI\_KeyEvent\_GetKeyText(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the key value from the specified key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| const char \* | Key value. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetKeySource()

ArkUI\_KeySourceType OH\_ArkUI\_KeyEvent\_GetKeySource(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the type of input device that triggers the specified key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_KeySourceType](#arkui_keysourcetype) | Input device type. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_StopPropagation()

void OH\_ArkUI\_KeyEvent\_StopPropagation(const ArkUI\_UIInputEvent\* event, bool stopPropagation)

**Description**

Stops the specified key event from bubbling upwards or downwards.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| bool stopPropagation | Whether to stop event propagation. The value **true** means to stop event propagation, and **false** means the opposite. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetKeyIntensionCode()

ArkUI\_KeyIntension OH\_ArkUI\_KeyEvent\_GetKeyIntensionCode(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the intention code associated with the specified key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_KeyIntension](#arkui_keyintension) | Intention code associated with the key event. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_GetUnicode()

uint32\_t OH\_ArkUI\_KeyEvent\_GetUnicode(const ArkUI\_UIInputEvent\* event)

**Description**

Obtains the Unicode value of the specified key event. Non-space basic Latin characters in the 0x0021-0x007E range are supported. Characters with a value of 0 are not supported. In the case of key combination, this API returns the Unicode value of the key corresponding to the key event.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| uint32\_t | Unicode value. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_SetConsumed()

void OH\_ArkUI\_KeyEvent\_SetConsumed(const ArkUI\_UIInputEvent\* event, bool isConsumed)

**Description**

Sets whether the specified key event is consumed in the key event callback.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| bool isConsumed | Whether the key event is consumed by the callback. The value **true** means that the key event is consumed, and **false** the opposite. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_Dispatch()

void OH\_ArkUI\_KeyEvent\_Dispatch(ArkUI\_NodeHandle node, const ArkUI\_UIInputEvent\* event)

**Description**

Dispatches the specified key event to a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Target node. |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |

#### \[h2\]OH\_ArkUI\_KeyEvent\_IsNumLockOn()

ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsNumLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)

**Description**

Obtains the state of the NumLock key when the specified key event occurs.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| bool\* state | Output parameter that returns the state of the NumLock key. The value **true** indicates an activated state, and **false** indicates an inactivated state. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyEvent\_IsCapsLockOn()

ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsCapsLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)

**Description**

Obtains the state of the CapsLock key when the specified key event occurs.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| bool\* state | Output parameter that returns the state of the CapsLock key. The value **true** indicates an activated state, and **false** indicates an inactivated state. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_KeyEvent\_IsScrollLockOn()

ArkUI\_ErrorCode OH\_ArkUI\_KeyEvent\_IsScrollLockOn(const ArkUI\_UIInputEvent\* event, bool\* state)

**Description**

Obtains the state of the ScrollLock key when the specified key event occurs.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ArkUI\_UIInputEvent](../../structs/arkui-uiinputevent/document.md)\* event | Pointer to the target **ArkUI\_UIInputEvent** object. |
| bool\* state | Output parameter that returns the state of the ScrollLock key. The value **true** indicates an activated state, and **false** indicates an inactivated state. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
