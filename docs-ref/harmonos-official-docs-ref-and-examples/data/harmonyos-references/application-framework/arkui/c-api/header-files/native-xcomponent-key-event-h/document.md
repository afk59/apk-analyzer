# native\_xcomponent\_key\_event.h

#### Overview

Declares the enums used to access native XComponent key events.

**File to include**: <ace/xcomponent/native\_xcomponent\_key\_event.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 10

**Related module**: [OH\_NativeXComponent Native XComponent](../../modules/oh-nativexcomponent-native-xcomponent/document.md)

**Sample**: [NativeXComponentSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeXComponentSample)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeXComponent\_KeyCode](#oh_nativexcomponent_keycode) | OH\_NativeXComponent\_KeyCode | Enumerates the key codes for key events. |
| [OH\_NativeXComponent\_KeyAction](#oh_nativexcomponent_keyaction) | OH\_NativeXComponent\_KeyAction | Enumerates the key event actions. |

#### Enum Description

#### \[h2\]OH\_NativeXComponent\_KeyCode

enum OH\_NativeXComponent\_KeyCode

**Description**

Enumerates the key codes for key events.

**Since**: 10

| Value | Description |
| :-- | :-- |
| KEY\_UNKNOWN = -1 | Unknown key |
| KEY\_FN = 0 | Function (Fn) key |
| KEY\_HOME = 1 | Function (Home) key |
| KEY\_BACK = 2 | Back key |
| KEY\_MEDIA\_PLAY\_PAUSE = 10 | Play/Pause key |
| KEY\_MEDIA\_STOP = 11 | Stop key |
| KEY\_MEDIA\_NEXT = 12 | Next key |
| KEY\_MEDIA\_PREVIOUS = 13 | Previous key |
| KEY\_MEDIA\_REWIND = 14 | Rewind key |
| KEY\_MEDIA\_FAST\_FORWARD = 15 | Fast forward key |
| KEY\_VOLUME\_UP = 16 | Volume Up key |
| KEY\_VOLUME\_DOWN = 17 | Volume Down key |
| KEY\_POWER = 18 | Power key |
| KEY\_CAMERA = 19 | Camera key |
| KEY\_VOLUME\_MUTE = 22 | Speaker Mute key |
| KEY\_MUTE = 23 | Mute key |
| KEY\_BRIGHTNESS\_UP = 40 | Brightness Up key. |
| KEY\_BRIGHTNESS\_DOWN = 41 | Brightness Down key. |
| KEY\_0 = 2000 | Key 0 |
| KEY\_1 = 2001 | Key 1 |
| KEY\_2 = 2002 | Key 2 |
| KEY\_3 = 2003 | Key 3 |
| KEY\_4 = 2004 | Key 4 |
| KEY\_5 = 2005 | Key 5 |
| KEY\_6 = 2006 | Key 6 |
| KEY\_7 = 2007 | Key 7 |
| KEY\_8 = 2008 | Key 8 |
| KEY\_9 = 2009 | Key 9 |
| KEY\_STAR = 2010 | Key \* |
| KEY\_POUND = 2011 | Key # |
| KEY\_DPAD\_UP = 2012 | Up key on D-pad. |
| KEY\_DPAD\_DOWN = 2013 | Down key on D-pad. |
| KEY\_DPAD\_LEFT = 2014 | Left key on D-pad. |
| KEY\_DPAD\_RIGHT = 2015 | Right key on D-pad. |
| KEY\_DPAD\_CENTER = 2016 | Center key on D-pad. |
| KEY\_A = 2017 | Key A |
| KEY\_B = 2018 | Key B |
| KEY\_C = 2019 | Key C |
| KEY\_D = 2020 | Key D |
| KEY\_E = 2021 | Key E |
| KEY\_F = 2022 | Key F |
| KEY\_G = 2023 | Key G |
| KEY\_H = 2024 | Key H |
| KEY\_I = 2025 | Key I |
| KEY\_J = 2026 | Key J |
| KEY\_K = 2027 | Key K |
| KEY\_L = 2028 | Key L |
| KEY\_M = 2029 | Key M |
| KEY\_N = 2030 | Key N |
| KEY\_O = 2031 | Key O |
| KEY\_P = 2032 | Key P |
| KEY\_Q = 2033 | Key Q |
| KEY\_R = 2034 | Key R |
| KEY\_S = 2035 | Key S |
| KEY\_T = 2036 | Key T |
| KEY\_U = 2037 | Key U |
| KEY\_V = 2038 | Key V |
| KEY\_W = 2039 | Key W |
| KEY\_X = 2040 | Key X |
| KEY\_Y = 2041 | Key Y |
| KEY\_Z = 2042 | Key Z |
| KEY\_COMMA = 2043 | Key , |
| KEY\_PERIOD = 2044 | Key . |
| KEY\_ALT\_LEFT = 2045 | Left Alt key |
| KEY\_ALT\_RIGHT = 2046 | Right Alt key |
| KEY\_SHIFT\_LEFT = 2047 | Left Shift key |
| KEY\_SHIFT\_RIGHT = 2048 | Right Shift key |
| KEY\_TAB = 2049 | Tab key |
| KEY\_SPACE = 2050 | Space key |
| KEY\_SYM = 2051 | Symbol key |
| KEY\_EXPLORER = 2052 | Explorer key, which is used to start the explorer application |
| KEY\_ENVELOPE = 2053 | Email key, which is used to start the email application |
| KEY\_ENTER = 2054 | Enter key |
| KEY\_DEL = 2055 | Delete key |
| KEY\_GRAVE = 2056 | Key \` |
| KEY\_MINUS = 2057 | Key - |
| KEY\_EQUALS = 2058 | Key = |
| KEY\_LEFT\_BRACKET = 2059 | Key \[ |
| KEY\_RIGHT\_BRACKET = 2060 | Key \] |
| KEY\_BACKSLASH = 2061 | Key | |
| KEY\_SEMICOLON = 2062 | Key ; |
| KEY\_APOSTROPHE = 2063 | Key ' |
| KEY\_SLASH = 2064 | Key / |
| KEY\_AT = 2065 | Key @ |
| KEY\_PLUS = 2066 | Key + |
| KEY\_MENU = 2067 | Menu key |
| KEY\_PAGE\_UP = 2068 | Page Up key |
| KEY\_PAGE\_DOWN = 2069 | Page Down key |
| KEY\_ESCAPE = 2070 | ESC key. |
| KEY\_FORWARD\_DEL = 2071 | Forward Delete key |
| KEY\_CTRL\_LEFT = 2072 | Left Ctrl key |
| KEY\_CTRL\_RIGHT = 2073 | Right Ctrl key |
| KEY\_CAPS\_LOCK = 2074 | Caps Lock key |
| KEY\_SCROLL\_LOCK = 2075 | Scroll Lock key |
| KEY\_META\_LEFT = 2076 | Left Meta key |
| KEY\_META\_RIGHT = 2077 | Right Meta key |
| KEY\_FUNCTION = 2078 | Function key |
| KEY\_SYSRQ = 2079 | System Request/Print Screen key |
| KEY\_BREAK = 2080 | Break/Pause key |
| KEY\_MOVE\_HOME = 2081 | Move to Home key |
| KEY\_MOVE\_END = 2082 | Move to End key |
| KEY\_INSERT = 2083 | Insert key |
| KEY\_FORWARD = 2084 | Forward key |
| KEY\_MEDIA\_PLAY = 2085 | Play key |
| KEY\_MEDIA\_PAUSE = 2086 | Pause key |
| KEY\_MEDIA\_CLOSE = 2087 | Close key |
| KEY\_MEDIA\_EJECT = 2088 | Eject key |
| KEY\_MEDIA\_RECORD = 2089 | Record key |
| KEY\_F1 = 2090 | F1 key |
| KEY\_F2 = 2091 | F2 key |
| KEY\_F3 = 2092 | F3 key |
| KEY\_F4 = 2093 | F4 key |
| KEY\_F5 = 2094 | F5 key |
| KEY\_F6 = 2095 | F6 key |
| KEY\_F7 = 2096 | F7 key |
| KEY\_F8 = 2097 | F8 key |
| KEY\_F9 = 2098 | F9 key |
| KEY\_F10 = 2099 | F10 key |
| KEY\_F11 = 2100 | F11 key |
| KEY\_F12 = 2101 | F12 key |
| KEY\_NUM\_LOCK = 2102 | Number Lock key on numeric keypad |
| KEY\_NUMPAD\_0 = 2103 | Key 0 on numeric keypad |
| KEY\_NUMPAD\_1 = 2104 | Key 1 on numeric keypad |
| KEY\_NUMPAD\_2 = 2105 | Key 2 on numeric keypad |
| KEY\_NUMPAD\_3 = 2106 | Key 3 on numeric keypad |
| KEY\_NUMPAD\_4 = 2107 | Key 4 on numeric keypad |
| KEY\_NUMPAD\_5 = 2108 | Key 5 on numeric keypad |
| KEY\_NUMPAD\_6 = 2109 | Key 6 on numeric keypad |
| KEY\_NUMPAD\_7 = 2110 | Key 7 on numeric keypad |
| KEY\_NUMPAD\_8 = 2111 | Key 8 on numeric keypad |
| KEY\_NUMPAD\_9 = 2112 | Key 9 on numeric keypad |
| KEY\_NUMPAD\_DIVIDE = 2113 | Key / on numeric keypad |
| KEY\_NUMPAD\_MULTIPLY = 2114 | Key \* on numeric keypad |
| KEY\_NUMPAD\_SUBTRACT = 2115 | Key - on numeric keypad |
| KEY\_NUMPAD\_ADD = 2116 | Key + on numeric keypad |
| KEY\_NUMPAD\_DOT = 2117 | Key . on numeric keypad |
| KEY\_NUMPAD\_COMMA = 2118 | Key , on numeric keypad |
| KEY\_NUMPAD\_ENTER = 2119 | Enter key on numeric keypad |
| KEY\_NUMPAD\_EQUALS = 2120 | Key = on numeric keypad |
| KEY\_NUMPAD\_LEFT\_PAREN = 2121 | Key ( on numeric keypad |
| KEY\_NUMPAD\_RIGHT\_PAREN = 2122 | Key ) on numeric keypad |
| KEY\_VIRTUAL\_MULTITASK = 2210 | Multi-task key |
| KEY\_SLEEP = 2600 | Sleep key |
| KEY\_ZENKAKU\_HANKAKU = 2601 | Zenkaku/Hankaku key |
| KEY\_102ND = 2602 | 102nd key |
| KEY\_RO = 2603 | Ro key |
| KEY\_KATAKANA = 2604 | Katakana key |
| KEY\_HIRAGANA = 2605 | Hiragana key |
| KEY\_HENKAN = 2606 | Henkan key |
| KEY\_KATAKANA\_HIRAGANA = 2607 | Katakana/Hiragana key |
| KEY\_MUHENKAN = 2608 | Muhenkan key |
| KEY\_LINEFEED = 2609 | Linefeed key |
| KEY\_MACRO = 2610 | Macro key |
| KEY\_NUMPAD\_PLUSMINUS = 2611 | Plus/Minus key on the numeric keypad |
| KEY\_SCALE = 2612 | Scale key |
| KEY\_HANGUEL = 2613 | Hanguel key |
| KEY\_HANJA = 2614 | Hanja key |
| KEY\_YEN = 2615 | Yen key |
| KEY\_STOP = 2616 | Stop key |
| KEY\_AGAIN = 2617 | Again key |
| KEY\_PROPS = 2618 | Props key |
| KEY\_UNDO = 2619 | Undo key |
| KEY\_COPY = 2620 | Copy key |
| KEY\_OPEN = 2621 | Open key |
| KEY\_PASTE = 2622 | Paste key |
| KEY\_FIND = 2623 | Find key |
| KEY\_CUT = 2624 | Cut key |
| KEY\_HELP = 2625 | Help key |
| KEY\_CALC = 2626 | Calc key, which is used to start the calculator application |
| KEY\_FILE = 2627 | File key |
| KEY\_BOOKMARKS = 2628 | Bookmarks key |
| KEY\_NEXT = 2629 | Next key |
| KEY\_PLAYPAUSE = 2630 | Play/Pause key |
| KEY\_PREVIOUS = 2631 | Previous key |
| KEY\_STOPCD = 2632 | Stop CD key |
| KEY\_CONFIG = 2634 | Config key |
| KEY\_REFRESH = 2635 | Refresh key |
| KEY\_EXIT = 2636 | Exit key |
| KEY\_EDIT = 2637 | Edit key |
| KEY\_SCROLLUP = 2638 | Scroll Up key |
| KEY\_SCROLLDOWN = 2639 | Scroll Down key |
| KEY\_NEW = 2640 | New key |
| KEY\_REDO = 2641 | Redo key |
| KEY\_CLOSE = 2642 | Close key |
| KEY\_PLAY = 2643 | Play key |
| KEY\_BASSBOOST = 2644 | Bass Boost key |
| KEY\_PRINT = 2645 | Print key |
| KEY\_CHAT = 2646 | Chat key |
| KEY\_FINANCE = 2647 | Finance key |
| KEY\_CANCEL = 2648 | Cancel key |
| KEY\_KBDILLUM\_TOGGLE = 2649 | Keyboard Illumination Toggle key |
| KEY\_KBDILLUM\_DOWN = 2650 | Keyboard Illumination Up key |
| KEY\_KBDILLUM\_UP = 2651 | Keyboard Illumination Down key |
| KEY\_SEND = 2652 | Send key |
| KEY\_REPLY = 2653 | Reply key |
| KEY\_FORWARDMAIL = 2654 | Forward Mail key |
| KEY\_SAVE = 2655 | Save key |
| KEY\_DOCUMENTS = 2656 | Documents key |
| KEY\_VIDEO\_NEXT = 2657 | Next Video key |
| KEY\_VIDEO\_PREV = 2658 | Previous Video key |
| KEY\_BRIGHTNESS\_CYCLE = 2659 | Brightness Cycle key |
| KEY\_BRIGHTNESS\_ZERO = 2660 | Brightness Zero key |
| KEY\_DISPLAY\_OFF = 2661 | Display Off key |
| KEY\_BTN\_MISC = 2662 | Misc Button key |
| KEY\_GOTO = 2663 | Goto key |
| KEY\_INFO = 2664 | Info key |
| KEY\_PROGRAM = 2665 | Program key |
| KEY\_PVR = 2666 | PVR key |
| KEY\_SUBTITLE = 2667 | Subtitle key |
| KEY\_FULL\_SCREEN = 2668 | Full Screen key |
| KEY\_KEYBOARD = 2669 | Keyboard. |
| KEY\_ASPECT\_RATIO = 2670 | Aspect Ratio key |
| KEY\_PC = 2671 | Port Control key |
| KEY\_TV = 2672 | TV key |
| KEY\_TV2 = 2673 | TV key 2 |
| KEY\_VCR = 2674 | VCR key |
| KEY\_VCR2 = 2675 | VCR key 2 |
| KEY\_SAT = 2676 | SAT key |
| KEY\_CD = 2677 | CD key |
| KEY\_TAPE = 2678 | Tape key |
| KEY\_TUNER = 2679 | Tuner key |
| KEY\_PLAYER = 2680 | Player key |
| KEY\_DVD = 2681 | DVD key |
| KEY\_AUDIO = 2682 | Audio key |
| KEY\_VIDEO = 2683 | Video key |
| KEY\_MEMO = 2684 | Memo key |
| KEY\_CALENDAR = 2685 | Calendar key |
| KEY\_RED = 2686 | Red indicator. |
| KEY\_GREEN = 2687 | Green indicator. |
| KEY\_YELLOW = 2688 | Yellow indicator. |
| KEY\_BLUE = 2689 | Blue indicator. |
| KEY\_CHANNELUP = 2690 | Channel Up key |
| KEY\_CHANNELDOWN = 2691 | Channel Down key |
| KEY\_LAST = 2692 | Last key |
| KEY\_RESTART = 2693 | Restart key |
| KEY\_SLOW = 2694 | Slow key |
| KEY\_SHUFFLE = 2695 | Shuffle key |
| KEY\_VIDEOPHONE = 2696 | Videophone key |
| KEY\_GAMES = 2697 | Games key |
| KEY\_ZOOMIN = 2698 | Zoom in |
| KEY\_ZOOMOUT = 2699 | Zoom out |
| KEY\_ZOOMRESET = 2700 | Zoom Reset key |
| KEY\_WORDPROCESSOR = 2701 | Word Processor key |
| KEY\_EDITOR = 2702 | Editor key |
| KEY\_SPREADSHEET = 2703 | Spreadsheet key |
| KEY\_GRAPHICSEDITOR = 2704 | Graphics Editor key |
| KEY\_PRESENTATION = 2705 | Presentation key |
| KEY\_DATABASE = 2706 | Database key |
| KEY\_NEWS = 2707 | News key |
| KEY\_VOICEMAIL = 2708 | Voicemail key |
| KEY\_ADDRESSBOOK = 2709 | Address book key |
| KEY\_MESSENGER = 2710 | Messenger key |
| KEY\_BRIGHTNESS\_TOGGLE = 2711 | Brightness Toggle key |
| KEY\_SPELLCHECK = 2712 | Spell Check key |
| KEY\_COFFEE = 2713 | Coffee key, which is used to launch screen lock or screen saver |
| KEY\_MEDIA\_REPEAT = 2714 | Media Repeat key |
| KEY\_IMAGES = 2715 | Images key |
| KEY\_BUTTONCONFIG = 2716 | Button Configuration key |
| KEY\_TASKMANAGER = 2717 | Task Manager key |
| KEY\_JOURNAL = 2718 | Log key |
| KEY\_CONTROLPANEL = 2719 | Control Panel key |
| KEY\_APPSELECT = 2720 | App Select key |
| KEY\_SCREENSAVER = 2721 | Screen Saver key |
| KEY\_ASSISTANT = 2722 | Assistant key |
| KEY\_KBD\_LAYOUT\_NEXT = 2723 | Next Keyboard Layout key |
| KEY\_BRIGHTNESS\_MIN = 2724 | Min Brightness key |
| KEY\_BRIGHTNESS\_MAX = 2725 | Max Brightness key |
| KEY\_KBDINPUTASSIST\_PREV = 2726 | Keyboard Input-assisted Previous key |
| KEY\_KBDINPUTASSIST\_NEXT = 2727 | Keyboard Input-assisted Next key |
| KEY\_KBDINPUTASSIST\_PREVGROUP = 2728 | Keyboard Input-assisted Previous key |
| KEY\_KBDINPUTASSIST\_NEXTGROUP = 2729 | Keyboard Input-assisted Next key |
| KEY\_KBDINPUTASSIST\_ACCEPT = 2730 | Keyboard Input-assisted Accept key |
| KEY\_KBDINPUTASSIST\_CANCEL = 2731 | Keyboard Input-assisted Cancel key |
| KEY\_FRONT = 2800 | Front key, which is used to launch the windshield defogger |
| KEY\_SETUP = 2801 | Setup key |
| KEY\_WAKEUP = 2802 | Wakeup key |
| KEY\_SENDFILE = 2803 | Send File key |
| KEY\_DELETEFILE = 2804 | Delete File key |
| KEY\_XFER = 2805 | XFER key, which is used to start file transfer |
| KEY\_PROG1 = 2806 | Program key 1 |
| KEY\_PROG2 = 2807 | Program key 2 |
| KEY\_MSDOS = 2808 | MS-DOS key |
| KEY\_SCREENLOCK = 2809 | Screen Lock key |
| KEY\_DIRECTION\_ROTATE\_DISPLAY = 2810 | Directional Rotation Display key |
| KEY\_CYCLEWINDOWS = 2811 | Windows Cycle key |
| KEY\_COMPUTER = 2812 | Key |
| KEY\_EJECTCLOSECD = 2813 | Eject CD key |
| KEY\_ISO = 2814 | ISO key |
| KEY\_MOVE = 2815 | Move key |
| KEY\_F13 = 2816 | F13 key |
| KEY\_F14 = 2817 | F14 key |
| KEY\_F15 = 2818 | F15 key |
| KEY\_F16 = 2819 | F16 key |
| KEY\_F17 = 2820 | F17 key |
| KEY\_F18 = 2821 | F18 key |
| KEY\_F19 = 2822 | F19 key |
| KEY\_F20 = 2823 | F20 key |
| KEY\_F21 = 2824 | F21 key |
| KEY\_F22 = 2825 | F22 key |
| KEY\_F23 = 2826 | F23 key |
| KEY\_F24 = 2827 | F24 key |
| KEY\_PROG3 = 2828 | Program key 3 |
| KEY\_PROG4 = 2829 | Program key 4 |
| KEY\_DASHBOARD = 2830 | Dashboard key |
| KEY\_SUSPEND = 2831 | Suspend key |
| KEY\_HP = 2832 | HP key |
| KEY\_SOUND = 2833 | Sound key |
| KEY\_QUESTION = 2834 | Question key |
| KEY\_CONNECT = 2836 | Connect key |
| KEY\_SPORT = 2837 | Sport key |
| KEY\_SHOP = 2838 | Shop key |
| KEY\_ALTERASE = 2839 | Alternate key |
| KEY\_SWITCHVIDEOMODE = 2841 | Switch Video Mode key (monitor, LCD, and TV, etc.) |
| KEY\_BATTERY = 2842 | Battery key |
| KEY\_BLUETOOTH = 2843 | Bluetooth key |
| KEY\_WLAN = 2844 | WLAN key |
| KEY\_UWB = 2845 | Ultra-wideband key |
| KEY\_WWAN\_WIMAX = 2846 | WWAN WiMAX key |
| KEY\_RFKILL = 2847 | RF Kill key |
| KEY\_CHANNEL = 3001 | Channel key |
| KEY\_BTN\_0 = 3100 | Button 0 |
| KEY\_BTN\_1 = 3101 | Button 1 |
| KEY\_BTN\_2 = 3102 | Button 2 |
| KEY\_BTN\_3 = 3103 | Button 3 |
| KEY\_BTN\_4 = 3104 | Button 4 |
| KEY\_BTN\_5 = 3105 | Button 5 |
| KEY\_BTN\_6 = 3106 | Button 6 |
| KEY\_BTN\_7 = 3107 | Button 7 |
| KEY\_BTN\_8 = 3108 | Button 8 |
| KEY\_BTN\_9 = 3109 | Button 9 |

#### \[h2\]OH\_NativeXComponent\_KeyAction

enum OH\_NativeXComponent\_KeyAction

**Description**

Enumerates the key event actions.

**Since**: 10

| Value | Description |
| :-- | :-- |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_UNKNOWN = -1 | Unknown key action. |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_DOWN = 0 | Key press. |
| OH\_NATIVEXCOMPONENT\_KEY\_ACTION\_UP = 1 | Key release. |
