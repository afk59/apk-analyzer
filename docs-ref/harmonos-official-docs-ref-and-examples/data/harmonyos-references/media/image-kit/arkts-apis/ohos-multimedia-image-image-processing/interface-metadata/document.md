# Interface (Metadata)

The **Metadata** class provides APIs for storing image metadata. For details about the supported metadata types, see [MetadataType](../enums/document.md#metadatatype13).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/EiN4hL6fQti_SJEHdnOQ8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3613E415BE4068F9250613931BE33467D41AE41FB9CBCB1D46B7A68219297FD1)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { image } from '@kit.ImageKit';

#### getProperties13+

getProperties(key: Array<string>): Promise<Record<string, string | null>>

Obtains the values of properties from the image's metadata. This API uses a promise to return the result.

For details about how to obtain the property values, see [PropertyKey](../enums/document.md#propertykey7), [FragmentMapPropertyKey](../enums/document.md#fragmentmappropertykey13), and [GifPropertyKey](../enums/document.md#gifpropertykey20)

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | Array<string> | Yes | Names of the properties. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Record<string, string | null>> | Promise used to return the property values. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    await metaData.getProperties(\["ImageWidth", "ImageLength"\]).then((data2) => {
      console.info('Get properties ',JSON.stringify(data2));
    }).catch((error: BusinessError) => {
      console.error(\`Get properties failed error.code is ${error.code}, error.message is ${error.message}\`);
    });
  } else {
    console.error('Metadata is null.');
  }
}

#### setProperties13+

setProperties(records: Record<string, string | null>): Promise<void>

Sets the values of properties for the image's metadata. This API uses a promise to return the result.

For details about how to obtain the property values, see [PropertyKey](../enums/document.md#propertykey7), [FragmentMapPropertyKey](../enums/document.md#fragmentmappropertykey13), and [GifPropertyKey](../enums/document.md#gifpropertykey20)

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| records | Record<string, string | null> | Yes | Array of properties and their values. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. If the operation fails, an error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Image Error Codes](../../../error-codes/image-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed; |
| 7600202 | Unsupported metadata. Possible causes: 1. Unsupported metadata type. 2. The metadata type does not match the auxiliary picture type. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function SetProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let setkey: Record<string, string | null> = {
      "ImageWidth": "200",
      "ImageLength": "300"
    };
    await metaData.setProperties(setkey).then(async () => {
      console.info('Set AuxPictureObj properties success.');
    }).catch((error: BusinessError) => {
      console.error(\`Failed to set metadata Properties. code is ${error.code}, message is ${error.message}\`);
    })
  } else {
    console.error('AuxPictureObj metadata is null. ');
  }
}

#### getAllProperties13+

getAllProperties(): Promise<Record<string, string | null>>

Obtains all properties and values from the image's metadata. This API uses a promise to return the result.

For details about how to obtain the property values, see [PropertyKey](../enums/document.md#propertykey7), [FragmentMapPropertyKey](../enums/document.md#fragmentmappropertykey13), and [GifPropertyKey](../enums/document.md#gifpropertykey20)

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Record<string, string | null>> | Promise used to return the values of all properties. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function GetAllProperties(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    await metaData.getAllProperties().then((data2) => {
      const count = Object.keys(data2).length;
      console.info('Metadata have ', count, ' properties');
      console.info(\`Get metadata all properties: ${data2}\`);
    }).catch((error: BusinessError) => {
      console.error(\`Get metadata all properties failed error.code is ${error.code}, error.message is ${error.message}\`);
    });
  } else {
    console.error('Metadata is null.');
  }
}

#### clone13+

clone(): Promise<Metadata>

Clones the metadata. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Metadata](#)\> | Promise used to return the metadata instance. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function Clone(context: Context) {
  const resourceMgr = context.resourceManager;
  const rawFile = await resourceMgr.getRawFileContent("exif.jpg"); // An image containing Exif metadata is required.
  let ops: image.SourceOptions = {
    sourceDensity: 98,
  }
  let imageSource: image.ImageSource = image.createImageSource(rawFile.buffer as ArrayBuffer, ops);
  let commodityPixelMap: image.PixelMap = await imageSource.createPixelMap();
  let pictureObj: image.Picture = image.createPicture(commodityPixelMap);
  let metadataType: image.MetadataType = image.MetadataType.EXIF\_METADATA;
  let metaData: image.Metadata | null = await pictureObj.getMetadata(metadataType);
  if (metaData != null) {
    let new\_metadata: image.Metadata = await metaData.clone();
    new\_metadata.getProperties(\["ImageWidth"\]).then((data1) => {
      console.info(\`Clone new\_metadata and get Properties: ${data1}\`);
    }).catch((err: BusinessError) => {
      console.error(\`Clone new\_metadata failed, error : ${err}\`);
    });
  } else {
    console.error('Metadata is null.');
  }
}
