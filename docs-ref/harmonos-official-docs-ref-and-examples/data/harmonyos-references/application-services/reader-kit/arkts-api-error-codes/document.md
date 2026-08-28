# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/yQ9CeSUQSxGLxRC810vDIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F8F781D28BC310CF070E28A2C94455281177ABFC2406F9879201A18659E68E6)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

#### 1016900002

**Message**

Read Page Component is not initialized.

**Description**

**ReadPageComponent** is not initialized.

**Solution**

1.  Initialize **ReadPageComponent** before calling its capabilities.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016900003

**Message**

Invalid request.

**Description**

Invalid request.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016900999

**Message**

Other error.

**Description**

Other error.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016910001

**Message**

Invalid spine item.

**Description**

Invalid content.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016910002

**Message**

Unexpected spine item resource data.

**Description**

Abnormal content resource data.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016910003

**Message**

Spine item resource data out of range.

**Description**

No **SpineItem** content resource corresponding to the **spineIndex** value is found.

**Solution**

1.  Check whether the resource data is the result after parsing.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1016910004

**Message**

Invalid caller.

**Description**

Invalid caller.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1017000001

**Message**

Book parser is not initialized

**Description**

The book parser is not initialized.

**Solution**

Check whether [getDefaultHandler](../arkts-apis/bookparser-book-parsing-capability/document.md#section896820167243) is called successfully and [registerBookParser](../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section181215815104) is called to register the handler prior to [startPlay](../arkts-apis/readercore-reader-kit-core-capabilities/document.md#section3667128165411).

#### 1017000999

**Message**

Other error.

**Description**

Other error.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1017010001

**Message**

Invalid spine item.

**Description**

Invalid content.

**Solution**

1.  Check whether the resource data is the result after parsing.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1017010002

**Message**

Invalid request.

**Description**

Invalid request.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1017010003

**Message**

Book file format is unexpected.

**Description**

Book format error.

**Solution**

1.  Check whether the book format is **txt**, **epub**, **mobi**, **azw3**, or **azw**.
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1017010004

**Message**

File is not existed.

**Description**

The file does not exist.

**Solution**

1.  Ensure that the book exists in the [app sandbox directory](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-sandbox-directory) (**/haps/entry/files/**).
2.  Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
