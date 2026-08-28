# Overview

The resource package background download functions are supported since version 5.1.0(18).

The resource package background download function silently downloads resource files, such as level packages, 3D character models, and textures, to user devices, minimizing the time users have to wait for resource download after launching a game. This addresses the problem of slow game launch, providing users with an instant play experience.

#### Main Functions

## Resource Package Download in the System Background

<table style="border-style: none;"><tbody><tr><td class="nocellnorowborder" style="border: none;" valign="top" width="50%"><ul><li>Scenario 1<p>After a user installs or updates a game on AppGallery and when the game is not started, the system automatically triggers resource package download if it detects resource package updates. The user can swipe down the notification panel to view the resource package download progress in real time.</p></li></ul></td><td class="cell-norowborder" style="border: none;" valign="top" width="50%"><ul><li>Scenario 2<p>When the user device meets the idle conditions and the game is not started, the system automatically triggers resource package download if it detects that the previous update was incomplete or that new resource packages need to be updated for the game. The user can swipe down the notification panel to view the resource package download progress in real time.</p></li></ul></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><video class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-user-active" controls="controls" height="525.00px" preload="auto" width="525.00px"><source src="https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/87/v3/_XCzf1LyRWCeq_hu1GixYQ/en-us_media_0000002418917253.mp4?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062051Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=6C1F77F0E0A369CF8A4897149B4933A364EA2CB0DFF882EAA48D2882920CD501" type="video/mp4"></video></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%"><p><video class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-user-active" controls="controls" height="525.00px" preload="auto" width="525.00px"><source src="https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/56/v3/5jnG4aMVRueuexJNryhjRQ/en-us_media_0000002418917257.mp4?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062051Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=4CB3880DCE2122F3D204A07EBB5D0C2C71295A49FD39E42BCE367C815B5F9839" type="video/mp4"></video></p></td></tr></tbody></table>

## Resource Package Download Switching from the System Background to the App Foreground

<table style="border-style: none;"><tbody><tr><td class="cell-norowborder" colspan="2" style="border: none;" valign="top"><p>After a user installs or updates a game on AppGallery and when the game is not started, the system automatically triggers resource package download if it detects resource package updates. The user can swipe down the notification panel to view the resource package download progress in real time. If the user launches the game app during the download, the game takes over the unfinished download task.</p></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><video class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-user-active" controls="controls" height="525.00px" preload="auto" width="525.00px"><source src="https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/6a/v3/4o6UaQlhREmFukvb5h-xog/en-us_media_0000002385158154.mp4?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062051Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=5861DE5F57AD52373632909AF11E86D2FE8501CDBF0F7CBD11C88D6CA3F2D8BA" type="video/mp4"></video></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

## Resource Package Download in the App Foreground

<table style="border-style: none;"><tbody><tr><td class="cell-norowborder" colspan="2" style="border: none;" valign="top"><p>When a user launches the game app, if it detects that the previous resource package update was incomplete or that new resource packages need to be updated, the game will resume the unfinished download task or initiate a new download task.</p></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><video class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-user-active" controls="controls" height="525.00px" preload="auto" width="525.00px"><source src="https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/a5/v3/dRlRAHGERSK82N2kU1MbyQ/en-us_media_0000002418797405.mp4?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062051Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=4CBC65D422C670D3FB96279D122CF789AA62A06035D526CCADBDEDF236109F94" type="video/mp4"></video></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

## Resource Package Download Switching from the App Foreground to the App Background

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/OOFmBdR7Ss6TiJCZJh1PTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062051Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D9785A9403F5165C74349F41D741D28C53EFE06301318AC3DCA513AD9FBC0D)

This download function must be used together with [continuous tasks of the dataTransfer type](../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md).

<table style="border-style: none;"><tbody><tr><td class="cell-norowborder" colspan="2" style="border: none;" valign="top"><p>If the game is switched to the background during resource package download in the foreground, the download task will continue without interruption. The user can swipe down the notification panel to view the resource package download progress in real time.</p></td></tr><tr><td class="row-nocellborder" style="border: none;" valign="top" width="50%"><p><video class="edui-upload-video vjs-fluid vjs-default-skin video-js vjs-paused vjs_video_3-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-user-active" controls="controls" height="525.00px" preload="auto" width="525.00px"><source src="https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/ae/v3/SZTQi-GGTSqikRJEAjxepg/en-us_media_0000002385318042.mp4?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062051Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=0BE21F185829C2EDE81E570E244C8208E88C74BA34B6E31E1072339B3FC93F9A" type="video/mp4"></video></p></td><td class="cellrowborder" style="border: none;" valign="top" width="50%">&nbsp;&nbsp;</td></tr></tbody></table>

#### Implementation Procedure

| 
No.

 | 

Step

 | 

Description

 |
| :-- | :-- | :-- |
| 

1

 | 

[Preparations](../preparations/document.md)

 | 

Make relevant preparations in advance.

 |
| 

2

 | 

Developing the Resource Package Background Download Functions

 | 

[Developing the Function of Resource Package Download in the System Background](../developing-the-function-of-resource-package-download-in-the-system-background/document.md)

 | 

Integrate the following resource package download functions into your game project: download in the system background, download in the app foreground, and download switching from the system background to the app foreground.

 |
| 

[Developing the Function of Resource Package Download in the App Foreground](../developing-the-function-of-resource-package-download-in-the-app-foreground/document.md)

 |
| 

[Developing the Function of Resource Package Download Switching from the System Background to the App Foreground](../developing-the-function-of-resource-package-download-switching-from-the-system-b/document.md)

 |
| 

3

 | 

Releasing a Resource Package Download Task

 | 

[Going to the Request Page](../releasing-a-resource-package-download-task/document.md#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section514181912359)

 | 

Create and release a resource package download task in AppGallery Connect. Before releasing a download task, you are advised to test whether a resource package can be successfully downloaded to your local device.

 |
| 

[Creating a Download Task](../releasing-a-resource-package-download-task/document.md#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section1494105011355)

 |
| 

[Submitting a Download Task](../releasing-a-resource-package-download-task/document.md#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section124381849103616)

 |
| 

[Testing the Download Functions](../releasing-a-resource-package-download-task/document.md#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section6757103624010)

 |
| 

[Releasing a Download Task](../releasing-a-resource-package-download-task/document.md#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section9206134163716)

 |
| 

4

 | 

[Viewing Resource Package Distribution Data](../viewing-resource-package-distribution-data/document.md)

 | 

After releasing a resource package download task, you can view the resource package distribution data in AppGallery Connect.

 |

#### Basic Concepts

| 
Concept

 | 

Description

 |
| :-- | :-- |
| 

CDN

 | 

A Content Delivery Network (CDN) utilizes distributed resource servers to boost the website access speed. You can configure a Huawei CDN or a third-party CDN when creating a resource package download task in AppGallery Connect.

 |
| 

Resource acceleration ExtensionAbility

 | 

The [ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-extensionability) component is designed to provide particular functionalities for specific scenarios (such as widgets and input methods). The [resource acceleration ExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/graphics-accelerate-extensionability) is the framework for resource package background download and provides key lifecycle functions. Corresponding callback functions are called when background download tasks succeed, fail, or end.

 |
| 

System background download

 | 

When the game app process is not loaded, the system can automatically start resource package download in the background.

 |
