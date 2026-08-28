# @ohos.wallpaper (Wallpaper)

The **wallpaper** module provides APIs for switching between wallpapers. Since API version 9, the APIs of this module function as system APIs, and only system applications are allowed to switch between wallpapers. Applications that use the wallpaper, for example, the home screen, need to subscribe to wallpaper changes and update the wallpaper accordingly.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/0W_yNMQXQsW8acuhprob2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9CD26D6F9EF4DFEFB6CEECADDF6B39721CDE86B5CF8351AC60ED172DBB617F9)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { wallpaper } from '@kit.BasicServicesKit';

#### WallpaperType7+

Enumerates the wallpaper types.

**System capability**: SystemCapability.MiscServices.Wallpaper

| Name | Value | Description |
| :-- | :-- | :-- |
| WALLPAPER\_SYSTEM | 0 | Home screen wallpaper. |
| WALLPAPER\_LOCKSCREEN | 1 | Lock screen wallpaper. |

#### RgbaColor(deprecated)

Defines the RGBA color space for the wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/VBWCB_FSTme3g8gPenMytg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C89FFF40FF35208E498F1A0A72DFD65B0C684A0902CEB9934E548DB8D42E7C)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| red | number | No | No | Red color. The value ranges from 0 to 255. |
| green | number | No | No | Green color. The value ranges from 0 to 255. |
| blue | number | No | No | Blue color. The value ranges from 0 to 255. |
| alpha | number | No | No | Alpha value. The value ranges from 0 to 255. |

#### wallpaper.on('colorChange')(deprecated)

on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

Subscribes to the wallpaper color change event. Multi-thread concurrent calls are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/9Mm4bPQaRnmcaM5lAS-knw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C04D7F0CA569E571A9AF8483E554C359A169891C1366AEA2E9B3693C29E62034)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to subscribe to. The value **'colorChange'** indicates subscribing to the wallpaper color change event. |
| callback | function | Yes | 
Callback triggered when the wallpaper color changes. The wallpaper type and main colors are returned.

\- colors

Main color of the wallpaper. For details, see [RgbaColor](#rgbacolordeprecated).

\- wallpaperType

Wallpaper type.

 |

**Example**

try {
    let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
        console.info(\`wallpaper color changed.\`);
    };
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(\`failed to on because: ${JSON.stringify(error)}\`);
}

#### wallpaper.off('colorChange')(deprecated)

off(type: 'colorChange', callback?: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

Unsubscribes from the wallpaper color change event. Multi-thread concurrent calls are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/x9whjp4ISiWdxs_zEnykIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=794AE249372CDCB0F79EE80B0E9A7038E153F3E104DE6C47F48081A5FB08E12E)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Type of the event to unsubscribe from. The value **'colorChange'** indicates unsubscribing from the wallpaper color change event. |
| callback | function | No | 
Callback used for unsubscription. If this parameter is not set, this API unsubscribes from all callbacks of the specified event type.

\- colors

Main color of the wallpaper. For details, see [RgbaColor](#rgbacolordeprecated).

\- wallpaperType

Wallpaper type.

 |

**Example**

let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
    console.info(\`wallpaper color changed.\`);
};
try {
    wallpaper.on('colorChange', listener);
} catch (error) {
    console.error(\`failed to on because: ${JSON.stringify(error)}\`);
}

try {
    // Unsubscribe from the listener.
    wallpaper.off('colorChange', listener);
} catch (error) {
    console.error(\`failed to off because: ${JSON.stringify(error)}\`);
}

try {
    // Unsubscribe from all subscriptions of the colorChange type.
    wallpaper.off('colorChange');
} catch (error) {
    console.error(\`failed to off because: ${JSON.stringify(error)}\`);
}

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType, callback: AsyncCallback<Array<RgbaColor>>): void

Obtains the main color information of the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/hAxqMm_fQ1yKO5ny91BPwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7B2F6A0EC34975A5BEB542F9F758B11F7F00CEE15AB2B51C17DE0F71A267AAB)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |
| callback | AsyncCallback<Array<[RgbaColor](#rgbacolordeprecated)\>> | Yes | Callback used to return the main color information of the wallpaper. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError, data: Array<wallpaper.RgbaColor>) => {
    if (error) {
        console.error(\`failed to getColors because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to getColors: ${JSON.stringify(data)}\`);
});

#### wallpaper.getColors(deprecated)

getColors(wallpaperType: WallpaperType): Promise<Array<RgbaColor>>

Obtains the main color information of the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/SHyxOYsfQMuWfH95NdGTJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4544D56B04C7AE6204878595A7B3C784ED58897D2971F2FAFD0946344EBF5E92)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[RgbaColor](#rgbacolordeprecated)\>> | Promise used to return the main color information of the wallpaper. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then((data: Array<wallpaper.RgbaColor>) => {
    console.info(\`success to getColors: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to getColors because: ${JSON.stringify(error)}\`);
});

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

Obtains the ID of the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/FhOAa3uKTHaSHETdUR21Ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=886967171CACA4D56CF0E56F67F2EB885098B0A6DADE354DEFDFD1AA780CBAC8)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the wallpaper ID. If the wallpaper of the specified type is configured, a number greater than or equal to **0** is returned. Otherwise, **\-1** is returned. The value ranges from -1 to (2^31-1). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError, data: Number) => {
    if (error) {
        console.error(\`failed to getId because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to getId: ${JSON.stringify(data)}\`);
});

#### wallpaper.getId(deprecated)

getId(wallpaperType: WallpaperType): Promise<number>

Obtains the ID of the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/yX7etU6lQh-c4vL96h2vxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2333B8162E10AEDCB67CB4E1D9ABC7616954261B3BAA9AFD96C6768C3249C482)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the wallpaper ID. If this type of wallpaper is configured, a number greater than or equal to **0** is returned. Otherwise, **\-1** is returned. The value ranges from -1 to (2^31-1). |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getId(wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then((data: Number) => {
    console.info(\`success to getId: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to getId because: ${JSON.stringify(error)}\`);
});

#### wallpaper.getMinHeight(deprecated)

getMinHeight(callback: AsyncCallback<number>): void

Obtains the minimum height of this wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/E0uQEHP3TCmnfy8koplaRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDD1D96041C83AF450801B40AE44CBCBFEA9FDD9CAC0FD58B7CFE48C50DC378B)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the minimum wallpaper height, in pixels. If the return value is **0**, no wallpaper is set. In this case, the default height should be used instead. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight((error: BusinessError, data: Number) => {
    if (error) {
        console.error(\`failed to getMinHeight because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to getMinHeight: ${JSON.stringify(data)}\`);
});

#### wallpaper.getMinHeight(deprecated)

getMinHeight(): Promise<number>

Obtains the minimum height of this wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/RopmvOUoQTa10W2cQzYGTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25E27239125FFD9E1E42A2CC99A673AA13531063A01F8218D2BE7359E75FE1EF)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the minimum wallpaper height, in pixels. If the return value is **0**, no wallpaper is set. In this case, the default height should be used instead. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinHeight().then((data: Number) => {
    console.info(\`success to getMinHeight: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
    console.error(\`failed to getMinHeight because: ${JSON.stringify(error)}\`);
});

#### wallpaper.getMinWidth(deprecated)

getMinWidth(callback: AsyncCallback<number>): void

Obtains the minimum width of this wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/x4F95O45RW2ERY5OC40HnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1880070CD3A659A0D350FFFB8E9BB3BBD7B892BCE537D6445A8BA3E4D4E5E979)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the minimum wallpaper width, in pixels. If the return value is **0**, no wallpaper is set. In this case, the default width should be used instead. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth((error: BusinessError, data: Number) => {
    if (error) {
        console.error(\`failed to getMinWidth because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to getMinWidth: ${JSON.stringify(data)}\`);
});

#### wallpaper.getMinWidth(deprecated)

getMinWidth(): Promise<number>

Obtains the minimum width of this wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/qEkXvmPFRMS6UeNEtTXCIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7943FE15AE350F2E4A69B4B360CEA686DFA921D77E0450D591610A299CE04508)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the minimum wallpaper width, in pixels. If the return value is **0**, no wallpaper is set. In this case, the default width should be used instead. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getMinWidth().then((data: Number) => {
    console.info(\`success to getMinWidth: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to getMinWidth because: ${JSON.stringify(error)}\`);
});

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

Obtains the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/9fGVgBgxRom4_s86HdDhnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=213E4A59EDD8E9DC70BAE1D0005E25AA35BDD62100EFE618CE181D84859B9B84)

This API is supported since API version 8 and deprecated since API version 9.

**Required permissions**: ohos.permission.GET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. If the operation is successful, the file descriptor ID to the wallpaper is returned. Otherwise, error information is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError, data: number) => {
    if (error) {
        console.error(\`failed to getFile because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to getFile: ${JSON.stringify(data)}\`);
});

#### wallpaper.getFile(deprecated)

getFile(wallpaperType: WallpaperType): Promise<number>

Obtains the wallpaper of the specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sQR_AbKZQgqtK42u2cJBdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A31A6BC6F60BA4F493E5C9FEC8E39FAD69AF14CA055ECA3F559C22DED971C0E3)

This API is supported since API version 8 and deprecated since API version 9.

**Required permissions**: ohos.permission.GET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, the file descriptor ID to the wallpaper is returned. Otherwise, error information is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then((data: number) => {
    console.info(\`success to getFile: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to getFile because: ${JSON.stringify(error)}\`);
});

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(callback: AsyncCallback<boolean>): void

Checks whether to allow the application to change the wallpaper for the current user.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/deW_B3SRQYuXNcsWU6-5gQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A39E56DAC8DA104E6890945FF87140F2A75B5E2BBE708405671F863A667577C)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return whether to allow the application to change the wallpaper for the current user. The value **true** means that the operation is allowed, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(\`failed to isChangePermitted because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to isChangePermitted: ${JSON.stringify(data)}\`);
});

#### wallpaper.isChangePermitted(deprecated)

isChangePermitted(): Promise<boolean>

Checks whether to allow the application to change the wallpaper for the current user.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ZOcCofvEQiKSkAcWQMnJ7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C4342AEEF16C708DD69DE310A72811C1C5C936137455F3A59D52D1F794FE5CC)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether to allow the application to change the wallpaper for the current user. The value **true** means that the operation is allowed, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isChangePermitted().then((data: Boolean) => {
    console.info(\`success to isChangePermitted: ${JSON.stringify(data)}\`);
}).catch((error: BusinessError) => {
    console.error(\`failed to isChangePermitted because: ${JSON.stringify(error)}\`);
});

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(callback: AsyncCallback<boolean>): void

Checks whether the user is allowed to set wallpapers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/zn0fIHKGRSK1pugkd2tXqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F38206B208D1CEECE91E78515E5B866E2B12334BA955A2A6ECE6AE50E553B19B)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return whether the user is allowed to set wallpapers. The value **true** means that the operation is allowed, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed((error: BusinessError, data: Boolean) => {
    if (error) {
        console.error(\`failed to isOperationAllowed because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to isOperationAllowed: ${JSON.stringify(data)}\`);
});

#### wallpaper.isOperationAllowed(deprecated)

isOperationAllowed(): Promise<boolean>

Checks whether the user is allowed to set wallpapers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/jgvyBWPUTpWnu-CkVo0qMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBD5F76A7AC56B3D5739C74CE76CCDCF62FBDCC22F174D607487D005AE2A21AE)

This API is supported since API version 7 and deprecated since API version 9.

**System capability**: SystemCapability.MiscServices.Wallpaper

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return whether the user is allowed to set wallpapers. The value **true** means that the operation is allowed, and **false** means the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.isOperationAllowed().then((data: Boolean) => {
    console.info(\`success to isOperationAllowed: ${JSON.stringify(data)}\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to isOperationAllowed because: ${JSON.stringify(error)}\`);
});

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

Resets the wallpaper of the specified type to the default wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/c9aHNEbRQ9apOsy4OlfGWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D69DEF9A5D5DCF141107B79C6C14EBBA35887B42080E66D2C2AC50DBB2F53460)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the wallpaper is reset, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(\`failed to reset because: ${JSON.stringify(error)}\`);
        return;
    }
    console.info(\`success to reset.\`);
});

#### wallpaper.reset(deprecated)

reset(wallpaperType: WallpaperType): Promise<void>

Resets the wallpaper of the specified type to the default wallpaper.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/nDsn0et0RBKvwhSXmzx9YQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DE9ECB65786707D76B58F5DFCF3F7FDAB81C222A5619972AC6DE99103AD632B)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

wallpaper.reset(wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then(() => {
    console.info(\`success to reset.\`);
}).catch((error: BusinessError) => {
    console.error(\`failed to reset because: ${JSON.stringify(error)}\`);
});

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

Sets a specified source as the wallpaper of a specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/O_0IXwXZSpeTYl3652Yfbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24FEFF1360BB10161F4ECC245FC958A340E506DD323E6972F1A647EDB824705B)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | string | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | URI of a JPEG or PNG file, or pixel map of a PNG file. |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the wallpaper is set, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// The source type is string.
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError) => {
    if (error) {
        console.error(\`failed to setWallpaper because: ${JSON.stringify(error)}\`);
       return;
       }
    console.info(\`success to setWallpaper.\`);
});

// The source type is image.PixelMap.
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER\_SYSTEM, (error: BusinessError) => {
        if (error) {
            console.error(\`failed to setWallpaper because: ${JSON.stringify(error)}\`);
            return;
        }
        console.info(\`success to setWallpaper.\`);
    });
}).catch((error: BusinessError) => {
    console.error(\`failed to createPixelMap because: ${JSON.stringify(error)}\`);
});

#### wallpaper.setWallpaper(deprecated)

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType): Promise<void>

Sets a specified source as the wallpaper of a specified type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/gDJQVTzLQAyis-HmKRxByA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C91D44DF05840F9567E1F53409E4AE05DD4ED78CF98111D3450213404CD4391)

This API is supported since API version 7 and deprecated since API version 9.

**Required permissions**: ohos.permission.SET\_WALLPAPER

**System capability**: SystemCapability.MiscServices.Wallpaper

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | string | [image.PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | URI of a JPEG or PNG file, or pixel map of a PNG file. |
| wallpaperType | [WallpaperType](#wallpapertype7) | Yes | Wallpaper type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// The source type is string.
let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then(() => {
    console.info(\`success to setWallpaper.\`);
  }).catch((error: BusinessError) => {
    console.error(\`failed to setWallpaper because: ${JSON.stringify(error)}\`);
});
  
// The source type is image.PixelMap.
let imageSource = image.createImageSource("file://" + wallpaperPath);
let opts: image.DecodingOptions = {
    desiredSize: {
        height: 3648,
        width: 2736
    }
};
imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
    wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER\_SYSTEM).then(() => {
        console.info(\`success to setWallpaper.\`);
    }).catch((error: BusinessError) => {
        console.error(\`failed to setWallpaper because: ${JSON.stringify(error)}\`);
    });
  }).catch((error: BusinessError) => {
    console.error(\`failed to createPixelMap because: ${JSON.stringify(error)}\`);
});
