# Using the Delayed Copy and Paste Feature of the Pasteboard

#### When to Use

The [pasteboard service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard) provides the capability of managing the pasteboard of the system to support the copy and paste functions of the system.

When copy is performed repeatedly, redundant data is stored in the pasteboard cache, which increases the memory usage. To optimize the memory and support the paste of specified data types, the pasteboard provides the delayed copy and paste function.

When a user copies data in an application that uses the delayed copy and paste function, the real data is not immediately written into the cache of the pasteboard service, but is obtained from the application when the data needs to be pasted.

#### Constraints

-   The pasteboard content, including system service metadata and application settings, has a maximum size of 128 MB by default. For PCs/2-in-1 devices, the maximum size can be changed through system settings, with a valid range from 128 MB to 2 GB.
    
-   NDK APIs support only record-based delayed copy and paste.
    
-   If the amount of data to be copied is small and the time required for preparing data does not affect user experience, avoid using the delayed copy feature. Instead, you are advised to write data directly to the pasteboard.
    

#### Using Record-based Delayed Copy and Paste

This solution allows you to query the data type before pasting. Applications can determine whether to request data from the pasteboard based on the query result.

Since API version 21, when an application exits, it can call [OH\_Pasteboard\_SetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_setdata) to submit all copied data and call [OH\_Pasteboard\_SyncDelayedDataAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_syncdelayeddataasync) to notify the pasteboard to obtain all data.

1.  When the application uses the delayed copy feature, only the data types supported by the application are written to the pasteboard. Before exiting, the application should call [OH\_Pasteboard\_SetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_setdata) to submit all copied data or call [OH\_Pasteboard\_SyncDelayedDataAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_syncdelayeddataasync) to sync data to the pasteboard. The application can exit only after data sync is complete. Otherwise, other applications may fail to obtain data.
    
2.  Calling the [OH\_Pasteboard\_SyncDelayedDataAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_syncdelayeddataasync) API prolongs the exit process. Applications should copy data to the pasteboard directly instead of calling the [OH\_UdmfRecordProvider\_SetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-h#oh_udmfrecordprovider_setdata) and [OH\_Pasteboard\_SyncDelayedDataAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_syncdelayeddataasync) APIs.
    
3.  If an application exits abnormally when it uses the delayed copy feature, the data sync cannot be triggered. As a result, other applications cannot obtain data to paste.
    

## Available APIs

For details about the APIs, see [Pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pasteboard) and [UDMF](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf).

| Name | Description |
| :-- | :-- |
| OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create() | Creates a pointer to the **OH\_UdmfRecordProvider** instance. |
| int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize) | Sets a callback for the **OH\_UdmfRecordProvider**. |
| int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider) | Sets **OH\_UdmfRecordProvider** in an **OH\_UdmfRecord** instance. |
| int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data) | Writes data to the pasteboard. |
| OH\_UdmfData \* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status) | Obtains data from the pasteboard. |
| OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count) | Obtains all data records from an **OH\_UdmfData** instance. |
| void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode)) | Syncs all delayed data from the application to the pasteboard. When the application uses the delayed copy feature, only the data types supported by the application are written to the pasteboard. Before exiting, the application should call [OH\_Pasteboard\_SetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_setdata) to submit all copied data or call [OH\_Pasteboard\_SyncDelayedDataAsync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_syncdelayeddataasync) to sync data to the pasteboard. The application can exit only after data sync is complete. Otherwise, other applications may fail to obtain data. |

## How to Develop

The following uses plain text and HTML data as an example to describe how to set delayed data copy to the pasteboard service.

For better code readability, the operation result verification of each step is omitted in the following code. In actual development, you need to check whether each call is successful.

1.  Include header files.
    
    #include <cstring>
    #include <hilog/log.h>
    #include <database/pasteboard/oh\_pasteboard.h>
    #include <database/udmf/udmf.h>
    #include <database/udmf/uds.h>
    #include <database/udmf/udmf\_meta.h>
    #include <accesstoken/ability\_access\_control.h>
    
2.  Define a data providing function for **OH\_UdmfRecordProvider** and a callback function for destroying this instance.
    
    // 1. Define a callback to be invoked to return the pasteboard data obtained.
    void\* GetDataCallback(void\* context, const char\* type)
    {
        // Plain text type.
        if (memcmp(type, UDMF\_META\_PLAIN\_TEXT, sizeof(UDMF\_META\_PLAIN\_TEXT) - 1) == 0) {
            // Create a Uds object of the plain text type.
            OH\_UdsPlainText\* udsText = OH\_UdsPlainText\_Create();
            // Set the plain text content.
            OH\_UdsPlainText\_SetContent(udsText, "hello world");
            return udsText;
        } else if (strcmp(type, UDMF\_META\_HTML) == 0) {
            // Create a Uds object of the HTML type.
            OH\_UdsHtml\* udsHtml = OH\_UdsHtml\_Create();
            // Set the HTML content.
            OH\_UdsHtml\_SetContent(udsHtml, "<div>hello world</div>");
            return udsHtml;
        }
        return nullptr;
    }
    // 2. Define a callback to be invoked when OH\_UdmfRecordProvider is destroyed.
    void ProviderFinalizeCallback(void\* context)
    {
        OH\_LOG\_INFO(LOG\_APP, "OH\_UdmfRecordProvider finalize.");
    }
    
3.  Define the **OH\_Pasteboard\_SyncDelayedDataAsync** callback.
    
    // 3. Define the callback triggered when the application exits and calls the delayed data sync API.
    void SyncCallback(int errorCode)
    {
        // Application exits.
    }
    
4.  Prepare the data for delayed copy in the pasteboard. The plain text and HTML data is not written to the pasteboard until the **GetDataCallback** function is triggered when the data consumer obtains **OH\_UdsPlainText** or **OH\_UdsHtml** from **OH\_UdmfRecord**.
    
    OH\_Pasteboard\* CreateAndSetPasteboardData()
    {
        // 4. Create an OH\_UdmfRecord object.
        OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
        // 5. Create an OH\_UdmfRecordProvider object and set two callback functions used to provide and destruct data.
        OH\_UdmfRecordProvider\* provider = OH\_UdmfRecordProvider\_Create();
        OH\_UdmfRecordProvider\_SetData(provider, (void \*)record, GetDataCallback, ProviderFinalizeCallback);
        // 6. Bind the provider to the record and set the supported data type.
        #define TYPE\_COUNT 2
        const char\* types\[TYPE\_COUNT\] = {UDMF\_META\_PLAIN\_TEXT, UDMF\_META\_HTML};
        OH\_UdmfRecord\_SetProvider(record, types, TYPE\_COUNT, provider);
        // 7. Create an OH\_UdmfData object and add OH\_UdmfRecord to it.
        OH\_UdmfData\* setData = OH\_UdmfData\_Create();
        if (setData != nullptr) {
            OH\_UdmfData\_AddRecord(setData, record);
        }
        // 8. Create an OH\_Pasteboard object and write data to the pasteboard.
        OH\_Pasteboard\* pasteboard = OH\_Pasteboard\_Create();
        if (setData != nullptr) {
            OH\_Pasteboard\_SetData(pasteboard, setData);
        }
        OH\_UdmfRecordProvider\_Destroy(provider);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(setData);
        return pasteboard;
    }
    
5.  Obtain the data for delayed copy from the pasteboard.
    
    void ProcessRecordType(OH\_UdmfRecord\* record, const char\* recordType)
    {
        OH\_UdsPlainText\* udsText = nullptr;
        OH\_UdsHtml\* udsHtml = nullptr;
        if (strcmp(recordType, UDMF\_META\_PLAIN\_TEXT) == 0) {
            // Create a Uds object of the plain text type.
            udsText = OH\_UdsPlainText\_Create();
            if (udsText != nullptr) {
                // Obtain the Uds object of the plain text type from record.
                OH\_UdmfRecord\_GetPlainText(record, udsText);
                // Obtain the content from the Uds object.
                const char\* content = OH\_UdsPlainText\_GetContent(udsText);
            } else if (strcmp(recordType, UDMF\_META\_HTML) == 0) {
                // Create a Uds object of the HTML type.
                udsHtml = OH\_UdsHtml\_Create();
                if (udsHtml != nullptr) {
                    // Obtain the Uds object of the HTML type from record.
                    OH\_UdmfRecord\_GetHtml(record, udsHtml);
                    // Obtain the content from the Uds object.
                    const char\* content = OH\_UdsHtml\_GetContent(udsHtml);
                }
            }
        }
    }
    void ProcessRecord(OH\_UdmfRecord\* record)
    {
        // 13. Query the data types in OH\_UdmfRecord.
        unsigned typeCount = 0;
        char\*\* recordTypes = OH\_UdmfRecord\_GetTypes(record, &typeCount);
        // 14. Traverse data types.
        for (unsigned int typeIndex = 0; typeIndex < typeCount; ++typeIndex) {
            const char\* recordType = recordTypes\[typeIndex\];
            ProcessRecordType(record, recordType);
        }
    }
    
    static napi\_value NAPI\_Pasteboard\_time(napi\_env env, napi\_callback\_info info)
    {
        OH\_Pasteboard\* pasteboard = CreateAndSetPasteboardData();
        // 9. Record the number of changes to pasteboard data.
        uint32\_t changeCount = OH\_Pasteboard\_GetChangeCount(pasteboard);
    
        // 10. Obtain OH\_UdmfData from the pasteboard.
        int status = -1;
        bool hasPermission = OH\_AT\_CheckSelfPermission("ohos.permission.READ\_PASTEBOARD");
        if (!hasPermission) {
            OH\_LOG\_ERROR(LOG\_APP, "No Permission READ\_PASTEBOARD");
        };
        OH\_UdmfData\* getData = OH\_Pasteboard\_GetData(pasteboard, &status);
        if (getData == nullptr) {
            // Handle the error case and clear resources.
            OH\_LOG\_ERROR(LOG\_APP, "Failed to get data from pasteboard, status: %d\\n", status);
        }
    
        // 11. Obtain all OH\_UdmfRecord objects from OH\_UdmfData.
        unsigned int recordCount = 0;
        OH\_UdmfRecord\*\* getRecords = OH\_UdmfData\_GetRecords(getData, &recordCount);
        OH\_UdsPlainText\* udsText = nullptr;
        OH\_UdsHtml\* udsHtml = nullptr;
    
        // 12. Traverse OH\_UdmfRecord.
        for (unsigned int recordIndex = 0; recordIndex < recordCount; ++recordIndex) {
            OH\_UdmfRecord\* record = getRecords\[recordIndex\];
            ProcessRecord(record);
        }
    
6.  If the data in the pasteboard does not change, the application notifies the pasteboard to obtain all data before exiting and exits only after the callback is complete. Otherwise, other applications may fail to obtain data.
    
    // 15. Check whether the data in the pasteboard changes.
    uint32\_t newChangeCount = OH\_Pasteboard\_GetChangeCount(pasteboard);
    if (newChangeCount == changeCount) {
        // 16. Notify the pasteboard to obtain all data.
        OH\_Pasteboard\_SyncDelayedDataAsync(pasteboard, SyncCallback);
        // The application exits only after SyncCallback is complete.
    } else {
        // Application exits.
        OH\_LOG\_INFO(LOG\_APP, "No newChangeCount in pasteboard.");
    }
    
7.  Release the memory after the objects are used.
    
        OH\_UdsPlainText\_Destroy(udsText);
        OH\_UdsHtml\_Destroy(udsHtml);
        OH\_UdmfData\_Destroy(getData);
        OH\_Pasteboard\_Destroy(pasteboard);
    }
