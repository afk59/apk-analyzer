# Environment Variable Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/SlPHV6YVQn2a2Yt6c9nXsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F99F34DE1BC92A6122FF6C7DA00017C7909CBA16B15AC2FB7840CD28A98E5734)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 140000 Invalid @Env Input Parameter

**Error Message**

Invalid key for @Env

**Description**

This error code is reported when an invalid parameter is passed to [@Env](../../../arkts-components/responsive-environment-variable/env-environment-variable/document.md#env).

**Possible Causes**

The parameter provided to @Env is invalid. @Env supports only parameters of the [SystemProperties](../../../arkts-components/responsive-environment-variable/env-environment-variable/document.md#systemproperties) type. For details, see [Supported Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-env-system-property#supported-parameters).

**Solution**

Ensure that the @Env parameter type is of the [SystemProperties](../../../arkts-components/responsive-environment-variable/env-environment-variable/document.md#systemproperties) type. For details, see [@Env: Environment Variable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-env-system-property).
