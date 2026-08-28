# Generating a Key (C/C++)

This topic walks you through on how to randomly generate a key with the ECC algorithm. For details about the scenarios and supported algorithms, see [Supported Algorithms](../key-generation-overview-and-algorithm-specifications/document.md#supported-algorithms).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/9BHXWZdPRcyJjyaplCN05w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0DC5F557183EF02EC26F6E9B4360EFBEF6D49C5F30820BD2505C90FF8219995)

Key aliases must not contain sensitive information, such as personal data.

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set. Construct **paramSet** using [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset), [OH\_Huks\_AddParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_addparams), and [OH\_Huks\_BuildParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_buildparamset).
    
    The key property set must contain the [OH\_Huks\_KeyAlg](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keyalg), [OH\_Huks\_KeySize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keysize), and [OH\_Huks\_KeyPurpose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keypurpose) properties. Note that a key can have only one purpose, and the purpose specified during key generation must match the key purpose during usage. Otherwise, an exception occurs.
    
3.  Call [OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem) and pass in the key alias and key property set to generate a key.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Kr0BuZsNRpWdvtAjiLIpug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062010Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A786CEE8B7E2A65B6C30748383D168055E79CDC9EEE20D5207E68F56169E6729)

If the service uses the same key alias to call the HUKS API to generate a key again, HUKS will generate a new key and overwrite the historical key file.

/\* Generate an ECC key. \*/
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

static napi\_value GenerateKey(napi\_env env, napi\_callback\_info info)
{
    /\* 1. Set the key alias. \*/
    const char \*alias = "test\_generate";
    struct OH\_Huks\_Blob aliasBlob = {.size = (uint32\_t)strlen(alias), .data = (uint8\_t \*)alias};
    struct OH\_Huks\_ParamSet \*testGenerateKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        /\* 2. Initialize the key property set. \*/
        ohResult = InitParamSet(&testGenerateKeyParamSet, g\_testGenerateKeyParam,
                                sizeof(g\_testGenerateKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3. Generate a key. \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
    } while (0);
    OH\_Huks\_FreeParamSet(&testGenerateKeyParamSet);
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
