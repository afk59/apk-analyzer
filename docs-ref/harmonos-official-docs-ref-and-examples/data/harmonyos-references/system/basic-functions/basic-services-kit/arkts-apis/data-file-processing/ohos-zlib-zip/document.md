# @ohos.zlib (Zip)

The **Zip** module provides APIs for file compression and decompression.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/JGayefPiSbqRPyQzVN2vmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A71A73CBF93906A23CF6FC9764ADB776DE7F4BF15D00849292BC4D6AEA16F667)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { zlib } from '@kit.BasicServicesKit';

#### zlib.zipFile(deprecated)

zipFile(inFile: string, outFile: string, options: Options): Promise<void>

Zips a file. The execution result is returned after the compression is complete. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/6zadpTpkR9m9RYnrTm381w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A8DEA882884910C026C16BEBA1653AACA4920CED28C922CB67D6C2DF7B13B7E)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [zlib.compressFile](#zlibcompressfile9) instead.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the folder or file to zip. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |
| outFile | string | Yes | Path of the zipped file. The file name extension is .zip. |
| options | [Options](#options) | Yes | Optional parameters for the zip operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  memLevel: zlib.MemLevel.MEM\_LEVEL\_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY
};

zlib.zipFile(inFile, outFile, options).then((data: void) => {
  console.info('zipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
});

#### zlib.unzipFile(deprecated)

unzipFile(inFile:string, outFile:string, options: Options): Promise<void>

Unzips a file. The execution result is returned after the decompression is complete. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/PnmQUcIdQRquCWUZxHbnyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F26B40C128672373401EE8C68CF1151F7DB2EFE468F716CC62FCEFC36BED93A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [zlib.decompressFile](#zlibdecompressfile9) instead.

The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise, the error code -1 is returned.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the file to unzip. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If the.zip file to be unzipped contains Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed after unzipping. |
| outFile | string | Yes | Path of the unzipped file. |
| options | [Options](#options) | Yes | Optional parameters for the unzip operation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFile = '/data/storage/el2/base/temp/xxx';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  memLevel: zlib.MemLevel.MEM\_LEVEL\_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY
};

zlib.unzipFile(inFile, outFile, options).then((data: void) => {
  console.info('unzipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
})

#### zlib.compressFile9+

compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

Compresses a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/dODZRsLhTmKTMT2R7J4I_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B76F13970467F73BF272AE4F4AB8BDCED7F5DD636768C758C38A9BC7BC02826)

To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the folder or file to compress. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). The folder to compress cannot be empty. Otherwise, an error will be reported when [decompressFile](#zlibdecompressfile9) is used to decompress the folder. |
| outFile | string | Yes | Path of the compressed file. When multiple threads compress files at the same time, the values of **outFile** must be different. |
| options | [Options](#options) | Yes | Compression parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **null** is returned; otherwise, a specific error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  memLevel: zlib.MemLevel.MEM\_LEVEL\_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY
};

try {
  zlib.compressFile(inFile, outFile, options, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(\`compressFile errData is errCode:${errData.code}  message:${errData.message}\`);
    } else {
      console.info(\`compressFile success.\`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`compressFile errData is errCode:${code}  message:${message}\`);
}

#### zlib.compressFile9+

compressFile(inFile: string, outFile: string, options: Options): Promise<void>

Compresses a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/IJGdfKzNThKVJlMGSg1yBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=015BE645F2C179AC2E66A335081613C5A5006F76B01B91AB64A1BA024D08A548)

To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the folder or file to compress. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). The folder to compress cannot be empty. Otherwise, an error will be reported when [decompressFile](#zlibdecompressfile9) is used to decompress the folder. |
| outFile | string | Yes | Path of the compressed file. When multiple threads compress files at the same time, the values of **outFile** must be different. |
| options | [Options](#options) | Yes | Compression parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  memLevel: zlib.MemLevel.MEM\_LEVEL\_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY
};

try {
  zlib.compressFile(inFile, outFile, options).then((data: void) => {
    console.info('compressFile success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`errData is errCode:${code}  message:${message}\`);
}

#### zlib.decompressFile9+

decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void

Decompresses a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/rK8TX79oQ8i-SJJ8hD6r2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B8FF30C3C6CC8575DD50F1746BF92132BE8C77BDC822821B20E9636D1087A47)

To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.

The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise, the error code 900003 is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the file to decompress. The file name extension must be .zip. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If the.zip file to be unzipped contains Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed after unzipping. |
| outFile | string | Yes | Path of the decompressed file. The path must exist in the system. Otherwise, the decompression fails. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If a file or folder with the same name already exists in the path, they will be overwritten. When multiple threads decompress files at the same time, the values of **outFile** must be different. |
| options | [Options](#options) | Yes | Decompression parameters. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **null** is returned; otherwise, a specific error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  parallel: zlib.ParallelStrategy.PARALLEL\_STRATEGY\_PARALLEL\_DECOMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(\`decompressFile errData is errCode:${errData.code}  message:${errData.message}\`);
    } else {
      console.info(\`decompressFile success.\`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`decompressFile errData is errCode:${code}  message:${message}\`);
}

#### zlib.decompressFile9+

decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>

Decompresses a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/CyXlJ3sxQfK87WwZAuEtjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=319FEFB4000AD2D4821B99BED58AECAF5F9C8880C023C17E06AB8A5A5E744984)

To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.

The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise, the error code 900003 is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the file to decompress. The file name extension must be .zip. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If the.zip file to be unzipped contains Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed after unzipping. |
| outFile | string | Yes | Path of the decompressed file. The path must exist in the system. Otherwise, the decompression fails. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If a file or folder with the same name already exists in the path, they will be overwritten. When multiple threads decompress files at the same time, the values of **outFile** must be different. |
| options | [Options](#options) | No | Decompression parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION
};

try {
  zlib.decompressFile(inFile, outFileDir, options).then((data: void) => {
    console.info('decompressFile success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`errData is errCode:${code}  message:${message}\`);
}

#### zlib.decompressFile10+

decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void

Decompresses a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/corT1Z1PR7qqrZz0NhYcZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE2ED8E9E1FF18765DE4B77206E573E2DD54BF12E43A86D050363D35EC0AAFFA)

To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.

The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise, the error code 900003 is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFile | string | Yes | Path of the file to decompress. The file name extension must be .zip. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If the.zip file to be unzipped contains Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed after unzipping. |
| outFile | string | Yes | Path of the decompressed file. The path must exist in the system. Otherwise, the decompression fails. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). If a file or folder with the same name already exists in the path, they will be overwritten. When multiple threads decompress files at the same time, the values of **outFile** must be different. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **null** is returned; otherwise, a specific error code is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFileDir = '/data/storage/el2/base/temp';

try {
  zlib.decompressFile(inFile, outFileDir, (errData: BusinessError) => {
    if (errData !== null) {
      console.error(\`decompressFile failed. code is ${errData.code}, message is ${errData.message}\`);
    } else {
      console.info(\`decompressFile success.\`);
    }
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`decompressFile failed. code is ${code}, message is ${message}\`);
}

#### zlib.getOriginalSize12+

getOriginalSize(compressedFile: string): Promise<number>

Obtains the original size of a compressed file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| compressedFile | string | Yes | Specifies the path of the compressed file. Only .zip files are supported. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise object, which returns the original size of the compressed file, in bytes. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | The parameter check failed. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900003 | The input source file is not in ZIP format or is damaged. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let compressedFile = '/data/storage/el2/base/temp/test.zip';

try {
  zlib.getOriginalSize(compressedFile).then((data: number) => {
    console.info(\`getOriginalSize success. getOriginalSize: ${data}\`);
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`errData is errCode:${code}  message:${message}\`);
}

#### zlib.compressFiles12+

compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>

Compresses multiple specified files. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inFiles | Array<string> | Yes | Path of the folder or file to compress. The path must be an application sandbox path, which can be obtained from the context. For details about the context, see [FA Model](../../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) and [Stage Model](../../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md). The folder to compress cannot be empty. Otherwise, an error will be reported when [decompressFile](#zlibdecompressfile9) is used to decompress the folder. |
| outFile | string | Yes | Path of the compressed file. When multiple threads compress files at the same time, the values of **outFile** must be different. |
| options | [Options](#options) | Yes | Compression parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 900001 | The input source file is invalid. |
| 900002 | The input destination file is invalid. |

**Example**

// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let pathDir = 'data/storage/el2/base/temp/xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
  memLevel: zlib.MemLevel.MEM\_LEVEL\_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY
};

try {
  zlib.compressFiles(\[inFile, pathDir\], outFile, options).then((data: void) => {
    console.info('compressFiles success. data: ' + JSON.stringify(data));
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(\`errData is errCode:${code}  message:${message}\`);
}

#### zlib.createChecksum12+

createChecksum(): Promise<Checksum>

Creates this checksum object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Checksum](#checksum12)\> | Promise used to return the created checksum object. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

zlib.createChecksum().then((data) => {
  console.info('createChecksum success');
})

#### zlib.createChecksumSync12+

createChecksumSync(): Checksum

Creates this checksum object. A checksum instance is returned upon a success.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| [Checksum](#checksum12) | Checksum object instance. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

#### Checksum12+

Checksum object.

#### \[h2\]adler3212+

adler32(adler: number, buf: ArrayBuffer): Promise<number>

Calculates the Adler-32 checksum. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| adler | number | Yes | Initial value of the Adler-32 checksum. |
| buf | ArrayBuffer | Yes | Data buffer for calculating the checksum. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the calculated Adler-32 checksum. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data\[i\] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.adler32(0, arrayBufferIn).then(data => {
  console.info('adler32 success', data);
})

#### \[h2\]adler32Combine12+

adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>

Combines two Adler-32 checksums. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| adler1 | number | Yes | The first Adler-32 checksum to be combined. |
| adler2 | number | Yes | The second Adler-32 checksum to be combined. |
| len2 | number | Yes | Length of the data block of the second Adler-32 checksum. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the combined Adler-32 checksum. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data\[i\] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let adler1 = 0;
  let adler2 = 1;
  await checksum.adler32(0, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler1 = data;
  })
  await checksum.adler32(1, arrayBufferIn).then(data => {
    console.info('adler32 success', data);
    adler2 = data;
  })
  await checksum.adler32Combine(adler1, adler2, 12).then((data) => {
    console.info('adler32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]crc3212+

crc32(crc: number, buf: ArrayBuffer): Promise<number>

Updates a CRC-32 checksum. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| crc | number | Yes | Initial value of the CRC-32 checksum. |
| buf | ArrayBuffer | Yes | Data buffer for calculating the checksum. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the updated CRC-32 checksum. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data\[i\] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc32(0, arrayBufferIn).then((data) => {
  console.info('crc32 success', data);
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]crc32Combine12+

crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>

Combines two CRC-32 checksums. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| crc1 | number | Yes | The first CRC-32 checksum to be combined. |
| crc2 | number | Yes | The second CRC-32 checksum to be combined. |
| len2 | number | Yes | Indicates the length of the second data block checked by CRC-32 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the combined CRC-32 checksum. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(12);
  let data = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    data\[i\] = str.charCodeAt(i);
  }
  let checksum = zlib.createChecksumSync()
  let crc1 = 0;
  let crc2 = 1;
  await checksum.crc32(0, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc1 = data;
  })
  await checksum.crc32(1, arrayBufferIn).then(data => {
    console.info('crc32 success', data);
    crc2 = data;
  })
  await checksum.crc32Combine(crc1, crc2, 12).then((data) => {
    console.info('crc32Combine success', data);
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]crc6412+

crc64(crc: number, buf: ArrayBuffer): Promise<number>

Updates a CRC-64 checksum. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| crc | number | Yes | Initial value of the CRC-64 checksum. |
| buf | ArrayBuffer | Yes | Data buffer for calculating the checksum. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the updated CRC-64 checksum. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(12);
let data = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  data\[i\] = str.charCodeAt(i);
}

let checksum = zlib.createChecksumSync()

checksum.crc64(0, arrayBufferIn).then((data) => {
  console.info('crc64 success', data);
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]getCrcTable12+

getCrcTable(): Promise<Array<number>>

Obtains this CRC-32 checksum table. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the CRC-32 checksum table. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrcTable().then((data) => {
  console.info('getCrcTable success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]getCrc64Table12+

getCrc64Table(): Promise<Array<number>>

Obtains this CRC-64 checksum table. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the CRC-64 checksum table. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()

checksum.getCrc64Table().then((data) => {
  console.info('getCrc64Table success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### zlib.createZip12+

createZip(): Promise<Zip>

Creates this **Zip** instance. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Zip](#zip12)\> | Promise used to return the **Zip** instance created. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

zlib.createZip().then(data => {
  console.info('createZip success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### zlib.createZipSync12+

createZipSync(): Zip

Creates this **Zip** instance. A **Zip** instance is returned upon a success.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| [Zip](#zip12) | The **Zip** instance created. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

#### Zip12+

Defines the **Zip** instance. It provides APIs to zip or unzip data in Zlib, Deflate, or Gzip format.

#### \[h2\]getZStream12+

getZStream(): Promise<ZStream>

Obtains this stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ZStream](#zstream12)\> | Promise used to return the **ZStream** object. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.getZStream().then(data => {
  console.info('getZStream success');
})

#### \[h2\]zlibVersion12+

zlibVersion(): Promise<string>

Obtains the version information of this zlib library connected. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the version of the current zlib library. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.zlibVersion().then((data) => {
  console.info('zlibVersion success')
})

#### \[h2\]zlibCompileFlags12+

zlibCompileFlags(): Promise<number>

Returns the flags indicating compile-time options. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the flags indicating compile-time options. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();

zip.zlibCompileFlags().then((data) => {
  console.info('zlibCompileFlags success')
})

#### \[h2\]compress12+

compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

Compresses the source buffer into the destination buffer. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dest | ArrayBuffer | Yes | Destination buffer. |
| source | ArrayBuffer | Yes | Source buffer. |
| sourceLen | number | No | Length of the source data. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ZipOutputInfo](#zipoutputinfo12)\> | Promise used to return the result status and the total size of the destination buffer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { util } from '@kit.ArkTS';
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world! Hello, world!';
const enc = util.TextEncoder.create('utf-8');
const u8 = enc.encodeInto(str);
const arrayBufferIn = u8.buffer.slice(u8.byteOffset, u8.byteOffset + u8.byteLength);

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.compress(arrayBufferOut, arrayBufferIn, 20).then((data) => {
  console.info('compress success:');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]compress212+

compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number): Promise<ZipOutputInfo>

Compresses the source buffer into the destination buffer. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dest | ArrayBuffer | Yes | Destination buffer. |
| source | ArrayBuffer | Yes | Source buffer. |
| level | CompressLevel | Yes | For details, see [CompressLevel](#compresslevel). |
| sourceLen | number | No | Length of the source data. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ZipOutputInfo](#zipoutputinfo12)\> | Promise used to return the result status and the total size of the destination buffer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { util } from '@kit.ArkTS';
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world! Hello, world!';
const enc = util.TextEncoder.create('utf-8');
const u8 = enc.encodeInto(str);
const arrayBufferIn = u8.buffer.slice(u8.byteOffset, u8.byteOffset + u8.byteLength);

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
  console.info('compress2 success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]uncompress12+

uncompress(dest:ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>

Decompresses the compressed data into the raw data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dest | ArrayBuffer | Yes | Destination buffer. |
| source | ArrayBuffer | Yes | Source buffer. |
| sourceLen | number | No | Length of the source data. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ZipOutputInfo](#zipoutputinfo12)\> | Promise used to return the result status and the total size of the destination buffer. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.compress(arrayBufferOut, arrayBufferIn, 12).then((data) => {
    console.info('compress success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.uncompress(arrayBufferIn, arrayBufferOut, 20).then((data) => {
    console.info('uncompress success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]uncompress212+

uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>

Decompresses the compressed data into the raw data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dest | ArrayBuffer | Yes | Destination buffer. |
| source | ArrayBuffer | Yes | Source buffer. |
| sourceLen | number | No | Length of the source data. The default value is **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DecompressionOutputInfo](#decompressionoutputinfo12)\> | Promise used to return the result status, total size of the destination buffer, and the length of the source data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.compress2(arrayBufferOut, arrayBufferIn, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('compress2 success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.uncompress2(arrayBufferIn, arrayBufferOut, 20).then((data) => {
    console.info('uncompress2 success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]compressBound12+

compressBound(sourceLen: number): Promise<number>

Calculates the maximum size of the compressed data to be returned. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sourceLen | number | Yes | Length of the source data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum size of the compressed data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray\[i\] = str.charCodeAt(i)
}

let zip = zlib.createZipSync();

zip.compressBound(str.length).then((data) => {
  console.info('compressBound success')
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]inflateValidate12+

inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>

Validates the checksum inside the compression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| check | number | Yes | Expected checksum. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateValidate({ availableIn: 1 }, 1).then(data => {
    console.info('inflateValidate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateSyncPoint12+

inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>

Finds the synchronization point of a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateSyncPoint({ availableIn: 1 }).then(data => {
    console.info('inflateSyncPoint success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateSync12+

inflateSync(strm: ZStream): Promise<ReturnStatus>

Skips invalid compressed data until a possible complete refresh point is found. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello, hello!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.deflateInit({}, zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflate({ nextIn: arrayBufferIn, availableIn: 3, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FULL\_FLUSH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflate({ availableIn: 11 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateEnd({}).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  try {
    await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 2 }).then(data => {
      console.info('inflateInit2 success')
    })
  } catch (errData) {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  }
  await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO\_FLUSH).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateSync({ availableIn: 26 }).then(data => {
    console.info('inflateSync success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateResetKeep12+

inflateResetKeep(strm: ZStream): Promise<ReturnStatus>

Resets the state of the decompression stream to retain the allocated Huffman tree and preset dictionary. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateResetKeep({ availableIn: 1 }).then(data => {
    console.info('inflateResetKeep success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateSetDictionary12+

inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

Initializes the dictionary content of a decompression stream based on the given dictionary data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| dictionary | ArrayBuffer | Yes | Dictionary data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello, hello!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  let dictionary = 'hello'
  let dictionarybuf = new ArrayBuffer(dictionary.length);
  let dictionarybufdata = new Uint8Array(dictionarybuf);
  for (let i = 0, j = dictionary.length; i < j; i++) {
    dictionarybufdata\[i\] = str.charCodeAt(i);
  }
  await zip.deflateInit({}, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_COMPRESSION).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflateSetDictionary({}, dictionarybuf).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflate({ nextIn: arrayBufferIn, availableIn: 14, nextOut: arrayBufferOut, availableOut: 100 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflateEnd({}).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  try {
    await zip.inflateInit({ nextIn: arrayBufferOut, availableIn: 100 }).then(data => {
      console.info('inflateInit success')
    })
  } catch (errData) {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  }
  await zip.inflate({ nextOut: arrayBufferIn, availableOut: 28 }, zlib.CompressFlushMode.NO\_FLUSH).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.inflateSetDictionary({}, dictionarybuf).then((data) => {
    console.info('inflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
}

#### \[h2\]inflateReset212+

inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

Resets the status of the specified decompression stream and updates the window size to start a new decompression operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| windowBits | number | Yes | 
Memory window size. The value is restricted in certain range based on the data formats. The options are as follows:

Zlib: \[1, 15\]

Gzip: (15, +∞)

Raw Deflate: \[-15, -1\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateReset2({ availableOut: 8 }, 15).then(data => {
    console.info('inflateReset2 success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateReset12+

inflateReset(strm: ZStream): Promise<ReturnStatus>

Resets the status of the specified decompression stream to the initial state to start a new decompression operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateReset({ availableIn: 1, availableOut: 8 }).then(data => {
    console.info('inflateReset success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflatePrime12+

inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

Sets the initial number of bits and bit value in the specified decompression stream to pre-fill the bit buffer at the beginning of the decompression stream to correctly process the data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| bits | number | Yes | Number of bits to be written to the bit buffer. |
| value | number | Yes | Bit value used to fill the bit buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflatePrime({ nextOut: arrayBufferOut }, 5, 2).then(data => {
    console.info('inflatePrime success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateMark12+

inflateMark(strm: ZStream): Promise<number>

Marks the location of the input data for random access. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the current location. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateMark({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }).then(data => {
    console.info('inflateMark success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateInit212+

inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>

Initializes a decompression stream with the specified **windowBits**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| windowBits | number | Yes | 
Memory window size. The value is restricted in certain range based on the data formats. The options are as follows:

Zlib: \[1, 15\]

Gzip: (15, +∞)

Raw Deflate: \[-15, -1\]

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray\[i\] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
).then(data => {
  console.info('inflateInit2 success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]inflateInit12+

inflateInit(strm: ZStream): Promise<ReturnStatus>

Initializes a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

let str = 'hello world!';
let arrayBufferIn = new ArrayBuffer(str.length);
let byteArray = new Uint8Array(arrayBufferIn);

for (let i = 0, j = str.length; i < j; i++) {
  byteArray\[i\] = str.charCodeAt(i)
}

let arrayBufferOut = new ArrayBuffer(100);
let zip = zlib.createZipSync();

zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
).then(data => {
  console.info('inflateInit success');
}).catch((errData: BusinessError) => {
  console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
})

#### \[h2\]inflateGetHeader12+

inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>

Obtains the header information of a gzip file before decompressing data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| header | [GzHeader](#gzheader12) | Yes | Header information of a gzip file extracted from the compressed data stream. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
  ).then(data => {
    console.info('inflateInit2 success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateGetHeader({ availableIn: 1, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then(data => {
    console.info('inflateGetHeader success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateGetDictionary12+

inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

Obtains the content and length of the decompression dictionary used in a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| dictionary | ArrayBuffer | Yes | Receives the actual contents of the decompression dictionary. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DictionaryOutputInfo](#dictionaryoutputinfo12)\> | Promise used to return the result status and length of the dictionary. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit2({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, 28
  ).then(data => {
    console.info('inflateInit2 success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('inflateGetDictionary success:')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateEnd12+

inflateEnd(strm: ZStream): Promise<ReturnStatus>

Releases all dynamically allocated data structs of a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateCopy12+

inflateCopy(source: Zip): Promise<ReturnStatus>

Copies a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | Zip | Yes | For details, see [Zip12+](#zip12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  let destZip = zlib.createZipSync();
  await destZip.inflateCopy(zip).then((data) => {
    console.info('inflateCopy success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateCodesUsed12+

inflateCodesUsed(strm: ZStream): Promise<number>

Describes the number of Huffman trees used in a decompression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the number of Huffman trees that have been used. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zip = zlib.createZipSync();
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateCodesUsed({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 8 }).then(data => {
    console.info('inflateCodesUsed success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]inflateBackInit12+

inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>

Initializes the internal stream state for decompression before using the **inflateBack()** function. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| windowBits | number | Yes | 
Memory window size. The value is restricted in certain range based on the data formats. The options are as follows:

Zlib: \[1, 15\]

Gzip: (15, +∞)

Raw Deflate: \[-15, -1\]

 |
| window | ArrayBuffer | Yes | Preset window buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

For details about the sample code, see [inflateBack](#inflateback12).

#### \[h2\]inflateBackEnd12+

inflateBackEnd(strm: ZStream): Promise<ReturnStatus>

Releases all memory allocated by the **inflateBackInit()** function. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

For details about the sample code, see [inflateBack](#inflateback12).

#### \[h2\]inflateBack12+

inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>

Implements decompression and uses callbacks to process input and output data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| backIn | InflateBackInputCallback | Yes | A function used to decompress data from the end of the array to read the original compressed data from the input source. |
| inDesc | object | Yes | Common object. |
| backOut | InflateBackOutputCallback | Yes | Writes the decompressed data to the destination buffer. |
| outDesc | object | Yes | Common object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let readIn: (inDesc: object) => ArrayBuffer = (inDesc: object): ArrayBuffer => {
    console.info("inDesc = ", JSON.stringify(inDesc));
    let buffer = new ArrayBuffer(26)
    let array = new Uint8Array(buffer);
    array.set(\[31, 139, 8, 0, 0, 0, 0, 0, 0, 10, 243, 72, 205, 201, 201, 231, 2, 0, 22, 53, 150, 49, 6, 0, 0, 0\]);
    return buffer;
  }

  let writeOut: (outDesc: object, buffer: ArrayBuffer, length: number) => number = (outDesc: object, buffer: ArrayBuffer, length: number): number => {
    console.info("outDesc = ", outDesc);
    console.info("buffer = ", buffer);
    console.info("length = ", length);
    let array = new Uint8Array(buffer);
    let dataString = "";
    for (let i = 0; i < length; i++) {
      dataString += String.fromCharCode(array\[i\]);
    }
    console.info('writeOut ', dataString);
    return 0;
  }

  let have = 0;
  let first = 1;
  let arrayBuffer = new ArrayBuffer(26);
  let next = new Uint8Array(arrayBuffer);
  let last = 0;
  let index = 0;
  let flags = 0;
  let NEXT2: () => number = (): number => {
    let o6: object = new Object()
    if (!have) {
      arrayBuffer = readIn(o6)
      next = new Uint8Array(arrayBuffer);
      console.info('readIn next = ', next.length)
      have = next.length;
    }
    if (have) {
      have--;
      last = next\[index\];
      index++;
    }
    else {
      last = -1;
    }
    return last;
  }

  let inflateBackTest: () => void = (async () => {
    try {
      have = 0;
      first = 1;
      arrayBuffer = new ArrayBuffer(26);
      next = new Uint8Array(arrayBuffer);
      last = 0;
      index = 0;
      flags = 0;
      let sr = zlib.createZipSync();
      let buffer = new ArrayBuffer(1024)
      await sr.inflateBackInit({}, 15, buffer).then((result) => {
        console.info('inflateBackInit Call result res', result)
      })
      let ret = 0;
      for (; ;) {
        if (NEXT2() == -1) {
          ret = 0;
          console.info('inflateBackTest Call result NEXT2() == -1')
          break;
        }
        console.info('have =  last = ', have, last)
        if (last != 31 || NEXT2() != 139 ) {
          ret = first ? -3 : -1;
          console.info('inflateBackTest Call result last != 31 || (NEXT2() != 139 && last != 157)')
          break;
        }
        first = 0;
        ret = -5;
        if (NEXT2() != 8) {
          if (last < 0) {
            console.info('inflateBackTest Call result 1 last == -1')
            break;
          }
        }
        flags = NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        NEXT2();
        if (last < 0) {
          console.info('inflateBackTest Call result 2 last == -1')
          break;
        }
        console.info('index =  have = ', next\[index\], have)
        let newArrayBuffer = new ArrayBuffer(have);
        let newNext = new Uint8Array(newArrayBuffer);
        for (let i = 0; i < have; i++) {
          newNext\[i\] = next\[26 - have + i\];
        }
        console.info('newArrayBuffer.length = ', newArrayBuffer.byteLength)
        console.info('newNext.length = ', newNext.length)
        let zStream: zlib.ZStream = {
          nextIn: newArrayBuffer,
          availableIn: have,
        };
        await sr.inflateBack(
          zStream,
          readIn,
          { fileName: 'test.gz' },
          writeOut,
          { fileName: 'test.gz' }).then((result) => {
            ret = result;
            console.info('inflateBack Call result res', result)
          })
        if (ret == 1) {
          console.info('inflateBackTest Call result success')
          break;
        }
      }
      await sr.inflateBackEnd({}).then((result) => {
        console.info('inflateBackEnd Call result res', result)
      })
    }
    catch (errData) {
      console.error(\`errData is message:${errData}\`);
    }
  })
  inflateBackTest();
}

#### \[h2\]InflateBackInputCallback12+

type InflateBackInputCallback = (inDesc: object) => ArrayBuffer

Inputs data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inDesc | object | Yes | User-defined data object. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Content buffer that is successfully read from the input data source. |

#### \[h2\]InflateBackOutputCallback12+

type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: number) => number

Outputs data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| outDesc | object | Yes | User-defined data object. |
| buf | ArrayBuffer | Yes | Stores the data to be written. |
| length | number | Yes | Length of the data written to the output buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of bytes in the output buffer. |

#### \[h2\]inflate12+

inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

Inflates data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| flush | CompressFlushMode | Yes | For details, see [CompressFlushMode](#compressflushmode12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800005 | The input data is incorrect. For example, the data does not conform to the zlib compression format, the compressed data is corrupted, or the data is not compressed. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateInit({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }
  ).then(data => {
    console.info('inflateInit success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflate({ availableIn: 8, availableOut: 8 }, 0).then((data) => {
    console.info('inflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.inflateEnd({ nextOut: arrayBufferOut }).then((data) => {
    console.info('inflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateInit12+

deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>

Initializes a compression stream with a specified compression level. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| level | CompressLevel | Yes | For details, see [CompressLevel](#compresslevel). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
}

#### \[h2\]deflateInit212+

deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number, memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>

Initializes a compression stream with the specified compression level, compression method, window size, memory level, and compression strategy. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| level | CompressLevel | Yes | For details, see [CompressLevel](#compresslevel). |
| method | CompressMethod | Yes | For details, see [CompressMethod](#compressmethod12). |
| windowBits | number | Yes | 
Memory window size. The value is restricted in certain range based on the data formats. The options are as follows:

Zlib: \[1, 15\]

Gzip: (15, +∞)

Raw Deflate: \[-15, -1\]

 |
| memLevel | MemLevel | Yes | For details, see [MemLevel](#memlevel). |
| strategy | CompressStrategy | Yes | For details, see [CompressStrategy](#compressstrategy). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED, zlib.CompressMethod.DEFLATED, 28,
    zlib.MemLevel.MEM\_LEVEL\_DEFAULT, zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY).then((data) => {
      console.info('deflateInit2 success');
    }).catch((errData: BusinessError) => {
      console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
    })
}

#### \[h2\]deflate12+

deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>

Deflates data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| flush | CompressFlushMode | Yes | For details, see [CompressFlushMode](#compressflushmode12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800007 | The input buffer is incorrect, and the output buffer is too small to accommodate the compressed or decompressed data. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
}

#### \[h2\]deflateEnd12+

deflateEnd(strm: ZStream): Promise<ReturnStatus>

Releases all dynamically allocated data structs of a compression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflate({ availableOut: 8 }, zlib.CompressFlushMode.FINISH).then((data) => {
    console.info('deflate success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
  await zip.deflateEnd({ nextOut: arrayBufferOut }).then(data => {
    console.info('deflateEnd success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateBound12+

deflateBound(strm: ZStream, sourceLength: number): Promise<number>

Calculates the maximum size of the compressed data. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| sourceLength | number | Yes | Length of the source data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the maximum size of the compressed data. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateBound({ nextOut: arrayBufferOut }, 12).then((data) => {
    console.info('deflateBound success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateSetHeader12+

deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>

Provides the header information of a gzip file when **deflateInit2()** requests a gzip stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| head | [GzHeader](#gzheader12) | Yes | Header information of a gzip file extracted from the compressed data stream. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit2(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED, zlib.CompressMethod.DEFLATED, 28,
    zlib.MemLevel.MEM\_LEVEL\_DEFAULT, zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY).then((data) => {
      console.info('deflateInit2 success');
    }).catch((errData: BusinessError) => {
      console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
    })
  await zip.deflateSetHeader({ nextIn: arrayBufferIn, availableIn: 1, nextOut: arrayBufferOut, availableOut: 1 }, { isText: true, os: 1, time: 1, xflags: 1, extra: arrayBufferIn, extraLen: 12, name: arrayBufferIn, comment: arrayBufferOut, hcrc: true, done: true }).then((data) => {
    console.info('deflateSetHeader success');
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`)
  })
}

#### \[h2\]deflateCopy12+

deflateCopy(source: Zip): Promise<ReturnStatus>

Copies a compression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | Zip | Yes | For details, see [Zip12+](#zip12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateCopy(zip).then((data) => {
    console.info('deflateCopy success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateSetDictionary12+

deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>

Initializes the compression dictionary from a given sequence of bytes. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| dictionary | ArrayBuffer | Yes | Dictionary data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateGetDictionary12+

deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>

Obtains the content and length of the decompression dictionary used in a compression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| dictionary | ArrayBuffer | Yes | Buffer that receives the actual contents of the decompression dictionary. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DictionaryOutputInfo](#dictionaryoutputinfo12)\> | Promise used to return the result status and length of the dictionary. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateSetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateSetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateGetDictionary({ nextOut: arrayBufferOut }, arrayBufferOut).then((data) => {
    console.info('deflateGetDictionary success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateTune12+

deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>

Fine-tunes the internal compression parameters of **deflate**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| goodLength | number | Yes | Matched length threshold. |
| maxLazy | number | Yes | Delay matching strategy used when the compression algorithm builds a Huffman tree. The value is an integer ranging from 0 to 4. **1**–**4**: A larger value indicates a lazier algorithm, which performs a slower matching process but generates a better compression result. **0**: Lazy matching is disabled. The algorithm builds a Huffman tree as soon as possible. The compression speed is fast, but the compression ratio is low. |
| niceLength | number | Yes | Appropriate delay length threshold. |
| maxChain | number | Yes | Maximum chain length. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateTune({ nextOut: arrayBufferOut }, 2, 2, 2, 2).then((data) => {
    console.info('deflateTune success:')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateReset12+

deflateReset(strm: ZStream): Promise<ReturnStatus>

Equivalent to call the **deflateEnd** API and then the **deflateInit** API. However, this API does not release or reallocate the internal decompression state. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateReset({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflateReset success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateResetKeep12+

deflateResetKeep(strm: ZStream): Promise<ReturnStatus>

Resets the initialized compression stream, but retains the compression parameters and dictionaries set by it. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateResetKeep({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflateResetKeep success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflatePending12+

deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>

Returns the number of bytes and bits of output that has been generated but not yet provided in the available output. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DeflatePendingOutputInfo](#deflatependingoutputinfo12)\> | Promise used to return the result status, and number of bits and bytes for output. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflatePending({ nextOut: arrayBufferOut }).then((data) => {
    console.info('deflatePending success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflateParams12+

deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

Dynamically updates the compression level and compression strategy. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| level | CompressLevel | Yes | For details, see [CompressLevel](#compresslevel). |
| strategy | CompressStrategy | Yes | For details, see [CompressStrategy](#compressstrategy). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync()
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflateParams(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION, zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY).then((data) => {
    console.info('deflateParams success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### \[h2\]deflatePrime12+

deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>

Inserts bits and values into the compression stream. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strm | ZStream | Yes | For details, see [ZStream12+](#zstream12). |
| bits | number | Yes | Number of bits to be inserted. The value ranges from 0 to 16. |
| value | number | Yes | Bit value corresponding to the number of bits. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result status. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib, BusinessError } from '@kit.BasicServicesKit';

async function demo() {
  let str = 'hello world!';
  let arrayBufferIn = new ArrayBuffer(str.length);
  let byteArray = new Uint8Array(arrayBufferIn);
  for (let i = 0, j = str.length; i < j; i++) {
    byteArray\[i\] = str.charCodeAt(i)
  }
  let arrayBufferOut = new ArrayBuffer(100);
  let zStream: zlib.ZStream = {
    nextIn: arrayBufferIn,
    availableIn: 1,
    nextOut: arrayBufferOut,
    availableOut: 1
  };
  let zip = zlib.createZipSync();
  await zip.deflateInit(zStream, zlib.CompressLevel.COMPRESS\_LEVEL\_BEST\_SPEED).then((data) => {
    console.info('deflateInit success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
  await zip.deflatePrime({ nextOut: arrayBufferOut }, 5, 2).then((data) => {
    console.info('deflatePrime success')
  }).catch((errData: BusinessError) => {
    console.error(\`errData is errCode:${errData.code}  message:${errData.message}\`);
  })
}

#### Options

Defines options used to compress or decompress a ZIP file.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| level | [CompressLevel](#compresslevel) | No | Yes | 
Compression level specified for compression or decompression.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| memLevel | [MemLevel](#memlevel) | No | Yes | 

Memory level specified for compression.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| strategy | [CompressStrategy](#compressstrategy) | No | Yes | 

Compression strategy specified for compression.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| parallel18+ | [ParallelStrategy](#parallelstrategy18) | No | Yes | 

Serial or parallel strategy specified for compression or decompression.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| pathSeparatorStrategy21+ | [PathSeparatorStrategy](#pathseparatorstrategy21) | No | Yes | 

Separator strategy for the file path in the compressed package specified for decompression.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### CompressLevel

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPRESS\_LEVEL\_NO\_COMPRESSION | 0 | Compress level 0 that indicates uncompressed. |
| COMPRESS\_LEVEL\_BEST\_SPEED | 1 | Compression level 1 that gives the best speed. |
| COMPRESS\_LEVEL\_BEST\_COMPRESSION | 9 | Compression level 9 that gives the best compression. |
| COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION | \-1 | Default compression level. |

#### MemLevel

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| MEM\_LEVEL\_MIN | 1 | Minimum memory used by the **zlib** API during compression. |
| MEM\_LEVEL\_MAX | 9 | Maximum memory used by the **zlib** API during compression. |
| MEM\_LEVEL\_DEFAULT | 8 | Default memory used by the **zlib** API during compression. |

#### CompressStrategy

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY | 0 | Default compression strategy. |
| COMPRESS\_STRATEGY\_FILTERED | 1 | Filtered compression strategy. |
| COMPRESS\_STRATEGY\_HUFFMAN\_ONLY | 2 | Huffman coding compression strategy. |
| COMPRESS\_STRATEGY\_RLE | 3 | RLE compression strategy. |
| COMPRESS\_STRATEGY\_FIXED | 4 | Fixed compression strategy. |

#### ParallelStrategy18+

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| PARALLEL\_STRATEGY\_SEQUENTIAL | 0 | Serial compression/decompression strategy (default). |
| PARALLEL\_STRATEGY\_PARALLEL\_DECOMPRESSION | 1 | Parallel decompression strategy. |

#### PathSeparatorStrategy21+

Defines **PathSeparatorStrategy**, a property of [Options](#options), used to specify the separator strategy for the file path in the compressed package specified for decompression.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| PATH\_SEPARATOR\_STRATEGY\_DEFAULT | 0 | Default value, indicating that separators in the file path of the compressed package are not processed. |
| PATH\_SEPARATOR\_STRATEGY\_REPLACE\_BACKSLASH | 1 | Backslashes () in the file path of the package are replaced with slashes (/). |

#### ErrorCode(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/rY5c-D4hRRaTYzfScJV8Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E735D4AFCA7C780891B5E856EA2863D439F843AC293EDDAC288FAAD927FB494)

This API is supported since API version 7 and deprecated since API version 9. No substitute is provided.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| ERROR\_CODE\_OK | 0 | The API is successfully called. |
| ERROR\_CODE\_ERRNO | \-1 | Failed to call the API. |

#### CompressFlushMode12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_FLUSH | 0 | Default value, indicating a normal operation. |
| PARTIAL\_FLUSH | 1 | Generates some refresh points in the stream. |
| SYNC\_FLUSH | 2 | Forcibly outputs all compressed data while maintaining the compression stream state. |
| FULL\_FLUSH | 3 | Resets the compression state. |
| FINISH | 4 | Ends the compression or decompression process. |
| BLOCK | 5 | Allows more precise control. |
| TREES | 6 | Implements special purposes. |

#### CompressMethod12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFLATED | 8 | Compression method. |

#### ReturnStatus12+

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| OK | 0 | 
The API is successfully called. This API is supported for use in atomic services.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| STREAM\_END | 1 | 

The API is successfully called, indicating that the entire data has been processed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| NEED\_DICT | 2 | 

The API is successfully called, indicating that a preset dictionary is required to continue decompression.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ZStream12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nextIn | ArrayBuffer | No | Yes | Input bytes to be compressed. |
| availableIn | number | No | Yes | Number of bytes available for **nextIn**. |
| totalIn | number | No | Yes | Total number of input bytes read so far. |
| nextOut | ArrayBuffer | No | Yes | Output bytes after compression. |
| availableOut | number | No | Yes | Number of remaining bytes available for **nextOut**. |
| totalOut | number | No | Yes | Total number of output bytes. |
| dataType | number | No | Yes | Binary or text of **deflate**, or decoding state of **inflate**. |
| adler | number | No | Yes | Adler-32 or CRC-32 value of uncompressed data. |

#### ZipOutputInfo12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | ReturnStatus | No | No | For details, see [ReturnStatus](#returnstatus12). |
| destLen | number | No | No | Total length of the destination buffer. |

#### DictionaryOutputInfo12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | ReturnStatus | No | No | For details, see [ReturnStatus](#returnstatus12). |
| dictionaryLength | number | No | No | Length of a dictionary. |

#### DecompressionOutputInfo12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | ReturnStatus | No | No | For details, see [ReturnStatus](#returnstatus12). |
| destLength | number | No | No | Length of the destination buffer. |
| sourceLength | number | No | No | Length of the source buffer. |

#### DeflatePendingOutputInfo12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | ReturnStatus | No | No | For details, see [ReturnStatus](#returnstatus12). |
| pending | number | No | No | Number of output bytes that have been generated. |
| bits | number | No | No | Number of output bits that have been generated. |

#### GzHeader12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isText | boolean | No | Yes | Returns **True** if the compressed data is considered text. |
| os | number | No | Yes | Operating system. |
| time | number | No | Yes | Modification time. |
| xflags | number | No | Yes | Extra flag. |
| extra | ArrayBuffer | No | Yes | Extra field. |
| extraLen | number | No | Yes | Length of the extra field. |
| name | ArrayBuffer | No | Yes | File name. |
| comment | ArrayBuffer | No | Yes | Comment. |
| hcrc | boolean | No | Yes | Returns **True** if the **crc** header exists. |
| done | boolean | No | Yes | Returns **True** after reading the gzip file header. |

#### zlib.createGZip12+

createGZip(): Promise<GZip>

Creates this **GZip** object. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GZip](#gzip12)\> | Promise used to return the **GZip** object created. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

zlib.createGZip().then((data) => {
  console.info('createGZip success');
})

#### zlib.createGZipSync12+

createGZipSync(): GZip

Creates this **GZip** object. A **GZip** instance is returned upon a success.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| [GZip](#gzip12) | gzip object instance. |

**Example**

import { zlib } from '@kit.BasicServicesKit';

let gzip = zlib.createGZipSync();

#### GZip12+

Describes gzip-related APIs.

#### \[h2\]gzdopen12+

gzdopen(fd: number, mode: string): Promise<void>

Associates gzip file with the file descriptor (fd) and opens the file for reading and decompressing, or compressing and writing. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor. Generally, the value is obtained by calling the **open** method or other methods. |
| mode | string | Yes | Specifies the access mode. For details, see the description of [gzopen](#gzopen12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800002 | No such file or access mode error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzdopenDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzdopen");
  let path = pathDir + "/gzdopen/test.gz";
  let file = fs.openSync(path, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
  let gzip = zlib.createGZipSync();
  await gzip.gzdopen(file.fd, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzdopenDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzbuffer12+

gzbuffer(size: number):Promise<number>

Sets the internal buffer size for the current library function. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the internal buffer to be set. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the operation is successful, **0** is returned. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { zlib } from '@kit.BasicServicesKit';

async function gzbufferDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzbuffer");
  let path = pathDir + "/gzbuffer/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzbuffer(648);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzbufferDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzopen12+

gzopen(path: string, mode: string): Promise<void>

Opens the .gz file in the specified path for reading and decompressing, or compressing and writing. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file to be opened. |
| mode | string | Yes | 
Specifies a mode for opening a file.

Basic modes (one of the following must be selected):

\- **"r"** or **"rb"**: read mode. The system automatically detects and decompresses the gzip file. If the file is not in gzip format, the original data is directly read.

\- **"w"** or **"wb"**: write mode. The system creates a new file and compresses data.

\- **"a"** or **"ab"**: append mode. The system appends a new gzip stream to the end of the existing file without verifying the format of the original file.

Optional function parameters (can be used together):

\- Compression level: **0** (no compression) to **9** (maximum compression). The default compression level is **6**. This parameter must be used together with the write or append mode.

\- Compression strategy: **"f"** (filtering strategy), **"h"** (Huffman coding strategy), **"R"** (RLE compression strategy), or **"F"** (fixed encoding strategy). You can only select one of the strategies.

\- Transparent mode: **"T"**. In this mode, data is not compressed and no gzip header is generated during writing (a common file is generated). This parameter is mutually exclusive with the compression strategy parameter.

\- Exclusive creation: **"x"**. The file fails to be opened if it already exists. This parameter must be used together with the write or append mode.

\- Close-on-exec flag: **"e"**. This parameter is used to set the **FD\_CLOEXEC** property of the file descriptor (system-dependent).

Examples:

\- **"r"**: read mode. Data is read in binary format.

\- **"rb"**: read mode. Data is read in binary format.

\- **"wb6"**: write mode. Data is written in binary format with the compression level of 6.

\- **"wb9f"**: write mode. Data is written in binary format with the maximum compression level and filtering strategy.

\- **"wbT"**: write mode. Data is not compressed and a common file is generated.

\- **"wbx"**: write mode. Data is written to the exclusively created file in binary format.

\- **"abx"**: append mode. Data is appended and written to the exclusively created file in binary format.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800002 | No such file or access mode error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzopenDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzopen");
  let path = pathDir + "/gzopen/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzopenDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzeof12+

gzeof(): Promise<number>

Checks whether the position from which data is read has reached the end of the gzip file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the end-of-file indicator is set while reading, **1** is returned. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzeofDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzeof");
  let path = pathDir + "/gzeof/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBufferWithData = new ArrayBuffer(20);
  let readNum = await gzip.gzread(readBufferWithData);
  let eofNum = await gzip.gzeof();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzeofDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzdirect12+

gzdirect(): Promise<number>

Checks whether the specified gzip file handle directly accesses the original uncompressed data and reallocates the buffer. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. If the original uncompressed data is directly accessed, **1** is returned. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzdirectDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzdirect");
  let path = pathDir + "/gzdirect/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let directNum = await gzip.gzdirect();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzdirectDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzclose12+

gzclose(): Promise<ReturnStatus>

Clears all pending output of the file. Closes the file and releases the decompression or compression state if necessary. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800006 | Memory allocation failed. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzcloseDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclose");
  let path = pathDir + "/gzclose/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzcloseDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzclearerr12+

gzclearerr(): Promise<void>

Clears the errors and end-of-file flags of a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzclearerrDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclearerr");
  let path = pathDir + "/gzclearerr/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  let writeNum = await gzip.gzwrite(writeBufferWithData, 16)
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBufferWithData = new ArrayBuffer(20);
  let readNum = await gzip.gzread(readBufferWithData);
  let eofNum = await gzip.gzeof();
  await gzip.gzclearerr();
  let eofNumClear = await gzip.gzeof();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzclearerrDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzerror12+

gzerror(): Promise<GzErrorOutputInfo>

Describes the last error message that reported for the file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GzErrorOutputInfo](#gzerroroutputinfo12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzerrorDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzerror");
  let path = pathDir + "/gzerror/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  try {
    await gzip.gzwrite(writeBufferWithData, -1);
  } catch (errData) {
    await gzip.gzerror().then((GzErrorOutputInfo) => {
      console.info('errCode', GzErrorOutputInfo.status);
      console.info('errMsg', GzErrorOutputInfo.statusMsg);
    })
  }
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzerrorDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzgetc12+

gzgetc(): Promise<number>

Reads and decompresses a byte from a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzgetcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzgetc");
  let path = pathDir + "/gzgetc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzputc(1);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzgetc();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzgetcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzflush12+

gzflush(flush: CompressFlushMode): Promise<ReturnStatus>

Flushes all pending output into a compressed file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flush | CompressFlushMode | Yes | Controls the flushing mode. For details, see [CompressFlushMode](#compressflushmode12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzflushDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzflush");
  let path = pathDir + "/gzflush/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let flushNum = await gzip.gzflush(zlib.CompressFlushMode.NO\_FLUSH);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzflushDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzfwrite12+

gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

Compresses data blocks that are declared with size and nitems from the buffer and writes the data blocks to a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Buffer to which data is to be written. |
| size | number | Yes | Number of bytes in a single data block. |
| nitems | number | Yes | Number of data blocks to be written. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzfwriteDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzfwrite");
  let path = pathDir + "/gzfwrite/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let bufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(bufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  let result = await gzip.gzfwrite(bufferWithData, 8, 2)
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzfwriteDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzfread12+

gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>

Decompresses and reads data from a gzip file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Destination buffer for storing read results. |
| size | number | Yes | Number of bytes in a single data block. |
| nitems | number | Yes | Number of data blocks to be written. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzfreadDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzfread");
  let path = pathDir + "/gzfread/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBuffer = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBuffer);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  await gzip.gzfwrite(writeBuffer, 8, 2);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBuffer = new ArrayBuffer(16);
  let result = await gzip.gzfread(readBuffer, 8, 2);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzfreadDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzclosew12+

gzclosew(): Promise<ReturnStatus>

Implements the same functions as that of **gzclose()** for writing or appending. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800006 | Memory allocation failed. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzclosewDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzclosew");
  let path = pathDir + "/gzclosew/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclosew();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzclosewDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzcloser12+

gzcloser(): Promise<ReturnStatus>

Implements the same functions as that of **gzclose()** for reading only. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzcloserDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzcloser");
  let path = pathDir + "/gzcloser/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  await gzip.gzcloser();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzcloserDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzwrite12+

gzwrite(buf: ArrayBuffer, len: number): Promise<number>

Compresses the uncompressed bytes of the declared length in the buffer and writes them to the file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Data buffer pointed by an object to be written. |
| len | number | Yes | Length of uncompressed bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzwriteDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzwrite");
  let path = pathDir + "/gzwrite/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let bufferWithData = new ArrayBuffer(16);
  let uint8View = new Uint8Array(bufferWithData);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  let result = await gzip.gzwrite(bufferWithData, 16);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzwriteDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzungetc12+

gzungetc(c: number): Promise<number>

Pushes **c** back into the input stream so that it will be read as the first character the next time the file is read. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| c | number | Yes | Characters before being pushed into the input stream. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzungetcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzungetc");
  let path = pathDir + "/gzungetc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  await gzip.gzread(new ArrayBuffer(1));
  let result = await gzip.gzungetc(1);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzungetcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gztell12+

gztell(): Promise<number>

Returns the start position of the next **gzread** or **gzwrite** in the file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gztellDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gztell");
  let path = pathDir + "/gztell/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gztell();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gztellDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzsetparams12+

gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>

Dynamically updates the compression level and compression strategy of a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| level | CompressLevel | Yes | Compression level. For details, see [CompressLevel](#compresslevel). |
| strategy | CompressStrategy | Yes | Compression strategy. For details, see [CompressStrategy](#compressstrategy). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzsetparamsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzsetparams");
  let path = pathDir + "/gzsetparams/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzsetparams(zlib.CompressLevel.COMPRESS\_LEVEL\_DEFAULT\_COMPRESSION,
    zlib.CompressStrategy.COMPRESS\_STRATEGY\_DEFAULT\_STRATEGY);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzsetparamsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzseek12+

gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>

Sets the start position to the offset position relative to the next **gzread** or **gzwrite** in the file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| offset | number | Yes | Target offset position. |
| whence | OffsetReferencePoint | Yes | Defines the reference point for the offset. For details, see [OffsetReferencePoint](#offsetreferencepoint12). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzseekDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzseek");
  let path = pathDir + "/gzseek/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzseek(2, zlib.OffsetReferencePoint.SEEK\_CUR);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzseekDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzrewind12+

gzrewind(): Promise<ReturnStatus>

Repositions the file pointer to the beginning of the file. This feature is applied only for reading. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReturnStatus](#returnstatus12)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzrewindDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzrewind");
  let path = pathDir + "/gzrewind/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let result = await gzip.gzrewind();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzrewindDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzread12+

gzread(buf: ArrayBuffer): Promise<number>

Reads a maximum of **len** uncompressed bytes from a file and decompresses them into the buffer. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Target offset position. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzreadDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzread");
  let path = pathDir + "/gzread/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let writeBuffer = new ArrayBuffer(16);
  let uint8View = new Uint8Array(writeBuffer);
  for (let i = 0; i < uint8View.length; i++) {
    uint8View\[i\] = i;
  }
  await gzip.gzwrite(writeBuffer, 16);
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let readBuffer = new ArrayBuffer(16);
  let result = await gzip.gzread(readBuffer);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzreadDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzputs12+

gzputs(str: string): Promise<number>

Compresses the given null-terminated strings and writes them to the file, excluding the null operator. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| str | string | Yes | Format descriptors and plain text. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzputsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzputs");
  let path = pathDir + "/gzputs/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzputs("hello");
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzputsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzputc12+

gzputc(ch: number): Promise<number>

Compresses **char** converted to an unsigned character and writes it to a file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ch | number | Yes | Write character ASCII. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzputcDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzputc");
  let path = pathDir + "/gzputc/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzputc(0);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzputcDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzprintf12+

gzprintf(format: string, ...args: Array<string | number>): Promise<number>

Converts and formats the parameters under the control of the string format and then compresses and writes them into a file, as shown in the **fprintf()**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| format | string | Yes | Format descriptors and plain text. |
| ...args | Array<string | number> | No | List of variable parameters. If variable parameters are passed, for example, **gzprintf("name is %s, age is %d", "Tom", 23)**, the content **"name is Tom, age is 23"** is written. If no variable parameter is passed, for example, **gzprintf("name is %s, age is %d")**, the content **"name is %s, age is %d"** is written. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800004 | Compression or decompression stream error, which may be caused by an initialization error in the zlib stream structure or a modified structure. |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzprintfDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzprintf");
  let path = pathDir + "/gzprintf/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzprintf("name is %s, age is %d", "Tom", 23);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzprintfDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzoffset12+

gzoffset(): Promise<number>

Returns the current compressed read or write offset of the file. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzoffsetDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzoffset");
  let path = pathDir + "/gzoffset/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  let result = await gzip.gzoffset();
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzoffsetDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### \[h2\]gzgets12+

gzgets(buf: ArrayBuffer): Promise<string>

Reads bytes from a compressed file until len-1 characters are read, a newline character is read and transferred to a buffer, or an end-of-file condition is encountered. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Stores the read row data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return a string ended with **null**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [zlib Error Codes](../../../error-codes/zlib-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified;

2\. Incorrect parameter types;

3\. Parameter verification failed.

 |
| 17800009 | Internal structure error. |

**Example**

import { zlib } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

async function gzgetsDemo(pathDir: string) {
  fs.mkdirSync(pathDir + "/gzgets");
  let path = pathDir + "/gzgets/test.gz";
  let gzip = zlib.createGZipSync();
  await gzip.gzopen(path, "wb");
  await gzip.gzputs("hello");
  await gzip.gzclose();
  await gzip.gzopen(path, "rb");
  let bufferWithData = new ArrayBuffer(16);
  let result = await gzip.gzgets(bufferWithData);
  await gzip.gzclose();
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('test gzip interface')
          .type(ButtonType.Capsule)
          .height(60)
          .width(200)
          .onClick(() => {
            let pathDir = this.getUIContext()?.getHostContext()?.cacheDir;
            if (typeof pathDir === 'string') {
              gzgetsDemo(pathDir);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### GzErrorOutputInfo12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | ReturnStatus | No | No | Zlib file status code. For details, see the definition of **ReturnStatus**. |
| statusMsg | string | No | No | The last status message reported on the zlib file. |

#### OffsetReferencePoint12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.BundleManager.Zlib

| Name | Value | Description |
| :-- | :-- | :-- |
| SEEK\_SET | 0 | Searches from the beginning of a file. |
| SEEK\_CUR | 1 | Searches from the current location. |
