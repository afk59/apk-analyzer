# @ohos.multimodalInput.keyCode (Keycode)

The **keyCode** module provides key codes of key devices, including keyboards, CDs, and gamepads.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/cK4-a7udQqO3s5Wxfjjj2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CE7C7E9F219C36FC2C9369BD5351E23634FA5EF860715667529E914791A102B)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { KeyCode } from '@kit.InputKit';

#### KeyCode

Enumerates the key codes.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| KEYCODE\_FN | 0 | Function (Fn) key |
| KEYCODE\_UNKNOWN | \-1 | Unknown key |
| KEYCODE\_HOME | 1 | Function (Home) key |
| KEYCODE\_BACK | 2 | Back key |
| KEYCODE\_SEARCH13+ | 9 | Search key |
| KEYCODE\_MEDIA\_PLAY\_PAUSE | 10 | 
Play/Pause key

Difference between this key and **KEYCODE\_PLAYPAUSE**:

**KEYCODE\_PLAYPAUSE** is an earlier definition, while **KEYCODE\_MEDIA\_PLAY\_PAUSE** is designed for modern media key devices.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_STOP | 11 | 

Media: Stop Key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_NEXT | 12 | 

Next key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_PREVIOUS | 13 | 

Previous key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_REWIND | 14 | 

Rewind key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_FAST\_FORWARD | 15 | 

Fast forward key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_VOLUME\_UP | 16 | Volume Up key |
| KEYCODE\_VOLUME\_DOWN | 17 | Volume Down key |
| KEYCODE\_POWER | 18 | Power key |
| KEYCODE\_CAMERA | 19 | Camera key |
| KEYCODE\_VOLUME\_MUTE | 22 | Speaker Mute key |
| KEYCODE\_MUTE | 23 | Mute key |
| KEYCODE\_BRIGHTNESS\_UP | 40 | Brightness Up key |
| KEYCODE\_BRIGHTNESS\_DOWN | 41 | Brightness Down key |
| KEYCODE\_0 | 2000 | Key 0 |
| KEYCODE\_1 | 2001 | Key 1 |
| KEYCODE\_2 | 2002 | Key 2 |
| KEYCODE\_3 | 2003 | Key 3 |
| KEYCODE\_4 | 2004 | Key 4 |
| KEYCODE\_5 | 2005 | Key 5 |
| KEYCODE\_6 | 2006 | Key 6 |
| KEYCODE\_7 | 2007 | Key 7 |
| KEYCODE\_8 | 2008 | Key 8 |
| KEYCODE\_9 | 2009 | Key 9 |
| KEYCODE\_STAR | 2010 | Key / |
| KEYCODE\_POUND | 2011 | Key / |
| KEYCODE\_DPAD\_UP | 2012 | Up key on D-pad |
| KEYCODE\_DPAD\_DOWN | 2013 | Down key on D-pad |
| KEYCODE\_DPAD\_LEFT | 2014 | Left key on D-pad |
| KEYCODE\_DPAD\_RIGHT | 2015 | Right key on D-pad |
| KEYCODE\_DPAD\_CENTER | 2016 | Center key on D-pad |
| KEYCODE\_A | 2017 | Key A |
| KEYCODE\_B | 2018 | Key B |
| KEYCODE\_C | 2019 | Key C |
| KEYCODE\_D | 2020 | Key D |
| KEYCODE\_E | 2021 | Key E |
| KEYCODE\_F | 2022 | Key F |
| KEYCODE\_G | 2023 | Key G |
| KEYCODE\_H | 2024 | Key H |
| KEYCODE\_I | 2025 | Key I |
| KEYCODE\_J | 2026 | Key J |
| KEYCODE\_K | 2027 | Key K |
| KEYCODE\_L | 2028 | Key L |
| KEYCODE\_M | 2029 | Key M |
| KEYCODE\_N | 2030 | Key N |
| KEYCODE\_O | 2031 | Key O |
| KEYCODE\_P | 2032 | Key P |
| KEYCODE\_Q | 2033 | Key Q |
| KEYCODE\_R | 2034 | Key R |
| KEYCODE\_S | 2035 | Key S |
| KEYCODE\_T | 2036 | Key T |
| KEYCODE\_U | 2037 | Key U |
| KEYCODE\_V | 2038 | Key V |
| KEYCODE\_W | 2039 | Key W |
| KEYCODE\_X | 2040 | Key X |
| KEYCODE\_Y | 2041 | Key Y |
| KEYCODE\_Z | 2042 | Key Z |
| KEYCODE\_COMMA | 2043 | Key , |
| KEYCODE\_PERIOD | 2044 | Key . |
| KEYCODE\_ALT\_LEFT | 2045 | Left Alt key |
| KEYCODE\_ALT\_RIGHT | 2046 | Right Alt key |
| KEYCODE\_SHIFT\_LEFT | 2047 | Left Shift key |
| KEYCODE\_SHIFT\_RIGHT | 2048 | Right Shift key |
| KEYCODE\_TAB | 2049 | Tab key |
| KEYCODE\_SPACE | 2050 | Space key |
| KEYCODE\_SYM | 2051 | Symbol key |
| KEYCODE\_EXPLORER | 2052 | Explorer key, which is used to start the explorer application |
| KEYCODE\_ENVELOPE | 2053 | Email key, which is used to start the email application |
| KEYCODE\_ENTER | 2054 | Enter key |
| KEYCODE\_DEL | 2055 | Delete key |
| KEYCODE\_GRAVE | 2056 | Key / |
| KEYCODE\_MINUS | 2057 | Key - |
| KEYCODE\_EQUALS | 2058 | Key = |
| KEYCODE\_LEFT\_BRACKET | 2059 | Key \[ |
| KEYCODE\_RIGHT\_BRACKET | 2060 | Key \] |
| KEYCODE\_BACKSLASH | 2061 | Key \\ |
| KEYCODE\_SEMICOLON | 2062 | Key ; |
| KEYCODE\_APOSTROPHE | 2063 | Key ' |
| KEYCODE\_SLASH | 2064 | Key / |
| KEYCODE\_AT | 2065 | Key / |
| KEYCODE\_PLUS | 2066 | Key + |
| KEYCODE\_MENU | 2067 | Menu key |
| KEYCODE\_PAGE\_UP | 2068 | Page Up key |
| KEYCODE\_PAGE\_DOWN | 2069 | Page Down key |
| KEYCODE\_ESCAPE | 2070 | Esc key |
| KEYCODE\_FORWARD\_DEL | 2071 | Forward Delete key |
| KEYCODE\_CTRL\_LEFT | 2072 | Left Ctrl key |
| KEYCODE\_CTRL\_RIGHT | 2073 | Right Ctrl key |
| KEYCODE\_CAPS\_LOCK | 2074 | Caps Lock key |
| KEYCODE\_SCROLL\_LOCK | 2075 | Scroll Lock key |
| KEYCODE\_META\_LEFT | 2076 | Left Meta key |
| KEYCODE\_META\_RIGHT | 2077 | Right Meta key |
| KEYCODE\_FUNCTION | 2078 | Function key |
| KEYCODE\_SYSRQ | 2079 | System Request/Print Screen key |
| KEYCODE\_BREAK | 2080 | Break/Pause key |
| KEYCODE\_MOVE\_HOME | 2081 | Move to Home key |
| KEYCODE\_MOVE\_END | 2082 | Move to End key |
| KEYCODE\_INSERT | 2083 | Insert key |
| KEYCODE\_FORWARD | 2084 | Forward key |
| KEYCODE\_MEDIA\_PLAY | 2085 | 

Play key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_PAUSE | 2086 | 

Media: Pause Key

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| KEYCODE\_MEDIA\_CLOSE | 2087 | Media: Close Key |
| KEYCODE\_MEDIA\_EJECT | 2088 | Media: Eject Key |
| KEYCODE\_MEDIA\_RECORD | 2089 | Record key |
| KEYCODE\_F1 | 2090 | F1 key |
| KEYCODE\_F2 | 2091 | F2 key |
| KEYCODE\_F3 | 2092 | F3 key |
| KEYCODE\_F4 | 2093 | F4 key |
| KEYCODE\_F5 | 2094 | F5 key |
| KEYCODE\_F6 | 2095 | F6 key |
| KEYCODE\_F7 | 2096 | F7 key |
| KEYCODE\_F8 | 2097 | F8 key |
| KEYCODE\_F9 | 2098 | F9 key |
| KEYCODE\_F10 | 2099 | F10 key |
| KEYCODE\_F11 | 2100 | F11 key |
| KEYCODE\_F12 | 2101 | F12 key |
| KEYCODE\_NUM\_LOCK | 2102 | Number Lock key on numeric keypad |
| KEYCODE\_NUMPAD\_0 | 2103 | Key 0 on numeric keypad |
| KEYCODE\_NUMPAD\_1 | 2104 | Key 1 on numeric keypad |
| KEYCODE\_NUMPAD\_2 | 2105 | Key 2 on numeric keypad |
| KEYCODE\_NUMPAD\_3 | 2106 | Key 3 on numeric keypad |
| KEYCODE\_NUMPAD\_4 | 2107 | Key 4 on numeric keypad |
| KEYCODE\_NUMPAD\_5 | 2108 | Key 5 on numeric keypad |
| KEYCODE\_NUMPAD\_6 | 2109 | Key 6 on numeric keypad |
| KEYCODE\_NUMPAD\_7 | 2110 | Key 7 on numeric keypad |
| KEYCODE\_NUMPAD\_8 | 2111 | Key 8 on numeric keypad |
| KEYCODE\_NUMPAD\_9 | 2112 | Key 9 on numeric keypad |
| KEYCODE\_NUMPAD\_DIVIDE | 2113 | Key / on numeric keypad |
| KEYCODE\_NUMPAD\_MULTIPLY | 2114 | Key ) on numeric keypad |
| KEYCODE\_NUMPAD\_SUBTRACT | 2115 | Key - on numeric keypad |
| KEYCODE\_NUMPAD\_ADD | 2116 | Key + on numeric keypad |
| KEYCODE\_NUMPAD\_DOT | 2117 | Key . on numeric keypad |
| KEYCODE\_NUMPAD\_COMMA | 2118 | Key , on numeric keypad |
| KEYCODE\_NUMPAD\_ENTER | 2119 | Enter key on numeric keypad |
| KEYCODE\_NUMPAD\_EQUALS | 2120 | Key = on numeric keypad |
| KEYCODE\_NUMPAD\_LEFT\_PAREN | 2121 | Key ( on numeric keypad |
| KEYCODE\_NUMPAD\_RIGHT\_PAREN | 2122 | Key ) on numeric keypad |
| KEYCODE\_VIRTUAL\_MULTITASK | 2210 | Multi-task key |
| KEYCODE\_BUTTON\_A15+ | 2301 | Joystick key A |
| KEYCODE\_BUTTON\_B15+ | 2302 | Joystick key B |
| KEYCODE\_BUTTON\_X15+ | 2304 | Joystick key X |
| KEYCODE\_BUTTON\_Y15+ | 2305 | Joystick key Y |
| KEYCODE\_BUTTON\_L115+ | 2307 | Joystick key L1 |
| KEYCODE\_BUTTON\_R115+ | 2308 | Joystick key R1 |
| KEYCODE\_BUTTON\_L215+ | 2309 | Joystick key L2 |
| KEYCODE\_BUTTON\_R215+ | 2310 | Joystick key R2 |
| KEYCODE\_BUTTON\_SELECT15+ | 2311 | Joystick key Select |
| KEYCODE\_BUTTON\_START15+ | 2312 | Joystick key Start |
| KEYCODE\_BUTTON\_MODE15+ | 2313 | Joystick key Mode |
| KEYCODE\_BUTTON\_THUMBL15+ | 2314 | Joystick key THUMBL |
| KEYCODE\_BUTTON\_THUMBR15+ | 2315 | Joystick key THUMBR |
| KEYCODE\_SLEEP | 2600 | Sleep key |
| KEYCODE\_ZENKAKU\_HANKAKU | 2601 | Zenkaku/Hankaku key |
| KEYCODE\_102ND | 2602 | International Keyboard Extension key |
| KEYCODE\_RO | 2603 | Ro key |
| KEYCODE\_KATAKANA | 2604 | Katakana key |
| KEYCODE\_HIRAGANA | 2605 | Hiragana key |
| KEYCODE\_HENKAN | 2606 | Henkan key |
| KEYCODE\_KATAKANA\_HIRAGANA | 2607 | Katakana/Hiragana key |
| KEYCODE\_MUHENKAN | 2608 | Muhenkan key |
| KEYCODE\_LINEFEED | 2609 | Linefeed key |
| KEYCODE\_MACRO | 2610 | Macro key |
| KEYCODE\_NUMPAD\_PLUSMINUS | 2611 | Plus/Minus key on the numeric keypad |
| KEYCODE\_SCALE | 2612 | Scale key |
| KEYCODE\_HANGUEL | 2613 | Hanguel key |
| KEYCODE\_HANJA | 2614 | Hanja key |
| KEYCODE\_YEN | 2615 | Yen key |
| KEYCODE\_STOP | 2616 | Stop key |
| KEYCODE\_AGAIN | 2617 | Again key |
| KEYCODE\_PROPS | 2618 | Props key |
| KEYCODE\_UNDO | 2619 | Undo key |
| KEYCODE\_COPY | 2620 | Copy key |
| KEYCODE\_OPEN | 2621 | Open key |
| KEYCODE\_PASTE | 2622 | Paste key |
| KEYCODE\_FIND | 2623 | Find key |
| KEYCODE\_CUT | 2624 | Cut key |
| KEYCODE\_HELP | 2625 | Help key |
| KEYCODE\_CALC | 2626 | Calc key, which is used to start the calculator application |
| KEYCODE\_FILE | 2627 | File key |
| KEYCODE\_BOOKMARKS | 2628 | Bookmarks key |
| KEYCODE\_NEXT | 2629 | Page Down key |
| KEYCODE\_PLAYPAUSE | 2630 | 

Play/Pause key

Difference between this key and **KEYCODE\_MEDIA\_PLAY\_PAUSE**:

**KEYCODE\_PLAYPAUSE** is an earlier definition, while **KEYCODE\_MEDIA\_PLAY\_PAUSE** is designed for modern media key devices.

 |
| KEYCODE\_PREVIOUS | 2631 | Page Up key |
| KEYCODE\_STOPCD | 2632 | Stop CD key |
| KEYCODE\_CONFIG | 2634 | Config key |
| KEYCODE\_REFRESH | 2635 | Refresh key |
| KEYCODE\_EXIT | 2636 | Exit key |
| KEYCODE\_EDIT | 2637 | Edit key |
| KEYCODE\_SCROLLUP | 2638 | Scroll Up key |
| KEYCODE\_SCROLLDOWN | 2639 | Scroll Down key |
| KEYCODE\_NEW | 2640 | New key |
| KEYCODE\_REDO | 2641 | Redo key |
| KEYCODE\_CLOSE | 2642 | Close key |
| KEYCODE\_PLAY | 2643 | Play key |
| KEYCODE\_BASSBOOST | 2644 | Bass Boost key |
| KEYCODE\_PRINT | 2645 | Print key |
| KEYCODE\_CHAT | 2646 | Chat key |
| KEYCODE\_FINANCE | 2647 | Finance key |
| KEYCODE\_CANCEL | 2648 | Cancel key |
| KEYCODE\_KBDILLUM\_TOGGLE | 2649 | Keyboard Illumination Toggle key |
| KEYCODE\_KBDILLUM\_DOWN | 2650 | Keyboard Illumination Down key |
| KEYCODE\_KBDILLUM\_UP | 2651 | Keyboard Illumination Up key |
| KEYCODE\_SEND | 2652 | Send key |
| KEYCODE\_REPLY | 2653 | Reply key |
| KEYCODE\_FORWARDMAIL | 2654 | Forward Mail key |
| KEYCODE\_SAVE | 2655 | Save key |
| KEYCODE\_DOCUMENTS | 2656 | Documents key |
| KEYCODE\_VIDEO\_NEXT | 2657 | Next Video key |
| KEYCODE\_VIDEO\_PREV | 2658 | Previous Video key |
| KEYCODE\_BRIGHTNESS\_CYCLE | 2659 | Brightness Cycle key |
| KEYCODE\_BRIGHTNESS\_ZERO | 2660 | Brightness Zero key |
| KEYCODE\_DISPLAY\_OFF | 2661 | Display Off key |
| KEYCODE\_BTN\_MISC | 2662 | Misc Button key |
| KEYCODE\_GOTO | 2663 | Goto key |
| KEYCODE\_INFO | 2664 | Info key |
| KEYCODE\_PROGRAM | 2665 | Program key |
| KEYCODE\_PVR | 2666 | PVR key |
| KEYCODE\_SUBTITLE | 2667 | Subtitle key |
| KEYCODE\_FULL\_SCREEN | 2668 | Full Screen key |
| KEYCODE\_KEYBOARD | 2669 | Keyboard. |
| KEYCODE\_ASPECT\_RATIO | 2670 | Aspect Ratio key |
| KEYCODE\_PC | 2671 | Port Control key |
| KEYCODE\_TV | 2672 | TV key |
| KEYCODE\_TV2 | 2673 | TV key 2 |
| KEYCODE\_VCR | 2674 | VCR key |
| KEYCODE\_VCR2 | 2675 | VCR key 2 |
| KEYCODE\_SAT | 2676 | SAT key |
| KEYCODE\_CD | 2677 | CD key |
| KEYCODE\_TAPE | 2678 | Tape key |
| KEYCODE\_TUNER | 2679 | Tuner key |
| KEYCODE\_PLAYER | 2680 | Player key |
| KEYCODE\_DVD | 2681 | DVD key |
| KEYCODE\_AUDIO | 2682 | Audio key |
| KEYCODE\_VIDEO | 2683 | Video key |
| KEYCODE\_MEMO | 2684 | Memo key |
| KEYCODE\_CALENDAR | 2685 | Calendar key |
| KEYCODE\_RED | 2686 | Red indicator. |
| KEYCODE\_GREEN | 2687 | Green indicator. |
| KEYCODE\_YELLOW | 2688 | Yellow indicator. |
| KEYCODE\_BLUE | 2689 | Blue indicator. |
| KEYCODE\_CHANNELUP | 2690 | Channel Up key |
| KEYCODE\_CHANNELDOWN | 2691 | Channel Down key |
| KEYCODE\_LAST | 2692 | Last key |
| KEYCODE\_RESTART | 2693 | Restart key |
| KEYCODE\_SLOW | 2694 | Slow key |
| KEYCODE\_SHUFFLE | 2695 | Shuffle key |
| KEYCODE\_VIDEOPHONE | 2696 | Videophone key |
| KEYCODE\_GAMES | 2697 | Games key |
| KEYCODE\_ZOOMIN | 2698 | Zoom in |
| KEYCODE\_ZOOMOUT | 2699 | Zoom out |
| KEYCODE\_ZOOMRESET | 2700 | Zoom Reset key |
| KEYCODE\_WORDPROCESSOR | 2701 | Word Processor key |
| KEYCODE\_EDITOR | 2702 | Editor key |
| KEYCODE\_SPREADSHEET | 2703 | Spreadsheet key |
| KEYCODE\_GRAPHICSEDITOR | 2704 | Graphics Editor key |
| KEYCODE\_PRESENTATION | 2705 | Presentation key |
| KEYCODE\_DATABASE | 2706 | Database key |
| KEYCODE\_NEWS | 2707 | News key |
| KEYCODE\_VOICEMAIL | 2708 | Voicemail key |
| KEYCODE\_ADDRESSBOOK | 2709 | Address book key |
| KEYCODE\_MESSENGER | 2710 | Messenger key |
| KEYCODE\_BRIGHTNESS\_TOGGLE | 2711 | Brightness Toggle key |
| KEYCODE\_SPELLCHECK | 2712 | Spell Check key |
| KEYCODE\_COFFEE | 2713 | Coffee key, which is used to launch screen lock or screen saver |
| KEYCODE\_MEDIA\_REPEAT | 2714 | Media Repeat key |
| KEYCODE\_IMAGES | 2715 | Images key |
| KEYCODE\_BUTTONCONFIG | 2716 | Button Configuration key |
| KEYCODE\_TASKMANAGER | 2717 | Task Manager key |
| KEYCODE\_JOURNAL | 2718 | Log key |
| KEYCODE\_CONTROLPANEL | 2719 | Control Panel key |
| KEYCODE\_APPSELECT | 2720 | App Select key |
| KEYCODE\_SCREENSAVER | 2721 | Screen Saver key |
| KEYCODE\_ASSISTANT | 2722 | Smart key |
| KEYCODE\_KBD\_LAYOUT\_NEXT | 2723 | Next Keyboard Layout key |
| KEYCODE\_BRIGHTNESS\_MIN | 2724 | Min Brightness key |
| KEYCODE\_BRIGHTNESS\_MAX | 2725 | Max Brightness key |
| KEYCODE\_KBDINPUTASSIST\_PREV | 2726 | Assist\_Previous key, used to view historical inputs |
| KEYCODE\_KBDINPUTASSIST\_NEXT | 2727 | Assist\_Next key, used to view predictive inputs |
| KEYCODE\_KBDINPUTASSIST\_PREVGROUP | 2728 | Assist\_Previous\_Group key, used to switch to the previous input method in the input group |
| KEYCODE\_KBDINPUTASSIST\_NEXTGROUP | 2729 | Assist\_Next\_Group key, used to switch to the next input method in the input group |
| KEYCODE\_KBDINPUTASSIST\_ACCEPT | 2730 | Keyboard Input-assisted Accept key |
| KEYCODE\_KBDINPUTASSIST\_CANCEL | 2731 | Keyboard Input-assisted Cancel key |
| KEYCODE\_FRONT | 2800 | Front key, which is used to launch the windshield defogger |
| KEYCODE\_SETUP | 2801 | Setup key |
| KEYCODE\_WAKEUP | 2802 | Wakeup key |
| KEYCODE\_SENDFILE | 2803 | Send File key |
| KEYCODE\_DELETEFILE | 2804 | Delete File key |
| KEYCODE\_XFER | 2805 | XFER key, which is used to start file transfer |
| KEYCODE\_PROG1 | 2806 | Program key 1 |
| KEYCODE\_PROG2 | 2807 | Program key 2 |
| KEYCODE\_MSDOS | 2808 | DOS Panel key |
| KEYCODE\_SCREENLOCK | 2809 | Screen Lock key |
| KEYCODE\_DIRECTION\_ROTATE\_DISPLAY | 2810 | Directional Rotation Display key |
| KEYCODE\_CYCLEWINDOWS | 2811 | Window Switching key |
| KEYCODE\_COMPUTER | 2812 | Key |
| KEYCODE\_EJECTCLOSECD | 2813 | Eject CD key |
| KEYCODE\_ISO | 2814 | ISO key |
| KEYCODE\_MOVE | 2815 | Move key |
| KEYCODE\_F13 | 2816 | F13 key |
| KEYCODE\_F14 | 2817 | F14 key |
| KEYCODE\_F15 | 2818 | F15 key |
| KEYCODE\_F16 | 2819 | F16 key |
| KEYCODE\_F17 | 2820 | F17 key |
| KEYCODE\_F18 | 2821 | F18 key |
| KEYCODE\_F19 | 2822 | F19 key |
| KEYCODE\_F20 | 2823 | F20 key |
| KEYCODE\_F21 | 2824 | F21 key |
| KEYCODE\_F22 | 2825 | F22 key |
| KEYCODE\_F23 | 2826 | F23 key |
| KEYCODE\_F24 | 2827 | F24 key |
| KEYCODE\_PROG3 | 2828 | Program key 3 |
| KEYCODE\_PROG4 | 2829 | Program key 4 |
| KEYCODE\_DASHBOARD | 2830 | Dashboard key |
| KEYCODE\_SUSPEND | 2831 | Suspend key |
| KEYCODE\_HP | 2832 | HP key |
| KEYCODE\_SOUND | 2833 | Sound key |
| KEYCODE\_QUESTION | 2834 | Question key |
| KEYCODE\_CONNECT | 2836 | Connect key |
| KEYCODE\_SPORT | 2837 | Sport key |
| KEYCODE\_SHOP | 2838 | Shop key |
| KEYCODE\_ALTERASE | 2839 | Alternate key |
| KEYCODE\_SWITCHVIDEOMODE | 2841 | Switch Video Mode key (monitor, LCD, and TV, etc.) |
| KEYCODE\_BATTERY | 2842 | Battery key |
| KEYCODE\_BLUETOOTH | 2843 | Bluetooth key |
| KEYCODE\_WLAN | 2844 | WLAN key |
| KEYCODE\_UWB | 2845 | Ultra-wideband Control key |
| KEYCODE\_WWAN\_WIMAX | 2846 | Mobile Network Control key |
| KEYCODE\_RFKILL | 2847 | RF Kill key |
| KEYCODE\_CHANNEL | 3001 | Channel key |
| KEYCODE\_BTN\_0 | 3100 | Button 0 |
| KEYCODE\_BTN\_1 | 3101 | Button 1 |
| KEYCODE\_BTN\_2 | 3102 | Button 2 |
| KEYCODE\_BTN\_3 | 3103 | Button 3 |
| KEYCODE\_BTN\_4 | 3104 | Button 4 |
| KEYCODE\_BTN\_5 | 3105 | Button 5 |
| KEYCODE\_BTN\_6 | 3106 | Button 6 |
| KEYCODE\_BTN\_7 | 3107 | Button 7 |
| KEYCODE\_BTN\_8 | 3108 | Button 8 |
| KEYCODE\_BTN\_9 | 3109 | Button 9 |
| KEYCODE\_DAGGER\_CLICK18+ | 3211 | Single tapping the smart watch's X-TAP sensor |
| KEYCODE\_DAGGER\_DOUBLE\_CLICK18+ | 3212 | Double tapping the smart watch's X-TAP sensor |
| KEYCODE\_DAGGER\_LONG\_PRESS18+ | 3213 | Long-pressing the smart watch's X-TAP sensor |
| KEYCODE\_DIV20+ | 3220 | Left button of the smart watch |
