# Overview

An online game is a game that requires Internet connection.

After integrating with the basic game service, an online game allows users to sign in with a HUAWEI ID or official game account on the multi-provider sign-in panel.

<table style="border-style: none;"><tbody><tr><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><span><img height="211.03109999999998" originheight="429" originwidth="943" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/d3izAP3DR1qoSr1fTovl7Q/en-us_image_0000002504493006.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062104Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=6DA34EAEAFCC3693E1A06912E0F177CE796FE9740BB9C0BF6874E1770204EC93" title="Click to enlarge" width="465.5"></span></p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p><span><img height="213.3719" originheight="429" originwidth="943" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/9H0T7DyjQQqCOmzbLP-5hQ/en-us_image_0000002491561266.png?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062104Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=DDC6FA26AED0A2AC8AB5D1D56CEF050E653B36A3BF4F16C39A56DD89BA203E00" title="Click to enlarge" width="465.5"></span></p></td></tr></tbody></table>

#### Online Game Sign-In Scenarios

## Sign-in with a HUAWEI ID

An online game must integrate HUAWEI ID sign-in.

After the integration, Huawei's platform assigns a player's **playerId**/**openId** in the HarmonyOS 4-and-earlier version of the game to their **gamePlayerId** in the HarmonyOS 5.0-and-later version, enabling interoperability for account assets (such as the character, server, and game progress information) between the two versions. This will not cause any changes to the HUAWEI IDs, your server, or database.

For users signing in with their HUAWEI IDs, the basic game service provides identity verification and anti-addiction for minors, and IAP Kit provides HUAWEI ID payment compliance control (for example, payment limits for minors).

## Sign-in with an Official Game Account

If your game has an official package and its own official account system, it must support official game account sign-in. In addition, the game needs to implement interoperability for account assets between the official game package and the game package for HarmonyOS 5.0 and later.

For users who sign in with their official game accounts, implement identity verification, anti-addiction for minors, and payment compliance control by yourself.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/XFXm6ry9Q4GEd7gQHcUOWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0ABCA239A61F1067C53CEC3C26E412B167B85AAD0C7B0A38A51F191A30EE8C8)

On devices running HarmonyOS 5.0 or later, there is a new requirement: the basic game service on the device implements identity verification and anti-addiction for minors for the HUAWEI ID signed in on the device. Even so, you still need to implement identity verification, anti-addiction for minors, and payment compliance control for official game account-based sign-in.

## Account Relationship Overview

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/8yrWEXpOTRaHAXqLsOYm3g/en-us_image_0000002517744543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53894F6592841207E47C8EEC08EC4FD5D9666C92E53A795E02132901B7A22320)

#### User Experience of Online Games

This section describes the game sign-in experience.

## First Sign-In

When a user launches the game for the first time, the multi-provider sign-in panel is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/QR_ccdXgSwW4yri98SQM6A/en-us_image_0000002491401394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2FDB121A2350DED93D6B1F6B756D297BF572037E63F68E55EF0116147D593FE "Click to enlarge")

-   Tap **Sign in with Let's play account**. The official game account sign-in page is displayed. The user enters the game after correctly entering their account information.
-   Tap **Sign in with HUAWEI ID**. The user signs in to the game with their HUAWEI ID, and a welcome banner is displayed on the top.

## Subsequent Sign-In

On future launches, the game will remember and automatically use the sign-in account from users' last session. For details about scenarios such as account switch and re-sign-in, please refer to [In-Game Account Switch](../sign-in-with-an-official-game-account/document.md#en-us_topic_0000002385861113_section26517112362).
