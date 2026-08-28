# SecurityAntivirus\_Antivirus

#### Overview

Defines antivirus app information.

**Start version**: 6.0.0(20)

**Related module**: [SecurityAntivirus](../../modules/securityantivirus/document.md)

**Header file**: [security\_antivirus.h](../../header-files/security-antivirus-h/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

const char \*[bundleName](#en-us_topic_0000002337386737_a165e68661c3730398273e1481d7f37f9)

 | 

Antivirus app package name.

 |
| 

const char \*[metadata](#en-us_topic_0000002337386737_ae66aa2161522f515b0ec6e1a5e4732e0)

 | 

Antivirus app information, including the current version number, last update time, antivirus switch status, and user ID.

 |

#### Member Variable Description

#### \[h2\]bundleName

const char \*SecurityAntivirus\_Antivirus::bundleName

**Description**

Antivirus app package name. For details about the requirements for the package name field, click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file).

## metadata

const char \*SecurityAntivirus\_Antivirus::metadata

**Description**

Antivirus app information, which is a JSON string containing the current version number, last update time, antivirus switch status, and user ID. For details about the requirements for the version number field, click [here](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file). The last update time is a 10-digit second-level or 13-digit millisecond-level timestamp. The antivirus switch status can only be **on** or **off**. The user ID is specified by **user\_id**. An example is as follows:

{
"version": "1.0.0.0",
"last\_update\_time": "1751877696",
"protection\_status": "on/off",
"user\_id": "100"
}
