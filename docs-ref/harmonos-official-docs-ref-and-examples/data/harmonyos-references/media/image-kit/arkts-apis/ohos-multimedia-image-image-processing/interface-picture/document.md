# Interface (Picture)

An image that contains special information can be decoded into a picture object, which generally contains the main picture, auxiliary picture, and metadata. The main picture contains most information about the image and is mainly used to render the image. The auxiliary picture is used to store data related to but different from the main picture, revealing more comprehensive details. The metadata is generally used to store information about the image file. The picture object class is used to read or write picture objects. Before calling any API in Picture, you must use [image.createPicture](../functions/document.md#imagecreatepicture13) to create a Picture object.

Images occupy a large amount of memory. When you finish using a Picture instance, call [release](#release13) to free the memory promptly. Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/uKatSdh9SnS9TcJEK264dQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=938CFAF110927D328ACB37914FA6D1688D55EB833C7CC4C2E07423CCCB458FD4)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### getMainPixelmap13+

getMainPixelmap(): PixelMap

Obtains the PixelMap object of the main picture. This API returns the result synchronously.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | PixelMap object. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetMainPixelmap(pictureObj : image.Picture) {
  let funcName = "getMainPixelmap";
  if (pictureObj != null) {
    let mainPixelmap: image.PixelMap = pictureObj.getMainPixelmap();
    if (mainPixelmap != null) {
      mainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info('GetMainPixelmap information height:' + imageInfo.size.height + ' width:' + imageInfo.size.width);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, \`Failed error.code: ${error.code} ,error.message: ${error.message}\`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
}

#### getHdrComposedPixelmap13+

getHdrComposedPixelmap(): Promise<PixelMap>

Generates a High Dynamic Range (HDR) image and obtains its PixelMap object. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PixelMap](../interface-pixelmap/document.md)\> | Promise used to return the PixelMap object. |

**Error codes**

For details about the error codes, see [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7600901 | Inner unknown error. Please check the logs for detailed information. |
| 7600201 | Unsupported operation. e.g.,1. The picture does not has a gainmap. 2. MainPixelMap's allocator type is not DMA. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetHdrComposedPixelmap(pictureObj : image.Picture) {
  let funcName = "getHdrComposedPixelmap";
  if (pictureObj != null) { // An HDR image is contained.
    let hdrComposedPixelmap: image.PixelMap = await pictureObj.getHdrComposedPixelmap();
    if (hdrComposedPixelmap != null) {
      hdrComposedPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(\`GetHdrComposedPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}\`);
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, \`Failed error.code: ${error.code} ,error.message: ${error.message}\`);
      });
    }
  } else {
    console.error('PictureObj is null');
  }
}

#### getGainmapPixelmap13+

getGainmapPixelmap(): PixelMap | null

Obtains the PixelMap object of the gain map.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelMap](../interface-pixelmap/document.md) | null | PixelMap object obtained. If there is no PixelMap object, null is returned. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetGainmapPixelmap(pictureObj : image.Picture) {
  let funcName = "getGainmapPixelmap";
  if (pictureObj != null) { // A gain map is contained.
    let gainPixelmap: image.PixelMap | null = pictureObj.getGainmapPixelmap();
    if (gainPixelmap != null) {
      gainPixelmap.getImageInfo().then((imageInfo: image.ImageInfo) => {
        if (imageInfo != null) {
          console.info(\`GetGainmapPixelmap information height:${imageInfo.size.height} width:${imageInfo.size.width}\`);
        } else {
          console.error('GainPixelmap is null');
        }
      }).catch((error: BusinessError) => {
        console.error(funcName, \`Failed error.code: ${error.code} ,error.message: ${error.message}\`);
      });
    } else {
      console.info('GainPixelmap is null');
    }
  } else {
    console.error('PictureObj is null');
  }
}

#### setAuxiliaryPicture13+

setAuxiliaryPicture(type: AuxiliaryPictureType, auxiliaryPicture: AuxiliaryPicture): void

Sets an auxiliary picture.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13) | Yes | Type of the auxiliary picture. |
| auxiliaryPicture | [AuxiliaryPicture](../interface-auxiliarypicture/document.md) | Yes | AuxiliaryPicture object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Example**

async function SetAuxiliaryPicture(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("hdr.jpg"); // An HDR-compatible image is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let pixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(pixelMap);
  if (pictureObj != null) {
    console.info('Create picture succeeded');
  } else {
    console.error('Create picture failed');
  }

  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
    if (auxPictureObj != null) {
      pictureObj.setAuxiliaryPicture(type, auxPictureObj);
    }
  }
}

#### getAuxiliaryPicture13+

getAuxiliaryPicture(type: AuxiliaryPictureType): AuxiliaryPicture | null

Obtains an auxiliary picture by type.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13) | Yes | Type of the auxiliary picture. |

**Return value**

| Type | Description |
| :-- | :-- |
| [AuxiliaryPicture](../interface-auxiliarypicture/document.md) | null | AuxiliaryPicture object. If there is no AuxiliaryPicture object, null is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |

**Example**

async function GetAuxiliaryPicture(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let type: image.AuxiliaryPictureType = image.AuxiliaryPictureType.GAINMAP;
    let auxPictureObj: image.AuxiliaryPicture | null = pictureObj.getAuxiliaryPicture(type);
  }
}

#### setMetadata13+

setMetadata(metadataType: MetadataType, metadata: Metadata): Promise<void>

Sets the metadata for this Picture object. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| metadataType | [MetadataType](../enums/document.md#metadatatype13) | Yes | Metadata type. |
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

async function SetPictureObjMetadata(exifContext: Context) {
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

  if (exifPictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
    let exifMetaData: image.Metadata = await exifPictureObj.getMetadata(metadataType);
    exifPictureObj.setMetadata(metadataType, exifMetaData).then(() => {
      console.info('Set metadata success');
    }).catch((error: BusinessError) => {
      console.error('Failed to set metadata. error.code: ' +JSON.stringify(error.code) + ' ,error.message:' + JSON.stringify(error.message));
    });
  } else {
    console.error('exifPictureOb is null');
  }
}

#### getMetadata13+

getMetadata(metadataType: MetadataType): Promise<Metadata>

Obtains the metadata of this Picture object. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| metadataType | [MetadataType](../enums/document.md#metadatatype13) | Yes | Metadata type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Metadata](../interface-metadata/document.md)\> | Promise used to return the metadata. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Example**

async function GetPictureObjMetadataProperties(pictureObj : image.Picture) {
  if (pictureObj != null) {
    let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
    let pictureObjMetaData: image.Metadata = await pictureObj.getMetadata(metadataType);
    if (pictureObjMetaData != null) {
      console.info('get picture metadata success');
    } else {
      console.error('get picture metadata is failed');
    }
  } else {
    console.error(" pictureObj is null");
  }
}

#### marshalling13+

marshalling(sequence: rpc.MessageSequence): void

Marshals this Picture object and writes it to a MessageSequence object.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequence | [rpc.MessageSequence](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#messagesequence9) | Yes | MessageSequence object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 62980097 | IPC error. Possible cause: 1.IPC communication failed. 2. Image upload exception. 3. Decode process exception. 4. Insufficient memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

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

async function Marshalling\_UnMarshalling(pictureObj : image.Picture) {
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

#### release13+

release(): void

Releases this Picture object.

Images occupy a large amount of memory. When you finish using a Picture instance, call this API to free the memory promptly.

Before releasing the instance, ensure that all asynchronous operations associated with the instance have finished and the instance is no longer needed.

**System capability**: SystemCapability.Multimedia.Image.Core

**Example**

async function Release(pictureObj : image.Picture) {
  let funcName = "Release";
  if (pictureObj != null) {
    pictureObj.release();
    if (pictureObj.getMainPixelmap() == null) {
      console.info(funcName, 'Success !');
    } else {
      console.error(funcName, 'Failed !');
    }
  } else {
    console.error('PictureObj is null');
  }
}
