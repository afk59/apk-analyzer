# About This Kit

Graphics Accelerate Kit is a comprehensive solution that combines advanced graphics rendering acceleration and resource management optimization. It aims to enhance the performance and user experience of graphics processing apps through hardware-software co-optimization. It applies to scenarios such as gaming, augmented reality (AR), virtual reality (VR), UI interaction rendering, and 3D animation. Gaming, in particular, exemplifies a GPU-intensive rendering use case on devices. This kit provides three core services: game rendering acceleration service, game resource acceleration service, and game launch acceleration service.

#### Service Introduction

-   Game Rendering Acceleration Service
    
    The game rendering acceleration service is a system-level graphics acceleration solution featuring hardware-software synergy. It helps game apps quickly build rendering acceleration capabilities such as frame generation, adaptive buffer resolution (ABR), and Open GPU Turbo X (OpenGTX), addressing the pain points such as unsmooth game running, frame freezing or loss, and overheating after long-time running.
    
    | 
    Functional Module
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    [Frame generation](../game-rendering-acceleration-service/developing-the-frame-generation-capability/document.md)
    
     | 
    
    In game scenes of high target frame rates with heavy GPU loads, the frame generation capability uses the hardware-software integrated motion estimation and motion compensation (MEMC) technology to efficiently insert predicted frames between real frames in a game, based on the time-domain and spatial-domain information in render pipelines. This not only maintains the original image quality to the maximum extent but also remarkably improves the game frame rate and smoothness, achieving lower system load and power consumption as well as longer phone battery life.
    
     |
    | 
    
    [ABR](../game-rendering-acceleration-service/developing-the-abr-capability/document.md)
    
     | 
    
    In game scenes of heavy GPU loads, the ABR capability detects the game and device status, adaptively determines the scale factor of resolutions, and adjusts the resolutions based on framebuffers (buffers for short hereinafter). It helps game apps achieve a more stable frame rate and lower power consumption.
    
     |
    | 
    
    [OpenGTX](../game-rendering-acceleration-service/developing-the-opengtx-capability/document.md)
    
     | 
    
    In game scenes of high frame rates and heavy loads, the OpenGTX capability uses the low-temperature polycrystalline oxide technology (LTPO, for a dynamic frame rate or refresh rate) to detect the game rendering status, game scenes, and device status in real time and adaptively adjust the game frame rate and the System on Chip (SoC) frequency or Double Data Rate (DDR) frequency of devices. This effectively reduces the system load and power consumption without affecting user experience.
    
     |
    

-   Game Resource Acceleration Service
    
    The game resource acceleration service uses technologies such as background task scheduling and preloading to efficiently update and manage resource packages in the background. This helps reduce player waiting time and enhance retention by providing a faster, smoother game launch experience.
    
    | 
    Functional Module
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    [Resource package background download](../game-resource-acceleration-service/resource-package-background-download/document.md)
    
     | 
    
    The resource package background download function silently downloads resource files, such as level packages, 3D character models, and textures, to user devices, minimizing the time users have to wait for resource download after launching a game. This addresses the problem of slow game launch, providing users with an instant play experience.
    
     |
    

-   Game Launch Acceleration Service
    
    The game launch acceleration service utilizes the precise restoration technology based on game memory snapshots, enabling a game to launch in just a few seconds and allowing players to enjoy a high-quality gaming experience.
    
    | 
    Functional Module
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    [Second-level game launch](../game-launch-acceleration-service/second-level-game-launch/document.md)
    
     | 
    
    The second-level game launch function enables the system to automatically create a memory snapshot when a game exits. During the next cold start, the game can directly load this memory snapshot for instant game launch and access, eliminating the usual lengthy loading process and significantly enhancing the gameplay experience.
    
     |
    

#### Restrictions

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Supported Devices

| 
Core Service

 | 

Supported Devices

 |
| :-- | :-- |
| 

Game rendering acceleration service

 | 

Phones and tablets

 |
| 

Game resource acceleration service

 | 

Phones and tablets

 |
| 

Game launch acceleration service

 | 

Phones and tablets

 |

#### Supported Emulators

Currently, this kit does not support emulators.
