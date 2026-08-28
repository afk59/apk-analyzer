# About This Kit

Distributed Service Kit implements distributed device management, distributed hardware management, distributed keyboard and mouse traversal, and distributed component management.

Distributed services are underpinned by distributed device management, which involves discovering and authenticating nearby devices, querying device information, and listening for device status. That is, distributed services can be performed only between authenticated devices.

You can implement cross-application collaboration by referring to [Cross-Device UIAbility Connection Development](../distributed-ability-connection-management/cross-device-uiability-connection-development/document.md). After the same account is logged in to devices and networking is successful, an application can start a [UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability) of the same application across devices to implement interaction of information, byte streams, images, and transmission streams.

#### Working Principles

The application is required to initiate a request for device discovery, authentication, query, and listening.

#### Constraints

The application needs user authorization before implementing distributed device management.
