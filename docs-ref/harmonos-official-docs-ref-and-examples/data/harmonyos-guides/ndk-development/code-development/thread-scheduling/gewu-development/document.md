# Gewu Development

#### Scenario

The feature is supported since API version 20. On-device inference ensures user data privacy, low deployment costs, low latency, and high availability without being affected by networks. However, compared with cloud inference, on-device inference faces greater challenges such as limited memory resources, limited computing power, and sensitivity to power consumption. In addition, it needs to ensure user experience and prevent frame freezing when running services. To address these challenges, Gewu provides QoS-aware inference acceleration and resource management optimization. This topic describes how to use Gewu APIs.

#### APIs

## Error Codes

**OH\_QoS\_GewuErrorCode** is an enumeration type of Gewu error codes. For details about the error codes returned by each function, see the API description.

## Session Handles

Session handles are used to manage sessions. You can obtain a session handle by successfully creating a session through **OH\_QoS\_GewuSession**. The session handle can be used to submit or abort a request and destroy a session.

typedef unsigned int OH\_QoS\_GewuSession;

## Request Handles

Request handles are used to manage requests. You can obtain a request handle by successfully submitting a request through **OH\_QoS\_GewuSubmitRequest**. The request handle can be used to abort a request.

typedef unsigned int OH\_QoS\_GewuRequest;

## Functions

| Name | Description |
| :-- | :-- |
| OH\_QoS\_GewuCreateSession | Creates a session. |
| OH\_QoS\_GewuDestroySession | Destroys a session. |
| OH\_QoS\_GewuSubmitRequest | Submits a request. |
| OH\_QoS\_GewuAbortRequest | Aborts a request. |

**OH\_QoS\_GewuCreateSession**

**Description**

Creates a session asynchronously.

That is, this API only initiates a session creation request and does not wait until the session resource allocation and model loading are complete. Gewu optimizes on-device inference resource management and enables dynamic on-demand resource loading.

The lifecycle of a session object starts from the return of the **OH\_QoS\_GewuCreateSession** function and ends when the **OH\_QoS\_GewuDestroySession** function is called.

**Declaration**

typedef struct {
    OH\_QoS\_GewuSession session;
    OH\_QoS\_GewuErrorCode error;
} OH\_QoS\_GewuCreateSessionResult;

OH\_QoS\_GewuCreateSessionResult OH\_QoS\_GewuCreateSession(const char\* attributes);

**Parameters**

-   The const char attributes\* parameter indicates the JSON string of the session attribute. It supports the following fields:
    -   **"model"**: String. Path of the model used by the session.

Example of the JSON string of attributes:

{
    "model": "/data/storage/el2/base/files/qwen2/"
}

**Return Value**

If the session is created successfully, the value of **error** in the return value **OH\_QoS\_GewuCreateSessionResult** is **OH\_QOS\_GEWU\_OK**, and the value of **session** is the created session handle.

If the session fails to be created, the value of **error** in the return value **OH\_QoS\_GewuCreateSessionResult** is the cause of the error. **OH\_QOS\_GEWU\_NOMEM** indicates that no sufficient memory is available for creating the session.

**OH\_QoS\_GewuDestroySession**

**Description**

Destroys a session.

You are advised to wait until all requests are complete or aborted before calling this API. If there are ongoing requests when this API is called, the requests will be aborted, and you will not receive responses. Note that after this API is called, the session object cannot be used.

**Declaration**

OH\_QoS\_GewuErrorCode OH\_QoS\_GewuDestroySession(OH\_QoS\_GewuSession session);

**Parameters**

-   **OH\_QoS\_GewuSession session**: Handle to the session to be destroyed.

**Return Value**

If the session is destroyed successfully, the return value is **OH\_QOS\_GEWU\_OK**.

If the session fails to be destroyed, the return value is the cause of the error. **OH\_QOS\_GEWU\_NOENT** indicates that the session cannot be found.

**OH\_QoS\_GewuSubmitRequest**

**Description**

Submits a request asynchronously. That is, this API only initiates a request but does not directly return a result. When this API returns, the request may not be executed. The result is returned through your callback.

**Declaration**

typedef struct {
    OH\_QoS\_GewuRequest request;
    OH\_QoS\_GewuErrorCode error;
} OH\_QoS\_GewuSubmitRequestResult;

typedef void (\*OH\_QoS\_GewuOnResponse)(void\* context, const char\* response);

OH\_QoS\_GewuSubmitRequestResult OH\_QoS\_GewuSubmitRequest(OH\_QoS\_GewuSession session, const char\* request,
    OH\_QoS\_GewuOnResponse callback, void\* context);

**Parameters**

The parameters of the **OH\_QoS\_GewuSubmitRequest** function are as follows:

-   **OH\_QoS\_GewuSession session**: Session handle, indicating the session to which the request is submitted.
-   const char request\*: JSON string of the request. The following fields are supported:
    -   **"messages"**: Array. Array of messages. Each element supports the following fields:
        -   **"role"**: String. Role type of the message. **"developer"** indicates indications provided by developers or the system, **"user"** indicates user input, and **"assistant"** indicates the result generated by the model.
        -   **"content"**: String. Message content.
    -   **"stream"**: Boolean or null. Whether to enable streaming inference. By default, streaming inference is disabled.
-   **OH\_QoS\_GewuOnResponse callback**: callback of the request.
-   void context\*: context pointer provided by yourself, which is passed to the callback. In common cases, your code can find the request corresponding to the received response through this parameter for further processing.

The parameters of the **OH\_QoS\_GewuOnResponse** callback are as follows:

-   void context\*: **context** pointer passed in when **OH\_QoS\_GewuSubmitRequest** is called.
-   const char response\*: JSON string of the response, which contains the following fields:
    -   **"message"**: Response message, which contains the following fields:
        -   **"role"**: String. Role type of the message, which should be **"assistant"**.
        -   **"content"**: String. Message content.
    -   **"finish\_reason"**: String or null. Finish reason. The possible values are as follows:
        -   **null**: The request is not stopped. In streaming inference, there are multiple responses, and only the last response has a non-empty **finish\_reason**. In non-streaming inference, there is only one response, and **finish\_reason** is not empty.
        -   **"stop"**: The request is stopped normally.
        -   **"abort"**: The request is stopped by the user in advance.
        -   **"length"**: The number of tokens exceeds the upper limit.

**Return Value**

If the request is submitted successfully, the value of **error** in **OH\_QoS\_GewuSubmitRequestResult** is **OH\_QOS\_GEWU\_OK**, and the value of **request** is the request handle.

If the request fails to be submitted, the value of **error** in **OH\_QoS\_GewuSubmitRequestResult** is the cause of the error. **OH\_QOS\_GEWU\_NOMEM** indicates that memory is insufficient for processing the request.

**OH\_QoS\_GewuAbortRequest**

**Description**

Aborts a request in advance.

In normal cases, after calling the **OH\_QoS\_GewuSubmitRequest** API to submit a request, you only need to wait until the inference is complete (that is, the response where **"finish\_reason"** is not empty is received); you do not need to call the **OH\_QoS\_GewuAbortRequest** API.

You need to call the **OH\_QoS\_GewuAbortRequest** API only when you want to abort an inference request in advance.

After this function is successfully called, you will not receive any response to the request, and the request handle cannot be used.

**Declaration**

OH\_QoS\_GewuErrorCode OH\_QoS\_GewuAbortRequest(OH\_QoS\_GewuSession session, OH\_QoS\_GewuRequest request);

**Parameters**

-   **OH\_QoS\_GewuSession session**: Handle to the request session.
-   **OH\_QoS\_GewuRequest request**: Handle to the request to be aborted.

**Return Value**

If the request is aborted successfully, the return value is **OH\_QOS\_GEWU\_OK**.

If the request fails to be aborted, the return value is the cause of the error. **OH\_QOS\_GEWU\_NOENT** indicates that the request cannot be found.

#### Examples

The following is an example:

#include <future>
#define LOG\_TAG "DEMO"
#include <hilog/log.h>
#include <nlohmann/json.hpp>
#include <qos/qos.h>
#include <string>

#define DEMO\_LOGD(fmt, ...) OH\_LOG\_DEBUG(LOG\_APP, fmt, ##\_\_VA\_ARGS\_\_)
#define DEMO\_LOGI(fmt, ...) OH\_LOG\_INFO(LOG\_APP, fmt, ##\_\_VA\_ARGS\_\_)
#define DEMO\_LOGW(fmt, ...) OH\_LOG\_WARN(LOG\_APP, fmt, ##\_\_VA\_ARGS\_\_)
#define DEMO\_LOGE(fmt, ...) OH\_LOG\_ERROR(LOG\_APP, fmt, ##\_\_VA\_ARGS\_\_)

using json = nlohmann::json;

/\* Used to save the chat status \*/
struct ChatContext {
public:
    ChatContext()
    {
        future = promise.get\_future();
    }

    void Join()
    {
        assert(future.valid());
        std::string stopReasonStr = future.get();
        DEMO\_LOGI("stopReasonStr=%s", stopReasonStr.c\_str());
    }

    std::promise<std::string> promise;
    std::future<std::string> future;
    std::string responseContent;
    bool earlyAbort = false;
};

/\* Callback triggered when the inference result is received \*/
void OnChatResponse(void \*context, const char \*response)
{
    ChatContext \*chatContext = static\_cast<ChatContext \*>(context);
    if (chatContext->earlyAbort) {
        DEMO\_LOGD("ignore response after early abort");
        return;
    }
    try {
        json responseJson = json::parse(response);
        chatContext->responseContent += responseJson.at("message").at("content").get<std::string>();
        json finishReasonJson = responseJson.at("finish\_reason");
        if (!finishReasonJson.is\_null()) {
            /\* finish \*/
            std::string finishReasonStr = finishReasonJson.get<std::string>();
            chatContext->promise.set\_value(finishReasonStr);
        } else if (chatContext->responseContent.find("\\n") != std::string::npos) {
            /\* customized stop \*/
            chatContext->promise.set\_value("customized");
            chatContext->earlyAbort = true;
        } else {
            /\* continue \*/
            ;
        }
    } catch (json::exception &e) {
        DEMO\_LOGE("failed to parse response: %s", e.what());
    }
}

int Demo(void)
{
    DEMO\_LOGI("Demo starts");
    json attrJson = {
        /\* Path of the model file. Change it with the actual path. \*/
        {"model", "/data/storage/el2/base/files/qwen2-awq"},
    };
    std::string attrStr = attrJson.dump(4);

    /\* Create a session \*/
    OH\_QoS\_GewuCreateSessionResult createResult = OH\_QoS\_GewuCreateSession(attrStr.c\_str());
    if (createResult.error != OH\_QOS\_GEWU\_OK) {
        DEMO\_LOGE("failed to create session, error=%d", (int)createResult.error);
        return -1;
    }
    OH\_QoS\_GewuSession session = createResult.session;

    /\* Create and submit a request \*/
    ChatContext context;
    json requestJson = {
        {"messages", json::array({
            {{"role", "developer"}, {"content", "You are a helpful assistant"}},
            {{"role", "user"}, {"content", "What is LLM?"}},
        })},
        {"stream", true},
    };
    std::string requestStr = requestJson.dump(4);
    OH\_QoS\_GewuSubmitRequestResult submitResult = OH\_QoS\_GewuSubmitRequest(session, requestStr.c\_str(),
                                                                           OnChatResponse, &context);
    if (submitResult.error != OH\_QOS\_GEWU\_OK) {
        DEMO\_LOGE("failed to submit request, error=%d", (int)submitResult.error);
        return -1;
    }
    OH\_QoS\_GewuRequest request = submitResult.request;
    context.Join();

    /\* Abort the request in advance \*/
    if (context.earlyAbort) {
        OH\_QoS\_GewuErrorCode error = OH\_QoS\_GewuAbortRequest(session, request);
        if (error != OH\_QOS\_GEWU\_OK) {
            DEMO\_LOGE("failed to abort request, error=%d", (int)error);
            return -1;
        }
    }

    /\* Print the result \*/
    DEMO\_LOGI("response: %s", context.responseContent.c\_str());

    /\* Destroy the session \*/
    OH\_QoS\_GewuErrorCode error = OH\_QoS\_GewuDestroySession(session);
    if (error != OH\_QOS\_GEWU\_OK) {
        DEMO\_LOGE("failed to destroy session, error=%d", (int)error);
        return -1;
    }
    return 0;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Te9RyEmmRji7R-b04G8vMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3C0412A23651E164AEE24407322D6DC1F2BFE3F18B75C672602E424297845A)

In the demo code, the third-party library nlohmann/json is used to simplify the parsing and construction of JSON data. nlohmann/json is a modern C++ JSON library that provides an intuitive and concise way to handle JSON data.

Its design concept is to make JSON operations as natural as using STL containers.

You can download the **json.hpp** file and save it to the **include** directory of the project. No additional library file is required.
