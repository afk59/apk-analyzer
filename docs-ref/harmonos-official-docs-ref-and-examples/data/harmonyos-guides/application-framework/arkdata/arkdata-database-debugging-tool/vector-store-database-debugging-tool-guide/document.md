# vector-store Database Debugging Tool Guide

Currently, when using the vector-store database for development, debugging, and problem locating, developers are unable to view the content information in the database files, such as metadata and user data.

To improve developers' work efficiency, the database debugging tool allows developers to view the vector-store database on devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/YqhILz6TQRmruYYpJGt85A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061921Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F5619D1D50FCD6920BC55E2A68B5282FE1D63E0136321D35A1EAD58F5AEE507)

-   The vector-store database debugging tool is available since HarmonyOS 6.0.0.
-   You can also use DevEco Studio to for database debugging. For details, see [App Database Access](../../../../coding-and-debugging/debugging-your-app/app-database-access/document.md).

#### Environment Requirements

-   Before using this tool, you need to obtain the [hdc](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md#environment-setup) tool, enable the [developer](../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432) mode, and run the **hdc shell** command.
-   This tool can be used only to debug applications. For details about how to configure applications for debugging, see [Running/Debugging Configuration](../../../../coding-and-debugging/debugging-your-app/running-debugging-configuration/document.md).

-   Connect the devices properly.

#### Preparations

-   Before using the vector-store debugging tool, switch to the target application path and then run the **arkdata** command to access the vector-store debugging tool. (You need to use ArkData to configure relevant parameters to open the vector-store database, and only after the database is successfully opened can you use the vector-store tool to add, delete, modify, and query data.)
    
    The following table describes the parameters supported by the arkdata command.
    
    | 
    Name
    
     | 
    
    Value Type
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- |
    | 
    
    \-t
    
     | 
    
    String
    
     | 
    
    Database type, which is used to access the corresponding database debugging tool. Value range: {**preference\_kv**, **preference\_xml**, **vector**}
    
     |
    | 
    
    \-f
    
     | 
    
    String
    
     | 
    
    Full path of the database file, which includes the file name. The path cannot end with a slash (/).
    
     |
    | 
    
    \-h
    
     | 
    
    N/A
    
     | 
    
    Help information about the program.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/e9JBVvQ3S-GKOOLyzuNyOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061921Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF63C4AED465DCB5A6F80AA3A14A3BC7BB6C9640917032FAC809083491133FC0)
    
    For the vector-store database debugging tool, the **\-p** and **\-c** parameters are not involved.
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ cd /data/app/el1/100/base/com.test.myapplication   // Go to the target application path. (The current path is an example. Go to the path based on your actual needs.)
    $ arkdata -t vector                                  // -f is not specified, indicating that no database file is specified. By default, a database named arkdata is created in the data/vector directory of the current working directory.
    Enter ".help" for usage hints. 
    vector>>> .q
    
    When opening the database in the path of a non-target application, if the **\-f** parameter is missing (which would trigger the default folder creation), the process of creating the data/vector folder hierarchy in the current directory fails. The error information is as follows:
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ arkdata -t vector
    \[unsucc\]Failed to create directory ./data/vector : Permission denied
    
    When opening the database in the path of a non-target application, the .db file fails to be created in the specified path. The error information is as follows:
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ arkdata -t vector -f ./vector 
    \[GMDB SERVER\] \[GMERR-1013000\] multi-process init init unsucc!
    \[ERROR\] open db fail, ret = -5000.
    
-   You can use **arkdata --help** to view all related parameters of the database.
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ arkdata --help
    USAGE
      arkdata \[option\]
    OPTION
      -t|--type      <preference\_kv | preference\_xml | vector>, it is mandatory
      -f|--file      <database file path> 
      -p|--pageSize  <database pageSize>  
      -c|--cacheSize <database cacheSize>
      -h|--help
    

#### Command List

The following table lists the commands supported by the vector-store debugging tool.

| 
Command Format

 | 

Description

 |
| :-- | :-- |
| 

.help

 | 

Shows help information.

 |
| 

.q | .quit

 | 

Exits the database interaction mode.

 |
| 

.mode <table|print>

 | 

Sets the output format. The default value is **table**.

 |
| 

.table

 | 

Lists all table names.

 |
| 

.index

 | 

Lists all index names.

 |
| 

.schema

 | 

Lists the schemas of tables.

 |
| 

.count

 | 

Lists the total number of records in all tables.

 |

The following table lists the common operation cases of the vector-store debugging tool.

| 
Shortcut

 | 

Command

 |
| :-- | :-- |
| 

[Creating a Table](#section71651950132117)

 | 

create table

 |
| 

[Querying a Table](#section678120270225)

 | 

.table or .schema

 |
| 

[Renaming a Table](#section6909621142315)

 | 

alter table t1 rename to new\_t1;

 |
| 

[Adding a Table Field](#section1467916548236)

 | 

alter table t1 add column c text;

 |
| 

[Renaming a Table Field](#section76161323162418)

 | 

alter table t1 rename b to new\_b;

 |
| 

[Deleting a Table Field](#section14309165425111)

 | 

alter table t1 drop column c;

 |
| 

[Deleting a Table](#section7753258172210)

 | 

drop table t1;

 |
| 

[Adding a Table Index](#section6911351162415)

 | 

create index idx\_1 on t3(a);

 |
| 

[Inserting Data](#section5176194314253)

 | 

insert into t2 values(1,'xx'),(2,'yy');

 |
| 

[Querying Data](#section1226512132519)

 | 

select \* from t1;

 |
| 

[Updating Data](#section1780084142614)

 | 

update t1 set b = 'z' where a =3;

 |
| 

[Deleting Data](#section11241318152616)

 | 

delete from t1 where b = 'z';

 |

#### Constraints

-   For the vector-store database debugging tool, the maximum length of a command statement is 1024 × 1024-1.
-   Since hdc displays garbled characters when Chinese is used, the database debugging tool does not support Chinese.
-   This tool is supported on smartphones and PCs/2-in-1 devices.

#### Command Usage and Examples

## Displaying All Commands and Descriptions

After the vector-store database is opened, you can run the help command to view the supported commands.

vector>>> .help

## Creating or Opening an Existing Database

1.  Run the **hdc shell** command to enter the shell interaction mode.
2.  You must switch to the target application path, go to the path where the db file exists, and run the **arkdata -t vector** command to create a database.
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ cd /data/app/el1/100/database/com.test.myapplication   // Go to the target application path. (The current path is an example. Go to the path based on your actual needs.)
    $ cd entry/rdb/                                          // Go to the path where the .db file exists. You need to have the read and write permissions on the .db file to create a new database.
    $ arkdata -t vector
    Enter ".help" for usage hints.
    vector>>>
    
3.  When a new database is created, the system automatically generates the following files. The tag **debug\_hap\_data\_file** indicates that the file is the target application file.
    
    $ ls -lZ ./data/vector/
    total 176
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  77824 2025-08-12 20:12 arkdata
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0   8208 2025-08-12 20:13 arkdata.ctrl
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  24592 2025-08-12 20:13 arkdata.ctrl.dwr
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0    512 2025-08-12 20:13 arkdata.redo
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0      8 2025-08-12 20:13 arkdata.safe
    -rw------- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  28672 2025-08-12 20:12 arkdata.undo
    
4.  Open an existing database.
    
    $ arkdata -t vector -f ./data/vector/arkdata
    Enter ".help" for usage hints.
    vector>>>
    

## Creating a Table

-   At the **vector>>>** prompt, run the **create table** command to create a table.
    
    // Create a table via a single-line command.
    vector>>> create table t1(a int unique, b text);
    vector>>> .schema
    +-------+------+----------+----------------------------------------+
    | type  | name | tbl\_name | sql                                    |
    +-------+------+----------+----------------------------------------+
    | TABLE | T1   | T1       | create table t1(a int unique, b text); |
    +-------+------+----------+----------------------------------------+
    // Create a table via a single multi-line command.
    vector>>> create table t7(
    a int unique,
    b text);
    vector>>> .schema
    +-------+------+----------+---------------------------------------+
    | type  | name | tbl\_name | sql                                   |
    +-------+------+----------+---------------------------------------+
    | TABLE | t7   | t7       | create table t7(a int unique,b text); |
    +-------+------+----------+---------------------------------------+ 
    

-   At the **vector>>>** prompt, run the following commands to create multiple tables.
    
    // Create tables via multiple commands in a single line.
    vector>>> create table t7(a int unique, b text); create table t8(a int unique, b text);
    vector>>> .schema
    +-------+------+----------+-----------------------------------------+
    | type  | name | tbl\_name | sql                                     |
    +-------+------+----------+-----------------------------------------+
    | TABLE | t7   | t7       | create table t7(a int unique, b text);  |
    | TABLE | t8   | t8       |  create table t8(a int unique, b text); |
    +-------+------+----------+-----------------------------------------+
    // Create tables via multiple commands in multiple lines.
    vector>>> create table t7(
    a int unique,
    b text);
    create table t8(
    a int unique,
    b text);
    vector>>> .schema
    +-------+------+----------+---------------------------------------+
    | type  | name | tbl\_name | sql                                   |
    +-------+------+----------+---------------------------------------+
    | TABLE | t7   | t7       | create table t7(a int unique,b text); |
    | TABLE | t8   | t8       | create table t8(a int unique,b text); |
    +-------+------+----------+---------------------------------------+
    

## Querying a Table

-   At the **vector>>>** prompt, run the **.table** command to list all table names in the database. The following information is displayed.
    
    vector>>>.table
    +------+
    | name | 
    +------+
    | T1   |
    | T2   |
    | T3   |
    +------+
    

-   Run the **.schema** command to display the structure information of all tables in the database. The following information is displayed.
    
    vector>>>.schema
    +-------+-------+----------+----------------------------------------+
    | type  | name  | tbl\_name | sql                                    |
    +-------+-------+----------+----------------------------------------+
    | TABLE | T1    | T1       | create table t1(a int unique, b text); |
    | TABLE | T2    | T2       | create table t2(a int unique, b text); |
    | TABLE | T3    | T3       | create table t3(a int, b text);        |
    | TABLE | t7    | t7       | create table t7(a int unique,b text);  |
    | TABLE | t8    | t8       | create table t8(a int unique,b text);  |
    Press 'q' to quit, 'n' to continue: i
    Invalid input. Press 'q' to quit, 'n' to continue: n
    | TABLE | T9   | T9       | create table t9(a int unique,b text);  |
    +-------+-------+----------+----------------------------------------+
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/B1OViBbESrKBxsnhKt6dSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061921Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58D8D90E04F54807DE4971ED5A7D16E860737F911C5FE247C30E093396E14B9C)
    
    When the number of displayed data items reaches 5, the system asks you whether to continue displaying or exit. Enter **q** to exit the display or enter **n** to continue displaying.
    

## Renaming a Table

At the vector>>> prompt, run the **alter table t1 rename to new\_t1;** command to rename the table. The following information is displayed.

vector>>> .schema
+-------+------+----------+--------------------------------------+
| type  | name | tbl\_name | sql                                  |
+-------+------+----------+--------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, new\_b text); |
+-------+------+----------+--------------------------------------+
vector>>> alter table t1 rename to new\_t1;  // Rename t1 to new\_t1.
vector>>> .schema
+-------+--------+----------+------------------------------------------+
| type  | name   | tbl\_name | sql                                      |
+-------+--------+----------+------------------------------------------+
| TABLE | NEW\_T1 | NEW\_T1   | create table NEW\_T1( a int, new\_b text); |
+-------+--------+----------+------------------------------------------+

## Adding a Table Field

At the **vector>>>** prompt, run the **alter table t1 add column c text;** command to add a table field. The following information is displayed.

vector>>> create table t1( a int, b text);
vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl\_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+
vector>>> alter table t1 add column c text;  // Add a field named c of the text type to the table t1.
vector>>> .schema
+-------+------+----------+------------------------------------------+
| type  | name | tbl\_name | sql                                      |
+-------+------+----------+------------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text, c text); |
+-------+------+----------+------------------------------------------+

## Renaming a Table Field

At the **vector>>>** prompt, run the **alter table t1 rename b to new\_b;** command to rename the table field. The following information is displayed.

vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl\_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+
vector>>> alter table t1 rename b to new\_b; // Rename column b of table t1 to new\_b.
vector>>> .schema
+-------+------+----------+--------------------------------------+
| type  | name | tbl\_name | sql                                  |
+-------+------+----------+--------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, new\_b text); |
+-------+------+----------+--------------------------------------+

## Deleting a Table Field

At the **vector>>>** prompt, run the **alter table t1 drop column c;** command to delete the specified field from the table. The following information is displayed.

vector>>> .schema
+-------+------+----------+------------------------------------------+
| type  | name | tbl\_name | sql                                      |
+-------+------+----------+------------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text, c text); |
+-------+------+----------+------------------------------------------+
vector>>> alter table t1 drop column c;  // Delete the c field from the t1 table.
vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl\_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+

## Deleting a Table

At the **vector>>>** prompt, run the **drop table t1;** command to delete the t1 table from the database. The following information is displayed.

vector>>>drop table t1;  // Delete table t1.
vector>>>.table
+------+
| name | 
+------+
| T2   |
+------+

## Adding a Table Index

At the **vector>>>** prompt, run the **create index idx\_1 on t3(a);** command to add an index to the corresponding column of the table. The following information is displayed.

vector>>> create table t3(a int, b text);  // An index can be created only when no data is added to the table.
vector>>> create index idx\_1 on t3(a);     // Add an index idx\_1 to the corresponding column of the table.
vector>>> .index
+-------+
| name  |
+-------+
| idx\_1 |
+-------+

## Inserting Data

-   At the **vector>>>** prompt, run the **insert into t2 values(1,'xx'),(2,'yy');** command to insert the specified KV pair. The following information is displayed.
    
    vector>>> insert into t2 values(1,'xx'),(2,'yy');
    vector>>> select \* from t2;
    +----+----+
    | a  | b  |
    +----+----+
    | 1  | xx |
    | 2  | yy |
    +----+----+
    vector>>> create table t1(a int unique, b text);
    vector>>> insert into t1 values(1,'x'),(2,'y');
    vector>>> select \* from t1;
    +----+----+
    | a  | b  |
    +----+----+
    | 1  | x  |
    | 2  | y  |
    +----+----+
    

-   At the **vector>>>** prompt, run the following commands to insert multiple data records.
    
    // Insert multiple data records via a single multi-line command.
    vector>>> insert into t7 values(1,'x'),
    (2,'y'); 
    vector>>> select \* from t7;
    +----+---+
    | a  | b |
    +----+---+ 
    | 1  | x |
    | 2  | y |
    +----+---+ 
    // Insert multiple data records via multiple commands in a single line.
    vector>>> insert into t7 values(1,'x');insert into t7 values(2,'y');
    vector>>> select \* from t7; 
    +----+---+ 
    | a  | b |
    +----+---+
    | 1  | x |
    | 2  | y |
    +----+---+
    // Insert multiple data records via multiple commands in multiple lines.
    vector>>> insert into t7 values(1,'x'),
    (2,'y');
    insert into t8 values(1,'xx'),
    (2,'yy'); 
    vector>>> select \* from t7;
    +----+---+
    | a  | b |
    +----+---+
    | 1  | x |
    | 2  | y |                                                                                                   
    +----+---+
    vector>>> select \* from t8;
    +----+----+
    | a  | b  |
    +----+----+
    | 1  | xx | 
    | 2  | yy |
    +----+----+
    

## Querying Data

1.  Scan the full table.
    
    -   At the **vector>>>** prompt, run the **.mode print** and **select \* from _table name_;** commands to query all data in the specified table. The following information is displayed.
        
        vector>>> .mode print
        vector>>> select \* from t1;
        \[row-0\]
        a            = 1
        b            = x
        \[row-1\]
        a            = 2
        b            = y
        
    
    -   At the **vector>>>** prompt, run the **.mode table** and **select \* from _table name_;** commands to query all data in the specified table. The following information is displayed.
        
        vector>>> .mode table
        vector>>> select \* from t1;
        +----+---+
        | a  | b |
        +----+---+
        | 1  | x |
        | 2  | y |
        +----+---+
        
2.  At the **vector>>>** prompt, run the **select \* from _table name_ where _filter condition_** command to query the KV pair of a specified key. The following information is displayed.
    
    vector>>> select \* from t1 where a =1;
    +----+---+
    | a  | b |
    +----+---+
    | 1  | x |
    +----+---+
    
3.  At the **vector>>>** prompt, run the **.count** command to list the total number of records in all tables. The following information is displayed.
    
    vector>>> .count
    +------------+--------------+
    | table\_name | record\_count |
    +------------+--------------+
    | T1         | 2            |
    | T2         | 2            |
    | T3         | 0            |
    +------------+--------------+
    

## Updating Data

At the **vector>>>** prompt, run the **update t1 set b = 'z' where a =3;** command to update the KV pair. The following information is displayed.

vector>>> select \* from t1;
+----+----+
| a  | b  |
+----+----+
| 1  | x  |
| 2  | y  |
| 3  | xx |
+----+----+
vector>>> update t1 set b = 'z' where a =3;
vector>>> select \* from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
| 3  | z |
+----+---+

## Deleting Data

At the **vector>>>** prompt, run the **delete from t1 where b = 'z';** command to delete the specified KV pair from the table. The following information is displayed.

vector>>> select \* from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
| 3  | z |
+----+---+
vector>>> delete from t1 where b = 'z';// Delete z from the t1 table.
vector>>> select \* from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+

At the **vector>>>** prompt, you can run the **.q** or **.quit** command to exit the database interaction mode. The following information is displayed.

vector>>>.q
$

#### Emulator Support

This tool supports the Emulator.

#### FAQs

## How do I delete characters?

You can press **Ctrl+Backspace** to delete a single character and press **Ctrl+U** to delete all characters.
