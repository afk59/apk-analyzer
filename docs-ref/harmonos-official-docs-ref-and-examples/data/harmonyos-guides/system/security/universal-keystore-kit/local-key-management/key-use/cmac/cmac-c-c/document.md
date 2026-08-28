# CMAC (C/C++)

Cipher-based Message Authentication Code (CMAC) is a type of message authentication code (MAC) based on block ciphers. Currently, it supports 3DES.

#### How to Develop

**Key Generation**

1.  Obtain the parameters for key generation.
2.  Call [OH\_Huks\_GenerateKeyItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_generatekeyitem) to generate a 128-bit key.

Alternatively, you can import a key. For details about the specifications, see [Supported Algorithms](../../../key-generation-and-import/key-import/key-import-overview-and-algorithm-specifications/document.md#supported-algorithms).

**CMAC Generation**

1.  Call [OH\_Huks\_InitParamSet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-param-h#oh_huks_initparamset) to obtain the algorithm parameter configuration.
2.  Call [OH\_Huks\_InitSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_initsession) and [OH\_Huks\_FinishSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_finishsession) to calculate the MAC value.

#include "huks/native\_huks\_api.h"
#include "huks/native\_huks\_param.h"
#include "huks/native\_huks\_type.h"
#include "napi/native\_api.h"
#include <string.h>

**static** **const** **uint32\_t** CMAC\_COMMON\_SIZE = 8;
**static** **const** **uint32\_t** IV\_SIZE = 8; 
**static** **uint8\_t** IV\[IV\_SIZE\] = { 0 };

OH\_Huks\_Result **InitParamSet**(struct OH\_Huks\_ParamSet \*\*paramSet, **const** struct OH\_Huks\_Param \*params, **uint32\_t** paramCount)
{
    OH\_Huks\_Result ret = OH\_Huks\_InitParamSet(paramSet);
    **if** (ret.errorCode != OH\_HUKS\_SUCCESS) {
        **return** ret;
    }
    ret = OH\_Huks\_AddParams(\*paramSet, params, paramCount);
    **if** (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        **return** ret;
    }
    ret = OH\_Huks\_BuildParamSet(paramSet);
    **if** (ret.errorCode != OH\_HUKS\_SUCCESS) {
        OH\_Huks\_FreeParamSet(paramSet);
        **return** ret;
    }
    **return** ret;
}

**static** **struct** **OH\_Huks\_Param** **g\_genParams**\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_3DES
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_3DES\_KEY\_SIZE\_128
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_MAC
    }
};

**static** **struct** **OH\_Huks\_Param** **g\_cmacParams**\[\] = {
    {
        .tag = OH\_HUKS\_TAG\_ALGORITHM,
        .uint32Param = OH\_HUKS\_ALG\_CMAC
    }, {
        .tag = OH\_HUKS\_TAG\_KEY\_SIZE,
        .uint32Param = OH\_HUKS\_3DES\_KEY\_SIZE\_128
    }, {
        .tag = OH\_HUKS\_TAG\_PURPOSE,
        .uint32Param = OH\_HUKS\_KEY\_PURPOSE\_MAC
    }, {
        .tag = OH\_HUKS\_TAG\_BLOCK\_MODE,
        .uint32Param = OH\_HUKS\_MODE\_CBC
    }, {
        .tag = OH\_HUKS\_TAG\_PADDING,
        .uint32Param = OH\_HUKS\_PADDING\_ISO\_IEC\_9797\_1
    }, {
        .tag = OH\_HUKS\_TAG\_IV,
        .blob = {
            .size = IV\_SIZE,
            .data = (**uint8\_t** \*)IV
        }
    }
};

OH\_Huks\_Result **HksCmacTest**(**const** struct OH\_Huks\_Blob \*keyAlias, **const** struct OH\_Huks\_ParamSet \*cmacParamSet,
    **const** struct OH\_Huks\_Blob \*inData, struct OH\_Huks\_Blob \*outData)
{
    **uint8\_t** handleE\[**sizeof**(**uint64\_t**)\] = {0};
    **struct** **OH\_Huks\_Blob** **handle** = {**sizeof**(**uint64\_t**), handleE};
    OH\_Huks\_Result ret = OH\_Huks\_InitSession(keyAlias, cmacParamSet, &handle, nullptr);
    **if** (ret.errorCode != OH\_HUKS\_SUCCESS) {
        **return** ret;
    }
    ret = OH\_Huks\_FinishSession(&handle, cmacParamSet, inData, outData);
    **return** ret;
}

**static** int32\_t **CmacKey**()
{
    **char** tmpKeyAlias\[\] = "test\_cmac";
    **struct** **OH\_Huks\_Blob** **keyAlias** = { (**uint32\_t**)strlen(tmpKeyAlias), (**uint8\_t** \*)tmpKeyAlias };
    **struct** **OH\_Huks\_ParamSet** \***genParamSet** = **nullptr**;
    **struct** **OH\_Huks\_ParamSet** \***cmacParamSet** = **nullptr**;
    OH\_Huks\_Result ohResult;
    **do** {
      _/\*_
       \* 1.1 Obtain the parameters for key generation.
       _\*/_
        ohResult = InitParamSet(&genParamSet, g\_genParams, **sizeof**(g\_genParams) / **sizeof**(OH\_Huks\_Param));
        **if** (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            **break**;
        }
       _/\*_       
       \* 1.2 Call OH\_Huks\_GenerateKeyItem.
        _\*/_
        ohResult = OH\_Huks\_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
        **if** (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            **break**;
        }
       _/\*_
        \* 2.1. Obtain CMAC algorithm parameter settings.
        _\*/_
        **char** tmpInData\[\] = "CMAC\_INDATA";
        **struct** **OH\_Huks\_Blob** **inData** = { (**uint32\_t**)strlen(tmpInData), (**uint8\_t** \*)tmpInData };
        **uint8\_t** mac\[CMAC\_COMMON\_SIZE\] = { 0 };
        **struct** **OH\_Huks\_Blob** macData= {CMAC\_COMMON\_SIZE, mac};
        ohResult = InitParamSet(&cmacParamSet, g\_cmacParams, **sizeof**(g\_cmacParams) / **sizeof**(OH\_Huks\_Param));
        **if** (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            **break**;
        }
       _/\*_
        \* 2.2 Call initSession and finishSession to calculate the MAC.
        _\*/_
        ohResult = HksCmacTest(&keyAlias, cmacParamSet, &inData, &macData);
        **if** (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
            **break**;
        }
    } **while** (0);
    OH\_Huks\_FreeParamSet(&genParamSet);
    OH\_Huks\_FreeParamSet(&cmacParamSet);
    return ohResult.errCode;
}
