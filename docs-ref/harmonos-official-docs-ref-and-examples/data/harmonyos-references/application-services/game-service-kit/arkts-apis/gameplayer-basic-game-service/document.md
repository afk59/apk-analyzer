# gamePlayer (Basic Game Service)

This module provides the basic game service capability of Game Service Kit.

**Start version**: 4.0.0(10)

#### Module Import

import { gamePlayer } from '@kit.GameServiceKit';

#### GSKLocalPlayer

Player information class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

gamePlayerId

 | 

string

 | 

No

 | 

No

 | 

Game player ID. **gamePlayerId** cannot be empty in the transfer scene. The value contains a maximum of 256 characters.

 |
| 

teamPlayerId

 | 

string

 | 

No

 | 

No

 | 

Team player ID. **teamPlayerId** cannot be empty in the association scene. The value contains a maximum of 256 characters.

 |
| 

idCompatibleType

 | 

number

 | 

No

 | 

No

 | 

ID compatibility type.

-   **0**: **gamePlayerId** is incompatible with **openId** and **playerId**. After the [getLocalPlayer](#section17453143012584) API is called, the player ID is generated when a player signs in to your game for the first time. **teamPlayerId** is incompatible with **unionId**. When the [unionLogin](#section157848375136) API is called, the player ID is generated when the player signs into your game for the first time and does not choose to transfer APK game data.
-   **1**: **gamePlayerId** is compatible with **playerId**. That is, if a player chooses to transfer APK game data when signing in to your game for the first time and the APK game uses **playerId** as the player ID, Game Service Kit uses **playerId** as the new **gamePlayerId**.
-   **2**: **gamePlayerId** is compatible with **openId**. That is, if a player chooses to transfer APK game data when signing in to your game for the first time and the APK game uses **openId** as the player ID, Game Service Kit uses **openId** as the new **gamePlayerId**.

 |
| 

level

 | 

number

 | 

No

 | 

No

 | 

Player level **This parameter is reserved. Currently, the fixed value 0 is returned.**

 |
| 

playableTime

 | 

number

 | 

No

 | 

No

 | 

Permitted gameplay duration of a player, in minutes. **This parameter is reserved. Currently, the fixed value -1 is returned.**

NOTE:

The value **\-1** indicates the permitted gameplay duration for an adult player. If the value is greater than or equal to **0**, it indicates the permitted gameplay duration for a minor player.

 |
| 

loginIdType

 | 

number

 | 

No

 | 

No

 | 

Type of the account ID used by a player to sign in to a game.

-   **1**: gamePlayerId
-   **2**: teamPlayerId

**Start version**: 5.0.0(12)

 |

#### GSKPlayerRole

Player role information class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/NLljui2cRPGHEm9IQgW3Pw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5338BDCEEC531BC77E5EA3B039160441F005F652B7358F653913760791061169)

**gamePlayerId**, **teamPlayerId**, and **thirdOpenId** cannot be left empty at the same time.

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

roleId

 | 

string

 | 

No

 | 

No

 | 

Player role ID. The value cannot be **""** or **null**. The value contains a maximum of 128 characters. If the game does not have a role system, set this parameter to **0**.

 |
| 

roleName

 | 

string

 | 

No

 | 

No

 | 

Player role name. The value cannot be **""** or **null**. The value contains a maximum of 128 characters. If the game does not have a role system, set this parameter to **default**.

 |
| 

serverId

 | 

string

 | 

No

 | 

Yes

 | 

Player zone server ID. The value contains a maximum of 128 characters.

 |
| 

serverName

 | 

string

 | 

No

 | 

Yes

 | 

Player zone server name. The value contains a maximum of 128 characters.

 |
| 

gamePlayerId

 | 

string

 | 

No

 | 

Yes

 | 

Game player ID. The value contains a maximum of 256 characters.

 |
| 

teamPlayerId

 | 

string

 | 

No

 | 

Yes

 | 

Team player ID. This parameter can be passed when the official game account is associated with **teamPlayerId**. The value contains a maximum of 256 characters.

 |
| 

thirdOpenId

 | 

string

 | 

No

 | 

Yes

 | 

Official game account ID. The value contains a maximum of 128 characters.

**Start version**: 5.0.0(12)

 |

#### ThirdUserInfo

Account compliance information class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/2Pr_tM_hTr6nJEl2BhnnHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062506Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1738E990E1B1AADDB06ACB79C91E28397DDEDA3277C4EE4D7B0403B77D57F4FE)

The **isRealName**, **isAdult**, and **ageRange** parameters are not required for HUAWEI ID compliance verification.

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

thirdOpenId

 | 

string

 | 

No

 | 

No

 | 

Official game account ID. The value contains a maximum of 128 characters. If there is no official game account ID, set this parameter to an empty string ("").

 |
| 

isRealName

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a player has passed identity verification.

-   **true**: yes
-   **false**: no

 |
| 

isAdult

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a player who has completed identity verification is identified as an adult.

-   **true**: yes
-   **false**: no

 |
| 

ageRange

 | 

[ThirdUserAgeRange](#section12735946153615)

 | 

No

 | 

Yes

 | 

Age range of a player.

 |

#### UnionLoginParam

Parameters for multi-provider sign-in.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

thirdAccountInfos

 | 

Array<[ThirdAccountInfo](#section412355692217)\>

 | 

No

 | 

No

 | 

Official game account information which is displayed in the multi-provider sign-in panel. The name of each account must be unique.

NOTE:

If only quick sign-in using a HUAWEI ID is required, set this parameter to an empty array.

 |
| 

showLoginDialog

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to forcibly display the multi-provider sign-in panel to allow players to choose to sign in again.

-   **true**: The multi-provider sign-in panel is forcibly displayed when the [unionLogin](#section157848375136) API is called.
    
    CAUTION:
    
    To switch to another account or perform other operations, set this parameter to **true**.
    
-   **false**: When the [unionLogin](#section157848375136) API is called, the sign-in method selected by the player last time is preferentially used and the multi-provider sign-in panel is not forcibly displayed.

The default value is **false**.

 |
| 

loginPanelType

 | 

[LoginPanelType](#section20129173413913)

 | 

No

 | 

Yes

 | 

Multi-provider sign-in panel type.

-   ICON
-   BUTTON

The default value is **ICON**.

 |

#### ThirdAccountInfo

Official game account information.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

accountIcon

 | 

[Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

No

 | 

No

 | 

Official game account icon. The icon size cannot exceed 35 KB.

NOTE:

Currently, only images in the **media** directory are supported.

 |
| 

accountName

 | 

string

 | 

No

 | 

No

 | 

Display name of the official game account in the multi-provider sign-in panel.

You are advised to pass a specific name such as **Sign in with xx account** or **Sign in with xx pass** (for example, **Sign in with Let's play account**), rather than using ambiguous names like **Sign in with official account**.

If the game has multiple language versions, you need to determine the current language and provide the corresponding account name.

When **LoginPanelType** is set to **BUTTON**, **accountName** is used as the button text.

The value contains a maximum of 19 characters.

 |
| 

accountIdentifier

 | 

string

 | 

No

 | 

Yes

 | 

Unique identifier of the current account. It is used to identify the account and determine the account selected by the player from the sign-in result.

You are advised to pass an identifier related to the current account, for example, **youyou\_account**.

The default value is **undefined**.

The value contains a maximum of 32 characters.

**Start version**: 6.0.2(22)

 |
| 

isOnTop

 | 

boolean

 | 

No

 | 

Yes

 | 

This parameter is valid only when **LoginPanelType** is set to **ICON**.

This parameter indicates whether the current account is pinned to the top in the multi-provider sign-in panel.

-   **true**: yes
-   **false**: no

The default value is **false**.

NOTE:

-   Only the first account with **isOnTop** set to **true** will be pinned to the top, and it will be displayed as a button (with button text set to the value of **accountName**). Non-pinned accounts are displayed as icons.
-   In the BUTTON- or ICON-type sign-in panel, the HUAWEI ID that is pinned to the top by Huawei side has a higher priority.

**Start version**: 6.0.2(22)

 |

#### BoundPlayerInfo

Association information class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

thirdOpenId

 | 

string

 | 

No

 | 

No

 | 

Official game account ID.

 |
| 

bindType

 | 

[BindType](#section198841412616)

 | 

No

 | 

No

 | 

Type of the association with the official game account.

 |

#### BindType

Account association enumeration class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

CP\_ACCOUNT\_LEVEL

 | 

0

 | 

Developer level.

 |
| 

APP\_LEVEL

 | 

1

 | 

Game level.

 |

#### UnionLoginResult

Multi-provider sign-in result.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

accountName

 | 

string

 | 

No

 | 

No

 | 

Account name.

-   If the player signs in to the game with a HUAWEI ID, **hw\_account** is returned.
-   If the player signs in to the game with an official game account provided by you, the passed **ThirdAccountInfo.accountName** is returned.
-   If an exception occurs during the sign-in, **official\_account** is returned.
    
    **official\_account** indicates that no specific account name can be returned. It is recommended that the player select one of the game accounts provided by you for sign-in.
    

The value contains a maximum of 19 characters.

 |
| 

needBinding

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether a player ID needs to be associated with an official game account.

-   **true**: association scene, where a player ID needs to be associated with an official game account.
-   **false**: transfer scene, where a player ID does not need to be associated with an official game account.

NOTE:

The game server needs to adapt to the sign-in scene selected by the player:

-   In the transfer scene, the policy for the server must be consistent with that for HarmonyOS channel packages.
-   In the association scene or when an official game account is used for sign-in, the policy for the server must be consistent with that for official game packages.

 |
| 

boundPlayerInfo

 | 

[BoundPlayerInfo](#section331911518595)

 | 

No

 | 

No

 | 

Official game account information associated with **PlayerId**.

 |
| 

localPlayer

 | 

[GSKLocalPlayer](#section1033653365917)

 | 

No

 | 

No

 | 

Play information.

 |
| 

accountIdentifier

 | 

string

 | 

No

 | 

Yes

 | 

Unique identifier of the current account, which is used to determine the account selected by the player.

-   If the player signs in to the game with a HUAWEI ID, **hw\_account** is returned.
-   If the player signs in to the game with an official game account provided by you, the passed **ThirdAccountInfo.accountIdentifier** is returned.
-   If an exception occurs during the sign-in, **official\_account** is returned.
    
    **official\_account** indicates that no specific account name can be returned. It is recommended that the player select one of the game accounts provided by you for sign-in.
    

The value contains a maximum of 32 characters.

**Start version**: 6.0.2(22)

 |

#### PlayerChangedResult

Player change result.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

event

 | 

[PlayerChangedEvent](#section57008633419)

 | 

No

 | 

No

 | 

Player change event.

 |
| 

resultInfo

 | 

string

 | 

No

 | 

No

 | 

JSON string that returns information about the current event. The value contains a maximum of 1024 characters.

 |

#### PlayerChangedEvent

Player change event enumeration class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

SWITCH\_GAME\_ACCOUNT

 | 

0

 | 

The player switches the game account.

 |

#### ThirdUserAgeRange

Age information enumeration class of the official game account.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

AGE\_RANGE\_8

 | 

1

 | 

The player is under the age of 8, with identity verification passed.

 |
| 

AGE\_RANGE\_16

 | 

2

 | 

The player's age is greater than or equal to 8 and less than 16, with identity verification passed.

 |
| 

AGE\_RANGE\_18

 | 

3

 | 

The player's age is greater than or equal to 16 and less than 18, with identity verification passed.

 |
| 

AGE\_RANGE\_ADULT

 | 

4

 | 

The player's age is greater than or equal to 18, with identity verification passed.

 |

#### LoginPanelType

Sign-in panel enumeration class.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

ICON

 | 

0

 | 

-   The multi-provider sign-in panel supports the following sign-in options: HUAWEI ID and up to three official game accounts.
-   You can set the **isOnTop** parameter for an official game account to pin it to the top.

 |
| 

BUTTON

 | 

1

 | 

-   The sign-in panel provides two sign-in options: HUAWEI ID and official game account, both displayed as buttons.
-   You do not need to set the **isOnTop** parameter. The official game account is on the top by default.

 |

#### GameErrorCode

Error code enumeration class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.1.0(11)

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
**Parameter**

 | 

Value

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTERNAL\_ERROR

 | 

1002000001

 | 

Common internal error.

 |
| 

NETWORK\_ERROR

 | 

1002000002

 | 

Network connection error.

 |
| 

GET\_HWID\_INFO\_FAILED

 | 

1002000003

 | 

No HUAWEI ID information is found.

 |
| 

REALNAME\_CANCELED\_OR\_NOT\_REALNAME

 | 

1002000004

 | 

Identity verification is required but the player cancels it or identity verification has not been performed.

 |
| 

COUNTRY\_OR\_REGION\_NOT\_SUPPORTED

 | 

1002000005

 | 

Only HUAWEI IDs with both the service area and registration location within the Chinese mainland are supported.

 |
| 

ANTI\_ADDICTION\_ERROR

 | 

1002000006

 | 

The player is a minor and the current time is not within the permitted game duration.

**Start version**: 5.0.0(12)

 |
| 

PRODUCT\_BELONG\_REGION\_ERROR

 | 

1002000007

 | 

The app to which the product belongs is not released to specified countries or regions.

 |
| 

HWID\_IN\_BLOCKLIST

 | 

1002000008

 | 

The HUAWEI ID is in the blocklist.

 |
| 

GAME\_ACCOUNT\_UNAVAILABLE

 | 

1002000009

 | 

Third-party game accounts are not supported currently.

**Start version**: 5.0.0(12)

 |
| 

PLAYER\_ID\_INVALID

 | 

1002000010

 | 

**teamPlayerId** does not match the current player.

**Start version**: 5.0.0(12)

 |
| 

AGREEMENT\_NOT\_AGREED

 | 

1002000011

 | 

The player does not agree to the privacy agreement.

**Start version**: 5.0.0(12)

 |
| 

OPEN\_ID\_OR\_PLAYER\_ID\_BOUND

 | 

1002000012

 | 

The official game account has been associated with **teamPlayerId**.

**Start version**: 5.0.0(12)

 |
| 

OPEN\_ID\_AND\_PLAYER\_ID\_NOT\_BOUND

 | 

1002000013

 | 

The official game account is not associated with **teamPlayerId**.

**Start version**: 5.0.0(12)

 |
| 

CURRENT\_API\_NOT\_AVAILABLE\_FOR\_GAME

 | 

1002000014

 | 

This API is not available for this game.

**Start version**: 5.0.0(12)

 |
| 

CURRENT\_PLAYER\_INFO\_INVALID

 | 

1002000015

 | 

The player information is invalid.

**Start version**: 5.0.0(12)

 |
| 

UNION\_LOGIN\_CANCELED

 | 

1002000016

 | 

The player cancels multi-provider sign-in.

**Start version**: 5.0.0(12)

 |
| 

ILLEGAL\_APPLICATION

 | 

1002000017

 | 

Invalid app.

**Start version**: 5.0.0(12)

 |
| 

NOT\_MINI\_GAME\_ERROR

 | 

1002000018

 | 

This API is available only for mini games.

**Start version**: 6.0.1(21)

 |
| 

PARAM\_ERROR

 | 

1002000019

 | 

Parameter error.

**Start version**: 6.0.1(21)

 |
| 

USER\_CANCELED

 | 

1002000020

 | 

The user canceled the current operation.

**Start version**: 6.0.1(21)

 |
| 

CALLS\_FREQUENT

 | 

1002000021

 | 

Excessive API call frequency.

**Start version**: 6.0.1(21)

 |
| 

PAY\_PRODUCT\_INVALID

 | 

1002000050

 | 

Invalid product information.

**Start version**: 6.0.1(21)

 |
| 

PAY\_PRODUCT\_OWNED

 | 

1002000051

 | 

The purchase failed because the user already owns the product.

**Start version**: 6.0.1(21)

 |
| 

PAY\_PRODUCT\_NOT\_OWNED

 | 

1002000052

 | 

The delivery failed because the user does not own the product.

**Start version**: 6.0.1(21)

 |
| 

PAY\_PRODUCT\_CONSUMED

 | 

1002000053

 | 

The product has been delivered. No more delivery is needed.

**Start version**: 6.0.1(21)

 |
| 

PAY\_ACCOUNT\_REGION\_UNSUPPORTED

 | 

1002000054

 | 

The country or region to which the signed-in HUAWEI ID belongs is not supported by IAP Kit.

**Start version**: 6.0.1(21)

 |
| 

PAY\_DEAL\_REJECTED

 | 

1002000056

 | 

The transaction is rejected.

**Start version**: 6.0.1(21)

 |

#### gamePlayer.init

init(context: common.UIAbilityContext): Promise<void>

Initializes Game Service Kit when the game is launched. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

CAUTION:

**UIAbility** must be extended, and the optimal time to obtain the context is after the game UIs have been successfully loaded in the **onWindowStageCreate** lifecycle method.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { gamePlayer } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent("pages/index", (err, data) => {
      try {
        gamePlayer.init(this.context).then(() => {
          hilog.info(0x0000, 'testTag', \`Succeeded in initializing.\`);
        });
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, 'testTag', \`Failed to init. Code: ${err.code}, message: ${err.message}\`);
      }
    });
  }
}

#### gamePlayer.init

init(context: common.UIAbilityContext, callback: AsyncCallback<void>): void

Initializes Game Service Kit when the game is launched. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

CAUTION:

**UIAbility** must be extended, and the optimal time to obtain the context is after the game UIs have been successfully loaded in the **onWindowStageCreate** lifecycle method.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the initialization is successful, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { gamePlayer } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
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
}

#### gamePlayer.unionLogin

unionLogin(context: common.UIAbilityContext, loginParam: UnionLoginParam): Promise<UnionLoginResult>

Enables multi-provider sign-in with a HUAWEI ID or an official game account. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

loginParam

 | 

[UnionLoginParam](#section1030452961619)

 | 

Yes

 | 

Parameters for multi-provider sign-in.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[UnionLoginResult](#section556415719255)\>

 | 

Promise that returns the multi-provider sign-in result object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000004

 | 

User cancels real name authentication or not real name.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000008

 | 

The HUAWEI ID is in the blocklist.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000014

 | 

This interface is not available for this game.

 |
| 

1002000016

 | 

Union login canceled by user.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct UnionLogin {
  build() {
    Row() {
      Button('unionLogin')
        .onClick(() => {
          this.callUnionLogin();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callUnionLogin() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let thirdAccountInfo1: gamePlayer.ThirdAccountInfo = {
  'accountName': 'testName1', // Display name of the official game account in the multi-provider sign-in panel. You are advised to pass a specific name such as **Sign in with xx account** or **Sign in with xx pass** (for example, **Sign in with Let's play account**), rather than using ambiguous names like **Sign in with official account**. If the game has multiple language versions, you need to determine the current language and provide the corresponding account name.
  'accountIcon': $r('app.media.icon'), // Icon resource information of the official game account. The total icon size cannot exceed 35 KB.
  'accountIdentifier': 'testIdentifier1', // Unique identifier of the current account. It is used to identify the account and determine the account selected by the player during sign-in result processing.
  'isOnTop': true // Whether the current account is pinned to the top. Only the first account with **isOnTop** set to **true** will be pinned to the top.
    };
    let request: gamePlayer.UnionLoginParam = {
  showLoginDialog: true, // Whether to display the multi-provider sign-in panel. The value **true** indicates that the panel will be forcibly displayed. The value **false** indicates that the player's last sign-in method will be used and the panel will not be displayed. However, the panel will always be displayed for first-time sign-ins or after a reinstallation.
      thirdAccountInfos: \[
    thirdAccountInfo1 // If the game does not have an official package or official account system, pass an empty array.
      \]
    };
    try {
      gamePlayer.unionLogin(context, request).then((result: gamePlayer.UnionLoginResult) => {
        hilog.info(0x0000, 'testTag', \`Succeeded in logging in: ${result?.accountName}\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.getLocalPlayer

getLocalPlayer(context: common.UIAbilityContext): Promise<GSKLocalPlayer>

Obtains the player information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[GSKLocalPlayer](#section1033653365917)\>

 | 

Promise that returns player information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000004

 | 

User cancels real name authentication or not real name.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000006

 | 

User is underage and has no playable time.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000014

 | 

This interface is not available for this game.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetLocalPlayer {
  build() {
    Row() {
      Button('getLocalPlayer')
        .onClick(() => {
          this.callGetLocalPlayer();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callGetLocalPlayer() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    try {
      gamePlayer.getLocalPlayer(context).then((result) => {
        hilog.info(0x0000, 'testTag', \`Succeeded in getting: ${result?.gamePlayerId}\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to get. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to get. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.getLocalPlayer

getLocalPlayer(context: common.UIAbilityContext, callback: AsyncCallback<GSKLocalPlayer>): void

Obtains the player information. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

callback

 | 

AsyncCallback<[GSKLocalPlayer](#section1033653365917)\>

 | 

Yes

 | 

Callback function. If the player information is successfully obtained, **err** is **undefined**. Otherwise, **err** is an error object.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000004

 | 

User cancels real name authentication or not real name.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000006

 | 

User is underage and has no playable time.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000014

 | 

This interface is not available for this game.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GetLocalPlayer {
  build() {
    Row() {
      Button('getLocalPlayer')
        .onClick(() => {
          this.callGetLocalPlayer();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callGetLocalPlayer() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    try {
      gamePlayer.getLocalPlayer(context, (error, result) => {
        if (error) {
          hilog.error(0x0000, 'testTag', \`Failed to get. Code: ${error.code}, message: ${error.message}\`);
          return;
        }
        hilog.info(0x0000, 'testTag', \`Succeeded in getting: ${result?.gamePlayerId}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to get. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.bindPlayer

bindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>

Associates the **teamPlayerId** corresponding to the player's HUAWEI ID with an official game account. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

thirdOpenId

 | 

string

 | 

Yes

 | 

Official game account ID. The value contains a maximum of 128 characters.

 |
| 

teamPlayerId

 | 

string

 | 

Yes

 | 

**teamPlayerId** corresponding to the player's HUAWEI ID.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000010

 | 

The playerId is not current player.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000012

 | 

The thirdOpenId or teamPlayerId has been bound.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct BindPlayer {
  build() {
    Row() {
      Button('bindPlayer')
        .onClick(() => {
          this.callBindPlayer();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callBindPlayer() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let thirdOpenId = '123xxxx';
    let teamPlayerId = '456xxx';
    try {
      gamePlayer.bindPlayer(context, thirdOpenId, teamPlayerId).then(() => {
        hilog.info(0x0000, 'testTag', \`Succeeded in binding.\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to bind. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to bind. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.unbindPlayer

unbindPlayer(context: common.UIAbilityContext, thirdOpenId: string, teamPlayerId: string): Promise<void>

Disassociates the **teamPlayerId** corresponding to the player's HUAWEI ID from an official game account. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

thirdOpenId

 | 

string

 | 

Yes

 | 

Official game account ID.

 |
| 

teamPlayerId

 | 

string

 | 

Yes

 | 

**teamPlayerId** corresponding to the player's HUAWEI ID.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000010

 | 

The playerId is not current player.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000013

 | 

The thirdOpenId and teamPlayerId are not bound.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct UnbindPlayer {
  build() {
    Row() {
      Button('unbindPlayer')
        .onClick(() => {
          this.callUnbindPlayer();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callUnbindPlayer() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let thirdOpenId = '123xxxx';
    let teamPlayerId = '456xxx';
    try {
      gamePlayer.unbindPlayer(context, thirdOpenId, teamPlayerId).then(() => {
        hilog.info(0x0000, 'testTag', \`Succeeded in unbinding.\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to unbind. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to unbind. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.verifyLocalPlayer

verifyLocalPlayer(context: common.UIAbilityContext, thirdUserInfo: ThirdUserInfo): Promise<void>

Verifies compliance for the HUAWEI ID used to sign in to the device, including identity verification and anti-addiction information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

thirdUserInfo

 | 

[ThirdUserInfo](#section1036174617108)

 | 

Yes

 | 

Player compliance information maintained by the game itself.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000004

 | 

User cancels real name authentication or not real name.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000006

 | 

User is underage and has no playable time.

 |
| 

1002000008

 | 

The HUAWEI ID is in the blocklist.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000015

 | 

The current player information is invalid. Execute the login process again to obtain the player information.

 |
| 

1002000017

 | 

Illegal application identity.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct VerifyLocalPlayer {
  build() {
    Row() {
      Button('verifyLocalPlayer')
        .onClick(() => {
          this.callVerifyLocalPlayer();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callVerifyLocalPlayer() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
// **thirdUserInfo** indicates the player compliance information. It is required if the player signs in to the game using an official game account. You do not need to pass related information if the player signs in with their HUAWEI ID.
    let request: gamePlayer.ThirdUserInfo = {
  thirdOpenId: '123xxxx', // Official game account ID. Leave this parameter empty when HUAWEI ID sign-in is used.
  isRealName: true // Whether the player has completed identity verification. The value **true** indicates yes and the value **false** indicates no. This parameter is not required when HUAWEI ID sign-in is used.
    };
    try {
      gamePlayer.verifyLocalPlayer(context, request).then(() => {
        hilog.info(0x0000, 'testTag', \`Succeeded in verifying.\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to verify. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.savePlayerRole

savePlayerRole(context: common.UIAbilityContext, request: GSKPlayerRole): Promise<void>

Saves the role information to the Huawei game server. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

request

 | 

[GSKPlayerRole](#section116223815415)

 | 

Yes

 | 

Reports role information after a player selects a role and a zone server. If the game does not have a role system, set **roleId** to **0** and **roleName** to **default**.

 |

**Returns**:

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SavePlayerRole {
  build() {
    Row() {
      Button('savePlayerRole')
        .onClick(() => {
          this.callSavePlayerRole();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callSavePlayerRole() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let request: gamePlayer.GSKPlayerRole = {
  roleId: '123', // Player role ID. If the game does not have a role system, pass **0**. Do not pass **""** or **null**.
  roleName: 'Jason', // Player role name. If the game does not have a role system, pass **default**. Do not pass **""** or **null**.
      serverId: '456',
      serverName: 'Zhangshan',
  gamePlayerId: '789' // Pass the actually obtained value of **gamePlayerId**.
    };
    try {
      gamePlayer.savePlayerRole(context, request).then(() => {
        hilog.info(0x0000, 'testTag', \`Succeeded in saving.\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to save. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.savePlayerRole

savePlayerRole(context: common.UIAbilityContext, request: GSKPlayerRole, callback: AsyncCallback<void>): void

Saves the role information to the Huawei game server. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.[UIAbilityContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md)

 | 

Yes

 | 

Context.

 |
| 

request

 | 

[GSKPlayerRole](#section116223815415)

 | 

Yes

 | 

Reports role information after a player selects a role and a zone server. If the game does not have a role system, set **roleId** to **0** and **roleName** to **default**.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the role information is successfully saved, **err** is **undefined**. Otherwise, **err** is an error object.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SavePlayerRole {
  build() {
    Row() {
      Button('savePlayerRole')
        .onClick(() => {
          this.callSavePlayerRole();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callSavePlayerRole() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let request: gamePlayer.GSKPlayerRole = {
  roleId: '123', // Player role ID. If the game does not have a role system, pass **0**. Do not pass **""** or **null**.
  roleName: 'Jason', // Player role name. If the game does not have a role system, pass **default**. Do not pass **""** or **null**.
      serverId: '456',
      serverName: 'Zhangshan',
  gamePlayerId: '789' // Pass the actually obtained value of **gamePlayerId**.
    };
    try {
      gamePlayer.savePlayerRole(context, request, () => {
        hilog.info(0x0000, 'testTag', \`Succeeded in saving.\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to save. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### gamePlayer.on('playerChanged')

on(type: 'playerChanged', callback: Callback<PlayerChangedResult>): void

Monitors the player change event. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Type of the event to listen for. The value is fixed at **'playerChanged'**.

 |
| 

callback

 | 

Callback<[PlayerChangedResult](#section7712953312)\>

 | 

Yes

 | 

Callback function, which returns the player change result.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let playerChangedEventCallback = (result: gamePlayer.PlayerChangedResult): void => {
  if (result.event === gamePlayer.PlayerChangedEvent.SWITCH\_GAME\_ACCOUNT) {
    // ...
    // The game account has been switched. After the local cache is cleared, call the **unionLogin** API again.
  }
}

// Call the **on** API to register the **playerChanged** event listener.
try {
  gamePlayer.on('playerChanged', playerChangedEventCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to register. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePlayer.off('playerChanged')

off(type: 'playerChanged', callback?: Callback<PlayerChangedResult>): void

Cancels monitoring of the player change event. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Type of the event for which listening is canceled. The value is fixed at **'playerChanged'**.

 |
| 

callback

 | 

Callback<[PlayerChangedResult](#section7712953312)\>

 | 

No

 | 

Callback function, which returns the player change result.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is left empty, all callback subscriptions for the **playerChanged** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |

**Example 1**:

import { gamePlayer } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  gamePlayer.off('playerChanged');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to unregister. Code: ${err.code}, message: ${err.message}\`);
}

**Example 2**:

import { gamePlayer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let playerChangedEventCallback = (result: gamePlayer.PlayerChangedResult): void => {
  if (result.event === gamePlayer.PlayerChangedEvent.SWITCH\_GAME\_ACCOUNT) {
    // ...
    // The game account has been switched. After the local cache is cleared, call the **unionLogin** API again.
  }
}

try {
  // The **playerChangedEventCallback** parameter is the second parameter of **gamePlayer.on('playerChanged', playerChangedEventCallback)**.
  gamePlayer.off('playerChanged', playerChangedEventCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to unregister. Code: ${err.code}, message: ${err.message}\`);
}

#### MiniGameLoginParam

Mini game sign-in information.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

gameAppId

 | 

string

 | 

No

 | 

No

 | 

App ID of a mini game.

 |
| 

extraData

 | 

string

 | 

No

 | 

Yes

 | 

Additional information, which must be a JSON string. Extra fields can be included as key-value pairs within this JSON string. Example:

let extraData = "{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}";

 |

#### MiniGamePlayer

Mini game player information.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

playerId

 | 

string

 | 

No

 | 

No

 | 

Player account ID.

 |
| 

isAdult

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether a player who has completed identity verification is identified as an adult.

-   **true**: yes
-   **false**: no

 |
| 

playerLevel

 | 

number

 | 

No

 | 

No

 | 

Account level of the current player.

 |
| 

playerSign

 | 

string

 | 

No

 | 

No

 | 

Player sign-in signature.

 |
| 

signTs

 | 

string

 | 

No

 | 

No

 | 

Timestamp of the player sign-in signature.

 |
| 

extraData

 | 

string

 | 

No

 | 

Yes

 | 

Additional information, which must be a JSON string. Extra fields can be included as key-value pairs within this JSON string. Example:

let extraData = "{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}";

 |

#### gamePlayer.on('miniGameAddictionPrevented')

on(type: 'miniGameAddictionPrevented', callback: Callback<string>): void

Registers a listener for mini game anti-addiction events. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Type of the event to listen for. The value is fixed at **'miniGameAddictionPrevented'**.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback function, which returns the result of registering a listener for mini game anti-addiction events.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1002000018

 | 

This API is only provided for HarmonyOS mini games.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let miniGameAddictionPreventedCallback = (result: string): void => {
  // Exit the mini game.
}

// Call the **on** API to register a listener for mini game anti-addiction events.
try {
  gamePlayer.on('miniGameAddictionPrevented', miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to register. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePlayer.off('miniGameAddictionPrevented')

off(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void

Deregisters the listener for mini game anti-addiction events. This API returns the result through a callback.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Type of the event to listen for. The value is fixed at **'miniGameAddictionPrevented'**.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback function, which returns the result of deregistering the listener for mini game anti-addiction events.

If this parameter is specified, the corresponding callback subscription will be canceled. If this parameter is not specified, all callback subscriptions for the **'miniGameAddictionPrevented'** event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1002000018

 | 

This API is only provided for HarmonyOS mini games.

 |

**Example 1**:

import { gamePlayer } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  gamePlayer.off('miniGameAddictionPrevented');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to unregister. Code: ${err.code}, message: ${err.message}\`);
}

**Example 2**:

import { gamePlayer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let miniGameAddictionPreventedCallback = (result: string): void => {
  // Exit the mini game.
}

try {
  // The **miniGameAddictionPreventedCallback** parameter is the second input parameter of **gamePlayer.on('miniGameAddictionPrevented', miniGameAddictionPreventedCallback)**.
  gamePlayer.off('miniGameAddictionPrevented', miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', \`Failed to unregister. Code: ${err.code}, message: ${err.message}\`);
}

#### gamePlayer.miniGameLogin

miniGameLogin(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer>

Signs in to a mini game. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.Context

 | 

Yes

 | 

Context.

 |
| 

loginParam

 | 

[MiniGameLoginParam](#section176210299469)

 | 

Yes

 | 

Mini game sign-in information.

 |

**Returns**:

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MiniGamePlayer](#section859174864711)\>

 | 

Promise that returns player information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000004

 | 

User cancels real name authentication or not real name.

 |
| 

1002000005

 | 

The country or region of the signed-in Huawei ID does not support.

 |
| 

1002000006

 | 

User is underage and has no playable time.

 |
| 

1002000008

 | 

The HUAWEI ID is in the blocklist.

 |
| 

1002000011

 | 

Agreement not agreed.

 |
| 

1002000018

 | 

This API is only provided for HarmonyOS mini games.

 |
| 

1002000019

 | 

Parameter error.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct MiniGameLogin {
  build() {
    Row() {
      Button('miniGameLogin')
        .onClick(() => {
          this.callMiniGameLogin();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callMiniGameLogin() {
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
  }
}

#### gamePlayer.miniGamePay

miniGamePay(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult>

Provides the mini game payment function. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 6.0.1(21)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

common.Context

 | 

Yes

 | 

Context.

 |
| 

parameter

 | 

[PurchaseParameter](#section1340120344598)

 | 

Yes

 | 

Parameters for purchasing a product.

 |

**Returns**:

| 
**Type**

 | 

Description

 |
| :-- | :-- |
| 

Promise<[CreatePurchaseResult](#section193852021105111)\>

 | 

Promise that returns the product creation result information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1002000001

 | 

System internal error.

 |
| 

1002000002

 | 

Network connection error.

 |
| 

1002000003

 | 

The HUAWEI ID is not signed in or not authorized.

 |
| 

1002000007

 | 

The application to which the product belongs is not listed in the specified country.

 |
| 

1002000018

 | 

This API is only provided for HarmonyOS mini games.

 |
| 

1002000019

 | 

Parameter error.

 |
| 

1002000020

 | 

The operation was canceled by the user.

 |
| 

1002000021

 | 

Too frequent API calls.

 |
| 

1002000050

 | 

Invalid product information.

 |
| 

1002000051

 | 

Failed to purchase a product because the user already owns the product.

 |
| 

1002000052

 | 

The purchase cannot be finished because the user has not paid for it.

 |
| 

1002000053

 | 

The purchase has been finished and cannot be finished again.

 |
| 

1002000054

 | 

The country or region of the signed-in HUAWEI ID does not support IAP.

 |
| 

1002000056

 | 

The user is not allowed to make purchase.

 |

**Example**:

import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct MiniGamePay {
  build() {
    Row() {
      Button('miniGamePay')
        .onClick(() => {
          this.callMiniGamePay();
        })
        .width('100%')
    }
    .margin(16)
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private callMiniGamePay() {
    let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    let request: gamePlayer.PurchaseParameter = {
  productId: 'xxx', // ID of the product to be paid for.
  productType: 0, // Product type to be queried.
  developerPayload: 'xxx', // Reserved for the merchant-side information. The length range of this parameter is \[0, 256\]. If this parameter is specified, its value will be returned to your app in a payment success callback.
  reservedInfo: 'xxx' // Additional information, which is a JSON string. Extra fields can be included as key-value pairs within this JSON string.
    };
    try {
      gamePlayer.miniGamePay(context, request).then((result: gamePlayer.CreatePurchaseResult) => {
        hilog.info(0x0000, 'testTag', \`Succeeded in paying\`);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to pay. Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', \`Failed to pay. Code: ${err.code}, message: ${err.message}\`);
    }
  }
}

#### PurchaseParameter

Product purchase parameter, intended for IAP Kit and mini games only.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

productId

 | 

string

 | 

No

 | 

No

 | 

ID of a product to be paid for.

 |
| 

productType

 | 

[ProductType](#section183551656122815)

 | 

No

 | 

No

 | 

Type of the product to query.

 |
| 

developerPayload

 | 

string

 | 

No

 | 

Yes

 | 

Information to retain, containing 0 to 256 characters. If a value exists, the value will be returned in a callback to the app after successful payment.

 |
| 

reservedInfo

 | 

string

 | 

No

 | 

Yes

 | 

Additional information passed via a JSON string in key-value format. Example:

let reservedInfo = "{\\"key1\\":\\"value1\\",\\"key2\\":\\"value2\\"}";

NOTE:

This parameter is reserved for you to pass additional information. You can choose to set it or not.

 |

#### ProductType

Product type, intended for IAP Kit and mini games only.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CONSUMABLE

 | 

0

 | 

Consumable.

 |
| 

NONCONSUMABLE

 | 

1

 | 

Non-consumable.

 |
| 

AUTORENEWABLE

 | 

2

 | 

Auto-renewable subscription.

**Start version**: 5.0.0(12)

 |

#### PurchaseResult

Product purchase result, which can be used only by IAP Kit.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

inAppPurchaseData

 | 

string

 | 

No

 | 

No

 | 

JSON string of purchase data.

 |
| 

signature

 | 

string

 | 

No

 | 

No

 | 

Signature string generated after the **paymentData** string is signed using the IAP private key.

 |
| 

signatureAlgorithm

 | 

string

 | 

No

 | 

No

 | 

Signing algorithm. The value is fixed at **SHA256WithRSA/PSS**.

 |

#### CreatePurchaseResult

Product purchase result, intended for IAP Kit and mini games only.

**System capability**: SystemCapability.Game.GameService.GamePlayer

**Start version**: 4.1.0(11)

| 
**Parameter**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

purchaseData

 | 

string

 | 

No

 | 

No

 | 

JSON string containing the purchase result.

 |
