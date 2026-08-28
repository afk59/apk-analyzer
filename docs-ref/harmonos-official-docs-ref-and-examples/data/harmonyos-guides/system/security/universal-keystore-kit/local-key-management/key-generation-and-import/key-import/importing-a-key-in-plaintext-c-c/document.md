# Importing a Key in Plaintext (C/C++)

This topic walks you through on how to import an ECC key. For details about the scenarios and supported algorithm specifications, see [Supported Algorithms](../key-import-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Encapsulate the key property set and key material. Construct **paramSet** using [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset), [OH\_Huks\_AddParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_addparams), and [OH\_Huks\_BuildParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_buildparamset).
    
    -   The key property set must contain the [OH\_Huks\_KeyAlg](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keyalg), [OH\_Huks\_KeySize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keysize), and [OH\_Huks\_KeyPurpose](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_keypurpose) properties.
    -   The key material must comply with the [HUKS key material format](../../../basic-concepts-of-local-key-management/document.md#key-material-format).
3.  Call [OH\_Huks\_ImportKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_importkeyitem) and pass in the key alias and key property set to import the key.
    

## Importing an AES256 Key

/\* Import an AES key in plaintext. \*/
#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

#define OH\_HUKS\_AES\_KEY\_SIZE\_32 32

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
static struct OH\_Huks\_Param g\_testImportKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_AES},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

napi\_value ImportAesKey(napi\_env env, napi\_callback\_info info)
{
    /\* Public key, which is used to import the key. \*/
    uint8\_t pubKey\[OH\_HUKS\_AES\_KEY\_SIZE\_32\] = {0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63,
                                               0x2a, 0x7c, 0x86, 0xba, 0xca, 0x64, 0x0b, 0x88, 0x96, 0xe2, 0xfa,
                                               0x77, 0xbc, 0x71, 0xe3, 0x0f, 0x0f, 0x9e, 0x3c, 0xe5, 0xf9};
    struct OH\_Huks\_Blob publicKey = {OH\_HUKS\_AES\_KEY\_SIZE\_32, pubKey};
    struct OH\_Huks\_ParamSet \*testImportKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&testImportKeyParamSet, g\_testImportKeyParam,
                                sizeof(g\_testImportKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* Import the key. \*/
        char newKey\[\] = "test\_aes\_import";
        struct OH\_Huks\_Blob newKeyAlias = {.size = (uint32\_t)strlen(newKey), .data = (uint8\_t \*)newKey};
        ohResult = OH\_Huks\_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
    } while (0);
    
    OH\_Huks\_FreeParamSet(&testImportKeyParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## Importing an RSA2048 Key Pair

/\* Import an RSA2048 key in plaintext. \*/
#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

#define RSA\_KEY\_SIZE\_1024 1024

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
static struct OH\_Huks\_Param g\_testImportKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_RSA},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_RSA\_KEY\_SIZE\_2048},
    {.tag = OH\_HUKS\_TAG\_IMPORT\_KEY\_TYPE, .uint32Param = OH\_HUKS\_KEY\_TYPE\_KEY\_PAIR},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

napi\_value ImportRsaKey(napi\_env env, napi\_callback\_info info)
{
    /\* Key material, which is used to import the key. \*/
    uint8\_t pubKey\[RSA\_KEY\_SIZE\_1024\] = {0x01, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x03,
        0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xc5, 0x35, 0x62, 0x48, 0xc4, 0x92, 0x87, 0x73, 0x0d, 0x42, 0x96,
        0xfc, 0x7b, 0x11, 0x05, 0x06, 0x0f, 0x8d, 0x66, 0xc1, 0x0e, 0xad, 0x37, 0x44, 0x92, 0x95, 0x2f, 0x6a, 0x55,
        0xba, 0xec, 0x1d, 0x54, 0x62, 0x0a, 0x4b, 0xd3, 0xc7, 0x05, 0xe4, 0x07, 0x40, 0xd9, 0xb7, 0xc2, 0x12, 0xcb,
        0x9a, 0x90, 0xad, 0xe3, 0x24, 0xe8, 0x5e, 0xa6, 0xf8, 0xd0, 0x6e, 0xbc, 0xd1, 0x69, 0x7f, 0x6b, 0xe4, 0x2b,
        0x4e, 0x1a, 0x65, 0xbb, 0x73, 0x88, 0x6b, 0x7c, 0xaf, 0x7e, 0xd0, 0x47, 0x26, 0xeb, 0xa5, 0xbe, 0xd6, 0xe8,
        0xee, 0x9c, 0xa5, 0x66, 0xa5, 0xc9, 0xd3, 0x25, 0x13, 0xc4, 0x0e, 0x6c, 0xab, 0x50, 0xb6, 0x50, 0xc9, 0xce,
        0x8f, 0x0a, 0x0b, 0xc6, 0x28, 0x69, 0xe9, 0x83, 0x69, 0xde, 0x42, 0x56, 0x79, 0x7f, 0xde, 0x86, 0x24, 0xca,
        0xfc, 0xaa, 0xc0, 0xf3, 0xf3, 0x7f, 0x92, 0x8e, 0x8a, 0x12, 0x52, 0xfe, 0x50, 0xb1, 0x5e, 0x8c, 0x01, 0xce,
        0xfc, 0x7e, 0xf2, 0x4f, 0x5f, 0x03, 0xfe, 0xa7, 0xcd, 0xa1, 0xfc, 0x94, 0x52, 0x00, 0x8b, 0x9b, 0x7f, 0x09,
        0xab, 0xa8, 0xa4, 0xf5, 0xb4, 0xa5, 0xaa, 0xfc, 0x72, 0xeb, 0x17, 0x40, 0xa9, 0xee, 0xbe, 0x8f, 0xc2, 0xd1,
        0x80, 0xc2, 0x0d, 0x44, 0xa9, 0x59, 0x44, 0x59, 0x81, 0x3b, 0x5d, 0x4a, 0xde, 0xfb, 0xae, 0x24, 0xfc, 0xa3,
        0xd9, 0xbc, 0x57, 0x55, 0xc2, 0x26, 0xbc, 0x19, 0xa7, 0x9a, 0xc5, 0x59, 0xa3, 0xee, 0x5a, 0xef, 0x41, 0x80,
        0x7d, 0xf8, 0x5e, 0xc1, 0x1d, 0x32, 0x38, 0x41, 0x5b, 0xb6, 0x92, 0xb8, 0xb7, 0x03, 0x0d, 0x3e, 0x59, 0x0f,
        0x1c, 0xb3, 0xe1, 0x2a, 0x95, 0x1a, 0x3b, 0x50, 0x4f, 0xc4, 0x1d, 0xcf, 0x73, 0x7c, 0x14, 0xca, 0xe3, 0x0b,
        0xa7, 0xc7, 0x1a, 0x41, 0x4a, 0xee, 0xbe, 0x1f, 0x43, 0xdd, 0xf9, 0x01, 0x00, 0x01, 0x88, 0x4b, 0x82, 0xe7,
        0xe3, 0xe3, 0x99, 0x75, 0x6c, 0x9e, 0xaf, 0x17, 0x44, 0x3e, 0xd9, 0x07, 0xfd, 0x4b, 0xae, 0xce, 0x92, 0xc4,
        0x28, 0x44, 0x5e, 0x42, 0x79, 0x08, 0xb6, 0xc3, 0x7f, 0x58, 0x2d, 0xef, 0xac, 0x4a, 0x07, 0xcd, 0xaf, 0x46,
        0x8f, 0xb4, 0xc4, 0x43, 0xf9, 0xff, 0x5f, 0x74, 0x2d, 0xb5, 0xe0, 0x1c, 0xab, 0xf4, 0x6e, 0xd5, 0xdb, 0xc8,
        0x0c, 0xfb, 0x76, 0x3c, 0x38, 0x66, 0xf3, 0x7f, 0x01, 0x43, 0x7a, 0x30, 0x39, 0x02, 0x80, 0xa4, 0x11, 0xb3,
        0x04, 0xd9, 0xe3, 0x57, 0x23, 0xf4, 0x07, 0xfc, 0x91, 0x8a, 0xc6, 0xcc, 0xa2, 0x16, 0x29, 0xb3, 0xe5, 0x76,
        0x4a, 0xa8, 0x84, 0x19, 0xdc, 0xef, 0xfc, 0xb0, 0x63, 0x33, 0x0b, 0xfa, 0xf6, 0x68, 0x0b, 0x08, 0xea, 0x31,
        0x52, 0xee, 0x99, 0xef, 0x43, 0x2a, 0xbe, 0x97, 0xad, 0xb3, 0xb9, 0x66, 0x7a, 0xae, 0xe1, 0x8f, 0x57, 0x86,
        0xe5, 0xfe, 0x14, 0x3c, 0x81, 0xd0, 0x64, 0xf8, 0x86, 0x1a, 0x0b, 0x40, 0x58, 0xc9, 0x33, 0x49, 0xb8, 0x99,
        0xc6, 0x2e, 0x94, 0x70, 0xee, 0x09, 0x88, 0xe1, 0x5c, 0x4e, 0x6c, 0x22, 0x72, 0xa7, 0x2a, 0x21, 0xdd, 0xd7,
        0x1d, 0xfc, 0x63, 0x15, 0x0b, 0xde, 0x06, 0x9c, 0xf3, 0x28, 0xf3, 0xac, 0x4a, 0xa8, 0xb5, 0x50, 0xca, 0x9b,
        0xcc, 0x0a, 0x04, 0xfe, 0x3f, 0x98, 0x68, 0x81, 0xac, 0x24, 0x53, 0xea, 0x1f, 0x1c, 0x6e, 0x5e, 0xca, 0xe8,
        0x31, 0x0d, 0x08, 0x12, 0xf3, 0x26, 0xf8, 0x5e, 0xeb, 0x10, 0x27, 0xae, 0xaa, 0xc3, 0xad, 0x6c, 0xc1, 0x89,
        0xdb, 0x7d, 0x5a, 0x12, 0x55, 0xad, 0x11, 0x19, 0xa1, 0xa9, 0x8f, 0x0b, 0x6d, 0x78, 0x8d, 0x1c, 0xdf, 0xe5,
        0x63, 0x82, 0x0b, 0x7d, 0x23, 0x04, 0xb4, 0x75, 0x8c, 0xed, 0x77, 0xfc, 0x1a, 0x85, 0x29, 0x11, 0xe0, 0x61};
    struct OH\_Huks\_Blob publicKey = {RSA\_KEY\_SIZE\_1024, pubKey};
    struct OH\_Huks\_ParamSet \*testImportKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&testImportKeyParamSet, g\_testImportKeyParam,
                                sizeof(g\_testImportKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* Import the key. \*/
        char newKey\[\] = "test\_rsa\_import";
        struct OH\_Huks\_Blob newKeyAlias = {.size = (uint32\_t)strlen(newKey), .data = (uint8\_t \*)newKey};
        ohResult = OH\_Huks\_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
    } while (0);
    
    OH\_Huks\_FreeParamSet(&testImportKeyParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## Importing the Public Key of an X25519 Key Pair

/\* Import an X25519 key in plaintext. \*/
#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <cstring>
#include "file.h"

#define X25519\_KEY\_SIZE\_32 32

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
static struct OH\_Huks\_Param g\_testImportKeyParam\[\] = {{.tag = OH\_HUKS\_TAG\_ALGORITHM, .uint32Param = OH\_HUKS\_ALG\_X25519},
    {.tag = OH\_HUKS\_TAG\_PURPOSE, .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_VERIFY},
    {.tag = OH\_HUKS\_TAG\_KEY\_SIZE, .uint32Param = OH\_HUKS\_CURVE25519\_KEY\_SIZE\_256},
    {.tag = OH\_HUKS\_TAG\_IMPORT\_KEY\_TYPE, .uint32Param = OH\_HUKS\_KEY\_TYPE\_PUBLIC\_KEY},
    {.tag = OH\_HUKS\_TAG\_DIGEST, .uint32Param = OH\_HUKS\_DIGEST\_NONE}};

napi\_value ImportX25519Key(napi\_env env, napi\_callback\_info info)
{
    /\* Public key, which is used to import the key. \*/
    uint8\_t pubKey\[X25519\_KEY\_SIZE\_32\] = {0x30, 0x2A, 0x30, 0x05, 0x06, 0x03, 0x2B, 0x65, 0x6E, 0x03, 0x21, 0x00,
        0xD2, 0x36, 0x9E, 0xCF, 0xF0, 0x61, 0x5B, 0x73, 0xCE, 0x4F, 0xF0, 0x40,
        0x2B, 0x89, 0x18, 0x3E, 0x06, 0x33, 0x60, 0xC6};
    struct OH\_Huks\_Blob publicKey = {X25519\_KEY\_SIZE\_32, pubKey};
    struct OH\_Huks\_ParamSet \*testImportKeyParamSet = nullptr;
    struct OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&testImportKeyParamSet, g\_testImportKeyParam,
                                sizeof(g\_testImportKeyParam) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* Import the key. \*/
        char newKey\[\] = "test\_X25519\_import";
        struct OH\_Huks\_Blob newKeyAlias = {.size = (uint32\_t)strlen(newKey), .data = (uint8\_t \*)newKey};
        ohResult = OH\_Huks\_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
    } while (0);
    
    OH\_Huks\_FreeParamSet(&testImportKeyParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
