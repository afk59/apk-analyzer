# Calling a Remote Program Using URPC

#### Use Case

Your app can send a URPC request, set parameters such as the priority, and receive a URPC response from the remote server. You can cancel a specified or all ongoing URPC requests based on your needs. After the request is completed, you need to close the session to release resources related to URPC.

#### Constraints

-   The capability of calling a remote program using URPC supports phones, 2-in-1 devices, tablets, wearables, and (since 5.1.1(19)) TVs.
-   This function requires a remote server. If you have this need, [submit an online ticket](https://developer.huawei.com/consumer/en/support/feedback/#/) to contact us.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-urpcapi#section848492671817).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

call: (funcName: string, request: object, returnValue: object, config?: CallingOption) => UrpcPromise

 | 

Sends a URPC request and obtains a URPC response from the server. This API returns the result asynchronously through a promise.

 |
| 

cancel: (callingId?: number | number\[\]) => void

 | 

Cancels a specified or all ongoing URPC requests. The return value is empty.

 |
| 

destroy: () => void

 | 

Destroys a **UrpcStub** instance.

 |

#### Example

## Creating urpcStub

1.  Import required modules.
    
    import { hilog } from "@kit.PerformanceAnalysisKit";
    import { urpc } from "@kit.RemoteCommunicationKit";
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Define the class for remote calls, which can be used to define both the input parameter and the return value of the called method. The following is an example:
    
    // Define the input parameter class of the method.
    export class MediaTaskRequestMessage {
      RequestMessage: urpc.FlowbufElement<string>;
    
      constructor() {
        this.RequestMessage = {type: 'STRING', value: "", name: ""};
      }
    
      setRequestMessage(RequestMessage: string) {
        this.RequestMessage.value = RequestMessage;
      }
    
      getRequestMessage(): string {
        return this.RequestMessage.value;
      }
    
    }
    
    // Define the class for receiving the return value of the called method.
    export class MediaTaskResponseMessage {
      ResponseMessage: urpc.FlowbufElement<string>;
    
      constructor() {
        this.ResponseMessage = {type: 'STRING', value: "", name: ""};
      }
    
      setResponseMessage(ResponseMessage: string) {
        this.ResponseMessage.value = ResponseMessage;
      }
    
      getResponseMessage(): string {
        return this.ResponseMessage.value;
      }
    
    }
    
3.  Create a request object and a response object.
    
    let request = new MediaTaskRequestMessage();
    let response = new MediaTaskResponseMessage();
    
4.  Configure the connection information and create **UrpcStub** for initiating URPC calls.
    
    // IP address and port number of the remote server that has been deployed in advance.
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
    let urpcStub = urpc.urpcStubCreate(config, funcList);
    

## Sending and Receiving Network Requests

urpcStub.then(async (stub: urpc.UrpcStub) =>{
  let upload\_config: urpc.CallingOption = {
    priority: 0
  };
  let urpcPromise = stub.call("uploadFile", request, response, upload\_config);
  urpcPromise.promise.then((resp: object) => {
    hilog.info(0x000, "urpc", "resp: %{public}s", resp);
  }).catch((err: BusinessError) => {
    hilog.error(0x000, "urpc", "the error code is %d", err.code);
  })
}).catch((error: BusinessError) => {
  hilog.error(0x000, "urpc", "urpc call failed, error code is %d", error.code);
})

## (Optional) Canceling Network Requests

After initiating a URPC request with **call**, you can call **cancel** to cancel the request with the specified **callingId** or all ongoing requests initiated using **UrpcStub** (if **callingId** is not specified) if you do not need to receive responses.

urpcStub.then(async (stub: urpc.UrpcStub) =>{
  let upload\_config: urpc.CallingOption = {
    priority: 0
  };
  let urpcPromise = stub.call("uploadFile", request, response, upload\_config);
  stub.cancel(urpcPromise.callingId);
}).catch((error: BusinessError) => {
  hilog.error(0x000, "urpc", "urpc cancel failed, error code is %d", error.code);
})

## Disabling URPC

After all URPC requests are processed as required, you can call **destroy** to release **UrpcStub**\-related resources.

urpcStub.then(async (stub: urpc.UrpcStub) =>{
  stub.destroy();
}).catch((error: BusinessError) => {
  hilog.error(0x000, "urpc", "urpc destroy failed, error code is %d", error.code);
})
