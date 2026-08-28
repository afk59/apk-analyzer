# USB Service Development Overview

#### Basic Concepts

The USB service is an abstraction of underlying hardware-based USB devices. It is classified into a host and a device.

In a host, with the APIs provided by the USB service, you can obtain the list of connected USB devices, manage device access permissions, and perform data transfer or control transfer with the connected devices. In addition, for transfer modes, synchronous transfer and asynchronous transfer are available; for transfer types, interrupt transfer, isochronous transfer, and bulk transfer are supported. Before data transfer, you need to obtain the device list, verify the device access permission, enable or connect to the device, and declare the device APIs.

#### Working Principles

The USB subsystem logically consists of three parts: USB API, USB Service, and USB HAL. The following figure shows how the USB service is implemented.

**Figure 1** Implementation of the USB service

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/fTmRi2Y3RBavDv2MyZGrfQ/en-us_image_0000002537765098.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82C7F68A5A62CA1E9E50451AC46521ED69F8E78AAC44D49B3B005CBC99845156)

-   USB API: provides USB APIs that implement various basic functions, for example, query of the USB device list, bulk data transfer, control transfer, and permission control.
    
-   USB Service: receives, parses, and distributes Hardware Abstraction Layer (HAL) data, and manages devices.
    
-   USB HAL: provides driver capability APIs that can be directly called in user mode.
