# Local AVSession Overview

#### Interaction Process

For a local AVSession, the data sources are on the local device. The figure below illustrates the interaction process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/JfowZErvQgq7fOZNxUX9oA/en-us_image_0000002568684887.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60433DD5EDDD17B0245E7C6768C0022ABAEE5C061FAC8F2541FD56EDEDCA455E)

This process involves two roles: provider and controller.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/OYV5s0PySmCcPLw42hTHhg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F23D481E9FADB8344B46A49E2C7C95A0EF6D67FEB7E686BBA3BCC322F27E7E8D)

The controller must be a system application. A third-party application can be a provider.

In the local AVSession, the provider exchanges information with the controller through AVSessionManager.

1.  The provider creates an AVSession object through AVSessionManager.
    
2.  Through the AVSession object, the provider sets session metadata (such as the asset ID, title, and duration) and playback attributes (such as the playback state, speed, and position).
    
3.  The controller creates an AVSessionController object through AVSessionManager.
    
4.  Through the AVSessionController object, the controller listens for changes of the session metadata and playback attributes.
    
5.  Through the AVSessionController object, the controller sends control commands to the AVSession object.
    
6.  Through the AVSession object, the provider listens for the control commands, for example, play, playNext, fastForward, and setSpeed, from the controller.
    

#### AVSessionManager

AVSessionManager provides the capability of managing sessions. It can create an AVSession object, create an AVSessionController object, send control commands, and listen for session state changes.

Unlike the AVSession and AVSessionController objects, AVSessionManager is not a specific object, but the root namespace of AVSessions. You can import AVSessionManager as follows:

import { avSession as AVSessionManager } from '@kit.AVSessionKit';

All the APIs in the root namespace can be used as APIs of AVSessionManager.

The code snippet below shows how the provider creates an AVSession object by using AVSessionManager:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/hoH3J2v2QbqrofLVymhIuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7929B10F0487CA382045F7F105F253A197EC3BE1D4A80657C152EED9878E5BD4)

The sample code below demonstrates only the API call for creating an AVSession object. When actually using it, the application must ensure that the AVSession object remains throughout the application's background playback activities. This prevents the system from reclaiming or releasing it, which could lead to playback being controlled by the system.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          // Create an AVSession object.
          let context = this.getUIContext().getHostContext() as Context;
          let session: AVSessionManager.AVSession = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', 'audio');
          console.info(\`session create done : sessionId : ${session.sessionId}\`);
        })
    }
    .width('100%')
    .height('100%')
  }
}

For more APIs of AVSessionManager, see [Module Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession).
