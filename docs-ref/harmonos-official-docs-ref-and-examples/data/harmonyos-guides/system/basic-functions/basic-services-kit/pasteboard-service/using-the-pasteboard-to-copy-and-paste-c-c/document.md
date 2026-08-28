# Using the Pasteboard to Copy and Paste (C/C++)

#### When to Use

The pasteboard allows you to copy and paste data of the plain text, hypertext, and URI.

#### Basic Concepts

-   [**OH\_PasteboardObserver**](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pasteboard-oh-pasteboardobserver): pasteboard observer object, which is used to listen for data changes on the pasteboard.
-   [**OH\_Pasteboard**](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pasteboard-oh-pasteboard): pasteboard object, which is used to query and write data.
-   [**OH\_UdmfData**](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-oh-udmfdata): unified data object.

#### Constraints

-   The pasteboard content, including system service metadata and application settings, has a maximum size of 128 MB by default. For PCs/2-in-1 devices, the maximum size can be changed through system settings, with a valid range from 128 MB to 2 GB.
-   To ensure the accuracy of the pasteboard data, only one copy can be performed at a time.
-   Currently, supported data types include **OH\_UdsPlainText** (plain text), **OH\_UdsHtml** (hypertext markup language), **OH\_UdsFileUri** (file URI). **OH\_UdsPixelMap** (pixel map), **OH\_UdsHyperlink** (hyperlink), **OH\_UdsAppItem** (application icon), and custom type. The data types supported by ArkTS APIs are different from those supported by NDK APIs. You need to match the data types with the corresponding APIs during usage. For details, see [Using the Pasteboard to Copy and Paste](../using-the-pasteboard-to-copy-and-paste/document.md#mapping-between-arkts-and-ndk-data-types).
-   When you copy and paste data of a custom type, the specified type name cannot be the same as an existing one.
-   Since API version 12, [permission control](../requesting-permissions-to-access-the-pasteboard/document.md) is added to the pasteboard reading API to enhance user privacy protection.
-   The [setUnifiedData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#setunifieddata12) and [getUnifiedData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getunifieddata12) APIs added in API version 12 are independent of the [OH\_Pasteboard\_SetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_setdata) and [OH\_Pasteboard\_GetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getdata) APIs mentioned in this topic. Use the corresponding APIs when writing and reading data.

#### Available APIs

For details about more APIs and their usage, see [Pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pasteboard).

| API | Description |
| :-- | :-- |
| OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create() | Creates a pasteboard observer object. |
| OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer) | Destroys the pasteboard observer object. |
| int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context, const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize) | Sets the callback used to return data changes to the pasteboard observer object. |
| OH\_Pasteboard\* OH\_Pasteboard\_Create() | Creates a pasteboard instance. |
| void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard) | Destroys the pasteboard instance. |
| int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | Subscribes to the pasteboard observer. |
| int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer) | Unsubscribes from the pasteboard observer. |
| bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard) | Checks whether the pasteboard data comes from remote devices. |
| int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len) | Obtains the pasteboard data source. |
| bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type) | Checks whether the pasteboard contains data of the specified type. |
| bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard) | Checks whether the pasteboard contains data. |
| OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status) | Obtains data from the pasteboard. |
| int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data) | Writes data to the pasteboard. |
| int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard) | Clears data from the pasteboard. |
| void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type) | Notifies data changes in the pasteboard. |
| void (\*Pasteboard\_Finalize)(void\* context) | Releases context resources when the pasteboard observer object is destroyed. |

#### How to Develop

1.  Add dynamic link libraries.
    
    \# Add the following libraries to \*\*CMakeLists.txt\*\*.
    libudmf.so
    libpasteboard.so
    
2.  Include header files.
    
    #include <cstdio>
    #include <cstring>
    #include <hilog/log.h>
    #include <database/pasteboard/oh\_pasteboard.h>
    #include <database/udmf/udmf.h>
    #include <database/udmf/uds.h>
    
3.  Define the callback for listening for pasteboard data changes.
    
    // Define the callback for notifying data changes in the pasteboard.
    static void PasteboardNotifyImpl2(void\* context, Pasteboard\_NotifyType type)
    {
        OH\_LOG\_INFO(LOG\_APP, "Pasteboard\_NotifyType, type: %d", type);
    }
    // Define the callback for notifying when the pasteboard observer object is destroyed.
    static void PasteboardFinalizeImpl2(void\* context)
    {
        OH\_LOG\_INFO(LOG\_APP, "callback: Pasteboard\_Finalize");
    }
    
4.  Subscribe to the pasteboard observer.
    
    static void PasteboardTestObserver()
    {
        // 1. Create a pasteboard instance.
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        // 2. Create a pasteboard observer instance.
        OH\_PasteboardObserver\* observer = OH\_PasteboardObserver\_Create();
        // 3. Set two callbacks to the pasteboard observer instance.
        OH\_PasteboardObserver\_SetData(observer, (void\*)pasteboard, PasteboardNotifyImpl2, PasteboardFinalizeImpl2);
        // 4. Subscribe to local data changes on the pasteboard.
        OH\_Pasteboard\_Subscribe(pasteboard, NOTIFY\_LOCAL\_DATA\_CHANGE, observer);
    }
    
5.  Write data to the pasteboard.
    
    static napi\_value NAPI\_Pasteboard\_set(napi\_env env, napi\_callback\_info info)
    {
        napi\_value args\[1\];
        size\_t argc = 1;
        napi\_status status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        char text\[256\];
        size\_t value0Size;
        status = napi\_get\_value\_string\_utf8(env, args\[0\], text, sizeof(text), &value0Size);
        // 1. Create a pasteboard instance.
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        if (pasteboard == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "Failed to create pasteboard instance.");
        };
        // 2. Create an OH\_UdmfRecord object and add text data to it.
        OH\_UdsPlainText\* udsPlainText = OH\_UdsPlainText\_Create();
        OH\_UdsPlainText\_SetContent(udsPlainText, text);
        OH\_UdsHtml\* udsHtml = OH\_UdsHtml\_Create();
        OH\_UdsHtml\_SetContent(udsHtml, "hello world");
        OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
        OH\_UdmfRecord\_AddPlainText(record, udsPlainText);
        OH\_UdmfRecord\_AddHtml(record, udsHtml);
        // 3. Create an OH\_UdmfData object and add OH\_UdmfRecord to it.
        OH\_UdmfData\* data = OH\_UdmfData\_Create();
        OH\_UdmfData\_AddRecord(data, record);
        // 4. Write data to the pasteboard.
        OH\_Pasteboard\_SetData(pasteboard, data);
        // 5. Destroy the pointer when the object is no longer required.
        OH\_UdsPlainText\_Destroy(udsPlainText);
        OH\_UdsHtml\_Destroy(udsHtml);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_Pasteboard\_Destroy(pasteboard);
        // ...
    }
    
6.  Read data from the pasteboard.
    
    static napi\_value NAPI\_Pasteboard\_get(napi\_env env, napi\_callback\_info info)
    {
        // 1. Create a pasteboard instance.
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        if (pasteboard == nullptr) {
            OH\_LOG\_INFO(LOG\_APP, "Failed to create pasteboard instance.");
        };
        // 2. Check whether the pasteboard contains text data.
        bool hasPlainTextData = OH\_Pasteboard\_HasType(pasteboard, "text/plain");
        if (hasPlainTextData) {
            // 3. Obtain the unified data OH\_UdmfData from the pasteboard.
            int ret = 0;
            OH\_UdmfData\* udmfData = OH\_Pasteboard\_GetData(pasteboard, &ret);
            if (udmfData == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get data from pasteboard.");
            };
            // 4. Obtain the first data record from OH\_UdmfData.
            OH\_UdmfRecord\* record = OH\_UdmfData\_GetRecord(udmfData, 0);
            if (record == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get record from udmfData.");
            };
            // 5. Obtain the text data from the data record.
            OH\_UdsPlainText\* plainText = OH\_UdsPlainText\_Create();
            if (plainText == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to create plain text object.");
            };
            OH\_UdmfRecord\_GetPlainText(record, plainText);
            const char\* content = OH\_UdsPlainText\_GetContent(plainText);
            if (content == nullptr) {
                OH\_LOG\_INFO(LOG\_APP, "Failed to get content from plain text.");
            }
            napi\_value result;
            napi\_create\_string\_utf8(env, content, strlen(content), &result);
            // 6. Destroy the pointer when the object is no longer required.
            OH\_UdsPlainText\_Destroy(plainText);
            OH\_UdmfRecord\_Destroy(record);
            return result;
        } else {
            OH\_LOG\_INFO(LOG\_APP, "No plain text data in pasteboard.");
        }
        OH\_Pasteboard\_Destroy(pasteboard);
    }
