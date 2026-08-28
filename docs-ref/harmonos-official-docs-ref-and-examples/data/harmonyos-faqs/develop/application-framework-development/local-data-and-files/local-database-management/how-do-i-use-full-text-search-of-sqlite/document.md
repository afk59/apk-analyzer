# How do I use full-text search of SQLite?

**Solution**

Currently, there is no API available for this feature. You need to execute the SQL statement **CREATE VIRTUAL TABLE** to create an FTS table, and then use **MATCH** to search for data.

[executeSql](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#executesql10): executes an SQL statement that contains specified arguments but returns no value.

[querySql](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore#querysql10): queries data in the database based on the specified SQL statement.
