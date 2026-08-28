# swiper

The **Swiper** component provides a container that allows users to switch among child components using swipe gestures.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/FR8rJIXcQDm7o0tnL1TcpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062300Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7D407BF0FE2DB13148A61365995F4A5BBEB49BBF7C4316FA935969C6004F2B8)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Attributes

In addition to the [universal attributes](../../universal-components/universal-attributes/document.md), the following attributes are supported.

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| index | number | 0 | No | Index of the child component currently displayed in the container. |
| indicator | boolean | true | No | Whether to enable the indicator. The default value is **true**. |
| digital | boolean | false | No | 
Whether to enable the digital indicator. The default value is **false**.

The digital indicator takes effect only when **indicator** is set to **true**.

 |
| loop | boolean | true | No | Whether to enable looping. |
| duration | number | 0 | No | Duration of the autoplay for child component switching. |
| vertical | boolean | false | No | Whether the swipe gesture is performed vertically. A vertical swipe uses the vertical indicator. |

#### Styles

In addition to the [universal styles](../../universal-components/universal-styles/document.md), the following styles are supported.

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| indicator-color | <color> | \- | No | Fill color of the indicator. |
| indicator-selected-color | <color> | \- | No | Color of the currently selected indicator. |
| indicator-size | <length> | 4px | No | Diameter of the indicator. |
| indicator-top|left|right|bottom | <length> | <percentage> | \- | No | Relative position of the indicator in the swiper. |

#### Events

The [universal events](../../universal-components/universal-events/document.md) are supported.

#### Example

<!-- xxx.hml -->
<swiper class="container" index="{{index}}">
  <div class="swiper-item primary-item">
    <text>1</text>
  </div>
  <div class="swiper-item warning-item">
    <text>2</text>
  </div>
  <div class="swiper-item success-item">
    <text>3</text>
  </div>
</swiper>

/\* xxx.css \*/
.container {
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}
.swiper-item {
  width: 454px;
  height: 454px;
  justify-content: center;
  align-items: center;
}
.primary-item {
  background-color: #007dff;
}
.warning-item {
  background-color: #ff7500;
}
.success-item {
  background-color: #41ba41;
}

{
  "data": {
    "index": 1
  }
}

**4 x 4 widget**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/h2RuuNHHSPWFWi6_bBOMcA/en-us_image_0000002568766013.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062300Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C1B2046D4FD0ABDDA85E3416EE208AED8923B3BED01D1567FB7701321A5D031)
