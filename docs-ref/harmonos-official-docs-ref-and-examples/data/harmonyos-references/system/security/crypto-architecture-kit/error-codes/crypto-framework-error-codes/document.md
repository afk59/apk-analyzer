# Crypto Framework Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/33utVHhqQh2Ssp__y2nQ1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A97D2C6E827422274A5578929A56603D85D0C51B98F7EC0C0903EAEDB88766C2)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 17620001 Memory Operation Failed

**Error Message**

Memory operation failed.

**Description**

The memory operation failed.

**Possible Causes**

The memory allocation failed.

**Solution**

1.  Check whether the system is running properly.
2.  Check whether the service data is too long.

#### 17620002 Parameter Conversion Between ArkTS and C Failed

**Error Message**

Failed to convert parameters between arkts and c.

**Description**

The parameter conversion between ArkTS and C failed.

**Possible Causes**

An unexpected error occurs.

**Solution**

Check whether the system is running properly.

#### 17630001 Crypto Operation Error

**Error Message**

Crypto operation error.

**Description**

Failed to invoke the third-party cryptographic API.

**Possible Causes**

An error occurs when the cryptography framework interacts with a third-party algorithm library.

**Solution**

Check whether the input parameters of the API or associated APIs are correct.

For details about AES decryption failure, see [AES Decryption Failure Returning 17630001](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/crypto-aes-decryption-error-faq).
