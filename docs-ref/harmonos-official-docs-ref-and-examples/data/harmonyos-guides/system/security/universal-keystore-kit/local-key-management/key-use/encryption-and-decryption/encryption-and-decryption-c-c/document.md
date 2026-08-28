# Encryption and Decryption (C/C++)

The topic uses a 256-bit AES key as an example to describe how to encrypt and decrypt data. For details about the scenarios and supported algorithms, see [Supported Algorithms](../encryption-and-decryption-overview-and-algorithm-specifications/document.md#supported-algorithms).

#### Add the dynamic library in the CMake script.

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

**Key Generation**

1.  Specify the key alias. For details about the naming rules, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    
2.  Initialize the key property set.
    
3.  Use [OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem) to generate a key. For details, see [Key Generation Overview and Algorithm Specifications](../../../key-generation-and-import/key-generation/key-generation-overview-and-algorithm-specifications/document.md).
    

Alternatively, you can [import a key](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md).

**Encryption**

1.  Obtain the key alias.
    
2.  Obtain the data to be encrypted.
    
3.  Use [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset) to set algorithm parameters. If AES is used for encryption, the cipher mode and padding mode must be specified. In the following example, the cipher mode is **CBC** and the padding mode is **PKCS7**. In this case, the IV must be set.
    
4.  Use [OH\_Huks\_InitSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession) to initialize a key session and obtain the session handle.
    
5.  Use [OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession) to finish the key session and obtain the encrypted ciphertext.
    

**Decryption**

1.  Obtain the key alias.
    
2.  Obtain the ciphertext to be decrypted.
    
3.  Use [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset) to set algorithm parameters. If AES is used for decryption, the cipher mode and padding mode must be specified. In the following example, the cipher mode is CBC and the padding mode is PKCS7. In this case, the IV must be set.
    
4.  Use [OH\_Huks\_InitSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession) to initialize a key session and obtain the session handle.
    
5.  Use [OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession) to finish the key session and obtain the decrypted data.
    

**Key Deletion**

Use **OH\_Huks\_DeleteKeyItem** to delete the key that is not required. For details, see [Deleting a Key](../../../key-deletion/deleting-a-key-c-c/document.md).

## AES/CBC/NoPadding

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <string.h>
OH\_Huks\_Result InitParamSet(
    struct OH\_Huks\_ParamSet \*\*paramSet,
    const struct OH\_Huks\_Param \*params,
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
static uint8\_t IV\[IV\_SIZE\] = { 0 }; // this is a test value, for real use the iv should be different every time.
static struct OH\_Huks\_Param g\_genEncDecParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT | OH\_HUKS\_KEY\_PURPOSE\_DECRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CBC
    }
};
static struct OH\_Huks\_Param g\_encryptParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CBC
    }, {
        .tag = OH\_HUKS\_TAG\_IV,
        .blob = {
            .size = IV\_SIZE,
            .data = (uint8\_t \*)IV // this is a test value, for real use the iv should be different every time.
        }
    }
};
static struct OH\_Huks\_Param g\_decryptParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DECRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CBC
    }, {
        .tag = OH\_HUKS\_TAG\_IV,
        .blob = {
            .size = IV\_SIZE,
            .data = (uint8\_t \*)IV // this is a test value, for real use the iv should be different every time.
        }
    }
};
static const uint32\_t AES\_COMMON\_SIZE = 1024;
OH\_Huks\_Result HksAesCipherTestEncrypt(
        const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*encryptParamSet,
        const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*cipherText)
{
    uint8\_t handleE\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleEncrypt = {sizeof(uint64\_t), handleE};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
    return ret;
}
OH\_Huks\_Result HksAesCipherTestDecrypt(const struct OH\_Huks\_Blob \*keyAlias,
    const struct OH\_Huks\_ParamSet \*decryptParamSet, const struct OH\_Huks\_Blob \*cipherText,
    struct OH\_Huks\_Blob \*plainText, const struct OH\_Huks\_Blob \*inData)
{
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDecrypt = {sizeof(uint64\_t), handleD};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
    return ret;
}
static napi\_value EncDecKey(napi\_env env, napi\_callback\_info info)
{
    char tmpKeyAlias\[\] = "test\_enc\_dec";
    struct OH\_Huks\_Blob keyAlias = { (uint32\_t)strlen(tmpKeyAlias), (uint8\_t \*)tmpKeyAlias };
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*encryptParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*decryptParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        /\* 1. Generate Key \*/
        /\*
        \* Simulate the key generation scenario.
        \* 1.1. Set the key alias.
        \*/
        /\*
        \* 1.2. Obtain the parameters for key generation.
        \*/
        ohResult = InitParamSet(&genParamSet, g\_genEncDecParams, sizeof(g\_genEncDecParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*
        \* 1.3. Call generateKeyItem to generate a key.
        \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Encrypt \*/
        /\*
        \* Simulate the encryption scenario.
        \* 2.1. Obtain the key alias.
        \*/
        /\*
        \* 2.2. Obtain the data to be encrypted.
        \*/
        /\*
        \* 2.3. Obtain the algorithm parameters for encryption.
        \*/
        ohResult = InitParamSet(&encryptParamSet, g\_encryptParams, sizeof(g\_encryptParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        char tmpInData\[\] = "AES\_ECB\_INDATA\_1";
        struct OH\_Huks\_Blob inData = { (uint32\_t)strlen(tmpInData), (uint8\_t \*)tmpInData };
        uint8\_t cipher\[AES\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob cipherText = {AES\_COMMON\_SIZE, cipher};
        /\*
        \* 2.4. Call initSession to obtain a session handle.
        \*/
        /\*
        \* 2.5. Call finishSession to obtain the ciphertext.
        \*/
        ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 3. Decrypt \*/
        /\*
        \* Simulate the decryption scenario.
        \* 3.1. Obtain the key alias.
        \*/
        /\*
        \* 3.2. Obtain the ciphertext to be decrypted.
        \*/
        /\*
        \* 3.3 Obtain the algorithm parameters for decryption.
        \*/
        ohResult = InitParamSet(&decryptParamSet, g\_decryptParams, sizeof(g\_decryptParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        uint8\_t plain\[AES\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob plainText = {AES\_COMMON\_SIZE, plain};
        /\*
        \* 3.4. Call initSession to obtain a session handle.
        \*/
        /\*
        \* 3.5. Call finishSession to obtain the decrypted data.
        \*/
        ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
    } while (0);
    /\* 4. Delete Key \*/
    /\*
    \* Simulate the key deletion scenario.
    \* 4.1. Obtain the key alias.
    \*/
    /\*
    \* 4.2. Call deleteKeyItem to delete the key.
    \*/
    (void)OH\_Huks\_DeleteKeyItem(&keyAlias, genParamSet);
        
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&encryptParamSet);
    OH\_Huks\_FreeParamSet(&decryptParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

## AES/CCM/NoPadding

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <string.h>

static const uint32\_t IV\_SIZE = 16;
static const uint32\_t AEAD\_TAG\_LEN = 14;
static char IV\[IV\_SIZE\] = { 0 }; // this is a test value, for real use the iv should be different every time.
static char AEAD\[AEAD\_TAG\_LEN\] = { 0 };
static char NONCE\[OH\_HUKS\_AE\_NONCE\_LEN\] = { 0 };
static struct OH\_Huks\_Param g\_genEncDecParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT | OH\_HUKS\_KEY\_PURPOSE\_DECRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CCM
    }
};
static struct OH\_Huks\_Param g\_encryptParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_ENCRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CCM
    }, {
        .tag = OH\_HUKS\_TAG\_IV,
        .blob = {
            .size = IV\_SIZE,
            .data = (uint8\_t \*)IV // this is a test value, for real use the iv should be different every time.
        }
    }, {
        .tag = OH\_HUKS\_TAG\_NONCE,
        .blob = {
            .size = OH\_HUKS\_AE\_NONCE\_LEN,
            .data = (uint8\_t \*)NONCE
        }
    }, {
        .tag = OH\_HUKS\_TAG\_AE\_TAG\_LEN,
        .uint32Param = AEAD\_TAG\_LEN
    }
};
static struct OH\_Huks\_Param g\_decryptParams\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_AES
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_DECRYPT
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_AES\_KEY\_SIZE\_256
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_NONE
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CCM
    }, {
        .tag = OH\_HUKS\_TAG\_IV,
        .blob = {
            .size = IV\_SIZE,
            .data = (uint8\_t \*)IV // this is a test value, for real use the iv should be different every time.
        }
    }, {
        .tag = OH\_HUKS\_TAG\_NONCE,
        .blob = {
            .size = OH\_HUKS\_AE\_NONCE\_LEN,
            .data = (uint8\_t \*)NONCE
        }
    }, {
        .tag = OH\_HUKS\_TAG\_AE\_TAG,
        .blob = {
            .size = AEAD\_TAG\_LEN,
            .data = (uint8\_t \*)AEAD
        }
    }, {
        .tag = OH\_HUKS\_TAG\_AE\_TAG\_LEN,
        .uint32Param = AEAD\_TAG\_LEN
    }
};
static const uint32\_t AES\_COMMON\_SIZE = 1024;

OH\_Huks\_Result InitParamSet(
    struct OH\_Huks\_ParamSet \*\*paramSet,
    const struct OH\_Huks\_Param \*params,
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

OH\_Huks\_Result HksAesCipherTestEncrypt(
        const struct OH\_Huks\_Blob \*keyAlias, const struct OH\_Huks\_ParamSet \*encryptParamSet,
        const struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*cipherText)
{
    uint8\_t handleE\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleEncrypt = {sizeof(uint64\_t), handleE};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
    return ret;
}

OH\_Huks\_Result HksAesCipherTestDecrypt(const struct OH\_Huks\_Blob \*keyAlias,
    const struct OH\_Huks\_ParamSet \*decryptParamSet, const struct OH\_Huks\_Blob \*cipherText,
    struct OH\_Huks\_Blob \*plainText)
{
    uint8\_t handleD\[sizeof(uint64\_t)\] = {0};
    struct OH\_Huks\_Blob handleDecrypt = {sizeof(uint64\_t), handleD};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
    return ret;
}

static napi\_value EncDecKey(napi\_env env, napi\_callback\_info info)
{
    char tmpKeyAlias\[\] = "test\_aes\_ccm\_enc\_dec";
    struct OH\_Huks\_Blob keyAlias = { (uint32\_t)strlen(tmpKeyAlias), (uint8\_t \*)tmpKeyAlias };
    struct OH\_Huks\_ParamSet \*genParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*encryptParamSet = nullptr;
    struct OH\_Huks\_ParamSet \*decryptParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        /\* 1. Generate Key \*/
        /\*
        \* Simulate the key generation scenario.
        \* 1.1. Set the key alias.
        \*/
        /\*
        \* 1.2. Obtain the parameters for key generation.
        \*/
        ohResult = InitParamSet(&genParamSet, g\_genEncDecParams, sizeof(g\_genEncDecParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\*
        \* 1.3. Call generateKeyItem to generate a key.
        \*/
        ohResult = OH\_Huks\_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        /\* 2. Encrypt \*/
        /\*
        \* Simulate the encryption scenario.
        \* 2.1. Obtain the key alias.
        \*/
        /\*
        \* 2.2. Obtain the data to be encrypted.
        \*/
        /\*
        \* 2.3. Obtain the algorithm parameters for encryption.
        \*/
        ohResult = InitParamSet(&encryptParamSet, g\_encryptParams, sizeof(g\_encryptParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        char tmpInData\[\] = "AES\_CCM\_INDATA\_1";
        uint32\_t dataLen = (uint32\_t)strlen(tmpInData);
        struct OH\_Huks\_Blob inData = { dataLen, (uint8\_t \*)tmpInData };
        uint8\_t cipher\[AES\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob cipherText = {AES\_COMMON\_SIZE, cipher};
        /\*
        \* 2.4. Call initSession to obtain a session handle.
        \*/
        /\*
        \* 2.5. Call finishSession to obtain the ciphertext.
        \*/
        ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        strncpy(AEAD, (char \*)cipherText.data + dataLen, AEAD\_TAG\_LEN);
        cipherText.data\[dataLen\] = '\\0';
        cipherText.size -= AEAD\_TAG\_LEN;
        /\* 3. Decrypt \*/
        /\*
        \* Simulate the decryption scenario.
        \* 3.1. Obtain the key alias.
        \*/
        /\*
        \* 3.2. Obtain the ciphertext to be decrypted.
        \*/
        /\*
        \* 3.3 Obtain the algorithm parameters for decryption.
        \*/
        ohResult = InitParamSet(&decryptParamSet, g\_decryptParams, sizeof(g\_decryptParams) / sizeof(OH\_Huks\_Param));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        uint8\_t plain\[AES\_COMMON\_SIZE\] = {0};
        struct OH\_Huks\_Blob plainText = {AES\_COMMON\_SIZE, plain};
        /\*
        \* 3.4. Call initSession to obtain a session handle.
        \*/
        /\*
        \* 3.5. Call finishSession to obtain the decrypted data.
        \*/
        ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText);
    } while (0);
    /\* 4. Delete Key \*/
    /\*
    \* Simulate the key deletion scenario.
    \* 4.1. Obtain the key alias.
    \*/
    /\*
    \* 4.2. Call deleteKeyItem to delete the key.
    \*/
    (void)OH\_Huks\_DeleteKeyItem(&keyAlias, genParamSet);
        
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&encryptParamSet);
    OH\_Huks\_FreeParamSet(&decryptParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
