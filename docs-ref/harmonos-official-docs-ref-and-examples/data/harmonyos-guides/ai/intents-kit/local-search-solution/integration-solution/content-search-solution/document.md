# Content Search Solution

#### Solution Overview

When users interact with an app or atomic service, you can share data with the system according to the standard intent schema. Such data includes user behavior and content entities. You also need to implement intent calls either with or without parameters. Then, users can tap a widget to either perform a function in the background (like playing a specified song) or jump to a specified content page (such as the playback page of a specified song).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/1J6cVzTuSQij-Y9iunGoZw/en-us_image_0000002368482200.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062127Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D4663102DC9EADB33010030A6F150F783EAA0F001C2464EC49A3D0BBBB2D42A "Click to enlarge")

#### Intent Declaration

Take the local music search function as an example. You need to register the **PlayMusic** intent.

Edit the **insight\_intent.json** file to register the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

{
  // List of intents supported by your app.
  // Declare the mandatory intents contained in the plugin supported by your app. Your declaration will be verified during app release.
  "insightIntents": \[
    {
      // Intent name.
      // The name must comply with the Intents Kit specifications. Currently, only preconfigured intents for specific vertical domains are supported, while custom intents are not allowed.
      // Each intent name must be unique in an app.
      "intentName": "PlayMusic",
      // Vertical domain to which the intent belongs.
      "domain": "MusicDomain",
      // Intent version number.
      // When a plugin references an intent, the intent version number will be verified. The intent can be called only when the version number is the same as that defined by the plugin.
      "intentVersion": "1.0.1",
      // Entry to the intent call logic.
      "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
      "uiAbility": {
        // Ability that the intent belongs to.
      "ability": "EntryAbility",
        // **UIAbility** supports two execution modes: foreground and background.
        "executeMode": \[
          "background",
          "foreground"
        \]
      }
    }
  \]
}

#### Intent Sharing

Construct an intent object and call [shareIntent()](#section161911659112211) to implement intent sharing. You can construct multiple **PlayMusic** or **PlayMusicList** intent objects at the same time.

Take the local music search function as an example. You need to register the **PlayMusic** intent. Edit the **insight\_intent.json** file to register the intent. The **insight\_intent.json** file must be placed in the **src/main/resources/base/profile/insight\_intent.json** directory of any module. Only one **insight\_intent.json** file can exist in the entire project.

import { insightIntent } from '@kit.IntentsKit';
import { BusinessError } from '@kit.BasicServicesKit';
let playMusicIntent1: insightIntent.InsightIntent;
let playMusicIntent2: insightIntent.InsightIntent;
// API for data sharing. The intent array can contain more entities.
insightIntent.shareIntent(this.context, \[playMusicIntent1, playMusicIntent2\]).then(() => {
  console.info('shareIntent succeed');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});

Set the fields for sharing the **PlayMusic** intent. The sample code is as follows:

import { insightIntent } from '@kit.IntentsKit';
let playMusicIntent: insightIntent.InsightIntent = {
  intentName: "PlayMusic",
  intentVersion: "1.0.1",
  identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
  intentActionInfo: {
    actionMode: "EXECUTED",
    executedTimeSlots: {
      executedStartTime: 1637393212000,
      executedEndTime: 1637393112000,
    },
    currentPercentage: 50,
  },
  intentEntityInfo: {
    entityName: "Music",
    entityId: "C10194368",
    entityGroupId: "C10194321312",
    displayName: "Song 1",
    description: "NA",
    logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc\_logo.png",
    keywords: \["HUAWEI Music", "Makeup"\],
    rankingHint: 99,
    expirationTime: 1637393212000,
    metadataModificationTime: 1637393212000,
    activityType: \["1", "2", "3"\],
    artist: \["Singer 1", "Singer 2"\],
    lyricist: \["Lyricist 1", "Lyricist 2"\],
    composer: \["Composer 1", "Composer 2"\],
    albumName: "Album",
    duration: 244000,
    playCount: 100000,
    musicalGenre: \["Popular", "Chinese", "Golden hits", "Post-2000s"\],
    isPublicData: false,
  }
}

The following is a complete intent sharing example. This example constructs a **PlayMusic** intent and a **PlayMusicList** intent, and calls **shareIntent**.

import { insightIntent } from '@kit.IntentsKit';
import { BusinessError } from '@kit.BasicServicesKit';
let playMusicIntent: insightIntent.InsightIntent = {
  intentName: "PlayMusic",
  intentVersion: "1.0.1",
  identifier: "52dac3b0-6520-4974-81e5-25f0879449b5",
  intentActionInfo: {
    actionMode: "EXECUTED",
    executedTimeSlots: {
      executedStartTime: 1637393212000,
      executedEndTime: 1637393112000,
    },
    currentPercentage: 50,
  },
  intentEntityInfo: {
    entityName: "Music",
    entityId: "C10194368",
    entityGroupId: "C10194321312",
    displayName: "Song 1",
    description: "NA",
    logoURL: "https://www-file.abc.com/-/media/corporate/images/home/logo/abc\_logo.png",
    keywords: \["HUAWEI Music", "Makeup"\],
    rankingHint: 99,
    expirationTime: 1637393212000,
    metadataModificationTime: 1637393212000,
    activityType: \["1", "2", "3"\],
    artist: \["Singer 1", "Singer 2"\],
    lyricist: \["Lyricist 1", "Lyricist 2"\],
    composer: \["Composer 1", "Composer 2"\],
    albumName: "Album",
    duration: 244000,
    playCount: 100000,
    musicalGenre: \["Popular", "Chinese", "Golden hits", "Post-2000s"\],
    isPublicData: false,
  }
}
// API for data sharing. The intent array can contain more entities.
insightIntent.shareIntent(this.context, \[playMusicIntent\]).then(() => {
  console.info('shareIntent succeed');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});

#### Device-Side Intent Call

Implement **InsightIntentExecutor** yourself, and in the corresponding callback, implement the capability to open the landing page (the page displayed after users tap the recommendation widget) or the background execution capability.

The procedure is as follows:

1.  Extend **InsightIntentExecutor**.
2.  Override the corresponding method. For example, to open a foreground page, override the **onExecuteInUIAbilityForegroundMode** method.
3.  Identify the intent via its name (for example, **PlayMusic**), pass the intent parameters (**param**) to the corresponding method, and open the corresponding landing page (such as the music playback landing page), or play the music when the app or atomic service is running in the background.

import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
/\*\*
 \* Intent call example.
\*/
export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
  private static readonly PLAY\_MUSIC = 'PlayMusic';
  /\*\*
   \* Override the method to execute the intent in the foreground **UIAbility**.
   \*
   \* @param name Intent name.
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \* @returns Intent call result.
   \*/
  onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
    Promise<insightIntent.ExecuteResult> {
    // Dispatch processing logic based on the intent name. You can implement page redirection as needed.
    switch (name) {
      case InsightIntentExecutorImpl.PLAY\_MUSIC:
        return this.playMusic(param, pageLoader);
      default:
        break;
    }
    return Promise.resolve({
      code: -1,
      result: {
        message: 'unknown intent'
      }
    } as insightIntent.ExecuteResult)
  }
  /\*\*
   \* Implement the music playback function.
   \*
   \* @param param Intent parameters.
   \* @param pageLoader Window.
   \*/
  private playMusic(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
    return new Promise((resolve, reject) => {
      // TODO Implement an intent call. The input parameter of **loadContent** is the path to the music landing page, for example, **pages/SongPage**.
      pageLoader.loadContent('pages/SongPage')
        .then(() => {
          let entityId: string = (param.items as Array<object>)?.\[0\]?.\['entityId'\];
          // TODO If the intent is successfully called, log content will be displayed here.
          resolve({
            code: 0,
            result: {
              message: 'Intent execute succeed'
            }
          });
        })
        .catch((err: BusinessError) => {
          // TODO Handle the failure if the intent fails to be called.
          resolve({
            code: -1,
            result: {
              message: 'Intent execute failed'
            }
          })
        });
    })
  }
