# ArkWeb\_CookieManagerAPI

typedef struct {...} ArkWeb\_CookieManagerAPI

#### Overview

Defines the CookieManager API of ArkWeb. Before calling this API, you are advised to use [ARKWEB\_MEMBER\_MISSING](../../header-files/arkweb-type-h/document.md#macros) to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The CookieManager APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t size | Size of the struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode (\*fetchCookieSync)(const char\* url, bool incognito, bool includeHttpOnly, char\*\* cookieValue)](#fetchcookiesync) | Obtains the cookie value of a specified URL. |
| [ArkWeb\_ErrorCode (\*configCookieSync)(const char\* url,const char\* cookieValue, bool incognito, bool includeHttpOnly)](#configcookiesync) | Sets the cookie value of a specified URL. |
| [bool (\*existCookies)(bool incognito)](#existcookies) | Checks whether cookies exist. |
| [void (\*clearAllCookiesSync)(bool incognito)](#clearallcookiessync) | Clears all cookies. |
| [void (\*clearSessionCookiesSync)()](#clearsessioncookiessync) | Clears all session cookies. |

#### Member Function Description

#### \[h2\]fetchCookieSync()

ArkWeb\_ErrorCode (\*fetchCookieSync)(const char\* url, bool incognito, bool includeHttpOnly, char\*\* cookieValue)

**Description**

Obtains the cookie value of a specified URL.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* url | URL of the cookie to obtain. A complete URL is recommended. |
| bool incognito | Whether to obtain the webview memory cookie in incognito mode or in non-incognito mode. The value **true** means to obtain the webview memory cookie in incognito mode, and the value **false** means the opposite. |
| bool includeHttpOnly | Whether to include the cookie marked as **HttpOnly** in **cookieValue**. |
| char\*\* cookieValue | Cookie value of the URL. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode) | 
Error code.

[ARKWEB\_SUCCESS](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The cookie is successfully obtained.

[ARKWEB\_INVALID\_URL](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The URL is invalid.

[ARKWEB\_INVALID\_PARAM](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The parameter is invalid.

 |

#### \[h2\]configCookieSync()

ArkWeb\_ErrorCode (\*configCookieSync)(const char\* url,const char\* cookieValue, bool incognito, bool includeHttpOnly)

**Description**

Sets the cookie value of a specified URL.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* url | URL of the specified cookie. It must be a complete URL. |
| const char\* cookieValue | Cookie value to be set. |
| bool incognito | Whether to set the cookie of corresponding URL in incognito mode. The value **true** means to set the cookie of corresponding URL in incognito mode, and **false** means the opposite. |
| bool includeHttpOnly | Whether to overwrite the cookie marked as **HTTPOnly**. The value **true** means to overwrite the cookie marked as **HTTPOnly**, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode) | 
Error code.

[ARKWEB\_SUCCESS](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The cookie is successfully obtained.

[ARKWEB\_INVALID\_URL](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The URL is invalid.

[ARKWEB\_INVALID\_COOKIE\_VALUE](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The cookie value is invalid.

 |

#### \[h2\]existCookies()

bool (\*existCookies)(bool incognito)

**Description**

Checks whether cookies exist.

**Parameters**

| Name | Description |
| :-- | :-- |
| bool incognito | Whether the cookie exists in incognito mode or in non-incognito mode. The value **true** indicates that the cookie exists in incognito mode, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if the cookie exists; otherwise, **false** is returned. |

#### \[h2\]clearAllCookiesSync()

void (\*clearAllCookiesSync)(bool incognito)

**Description**

Clears all cookies.

**Parameters**

| Name | Description |
| :-- | :-- |
| bool incognito | Whether to clear all cookies in incognito mode. The value **true** means to clear all cookies in incognito mode, and **false** means the opposite. |

#### \[h2\]clearSessionCookiesSync()

void (\*clearSessionCookiesSync)()

**Description**

Clears all session cookies.
