# Managing Assets in a Group (C/C++)

Before managing assets in a group, ensure that you are familiar with the following operations:

-   [Adding an Asset (C/C++)](../adding-an-asset-c-c/document.md)
-   [Removing Assets (C/C++)](../removing-assets-c-c/document.md)
-   [Updating an Asset (C/C++)](../update-an-asset-c-c/document.md)
-   [Querying Assets (C/C++)](../querying-assets-c-c/document.md)

#### Prerequisites

Set the group ID, such as **demo\_group\_id**, in the **app.json5** file. You can set multiple group IDs for a group.

{
  "app": {
    // Other configuration items are omitted here.
    "assetAccessGroups": \[
      "demo\_group\_id",
      // "another\_group\_id",
      // ...
    \]
  }
}

Include header files.

#include "napi/native\_api.h"
#include <string.h>
#include "asset/asset\_api.h"

#### Adding an Asset to a Group

Add an asset to the group, with the password **demo\_pwd**, alias **demo\_alias**, and additional attribute **demo\_label**.

static napi\_value AddGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*secretStr = "demo\_pwd";
    const char \*aliasStr = "demo\_alias";
    const char \*labelStr = "demo\_label";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Blob group\_id = { (uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = secret},
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    int32\_t addResult = OH\_Asset\_Add(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, addResult, &ret);
    return ret;
}

#### Removing an Asset from a Group

Remove asset **demo\_alias** from group **demo\_group\_id**.

static napi\_value RemoveGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // Specify the asset alias to remove a single asset. To remove all assets, leave the alias unspecified.
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    int32\_t removeResult = OH\_Asset\_Remove(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, removeResult, &ret);
    return ret;
}

#### Updating an Asset in a Group

Update asset **demo\_alias** in group **demo\_group\_id** as follows: change the asset plaintext to **demo\_pwd\_new** and the additional attribute to **demo\_label\_new**.

static napi\_value UpdateGroupAsset(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*secretStr = "demo\_pwd\_new";
    const char \*labelStr = "demo\_label\_new";
    const char \*groupIdStr = "demo\_group\_id";

    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob new\_secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob new\_label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr query\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };
    Asset\_Attr attributesToUpdate\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = new\_secret},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = new\_label},
    };

    int32\_t updateResult = OH\_Asset\_Update(query, sizeof(query) / sizeof(query\[0\]), attributesToUpdate,
                                           sizeof(attributesToUpdate) / sizeof(attributesToUpdate\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, updateResult, &ret);
    return ret;
}

#### Querying the Plaintext of an Asset in a Group

Query the plaintext of asset **demo\_alias** in group **demo\_group\_id**.

static napi\_value QueryGroupAssetPlaintext(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";
    
    Asset\_Blob alias = { (uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr };
    Asset\_Blob group\_id = { (uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr };
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // Specify the alias of the asset to query.
        {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ALL}, // Return all asset information, including the attributes and asset plaintext, in the group.
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    Asset\_ResultSet resultSet = {0};
    int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
    if (queryResult == ASSET\_SUCCESS) {
        // Parse resultSet.
        for (uint32\_t i = 0; i < resultSet.count; i++) {
            // Parse the secret attribute. The data corresponds to secret->blob.data, and the size corresponds to secret->blob.size.
            Asset\_Attr \*secret = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_SECRET);
        }
    }
    OH\_Asset\_FreeResultSet(&resultSet);
    
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}

#### Querying the Attributes of an Asset in a Group

Query attributes of asset **demo\_alias**.

static napi\_value QueryGroupAssetAttribute(napi\_env env, napi\_callback\_info info)
{
    const char \*aliasStr = "demo\_alias";
    const char \*groupIdStr = "demo\_group\_id";
    
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob group\_id = {(uint32\_t)(strlen(groupIdStr)), (uint8\_t \*)groupIdStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // Specify the alias of the asset to query.
        {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES}, // Return only the asset attributes of the asset in the group, that is, the result does not include the asset plaintext.
        {.tag = ASSET\_TAG\_GROUP\_ID, .value.blob = group\_id},
    };

    Asset\_ResultSet resultSet = {0};
    int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
    if (queryResult == ASSET\_SUCCESS) {
        // Parse the result
        for (uint32\_t i = 0; i < resultSet.count; i++) {
            // Parse the data label. The data corresponds to label->blob.data, and the size corresponds to label->blob.size.
            Asset\_Attr \*label = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1);
        }
    }
    OH\_Asset\_FreeResultSet(&resultSet);
    
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}
