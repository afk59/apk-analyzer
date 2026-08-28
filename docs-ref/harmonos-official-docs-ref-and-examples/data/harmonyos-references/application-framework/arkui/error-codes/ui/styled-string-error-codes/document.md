# Styled String Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/SxWQGUtNQ-aUKwtF4lqVvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56F73906E9AB9046DA04C7BF6512695C63C901F6194A299847149FA559494B6D)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 170001 Conversion Error

**Error Message**

Convert Error.

**Description**

This error code is reported when the **fromHtml** API failed to convert the input string into a corresponding styled string.

**Possible Causes**

The provided string is empty or does not comply with the HTML format.

**Solution**

N/A

#### 180101 Invalid Styled String

**Error Message**

invalid styled string.

**Description**

This error code is reported when the **ArkUI\_StyledString\_Descriptor** object in the styled string serialization C API is null.

**Possible Causes**

The styled string passed in the parameter is incorrect.

**Solution**

Check that the styled string is correctly passed in the parameter.
