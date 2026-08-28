# (Mandatory) Mini Game Sign-In

After integrating the mini game sign-in API of the basic game service, your mini game will be able to allow players to quickly sign in with their HUAWEI IDs. The basic game service also provides HUAWEI ID identity verification and anti-addiction for minors for your mini game.

#### Prerequisites

You have made [all necessary preparations](../preparations/document.md).

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/a16SfWFNSQyNt2ETp24slg/en-us_image_0000002506511067.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=444924822C60D692D29C21196EE8E2B1DFC53A4F24AA99AE64A5785BD13953AA)

1.  The player starts the mini game.
2.  The mini game calls the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API to initialize Game Service Kit. After the initialization, the Huawei privacy agreement pop-up is displayed. Once the player accepts the terms, the process continues.
3.  The mini game calls the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section145017424483) API to register a listener for mini game anti-addiction events.
4.  The mini game calls the [miniGameLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section44488469397) API. The mini game displays a welcome banner on the top of the screen. Game Service Kit returns information including **playerId** and **playerSign** to the mini game. In addition, Game Service Kit checks whether the player has completed identity verification and is an adult.
    -   If the player has not completed identity verification, the [miniGameLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section44488469397) API will automatically display the identity verification pop-up for the player.
    -   If the player has completed identity verification and is identified as a minor, the [miniGameLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section44488469397) API will then automatically detect their game playtime. If the player signs in beyond the specified timeframe, the player will be forcibly signed out and error code [1002000006](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-error-code#section4418848101513) will be returned.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void

 | 

Initializes Game Service Kit using the default context. This API returns the result through a callback.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section145017424483)(type: 'miniGameAddictionPrevented', callback: Callback<string>): void

 | 

Listens for mini game anti-addiction events. This API returns the result through a callback.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section171668301498)(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void

 | 

Deregisters listeners for mini game anti-addiction events.

 |
| 

[miniGameLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section44488469397)(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>

 | 

Signs in to the mini game. This API returns the result through a promise.

 |

#### Development Procedure

## Importing Modules

Import Game Service Kit and common modules.

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

## Performing Initialization

Call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section225333655719) API to initialize Game Service Kit.

onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent("pages/index", (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', \`Succeeded in initializing.\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to init. Code: ${err.code}, message: ${err.message}\`);
    }
  });
}

## Listening for Mini Game Anti-Addiction Events

Call the [on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section145017424483) API to register a listener for mini game anti-addiction events.

private miniGameAddictionPreventedCallback(result: string) {
  // Exit the mini game.
}
// ...
// Call the **on** API to register a listener for mini game anti-addiction events.
try {
  gamePlayer.on('miniGameAddictionPrevented', this.miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to register. Code: ${err.code}, message: ${err.message}\`);
}

## Signing In to the Mini Game

Call the [miniGameLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section44488469397) API to sign in to the mini game.

let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.MiniGameLoginParam = {
  'gameAppId': '123xxx', // Mini game's app ID.
  'extraData': 'xxx' // Additional information, which must be in JSON string format.
};
try {
  gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
    hilog.info(0x0000, 'testTag', \`Succeeded in logging in\`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${err.code}, message: ${err.message}\`);
}

## Deregistering Listeners for Mini Game Anti-Addiction Events

Call the [off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-gameplayer#section171668301498) API to deregister listeners for mini game anti-addiction events when the mini game exits.

// Deregister all listeners for the **miniGameAddictionPrevented** events.
try {
  gamePlayer.off('miniGameAddictionPrevented');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to unregister. Code: ${err.code}, message: ${err.message}\`);
}
