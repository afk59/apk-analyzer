# Class (WebCookie)

Manages behavior of cookies in **Web** components. All **Web** components in an application share a **WebCookie**. You can use the **getCookieManager** API in **controller** to obtain the **WebCookie** for subsequent cookie management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/5IgB45EnTN-xzT3hg2Kr0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FDDD1BC69253DE73A1E6E3EBA93EB6ACBC153AA4C53E92E16E264F0FB610A331)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor

constructor()

Constructs a **WebCookie** object.

**System capability**: SystemCapability.Web.Webview.Core

#### setCookie(deprecated)

setCookie()

Sets the cookie. This API returns the result synchronously. **true** is returned if the operation is successful; otherwise, **false** is returned.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/mv6Dn3okT_CyJzAgClhJ0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95C0888C49233A6BB1F4883A1C6F155008907357FA3E7B7D0DFF93F4611C912E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [setCookie9+](../../../arkts-api/ohos-web-webview-webview/class-webcookiemanager/document.md#setcookiedeprecated) instead.

**System capability**: SystemCapability.Web.Webview.Core

#### saveCookie(deprecated)

saveCookie()

Saves the cookies in the memory to the drive. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/QR-8MH6kQCmcdxpOiKKi7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81BFDD89EA244A6383959D3FC9D64C1C46FE950DE48D920A88A0AB18EAC14255)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [saveCookieAsync9+](../../../arkts-api/ohos-web-webview-webview/class-webcookiemanager/document.md#savecookieasync) instead.

**System capability**: SystemCapability.Web.Webview.Core
