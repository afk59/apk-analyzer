# Using SoundPool to Play Short Sounds (ArkTS)

The [SoundPool](../../../about-this-kit/document.md#soundpool) class provides APIs to implement low-latency playback of short sounds.

Short sound effects (such as the camera shutter sound effect and system notification sound effect) are often required during application development. You can call the APIs provided by SoundPool to implement one-time loading of short sounds and multiple times of low-latency playback.

SoundPool currently supports playing of audio files that are under 1 MB in size after decoding. For audio files that exceed this limit after decoding, only the first 1 MB of data is played. This is equivalent to approximately 5.6 seconds of audio duration at a 44.1 kHz sampling rate with 16-bit depth for stereo sound. (At lower sampling rates or in mono mode, the duration may be slightly longer.)

This topic walks you through on how to use the SoundPool APIs to implement low-latency playback. For details about the API, see [SoundPool](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-multimedia-soundpool).

The full process includes creating a SoundPool instance, loading a sound (including decapsulation and decoding), setting playback parameters (loop mode, and playback priority), playing the sound, stopping the playback, and releasing the instance. (For details about the decoding formats, see [Audio Decoding](../../../../avcodec-kit/audio-and-video-codecs/audio-decoding/document.md).)

During application development, you must subscribe to playback state changes and call the APIs in the defined sequence. Otherwise, an exception or undefined behavior may occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/UkLtgWGgSeGa58sEwAolVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062042Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED3A7EC6D9E6865BBE5C753CAB498C26F291AAAC4C735FF3400225E9EF0986E3)

For details about the audio focus strategy when SoundPool is used to play short sounds, see [Introduction to Audio Focus and Audio Session](../../../../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md).

#### How to Develop

1.  Call [createSoundPool](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-f#mediacreatesoundpool10-1) to create a SoundPool instance.
    
    import { media } from '@kit.MediaKit';
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private soundPool: media.SoundPool | undefined = undefined;
    // If the value of usage in audioRenderInfo is STREAM\_USAGE\_UNKNOWN, STREAM\_USAGE\_MUSIC, STREAM\_USAGE\_MOVIE,
    // or STREAM\_USAGE\_AUDIOBOOK, SoundPool plays a short sound in audio mixing mode, without interrupting the playback of other audio streams.
    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
      rendererFlags: 1 // AudioRenderer flag.
    };
    
    // Create a SoundPool instance.
    this.soundPool = await media.createSoundPool(14, audioRendererInfo); // A maximum of 14 streams can be played simultaneously.
    
2.  Call [on('loadComplete')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#onloadcomplete) to listen for the completion of sound loading.
    
    private soundId: number = 0;
    // Callback invoked when the sound finishes loading.
    this.soundPool!.on('loadComplete', (soundId\_: number) => {
      this.soundId = soundId\_;
      console.info('loadComplete soundId: ' + soundId\_);
    })
    
3.  Call **on('playFinished')** or **on('playFinishedWithStreamId')** to listen for the completion of audio playback.
    
    When **'playFinished'** or **'playFinishedWithStreamId'** is subscribed to, the registered callback will be triggered upon the completion of audio playback.
    
    When both **'playFinished'** and **'playFinishedWithStreamId'** are subscribed to, only the **'playFinishedWithStreamId'** callback is triggered upon audio playback completion, while the **'playFinished'** callback is not.
    
    this.soundPool!.on('playFinished', () => {
      console.info("receive play finished message");
      // The sound can be played again.
    });
    this.soundPool!.on('playFinishedWithStreamId', (streamId) => {
      console.info("receive play finished message, streamId: " + streamId);
    });
    
4.  Call **on('error')** to listen for errors that may occur.
    
    this.soundPool!.on('error', (error: BusinessError) => {
      console.error('error happened,message is :' + error.code);
      console.error('error happened,message is :' + error.message);
    });
    
5.  Call **load()** to load a sound.
    
    You can pass in a URI or an FD to load the sound. The following uses the FD as an example. For more methods, see [SoundPool](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-multimedia-soundpool#load).
    
    When the system finishes loading the sound, the **loadComplete** callback is invoked to notify the user that the loading is complete. Perform the subsequent play operation after the callback is received.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private soundId: number = 0;
    // Obtain the context of the ability to which the current component belongs and obtain the application file path through the context.
    let context = this.getUIContext().getHostContext();
    // Obtain the file descriptor of the input file. test.ogg is a preset resource in the rawfile directory. Replace it with the actual one.
    let fileDescriptor = await context!.resourceManager.getRawFd('test.ogg');
    this.soundId = await this.soundPool!.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
    console.info(\`load soundPool soundId: ${this.soundId}\`)
    
6.  Set **PlayParameters**, and call **play** after the **loadComplete** callback is received. If **play()** with the same sound ID passed in is called for multiple times, the sound is played only once.
    
    private soundId: number = 0;
    private streamId: number = 0;
    let playParameters: media.PlayParameters = {
      loop: 1, // Loop once, meaning the sound will play twice in total.
      rate: 1, // Play at double speed.
      leftVolume: 0.5, // The value ranges from 0.0 to 1.0.
      rightVolume: 0.5, // The value ranges from 0.0 to 1.0.
      priority: 0, // The sound playback has the lowest priority.
    };
    // Start playback. The play operation can also contain PlayParameters. Perform the play operation after the audio resources are loaded, that is, after the loadComplete callback is received.
    this.soundPool!.play(this.soundId, playParameters, (error, streamID: number) => {
      if (error) {
        console.error(\`play sound Error: errCode is ${error.code}, errMessage is ${error.message}\`)
      } else {
        this.streamId = streamID;
        console.info('play success soundId:' + this.streamId);
      }
    });
    
7.  Call **setLoop()** to set the number of loops.
    
    // Set the number of loops.
    await this.soundPool!.setLoop(this.streamId, 2); // Play the sound three times.
    
8.  Call **setPriority()** to set the playback priority.
    
    // Set the priority.
    await this.soundPool!.setPriority(this.streamId, 1);
    
9.  Call **setVolume()** to set the playback volume.
    
    // Set the volume.
    await this.soundPool!.setVolume(this.streamId, 0.5, 0.5);
    
10.  Call **stop()** to stop the playback.
     
     // Stop the playback of the stream.
     await this.soundPool!.stop(this.streamId);
     
11.  Call **unload()** to unload a sound.
     
     // Unload the sound.
     await this.soundPool!.unload(this.soundId);
     
12.  Call **off('loadComplete')** to stop listening for the completion of sound loading.
     
     await this.soundPool!.off('loadComplete');
     
13.  Call **off('playFinished')** to stop listening for the completion of audio playback.
     
     await this.soundPool!.off('playFinished');
     
14.  Call **off('error')** to stop listening for errors.
     
     await this.soundPool!.off('error');
     
15.  Call **release()** to release the SoundPool instance.
     
     // Release the SoundPool instance.
     await this.soundPool!.release();
     

#### Running the Sample Project

Refer to the sample project to use SoundPool to play audio at a low latency.

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/SoundPool/SoundPoolArkTS), and copy its resources to the corresponding directories.
    
    SoundPoolArkTS
    entry/src/main/ets/
    └── pages
        └── Index.ets (Playback UI)
    entry/src/main/resources/
    ├── base
    │   ├── element
    │   │   ├── color.json
    │   │   ├── float.json
    │   │   └── string.json
    │   └── media
    │
    └── rawfile
        └── test.ogg (Audio resource)
    
2.  Compile and run the project.
