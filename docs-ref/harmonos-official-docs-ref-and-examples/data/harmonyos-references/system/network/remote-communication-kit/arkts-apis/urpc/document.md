# urpc

This module provides the URPC function. Apps can initiate RPC requests through the code generation APIs provided by URPC. Common URPC methods include **urpcStubCreate**, **call**, **cancel**, and **destroy**.

**Start version**: 5.0.1(13)

#### Module Import

import { urpc } from "@kit.RemoteCommunicationKit";

#### FlowbufType

type FlowbufType =

'INT8' | 'UINT8' | 'INT16' | 'UINT16' | 'INT32' | 'UINT32' | 'INT64' | 'UINT64' | 'BOOL' | 'FLOAT' | 'DOUBLE' | 'STRING' | 'BYTES' | 'MESSAGE' | 'REPEATED\_INT8' | 'REPEATED\_UINT8' | 'REPEATED\_INT16' | 'REPEATED\_UINT16' | 'REPEATED\_INT32' | 'REPEATED\_UINT32' | 'REPEATED\_INT64' | 'REPEATED\_UINT64' | 'REPEATED\_BOOL' | 'REPEATED\_FLOAT' | 'REPEATED\_DOUBLE' | 'REPEATED\_STRING' | 'REPEATED\_BYTES' | 'REPEATED\_MESSAGE' | 'ARRAY\_INT8' | 'ARRAY\_UINT8' | 'ARRAY\_INT16' | 'ARRAY\_UINT16' | 'ARRAY\_INT32' | 'ARRAY\_UINT32' | 'ARRAY\_INT64' | 'ARRAY\_UINT64' | 'ARRAY\_BOOL' | 'ARRAY\_FLOAT' | 'ARRAY\_DOUBLE';

Defines value types supported by URPC communication.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'INT8'

 | 

The parameter type is INT8.

 |
| 

'UINT8'

 | 

The parameter type is UINT8.

 |
| 

'INT16'

 | 

The parameter type is INT16.

 |
| 

'UINT16'

 | 

The parameter type is UINT16.

 |
| 

'INT32'

 | 

The parameter type is INT32.

 |
| 

'UINT32'

 | 

The parameter type is UINT32.

 |
| 

'INT64'

 | 

The parameter type is INT64.

 |
| 

'UINT64'

 | 

The parameter type is UINT64.

 |
| 

'BOOL'

 | 

The parameter type is BOOL.

 |
| 

'FLOAT'

 | 

The parameter type is FLOAT.

 |
| 

'DOUBLE'

 | 

The parameter type is DOUBLE.

 |
| 

'STRING'

 | 

The parameter type is STRING.

 |
| 

'BYTES'

 | 

The parameter type is BYTES.

 |
| 

'MESSAGE'

 | 

The parameter type is MESSAGE, which is customized.

 |
| 

'REPEATED\_INT8'

 | 

The parameter type is a variable-length INT8 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_UINT8'

 | 

The parameter type is a variable-length UINT8 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_INT16'

 | 

The parameter type is a variable-length INT16 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_UINT16'

 | 

The parameter type is a variable-length UINT16 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_INT32'

 | 

The parameter type is a variable-length INT32 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_UINT32'

 | 

The parameter type is a variable-length UINT32 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_INT64'

 | 

The parameter type is a variable-length INT64 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_UINT64'

 | 

The parameter type is a variable-length UINT64 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_BOOL'

 | 

The parameter type is a variable-length BOOL array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_FLOAT'

 | 

The parameter type is a variable-length INT8 array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_DOUBLE'

 | 

The parameter type is a variable-length DOUBLE array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_STRING'

 | 

The parameter type is a variable-length STRING array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_BYTES'

 | 

The parameter type is a variable-length BYTES array. This field is reserved and cannot be used in this version.

 |
| 

'REPEATED\_MESSAGE'

 | 

The parameter type is a variable-length custom MESSAGE array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_INT8'

 | 

The parameter type is a fixed-length INT8 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_UINT8'

 | 

The parameter type is a fixed-length UINT8 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_INT16'

 | 

The parameter type is a fixed-length INT16 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_UINT16'

 | 

The parameter type is a fixed-length UINT16 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_INT32'

 | 

The parameter type is a fixed-length INT32 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_UINT32'

 | 

The parameter type is a fixed-length UINT32 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_INT64'

 | 

The parameter type is a fixed-length INT64 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_UINT64'

 | 

The parameter type is a fixed-length UINT64 array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_BOOL'

 | 

The parameter type is a fixed-length BOOL array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_FLOAT'

 | 

The parameter type is a fixed-length FLOAT array. This field is reserved and cannot be used in this version.

 |
| 

'ARRAY\_DOUBLE'

 | 

The parameter type is a fixed-length DOUBLE array. This field is reserved and cannot be used in this version.

 |

#### FlowbufElement<T>

Defines the types of non-array URPC input parameters and return values.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[FlowbufType](#section123121188272)

 | 

No

 | 

No

 | 

Defines value types supported by URPC communication.

 |
| 

value

 | 

T

 | 

No

 | 

No

 | 

Value of a parameter.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Name of a parameter.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit"

let version: urpc.FlowbufElement<number> = {type: 'INT8', value: 0, name: ""};

#### FlowbufArrayElement<T>

Defines the types of URPC input parameters and return values of the array type.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[FlowbufType](#section123121188272)

 | 

No

 | 

No

 | 

Value types supported by URPC communication.

 |
| 

value

 | 

T\[\]

 | 

No

 | 

No

 | 

Value of a parameter.

 |
| 

length

 | 

number

 | 

No

 | 

No

 | 

Length of the array. The value ranges from 0 to 2147483647.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit"

let version: urpc.FlowbufArrayElement<number> = {type: 'ARRAY\_INT8', value: \[1,2,3\], length: 3};

#### urpc.urpcStubCreate

urpcStubCreate(config: UrpcInitConfiguration, funcList: string | string\[\]): Promise<UrpcStub>

Creates UrpcStub. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Required permission**: ohos.permission.INTERNET

**Start version**: 5.0.1(13)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

config

 | 

[UrpcInitConfiguration](#section18613443123412)

 | 

Yes

 | 

Stub configuration.

 |
| 

funcList

 | 

string | string\[\]

 | 

Yes

 | 

List of URPC functions to be called.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[UrpcStub](#section1671892662116)\>

 | 

Promise object, which is used to return the object that can be used to send a URPC request.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
| 

401

 | 

Parameter error.

 |
| 

10079100998

 | 

Function name error.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit";

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
}
let config: urpc.UrpcInitConfiguration = {
  timeout: 3000,
  mode: 'client',
  connect: connect
}

const funcList:string\[\] = \["uploadFile"\];
let urpcStub = await urpc.urpcStubCreate(config, funcList);

#### UrpcCall

type UrpcCall = (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise;

Sends a URPC request and obtains an HTTP response from the server.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

funcName

 | 

string

 | 

Yes

 | 

Function name in a URPC request.

 |
| 

request

 | 

object

 | 

Yes

 | 

URPC request object. The maximum size of the request data is 1 MB.

 |
| 

returnValue

 | 

object

 | 

Yes

 | 

URPC response object. The maximum size of the received data is 100 KB.

 |
| 

config

 | 

[CallingOption](#section731665213712)

 | 

No

 | 

Configuration for a single request. This field is reserved and does not take effect in the current version.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[UrpcPromise](#section154329285418)

 | 

Promise object, which is used to return the response object from the server.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

#### UrpcCancel

type UrpcCancel = (callingId?: number | number\[\]) => void;

Cancels specified or all ongoing URPC requests.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callingId

 | 

number | number\[\]

 | 

No

 | 

Identifier of a request to be canceled. If this field is not set, all requests corresponding to the UrpcStub are canceled. The value ranges from 0 to 2147483647.

 |

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

#### UrpcDestroy

type UrpcDestroy = () => void

Destroys a [UrpcStub](#section1671892662116) instance.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

**Error codes**: For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

#### UrpcStub

Represents a communication session that can be used to initiate URPC requests and provides various remote call methods (such as **call**, **cancel**, and **destroy**).

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

**Parameters**:

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

id

 | 

number

 | 

Yes

 | 

No

 | 

Unique identifier of **UrpcStub**.

 |
| 

call

 | 

[UrpcCall](#section1223416820339)

 | 

No

 | 

No

 | 

Request for calling URPC.

 |
| 

cancel

 | 

[UrpcCancel](#section16128181393419)

 | 

No

 | 

No

 | 

Request for canceling URPC.

 |
| 

destroy

 | 

[UrpcDestroy](#section4758175133410)

 | 

No

 | 

No

 | 

Request for destroying **UrpcStub**.

 |

#### UrpcInitConfiguration

Defines session configurations to facilitate refined control over HTTP sessions.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

mode

 | 

[UrpcMode](#section1898141153617)

 | 

No

 | 

Yes

 | 

Running mode of URPC. The default value is **client**.

 |
| 

connect

 | 

[UrpcConnectConfiguration](#section4802256134519)

 | 

No

 | 

No

 | 

Stub-related connection configurations, including the IP address, port number, URPC connection protocol, and whether multipath is enabled.

 |
| 

timeout

 | 

number

 | 

No

 | 

No

 | 

URPC connection timeout interval, in milliseconds. The value ranges from 0 to 4294967295. This field is reserved and does not take effect in the current version.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit";

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
}
let config: urpc.UrpcInitConfiguration = {
  timeout: 3000,
  mode: 'client',
  connect: connect
}

#### UrpcMode

type UrpcMode = 'client';

Defines the mode of the URPC node. Currently, only the **client** mode is supported, indicating that the client can initiate requests and wait for responses from the server.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'client'

 | 

Mode of the URPC node. The value is fixed to **client**.

 |

#### UrpcConnectConfiguration

Defines key URPC connection configurations, including the IP address, port number, and optional parameters such as the transmission protocol.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

node

 | 

[IpAndPort](#section59321354193610)

 | 

No

 | 

No

 | 

IP address and port number for connection.

 |
| 

protocol

 | 

[UrpcProtocol](#section557714186379)

 | 

No

 | 

Yes

 | 

Transmission protocol type used for connection. The default value is **eat** (EAT).

 |
| 

multiPath

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to support multipath transmission. The value **true** indicates yes and the multiple paths include cellular network and Wi-Fi. The value **false** indicates no and is the default value. This field is reserved and does not take effect in the current version.

 |
| 

flags

 | 

number

 | 

No

 | 

Yes

 | 

Indicates whether to enable certificate verification. The default value is **0**, indicating yes. Any non-0 value indicates no.

 |
| 

host

 | 

string

 | 

No

 | 

Yes

 | 

Domain name of the URPC service. The default value is an empty string.

 |
| 

caPath

 | 

string

 | 

No

 | 

Yes

 | 

Path of the certificate to be verified. The default value is an empty string.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit"

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}
let connect: urpc.UrpcConnectConfiguration = {
  node: node,
  protocol: 'eat',
  multiPath: false,
  flags: 0,
  host: "127.0.0.1",
  caPath: "data/single\_urpc/eat.pem"
}

#### IpAndPort

Defines the IP address and port number for URPC connection.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ip

 | 

string

 | 

No

 | 

No

 | 

IPv4 or IPv6 address of URPC.

 |
| 

port

 | 

number

 | 

No

 | 

No

 | 

Port number for URPC connection. The value ranges from 0 to 65535.

 |

**Example**:

import { urpc } from "@kit.RemoteCommunicationKit"

let node: urpc.IpAndPort = {
  ip: '127.0.0.1',
  port: 8000
}

#### UrpcPromise

Returns a value to a URPC request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

promise

 | 

Promise<Object>

 | 

No

 | 

No

 | 

Response object of a URPC request.

 |
| 

callingId

 | 

number

 | 

No

 | 

No

 | 

Unique ID of a URPC request. The value ranges from 0 to 2147483647.

 |

#### UrpcProtocol

type UrpcProtocol = 'eat'

URPC connection protocol. Currently, only the **eat** option is supported.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'eat'

 | 

Transmission protocol of the URPC node. The value is fixed to **eat**.

 |

#### CallingOption

Priority of a URPC request.

**System capability**: SystemCapability.Collaboration.RemoteCommunication

**Start version**: 5.0.1(13)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

priority

 | 

number

 | 

No

 | 

Yes

 | 

Priority of a URPC request. The default value is **0** and the maximum value is **3** (highest priority). A request with a higher priority can be transmitted first. This field is reserved and does not take effect in the current version.

 |
