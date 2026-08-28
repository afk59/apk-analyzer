# hid\_ddk\_types.h

#### Overview

Defines the enum variables and structs used in the HID DDK.

**File to include**: <hid/hid\_ddk\_types.h>

**Library**: libhid.z.so

**System capability**: SystemCapability.Driver.HID.Extension

**Since**: 11

**Related module**: [HidDdk](../../modules/hidddk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Hid\_EmitItem](../../structs/hid-emititem/document.md) | Hid\_EmitItem | Defines event information. |
| [Hid\_Device](../../structs/hid-device/document.md) | Hid\_Device | Defines basic device information. |
| [Hid\_EventTypeArray](../../structs/hid-eventtypearray/document.md) | Hid\_EventTypeArray | Defines an array of event types. |
| [Hid\_KeyCodeArray](../../structs/hid-keycodearray/document.md) | Hid\_KeyCodeArray | Defines an array of key codes. |
| [Hid\_AbsAxesArray](../../structs/hid-absaxesarray/document.md) | Hid\_AbsAxesArray | Defines an array of absolute coordinates. |
| [Hid\_RelAxesArray](../../structs/hid-relaxesarray/document.md) | Hid\_RelAxesArray | Defines an array of relative coordinates. |
| [Hid\_MscEventArray](../../structs/hid-msceventarray/document.md) | Hid\_MscEventArray | Defines an array of miscellaneous events. |
| [Hid\_EventProperties](../../structs/hid-eventproperties/document.md) | Hid\_EventProperties | Defines the event properties of a device. |
| [Hid\_RawDevInfo](../../structs/hid-rawdevinfo/document.md) | Hid\_RawDevInfo | Defines the raw device information. |
| [Hid\_DeviceHandle](../../structs/hid-devicehandle/document.md) | Hid\_DeviceHandle | Defines the opaque USB HID device structure. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Hid\_DeviceProp](#hid_deviceprop) | Hid\_DeviceProp | Enumerates the properties of input devices. |
| [Hid\_EventType](#hid_eventtype) | Hid\_EventType | Enumerates the event types. |
| [Hid\_SynEvent](#hid_synevent) | Hid\_SynEvent | Enumerates sync events. |
| [Hid\_KeyCode](#hid_keycode) | Hid\_KeyCode | Enumerates the key codes. |
| [Hid\_AbsAxes](#hid_absaxes) | Hid\_AbsAxes | Enumerates the absolute coordinates. |
| [Hid\_RelAxes](#hid_relaxes) | Hid\_RelAxes | Enumerates the relative coordinates. |
| [Hid\_MscEvent](#hid_mscevent) | Hid\_MscEvent | Enumerates miscellaneous input events. |
| [Hid\_DdkErrCode](#hid_ddkerrcode) | Hid\_DdkErrCode | Enumerates the HID DDK error codes. |
| [Hid\_ReportType](#hid_reporttype) | Hid\_ReportType | Defines the report (data packets exchanged between the HID device and the host) type. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| HID\_MAX\_REPORT\_BUFFER\_SIZE (16 \* 1024 - 1) | Defines the maximum size of the report buffer. |

#### Enum Description

#### \[h2\]Hid\_DeviceProp

enum Hid\_DeviceProp

**Description**

Enumerates the properties of input devices.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_PROP\_POINTER = 0x00 | Pointer device. |
| HID\_PROP\_DIRECT = 0x01 | Direct input device. |
| HID\_PROP\_BUTTON\_PAD = 0x02 | Touch device with bottom keys. |
| HID\_PROP\_SEMI\_MT = 0x03 | Full multi-touch device. |
| HID\_PROP\_TOP\_BUTTON\_PAD = 0x04 | Touch device with top soft keys. |
| HID\_PROP\_POINTING\_STICK = 0x05 | Pointing stick. |
| HID\_PROP\_ACCELEROMETER = 0x06 | Accelerometer. |

#### \[h2\]Hid\_EventType

enum Hid\_EventType

**Description**

Enumerates the event types.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_EV\_SYN = 0x00 | Sync event. |
| HID\_EV\_KEY = 0x01 | Key event. |
| HID\_EV\_REL = 0x02 | Relative coordinate event. |
| HID\_EV\_ABS = 0x03 | Absolute coordinate event. |
| HID\_EV\_MSC = 0x04 | Miscellaneous event. |

#### \[h2\]Hid\_SynEvent

enum Hid\_SynEvent

**Description**

Enumerates sync events.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_SYN\_REPORT = 0 | End of an event. |
| HID\_SYN\_CONFIG = 1 | Configuration synchronization. |
| HID\_SYN\_MT\_REPORT = 2 | End of a multi-touch ABS data packet. |
| HID\_SYN\_DROPPED = 3 | Event discarded. |

#### \[h2\]Hid\_KeyCode

enum Hid\_KeyCode

**Description**

Enumerates the key codes.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_KEY\_A = 30 | Key A |
| HID\_KEY\_B = 48 | Key B |
| HID\_KEY\_C = 46 | Key C |
| HID\_KEY\_D = 32 | Key D |
| HID\_KEY\_E = 18 | Key E |
| HID\_KEY\_F = 33 | Key F |
| HID\_KEY\_G = 34 | Key G |
| HID\_KEY\_H = 35 | Key H |
| HID\_KEY\_I = 23 | Key I |
| HID\_KEY\_J = 36 | Key J |
| HID\_KEY\_K = 37 | Key K |
| HID\_KEY\_L = 38 | Key L |
| HID\_KEY\_M = 50 | Key M |
| HID\_KEY\_N = 49 | Key N |
| HID\_KEY\_O = 24 | Key O |
| HID\_KEY\_P = 25 | Key P |
| HID\_KEY\_Q = 16 | Key Q |
| HID\_KEY\_R = 19 | Key R |
| HID\_KEY\_S = 31 | Key S |
| HID\_KEY\_T = 20 | Key T |
| HID\_KEY\_U = 22 | Key U |
| HID\_KEY\_V = 47 | Key V |
| HID\_KEY\_W = 17 | Key W |
| HID\_KEY\_X = 45 | Key X |
| HID\_KEY\_Y = 21 | Key Y |
| HID\_KEY\_Z = 44 | Key Z |
| HID\_KEY\_ESC = 1 | Key Esc |
| HID\_KEY\_0 = 11 | Key 0 |
| HID\_KEY\_1 = 2 | Key 1 |
| HID\_KEY\_2 = 3 | Key 2 |
| HID\_KEY\_3 = 4 | Key 3 |
| HID\_KEY\_4 = 5 | Key 4 |
| HID\_KEY\_5 = 6 | Key 5 |
| HID\_KEY\_6 = 7 | Key 6 |
| HID\_KEY\_7 = 8 | Key 7 |
| HID\_KEY\_8 = 9 | Key 8 |
| HID\_KEY\_9 = 10 | Key 9 |
| HID\_KEY\_GRAVE = 41 | Key grave (\`) |
| HID\_KEY\_MINUS = 12 | Key - |
| HID\_KEY\_EQUALS = 13 | Key = |
| HID\_KEY\_BACKSPACE = 14 | Key Backspace |
| HID\_KEY\_LEFT\_BRACKET = 26 | Key \[ |
| HID\_KEY\_RIGHT\_BRACKET = 27 | Key \] |
| HID\_KEY\_ENTER = 28 | Key Enter |
| HID\_KEY\_LEFT\_SHIFT = 42 | Left Shift |
| HID\_KEY\_BACKSLASH = 43 | Key | |
| HID\_KEY\_SEMICOLON = 39 | Key ; |
| HID\_KEY\_APOSTROPHE = 40 | Key ' |
| HID\_KEY\_SPACE = 57 | Key Space |
| HID\_KEY\_SLASH = 53 | Key / |
| HID\_KEY\_COMMA = 51 | Key comma (,) |
| HID\_KEY\_PERIOD = 52 | Key period (.) |
| HID\_KEY\_RIGHT\_SHIFT = 54 | Right Shift |
| HID\_KEY\_NUMPAD\_0 = 82 | Numeral 0 on the numeric keypad |
| HID\_KEY\_NUMPAD\_1 = 79 | Numeral 1 on the numeric keypad |
| HID\_KEY\_NUMPAD\_2 = 80 | Numeral 2 on the numeric keypad |
| HID\_KEY\_NUMPAD\_3 = 81 | Numeral 3 on the numeric keypad |
| HID\_KEY\_NUMPAD\_4 = 75 | Numeral 4 on the numeric keypad |
| HID\_KEY\_NUMPAD\_5 = 76 | Numeral 5 on the numeric keypad |
| HID\_KEY\_NUMPAD\_6 = 77 | Numeral 6 on the numeric keypad |
| HID\_KEY\_NUMPAD\_7 = 71 | Numeral 7 on the numeric keypad |
| HID\_KEY\_NUMPAD\_8 = 72 | Numeral 8 on the numeric keypad |
| HID\_KEY\_NUMPAD\_9 = 73 | Numeral 9 on the numeric keypad |
| HID\_KEY\_NUMPAD\_DIVIDE = 70 | Slash key (/) on the numeric keypad |
| HID\_KEY\_NUMPAD\_MULTIPLY = 55 | Asterisk key (\*) on the numeric keypad |
| HID\_KEY\_NUMPAD\_SUBTRACT = 74 | Minus key (-) on the numeric keypad |
| HID\_KEY\_NUMPAD\_ADD = 78 | Plus key (+) on the numeric keypad |
| HID\_KEY\_NUMPAD\_DOT = 83 | Decimal point (.) on the numeric keypad |
| HID\_KEY\_SYSRQ = 99 | SYSRQ key |
| HID\_KEY\_DELETE = 111 | Delete key |
| HID\_KEY\_MUTE = 113 | Mute key |
| HID\_KEY\_VOLUME\_DOWN = 114 | Volume Down key |
| HID\_KEY\_VOLUME\_UP = 115 | Volume Up key |
| HID\_KEY\_BRIGHTNESS\_DOWN = 224 | Brightness Down key |
| HID\_KEY\_BRIGHTNESS\_UP = 225 | Brightness Up key |
| HID\_BTN\_0 = 0x100 | Button 0 |
| HID\_BTN\_1 = 0x101 | Button 1 |
| HID\_BTN\_2 = 0x102 | Button 2 |
| HID\_BTN\_3 = 0x103 | Button 3 |
| HID\_BTN\_4 = 0x104 | Button 4 |
| HID\_BTN\_5 = 0x105 | Button 5 |
| HID\_BTN\_6 = 0x106 | Button 6 |
| HID\_BTN\_7 = 0x107 | Button 7 |
| HID\_BTN\_8 = 0x108 | Button 8 |
| HID\_BTN\_9 = 0x109 | Button 9 |
| HID\_BTN\_LEFT = 0x110 | Left mouse button |
| HID\_BTN\_RIGHT = 0x111 | Right mouse button |
| HID\_BTN\_MIDDLE = 0x112 | Middle mouse button |
| HID\_BTN\_SIDE = 0x113 | Side mouse button |
| HID\_BTN\_EXTRA = 0x114 | Extra mouse button |
| HID\_BTN\_FORWARD = 0x115 | Mouse forward button |
| HID\_BTN\_BACKWARD = 0x116 | Mouse backward button |
| HID\_BTN\_TASK = 0x117 | Mouse task button |
| HID\_BTN\_TOOL\_PEN = 0x140 | Pen |
| HID\_BTN\_TOOL\_RUBBER = 0x141 | Eraser |
| HID\_BTN\_TOOL\_BRUSH = 0x142 | Brush |
| HID\_BTN\_TOOL\_PENCIL = 0x143 | Pencil |
| HID\_BTN\_TOOL\_AIRBRUSH = 0x144 | Air brush |
| HID\_BTN\_TOOL\_FINGER = 0x145 | Finger |
| HID\_BTN\_TOOL\_MOUSE = 0x146 | Mouse |
| HID\_BTN\_TOOL\_LENS = 0x147 | Lens |
| HID\_BTN\_TOOL\_QUINT\_TAP = 0x148 | Five-finger touch |
| HID\_BTN\_STYLUS3 = 0x149 | Stylus 3 |
| HID\_BTN\_TOUCH = 0x14a | Touch |
| HID\_BTN\_STYLUS = 0x14b | Stylus |
| HID\_BTN\_STYLUS2 = 0x14c | Stylus 2 |
| HID\_BTN\_TOOL\_DOUBLE\_TAP = 0x14d | Two-finger touch |
| HID\_BTN\_TOOL\_TRIPLE\_TAP = 0x14e | Three-finger touch |
| HID\_BTN\_TOOL\_QUAD\_TAP = 0x14f | Four-finger touch |
| HID\_BTN\_WHEEL = 0x150 | Scroll wheel |

#### \[h2\]Hid\_AbsAxes

enum Hid\_AbsAxes

**Description**

Enumerates the absolute coordinates.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_ABS\_X = 0x00 | X axis |
| HID\_ABS\_Y = 0x01 | Y axis |
| HID\_ABS\_Z = 0x02 | Z axis |
| HID\_ABS\_RX = 0x03 | X axis of the right analog stick |
| HID\_ABS\_RY = 0x04 | Y axis of the right analog stick |
| HID\_ABS\_RZ = 0x05 | Z axis of the right analog stick |
| HID\_ABS\_THROTTLE = 0x06 | Throttle |
| HID\_ABS\_RUDDER = 0x07 | Rudder |
| HID\_ABS\_WHEEL = 0x08 | Scroll wheel |
| HID\_ABS\_GAS = 0x09 | Gas |
| HID\_ABS\_BRAKE = 0x0a | Brake |
| HID\_ABS\_HAT0X = 0x10 | HAT0X |
| HID\_ABS\_HAT0Y = 0x11 | HAT0Y |
| HID\_ABS\_HAT1X = 0x12 | HAT1X |
| HID\_ABS\_HAT1Y = 0x13 | HAT1Y |
| HID\_ABS\_HAT2X = 0x14 | HAT2X |
| HID\_ABS\_HAT2Y = 0x15 | HAT2Y |
| HID\_ABS\_HAT3X = 0x16 | HAT3X |
| HID\_ABS\_HAT3Y = 0x17 | HAT3Y |
| HID\_ABS\_PRESSURE = 0x18 | Pressure |
| HID\_ABS\_DISTANCE = 0x19 | Distance |
| HID\_ABS\_TILT\_X = 0x1a | Tilt of X axis |
| HID\_ABS\_TILT\_Y = 0x1b | Tilt of Y axis |
| HID\_ABS\_TOOL\_WIDTH = 0x1c | Width of the touch tool |
| HID\_ABS\_VOLUME = 0x20 | Volume |
| HID\_ABS\_MISC = 0x28 | Others |

#### \[h2\]Hid\_RelAxes

enum Hid\_RelAxes

**Description**

Enumerates the relative coordinates.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_REL\_X = 0x00 | X axis |
| HID\_REL\_Y = 0x01 | Y axis |
| HID\_REL\_Z = 0x02 | Z axis |
| HID\_REL\_RX = 0x03 | X axis of the right analog stick |
| HID\_REL\_RY = 0x04 | Y axis of the right analog stick |
| HID\_REL\_RZ = 0x05 | Z axis of the right analog stick |
| HID\_REL\_HWHEEL = 0x06 | Horizontal scroll wheel |
| HID\_REL\_DIAL = 0x07 | Scale |
| HID\_REL\_WHEEL = 0x08 | Scroll wheel |
| HID\_REL\_MISC = 0x09 | Others |
| HID\_REL\_RESERVED = 0x0a | Reserved |
| HID\_REL\_WHEEL\_HI\_RES = 0x0b | High-resolution scroll wheel |
| HID\_REL\_HWHEEL\_HI\_RES = 0x0c | High-resolution horizontal scroll wheel |

#### \[h2\]Hid\_MscEvent

enum Hid\_MscEvent

**Description**

Enumerates miscellaneous input events.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_MSC\_SERIAL = 0x00 | Serial number |
| HID\_MSC\_PULSE\_LED = 0x01 | Pulse |
| HID\_MSC\_GESTURE = 0x02 | Gesture |
| HID\_MSC\_RAW = 0x03 | Start event |
| HID\_MSC\_SCAN = 0x04 | Scan |
| HID\_MSC\_TIMESTAMP = 0x05 | Timestamp |

#### \[h2\]Hid\_DdkErrCode

enum Hid\_DdkErrCode

**Description**

Enumerates the HID DDK error codes.

**Since**: 11

| Enum | Description |
| :-- | :-- |
| HID\_DDK\_SUCCESS = 0 | Operation success. |
| HID\_DDK\_NO\_PERM = 201 | No permission. The value is changed from **\-6** to **201** since API version 16. |
| HID\_DDK\_INVALID\_PARAMETER = 401 | Invalid parameter. The value is changed from **\-2** to **401** since API version 16. |
| HID\_DDK\_FAILURE = 27300001 | Operation failed. The value is changed from **\-1** to **27300001** since API version 16. |
| HID\_DDK\_NULL\_PTR = 27300002 | Null pointer. The value is changed from **\-4** to **27300002** since API version 16. |
| HID\_DDK\_INVALID\_OPERATION = 27300003 | Invalid operation. The value is changed from **\-3** to **27300003** since API version 16. |
| HID\_DDK\_TIMEOUT = 27300004 | Timeout. The value is changed from **\-5** to **27300004** since API version 16. |
| HID\_DDK\_INIT\_ERROR = 27300005 | 
DDK initialization error.

**Since**: 18

 |
| HID\_DDK\_SERVICE\_ERROR = 27300006 | 

Service communication error.

**Since**: 18

 |
| HID\_DDK\_MEMORY\_ERROR = 27300007 | 

Memory errors, such as memory data copy failure and memory allocation failure.

**Since**: 18

 |
| HID\_DDK\_IO\_ERROR = 27300008 | 

I/O operation error.

**Since**: 18

 |
| HID\_DDK\_DEVICE\_NOT\_FOUND = 27300009 | 

Device not found.

**Since**: 18

 |

#### \[h2\]Hid\_ReportType

enum Hid\_ReportType

**Description**

Defines the report (data packets exchanged between the HID device and the host) type.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| HID\_INPUT\_REPORT = 0 | Input report. |
| HID\_OUTPUT\_REPORT = 1 | Output report. |
| HID\_FEATURE\_REPORT = 2 | Feature report. |

#### \[h2\]HID\_MAX\_REPORT\_BUFFER\_SIZE

HID\_MAX\_REPORT\_BUFFER\_SIZE (16 \* 1024 - 1)

**Description**

Defines the maximum size of the report buffer.

**Since**: 18
