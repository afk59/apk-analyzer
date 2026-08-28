# About This Kit

ArkGraphics 2D provides APIs for drawing and displaying graphics. With this set of APIs, you'll find your application development easier and more efficient.

#### Available Capabilities

-   Basic image processing capabilities, including brightness adjustment, blurring, grayscale adjustment, and color picker. For details, see [@ohos.effectKit (Image Effects)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-effectkit).
    
-   Basic capabilities for creating and managing color space objects and obtaining basic color space attributes. For details, see [@ohos.graphics.colorSpaceManager (Color Space Management)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-colorspacemanager) and [@ohos.graphics.sendableColorSpaceManager (Sendable Color Space Management)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-sendablecolorspacemanager).
    
-   Capabilities for specifying the frame rate based on the type of content. For details, see [Introduction to Variable Frame Rate](../using-variable-frame-rates/introduction-to-variable-frame-rates/document.md).
    
-   High Dynamic Range (HDR) capability. For details, see [@ohos.graphics.hdrCapability (HDR Capability)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hdrcapability).
    
-   Self-drawing capabilities, which you can use to customize and draw UI effects, basic shapes, texts, and images. For details, see [@ohos.graphics.drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-graphics-drawing).
    
-   Native capabilities related to graphics drawing and display. For details, see [NativeWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativewindow), [NativeBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativebuffer), [NativeImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-nativeimage), [NativeVsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativevsync), and [Drawing](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing).
    

#### Use Scenarios

-   Image effect processing: You can use the [effectKit module](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-effectkit) to process image effects based on UI effect requirements.
    
-   Setting color spaces: You can use image files and set color space information based on design requirements to draw and display images with a wide color space effect.
    
-   Frame rate customization: You can customize the frame rate for drawing based on different content and requirements. For example, you can set different frame rates for different gaming scenarios and screens to smoothen user experience and balance power consumption.
    
-   Self-drawing scenario: You can use Drawing and other modules to draw and display custom components (except the ArkUI components) or custom UI effects based on different UI effects and scenario requirements.
    

#### Features

-   Multiple frame rates in the same window: Different frame rates can be customized for different content in the same window, such as animations or self-drawing UIs. Different content runs independently.
    
-   Dynamic frame rate configuration: A third-party framework can dynamically request the frame rate for drawing based on UI scenarios, such as gaming and videos.
    
-   Recording playback: Recording commands can be cached and drawing commands can be played back to improve UI drawing efficiency.
    
-   Multiple rendering backends: A set of code can be used for multiple rendering backends. This reduces multi-device adaptation costs and meets differentiated application requirements.
