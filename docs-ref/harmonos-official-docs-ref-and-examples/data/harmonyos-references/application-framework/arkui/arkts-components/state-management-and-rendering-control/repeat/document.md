# Repeat

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/LuVJO05oTe6TZ0st2ACW3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F085F36896C1B9DD83F416F38133B9C67167B3CFB5D1D10CF635BE9B293074B3)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Repeat** performs iterative rendering based on array data and is typically used together with scrollable components.

This document provides API parameter descriptions. For details about the component descriptions and usage guidelines, see [Repeat: Reusing Components for Repeated Content Rendering](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat).

#### APIs

#### \[h2\]Repeat: <T>(arr: Array<T>)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| arr | Array<T> | Yes | Data source, which is an array of the **Array<T>** type. You can determine the data types. |

**Example**

// arr is an array of the Array<string> type, which is used as the data source for Repeat.
Repeat<string>(this.arr)

#### \[h2\]Repeat: <T>(arr: RepeatArray<T>)18+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/564u2qwwS8adWS6ubo87zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C057F6978F4E8D826C8A56A10E94F941C5522190CD3938AB91F17BA80D385B5)

Data sources of the RepeatArray type are supported since API version 18.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| arr | [RepeatArray<T>](#repeatarrayt18) | Yes | Data source, which is an array of the **RepeatArray<T>** type. You can determine the data types. |

#### Properties

In addition to the [drag-and-drop sorting](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md) attribute, the following attributes are supported.

#### \[h2\]each

each(itemGenerator: (repeatItem: RepeatItem<T>) => void)

Component generator. When the return value of [.templateId()](#templateid) does not match any [.template()](#template) type (that is, the current item does not match any defined template style), the data item is processed using **.each()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/R4IFsq3rQvakIVCP3UIGOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A634D25DA342844ABE3D4CCDE90777BAEF74A88ABA9DD24DE44A4E3F430B845)

-   The **each** property is mandatory. If it is omitted, runtime errors will occur.
    
-   The **itemGenerator** parameter is of the **RepeatItem** type, which combines **item** and **index**. Do not destructure **RepeatItem**.
    
-   This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| itemGenerator | (repeatItem: [RepeatItem<T>](#repeatitemt)) => void | Yes | Component generator. |

**Example**

// Create a Text component for each item in the arr array of the Array<string> type.
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })

#### \[h2\]key

key(keyGenerator: (item: T, index: number) => string)

Key generator.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nsEOX_7_Tt2ODPSQ3JSRjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F76EBEABE288F253FCCED94BFAB0E632C190CEABC7577490E354C3BEE240F44C)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyGenerator | (item: T, index: number) => string | Yes | 
Key generator.

**item**: data item in the **arr** array. It is optional.

**index**: index of a data item in the **arr** array. It is optional.

 |

**Example**

// Create a Text component for each item in the arr array of the Array<string> type.
// Use the string value as its key.
Repeat<string>(this.arr)
  .each((obj: RepeatItem<string>) => { Text(obj.item) })
  .key((obj: string) => obj)

#### \[h2\]virtualScroll

virtualScroll(virtualScrollOptions?: VirtualScrollOptions)

Enables virtual scrolling for **Repeat**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/HSPl4VXkTZ6jI07_QODaLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D19F40BC267940628BC620A4AAAC696061A89802A9695F9B2F0696E4EB84DA00)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| virtualScrollOptions | [VirtualScrollOptions](#virtualscrolloptions) | No | 
Virtual scrolling configuration.

Default value: **undefined**

 |

**Example**

// Create a Text component for each item in the arr array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll()
}

#### \[h2\]template

template(type: string, itemBuilder: RepeatItemBuilder<T>, templateOptions?: TemplateOptions)

Renders the corresponding template child component based on the template type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/vK0fWzxDTOizylZzA--vQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3FAE0ECF98D2E942965413EF78166639A971686AFBC0FD1F351E9B5096FF99A)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Current template type. |
| itemBuilder | [RepeatItemBuilder](#repeatitembuildert)<T> | Yes | Component generator. |
| templateOptions | [TemplateOptions](#templateoptions) | No | 
Current template configuration.

Default value: **undefined**

 |

**Example**

// arr is an array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
// Define a reusable template temp for generating Text components.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
}

#### \[h2\]templateId

templateId(typedFunc: TemplateTypedFunc<T>)

Assigns a template type for this data item.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/7DsKcwEbSrmPPb4g7pcy8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8BC5CC53A86614E9ED1D3617549443A605C1560BE7DE0F8A3F440EF59FB090F)

This API cannot be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| typedFunc | [TemplateTypedFunc](#templatetypedfunct)<T> | Yes | Function that generates a template type for each data item. |

**Example**

// arr is an array of the Array<string> type.
// Use Repeat in a List container component with virtual scrolling enabled.
// Define a reusable template temp for generating Text components.
// Use the temp template for all data items.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .templateId((item: string, index: number) => { return 'temp' })
}

#### RepeatArray<T>18+

type RepeatArray<T> = Array<T> | ReadonlyArray<T> | Readonly<Array<T>>

Defines a union type for **Repeat** data source parameters.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| Array<T> | Regular array type. |
| ReadonlyArray<T> | Read-only array type, where the array object cannot be modified. |
| Readonly<Array<T>> | Read-only array type, where the array object cannot be modified. |

#### RepeatItem<T>

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| item | T | No | No | Each data item in the **arr** array. **T** indicates the data type passed in. |
| index | number | No | No | Index corresponding to the current data item. |

#### VirtualScrollOptions

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| totalCount | number | No | Yes | 
Total number of data items to load, which may not equal the data source length.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| reusable18+ | boolean | No | Yes | 

Whether to enable the reuse feature. The value **true** means to enable the reuse feature, and **false** means the opposite.

Default value: **true**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| onLazyLoading19+ | (index: number) => void | No | Yes | 

Lazy loading function, which is used to write data to the specified data source index.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| onTotalCount19+ | () => number | No | Yes | 

Function to obtain the total number of data items, which may not equal the data source length. It is recommended that you use **onTotalCount** instead of **totalCount**. If both **totalCount** and **onTotalCount** are set, **totalCount** is ignored.

Value range: \[0, +∞)

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

## totalCount

**totalCount** indicates the length of the data to be loaded, which is the length of the original array by default and can be greater than the number of loaded data items. **arr.length** represents the length of the data source. The processing rules for **totalCount** are as follows:

-   When **totalCount** is omitted or set to a non-natural number, the value of **totalCount** is **arr.length**, and the list scrolls normally.
-   When the value of **totalCount** is greater than or equal to 0 and smaller than the value of **arr.length**, only data within the range of \[0, totalCount - 1\] is rendered.
-   When the value of **totalCount** is greater than the value of **arr.length**, data in the range of \[0, totalCount - 1\] will be rendered. The scrollbar style changes based on the value of **totalCount**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/5cB1vH2hQ2KvlYJz04CUqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFC2EFAE867F13B42E2434525C9E6511D7F7EDEFDC9ADDFDD11F754EBCDB085A)

When the value of **totalCount** is greater than the value of **arr.length**, the application must ensure that subsequent data is requested when the list is about to scroll to the end of the data source during parent component container scrolling. You need to handle error scenarios (such as network delays) for data requests until all data sources are loaded; otherwise, scrolling exceptions may occur during list scrolling. For solutions, see [Handling Cases Where the totalCount Value Exceeds the Data Source Length](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-rendering-control-repeat#handling-cases-where-the-totalcount-value-exceeds-the-data-source-length).

## onLazyLoading19+

**onLazyLoading** is supported since API version 19 and designed for lazy loading scenarios. You can implement a custom method to write data to a specified index in the data source. The processing rules for **onLazyLoading** are as follows:

-   Before reading the data corresponding to an index in the data source, **Repeat** checks whether the index contains data.
-   If no data exists but the **onLazyLoading** method is implemented, **Repeat** calls this method.
-   In the **onLazyLoading** method, data should be written to the index specified by **Repeat** in the format of arr\[index\] = .... Note that array operations except **\[\]** are not allowed, and elements except the specified index cannot be written. Otherwise, the system throws an exception.
-   After the **onLazyLoading** method is executed, if no data exists in the specified index, rendering exceptions occur.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/NaxepFRTShGeByQnmXSbBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=50426D0774509C455EF6546CB488AE543EE77DF145D485C6C5AA3CC021F93ED1)

-   When you use **onLazyLoading**, it is recommended that use it together with **onTotalCount** instead of **totalCount**.
-   **onLazyLoading** is recommended when the expected data length is greater than the actual source length.
-   Avoid using the **onLazyLoading** method to execute time-consuming operations. If data loading takes a long time, you are advised to create a placeholder for the data in the **onLazyLoading** method and then create an asynchronous task to load the data.
-   Data can be loaded infinitely when **onLazyLoading** is used and **onTotalCount** is set to **arr.length + 1**. Note that in this scenario, you must provide the initial data required for the first screen display, and you are advised to set **cachedCount > 0** for the parent container component. Otherwise, rendering exceptions will occur. Avoid using the **onLazyLoading** method together with the loop mode of **Swipe**. Otherwise, staying at **index = 0** will trigger continuous **onLazyLoading** calls. Pay attention to memory usage to avoid excessive memory consumption caused by continuous data loading.

## onTotalCount19+

**onTotalCount** is supported since API version 19 and designed for lazy loading scenarios. You can set a custom method to calculate the expected array length. The return value must be a natural number and can be different from the actual data source length **arr.length**. The rules for processing **onTotalCount** are as follows:

-   When the return value is a non-natural number, **arr.length** is used as the return value and the list scrolls normally.
-   When the return value is greater that or equal to **0** and smaller than **arr.length**, only data within the range of \[0, return value - 1\] is rendered.
-   When the return value is greater than **arr.length**, the data within the range of \[0, return value - 1\] is rendered. The scrollbar style changes based on the return value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/6-BLsa8wRl6ipHPDg0X0PA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=181B0BD3C404618ABAE8FDEDB5C37F362F5B17B8704AA42FB6248B3447B40407)

-   Unlike **totalCount**, **onTotalCount** can be proactively called by **Repeat** to update the expected data length when necessary.
-   Use either **totalCount** or **onTotalCount**, not both. If neither is set, **arr.length** is used by default. If both are set, **totalCount** is ignored.
-   When the return value of **onTotalCount** is greater than **arr.length**, you are advised to use **onLazyLoading** to implement lazy loading.

## Example

// arr is an array of the Array<string> type. Use Repeat in a List container component with virtual scrolling enabled.
// Set the total number of data items to the length of the data source and enable component reuse.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll( { totalCount: this.arr.length, reusable: true } )
}

// Assume that the total number of items is 100, and 3 items are needed for the initial screen rendering.
// The initial array provides the first three items (arr = \['No.0', 'No.1', 'No.2'\]) and enables the lazy loading feature.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }})
    .virtualScroll({
      onTotalCount: () => { return 100; },
      onLazyLoading: (index: number) => { this.arr\[index\] = \`No.${index}\`; }
    })
}

#### RepeatItemBuilder<T>

type RepeatItemBuilder<T> = (repeatItem: RepeatItem<T>) => void

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| repeatItem | [RepeatItem](#repeatitemt)<T> | No | 
State variable that combines **item** and **index**.

This parameter is ignored by default when it is not specified. Using this parameter in a closure function will cause a compilation error.

 |

#### TemplateOptions

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| cachedCount | number | No | Yes | Maximum number of child component nodes that can be cached in the cache pool of the current template. The value range is \[0, +∞). The default value is the sum of the number of nodes in the display area of the container component and the number of nodes in the preloading area. When this sum increases (during the scrolling, when only part of the height of child components is within the display area), the value of **cachedCount** also increases accordingly. Note that the value of **cachedCount** does not decrease. |

When **cachedCount** is set to the maximum number of nodes in the display area of the container component for the current template, **Repeat** achieves maximum reuse efficiency. If there are no nodes of the current template in the container component's display area, the cache list is not released, which increases application memory usage. You are advised to set **cachedCount** to the number of nodes within the container component's display area and adjust the value according to the actual situation. However, setting **cachedCount** to less than 2 is not recommended, as this may lead to the frequent node creation during rapid scrolling and result in performance degradation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/TFMUHIyAR4W88xqU9L0jww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C058D5B6393B0E3648E1B3E258866AA79508C20FA44EC5C3D64FF49EF5C4A011)

The **.cachedCount()** attribute of the scrollable container component and the **cachedCount** parameter of the **.template()** method of **Repeat** are used to balance performance and memory, but their meanings are different.

-   **.cachedCount()** of the scrollable container component: size of the preloading area outside the display area of the container component. The child component nodes in this area are located in the component tree. The scrollable container component renders nodes in these preloading areas, improving the list scrolling performance.
-   **cachedCount** in **.template()**: size of the cache pool for each template in the **Repeat** component. When rendering a new child component, **Repeat** checks whether there are available nodes in the cache pool for the corresponding template. If yes, the nodes are reused. If no, new nodes are created.

**Example**

// arr is an array of the Array<string> type. Use Repeat in a List container component with virtual scrolling enabled.
// Define a reusable template temp for generating Text components. Use the temp template for all data items.
// Set the maximum cache count for the temp template to 2.
List() {
  Repeat<string>(this.arr)
    .each((obj: RepeatItem<string>) => {})
    .virtualScroll()
    .template('temp', (obj: RepeatItem<string>) => { ListItem() { Text(obj.item) }}, { cachedCount: 2 })
    .templateId((item: string, index: number) => { return 'temp' })
}

#### TemplateTypedFunc<T>

type TemplateTypedFunc<T> = (item: T, index: number) => string

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| item | T | No | 
Each data item in the **arr** array. **T** indicates the data type passed in.

This parameter is ignored by default when it is not specified. Using this parameter in a closure function will cause a compilation error.

 |
| index | number | No | 

Index corresponding to the current data item.

This parameter is ignored by default when it is not specified. Using this parameter in a closure function will cause a compilation error.

 |
