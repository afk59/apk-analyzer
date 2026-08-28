# App Check Tool

#### Overview

The app check tool is used to analyze and detect application installation packages. Based on the parameter settings, it scans the HAP, HSP, or APP file in the specified path and generates detection reports, providing data support for you to optimize the package structure or locate problems. The tool provides the following functions:

-   Scans for duplicate files.
-   Scans for large files (files that exceed the specified size).
-   Collects statistics on the size and proportion of each type of file.
    

By default, the tool generates detection reports in JSON and HTML format.

The **app\_check\_tool.jar** package of the tool is stored in the **toolchains** directory of the SDK.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/I7FoK6d2Q-u-xcPVVd336g/en-us_image_0000002568684861.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062032Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63D149DE557AD264584E771AF4E078C0CDF849988E3F12073EDBD548ACC28C17)

#### Constraints

-   The app check tool must run in Java 8 or later.
-   The directory where the app check tool is running must have the read and write permissions.

#### Scanning for Duplicate Files

**Command example**

java -jar app\_check\_tool.jar --input ./test.app --out-path ./test --stat-duplicate true

**Table 1 Parameters of the command**

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| \--input | Yes | Path of the HAP, HSP, or APP file. |
| \--out-path | Yes | Path of the detection reports. |
| \--stat-duplicate | No | 
Whether to scan for duplicate files. The default value is **false**.

**true**: Scanning is enabled.

**false**: Scanning is disabled.

 |

**Detection report in JSON format**

\[{
    "taskType":1,
    "taskDesc":"find the duplicated files",
    "param":"--stat-duplicate",
    "startTime":"2023-11-17 14:48:01:265",
    "stopTime":"2023-11-17 14:48:01:434",
    "result":\[{
        "md5":"975c41f5727b416b1ffefa5bb0f073b2",
        "size":1108880,
        "files":\[
            "/application-entry-default.hap/libs/armeabi-v7a/example.so",
            "/entry-default.hap/libs/armeabi-v7a/example.so"
        \]
    }\]
}\]

**Table 2 Fields of the output**

| Field | Type | Description |
| :-- | :-- | :-- |
| taskType | int | Type of the task. The value **1** means a task for scanning for duplicate files. |
| taskDesc | String | Description of the task. |
| param | String | Parameter passed in by the scanning program. |
| startTime | String | Start time of the task. |
| stopTime | String | End time of the task. |
| result | Struct | Duplicate file statistics result. For details, see Table 3. |

**Table 3 Fields of the result**

| Field | Type | Description |
| :-- | :-- | :-- |
| md5 | String | MD5 value of the duplicate files. |
| size | int | Size of the duplicate files, in bytes. |
| files | Vector<String> | Paths of the duplicate files. |

#### Scanning for Large Files

**Command example**

java -jar app\_check\_tool.jar --input ./test.app --out-path ./test --stat-file-size 4

**Table 4 Parameters of the command**

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| \--input | Yes | Path of the HAP, HSP, or APP file. |
| \--out-path | Yes | Path of the detection reports. |
| \--stat-file-size | No | 
File size, in KB. A file with the size larger than this value is treated as a large file.

The value ranges from 0 to 4294967295, in KB.

 |

**Detection report in JSON format**

\[{
    "taskType":2,
    "taskDesc":"find files whose size exceed the limit size",
    "param":"--stat-file-size 4",
    "startTime":"2023-11-17 14:48:01:458",
    "stopTime":"2023-11-17 14:48:01:491",
    "result":\[{
            "file":"/application-entry-default.hap/libs/x86\_64/example.so",
            "size":1292840
    }\]
}\]

**Table 5 Fields of the output**

| Field | Type | Description |
| :-- | :-- | :-- |
| taskType | int | Type of the task. The value **2** means a task for scanning for large files. |
| taskDesc | String | Description of the task. |
| param | String | Parameter passed in by the scanning program. |
| startTime | String | Start time of the task. |
| stopTime | String | End time of the task. |
| result | Struct | Statistics result of files that exceed the specified size. For details, see Table 6. |

**Table 6 Fields of the result**

| Field | Type | Description |
| :-- | :-- | :-- |
| file | String | Path of a file. |
| size | int | Size of the file, in bytes. |

#### Collecting Statistics on the Size and Proportion by File Type

**Command example**

java -jar app\_check\_tool.jar --input ./test.app --out-path ./test --stat-suffix true

**Table 7 Parameters of the command**

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| \--input | Yes | Path of the HAP, HSP, or APP file. |
| \--out-path | Yes | Path of the detection reports. |
| \--stat-suffix | No | 
Whether to collect statistics on the size and proportion of each type of file. The default value is **false**.

**true**: Scanning is enabled.

**false**: Scanning is disabled.

 |

**Detection report in JSON format**

\[{
    "taskType":3,
    "taskDesc":"show files group by file type\[.suffix\]",
    "param":"--stat-suffix",
    "startTime":"2023-11-17 14:48:01:497",
    "stopTime":"2023-11-17 14:48:01:537",
    "pathList":\[
        "test.app/application-entry-default.hap",
        "test.app/entry-default.hap"
    \],
    "result":\[{
        "suffix":"so",
        "totalSize":1292840,
        "files":\[{
            "compress":"false",
            "file":"/application-entry-default.hap/libs/x86\_64/example.so",
            "size":1292840
        }\]
    },
    {
        "suffix":"abc",
        "totalSize":84852,
        "files":\[{
            "file":"/application-entry-default.hap/ets/modules.abc",
            "size":76304
        },
        {
            "file":"/entry-default.hap/ets/modules.abc",
            "size":8548
        }\]
    }\]
}\]

**Table 8 Fields of the output**

| Field | Type | Description |
| :-- | :-- | :-- |
| taskType | int | Type of the task. The value **3** means a task for collecting statistics on the size and proportion of each type of file. |
| taskDesc | String | Description of the task. |
| param | String | Parameter passed in by the scanning program. |
| startTime | String | Start time of the task. |
| stopTime | String | End time of the task. |
| pathList | Vector<String> | Paths of multiple HAP and HSP files. |
| result | Struct | Statistics result of the file size proportion of each type. For details, see Table 9. |

**Table 9 Fields of the result**

| Field | Type | Description |
| :-- | :-- | :-- |
| suffix | String | File name extension. |
| totalSize | int | Total size of scanned files of the same type, in bytes. |
| files | Struct | Path and size of files of the same type. For details, see Table 10. |

**Table 10 Fields of the Struct**

| Field | Type | Description |
| :-- | :-- | :-- |
| file | String | Path of a file. |
| size | int | File size, in bytes. |
| compress | bool | 
Whether the file is compressed. This field is displayed only for .so files.

**true**: The file is compressed.

**false**: The file is not compressed.

 |
