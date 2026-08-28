# FlowItem

**FlowItem** is a child component of the [WaterFlow](../waterflow/document.md) container and is used to display specific items in the container layout.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/eP568koLQoa-R8c1bBFEpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062239Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47532214444A51CCD37D89DE657D71B1B304669A9C916F0E7087A00C8EB15D3D)

-   This component is supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
-   This component can be used only as a child of [WaterFlow](../waterflow/document.md).
-   In the swiping scenario, the **FlowItem** component and its child components are frequently created and destroyed. You are advised to encapsulate components in the **FlowItem** component into custom components and decorating them with the @Reusable decorator, making the components reusable and reducing the overhead of repeatedly creating and destroying nodes in the ArkUI framework. For best practices, see [Reusing Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-waterflow-performance-optimization#section189041489339).

#### Child Components

This component supports only one child component.

#### APIs

FlowItem()

Creates a child component in the **WaterFlow** layout.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

None

#### Example

See [WaterFlow](../waterflow/document.md#example).
