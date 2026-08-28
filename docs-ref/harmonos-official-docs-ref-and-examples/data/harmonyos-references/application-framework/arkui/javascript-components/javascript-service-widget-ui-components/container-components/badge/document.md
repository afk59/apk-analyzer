# badge

The **<badge>** component is used to mark new events that require user attention in your application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/wbDBMbX5T6OuteM3EroKtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D4E968C5D635A78AE4551DDDC99AE9880B6E2F06294C8A2560D09852CAE4586)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component supports only one child component.

#### attributes

In addition to the [universal attributes](../../universal-components/universal-attributes/document.md), the following attributes are supported.

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| placement | string | rightTop | No | 
Position of a number or dot badge. Available values are as follows:

**right**: on the right border of the component.

\- **rightTop**: in the upper right corner of the component border.

\- **left**: on the left border of the component.

 |
| count | number | 0 | No | 

Number of notifications displayed via the badge. The default value is **0**. If the number of notifications is greater than 0, the badge changes from a dot to the number. If this attribute is not set or the value is less than or equal to 0, the badge is a dot.

When the **count** value is greater than the **maxcount** value, maxcount**+** is displayed. The largest integer value supported for **count** is **2147483647**.

 |
| visible | boolean | false | No | Whether to display the badge. The value **true** means that the badge shows up when a new notification is received. To use a number badge, set the **count** attribute. |
| maxcount | number | 99 | No | 

Maximum number of notifications. When the number of new notifications exceeds the value of this attribute, maxcount**+** is displayed, for example, **99+**.

Note: The maximum integer value is 2147483647.

 |
| config | BadgeConfig | \- | No | Configuration of the badge. |
| label | string | \- | No | 

Text of the new notification displayed via the badge.

When this attribute is set, attributes **count** and **maxcount** do not take effect.

 |

#### \[h2\]BadgeConfig

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| badgeColor | <color> | #fa2a2d | No | Background color of the badge. |
| textColor | <color> | #ffffff | No | Text color of the number badge. |
| textSize | <length> | 10px | No | Text size of the number badge. |
| badgeSize | <length> | 6px | No | Size of the dot badge. |

#### Styles

The [universal styles](../../universal-components/universal-styles/document.md) are supported.

#### Events

The [universal events](../../universal-components/universal-events/document.md) are supported.

#### Example

<!-- xxx.hml -->
<div class="container">
    <badge class="badge" config="{{ badgeConfig }}" visible="true" count="100" maxcount="99">
        <text class="text1">example</text>
    </badge>
    <badge class="badge" visible="true" count="1">
        <text class="text2">example</text>
    </badge>
</div>

/\* xxx.css \*/
.container {
    flex-direction: column;
    width: 100%;
    align-items: center;
}

.badge {
    width: 160px;
    height: 60px;
    margin-top: 30px;
}

.text1 {
    background-color: #f9a01e;
    font-size: 19fp;
}

.text2 {
    background-color: #46b1e3;
    font-size: 19fp;
}

// xxx.js
export default {
    data: {
        badgeConfig: {
            badgeColor: "#0a59f7",
            textColor: "#ffffff",
        }
    }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/QRmjCPaHQwqRi0RLrLtxyQ/en-us_image_0000002568686001.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D2E121BED90B6A8072FA1D0ECA3450B0E112FAC6AD6798FE15C0333A190F404)
