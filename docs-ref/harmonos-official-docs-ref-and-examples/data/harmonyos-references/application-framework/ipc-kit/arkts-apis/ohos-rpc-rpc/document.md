# @ohos.rpc (RPC)

The **RPC** module implements communication between processes, including inter-process communication (IPC) on a single device and remote procedure call (RPC) between processes on difference devices. IPC is implemented based on the Binder driver, and RPC is based on the DSoftBus driver.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/13K_n-zqTUmOtC5e0_suFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=808BAFC584F96C9249872CC612800BE1E54D96711A4047DE0CECB8B2104F8E04)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module supports return of error codes since API version 9.
    

#### Modules to Import

import { rpc } from '@kit.IPCKit';

#### ErrorCode9+

The APIs of this module return exceptions since API version 9. The following table lists the error codes.

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CHECK\_PARAM\_ERROR | 401 | Parameter check failed. |
| OS\_MMAP\_ERROR | 1900001 | Failed to call mmap. |
| OS\_IOCTL\_ERROR | 1900002 | Failed to call **ioctl** with the shared memory file descriptor. |
| WRITE\_TO\_ASHMEM\_ERROR | 1900003 | Failed to write data to the shared memory. |
| READ\_FROM\_ASHMEM\_ERROR | 1900004 | Failed to read data from the shared memory. |
| ONLY\_PROXY\_OBJECT\_PERMITTED\_ERROR | 1900005 | This operation is allowed only on the proxy object. |
| ONLY\_REMOTE\_OBJECT\_PERMITTED\_ERROR | 1900006 | This operation is allowed only on the remote object. |
| COMMUNICATION\_ERROR | 1900007 | Failed to communicate with the remote object over IPC. |
| PROXY\_OR\_REMOTE\_OBJECT\_INVALID\_ERROR | 1900008 | Invalid proxy or remote object. |
| WRITE\_DATA\_TO\_MESSAGE\_SEQUENCE\_ERROR | 1900009 | Failed to write data to MessageSequence. |
| READ\_DATA\_FROM\_MESSAGE\_SEQUENCE\_ERROR | 1900010 | Failed to read data from MessageSequence. |
| PARCEL\_MEMORY\_ALLOC\_ERROR | 1900011 | Failed to allocate memory during serialization. |
| CALL\_JS\_METHOD\_ERROR | 1900012 | Failed to invoke the JS callback. |
| OS\_DUP\_ERROR | 1900013 | Failed to call dup. |

#### TypeCode12+

Since API version 12, [writeArrayBuffer](#writearraybuffer12) and [readArrayBuffer](#readarraybuffer12) are added to pass ArrayBuffer data. The specific TypedArray type is determined by the **TypeCode** defined as follows.

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INT8\_ARRAY | 0 | The TypedArray type is **INT8\_ARRAY**. |
| UINT8\_ARRAY | 1 | The TypedArray type is **UINT8\_ARRAY**. |
| INT16\_ARRAY | 2 | The TypedArray type is **INT16\_ARRAY**. |
| UINT16\_ARRAY | 3 | The TypedArray type is **UINT16\_ARRAY**. |
| INT32\_ARRAY | 4 | The TypedArray type is **INT32\_ARRAY**. |
| UINT32\_ARRAY | 5 | The TypedArray type is **UINT32\_ARRAY**. |
| FLOAT32\_ARRAY | 6 | The TypedArray type is **FLOAT32\_ARRAY**. |
| FLOAT64\_ARRAY | 7 | The TypedArray type is **FLOAT64\_ARRAY**. |
| BIGINT64\_ARRAY | 8 | The TypedArray type is **BIGINT64\_ARRAY**. |
| BIGUINT64\_ARRAY | 9 | The TypedArray type is **BIGUINT64\_ARRAY**. |

#### MessageSequence9+

Provides APIs for reading and writing data in specific format. During RPC or IPC, the sender can use the **write()** method provided by **MessageSequence** to write data in specific format to a **MessageSequence** object. The receiver can use the **read()** method provided by **MessageSequence** to read data in specific format from a **MessageSequence** object. The data formats include basic data types and arrays, IPC objects, interface tokens, and custom sequenceable objects.

#### \[h2\]create9+

static create(): MessageSequence

Creates a **MessageSequence** object. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MessageSequence](#messagesequence9) | **MessageSequence** object created. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  hilog.info(0x0000, 'testTag', 'data is ' + data);

  // When the MessageSequence object is no longer used, the service calls the reclaim method to release resources.
  data.reclaim();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]reclaim9+

reclaim(): void

Reclaims the **MessageSequence** object that is no longer used.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let reply = rpc.MessageSequence.create();
  reply.reclaim();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeRemoteObject9+

writeRemoteObject(obj: IRemoteObject): void

Serializes the remote object and writes it to the [MessageSequence](#messagesequence9) object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | [IRemoteObject](#iremoteobject) | Yes | Remote object to serialize and write to the **MessageSequence** object. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900008 | The proxy or remote object is invalid. |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageSequence.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readRemoteObject9+

readRemoteObject(): IRemoteObject

Reads the remote object from **MessageSequence**. You can use this API to deserialize the **MessageSequence** object to generate an **IRemoteObject**. The remote object is read in the order in which it is written to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | Remote object obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageSequence.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
  let proxy = data.readRemoteObject();
  hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeInterfaceToken9+

writeInterfaceToken(token: string): void

Writes an interface token to this **MessageSequence** object. The remote object can use this interface token to verify the communication.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| token | string | Yes | Interface token to write. The length of the string must be less than 40960 bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInterfaceToken("aaa");
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readInterfaceToken9+

readInterfaceToken(): string

Reads the interface token from this **MessageSequence** object. The interface token is read in the sequence in which it is written to the **MessageSequence** object. The local object can use it to verify the communication.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface token obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInterfaceToken("aaa");
  let interfaceToken = data.readInterfaceToken();
  hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getSize9+

getSize(): number

Obtains the data size of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Size of the **MessageSequence** instance obtained, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let size = data.getSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getCapacity9+

getCapacity(): number

Obtains the capacity of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Capacity of the obtained **MessageSequence** object, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let result = data.getCapacity();
  hilog.info(0x0000, 'testTag', 'capacity is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]setSize9+

setSize(size: number): void

Sets the size of the data contained in this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Data size to set, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('Hello World');
  data.setSize(16);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]setCapacity9+

setCapacity(size: number): void

Sets the storage capacity of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Storage capacity of the **MessageSequence** object to set, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |
| 1900011 | Memory allocation failed. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.setCapacity(100);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getWritableBytes9+

getWritableBytes(): number

Obtains the writable capacity (in bytes) of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Writable capacity of the **MessageSequence** instance, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.setCapacity(100);
  let getWritableBytes = data.getWritableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getReadableBytes9+

getReadableBytes(): number

Obtains the readable capacity of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Readable capacity of the **MessageSequence** instance, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString("hello world");
  let result = data.getReadableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getReadPosition9+

getReadPosition(): number

Obtains the read position of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Read position obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString("hello world");
  let readPos = data.getReadPosition();
  hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getWritePosition9+

getWritePosition(): number

Obtains the write position of this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Write position obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
  let bwPos = data.getWritePosition();
  hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]rewindRead9+

rewindRead(pos: number): void

Moves the read pointer to the specified position.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pos | number | Yes | Position from which data is to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(12);
  data.writeString("sequence");
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'number is ' + number);
  data.rewindRead(0);
  let number2 = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]rewindWrite9+

rewindWrite(pos: number): void

Moves the write pointer to the specified position.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pos | number | Yes | Position from which data is to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(4);
  data.rewindWrite(0);
  data.writeInt(5);
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindWrite is: ' + number);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeByte9+

writeByte(val: number): void

Writes a byte value to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Byte value to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeByte(2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readByte9+

readByte(): number

Reads the byte value from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Byte value read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeByte(2);
  let ret = data.readByte();
  hilog.info(0x0000, 'testTag', 'readByte is: ' +  ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeShort9+

writeShort(val: number): void

Writes a short integer to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Short integer to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShort(8);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readShort9+

readShort(): number

Reads the short integer from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Short integer read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShort(8);
  let ret = data.readShort();
  hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeInt9+

writeInt(val: number): void

Writes an integer to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Integer to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readInt9+

readInt(): number

Reads the integer from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Integer read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeInt(10);
  let ret = data.readInt();
  hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeLong9+

writeLong(val: number): void

Writes a long integer to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Long integer to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLong(10000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readLong9+

readLong(): number

Reads the long integer from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Long integer read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLong(10000);
  let ret = data.readLong();
  hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeFloat9+

writeFloat(val: number): void

Writes a double value to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Double value to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloat(1.2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readFloat9+

readFloat(): number

Reads the double value from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Double value read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloat(1.2);
  let ret = data.readFloat();
  hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeDouble9+

writeDouble(val: number): void

Writes a double value to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Double value to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDouble(10.2);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readDouble9+

readDouble(): number

Reads the double value from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Double value read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDouble(10.2);
  let ret = data.readDouble();
  hilog.info(0x0000, 'testTag', 'readDouble is ' +  ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeBoolean9+

writeBoolean(val: boolean): void

Writes a Boolean value to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | boolean | Yes | Boolean value to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBoolean(false);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readBoolean9+

readBoolean(): boolean

Reads the Boolean value from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBoolean(false);
  let ret = data.readBoolean();
  hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeChar9+

writeChar(val: number): void

Writes a character to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | **Char** value to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeChar(97);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readChar9+

readChar(): number

Reads the character from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **Char** value read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeChar(97);
  let ret = data.readChar();
  hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeString9+

writeString(val: string): void

Writes a string to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | string | Yes | String to write. The length of the string must be less than 40960 bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('abc');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readString9+

readString(): string

Reads the string from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | String read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeString('abc');
  let ret = data.readString();
  hilog.info(0x0000, 'testTag', 'readString is ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeParcelable9+

writeParcelable(val: Parcelable): void

Writes a **Parcelable** object to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | [Parcelable](#parcelable9) | Yes | **Parcelable** object to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor( num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readParcelable9+

readParcelable(dataIn: Parcelable): void

Reads the **Parcelable** object from this **MessageSequence** object to the specified object (**dataIn**).

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | [Parcelable](#parcelable9) | Yes | **Parcelable** object to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect.

 |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor( num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeByteArray9+

writeByteArray(byteArray: number\[\]): void

Writes a byte array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| byteArray | number\[\] | Yes | Byte array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  data.writeByteArray(ByteArrayVar);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readByteArray9+

readByteArray(dataIn: number\[\]): void

Reads the byte array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Byte array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  data.writeByteArray(ByteArrayVar);
  let array: Array<number> = new Array(5);
  data.readByteArray(array);
  hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readByteArray9+

readByteArray(): number\[\]

Reads the byte array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Byte array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  data.writeByteArray(ByteArrayVar);
  let array = data.readByteArray();
  hilog.info(0x0000, 'testTag', 'readByteArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeShortArray9+

writeShortArray(shortArray: number\[\]): void

Writes a short array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shortArray | number\[\] | Yes | Short array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray(\[11, 12, 13\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readShortArray9+

readShortArray(dataIn: number\[\]): void

Reads the short array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Short array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray(\[11, 12, 13\]);
  let array: Array<number> = new Array(3);
  data.readShortArray(array);
  hilog.info(0x0000, 'testTag', 'readShortArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readShortArray9+

readShortArray(): number\[\]

Reads the short array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Short array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeShortArray(\[11, 12, 13\]);
  let array = data.readShortArray();
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeIntArray9+

writeIntArray(intArray: number\[\]): void

Writes an integer array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| intArray | number\[\] | Yes | Integer array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray(\[100, 111, 112\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readIntArray9+

readIntArray(dataIn: number\[\]): void

Reads the integer array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Integer array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray(\[100, 111, 112\]);
  let array: Array<number> = new Array(3);
  data.readIntArray(array);
  hilog.info(0x0000, 'testTag', 'readIntArray is  ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readIntArray9+

readIntArray(): number\[\]

Reads the integer array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Integer array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeIntArray(\[100, 111, 112\]);
  let array = data.readIntArray();
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeLongArray9+

writeLongArray(longArray: number\[\]): void

Writes a long array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| longArray | number\[\] | Yes | Long array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray(\[1111, 1112, 1113\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readLongArray9+

readLongArray(dataIn: number\[\]): void

Reads the long array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Long array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray(\[1111, 1112, 1113\]);
  let array: Array<number> = new Array(3);
  data.readLongArray(array);
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readLongArray9+

readLongArray(): number\[\]

Reads the long integer array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Long array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeLongArray(\[1111, 1112, 1113\]);
  let array = data.readLongArray();
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeFloatArray9+

writeFloatArray(floatArray: number\[\]): void

Writes a double array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| floatArray | number\[\] | Yes | Double array to write. The system processes float data as that of the double type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray(\[1.2, 1.3, 1.4\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readFloatArray9+

readFloatArray(dataIn: number\[\]): void

Reads the double array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Double array to read. The system processes float data as that of the double type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray(\[1.2, 1.3, 1.4\]);
  let array: Array<number> = new Array(3);
  data.readFloatArray(array);
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readFloatArray9+

readFloatArray(): number\[\]

Reads the double array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Double array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeFloatArray(\[1.2, 1.3, 1.4\]);
  let array = data.readFloatArray();
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeDoubleArray9+

writeDoubleArray(doubleArray: number\[\]): void

Writes a double array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| doubleArray | number\[\] | Yes | Double array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The type of the element in the array is incorrect.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readDoubleArray9+

readDoubleArray(dataIn: number\[\]): void

Reads the double array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Double array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
  let array: Array<number> = new Array(3);
  data.readDoubleArray(array);
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readDoubleArray9+

readDoubleArray(): number\[\]

Reads the double array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Double array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
  let array = data.readDoubleArray();
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeBooleanArray9+

writeBooleanArray(booleanArray: boolean\[\]): void

Writes a Boolean array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| booleanArray | boolean\[\] | Yes | Boolean array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray(\[false, true, false\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readBooleanArray9+

readBooleanArray(dataIn: boolean\[\]): void

Reads the Boolean array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | boolean\[\] | Yes | Boolean array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray(\[false, true, false\]);
  let array: Array<boolean> = new Array(3);
  data.readBooleanArray(array);
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readBooleanArray9+

readBooleanArray(): boolean\[\]

Reads the Boolean array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean\[\] | Boolean array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeBooleanArray(\[false, true, false\]);
  let array = data.readBooleanArray();
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeCharArray9+

writeCharArray(charArray: number\[\]): void

Writes a character array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| charArray | number\[\] | Yes | Character array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray(\[97, 98, 88\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readCharArray9+

readCharArray(dataIn: number\[\]): void

Reads the character array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Character array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray(\[97, 98, 88\]);
  let array: Array<number> = new Array(3);
  data.readCharArray(array);
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readCharArray9+

readCharArray(): number\[\]

Reads the character array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Character array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeCharArray(\[97, 98, 88\]);
  let array = data.readCharArray();
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeStringArray9+

writeStringArray(stringArray: string\[\]): void

Writes a string array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stringArray | string\[\] | Yes | String array to write. The length of a single element in the array must be less than 40960 bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The string length is greater than or equal to 40960 bytes;

5.The number of bytes copied to the buffer is different from the length of the obtained string.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(\["abc", "def"\]);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readStringArray9+

readStringArray(dataIn: string\[\]): void

Reads the string array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | string\[\] | Yes | String array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(\["abc", "def"\]);
  let array: Array<string> = new Array(2);
  data.readStringArray(array);
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readStringArray9+

readStringArray(): string\[\]

Reads the string array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | String array read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  data.writeStringArray(\["abc", "def"\]);
  let array = data.readStringArray();
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeNoException9+

writeNoException(): void

Writes information to this **MessageSequence** object indicating that no exception occurred.

**System capability**: SystemCapability.Communication.IPC.Core

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteMessageRequest called');
      try {
        reply.writeNoException();
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorCode ' + e.code);
        hilog.error(0x0000, 'testTag', 'rpc write no exception fail, errorMessage ' + e.message);
      }
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}

#### \[h2\]readException9+

readException(): void

Reads the exception information from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/mUCxYQ6aRaiOkFtG20Fm-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FCD8201EC82DCB403F501585009F98F6F4F4D68C07E3652C5A8B202D0F07A22)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **sendMessageRequest()** of the proxy object is called to send a message.

import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
  
try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeNoException();
  data.writeInt(6);
  if (proxy != undefined) {
    proxy.sendMessageRequest(1, data, reply, option)
      .then((result: rpc.RequestResult) => {
        if (result.errCode === 0) {
          hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
          result.reply.readException();
          let num = result.reply.readInt();
          hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        } else {
          hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
        }
      }).catch((e: Error) => {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest got exception: ' + JSON.stringify(e));
      }).finally (() => {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
        data.reclaim();
        reply.reclaim();
      });
  }
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeParcelableArray9+

writeParcelableArray(parcelableArray: Parcelable\[\]): void

Writes the **Parcelable** array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parcelableArray | [Parcelable](#parcelable9)\[\] | Yes | **Parcelable** array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let parcelable2 = new MyParcelable(2, "bbb");
  let parcelable3 = new MyParcelable(3, "ccc");
  let a = \[parcelable, parcelable2, parcelable3\];
  let data = rpc.MessageSequence.create();
  data.writeParcelableArray(a);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
}

#### \[h2\]readParcelableArray9+

readParcelableArray(parcelableArray: Parcelable\[\]): void

Reads the **Parcelable** array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| parcelableArray | [Parcelable](#parcelable9)\[\] | Yes | **Parcelable** array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The length of the array passed when reading is not equal to the length passed when writing to the array;

5.The element does not exist in the array.

 |
| 1900010 | Failed to read data from the message sequence. |
| 1900012 | Failed to call the JS callback function. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let parcelable2 = new MyParcelable(2, "bbb");
  let parcelable3 = new MyParcelable(3, "ccc");
  let a = \[parcelable, parcelable2, parcelable3\];
  let data = rpc.MessageSequence.create();
  data.writeParcelableArray(a);
  let b = \[new MyParcelable(0, ""), new MyParcelable(0, ""), new MyParcelable(0, "")\];
  data.readParcelableArray(b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'rpc write parcelable array fail, errorMessage ' + e.message);
}

#### \[h2\]writeRemoteObjectArray9+

writeRemoteObjectArray(objectArray: IRemoteObject\[\]): void

Writes an **IRemoteObject** array to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| objectArray | [IRemoteObject](#iremoteobject)\[\] | Yes | **IRemoteObject** array to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The element does not exist in the array;

5.The obtained remoteObject is null.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")\];
  let data = rpc.MessageSequence.create();
  data.writeRemoteObjectArray(a);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readRemoteObjectArray9+

readRemoteObjectArray(objects: IRemoteObject\[\]): void

Reads the **IRemoteObject** array from this **MessageSequence** object and writes it to the created empty array.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| objects | [IRemoteObject](#iremoteobject)\[\] | Yes | **IRemoteObject** array to read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The length of the array passed when reading is not equal to the length passed when writing to the array.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")\];
  let data = rpc.MessageSequence.create();
  data.writeRemoteObjectArray(a);
  let b: Array<rpc.IRemoteObject> = new Array(3);
  data.readRemoteObjectArray(b);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readRemoteObjectArray9+

readRemoteObjectArray(): IRemoteObject\[\]

Reads the **IRemoteObject** array from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject)\[\] | The **IRemoteObject** array is returned. If an empty array is written, **null** is returned. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")\];
  let data = rpc.MessageSequence.create();
  let b = data.readRemoteObjectArray();
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]closeFileDescriptor9+

static closeFileDescriptor(fd: number): void

Closes a file descriptor. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to close. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageSequence.closeFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]dupFileDescriptor9+

static dupFileDescriptor(fd: number): number

Duplicates a file descriptor. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to duplicate. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | New file descriptor. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900013 | Failed to call dup. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageSequence.dupFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]containFileDescriptors9+

containFileDescriptors(): boolean

Checks whether this **MessageSequence** object contains file descriptors.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the **MessageSequence** object contains file descriptors; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  let containFD = sequence.containFileDescriptors();
  hilog.info(0x0000, 'testTag', 'sequence after write fd containFd result is ' + containFD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeFileDescriptor9+

writeFileDescriptor(fd: number): void

Writes a file descriptor to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  sequence.writeFileDescriptor(file.fd);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readFileDescriptor9+

readFileDescriptor(): number

Reads the file descriptor from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | File descriptor read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  sequence.writeFileDescriptor(file.fd);
  let readFD = sequence.readFileDescriptor();
  hilog.info(0x0000, 'testTag', 'readFileDescriptor is ' + readFD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeAshmem9+

writeAshmem(ashmem: Ashmem): void

Writes an anonymous shared object to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | Yes | Anonymous shared object to write. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter is not an instance of the Ashmem object.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let ashmem = rpc.Ashmem.create("ashmem", 1024);
  // Write data to ashmem.
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  // Write the ashmem object to the messageSequence object.
  sequence.writeAshmem(ashmem);
  // Write the size of the transferred data to this MessageSequence object.
  sequence.writeInt(size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readAshmem9+

readAshmem(): Ashmem

Reads the anonymous shared object from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | Anonymous share object obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let ashmem = rpc.Ashmem.create("ashmem", 1024);
  // Write data to ashmem.
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  // Write the size of the transferred data to this MessageSequence object.
  sequence.writeInt(size);
  // Write the ashmem object to the messageSequence object.
  sequence.writeAshmem(ashmem);

  // Read the size of the transferred data.
  let dataSize = sequence.readInt();
  // Read the ashmem object from this MessageSequence object.
  let ashmem1 = sequence.readAshmem();
  // Read data from the ashmem object.
  ashmem1.mapReadWriteAshmem();
  let readResult = ashmem1.readDataFromAshmem(dataSize, 0);
  let readInt32View = new Int32Array(readResult);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getRawDataCapacity9+

getRawDataCapacity(): number

Obtains the maximum amount of raw data that can be held by this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum amount of raw data that **MessageSequence** can hold, that is, 128 MB. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let result = sequence.getRawDataCapacity();
  hilog.info(0x0000, 'testTag', 'sequence get RawDataCapacity result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeRawData(deprecated)

writeRawData(rawData: number\[\], size: number): void

Writes raw data to this **MessageSequence** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/SsdliaNyR3SV0EUhqWDOwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C4E96FB42B47D386DB2AADE76BEEA7E3F733A89A2477ADF383A919EA6D242BA)

This API is supported since API version 9 and deprecated since API version 11. Use [writeRawDataBuffer](#writerawdatabuffer11) instead.

This API cannot be called for multiple times in one parcel communication.

When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case, pay attention to the SELinux configuration.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawData | number\[\] | Yes | Raw data to write. The size cannot exceed 128 MB. |
| size | number | Yes | Size of the raw data, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The transferred size cannot be obtained;

5.The transferred size is less than or equal to 0;

6.The element does not exist in the array;

7.Failed to obtain typedArray information;

8.The array is not of type int32;

9.The length of typedarray is smaller than the size of the original data sent.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let arr = \[1, 2, 3, 4, 5\];
  sequence.writeRawData(arr, arr.length);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeRawDataBuffer11+

writeRawDataBuffer(rawData: ArrayBuffer, size: number): void

Writes raw data to this **MessageSequence** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Q_YT7nPwQUqTPVuYRhJ5oQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0F453042D5BE60AC42A893070477F6B58A65778B203D33C6D97E4C9082F194B)

This API cannot be called for multiple times in one parcel communication.

When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case, pay attention to the SELinux configuration.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawData | ArrayBuffer | Yes | Raw data to write. The size cannot exceed 128 MB. |
| size | number | Yes | Size of the raw data, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain arrayBuffer information;

4.The transferred size cannot be obtained;

5.The transferred size is less than or equal to 0;

6.The transferred size is greater than the byte length of ArrayBuffer.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(64 \* 1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  let sequence = rpc.MessageSequence.create();
  sequence.writeRawDataBuffer(buffer, size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readRawData(deprecated)

readRawData(size: number): number\[\]

Reads raw data from this **MessageSequence** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/-HdP3sDLTiK_Iwm9To9DGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99659441D6FC71824D5FE604EC840557024E619EBFD82738FCFC3A18DED37FB9)

This API is supported since API version 9 and deprecated since API version 11. Use [readRawDataBuffer](#readrawdatabuffer11) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the raw data to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Raw data obtained, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let sequence = rpc.MessageSequence.create();
  let arr = \[1, 2, 3, 4, 5\];
  sequence.writeRawData(arr, arr.length);
  let size = arr.length;
  let result = sequence.readRawData(size);
  hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readRawDataBuffer11+

readRawDataBuffer(size: number): ArrayBuffer

Reads raw data from this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the raw data to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Raw data obtained, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(64 \* 1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  let sequence = rpc.MessageSequence.create();
  sequence.writeRawDataBuffer(buffer, size);
  let result = sequence.readRawDataBuffer(size);
  let readInt32View = new Int32Array(result);
  hilog.info(0x0000, 'testTag', 'sequence read raw data result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeArrayBuffer12+

writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void

Writes data of the ArrayBuffer type to this **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Data to write. |
| typeCode | [TypeCode](#typecode12) | Yes | 
TypedArray type of the ArrayBuffer data.

The underlying write mode is determined based on the enum value of **TypeCode** passed by the service.

 |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The parameter is an empty array;

2.The number of parameters is incorrect;

3.The parameter type does not match;

4.The obtained value of typeCode is incorrect;

5.Failed to obtain arrayBuffer information.

 |
| 1900009 | Failed to write data to the message sequence. |

**Example**

// In this example, the value of TypeCode is Int16Array.
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let buffer = new ArrayBuffer(10);
  let int16View = new Int16Array(buffer);
  for (let i = 0; i < int16View.length; i++) {
    int16View\[i\] = i \* 2 + 1;
  }
  data.writeArrayBuffer(buffer, rpc.TypeCode.INT16\_ARRAY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readArrayBuffer12+

readArrayBuffer(typeCode: TypeCode): ArrayBuffer

Reads data of the ArrayBuffer type from this **MessageSequence**.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| typeCode | [TypeCode](#typecode12) | Yes | 
TypedArray type of the ArrayBuffer data.

The underlying read mode is determined based on the enum value of **TypeCode** passed by the service.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Data of the ArrayBuffer type read, in bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The obtained value of typeCode is incorrect;

 |
| 1900010 | Failed to read data from the message sequence. |

**Example**

// In this example, the value of TypeCode is Int16Array.
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data = rpc.MessageSequence.create();
  let buffer = new ArrayBuffer(10);
  let int16View = new Int16Array(buffer);
  for (let i = 0; i < int16View.length; i++) {
    int16View\[i\] = i \* 2 + 1;
  }
  data.writeArrayBuffer(buffer, rpc.TypeCode.INT16\_ARRAY);
  let result = data.readArrayBuffer(rpc.TypeCode.INT16\_ARRAY);
  let readInt16View = new Int16Array(result);
  hilog.info(0x0000, 'testTag', 'read ArrayBuffer result is ' + readInt16View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### MessageParcel(deprecated)

Provides APIs for reading and writing data in specific format. During RPC, the sender can use the **write()** method provided by **MessageParcel** to write data in specific format to a **MessageParcel** object. The receiver can use the **read()** method provided by **MessageParcel** to read data in specific format from a **MessageParcel** object. The data formats include basic data types and arrays, IPC objects, interface tokens, and custom sequenceable objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/4nHg-EPOSHmvudD0QlGlHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D408FC37F0315D0887AED32A8F55D7FF1C9DDE8591FA1DE921905761B8D3F069)

This API is supported since API version 7 and deprecated since API version 9. Use [MessageSequence](#messagesequence9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]create(deprecated)

static create(): MessageParcel

Creates a **MessageParcel** object. This method is a static method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/RLgoUyomRmOngBP4iSAANA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEACA451DFB4DCA5C5B43CAB39D48227D0744BF0F0C0351E6C3ED9EE55404E47)

This API is supported since API version 7 and deprecated since API version 9. Use [create](#create9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MessageParcel](#messageparceldeprecated) | **MessageParcel** object created. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  hilog.info(0x0000, 'testTag', 'data is ' + data);

  // When the MessageParcel object is no longer used, the service calls the reclaim method to release resources.
  data.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]reclaim(deprecated)

reclaim(): void

Reclaims the **MessageParcel** object that is no longer used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/LkHdzCuRT_SVD7rywskwIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E58FDA25B2A2581994BA2D2433077AA868FAB8E494572065D92878FEC6F6BE43)

This API is supported since API version 7 and deprecated since API version 9. Use [reclaim](#reclaim9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let reply = rpc.MessageParcel.create();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeRemoteObject(deprecated)

writeRemoteObject(object: IRemoteObject): boolean

Serializes a remote object and writes it to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/R0k95cVtQlmJsVvJoKgOYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0D3E76F4794356092BC874682A0A17399C5C3DFBED7766316C8413FDA9F6F3A)

This API is supported since API version 7 and deprecated since API version 9. Use [writeRemoteObject](#writeremoteobject9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | Yes | Remote object to serialize and write to the **MessageParcel** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readRemoteObject(deprecated)

readRemoteObject(): IRemoteObject

Reads the remote object from this **MessageParcel** object. You can use this method to deserialize the **MessageParcel** object to generate an **IRemoteObject**. The remote objects are read in the order in which they are written to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/A9HCYH5eQbK6MCgIXoe1Mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0868733805A513587DC109C5E30DC0657CF9A1B785DB46A9CCF372A9B979E56)

This API is supported since API version 7 and deprecated since API version 9. Use [readRemoteObject](#readremoteobject9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | Remote object obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let data = rpc.MessageParcel.create();
  let testRemoteObject = new TestRemoteObject("testObject");
  data.writeRemoteObject(testRemoteObject);
  let proxy = data.readRemoteObject();
  hilog.info(0x0000, 'testTag', 'readRemoteObject is ' + proxy);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeInterfaceToken(deprecated)

writeInterfaceToken(token: string): boolean

Writes an interface token to this **MessageParcel** object. The remote object can use this interface token to verify the communication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/tKXgwlrLRVS8Ukb7Co2YhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B9D13F772E61E93F57D5D93928EB8FBDE4BAC400B7DFBF4EB810FFB73EA3FC6)

This API is supported since API version 7 and deprecated since API version 9. Use [writeInterfaceToken](#writeinterfacetoken9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| token | string | Yes | Interface token to write. The length of the string must be less than 40960 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  hilog.info(0x0000, 'testTag', 'RpcServer: writeInterfaceToken is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readInterfaceToken(deprecated)

readInterfaceToken(): string

Reads the interface token from this **MessageParcel** object. The interface token is read in the sequence in which it is written to the **MessageParcel** object. The local object can use it to verify the communication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/c6MREWTAQi-VcymVhaQVNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B54B68916D8B7D7A03DAFB0274D54DFF0D5F534B4722D8CFE4BDD21E96AF64A)

This API is supported since API version 7 and deprecated since API version 9. Use [readInterfaceToken](#readinterfacetoken9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface token obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInterfaceToken("aaa");
  let interfaceToken = data.readInterfaceToken();
  hilog.info(0x0000, 'testTag', 'RpcServer: interfaceToken is ' + interfaceToken);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getSize(deprecated)

getSize(): number

Obtains the data size of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/9OE9Bx6uRa-E4yncpwZpxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=190A83A0B06C5A3DF57B2070073F44B1A99017DF03572AF958718E13FE681D30)

This API is supported since API version 7 and deprecated since API version 9. Use [getSize](#getsize9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Size of the **MessageParcel** object obtained, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let size = data.getSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getCapacity(deprecated)

getCapacity(): number

Obtains the capacity of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/rXkJAc26T0-CiD0-WiU0ug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B4401718471392A2427537DA13A5A70971426240CDAC90995494104014F1FBF)

This API is supported since API version 7 and deprecated since API version 9. Use [getCapacity](#getcapacity9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **MessageParcel** capacity obtained, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.getCapacity();
  hilog.info(0x0000, 'testTag', 'capacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]setSize(deprecated)

setSize(size: number): boolean

Sets the size of data contained in this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/urTM7SnPTlOOD-5BatCBWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4169D3D2AA4E8B45A3D13AFA7AAD9BB3493C8C41E1C2185601AEC47FEBFFDB1)

This API is supported since API version 7 and deprecated since API version 9. Use [setSize](#setsize9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Data size to set, in bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let setSize = data.setSize(16);
  hilog.info(0x0000, 'testTag', 'setSize is ' + setSize);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]setCapacity(deprecated)

setCapacity(size: number): boolean

Sets the storage capacity of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/F82SvTrxREmdxnm56R3Stg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A98F318BBB4C23910F271EFA039882B190BFD8138B81C2A71E73187CD0E2A55)

This API is supported since API version 7 and deprecated since API version 9. Use [setCapacity](#setcapacity9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Storage capacity to set, in bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.setCapacity(100);
  hilog.info(0x0000, 'testTag', 'setCapacity is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getWritableBytes(deprecated)

getWritableBytes(): number

Obtains the writable capacity of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/r5Hya1URRA2hFpzqmbXRTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24890A1826DBF989ECFFF3D0F7BBFE9AEE2B18C0C87DC320500CA2CD27AAF303)

This API is supported since API version 7 and deprecated since API version 9. Use [getWritableBytes](#getwritablebytes9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **MessageParcel** writable capacity obtained, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let getWritableBytes = data.getWritableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getWritableBytes is ' + getWritableBytes);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getReadableBytes(deprecated)

getReadableBytes(): number

Obtains the readable capacity of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_AsRJr3BQwK3Xh5qoOVixw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15F104734431907E158BE6F442BF1EDFE07338812982E33391ABE7485CA0A596)

This API is supported since API version 7 and deprecated since API version 9. Use [getReadableBytes](#getreadablebytes9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **MessageParcel** object readable capacity, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(1);
  let result = data.getReadableBytes();
  hilog.info(0x0000, 'testTag', 'RpcServer: getReadableBytes is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getReadPosition(deprecated)

getReadPosition(): number

Obtains the read position of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/OjuqJNE3QG-bQ4K1s_E-uQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D0452F7CA8CD9E38AA1D06D6C46218CA9D06D36CB7C2BCCD3E5239CB8B060D1)

This API is supported since API version 7 and deprecated since API version 9. Use [getReadPosition](#getreadposition9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current read position of the **MessageParcel** object. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let readPos = data.getReadPosition();
  hilog.info(0x0000, 'testTag', 'readPos is ' + readPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getWritePosition(deprecated)

getWritePosition(): number

Obtains the write position of this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/RhxjF-ztRd6XImQb-cDBVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6031A8A03E3F2840A8540F68C6D6BEA80604A163AE9F176DB5440E30BB36C74)

This API is supported since API version 7 and deprecated since API version 9. Use [getWritePosition](#getwriteposition9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current write position of the **MessageParcel** object. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(10);
  let bwPos = data.getWritePosition();
  hilog.info(0x0000, 'testTag', 'bwPos is ' + bwPos);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]rewindRead(deprecated)

rewindRead(pos: number): boolean

Moves the read pointer to the specified position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/pfebw4XcRgGAThKQJTMEzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C64FF31FE124E0CBABCB15D26C4F5503554A9B4AD01DED6C77D58C6682EFE680)

This API is supported since API version 7 and deprecated since API version 9. Use [rewindRead](#rewindread9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pos | number | Yes | Position from which data is to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the read position changes; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(12);
  data.writeString("parcel");
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'number is ' + number);
  data.rewindRead(0);
  let number2 = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindRead is ' + number2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]rewindWrite(deprecated)

rewindWrite(pos: number): boolean

Moves the write pointer to the specified position.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/g7CsyEfuRzyXbrOjVM9Rlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A780C289E781A6582D0F6C82F100940E0C445A2AC68DBD21515E48C373EDCD04)

This API is supported since API version 7 and deprecated since API version 9. Use [rewindWrite](#rewindwrite9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pos | number | Yes | Position from which data is to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the write position changes; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  data.writeInt(4);
  data.rewindWrite(0);
  data.writeInt(5);
  let number = data.readInt();
  hilog.info(0x0000, 'testTag', 'rewindWrite is ' + number);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeByte(deprecated)

writeByte(val: number): boolean

Writes a Byte value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_DJgxYnKQKmJysKq_YzgyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B5BC948A1601C789BEF0BBCA9F23A9526E9402F2E5C79751AE237F7F0E95BF1)

This API is supported since API version 7 and deprecated since API version 9. Use [writeByte](#writebyte9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Byte value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readByte(deprecated)

readByte(): number

Reads the byte value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/4KQleMzgRYeR5MgysbXXDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AC588AC90B769C7503CEC1C30286DA09C84FDDB1CDAF5CCF7C69450F2023DDD)

This API is supported since API version 7 and deprecated since API version 9. Use [readByte](#readbyte9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Byte value read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeByte(2);
  hilog.info(0x0000, 'testTag', 'writeByte is ' + result);
  let ret = data.readByte();
  hilog.info(0x0000, 'testTag', 'readByte is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeShort(deprecated)

writeShort(val: number): boolean

Writes a short int value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/IeWBpJ9OSBSUiFsIB2gRNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDD299C2F3B6113C9E48B8DDDDF0058656967E345B240F90D4BE130E5F8768A7)

This API is supported since API version 7 and deprecated since API version 9. Use [writeShort](#writeshort9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Short integer to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readShort(deprecated)

readShort(): number

Reads the short integer from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ohdFCsS8RfqKv_mf76covg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=283F2C338C60DBB9B155764EBE053967D2987EE4160EF6402F215F4A98B5C2C4)

This API is supported since API version 7 and deprecated since API version 9. Use [readShort](#readshort9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Short integer read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShort(8);
  hilog.info(0x0000, 'testTag', 'writeShort is ' + result);
  let ret = data.readShort();
  hilog.info(0x0000, 'testTag', 'readShort is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeInt(deprecated)

writeInt(val: number): boolean

Writes an int value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/DhttcjDYSY-JsC_VOmI-lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA11CCC1E51EAC494F24B1BFF14AB28D9E99DCDCB446DFAA5DDC7D2D1BD7DF88)

This API is supported since API version 7 and deprecated since API version 9. Use [writeInt](#writeint9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Integer to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readInt(deprecated)

readInt(): number

Reads the integer from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/wQ9xvMVRRWSQLvuZYZfFlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A028E1782A6B942D1425A1C39FEB534E452E8A6674142B8F76AC5D95530164AF)

This API is supported since API version 7 and deprecated since API version 9. Use [readInt](#readint9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Integer read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeInt(10);
  hilog.info(0x0000, 'testTag', 'writeInt is ' + result);
  let ret = data.readInt();
  hilog.info(0x0000, 'testTag', 'readInt is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeLong(deprecated)

writeLong(val: number): boolean

Writes a long int value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/cgaKTBrzQ9-uAmjQWzFFXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46E324E3E8BA61058928B87C2C004458F2D0CAA433D7A01B0E81D7BEAE1F992E)

This API is supported since API version 7 and deprecated since API version 9. Use [writeLong](#writelong9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Long int value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readLong(deprecated)

readLong(): number

Reads the long int value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/hIBdFVaWSsCvex0lzagGYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D9214107D5AB0D9D4B3334E6A5844BFDC3CE37950F2D00F5CD72B799534734A)

This API is supported since API version 7 and deprecated since API version 9. Use [readLong](#readlong9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Long integer read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLong(10000);
  hilog.info(0x0000, 'testTag', 'writeLong is ' + result);
  let ret = data.readLong();
  hilog.info(0x0000, 'testTag', 'readLong is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeFloat(deprecated)

writeFloat(val: number): boolean

Writes a double value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/l5V8f49qR1KO0XLy1KL74A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9727CF56CCBB09F14CAA3108CF7796571229CA7BE8FCD9498DC08C70D9E33DFC)

This API is supported since API version 7 and deprecated since API version 9. Use [writeFloat](#writefloat9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Double value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readFloat(deprecated)

readFloat(): number

Reads the double value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/eooficF5QkC2aIbiszVq3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BC46670151821065FC6D75793CA8DC82CDBF848C61C4017E5C612CDD6C37005)

This API is supported since API version 7 and deprecated since API version 9. Use [readFloat](#readfloat9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Double value read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloat(1.2);
  hilog.info(0x0000, 'testTag', 'writeFloat is ' + result);
  let ret = data.readFloat();
  hilog.info(0x0000, 'testTag', 'readFloat is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeDouble(deprecated)

writeDouble(val: number): boolean

Writes a double value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/75KTucfjTAyn_B3NWyfeXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FA5027EFBB10DF612F1EE1A29377EBD7E5FFFB6BC2508F999F3B24806B8F1D5)

This API is supported since API version 7 and deprecated since API version 9. Use [writeDouble](#writedouble9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | Double value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readDouble(deprecated)

readDouble(): number

Reads the double value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/g065vf4kSOqbWmdWujiPbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D36FE2BEB74976FF13937CB4D191239419C6ACA460159340A6DFA9609C86C55A)

This API is supported since API version 7 and deprecated since API version 9. Use [readDouble](#readdouble9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Double value read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDouble(10.2);
  hilog.info(0x0000, 'testTag', 'writeDouble is ' + result);
  let ret = data.readDouble();
  hilog.info(0x0000, 'testTag', 'readDouble is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeBoolean(deprecated)

writeBoolean(val: boolean): boolean

Writes a Boolean value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/1-ARWRWMRzi1QgIwUcX86A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=295AE07A39C55B3D99F927F40789AEF6B8AA514315AACFBA28E9EB0DCF791CFE)

This API is supported since API version 7 and deprecated since API version 9. Use [writeBoolean](#writeboolean9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | boolean | Yes | Boolean value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readBoolean(deprecated)

readBoolean(): boolean

Reads the Boolean value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1PRS_IakR1y1CRYevia59w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF78F1E5DBA8F92B308C8C4768A598ACB64AEACB7AF30BE565DE12B4A5D30DFA)

This API is supported since API version 7 and deprecated since API version 9. Use [readBoolean](#readboolean9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBoolean(false);
  hilog.info(0x0000, 'testTag', 'writeBoolean is ' + result);
  let ret = data.readBoolean();
  hilog.info(0x0000, 'testTag', 'readBoolean is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeChar(deprecated)

writeChar(val: number): boolean

Writes a single character value to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/oXlGfzcFR0SFVBTzhXOPFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21BF708302224251FE3A07327E1AE1980E22CBAE1AEB209D05CE61515BF4A4D0)

This API is supported since API version 7 and deprecated since API version 9. Use [writeChar](#writechar9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | number | Yes | **Char** value to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readChar(deprecated)

readChar(): number

Reads the single character value from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/10Va8daXR8mBvU9Rtk28wQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60A14D98A48760BD60FD069B2DBDC0728F0EC96C2B9C7FE67F6D4EAF619F2CEF)

This API is supported since API version 7 and deprecated since API version 9. Use [readChar](#readchar9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **Char** value read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeChar(97);
  hilog.info(0x0000, 'testTag', 'writeChar is ' + result);
  let ret = data.readChar();
  hilog.info(0x0000, 'testTag', 'readChar is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeString(deprecated)

writeString(val: string): boolean

Writes a string to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/0jiEG_0cTA6taBnxJY9AyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EFD2FB5882C5828B8B586A5AD6B473D85D450B0269CA2E60FC84B44798E3202)

This API is supported since API version 7 and deprecated since API version 9. Use [writeString](#writestring9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | string | Yes | String to write. The length of the string must be less than 40960 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readString(deprecated)

readString(): string

Reads the string from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/nUkYuQdrT1i0esdBvfw23A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79708DCF6BE95D76FAD01963BFA101ABF44D8D992FC6FE30485295D4BD3E58DD)

This API is supported since API version 7 and deprecated since API version 9. Use [readString](#readstring9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | String read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeString('abc');
  hilog.info(0x0000, 'testTag', 'writeString is ' + result);
  let ret = data.readString();
  hilog.info(0x0000, 'testTag', 'readString is ' + ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeSequenceable(deprecated)

writeSequenceable(val: Sequenceable): boolean

Writes a **Sequenceable** object to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/-hHWPrxdRKGdBvGug-31mQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=065F26F6EEA854E9C7B0193E93513D994E564C265D2A361137CAE09F02999D49)

This API is supported since API version 7 and deprecated since API version 9. Use [writeParcelable](#writeparcelable9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| val | [Sequenceable](#sequenceabledeprecated) | Yes | **Sequenceable** object to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readSequenceable(deprecated)

readSequenceable(dataIn: Sequenceable): boolean

Reads member variables from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/HKIpC40GTvGC_t7jtdwL8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=604DF1FAF366FE0F03925BD415A613B9D13F7E0232545F3B733B770D5CB42F0A)

This API is supported since API version 7 and deprecated since API version 9. Use [readParcelable](#readparcelable9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | [Sequenceable](#sequenceabledeprecated) | Yes | Object that reads member variables from the **MessageParcel** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeByteArray(deprecated)

writeByteArray(byteArray: number\[\]): boolean

Writes a byte array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/hUV8dq8WTjGOxaLMGCf19A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=871BA1D91B8EC7E5EE4DAC1754CE83B2205D3F6FED8335B6600C317915AA27DF)

This API is supported since API version 7 and deprecated since API version 9. Use [writeByteArray](#writebytearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| byteArray | number\[\] | Yes | Byte array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readByteArray(deprecated)

readByteArray(dataIn: number\[\]): void

Reads the byte array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/xLxe8ZLzT2iXsSuQFkm9Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0255CB6272982437C2A4CB8CC5171DE844F7B021DFDDCC281B91C69DCA065FD2)

This API is supported since API version 7 and deprecated since API version 9. Use [readByteArray](#readbytearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Byte array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  let result = data.writeByteArray(ByteArrayVar);
  let array: Array<number> = new Array(5);
  data.readByteArray(array);
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readByteArray(deprecated)

readByteArray(): number\[\]

Reads the byte array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/J7kbzBgKQlqRrxpmSSa6IA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25FB3BD81ED5135B49F0405EA60EB5C3904681E9E98F9EA609E60A9E4C0179F3)

This API is supported since API version 7 and deprecated since API version 9. Use [readByteArray](#readbytearray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Byte array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  let result = data.writeByteArray(ByteArrayVar);
  hilog.info(0x0000, 'testTag', 'writeByteArray is ' + result);
  let array = data.readByteArray();
  hilog.info(0x0000, 'testTag', 'readByteArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeShortArray(deprecated)

writeShortArray(shortArray: number\[\]): boolean

Writes a short array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/nQgTcdRGRNut-eleKXcXGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48683648A8B4542A2B1A0A4C2DCD0A40A9339D8A9358DC927D02635E44DF9A05)

This API is supported since API version 7 and deprecated since API version 9. Use [writeShortArray](#writeshortarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shortArray | number\[\] | Yes | Short array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray(\[11, 12, 13\]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readShortArray(deprecated)

readShortArray(dataIn: number\[\]): void

Reads the short array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/a8YH18NGTpOvEHfQKwPYJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=299997746218A1550613EBB677E7ED946D0C14C5B7147A5E2F9B70C53387C030)

This API is supported since API version 7 and deprecated since API version 9. Use [readShortArray](#readshortarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Short array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray(\[11, 12, 13\]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readShortArray(array);
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readShortArray(deprecated)

readShortArray(): number\[\]

Reads the short array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/c0bSX8xSTp6jl9zUyrRLHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AEF09A829708B7820F250DFCF2635034DE4E8187BF3FB8BBCCA75B9563CFA9F)

This API is supported since API version 7 and deprecated since API version 9. Use [readShortArray](#readshortarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Short array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeShortArray(\[11, 12, 13\]);
  hilog.info(0x0000, 'testTag', 'writeShortArray is ' + result);
  let array = data.readShortArray();
  hilog.info(0x0000, 'testTag', 'readShortArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeIntArray(deprecated)

writeIntArray(intArray: number\[\]): boolean

Writes an integer array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4mq_CXJ6RE2McniltmqcPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33BD717D31B14DC4F75D289DBD9422A311F5C3B7A43BF8321D47F574307E6C81)

This API is supported since API version 7 and deprecated since API version 9. Use [writeIntArray](#writeintarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| intArray | number\[\] | Yes | Integer array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray(\[100, 111, 112\]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readIntArray(deprecated)

readIntArray(dataIn: number\[\]): void

Reads the integer array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/uwzX2lzbT5Ku_9Pp1gy5og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4457917C7E2C10DA1D45D5507DA27FE8E1B918CB942794227EF57D68970465B9)

This API is supported since API version 7 and deprecated since API version 9. Use [readIntArray](#readintarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Integer array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray(\[100, 111, 112\]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readIntArray(array);
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readIntArray(deprecated)

readIntArray(): number\[\]

Reads the integer array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/3b8OtOWvRWS0uPWhgvslIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53DA3555DBA8CE4C0BE4AE33A2190DB62880E989F2DB3FF789EDF12DC35668AE)

This API is supported since API version 7 and deprecated since API version 9. Use [readIntArray](#readintarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Integer array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeIntArray(\[100, 111, 112\]);
  hilog.info(0x0000, 'testTag', 'writeIntArray is ' + result);
  let array = data.readIntArray();
  hilog.info(0x0000, 'testTag', 'readIntArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeLongArray(deprecated)

writeLongArray(longArray: number\[\]): boolean

Writes a long array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/qNNluiQuT_eTv4CrM4PEPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CDB628E177075681508293795D009F6CD255E516FD1174CF79BA2FCC9716AF6)

This API is supported since API version 7 and deprecated since API version 9. Use [writeLongArray](#writelongarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| longArray | number\[\] | Yes | Long array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray(\[1111, 1112, 1113\]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readLongArray(deprecated)

readLongArray(dataIn: number\[\]): void

Reads the long array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/3EnYk8wsTvSO41FILrh-Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9504C61BAFB84EA1CA75A2D00EAF63A73A02B6D25C8BC143924FB26BEC2DBC18)

This API is supported since API version 7 and deprecated since API version 9. Use [readLongArray](#readlongarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Long array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray(\[1111, 1112, 1113\]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readLongArray(array);
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readLongArray(deprecated)

readLongArray(): number\[\]

Reads the long array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/9T8MHaB5Qve6TBnwLff89g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ADCF69A4E8F61DE2BBE36EAD2D8BA616D18EA8493181F81EB4B238BCC9D1D93)

This API is supported since API version 7 and deprecated since API version 9. Use [readLongArray](#readlongarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Long array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeLongArray(\[1111, 1112, 1113\]);
  hilog.info(0x0000, 'testTag', 'writeLongArray is ' + result);
  let array = data.readLongArray();
  hilog.info(0x0000, 'testTag', 'readLongArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeFloatArray(deprecated)

writeFloatArray(floatArray: number\[\]): boolean

Writes a double array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/IFKUpDsHRNGyYdaMMEp77Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1090AB94F943B59CF9E27546D5FC1C7849B851FF34B53AC813834A20C87CE0A)

This API is supported since API version 7 and deprecated since API version 9. Use [writeFloatArray](#writefloatarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| floatArray | number\[\] | Yes | Double array to write. The system processes float data as that of the double type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray(\[1.2, 1.3, 1.4\]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readFloatArray(deprecated)

readFloatArray(dataIn: number\[\]): void

Reads the double array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/y-ABNosWRuWItM4m6zGCmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60DA36F1F0BE38671DDFB8C29CE5B6B007C58E3669A7A51CB5FFE623CEFB82B3)

This API is supported since API version 7 and deprecated since API version 9. Use [readFloatArray](#readfloatarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Double array to read. The system processes float data as that of the double type. Therefore, the total number of bytes occupied by a float array must be calculated as the double type. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray(\[1.2, 1.3, 1.4\]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readFloatArray(array);
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readFloatArray(deprecated)

readFloatArray(): number\[\]

Reads the double array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Ju08TCntS7qq8QAkmwiRQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=852A8AA8A984CC9552E02E64838259EA0F68302821224DA3EEEE53C6637F3F0D)

This API is supported since API version 7 and deprecated since API version 9. Use [readFloatArray](#readfloatarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Double array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeFloatArray(\[1.2, 1.3, 1.4\]);
  hilog.info(0x0000, 'testTag', 'writeFloatArray is ' + result);
  let array = data.readFloatArray();
  hilog.info(0x0000, 'testTag', 'readFloatArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeDoubleArray(deprecated)

writeDoubleArray(doubleArray: number\[\]): boolean

Writes a double array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/c6P6AaHnSQKOBnz4bPixMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EAE5446C40ACBD9C69D0FA53C26A17F562E151BBF57BDF3EDC1876E2021796E)

This API is supported since API version 7 and deprecated since API version 9. Use [writeDoubleArray](#writedoublearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| doubleArray | number\[\] | Yes | Double array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readDoubleArray(deprecated)

readDoubleArray(dataIn: number\[\]): void

Reads the double array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bt9PMYsjRyK22ofwq0yXUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CFC1CDB75559C267B5052EDA485E3E514C14A556C3D3E937688677EBA662371)

This API is supported since API version 7 and deprecated since API version 9. Use [readDoubleArray](#readdoublearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Double array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readDoubleArray(array);
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readDoubleArray(deprecated)

readDoubleArray(): number\[\]

Reads the double array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/2udpfwHMTTOqsss8jQZf_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E96BF1E568336F3746DDB06A565007F299D96EC99F271B4EB3113CECB8DD446B)

This API is supported since API version 7 and deprecated since API version 9. Use [readDoubleArray](#readdoublearray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Double array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeDoubleArray(\[11.1, 12.2, 13.3\]);
  hilog.info(0x0000, 'testTag', 'writeDoubleArray is ' + result);
  let array = data.readDoubleArray();
  hilog.info(0x0000, 'testTag', 'readDoubleArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeBooleanArray(deprecated)

writeBooleanArray(booleanArray: boolean\[\]): boolean

Writes a Boolean array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/X8hpC-FKQ_OS_MygzF-3qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C1E8FEA693E1ABBA02D5B0797AFD90D02E052715F9546B034E3D7B722E016D5)

This API is supported since API version 7 and deprecated since API version 9. Use [writeBooleanArray](#writebooleanarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| booleanArray | boolean\[\] | Yes | Boolean array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray(\[false, true, false\]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readBooleanArray(deprecated)

readBooleanArray(dataIn: boolean\[\]): void

Reads the Boolean array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/hOR8LUtJQ3OY8YPUUT6mww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD4D2088390659844E553E0B3A5B3144DDF06831F05ED27FBFCEF5E9F9421D38)

This API is supported since API version 7 and deprecated since API version 9. Use [readBooleanArray](#readbooleanarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | boolean\[\] | Yes | Boolean array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray(\[false, true, false\]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array: Array<boolean> = new Array(3);
  data.readBooleanArray(array);
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readBooleanArray(deprecated)

readBooleanArray(): boolean\[\]

Reads the Boolean array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/ky0TsP0sQqC6vp0q46MLVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E4503A323561869EE5CB2515E8C89959A2FC92267979E6C88B9762CC9474454)

This API is supported since API version 7 and deprecated since API version 9. Use [readBooleanArray](#readbooleanarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean\[\] | Boolean array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeBooleanArray(\[false, true, false\]);
  hilog.info(0x0000, 'testTag', 'writeBooleanArray is ' + result);
  let array = data.readBooleanArray();
  hilog.info(0x0000, 'testTag', 'readBooleanArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeCharArray(deprecated)

writeCharArray(charArray: number\[\]): boolean

Writes a single character array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/gP8tMOzCTu-AgPgxq5xYGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D2CC979C24A3FB5224C297544E53B6AA324960EB514161FFFDC2E458FF2D709)

This API is supported since API version 7 and deprecated since API version 9. Use [writeCharArray](#writechararray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| charArray | number\[\] | Yes | Character array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray(\[97, 98, 88\]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readCharArray(deprecated)

readCharArray(dataIn: number\[\]): void

Reads the character array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/zeomgLAPTtapEftiAdEFww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D4A35167A8D738C62C79D3D394E53C90632DA7D07E4BA9A0E1FE05921CCD389)

This API is supported since API version 7 and deprecated since API version 9. Use [readCharArray](#readchararray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | number\[\] | Yes | Character array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray(\[97, 98, 99\]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array: Array<number> = new Array(3);
  data.readCharArray(array);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readCharArray(deprecated)

readCharArray(): number\[\]

Reads the single character array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/0ek_yRjCQtSdWKfdyEhVqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=886EE5D79105B6AD838A445C46A247A85FE35208A1C74AF0B9F5261F39162CF5)

This API is supported since API version 7 and deprecated since API version 9. Use [readCharArray](#readchararray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Character array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeCharArray(\[97, 98, 99\]);
  hilog.info(0x0000, 'testTag', 'writeCharArray is ' + result);
  let array = data.readCharArray();
  hilog.info(0x0000, 'testTag', 'readCharArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeStringArray(deprecated)

writeStringArray(stringArray: string\[\]): boolean

Writes a string array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/GVI1exDwQ_GkNqUvKBQBfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFEC6EA1E60A543E5541C0EF92BECED08FFEC31D51E067F37FAC716DF9C124CA)

This API is supported since API version 7 and deprecated since API version 9. Use [writeStringArray](#writestringarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| stringArray | string\[\] | Yes | String array to write. The length of a single element in the array must be less than 40960 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(\["abc", "def"\]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readStringArray(deprecated)

readStringArray(dataIn: string\[\]): void

Reads the string array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/l1HvJc65Q_yMu6GCLuggWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E08BC16AAFF0E6B5EE5FC351CDB63D9BC356804D2E88FC520B67DE1A9CEF416E)

This API is supported since API version 7 and deprecated since API version 9. Use [readStringArray](#readstringarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | string\[\] | Yes | String array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(\["abc", "def"\]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array: Array<string> = new Array(2);
  data.readStringArray(array);
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readStringArray(deprecated)

readStringArray(): string\[\]

Reads the string array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/fz8vgCU5SACfsBAyOuPHHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC929BC7C804CB9F6529BA44A2CA97B788457937C75C71510EF6C75F9F240FD9)

This API is supported since API version 7 and deprecated since API version 9. Use [readStringArray](#readstringarray9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string\[\] | String array read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let data = rpc.MessageParcel.create();
  let result = data.writeStringArray(\["abc", "def"\]);
  hilog.info(0x0000, 'testTag', 'writeStringArray is ' + result);
  let array = data.readStringArray();
  hilog.info(0x0000, 'testTag', 'readStringArray is ' + array);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeNoException(deprecated)

writeNoException(): void

Writes information to this **MessageParcel** object indicating that no exception occurred.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/TpJH8u2IQW6nuW40yFuQQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A576EB6513F8657ADDFA6F3B712D6DFB984E83635424E7C0F6A33835755620C)

This API is supported since API version 8 and deprecated since API version 9. Use [writeNoException](#writenoexception9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      reply.writeNoException();
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}

#### \[h2\]readException(deprecated)

readException(): void

Reads the exception information from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/r8UlT2BjRSekZEhSx6mNNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27F9D125F62CC456E507F269D5AC692E330966DBFFDD15A5B1F450712B2BE465)

This API is supported since API version 8 and deprecated since API version 9. Use [readException](#readexception9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tAkS0qVGSvuJupP348Eg8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=994361B809CCD055AA614B00FD32A55A30434127948BC2D09606896195BE760D)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **sendRequest()** of the proxy object is called to send a message.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeNoException();
  data.writeString('hello');
  if (proxy != undefined) {
    let a = proxy.sendRequest(1, data, reply, option) as Object;
    let b = a as Promise<rpc.SendRequestResult>;
    b.then((result: rpc.SendRequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendRequest got result');
        result.reply.readException();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendRequest got exception: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeSequenceableArray(deprecated)

writeSequenceableArray(sequenceableArray: Sequenceable\[\]): boolean

Writes a **Sequenceable** array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/HGAsxkpdQZGMMGu55sb3Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77AE63BFD5BB5B96C1EFE33395C4D9C72DF9F8E331CBA03988DDE10A75D6911D)

This API is supported since API version 7 and deprecated since API version 9. Use [writeParcelableArray](#writeparcelablearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequenceableArray | [Sequenceable](#sequenceabledeprecated)\[\] | Yes | **Sequenceable** array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = \[sequenceable, sequenceable2, sequenceable3\];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readSequenceableArray(deprecated)

readSequenceableArray(sequenceableArray: Sequenceable\[\]): void

Reads the **Sequenceable** array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/L2-NV2cLSFG7gw6gqe3szQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7068D35F77D75F67287BF9B85680705B2767D43E1D8C9762AFF41D0CC9780E70)

This API is supported since API version 8 and deprecated since API version 9. Use [readParcelableArray](#readparcelablearray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sequenceableArray | [Sequenceable](#sequenceabledeprecated)\[\] | Yes | **Sequenceable** array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let sequenceable2 = new MySequenceable(2, "bbb");
  let sequenceable3 = new MySequenceable(3, "ccc");
  let a = \[sequenceable, sequenceable2, sequenceable3\];
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceableArray(a);
  hilog.info(0x0000, 'testTag', 'writeSequenceableArray is ' + result);
  let b = \[new MySequenceable(0, ""), new MySequenceable(0, ""), new MySequenceable(0, "")\];
  data.readSequenceableArray(b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeRemoteObjectArray(deprecated)

writeRemoteObjectArray(objectArray: IRemoteObject\[\]): boolean

Writes an **IRemoteObject** array to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/JD8harUkSDSdlRcsI3pg0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81ACC0A9CA7EDFB5BCC0C760CACB3326AC11EB430B92DADF6059093C4A508E52)

This API is supported since API version 8 and deprecated since API version 9. Use [writeRemoteObjectArray](#writeremoteobjectarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| objectArray | [IRemoteObject](#iremoteobject)\[\] | Yes | **IRemoteObject** array to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"), new TestRemoteObject("testObject3")\];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'writeRemoteObjectArray is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readRemoteObjectArray(deprecated)

readRemoteObjectArray(objects: IRemoteObject\[\]): void

Reads the **IRemoteObject** array from this **MessageParcel** object and writes it to the created empty array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/bG_rWzh0Q4OErhyDwHJBxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E5E360A59B641AB64D2143E01382299D5B4EA3B8C531328E255B14325925CAB)

This API is supported since API version 8 and deprecated since API version 9. Use [readRemoteObjectArray](#readremoteobjectarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| objects | [IRemoteObject](#iremoteobject)\[\] | Yes | **IRemoteObject** array to read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")\];
  let data = rpc.MessageParcel.create();
  data.writeRemoteObjectArray(a);
  let b: Array<rpc.IRemoteObject> = new Array(3);
  data.readRemoteObjectArray(b);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readRemoteObjectArray(deprecated)

readRemoteObjectArray(): IRemoteObject\[\]

Reads the **IRemoteObject** array from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/A9xEsfCXRT2JlD2LeIVEcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF8657B3810851CA576AB056F563E776700A334889052CCD5F706C24F9E5B472)

This API is supported since API version 8 and deprecated since API version 9. Use [readRemoteObjectArray](#readremoteobjectarray9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject)\[\] | **IRemoteObject** object array obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // The specific processing is determined by the service.
    return true;
  }
}

try {
  let a = \[new TestRemoteObject("testObject1"), new TestRemoteObject("testObject2"),
    new TestRemoteObject("testObject3")\];
  let data = rpc.MessageParcel.create();
  let result = data.writeRemoteObjectArray(a);
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + result);
  let b = data.readRemoteObjectArray();
  hilog.info(0x0000, 'testTag', 'readRemoteObjectArray is ' + b);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]closeFileDescriptor(deprecated)

static closeFileDescriptor(fd: number): void

Closes a file descriptor. This API is a static method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/XTC-lv7BRESr2n66NZ2eNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78745E71AB8B03BBB4794136388630F27F663F6CBBEB6192D7F49F4719591379)

This API is supported since API version 8 and deprecated since API version 9. Use [closeFileDescriptor](#closefiledescriptor9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to close. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.closeFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]dupFileDescriptor(deprecated)

static dupFileDescriptor(fd: number) :number

Duplicates a file descriptor. This API is a static method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/7UO9uzK1T7aBazhc0-dXMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E52C69A3E53DD95D36424D9FA003B5D7A3012B9172B778E9DE361CFF109FEE4F)

This API is supported since API version 8 and deprecated since API version 9. Use [dupFileDescriptor](#dupfiledescriptor9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to duplicate. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | New file descriptor. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  rpc.MessageParcel.dupFileDescriptor(file.fd);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]containFileDescriptors(deprecated)

containFileDescriptors(): boolean

Checks whether this **MessageParcel** object contains file descriptors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/yvgc5qv2RzuFnKBPyAuulQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F97939B69F074092ABF07735E1FCFC53C1D08D352B9911466898288D90681399)

This API is supported since API version 8 and deprecated since API version 9. Use [containFileDescriptors](#containfiledescriptors9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the **MessageParcel** object contains file descriptors; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
  let containFD = parcel.containFileDescriptors();
  hilog.info(0x0000, 'testTag', 'parcel after write fd containFd result is ' + containFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeFileDescriptor(deprecated)

writeFileDescriptor(fd: number): boolean

Writes a file descriptor to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/6IpexdDbRCSfh5JZOBSpag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFD9A51FA2CD8C0018B7336723029041C9D058EF20196F62B3F4CB38A0B88DB2)

This API is supported since API version 8 and deprecated since API version 9. Use [writeFileDescriptor](#writefiledescriptor9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  let writeResult = parcel.writeFileDescriptor(file.fd);
  hilog.info(0x0000, 'testTag', 'parcel writeFd result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readFileDescriptor(deprecated)

readFileDescriptor(): number

Reads the file descriptor from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Wjz09AEITAKGoIjLjy8o7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA2B34552761931AE0C28E7B04F285E325CF8DD154D5D96EC1CAF00BE4CD9A79)

This API is supported since API version 8 and deprecated since API version 9. Use [readFileDescriptor](#readfiledescriptor9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | File descriptor read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { fileIo } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let filePath = "path/to/file";
  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
  parcel.writeFileDescriptor(file.fd);
  let readFD = parcel.readFileDescriptor();
  hilog.info(0x0000, 'testTag', 'parcel read fd is ' + readFD);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeAshmem(deprecated)

writeAshmem(ashmem: Ashmem): boolean

Writes an anonymous shared object to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/_t-uiCHdRTGu6sWvMevbqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E57D620A5D76A17FA39C05FBE0679A4000F13CDF19DCA0439794460DE53DC9A)

This API is supported since API version 8 and deprecated since API version 9. Use [writeAshmem](#writeashmem9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | Yes | Anonymous shared object to write. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readAshmem(deprecated)

readAshmem(): Ashmem

Reads the anonymous shared object from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/z5-LGNTFRdaHe15U74liSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D113B1A9701E8BF1D3049E61C8B46EF3DADD40548C3B7CAAB04761595C02A227)

This API is supported since API version 8 and deprecated since API version 9. Use [readAshmem](#readashmem9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | Anonymous share object obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024);
  let isWriteSuccess = parcel.writeAshmem(ashmem);
  hilog.info(0x0000, 'testTag', 'write ashmem to result is ' + isWriteSuccess);
  let readAshmem = parcel.readAshmem();
  hilog.info(0x0000, 'testTag', 'read ashmem to result is ' + readAshmem);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getRawDataCapacity(deprecated)

getRawDataCapacity(): number

Obtains the maximum amount of raw data that can be held by this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/z4yWtHWXTnKY7H-Adza5Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=127B23E06F290A21A292AB5BAF1F0282DF22CBA68DD1C49054CFDF9EB48378E2)

This API is supported since API version 8 and deprecated since API version 9. Use [getRawDataCapacity](#getrawdatacapacity9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum amount of raw data that **MessageParcel** can hold, that is, 128 MB. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let result = parcel.getRawDataCapacity();
  hilog.info(0x0000, 'testTag', 'parcel get RawDataCapacity result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeRawData(deprecated)

writeRawData(rawData: number\[\], size: number): boolean

Writes raw data to this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/WAiE9IJ6RbySMMy2BAVQVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03ED9D51A1FDC29643B1911842120C8FF963DC16FF7D8E13797170164129B107)

This API is supported since API version 8 and deprecated since API version 9. Use [writeRawDataBuffer](#writerawdatabuffer11) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rawData | number\[\] | Yes | Raw data to write. The size cannot exceed 128 MB. |
| size | number | Yes | Size of the raw data, in bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = \[1, 2, 3, 4, 5\];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]readRawData(deprecated)

readRawData(size: number): number\[\]

Reads raw data from this **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/p68e7dPVTx2pH1BKVcs5SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E9EF8F9589F9EEE6A6150D2C9CC73FE02B7D4AC8832BCF6AABA3A73311619FA)

This API is supported since API version 8 and deprecated since API version 9. Use [readRawDataBuffer](#readrawdatabuffer11) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the raw data to read. |

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Raw data obtained, in bytes. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let parcel = new rpc.MessageParcel();
  let arr = \[1, 2, 3, 4, 5\];
  let isWriteSuccess = parcel.writeRawData(arr, arr.length);
  hilog.info(0x0000, 'testTag', 'parcel write raw data result is ' + isWriteSuccess);
  let result = parcel.readRawData(5);
  hilog.info(0x0000, 'testTag', 'parcel read raw data result is ' + result);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### Parcelable9+

Writes an object to a **MessageSequence** and reads it from the **MessageSequence** during IPC.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]marshalling9+

marshalling(dataOut: MessageSequence): boolean

Marshals this **Parcelable** object into a **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataOut | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object to which the **Parcelable** object is to be marshaled. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]unmarshalling9+

unmarshalling(dataIn: MessageSequence): boolean

Unmarshals this **Parcelable** object from a **MessageSequence** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object from which the **Parcelable** object is to be unmarshaled. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyParcelable implements rpc.Parcelable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageSequence: rpc.MessageSequence): boolean {
    messageSequence.writeInt(this.num);
    messageSequence.writeString(this.str);
    return true;
  }
  unmarshalling(messageSequence: rpc.MessageSequence): boolean {
    this.num = messageSequence.readInt();
    this.str = messageSequence.readString();
    hilog.info(0x0000, 'testTag', 'readInt is ' + this.num + ' readString is ' + this.str);
    return true;
  }
}

try {
  let parcelable = new MyParcelable(1, "aaa");
  let data = rpc.MessageSequence.create();
  data.writeParcelable(parcelable);
  let ret = new MyParcelable(0, "");
  data.readParcelable(ret);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### Sequenceable(deprecated)

Writes objects of classes to a **MessageParcel** and reads them from the **MessageParcel** during IPC.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/6THgAHFxQHmKqg-kl8wT_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEB8FF50437309D51EE93005347E61AE6A107DE63C0EFD7802374641F42B3AAA)

This API is supported since API version 7 and deprecated since API version 9. Use [Parcelable](#parcelable9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]marshalling(deprecated)

marshalling(dataOut: MessageParcel): boolean

Marshals the sequenceable object into a **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/hnQhXARgQaC8fB1jWzX9qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CAF78B0F4AC6095E0578A92439220EE71CBEDE459586E6CE037BD072D9BFEB1)

This API is supported since API version 7 and deprecated since API version 9. Use [marshalling](#marshalling9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataOut | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object to which the sequenceable object is to be marshaled. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]unmarshalling(deprecated)

unmarshalling(dataIn: MessageParcel): boolean

Unmarshals this sequenceable object from a **MessageParcel** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/-U-qqLi3T26qrVjoBlH6Kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CB4F2527C436F3903A5F3AC8DD3811E829CD44E5963BBDBF2125F13139613ED)

This API is supported since API version 7 and deprecated since API version 9. Use [unmarshalling](#unmarshalling9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataIn | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object in which the sequenceable object is to be unmarshaled. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MySequenceable implements rpc.Sequenceable {
  num: number = 0;
  str: string = '';
  constructor(num: number, str: string) {
    this.num = num;
    this.str = str;
  }
  marshalling(messageParcel: rpc.MessageParcel): boolean {
    messageParcel.writeInt(this.num);
    messageParcel.writeString(this.str);
    return true;
  }
  unmarshalling(messageParcel: rpc.MessageParcel): boolean {
    this.num = messageParcel.readInt();
    this.str = messageParcel.readString();
    return true;
  }
}

try {
  let sequenceable = new MySequenceable(1, "aaa");
  let data = rpc.MessageParcel.create();
  let result = data.writeSequenceable(sequenceable);
  hilog.info(0x0000, 'testTag', 'writeSequenceable is ' + result);
  let ret = new MySequenceable(0, "");
  let result2 = data.readSequenceable(ret);
  hilog.info(0x0000, 'testTag', 'readSequenceable is ' + result2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### IRemoteBroker

Represents the holder of a remote proxy object. It is used to obtain a proxy object.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]asObject

asObject(): IRemoteObject

Obtains a proxy or remote object. This API must be implemented by its derived classes.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | Returns the **RemoteObject** if it is the caller; returns the [IRemoteObject](#iremoteobject), the holder of this **RemoteProxy** object, if the caller is a [RemoteProxy](#remoteproxy) object. |

**Example**

import { rpc } from '@kit.IPCKit';

class TestAbility extends rpc.RemoteObject {
  asObject() {
    return this;
  }
}
let remoteObject = new TestAbility("testObject").asObject();

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/8g8Ig4TBT7Csvk4ychrrGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7942B90AF2E4E71C94ED4BD44CDBA85E2C522084E0F5D4DDBFE59B2078884A32)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want  = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **asObject()** of the proxy object is called to obtain the proxy or remote object.

import { rpc } from '@kit.IPCKit';

class TestProxy {
  remote: rpc.IRemoteObject;
  constructor(remote: rpc.IRemoteObject) {
    this.remote = remote;
  }
  asObject() {
    return this.remote;
  }
}
if (proxy != undefined) {
  let iRemoteObject = new TestProxy(proxy).asObject();
}

#### DeathRecipient

Subscribes to death notifications of a remote object. When the remote object is dead, the local end will receive a notification and **[onRemoteDied](#onremotedied)** will be called. A remote object is dead when the process holding the object is terminated or the device of the remote object is shut down or restarted. If the local and remote objects belong to different devices, the remote object is dead when the device holding the remote object is detached from the network.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]onRemoteDied

onRemoteDied(): void

Called to perform subsequent operations when a death notification of the remote object is received.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}

#### RequestResult9+

Defines the response to the request.

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| errCode | number | No | No | Error code. |
| code | number | No | No | Message code. |
| data | [MessageSequence](#messagesequence9) | No | No | **MessageSequence** object sent to the remote process. |
| reply | [MessageSequence](#messagesequence9) | No | No | **MessageSequence** object returned by the remote process. |

#### SendRequestResult(deprecated)

Defines the response to the request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/JeIa72mXSCu9N28MpXkCBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4B111FB4037574A9308A531394DA8DF98356F9EA639EFD734216E797206D3AF)

This API is supported since API version 8 and deprecated since API version 9. Use [RequestResult](#requestresult9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| errCode | number | No | No | Error code. |
| code | number | No | No | Message code. |
| data | [MessageParcel](#messageparceldeprecated) | No | No | **MessageParcel** object sent to the remote process. |
| reply | [MessageParcel](#messageparceldeprecated) | No | No | **MessageParcel** object returned by the remote process. |

#### IRemoteObject

Provides methods to query of obtain interface descriptors, add or delete death notifications, dump object status to specific files, and send messages.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]getLocalInterface9+

getLocalInterface(descriptor: string): IRemoteBroker

Obtains the string of the interface descriptor.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | string | Yes | Interface descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | **IRemoteBroker** object bound to the specified interface token. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(descriptor: string): IRemoteBroker

Obtains the string of the interface descriptor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Flt1bKymT9CrhSl6am-cUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACDA26AD80E3857D2CB3B4EFFDD43DCDAF11B17A72838F4D23558554B8B75B3B)

This API is supported since API version 7 and deprecated since API version 9. Use [getLocalInterface](#getlocalinterface9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | string | Yes | Interface descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | **IRemoteBroker** object bound to the specified interface token. |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message does not contain any content. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/4p07fGm_SFi54ob3OIB1HA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65D4A216EBD3AF0A694F16FE4560BBAD8EB51E6CC739D08C39139955489AB11A)

This API is supported since API version 7 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the message is sent successfully; returns **false** otherwise. |

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise used to return a **requestResult** object. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/1NKWzH8nTsKxl2t5HGyh6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E24FE6E7EA88BA89B9827BF6282B03E968FD770187E572B6C813800251491A9)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise used to return a **sendRequestResult** instance. |

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains the returned information.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | Yes | Callback used to return the result. When the message is sent successfully, the data returned by the server can be read from **RequestResult**. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/StGyiJMRT1Kx_dVbB1IRFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C90C877056C598A2A08B5864D309DED329E12A3D9D48C81E3FB30DD479DB0336)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | Yes | Callback for receiving the sending result. |

#### \[h2\]registerDeathRecipient9+

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

Registers a callback for receiving death notifications of the remote object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to register. |
| flags | number | Yes | Flag of the death notification. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]addDeathRecipient(deprecated)

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

Adds a callback for receiving death notifications of the remote object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/iqL7iSTmR0OxdviCfq0rvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A25150EA77C67B910561E238138537BA16DF5CF8561812917AF359EF93D2BDAD)

This API is supported since API version 7 and deprecated since API version 9. Use [registerDeathRecipient](#registerdeathrecipient9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to register. |
| flags | number | Yes | Flag of the death notification. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the callback is added successfully; returns **false** otherwise. |

#### \[h2\]unregisterDeathRecipient9+

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

Unregisters from the callback used to receive death notifications of the remote object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to unregister. |
| flags | number | Yes | Flag of the death notification. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900005 | Operation allowed only for the proxy object. |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]removeDeathRecipient(deprecated)

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

Removes the callback used to receive death notifications of the remote object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/2hfTIxiaQvWTUV0FQGgRNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3B07E835F1DEC4C5B30CF667FC5D2C530E3A5901D6E623ECF37EF180073DA01)

This API is supported since API version 7 and deprecated since API version 9. Use [unregisterDeathRecipient](#unregisterdeathrecipient9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to unregister. |
| flags | number | Yes | Flag of the death notification. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the callback is removed; returns **false** otherwise. |

#### \[h2\]getDescriptor9+

getDescriptor(): string

Obtains the interface descriptor (which is a string) of this object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

Obtains the interface descriptor (which is a string) of this object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/YhOP2ybKSiOkWBsXyFWqYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=006C02037AB2F220A472A7F744F8BC94224BA41552E96163C9F7CDFB9A61CBA8)

This API is supported since API version 7 and deprecated since API version 9. Use [getDescriptor](#getdescriptor9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

#### \[h2\]isObjectDead

isObjectDead(): boolean

Checks whether this object is dead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the object is dead; returns **false** otherwise. |

#### RemoteProxy

Provides APIs to implement **IRemoteObject**.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]Properties

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| PING\_TRANSACTION | number | Yes | No | Internal instruction code used to test whether the IPC service is normal. |
| DUMP\_TRANSACTION | number | Yes | No | Internal instruction code used to obtain IPC service status information. |
| INTERFACE\_TRANSACTION | number | Yes | No | Internal instruction code used to obtain the remote interface token. |
| MIN\_TRANSACTION\_ID | number | Yes | No | Minimum valid instruction code. |
| MAX\_TRANSACTION\_ID | number | Yes | No | Maximum valid instruction code. |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Da2kUngSTG6qw9n2JkaADw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62F773C17962CAC5DD5E11824CDD7ADB01E063839CBE14CB25B69436E74514D1)

This API is supported since API version 7 and deprecated since API version 8. Use [sendMessageRequest](#sendmessagerequest9-2) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the message is sent successfully; returns **false** otherwise. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/g_t4jbgcRP2FkB_77c4-hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B75E3F0E952D6A9AAC74C6E341EF8780A9E9F5FA2CC1CB67DC208C6B62B974E0)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **sendRequest()** of the proxy object is called to send a message.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    let ret: boolean = proxy.sendRequest(1, data, reply, option);
    if (ret) {
      hilog.info(0x0000, 'testTag', 'sendRequest got result');
      let msg = reply.readString();
      hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
    } else {
      hilog.error(0x0000, 'testTag', 'sendRequest failed');
    }
    hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
    data.reclaim();
    reply.reclaim();
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise used to return a **requestResult** instance. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/DHTlOiFjTSeWej8XA6qMWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87B27014D1E25C1766D6B3DB413513F712DC9347399C518F0B613D2B72B6940C)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **sendMessageRequest()** of the proxy object is called to send a message.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    proxy.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
}

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/5eatrU6FSVm9dyrGpvjNvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=12D8F11FD071D294425B6B4F7407E4094310C6390EB4D0B60BE1DCE32CA6AFAC)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9-2) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise used to return a **sendRequestResult** instance. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/g2pos7b8SHmIq6wB-S1lPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4431D9FE42409A75BF3651F1437438948862AB3BC91EE058B386B138C9B87B18)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **sendRequest()** of the proxy object is called to send a message.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  if (proxy != undefined) {
    let a = proxy.sendRequest(1, data, reply, option) as Object;
    let b = a as Promise<rpc.SendRequestResult>;
    b.then((result: rpc.SendRequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
  }
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + error);
}

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked at certain time after the response to **RequestResult** is returned, and the reply contains the returned information.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | Yes | Callback used to return the result. When the message is sent successfully, the data returned by the server can be read from **RequestResult**. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/IXEdPvtRShSTUCblWVIMhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAB72D74AC2F662C903EB74711E2FDDFDAA9AA03E6D6BF0D5E50E6F2DDA8ABD8)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9-3) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | Yes | Callback for receiving the sending result. |

#### \[h2\]getLocalInterface9+

getLocalInterface(interface: string): IRemoteBroker

Obtains the **LocalInterface** object of an interface token.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interface | string | Yes | Interface descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | Returns **Null** by default, which indicates a proxy interface. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | check param failed |
| 1900006 | Operation allowed only for the remote object. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/5w1MUIJXRM2AE0UpOd6E8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1661ADFBB5FA8DF53C4706D778A9239C11537D30093DC33D86BFBAE38369AD4)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **getLocalInterface()** of the proxy object is called to obtain the interface descriptor.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (proxy != undefined) {
  try {
    let broker: rpc.IRemoteBroker = proxy.getLocalInterface("testObject");
    hilog.info(0x0000, 'testTag', 'getLocalInterface is ' + broker);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'rpc get local interface fail, errorMessage ' + e.message);
  }
}

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(interface: string): IRemoteBroker

Obtains the **LocalInterface** object of an interface token.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/7CORYwVXSGCvCGzd5eakpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48A55868510950E4061AC6A9732F19EC5F74E1117CFEA22EB39EA7B5DE329E68)

This API is supported since API version 7 and deprecated since API version 9. Use [getLocalInterface](#getlocalinterface9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interface | string | Yes | Interface descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | Returns **Null** by default, which indicates a proxy interface. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/35m2yTCwQNavEmXv7bekDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28F9079E527721E40A881FE48EED3E37445ADB2E0D0E22E6E71B384B7F75AA19)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **queryLocalInterface()** of the proxy object is called to obtain the interface descriptor.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let broker: rpc.IRemoteBroker = proxy.queryLocalInterface("testObject");
  hilog.info(0x0000, 'testTag', 'queryLocalInterface is ' + broker);
}

#### \[h2\]registerDeathRecipient9+

registerDeathRecipient(recipient: DeathRecipient, flags: number): void

Registers a callback for receiving death notifications of the remote object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to register. |
| flags | number | Yes | Flag of the death notification. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900008 | The proxy or remote object is invalid. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/qkXLr_VNQHea_bgHnnq93A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D453B41C497320947DC7776BB7B91FB570B12F503DF6B7F0668022B8EC7B811)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **registerDeathRecipient()** of the proxy object is called to register a callback for receiving the death notification of the remote object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  try {
    let deathRecipient = new MyDeathRecipient();
    proxy.registerDeathRecipient(deathRecipient, 0);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'proxy register deathRecipient fail, errorMessage ' + e.message);
  }
}

#### \[h2\]addDeathRecipient(deprecated)

addDeathRecipient(recipient: DeathRecipient, flags: number): boolean

Adds a callback for receiving death notifications of the remote object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/o_UeP7vwSdiwP0A-hi0AkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D78EF3D66A3D1CC12EA61CEF6EA05773122CE2BDFA7DE59610BB2EA5AF83F31)

This API is supported since API version 7 and deprecated since API version 9. Use [registerDeathRecipient](#registerdeathrecipient9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to add. |
| flags | number | Yes | Flag of the death notification. This parameter is reserved. It is set to **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the callback is added successfully; returns **false** otherwise. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/t3oliGZaQiSZ3WPka1D36Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0D245B8B717BC0892D848D6849A57F4E26AA4CB015E9D32F0A2231137526AC7)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **addDeathRecipient()** of the proxy object is called to add a callback for receiving the death notification of the remove object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  let deathRecipient = new MyDeathRecipient();
  proxy.addDeathRecipient(deathRecipient, 0);
}

#### \[h2\]unregisterDeathRecipient9+

unregisterDeathRecipient(recipient: DeathRecipient, flags: number): void

Unregisters from the callback used to receive death notifications of the remote object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to unregister. |
| flags | number | Yes | Flag of the death notification. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The callback used to receive remote object death notifications is empty.

 |
| 1900008 | The proxy or remote object is invalid. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/tiz4RxFXQa6Fekikm6itfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E308934DE65A0041E8431A917171691368540A20F469A9DD572A8784D9666B95)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **unregisterDeathRecipient()** of the proxy object is called to unregister the callback for receiving the death notification of the remote object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  try {
    let deathRecipient = new MyDeathRecipient();
    proxy.registerDeathRecipient(deathRecipient, 0);
    proxy.unregisterDeathRecipient(deathRecipient, 0);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'proxy unregister deathRecipient fail, errorMessage ' + e.message);
  }
}

#### \[h2\]removeDeathRecipient(deprecated)

removeDeathRecipient(recipient: DeathRecipient, flags: number): boolean

Removes the callback used to receive death notifications of the remote object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/f6vo58lxTG6DKO7mmMN0TA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33142A856E295386158A0D0006E18A9174EA4B44EC1FA4016907D61F0EF14A6F)

This API is supported since API version 7 and deprecated since API version 9. Use [unregisterDeathRecipient](#unregisterdeathrecipient9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recipient | [DeathRecipient](#deathrecipient) | Yes | Callback to remove. |
| flags | number | Yes | Flag of the death notification. This parameter is reserved. It is set to **0**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the callback is removed; returns **false** otherwise. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/ForbPFLpRn6CtDfjl6Qs_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A7B9F559E94A165BC7F61FD5C2C99AE2E0EADA379EF7D4ABD3C2896818505CE)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **removeDeathRecipient()** of the proxy object is called to remove the callback used to receive the death notification of the remote object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
if (proxy != undefined) {
  let deathRecipient = new MyDeathRecipient();
  proxy.addDeathRecipient(deathRecipient, 0);
  proxy.removeDeathRecipient(deathRecipient, 0);
}

#### \[h2\]getDescriptor9+

getDescriptor(): string

Obtains the interface descriptor (which is a string) of this object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900007 | communication failed. |
| 1900008 | The proxy or remote object is invalid. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/DOI4nv7TS6OJBU_ksYmHOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83C85A2C66762312788E220D374E14FCF87342EBAB1CB2F8B899205FBFA5B7E4)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **getDescriptor()** of the proxy object is called to obtain the interface descriptor of the object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

if (proxy != undefined) {
  try {
    let descriptor: string = proxy.getDescriptor();
    hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorCode ' + e.code);
    hilog.error(0x0000, 'testTag', 'rpc get interface descriptor fail, errorMessage ' + e.message);
  }
}

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

Obtains the interface descriptor of this proxy object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/4RUUsokFSkKWPBfHqusGdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A24287EF8F75088F21BD2F2C3ED84143312BD7E4FAAC4B7C81897C66E82EBFFC)

This API is supported since API version 7 and deprecated since API version 9. Use [getDescriptor](#getdescriptor9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/PrWI8hHyQ8S6vzdJd4NeTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F0A4A74E7B486FE1C05F84F4D6FA22CC03B21CF4B9CFD5804F4D98D423DFFCA)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **getInterfaceDescriptor()** of the proxy object is called to obtain the interface descriptor of the current proxy object.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let descriptor: string = proxy.getInterfaceDescriptor();
  hilog.info(0x0000, 'testTag', 'descriptor is ' + descriptor);
}

#### \[h2\]isObjectDead

isObjectDead(): boolean

Checks whether the **RemoteObject** is dead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if **RemoteObject** is dead; returns **false** otherwise. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/vzYTCmlYSp-LqNzgZEjiww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1537690DD570998444BA744FA05D2EBFB1F3DFE0DC0947F358849A99CC5DF0BA)

In the sample code provided in this topic, **this.getUIContext().getHostContext()** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

// If the FA model is used, import featureAbility from @kit.AbilityKit.
// import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let proxy: rpc.IRemoteObject | undefined;
let connect: common.ConnectOptions = {
  onConnect: (elementName, remoteProxy) => {
    hilog.info(0x0000, 'testTag', 'js onConnect called');
    proxy = remoteProxy;
  },
  onDisconnect: (elementName) => {
    hilog.info(0x0000, 'testTag', 'onDisconnect');
  },
  onFailed: () => {
    hilog.info(0x0000, 'testTag', 'onFailed');
  }
};
let want: Want = {
  // Obtain the package name and ability name on the server.
  bundleName: "com.ohos.server",
  abilityName: "com.ohos.server.EntryAbility",
};

// Use this method to connect to the ability for the FA model.
// FA.connectAbility(want,connect);

// Save the connection ID, which will be used for the subsequent service disconnection.
let context: common.UIAbilityContext = this.getUIContext().getHostContext(); // UIAbilityContext
// Save the connection ID, which will be used for the subsequent service disconnection.
let connectionId = context.connectServiceExtensionAbility(want, connect);

The proxy object in the **onConnect** callback can be assigned a value only after the ability is connected asynchronously. Then, **isObjectDead()** of the proxy object is called to check whether this object is dead.

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

if (proxy != undefined) {
  let isDead: boolean = proxy.isObjectDead();
  hilog.info(0x0000, 'testTag', 'isObjectDead is ' + isDead);
}

#### MessageOption

Defines the options used to construct the **MessageOption** object.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]Properties

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| TF\_SYNC | number | Yes | No | Synchronous call. |
| TF\_ASYNC | number | Yes | No | Asynchronous call. |
| TF\_ACCEPT\_FDS | number | Yes | No | Indication to **sendMessageRequest9+** for passing the file descriptor. |
| TF\_WAIT\_TIME | number | Yes | No | RPC wait time, in seconds. This parameter cannot be used in IPC. The default waiting time is 8 seconds. You are advised not to change the waiting time. |

#### \[h2\]constructor9+

constructor(async?: boolean)

A constructor used to create a **MessageOption** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| async | boolean | No | Whether to execute the call asynchronously. The value **true** means to execute the call asynchronously; the value **false** means to execute the call synchronously. The default value is **synchronous**. |

**Example**

import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.MessageOption {
  constructor(async: boolean) {
    super(async);
  }
}

#### \[h2\]constructor

constructor(syncFlags?: number, waitTime?: number)

A constructor used to create a **MessageOption** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| syncFlags | number | No | Call flag to set. The options are as follows: 0 (synchronous call) and 1 (asynchronous call). The default value is **synchronous**. |
| waitTime | number | No | Maximum wait time for an RPC call. The default value is **TF\_WAIT\_TIME**. |

**Example**

import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.MessageOption {
  constructor(syncFlags?: number,waitTime?: number) {
    super(syncFlags,waitTime);
  }
}

#### \[h2\]isAsync9+

isAsync(): boolean

Checks whether [sendMessageRequest](#sendmessagerequest9-2) is called asynchronously.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if **SendMessageRequest** is called asynchronously; returns **false** if it is called synchronously. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let result = option.isAsync();
} catch (error) {
  hilog.info(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]setAsync9+

setAsync(isAsync: boolean): void

Sets whether to call [sendMessageRequest](#sendmessagerequest9-2) asynchronously.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isAsync | boolean | Yes | Whether to execute the call asynchronously. The value **true** means to execute the call asynchronously; the value **false** means to execute the call synchronously. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setAsync(true);
} catch (error) {
  hilog.info(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getFlags

getFlags(): number

Obtains the call flag, which can be synchronous or asynchronous.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Call flag obtained. **0**: synchronous call flag; **1**: asynchronous call flag. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  hilog.info(0x0000, 'testTag', 'create object successfully');
  let flag = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
  option.setFlags(rpc.MessageOption.TF\_ASYNC);
  hilog.info(0x0000, 'testTag', 'run setFlags success');
  let flag2 = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag2 is ' + flag2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]setFlags

setFlags(flags: number): void

Sets the call flag, which can be synchronous or asynchronous.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| flags | number | Yes | Call flag to set. **0**: synchronous call flag; **1**: asynchronous call flag. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setFlags(rpc.MessageOption.TF\_ASYNC);
  hilog.info(0x0000, 'testTag', 'run setFlags success');
  let flag = option.getFlags();
  hilog.info(0x0000, 'testTag', 'run getFlags success, flag is ' + flag);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getWaitTime

getWaitTime(): number

Obtains the maximum wait time for an RPC call.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Maximum wait time obtained. The default value is **TF\_WAIT\_TIME**. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  let time = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
  option.setWaitTime(16);
  let time2 = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time2);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]setWaitTime

setWaitTime(waitTime: number): void

Sets the maximum wait time for an RPC call.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| waitTime | number | Yes | Maximum wait time to set. The upper limit is 3000 seconds. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let option = new rpc.MessageOption();
  option.setWaitTime(16);
  let time = option.getWaitTime();
  hilog.info(0x0000, 'testTag', 'run getWaitTime success, time is ' + time);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### IPCSkeleton

Obtains IPC context, including the UID and PID, local and remote device IDs, and whether the method is invoked on the same device.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]getContextObject

static getContextObject(): IRemoteObject

Obtains the system capability manager. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteObject](#iremoteobject) | System capability manager obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let samgr = rpc.IPCSkeleton.getContextObject();
  hilog.info(0x0000, 'testTag', 'RpcServer: getContextObject result: ' + samgr);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]getCallingPid

static getCallingPid(): number

Obtains the PID of the caller. This API is a static method, which is called by the [RemoteObject](#remoteobject) object in the IPC context [onRemoteMessageRequest](#onremotemessagerequest9). If the method is not called in the IPC context, the PID of the current process is returned.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | PID of the caller. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerPid = rpc.IPCSkeleton.getCallingPid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid result: ' + callerPid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]getCallingUid

static getCallingUid(): number

Obtains the UID of the caller. This API is a static method, which is called by the [RemoteObject](#remoteobject) object in the IPC context [onRemoteMessageRequest](#onremotemessagerequest9). If the method is not called in the IPC context, the UID of the current process is returned.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | UID of the caller. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerUid = rpc.IPCSkeleton.getCallingUid();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid result: ' + callerUid);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]getCallingTokenId8+

static getCallingTokenId(): number

Obtains the caller's token ID, which is used to verify the caller identity.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Token ID of the caller obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
      hilog.info(0x0000, 'testTag', 'RpcServer: getCallingTokenId result: ' + callerTokenId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]getCallingDeviceID

static getCallingDeviceID(): string

Obtains the ID of the device hosting the caller's process. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Device ID obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callerDeviceID = rpc.IPCSkeleton.getCallingDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: callerDeviceID is ' + callerDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]getLocalDeviceID

static getLocalDeviceID(): string

Obtains the local device ID. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Local device ID obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let localDeviceID = rpc.IPCSkeleton.getLocalDeviceID();
      hilog.info(0x0000, 'testTag', 'RpcServer: localDeviceID is ' + localDeviceID);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]isLocalCalling

static isLocalCalling(): boolean

Checks whether the peer process is a process of the local device. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the local and peer processes are on the same device; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let isLocalCalling = rpc.IPCSkeleton.isLocalCalling();
      hilog.info(0x0000, 'testTag', 'RpcServer: isLocalCalling is ' + isLocalCalling);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]flushCmdBuffer9+

static flushCmdBuffer(object: IRemoteObject): void

Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API is a static method. You are advised to call this API before performing any sensitive operation.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | Yes | **RemoteProxy** specified. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  rpc.IPCSkeleton.flushCmdBuffer(remoteObject);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}

#### \[h2\]flushCommands(deprecated)

static flushCommands(object: IRemoteObject): number

Flushes all suspended commands from the specified **RemoteProxy** to the corresponding **RemoteObject**. This API is a static method. You are advised to call this API before performing any sensitive operation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/bvpf3CBJRIegcYmjyPYAmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D41B9AD299517D899A0DDAB39BBA03CC7CD5AD0037DDB3C8343ACA73AFA727A9)

This API is supported since API version 7 and deprecated since API version 9. Use [flushCmdBuffer](#flushcmdbuffer9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| object | [IRemoteObject](#iremoteobject) | Yes | **RemoteProxy** specified. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Returns **0** if the operation is successful; returns an error code if the input object is null or a **RemoteObject**, or if the operation fails. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let remoteObject = new TestRemoteObject("aaa");
  let ret = rpc.IPCSkeleton.flushCommands(remoteObject);
  hilog.info(0x0000, 'testTag', 'RpcServer: flushCommands result: ' + ret);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'proxy flushCmdBuffer fail, errorMessage ' + e.message);
}

#### \[h2\]resetCallingIdentity

static resetCallingIdentity(): string

Resets the UID and PID of the remote user to those of the local user. This API is a static method and is used in scenarios such as identity authentication.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | String containing the UID and PID of the remote user. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]restoreCallingIdentity9+

static restoreCallingIdentity(identity: string): void

Restores the UID and PID of the remote user. This API is a static method. It is usually called after **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are required. This API is supported only in the IPC context [onRemoteMessageRequest](#onremotemessagerequest9); otherwise, it returns directly.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| identity | string | Yes | A string containing the UID and PID of the remote user. The length of the string must be less than 40960 bytes. are returned by **resetCallingIdentity**. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      rpc.IPCSkeleton.restoreCallingIdentity(callingIdentity);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### \[h2\]setCallingIdentity(deprecated)

static setCallingIdentity(identity: string): boolean

Sets the UID and PID of the remote user. This API is a static method. It is usually called after **resetCallingIdentity**, and the UID and PID of the remote user returned by **resetCallingIdentity** are required.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/VLPicmq_R1y6bmzugv3oqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75873B9606D556BF3DFA40ED2AD3BC416A3C0C89A70E09C7314398BA822EE6D4)

This API is supported since API version 7 and deprecated since API version 9. Use [restoreCallingIdentity](#restorecallingidentity9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| identity | string | Yes | String containing the remote user's UID and PID, which are returned by **resetCallingIdentity**. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    try {
      let callingIdentity = rpc.IPCSkeleton.resetCallingIdentity();
      hilog.info(0x0000, 'testTag', 'RpcServer: callingIdentity is ' + callingIdentity);
      let ret = rpc.IPCSkeleton.setCallingIdentity(callingIdentity);
      hilog.info(0x0000, 'testTag', 'RpcServer: setCallingIdentity is ' + ret);
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'error ' + error);
    }
    return true;
  }
}

#### RemoteObject

Provides methods to implement **RemoteObject**. The service provider must inherit from this class.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]constructor

constructor(descriptor: string)

A constructor used to create a **RemoteObject** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | string | Yes | Interface descriptor. The length of the string must be less than 40960 bytes. |

**Example**

import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
}

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/sRC-gJnHQrWxSG72hMSuEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB4588D421D1EDBF6283E096B8FF0DE99261EEF7BAFA3A61C30E3B25633DF032)

This API is supported since API version 7 and deprecated since API version 8. Use [sendMessageRequest](#sendmessagerequest9-4) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the message is sent successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class testRemoteObject extends rpc.RemoteObject {
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel,
    option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let ret: boolean = testRemoteObject.sendRequest(1, data, reply, option);
  if (ret) {
    hilog.info(0x0000, 'testTag', 'sendRequest got result');
    let msg = reply.readString();
    hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
  } else {
    hilog.error(0x0000, 'testTag', 'sendRequest failed');
  }
  hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
  data.reclaim();
  reply.reclaim();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): Promise<RequestResult>

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendMessageRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RequestResult](#requestresult9)\> | Promise used to return a **RequestResult** instance. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  data.writeInt(1);
  data.writeString("hello");
  testRemoteObject.sendMessageRequest(1, data, reply, option)
    .then((result: rpc.RequestResult) => {
      if (result.errCode === 0) {
        hilog.info(0x0000, 'testTag', 'sendMessageRequest got result');
        let num = result.reply.readInt();
        let msg = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'reply num: ' + num);
        hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
      } else {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode: ' + result.errCode);
      }
    }).catch((e: Error) => {
      hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + JSON.stringify(e));
    }).finally (() => {
      hilog.info(0x0000, 'testTag', 'sendMessageRequest ends, reclaim parcel');
      data.reclaim();
      reply.reclaim();
    });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error: ' + error);
}

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): Promise<SendRequestResult>

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a promise will be fulfilled immediately and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a promise will be fulfilled when the response to **sendRequest** is returned, and the reply message contains the returned information. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/1uJgMywYT8yBhwnOshJ8Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=629B4E979C48408E76D541904EB0C0E7A996BA7D93AEC7E79C1D31A89BBFF5E2)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9-4) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SendRequestResult](#sendrequestresultdeprecated)\> | Promise used to return a **sendRequestResult** instance. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let option = new rpc.MessageOption();
  let data = rpc.MessageParcel.create();
  let reply = rpc.MessageParcel.create();
  data.writeInt(1);
  data.writeString("hello");
  let a = testRemoteObject.sendRequest(1, data, reply, option) as Object;
  let b = a as Promise<rpc.SendRequestResult>;
  b.then((result: rpc.SendRequestResult) => {
    if (result.errCode === 0) {
      hilog.info(0x0000, 'testTag', 'sendRequest got result');
      let num = result.reply.readInt();
      let msg = result.reply.readString();
      hilog.info(0x0000, 'testTag', 'reply num: ' + num);
      hilog.info(0x0000, 'testTag', 'reply msg: ' + msg);
    } else {
      hilog.error(0x0000, 'testTag', 'sendRequest failed, errCode: ' + result.errCode);
    }
  }).catch((e: Error) => {
    hilog.error(0x0000, 'testTag', 'sendRequest failed, error: ' + JSON.stringify(e));
  }).finally (() => {
    hilog.info(0x0000, 'testTag', 'sendRequest ends, reclaim parcel');
    data.reclaim();
    reply.reclaim();
  });
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}

#### \[h2\]sendMessageRequest9+

sendMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption, callback: AsyncCallback<RequestResult>): void

Sends a **MessageSequence** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendMessageRequest** is returned, and the reply message contains the returned information.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object holding the data to send. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[RequestResult](#requestresult9)\> | Yes | Callback used to return the result. When the message is sent successfully, the data returned by the server can be read from **RequestResult**. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain the passed object instance.

 |

#### \[h2\]sendRequest(deprecated)

sendRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption, callback: AsyncCallback<SendRequestResult>): void

Sends a **MessageParcel** message to the remote process in synchronous or asynchronous mode. If asynchronous mode is set in **options**, a callback will be called immediately, and the reply message is empty. The specific reply needs to be obtained from the callback on the service side. If synchronous mode is set in **options**, a callback will be invoked when the response to **sendRequest** is returned, and the reply message contains the returned information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Uh3-RBVpTcqsCVTv3kphZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6687D5E6BEF21C87E52DFEBDDE34AEF07E5815DDE6AFEEF4D6857A987A43DA40)

This API is supported since API version 8 and deprecated since API version 9. Use [sendMessageRequest](#sendmessagerequest9-5) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Message code \[1-16777215\] called by the request, which is determined by the communication parties. If the method is generated by an IDL tool, the message code is automatically generated by the IDL tool. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object holding the data to send. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that receives the response. |
| options | [MessageOption](#messageoption) | Yes | Request sending mode, which can be synchronous (default) or asynchronous. |
| callback | AsyncCallback<[SendRequestResult](#sendrequestresultdeprecated)\> | Yes | Callback for receiving the sending result. |

#### \[h2\]onRemoteMessageRequest9+

onRemoteMessageRequest(code: number, data: MessageSequence, reply: MessageSequence, options: MessageOption): boolean | Promise<boolean>

Called to return a response to **sendMessageRequest()**. The server processes the request synchronously or asynchronously and returns the result in this API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/m7TAKL1_QPK6kEmJ6uLzAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0121B022669FF54E2EC3E7ADD52EB4FE17C006D23EA08040503CAC537171C17D)

You are advised to override **onRemoteMessageRequest** preferentially, which implements synchronous and asynchronous message processing.

If both **onRemoteRequest** and **onRemoteMessageRequest** are overridden, only **onRemoteMessageRequest** takes effect.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Service request code sent by the remote end. |
| data | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object that holds the parameters called by the client. |
| reply | [MessageSequence](#messagesequence9) | Yes | **MessageSequence** object to which the result is written. |
| options | [MessageOption](#messageoption) | Yes | Whether the operation is synchronous or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Promise<boolean> | 
\- If the request is processed synchronously in **onRemoteMessageRequest**, a Boolean value is returned. The value **true** means that the operation is successful, and **false** means the opposite.

\- If the request is processed asynchronously in **onRemoteMessageRequest**, a promise object is returned. The value **true** means that the operation is successful, and **false** means the opposite.

 |

**Example**

// Override \*\*onRemoteMessageRequest\*\* to process requests synchronously.
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}

**Example**

// Override \*\*onRemoteMessageRequest\*\* to process requests asynchronously.
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    await new Promise((resolve: (data: rpc.RequestResult) => void) => {
      setTimeout(resolve, 100);
    })
    return true;
  }
}

**Example**

// Override \*\*onRemoteMessageRequest\*\* and \*\*onRemoteRequest\*\* to process requests synchronously.
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
     if (code === 1) {
        hilog.info(0x0000, 'testTag', 'RpcServer: sync onRemoteMessageRequest is called');
        return true;
     } else {
        hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
        return false;
     }
  }
    // Only onRemoteMessageRequest is executed.
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: async onRemoteMessageRequest is called');
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
    return true;
  }
}

#### \[h2\]onRemoteRequest(deprecated)

onRemoteRequest(code: number, data: MessageParcel, reply: MessageParcel, options: MessageOption): boolean

Called to return a response to **sendRequest()**. The server processes the request and returns a response in this function.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Zdjt-MHfTvSibTRE9CHBlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F64F40B676028E9B36A269ECD30084FE0DEB717F16F19C753C1C4FFB851C64BD)

This API is supported since API version 7 and deprecated since API version 9. Use [onRemoteMessageRequest](#onremotemessagerequest9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| code | number | Yes | Service request code sent by the remote end. |
| data | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object that holds the parameters called by the client. |
| reply | [MessageParcel](#messageparceldeprecated) | Yes | **MessageParcel** object carrying the result. |
| options | [MessageOption](#messageoption) | Yes | Whether the operation is synchronous or asynchronous. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteRequest(code: number, data: rpc.MessageParcel, reply: rpc.MessageParcel, option: rpc.MessageOption): boolean {
    if (code === 1) {
      hilog.info(0x0000, 'testTag', 'RpcServer: onRemoteRequest called');
      return true;
    } else {
      hilog.error(0x0000, 'testTag', 'RpcServer: unknown code: ' + code);
      return false;
    }
  }
}

#### \[h2\]getCallingUid

getCallingUid(): number

Obtains the UID of the remote process.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | UID of the remote process obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingUid: ' + testRemoteObject.getCallingUid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}

#### \[h2\]getCallingPid

getCallingPid(): number

Obtains the PID of the remote process.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | PID of the remote process obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  hilog.info(0x0000, 'testTag', 'RpcServer: getCallingPid: ' + testRemoteObject.getCallingPid());
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}

#### \[h2\]getLocalInterface9+

getLocalInterface(descriptor: string): IRemoteBroker

Obtains the string of the interface descriptor.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | string | Yes | String of the interface descriptor. The length of the string must be less than 40960 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | **IRemoteBroker** object bound to the specified interface token. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.getLocalInterface("testObject");
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]queryLocalInterface(deprecated)

queryLocalInterface(descriptor: string): IRemoteBroker

Checks whether the remote object corresponding to the specified interface token exists.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/TrQJtnrUQLO0O8_cI6woFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FC188A46B6452291BA7BE0597DF1BAC17F59137F40A7051DFB016F25F815BBA)

This API is supported since API version 7 and deprecated since API version 9. Use [getLocalInterface](#getlocalinterface9-2) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| descriptor | string | Yes | Interface descriptor. |

**Return value**

| Type | Description |
| :-- | :-- |
| [IRemoteBroker](#iremotebroker) | Returns the remote object if a match is found; returns **Null** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testRemoteObject = new TestRemoteObject("testObject");
  testRemoteObject.queryLocalInterface("testObject");
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error: ' + error);
}

#### \[h2\]getDescriptor9+

getDescriptor(): string

Obtains the interface descriptor of this object. The interface descriptor is a string.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900008 | The proxy or remote object is invalid. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}
try {
  let testObject = new TestRemoteObject("ipcTest");
  let descriptor = testObject.getDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is ' + descriptor);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]getInterfaceDescriptor(deprecated)

getInterfaceDescriptor(): string

Obtains the interface descriptor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/L59w3ac2R-q6xvj-ySruhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=518588EEC5CA924F756129AFB105EDEDAD2EA5F9815C3F12B9885A89BBCF5F53)

This API is supported since API version 7 and deprecated since API version 9. Use [getDescriptor](#getdescriptor9-2) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Interface descriptor obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption): boolean | Promise<boolean> {
    // Process services based on the actual service logic.
    return true;
  }
}

try {
  let testRemoteObject = new TestRemoteObject("testObject");
  let descriptor = testRemoteObject.getInterfaceDescriptor();
  hilog.info(0x0000, 'testTag', 'RpcServer: descriptor is: ' + descriptor);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]modifyLocalInterface9+

modifyLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

Binds an interface descriptor to an **IRemoteBroker** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localInterface | [IRemoteBroker](#iremotebroker) | Yes | **IRemoteBroker** object. |
| descriptor | string | Yes | **IRemoteBroker** object bound to the interface descriptor. The length of the descriptor must be less than 40960 bytes. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The string length is greater than or equal to 40960 bytes;

4.The number of bytes copied to the buffer is different from the length of the obtained string.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    try {
      this.modifyLocalInterface(this, descriptor);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
      hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
    }
  }
  registerDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // Implement the method logic based on service requirements.
  }
  unregisterDeathRecipient(recipient: MyDeathRecipient, flags: number) {
    // Implement the method logic based on service requirements.
  }
}
let testRemoteObject = new TestRemoteObject("testObject");

#### \[h2\]attachLocalInterface(deprecated)

attachLocalInterface(localInterface: IRemoteBroker, descriptor: string): void

Binds an interface descriptor to an **IRemoteBroker** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/MSM93oSaRPWWwY5Ywq_z2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BD0E8B611D1C17232945F53576FAF2E9E4C3D69FCA5E7E02F433CAE0138A269)

This API is supported since API version 7 and deprecated since API version 9. Use [modifyLocalInterface](#modifylocalinterface9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| localInterface | [IRemoteBroker](#iremotebroker) | Yes | **IRemoteBroker** object. |
| descriptor | string | Yes | Interface descriptor. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
    this.attachLocalInterface(this, descriptor);
  }
  addDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // Implement the method logic based on service requirements.
    return true;
  }
  removeDeathRecipient(recipient: MyDeathRecipient, flags: number): boolean {
    // Implement the method logic based on service requirements.
    return true;
  }
}
let testRemoteObject = new TestRemoteObject("testObject");

#### Ashmem8+

Provides methods related to anonymous shared memory objects, including creating, closing, mapping, and unmapping an **Ashmem** object, reading data from and writing data to an **Ashmem** object, obtaining the **Ashmem** size, and setting **Ashmem** protection.

The shared memory applies only to cross-process communication within the local device.

**System capability**: SystemCapability.Communication.IPC.Core

#### \[h2\]Properties

**System capability**: SystemCapability.Communication.IPC.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| PROT\_EXEC | number | Yes | No | Mapped memory protection type, indicating that the mapped memory is executable. |
| PROT\_NONE | number | Yes | No | Mapped memory protection type, indicating that the mapped memory cannot be accessed. |
| PROT\_READ | number | Yes | No | Mapped memory protection type, indicating that the mapped memory is readable. |
| PROT\_WRITE | number | Yes | No | Mapped memory protection type, indicating that the mapped memory is readable. |

#### \[h2\]create9+

static create(name: string, size: number): Ashmem

Creates an **Ashmem** object with the specified name and size. This API is a static method.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **Ashmem** object to create. The length of the Ashmem name cannot be 0. |
| size | number | Yes | Size of the **Ashmem** object, in bytes. The value must be greater than 0. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | Returns the **Ashmem** object if it is created successfully; returns null otherwise. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The Ashmem name passed is empty;

4.The Ashmem size passed is less than or equal to 0.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]createAshmem(deprecated)

static createAshmem(name: string, size: number): Ashmem

Creates an **Ashmem** object with the specified name and size. This API is a static method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XjMLa9U7Q7iB1EEUQOwR0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9B91BE709E72E3F97969447D208AE88478635D8246098F93BB4DC0335C0989B)

This API is supported since API version 8 and deprecated since API version 9. Use [create](#create9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| name | string | Yes | Name of the **Ashmem** object to create. |
| size | number | Yes | Size (in bytes) of the **Ashmem** object to create. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | Returns the **Ashmem** object if it is created successfully; returns null otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.createAshmem("ashmem", 1024\*1024);
  hilog.info(0x0000, 'testTag', 'create ashmem: ' + ashmem);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag',  'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]create9+

static create(ashmem: Ashmem): Ashmem

Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem** objects point to the same shared memory region.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | Yes | Existing **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | **Ashmem** object created. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The passed parameter is not an Ashmem object;

3.The ashmem instance for obtaining packaging is empty.

 |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let ashmem2 = rpc.Ashmem.create(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]createAshmemFromExisting(deprecated)

static createAshmemFromExisting(ashmem: Ashmem): Ashmem

Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem** objects point to the same shared memory region.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/XegUKaqbSoSmrMoKDIAAjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40145FBE4318FF378B99B676573E3E1EF8CEFA89EFB6B39D926BDF6D6A7CD019)

This API is supported since API version 8 and deprecated since API version 9. Use [create](#create9-1) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ashmem | [Ashmem](#ashmem8) | Yes | Existing **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Ashmem](#ashmem8) | **Ashmem** object created. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let ashmem2 = rpc.Ashmem.createAshmemFromExisting(ashmem);
  let size = ashmem2.getAshmemSize();
  hilog.info(0x0000, 'testTag', 'size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]closeAshmem8+

closeAshmem(): void

Closes this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Ke4oW9H9T_KC36zL7UGkMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8D5DDE29F16CA4BA6F922D7223884BBA0CC9A0AE6B53125DE82482081697376)

Before closing the **Ashmem** object, you need to remove the address mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.closeAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]unmapAshmem8+

unmapAshmem(): void

Deletes the mappings for the specified address range of this **Ashmem** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.unmapAshmem();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]getAshmemSize8+

getAshmemSize(): number

Obtains the memory size of this **Ashmem** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | **Ashmem** size obtained. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let size = ashmem.getAshmemSize();
  hilog.info(0x0000, 'testTag', ' size is ' + size);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]mapTypedAshmem9+

mapTypedAshmem(mapType: number): void

Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is specified by this **Ashmem** object.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mapType | number | Yes | Protection level of the memory region to which the shared file is mapped. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The passed mapType exceeds the maximum protection level.

 |
| 1900001 | Failed to call mmap. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapTypedAshmem(rpc.Ashmem.PROT\_READ | rpc.Ashmem.PROT\_WRITE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]mapAshmem(deprecated)

mapAshmem(mapType: number): boolean

Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is specified by this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/TxFUHZPBQPC0S42Sf6YTxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A392CB3D8418BEDFE06A6B5BC8FF9DE6591DAC21826874CFE4FC5BBD1C2EFCA)

This API is supported since API version 8 and deprecated since API version 9. Use [mapTypedAshmem](#maptypedashmem9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mapType | number | Yes | Protection level of the memory region to which the shared file is mapped. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the mapping is created; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let mapReadAndWrite = ashmem.mapAshmem(rpc.Ashmem.PROT\_READ | rpc.Ashmem.PROT\_WRITE);
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapReadAndWrite);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]mapReadWriteAshmem9+

mapReadWriteAshmem(): void

Maps the shared file to the readable and writable virtual address space of the process.

**System capability**: SystemCapability.Communication.IPC.Core

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900001 | Failed to call mmap. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadWriteAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]mapReadAndWriteAshmem(deprecated)

mapReadAndWriteAshmem(): boolean

Maps the shared file to the readable and writable virtual address space of the process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/8QxRHYloSAmyLadYpghWqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5241E51FEC47CBAA66025F40E1F7E535E3F7769CCDFB15A87AC583A0F9CD2AF)

This API is supported since API version 8 and deprecated since API version 9. Use [mapReadWriteAshmem](#mapreadwriteashmem9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the mapping is created; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'map ashmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]mapReadonlyAshmem9+

mapReadonlyAshmem(): void

Maps the shared file to the read-only virtual address space of the process.

**System capability**: SystemCapability.Communication.IPC.Core

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 1900001 | Failed to call mmap. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadonlyAshmem();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]mapReadOnlyAshmem(deprecated)

mapReadOnlyAshmem(): boolean

Maps the shared file to the read-only virtual address space of the process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/XFvDCfrdTvm79Qah4wbR3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF9F5E8BDE50E587F537E1DD2436A9B3FF85833C8E7171928A5ACF68865959B0)

This API is supported since API version 8 and deprecated since API version 9. Use [mapReadonlyAshmem](#mapreadonlyashmem9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the mapping is created; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let mapResult = ashmem.mapReadOnlyAshmem();
  hilog.info(0x0000, 'testTag', 'Ashmem mapReadOnlyAshmem result is ' + mapResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]setProtectionType9+

setProtectionType(protectionType: number): void

Sets the protection level of the memory region to which the shared file is mapped.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| protectionType | number | Yes | Protection type to set. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900002 | Failed to call ioctl. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.setProtectionType(rpc.Ashmem.PROT\_READ);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc set protection type fail, errorMessage ' + e.message);
}

#### \[h2\]setProtection(deprecated)

setProtection(protectionType: number): boolean

Sets the protection level of the memory region to which the shared file is mapped.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/SOewqgDPQp2erWXjR7UMNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCDD6BCD434B06B141E095BEE043A4E906B6A39BCD5A47C24F3F412167FA68EF)

This API is supported since API version 8 and deprecated since API version 9. Use [setProtectionType](#setprotectiontype9) instead.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| protectionType | number | Yes | Protection type to set. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let result = ashmem.setProtection(rpc.Ashmem.PROT\_READ);
  hilog.info(0x0000, 'testTag', 'Ashmem setProtection result is ' + result);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'error ' + error);
}

#### \[h2\]writeDataToAshmem11+

writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void

Writes data to the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/ttvRwFAtRsCCZD3xUMTxYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0FDA6BAAC561CCD1BBD17629F626C04E31C98D38E5B230D05866D6ED3C45754)

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | ArrayBuffer | Yes | Data to write. |
| size | number | Yes | Size of the data to write. |
| offset | number | Yes | Start position of the data to write in the memory region associated with this **Ashmem** object. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.Failed to obtain arrayBuffer information.

 |
| 1900003 | Failed to write data to the shared memory. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]writeAshmem(deprecated)

writeAshmem(buf: number\[\], size: number, offset: number): void

Writes data to the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/yEgnB6FJRiGzrmr6cXkdzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEA7C401BCE51A0C89EE429D553BFE73F0FAD5CEB1ED0B185D44DC4C1F95EA39)

This API is supported since API version 9 and deprecated since API version 11. Use [writeDataToAshmem](#writedatatoashmem11) instead.

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | number\[\] | Yes | Data to write. |
| size | number | Yes | Size of the data to write. |
| offset | number | Yes | Start position of the data to write in the memory region associated with this **Ashmem** object. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match;

3.The element does not exist in the array.

 |
| 1900003 | Failed to write data to the shared memory. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'Rpc write to ashmem fail, errorMessage ' + e.message);
}

#### \[h2\]writeToAshmem(deprecated)

writeToAshmem(buf: number\[\], size: number, offset: number): boolean

Writes data to the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/JabPuUoTSnyrpAMC8xjKAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=996EF8395B21474BC0BCBC0F71851979535C29DF148BB78EF1ACD5AF446386BF)

This API is supported since API version 8 and deprecated since API version 9. Use [writeDataToAshmem](#writedatatoashmem11) instead.

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buf | number\[\] | Yes | Data to write. |
| size | number | Yes | Size of the data to write. |
| offset | number | Yes | Start position of the data to write in the memory region associated with this **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the data is written successfully; returns **false** otherwise. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}

#### \[h2\]readDataFromAshmem11+

readDataFromAshmem(size: number, offset: number): ArrayBuffer

Reads data from the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/sDggtT0USziQJNPhyLEjFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DA03EB1AA6996D1BDC59AE8B462638AA3342874E66921810FEA80D91BFA6FB2)

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the data to read. |
| offset | number | Yes | Start position of the data to read in the memory region associated with this **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Data read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900004 | Failed to read data from the shared memory. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let buffer = new ArrayBuffer(1024);
  let int32View = new Int32Array(buffer);
  for (let i = 0; i < int32View.length; i++) {
    int32View\[i\] = i \* 2 + 1;
  }
  let size = buffer.byteLength;
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadWriteAshmem();
  ashmem.writeDataToAshmem(buffer, size, 0);
  let readResult = ashmem.readDataFromAshmem(size, 0);
  let readInt32View = new Int32Array(readResult);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readInt32View);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readAshmem(deprecated)

readAshmem(size: number, offset: number): number\[\]

Reads data from the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Rn1vDNiPQbyLYY6fC5lPIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89A9174E6BEEECF0A0BE5538E755B7BEFE0A07EE7DF9C4CEEF1F49935778D787)

This API is supported since API version 9 and deprecated since API version 11. Use [readDataFromAshmem](#readdatafromashmem11) instead.

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the data to read. |
| offset | number | Yes | Start position of the data to read in the memory region associated with this **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Data read. |

**Error codes**

For details about the error codes, see [RPC Error Codes](../../error-codes/rpc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1.The number of parameters is incorrect;

2.The parameter type does not match.

 |
| 1900004 | Failed to read data from the shared memory. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  ashmem.mapReadWriteAshmem();
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  ashmem.writeAshmem(ByteArrayVar, 5, 0);
  let readResult = ashmem.readAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read from Ashmem result is ' + readResult);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  hilog.error(0x0000, 'testTag', 'errorCode ' + e.code);
  hilog.error(0x0000, 'testTag', 'errorMessage ' + e.message);
}

#### \[h2\]readFromAshmem(deprecated)

readFromAshmem(size: number, offset: number): number\[\]

Reads data from the shared file associated with this **Ashmem** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/INyVJOJUSWikYVNDp_affg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062325Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1949DBC73928424A951206F05E921C82A4987BFC567F66CAE8E5BD8C7B3E642)

This API is supported since API version 8 and deprecated since API version 9. Use [readDataFromAshmem](#readdatafromashmem11) instead.

Before writing an **Ashmem** object, you need to call [mapReadWriteAshmem](#mapreadwriteashmem9) for mapping.

**System capability**: SystemCapability.Communication.IPC.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | number | Yes | Size of the data to read. |
| offset | number | Yes | Start position of the data to read in the memory region associated with this **Ashmem** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number\[\] | Data read. |

**Example**

import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let ashmem = rpc.Ashmem.create("ashmem", 1024\*1024);
  let mapResult = ashmem.mapReadAndWriteAshmem();
  hilog.info(0x0000, 'testTag', 'RpcTest map ashmem result is ' + mapResult);
  let ByteArrayVar = \[1, 2, 3, 4, 5\];
  let writeResult = ashmem.writeToAshmem(ByteArrayVar, 5, 0);
  hilog.info(0x0000, 'testTag', 'write to Ashmem result is ' + writeResult);
  let readResult = ashmem.readFromAshmem(5, 0);
  hilog.info(0x0000, 'testTag', 'read to Ashmem result is ' + readResult);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'error is ' + error);
}
