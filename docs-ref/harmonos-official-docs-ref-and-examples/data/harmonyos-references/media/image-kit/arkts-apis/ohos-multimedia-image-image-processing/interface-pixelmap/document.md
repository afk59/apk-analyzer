# Interface (PixelMap)

The **PixelMap** class provides APIs to read or write image data and obtain image information. Before calling any API in PixelMap, you must use [image.createPixelMap](../functions/document.md#imagecreatepixelmap8) to create a PixelMap object. Currently, the maximum size of a serialized PixelMap is 128 MB. A larger size will cause a display failure. The size is calculated as follows: Width × Height × [Bytes per pixel](../enums/document.md#pixelmapformat7).

Since API version 11, PixelMap supports cross-thread calls through [Worker](../../../../../application-framework/arkts/arkts-apis/ohos-worker-starting-the-worker/document.md). If a PixelMap object is invoked by another thread through [Worker](../../../../../application-framework/arkts/arkts-apis/ohos-worker-starting-the-worker/document.md), all APIs of the PixelMap object cannot be called in the original thread. Otherwise, error 501 is reported, indicating that the server cannot complete the request.

Before calling any API in PixelMap, you can use [image.createPixelMap](../functions/document.md#imagecreatepixelmap8) to pass pixel data to create a PixelMap object, or use [ImageSource](../interface-imagesource/document.md) to decode an image to a PixelMap object.

To develop an atomic service, use [ImageSource](../interface-imagesource/document.md) to create a PixelMap object.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/qyvAd9HpSwW4VwThv_eyPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=339DE4ED7EB5F7394A2D2E22F2C6123D99261DA778EE35EE82C30F3E6CADA2FD)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 7.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isEditable7+ | boolean | Yes | No | 
Whether the image pixels are editable. **true** if editable, **false** otherwise. The value **false** provides better image rendering and transmission performance.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

 |
| isStrideAlignment11+ | boolean | Yes | No | Whether the row data of the image is memory aligned. The value **true** means that the row data is memory-aligned, and there may be blank bytes padded at the end of each row to meet alignment requirements. The value **false** means that the row data is not memory-aligned, and rows are packed contiguously with no padding bytes at the end. |

#### readPixelsToBuffer7+

readPixelsToBuffer(dst: ArrayBuffer): Promise<void>

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
    }).catch((error: BusinessError) => {
      console.error(\`Failed to read image pixel data. code is ${error.code}, message is ${error.message}\`); // Called if no condition is met.
    })
  }
}

#### readPixelsToBuffer7+

readPixelsToBuffer(dst: ArrayBuffer, callback: AsyncCallback<void>): void

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(pixelMap : image.PixelMap) {
  const readBuffer: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBuffer(readBuffer, (error: BusinessError, res: void) => {
      if(error) {
        console.error(\`Failed to read image pixel data. code is ${error.code}, message is ${error.message}\`); // Called if no condition is met.
        return;
      } else {
        console.info('Succeeded in reading image pixel data.'); // Called if the condition is met.
      }
    })
  }
}

#### readPixelsToBufferSync12+

readPixelsToBufferSync(dst: ArrayBuffer): void

Reads the pixels of this PixelMap object based on the PixelMap's pixel format and writes the data to the buffer. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dst | ArrayBuffer | Yes | Buffer to which the pixels will be written. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function ReadPixelsToBufferSync(pixelMap : image.PixelMap) {
  const bufferSize = pixelMap.getPixelBytesNumber();
  const readBuffer = new ArrayBuffer(bufferSize);
  if (pixelMap != undefined) {
    pixelMap.readPixelsToBufferSync(readBuffer);
  }
}

#### readPixels7+

readPixels(area: PositionArea): Promise<void>

Reads the pixels in the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).region of this PixelMap object in the BGRA\_8888 format and writes the data to the [PositionArea](../interfaces-others/document.md#positionarea7).pixels buffer. This API uses a promise to return the result.

You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.

YUV region calculation formula: region to read (region.size{width \* height}) \* 1.5 (1 \* Y component + 0.25 \* U component + 0.25 \* V component)

RGBA region calculation formula: region to read (region.size{width \* height}) \* 4 (1 \* R component + 1 \* G component + 1 \* B component + 1 \* A component)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area from which the pixels will be read. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // Called if the condition is met.
      console.info('RGBA data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// Called if the condition is not met.
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 1.5.
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area).then(() => {
      console.info('Succeeded in reading the image data in the area.'); // Called if the condition is met.
      console.info('YUV data is ', new Uint8Array(area.pixels));
    }).catch((error: BusinessError) => {
      console.error("Failed to read the image data in the area. code is ", error);// Called if the condition is not met.
    })
  }
}

#### readPixels7+

readPixels(area: PositionArea, callback: AsyncCallback<void>): void

Reads the pixels in the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).region of this PixelMap object in the BGRA\_8888 format and writes the data to the [PositionArea](../interfaces-others/document.md#positionarea7).pixels buffer. This API uses an asynchronous callback to return the result.

You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.

YUV region calculation formula: region to read (region.size{width \* height}) \* 1.5 (1 \* Y component + 0.25 \* U component + 0.25 \* V component)

RGBA region calculation formula: region to read (region.size{width \* height}) \* 4 (1 \* R component + 1 \* G component + 1 \* B component + 1 \* A component)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area from which the pixels will be read. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsRGBA(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('RGBA data is ', new Uint8Array(area.pixels));
      }
    })
  }
}

async function ReadPixelsYUV(pixelMap : image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 1.5.
    offset: 0,
    stride: 8,
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixels(area, (error: BusinessError) => {
      if (error) {
        console.error("Failed to read pixelmap from the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in reading pixelmap from the specified area.');
        console.info('YUV data is ', new Uint8Array(area.pixels));
      }
    })
  }
}

#### readPixelsSync12+

readPixelsSync(area: PositionArea): void

Reads the pixels in the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).region of this PixelMap object in the BGRA\_8888 format and writes the data to the [PositionArea](../interfaces-others/document.md#positionarea7).pixels buffer. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area from which the pixels will be read. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function ReadPixelsSync(pixelMap : image.PixelMap) {
  const area : image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  if (pixelMap != undefined) {
    pixelMap.readPixelsSync(area);
  }
}

#### writePixels7+

writePixels(area: PositionArea): Promise<void>

Reads the pixels in the [PositionArea](../interfaces-others/document.md#positionarea7).region buffer in the BGRA\_8888 format and writes the data to the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).pixels in this PixelMap object. This API uses a promise to return the result.

You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.

YUV region calculation formula: region to read (region.size{width \* height}) \* 1.5 (1 \* Y component + 0.25 \* U component + 0.25 \* V component)

RGBA region calculation formula: region to read (region.size{width \* height}) \* 4 (1 \* R component + 1 \* G component + 1 \* B component + 1 \* A component)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area to which the pixels will be written. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(6),  // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 1.5.
    offset: 0,
    stride: 8, // This variable is not used by writePixels when the PixelMap is in YUV format.
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area).then(() => {
      console.info('Succeeded in writing pixelmap into the specified area.');
    }).catch((error: BusinessError) => {
      console.error("Failed to write pixelmap into the specified area. code is ", error);
    })
  }
}

#### writePixels7+

writePixels(area: PositionArea, callback: AsyncCallback<void>): void

Reads the pixels in the [PositionArea](../interfaces-others/document.md#positionarea7).region buffer in the BGRA\_8888 format and writes the data to the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).pixels in this PixelMap object. This API uses an asynchronous callback to return the result.

You can use a formula to calculate the size of the memory to be applied for based on **PositionArea**.

YUV region calculation formula: region to read (region.size{width \* height}) \* 1.5 (1 \* Y component + 0.25 \* U component + 0.25 \* V component)

RGBA region calculation formula: region to read (region.size{width \* height}) \* 4 (1 \* R component + 1 \* G component + 1 \* B component + 1 \* A component)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area to which the pixels will be written. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function WritePixelsRGBA(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(8), // 8 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 4.
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}

async function WritePixelsYUV(pixelMap:image.PixelMap) {
  const area: image.PositionArea = { pixels: new ArrayBuffer(6), // 6 is the size of the PixelMap buffer to create. The value is calculated as follows: height \* width \* 1.5.
    offset: 0,
    stride: 8, // This variable is not used by writePixels when the PixelMap is in YUV format.
    region: { size: { height: 2, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixels(area, (error : BusinessError) => {
      if (error) {
        console.error("Failed to write pixelmap into the specified area. code is ", error);
        return;
      } else {
        console.info('Succeeded in writing pixelmap into the specified area.');
      }
    })
  }
}

#### writePixelsSync12+

writePixelsSync(area: PositionArea): void

Reads the pixels in the [PositionArea](../interfaces-others/document.md#positionarea7).region buffer in the BGRA\_8888 format and writes the data to the area specified by [PositionArea](../interfaces-others/document.md#positionarea7).pixels in this PixelMap object. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| area | [PositionArea](../interfaces-others/document.md#positionarea7) | Yes | Area to which the pixels will be written. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function WritePixelsSync(pixelMap:image.PixelMap) {
  const area: image.PositionArea = {
    pixels: new ArrayBuffer(8),
    offset: 0,
    stride: 8,
    region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
  };
  let bufferArr: Uint8Array = new Uint8Array(area.pixels);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writePixelsSync(area);
  }
}

#### writeBufferToPixels7+

writeBufferToPixels(src: ArrayBuffer): Promise<void>

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color).then(() => {
      console.info("Succeeded in writing data from a buffer to a PixelMap.");
    }).catch((error: BusinessError) => {
      console.error(\`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### writeBufferToPixels7+

writeBufferToPixels(src: ArrayBuffer, callback: AsyncCallback<void>): void

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the pixels in the buffer are successfully written to the PixelMap, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function WriteBufferToPixels(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixels(color, (error: BusinessError) => {
      if (error) {
        console.error(\`Failed to write data from a buffer to a PixelMap. code is ${error.code}, message is ${error.message}\`);
        return;
      } else {
        console.info("Succeeded in writing data from a buffer to a PixelMap.");
      }
    })
  }
}

#### writeBufferToPixelsSync12+

writeBufferToPixelsSync(src: ArrayBuffer): void

Reads the pixels in the buffer based on the PixelMap's pixel format and writes the data to this PixelMap object. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | ArrayBuffer | Yes | Buffer from which the pixels are read. The buffer size is obtained by calling [getPixelBytesNumber](#getpixelbytesnumber7). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function WriteBufferToPixelsSync(pixelMap:image.PixelMap) {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let bufferArr : Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = i + 1;
  }
  if (pixelMap != undefined) {
    pixelMap.writeBufferToPixelsSync(color);
  }
}

#### getImageInfo7+

getImageInfo(): Promise<ImageInfo>

Obtains the image information of a PixelMap. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ImageInfo](../interfaces-others/document.md#imageinfo)\> | Promise used to return the image information. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetImageInfo(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
      if (imageInfo != undefined) {
        console.info(\`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}\`);
      }
    }).catch((error: BusinessError) => {
      console.error(\`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### getImageInfo7+

getImageInfo(callback: AsyncCallback<ImageInfo>): void

Obtains the image information. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ImageInfo](../interfaces-others/document.md#imageinfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the image information obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function GetImageInfoSync(pixelMap : image.PixelMap){
  if (pixelMap != undefined) {
    pixelMap.getImageInfo((error: BusinessError, imageInfo: image.ImageInfo) => {
      if (error) {
        console.error(\`Failed to obtain the image pixel map information. code is ${error.code}, message is ${error.message}\`);
        return;
      } else {
        console.info(\`Succeeded in obtaining the image pixel map information ${imageInfo.size.height}\`);
      }
    })
  }
}

#### getImageInfoSync12+

getImageInfoSync(): ImageInfo

Obtains the image information. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageInfo](../interfaces-others/document.md#imageinfo) | Image information. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 501 | Resource Unavailable |

**Example**

function GetImageInfoSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let imageInfo : image.ImageInfo = pixelMap.getImageInfoSync();
    return imageInfo;
  }
  return undefined;
}

#### getBytesNumberPerRow7+

getBytesNumberPerRow(): number

Obtains the number of bytes per row of this image. Unit: bytes.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of bytes per row. |

**Example**

function GetBytesNumberPerRow(pixelMap: image.PixelMap) {
  let rowCount: number = pixelMap.getBytesNumberPerRow();
}

#### getPixelBytesNumber7+

getPixelBytesNumber(): number

Obtains the total number of bytes of this image. Unit: bytes.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Total number of bytes. |

**Example**

function GetPixelBytesNumber(pixelMap: image.PixelMap) {
  let pixelBytesNumber: number = pixelMap.getPixelBytesNumber();
}

#### getDensity9+

getDensity():number

Obtains the pixel density of this image. Unit: ppi (pixels/inch)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Pixel density, in ppi. |

**Example**

function GetDensity(pixelMap: image.PixelMap) {
  let getDensity: number = pixelMap.getDensity();
}

#### opacity9+

opacity(rate: number, callback: AsyncCallback<void>): void

Sets an opacity rate for this image. This API uses an asynchronous callback to return the result. It is invalid for YUV images.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | number | Yes | Opacity rate. The value range is (0,1\]. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to set opacity. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in setting opacity.");
      }
    })
  }
}

#### opacity9+

opacity(rate: number): Promise<void>

Sets an opacity rate for this image. It is invalid for YUV images. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | number | Yes | Opacity rate. The value range is (0,1\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Opacity(pixelMap:image.PixelMap) {
  let rate: number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacity(rate).then(() => {
      console.info('Succeeded in setting opacity.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set opacity. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### opacitySync12+

opacitySync(rate: number): void

Sets an opacity rate for this image. This API returns the result synchronously. It is invalid for YUV images.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rate | number | Yes | Opacity rate. The value range is (0,1\]. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function OpacitySync(pixelMap:image.PixelMap) {
  let rate : number = 0.5;
  if (pixelMap != undefined) {
    pixelMap.opacitySync(rate);
  }
}

#### createAlphaPixelmap9+

createAlphaPixelmap(): Promise<PixelMap>

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](#)\> | Promise used to return the PixelMap object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap().then((alphaPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating alpha pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to create alpha pixelmap. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### createAlphaPixelmap9+

createAlphaPixelmap(callback: AsyncCallback<PixelMap>): void

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. It is invalid for YUV images. This API returns the result through a callback.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[PixelMap](#)\> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateAlphaPixelmap(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.createAlphaPixelmap((err: BusinessError, alphaPixelMap: image.PixelMap) => {
      if (alphaPixelMap == undefined) {
        console.error(\`Failed to obtain new pixel map. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info('Succeeded in obtaining new pixel map.');
      }
    })
  }
}

#### createAlphaPixelmapSync12+

createAlphaPixelmapSync(): PixelMap

Creates a PixelMap object that contains only the alpha channel information. This object can be used for the shadow effect. This API returns the result synchronously. It is invalid for YUV images.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](#) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function CreateAlphaPixelmapSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let pixelmap : image.PixelMap = pixelMap.createAlphaPixelmapSync();
    return pixelmap;
  }
  return undefined;
}

#### scale9+

scale(x: number, y: number, callback: AsyncCallback<void>): void

Scales this image based on the scale factors of the width and height. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/01S5-9bBT0u6iX80Hnmbrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14DDA9D6D91617F318B3FFD35E8198954E098A7DFBD4A6D1EB40B3653C11DA64)

1.  You are advised to set the scale factors to non-negative numbers to avoid a flipping effect.
2.  Scale factors of the width and height = Width and height of the resized image/Width and height of the original image

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in scaling pixelmap.");
      }
    })
  }
}

#### scale9+

scale(x: number, y: number): Promise<void>

Scales this image based on the scale factors of the width and height. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/wfvB9BOgRj6aslPqJt2pvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E232890ED8E90B8026E2A782FAF37606FD3AF4DDCF1A5E25AB60C64DF62D6095)

1.  You are advised to set the scale factors to non-negative numbers to avoid a flipping effect.
2.  Scale factors of the width and height = Width and height of the resized image/Width and height of the original image

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Scale(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### scaleSync12+

scaleSync(x: number, y: number): void

Scales this image based on the scale factors of the width and height. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/wU165KT-S9isV6c6v97qZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF28B51D94B308EE5AC29236FF7DC02A9CABA5EC82CBFBD8B69B223BDE8EE245)

1.  You are advised to set the scale factors to non-negative numbers to avoid a flipping effect.
2.  Scale factors of the width and height = Width and height of the resized image/Width and height of the original image

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY);
  }
}

#### scale12+

scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/BNwYmZWZSh-D0RQUa0hmCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6B224DC653A3D8A2A4D9E8BEA52B7967A77F9D0E5BCE83A07280EEAA277050A)

1.  You are advised to set the scale factors to non-negative numbers to avoid a flipping effect.
2.  Scale factors of the width and height = Width and height of the resized image/Width and height of the original image

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | Yes | Anti-aliasing level. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function ScaleSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scale(scaleX, scaleY, image.AntiAliasingLevel.LOW).then(() => {
      console.info('Succeeded in scaling pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to scale pixelmap. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### scaleSync12+

scaleSync(x: number, y: number, level: AntiAliasingLevel): void

Scales this image based on the specified anti-aliasing level and the scale factors for the width and height. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/l_Sk402UR02nCwnNz5-lqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6826EF8B78CB951E941E7F17835EC1349F1D8A0B5742FB1A3124BB4860689CD2)

1.  You are advised to set the scale factors to non-negative numbers to avoid a flipping effect.
2.  Scale factors of the width and height = Width and height of the resized image/Width and height of the original image

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | Yes | Anti-aliasing level. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function ScaleSync(pixelMap: image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    pixelMap.scaleSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}

#### createScaledPixelMap18+

createScaledPixelMap(x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](#)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateScaledPixelMap(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
      pixelMap.createScaledPixelMap(scaleX, scaleY, image.AntiAliasingLevel.LOW).then((scaledPixelMap: image.PixelMap) => {
      console.info('Succeeded in creating scaledPixelMap.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to create scaledPixelMap. Error code is ${error.code}, error message is ${error.message}\`);
    })
  }
}

#### createScaledPixelMapSync18+

createScaledPixelMapSync(x: number, y: number, level?: AntiAliasingLevel): PixelMap

Creates an image that has been resized based on the specified anti-aliasing level and the scale factors of the width and height. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Scale factor of the width. |
| y | number | Yes | Scale factor of the height. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](#) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function CreateScaledPixelMapSync(pixelMap:image.PixelMap) {
  let scaleX: number = 2.0;
  let scaleY: number = 1.0;
  if (pixelMap != undefined) {
    let scaledPixelMap = pixelMap.createScaledPixelMapSync(scaleX, scaleY, image.AntiAliasingLevel.LOW);
  }
}

#### createCroppedAndScaledPixelMap22+

createCroppedAndScaledPixelMap(region: Region, x: number, y: number, level?: AntiAliasingLevel): Promise<PixelMap>

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | number | Yes | Scale factor of the width. It must not be **0**. |
| y | number | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](#)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | The PixelMap has been released. |
| 7600204 | Invalid region. |
| 7600205 | Unsupported memory format or pixel format. |
| 7600301 | Memory alloc failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMap(pixelMap: PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  pixelMap.createCroppedAndScaledPixelMap(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH)
    .then((croppedAndScaled: PixelMap) => {
      console.info('PixelMap crop and scale succeeded.');
    })
    .catch((error: BusinessError) => {
      console.error(\`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}\`);
    });
}

#### createCroppedAndScaledPixelMapSync22+

createCroppedAndScaledPixelMapSync(region: Region, x: number, y: number, level?: AntiAliasingLevel): PixelMap

Creates an image that has been cropped and resized based on the specified cropping area, scale factors of the width and height, and anti-aliasing level. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Area to crop. It must be within the original image's dimension (in pixels). |
| x | number | Yes | Scale factor of the width. It must not be **0**. |
| y | number | Yes | Scale factor of the height. It must not be **0**. |
| level | [AntiAliasingLevel](../enums/document.md#antialiasinglevel12) | No | Anti-aliasing level. The default value is **AntiAliasingLevel.NONE**. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](#) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | The PixelMap has been released. |
| 7600204 | Invalid region. |
| 7600205 | Unsupported memory format or pixel format. |
| 7600301 | Memory alloc failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function DemoCreateCroppedAndScaledPixelMapSync(pixelMap: PixelMap) {
  const imageInfo = pixelMap.getImageInfoSync();
  const region: image.Region = {
    size: { width: imageInfo.size.width / 2, height: imageInfo.size.height / 2 },
    x: imageInfo.size.width / 4,
    y: imageInfo.size.height / 4
  };
  const scaleX: number = 2.0;
  const scaleY: number = 2.0;
  try {
    const croppedAndScaled = pixelMap.createCroppedAndScaledPixelMapSync(region, scaleX, scaleY, image.AntiAliasingLevel.HIGH);
  } catch (e) {
    const error = e as BusinessError;
    console.error(\`PixelMap crop and scale failed. Error code: ${error.code}, message: ${error.message}\`);
  }
}

#### clone18+

clone(): Promise<PixelMap>

Copies this PixelMap object. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](#)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 501 | Resource unavailable. |
| 62980102 | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| 62980103 | Image YUV And ASTC types are not supported. |
| 62980104 | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.clone().then((clonePixelMap: image.PixelMap) => {
      console.info('Succeeded clone pixelmap.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to clone pixelmap. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### cloneSync18+

cloneSync(): PixelMap

Copies this PixelMap object. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](#) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 501 | Resource unavailable. |
| 62980102 | Image malloc abnormal. This status code is thrown when an error occurs during the process of copying data. |
| 62980103 | Image YUV And ASTC types are not supported. |
| 62980104 | Image initialization abnormal. This status code is thrown when an error occurs during the process of creating empty pixelmap. |
| 62980106 | The image data is too large. This status code is thrown when an error occurs during the process of checking size. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function CloneSync(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      let clonedPixelMap:image.PixelMap = pixelMap.cloneSync();
    } catch(e) {
      let error = e as BusinessError;
      console.error(\`clone pixelmap error. code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### translate9+

translate(x: number, y: number, callback: AsyncCallback<void>): void

Translates this image based on given coordinates. This API uses an asynchronous callback to return the result.

The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X coordinate to translate, in px. |
| y | number | Yes | Y coordinate to translate, in px. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in translating pixelmap.");
      }
    })
  }
}

#### translate9+

translate(x: number, y: number): Promise<void>

Translates a PixelMap based on given coordinates. This API uses a promise to return the result.

The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X coordinate to translate, in px. |
| y | number | Yes | Y coordinate to translate, in px. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Translate(pixelMap:image.PixelMap) {
  let translateX: number = 50.0;
  let translateY: number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translate(translateX, translateY).then(() => {
      console.info('Succeeded in translating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to translate pixelmap. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### translateSync12+

translateSync(x: number, y: number): void

Translates this image based on given coordinates. This API returns the result synchronously.

The size of the translated image is changed to width+X and height+Y. It is recommended that the new width and height not exceed the width and height of the screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | X coordinate to translate, in px. |
| y | number | Yes | Y coordinate to translate, in px. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function TranslateSync(pixelMap:image.PixelMap) {
  let translateX : number = 50.0;
  let translateY : number = 10.0;
  if (pixelMap != undefined) {
    pixelMap.translateSync(translateX, translateY);
  }
}

#### rotate9+

rotate(angle: number, callback: AsyncCallback<void>): void

Rotates this image based on a given angle. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/2EFtiH9nRXi6B6ZwZdy3WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48B018E9104E601BD47ABEEF62DC2DA4025E72BBC690364CBC299ED387C27C92)

1.  The allowable range for image rotation angles is \[0, 360\]. Angles outside this range are automatically adjusted according to the 360-degree cycle. For example, an angle of -100 degrees will produce the same result as 260 degrees.
2.  If the rotation angle is not an integer multiple of 90 degrees, the image size will change after rotation.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | Angle to rotate. Unit: degrees. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in rotating pixelmap.");
      }
    })
  }
}

#### rotate9+

rotate(angle: number): Promise<void>

Rotates a PixelMap based on a given angle. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/FndO8uZpQLmuEF2BHpqF7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B77CA60E3EA03F612AB23876B96F16E8B515F56192492C5F03AF50F926145F9A)

1.  The allowable range for image rotation angles is \[0, 360\]. Angles outside this range are automatically adjusted according to the 360-degree cycle. For example, an angle of -100 degrees will produce the same result as 260 degrees.
2.  If the rotation angle is not an integer multiple of 90 degrees, the image size will change after rotation.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | Angle to rotate. Unit: degrees. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Rotate(pixelMap:image.PixelMap) {
  let angle: number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotate(angle).then(() => {
      console.info('Succeeded in rotating pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to rotate pixelmap. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### rotateSync12+

rotateSync(angle: number): void

Rotates this image based on a given angle. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/OqLYDKI5QM2a2Ut4JmdOJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D51A1D5B6F0AF155845852C06666BCB4F37910ECA75EE2DE8DC2DFBB41BB697B)

1.  The allowable range for image rotation angles is \[0, 360\]. Angles outside this range are automatically adjusted according to the 360-degree cycle. For example, an angle of -100 degrees will produce the same result as 260 degrees.
2.  If the rotation angle is not an integer multiple of 90 degrees, the image size will change after rotation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| angle | number | Yes | Angle to rotate. Unit: degrees. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

function RotateSync(pixelMap: image.PixelMap) {
  let angle : number = 90.0;
  if (pixelMap != undefined) {
    pixelMap.rotateSync(angle);
  }
}

#### flip9+

flip(horizontal: boolean, vertical: boolean, callback: AsyncCallback<void>): void

Flips this image horizontally or vertically, or both. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in flipping pixelmap.");
      }
    })
  }
}

#### flip9+

flip(horizontal: boolean, vertical: boolean): Promise<void>

Flips a PixelMap based on a given angle. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Flip(pixelMap:image.PixelMap) {
  let horizontal: boolean = true;
  let vertical: boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flip(horizontal, vertical).then(() => {
      console.info('Succeeded in flipping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to flip pixelmap. code is ${err.code}, message is ${err.message}\`);
    })
  }
}

#### flipSync12+

flipSync(horizontal: boolean, vertical: boolean): void

Flips this image horizontally or vertically, or both. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| horizontal | boolean | Yes | Whether to flip the image horizontally. **true** to flip the image horizontally, **false** otherwise. |
| vertical | boolean | Yes | Whether to flip the image vertically. **true** to flip the image vertically, **false** otherwise. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function FlipSync(pixelMap:image.PixelMap) {
  let horizontal : boolean = true;
  let vertical : boolean = false;
  if (pixelMap != undefined) {
    pixelMap.flipSync(horizontal, vertical);
  }
}

#### crop9+

crop(region: Region, callback: AsyncCallback<void>): void

Crops this image based on a given size. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region, (err: BusinessError) => {
      if (err) {
        console.error(\`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info("Succeeded in cropping pixelmap.");
      }
    })
  }
}

#### crop9+

crop(region: Region): Promise<void>

Crops a PixelMap based on a given size. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Crop(pixelMap:image.PixelMap) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.crop(region).then(() => {
      console.info('Succeeded in cropping pixelmap.');
    }).catch((err: BusinessError) => {
      console.error(\`Failed to crop pixelmap. code is ${err.code}, message is ${err.message}\`);

    });
  }
}

#### cropSync12+

cropSync(region: Region): void

Crops this image based on a given size. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Size of the image after cropping. The value cannot exceed the width or height of the image. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 501 | Resource Unavailable |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function CropSync(pixelMap:image.PixelMap) {
  let region : image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  if (pixelMap != undefined) {
    pixelMap.cropSync(region);
  }
}

#### getColorSpace10+

getColorSpace(): colorSpaceManager.ColorSpaceManager

Obtains the color space of this image.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | Color space obtained. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980101 | The image data is abnormal. |
| 62980103 | The image data is not supported. |
| 62980115 | Invalid image parameter. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function GetColorSpace(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    let csm = pixelMap.getColorSpace();
  }
}

#### setColorSpace10+

setColorSpace(colorSpace: colorSpaceManager.ColorSpaceManager): void

Sets the color space for this image.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | Yes | Color space to set. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980111 | The image source data is incomplete. |
| 62980115 | If the image parameter invalid. |

**Example**

import { colorSpaceManager } from '@kit.ArkGraphics2D';

function SetColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let csm: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    pixelMap.setColorSpace(csm);
  }
}

#### applyColorSpace11+

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager, callback: AsyncCallback<void>): void

Performs color space conversion (CSC) on the image pixel color based on a given color space. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetColorSpace | [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | Yes | Target color space. SRGB, DCI\_P3, DISPLAY\_P3, and ADOBE\_RGB\_1998 are supported. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980104 | Failed to initialize the internal object. |
| 62980108 | Failed to convert the color space. |
| 62980115 | Invalid image parameter. |

**Example**

import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
    try {
      pixelMap.applyColorSpace(targetColorSpace, (error: BusinessError) => {
        if (error) {
          console.error(\`ApplyColorSpace failed. code is ${error.code}, message is ${error.message}\`);
          return;
        } else {
          console.info("Succeeded ApplyColorSpace.");
        }
      });
    } catch (error) {
      console.error(\`Failed to apply color space for pixelmap object, error code is ${error}\`);
      return;
    }
    console.info('Succeeded in applying color space for pixelmap object.');
  }
}

#### applyColorSpace11+

applyColorSpace(targetColorSpace: colorSpaceManager.ColorSpaceManager): Promise<void>

Performs Color Space Converters (CSC) on the image pixel color based on a given color space. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetColorSpace | [colorSpaceManager.ColorSpaceManager](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspacemanager) | Yes | Target color space. SRGB, DCI\_P3, DISPLAY\_P3, and ADOBE\_RGB\_1998 are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980104 | Failed to initialize the internal object. |
| 62980108 | Failed to convert the color space. |
| 62980115 | Invalid image parameter. |

**Example**

import { colorSpaceManager } from '@kit.ArkGraphics2D';
import { BusinessError } from '@kit.BasicServicesKit';

function ApplyColorSpace(pixelMap:image.PixelMap) {
  let colorSpaceName = colorSpaceManager.ColorSpace.SRGB; // The colorSpaceManager.ColorSpace object is supported only on 2-in-1 devices/PCs.
  let targetColorSpace: colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceName);
  if (pixelMap != undefined) {
      pixelMap.applyColorSpace(targetColorSpace).then(() => {
      console.info('Succeeded in applying color space for pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to apply color space for pixelmap object, error code is ${error}\`);
      return;
    });
  }
}

#### toSdr12+

toSdr(): Promise<void>

Converts a PixelMap from the HDR format to the SDR format. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980137 | Invalid image operation. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ToSdr(context: Context) {
  // Replace app.media.startIcon with a local HDR image.
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    pixelmap.toSdr().then(() => {
      let imageInfo = pixelmap.getImageInfoSync();
      console.info("after toSdr ,imageInfo isHdr:" + imageInfo.isHdr);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to set sdr. code is ${err.code}, message is ${err.message}\`);
    });
  } else {
    console.error('Failed to create pixelMap.');
  }
}

#### getMetadata12+

getMetadata(key: HdrMetadataKey): HdrMetadataValue

Obtains the value of the metadata with a given key in this PixelMap.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [HdrMetadataKey](../enums/document.md#hdrmetadatakey12) | Yes | Key of the HDR metadata. |

**Return value**

| Type | Description |
| :-- | :-- |
| [HdrMetadataValue](../types/document.md#hdrmetadatavalue12) | Value of the metadata with the given key. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980173 | The DMA memory does not exist. |
| 62980302 | Memory copy failed. Possibly caused by invalid metadata value. |

**Example**

async function GetMetadata(context: Context) {
  // Replace app.media.startIcon with a local HDR image.
  let img = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id);
  let imageSource = image.createImageSource(img.buffer.slice(0));
  let decodingOptions: image.DecodingOptions = {
    desiredDynamicRange: image.DecodingDynamicRange.AUTO
  };
  let pixelmap = imageSource.createPixelMapSync(decodingOptions);
  if (pixelmap != undefined) {
    console.info('Succeeded in creating pixelMap object.');
    try {
      let staticMetadata = pixelmap.getMetadata(image.HdrMetadataKey.HDR\_STATIC\_METADATA);
      console.info(\`getMetadata:${staticMetadata}\`);
    } catch (e) {
      console.error('pixelmap create failed' + e);
    }
  } else {
    console.error('Failed to create pixelMap.');
  }
}

#### setMetadata12+

setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>

Sets the value for the metadata with a given key in this PixelMap. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | [HdrMetadataKey](../enums/document.md#hdrmetadatakey12) | Yes | Key of the HDR metadata. |
| value | [HdrMetadataValue](../types/document.md#hdrmetadatavalue12) | Yes | Value of the metadata. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980173 | The DMA memory does not exist. |
| 62980302 | Memory copy failed. Possibly caused by invalid metadata value. |

**Example**

For details about how to create a PixelMap with DMA\_ALLOC memory, see [Default Memory Allocation Mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#default-memory-allocation-method).

import { BusinessError } from '@kit.BasicServicesKit';
import {image} from '@kit.ImageKit';

function SetMetadata(pixelMap: image.PixelMap) { // The input parameter pixelMap must be of the DMA\_ALLOC memory type. For details about how to create a PixelMap with DMA\_ALLOC memory, see the preceding link.
  let staticMetadata: image.HdrStaticMetadata = {
    displayPrimariesX: \[1.1, 1.1, 1.1\],
    displayPrimariesY: \[1.2, 1.2, 1.2\],
    whitePointX: 1.1,
    whitePointY: 1.2,
    maxLuminance: 2.1,
    minLuminance: 1.0,
    maxContentLightLevel: 2.1,
    maxFrameAverageLightLevel: 2.1,
  };
  pixelMap.setMetadata(image.HdrMetadataKey.HDR\_STATIC\_METADATA, staticMetadata).then(() => {
    console.info('Succeeded in setting pixelMap metadata.');
  }).catch((error: BusinessError) => {
    console.error("Failed to set the metadata.code ", error);
  })
}

#### setTransferDetached12+

setTransferDetached(detached: boolean): void

Sets whether to detach from the original thread when this PixelMap is transmitted across threads. This API applies to the scenario where the PixelMap needs to be released immediately.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| detached | boolean | Yes | Whether to detach from the original thread. **true** to detach, **false** otherwise. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 501 | Resource Unavailable |

**Example**

import { common } from '@kit.AbilityKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
// Child thread method.
async function loadPixelMap(rawFileDescriptor: number): Promise<PixelMap> {
  // Create an ImageSource instance.
  const imageSource = image.createImageSource(rawFileDescriptor);
  // Create a pixelMap.
  const pixelMap = imageSource.createPixelMapSync();
  // Release the ImageSource instance.
  imageSource.release();
  // Disconnect the reference of the original thread after the cross-thread transfer of the pixelMap is complete.
  pixelMap.setTransferDetached(true);
  // Return the pixelMap to the main thread.
  return pixelMap;
}

@Entry
@Component
struct Demo {
  @State pixelMap: PixelMap | undefined = undefined;
  // Main thread method.
  private loadImageFromThread(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr = context.resourceManager;
    // 'example.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
    resourceMgr.getRawFd('example.jpg').then(rawFileDescriptor => {
      taskpool.execute(loadPixelMap, rawFileDescriptor).then(pixelMap => {
        if (pixelMap) {
          this.pixelMap = pixelMap as PixelMap;
          console.info('Succeeded in creating pixelMap.');
          // The main thread releases the pixelMap. Because setTransferDetached has been called when the child thread returns pixelMap, the pixelMap can be released immediately.
          this.pixelMap.release();
        } else {
          console.error('Failed to create pixelMap.');
        }
      });
    });
  }
  build() {
    // ...
  }
}

#### marshalling10+

marshalling(sequence: rpc.MessageSequence): void

Marshals this PixelMap object and writes it to a MessageSequence object.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequence | [rpc.MessageSequence](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | MessageSequence object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980115 | Invalid image parameter. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**Example**

import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel\_map: image.PixelMap;
  constructor(conPixelMap : image.PixelMap) {
    this.pixel\_map = conPixelMap;
  }
  marshalling(messageSequence : rpc.MessageSequence) {
    this.pixel\_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel: image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap: image.PixelMap) => {
        this.pixel\_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo: image.ImageInfo) => {
          console.info(\`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}\`);
        })
      })
    });
    return true;
  }
}
async function Marshalling() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA\_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap: image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // Implement serialization.
    let parcelable: MySequence = new MySequence(pixelMap);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // Implement deserialization to obtain data through the RPC.
    let ret: MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}

#### unmarshalling10+

unmarshalling(sequence: rpc.MessageSequence): Promise<PixelMap>

Unmarshals a MessageSequence object to obtain a PixelMap object. To create a PixelMap object in synchronous mode, use [createPixelMapFromParcel](../functions/document.md#imagecreatepixelmapfromparcel11).

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequence | [rpc.MessageSequence](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | MessageSequence object that stores the PixelMap information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](#)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980115 | Invalid image parameter. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |

**Example**

import { rpc } from '@kit.IPCKit';

class MySequence implements rpc.Parcelable {
  pixel\_map: image.PixelMap;
  constructor(conPixelMap: image.PixelMap) {
    this.pixel\_map = conPixelMap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel\_map.marshalling(messageSequence);
    console.info('marshalling');
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    image.createPixelMap(new ArrayBuffer(96), {size: { height:4, width: 6}}).then((pixelParcel : image.PixelMap) => {
      pixelParcel.unmarshalling(messageSequence).then(async (pixelMap : image.PixelMap) => {
        this.pixel\_map = pixelMap;
        pixelMap.getImageInfo().then((imageInfo : image.ImageInfo) => {
          console.info(\`unmarshalling information h: ${imageInfo.size.height} w: ${imageInfo.size.width}\`);
        })
      })
    });
    return true;
  }
}
async function Unmarshalling() {
  const color: ArrayBuffer = new ArrayBuffer(96);
  let bufferArr: Uint8Array = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i++) {
    bufferArr\[i\] = 0x80;
  }
  let opts: image.InitializationOptions = {
    editable: true,
    pixelFormat: image.PixelMapFormat.BGRA\_8888,
    size: { height: 4, width: 6 },
    alphaType: image.AlphaType.UNPREMUL
  }
  let pixelMap: image.PixelMap | undefined = undefined;
  await image.createPixelMap(color, opts).then((srcPixelMap : image.PixelMap) => {
    pixelMap = srcPixelMap;
  })
  if (pixelMap != undefined) {
    // Implement serialization.
    let parcelable: MySequence = new MySequence(pixelMap);
    let data : rpc.MessageSequence = rpc.MessageSequence.create();
    data.writeParcelable(parcelable);

    // Implement deserialization to obtain data through the RPC.
    let ret : MySequence = new MySequence(pixelMap);
    data.readParcelable(ret);
  }
}

#### release7+

release(): Promise<void>

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses a promise to return the result.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/x8yUL5ZTTGqNjrseD7Ck-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3B0002B4D38D98382FBFE5C776922025D097CD63E8C3715D85BB810319C4B81)

Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    await pixelMap.release().then(() => {
      console.info('Succeeded in releasing pixelmap object.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to release pixelmap object. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### release7+

release(callback: AsyncCallback<void>): void

Releases this PixelMap instance. After the release, any attempt to access the internal data of this object will fail. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/sAZzJDGTRAKV5l6r94w-Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B572BB10A826F571A28E79B98FBA1F56A4DF978CBC892A9A0B3FA919B138B730)

Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Release(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    pixelMap.release((err: BusinessError) => {
      if (err) {
        console.error(\`Failed to release pixelmap object. code is ${err.code}, message is ${err.message}\`);
        return;
      } else {
        console.info('Succeeded in releasing pixelmap object.');
      }
    })
  }
}

#### convertPixelFormat12+

convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>

Converts between YUV and RGB formats. This API uses a promise to return the result.

Conversion between NV12/NV21 and RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16 and conversion between YCRCB\_P010/YCBCR\_P010 and RGBA1010102 are supported.

Since API version 18, this API can be used for conversion from ASTC\_4x4 to RGBA\_8888.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/1qjIZ6IuTOyewdaooaWqgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D86FC946B5EFA0D5F915BB21327486FC69B91BF9C279795FA2EBDEAD47E625B)

Call this API to convert the format from ASTC\_4x4 to RGBA\_8888 only when you need to access pixels of images in ASTC\_4x4 format. The conversion from ASTC\_4x4 to RGBA\_8888 is slow and is not recommended in other cases.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| targetPixelFormat | [PixelMapFormat](../enums/document.md#pixelmapformat7) | Yes | Target pixel format. Currently, only conversion between NV12/NV21 and RGB888/RGBA8888/RGB565/BGRA8888/RGBAF16, conversion between YCRCB\_P010/YCBCR\_P010 and RGBA1010102, and conversion from ASTC\_4x4 to RGBA\_8888 are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980111 | The image source data is incomplete. |
| 62980115 | Invalid input parameter. |
| 62980178 | Failed to create the pixelmap. |
| 62980274 | The conversion failed |
| 62980276 | The type to be converted is an unsupported target pixel format |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ConvertPixelFormat(pixelMap: image.PixelMap) {
  if (pixelMap != undefined) {
    // Set the target pixel format to NV12.
    let targetPixelFormat = image.PixelMapFormat.NV12;
    pixelMap.convertPixelFormat(targetPixelFormat).then(() => {
      // The pixelMap is converted to the NV12 format.
      console.info('PixelMapFormat convert Succeeded');
    }).catch((error: BusinessError) => {
      // The pixelMap fails to be converted to the NV12 format.
      console.error(\`PixelMapFormat convert Failed. code is ${error.code}, message is ${error.message}\`);
    })
  }
}

#### setMemoryNameSync13+

setMemoryNameSync(name: string): void

Sets a memory name for this PixelMap.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Memory name, which can be set only for a PixelMap with the DMA or ASHMEM memory format. The name length for DMA memory settings should be within the range of 1 to 255 bytes. For ASHMEM memory settings, the name length should be within the range of 1 to 244 bytes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.The length of the input parameter is too long. 2.Parameter verification failed. |
| 501 | Resource unavailable. |
| 62980286 | Memory format not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function SetMemoryNameSync(pixelMap:image.PixelMap) {
  if (pixelMap != undefined) {
    try {
      pixelMap.setMemoryNameSync("PixelMapName Test");
    } catch(e) {
      let error = e as BusinessError;
      console.error(\`setMemoryNameSync error. code is ${error.code}, message is ${error.message}\`);
    }
  }
}

#### getUniqueId22+

getUniqueId(): number

Obtains the unique ID of this PixelMap.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unique ID. The value is a positive integer. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | The PixelMap has been released. |

**Example**

function DemoGetUniqueId(pixelMap: PixelMap) {
  const uniqueId: number = pixelMap.getUniqueId();
}

#### isReleased22+

isReleased(): boolean

Checks whether this PixelMap object is released. If released, any attempt to access the internal data of this object will fail.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/m5ADpxMkQbiOikv4KD4o_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82F99B5DFC65CCBDB359D2FE5E2E0E2D2E609FA309F09ED4543502E3704CBBDF)

Release occurs when an ArkTS object relinquishes control over its associated native object. The memory occupied by the native object is reclaimed only after all managing ArkTS objects have relinquished their control.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for whether the PixelMap object is released. **true** if released; **false** otherwise. |

**Example**

async function DemoIsReleased(pixelMap: PixelMap) { // Unreleased PixelMap.
  pixelMap.isReleased(); // Return false.
  await pixelMap.release();
  pixelMap.isReleased(); // Return true.
}
