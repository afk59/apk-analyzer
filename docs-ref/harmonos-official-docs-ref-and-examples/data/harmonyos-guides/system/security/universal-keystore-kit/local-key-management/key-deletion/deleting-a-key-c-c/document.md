# Deleting a Key (C/C++)

To ensure data security, delete the key that is no longer required.

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

For example, delete a 256-bit HKDF key.

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Use [OH\_Huks\_DeleteKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_deletekeyitem) to delete the key.
    

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

struct OH\_Huks\_Param g\_testGenerateKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
                                                 {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
                                                 {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
                                                 {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

/\* 1. Generate a key. \*/
static OH\_Huks\_Result GenerateKeyHelper(const char \*alias)
{
    struct OH\_Huks\_Blob aliasBlob = {.size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias};
    struct OH\_Huks\_ParamSet \*testGenerateKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;

    do {
        ohResult = InitParamSet(&testGenerateKeyParamSet, g\_testGenerateKeyParam,
                                sizeof(g\_testGenerateKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = OH\_Huks\_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
    } while (0);
    
    OH\_Huks\_FreeParamSet(&testGenerateKeyParamSet);
    return ohResult;
}

static napi\_value DeleteKey(napi\_env env, napi\_callback\_info info)
{
    const char \*alias = "test\_key";
    struct OH\_Huks\_Blob keyAlias = {
        (uint32\_t)strlen("test\_key"),
        (uint8\_t \*)"test\_key"
    };
    
    /\* 1. Generate a key. \*/
    OH\_Huks\_Result genResult = GenerateKeyHelper(alias);
    if (genResult.errorCode != OH\_HUKS\_SUCCESS) {
        napi\_value ret;
        napi\_create\_int32(env, genResult.errorCode, &ret);
        return ret;
    }

    /\* 2. Delete the key. \*/
    struct OH\_Huks\_Result ohResult = OH\_Huks\_DeleteKeyItem(&keyAlias, nullptr);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
