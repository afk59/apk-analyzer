# AVSession Provider (C/C++)

The OHAVSession module provides C APIs to implement an AVSession provider. An audio and video application needs to access the AVSession service as a provider in order to display media information in the controller (for example, Media Controller) and respond to playback control commands delivered by the controller.

#### Prerequisites

To use [native\_avsession.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avsession-h) to implement media sessions, add the corresponding header files.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(entry PUBLIC libohavsession.so)

## Including Header Files

#include <multimedia/av\_session/native\_avmetadata.h>
#include <multimedia/av\_session/native\_avsession.h>
#include <multimedia/av\_session/native\_avsession\_errors.h>

#### How to Develop

To access a local session with the NDK, perform the following steps:

1.  Create a session and activate the media. Specifically, pass the session type (specified by **AVSession\_Type**), custom tag, bundle name, and ability name.
    
    OH\_AVSession\* avsession;
    OH\_AVSession\_Create(SESSION\_TYPE\_AUDIO, "testsession", "com.example.application", "MainAbility", &avsession);
    OH\_AVSession\_Activate(avsession);
    
    **AVSession\_Type** can be set to any of the following types:
    
    -   SESSION\_TYPE\_AUDIO
    -   SESSION\_TYPE\_VIDEO
    -   SESSION\_TYPE\_VOICE\_CALL
    -   SESSION\_TYPE\_VIDEO\_CALL
2.  Set the metadata of the media asset to be played.
    
    To set metadata, use **OH\_AVMetadataBuilder** to construct specific data, generate an OH\_AVMetadata instance, and then call the APIs of **OH\_AVMetadata** to set the asset.
    
    The code snippet below shows how to call **OH\_AVMetadataBuilder** to construct metadata:
    
    // Create an OH\_AVMetadataBuilder.
    OH\_AVMetadataBuilder\* builder;
    OH\_AVMetadataBuilder\_Create(&builder);
        
    OH\_AVMetadata\* ohMetadata;
    OH\_AVMetadataBuilder\_SetTitle(builder, "Anonymous title");
    OH\_AVMetadataBuilder\_SetArtist(builder, "Anonymous artist");
    OH\_AVMetadataBuilder\_SetAuthor(builder, "Anonymous author");
    OH\_AVMetadataBuilder\_SetAlbum(builder, "Anonymous album");
    OH\_AVMetadataBuilder\_SetWriter(builder, "Anonymous writer");
    OH\_AVMetadataBuilder\_SetComposer(builder, "Anonymous composer");
    OH\_AVMetadataBuilder\_SetDuration(builder, DURATION\_TIME); // DURATION\_TIME = 3600
    // MediaImageUri can only be set to a network address.
    OH\_AVMetadataBuilder\_SetMediaImageUri(builder, "https://xxx.xxx.xx");
    OH\_AVMetadataBuilder\_SetSubtitle(builder, "Anonymous subtitle");
    OH\_AVMetadataBuilder\_SetDescription(builder, "For somebody");
    // Lyric can only be set to the lyric content. (The application must combine the lyric content into a string.)
    OH\_AVMetadataBuilder\_SetLyric(builder, "balabala");
    OH\_AVMetadataBuilder\_SetAssetId(builder, "000");
    OH\_AVMetadataBuilder\_SetSkipIntervals(builder, SECONDS\_30);
    OH\_AVMetadataBuilder\_SetDisplayTags(builder,  AVSESSION\_DISPLAYTAG\_AUDIO\_VIVID);
    
    /\*\*
     \* Generate an AVMetadata object.
     \*/
    OH\_AVMetadataBuilder\_GenerateAVMetadata(builder, &ohMetadata);
        
    /\*\*
     \* Set the AVMetadata object.
     \*/
    OH\_AVSession\_SetAVMetadata(avsession, ohMetadata);
    
    When the AVMetadata is no longer needed, call **OH\_AVMetadataBuilder\_Destroy** to destroy it and do not use it anymore.
    
    OH\_AVMetadata\_Destroy(ohMetadata);
    OH\_AVMetadataBuilder\_Destroy(builder);
    
3.  Update the media playback status information.
    
    The information includes the playback state, playback position, playback speed, and favorite status. You can use the APIs to set the information.
    
    AVSession\_ErrCode ret = AV\_SESSION\_ERR\_SUCCESS;
        
    // Set the playback state, which is in the range \[0,11\].
    AVSession\_PlaybackState state = PLAYBACK\_STATE\_PREPARING;
    ret = OH\_AVSession\_SetPlaybackState(avsession, state);
    // ...
        
    // Set the playback position.
    AVSession\_PlaybackPosition\* playbackPosition = new AVSession\_PlaybackPosition;
    playbackPosition->elapsedTime = ELAPSED\_TIME; // ELAPSED\_TIME = 1000
    playbackPosition->updateTime = UPDATE\_TIME; // UPDATE\_TIME = 16111150
    ret = OH\_AVSession\_SetPlaybackPosition(avsession, playbackPosition);
    
4.  Listen for playback control commands delivered by the controller, for example, Media Controller.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/D8ojSa9rRwSdJfrqGUay2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2A6DDCA61D67A75F121EBAAB0EF8FE3441429EB44CC6B8BE3749A6A9A9D1EB7)
    
    After the provider registers a listener for fixed playback control commands, the commands will be reflected in **getValidCommands()** of the controller. In other words, the controller determines that the command is valid and triggers the corresponding event as required. To ensure that the playback control commands delivered by the controller can be executed normally, the provider should not use a null implementation for listening.
    
    To avoid any exception, call the API to unregister the listener when the service ends.
    
    Currently, the following playback control commands are supported:
    
    -   Play
    -   Pause
    -   Stop
    -   Play previous
    -   Play next
    -   Rewind
    -   Fast forward
    -   Seek
    -   Favorite
    
    // Register the callbacks for the commands of play, pause, stop, play previous, and play next.
    // CONTROL\_CMD\_PLAY = 0; play.
    // CONTROL\_CMD\_PAUSE = 1; pause.
    // CONTROL\_CMD\_STOP = 2; stop.
    // CONTROL\_CMD\_PLAY\_NEXT = 3; play next.
    // CONTROL\_CMD\_PLAY\_PREVIOUS = 4; play previous.
    AVSession\_ControlCommand command = CONTROL\_CMD\_PLAY;
    OH\_AVSessionCallback\_OnCommand commandCallback = \[\](OH\_AVSession\* session, AVSession\_ControlCommand command,
        void\* userData) -> AVSessionCallback\_Result {
        return AVSESSION\_CALLBACK\_RESULT\_SUCCESS;
    };
    int userData = 0;
    OH\_AVSession\_RegisterCommandCallback(avsession, command, commandCallback, (void \*)(&userData));
        
    // Register the callback for the fast-forward operation.
    OH\_AVSessionCallback\_OnFastForward fastForwardCallback = \[\](OH\_AVSession\* session, uint32\_t seekTime,
        void\* userData) -> AVSessionCallback\_Result {
        return AVSESSION\_CALLBACK\_RESULT\_SUCCESS;
    };
    OH\_AVSession\_RegisterForwardCallback(avsession, fastForwardCallback, (void \*)(&userData));
    
    The related callbacks are as follows:
    
    | API | Description |
    | :-- | :-- |
    | OH\_AVSession\_RegisterCommandCallback(OH\_AVSession\* avsession, AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback, void\* userData) | Registers a callback for a common playback control command, which can be play, pause, stop, play previous, or play next. |
    | OH\_AVSession\_RegisterForwardCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnFastForward callback, void\* userData) | Registers a callback for the fast-forward operation. |
    | OH\_AVSession\_RegisterRewindCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnRewind callback, void\* userData) | Registers a callback for the rewind operation. |
    | OH\_AVSession\_RegisterSeekCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSeek callback, void\* userData) | Registers a callback for the seek operation. |
    | OH\_AVSession\_RegisterToggleFavoriteCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnToggleFavorite callback, void\* userData) | Registers a callback for the favorite operation. |
    
5.  When the audio and video application exits and does not need to continue playback, cancel the listener and destroy the AVSession object. The example code is as follows:
    
    OH\_AVSession\_Destroy(avsession);
