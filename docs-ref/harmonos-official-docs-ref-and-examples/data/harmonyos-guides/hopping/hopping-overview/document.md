# Hopping Overview

#### Application Scenarios

As the all-scenario, multi-device lifestyle becomes popular, users have an increasing number of devices. Each device provides users with what they need in a certain scenario. For example, watches allow users to view information in a timely manner, and smart TVs deliver an immersive watching experience. However, each device has its limitations. For example, typing text on a smart TV is frustrating as it is much more difficult than on a mobile device. If multiple devices can sense each other through a distributed OS and together form a Super Device, the strengths of each device can be fully exerted, thereby providing a more natural and smoother distributed experience for users.

Hopping allows distributed operations across devices that run HarmonyOS. It includes cross-device migration and multi-device collaboration.

#### Basic Concepts

-   **Hopping**
    
    Hopping allows distributed operations across multiple devices that run HarmonyOS. It breaks boundaries of devices and enables multi-device collaboration, achieving precise control, universal coordination, and seamless hops of user applications. For example, a user can edit the same email, carry out fitness, or play a game across devices. Hopping provides broad application scenarios, innovative product perspectives, enhanced product advantages, and superior experience. Hopping includes **cross-device migration** and **multi-device collaboration**.
    
-   **Cross-device migration**
    
    When the environment changes, for example, when a user goes outdoors or when a more appropriate device is detected, the user can migrate an ongoing task to another device for better experience. The application on the source device can automatically exit, depending on the setting.
    
    A typical cross-device migration scenario is as follows: You migrate a video playback task from a tablet to a smart TV. The video application on the tablet exits.
    
    From the perspective of application development, cross-device migration enables the UIAbility component running on device A to migrate to and keep running on device B. After the migration is complete, the UIAbility component on device A automatically exits (depending on the setting).
    
-   **Multi-device collaboration**
    
    Multi-device collaboration provides users with more efficient and immersive experience than with a single device.
    
    Multi-device collaboration is used in the following typical scenarios:
    
    Scenario 1: You open the same note on devices A and B. On device A, you select images from the local Gallery, insert them to the note, and edit them. On device B, you edit the text.
    
    Scenario 2: You are chatting with a customer on device A, and the customer asks for a file, which is stored on device B. You can use the chat software to open the file application on device B, select the required file, and send it back to device A. Then, you use the chat software to send it to the customer.
    
    From the perspective of application development, multi-device collaboration enables different UIAbility or ServiceExtensionAbility components to run simultaneously or alternately on multiple devices to provide a complete service, or enables the same UIAbility and ServiceExtensionAbility component to run simultaneously on multiple devices to provide a complete service.
    

#### Typical Scenarios

-   Cross-device migration
    -   [Media playback control](../../media/avsession-kit/distributed-avsession/using-avcastpicker/introduction-to-playback-control/document.md): allows audio to be easily and smoothly played across HarmonyOS devices that form a Super Device. For example, the user can switch the audio played on a smartphone to a 2-in-1 device without any interruption.
    -   [Application continuation](../application-continuation/application-continuation-overview/document.md): allows the operations performed by a user on one device to be quickly switched and seamlessly continued in the same application on another device.
-   Multi-device collaboration
    -   [Cross-device drag-and-drop](../cross-device-drag-and-drop/cross-device-drag-and-drop-overview/document.md): allows the keyboard and mouse to be shared across devices. Files and texts can be dragged and dropped between tablets or any 2-in-1 devices.
    -   [Cross-device pasteboard](../cross-device-pasteboard/cross-device-pasteboard-overview/document.md): allows a user to copy a piece of text in the application of device A and paste it to the application of device B, achieving efficient content sharing across devices.
    -   [Device interconnectivity](../../system/network/service-collaboration-kit/device-interconnectivity-arkts/introduction-to-device-interconnectivity/document.md): enables a tablet or 2-in-1 device to use the camera, scanning, gallery, and other features of a smartphone.
