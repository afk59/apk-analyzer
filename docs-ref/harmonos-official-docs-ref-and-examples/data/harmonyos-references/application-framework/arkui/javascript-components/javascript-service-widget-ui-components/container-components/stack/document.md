# stack

The **<stack>** component provides a stack container where child components are successively stacked and the latter one overwrites the previous one.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CjdiYjXKQWyRzc0x-f2e0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D73342AC2BBC3121871F178FDEAE8CC709631116DACC440A091F9867072D909D)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

#### Attributes

The [universal attributes](../../universal-components/universal-attributes/document.md) are supported.

#### Styles

The [universal styles](../../universal-components/universal-styles/document.md) are supported.

#### Events

The [universal events](../../universal-components/universal-events/document.md) are supported.

#### Example

<!-- xxx.hml -->
<stack class="stack-parent">
  <div class="back-child bd-radius"></div>
  <div class="positioned-child bd-radius"></div>
  <div class="front-child bd-radius"></div>
</stack>

/\* xxx.css \*/
.stack-parent {
  width: 400px;
  height: 400px;
  margin: 50px;
  background-color: #ffffff;
  border-width: 1px;
  border-style: solid;
}
.back-child {
  width: 300px;
  height: 300px;
  background-color: #3f56ea;
}
.front-child {
  width: 100px;
  height: 100px;
  background-color: #00bfc9;
}
.positioned-child {
  width: 100px;
  height: 100px;
  left: 50px;
  top: 50px;
  background-color: #47cc47;
}
.bd-radius {
  border-radius: 16px;
}

**4 x 4 widget**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/d1MoiEBbTOWIGjqAJkhmZw/en-us_image_0000002568686003.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F98235F9E6CF1D9D05BC521726BD57D4258A5CDFE6DBD2E4A14C699155826BF)
