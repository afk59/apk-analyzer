# Key Agreement (C/C++)

This topic uses X25519, DH, and ECDH as an example to demonstrate how to perform key agreement for HUKS-managed keys. For details about the scenarios and supported algorithm specifications, see [Supported Algorithms](../key-agreement-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

**Key Generation**

Generate an asymmetric key for device A and device B each. For details, see [Key Generation](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md) or [Key Import](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

When generating a key, you can specify the **OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** parameter (optional) to indicate whether the key generated is managed by HUKS.

**Key Export**

Export the public key of the asymmetric key pair of device A and device B. For details, see [Key Export](../../../other-operations/exporting-a-key/exporting-a-key-arkts/document.md).

**Key Agreement**

Perform key agreement using the public key of the peer device and private key of the local device (that is, public key of device B and private key of device A for device A, and public key of device A and private key of device B for device B) to produce a shared secret.

During key agreement, you can set **OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG** (optional) to specify how the shared secret generated is managed.

-   If this tag is set to **OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS**, the shared secret is managed by HUKS. That is, the shared secret is always in a secure environment throughout its lifecycle.
    
-   If this tag is set to **OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED**, the shared secret generated will be returned to the caller for management. That is, the service side ensures the key security.
    
-   If this tag is not set, the shared secret generated can be either managed by HUKS or returned to the caller for management. The key protection mode can be set in the subsequent key agreement on the service side.
    

| Key Generation | Key Agreement | Specifications |
| :-- | :-- | :-- |
| OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
| OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
| The tag is not set. | OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | The key is managed by HUKS. |
| The tag is not set. | OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | The key is returned to the caller for management. |
| The tag is not set. | The tag is not set. | The key is returned to the caller for management. |

Note: The tag value set in key agreement should not conflict with the tag value set in key generation. The above table lists only valid settings.

**Key Deletion**

Delete the keys from device A and device B when the keys are not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-c-c/document.md).

#### Development Cases

The following uses the X25519, DH, and ECDH keys as examples for key agreement.

## X25519 Asymmetric Key Agreement

Prepare the X25519 key agreement materials.

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* Initialize parameters. \*/
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
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1\_final"};
/\* Set the key parameter set. \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static const uint32\_t X25519\_COMMON\_SIZE = 256;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksX25519AgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksX25519AgreeKeyAliasTest001\_2"};

Perform key agreement.

/\* Export a key. \*/
OH\_Huks\_Result HksX25519AgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
    struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
    const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_X25519\_Agree\_Test";
/\* Perform key agreement. \*/
OH\_Huks\_Result HksX25519AgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
    const struct OH\_Huks\_ParamSet \*initParamSet,
    const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[X25519\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {X25519\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* Generate an asymmetric key pair for device A. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* Generate an asymmetric key pair for device B. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* Perform key agreement. \*/
    ohResult = HksX25519AgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

/\* Key agreement process. \*/
napi\_value X25519AgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = OH\_HUKS\_AES\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = OH\_HUKS\_AES\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = X25519\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = X25519\_COMMON\_SIZE, .data = nullptr};
    OH\_Huks\_Result ohResult;
    do {
        /\* 1. Set the key alias and key parameter set. \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Generate keys on device A and device B. \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3. Export the public key from device A and device B separately. \*/
        ohResult = HksX25519AgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4. Perform key agreement on device A and device B. \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5. Delete the keys from device A and device B. \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## DH Key Agreement

Prepare the DH key agreement materials.

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* Initialize parameters. \*/
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
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_1\_final"};
/\* Set the key parameter set. \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\_2\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_DH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_DH\_KEY\_SIZE\_2048}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\_2\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_ECB},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static const uint32\_t DH\_COMMON\_SIZE = 2048;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksDHAgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksDHAgreeKeyAliasTest001\_2"};

Perform key agreement.

static OH\_Huks\_Result MallocAndCheckBlobData(struct OH\_Huks\_Blob \*blob, const uint32\_t blobSize)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (blobSize == 0 || blobSize > DH\_COMMON\_SIZE) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
        return ret;
    }
    blob->data = (uint8\_t \*)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    return ret;
}
/\* Export a key. \*/
OH\_Huks\_Result HksDHAgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
    struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
    const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_DH\_Agree\_Test";
/\* Perform key agreement. \*/
OH\_Huks\_Result HksDHAgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
    const struct OH\_Huks\_ParamSet \*initParamSet,
    const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[DH\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {DH\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* Generate an asymmetric key pair for device A. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* Generate an asymmetric key pair for device B. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* Perform key agreement. \*/
    ohResult = HksDHAgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

/\* Key agreement process. \*/
napi\_value DhAgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = DH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = DH\_COMMON\_SIZE, .data = nullptr};

    OH\_Huks\_Result ohResult;
    do {
        /\* 1. Set the key alias and key parameter set. \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Generate keys on device A and device B. \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3. Export the public key from device A and device B separately. \*/
        ohResult = HksDHAgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4. Perform key agreement on device A and device B. \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5. Delete the keys from device A and device B. \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## ECDH Key Agreement

Prepare the ECDH key agreement materials.

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

/\* Initialize parameters. \*/
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
static const uint32\_t IV\_SIZE = 16;
static uint8\_t IV\[IV\_SIZE\] = {0}; // this is a test value, for real use the iv should be different every time
static struct OH\_Huks\_Blob g\_keyAliasFinal1001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1\_final"};
/\* Set the key parameter set. \*/
static struct OH\_Huks\_Param g\_genAgreeParams\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECC},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};
static struct OH\_Huks\_Param g\_agreeParamsInit01\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECDH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_agreeParamsFinish01\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal1001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_CBC}};
static struct OH\_Huks\_Blob g\_keyAliasFinal2001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_2\_final"),
                                                  (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_2\_final"};
static struct OH\_Huks\_Param g\_agreeParamsInit02\[\] = {
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_ECDH},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_ECC\_KEY\_SIZE\_256}};
static struct OH\_Huks\_Param g\_agreeParamsFinish02\[\] = {
    {.tag = OH\_HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG, .uint32Param = OH\_HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS},
    {.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_AGREE},
    {.tag = OH\_HUKS\_TAG\_KEY\_ALIAS, .blob = g\_keyAliasFinal2001},
    {.tag = OH\_HUKS\_TAG\_PADDING, .uint32Param = OH\_HUKS\_PADDING\_NONE},
    {.tag = OH\_HUKS\_TAG\_BLOCK\_MODE, .uint32Param = OH\_HUKS\_MODE\_CBC}};
static const uint32\_t ECDH\_COMMON\_SIZE = 1024;
static struct OH\_Huks\_Blob g\_keyAlias01001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_1"),
                                              (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_1"};
static struct OH\_Huks\_Blob g\_keyAlias02001 = {(uint32\_t)strlen("HksECDHAgreeKeyAliasTest001\_2"),
                                              (uint8\_t \*)"HksECDHAgreeKeyAliasTest001\_2"};

Functions for ECDH key agreement, including memory allocation, parameter initialization, key generation, and resource cleanup.

static OH\_Huks\_Result MallocAndCheckBlobData(struct OH\_Huks\_Blob \*blob, const uint32\_t blobSize)
{
    struct OH\_Huks\_Result ret;
    ret.errorCode = OH\_HUKS\_SUCCESS;
    if (blobSize == 0 || blobSize > ECDH\_COMMON\_SIZE) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
        return ret;
    }
    blob->data = (uint8\_t \*)malloc(blobSize);
    if (blob->data == NULL) {
        ret.errorCode = OH\_HUKS\_ERR\_CODE\_INTERNAL\_ERROR;
    }
    return ret;
}

/\* Export a key. \*/
OH\_Huks\_Result HksEcdhAgreeExport(const struct OH\_Huks\_Blob \*keyAlias1, const struct OH\_Huks\_Blob \*keyAlias2,
                                  struct OH\_Huks\_Blob \*publicKey1, struct OH\_Huks\_Blob \*publicKey2,
                                  const struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ret = OH\_Huks\_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}
static const char \*IN\_DATA = "Hks\_ECDH\_Agree\_Test\_000000000000000000000000000000000000000000000000000000000000"
                              "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
                              "0000000000000000000000000000000000000000000000000000000000000000000000000\_string";
/\* Perform key agreement. \*/
OH\_Huks\_Result HksEcdhAgreeFinish(const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_Blob \*publicKey,
                                  const struct OH\_Huks\_ParamSet \*initParamSet,
                                  const struct OH\_Huks\_ParamSet \*finishParamSet, struct OH\_Huks\_Blob \*outData)
{
    struct OH\_Huks\_Blob inData = {(uint32\_t)strlen(IN\_DATA), (uint8\_t \*)IN\_DATA};
    uint8\_t handleU\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handle = {sizeof(uint64\_t), handleU};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, initParamSet, &handle, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    uint8\_t outDataU\[ECDH\_COMMON\_SIZE\] = {0};
    struct OH\_Huks\_Blob outDataUpdate = {ECDH\_COMMON\_SIZE, outDataU};
    ret = OH\_Huks\_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, finishParamSet, &inData, outData);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    return ret;
}

static OH\_Huks\_Result InitializeAgreeParamSets(struct OH\_Huks\_ParamSet \*\*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet01,
    struct OH\_Huks\_ParamSet \*\*finishParamSet01,
    struct OH\_Huks\_ParamSet \*\*initParamSet02,
    struct OH\_Huks\_ParamSet \*\*finishParamSet02)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = InitParamSet(genParamSet, g\_genAgreeParams,
                            sizeof(g\_genAgreeParams) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet01, g\_agreeParamsInit01,
                            sizeof(g\_agreeParamsInit01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet01, g\_agreeParamsFinish01,
                            sizeof(g\_agreeParamsFinish01) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(initParamSet02, g\_agreeParamsInit02,
                            sizeof(g\_agreeParamsInit02) / sizeof(OH\_Huks\_Param));
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    ohResult = InitParamSet(finishParamSet02, g\_agreeParamsFinish02,
                            sizeof(g\_agreeParamsFinish02) / sizeof(OH\_Huks\_Param));
    return ohResult;
}

static OH\_Huks\_Result GenerateKeyPair(struct OH\_Huks\_ParamSet \*genParamSet)
{
    OH\_Huks\_Result ohResult;
    
    /\* Generate an asymmetric key pair for device A. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias01001, genParamSet, nullptr);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    
    /\* Generate an asymmetric key pair for device B. \*/
    ohResult = OH\_Huks\_GenerateKeyItem(&g\_keyAlias02001, genParamSet, nullptr);
    return ohResult;
}

static OH\_Huks\_Result KeyAgreement(struct OH\_Huks\_Blob \*g\_keyAlias,
    struct OH\_Huks\_Blob \*publicKey,
    struct OH\_Huks\_Blob \*outData,
    struct OH\_Huks\_ParamSet \*initParamSet,
    struct OH\_Huks\_ParamSet \*finishParamSet)
{
    OH\_Huks\_Result ohResult;
    
    ohResult = MallocAndCheckBlobData(outData, outData->size);
    if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
        return ohResult;
    }
    /\* Perform key agreement. \*/
    ohResult = HksEcdhAgreeFinish(g\_keyAlias, publicKey, initParamSet, finishParamSet, outData);
    return ohResult;
}

static void CleanKey(struct OH\_Huks\_Blob \*genKeyAlias,
    struct OH\_Huks\_Blob \*genKeyAliasFinal,
    struct OH\_Huks\_ParamSet \*genParamSet,
    struct OH\_Huks\_ParamSet \*\*initParamSet,
    struct OH\_Huks\_ParamSet \*\*finishParamSet)
{
    OH\_Huks\_DeleteKeyItem(genKeyAlias, genParamSet);
    OH\_Huks\_DeleteKeyItem(genKeyAliasFinal, NULL);
    OH\_Huks\_FreeParamSet(initParamSet);
    OH\_Huks\_FreeParamSet(finishParamSet);
}

The complete workflow of ECDH key agreement is as follows:

/\* Key agreement process. \*/
napi\_value EcdhAgreeKey(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet01 = nullptr;
    struct OH\_Huks\_ParamSet \*initParamSet02 = nullptr;
    struct OH\_Huks\_ParamSet \*finishParamSet02 = nullptr;
    struct OH\_Huks\_Blob publicKey01 = {.size = OH\_HUKS\_ECC\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob publicKey02 = {.size = OH\_HUKS\_ECC\_KEY\_SIZE\_256, .data = nullptr};
    struct OH\_Huks\_Blob outData01 = {.size = ECDH\_COMMON\_SIZE, .data = nullptr};
    struct OH\_Huks\_Blob outData02 = {.size = ECDH\_COMMON\_SIZE, .data = nullptr};
    OH\_Huks\_Result ohResult;
    do {
        /\* 1. Set the key alias and key parameter set. \*/
        ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
                                            &initParamSet02, &finishParamSet02);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Generate keys on device A and device B. \*/
        ohResult = GenerateKeyPair(genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3. Export the public key from device A and device B separately. \*/
        ohResult = HksEcdhAgreeExport(&g\_keyAlias01001, &g\_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 4. Perform key agreement on device A and device B. \*/
        ohResult = KeyAgreement(&g\_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = KeyAgreement(&g\_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
    } while (0);
    free(publicKey01.data);
    free(publicKey02.data);
    free(outData01.data);
    free(outData02.data);
    /\* 5. Delete the keys from device A and device B. \*/
    CleanKey(&g\_keyAlias01001, &g\_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
    CleanKey(&g\_keyAlias02001, &g\_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
    OH\_Huks\_FreeParamSet(&genParamSet);

    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
