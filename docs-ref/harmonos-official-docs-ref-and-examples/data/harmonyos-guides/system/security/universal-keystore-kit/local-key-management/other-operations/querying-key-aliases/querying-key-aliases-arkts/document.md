# Querying Key Aliases (ArkTS)

This topic walks you through on how to query key aliases.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/wk6_hm2QQJ6TvASeRpHyuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B1199F86FF68936D97EF74FCCBE5EC24D3B92C5BFFE7A9CE84F2BFB3A364762)

Lite wearables do not support query of key aliases.

#### How to Develop

1.  Initialize the key property set to query the tags of key aliases. The tags support only [HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-huks-type-h#oh_huks_authstoragelevel).
    
2.  Use [listAliases](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#hukslistaliases12) to query the key aliases.
    

/\*
 \* The following example uses promise-based APIs to query key aliases.
 \*/
import { huks } from '@kit.UniversalKeystoreKit'

async function testListAliases() {
  /\* 1. Initialize the key property set. \*/
  let queryProperties: Array<huks.HuksParam> = \[
    {
      tag: huks.HuksTag.HUKS\_TAG\_AUTH\_STORAGE\_LEVEL,
      value: huks.HuksAuthStorageLevel.HUKS\_AUTH\_STORAGE\_LEVEL\_DE
    }
  \];
  let queryOptions: huks.HuksOptions = {
    properties: queryProperties
  };

  try {
    /\* 2. Query key aliases. \*/
    let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
    console.info(\`promise: listAliases success\`);
  } catch (error) {
    console.error(\`promise: listAliases fail\`);
    throw (error as Error);
  }
}
