# arkweb\_error\_code.h

#### Overview

Declares the error codes of the ArkWeb NDK APIs.

**File to include**: <web/arkweb\_error\_code.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_ErrorCode](#arkweb_errorcode) | ArkWeb\_ErrorCode | Enumerates the error codes of ArkWeb NDK APIs. |
| [ArkWeb\_BlanklessErrorCode](#arkweb_blanklesserrorcode) | ArkWeb\_BlanklessErrorCode | Enumerates the error codes for the blankless loading. |

#### Enum Description

#### \[h2\]ArkWeb\_ErrorCode

enum ArkWeb\_ErrorCode

**Description**

Enumerates the error codes of ArkWeb NDK APIs.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ARKWEB\_SUCCESS = 0 | Operation successful. |
| ARKWEB\_INIT\_ERROR = 17100001 | Initialization error. |
| ARKWEB\_ERROR\_UNKNOWN = 17100100 | Unknown error. |
| ARKWEB\_INVALID\_PARAM = 17100101 | Invalid parameter. |
| ARKWEB\_SCHEME\_REGISTER\_FAILED = 17100102 | Failed to register the scheme. Register the scheme before creating the **Web** component. |
| ARKWEB\_INVALID\_URL = 17100103 | Invalid URL. |
| ARKWEB\_INVALID\_COOKIE\_VALUE = 17100104 | Invalid cookie value. |
| ARKWEB\_LIBRARY\_OPEN\_FAILURE = 17100105 | 
Failed to open the dynamic link library.

**Since**: 15

 |
| ARKWEB\_LIBRARY\_SYMBOL\_NOT\_FOUND = 17100106 | 

The required symbol cannot be found in the dynamic link library.

**Since**: 15

 |
| ARKWEB\_COOKIE\_MANAGER\_NOT\_INITIALIZED = 17100107 | 

**CookieManager** is not initialized.

**Since**: 20

 |
| ARKWEB\_COOKIE\_MANAGER\_INITIALIZE\_FAILED = 17100108 | 

**CookieManager** fails to be initialized.

**Since**: 20

 |
| ARKWEB\_COOKIE\_SAVE\_FAILED = 17100109 | 

Cookies fail to be saved.

**Since**: 20

 |

#### \[h2\]ArkWeb\_BlanklessErrorCode

enum ArkWeb\_BlanklessErrorCode

**Description**

Enumerates the error codes for the blankless loading.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| ARKWEB\_BLANKLESS\_SUCCESS = 0 | Operation successful. |
| ARKWEB\_BLANKLESS\_ERR\_UNKNOWN = -1 | Unknown error or internal status error. |
| ARKWEB\_BLANKLESS\_ERR\_INVALID\_ARGS = -2 | Invalid parameter. |
| ARKWEB\_BLANKLESS\_ERR\_CONTROLLER\_NOT\_INITED = -3 | **WebViewController** is not bound to any component. |
| ARKWEB\_BLANKLESS\_ERR\_KEY\_NOT\_MATCH = -4 | The key value is not matched. The **OH\_NativeArkWeb\_SetBlanklessLoadingWithKey** and **OH\_NativeArkWeb\_GetBlanklessInfoWithKey** APIs must be used in pair and use the same key value. |
| ARKWEB\_BLANKLESS\_ERR\_SIGNIFICANT\_CHANGE = -5 | When the similarity is low, the system will deem the scene change too abrupt and frame insertion through the **OH\_NativeArkWeb\_SetBlanklessLoadingWithKey** API will fail. |
| ARKWEB\_BLANKLESS\_ERR\_DEVICE\_NOT\_SUPPORT = 801 | This device does not support this feature. |
