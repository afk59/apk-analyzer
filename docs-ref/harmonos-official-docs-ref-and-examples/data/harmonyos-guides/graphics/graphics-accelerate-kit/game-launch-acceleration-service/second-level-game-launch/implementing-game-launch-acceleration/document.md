# Implementing Game Launch Acceleration

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/2jZUQVLvTM2RW9tJ7eh7EA/en-us_image_0000002518200895.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC8847936A4117A03C1BCA3B1BB42BB62F70F7C7832EC91EFC87665956594DCF)

1.  A user launches the game.
2.  The game calls the [setSupportedProcessCache](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetsupportedprocesscache12) API in **onCreate** to enable caching for fast game launch.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/nHMhJioZQVir9cNSRQeu-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=470FF35FB6F119A184F0FA6E7EE7CFF45DA1B0AC475463B0677E79127C39D09C)
    
    Some device models do not support the setting for process resource caching. Therefore, you need to use a try-catch block to capture exceptions when calling [setSupportedProcessCache](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetsupportedprocesscache12).
    
3.  The user swipes up to exit the game.
4.  The game calls the [isLaunchMirrorEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-launchacceleration#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425) API in **onWindowStageWillDestroy** to query the game launch acceleration service for whether the memory snapshot function is enabled. If the function is enabled, the ArkTS side instructs the game engine to switch from the current scene to the sign-in screen. After the scene switching is complete, the game engine returns the result to the ArkTS side. If the scene switching fails or times out, the [setSupportedProcessCache](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetsupportedprocesscache12) API is called to disable caching for fast game launch.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/DcB5Gwh-SD-c2_lkb6rCow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B636A289510399F31F0A87FCB3D420E4E5C1C22D9D203E4AEF4A0E57139E8AF)
    
    You are advised to switch the scene to the game sign-in screen and set the switching timeout interval to 5 seconds.
    
5.  The game calls the [isLaunchMirrorEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-launchacceleration#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425) API again in **onDestroy** to check the status of the memory snapshot function. If the function is disabled, the engine destruction process will be executed, and the game process will then exit immediately.
6.  The user launches the game again.
7.  The game determines the launch mode based on whether a memory snapshot exists. If a memory snapshot exists, the system swaps the game objects previously swapped out to the disk back into memory, implementing a fast game launch. If no memory snapshot exists, the game launches through a normal process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/7IiQL8vrRUGLJPbXKmfNbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCA3E7083EC9EDBC1F2821C06D624FE28EBDB858407660BE3157C8F5252BDC6E)
    
    According to the release review guidelines, you are advised to display a splash screen with a healthy gaming reminder before the memory snapshot screen during fast game launch.
    

#### Lifecycle

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/cUyPJV9cRI6A0xWtatM0fQ/en-us_image_0000002499306740.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E28544F0A1358618428F22C7DEAEEAF43C8CBC121E4C80868D82619B1E82390)

-   Cold start scenario
    
    The game process creates the AbilityStage, UIAbility, and WindowStage objects in sequence to initialize the app and UI.
    
-   Second-level launch scenario
    
    After the second-level game launch function is enabled, when a user swipes up to exit the game, the system destroys the WindowStage and UIAbility objects in sequence, and then deeply freezes the game process. To reduce memory usage, the system swaps out most objects in the game process to the disk and retains only a few essential objects in memory.
    
    When a second-level game launch is triggered, the system swaps the previously swapped-out game objects back into memory, and the game process recreates the UIAbility and WindowStage objects, thereby implementing rapid recovery and launch.
    

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-launchacceleration).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[isLaunchMirrorEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-launchacceleration#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425)(): boolean

 | 

Checks whether the memory snapshot function is enabled for the game.

 |

#### Development Procedure

1.  Import the Graphics Accelerate Kit module.
    
    import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
    
2.  Call the [setSupportedProcessCache](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-applicationcontext#applicationcontextsetsupportedprocesscache12) API in **onCreate** when the game is launched, to enable caching for fast game launch.
    
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // Compatibility: Use **canIUse()** to check whether the device supports the launch acceleration service.
        try {
          this.context.getApplicationContext().setSupportedProcessCache(true);
        } catch (error) {
          let code = (error as BusinessError).code;
          let message = (error as BusinessError).message;
          console.error(\`setSupportedProcessCache fail, code: ${code}, msg: ${message}\`);
        }
      }
    }
    
3.  When the game exits, call the [isLaunchMirrorEnabled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-launchacceleration#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425) API to check whether the game memory snapshot function is enabled. If the function is enabled, the game first switches to a specific scene in **onWindowStageWillDestroy**. You are advised to switch to the game sign-in screen and cancel the game engine destruction step in **onDestroy**. The system automatically creates a memory snapshot before the game exits, which takes about 4 seconds.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/NmTeew7CQtK4G9qoRSdeVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062052Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BEA6792BBBCA90BA7551E69FFA14D881620F779E8F08793F3992D2C3521A3939)
    
    -   Since creating a memory snapshot takes 4 seconds, the second-level game launch function will not work if the user re-enters the game within this time window. Instead, the game will undergo a normal cold start.
    -   If the user swipes up to exit again within 10 seconds after a memory snapshot–based game launch, the system's Design for Reliability (DFR) protection mechanism will disable acceleration for the next game launch to prevent potential issues.
    -   The system determines whether to enable the memory snapshot function by considering the game's activity level, the number of existing memory snapshots, and the amount of memory swapped out to disk for the current day on the current device.
    
    onWindowStageWillDestroy(): void {
      if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // Compatibility: Use **canIUse()** to check whether the device supports the launch acceleration service.
        let enable = launchAcceleration.isLaunchMirrorEnabled()
        if (enable) {
          // Code logic for scene switching.
        }
      }
    }
    onDestroy(): void {
      if (canIUse("SystemCapability.GraphicsGame.LaunchAcceleration")) {  // Compatibility: Use **canIUse()** to check whether the device supports the launch acceleration service.
        let enable = launchAcceleration.isLaunchMirrorEnabled()
        if (!enable) {
          // Destroy the game engine only if the game memory snapshot function is disabled.
        }
      }
    }
