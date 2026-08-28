# Class (HttpAuthHandler)

Implements the **HttpAuthHandler** object. For details about the sample code, see [onHttpAuthRequest](../events/document.md#onhttpauthrequest9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iokmI_4NTzm_zX1JGuq_qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE14FDDD846C96237BDE9F961A986842953D92F0B1DAA11F76B34D5C15DF6FA8)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs an **HttpAuthHandler**.

**System capability**: SystemCapability.Web.Webview.Core

#### cancel9+

cancel(): void

Cancels HTTP authentication as requested by the user.

**System capability**: SystemCapability.Web.Webview.Core

#### confirm9+

confirm(userName: string, password: string): boolean

Performs HTTP authentication with the user name and password provided by the user.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| userName | string | Yes | HTTP authentication user name. |
| password | string | Yes | HTTP authentication password. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if the authentication is successful; otherwise, **false** is returned. |

#### isHttpAuthInfoSaved9+

isHttpAuthInfoSaved(): boolean

Sets whether to use the account name and password cached on the server for authentication.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if the authentication is successful; otherwise, **false** is returned. |
