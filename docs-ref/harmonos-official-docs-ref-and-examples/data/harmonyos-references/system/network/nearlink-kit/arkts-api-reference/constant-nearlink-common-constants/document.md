# constant (NearLink Common Constants)

This module defines some common constants.

**Start version**: 5.0.1(13)

#### Module Import

import { constant } from '@kit.NearLinkKit';

#### PairingState

Enumerated values of pairing statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PAIRING\_STATE\_NONE

 | 

1

 | 

Not paired.

 |
| 

PAIRING\_STATE\_PAIRING

 | 

2

 | 

Pairing.

 |
| 

PAIRING\_STATE\_PAIRED

 | 

3

 | 

Paired.

 |

#### ConnectionState

Enumerated values of connection statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

STATE\_CONNECTING

 | 

0

 | 

Connecting.

 |
| 

STATE\_CONNECTED

 | 

1

 | 

Connected.

 |
| 

STATE\_DISCONNECTING

 | 

2

 | 

Disconnecting.

 |
| 

STATE\_DISCONNECTED

 | 

3

 | 

Disconnected.

 |

#### DeviceClass

Enumerated values of device types.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.0.1(13)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DEVICE\_UNCATEGORIZED

 | 

0x000100

 | 

Uncategorized device.

 |
| 

DEVICE\_PHONE

 | 

0x000200

 | 

Landline.

 |
| 

DEVICE\_SMARTPHONE

 | 

0x000201

 | 

Smart phone.

 |
| 

DEVICE\_COMPUTER

 | 

0x000300

 | 

PC.

 |
| 

DEVICE\_LAPTOP

 | 

0x000301

 | 

Laptop.

 |
| 

DEVICE\_TABLET

 | 

0x000302

 | 

Tablet.

 |
| 

DEVICE\_ALL\_IN\_ONE\_COMPUTER

 | 

0x000303

 | 

2-in-1 device.

 |
| 

DEVICE\_MINI\_PC

 | 

0x000304

 | 

Mini PC.

 |
| 

DEVICE\_WATCH

 | 

0x000400

 | 

Watch.

 |
| 

DEVICE\_SMART\_WATCH

 | 

0x000401

 | 

Smart watch.

 |
| 

DEVICE\_HUMAN\_INTERFACE

 | 

0x000500

 | 

Human-machine interface.

 |
| 

DEVICE\_KEYBOARD

 | 

0x000501

 | 

Keyboard.

 |
| 

DEVICE\_MOUSE

 | 

0x000502

 | 

Mouse.

 |
| 

DEVICE\_HANDLE

 | 

0x000503

 | 

Handle.

 |
| 

DEVICE\_STYLUS

 | 

0x000504

 | 

Stylus.

 |
| 

DEVICE\_TOUCHPAD

 | 

0x000505

 | 

Touchpad.

 |
| 

DEVICE\_AUDIO\_PLAYBACK

 | 

0x000600

 | 

Audio player.

 |
| 

DEVICE\_SMART\_SPEAKER

 | 

0x000601

 | 

Smart speaker.

 |
| 

DEVICE\_ECHO\_WALL

 | 

0x000602

 | 

Echo device.

 |
| 

DEVICE\_AUDIO\_CAPTURE

 | 

0x000700

 | 

Recorder.

 |
| 

DEVICE\_KARAOKE\_MICROPHONE

 | 

0x000701

 | 

Karaoke microphone.

 |
| 

DEVICE\_LAPEL\_MICROPHONE

 | 

0x000702

 | 

Wearable microphone.

 |
| 

DEVICE\_WEARABLE\_AUDIO

 | 

0x000800

 | 

Wearable audio device.

 |
| 

DEVICE\_IN\_EAR\_EARPHONE

 | 

0x000801

 | 

In-ear headphone.

 |
| 

DEVICE\_HEADSET

 | 

0x000802

 | 

Headset.

 |
| 

DEVICE\_OVER\_EAR\_HEADPHONE

 | 

0x000803

 | 

Over-ear headphone.

 |
| 

DEVICE\_NECKBAND\_EARPHONE

 | 

0x000804

 | 

Neckband earphone.

 |
| 

DEVICE\_PERSONAL\_CARE

 | 

0x000900

 | 

Personal care.

 |
| 

DEVICE\_INTELLIGENT\_TOOTHBRUSH

 | 

0x000901

 | 

Smart toothbrush.

 |
| 

DEVICE\_SMART\_CUP

 | 

0x000902

 | 

Smart cup.

 |
| 

DEVICE\_INTELLIGENT\_SHAVER

 | 

0x000903

 | 

Smart shaver.

 |
| 

DEVICE\_HVAC

 | 

0x000A00

 | 

Heating, ventilation, and air conditioning (HVAC).

 |
| 

DEVICE\_AIR\_PURIFIER

 | 

0x000A01

 | 

Air purifier.

 |
| 

DEVICE\_HUMIDIFIER

 | 

0x000A02

 | 

Humidifier.

 |
| 

DEVICE\_AIR\_CIRCULATION\_FAN

 | 

0x000A03

 | 

Air circulation fan.

 |
| 

DEVICE\_ELECTRIC\_RIDE

 | 

0x000B00

 | 

Electric cycling tool.

 |
| 

DEVICE\_ELECTRIC\_SCOOTER

 | 

0x000B01

 | 

Electric skateboard.

 |
| 

DEVICE\_ELECTRIC\_BICYCLE

 | 

0x000B02

 | 

Electric bicycle.

 |
| 

DEVICE\_LIGHT\_FITTING

 | 

0x000C00

 | 

Light fittings.

 |
| 

DEVICE\_SMART\_TABLE\_LAMP

 | 

0x000C01

 | 

Smart table lamp.

 |
| 

DEVICE\_REMOTE\_CONTROL

 | 

0x000D00

 | 

Remote control device.

 |
| 

DEVICE\_TV\_REMOTE\_CONTROL

 | 

0x000D01

 | 

TV remote control.

 |
| 

DEVICE\_IMAGING

 | 

0x000E00

 | 

Imaging device.

 |
| 

DEVICE\_SMART\_TV

 | 

0x000E01

 | 

Smart TV.

 |
| 

DEVICE\_IP\_CAMERA

 | 

0x000E02

 | 

IP camera.

 |
| 

DEVICE\_SCREEN\_CASTER

 | 

0x000E03

 | 

Projector.

 |
| 

DEVICE\_NETWORKING

 | 

0x000F00

 | 

Networking device.

 |
| 

DEVICE\_IOT\_GATEWAY

 | 

0x000F01

 | 

IoT gateway.

 |
| 

DEVICE\_ACCESS\_CONTROL

 | 

0x001000

 | 

Access control device.

 |
| 

DEVICE\_INTELLIGENT\_LOCK

 | 

0x001001

 | 

Smart lock.

 |
| 

DEVICE\_SMART\_KEY

 | 

0x001002

 | 

Smart key device.

 |
| 

DEVICE\_VEHICLE\_KEY

 | 

0x001003

 | 

Car key.

**Start version**: 5.1.0(18)

 |
| 

DEVICE\_VEHICLE\_LOCK

 | 

0x001004

 | 

Car lock.

**Start version**: 5.1.0(18)

 |

#### AcbState

Enumerated values of logical link connection statuses with a remote device.

**System capability**: SystemCapability.Communication.NearLink.Core

**Start version**: 5.1.0(18)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DISCONNECTED

 | 

0

 | 

Disconnected.

 |
| 

CONNECTED

 | 

1

 | 

Connected.

 |
| 

ENCRYPTED

 | 

2

 | 

Encrypted.

 |
