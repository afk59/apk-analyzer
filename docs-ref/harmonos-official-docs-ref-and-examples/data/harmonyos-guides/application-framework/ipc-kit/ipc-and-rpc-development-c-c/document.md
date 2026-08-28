# IPC and RPC Development (C/C++)

#### When to Use

Inter-process communication (IPC) allows the proxy and stub running in different processes to communicate with each other using C/C++ APIs.

The IPC C APIs do not provide the capability of obtaining the communication proxy object. This feature depends on [Ability Kit](../../ability-kit/about-this-kit/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/pzPFspzASZOtIWI_qVORZQ/en-us_image_0000002537765072.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D318B9E56869E3C6A010E78A4E095482C31571CB8040D5B68B3EDCF6ECE3E564)

This document describes how to use the IPC C APIs.

#### Available APIs

**Table 1** Key APIs

| API | Description |
| :-- | :-- |
| 
typedef int (\*OH\_OnRemoteRequestCallback)

(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,

void \*userData);

 | Called to process the peer request at the stub. |
| 

OHIPCRemoteStub\* OH\_IPCRemoteStub\_Create

(const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback,

OH\_OnRemoteDestroyCallback destroyCallback, void \*userData);

 | Creates an **OHIPCRemoteStub** object. |
| 

int OH\_IPCRemoteProxy\_SendRequest(const OHIPCRemoteProxy \*proxy,

uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply,

const OH\_IPC\_MessageOption \*option);

 | Sends an IPC message. |
| struct OHIPCRemoteProxy; | Defines an **OHIPCRemoteProxy** object, which is used to send requests to the peer end. The **OHIPCRemoteProxy** object is returned by an ability API. |
| 

OHIPCDeathRecipient\* OH\_IPCDeathRecipient\_Create

(OH\_OnDeathRecipientCallback deathRecipientCallback,

OH\_OnDeathRecipientDestroyCallback destroyCallback,

void \*userData);

 | Creates an **OHIPCRemoteStub** object, which triggers a notification when the **OHIPCDeathRecipient** object dies unexpectedly. |
| 

int OH\_IPCRemoteProxy\_AddDeathRecipient(OHIPCRemoteProxy \*proxy,

OHIPCDeathRecipient \*recipient);

 | Subscribes to the death of an **OHIPCRemoteStub** object for an **OHIPCRemoteProxy** object. |

For details about the APIs, see [IPCKit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ipckit).

#### How to Develop

Create a stub object on the server, obtain the proxy object of the client through ability APIs, and use the proxy object to communicate with the stub object on the server through IPC. Then, register the death notification callback of the remote object to detect the death status of the process hosting the remote stub object.

## Adding Dynamic Link Libraries

Add the following libraries to **CMakeLists.txt**.

\# ipc capi
libipc\_capi.so
# Ability C/C++ APIs
libchild\_process.so

## Adding Header Files

// IPC C/C++ APIs
#include <IPCKit/ipc\_kit.h>
// Ability C/C++ APIs
#include <AbilityKit/native\_child\_process.h>

## Implementing IPC

**Common Data and Functions**

#include <string>
#include <thread>
#include <mutex>
#include <chrono>
#include <condition\_variable>
#include <IPCKit/ipc\_kit.h>
#include <AbilityKit/native\_child\_process.h>
#include <hilog/log.h>
#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x0201
#define LOG\_TAG "IPCCApiSample"

enum RequestCode {
    ASYNC\_ADD\_CODE = 1,
    REQUEST\_EXIT\_CODE = 2,
    OTHER\_CODE
};
static constexpr int MAX\_MEMORY\_SIZE = 204800;
static const std::string INTERFACE\_DESCRIPTOR = "INTERFACE\_DESCRIPTOR";
static const std::string NATIVE\_REMOTE\_STUB\_TEST\_TOKEN = "native.remote.stub";
static const std::string NATIVE\_REMOTE\_STUB\_ASYNC\_CALL\_TEST\_TOKEN = "native.remote.stub.async.call";

// Define the memory allocation function.
static void\* LocalMemoryAllocator(int32\_t len) {
    if (len < 0 || len > MAX\_MEMORY\_SIZE ) {
        return nullptr;
    }
    void \*buffer = malloc(len);
    if (buffer == nullptr) {
        return nullptr;
    }
    memset(buffer, 0, len);
    return buffer;
}

**Server Object IpcCApiStubTest**

class IpcCApiStubTest {
public:
    explicit IpcCApiStubTest();
    ~IpcCApiStubTest();
    void MainProc();
    OHIPCRemoteStub\* GetRemoteStub();
    static int OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData);
private:
    int AsyncAdd(const OHIPCParcel \*data);
    int RequestExitChildProcess();
private:
    OHIPCRemoteStub \*stub\_{ nullptr };
    std::mutex childMutex\_;
    std::condition\_variable childCondVar\_;
};

IpcCApiStubTest::IpcCApiStubTest() {
    // Create a stub object.
    stub\_ = OH\_IPCRemoteStub\_Create(INTERFACE\_DESCRIPTOR.c\_str(), &IpcCApiStubTest::OnRemoteRequest,
        nullptr, this);
}

IpcCApiStubTest::~IpcCApiStubTest() {
    if (stub\_ != nullptr) {
        // Destroy the stub object when it is no longer used.
        OH\_IPCRemoteStub\_Destroy(stub\_);
    }
}

void IpcCApiStubTest::MainProc() {
    std::unique\_lock<std::mutex> autoLock(childMutex\_);
    childCondVar\_.wait(autoLock);
}

OHIPCRemoteStub\* IpcCApiStubTest::GetRemoteStub() {
    return stub\_;
}

// Request processing function of the server. Requests sent by the client are processed in this function.
int IpcCApiStubTest::OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data, OHIPCParcel \*reply, void \*userData) {
    int readLen = 0;
    char \*token = nullptr;
    // Verify the current communication based on interfaceToken sent by the client.
    if (OH\_IPCParcel\_ReadInterfaceToken(data, &token, &readLen, LocalMemoryAllocator) != OH\_IPC\_SUCCESS
        || NATIVE\_REMOTE\_STUB\_TEST\_TOKEN != token) {
        if (token != nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "check InterfaceToken failed");
            free(token);
        }
        return OH\_IPC\_PARCEL\_WRITE\_ERROR;
    }
    free(token);
    auto \*stubTest = reinterpret\_cast<IpcCApiStubTest \*>(userData);
    if (stubTest == nullptr) {
        return OH\_IPC\_CHECK\_PARAM\_ERROR;
    }
    auto rqCode = RequestCode(code);
    switch (rqCode) {
        case ASYNC\_ADD\_CODE: {
            return stubTest->AsyncAdd(data);
        }
        case REQUEST\_EXIT\_CODE: {
            return stubTest->RequestExitChildProcess();
        }
        default:
            break;
    }
    return OH\_IPC\_SUCCESS;
}

int IpcCApiStubTest::AsyncAdd(const OHIPCParcel \*data) {
    int a = 0;
    int b = 0;
    OH\_LOG\_INFO(LOG\_APP, "start async add a=%d,b=%d", a, b);
    if ((OH\_IPCParcel\_ReadInt32(data, &a) != OH\_IPC\_SUCCESS)
        || (OH\_IPCParcel\_ReadInt32(data, &b) != OH\_IPC\_SUCCESS)) {
        return OH\_IPC\_PARCEL\_READ\_ERROR;
    }
    // Obtain the proxy object for IPC.
    auto proxyCallBack = OH\_IPCParcel\_ReadRemoteProxy(data);
    if (proxyCallBack == nullptr) {
        return OH\_IPC\_PARCEL\_READ\_ERROR;
    }
    OH\_LOG\_INFO(LOG\_APP, "start create sendCallBack thread!");
    // Define asynchronous thread processing and use proxyCallBack to respond to asynchronous results. To implement synchronous calls, use replyData to write the response result.
    std::thread th(\[proxyCallBack, a, b\] {
        auto data = OH\_IPCParcel\_Create();
        if (data == nullptr) {
            // If the parcel fails to be created, destroy the obtained proxyCallBack object.
            OH\_IPCRemoteProxy\_Destroy(proxyCallBack);
            return;
        }
        auto reply = OH\_IPCParcel\_Create();
        if (reply == nullptr) {
            OH\_IPCParcel\_Destroy(data);
            OH\_IPCRemoteProxy\_Destroy(proxyCallBack);
            return;
        }
        if (OH\_IPCParcel\_WriteInt32(data, a + b) != OH\_IPC\_SUCCESS) {
            OH\_IPCParcel\_Destroy(data);
            OH\_IPCParcel\_Destroy(reply);
            OH\_IPCRemoteProxy\_Destroy(proxyCallBack);
            return;
        }
        // The asynchronous thread processing result is returned to the service requester in IPC synchronous calls.
        OH\_IPC\_MessageOption option = { OH\_IPC\_REQUEST\_MODE\_SYNC, 0 };
        OH\_LOG\_INFO(LOG\_APP, "thread start sendCallBack!");
        // Send an IPC request.
        int ret = OH\_IPCRemoteProxy\_SendRequest(proxyCallBack, ASYNC\_ADD\_CODE, data, reply, &option);
        OH\_LOG\_INFO(LOG\_APP, "thread sendCallBack ret = %d", ret);
        if (ret != OH\_IPC\_SUCCESS) {
            OH\_IPCParcel\_Destroy(data);
            OH\_IPCParcel\_Destroy(reply);
            OH\_IPCRemoteProxy\_Destroy(proxyCallBack);
            return;
        }
        OH\_IPCRemoteProxy\_Destroy(proxyCallBack);
        OH\_IPCParcel\_Destroy(data);
        OH\_IPCParcel\_Destroy(reply);
    });
    th.detach();
    return OH\_IPC\_SUCCESS;
}

int IpcCApiStubTest::RequestExitChildProcess() {
    std::unique\_lock<std::mutex> autoLock(childMutex\_);
    childCondVar\_.notify\_all();
    return OH\_IPC\_SUCCESS;
}

**Client Proxy Object IpcCApiProxyTest**

// User-defined error code.
static constexpr int OH\_IPC\_CREATE\_OBJECT\_ERROR = OH\_IPC\_USER\_ERROR\_CODE\_MIN + 1;

class IpcCApiProxyTest {
public:
    explicit IpcCApiProxyTest(OHIPCRemoteProxy \*proxy);
    ~IpcCApiProxyTest();
public:
    int AsyncAdd(int a, int b, int &result);
    int RequestExitChildProcess();
    void ClearResource();
private:
    void SendAsyncReply(int &replyValue);
    int WaitForAsyncReply(int timeOut);
    // Note: OnRemoteRequest is the callback function used by the stub object to process IPC requests. This function does not need to be implemented on the proxy side.
    // OnRemoteRequest is the callback function used by the asynchronous callback object (replyStub\_) to process IPC requests.
    static int OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data,
        OHIPCParcel \*reply, void \*userData);
    static void OnDeathRecipientCB(void \*userData);
private:
    int asyncReply\_{};
    std::mutex mutex\_;
    std::condition\_variable cv\_;
    OHIPCRemoteProxy \*proxy\_{ nullptr };
    OHIPCRemoteStub \*replyStub\_{ nullptr };
    OHIPCDeathRecipient \*deathRecipient\_{ nullptr };
};

IpcCApiProxyTest::IpcCApiProxyTest(OHIPCRemoteProxy \*proxy) {
    if (proxy == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "proxy is nullptr");
        return;
    }
    proxy\_ = proxy;
    replyStub\_ = OH\_IPCRemoteStub\_Create(NATIVE\_REMOTE\_STUB\_ASYNC\_CALL\_TEST\_TOKEN.c\_str(), OnRemoteRequest,
        nullptr, this);
    if (replyStub\_ == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "create reply stub failed!");
        return;
    }
    // Create a death callback object.
    deathRecipient\_ = OH\_IPCDeathRecipient\_Create(OnDeathRecipientCB, nullptr, this);
    if (deathRecipient\_ == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCDeathRecipient\_Create failed!");
        return;
    }
    // Register the death callback object with the proxy to detect the death status of the stub object on the server.
    OH\_IPCRemoteProxy\_AddDeathRecipient(proxy\_, deathRecipient\_);
}

IpcCApiProxyTest::~IpcCApiProxyTest() {
    if (proxy\_ != nullptr) {
        OH\_IPCRemoteProxy\_Destroy(proxy\_);
    }
    if (deathRecipient\_ != nullptr) {
        OH\_IPCDeathRecipient\_Destroy(deathRecipient\_);
    }
    if (replyStub\_ != nullptr) {
        OH\_IPCRemoteStub\_Destroy(replyStub\_);
    }
}

int IpcCApiProxyTest::AsyncAdd(int a, int b, int &result) {
    OH\_LOG\_INFO(LOG\_APP, "start %d + %d", a, b);
    auto data = OH\_IPCParcel\_Create();
    if (data == nullptr) {
        return OH\_IPC\_CREATE\_OBJECT\_ERROR;
    }
    // Write the interface token for verification.
    if (OH\_IPCParcel\_WriteInterfaceToken(data, NATIVE\_REMOTE\_STUB\_TEST\_TOKEN.c\_str()) != OH\_IPC\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCParcel\_WriteInterfaceToken failed!");
        OH\_IPCParcel\_Destroy(data);
        return OH\_IPC\_PARCEL\_WRITE\_ERROR;
    }
    if (OH\_IPCParcel\_WriteInt32(data, a) != OH\_IPC\_SUCCESS
        || OH\_IPCParcel\_WriteInt32(data, b) != OH\_IPC\_SUCCESS
        || OH\_IPCParcel\_WriteRemoteStub(data, replyStub\_) != OH\_IPC\_SUCCESS) {
        OH\_IPCParcel\_Destroy(data);
        return OH\_IPC\_PARCEL\_WRITE\_ERROR;
    }
    // Use replyStub\_ to receive responses in asynchronous transmission. In asynchronous processing, the OHIPCRemoteStub object for receiving the result needs to be written.
    OH\_IPC\_MessageOption option = { OH\_IPC\_REQUEST\_MODE\_ASYNC, 0 };
    int ret = OH\_IPCRemoteProxy\_SendRequest(proxy\_, RequestCode::ASYNC\_ADD\_CODE, data, nullptr, &option);
    if (ret != OH\_IPC\_SUCCESS) {
        OH\_IPCParcel\_Destroy(data);
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCRemoteProxy\_SendRequest failed!");
        return ret;
    }
    static constexpr int TIMEOUT = 3;
    WaitForAsyncReply(TIMEOUT);
    OH\_LOG\_INFO(LOG\_APP, "asyncReply\_:%d", asyncReply\_);
    result = asyncReply\_;
    OH\_IPCParcel\_Destroy(data);
    return OH\_IPC\_SUCCESS;
}

int IpcCApiProxyTest::RequestExitChildProcess() {
    auto data = OH\_IPCParcel\_Create();
    if (data == nullptr) {
        return OH\_IPC\_CREATE\_OBJECT\_ERROR;
    }
    auto reply = OH\_IPCParcel\_Create();
    if (reply == nullptr) {
        OH\_IPCParcel\_Destroy(data);
        return OH\_IPC\_CREATE\_OBJECT\_ERROR;
    }
    if (OH\_IPCParcel\_WriteInterfaceToken(data, NATIVE\_REMOTE\_STUB\_TEST\_TOKEN.c\_str()) != OH\_IPC\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCParcel\_WriteInterfaceToken failed!");
        OH\_IPCParcel\_Destroy(data);
        OH\_IPCParcel\_Destroy(reply);
        return OH\_IPC\_PARCEL\_WRITE\_ERROR;
    }
    OH\_IPC\_MessageOption option = { OH\_IPC\_REQUEST\_MODE\_SYNC, 0 };
    int ret = OH\_IPCRemoteProxy\_SendRequest(proxy\_, RequestCode::REQUEST\_EXIT\_CODE, data, reply, &option);
    if (ret != OH\_IPC\_SUCCESS) {
        OH\_IPCParcel\_Destroy(data);
        OH\_IPCParcel\_Destroy(reply);
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCRemoteProxy\_SendRequest failed!");
        return ret;
    }
    OH\_IPCParcel\_Destroy(data);
    OH\_IPCParcel\_Destroy(reply);
    return OH\_IPC\_SUCCESS;
}

void IpcCApiProxyTest::SendAsyncReply(int &replyValue) {
    std::unique\_lock<std::mutex> lck(mutex\_);
    asyncReply\_ = replyValue;
    cv\_.notify\_all();
}

int IpcCApiProxyTest::WaitForAsyncReply(int timeOut) {
    asyncReply\_ = 0;
    std::unique\_lock<std::mutex> lck(mutex\_);
    cv\_.wait\_for(lck, std::chrono::seconds(timeOut), \[&\] {
        return asyncReply\_ != 0;
    });
    return asyncReply\_;
}

int IpcCApiProxyTest::OnRemoteRequest(uint32\_t code, const OHIPCParcel \*data,
        OHIPCParcel \*reply, void \*userData) {
    OH\_LOG\_INFO(LOG\_APP, "start %u", code);
    auto \*proxyTest = reinterpret\_cast<IpcCApiProxyTest \*>(userData);
    if (proxyTest == nullptr || code != static\_cast<uint32\_t>(RequestCode::ASYNC\_ADD\_CODE)) {
        OH\_LOG\_ERROR(LOG\_APP, "check param failed!");
        return OH\_IPC\_CHECK\_PARAM\_ERROR;
    }
    int32\_t val = -1;
    if (OH\_IPCParcel\_ReadInt32(data, &val) != OH\_IPC\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_IPCParcel\_ReadInt32 failed!");
        return OH\_IPC\_PARCEL\_READ\_ERROR;
    }
    proxyTest->SendAsyncReply(val);
    return OH\_IPC\_SUCCESS;
}

void IpcCApiProxyTest::ClearResource() {
    // clear resource;
}

void IpcCApiProxyTest::OnDeathRecipientCB(void \*userData) {
    auto \*proxyTest = reinterpret\_cast<IpcCApiProxyTest \*>(userData);
    if (proxyTest != nullptr) {
        proxyTest->ClearResource();
    }
    OH\_LOG\_INFO(LOG\_APP, "the stub is dead!");
}

**libipcCapiDemo.so for Server Calls**

IpcCApiStubTest g\_ipcStubObj;

#ifdef \_\_cplusplus
extern "C" {

// The following functions need to be implemented for the server. For details, see the Ability APIs.
OHIPCRemoteStub\* NativeChildProcess\_OnConnect() {
    OH\_LOG\_INFO(LOG\_APP, "NativeChildProcess\_OnConnect");
    return g\_ipcStubObj.GetRemoteStub();
}

void NativeChildProcess\_MainProc() {
    OH\_LOG\_INFO(LOG\_APP, "NativeChildProcess\_MainProc");
    g\_ipcStubObj.MainProc();
    OH\_LOG\_INFO(LOG\_APP, "NativeChildProcess\_MainProc End");
}

}
#endif

**Client Invocation Entry**

IpcCApiProxyTest \*g\_ipcProxy = nullptr;

// Callback to be invoked when the IPC channel is set up via the ability.
void OnNativeChildProcessStarted(int errCode, OHIPCRemoteProxy \*remoteProxy) {
    OH\_LOG\_INFO(LOG\_APP, "OnNativeChildProcessStarted proxy=%{public}p err=%{public}d", remoteProxy, errCode);
    if (remoteProxy == nullptr) {
        return;
    }
    g\_ipcProxy = new (std::nothrow) IpcCApiProxyTest(remoteProxy);
    if (g\_ipcProxy == nullptr) {
        OH\_IPCRemoteProxy\_Destroy(remoteProxy);
        OH\_LOG\_ERROR(LOG\_APP, "Alloc IpcCApiProxyTest object failed");
        return;
    }
}

int main(int argc, char \*argv\[\]) {
    // Call the ability API to create a child process and load the libipcCapiDemo.so file specified in the parameter. The process startup result is asynchronously notified through the callback parameter OnNativeChildProcessStarted. The proxy object is obtained from the callback function.
    int32\_t ret = OH\_Ability\_CreateNativeChildProcess("libipcCapiDemo.so", OnNativeChildProcessStarted);
    if (ret != 0) {
        return -1;
    }
    if (g\_ipcProxy == nullptr) {
        return -1;
    }
    int a = 2;
    int b = 3;
    int result = 0;
    ret = g\_ipcProxy->AsyncAdd(a, b, result);
    OH\_LOG\_INFO(LOG\_APP, "AsyncAdd: %d + %d = %d, ret=%d", a, b, result, ret);

    // Trigger the stub process to exit.
    ret = g\_ipcProxy->RequestExitChildProcess();
    // The death notification callback function (IpcCApiProxyTest::OnDeathRecipientCB) is automatically executed.
    if (g\_ipcProxy != nullptr) {
        delete g\_ipcProxy;
        g\_ipcProxy = nullptr;
    }
    return 0;
}
