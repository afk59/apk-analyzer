# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Y3ZEyQCjRcKF-8CC98D-SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60A82A5924583B45459E6CFA1FAEE9D3911E892AEAC80C5D56B6DAE230653BC1)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### image.createPicture13+

createPicture(mainPixelmap : PixelMap): Picture

Creates a Picture object based on a main PixelMap.

Images occupy a large amount of memory. When you finish using a Picture instance, call [release](../interface-picture/document.md#release13) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mainPixelmap | [PixelMap](../interface-pixelmap/document.md) | Yes | Main PixelMap. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Picture](../interface-picture/document.md) | Picture object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |

**Example**

async function CreatePicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }
}

#### image.createPictureFromParcel13+

createPictureFromParcel(sequence: rpc.MessageSequence): Picture

Creates a Picture object from a MessageSequence object.

Images occupy a large amount of memory. When you finish using a Picture instance, call [release](../interface-picture/document.md#release13) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequence | [rpc.MessageSequence](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | MessageSequence object that stores the Picture information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Picture](../interface-picture/document.md) | Picture object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types.3.Parameter verification failed. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**Example**

import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  picture: image.Picture | null = null;
  constructor(conPicture: image.Picture) {
    this.picture = conPicture;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    if(this.picture != null) {
      this.picture.marshalling(messageSequence);
      console.info('Marshalling success !');
      return true;
    } else {
      console.error('Marshalling failed !');
      return false;
    }
  }
  unmarshalling(messageSequence : rpc.MessageSequence) {
    this.picture = image.createPictureFromParcel(messageSequence);
    this.picture.getMainPixelmap().getImageInfo().then((imageInfo : image.ImageInfo) => {
      console.info(\`Unmarshalling to get mainPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Unmarshalling failed error.code: ${error.code} ,error.message: ${error.message}\`);
    });
    return true;
  }
}

async function Marshalling\_UnMarshalling(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("test.jpg");
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  if (pictureObj != null) {
    let parcelable: MySequence = new MySequence(pictureObj);
    let data: rpc.MessageSequence = rpc.MessageSequence.create();
    // Implement serialization.
    data.writeParcelable(parcelable);
    let ret: MySequence = new MySequence(pictureObj);
    // Implement deserialization.
    data.readParcelable(ret);
  } else {
    console.error('PictureObj is null');
  }
}

#### image.createPixelMap8+

createPixelMap(colors: ArrayBuffer, options: InitializationOptions): Promise<PixelMap>

Creates a PixelMap object with the default BGRA\_8888 format and specified pixel properties. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | ArrayBuffer | Yes | 
Buffer for storing the pixel data. It is used to initialize the pixels of the PixelMap. Before initialization, the pixel format in the buffer must be specified by [InitializationOptions](../interfaces-others/document.md#initializationoptions8).srcPixelFormat.

**NOTE**: The length of the buffer required for storing the pixel data is determined by multiplying the width, height, and the number of bytes per pixel.

 |
| options | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | 
Promise used to return the PixelMap object.

If the size of the created PixelMap exceeds that of the original image, the PixelMap size of the original image is returned.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create pixelmap. code is ${error.code}, message is ${error.message}\`);
  })
}

#### image.createPixelMap8+

createPixelMap(colors: ArrayBuffer, options: InitializationOptions, callback: AsyncCallback<PixelMap>): void

Creates a PixelMap object with the default BGRA\_8888 format and specified pixel properties. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | ArrayBuffer | Yes | 
Buffer for storing the pixel data. It is used to initialize the pixels of the PixelMap. Before initialization, the pixel format in the buffer must be specified by [InitializationOptions](../interfaces-others/document.md#initializationoptions8).srcPixelFormat.

**NOTE**: The length of the buffer required for storing the pixel data is determined by multiplying the width, height, and the number of bytes per pixel.

 |
| options | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |
| callback | AsyncCallback<[PixelMap](../interface-pixelmap/document.md)\> | Yes | Callback used to return the result. If the operation is successful, **err** is undefined and **data** is the PixelMap object obtained; otherwise, **err** is an error object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  image.createPixelMap(color, opts, (error: BusinessError, pixelMap: image.PixelMap) => {
    if(error) {
      console.error(\`Failed to create pixelmap. code is ${error.code}, message is ${error.message}\`);
      return;
    } else {
      console.info('Succeeded in creating pixelmap.');
    }
  })
}

#### image.createPixelMapUsingAllocator20+

createPixelMapUsingAllocator(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): Promise<PixelMap>

Creates a PixelMap object with the specified properties and memory type. By default, the BGRA\_8888 format is used to process data. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | ArrayBuffer | Yes | 
Buffer for storing the pixel data. It is used to initialize the pixels of the PixelMap. Before initialization, the pixel format in the buffer must be specified by [InitializationOptions](../interfaces-others/document.md#initializationoptions8).srcPixelFormat.

**NOTE**: The length of the buffer required for storing the pixel data is determined by multiplying the width, height, and the number of bytes per pixel.

 |
| param | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |
| allocatorType | [AllocatorType](../enums/document.md#allocatortype15) | No | 

Memory type for creating the PixelMap. The default memory type is **AllocatorType.AUTO**.

1\. **image.AllocatorType.AUTO**: The following formats are not supported for this memory type: UNKNOWN, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4. For RGBA\_1010102, DMA memory is allocated by default. For other formats (RGB\_565, RGBA\_8888, BGRA\_8888, and RGBAF\_16), DMA memory is allocated if the dimensions exceed 512\*512; otherwise, shared memory is allocated.

2\. **image.AllocatorType.DMA**: The formats RGBA\_1010102, RGB\_565, RGBA\_8888, BGRA\_8888, and RGBAF\_16 support DMA memory types. Other formats do not support DMA memory types.

3\. **image.AllocatorType.SHARED**: The formats UNKNOWN, RGBA\_1010102, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4 do not support shared memory. Other formats support shared memory.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |
| 7600302 | Memory copy failed. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapUseAllocator() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, srcPixelFormat: image.PixelMapFormat.RGBA\_8888, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  image.createPixelMapUsingAllocator(color, opts, image.AllocatorType.AUTO).then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in creating pixelmap.');
  }).catch((error: BusinessError) => {
    console.error("Failed to create pixelmap. code is ", error.code);
  })
}

#### image.createPixelMapFromParcel11+

createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap

Creates a PixelMap object from a MessageSequence object.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequence | [rpc.MessageSequence](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | MessageSequence object that stores the PixelMap information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |
| 62980115 | Invalid input parameter. |
| 62980105 | Failed to get the data. |
| 62980177 | Abnormal API environment. |
| 62980178 | Failed to create the PixelMap. |
| 62980179 | Abnormal buffer size. |
| 62980180 | FD mapping failed. Possible cause: 1. Size and address does not match. 2. Memory map in memalloc failed. |
| 62980246 | Failed to read the PixelMap. |

**Example**

import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MySequence implements rpc.Parcelable {
  pixel\_map: image.PixelMap;
  constructor(conPixelmap: image.PixelMap) {
    this.pixel\_map = conPixelmap;
  }
  marshalling(messageSequence: rpc.MessageSequence) {
    this.pixel\_map.marshalling(messageSequence);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence) {
    try {
      this.pixel\_map = image.createPixelMapFromParcel(messageSequence);
    } catch(e) {
      let error = e as BusinessError;
      console.error(\`createPixelMapFromParcel error. code is ${error.code}, message is ${error.message}\`);
      return false;
    }
    return true;
  }
}
async function CreatePixelMapFromParcel() {
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

    // Obtain the PixelMap object.
    let newPixelmap = ret.pixel\_map;
  }
}

#### image.createPixelMapFromSurface11+

createPixelMapFromSurface(surfaceId: string, region: Region): Promise<PixelMap>

Creates a PixelMap object based on the surface ID and region information. The size of the region is specified by [Region](../interfaces-others/document.md#region8).size. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/m_D0Uo_JSZubjymzfXeffw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CEC734B2A0CE65E71936BB1B43F83DCA35D77D82FEF4B15F86FE3861AB7A1A0)

For foldable devices, during switching between folded and unfolded states, the API call may fail because of the built-in rotation angle of the surface. You need to adjust the width and height to match the rotation angle. You are advised to use [image.createPixelMapFromSurface](#imagecreatepixelmapfromsurface15).

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which can be obtained through the preview component, for example, [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Area of the image to capture. Capture must start from the top-left corner of the screen, so **x** and **y** in **Region** must be **0**, and **Width** and **height** in **Region.size** must be within the range \[1, preview stream width\] and \[1, preview stream height\], respectively. To capture any area, first use [image.createPixelMapFromSurface](#imagecreatepixelmapfromsurface15) to obtain the full screen, and then use [crop](../interface-pixelmap/document.md#crop9) to capture the desired area. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 62980115 | If the image parameter invalid. |
| 62980105 | Failed to get the data. |
| 62980178 | Failed to create the PixelMap. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapFromSurface(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  image.createPixelMapFromSurface(surfaceId, region).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create pixelmap. code is ${error.code}, message is ${error.message}\`);
  });
}

#### image.createPixelMapFromSurfaceSync12+

createPixelMapFromSurfaceSync(surfaceId: string, region: Region): PixelMap

Creates a PixelMap object based on the surface ID and region information. This API returns the result synchronously. The size of the region is specified by [Region](../interfaces-others/document.md#region8).size.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/kIFlqx3LRuW0HxVdEtAdYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68DC678C1BE71FB92D7291A09FB395E5497E7D121BCD19DE3881027B5D79B6A6)

For foldable devices, during switching between folded and unfolded states, the API call may fail because of the built-in rotation angle of the surface. You need to adjust the width and height to match the rotation angle. In such cases, [image.createPixelMapFromSurfaceSync](#imagecreatepixelmapfromsurfacesync15) is recommended.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which can be obtained through the preview component, for example, [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |
| region | [Region](../interfaces-others/document.md#region8) | Yes | Area of the image to capture. Capture must start from the top-left corner of the screen, so **x** and **y** in **Region** must be **0**, and **Width** and **height** in **Region.size** must be within the range \[1, preview stream width\] and \[1, preview stream height\], respectively. To capture any area, first use [image.createPixelMapFromSurfaceSync](#imagecreatepixelmapfromsurfacesync15) to obtain the full screen, and then use [cropSync](../interface-pixelmap/document.md#cropsync12) to capture the desired area. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980105 | Failed to get the data. |
| 62980178 | Failed to create the PixelMap. |

**Example**

async function Demo(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  let pixelMap: image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId, region);
  return pixelMap;
}

#### image.createPixelMapFromSurface15+

createPixelMapFromSurface(surfaceId: string): Promise<PixelMap>

Creates a PixelMap object from a surface ID. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which can be obtained through the preview component, for example, [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980105 | Failed to get the data |
| 62980178 | Failed to create the PixelMap |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapFromSurface(surfaceId: string) {
  image.createPixelMapFromSurface(surfaceId).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to create pixelmap. code is ${error.code}, message is ${error.message}\`);
  });
}

#### image.createPixelMapFromSurfaceSync15+

createPixelMapFromSurfaceSync(surfaceId: string): PixelMap

Creates a PixelMap object from a surface ID. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| surfaceId | string | Yes | Surface ID, which can be obtained through the preview component, for example, [XComponent](../../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980105 | Failed to get the data |
| 62980178 | Failed to create the PixelMap |

**Example**

async function CreatePixelMapFromSurfaceSync(surfaceId: string) {
  let pixelMap : image.PixelMap = image.createPixelMapFromSurfaceSync(surfaceId);
  return pixelMap;
}

#### image.createPixelMapSync12+

createPixelMapSync(colors: ArrayBuffer, options: InitializationOptions): PixelMap

Creates a PixelMap object with the specified properties. By default, the BGRA\_8888 format is used to process data. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | ArrayBuffer | Yes | 
Buffer for storing the pixel data. It is used to initialize the pixels of the PixelMap. Before initialization, the pixel format in the buffer must be specified by [InitializationOptions](../interfaces-others/document.md#initializationoptions8).srcPixelFormat.

**NOTE**: The length of the buffer required for storing the pixel data is determined by multiplying the width, height, and the number of bytes per pixel.

 |
| options | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |

**Example**

function CreatePixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
  return pixelMap;
}

#### image.createPixelMapSync12+

createPixelMapSync(options: InitializationOptions): PixelMap

Creates a PixelMap object with the specified pixel properties. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |

**Example**

function CreatePixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(opts);
  return pixelMap;
}

#### image.createPixelMapUsingAllocatorSync20+

createPixelMapUsingAllocatorSync(colors: ArrayBuffer, param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

Creates a PixelMap object with the specified properties and memory type. By default, the BGRA\_8888 format is used to process data. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colors | ArrayBuffer | Yes | 
Buffer for storing the pixel data. It is used to initialize the pixels of the PixelMap. Before initialization, the pixel format in the buffer must be specified by [InitializationOptions](../interfaces-others/document.md#initializationoptions8).srcPixelFormat.

**NOTE**: The length of the buffer required for storing the pixel data is determined by multiplying the width, height, and the number of bytes per pixel.

 |
| param | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |
| allocatorType | [AllocatorType](../enums/document.md#allocatortype15) | No | 

Memory type for creating the PixelMap. The default memory type is **AllocatorType.AUTO**.

1\. **image.AllocatorType.AUTO**: The following formats are not supported for this memory type: UNKNOWN, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4. For RGBA\_1010102, DMA memory is allocated by default. For other formats (RGB\_565, RGBA\_8888, BGRA\_8888, and RGBAF\_16), DMA memory is allocated if the dimensions exceed 512\*512; otherwise, shared memory is allocated.

2\. **image.AllocatorType.DMA**: The formats RGBA\_1010102, RGB\_565, RGBA\_8888, BGRA\_8888, and RGBAF\_16 support DMA memory types. Other formats do not support DMA memory types.

3\. **image.AllocatorType.SHARED**: The formats UNKNOWN, RGBA\_1010102, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4 do not support shared memory. Other formats support shared memory.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |
| 7600302 | Memory copy failed. |

**Example**

function CreatePixelMapSync() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  let opts: image.InitializationOptions = { editable: true, srcPixelFormat: image.PixelMapFormat.RGBA\_8888, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(color, opts, image.AllocatorType.AUTO);
  return pixelMap;
}

#### image.createPixelMapUsingAllocatorSync20+

createPixelMapUsingAllocatorSync(param: InitializationOptions, allocatorType?: AllocatorType): PixelMap

Creates a PixelMap object with the specified pixel properties. This API returns the result synchronously.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | [InitializationOptions](../interfaces-others/document.md#initializationoptions8) | Yes | Pixel properties, including the alpha type, size, scale mode, pixel format, and editable. |
| allocatorType | [AllocatorType](../enums/document.md#allocatortype15) | No | 
Memory type for creating the PixelMap. The default memory type is **AllocatorType.AUTO**.

1\. **image.AllocatorType.AUTO**: The following formats are not supported for this memory type: UNKNOWN and ASTC\_4x4. For RGBA\_1010102, YCBCR\_P010, and YCRCB\_P010, DMA memory is allocated by default. For other formats (RGB\_565, RGBA\_8888, BGRA\_8888, and RGBAF\_16), DMA memory is allocated if the dimensions exceed 512\*512; otherwise, shared memory is allocated.

2\. **image.AllocatorType.DMA**: The formats RGB\_565, RGBA\_8888, BGRA\_8888, RGBAF\_16, RGBA\_1010102, YCBCR\_P010, and YCRCB\_P010 support DMA memory type. Other formats do not support DMA memory type.

3\. **image.AllocatorType.SHARED**: The formats UNKNOWN, RGBA\_1010102, YCBCR\_P010, YCRCB\_P010, and ASTC\_4x4 do not support shared memory. Other formats support shared memory.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. If the operation fails, an error is thrown. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600201 | Unsupported operation. |
| 7600301 | Memory alloc failed. |

**Example**

function CreatePixelMapSync() {
  let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapUsingAllocatorSync(opts, image.AllocatorType.AUTO);
  return pixelMap;
}

#### image.createPremultipliedPixelMap12+

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

Converts a non-premultiplied alpha of a PixelMap to a premultiplied one and stores the converted data to a target PixelMap. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../interface-pixelmap/document.md) | Yes | Source PixelMap object. |
| dst | [PixelMap](../interface-pixelmap/document.md) | Yes | Target PixelMap object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \* 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr\[i\] = 255;
    bufferArr\[i+1\] = 255;
    bufferArr\[i+2\] = 122;
    bufferArr\[i+3\] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
    if(error) {
      console.error(\`Failed to convert pixelmap, error code is ${error}\`);
      return;
    } else {
      console.info('Succeeded in converting pixelmap.');
    }
  })
}

#### image.createPremultipliedPixelMap12+

createPremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

Converts a non-premultiplied alpha of a PixelMap to a premultiplied one and stores the converted data to a target PixelMap. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../interface-pixelmap/document.md) | Yes | Source PixelMap object. |
| dst | [PixelMap](../interface-pixelmap/document.md) | Yes | Target PixelMap object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \* 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr\[i\] = 255;
    bufferArr\[i+1\] = 255;
    bufferArr\[i+2\] = 122;
    bufferArr\[i+3\] = 122;
  }
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForUnpre);
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForPre);
  image.createPremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
    console.info('Succeeded in converting pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to convert pixelmap, error code is ${error}\`);
  })
}

#### image.createUnpremultipliedPixelMap12+

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void

Converts a premultiplied alpha of a PixelMap to a non-premultiplied one and stores the converted data to a target PixelMap. This API uses an asynchronous callback to return the result.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../interface-pixelmap/document.md) | Yes | Source PixelMap object. |
| dst | [PixelMap](../interface-pixelmap/document.md) | Yes | Target PixelMap object. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed |
| 62980103 | The image data is not supported |
| 62980246 | Failed to read the pixelMap |
| 62980248 | Pixelmap not allow modify |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateUnpremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \* 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr\[i\] = 255;
    bufferArr\[i+1\] = 255;
    bufferArr\[i+2\] = 122;
    bufferArr\[i+3\] = 122;
  }
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForPre);
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForUnpre);
  image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap, (error: BusinessError) => {
    if(error) {
      console.error(\`Failed to convert pixelmap, error code is ${error}\`);
      return;
    } else {
      console.info('Succeeded in converting pixelmap.');
    }
  })
}

#### image.createUnpremultipliedPixelMap12+

createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>

Converts a premultiplied alpha of a PixelMap to a non-premultiplied one and stores the converted data to a target PixelMap. This API returns the result asynchronously through a promise.

Images occupy a large amount of memory. When you finish using a PixelMap instance, call [release](../interface-pixelmap/document.md#release7) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../interface-pixelmap/document.md) | Yes | Source PixelMap object. |
| dst | [PixelMap](../interface-pixelmap/document.md) | Yes | Target PixelMap object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980103 | The image data is not supported. |
| 62980246 | Failed to read the pixelMap. |
| 62980248 | Pixelmap not allow modify. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateUnpremultipliedPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(16); // 16 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \* 4.
  let bufferArr = new Uint8Array(color);
  for (let i = 0; i < bufferArr.length; i += 4) {
    bufferArr\[i\] = 255;
    bufferArr\[i+1\] = 255;
    bufferArr\[i+2\] = 122;
    bufferArr\[i+3\] = 122;
  }
  let optsForPre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.PREMUL}
  let srcPixelmap = image.createPixelMapSync(color, optsForPre);
  let optsForUnpre: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 2, width: 2 } , alphaType: image.AlphaType.UNPREMUL}
  let dstPixelMap = image.createPixelMapSync(optsForUnpre);
  image.createUnpremultipliedPixelMap(srcPixelmap, dstPixelMap).then(() => {
    console.info('Succeeded in converting pixelmap.');
  }).catch((error: BusinessError) => {
    console.error(\`Failed to convert pixelmap, error code is ${error}\`);
  })
}

#### image.createImageSource

createImageSource(uri: string): ImageSource

Creates an ImageSource instance based on a given URI.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | 
Image path. Currently, only the application sandbox path is supported.

The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic12+ (depending on the hardware), [.svg10+](#svg-tags), and .ico11+.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

async function CreateImageSource(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.jpg";
  const imageSourceObj: image.ImageSource = image.createImageSource(path);
}

#### image.createImageSource9+

createImageSource(uri: string, options: SourceOptions): ImageSource

Creates an ImageSource instance based on a given URI.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | 
Image path. Currently, only the application sandbox path is supported.

The following formats are supported: .jpg, .png, .gif, .bmp, .webp, .dng, .heic12+ (depending on the hardware), [.svg10+](#svg-tags), and .ico11+.

 |
| options | [SourceOptions](../interfaces-others/document.md#sourceoptions9) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 'test.png' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const path: string = context.filesDir + "/test.png";
  let imageSourceObj: image.ImageSource = image.createImageSource(path, sourceOptions);
}

#### image.createImageSource7+

createImageSource(fd: number): ImageSource

Creates an ImageSource instance based on a given file descriptor.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  let filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd);
}

#### image.createImageSource9+

createImageSource(fd: number, options: SourceOptions): ImageSource

Creates an ImageSource instance based on a given file descriptor.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor. |
| options | [SourceOptions](../interfaces-others/document.md#sourceoptions9) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';

async function CreateImageSource(context : Context) {
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  const filePath: string = context.filesDir + "/test.jpg";
  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
  const imageSourceObj: image.ImageSource = image.createImageSource(file.fd, sourceOptions);
}

#### image.createImageSource9+

createImageSource(buf: ArrayBuffer): ImageSource

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](#imagecreatepixelmapsync12).

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Array of image buffers. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

async function CreateImageSource() {
  const buf: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height \* width \*4.
  const imageSourceObj: image.ImageSource = image.createImageSource(buf);
}

#### image.createImageSource9+

createImageSource(buf: ArrayBuffer, options: SourceOptions): ImageSource

Creates an ImageSource instance based on buffers. The data passed by **buf** must be undecoded. Do not pass the pixel buffer data such as RBGA and YUV. If you want to create a PixelMap based on the pixel buffer data, call [image.createPixelMapSync](#imagecreatepixelmapsync12).

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Array of image buffers. |
| options | [SourceOptions](../interfaces-others/document.md#sourceoptions9) | Yes | Image properties, including the image pixel density, pixel format, and image size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

async function CreateImageSource() {
  const data: ArrayBuffer = new ArrayBuffer(112);
  let sourceOptions: image.SourceOptions = { sourceDensity: 120 };
  const imageSourceObj: image.ImageSource = image.createImageSource(data, sourceOptions);
}

#### image.createImageSource11+

createImageSource(rawfile: resourceManager.RawFileDescriptor, options?: SourceOptions): ImageSource

Creates an ImageSource instance based on the raw file descriptor of an image resource file.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawfile | [resourceManager.RawFileDescriptor](../../../../../application-framework/localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#rawfiledescriptor9) | Yes | Raw file descriptor of the image resource file. |
| options | [SourceOptions](../interfaces-others/document.md#sourceoptions9) | No | Image properties, including the image pixel density, pixel format, and image size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
  
async function CreateImageSource(context : Context) {
  // Obtain a resource manager.
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 'test.jpg' is only an example. Replace it with the actual one in use. Otherwise, the imageSource instance fails to be created, and subsequent operations cannot be performed.
  resourceMgr.getRawFd('test.jpg').then((rawFileDescriptor: resourceManager.RawFileDescriptor) => {
    const imageSourceObj: image.ImageSource = image.createImageSource(rawFileDescriptor);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get RawFileDescriptor.code is ${error.code}, message is ${error.message}\`);
  })
}

#### image.CreateIncrementalSource9+

CreateIncrementalSource(buf: ArrayBuffer): ImageSource

Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or writing of Exif information.

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

The ImageSource instance created in incremental mode supports the following capabilities (applicable to synchronous, callback, and promise modes):

-   Obtaining image information: Call [getImageInfo](../interface-imagesource/document.md#getimageinfo) to obtain image information by index, or call [getImageInfo](../interface-imagesource/document.md#getimageinfo-1) to directly obtain image information.
-   Obtaining an image property: Call [getImageProperty](../interface-imagesource/document.md#getimageproperty11) to obtain the value of a property with the specified index in an image.
-   Obtaining image properties: Call [getImageProperties](../interface-imagesource/document.md#getimageproperties12) to obtain the values of properties with the given names in an image.
-   Updating incremental data: Call [updateData](../interface-imagesource/document.md#updatedata9).
-   Creating a PixelMap object: Call [createPixelMap](../interface-imagesource/document.md#createpixelmap7) or [createPixelMap](../interface-imagesource/document.md#createpixelmap7-2) to create a PixelMap object based on decoding options; call [createPixelMap](../interface-imagesource/document.md#createpixelmap7-1) to create a PixelMap object based on default parameters.
-   Releasing an ImageSource instance: Call [release](../interface-imagesource/document.md#release).

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Incremental data. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateIncrementalImageSource(context : Context) {
  let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // Obtain the image resource.
  // 'app.media.startIcon' is only an example. Replace it with the actual one in use. Otherwise, the imageArray instance fails to be created, and subsequent operations cannot be performed.
  let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // Image slice.
  let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
  const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength));
  imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
    imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
      let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
      let imageInfo = pixelMap.getImageInfoSync();
      console.info('Succeeded in creating pixelMap');
    }).catch((error : BusinessError) => {
      console.error(\`Failed to updateData error code is ${error.code}, message is ${error.message}\`);
    })
  }).catch((error : BusinessError) => {
    console.error(\`Failed to updateData error code is ${error.code}, message is ${error.message}\`);
  })
}

#### image.CreateIncrementalSource9+

CreateIncrementalSource(buf: ArrayBuffer, options?: SourceOptions): ImageSource

Creates an ImageSource instance in incremental mode based on buffers. Such an instance does not support reading or writing of Exif information.

The capabilities supported by the ImageSource instance created by this API are the same as those supported by the instance created by [CreateIncrementalSource(buf: ArrayBuffer): ImageSource](#imagecreateincrementalsource9).

Images occupy a large amount of memory. When you finish using an ImageSource instance, call [release](../interface-imagesource/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Incremental data. |
| options | [SourceOptions](../interfaces-others/document.md#sourceoptions9) | No | Image properties, including the image pixel density, pixel format, and image size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageSource](../interface-imagesource/document.md) | ImageSource instance. If the operation fails, undefined is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function CreateIncrementalImageSource(context : Context) {
  let imageArray = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id); // Obtain the image resource.
  // 'app.media.startIcon' is only an example. Replace it with the actual one in use. Otherwise, the imageArray instance fails to be created, and subsequent operations cannot be performed.
  let splitBuff1 = imageArray.slice(0, imageArray.byteLength / 2);  // Image slice.
  let splitBuff2 = imageArray.slice(imageArray.byteLength / 2);
  let sourceOptions: image.SourceOptions = { sourceDensity: 120};

  const imageSourceIncrementalSApi: image.ImageSource = image.CreateIncrementalSource(new ArrayBuffer(imageArray.byteLength), sourceOptions);
  imageSourceIncrementalSApi.updateData(splitBuff1, false, 0, splitBuff1.byteLength).then(() => {
    imageSourceIncrementalSApi.updateData(splitBuff2, true, 0, splitBuff2.byteLength).then(() => {
      let pixelMap = imageSourceIncrementalSApi.createPixelMapSync();
      let imageInfo = pixelMap.getImageInfoSync();
      console.info('Succeeded in creating pixelMap');
    }).catch((error : BusinessError) => {
      console.error(\`Failed to updateData error code is ${error.code}, message is ${error.message}\`);
    })
  }).catch((error : BusinessError) => {
    console.error(\`Failed to updateData error code is ${error.code}, message is ${error.message}\`);
  })
}

#### image.getImageSourceSupportedFormats20+

getImageSourceSupportedFormats(): string\[\]

Obtains the supported decoding formats, represented by MIME types.

**System capability**: SystemCapability.Multimedia.Image.ImageSource

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | List of supported decoding formats (MIME types). |

**Example**

async function GetImageSourceSupportedFormats() {
    let formats = image.getImageSourceSupportedFormats();
    console.info('formats:', formats);
}

#### image.createImagePacker

createImagePacker(): ImagePacker

Creates an ImagePacker instance.

Images occupy a large amount of memory. When you finish using an ImagePacker instance, call [release](../interface-imagepacker/document.md#release) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Return value**

| Type | Description |
| :-- | :-- |
| [ImagePacker](../interface-imagepacker/document.md) | ImagePacker instance created. |

**Example**

async function CreateImagePacker() {
  const imagePackerObj: image.ImagePacker = image.createImagePacker();
}

#### image.getImagePackerSupportedFormats20+

getImagePackerSupportedFormats(): string\[\]

Obtains the supported encoding formats, represented by MIME types.

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | List of supported encoding formats (MIME types). |

**Example**

async function GetImagePackerSupportedFormats() {
    let formats = image.getImagePackerSupportedFormats();
    console.info('formats:', formats);
}

#### image.createAuxiliaryPicture13+

createAuxiliaryPicture(buffer: ArrayBuffer, size: Size, type: AuxiliaryPictureType): AuxiliaryPicture

Creates an AuxiliaryPicture instance based on the ArrayBuffer image data, auxiliary picture size, and auxiliary picture type. This API accepts only continuous pixel data in BGRA format and will create an auxiliary picture in RGBA format.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call [release](../interface-auxiliarypicture/document.md#release13) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Image data stored in the buffer. |
| size | [Size](../interfaces-others/document.md#size) | Yes | Size of the auxiliary picture, in px. |
| type | [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13) | Yes | Type of the auxiliary picture. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AuxiliaryPicture](../interface-auxiliarypicture/document.md) | AuxiliaryPicture instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Example**

async function CreateAuxiliaryPicture(context: Context) {
  let funcName = "CreateAuxiliaryPicture";
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let auxBuffer: ArrayBuffer = rawFile.buffer as ArrayBuffer;
  let auxSize: Size = {
    height: 180,
    width: 240
  };
  let auxType: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
  let auxPictureObj: image.AuxiliaryPicture | null = image.createAuxiliaryPicture(auxBuffer, auxSize, auxType);
  if(auxPictureObj != null) {
    let type: image.AuxiliaryPictureType = auxPictureObj.getType();
    console.info(funcName, \`CreateAuxiliaryPicture succeeded this.Aux\_picture.type ${type}\`);
  } else {
    console.error(funcName, 'CreateAuxiliaryPicture failed');
  }
}

#### image.createImageReceiver11+

createImageReceiver(size: Size, format: ImageFormat, capacity: number): ImageReceiver

Creates an ImageReceiver instance by specifying the image size, format, and capacity. The ImageReceiver object acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with [createPreviewOutput](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-cameramanager/document.md#createpreviewoutput).

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call [release](../interface-imagereceiver/document.md#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Size](../interfaces-others/document.md#size) | Yes | Default size of the image. This parameter does not affect the size of the received image. The actual returned size is determined by the producer, for example, the camera. |
| format | [ImageFormat](../enums/document.md#imageformat9) | Yes | Image format, which is a constant of [ImageFormat](../enums/document.md#imageformat9). (Currently, only **ImageFormat:JPEG** is supported. The format actually returned is determined by the producer, for example, camera.) |
| capacity | number | Yes | Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageReceiver](../interface-imagereceiver/document.md) | ImageReceiver instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |

**Example**

let size: image.Size = {
  height: 8192,
  width: 8192
}
let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);

#### image.createImageCreator11+

createImageCreator(size: Size, format: ImageFormat, capacity: number): ImageCreator

Creates an ImageCreator instance by specifying the image size, format, and capacity.

Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](../interface-imagecreator/document.md#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.ImageCreator

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Size](../interfaces-others/document.md#size) | Yes | Default size of the image. |
| format | [ImageFormat](../enums/document.md#imageformat9) | Yes | Image format, for example, YCBCR\_422\_SP or JPEG. |
| capacity | number | Yes | Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageCreator](../interface-imagecreator/document.md) | ImageCreator instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types; |

**Example**

let size: image.Size = {
  height: 8192,
  width: 8192
}
let creator: image.ImageCreator = image.createImageCreator(size, image.ImageFormat.JPEG, 8);

#### image.createImageReceiver(deprecated)

createImageReceiver(width: number, height: number, format: number, capacity: number): ImageReceiver

Creates an ImageReceiver instance by specifying the image width, height, format, and capacity. The ImageReceiver object acts as the receiver and consumer of images. Its parameter properties do not actually affect the received images. The configuration of image properties should be done on the sending side (the producer), such as when creating a camera preview stream with [createPreviewOutput](../../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-cameramanager/document.md#createpreviewoutput).

Images occupy a large amount of memory. When you finish using an ImageReceiver instance, call [release](../interface-imagereceiver/document.md#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/vLe5xq4JQJKr-DoVTR4FPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A551C613CF123B08A545DDCC739931218D8DA41C2055E41FD465CD25135384B2)

This API is supported since API version 9 and is deprecated since API version 11. You are advised to use [createImageReceiver](#imagecreateimagereceiver11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageReceiver

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Default image width, in px. This parameter does not affect the width of the received image. The actual width is determined by the producer, for example, the camera. |
| height | number | Yes | Default image height, in px. This parameter does not affect the height of the received image. The actual height is determined by the producer, for example, the camera. |
| format | number | Yes | Image format, which is a constant of [ImageFormat](../enums/document.md#imageformat9). (Currently, only **ImageFormat:JPEG** is supported. The format actually returned is determined by the producer, for example, camera.) |
| capacity | number | Yes | Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageReceiver](../interface-imagereceiver/document.md) | ImageReceiver instance. |

**Example**

let receiver: image.ImageReceiver = image.createImageReceiver(8192, 8192, image.ImageFormat.JPEG, 8);

#### image.createImageCreator(deprecated)

createImageCreator(width: number, height: number, format: number, capacity: number): ImageCreator

Creates an ImageCreator instance by specifying the image width, height, format, and capacity.

Images occupy a large amount of memory. When you finish using an ImageCreator instance, call [release](../interface-imagecreator/document.md#release9) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/TJJwyOPGRVa198rYt9qvcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C831256EC7728CFE71D62A98BA2116CB81B0B167437AE2DCC7516F4738A8A89)

This API is supported since API version 9 and is deprecated since API version 11. You are advised to use [createImageCreator](#imagecreateimagecreator11) instead.

**System capability**: SystemCapability.Multimedia.Image.ImageCreator

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | Default image width, in px. |
| height | number | Yes | Default image height, in px. |
| format | number | Yes | Image format, for example, YCBCR\_422\_SP or JPEG. |
| capacity | number | Yes | Maximum number of images that can be accessed at the same time. This parameter is used only as an expected value. The actual capacity is determined by the device hardware. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageCreator](../interface-imagecreator/document.md) | ImageCreator instance. |

**Example**

let creator: image.ImageCreator = image.createImageCreator(8192, 8192, image.ImageFormat.JPEG, 8);

#### SVG Tags

The SVG tags are supported since API version 10. The used version is (SVG) 1.1, and the width and height of the SVG tag must be set. An XML declaration can be added to an SVG file and start with **<?xml**. The following tags are supported:

-   a
-   circle
-   clipPath
-   defs
-   ellipse
-   feBlend
-   feColorMatrix
-   feComposite
-   feDiffuseLighting
-   feDisplacementMap
-   feDistantLight
-   feFlood
-   feGaussianBlur
-   feImage
-   feMorphology
-   feOffset
-   fePointLight
-   feSpecularLighting
-   feSpotLight
-   feTurbulence
-   filter
-   g
-   image
-   line
-   linearGradient
-   mask
-   path
-   pattern
-   polygon
-   polyline
-   radialGradient
-   rect
-   stop
-   svg
-   text
-   textPath
-   tspan
-   use
