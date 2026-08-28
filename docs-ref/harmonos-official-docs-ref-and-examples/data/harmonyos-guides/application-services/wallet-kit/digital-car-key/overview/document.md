# Overview

Wallet Kit provides the digital car key capability to simulate physical car keys based on Huawei's "chip-device-cloud" technologies. Such digital car keys are more secure and meet the Intelligent Car Connectivity Industry Ecosystem Alliance (ICCE) standards.

With this capability integrated, a user's device that is connected with a car through Bluetooth or NFC can be used as a key to unlock and start the car. Security of the service is ensured by SE and TEE.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/o7PqqBw5T8uPOsQj-rUTKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFD112765A2EC221D29072ECAFADC29462EA4DDDCBEDC7EACDF8391A7E81C0EE)

This function is supported only in the Chinese mainland.

#### Overall Architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/i1SO4JJcRjCkRbsiKG9iug/en-us_image_0000002183081154.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9823F2798DFE1E66AC895B65FD5D6F1A44197EE8380995CFF300F4093A1BF7F1)

## Roles Involved

| 
Role

 | 

Description

 |
| :-- | :-- |
| 

DK

 | 

Digital key.

 |
| 

Car key applet

 | 

Huawei provides a secure channel for automotive manufacturers to write the key and unique data to an applet instance.

 |
| 

BLE

 | 

Bluetooth Low Energy.

 |
| 

NFC

 | 

Near field communication.

 |

## Typical Service Interaction

When a user applies to enable a digital key in the car owner app on the phone:

The DK management service sends the key card information to HUAWEI Wallet through the HUAWEI Wallet server and writes the information to the car key applet instance of the mobile security chipset.

The car communicates with the mobile device in either of the following modes:

-   Through the NFC module (usually located in the driver-side rearview mirror or B-pillar): The car communicates with the mobile security chipset through the NFC channel.
-   Through the BLE module: The car communicates with the mobile security chipset through HUAWEI Wallet using Bluetooth.
