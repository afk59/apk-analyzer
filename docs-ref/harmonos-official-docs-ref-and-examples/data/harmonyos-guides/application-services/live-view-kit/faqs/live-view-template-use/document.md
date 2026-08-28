# Live View Template Use

#### When the Progress Visualization Template Is Used and **indicatorType** Is Set to **INDICATOR\_TYPE\_OVERLAY**, How to Make an Image Completely Overlay the Progress Bar If It Is Too Wide

When **indicatorType** is set to **INDICATOR\_TYPE\_OVERLAY**, the icon area is 64 x 56 vp. If an image is too wide, it will be scaled proportionally. So you need to adjust the image size and style for the desired effect.

Expected effect: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/NGP61MGRSCmts8YGRR2IXQ/en-us_image_0000002543551655.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50A4001C12225FDC34F178FE8EED266C05E6377AA3F2A179FFE471B0C9AAD429)

#### How to Change the Icon in the Upper Left Corner of a Live View

Only the navigation template provides [currentNavigationIcon](https://developer.huawei.com/consumer/en/doc/harmonyos-references/liveview-liveviewmanager#section19117745094) for you to set the icon in the upper left corner of a live view. The other templates display the app logo icon by default and do not support changing the icon.
