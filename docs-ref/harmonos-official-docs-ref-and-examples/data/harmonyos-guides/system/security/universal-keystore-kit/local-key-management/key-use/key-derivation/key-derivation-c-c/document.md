# Key Derivation (C/C++)

This topic walks you through on how to derive a key using HKDF and PBKDF2. For details about the scenarios and supported algorithm specifications, see [Supported Algorithms](../key-derivation-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set. You can set **OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** (optional) to specify how the key derived from this key is managed.
    
    -   If this tag is set to **OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS**, the derived key is managed by HUKS. That is, the derived key is always in a secure environment throughout its lifecycle.
        
    -   If this tag is set to **OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED**, the derived key will be returned to the caller for management. That is, the service side ensures the key security.
        
    -   If this tag is not set, the derived key can be either managed by HUKS or returned to the caller for management. The key protection mode can be set in the subsequent key derivation on the service side.
        
3.  Use [OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem) to generate a key. For details, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    

Alternatively, you can [import a key](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

**Key Derivation**

1.  Obtain the key alias and set the **HuksOptions** parameter.
    
    You can set **OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** to specify how the derived key is managed.
    
    | Key Generation | Key Derivation | Specifications |
    | :-- | :-- | :-- |
    | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
    | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
    | The tag is not set. | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
    | The tag is not set. | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
    | The tag is not set. | The tag is not set. | The key is returned to the caller for management. |
    
    Note: The tag value set in key derivation should not conflict with the tag value set in key generation. The above table lists only valid settings.
    
2.  Use [OH\_Huks\_InitSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession) to initialize a key session and obtain the session handle.
    
3.  Use [OH\_Huks\_UpdateSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_updatesession) to update the key session.
    
4.  Use [OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession) to end the key session and finish derivation.
    

**Key Deletion**

Use **OH\_Huks\_DeleteKeyItem** to delete the key that is not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-c-c/document.md).

#### Development Cases

## HKDF

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>

static OH\_Huks\_Result InitParamSet(struct OH\_Huks\_ParamSet \*\*paramSet, const struct OH\_Huks\_Param \*params,
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

static const uint32\_t DERIVE\_KEY\_SIZE\_32 = 32;
static const uint32\_t DERIVE\_KEY\_SIZE\_256 = 256;
static struct OH\_Huks\_Blob g\_deriveKeyAlias = {(uint32\_t)strlen("test\_derive"), (uint8\_t \*)"test\_derive"};
static struct OH\_Huks\_Param g\_genDeriveParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_hkdfParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_HKDF},
                                              {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
                                              {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
                                              {.tag = OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_32}};
static struct OH\_Huks\_Param g\_hkdfFinishParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_deriveKeyAlias},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256}};
static const uint32\_t COMMON\_SIZE = 2048;
static const char \*G\_DERIVE\_IN\_DATA = "Hks\_HKDF\_Derive\_Test\_0\_string";
static OH\_Huks\_Result PerformHkdfDerivation(const struct OH\_Huks\_Blob \*genAlias,
    struct OH\_Huks\_ParamSet \*hkdfParamSet,
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet,
    const struct OH\_Huks\_Blob &inData)
{
    OH\_Huks\_Result ohResult;
    // Init
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDerive = {sizeof(uint64\_t), handleD};
    ohResult = OH\_Huks\_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Update
    uint8\_t tmpOut\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outData = {COMMON\_SIZE, tmpOut};
    ohResult = OH\_Huks\_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Finish
    uint8\_t outDataD\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataDerive = {COMMON\_SIZE, outDataD};
    ohResult = OH\_Huks\_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
    return ohResult;
}

napi\_value HkdfDeriveKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob genAlias = {(uint32\_t)strlen("test\_signVerify"), (uint8\_t \*)"test\_signVerify"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(G\_DERIVE\_IN\_DATA), (uint8\_t \*)G\_DERIVE\_IN\_DATA};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&genParamSet, g\_genDeriveParams, sizeof(g\_genDeriveParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }

        ohResult = InitParamSet(&hkdfParamSet, g\_hkdfParams, sizeof(g\_hkdfParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        // finish paramset
        ohResult =
            InitParamSet(&hkdfFinishParamSet, g\_hkdfFinishParams, sizeof(g\_hkdfFinishParams) /
              sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 1. Generate a key. \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Derive a key. \*/
        ohResult = PerformHkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
    } while (0);
    (void)OH\_Huks\_DeleteKeyItem(&genAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(&g\_deriveKeyAlias, nullptr);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&hkdfParamSet);
    OH\_Huks\_FreeParamSet(&hkdfFinishParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## PBKDF2

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

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
static const uint32\_t DERIVE\_KEY\_SIZE\_32 = 32;
static const uint32\_t DERIVE\_KEY\_SIZE\_256 = 256;
static const uint32\_t DERIVE\_KEY\_ITERATION = 10000;
static const uint32\_t SALT\_SIZE = 8;
static const char DERIVE\_KEY\_SALT\[SALT\_SIZE\] = "mysalt1";
static struct OH\_Huks\_Blob g\_deriveKeyAlias = {(uint32\_t)strlen("test\_derive"), (uint8\_t \*)"test\_derive"};
static struct OH\_Huks\_Param g\_genDeriveParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_hkdfParams\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_PBKDF2},
                                              {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
                                              {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_SHA256},
                                              {.tag = OH\_HUKS\_TAG\_DERIVE\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_32},
                                              {.tag = OH\_HUKS\_TAG\_ITERATION, .uint32Param = DERIVE\_KEY\_ITERATION},
                                              {.tag = OH\_HUKS\_TAG\_SALT,
                                               .blob = {
                                                   .size = SALT\_SIZE,
                                                   .data = (uint8\_t \*) DERIVE\_KEY\_SALT
                                               }}};
static struct OH\_Huks\_Param g\_hkdfFinishParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_deriveKeyAlias},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = DERIVE\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DERIVE},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB}};
static const uint32\_t COMMON\_SIZE = 1024;
static const char \*G\_DERIVE\_IN\_DATA = "Hks\_PBKDF2\_Derive\_Test\_0\_string";
static OH\_Huks\_Result PerformPbkdfDerivation(const struct OH\_Huks\_Blob \*genAlias,
    struct OH\_Huks\_ParamSet \*hkdfParamSet,
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet,
    const struct OH\_Huks\_Blob &inData)
{
    OH\_Huks\_Result ohResult;
    // Init
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDerive = {sizeof(uint64\_t), handleD};
    ohResult = OH\_Huks\_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Update
    uint8\_t tmpOut\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outData = {COMMON\_SIZE, tmpOut};
    ohResult = OH\_Huks\_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    // Finish
    uint8\_t outDataD\[COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataDerive = {COMMON\_SIZE, outDataD};
    ohResult = OH\_Huks\_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
    return ohResult;
}

napi\_value PbkdfDeriveKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob genAlias = {(uint32\_t)strlen("test\_signVerify"), (uint8\_t \*)"test\_signVerify"};
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(G\_DERIVE\_IN\_DATA), (uint8\_t \*)G\_DERIVE\_IN\_DATA};
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*hkdfFinishParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&genParamSet, g\_genDeriveParams, sizeof(g\_genDeriveParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = InitParamSet(&hkdfParamSet, g\_hkdfParams, sizeof(g\_hkdfParams) /
                     sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult =InitParamSet(&hkdfFinishParamSet, g\_hkdfFinishParams, sizeof(g\_hkdfFinishParams) /
              sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 1. Generate a key. \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&genAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Derive a key. \*/
        ohResult = PerformPbkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
    } while (0);
    (void)OH\_Huks\_DeleteKeyItem(&genAlias, nullptr);
    (void)OH\_Huks\_DeleteKeyItem(&g\_deriveKeyAlias, nullptr);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&hkdfParamSet);
    OH\_Huks\_FreeParamSet(&hkdfFinishParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
