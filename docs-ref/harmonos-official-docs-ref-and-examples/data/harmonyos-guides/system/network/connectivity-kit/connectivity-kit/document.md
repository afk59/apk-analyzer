# Connectivity Kit

#### About This Kit

Mobile devices have become an integral part of everyday life. For example, people listen to music with Bluetooth headphones, surf the Internet over Wi-Fi, and use their mobile phone as a transit pass or credit card.

In these applications, NFC implements short-range interactions like payments and access control, Bluetooth provides basic wireless connections for devices, such as headphones, wearables, and peripheral devices, and Wi-Fi provides high-speed Internet access.

You can use Connectivity Kit to design mobile applications to meet diverse user needs in their daily lives.

## Bluetooth

Bluetooth is a wireless communication technology that implements short-range data transmission. The Bluetooth technical specifications are formulated by the Bluetooth Special Interest Group (SIG). It can be used to connect a variety of devices, including smartphones, headsets, speakers, keyboards, mouse devices, and printers. Bluetooth features low power consumption, low cost, and ease of use.

Different Bluetooth modules provide APIs applicable to different scenarios, helping developers develop Bluetooth-related features.

-   **ACCESS module**
    
    Provides capabilities such as enabling and disabling Bluetooth and obtaining the Bluetooth status. You need to enable Bluetooth through this module before using other Bluetooth functions. For details, see [@ohos.bluetooth.access](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-access).
    
-   **CONNECTION module**
    
    Provides capabilities such as discovering and pairing Bluetooth devices, as well as obtaining information about the local and peer devices. For details, see [@ohos.bluetooth.connection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-connection).
    
-   **BLE module**
    
    Provides Bluetooth Low Energy (BLE) capabilities, such as discovering devices, sending advertising packets, discovering services, and transmitting data. For details, see [@ohos.bluetooth.ble](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-ble).
    
-   **SOCKET module**
    
    Provides capabilities such as connecting and transmitting data between Bluetooth devices over Serial Port Profile (SPP). For details, see [@ohos.bluetooth.socket](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-socket).
    
-   **A2DP module**
    
    Establishes Bluetooth connections between devices and transmits high-quality audio over Advanced Audio Distribution Profile (A2DP). For example, this module enables transmission of audio data streams between a phone and audio peripherals (such as headsets and speakers) for music streaming playback. For details, see [@ohos.bluetooth.a2dp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-a2dp).
    
-   **HFP module**
    
    Establishes connections between Bluetooth devices and enables hands-free calls over the Hands-Free Profile (HFP), supporting functions such as two-way voice call and control. For details, see [@ohos.bluetooth.hfp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-hfp).
    
-   **HID module**
    
    Implements communication, wireless control, and data transmission between Bluetooth devices over Human Interface Device Profile (HID). For example, this module enables low-latency bidirectional communication between devices such as keyboards, mouse devices, and gamepads and hosts (such as phones, tablets, and PCs). For details, see [@ohos.bluetooth.hid](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-hid).
    
-   **PAN module**
    
    Implements network sharing between devices over Personal Area Network (PAN). For example, this module supports Internet sharing between a phone and a PC. For details, see [@ohos.bluetooth.pan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-pan).
    
-   **MAP module**
    
    Implements message sharing between devices over Message Access Profile (MAP). For example, this module supports SMS message synchronization between a phone and a head unit. For details, see [@ohos.bluetooth.map](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-map).
    
-   **PBAP module**
    
    Implements phone book data sharing between devices over Phone Book Access Profile (PBAP). For example, this module supports synchronization of contact and call log data between a phone and a head unit. For details, see [@ohos.bluetooth.pbap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-pbap).
    

## WLAN

A wireless local area network (WLAN) uses the radio, infrared, or other technologies to transmit data between devices that are not physically connected with each other. It is widely used in offices and public places where mobile devices are used.

The WLAN system provides users with WLAN access (STA mode), peer-to-peer data transmission (P2P mode), and hotspot sharing (AP mode).

-   STA mode
    
    The device in Station (STA) mode can be considered as a client of an existing wireless network. It can be connected to another routing network, such as a home router, to provide uplink data services. For details, see [@ohos.wifiManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-wifimanager).
    
-   P2P mode
    
    The P2P mode is also called Wi-Fi Direct, which allows two devices to establish a direct Wi-Fi connection without an intermediary wireless access point (AP). It can set up a TCP/IP connection between two STAs without an AP. Of the two STAs, one is called the group owner (GO), which serves as a traditional AP; the other is called a group client (GC), which connects to the GO like an AP. For details, see [@ohos.wifiManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-wifimanager).
    
-   AP mode
    
    In AP mode, the Wi-Fi module provides downlink data services for the devices (clients) that join the WLAN. It creates a WLAN, like a central device, allowing other devices to connect to this network. For details, see [@ohos.wifiManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-wifimanager).
    

## NFC

The Near Field Communication (NFC) service provides functionalities such as NFC switch control, NFC tag reading and writing, and NFC card emulation.

-   NFC control
    
    The **nfc.controller** module provides APIs for enabling and disabling NFC. To call the APIs provided by this module, the application must have the ohos.permission.MANAGE\_SECURE\_SETTINGS permission, which is available only for system applications. That is, only system applications can enable or disable NFC. For details, see [@ohos.nfc.controller](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-nfccontroller).
    
-   NFC tag reading and writing
    
    The **nfc.tag** module provides APIs for discovering NFC tags, dispatching NFC tags to applications, and enabling applications to read or write NFC tags. You need to declare the NFC tag read/write capability for your application in the specified format, so that the application can receive NFC tags dispatched. For details, see [@ohos.nfc.tag](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-nfctag).
    
-   NFC card emulation
    
    The **cardEmulation** module provides APIs for implementing payment card and access card solutions. You need to declare the NFC card emulation capability for your application in the specified format so that the application can implement NFC communications. For details, see [@ohos.nfc.cardEmulation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cardemulation).
    

## Working Principles

Connectivity Kit provides basic communication services for applications. Before a communication service is used by an application, the related feature must be enabled or a connection must be set up. When the service ends, the connection must be closed actively.

## Constraints

Device capabilities can be used only after the related switch is enabled after user authorization. Otherwise, the system does not provide services for third-party applications.

## Related Samples

The following samples are provided to help you better understand how to develop Bluetooth-related services:

-   [bluetooth](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Connectivity/Bluetooth)
