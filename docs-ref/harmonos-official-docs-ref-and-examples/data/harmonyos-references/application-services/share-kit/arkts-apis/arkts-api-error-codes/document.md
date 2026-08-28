# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/MUrWr9AtTk-FmEzlGsyj5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062520Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C69FE64D0FD02493F0B7A7BBE41DF2E950E87CFAAC14217644B36C5415D912D1)

This topic describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1003700001 Number of Data Records Exceeding the Maximum

**Message**

The number of records exceeds the maximum.

**Description**

The number of data records exceeds the maximum.

**Possible causes**

The number of data records exceeds the maximum, which is **500** currently.

**Solution**

Limit the number of items that can be shared.

#### 1003702001 Invalid Data Record Format/Unsupported Data Type

**Message**

Record types are not support.(The batch and multiple selection modes support { @link UDMF.File } type records only.)

**Description**

The data record type is not supported.

**Possible causes**

1\. The data record type cannot be identified, is not supported, or is invalid.

2\. The **uri** and **content** parameters in **SharedRecord** are both empty.

3\. The value of **uri** is in an invalid format.

**Solution**

1\. Verify that the data type is a preset type defined by [UniformDataType](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md#uniformdatatype) or a known custom type.

2\. Verify that either **uri** or **content** is set in **SharedRecord**.

3\. Verify the format of the value of **uri**.

#### 1003702002 Data Transmitted Across Processes Is Oversized

**Message**

IPC data is oversized.

**Description**

The data transmitted across processes exceeds the upper limit (200 KB, including parameters in the **want** data.)

**Possible causes**

1.  The thumbnail is too large.
2.  There is too much text content.

**Solution**

1\. Compress the thumbnail binary data passed through **SharedRecord**.

2\. Limit the number of characters in the text that can be shared by a user.

#### 1003703001 Data Parsing Failure

**Message**

Parse data failed.

**Description**

The **want** data which contains key information about the shared data is invalid and cannot be parsed.

**Possible causes**

The input parameter is invalid during the [getContactInfo](../systemshare-system-share/document.md#section19799132782117) or [getSharedData](../systemshare-system-share/document.md#section661613319216) call. For example, the parsed data is not for sharing or a certain parameter does not exist.

**Solution**

1\. Terminate the shared data processing through the ability of the target app.

2\. Display a message to the user indicating the data sharing error.
