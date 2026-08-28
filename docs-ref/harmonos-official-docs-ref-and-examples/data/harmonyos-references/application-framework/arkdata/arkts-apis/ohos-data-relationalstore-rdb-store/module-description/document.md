# Module Description

The relational database (RDB) manages data based on relational models. The **relationalStore** module provides a complete mechanism for managing local databases based on the underlying SQLite. You can use the APIs to perform operations such as adding, deleting, modifying, and querying data, and directly run SQL statements. In addition, you can obtain sendable data using [ResultSet.getSendableRow](../interface-resultset/document.md#getsendablerow12) and transfer the data across threads.

To ensure successful data access, limit the size of a data record to 2 MB. If a data record exceeds 2 MB, it can be inserted successfully but cannot be read.

Querying data from a large amount of data may take time or even cause application suspension. In this case, you can perform batch operations. For details, see [Batch Database Operations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/batch-database-operations-guide). Moreover, observe the following:

-   The number of data records to be queried at a time should not exceed 5000.
-   Use [TaskPool](../../../../arkts/arkts-apis/ohos-taskpool-starting-the-task-pool/document.md) if there is a large amount of data needs to be queried.
-   Keep concatenated SQL statements as concise as possible.
-   Query data in batches.

The **relationalStore** module provides the following functionalities:

-   [RdbPredicates](../class-rdbpredicates/document.md): provides predicates indicating the nature, feature, or relationship of a data entity in an RDB store. It is used to define the operation conditions for an RDB store.
-   [RdbStore](../interface-rdbstore/document.md): provides APIs for managing data in an RDB store.
-   [ResultSet](../interface-resultset/document.md): provides APIs for accessing the result set obtained from the RDB store.
-   [Transaction](../interface-transaction/document.md): provides APIs for managing transaction objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/2xcKZQI7R9GG-_58bqICBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7898FC6C851FBD46C542D5C4AA175B90FBA24A8AA0FC37DA1323F07900FB732)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Module to Import

import { relationalStore } from '@kit.ArkData';
