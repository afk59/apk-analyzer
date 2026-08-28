# Overview

#### Highlights

-   **Stable frame rate, less frame freezing or loss**
    
    With the frame generation and ABR capabilities, game apps can run more stably and smoothly thanks to higher frame rates and less frame freezing or loss, while keeping almost the same image quality. With the OpenGTX capability, game apps can dynamically adjust their frame rates, refresh rates, and SoC/DDR frequency based on key information such as the game scene and device status, achieving smooth running on devices.
    

-   **Lower power consumption, less heat, and longer battery life**
    
    With the frame generation and ABR capabilities, game apps can run with significantly lower GPU loads and power consumption (the per-frame power consumption can be reduced by 10% or more). This helps mitigate phone heat and extend battery life. With the OpenGTX capability, game apps can control the game frame rate and device SoC/DDR frequency to minimize the performance overhead on devices while maintaining a good gaming experience for users. It also helps reduce power consumption and heat dissipation, prolonging battery life.
    

#### Use Cases

-   Frame generation
    
    To meet the requirements of different game scenes, we provide two frame generation modes: interpolation and extrapolation. The following table describes the application scenarios of each mode.
    
    | 
    Frame Generation Mode
    
     | 
    
    Application Scenarios
    
     |
    | :-- | :-- |
    | 
    
    [Interpolation mode](../developing-the-frame-generation-capability/interpolation-mode/document.md)
    
     | 
    
    Role-playing games, racing games, and other games that have high requirements on rendering quality and running smoothness.
    
     |
    | 
    
    [Extrapolation mode](../developing-the-frame-generation-capability/extrapolation-mode/document.md)
    
     | 
    
    Action games, shooting games, and other games that have high requirements on response latency and operation sensitivity.
    
     |
    
-   ABR
    
    | 
    ABR Policy
    
     | 
    
    Application Scenarios
    
     |
    | :-- | :-- |
    | 
    
    [Perception based on camera motion](../developing-the-abr-capability/document.md)
    
     | 
    
    Racing games, role-playing games, shooting games, and other games with fast on-screen motion. The buffer resolutions are adjusted in game scenes such as speed acceleration, running, and perspective rotation, for a more stable frame rate and lower power consumption, with little perceived impact to image quality.
    
     |
    
-   OpenGTX
    
    The OpenGTX LTPO solution provides three dynamic frame rate or refresh rate control modes for game scenes of high frame rates and heavy loads. The following table describes the application scenarios of each mode.
    
    | 
    LTPO Mode
    
     | 
    
    Application Scenarios
    
     |
    | :-- | :-- |
    | 
    
    SCENE\_MODE
    
     | 
    
    Different frame rates are set for different game scenes, for example, 120 FPS for the "playing" scene.
    
     |
    | 
    
    TOUCH\_MODE
    
     | 
    
    Frame rates are set based on the touch frequency.
    
     |
    | 
    
    ADAPTIVE\_MODE
    
     | 
    
    Frame rates are adaptively controlled based on the scene, camera, and touch frequency.
    
     |
    

#### Scenario Restrictions

-   Frame generation
    -   This capability is most suitable for game scenes of high target frame rates with heavy GPU loads. Using this capability in game scenes with light loads may lead to negative power consumption gains or even blurring artifacts when the target frame rate is lower than 60 FPS.
    -   There are two motion estimation modes, basic mode and enhanced mode, for the frame generation capability. The following table describes the restrictions on the two modes.
        
        | 
        Motion Estimation Mode
        
         | 
        
        Development Preparations
        
         | 
        
        Scenario Restrictions
        
         |
        | :-- | :-- | :-- |
        | 
        
        Basic mode
        
         | 
        
        \-
        
         | 
        
        This mode is applicable to game scenes where the camera or object is still or moving slowly. Using it in scenes of high-speed movements or complex particle effects may cause blurring artifacts and ghosting.
        
         |
        | 
        
        Enhanced mode
        
         | 
        
        You need to mark the draw calls for drawing vertices. Compared with the basic mode, the enhanced mode uses the vertex information in 3D scenes for more accurate motion estimation, achieving a better frame generation effect.
        
         | 
        
        1\. The frame generation effect works well for game scenes where the camera or object is moving either slowly or quickly. Compared with the **basic mode**, it significantly mitigates blurring artifacts. However, ghosting may occur in scenes of complex particle effects.
        
        2\. The enhanced frame generation mode is supported only by the OpenGL ES graphics API and is not supported by Vulkan.
        
         |
        
    -   The frame generation APIs cannot be called concurrently.
-   ABR
    -   Currently, the ABR capability supports adaptive resolution adjustment for only one buffer in each API call. You need to enable this capability for a buffer corresponding to a pass with heavy GPU loads in game rendering pipelines.
    -   The ABR APIs cannot be called concurrently.
-   OpenGTX
    -   Device specifications: The devices must support LTPO screens.
