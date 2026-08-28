# Querying Key Aliases (C/C++)

This topic walks you through on how to query key aliases.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/mBJmnFu_SRW7ZK4E8CMgEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A99D3C6EC1AD173AC06D275C78C8638F86AC0C94FA61575376801E43AB1DA31)

Lite wearables do not support query of key aliases.

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libhuks\_ndk.z.so)

#### How to Develop

1.  Initialize the key property set to query the tags of key aliases. The tags support only [OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_authstoragelevel).
    
2.  Call [OH\_Huks\_ListAliases](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-api-h#oh_huks_listaliases) to query key aliases.
    

/\* Query key aliases. \*/
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

struct OH\_Huks\_Param g\_testQueryParam\[\] = {
   {
       .tag = OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL,
       .uint32Param = OH\_HUKS\_AUTH\_STORAGE\_LEVEL\_DE
   },
};

static napi\_value ListAliases(napi\_env env, napi\_callback\_info info)
{
   struct OH\_Huks\_ParamSet \*testQueryParamSet = nullptr;
   struct OH\_Huks\_KeyAliasSet \*outData = nullptr;
   struct OH\_Huks\_Result ohResult;
   do {
       /\* 1. Initialize the key property set. \*/
       ohResult = InitParamSet(&testQueryParamSet, g\_testQueryParam,
           sizeof(g\_testQueryParam) / sizeof(OH\_Huks\_Param));
       if (ohResult.errorCode != OH\_HUKS\_SUCCESS) {
           break;
       }
       /\* 2. Query key aliases. \*/
       ohResult = OH\_Huks\_ListAliases(testQueryParamSet, &outData);
   } while (0);

   OH\_Huks\_FreeParamSet(&testQueryParamSet);
   OH\_Huks\_FreeKeyAliasSet(outData);
   napi\_value ret;
   napi\_create\_int32(env, ohResult.errorCode, &ret);
   return ret;
}
