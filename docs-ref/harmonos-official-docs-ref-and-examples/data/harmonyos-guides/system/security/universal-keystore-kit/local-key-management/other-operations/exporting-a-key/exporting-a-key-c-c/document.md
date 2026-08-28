# Exporting a Key (C/C++)

This topic walks you through on how to export the public key of a persistently stored asymmetric key. Currently, HUKS supports export of the ECC, RSA, Ed25519, X25519, and SM2 public keys.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/O6yHejt7RUqby9KCreO__w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9AB8F59719C738DAC5235B06587372DA32910BAF8ABD84ABFED1FD92BEBB2CC)

Lite wearables support export of only the RSA public keys.

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

1.  Set parameters.
    
    -   **keyAlias**: key alias encapsulated in an [OH\_Huks\_Blob](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) struct. The maximum length of the key alias is 128 bytes.
    -   **paramSetIn**: This parameter is reserved. Leave it empty.
    -   **key**: [OH\_Huks\_Blob](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hukstypeapi-oh-huks-blob) object used to hold the key exported. Ensure that there is enough memory for storing the key exported.
2.  Call [OH\_Huks\_GetKeyItemParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_getkeyitemparamset) to pass in the preceding parameters.
    
3.  Check the return value. If the operation is successful, the exported key is in the **key** field in the DER format defined in X.509. For details about the format, see [Public Key Material Format](../../../basic-concepts-of-local-key-management/document.md#public-key-material-format). If the operation fails, an error code is returned.
    

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
/\* Generate an ECC key. \*/
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

struct OH\_Huks\_Param g\_testGenerateKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
                                                 {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
                                                 {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
                                                 {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

static OH\_Huks\_Result GenerateKeyHelper(const char \*alias)
{
    struct OH\_Huks\_Blob aliasBlob = {.size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias};
    struct OH\_Huks\_ParamSet \*testGenerateKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        /\* 1. Initialize the key property set. \*/
        ohResult = InitParamSet(&testGenerateKeyParamSet, g\_testGenerateKeyParam,
                                sizeof(g\_testGenerateKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Generate a key. \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
    } while (0);
    OH\_Huks\_FreeParamSet(&testGenerateKeyParamSet);
    return ohResult;
}

static napi\_value ExportKey(napi\_env env, napi\_callback\_info info)
{
    /\* 1. Set the key alias. \*/
    const char \*alias = "test\_key";
    struct OH\_Huks\_Blob aliasBlob = { .size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias };
    /\* Generate a key. \*/
    OH\_Huks\_Result genResult = GenerateKeyHelper(alias);
    if (genResult.errorCode != OH\_HUKS\_SUCCESS) {
        napi\_value ret;
        napi\_create\_int32(env, genResult.errorCode, &ret);
        return ret;
    }
    /\* Request the memory for holding the public key to be exported. \*/
    uint8\_t \*pubKey = (uint8\_t \*)malloc(512); // Request memory based on the key size.
    if (pubKey == nullptr) {
        return nullptr;
    }
    struct OH\_Huks\_Blob keyBlob = { 256, pubKey };
    struct OH\_Huks\_Result ohResult;
    do {
        ohResult = OH\_Huks\_ExportPublicKeyItem(&aliasBlob, nullptr, &keyBlob);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    free(pubKey);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
