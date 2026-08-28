# HMAC (C/C++)

Hash-based Message Authentication Code (HMAC) is a specific type of message authentication code (MAC) involving a cryptographic has function and a secret cryptographic key. For details about the scenarios and supported algorithm specifications, see [HMAC Overview and Algorithm Specifications](../hmac-overview-and-algorithm-specifications/document.md).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set.
    
3.  Use [OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem) to generate a key. For details about the HMAC specifications supported, see [Supported Algorithms](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md#supported-algorithms).
    

You can also import a key. For details about the supported algorithms, see [Supported Algorithms](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md#supported-algorithms).

**HMAC Generation**

1.  Obtain the key alias.
    
2.  Obtains the data to be calculated.
    
3.  Use [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset) to set algorithm parameters.
    
4.  Use [OH\_Huks\_InitSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession) to initialize a key session and obtain the session handle.
    
5.  Call [OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession) to finish the key session and obtain the hashed data.
    

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>

OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
                            uint32\_t paramCount)
{
    OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    ret = OH\_Huks\_BuildParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        return ret;
    }
    return ret;
}

static struct OH\_Huks\_Param g\_genHmacParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_HMAC},
                                                 {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_MAC},
                                                 {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
                                                 {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA384}};

static const uint32\_t HMAC\_COMMON\_SIZE = 1024;
OH\_Huks\_Result HksHmacTest(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*hmacParamSet,
                           const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*hashText)
{
    uint8\_t handleE\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleE};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, hmacParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, hmacParamSet, inData, hashText);
    return ret;
}

static napi\_value HmacKey(napi\_env env, napi\_callback\_info info)
{
    char tmpKeyAlias\[\] = "test\_hmac";
    struct OH\_Huks\_Blob keyAlias = {(uint32\_t)strlen(tmpKeyAlias), (uint8\_t \*)tmpKeyAlias};
    struct OH\_Huks\_ParamSet \*hmacParamSet = nullptr;
    OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&hmacParamSet, g\_genHmacParams, sizeof(g\_genHmacParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = OH\_Huks\_GenerateKeyItem(&keyAlias, hmacParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        char tmpInData\[\] = "HMAC\_MAC\_INDATA\_1";
        struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(tmpInData), (uint8\_t \*)tmpInData};
        uint8\_t cipher\[HMAC\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob hashText = {HMAC\_COMMON\_SIZE, cipher};

        ohResult = HksHmacTest(&keyAlias, hmacParamSet, &inData, &hashText);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);

    OH\_Huks\_FreeParamSet(&hmacParamSet);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
