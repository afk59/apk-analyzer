# About This Kit

Audio and Video Session (AVSession) Kit provides the audio and video management service, which manages the playback behavior of all audio and video applications in the system in a unified manner. You can use the kit to quickly build unified audio and video display and control capabilities.

#### Capability Scope

-   Unified audio and video management: Audio and video applications access AVSession and send it application data (for example, the song that is being played and the playback state). Through a controller, the user can choose another application or device for playback.
    
-   Restricted audio background playback: After an audio application accesses AVSession, it can continue audio playback in the background. To use this feature, the application must also request a [continuous task](../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).
    

#### Highlights

-   Consistent user experience
    
    Audio and video applications access AVSession and send it application data (for example, the song that is being played and the playback state).
    
    Through a controller, the user can choose another application or device for playback.
    
-   Standardize background playback management
    
    Through the controller, the background playback of applications is visible and controllable.
    
    The system enforces strict control over background playback. For applications that have not integrated with AVSession or for applications that have integrated with AVSession but do not have a valid AVSession instance when they move to the background, their audio playback is forcibly paused. This addresses the issue of applications playing audio maliciously in the background, making it difficult for users to locate and close the offending application.
    

#### Basic Concepts

Be familiar with the following basic concepts before development:

-   AVSession
    
    For AVSession, one end is the audio and video applications under control, and the other end is a controller (for example, Media Controller or AI Voice). AVSession provides a channel for information exchange between the application and controller.
    
-   Provider
    
    An audio and video application that accesses the AVSession service. After accessing AVSession, the audio and video application must provide the media information, for example, the name of the item to play and the playback state, to AVSession. Through AVSession, the application also receives control commands from the controller and responds accordingly.
    
-   Controller
    
    A system application that accesses AVSession to provide global control on audio and video playback behavior. Typical controllers are Media Controller and AI Voice. The following sections use Media Controller as an example of the controller. After accessing AVSession, the controller obtains the latest media information and sends control commands to the audio and video applications through AVSession.
    
-   AVSessionController
    
    An object that controls the playback behavior of the provider. It obtains the playback information of the audio and video application and listens for the application playback changes to synchronize the AVSession information between the application and controller. The controller is the holder of an AVSessionController object.
    
-   AVSessionManager
    
    An object that provides the capability of managing sessions. It can create an AVSession object, create an AVSessionController object, send control commands, and listen for session state changes.
    

#### AVSession Interaction Process

AVSessions are classified into local AVSessions and distributed AVSessions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/N8cgRkWUQcGjol3h9dlY_w/en-us_image_0000002537925110.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3CAC0A7946ACC05443B2921424C8ED5FF5EF7E5D08050C758ABFF20A89B9A03)

-   Local AVSession
    
    Local AVSession establishes a connection between the provider and controller in the local device, so as to implement unified playback control and media information display for audio and video applications in the system.
    
-   Distributed AVSession
    
    Distributed AVSession establishes a connection between the provider and controller in the cross-device scenario, so as to implement cross-device playback control and media information display for audio and video applications in the system. For example, you can project the content played on device A to device B and perform playback control on device B.
    

#### Constraints

All audio and video applications that need to be played in the background must be connected to AVSession and background task management. Otherwise, audio playback is forcibly paused when such an application switches to the background.

#### Relationship with Related Kits

To implement background playback, an application needs to use the capabilities of [Background Tasks Kit](../../../application-framework/background-tasks-kit/about-this-kit/document.md) to request a continuous task to avoid being suspended.
