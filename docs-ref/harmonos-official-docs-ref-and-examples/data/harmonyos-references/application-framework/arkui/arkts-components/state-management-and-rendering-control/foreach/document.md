# ForEach

**ForEach** enables rendering of repeated content based on array type data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/hrG0kpL0RSKYaGJzTj-iug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=423F3042BB505C56F5434DB73F31C1B1FACA61884D1FB64B4C5FA092FFE36D38)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

For details about the development, see [ForEach: Rendering Repeated Content](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach).

#### APIs

ForEach(arr: Array<any>, itemGenerator: (item: any, index: number) => void, keyGenerator?: (item: any, index: number) => string)

**ForEach** enables rendering of repeated content based on array type data. It must be used in a container component, and the component it returns must be one allowed inside the container component. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is [List](../../scroll-and-swipe/list/document.md) or [ListItemGroup](../../scroll-and-swipe/listitemgroup/document.md).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| arr | Array<any> | Yes | 
Data source, which is an array.

If this parameter is set to **undefined**, the **ForEach** API does not take effect.

**NOTE**

\- You can set this parameter to an empty array. In this case, no child component is created.

\- You can also set this parameter to a function whose return value is an array, for example, **arr.slice (1, 3)**. However, the set function cannot change any state variables including the array itself. For example, **Array.splice**, **Array.sort**, and **Array.reverse** functions are not allowed, as they may change the array.

 |
| itemGenerator | (item: any, index: number) => void | Yes | 

Component generator.

\- It generates a component for each data item in an array.

\- (Optional) **item**: data item in the **arr** array.

\- (Optional) **index**: index of the data item in the **arr** array.

**NOTE**

\- The type of the created component must be the one allowed inside the parent container component of **ForEach**. For example, a **ListItem** component is allowed only when the parent container component of **ForEach** is **List**.

 |
| keyGenerator | (item: any, index: number) => string | No | 

Key generator.

\- It generates a unique and persistent key for each array item of the data source **arr**. You can customize the key generation rule using this function.

\- (Optional) **item**: data item in the **arr** array.

\- (Optional) **index**: index of the data item in the **arr** array.

**NOTE**

\- If this function is not specified, the default key generator of the framework is used: **(item: T, index: number) => { return index + '\_\_' + JSON.stringify(item); }**.

\- The key generator should not change any component state.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/GXIPe4DuTP-CaqFzmgVbgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE2932BFBCD08B7084F9B4F67FE91FC3704C1B2200873AECB674F57EAB8CB0D8)

-   The **itemGenerator** function can contain an **if/else** statement, and an **if/else** statement can contain **ForEach**.
-   On initial rendering, **ForEach** loads all data of the data source, creates a component for each data item, and mounts the created components to the render tree. If the data source contains a large number of items or performance is a critical concern, you are advised to use **LazyForEach**. For best practices, see [Performance Optimization Using LazyForEach](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-lazyforeach-optimization).

The data source item type is **any**, and no type consistency check is performed. It is recommended that you maintain consistent type declarations when using \*\*ForEach \*\*(see the following code snippet). Incorrect usage shown in the following code snippet may cause child component rendering failures.

// Incorrect usage.
arr: Array<Type1 | Type2> = \[\];

ForEach(this.arr, (item: Type1) => {...}, (item: Type2) => item.toString()) // The item type is inconsistent with the data item type.

// Correct usage.
arr: Array<Type1 | Type2> = \[\];

ForEach(this.arr, (item: Type1 | Type2) => {...}, (item: Type1 | Type2) => item.toString()) // The type of item matches the type of the array elements.

#### Attributes

The [drag-and-drop sorting](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md) attribute is supported.
