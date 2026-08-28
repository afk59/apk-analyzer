# Cross-Device Drag and Drop Development

The cross-device drag-and-drop feature allows the system to automatically complete screen hopping and data transmission across devices. The following walks you through the development process.

#### Constraints

This feature can be used only when the following conditions are met:

-   **Supported devices**
    
    Tablets or 2-in-1 devices running HarmonyOS NEXT Developer Preview0 or later.
    
-   **Constraints**
    -   The same HUAWEI ID is logged on both devices.
    -   Wi-Fi and Bluetooth must be enabled on both devices, and the devices must be connected to the same LAN.
    -   Screen hopping must be enabled.
    -   The resource files preset in the application (that is, the resource files that are contained in the HAP before the application is installed) cannot be dragged and dropped across devices.

#### Available APIs

Before developing a specific function, read the reference documents to obtain the detailed API description.

-   [Drag-and-drop control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-drag-drop): attribute indicating whether the component can respond to drag and drop events. Only the component with the **draggable** attribute set to **true** can respond to drag-and-drop events.
    
    By default, some components support drag-and-drop control. For these components, you only need to set **draggable** to **true**. The system automatically implements the write operation of **onDragStart** or the read operation of **onDrop** based on the component support.
    
-   [Drag-and-drop event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-drag-drop): A drag-and-drop event is triggered when a component is selected and dragged.
    
    Components can be dragged in or out based on service requirements.
    

#### Development Example

Drag-and-drop events are operated and responded by a click on the left mouse button. For details about development examples, see [Drag Event](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-drag-drop).
