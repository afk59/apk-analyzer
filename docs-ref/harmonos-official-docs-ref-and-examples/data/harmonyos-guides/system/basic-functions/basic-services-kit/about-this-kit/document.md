# About This Kit

Basic Services Kit provides basic capabilities for application developers, from pasteboard read/write, file upload/download, file compression, file printing, inter-process/inter-thread communication, to device and application account management.

#### When to Use

Basic Services Kit is typically used in the following scenarios:

-   Pasteboard read/write
    
    -   Intra-device copy and paste: For example, copy a piece of text in application A and paste it to another application.
    -   Cross-device copy and paste: For example, copy a piece of text in a browser on device A and paste it to a notes application on device B.
-   File upload and download
    
    -   Upload and download in the foreground: usually involves small data volume and real-time feedback. Examples: send social media posts (such as images and short videos), share files with friends, and save images to the local device.
    -   Upload and download in the background: usually involves large data volume and resumable transfers. Examples: cloud-device data synchronization and movie download.
-   Inter-process/Inter-thread communication
    
    -   Inter-process communication: For example, an ExtensionAbility sends events to the main process.
    -   Inter-thread communication: For example, after processing a network request, the worker thread transfers the event back to the UI main thread.

#### Capability Scope

Depending on different use cases, this kit provides the following capabilities:

-   Data file processing
    
    -   [Pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard): provides the copy and paste support. You can use the provided APIs to operate pasteboard content of the plain text, HTML, URI, pixel map, and other types.
    -   [Compression](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-zlib): provides APIs for file compression and decompression.
    -   [Print](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-print): provides APIs for basic print operations, for example, transferring files for printing and setting printing parameters.
    -   [Upload and download](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-request): provides basic upload, download, and background transmission agent capabilities.
-   Inter-process/Inter-thread communication
    
    -   [Common event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-commoneventmanager): provides inter-process communication capabilities, including the capabilities to publish, subscribe to, and unsubscribe from common events. For details about the development guide, see [Introduction to Common Events](../process-and-thread-communication/using-common-events-for-ipc/introduction-to-common-events/document.md).
    -   [Emitter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-emitter): provides intra-thread communication capabilities, including the capabilities to publish, subscribe to, and unsubscribe from custom events. For details about the development guide, see [Using Emitter for Inter-Thread Communication](../process-and-thread-communication/using-emitter-for-inter-thread-communication/document.md).
-   Device management
    
    -   [Device information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-device-info): provides APIs for querying product information, such as the device type, device brand, product series, and product version.
    -   [Data item settings](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-settings): provides APIs for setting data items, such as airplane mode and explore by touch.
    -   [Battery information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-battery-info): provides APIs for querying the battery information.
    -   [Power management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-power): provides system power management capabilities, such as querying the screen status.
    -   [Running lock](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-runninglock): provides APIs for creating, querying, holding, and releasing running locks.
    -   [Thermal management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-thermal): provides thermal management capabilities, such as thermal level query.
    -   [USB management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager): provides USB device management capabilities, including USB device list query, bulk data transfer, control transfer, and permission control. For details about the development guide, see [USB Service Development Overview](../usb-service/developing-usb-services/usb-service-development-overview/document.md).
-   Others
    
    -   [Application account management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-appaccount): provides application account management and data management capabilities. For details, see [Managing Application Accounts](../account-management/application-accounts/managing-application-accounts/document.md).
    -   [Public callback information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base): defines the public callback types of ArkTS APIs, including the common and error callbacks.
    -   [Time and time zone](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-date-time): provides APIs for obtaining the system time and time zone.

#### Relationship with Other Kits

-   [ArkTS Kit](../../../../application-framework/arkts/about-this-kit/document.md): [Multithreaded concurrency (TaskPool and Worker)](../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/overview-of-multithreaded-concurrency/document.md) in ArkTS Kit needs to use Emitter in this kit for inter-thread communication.
    
-   [Ability Kit](../../../../application-framework/ability-kit/about-this-kit/document.md): Common events in this kit are required for inter-process communication in Ability Kit.
    
-   [Core File Kit](../../../../application-framework/core-file-kit/about-this-kit/document.md): Core File Kit provides file access and management capabilities. You can use Core File Kit for application file access, file sharing, and data backup and restore, and use this kit to implement file compression, file upload and download, and file printing.
