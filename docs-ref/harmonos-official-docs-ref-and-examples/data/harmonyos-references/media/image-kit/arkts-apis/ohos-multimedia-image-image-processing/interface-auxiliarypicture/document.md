# Interface (AuxiliaryPicture)

The **AuxiliaryPicture** class is used to read or write auxiliary picture data of an image and obtain auxiliary picture information of an image. The supported types of auxiliary pictures can be found in [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13).

Before calling any API in AuxiliaryPicture, you must create an AuxiliaryPicture instance using [image.createAuxiliaryPicture](../functions/document.md#imagecreateauxiliarypicture13) or [getAuxiliaryPicture](../interface-picture/document.md#getauxiliarypicture13) in Picture.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call [release](#release13) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/stfrupf6TdqROfUtiRefXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062431Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10DA5FC7D431EF8D1B629AB336AFFC6E86DFD0BAD464554B242AF12947E419C9)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### writePixelsFromBuffer13+

writePixelsFromBuffer(data: ArrayBuffer): Promise<void>

Reads pixels from an ArrayBuffer and writes the data to this AuxiliaryPicture object. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | ArrayBuffer | Yes | Pixels of the auxiliary picture. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Example**

async function WritePixelsFromBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    let auxBuffer: ArrayBuffer = await auxPictureObj.readPixelsToBuffer();
    await auxPictureObj.writePixelsFromBuffer(auxBuffer);
    console.info('Write pixels from buffer success.');
  } else {
    console.error('AuxPictureObj is null.');
  }
}

#### readPixelsToBuffer13+

readPixelsToBuffer(): Promise<ArrayBuffer>

Reads pixels of this auxiliary picture and writes the data to an ArrayBuffer. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<ArrayBuffer> | Promise used to return the pixels of the auxiliary picture. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function ReadPixelsToBuffer(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(image.AuxiliaryPictureType.GAINMAP);
  if(auxPictureObj != null) {
    await auxPictureObj.readPixelsToBuffer().then((pixelsBuffer: ArrayBuffer) => {
      console.info('Read pixels to buffer success.' );
    }).catch((error: BusinessError) => {
      console.error(\`Read pixels to buffer failed error.code: ${error.code}, error.message: ${error.message}\`);
    });
  } else {
    console.error('AuxPictureObj is null.');
  }
}

#### getType13+

getType(): AuxiliaryPictureType

Obtains the type of this auxiliary picture.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13) | Type of the auxiliary picture. |

**Example**

async function GetAuxiliaryPictureType(auxPictureObj : image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let type: image.AuxiliaryPictureType = auxPictureObj.getType();
    console.info('Success get auxiliary picture type ' +  JSON.stringify(type));
  } else {
    console.error('Failed get auxiliary picture type ');
  }
}

#### setMetadata13+

setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>

Sets the metadata for this auxiliary picture. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| metadataType | [MetadataType](../enums/document.md#metadatatype13) | Yes | Metadata type, which is used to set the corresponding metadata. |
| metadata | [Metadata](../interface-metadata/document.md) | Yes | Metadata object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function SetAuxPictureObjMetadata(exifContext: Context, auxPictureObj: image.AuxiliaryPicture) {
  const exifResourceMgr = exifContext.resourceManager;
  const exifRawFile = await exifResourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let exifOps: image.SourceOptions = {
    sourceDensity: 98,
  }
  let exifImageSource: image.ImageSource = image.createImageSource(exifRawFile.buffer as ArrayBuffer, exifOps);
  let exifCommodityPixelMap: image.PixelMap = await exifImageSource.createPixelMap();
  let exifPictureObj: image.Picture = image.createPicture(exifCommodityPixelMap);
  if (exifPictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    auxPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error(\`Set metadata failed.error.code: ${error.code}, error.message: ${error.message}\`);
    });
  } else {
    console.error('AuxPictureObjMetaData is null');
  }
}

#### getMetadata13+

getMetadata(metadataType: MetadataType): Promise<Metadata>

Obtains the metadata of this auxiliary picture. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| metadataType | [MetadataType](../enums/document.md#metadatatype13) | Yes | Metadata type, which is used to obtain metadata of the corresponding type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Metadata](../interface-metadata/document.md)\> | Promise that returns the metadata. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Example**

async function GetAuxPictureObjMetadata(auxPictureObj: image.AuxiliaryPicture) {
  if (auxPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
    let auxPictureObjMetaData: image.Metadata | null = await auxPictureObj.getMetadata(metadataType);
    if (auxPictureObjMetaData != null) {
      console.info('Get AuxPictureObj Metadata success' );
    } else {
      console.error('Get AuxPictureObj Metadata failed');
    }
  } else {
    console.error('Get AuxPictureObj is null.');
  }
}

#### getAuxiliaryPictureinfo13+

getAuxiliaryPictureInfo(): AuxiliaryPictureInfo

Obtains the auxiliary picture information.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [AuxiliaryPictureInfo](../interfaces-others/document.md#auxiliarypictureinfo13) | Auxiliary picture information. |

**Example**

async function GetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
  if(auxPictureObj != null) {
    let auxinfo: image.AuxiliaryPictureInfo = auxPictureObj.getAuxiliaryPictureInfo();
    console.info('GetAuxiliaryPictureInfo Type: ' + auxinfo.auxiliaryPictureType +
      ' height: ' + auxinfo.size.height + ' width: ' + auxinfo.size.width +
      ' rowStride: ' +  auxinfo.rowStride +  ' pixelFormat: ' + auxinfo.pixelFormat +
      ' colorSpace: ' +  auxinfo.colorSpace);
  } else {
    console.error('Get auxiliary picture information failed');
  }
}

#### setAuxiliaryPictureinfo13+

setAuxiliaryPictureInfo(info: AuxiliaryPictureInfo): void

Sets the auxiliary picture information.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| info | [AuxiliaryPictureInfo](../interfaces-others/document.md#auxiliarypictureinfo13) | Yes | Auxiliary picture information. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Example**

import { colorSpaceManager } from '@kit.ArkGraphics2D';

async function SetAuxiliaryPictureInfo(auxPictureObj: image.AuxiliaryPicture) {
  if(auxPictureObj != null) {
    let colorSpaceName = colorSpaceManager.ColorSpace.SRGB;
    let info: image.AuxiliaryPictureInfo = {
      auxiliaryPictureType: image.AuxiliaryPictureType.GAINMAP,
      size: {height: 100, width: 200},
      pixelFormat: image.PixelMapFormat.RGBA\_8888,
      rowStride: 0,
      colorSpace: colorSpaceManager.create(colorSpaceName),
    };
    auxPictureObj.setAuxiliaryPictureInfo(info);
  }
}

#### release13+

release():void

Releases this AuxiliaryPicture object. No value is returned.

Images occupy a large amount of memory. When you finish using an AuxiliaryPicture instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Example**

async function Release(auxPictureObj: image.AuxiliaryPicture) {
  let funcName = "Release";
  if (auxPictureObj != null) {
    auxPictureObj.release();
    if (auxPictureObj.getType() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
