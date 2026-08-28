# Implementing Interaction Responses

The ArkUI framework offers a comprehensive set of APIs for handling input events from various peripherals. Beyond basic input handling, ArkUI also provides advanced APIs for responding to normalized user interactions such as gestures, drag and drop, and focus management.

Compared with raw input events, gestures are the preferred method for handling user interactions. Gestures abstract away device-specific differences and represent high-level interaction intent. For example, a tap gesture can be triggered by either a finger touch or a mouse click, and applications only need to bind to the tap gesture to support both input types seamlessly. To deepen your understanding of interaction handling in ArkUI, refer to the following guides:

[Interaction Mechanism Overview](interaction-mechanism-overview/document.md): explains the core concepts and principles behind ArkUI's interaction model.

[Input Devices and Events](input-devices-and-events/document.md): covers raw input events from different devices and how to process them.

[Implementing Gesture Responses](implementing-gesture-responses/document.md): explains how to handle standardized gesture interactions.

[Supporting Unified Drag-and-Drop](implementing-unified-drag-and-drop/document.md): guides you through implementing consistent drag and drop behavior across devices.

[Supporting Focus Processing](implementing-focus-support/document.md): shows how to manage component focus within the UI.

When developing UI components using the NDK, you can add interaction responses through the following resources:

-   [Listening for Component Events](../../using-ndk-apis-to-build-uis/adding-interaction-events/listening-for-component-events/document.md): Learn how to bind basic input events to components.
-   [Binding Gesture Events](../../using-ndk-apis-to-build-uis/adding-interaction-events/binding-gesture-events/document.md): Add gesture support to components for richer interaction.
-   [Drag Event](../../using-ndk-apis-to-build-uis/adding-interaction-events/drag-event/document.md): Implement unified drag and drop functionality using NDK APIs.

-   **[Interaction Response Overview](interaction-response-overview/document.md)**  
    
-   **[Interaction Mechanism Overview](interaction-mechanism-overview/document.md)**  
    
-   **[Input Devices and Events](input-devices-and-events/document.md)**  
    
-   **[Implementing Gesture Responses](implementing-gesture-responses/document.md)**  
    
-   **[Implementing Unified Drag and Drop](implementing-unified-drag-and-drop/document.md)**  
    
-   **[Implementing Focus Support](implementing-focus-support/document.md)**
