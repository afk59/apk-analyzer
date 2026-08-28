# General Query (C/C++)

From API version 22, **huksExternalCrypto** provides the general query API. This API can be used to obtain general property information from a UKey device. For details about the scenarios, see [General Query Overview and Specifications](../general-query-overview-and-specifications/document.md).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so libhuks\_external\_crypto.z.so)

#### How to Develop

**Obtaining properties**

1.  Construct **resourceId** and **propertyId**, and call [OH\_Huks\_OpenResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_openresource) to open the resource.
    
2.  Initialize the parameter set: Construct the parameter set **paramSet** by using [OH\_Huks\_InitExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_initexternalcryptoparamset), [OH\_Huks\_AddExternalCryptoParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_addexternalcryptoparams), and [OH\_Huks\_BuildExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_buildexternalcryptoparamset).
    
3.  Call [OH\_Huks\_GetProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_getproperty) to obtain the property information.
    
4.  Call [OH\_Huks\_GetExternalCryptoParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_getexternalcryptoparam) to extract the result from the output parameter set.
    
5.  Call [OH\_Huks\_FreeExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_freeexternalcryptoparamset) to release the parameter set resource.
    

#### Development Cases

#include "huks/native\_huks\_external\_crypto\_api.h"
#include "huks/native\_huks\_external\_crypto\_type.h"
#include "napi/native\_api.h"
#include <string.h>

OH\_Huks\_Result InitExternalCryptoParamSet(
    OH\_Huks\_ExternalCryptoParamSet \*\*paramSet,
    const OH\_Huks\_ExternalCryptoParam \*params,
    uint32\_t paramCount)
{
    OH\_Huks\_Result ret = OH\_Huks\_InitExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        return ret;
    }
    ret = OH\_Huks\_AddExternalCryptoParams(\*paramSet, params, paramCount);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    ret = OH\_Huks\_BuildExternalCryptoParamSet(paramSet);
    if (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeExternalCryptoParamSet(paramSet);
        return ret;
    }
    return ret;
}

static napi\_value GetProperty(napi\_env env, napi\_callback\_info info)
{
    /\* 1. Assume that the resource specified by resourceId has been opened. \*/
    const char \*resourceIdStr = "{\\"providerName\\":\\"testProviderName\\",\\"abilityName\\":\\"CryptoExtension\\","
                              "\\"bundleName\\":\\"com.example.cryptoapplication\\",\\"index\\":{\\"key\\":\\"testKey\\"}}";
    const char \*propertyIdStr = "SKF\_GetDevInfo"; // Name of the property function defined in the GMT 0016-2023 standard
    
    struct OH\_Huks\_Blob resourceId = {
        (uint32\_t)strlen(resourceIdStr),
        (uint8\_t \*)resourceIdStr
    };
    struct OH\_Huks\_Blob propertyId = {
        (uint32\_t)strlen(propertyIdStr),
        (uint8\_t \*)propertyIdStr
    };
    
    /\* 2. Construct input parameters. \*/
    OH\_Huks\_ExternalCryptoParam params\[\] = {};
    OH\_Huks\_ExternalCryptoParamSet \*paramSetIn = nullptr;
    OH\_Huks\_ExternalCryptoParamSet \*paramSetOut = nullptr;
    OH\_Huks\_Result ohResult;
    
    do {
        /\* 3. Initialize and build the input parameter set. \*/
        ohResult = InitExternalCryptoParamSet(&paramSetIn, params,
            sizeof(params) / sizeof(OH\_Huks\_ExternalCryptoParam));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        /\* 4. Call OH\_Huks\_GetProperty to obtain the properties. \*/
        ohResult = OH\_Huks\_GetProperty(&resourceId, &propertyId, paramSetIn, &paramSetOut);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        
        /\* 5. Extract the result from the output parameter set.
         \* The output parameter set is allocated internally by the function, and the found property data is stored in OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA TAG.
         \* The following shows how to iterate over the returned params and safely extract the returned property string (example).
         \*/
        if (paramSetOut != nullptr && paramSetOut->paramsCnt > 0) {
            for (uint32\_t i = 0; i < paramSetOut->paramsCnt; i++) {
                OH\_Huks\_ExternalCryptoParam \*param = &paramSetOut->params\[i\];
                /\* Return data convention: The GetProperty result is stored in OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA TAG (the JSON text is used as an example). \*/
                if (param->tag == OH\_HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA) {
                    /\* Note: param->blob.data may not end with '\\0'. You need to copy the data and manually add the terminator. \*/
                    char \*outStr = (char \*)malloc(param->blob.size + 1);
                    if (outStr != NULL) {
                        memcpy(outStr, param->blob.data, param->blob.size);
                        outStr\[param->blob.size\] = '\\0';
                        // Parse outStr (for example, using the JSON parsing library). The following is an example:
                        // parse\_json(outStr);
                        free(outStr);
                    }
                }
            }
        }
    } while (0);
    
    /\* 6. Release the resources. \*/
    OH\_Huks\_FreeExternalCryptoParamSet(&paramSetIn);
    OH\_Huks\_FreeExternalCryptoParamSet(&paramSetOut);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
