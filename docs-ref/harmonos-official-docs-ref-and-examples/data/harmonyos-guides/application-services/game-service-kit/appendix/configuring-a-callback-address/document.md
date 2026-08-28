# Configuring a Callback Address

To receive event notifications from Huawei game server when a key event occurs, configure the callback address of your server in AppGallery Connect. For details about the API prototype for sending notifications, please refer to the [Account Disassociation Notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/gameservice-unbindplayer-notification) API. The key event and its corresponding processing logic are as follows:

| 
Key Event

 | 

Processing Logic to Be Implemented by the Game

 |
| :-- | :-- |
| 

A user deregisters their HUAWEI ID.

 | 

Clear the account data.

 |

To configure the callback address of your server in AppGallery Connect, perform the following steps:

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, and select your project and game.
2.  Choose **Build** > **Game Service** from the navigation pane on the left, and set **Account Scheme Access Callback Address Configuration** to your server address. Huawei game server will then send event notifications to this address when a key event occurs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/N1i4hpODSSqbYnBwsCUe7w/en-us_image_0000002491561964.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=679781724BA583C9C13487F3511FBFEA2B2D655B5EED2CA91862DCCC2BC9B2A2)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/OPlAxQwOSA-q70LfS9e7lQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0DBC463CAC1E54EE5B273F1226F5A90A597A92BEEAB4A13F8E151240EFEF05ED)
    
    The callback address must support HTTPS and have a valid commercial certificate.
