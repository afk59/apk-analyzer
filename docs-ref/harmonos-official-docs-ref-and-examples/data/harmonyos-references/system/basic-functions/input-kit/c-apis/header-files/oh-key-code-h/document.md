# oh\_key\_code.h

#### Overview

Defines key codes of the key device.

**File to include**: <multimodalinput/oh\_key\_code.h>

**Library**: libohinput.so

**System capability**: SystemCapability.MultimodalInput.Input.Core

**Since**: 12

**Related module**: [input](../../modules/input/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Input\_KeyCode](#input_keycode) | Input\_KeyCode | Key code. |

#### Enum Description

#### \[h2\]Input\_KeyCode

enum Input\_KeyCode

**Description**

Enumerates the key codes.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| KEYCODE\_UNKNOWN = -1 | Unknown key |
| KEYCODE\_FN = 0 | Function (Fn) key |
| KEYCODE\_HOME = 1 | 
Function (Home) key

**Since**: 22

 |
| KEYCODE\_BACK = 2 | 

Back button

**Since**: 22

 |
| KEYCODE\_SEARCH = 9 | 

Search key

**Since**: 22

 |
| KEYCODE\_MEDIA\_PLAY\_PAUSE = 10 | 

Media: Play/Pause key

**Since**: 22

Difference between this key and **KEYCODE\_PLAYPAUSE**:

**KEYCODE\_PLAYPAUSE** is an earlier definition, while **KEYCODE\_MEDIA\_PLAY\_PAUSE** is designed for modern media key devices.

 |
| KEYCODE\_MEDIA\_STOP = 11 | 

Media: Stop Key

**Since**: 22

 |
| KEYCODE\_MEDIA\_NEXT = 12 | 

Media: Next key

**Since**: 22

 |
| KEYCODE\_MEDIA\_PREVIOUS = 13 | 

Media: Previous key

**Since**: 22

 |
| KEYCODE\_MEDIA\_REWIND = 14 | 

Media: Rewind key

**Since**: 22

 |
| KEYCODE\_MEDIA\_FAST\_FORWARD = 15 | 

Media: Fast Forward key

**Since**: 22

 |
| KEYCODE\_VOLUME\_UP = 16 | Volume Up key |
| KEYCODE\_VOLUME\_DOWN = 17 | Volume Down key |
| KEYCODE\_POWER = 18 | Power key |
| KEYCODE\_CAMERA = 19 | Camera key |
| KEYCODE\_VOLUME\_MUTE = 22 | Speaker Mute key |
| KEYCODE\_MUTE = 23 | Mute key |
| KEYCODE\_BRIGHTNESS\_UP = 40 | Brightness Up key |
| KEYCODE\_BRIGHTNESS\_DOWN = 41 | Brightness Down key |
| KEYCODE\_0 = 2000 | Key 0 |
| KEYCODE\_1 = 2001 | Key 1 |
| KEYCODE\_2 = 2002 | Key 2 |
| KEYCODE\_3 = 2003 | Key 3 |
| KEYCODE\_4 = 2004 | Key 4 |
| KEYCODE\_5 = 2005 | Key 5 |
| KEYCODE\_6 = 2006 | Key 6 |
| KEYCODE\_7 = 2007 | Key 7 |
| KEYCODE\_8 = 2008 | Key 8 |
| KEYCODE\_9 = 2009 | Key 9 |
| KEYCODE\_STAR = 2010 | Key \* |
| KEYCODE\_POUND = 2011 | Key # |
| KEYCODE\_DPAD\_UP = 2012 | Up key on D-pad |
| KEYCODE\_DPAD\_DOWN = 2013 | Down key on D-pad |
| KEYCODE\_DPAD\_LEFT = 2014 | Left key on D-pad |
| KEYCODE\_DPAD\_RIGHT = 2015 | Right key on D-pad |
| KEYCODE\_DPAD\_CENTER = 2016 | Center key on D-pad |
| KEYCODE\_A = 2017 | Key A |
| KEYCODE\_B = 2018 | Key B |
| KEYCODE\_C = 2019 | Key C |
| KEYCODE\_D = 2020 | Key D |
| KEYCODE\_E = 2021 | Key E |
| KEYCODE\_F = 2022 | Key F |
| KEYCODE\_G = 2023 | Key G |
| KEYCODE\_H = 2024 | Key H |
| KEYCODE\_I = 2025 | Key I |
| KEYCODE\_J = 2026 | Key J |
| KEYCODE\_K = 2027 | Key K |
| KEYCODE\_L = 2028 | Key L |
| KEYCODE\_M = 2029 | Key M |
| KEYCODE\_N = 2030 | Key N |
| KEYCODE\_O = 2031 | Key O |
| KEYCODE\_P = 2032 | Key P |
| KEYCODE\_Q = 2033 | Key Q |
| KEYCODE\_R = 2034 | Key R |
| KEYCODE\_S = 2035 | Key S |
| KEYCODE\_T = 2036 | Key T |
| KEYCODE\_U = 2037 | Key U |
| KEYCODE\_V = 2038 | Key V |
| KEYCODE\_W = 2039 | Key W |
| KEYCODE\_X = 2040 | Key X |
| KEYCODE\_Y = 2041 | Key Y |
| KEYCODE\_Z = 2042 | Key Z |
| KEYCODE\_COMMA = 2043 | Key , |
| KEYCODE\_PERIOD = 2044 | Key . |
| KEYCODE\_ALT\_LEFT = 2045 | Left Alt key |
| KEYCODE\_ALT\_RIGHT = 2046 | Right Alt key |
| KEYCODE\_SHIFT\_LEFT = 2047 | Left Shift key |
| KEYCODE\_SHIFT\_RIGHT = 2048 | Right Shift key |
| KEYCODE\_TAB = 2049 | Tab key |
| KEYCODE\_SPACE = 2050 | Space key |
| KEYCODE\_SYM = 2051 | Symbol key |
| KEYCODE\_EXPLORER = 2052 | Explorer key, used to start the explorer application |
| KEYCODE\_ENVELOPE = 2053 | Email key, used to start the email application |
| KEYCODE\_ENTER = 2054 | Enter key |
| KEYCODE\_DEL = 2055 | Delete key |
| KEYCODE\_GRAVE = 2056 | Key \` |
| KEYCODE\_MINUS = 2057 | Key - |
| KEYCODE\_EQUALS = 2058 | Key = |
| KEYCODE\_LEFT\_BRACKET = 2059 | Key \[ |
| KEYCODE\_RIGHT\_BRACKET = 2060 | Key \] |
| KEYCODE\_BACKSLASH = 2061 | Key \\ |
| KEYCODE\_SEMICOLON = 2062 | Key ; |
| KEYCODE\_APOSTROPHE = 2063 | Key ' |
| KEYCODE\_SLASH = 2064 | Key / |
| KEYCODE\_AT = 2065 | Key @ |
| KEYCODE\_PLUS = 2066 | Key + |
| KEYCODE\_MENU = 2067 | Menu key |
| KEYCODE\_PAGE\_UP = 2068 | Page Up key |
| KEYCODE\_PAGE\_DOWN = 2069 | Page Down key |
| KEYCODE\_ESCAPE = 2070 | Esc key |
| KEYCODE\_FORWARD\_DEL = 2071 | Forward Delete key |
| KEYCODE\_CTRL\_LEFT = 2072 | Left Ctrl key |
| KEYCODE\_CTRL\_RIGHT = 2073 | Right Ctrl key |
| KEYCODE\_CAPS\_LOCK = 2074 | Caps Lock key |
| KEYCODE\_SCROLL\_LOCK = 2075 | Scroll Lock key |
| KEYCODE\_META\_LEFT = 2076 | Left Meta key |
| KEYCODE\_META\_RIGHT = 2077 | Right Meta key |
| KEYCODE\_FUNCTION = 2078 | Function key |
| KEYCODE\_SYSRQ = 2079 | System Request/Print Screen key |
| KEYCODE\_BREAK = 2080 | Break/Pause key |
| KEYCODE\_MOVE\_HOME = 2081 | Move to Home key |
| KEYCODE\_MOVE\_END = 2082 | Move to End key |
| KEYCODE\_INSERT = 2083 | Insert key |
| KEYCODE\_FORWARD = 2084 | Forward key |
| KEYCODE\_MEDIA\_PLAY = 2085 | Media: Play key |
| KEYCODE\_MEDIA\_PAUSE = 2086 | Media: Pause key |
| KEYCODE\_MEDIA\_CLOSE = 2087 | Media: Close key |
| KEYCODE\_MEDIA\_EJECT = 2088 | Media: Reject key |
| KEYCODE\_MEDIA\_RECORD = 2089 | Media: Record key |
| KEYCODE\_F1 = 2090 | F1 key |
| KEYCODE\_F2 = 2091 | F2 key |
| KEYCODE\_F3 = 2092 | F3 key |
| KEYCODE\_F4 = 2093 | F4 key |
| KEYCODE\_F5 = 2094 | F5 key |
| KEYCODE\_F6 = 2095 | F6 key |
| KEYCODE\_F7 = 2096 | F7 key |
| KEYCODE\_F8 = 2097 | F8 key |
| KEYCODE\_F9 = 2098 | F9 key |
| KEYCODE\_F10 = 2099 | F10 key |
| KEYCODE\_F11 = 2100 | F11 key |
| KEYCODE\_F12 = 2101 | F12 key |
| KEYCODE\_NUM\_LOCK = 2102 | Number Lock key |
| KEYCODE\_NUMPAD\_0 = 2103 | Key 0 on numeric keypad |
| KEYCODE\_NUMPAD\_1 = 2104 | Key 1 on numeric keypad |
| KEYCODE\_NUMPAD\_2 = 2105 | Key 2 on numeric keypad |
| KEYCODE\_NUMPAD\_3 = 2106 | Key 3 on numeric keypad |
| KEYCODE\_NUMPAD\_4 = 2107 | Key 4 on numeric keypad |
| KEYCODE\_NUMPAD\_5 = 2108 | Key 5 on numeric keypad |
| KEYCODE\_NUMPAD\_6 = 2109 | Key 6 on numeric keypad |
| KEYCODE\_NUMPAD\_7 = 2110 | Key 7 on numeric keypad |
| KEYCODE\_NUMPAD\_8 = 2111 | Key 8 on numeric keypad |
| KEYCODE\_NUMPAD\_9 = 2112 | Key 9 on numeric keypad |
| KEYCODE\_NUMPAD\_DIVIDE = 2113 | Key / on numeric keypad |
| KEYCODE\_NUMPAD\_MULTIPLY = 2114 | Key \* on numeric keypad |
| KEYCODE\_NUMPAD\_SUBTRACT = 2115 | Key - on numeric keypad |
| KEYCODE\_NUMPAD\_ADD = 2116 | Key + on numeric keypad |
| KEYCODE\_NUMPAD\_DOT = 2117 | Key . on numeric keypad |
| KEYCODE\_NUMPAD\_COMMA = 2118 | Key , on numeric keypad |
| KEYCODE\_NUMPAD\_ENTER = 2119 | Enter key on numeric keypad |
| KEYCODE\_NUMPAD\_EQUALS = 2120 | Key = on numeric keypad |
| KEYCODE\_NUMPAD\_LEFT\_PAREN = 2121 | Key ( on numeric keypad |
| KEYCODE\_NUMPAD\_RIGHT\_PAREN = 2122 | Key ) on numeric keypad |
| KEYCODE\_VIRTUAL\_MULTITASK = 2210 | 

Multi-task key

**Since**: 22

 |
| KEYCODE\_BUTTON\_A = 2301 | 

Joystick key A

**Since**: 22

 |
| KEYCODE\_BUTTON\_B = 2302 | 

Joystick key B

**Since**: 22

 |
| KEYCODE\_BUTTON\_X = 2304 | 

Joystick key X

**Since**: 22

 |
| KEYCODE\_BUTTON\_Y = 2305 | 

Joystick key Y

**Since**: 22

 |
| KEYCODE\_BUTTON\_L1 = 2307 | 

Joystick key L1

**Since**: 22

 |
| KEYCODE\_BUTTON\_R1 = 2308 | 

Joystick key R1

**Since**: 22

 |
| KEYCODE\_BUTTON\_L2 = 2309 | 

Joystick key L2

**Since**: 22

 |
| KEYCODE\_BUTTON\_R2 = 2310 | 

Joystick key R2

**Since**: 22

 |
| KEYCODE\_BUTTON\_SELECT = 2311 | 

Joystick key Select

**Since**: 22

 |
| KEYCODE\_BUTTON\_START = 2312 | 

Joystick key Start

**Since**: 22

 |
| KEYCODE\_BUTTON\_MODE = 2313 | 

Joystick key Mode

**Since**: 22

 |
| KEYCODE\_BUTTON\_THUMBL = 2314 | 

Joystick key THUMBL

**Since**: 22

 |
| KEYCODE\_BUTTON\_THUMBR = 2315 | 

Joystick key THUMBR

**Since**: 22

 |
| KEYCODE\_SLEEP = 2600 | 

Sleep key

**Since**: 22

 |
| KEYCODE\_ZENKAKU\_HANKAKU = 2601 | 

Zenkaku/Hankaku key

**Since**: 22

 |
| KEYCODE\_102ND = 2602 | 

International Keyboard Extension key

**Since**: 22

 |
| KEYCODE\_RO = 2603 | 

Ro key

**Since**: 22

 |
| KEYCODE\_KATAKANA = 2604 | 

Katakana key

**Since**: 22

 |
| KEYCODE\_HIRAGANA = 2605 | 

Hiragana key

**Since**: 22

 |
| KEYCODE\_HENKAN = 2606 | 

Henkan key

**Since**: 22

 |
| KEYCODE\_KATAKANA\_HIRAGANA = 2607 | 

Katakana/Hiragana key

**Since**: 22

 |
| KEYCODE\_MUHENKAN = 2608 | 

Muhenkan key

**Since**: 22

 |
| KEYCODE\_LINEFEED = 2609 | 

Linefeed key

**Since**: 22

 |
| KEYCODE\_MACRO = 2610 | 

Macro key

**Since**: 22

 |
| KEYCODE\_NUMPAD\_PLUSMINUS = 2611 | 

Plus/Minus key on the numeric keypad

**Since**: 22

 |
| KEYCODE\_SCALE = 2612 | 

Scale key

**Since**: 22

 |
| KEYCODE\_HANGUEL = 2613 | 

Hanguel key

**Since**: 22

 |
| KEYCODE\_HANJA = 2614 | 

Hanja key

**Since**: 22

 |
| KEYCODE\_YEN = 2615 | 

Yen key

**Since**: 22

 |
| KEYCODE\_STOP = 2616 | 

Stop key

**Since**: 22

 |
| KEYCODE\_AGAIN = 2617 | 

Again key

**Since**: 22

 |
| KEYCODE\_PROPS = 2618 | 

Props key

**Since**: 22

 |
| KEYCODE\_UNDO = 2619 | 

Undo key

**Since**: 22

 |
| KEYCODE\_COPY = 2620 | 

Copy key

**Since**: 22

 |
| KEYCODE\_OPEN = 2621 | 

Open key

**Since**: 22

 |
| KEYCODE\_PASTE = 2622 | 

Paste key

**Since**: 22

 |
| KEYCODE\_FIND = 2623 | 

Find key

**Since**: 22

 |
| KEYCODE\_CUT = 2624 | 

Cut key

**Since**: 22

 |
| KEYCODE\_HELP = 2625 | 

Help key

**Since**: 22

 |
| KEYCODE\_CALC = 2626 | 

Calc key, which is used to start the calculator application

**Since**: 22

 |
| KEYCODE\_FILE = 2627 | 

File key

**Since**: 22

 |
| KEYCODE\_BOOKMARKS = 2628 | 

Bookmarks key

**Since**: 22

 |
| KEYCODE\_NEXT = 2629 | 

Page Down key

**Since**: 22

 |
| KEYCODE\_PLAYPAUSE = 2630 | 

Media: Play/Pause key

**Since**: 22

Difference between this key and **KEYCODE\_MEDIA\_PLAY\_PAUSE**:

**KEYCODE\_PLAYPAUSE** is an earlier definition, while **KEYCODE\_MEDIA\_PLAY\_PAUSE** is designed for modern media key devices.

 |
| KEYCODE\_PREVIOUS = 2631 | 

Page Up key

**Since**: 22

 |
| KEYCODE\_STOPCD = 2632 | 

Stop CD key

**Since**: 22

 |
| KEYCODE\_CONFIG = 2634 | 

Configuration key

**Since**: 22

 |
| KEYCODE\_REFRESH = 2635 | 

Refresh key

**Since**: 22

 |
| KEYCODE\_EXIT = 2636 | 

Exit key

**Since**: 22

 |
| KEYCODE\_EDIT = 2637 | 

Edit key

**Since**: 22

 |
| KEYCODE\_SCROLLUP = 2638 | 

Scroll Up key

**Since**: 22

 |
| KEYCODE\_SCROLLDOWN = 2639 | 

Scroll Down key

**Since**: 22

 |
| KEYCODE\_NEW = 2640 | 

New key

**Since**: 22

 |
| KEYCODE\_REDO = 2641 | 

Redo key

**Since**: 22

 |
| KEYCODE\_CLOSE = 2642 | 

Close key

**Since**: 22

 |
| KEYCODE\_PLAY = 2643 | 

Play key

**Since**: 22

 |
| KEYCODE\_BASSBOOST = 2644 | 

Bass Boost key

**Since**: 22

 |
| KEYCODE\_PRINT = 2645 | 

Print key

**Since**: 22

 |
| KEYCODE\_CHAT = 2646 | 

Chat key

**Since**: 22

 |
| KEYCODE\_FINANCE = 2647 | 

Finance key

**Since**: 22

 |
| KEYCODE\_CANCEL = 2648 | 

Cancel key

**Since**: 22

 |
| KEYCODE\_KBDILLUM\_TOGGLE = 2649 | 

Keyboard Illumination Toggle key

**Since**: 22

 |
| KEYCODE\_KBDILLUM\_DOWN = 2650 | 

Keyboard Illumination Down key

**Since**: 22

 |
| KEYCODE\_KBDILLUM\_UP = 2651 | 

Keyboard Illumination Up key

**Since**: 22

 |
| KEYCODE\_SEND = 2652 | 

Send key

**Since**: 22

 |
| KEYCODE\_REPLY = 2653 | 

Reply key

**Since**: 22

 |
| KEYCODE\_FORWARDMAIL = 2654 | 

Forward Mail key

**Since**: 22

 |
| KEYCODE\_SAVE = 2655 | 

Save key

**Since**: 22

 |
| KEYCODE\_DOCUMENTS = 2656 | 

Documents key

**Since**: 22

 |
| KEYCODE\_VIDEO\_NEXT = 2657 | 

Next Video key

**Since**: 22

 |
| KEYCODE\_VIDEO\_PREV = 2658 | 

Previous Video key

**Since**: 22

 |
| KEYCODE\_BRIGHTNESS\_CYCLE = 2659 | 

Brightness Cycle key

**Since**: 22

 |
| KEYCODE\_BRIGHTNESS\_ZERO = 2660 | 

Brightness Zero key

**Since**: 22

 |
| KEYCODE\_DISPLAY\_OFF = 2661 | 

Display Off Key

**Since**: 22

 |
| KEYCODE\_BTN\_MISC = 2662 | 

Misc Button key

**Since**: 22

 |
| KEYCODE\_GOTO = 2663 | 

Goto key

**Since**: 22

 |
| KEYCODE\_INFO = 2664 | 

Info key

**Since**: 22

 |
| KEYCODE\_PROGRAM = 2665 | 

Program key

**Since**: 22

 |
| KEYCODE\_PVR = 2666 | 

PVR key

**Since**: 22

 |
| KEYCODE\_SUBTITLE = 2667 | 

Subtitle key

**Since**: 22

 |
| KEYCODE\_FULL\_SCREEN = 2668 | 

Full Screen key

**Since**: 22

 |
| KEYCODE\_KEYBOARD = 2669 | 

Keyboard

**Since**: 22

 |
| KEYCODE\_ASPECT\_RATIO = 2670 | 

Aspect Ratio key

**Since**: 22

 |
| KEYCODE\_PC = 2671 | 

Port Control key

**Since**: 22

 |
| KEYCODE\_TV = 2672 | 

TV key

**Since**: 22

 |
| KEYCODE\_TV2 = 2673 | 

TV key 2

**Since**: 22

 |
| KEYCODE\_VCR = 2674 | 

VCR key

**Since**: 22

 |
| KEYCODE\_VCR2 = 2675 | 

VCR key 2

**Since**: 22

 |
| KEYCODE\_SAT = 2676 | 

SAT key

**Since**: 22

 |
| KEYCODE\_CD = 2677 | 

CD key

**Since**: 22

 |
| KEYCODE\_TAPE = 2678 | 

Tape key

**Since**: 22

 |
| KEYCODE\_TUNER = 2679 | 

Tuner key

**Since**: 22

 |
| KEYCODE\_PLAYER = 2680 | 

Player key

**Since**: 22

 |
| KEYCODE\_DVD = 2681 | 

DVD key

**Since**: 22

 |
| KEYCODE\_AUDIO = 2682 | 

Audio key

**Since**: 22

 |
| KEYCODE\_VIDEO = 2683 | 

Video key

**Since**: 22

 |
| KEYCODE\_MEMO = 2684 | 

Memo key

**Since**: 22

 |
| KEYCODE\_CALENDAR = 2685 | 

Calendar key

**Since**: 22

 |
| KEYCODE\_RED = 2686 | 

Red indicator

**Since**: 22

 |
| KEYCODE\_GREEN = 2687 | 

Green indicator

**Since**: 22

 |
| KEYCODE\_YELLOW = 2688 | 

Yellow indicator

**Since**: 22

 |
| KEYCODE\_BLUE = 2689 | 

Blue indicator

**Since**: 22

 |
| KEYCODE\_CHANNELUP = 2690 | 

Channel Up key

**Since**: 22

 |
| KEYCODE\_CHANNELDOWN = 2691 | 

Channel Down key

**Since**: 22

 |
| KEYCODE\_LAST = 2692 | 

Last key

**Since**: 22

 |
| KEYCODE\_RESTART = 2693 | 

Restart key

**Since**: 22

 |
| KEYCODE\_SLOW = 2694 | 

Slow key

**Since**: 22

 |
| KEYCODE\_SHUFFLE = 2695 | 

Shuffle key

**Since**: 22

 |
| KEYCODE\_VIDEOPHONE = 2696 | 

Videophone key

**Since**: 22

 |
| KEYCODE\_GAMES = 2697 | 

Games key

**Since**: 22

 |
| KEYCODE\_ZOOMIN = 2698 | 

Zoom In key

**Since**: 22

 |
| KEYCODE\_ZOOMOUT = 2699 | 

Zoom Out key

**Since**: 22

 |
| KEYCODE\_ZOOMRESET = 2700 | 

Zoom Reset key

**Since**: 22

 |
| KEYCODE\_WORDPROCESSOR = 2701 | 

Word Processor key

**Since**: 22

 |
| KEYCODE\_EDITOR = 2702 | 

Editor key

**Since**: 22

 |
| KEYCODE\_SPREADSHEET = 2703 | 

Spreadsheet key

**Since**: 22

 |
| KEYCODE\_GRAPHICSEDITOR = 2704 | 

Graphics Editor key

**Since**: 22

 |
| KEYCODE\_PRESENTATION = 2705 | 

Presentation key

**Since**: 22

 |
| KEYCODE\_DATABASE = 2706 | 

Database key

**Since**: 22

 |
| KEYCODE\_NEWS = 2707 | 

News key

**Since**: 22

 |
| KEYCODE\_VOICEMAIL = 2708 | 

Voice mailbox

**Since**: 22

 |
| KEYCODE\_ADDRESSBOOK = 2709 | 

Address book key

**Since**: 22

 |
| KEYCODE\_MESSENGER = 2710 | 

Messenger key

**Since**: 22

 |
| KEYCODE\_BRIGHTNESS\_TOGGLE = 2711 | 

Brightness Toggle key

**Since**: 22

 |
| KEYCODE\_SPELLCHECK = 2712 | 

Spell Check key

**Since**: 22

 |
| KEYCODE\_COFFEE = 2713 | 

Coffee key, which is used to launch screen lock or screen saver

**Since**: 22

 |
| KEYCODE\_MEDIA\_REPEAT = 2714 | 

Media Repeat key

**Since**: 22

 |
| KEYCODE\_IMAGES = 2715 | 

Images key

**Since**: 22

 |
| KEYCODE\_BUTTONCONFIG = 2716 | 

Button Configuration key

**Since**: 22

 |
| KEYCODE\_TASKMANAGER = 2717 | 

Task Manager

**Since**: 22

 |
| KEYCODE\_JOURNAL = 2718 | 

Log key

**Since**: 22

 |
| KEYCODE\_CONTROLPANEL = 2719 | 

Control Panel key

**Since**: 22

 |
| KEYCODE\_APPSELECT = 2720 | 

App Select key

**Since**: 22

 |
| KEYCODE\_SCREENSAVER = 2721 | 

Screen Saver key

**Since**: 22

 |
| KEYCODE\_ASSISTANT = 2722 | 

Assistant key

**Since**: 22

 |
| KEYCODE\_KBD\_LAYOUT\_NEXT = 2723 | 

Next Keyboard Layout key

**Since**: 22

 |
| KEYCODE\_BRIGHTNESS\_MIN = 2724 | 

Min Brightness key

**Since**: 22

 |
| KEYCODE\_BRIGHTNESS\_MAX = 2725 | 

Max Brightness key

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_PREV = 2726 | 

Assist\_Previous key, used to view historical inputs

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_NEXT = 2727 | 

Assist\_Next key, used to view predictive inputs

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_PREVGROUP = 2728 | 

Assist\_Previous\_Group key, used to switch to the previous input method in the input group

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_NEXTGROUP = 2729 | 

Assist\_Next\_Group key, used to switch to the next input method in the input group

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_ACCEPT = 2730 | 

Keyboard Input-assisted Accept key

**Since**: 22

 |
| KEYCODE\_KBDINPUTASSIST\_CANCEL = 2731 | 

Keyboard Input-assisted Cancel key

**Since**: 22

 |
| KEYCODE\_FRONT = 2800 | 

Front key, which is used to launch the windshield defogger

**Since**: 22

 |
| KEYCODE\_SETUP = 2801 | 

Setup key

**Since**: 22

 |
| KEYCODE\_WAKEUP = 2802 | 

Wakeup key

**Since**: 22

 |
| KEYCODE\_SENDFILE = 2803 | 

Send File key

**Since**: 22

 |
| KEYCODE\_DELETEFILE = 2804 | 

Delete File key

**Since**: 22

 |
| KEYCODE\_XFER = 2805 | 

XFER key, which is used to start file transfer

**Since**: 22

 |
| KEYCODE\_PROG1 = 2806 | 

Program key 1

**Since**: 22

 |
| KEYCODE\_PROG2 = 2807 | 

Program key 2

**Since**: 22

 |
| KEYCODE\_MSDOS = 2808 | 

DOS key

**Since**: 22

 |
| KEYCODE\_SCREENLOCK = 2809 | 

Screen Lock key

**Since**: 22

 |
| KEYCODE\_DIRECTION\_ROTATE\_DISPLAY = 2810 | 

Directional Rotation Display key

**Since**: 22

 |
| KEYCODE\_CYCLEWINDOWS = 2811 | 

Window Cycle key

**Since**: 22

 |
| KEYCODE\_COMPUTER = 2812 | 

Computer key

**Since**: 22

 |
| KEYCODE\_EJECTCLOSECD = 2813 | 

Eject CD key

**Since**: 22

 |
| KEYCODE\_ISO = 2814 | 

ISO key

**Since**: 22

 |
| KEYCODE\_MOVE = 2815 | 

Move key

**Since**: 22

 |
| KEYCODE\_F13 = 2816 | 

F13 key

**Since**: 22

 |
| KEYCODE\_F14 = 2817 | 

F14 key

**Since**: 22

 |
| KEYCODE\_F15 = 2818 | 

F15 key

**Since**: 22

 |
| KEYCODE\_F16 = 2819 | 

F16 key

**Since**: 22

 |
| KEYCODE\_F17 = 2820 | 

F17 key

**Since**: 22

 |
| KEYCODE\_F18 = 2821 | 

F18 key

**Since**: 22

 |
| KEYCODE\_F19 = 2822 | 

F19 key

**Since**: 22

 |
| KEYCODE\_F20 = 2823 | 

F20 key

**Since**: 22

 |
| KEYCODE\_F21 = 2824 | 

F21 key

**Since**: 22

 |
| KEYCODE\_F22 = 2825 | 

F22 key

**Since**: 22

 |
| KEYCODE\_F23 = 2826 | 

F23 key

**Since**: 22

 |
| KEYCODE\_F24 = 2827 | 

F24 key

**Since**: 22

 |
| KEYCODE\_PROG3 = 2828 | 

Program key 3

**Since**: 22

 |
| KEYCODE\_PROG4 = 2829 | 

Program key 4

**Since**: 22

 |
| KEYCODE\_DASHBOARD = 2830 | 

Dashboard

**Since**: 22

 |
| KEYCODE\_SUSPEND = 2831 | 

Suspend key

**Since**: 22

 |
| KEYCODE\_HP = 2832 | 

HP key

**Since**: 22

 |
| KEYCODE\_SOUND = 2833 | 

Sound key

**Since**: 22

 |
| KEYCODE\_QUESTION = 2834 | 

Question key

**Since**: 22

 |
| KEYCODE\_CONNECT = 2836 | 

Connect key

**Since**: 22

 |
| KEYCODE\_SPORT = 2837 | 

Sport key

**Since**: 22

 |
| KEYCODE\_SHOP = 2838 | 

Shop key

**Since**: 22

 |
| KEYCODE\_ALTERASE = 2839 | 

Alternate key

**Since**: 22

 |
| KEYCODE\_SWITCHVIDEOMODE = 2841 | 

Switch Video Mode key (monitor, LCD, and TV, etc.)

**Since**: 22

 |
| KEYCODE\_BATTERY = 2842 | 

Battery key

**Since**: 22

 |
| KEYCODE\_BLUETOOTH = 2843 | 

Bluetooth key

**Since**: 22

 |
| KEYCODE\_WLAN = 2844 | 

WLAN key

**Since**: 22

 |
| KEYCODE\_UWB = 2845 | 

Ultra-wideband key

**Since**: 22

 |
| KEYCODE\_WWAN\_WIMAX = 2846 | 

Mobile Network Control key

**Since**: 22

 |
| KEYCODE\_RFKILL = 2847 | 

RF Kill key

**Since**: 22

 |
| KEYCODE\_CHANNEL = 3001 | 

Channel key

**Since**: 22

 |
| KEYCODE\_BTN\_0 = 3100 | 

Button 0

**Since**: 22

 |
| KEYCODE\_BTN\_1 = 3101 | 

Button 1

**Since**: 22

 |
| KEYCODE\_BTN\_2 = 3102 | 

Button 2

**Since**: 22

 |
| KEYCODE\_BTN\_3 = 3103 | 

Button 3

**Since**: 22

 |
| KEYCODE\_BTN\_4 = 3104 | 

Button 4

**Since**: 22

 |
| KEYCODE\_BTN\_5 = 3105 | 

Button 5

**Since**: 22

 |
| KEYCODE\_BTN\_6 = 3106 | 

Button 6

**Since**: 22

 |
| KEYCODE\_BTN\_7 = 3107 | 

Button 7

**Since**: 22

 |
| KEYCODE\_BTN\_8 = 3108 | 

Button 8

**Since**: 22

 |
| KEYCODE\_BTN\_9 = 3109 | 

Button 9

**Since**: 22

 |
| KEYCODE\_DAGGER\_CLICK = 3211 | 

Single tapping the smart watch's X-TAP sensor

**Since**: 22

 |
| KEYCODE\_DAGGER\_DOUBLE\_CLICK = 3212 | 

Double tapping the smart watch's X-TAP sensor

**Since**: 22

 |
| KEYCODE\_DAGGER\_LONG\_PRESS = 3213 | 

Long-pressing the smart watch's X-TAP sensor

**Since**: 22

 |
| KEYCODE\_DIV = 3220 | 

Left button of the smart watch

**Since**: 22

 |
