# PlayImageAnimation

#### Module Import

import { map } from '@kit.MapKit';

#### PlayImageAnimation

Frame animation for controlling multiple images, which inherits from [Animation](../animation/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

import { image } from '@kit.ImageKit';

let images: Array<ResourceStr | image.PixelMap> = \[
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
\];
let playImageAnimation: map.PlayImageAnimation = new map.PlayImageAnimation();
await playImageAnimation.addImages(images);

#### \[h2\]addImages

addImages(images: Array<ResourceStr | image.PixelMap>): Promise<void>

Adds image resources of an animation. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

images

 | 

Array<[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Yes

 | 

Image resources of an animation.

NOTE:

-   It is recommended that these images be of the same size.
-   The number of images cannot exceed 200.
-   The duration must be greater than 33 ms. If this condition is not met, it will be adjusted to 33 ms.
-   If this parameter value is of the string type, store images in **resources/rawfile**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Invalid input parameter.

 |

**Example**:

import { image } from '@kit.ImageKit';

let images: Array<ResourceStr | image.PixelMap> = \[
   'test1.png',
   'test2.png',
   'test3.png',
   'test4.png'
\];
await playImageAnimation.addImages(images);
