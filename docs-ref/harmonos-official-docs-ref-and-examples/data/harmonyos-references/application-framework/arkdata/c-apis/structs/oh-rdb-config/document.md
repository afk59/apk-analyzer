# OH\_Rdb\_Config

typedef struct  {...} OH\_Rdb\_Config

#### Overview

Defines the RDB store configuration.

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int selfSize | Size of the struct. |
| const char\* dataBaseDir | Path of the database file. |
| const char\* storeName | Name of the RDB store. |
| const char\* bundleName | Bundle name of the application. |
| const char\* moduleName | Module name. |
| bool isEncrypt | Whether to encrypt the RDB store. The value **true** means to encrypt the RDB store; the value **false** means the opposite. |
| int securityLevel | Database security level ([OH\_Rdb\_SecurityLevel](../../header-files/relational-store-h/document.md#oh_rdb_securitylevel)). |
| int area | 
Database security area level ([Rdb\_SecurityArea](../../header-files/relational-store-h/document.md#rdb_securityarea)).

**Since**: 11

 |
