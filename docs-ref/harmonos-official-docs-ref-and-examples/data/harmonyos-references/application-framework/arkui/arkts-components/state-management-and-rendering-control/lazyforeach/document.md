# LazyForEach

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/BQ20ybsqSVSZhWdzbqxH1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AD6F9AF078D904CA3450DE86884084E7F3D3A158AB46D80A512D7798286051D)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

For details about the development, see [LazyForEach: Lazy Data Loading](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach).

In scenarios involving a large number of child components, LazyForEach, when combined with techniques such as cached list items, dynamic preloading, and component reuse, can significantly improve scrolling frame rates while reducing memory usage. For best practices, see [Optimizing Frame Loss for Long List Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list).

#### APIs

LazyForEach(dataSource: IDataSource, itemGenerator: (item: any, index: number) => void, keyGenerator?: (item: any, index: number) => string)

**LazyForEach** iterates over provided data sources and creates corresponding components during each iteration. When **LazyForEach** is used in a scrolling container, the framework creates components as required within the visible area of the scrolling container. When a component is out of the visible area, the framework destroys and reclaims the component to reduce memory usage.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataSource | [IDataSource](#idatasource) | Yes | **LazyForEach** data source. You need to implement related APIs. |
| itemGenerator | (item: any, index: number) => void | Yes | 
Child component generation function, which generates a child component for each data item in the array.

**NOTE**

\- (Optional) **item**: data item.

(Optional) **index**: index of the data item.

\- The function body of **itemGenerator** must be included in braces {...}.

\- **itemGenerator** can and must generate only one child component for each iteration.

\- The **if** statement is allowed in **itemGenerator**, but you must ensure that each branch of the **if** statement creates a child component of the same type.

 |
| keyGenerator | (item: any, index: number) => string | No | 

ID generation function, which generates a unique and fixed ID for each data item in the data source. Components are updated only when their generated key changes. The **keyGenerator** parameter is optional, but you are advised to provide it so that the development framework can better identify array changes and update components correctly.

The default value is an empty callback.

**NOTE**

\- (Optional) **item**: data item.

(Optional) **index**: index of the data item.

\- When **keyGenerator** is omitted, the default function **(item: Object, index: number) => { return viewId + '-' + index.toString(); }** is used, where key generation is affected by the index value only (**viewId** is compiler-generated and consistent within the same **LazyForEach** component).

\- To ensure correct and efficient child component updates, avoiding rendering anomalies or performance degradation, keys must meet the following requirements:

1\. Uniqueness: Each data item must have a distinct key.

2\. Consistency: Keys must remain unchanged for unmodified data items.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/W9GE-CiHSxiXBqRuRxvm8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CBC17AEDC9C8D497BD4E7C830FCBAA6FECC358C91AC68163F4F8D91922C9DEE)

To ensure smooth scrolling and prevent frame drops, avoid time-consuming operations in **keyGenerator** and **itemGenerator** functions. For best practices, see [Optimizing Time-Consuming Operations in the Main Thread: Repeated Rendering](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439). The **JSON.stringify()** method is particularly discouraged for key generation in complex business scenarios. When processing item objects, this serialization method consumes significant computational resources and execution time, which can substantially degrade page rendering performance. For best practices, see [Optimizing Performance Using LazyForEach: Rules for Generating Key Values and Creating Components](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-lazyforeach-optimization#section68711519072).

#### Attributes

The [drag-and-drop sorting](../../universal-attributes/interaction-properties/drag-and-drop-sorting/document.md) attribute is supported.

#### IDataSource

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]totalCount

totalCount(): number

Obtains the total number of data items.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total number of data items, which is subject to the data source. |

#### \[h2\]getData

getData(index: number): any

Obtains the data item that matches the specified index.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | Index of the data record to obtain. The value range is \[0, data source length - 1\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| any | Data item that matches the specified index. The actual type is determined by the data source implementation. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/MRusP88lScWd0zOI7E4KKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=910A86FC29361273DEC0ED952FC7A332B480579E203B04940DA39C6FB531FA25)

To ensure smooth scrolling and prevent frame drops, avoid time-consuming operations in the **getData** function. For best practices, see [Optimizing Time-Consuming Operations in the Main Thread: Repeated Rendering](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-time-optimization-of-the-main-thread#section4551193714439).

#### \[h2\]registerDataChangeListener

registerDataChangeListener(listener: DataChangeListener): void

Registers a listener for data changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| listener | [DataChangeListener](#datachangelistener) | Yes | Listener for data changes. |

#### \[h2\]unregisterDataChangeListener

unregisterDataChangeListener(listener: DataChangeListener): void

Unregisters the listener for data changes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| listener | [DataChangeListener](#datachangelistener) | Yes | Listener for data changes. |

#### DataChangeListener

Listener for data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/jNGnYJ2vSQ6tKLqLmr2g5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCFCC8FB8F4A53D8F22F08FABD959F0E23AAC6CC67352965AEA12ACACC135533)

In APIs of **DataChangeListener** other than **onDatasetChange**, if the value of **index** is negative, the value is treated as **0** by default. In **onDatasetChange**, if the specified index in a **DataOperation** is outside the data source index range, the corresponding **DataOperation** does not take effect. (In **DataAddOperation**, the value of **index** can equal the data source length.)

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onDataReloaded

onDataReloaded(): void

Invoked when all data is reloaded. For data items whose key remains unchanged, the original child component is used. For data items whose key changes, a new child component is created.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]onDataAdded(deprecated)

onDataAdded(index: number): void

Invoked when data is added to the position indicated by the specified index.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/lb1oyrk2SC2UrkN4HpOEHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2C18C47D1668E802CD0C0D306B0A59BA61276704866BACBCF9A44286C62498C)

This API is supported since API version 7 and deprecated since API version 8. Use [onDataAdd](#ondataadd8) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the position where data is added. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataMoved(deprecated)

onDataMoved(from: number, to: number): void

Invoked when data is moved, that is, when data is swapped between the **from** and **to** positions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/xB-eNegiQVeFCJ72y7sbTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC02D56DFD0CEBE0D22AA7319C91D17FF6CDBAD355A106DAC91B0EDE54ED6893)

-   This API is supported since API version 7 and deprecated since API version 8. Use [onDataMove](#ondatamove8) instead.
    
-   The ID must remain unchanged before and after data movement. If the ID changes, APIs for deleting and adding data must be called.
    

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | number | Yes | 
Original position of data. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |
| to | number | Yes | 

Target position of data. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataDeleted(deprecated)

onDataDeleted(index: number): void

Invoked when data is deleted from the position indicated by the specified index. LazyForEach will update the displayed content accordingly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/WFC2I1knT0aMWsnHddVcxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A314F6546363DE8A134CD28ABE8ED86A112C5559A1C335248DA1B1FF8957438)

This API is supported since API version 7 and deprecated since API version 8. Use [onDataDelete](#ondatadelete8) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the position where data is deleted. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataChanged(deprecated)

onDataChanged(index: number): void

Invoked when data in the position indicated by the specified index is changed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Oqg3D51ERsGscbkuHI0lug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDEC575FCA2E8C42EEC1C6137AEAD36B9D070232545549DDB6BDE3032AB57A05)

This API is supported since API version 7 and deprecated since API version 8. Use [onDataChange](#ondatachange8) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Listener for data changes. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataAdd8+

onDataAdd(index: number): void

Invoked when data is added to the position indicated by the specified index.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the position where data is added. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataMove8+

onDataMove(from: number, to: number): void

Invoked when data is moved, that is, when data is swapped between the **from** and **to** positions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/mf4THH-9QEO41nBSgF4RAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A769975FBAD02C6D72B196121D2FE05B29B338055372D5AA170B0079BF9FECB9)

The ID must remain unchanged before and after data movement. If the ID changes, APIs for deleting and adding data must be called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| from | number | Yes | 
Original position of data. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |
| to | number | Yes | 

Target position of data. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataDelete8+

onDataDelete(index: number): void

Invoked when data is deleted from the position indicated by the specified index. LazyForEach will update the displayed content accordingly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/JhciuyabS0iTKMafeNgk1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CC11F04711484062CA2C8059BEA8470CEC79BE47520D3CE78F7F9D4568BCE4A)

Before **onDataDelete** is called, ensure that the corresponding data in **dataSource** has been deleted. Otherwise, undefined behavior will occur during page rendering.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the position where data is deleted. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDataChange8+

onDataChange(index: number): void

Invoked when data in the position indicated by the specified index is changed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| index | number | Yes | 
Index of the position where data is changed. The value range is \[0, data source length - 1\].

If the value is less than 0, it is treated as **0**. If the value is greater than the data source length minus 1, it is treated as the data source length minus 1.

 |

#### \[h2\]onDatasetChange12+

onDatasetChange(dataOperations: DataOperation\[\]): void

Invoked when data is processed in batches to notify the component of refreshing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/KoX-Tpa3TXyFfLP9h4QSUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5021C017F2030EF169BF2E7EDFB32CDE1CB2510910FA0966C342FF4EA8637DEE)

This API cannot be used together with other data operation APIs of **DataChangeListener**. For example, in the same **LazyForEach**, if you have called **onDataAdd**, do not call **onDatasetChange**; if you have called **onDatasetChange**, do not call **onDataAdd** or other data operation APIs. Different **LazyForEach** instances on the page do not affect each other. When data is processed in batches within the same **onDatasetChange** callback, if multiple **DataOperation** instances target the same index, only the first **DataOperation** will take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataOperations | [DataOperation](#dataoperation12)\[\] | Yes | Array of data operations performed. |

#### DataOperation12+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/g4zIcjYHQk-nD5uKmDpTxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=877A448D1F6CE3BF3EAD7C24828826B397C045FCE53C1B6EE4A507DF9AE741AE)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]DataAddOperation

Represents an operation for adding data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).ADD | No | No | Type of data addition. |
| index | number | No | No | Index at which to insert the data record. The value range is \[0, data source length\]. |
| count | number | No | Yes | 
Number of data records to insert.

Default value: **1**

 |
| key | string | Array<string> | No | Yes | Keys to assign to the inserted data records. The original keys are used by default. |

#### \[h2\]DataDeleteOperation

Represents an operation for deleting data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).DELETE | No | No | Type of data deletion. |
| index | number | No | No | Index at which to start deleting data. The value range is \[0, data source length - 1\]. |
| count | number | No | Yes | 
Number of data records to delete.

Default value: **1**

 |

#### \[h2\]DataChangeOperation

Represents an operation for changing data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).CHANGE | No | No | Type of data change. |
| index | number | No | No | Index of the data to be changed. The value range is \[0, data source length - 1\]. |
| key | string | No | Yes | New key to assign to the changed data. The original key is used by default. |

#### \[h2\]DataMoveOperation

Represents an operation for moving data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).MOVE | No | No | Type of data movement. |
| index | [MoveIndex](#moveindex12) | No | No | Positions for the movement. The value range is \[0, data source length - 1\]. |
| key | string | No | Yes | New key to assign to the moved data. The original key is used by default. |

#### \[h2\]DataExchangeOperation

Represents an operation for exchanging data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).EXCHANGE | No | No | Type of data exchange. |
| index | [ExchangeIndex](#exchangeindex12) | No | No | Positions for the exchange. The value range is \[0, data source length - 1\]. |
| key | [ExchangeKey](#exchangekey12) | No | Yes | New keys to assign to the exchanged data. The original keys are used by default. |

#### \[h2\]DataReloadOperation

Represents an operation for reloading data. If the **onDatasetChange** event contains a **DataOperationType.RELOAD** operation, all other operations in the event are ineffective. In such cases, the framework will call **keyGenerator** to perform a comparison of keys with their corresponding values.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [DataOperationType](#dataoperationtype).RELOAD | No | No | Type of data reloading. |

#### \[h2\]DataOperationType

Enumerates the data operation types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ADD | add | Data addition. |
| DELETE | delete | Data deletion. |
| CHANGE | change | Data change. |
| MOVE | move | Data movement. |
| EXCHANGE | exchange | Data exchange. |
| RELOAD | reload | Data reloading. |

#### MoveIndex12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| from | number | No | No | Start position for the movement. The value range is \[0, data source length - 1\]. |
| to | number | No | No | End position for the movement. The value range is \[0, data source length - 1\]. |

#### ExchangeIndex12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | number | No | No | First position for the exchange. The value range is \[0, data source length - 1\]. |
| end | number | No | No | Second position for the exchange. The value range is \[0, data source length - 1\]. |

#### ExchangeKey12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| start | string | No | No | New key to assign to the first position in the exchange. The original key is used by default. |
| end | string | No | No | New key to assign to the second position in the exchange. The original key is used by default. |
