# Opening and Closing Resources (C/C++)

#### Opening Resources

From API version 22, **huksExternalCrypto** provides the APIs for opening and closing resources. Before performing key operations (such as key operations, common operations, and PIN authentication), applications need to call [OH\_Huks\_OpenResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_openresource) to open resources. To open resources, you need to obtain **resourceId** by calling the [certificate selection API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22) provided by the certificate management system.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so libhuks\_external\_crypto.z.so)

## How to Develop

1.  Obtain [keyUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certreference22) as **resourceId** by calling the [certificate selection API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22) provided by the certificate management system.
    
2.  Initialize the parameter set: Construct the parameter set **paramSet** by using [OH\_Huks\_InitExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_initexternalcryptoparamset), [OH\_Huks\_AddExternalCryptoParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_addexternalcryptoparams), and [OH\_Huks\_BuildExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_buildexternalcryptoparamset).
    
3.  Call [OH\_Huks\_OpenResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_openresource) to open the resource.
    

## Development Cases

#include "huks/native\_huks\_external\_crypto\_api.h"
#include "huks/native\_huks\_param.h"
#include "napi/native\_api.h"
#include <string.h>

OH\_Huks\_Result InitParamSet(
    struct OH\_Huks\_ExternalCryptoParamSet \*\*paramSet,
    const struct OH\_Huks\_ExternalCryptoParam \*params,
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

static const char \*g\_resourceId = "{\\"providerName\\":\\"testProviderName\\",\\"abilityName\\":\\"CryptoExtension\\",\\"bundleName\\":\\"com.example.cryptoapplication\\",\\"index\\":{\\"key\\":\\"testKey\\"}}";

static struct OH\_Huks\_ExternalCryptoParam g\_openResourceParamsTest\[\] = {};

static napi\_value OpenResource(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob resourceId = {
        (uint32\_t)strlen(g\_resourceId),
        (uint8\_t \*)g\_resourceId
    };
    struct OH\_Huks\_ExternalCryptoParamSet \*openResourceParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&openResourceParamSet, g\_openResourceParamsTest,
            sizeof(g\_openResourceParamsTest) / sizeof(OH\_Huks\_ExternalCryptoParam));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = OH\_Huks\_OpenResource(&resourceId, openResourceParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    OH\_Huks\_FreeExternalCryptoParamSet(&openResourceParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}

#### Closing Resources

An ecosystem application calls the certificate HAP UI to display a certificate list. When a user selects a certificate, and the ecosystem application obtains **resourceId** that can be used to closing the corresponding resource. For details about the scenarios and specifications, see [Resource Management Overview and Specifications](../resource-management-overview-and-specifications/document.md).

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so libhuks\_external\_crypto.z.so)

## How to Develop

1.  Obtain **resourceId** by calling the [certificate selection API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22) provided by the certificate management system.
    
2.  Initialize the parameter set: Construct the parameter set **paramSet** by using [OH\_Huks\_InitExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_initexternalcryptoparamset), [OH\_Huks\_AddExternalCryptoParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_addexternalcryptoparams), and [OH\_Huks\_BuildExternalCryptoParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_buildexternalcryptoparamset).
    
3.  Call [OH\_Huks\_CloseResource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-external-crypto-api-h#oh_huks_closeresource) to close the resource. This API calls [onClearUkeyPinAuthState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoextensionability#cryptoextensionabilityonclearukeypinauthstate) to clear the PIN authentication status associated with the resource, and calls [onFinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cryptoextensionability#cryptoextensionabilityonfinishsession) to clear the session handle associated with the resource.
    

## Development Cases

#include "huks/native\_huks\_external\_crypto\_api.h"
#include "huks/native\_huks\_param.h"
#include "huks/native\_huks\_type.h"
#include "huks/native\_huks\_api.h"
#include "napi/native\_api.h"
#include <string.h>

OH\_Huks\_Result InitParamSet(
    struct OH\_Huks\_ExternalCryptoParamSet \*\*paramSet,
    const struct OH\_Huks\_ExternalCryptoParam \*params,
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

static const char \*g\_resourceId = "{\\"providerName\\":\\"testProviderName\\",\\"abilityName\\":\\"CryptoExtension\\",\\"bundleName\\":\\"com.example.cryptoapplication\\",\\"userid\\":100,\\"index\\":{\\"key\\":\\"testKey\\"}}";

static struct OH\_Huks\_ExternalCryptoParam g\_closeResourceParamsTest\[\] = {};

static napi\_value CloseResource(napi\_env env, napi\_callback\_info info)
{
    struct OH\_Huks\_Blob resourceId = {
        (uint32\_t)strlen(g\_resourceId),
        (uint8\_t \*)g\_resourceId
    };
    struct OH\_Huks\_ExternalCryptoParamSet \*closeResourceParamSet = nullptr;
    OH\_Huks\_Result ohResult;
    do {
        ohResult = InitParamSet(&closeResourceParamSet, g\_closeResourceParamsTest,
            sizeof(g\_closeResourceParamsTest) / sizeof(OH\_Huks\_ExternalCryptoParam));
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
        ohResult = OH\_Huks\_CloseResource(&resourceId, closeResourceParamSet);
        if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            break;
        }
    } while (0);
    OH\_Huks\_FreeExternalCryptoParamSet(&closeResourceParamSet);
    
    napi\_value ret;
    napi\_create\_int32(env, ohResult.errorCode, &ret);
    return ret;
}
