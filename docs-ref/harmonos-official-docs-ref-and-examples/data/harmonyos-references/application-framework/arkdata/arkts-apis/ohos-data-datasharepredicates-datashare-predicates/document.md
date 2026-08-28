# @ohos.data.dataSharePredicates (DataShare Predicates)

**DataSharePredicates** provides a filter object to query data in a database by using **DataShare** APIs. It is often used to update, delete, and query data.

The APIs provided by **DataSharePredicates** correspond to the filter criteria of the database. Before using the APIs, you need to have basic database knowledge.

**DataSharePredicates** applies to the following scenario:

-   It is used as a search criterion in the media file management service. For details, see [FetchOptions](../../../../media/media-library-kit/arkts-apis/ohos-file-photoaccesshelper-album-management/interfaces-others/document.md#fetchoptions) in the fetch options of the album management. In this scenario, you do not need to pay attention to the database type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/n_BRx7RJRqm-7Plf8CDNPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6319BE90AEB761D3691FA9EA817556FE4023D0B949E0DEE18443456A85575437)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { dataSharePredicates } from '@kit.ArkData';

#### DataSharePredicates

Provides APIs for setting different **DataSharePredicates** objects. This type is not multi-thread safe. If a **DataSharePredicates** instance is operated by multiple threads at the same time in an application, use a lock for it.

#### \[h2\]equalTo10+

equalTo(field: string, value: ValueType): DataSharePredicates

Creates a **DataSharePredicates** object to search for the records in the specified column that are equal to the given value.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | 
Column name in the database table.

If this parameter is set to **undefined** or **null**, the predicate used is invalid.

 |
| value | [ValueType](../ohos-data-valuesbucket-data-set/document.md#valuetype) | Yes | 

Value to match.

If this parameter is set to **undefined** or **null**, the predicate used is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object created. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose");

#### \[h2\]and10+

and(): DataSharePredicates

Creates a **DataSharePredicates** object to add the AND condition.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object with the AND operator. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "lisi")
    .and()
    .equalTo("SALARY", 200.5);

#### \[h2\]orderByAsc10+

orderByAsc(field: string): DataSharePredicates

Creates a **DataSharePredicates** object that sorts records in ascending order.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | 
Column name in the database table.

If this parameter is set to **undefined** or **null**, the predicate used is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object created. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByAsc("AGE");

#### \[h2\]orderByDesc10+

orderByDesc(field: string): DataSharePredicates

Creates a **DataSharePredicates** object that sorts data in descending order.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | 
Column name in the database table.

If this parameter is set to **undefined** or **null**, the predicate used is invalid.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object created. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.orderByDesc("AGE");

#### \[h2\]limit10+

limit(total: number, offset: number): DataSharePredicates

Creates a **DataSharePredicates** object to specify the number of records in the result and the start position.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| total | number | Yes | 
Maximum number of records.

If the KV store is used and **total** is **undefined** or **null**, the maximum number of records is 0. For details about the value range, see the description of this parameter in [limit](../ohos-data-distributedkvstore-distributed-kv-store/document.md#limit).

If the RDB store is used and **total** is **undefined** or **null**, the maximum number of records is not limited. For details about the value range, see the description of this parameter in [limitAs](../ohos-data-distributedkvstore-distributed-kv-store/document.md#limit).

 |
| offset | number | Yes | 

Start position of the query result.

If this parameter is set to **undefined** or **null**, the start position is the beginning of the result set.

For details about the value range in a KV store, see the description of this parameter in [limit](../ohos-data-distributedkvstore-distributed-kv-store/document.md#limit).

For details about the value range in an RDB store, see the description of the **rowOffset** parameter in [offsetAs](../ohos-data-relationalstore-rdb-store/class-rdbpredicates/document.md#offsetas).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object created. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.equalTo("NAME", "Rose").limit(10, 3);

#### \[h2\]in10+

in(field: string, value: Array<ValueType>): DataSharePredicates

Creates a **DataSharePredicates** object to match the data that is within the specified range.

Currently, both the RDB store and KV store support this predicate.

**System capability**: SystemCapability.DistributedDataManager.DataShare.Core

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| field | string | Yes | 
Column name in the database table.

If this parameter is set to **undefined** or **null**, the predicate used is invalid.

 |
| value | Array<[ValueType](../ohos-data-valuesbucket-data-set/document.md#valuetype)\> | Yes | Array of the values to match. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataSharePredicates](#datasharepredicates) | **DataSharePredicates** object created. |

**Example**

let predicates = new dataSharePredicates.DataSharePredicates();
predicates.in("AGE", \[18, 20\]);
