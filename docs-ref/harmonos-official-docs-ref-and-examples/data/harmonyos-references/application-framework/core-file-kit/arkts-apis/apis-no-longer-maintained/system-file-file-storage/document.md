# @system.file (File Storage)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/6r4PAGZpR2GZvBQ2fyhnKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3F2AFD6E306A7AD81317304017D6B3064269F13673A23B616765D7C71205651)

-   Module maintenance policy:
    -   For lite wearables, this module is constantly maintained and available.
    -   For other device types, this module is no longer maintained since API version 10, and you are advised to use [@ohos.file.fs](../../ohos-file-fs-file-management/document.md) instead.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import file from '@system.file';

#### file.move

move(Object): void

Moves a specified file to a given location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/NrWZ-robSVK_BkD5eSiQeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BF854A1993997E81527146B7A799640D5F55233B2960AD704F17DE6E9A56F3F)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.moveFile](../../ohos-file-fs-file-management/document.md#fsmovefile) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcUri | string | Yes | URI of the file to move. The value can contain a maximum of 128 characters, excluding the following characters: "\*+,:;<=>?\[\]|\\x7F |
| dstUri | string | Yes | URI of the location to which the file is to move. The value can contain a maximum of 128 characters, excluding the following characters: "\*+,:;<=>?\[\]|\\x7F |
| success | Function | No | Called when the file is moved to the specified location. This API returns the URI of the destination location. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  move() {
    file.move({
      srcUri: 'internal://app/myfiles1',
      dstUri: 'internal://app/myfiles2',
      success: function(uri) {
        console.info('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.copy

copy(Object): void

Copies a file to the given URI.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/P5DdoCGgQWGd8mQsiVt7ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D5AEE6DED26B5B81C35B2A0FFA3A973322CC4869FADCAE639EAED4A79C7156E)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.copyFile](../../ohos-file-fs-file-management/document.md#fscopyfile) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| srcUri | string | Yes | URI of the file to copy. |
| dstUri | string | Yes | 
URI of the location to which the copy is to be saved.

The directory of application resources and URI of the **tmp** type are not supported.

 |
| success | Function | No | Called when the file is copied and saved to the specified location. This API returns the URI of the destination location. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  copy() {
    file.copy({
      srcUri: 'internal://app/file.txt',
      dstUri: 'internal://app/file\_copy.txt',
      success: function(uri) {
        console.info('call success callback success');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.list

list(Object): void

Obtains all files in the specified directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/jnGa8ywYSta2Ktdie5dcuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F2DF15B9889133C693A5A7D519ED10BC9B585B35ECCBBF9D6676A7084B24716)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the directory. The value can contain a maximum of 128 characters, excluding the following characters: "\*+,:;<=>?\[\]|\\x7F |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Return value of success()**

| Name | Type | Description |
| :-- | :-- | :-- |
| fileList | Array<FileInfo> | 
File list. The format of each file is as follows:

{

uri:'file1',

lastModifiedTime:1589965924479,

length:10240,

type: 'file'

}

 |

**Table 1** FileInfo

| Name | Type | Description |
| :-- | :-- | :-- |
| uri | string | URI of the file. |
| lastModifiedTime | number | Timestamp when the file is stored the last time, which is the number of milliseconds elapsed since 1970/01/01 00:00:00 GMT. |
| length | number | File size, in bytes. |
| type | string | 
File type. Available values are as follows:

\- **dir**: directory

\- **file**: file

 |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  list() {
    file.list({
      uri: 'internal://app/pic',
      success: function(data) {
        console.info(JSON.stringify(data.fileList));
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.get

get(Object): void

Obtains information about a local file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/MsvPoy4uT9uH-riy6rIjgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB831CA07292AE867795053155C9115F8657493776260C0623697319CD0B1630)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.stat](../../ohos-file-fs-file-management/document.md#fsstat) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file. |
| recursive | boolean | No | Whether to obtain the subdirectory file list recursively. The value **true** means to obtain the subdirectory file list recursively; the value **false** means the opposite. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Return value of success()**

| Name | Type | Description |
| :-- | :-- | :-- |
| uri | string | URI of the file. |
| length | number | File size, in bytes. |
| lastModifiedTime | number | Timestamp when the file is stored the last time, which is the number of milliseconds elapsed since 1970/01/01 00:00:00 GMT. |
| type | string | 
File type. Available values are as follows:

\- **dir**: directory

\- **file**: file

 |
| subFiles | Array | List of files. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  get() {
    file.get({
      uri: 'internal://app/file',
      success: function(data) {
        console.info(data.uri);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.delete

delete(Object): void

Deletes a local file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/PDywkktpR0mDFAibWNIXZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6F7AA001BEAF116DF3472CFAF2A7566950D5F2C6F3549A2E9D9760DAC40F9E1)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.unlink](../../ohos-file-fs-file-management/document.md#fsunlink) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to delete. It cannot be an application resource path. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  delete() {
    file.delete({
      uri: 'internal://app/my\_file',
      success: function() {
        console.info('call delete success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.writeText

writeText(Object): void

Writes text into a file. Only text files can be read and written.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/s5WYoldTTKyq6_gsG0SjnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B90FCEBB536F67826B15C39A2B5ED37F2D97B6749CA0D59C71030D0D45ED5F73)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.write](../../ohos-file-fs-file-management/document.md#fswrite) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of a local file. If it does not exist, a file will be created. |
| text | string | Yes | String to write into the file. |
| encoding | string | No | Encoding format. The default format is **UTF-8**. |
| append | boolean | No | Whether to enable the append mode. The default value is **false**. The value **true** means to enable the append mode; the value **false** means the opposite. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |

**Example**

export default {
  writeText() {
    file.writeText({
      uri: 'internal://app/test.txt',
      text: 'Text that just for test.',
      success: function() {
        console.info('call writeText success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.writeArrayBuffer

writeArrayBuffer(Object): void

Writes buffer data into a file. Only text files can be read and written.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/M7GExdtkTECet5B9wjr_MA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D05ACA2CBE32CAA4399454AA498051C66670305EB74A89F5D8E1CEA8FD6EF4AC)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.write](../../ohos-file-fs-file-management/document.md#fswrite) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of a local file. If it does not exist, a file will be created. |
| buffer | Uint8Array | Yes | Buffer from which the data is derived. |
| position | number | No | Offset to the position where the writing starts. The default value is **0**. |
| append | boolean | No | Whether to enable the append mode. The default value is **false**. If the value is **true**, the **position** parameter will become invalid. The value **true** means to enable the append mode; the value **false** means the opposite. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |

**Example**

export default {
  writeArrayBuffer() {
    file.writeArrayBuffer({
      uri: 'internal://app/test',
      buffer: new Uint8Array(8), // The buffer is of the Uint8Array type.
      success: function() {
        console.info('call writeArrayBuffer success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.readText

readText(Object): void

Reads text from a file. Only text files can be read and written.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/7k-CE32CQDm-0HzJ3kXsfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8702B5B927A4804CF28B661CC3A146254A80383C80D9A6F6F8FA6BDDAE2ED8F9)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.readText](../../ohos-file-fs-file-management/document.md#fsreadtext) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of a local file. |
| encoding | string | No | Encoding format. The default format is **UTF-8**. |
| position | number | No | Position where the reading starts. The default value is the start position of the file. |
| length | number | No | Length of the text to read, in bytes. The default value is **4096**. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Return value of success()**

| Name | Type | Description |
| :-- | :-- | :-- |
| text | string | Text read from the specified file. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |
| 302 | The text to read exceeds 4 KB. |

**Example**

export default {
  readText() {
    file.readText({
      uri: 'internal://app/text.txt',
      success: function(data) {
        console.info('call readText success: ' + data.text);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.readArrayBuffer

readArrayBuffer(Object): void

Reads buffer data from a file. Only text files can be read and written.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/HC26H7r1T2GAUVcmy2qfOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA501303F1643BD3AC8701A62AEE8C218A8053AF3406BFFAB76ECA40250AAEFC)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.read](../../ohos-file-fs-file-management/document.md#fsread) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of a local file. |
| position | number | No | Position where the reading starts. The default value is the start position of the file. |
| length | number | No | Length of data to read. If this parameter is not set, the reading proceeds until the end of the file. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Return value of success()**

| Name | Type | Description |
| :-- | :-- | :-- |
| buffer | Uint8Array | Data read. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  readArrayBuffer() {
    file.readArrayBuffer({
      uri: 'internal://app/test',
      position: 10,
      length: 200,
      success: function(data) {
        console.info('call readArrayBuffer success: ' + data.buffer);
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.access

access(Object): void

Checks whether a file or directory exists.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ifg5mLwcRby3iJ68vr_AUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22B5DF6609FB1AA664D9DA1512C24A66D3751EDAF5CAD1E3813D39252403F82D)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.access](../../ohos-file-fs-file-management/document.md#fsaccess) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the directory or file to check. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  access() {
    file.access({
      uri: 'internal://app/test',
      success: function() {
        console.info('call access success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.mkdir

mkdir(Object): void

Creates a directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/tT-_4Q2lSkqtUYxIE-HS4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5AB9B530319C31D8CD849B2B822D4B5771C192E396C3B667A2493636E199598)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.mkdir](../../ohos-file-fs-file-management/document.md#fsmkdir) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the directory to delete. |
| recursive | boolean | No | Whether to recursively create the upper-level directory of the specified directory. The default value is **false**. The value **true** means to create upper-level directory recursively; the value false means the opposite. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |

**Example**

export default {
  mkdir() {
    file.mkdir({
      uri: 'internal://app/test\_directory',
      success: function() {
        console.info('call mkdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}

#### file.rmdir

rmdir(Object): void

Deletes a directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/OYaUEZQQRXWeocN9b2XJRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F037624CC8B853DA5D26768E3EF487EBA5F12E772DC5779FA8E5B44936BABE86)

This API is deprecated since API version 10 for all device types except lite wearables. Use [fs.rmdir](../../ohos-file-fs-file-management/document.md#fsrmdir) instead.

**System Capability**: SystemCapability.FileManagement.File.FileIO.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the directory to delete. |
| recursive | boolean | No | Whether to recursively delete files and subdirectories of the specified directory. The default value is **false**. The value **true** means to recursively delete files and subdirectories of the specified directory; the value **false** means the opposite. |
| success | Function | No | Called when the directory is deleted. |
| fail | Function | No | Called when the directory fails to be deleted. |
| complete | Function | No | Called when the execution is complete. |

**Error codes**

| Error Code | Description |
| :-- | :-- |
| 202 | Incorrect parameters are detected. |
| 300 | An I/O error occurs. |
| 301 | The file or directory does not exist. |

**Example**

export default {
  rmdir() {
    file.rmdir({
      uri: 'internal://app/test\_directory',
      success: function() {
        console.info('call rmdir success.');
      },
      fail: function(data, code) {
        console.error('call fail callback fail, code: ' + code + ', data: ' + data);
      },
    });
  }
}
