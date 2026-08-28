# RDB

#### Overview

Distributed data manager supports persistence of various structured data on a single device, and data synchronization and sharing between a device and the cloud.

It defines a series of data types for operations, such as data addition, deletion, modification, and query.

**Since**: 11

#### Files

| Name | Description |
| :-- | :-- |
| [data\_asset.h](../../header-files/data-asset-h/document.md) | 
Defines data asset structs.

Asset is a data struct used in data management. You can use it to set and obtain file attributes, including the name, absolute path, relative path, creation time, modification time, status, and size of a file.

 |
| [oh\_cursor.h](../../header-files/oh-cursor-h/document.md) | Defines APIs to access the result set obtained by querying the RDB store. A result set is a set of results returned after **query()** is called. |
| [oh\_data\_value.h](../../header-files/oh-data-value-h/document.md) | 

Defines APIs and enums related to a single data value.

Since API version 18, **OH\_ColumnType** is moved from **oh\_cursor.h** to this file. This type is supported in versions earlier than API version 18 and can be used in all versions.

 |
| [oh\_data\_values.h](../../header-files/oh-data-values-h/document.md) | Defines APIs and enums related to multiple data values. |
| [oh\_data\_values\_buckets.h](../../header-files/oh-data-values-buckets-h/document.md) | Defines structs, APIs, and enums related to stored data values. |
| [oh\_predicates.h](../../header-files/oh-predicates-h/document.md) | Defines the predicates for an RDB store. |
| [oh\_rdb\_crypto\_param.h](../../header-files/oh-rdb-crypto-param-h/document.md) | Defines functions and enums related to encryption parameters of the RDB store. |
| [oh\_rdb\_transaction.h](../../header-files/oh-rdb-transaction-h/document.md) | Defines APIs and enums related to transactions. |
| [oh\_rdb\_types.h](../../header-files/oh-rdb-types-h/document.md) | Defines types related to data values. |
| [oh\_value\_object.h](../../header-files/oh-value-object-h/document.md) | Defines APIs for type conversion. |
| [oh\_values\_bucket.h](../../header-files/oh-values-bucket-h/document.md) | Defines the types of the key and value in a KV pair. |
| [relational\_store.h](../../header-files/relational-store-h/document.md) | Defines APIs for managing data in an RDB store. The APIs not marked as supporting vector stores are available only to RDB stores. |
| [relational\_store\_error\_code.h](../../header-files/relational-store-error-code-h/document.md) | Defines the error codes used for RDB stores. |
