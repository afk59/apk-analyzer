# Sharing Data via Unified Data Channels (C/C++)

#### When to Use

In many-to-many data sharing across applications, a data channel needs to be provided to write data of different applications and share the data with other applications.

The Unified Data Management Framework (UDMF) provides unified data channels and standard APIs for writing and reading data across applications in different service scenarios.

#### Definition and Implementation of Unified Data Channels

Unified data channels are used to write and read data across applications in various service scenarios. They can temporarily store unified data objects that need to be shared by applications and comply with unified data definitions, and provide the data objects for other applications to access. In addition, they can modify temporarily stored data, delete permissions, and manage lifecycles based on certain policies.

The unified data channel is implemented by the system ability provided by UDMF. When an application (data provider) needs to share data, it calls the **insertData()** method to write the data to the UDMF data channel, and calls **updateData()** or **deleteData()** to update or delete the data saved by the application. The target application (data consumer) can access the data by the APIs provided by UDMF.

Avoid using **unifiedDataChannel** APIs in multi-threaded calls.

The unified data object (**UnifiedData**) is uniquely identified by a URI in the UDMF data channel. The URI is in the **udmf://intention/bundleName/groupId** format, where:

-   **udmf**: protocol used to provide the data channel.
    
-   **intention**: an enum of the data channel types supported by UDMF.
    
-   **bundleName**: bundle name of the data source application.
    
-   **groupId**: group ID used for batch data management.
    

Currently, UDMF provides the public data channel for cross-application data sharing.

The public data channel allows all applications to write data into it. When data is written, a unique identifier is generated, which can be used to update, delete, and query the specified data, or perform a full query. To read all data in the public data channel, set **Intention** to **DATA\_HUB**. The public data channel is used only to transmit process data between applications and cannot be used to transmit permission-controlled data, such as files in sandbox directories. UDMF manages the data lifecycle in a unified manner and deletes the data that has been stored for more than one hour every hour.

#### Available APIs

For details about the APIs, see [UDMF](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-udmf-h).

| API | Description |
| :-- | :-- |
| OH\_UdsHyperlink\* OH\_UdsHyperlink\_Create() | Creates a pointer to an **OH\_UdsHyperlink** instance. |
| int OH\_UdsHyperlink\_SetDescription(OH\_UdsHyperlink\* pThis, const char\* description) | Sets the description parameter in an **OH\_UdsHyperlink** instance. |
| OH\_UdmfRecord\* OH\_UdmfRecord\_Create() | Creates a pointer to an **OH\_UdmfRecord** instance. |
| int OH\_UdmfRecord\_AddHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | Adds hyperlink data to an **OH\_UdmfRecord** instance. |
| OH\_UdmfData\* OH\_UdmfData\_Create() | Creates a pointer to an **OH\_UdmfData** instance. |
| int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record) | Adds an **OH\_UdmfRecord** to an **OH\_UdmfData** instance. |
| int OH\_Udmf\_SetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData \*unifiedData, char \*key, unsigned int keyLen) | Sets an **OH\_UdmfData** instance in the UDMF database. |
| void OH\_UdsHyperlink\_Destroy(OH\_UdsHyperlink\* pThis) | Destroys the pointer to an **OH\_UdsHyperlink** instance. |
| void OH\_UdmfRecord\_Destroy(OH\_UdmfRecord\* pThis) | Destroys the pointer to an **OH\_UdmfRecord** instance. |
| void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis) | Destroys the pointer to an **OH\_UdmfData** instance. |
| char\*\* OH\_UdmfRecord\_GetTypes(OH\_UdmfRecord\* pThis, unsigned int\* count) | Obtains all data types from an **OH\_UdmfRecord** instance. |
| int OH\_UdmfRecord\_GetHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink) | Obtains the hyperlink data from an **OH\_UdmfRecord** instance. |
| int OH\_Udmf\_GetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | Obtains an **OH\_UdmfData** instance from the UDMF database based on the data channel type. |
| int OH\_Udmf\_UpdateUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\* unifiedData) | Updates an **OH\_UdmfData** instance in the UDMF database. |
| int OH\_Udmf\_DeleteUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize) | Deletes an **OH\_UdmfData** instance from the UDMF database. |
| bool OH\_UdmfData\_HasType(OH\_UdmfData\* pThis, const char\* type) | Checks whether the specified type exists in an **OH\_UdmfData** instance. |
| OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count) | Obtains all data records from an **OH\_UdmfData** instance. |
| OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create() | Creates a pointer to the **OH\_UdmfRecordProvider** instance. |
| int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize) | Sets a callback for the **OH\_UdmfRecordProvider**. |
| int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider) | Sets **OH\_UdmfRecordProvider** in an **OH\_UdmfRecord** instance. |
| OH\_UdmfOptions\* OH\_UdmfOptions\_Create() | Creates a pointer to an **OH\_UdmfOptions** instance. |
| void OH\_UdmfOptions\_Destroy(OH\_UdmfOptions\* pThis) | Destroys the pointer to an **OH\_UdmfOptions** instance. |

#### Adding Dynamic Link Libraries

Add the following libraries to **CMakeLists.txt**.

libudmf.so, libhilog\_ndk.z.so

#### Including Header Files

#include <cstdio>
#include <cstring>
#include <database/udmf/utd.h>
#include <database/udmf/uds.h>
#include <database/udmf/udmf.h>
#include <database/udmf/udmf\_meta.h>
#include <database/udmf/udmf\_err\_code.h>
#include <hilog/log.h>

#undef LOG\_TAG
#define LOG\_TAG "MY\_LOG"

#### Writing UDS Data Using UDMF

To write the **OH\_UdsHyperlink** data, perform the following steps:

1.  Create a UDS data structure for hyperlink.
2.  Set the URL and description for the hyperlink.
3.  Create an **OH\_UdmfRecord** object and add the hyperlink data to it.
4.  Create an **OH\_UdmfData** object and add **OH\_UdmfRecord** to it.
5.  Construct an **OH\_UdmfOptions**.
6.  Construct and write data to the database. The key of the data is returned.
7.  Destroy all the pointers created.

int32\_t SetHyperlinkData(OH\_UdsHyperlink\* hyperlink, OH\_UdmfRecord\* record, OH\_UdmfData\* data)
{
    // 2. Set the URL and description for the hyperlink.
    int ret = OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo.com");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set url error!");
        return ret;
    }
    ret = OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the description.");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set description error!");
        return ret;
    }
    // 3. Add the hyperlink data to OH\_UdmfRecord.
    ret = OH\_UdmfRecord\_AddHyperlink(record, hyperlink);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add hyperlink to record error!");
        return ret;
    }
    // 4. Add OH\_UdmfRecord to OH\_UdmfData.
    ret = OH\_UdmfData\_AddRecord(data, record);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add record to data error!");
        return ret;
    }
    return UDMF\_E\_OK;
}

int32\_t CreateDataTest()
{
    // 1. Create the UDS data struct, OH\_UdmfRecord object, and OH\_UdmfData object of the hyperlink.
    OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    int32\_t ret = SetHyperlinkData(hyperlink, record, data);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        return ret;
    }
    // Construct an OH\_UdmfOptions.
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 6. Construct and write data to the database. The key of the data is returned.
    char key\[UDMF\_KEY\_BUFFER\_LEN\] = {0};
    ret = OH\_Udmf\_SetUnifiedDataByOptions(options, data, key, sizeof(key));
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_LOG\_INFO(LOG\_APP, "key = %{public}s", key);
    // 7. Destroy all the pointers created.
    OH\_UdsHyperlink\_Destroy(hyperlink);
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}

#### Obtaining UDS Data Using UDMF

To obtain the **OH\_UdsHyperlink** data, perform the following steps:

1.  Construct an **OH\_UdmfOptions**.
2.  Obtain data through **OH\_UdmfOptions**.
3.  Check whether **OH\_UdmfData** has the required data type.
4.  Obtain data records and hyperlink data.
5.  Destroy all the pointers created.

int32\_t ProcessHyperlinks(OH\_UdmfRecord\* record, unsigned int recordTypeIdCount, char\*\* typeIdsFromRecord)
{
    for (unsigned int k = 0; k < recordTypeIdCount; k++) {
         // Obtain the hyperlink data from OH\_UdmfRecord.
        if (strcmp(typeIdsFromRecord\[k\], UDMF\_META\_HYPERLINK) == 0) {
             // Create a UDS to hold the hyperlink data read from the unified record.
            OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
            int32\_t ret = OH\_UdmfRecord\_GetHyperlink(record, hyperlink);
            if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Fail get hyperlink from record!");
                return ret;
            }
            // Read information in OH\_UdsHyperlink.
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink type id is : %{public}s", OH\_UdsHyperlink\_GetType(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink url is : %{public}s", OH\_UdsHyperlink\_GetUrl(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink description is : %{public}s",
                OH\_UdsHyperlink\_GetDescription(hyperlink));
            OH\_UdsHyperlink\_Destroy(hyperlink);
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessData(OH\_UdmfData\* data)
{
    unsigned int recordsCount = 0;
    OH\_UdmfRecord\*\* records = OH\_UdmfData\_GetRecords(data, &recordsCount);
    OH\_LOG\_INFO(LOG\_APP, "the count of records count is %{public}u", recordsCount);
    for (unsigned int j = 0; j < recordsCount; j++) {
        // Obtain the OH\_UdmfRecord type list.
        unsigned int recordTypeIdCount = 0;
        char\*\* typeIdsFromRecord = OH\_UdmfRecord\_GetTypes(records\[j\], &recordTypeIdCount);
        int32\_t ret = ProcessHyperlinks(records\[j\], recordTypeIdCount, typeIdsFromRecord);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "ProcessRecordHyperlinks error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t HandleUdmfHyperlinkData(OH\_UdmfData\* readData, unsigned int dataSize, OH\_UdmfData\*\* dataArray)
{
    for (unsigned int i = 0; i < dataSize; i++) {
        OH\_UdmfData\* data = OH\_UDMF\_GetDataElementAt(dataArray, i);
         // 3. Check whether OH\_UdmfData has the required data type.
        if (!OH\_UdmfData\_HasType(data, UDMF\_META\_HYPERLINK)) {
            OH\_LOG\_INFO(LOG\_APP, "There is no hyperlink type in data\[%{public}u\].", i);
            continue;
        }
        // 4. Obtain data records and hyperlink data.
        int32\_t ret = ProcessData(data);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "Process data error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t GetDataTest()
{
    // 1. Construct an OH\_UdmfOptions.
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    int32\_t ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 2. Obtain data through OH\_UdmfOptions.
    unsigned int dataSize = 0;
    OH\_UdmfData\* readData = nullptr;
    ret = OH\_Udmf\_GetUnifiedDataByOptions(options, &readData, &dataSize);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Get Data error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_UdmfOptions\_Destroy(options);
    OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
    OH\_UdmfData\*\* dataArray = &readData;
    ret = HandleUdmfHyperlinkData(readData, dataSize, dataArray);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Get Data error!");
        return ret;
    }
    // 5. Destroy all the pointers created.
    OH\_Udmf\_DestroyDataArray(dataArray, dataSize);
    return UDMF\_E\_OK;
}

#### Updating UDS Data Using UDMF

To update the **OH\_UdsHyperlink** data, perform the following steps:

1.  Create a UDS data structure for hyperlink.
2.  Set the URL and description for the hyperlink.
3.  Create an **OH\_UdmfRecord** object and add the hyperlink data to it.
4.  Create an **OH\_UdmfData** object and add **OH\_UdmfRecord** to it.
5.  Construct an **OH\_UdmfOptions**.
6.  Update data and write the data to the database.
7.  Destroy all the pointers created.

int32\_t AddHyperlinkToUdmfRecord(OH\_UdsHyperlink\* hyperlink, OH\_UdmfRecord\* record, OH\_UdmfData\* data)
{
    // 2. Set the URL and description for the hyperlink.
    int32\_t ret = OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo2.com");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set url error!");
        return ret;
    }
    ret = OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the new description.");
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Hyperlink set description error!");
        return ret;
    }
    // 3. Add the hyperlink data to OH\_UdmfRecord.
    ret = OH\_UdmfRecord\_AddHyperlink(record, hyperlink);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add hyperlink to record error!");
        return ret;
    }
    // 4. Add OH\_UdmfRecord to OH\_UdmfData.
    ret = OH\_UdmfData\_AddRecord(data, record);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Add record to data error!");
        return ret;
    }
    return UDMF\_E\_OK;
}

int32\_t UpdateDataTest()
{
    // 1. Create the UDS data struct, OH\_UdmfRecord object, and OH\_UdmfData object of the hyperlink.
    OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    int32\_t ret = AddHyperlinkToUdmfRecord(hyperlink, record, data);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Fail to create hyperlink!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        return ret;
    }
    // 5. Construct an OH\_UdmfOptions.
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    // The key here is an example and cannot be directly used. The key must be the same as that returned by OH\_Udmf\_SetUnifiedDataByOptions.
    char key\[\] = "udmf://DataHub/com.ohos.test/0123456789";
    ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK
        || OH\_UdmfOptions\_SetKey(options, key) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 6. Update data and write the data to the database.
    ret = OH\_Udmf\_UpdateUnifiedData(options, data);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Update data error!");
        OH\_UdsHyperlink\_Destroy(hyperlink);
        OH\_UdmfRecord\_Destroy(record);
        OH\_UdmfData\_Destroy(data);
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_LOG\_INFO(LOG\_APP, "update data success");
    // 7. Destroy all the pointers created.
    OH\_UdsHyperlink\_Destroy(hyperlink);
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}

#### Deleting UDS Data Using UDMF

To delete the **OH\_UdsHyperlink** data, perform the following steps:

1.  Construct an **OH\_UdmfOptions**.
2.  Delete data through **OH\_UdmfOptions**.
3.  Check whether **OH\_UdmfData** has the required data type.
4.  Obtain data records and hyperlink data.
5.  Obtain elements in data records.
6.  Destroy all the pointers created.

int32\_t ProcessRecordHyperlinks(OH\_UdmfRecord\* record, unsigned int recordTypeIdCount, char\*\* typeIdsFromRecord)
{
    for (unsigned int k = 0; k < recordTypeIdCount; k++) {
        // Obtain the hyperlink data from OH\_UdmfRecord.
        if (strcmp(typeIdsFromRecord\[k\], UDMF\_META\_HYPERLINK) == 0) {
            // Create a UDS to hold the hyperlink data read from the unified record.
            OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
            int32\_t ret = OH\_UdmfRecord\_GetHyperlink(record, hyperlink);
            if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "Fail get hyperlink from record!");
                OH\_UdsHyperlink\_Destroy(hyperlink);
                return ret;
            }
            // Read information in OH\_UdsHyperlink.
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink type id is : %{public}s", OH\_UdsHyperlink\_GetType(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink url is : %{public}s", OH\_UdsHyperlink\_GetUrl(hyperlink));
            OH\_LOG\_INFO(LOG\_APP, "The hyperlink description is : %{public}s",
                OH\_UdsHyperlink\_GetDescription(hyperlink));
            OH\_UdsHyperlink\_Destroy(hyperlink);
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessDataElement(OH\_UdmfData\* data)
{
    unsigned int recordsCount = 0;
    OH\_UdmfRecord\*\* records = OH\_UdmfData\_GetRecords(data, &recordsCount);
    OH\_LOG\_INFO(LOG\_APP, "the count of records count is %{public}u", recordsCount);
    // 5. Obtain elements in data records.
    for (unsigned int j = 0; j < recordsCount; j++) {
        // Obtain the OH\_UdmfRecord type list.
        unsigned int recordTypeIdCount = 0;
        char\*\* typeIdsFromRecord = OH\_UdmfRecord\_GetTypes(records\[j\], &recordTypeIdCount);
        int32\_t ret = ProcessRecordHyperlinks(records\[j\], recordTypeIdCount, typeIdsFromRecord);
        if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "ProcessRecordHyperlinks error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t ProcessHyperlinkDataFromArray(OH\_UdmfData\* readData, unsigned int dataSize, OH\_UdmfData\*\* dataArray)
{
    for (unsigned int i = 0; i < dataSize - 1; i++) {
        OH\_UdmfData\* data = OH\_UDMF\_GetDataElementAt(dataArray, i);
        // 3. Check whether OH\_UdmfData has the required data type.
        if (!OH\_UdmfData\_HasType(data, UDMF\_META\_HYPERLINK)) {
            OH\_LOG\_INFO(LOG\_APP, "There is no hyperlink type in data\[%{public}u\].", i);
            continue;
        }
        // 4. Obtain data records and hyperlink data.
        int32\_t ret = ProcessDataElement(data);
        if (ret != UDMF\_E\_OK) {
            OH\_LOG\_ERROR(LOG\_APP, "processDataElement data error!");
            return ret;
        }
    }
    return UDMF\_E\_OK;
}

int32\_t DeleteDataTest()
{
    // 1. Construct an OH\_UdmfOptions.
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    int32\_t ret = OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    // 2. Delete data through OH\_UdmfOptions.
    unsigned int dataSize = 0;
    OH\_UdmfData\* readData = nullptr;
    ret = OH\_Udmf\_DeleteUnifiedData(options, &readData, &dataSize);
    if (ret != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Delete Data error!");
        OH\_UdmfOptions\_Destroy(options);
        return ret;
    }
    OH\_UdmfOptions\_Destroy(options);
    if (dataSize == 0) {
        OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
        return UDMF\_E\_OK;
    }
    OH\_LOG\_INFO(LOG\_APP, "the size of data is %{public}u", dataSize);
    OH\_UdmfData\*\* dataArray = &readData;
    ret = ProcessHyperlinkDataFromArray(readData, dataSize, dataArray);
    if (ret != UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Process hyperlink data error!");
        return ret;
    }
    // 6. Destroy all the pointers created.
    OH\_Udmf\_DestroyDataArray(dataArray, dataSize);
    return UDMF\_E\_OK;
}

#### Writing UDS Data in Delayed Mode Using UDMF

## Defining a Function for Providing UDS Data

The following uses hyperlink data as an example to describe how to define a callback function that provides UDS data.

1.  Define a data providing function for **OH\_UdmfRecordProvider**.
2.  Create a UDS of the hyperlink type in the data providing function.
3.  Set the URL and description for the hyperlink.
4.  Define a callback to be invoked when **OH\_UdmfRecordProvider** is destroyed.

// For better code readability, the operation result verification of each step is omitted in the following code. In actual development, you need to check whether each call is successful.
// 1. Define a callback to be invoked to return the UDS data obtained.
static void\* GetDataCallback(void\* context, const char\* type)
{
    if (strcmp(type, UDMF\_META\_HYPERLINK) == 0) {
        // 2. Create a UDS for hyperlink data.
        OH\_UdsHyperlink\* hyperlink = OH\_UdsHyperlink\_Create();
        // 3. Set the URL and description for the hyperlink.
        OH\_UdsHyperlink\_SetUrl(hyperlink, "www.demo.com");
        OH\_UdsHyperlink\_SetDescription(hyperlink, "This is the description.");
        return hyperlink;
    }
    return nullptr;
}
// 4. Define a callback to be invoked when OH\_UdmfRecordProvider is destroyed.
static void ProviderFinalizeCallback(void\* context) { OH\_LOG\_INFO(LOG\_APP, "OH\_UdmfRecordProvider finalize."); }

## Writing UDS Data in Delayed Mode

The following uses hyperlink data as an example to describe how to use OH\_UdmfRecordProvider and UDMF to write data in delayed mode. The hyperlink data is not written to the database until the **GetDataCallback** function is triggered when the data consumer obtains **OH\_UdsHyperlink** from **OH\_UdmfRecord**.

1.  Create an **OH\_UdmfRecordProvider** instance and set a data providing function for it and a callback to be invoked when this instance is destroyed.
2.  Create an **OH\_UdmfRecord** object and configure **OH\_UdmfRecordProvider** in it.
3.  Create an **OH\_UdmfData** object and add **OH\_UdmfRecord** to it.
4.  Construct and write data to the database. The key of the data is returned.
5.  Destroy all the pointers created.

int32\_t ProviderSetDataTest()
{
    // For better code readability, the operation result verification of each step is omitted in the following code. In actual development, you need to check whether each call is successful.
    // 1. Create an OH\_UdmfRecordProvider instance and set a data providing function for it and a callback to be invoked when this instance is destroyed.
    OH\_UdmfRecordProvider\* provider = OH\_UdmfRecordProvider\_Create();
    OH\_UdmfRecordProvider\_SetData(provider, (void\*)provider, GetDataCallback, ProviderFinalizeCallback);

    // 2. Create an OH\_UdmfRecord object and configure OH\_UdmfRecordProvider in it.
    OH\_UdmfRecord\* record = OH\_UdmfRecord\_Create();
    const char\* types\[1\] = {UDMF\_META\_HYPERLINK};
    OH\_UdmfRecord\_SetProvider(record, types, 1, provider);

    // 3. Create an OH\_UdmfData object and add OH\_UdmfRecord to it.
    OH\_UdmfData\* data = OH\_UdmfData\_Create();
    OH\_UdmfData\_AddRecord(data, record);

    // 4. Construct and write data to the database. The key of the data is returned.
    OH\_UdmfOptions\* options = OH\_UdmfOptions\_Create();
    if (OH\_UdmfOptions\_SetIntention(options, Udmf\_Intention::UDMF\_INTENTION\_DATA\_HUB) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set option error!");
        OH\_UdmfOptions\_Destroy(options);
        return UDMF\_ERR;
    }
    char key\[UDMF\_KEY\_BUFFER\_LEN\] = {0};
    if (OH\_Udmf\_SetUnifiedDataByOptions(options, data, key, sizeof(key)) != Udmf\_ErrCode::UDMF\_E\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Set data error!");
    }
    OH\_LOG\_INFO(LOG\_APP, "key = %{public}s", key);

    // 5. Destroy all the pointers created.
    OH\_UdmfRecord\_Destroy(record);
    OH\_UdmfData\_Destroy(data);
    OH\_UdmfOptions\_Destroy(options);
    return UDMF\_E\_OK;
}
