# Developing a Fun-based Widget

Currently, fun-based widgets support mini-games developed with quick games. This kind of widget is in the inactive state by default. When a user taps the widget, it switches to the active state and the game begins. During the game, users can tap the pause icon to pause the game. In the paused state, users can resume the game by tapping the resume icon or end the game by tapping the stop icon.

#### Basic Concepts

Fun-based widgets can be in one of the following states: active (game running), paused (game paused), and inactive (game ended).

## Active State

In this state, the widget UI is carried by the mini-game page developed by the widget provider using quick games. The system supports an "overflow" effect, allowing game content to render beyond the widget rendering area.

**Figure 1** Fun-based widget in the active state

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/L9abisS0QH-WU-ETIGaPdg/en-us_image_0000002568764789.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061953Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C149189F10152DBB2E3A6DD115CC3DC5C1F79C6CCFAAC449CA03ED5DD51F23AA)

## Paused State

In this state, the widget UI is carried by the content in **widgetCard.ets** of the widget provider. Meanwhile, the system renders the resume and stop icons on the widget by default.

**Figure 2** Fun-based widget in the paused state

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/q97fryq7SdG2fPEe7-mAYg/en-us_image_0000002537765064.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061953Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDD890E5AB94A4AF92CDE0C731242B1BBA94C27CEECE10EBFFCD48F9B18F208D)

## Inactive State

In this state, the widget behaves like a common widget, complying with the existing widget development specifications. The widget UI is carried by the content in **widgetCard.ets**.

**Figure 3** Fun-based widget in the inactive state

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/P6BgvG_iRWWwRobEh93xLA/en-us_image_0000002537925004.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061953Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD6FAF5E4BD68FD8E2D64D95F582D255712AB48C84F9F4B46A5636621499ECE7)

#### Constraints

1.  When a user interacts with a widget, for example, by tapping, long-pressing, or dragging, the interactive target area is always the same size as the widget rendering area. Even if the animation rendering area extends beyond the widget rendering area, the excess part is only used for UI display and does not respond to interactive events.
2.  In the active state, interactive events within the widget's rendering area are responded to by the mini-game page developed by the widget provider. In other states, interactive events are responded to by the common widget developed by the widget provider.
3.  At a time, only one widget can be in the active or paused state for fun-based interactions. When a user taps a widget to activate it, all other fun-based widgets are automatically switched to the inactive state.
4.  For details about other design specifications and restrictions, refer to how to develop a creative widget.

#### How to Develop

For details about how to develop game content, refer to how to develop a game widget.

For details about on-device widget configuration and development, see [the configuration of fun-based widgets](../../configuring-arkts-widget-configuration-files/document.md#funinteractionparams-field).
