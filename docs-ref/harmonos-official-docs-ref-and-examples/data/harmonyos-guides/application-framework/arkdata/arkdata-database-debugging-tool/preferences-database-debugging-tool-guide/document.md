# Preferences Database Debugging Tool Guide

Currently, when using the preferences database for development, debugging, and problem locating, developers are unable to view the content information in the database files, such as metadata and user data.

To improve developers' work efficiency, the database debugging tool allows developers to view the preference\_kv and preference\_xml databases on devices.

The preferences storage type corresponding to the preference\_kv database is the [GSKV](../../application-data-persistence/persisting-user-preferences-arkts/document.md#gskv) format, and the preference storage type corresponding to the preference\_xml database is the [XML](../../application-data-persistence/persisting-user-preferences-arkts/document.md#xml) format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/PQgy5H9nTQG3tar7F6A4jA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061922Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=414F389C47112FA541752FCEC483ED925E60E27E1C1570684CEF29436E4E67CF)

The preferences database debugging tool is available since HarmonyOS 6.0.0.

#### Environment Requirements

-   Before using this tool, you need to obtain the [hdc](../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md#environment-setup) tool, enable the [developer](../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432) mode, and run the **hdc shell** command.
-   This tool can be used only to debug applications. For details about how to configure applications for debugging, see [Running/Debugging Configuration](../../../../coding-and-debugging/debugging-your-app/running-debugging-configuration/document.md).

-   Connect the devices properly.

#### Preparations

-   Before using the Preferences debugging tool, switch to the target application path and then run the **arkdata** command to access this tool. (You need to use ArkData to configure relevant parameters to open the preferences database, and only after the database is successfully opened can you use the Preferences tool to add, delete, modify, and query data.)
    
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
    
    \-p
    
     | 
    
    Integer
    
     | 
    
    Database **pagesize**, a database opening configuration parameter, indicates the size of a single page to be stored. The default value is **32**; allowed values are **4**, **8**, **16**, **32**, and **64**.
    
     |
    | 
    
    \-c
    
     | 
    
    Integer
    
     | 
    
    Database **cacheSize** (or **bufferPoolSize**), a database opening configuration parameter, indicates the size of the memory cache pool. The default value is **2048**; allowed values are **2048** and **4096**.
    
     |
    | 
    
    \-h
    
     | 
    
    N/A
    
     | 
    
    Help information about the program.
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/49WKRtKITzC6MH4mQpW-CQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061922Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DFE6E73C5347BB4D54212B08CC05D2788211161864E898720B9FC6C51299A66)
    
    The **\-p** and **\-c** parameters of the preferences database debugging tool are invalid. If the values of **pagesize** and **cachesize** are within the specified range, the default values **32** and **2048** are used. If the values are beyond the specified range, an error is reported.
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ cd /data/app/el1/100/base/com.test.myapplication   // Go to the target application path. (The current path is an example. Go to the path based on your actual needs.)
    $ arkdata -t preference\_kv                           // -f is not specified, indicating that no database file is specified. By default, a database named "arkdata" is created in the data/preference\_kv directory of the current working directory.
    Enter ".help" for usage hints. 
    
    When opening the database in the path of a non-target application, if the **\-f** parameter is missing (which would trigger the default folder creation), the process of creating the **data/preference\_kv** folder hierarchy in the current directory fails. The error information is as follows:
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ arkdata -t preference\_kv
    \[unsucc\]Failed to create directory ./data/preference\_kv : Permission denied
    
    When opening the database in the path of a non-target application, the .db file fails to be created in the specified path. The error information is as follows:
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ arkdata -t preference\_kv -f ./preference\_kv
    \[GMDB SERVER\] \[GMERR-1013000\] multi-process init init unsucc!
    \[ERROR\] open db fail, ret = -5000.
    
    Cross-read and cross-write operations between databases preference\_xml and preference\_kv (which share the same name) are not allowed. When preference\_kv opens a preference\_xml database, an error is reported. When preference\_xml opens a preference\_kv database, the database is damaged. The error information is as follows:
    
    $ ls ./data/preference\_kv
    arkdata       arkdata.ctrl.dwr  arkdata.redo  arkdata.undo
    arkdata.ctrl  arkdata.map       arkdata.safe
    $ ls ./data/preference\_xml/
    arkdata  arkdata.lock
    $ arkdata -t preference\_kv -f ./data/preference\_xml/arkdata
    \[GMDB SERVER\] \[GMERR-1019003\] open-mode check init unsucc!
    \[unsucc\] open db fail, ret = -43000
    $ arkdata -t preference\_xml -f ./data/preference\_kv/arkdata
    Enter ".help" for usage hints.
    preference\_xml>>> /data/temp/./data/preference\_kv/arkdata:1: parser error : Start tag expected, '<' not found
    ^
    
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

The following table lists the commands supported by the preference\_kv and preference\_xml debugging tools.

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

get key:{key name}

 | 

Queries the database based on the specified key.

 |
| 

put key:{key name}

value:{value}

 | 

Inserts a KV pair to the database or updates the KV pair. You need to input two lines of commands, where the first line uses **key:** as the keyword and the second line uses **value:** as the keyword.

Example: **put key:123**

**value:345**

 |
| 

delete key:{key name}

 | 

Deletes a KV pair.

Example: **delete key:123**

 |
| 

delete

 | 

Deletes all contents in the table.

 |
| 

scan

 | 

Scans the full table.

NOTE:

preference\_xml supports full table scanning, but preference\_kv does not.

 |

#### Constraints

-   Numbers are of the int type by default. If a number is enclosed in quotation marks, the number is identified as string type.
-   Command line input data supports only the string, number, and boolean types. Other types will be converted to the string type.
-   Since hdc displays garbled characters when Chinese is used, the database debugging tool does not support Chinese.
-   This tool is supported on smartphones and PCs/2-in-1 devices.

#### Command Usage and Examples

## Displaying All Commands and Descriptions

After the preference\_kv or preference\_xml database is opened, you can run the **.help** command to view the supported commands.

preference\_kv>>> .help

preference\_xml>>> .help

## Creating or Opening an Existing Database

1.  Run the **hdc shell** command to enter the shell interaction mode.
2.  You must switch to the target application path, go to the path where the .db file exists, and run the **arkdata -t preference\_kv -f perfdata** or **arkdata -t preference\_xml -f perfdata** command to create a database.
    
    C:\\Users\\\*\*\*\*\*>hdc shell
    $ cd /data/app/el1/100/database/com.test.myapplication   // Go to the target application path. (The current path is an example. Go to the path based on your actual needs.)
    $ cd entry/rdb/                                          // Go to the path where the .db file exists. You need to have the read and write permissions on the .db file to create a new database.
    $ arkdata -t preference\_kv
    Enter ".help" for usage hints.
    preference\_kv>>>.q
    $ arkdata -t preference\_xml
    Enter ".help" for usage hints.
    preference\_xml>>> put key:1                               // preference\_xml needs to put a data record so that the database file can be created internally.
     ...>>> value:1
    preference\_xml>>> .q
    
3.  When a new database is created, the system automatically generates the following files. The tag **debug\_hap\_data\_file** indicates that the file is the target application file.
    
    $ ls -lZ ./data/preference\_kv/
    total 148
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  73728 2025-08-12 20:31 arkdata
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0   4112 2025-08-12 20:31 arkdata.ctrl
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  12304 2025-08-12 20:31 arkdata.ctrl.dwr
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0      0 2025-08-12 20:31 arkdata.map
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0    512 2025-08-12 20:31 arkdata.redo
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0      8 2025-08-12 20:31 arkdata.safe
    -rw-rw---- 1 shell shell u:object\_r:debug\_hap\_data\_file:s0  16384 2025-08-12 20:31 arkdata.undo
    
    $ ls -lZ ./data/preference\_xml/
    total 12
    -rw-rw---- 1 root ddms u:object\_r:debug\_hap\_data\_file:s0  105 2025-09-05 15:11 arkdata
    -rw-rw---- 1 root ddms u:object\_r:debug\_hap\_data\_file:s0    0 2025-09-05 15:11 arkdata.lock
    
4.  Open an existing database.
    
    $ arkdata -t preference\_kv -f ./data/preference\_kv/arkdata
    Enter ".help" for usage hints.
    preference\_kv>>>
    

## Inserting Data

At the **preference\_kv>>>** prompt, you can insert a KV pair using the **put** command, and the following information is displayed.

preference\_kv>>> put key:name
 ...>>> value:123
preference\_kv>>> put key:id\_name
 ...>>> value:'123'
preference\_kv>>> get key:name   // Result without quotation marks.
type int: 123
preference\_kv>>> get key:id\_name   // Result with quotation marks.
type string: 123

## Scanning the Full Table

-   At the **preference\_xml>>>** prompt, you can scan the full table using the **scan** command, and the following information is displayed.
    
    preference\_xml>>> scan
    ==========================PREFERENCES XML INFO============================
    DataCount:7
    ==========================PREFERENCES XML DATA============================
    ==========================Data Index:1==========================
    key:
    1
    value:
    type int: 1
    ==========================Data Index:2==========================
    key:
    2
    value:
    type int: 2
    ==========================Data Index:3==========================
    key:
    3
    value:
    type int: 3
    ==========================Data Index:4==========================
    key:
    4
    value:
    type int: 4
    ==========================Data Index:5==========================
    key:
    5
    value:
    type int: 5
    Press 'q' to quit, 'n' to continue: n
    ==========================Data Index:6==========================
    key:
    6
    value:
    type int: 6
    ==========================Data Index:7==========================
    key:
    7
    value:
    type int: 7
    preference\_xml>>>
    
-   preference\_kv does not support full table scanning. The following information is displayed.
    
    preference\_kv>>> scan
    \[unsucc\] Unable to parse command.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/YHNPYSJJTtGdHzbF9lCKZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061922Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC31735E4AA919873EB9FDAEEC0A771511C885D179E32F5D469A3F7064DAF252)

When the number of displayed data items reaches 5, the system asks you whether to continue displaying or exit. Enter **q** to exit the display or enter **n** to continue displaying.

## Querying a Single Value

At the **preference\_kv>>>** prompt, you can run the **get** command to query the specified KV pair, and the following information is displayed.

preference\_kv>>> get key:name
 No data for key = name  // No value available.

The values queried with and without quotation marks are different. The following information is displayed.

preference\_kv>>> put key:name
 ...>>> value:123
preference\_kv>>> put key:id\_name
 ...>>> value:'123'
preference\_kv>>> put key:name
 ...>>> value:true
preference\_kv>>> put key:name1
 ...>>> value:'true'
preference\_kv>>> get key:name      // Result of the number without quotation marks.
type int: 123
preference\_kv>>> get key:id\_name   // Result of the number with quotation marks.
type string: 123
preference\_kv>>> get key:name      // Result of true without quotation marks.
type bool: 1
preference\_kv>>> get key:name1     // Result of true with quotation marks.
type string: true

## Updating Data

At the **preference\_kv>>>** prompt, if the specified key exists, you can run the **put** command to update the KV pair. The following information is displayed.

preference\_kv>>> put key:name
 ...>>> value:x
preference\_kv>>> get key:name
type string: x
preference\_kv>>> put key:name
 ...>>> value:y
preference\_kv>>> get key:name
type string: y

## Deleting Data

At the **preference\_kv>>>** prompt, you can run the **delete** command to delete a specified KV pair. The following information is displayed.

preference\_kv>>> get key:name
type string: y
preference\_kv>>> delete key:name
preference\_kv>>> get key:name
 No data for key = key:name

If the **delete** command is used without specifying a KV pair, all data in the table is deleted. The following information is displayed.

preference\_kv>>> get key:name
type int: xx
preference\_kv>>> get key:id\_name 
type int: yy
preference\_kv>>> delete
preference\_kv>>> get key:name
 No data for key = name
preference\_kv>>> get key:id\_name 
 No data for key = id\_name 

At the **preference\_kv>>>** prompt, you can run the **.q** or **.quit** command to exit the database interaction mode. The following information is displayed.

preference\_kv>>>.q
$ 

#### Emulator Support

This tool supports the Emulator.

#### FAQs

## How do I delete characters?

You can press **Ctrl+Backspace** to delete a single character and press **Ctrl+U** to delete all characters.
