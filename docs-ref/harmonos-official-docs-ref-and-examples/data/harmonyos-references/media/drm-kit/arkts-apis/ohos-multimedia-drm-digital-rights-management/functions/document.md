# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wbdfo2vvSvaML09R8TtOTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062430Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2B7D6461C635CBFCD58848FFC0B5A4D22C012C0086FD9B931545BD8F5586FD4)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { drm } from '@kit.DrmKit';

#### drm.createMediaKeySystem

createMediaKeySystem(name: string): MediaKeySystem

Creates a MediaKeySystem instance.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | DRM solution name, for example, **"com.wiseplay.drm"**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaKeySystem](../interface-mediakeysystem/document.md) | MediaKeySystem instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700103 | Meet max MediaKeySystem num limit |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem("com.wiseplay.drm");
} catch (err) {
  let error = err as BusinessError;
  console.error(\`createMediaKeySystem ERROR: ${error}\`);
}

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string): boolean

Checks whether the device supports the specified DRM solution.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | DRM solution name, for example, **"com.wiseplay.drm"**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the DRM solution. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed, the param name's length is zero or too big(exceeds 4096 Bytes). |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm");
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`isMediaKeySystemSupported ERROR: ${error}\`);
}

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string): boolean

Checks whether the device supports the combination of the DRM solution and MIME type.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | DRM solution name. Before calling this API, ensure that the DRM solution name is supported by calling [isMediaKeySystemSupported](#drmismediakeysystemsupported). |
| mimeType | string | Yes | MIME type. The supported MIME types depend on the DRM solution. For example, video/avc and video/hevc. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the combination. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc");
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`isMediaKeySystemSupported ERROR: ${error}\`);
}

#### drm.isMediaKeySystemSupported

isMediaKeySystemSupported(name: string, mimeType: string, level: ContentProtectionLevel): boolean

Checks whether the device supports the combination of the DRM solution, MIME type, and content protection level.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | DRM solution name. Before calling this API, ensure that the DRM solution name is supported by calling [isMediaKeySystemSupported](#drmismediakeysystemsupported). |
| mimeType | string | Yes | MIME type. The supported MIME types depend on the DRM solution. Before calling this API, ensure that the MIME type is supported by calling [isMediaKeySystemSupported](#drmismediakeysystemsupported-1). |
| level | [ContentProtectionLevel](../enums/document.md#contentprotectionlevel) | Yes | Content protection level. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the combination. **true** if supported, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. Possibly because: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let supported: boolean = drm.isMediaKeySystemSupported("com.wiseplay.drm", "video/avc", drm.ContentProtectionLevel.CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO);
  console.info("isMediaKeySystemSupported: ", supported);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`isMediaKeySystemSupported ERROR: ${error}\`);
}

#### drm.getMediaKeySystemUuid12+

getMediaKeySystemUuid(name: string): string;

Obtains the UUID of the DRM content protection system supported by the specified DRM solution.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | DRM solution name. You can check whether the solution name is supported by calling [isMediaKeySystemSupported](#drmismediakeysystemsupported). |

**Return value**

| Type | Description |
| :-- | :-- |
| string | UUID of the DRM content protection system. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed.Possibly because: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let uuid: string = drm.getMediaKeySystemUuid("com.wiseplay.drm");
  console.info("getMediaKeySystemUuid: ", uuid);
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getMediaKeySystemUuid ERROR: ${error}\`);
}

#### drm.getMediaKeySystems12+

getMediaKeySystems(): MediaKeySystemDescription\[\]

Obtains the list of plugins supported by the device.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaKeySystemDescription\[\]](../interfaces-others/document.md#mediakeysystemdescription12) | Array of supported plugins. |

**Error codes**

For details about the error codes, see [DRM Error Codes](../../../error-codes/drm-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 24700101 | All unknown errors |
| 24700201 | Fatal service error, for example, service died |

**Example**

import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let description: drm.MediaKeySystemDescription\[\] = drm.getMediaKeySystems();
} catch (err) {
  let error = err as BusinessError;
  console.error(\`getMediaKeySystems ERROR: ${error}\`);
}
