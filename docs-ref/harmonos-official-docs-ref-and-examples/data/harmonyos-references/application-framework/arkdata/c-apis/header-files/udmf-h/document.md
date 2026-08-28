# udmf.h

#### Overview

Defines the APIs, data structs, and enums for accessing the UDMF.

**File to include**: <database/udmf/udmf.h>

**Library**: libudmf.so

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Since**: 12

**Related module**: [UDMF](../../modules/udmf/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md) | OH\_UdmfData | Defines a struct for a unified data object. |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) | OH\_UdmfRecord | Defines a struct for a data record in a unified data object. |
| [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) | OH\_UdmfRecordProvider | Defines a struct for the data record provider in a unified data object. |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) | OH\_UdmfProperty | Defines a struct for a data record property in a uniform data object. |
| [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) | OH\_Udmf\_ProgressInfo | Defines a struct for progress information. |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) | OH\_UdmfGetDataParams | Defines a struct for parameters used to obtain UDMF data asynchronously. |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) | OH\_UdmfOptions | Defines the optional parameters for data operations. |
| [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) | OH\_UdmfDataLoadParams | Defines a struct for data loading parameters. |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) | OH\_UdmfDataLoadInfo | Defines a struct for the data loading information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Udmf\_Intention](#udmf_intention) | Udmf\_Intention | Enumerates the UDMF data channel types. |
| [Udmf\_ShareOption](#udmf_shareoption) | Udmf\_ShareOption | Enumerates the options for using the unified data in a device. |
| [Udmf\_FileConflictOptions](#udmf_fileconflictoptions) | Udmf\_FileConflictOptions | Enumerates the options used to resolve file copy conflicts. |
| [Udmf\_ProgressIndicator](#udmf_progressindicator) | Udmf\_ProgressIndicator | Enumerates the progress indicator options. You can use the default progress indicator as required. |
| [Udmf\_Visibility](#udmf_visibility) | Udmf\_Visibility | Enumerates data visibility level. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [UDMF\_KEY\_BUFFER\_LEN (512)](#udmf_key_buffer_len) | \- | Defines minimum length of the buffer that holds the key (unique identifier) of a unified data object. |
| [typedef void (\*OH\_Udmf\_DataProgressListener)(OH\_Udmf\_ProgressInfo\* progressInfo, OH\_UdmfData\* data)](#oh_udmf_dataprogresslistener) | OH\_Udmf\_DataProgressListener | 
Defines the callback used to return the data retrieval progress information and data obtained.

A null pointer is returned if the progress is less than 100%. The data obtained is returned only when the progress reaches 100%.

 |
| [OH\_UdmfData\* OH\_UdmfData\_Create()](#oh_udmfdata_create) | \- | Creates an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfData\_Destroy](#oh_udmfdata_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis)](#oh_udmfdata_destroy) | \- | Destroys an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record)](#oh_udmfdata_addrecord) | \- | Adds an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) to an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [bool OH\_UdmfData\_HasType(OH\_UdmfData\* pThis, const char\* type)](#oh_udmfdata_hastype) | \- | Checks whether the specified type exists in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [char\*\* OH\_UdmfData\_GetTypes(OH\_UdmfData\* pThis, unsigned int\* count)](#oh_udmfdata_gettypes) | \- | Obtains all data types in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count)](#oh_udmfdata_getrecords) | \- | Obtains all records contained in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [typedef void (\*UdmfData\_Finalize)(void\* context)](#udmfdata_finalize) | UdmfData\_Finalize | Defines a callback function used to release the context. This callback is invoked when the **OH\_UdmfRecordProvider** instance is destroyed. |
| [OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create()](#oh_udmfrecordprovider_create) | \- | Creates an [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfRecordProvider\_Destroy](#oh_udmfrecordprovider_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [int OH\_UdmfRecordProvider\_Destroy(OH\_UdmfRecordProvider\* provider)](#oh_udmfrecordprovider_destroy) | \- | Destroys an [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance. |
| [typedef void\* (\*OH\_UdmfRecordProvider\_GetData)(void\* context, const char\* type)](#oh_udmfrecordprovider_getdata) | OH\_UdmfRecordProvider\_GetData | Defines a callback function used to obtain data by type. This callback will be invoked to return the data obtained from **OH\_UdmfRecord**. |
| [int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize)](#oh_udmfrecordprovider_setdata) | \- | Sets a callback for an **OH\_UdmfRecordProvider** instance to provide data. |
| [OH\_UdmfRecord\* OH\_UdmfRecord\_Create()](#oh_udmfrecord_create) | \- | Creates an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfRecord\_Destroy](#oh_udmfrecord_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdmfRecord\_Destroy(OH\_UdmfRecord\* pThis)](#oh_udmfrecord_destroy) | \- | Destroys an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddGeneralEntry(OH\_UdmfRecord\* pThis, const char\* typeId, unsigned char\* entry, unsigned int count)](#oh_udmfrecord_addgeneralentry) | \- | Adds customized general data to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. This API cannot be used to add data of UDS types (such as PlainText, Link, and Pixelmap). |
| [int OH\_UdmfRecord\_AddPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText)](#oh_udmfrecord_addplaintext) | \- | Adds data of the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink)](#oh_udmfrecord_addhyperlink) | \- | Adds data of the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddHtml(OH\_UdmfRecord\* pThis, OH\_UdsHtml\* html)](#oh_udmfrecord_addhtml) | \- | Adds data of the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddAppItem(OH\_UdmfRecord\* pThis, OH\_UdsAppItem\* appItem)](#oh_udmfrecord_addappitem) | \- | Adds data of the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri)](#oh_udmfrecord_addfileuri) | \- | Adds data of the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddPixelMap(OH\_UdmfRecord\* pThis, OH\_UdsPixelMap\* pixelMap)](#oh_udmfrecord_addpixelmap) | \- | Adds data of the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddArrayBuffer(OH\_UdmfRecord\* record, const char\* type, OH\_UdsArrayBuffer\* buffer)](#oh_udmfrecord_addarraybuffer) | \- | Adds data of the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_AddContentForm(OH\_UdmfRecord\* pThis, OH\_UdsContentForm\* contentForm)](#oh_udmfrecord_addcontentform) | \- | Adds data of the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [char\*\* OH\_UdmfRecord\_GetTypes(OH\_UdmfRecord\* pThis, unsigned int\* count)](#oh_udmfrecord_gettypes) | \- | Obtains all data types in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetGeneralEntry(OH\_UdmfRecord\* pThis, const char\* typeId, unsigned char\*\* entry, unsigned int\* count)](#oh_udmfrecord_getgeneralentry) | \- | Obtains the data of the specified type in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText)](#oh_udmfrecord_getplaintext) | \- | Obtains [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink)](#oh_udmfrecord_gethyperlink) | \- | Obtains [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetHtml(OH\_UdmfRecord\* pThis, OH\_UdsHtml\* html)](#oh_udmfrecord_gethtml) | \- | Obtains [OH\_UdsHtml](../../structs/oh-udshtml/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetAppItem(OH\_UdmfRecord\* pThis, OH\_UdsAppItem\* appItem)](#oh_udmfrecord_getappitem) | \- | Obtains [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider)](#oh_udmfrecord_setprovider) | \- | Sets the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri)](#oh_udmfrecord_getfileuri) | \- | Obtains [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetPixelMap(OH\_UdmfRecord\* pThis, OH\_UdsPixelMap\* pixelMap)](#oh_udmfrecord_getpixelmap) | \- | Obtains [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetArrayBuffer(OH\_UdmfRecord\* record, const char\* type, OH\_UdsArrayBuffer\* buffer)](#oh_udmfrecord_getarraybuffer) | \- | Obtains [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfRecord\_GetContentForm(OH\_UdmfRecord\* pThis, OH\_UdsContentForm\* contentForm)](#oh_udmfrecord_getcontentform) | \- | Obtains [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [int OH\_UdmfData\_GetPrimaryPlainText(OH\_UdmfData\* data, OH\_UdsPlainText\* plainText)](#oh_udmfdata_getprimaryplaintext) | \- | Obtains the first [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) data from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [int OH\_UdmfData\_GetPrimaryHtml(OH\_UdmfData\* data, OH\_UdsHtml\* html)](#oh_udmfdata_getprimaryhtml) | \- | Obtains the first [OH\_UdsHtml](../../structs/oh-udshtml/document.md) data from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [int OH\_UdmfData\_GetRecordCount(OH\_UdmfData\* data)](#oh_udmfdata_getrecordcount) | \- | Obtains the number of data records contained in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [OH\_UdmfRecord\* OH\_UdmfData\_GetRecord(OH\_UdmfData\* data, unsigned int index)](#oh_udmfdata_getrecord) | \- | Obtains the specified data record from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [bool OH\_UdmfData\_IsLocal(OH\_UdmfData\* data)](#oh_udmfdata_islocal) | \- | Checks whether an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance is from the local device. |
| [OH\_UdmfProperty\* OH\_UdmfProperty\_Create(OH\_UdmfData\* unifiedData)](#oh_udmfproperty_create) | \- | Creates an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfProperty\_Destroy](#oh_udmfproperty_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdmfProperty\_Destroy(OH\_UdmfProperty\* pThis)](#oh_udmfproperty_destroy) | \- | Destroys an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [const char\* OH\_UdmfProperty\_GetTag(OH\_UdmfProperty\* pThis)](#oh_udmfproperty_gettag) | \- | Obtains the custom tag value from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int64\_t OH\_UdmfProperty\_GetTimestamp(OH\_UdmfProperty\* pThis)](#oh_udmfproperty_gettimestamp) | \- | Obtains the timestamp from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [Udmf\_ShareOption OH\_UdmfProperty\_GetShareOption(OH\_UdmfProperty\* pThis)](#oh_udmfproperty_getshareoption) | \- | Obtains the share option from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int OH\_UdmfProperty\_GetExtrasIntParam(OH\_UdmfProperty\* pThis, const char\* key, int defaultValue)](#oh_udmfproperty_getextrasintparam) | \- | Obtains the customized extra integer parameter from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [const char\* OH\_UdmfProperty\_GetExtrasStringParam(OH\_UdmfProperty\* pThis, const char\* key)](#oh_udmfproperty_getextrasstringparam) | \- | Obtains the customized extra string parameter from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int OH\_UdmfProperty\_SetTag(OH\_UdmfProperty\* pThis, const char\* tag)](#oh_udmfproperty_settag) | \- | Sets the tag value for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int OH\_UdmfProperty\_SetShareOption(OH\_UdmfProperty\* pThis, Udmf\_ShareOption option)](#oh_udmfproperty_setshareoption) | \- | Sets the [Udmf\_ShareOption](#udmf_shareoption) for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int OH\_UdmfProperty\_SetExtrasIntParam(OH\_UdmfProperty\* pThis, const char\* key, int param)](#oh_udmfproperty_setextrasintparam) | \- | Sets the extra integer parameter for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [int OH\_UdmfProperty\_SetExtrasStringParam(OH\_UdmfProperty\* pThis, const char\* key, const char\* param)](#oh_udmfproperty_setextrasstringparam) | \- | Sets the extra string parameter for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [OH\_UdmfOptions\* OH\_UdmfOptions\_Create()](#oh_udmfoptions_create) | \- | Creates an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. If this pointer is no longer required, use [OH\_UdmfOptions\_Destroy](#oh_udmfoptions_destroy) to destroy it. Otherwise, memory leaks may occur. |
| [void OH\_UdmfOptions\_Destroy(OH\_UdmfOptions\* pThis)](#oh_udmfoptions_destroy) | \- | Destroys an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [const char\* OH\_UdmfOptions\_GetKey(OH\_UdmfOptions\* pThis)](#oh_udmfoptions_getkey) | \- | Obtains the key (unique identifier) from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [int OH\_UdmfOptions\_SetKey(OH\_UdmfOptions\* pThis, const char\* key)](#oh_udmfoptions_setkey) | \- | Sets the key (unique identifier) in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [Udmf\_Intention OH\_UdmfOptions\_GetIntention(OH\_UdmfOptions\* pThis)](#oh_udmfoptions_getintention) | \- | Obtains the data channel information from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [int OH\_UdmfOptions\_SetIntention(OH\_UdmfOptions\* pThis, Udmf\_Intention intention)](#oh_udmfoptions_setintention) | \- | Sets the data channel content parameter in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [int OH\_UdmfOptions\_Reset(OH\_UdmfOptions\* pThis)](#oh_udmfoptions_reset) | \- | Resets an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance to empty. |
| [int OH\_Udmf\_GetUnifiedData(const char\* key, Udmf\_Intention intention, OH\_UdmfData\* unifiedData)](#oh_udmf_getunifieddata) | \- | Obtains an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database. |
| [int OH\_Udmf\_GetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize)](#oh_udmf_getunifieddatabyoptions) | \- | Obtains an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database by data channel type. |
| [int OH\_Udmf\_SetUnifiedData(Udmf\_Intention intention, OH\_UdmfData\* unifiedData, char\* key, unsigned int keyLen)](#oh_udmf_setunifieddata) | \- | Sets an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database. |
| [int OH\_Udmf\_SetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData \*unifiedData, char \*key, unsigned int keyLen)](#oh_udmf_setunifieddatabyoptions) | \- | Sets an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database. |
| [int OH\_Udmf\_UpdateUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\* unifiedData)](#oh_udmf_updateunifieddata) | \- | Updates an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database. |
| [int OH\_Udmf\_DeleteUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize)](#oh_udmf_deleteunifieddata) | \- | Deletes an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database. |
| [void OH\_Udmf\_DestroyDataArray(OH\_UdmfData\*\* dataArray, unsigned int dataSize)](#oh_udmf_destroydataarray) | \- | Destroys the memory of the data array. |
| [int OH\_UdmfProgressInfo\_GetProgress(OH\_Udmf\_ProgressInfo\* progressInfo)](#oh_udmfprogressinfo_getprogress) | \- | Obtains the progress (in percentage) from an [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance. |
| [int OH\_UdmfProgressInfo\_GetStatus(OH\_Udmf\_ProgressInfo\* progressInfo)](#oh_udmfprogressinfo_getstatus) | \- | Obtains the status information from an [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance. |
| [OH\_UdmfGetDataParams\* OH\_UdmfGetDataParams\_Create()](#oh_udmfgetdataparams_create) | \- | 

Creates an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_UdmfGetDataParams\_Destroy](#oh_udmfgetdataparams_destroy) to destroy it. Otherwise, memory leaks may occur.

 |
| [void OH\_UdmfGetDataParams\_Destroy(OH\_UdmfGetDataParams\* pThis)](#oh_udmfgetdataparams_destroy) | \- | Destroys an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| [void OH\_UdmfGetDataParams\_SetDestUri(OH\_UdmfGetDataParams\* params, const char\* destUri)](#oh_udmfgetdataparams_setdesturi) | \- | 

Sets the destination directory in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

If the destination directory is set, data of the file type will be copied to the specified directory. The file type data obtained in the callback will be replaced with the URI of the destination directory.

If the destination directory is not specified, the file will not be copied. The file type data obtained in the callback is the URI of the source directory.

If the application involves complex file processing or files need to be copied to multiple directories, you are advised to leave this parameter unspecified and let the application handle the file copy.

 |
| [void OH\_UdmfGetDataParams\_SetFileConflictOptions(OH\_UdmfGetDataParams\* params, const Udmf\_FileConflictOptions options)](#oh_udmfgetdataparams_setfileconflictoptions) | \- | Sets the policy for resolving file conflicts in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| [void OH\_UdmfGetDataParams\_SetProgressIndicator(OH\_UdmfGetDataParams\* params, const Udmf\_ProgressIndicator progressIndicator)](#oh_udmfgetdataparams_setprogressindicator) | \- | Sets the progress indicator in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| [void OH\_UdmfGetDataParams\_SetDataProgressListener(OH\_UdmfGetDataParams\* params, const OH\_Udmf\_DataProgressListener dataProgressListener)](#oh_udmfgetdataparams_setdataprogresslistener) | \- | Sets the callback used to return the progress obtained in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| [Udmf\_Visibility OH\_UdmfOptions\_GetVisibility(OH\_UdmfOptions\* pThis)](#oh_udmfoptions_getvisibility) | \- | Obtains the data visibility level from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [int OH\_UdmfOptions\_SetVisibility(OH\_UdmfOptions\* pThis, Udmf\_Visibility visibility)](#oh_udmfoptions_setvisibility) | \- | Sets the data visibility level in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [typedef OH\_UdmfData\* (\*OH\_Udmf\_DataLoadHandler)(OH\_UdmfDataLoadInfo\* acceptableInfo)](#oh_udmf_dataloadhandler) | OH\_Udmf\_DataLoadHandler | Defines the callback used to load data. |
| [OH\_UdmfDataLoadParams\* OH\_UdmfDataLoadParams\_Create()](#oh_udmfdataloadparams_create) | \- | Creates an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance and a pointer to it. |
| [void OH\_UdmfDataLoadParams\_Destroy(OH\_UdmfDataLoadParams\* pThis)](#oh_udmfdataloadparams_destroy) | \- | Destroys an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |
| [void OH\_UdmfDataLoadParams\_SetLoadHandler(OH\_UdmfDataLoadParams\* params, const OH\_Udmf\_DataLoadHandler dataLoadHandler)](#oh_udmfdataloadparams_setloadhandler) | \- | Sets the processing function for data loading in an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |
| [void OH\_UdmfDataLoadParams\_SetDataLoadInfo(OH\_UdmfDataLoadParams\* params, OH\_UdmfDataLoadInfo\* dataLoadInfo)](#oh_udmfdataloadparams_setdataloadinfo) | \- | Sets data loading information in an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |
| [OH\_UdmfDataLoadInfo\* OH\_UdmfDataLoadInfo\_Create()](#oh_udmfdataloadinfo_create) | \- | Creates an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [void OH\_UdmfDataLoadInfo\_Destroy(OH\_UdmfDataLoadInfo\* dataLoadInfo)](#oh_udmfdataloadinfo_destroy) | \- | Destroys an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [char\*\* OH\_UdmfDataLoadInfo\_GetTypes(OH\_UdmfDataLoadInfo\* dataLoadInfo, unsigned int\* count)](#oh_udmfdataloadinfo_gettypes) | \- | Obtains the data types from an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [void OH\_UdmfDataLoadInfo\_SetType(OH\_UdmfDataLoadInfo\* dataLoadInfo, const char\* type)](#oh_udmfdataloadinfo_settype) | \- | Sets the data type in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [int OH\_UdmfDataLoadInfo\_GetRecordCount(OH\_UdmfDataLoadInfo\* dataLoadInfo)](#oh_udmfdataloadinfo_getrecordcount) | \- | Obtains the number of records in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [void OH\_UdmfDataLoadInfo\_SetRecordCount(OH\_UdmfDataLoadInfo\* dataLoadInfo, unsigned int recordCount)](#oh_udmfdataloadinfo_setrecordcount) | \- | Sets the number of records in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| [OH\_UdmfData\* OH\_UDMF\_GetDataElementAt(OH\_UdmfData\*\* dataArray, unsigned int index)](#oh_udmf_getdataelementat) | \- | Obtains the unified data object with the specified index from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) array. |

#### Enum Description

#### \[h2\]Udmf\_Intention

enum Udmf\_Intention

**Description**

Enumerates the UDMF data channel types.

**Since**: 12

| Name | Description |
| :-- | :-- |
| UDMF\_INTENTION\_DRAG | Channel for dragging data. |
| UDMF\_INTENTION\_PASTEBOARD | Channel for pasteboard data. |
| UDMF\_INTENTION\_DATA\_HUB | 
Public data channel.

**Since**: 20

 |
| UDMF\_INTENTION\_SYSTEM\_SHARE | 

Channel for sharing data by the system.

**Since**: 20

 |
| UDMF\_INTENTION\_PICKER | 

Channel for picker data.

**Since**: 20

 |
| UDMF\_INTENTION\_MENU | 

Channel for menu data.

**Since**: 20

 |

#### \[h2\]Udmf\_ShareOption

enum Udmf\_ShareOption

**Description**

Enumerates the options for using the unified data in a device.

**Since**: 12

| Name | Description |
| :-- | :-- |
| SHARE\_OPTIONS\_INVALID | Invalid use. |
| SHARE\_OPTIONS\_IN\_APP | **UnifiedData** can be used only in the same application of a device. |
| SHARE\_OPTIONS\_CROSS\_APP | **UnifiedData** can be used across applications of a device. |

#### \[h2\]Udmf\_FileConflictOptions

enum Udmf\_FileConflictOptions

**Description**

Enumerates the options used to resolve file copy conflicts.

**Since**: 15

| Name | Description |
| :-- | :-- |
| UDMF\_OVERWRITE = 0 | Overwrites the file with the same name in the destination directory. This is the default value. |
| UDMF\_SKIP = 1 | Skips the file if there is a file with the same name in the destination directory. |

#### \[h2\]Udmf\_ProgressIndicator

enum Udmf\_ProgressIndicator

**Description**

Enumerates the progress indicator options. You can use the default progress indicator as required.

**Since**: 15

| Name | Description |
| :-- | :-- |
| UDMF\_NONE = 0 | The default progress indicator is not used. |
| UDMF\_DEFAULT = 1 | The default progress indicator is used. If data is obtained within 500 ms, the default progress bar is not started. |

#### \[h2\]Udmf\_Visibility

enum Udmf\_Visibility

**Description**

Enumerates data visibility level.

**Since**: 20

| Name | Description |
| :-- | :-- |
| UDMF\_ALL | Visible to all applications. |
| UDMF\_OWN\_PROCESS | Visible only to the data provider. |

#### Function Description

#### \[h2\]OH\_UdmfGetDataParams\_SetAcceptableInfo()

void OH\_UdmfGetDataParams\_SetAcceptableInfo(OH\_UdmfGetDataParams\* params, OH\_UdmfDataLoadInfo\* acceptableInfo)

**Description**

Sets the acceptable data description in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* params | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* acceptableInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |

#### \[h2\]OH\_UdmfDataLoadParams\_Create()

OH\_UdmfDataLoadParams\* OH\_UdmfDataLoadParams\_Create()

**Description**

Creates an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance and a pointer to it.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md)\* | Returns a pointer to the [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfDataLoadParams\_Destroy()

void OH\_UdmfDataLoadParams\_Destroy(OH\_UdmfDataLoadParams\* pThis)

**Description**

Destroys an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md)\* pThis | Pointer to the [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |

#### \[h2\]OH\_UdmfDataLoadParams\_SetLoadHandler()

void OH\_UdmfDataLoadParams\_SetLoadHandler(OH\_UdmfDataLoadParams\* params, const OH\_Udmf\_DataLoadHandler dataLoadHandler)

**Description**

Sets the processing function for data loading in an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md)\* params | Pointer to the [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |
| [const OH\_Udmf\_DataLoadHandler](#oh_udmf_dataloadhandler) dataLoadHandler | User-defined processing function for data loading. |

#### \[h2\]OH\_UdmfDataLoadParams\_SetDataLoadInfo()

void OH\_UdmfDataLoadParams\_SetDataLoadInfo(OH\_UdmfDataLoadParams\* params, OH\_UdmfDataLoadInfo\* dataLoadInfo)

**Description**

Sets data loading information in an [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md)\* params | Pointer to the [OH\_UdmfDataLoadParams](../../structs/oh-udmfdataloadparams/document.md) instance. |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |

#### \[h2\]OH\_UdmfDataLoadInfo\_Create()

OH\_UdmfDataLoadInfo\* OH\_UdmfDataLoadInfo\_Create()

**Description**

Creates an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* | Returns a pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfDataLoadInfo\_Destroy()

void OH\_UdmfDataLoadInfo\_Destroy(OH\_UdmfDataLoadInfo\* dataLoadInfo)

**Description**

Destroys an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |

#### \[h2\]OH\_UdmfDataLoadInfo\_GetTypes()

char\*\* OH\_UdmfDataLoadInfo\_GetTypes(OH\_UdmfDataLoadInfo\* dataLoadInfo, unsigned int\* count)

**Description**

Obtains the data types from an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| unsigned int\* count | Number of data types returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | String array of the returned data types. |

#### \[h2\]OH\_UdmfDataLoadInfo\_SetType()

void OH\_UdmfDataLoadInfo\_SetType(OH\_UdmfDataLoadInfo\* dataLoadInfo, const char\* type)

**Description**

Sets the data type in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| const char\* type | A sting indicating the data type. |

#### \[h2\]OH\_UdmfDataLoadInfo\_GetRecordCount()

int OH\_UdmfDataLoadInfo\_GetRecordCount(OH\_UdmfDataLoadInfo\* dataLoadInfo)

**Description**

Obtains the number of records in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of records. |

#### \[h2\]OH\_UdmfDataLoadInfo\_SetRecordCount()

void OH\_UdmfDataLoadInfo\_SetRecordCount(OH\_UdmfDataLoadInfo\* dataLoadInfo, unsigned int recordCount)

**Description**

Sets the number of records in an [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* dataLoadInfo | Pointer to the [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md) instance. |
| unsigned int recordCount | Number of records. |

#### \[h2\]OH\_Udmf\_DataLoadHandler()

typedef OH\_UdmfData\* (\*OH\_Udmf\_DataLoadHandler)(OH\_UdmfDataLoadInfo\* acceptableInfo)

**Description**

Defines the callback used to load data.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfDataLoadInfo](../../structs/oh-udmfdataloadinfo/document.md)\* acceptableInfo | Data type and data size that can be received. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* (\*OH\_Udmf\_DataLoadHandler) | Data to be loaded. |

#### \[h2\]OH\_UdmfOptions\_GetVisibility()

Udmf\_Visibility OH\_UdmfOptions\_GetVisibility(OH\_UdmfOptions\* pThis)

**Description**

Obtains the data visibility level from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Udmf\_Visibility](#udmf_visibility) | Value of the [Udmf\_Visibility](#udmf_visibility) instance obtained. |

#### \[h2\]OH\_UdmfOptions\_SetVisibility()

int OH\_UdmfOptions\_SetVisibility(OH\_UdmfOptions\* pThis, Udmf\_Visibility visibility)

**Description**

Sets the data visibility level in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [Udmf\_Visibility](#udmf_visibility) visibility | Data visibility level [Udmf\_Visibility](#udmf_visibility). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Execution result. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]UDMF\_KEY\_BUFFER\_LEN()

UDMF\_KEY\_BUFFER\_LEN (512)

**Description**

Defines minimum length of the buffer that holds the key (unique identifier) of a unified data object.

**Since**: 12

#### \[h2\]OH\_Udmf\_DataProgressListener()

typedef void (\*OH\_Udmf\_DataProgressListener)(OH\_Udmf\_ProgressInfo\* progressInfo, OH\_UdmfData\* data)

**Description**

Defines the callback used to return the data retrieval progress information and data obtained.

A null pointer is returned if the progress is less than 100%. The data obtained is returned only when the progress reaches 100%.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md)\* progressInfo | Progress information obtained. |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Data obtained. |

#### \[h2\]OH\_UdmfData\_Create()

OH\_UdmfData\* OH\_UdmfData\_Create()

**Description**

Creates an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfData\_Destroy](#oh_udmfdata_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* | Returns a pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

**See**

OH\_UdmfData

#### \[h2\]OH\_UdmfData\_Destroy()

void OH\_UdmfData\_Destroy(OH\_UdmfData\* pThis)

**Description**

Destroys an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* pThis | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |

**See**

OH\_UdmfData

#### \[h2\]OH\_UdmfData\_AddRecord()

int OH\_UdmfData\_AddRecord(OH\_UdmfData\* pThis, OH\_UdmfRecord\* record)

**Description**

Adds an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) to an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* pThis | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* record | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfData\_HasType()

bool OH\_UdmfData\_HasType(OH\_UdmfData\* pThis, const char\* type)

**Description**

Checks whether the specified type exists in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* pThis | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| const char\* type | Pointer to the type to check. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result. The value **true** means the **OH\_UdmfData** instance contains the specified type; the value **false** means the opposite. |

#### \[h2\]OH\_UdmfData\_GetTypes()

char\*\* OH\_UdmfData\_GetTypes(OH\_UdmfData\* pThis, unsigned int\* count)

**Description**

Obtains all data types in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* pThis | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| unsigned int\* count | Pointer to the number of data types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | Returns the data types obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfData\_GetRecords()

OH\_UdmfRecord\*\* OH\_UdmfData\_GetRecords(OH\_UdmfData\* pThis, unsigned int\* count)

**Description**

Obtains all records contained in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* pThis | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| unsigned int\* count | Pointer to the number of records obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\*\* | Returns a pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]UdmfData\_Finalize()

typedef void (\*UdmfData\_Finalize)(void\* context)

**Description**

Defines a callback function used to release the context. This callback is invoked when the **OH\_UdmfRecordProvider** instance is destroyed.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* context | Pointer to the context to release. |

#### \[h2\]OH\_UdmfRecordProvider\_Create()

OH\_UdmfRecordProvider\* OH\_UdmfRecordProvider\_Create()

**Description**

Creates an [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfRecordProvider\_Destroy](#oh_udmfrecordprovider_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md)\* | Returns a pointer to the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfRecordProvider\_Destroy()

int OH\_UdmfRecordProvider\_Destroy(OH\_UdmfRecordProvider\* provider)

**Description**

Destroys an [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md)\* provider | Pointer to the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecordProvider\_GetData()

typedef void\* (\*OH\_UdmfRecordProvider\_GetData)(void\* context, const char\* type)

**Description**

Defines a callback function used to obtain data by type. This callback will be invoked to return the data obtained from **OH\_UdmfRecord**.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* context | Pointer to the context set by [OH\_UdmfRecordProvider\_SetData](#oh_udmfrecordprovider_setdata). |
| const char\* type | Pointer to the type of the data to obtain. For details, see [udmf\_meta.h](../udmf-meta-h/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Uniform data obtained. |

#### \[h2\]OH\_UdmfRecordProvider\_SetData()

int OH\_UdmfRecordProvider\_SetData(OH\_UdmfRecordProvider\* provider, void\* context, const OH\_UdmfRecordProvider\_GetData callback, const UdmfData\_Finalize finalize)

**Description**

Sets a callback for an **OH\_UdmfRecordProvider** instance to provide data.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md)\* provider | Pointer to the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance. |
| void\* context | Pointer to the context, which is passed as the first parameter to [OH\_UdmfRecordProvider\_GetData](#oh_udmfrecordprovider_getdata). |
| const [OH\_UdmfRecordProvider\_GetData](#oh_udmfrecordprovider_getdata) callback | Callback used to obtain data. For details, see [OH\_UdmfRecordProvider\_GetData](#oh_udmfrecordprovider_getdata). |
| const [UdmfData\_Finalize](#udmfdata_finalize) finalize | Optional callback used to release the context data when the **OH\_UdmfRecordProvider** instance is destroyed. For details, see [UdmfData\_Finalize](#udmfdata_finalize). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_Create()

OH\_UdmfRecord\* OH\_UdmfRecord\_Create()

**Description**

Creates an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfRecord\_Destroy](#oh_udmfrecord_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* | Returns a pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfRecord\_Destroy()

void OH\_UdmfRecord\_Destroy(OH\_UdmfRecord\* pThis)

**Description**

Destroys an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |

#### \[h2\]OH\_UdmfRecord\_AddGeneralEntry()

int OH\_UdmfRecord\_AddGeneralEntry(OH\_UdmfRecord\* pThis, const char\* typeId, unsigned char\* entry, unsigned int count)

**Description**

Adds customized general data to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. This API cannot be used to add data of UDS types (such as PlainText, Link, and Pixelmap).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* typeId | Pointer to the data type identifier, which is used to distinguish custom data types from system-defined types. It is recommended that the value start with 'ApplicationDefined'. |
| unsigned char\* entry | Pointer to the customized data to add. |
| unsigned int count | Size of customized data to add. The data size cannot exceed 4 KB. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddPlainText()

int OH\_UdmfRecord\_AddPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText)

**Description**

Adds data of the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* plainText | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddHyperlink()

int OH\_UdmfRecord\_AddHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink)

**Description**

Adds data of the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* hyperlink | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddHtml()

int OH\_UdmfRecord\_AddHtml(OH\_UdmfRecord\* pThis, OH\_UdsHtml\* html)

**Description**

Adds data of the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* html | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddAppItem()

int OH\_UdmfRecord\_AddAppItem(OH\_UdmfRecord\* pThis, OH\_UdsAppItem\* appItem)

**Description**

Adds data of the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* appItem | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddFileUri()

int OH\_UdmfRecord\_AddFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri)

**Description**

Adds data of the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* fileUri | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddPixelMap()

int OH\_UdmfRecord\_AddPixelMap(OH\_UdmfRecord\* pThis, OH\_UdsPixelMap\* pixelMap)

**Description**

Adds data of the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pixelMap | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddArrayBuffer()

int OH\_UdmfRecord\_AddArrayBuffer(OH\_UdmfRecord\* record, const char\* type, OH\_UdsArrayBuffer\* buffer)

**Description**

Adds data of the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* record | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* type | Pointer to the ArrayBuffer type ID, which must be unique. |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* buffer | Pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_AddContentForm()

int OH\_UdmfRecord\_AddContentForm(OH\_UdmfRecord\* pThis, OH\_UdsContentForm\* contentForm)

**Description**

Adds data of the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) type to an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* contentForm | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_GetTypes()

char\*\* OH\_UdmfRecord\_GetTypes(OH\_UdmfRecord\* pThis, unsigned int\* count)

**Description**

Obtains all data types in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| unsigned int\* count | Pointer to the number of data types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| char\*\* | Returns a list of data types obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfRecord\_GetGeneralEntry()

int OH\_UdmfRecord\_GetGeneralEntry(OH\_UdmfRecord\* pThis, const char\* typeId, unsigned char\*\* entry, unsigned int\* count)

**Description**

Obtains the data of the specified type in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* typeId | Pointer to the data type ID. |
| unsigned char\*\* entry | Double pointer to the data obtained. |
| unsigned int\* count | Pointer to the length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs.

 |

#### \[h2\]OH\_UdmfRecord\_GetPlainText()

int OH\_UdmfRecord\_GetPlainText(OH\_UdmfRecord\* pThis, OH\_UdsPlainText\* plainText)

**Description**

Obtains [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* plainText | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs.

 |

#### \[h2\]OH\_UdmfRecord\_GetHyperlink()

int OH\_UdmfRecord\_GetHyperlink(OH\_UdmfRecord\* pThis, OH\_UdsHyperlink\* hyperlink)

**Description**

Obtains [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md)\* hyperlink | Pointer to the [OH\_UdsHyperlink](../../structs/oh-udshyperlink/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs.

 |

#### \[h2\]OH\_UdmfRecord\_GetHtml()

int OH\_UdmfRecord\_GetHtml(OH\_UdmfRecord\* pThis, OH\_UdsHtml\* html)

**Description**

Obtains [OH\_UdsHtml](../../structs/oh-udshtml/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* html | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs.

 |

#### \[h2\]OH\_UdmfRecord\_GetAppItem()

int OH\_UdmfRecord\_GetAppItem(OH\_UdmfRecord\* pThis, OH\_UdsAppItem\* appItem)

**Description**

Obtains [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md)\* appItem | Pointer to the [OH\_UdsAppItem](../../structs/oh-udsappitem/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs.

 |

#### \[h2\]OH\_UdmfRecord\_SetProvider()

int OH\_UdmfRecord\_SetProvider(OH\_UdmfRecord\* pThis, const char\* const\* types, unsigned int count, OH\_UdmfRecordProvider\* provider)

**Description**

Sets the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* const\* types | Pointer to the data types to be provided. |
| unsigned int count | Number of the data types. |
| [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md)\* provider | Pointer to the [OH\_UdmfRecordProvider](../../structs/oh-udmfrecordprovider/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_GetFileUri()

int OH\_UdmfRecord\_GetFileUri(OH\_UdmfRecord\* pThis, OH\_UdsFileUri\* fileUri)

**Description**

Obtains [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md)\* fileUri | Pointer to the [OH\_UdsFileUri](../../structs/oh-udsfileuri/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_GetPixelMap()

int OH\_UdmfRecord\_GetPixelMap(OH\_UdmfRecord\* pThis, OH\_UdsPixelMap\* pixelMap)

**Description**

Obtains [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md)\* pixelMap | Pointer to the [OH\_UdsPixelMap](../../structs/oh-udspixelmap/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_GetArrayBuffer()

int OH\_UdmfRecord\_GetArrayBuffer(OH\_UdmfRecord\* record, const char\* type, OH\_UdsArrayBuffer\* buffer)

**Description**

Obtains [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* record | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* type | Pointer to the data type ID of the ArrayBuffer data to obtain. |
| [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md)\* buffer | Pointer to the [OH\_UdsArrayBuffer](../../structs/oh-udsarraybuffer/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfRecord\_GetContentForm()

int OH\_UdmfRecord\_GetContentForm(OH\_UdmfRecord\* pThis, OH\_UdsContentForm\* contentForm)

**Description**

Obtains [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) data from an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md)\* contentForm | Pointer to the [OH\_UdsContentForm](../../structs/oh-udscontentform/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfData\_GetPrimaryPlainText()

int OH\_UdmfData\_GetPrimaryPlainText(OH\_UdmfData\* data, OH\_UdsPlainText\* plainText)

**Description**

Obtains the first [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) data from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md)\* plainText | Pointer to the [OH\_UdsPlainText](../../structs/oh-udsplaintext/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfData\_GetPrimaryHtml()

int OH\_UdmfData\_GetPrimaryHtml(OH\_UdmfData\* data, OH\_UdsHtml\* html)

**Description**

Obtains the first [OH\_UdsHtml](../../structs/oh-udshtml/document.md) data from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| [OH\_UdsHtml](../../structs/oh-udshtml/document.md)\* html | Pointer to the [OH\_UdsHtml](../../structs/oh-udshtml/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfData\_GetRecordCount()

int OH\_UdmfData\_GetRecordCount(OH\_UdmfData\* data)

**Description**

Obtains the number of data records contained in an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of the data records in an [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance obtained. |

#### \[h2\]OH\_UdmfData\_GetRecord()

OH\_UdmfRecord\* OH\_UdmfData\_GetRecord(OH\_UdmfData\* data, unsigned int index)

**Description**

Obtains the specified data record from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| unsigned int index | Subscript of the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance to be obtained in [OH\_UdmfData](../../structs/oh-udmfdata/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md)\* | Returns a pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfData\_IsLocal()

bool OH\_UdmfData\_IsLocal(OH\_UdmfData\* data)

**Description**

Checks whether an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance is from the local device.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* data | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result. The value **true** means the data is from the local device; the value **false** means the opposite. |

#### \[h2\]OH\_UdmfProperty\_Create()

OH\_UdmfProperty\* OH\_UdmfProperty\_Create(OH\_UdmfData\* unifiedData)

**Description**

Creates an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance and a pointer to it. If this pointer is no longer required, use [OH\_UdmfProperty\_Destroy](#oh_udmfproperty_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* unifiedData | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* | Returns a pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfProperty\_Destroy()

void OH\_UdmfProperty\_Destroy(OH\_UdmfProperty\* pThis)

**Description**

Destroys an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |

#### \[h2\]OH\_UdmfProperty\_GetTag()

const char\* OH\_UdmfProperty\_GetTag(OH\_UdmfProperty\* pThis)

**Description**

Obtains the custom tag value from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the custom tag value obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfProperty\_GetTimestamp()

int64\_t OH\_UdmfProperty\_GetTimestamp(OH\_UdmfProperty\* pThis)

**Description**

Obtains the timestamp from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Timestamp obtained. |

#### \[h2\]OH\_UdmfProperty\_GetShareOption()

Udmf\_ShareOption OH\_UdmfProperty\_GetShareOption(OH\_UdmfProperty\* pThis)

**Description**

Obtains the share option from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Udmf\_ShareOption](#udmf_shareoption) | Share option in the [Udmf\_ShareOption](#udmf_shareoption) instance obtained. |

#### \[h2\]OH\_UdmfProperty\_GetExtrasIntParam()

int OH\_UdmfProperty\_GetExtrasIntParam(OH\_UdmfProperty\* pThis, const char\* key, int defaultValue)

**Description**

Obtains the customized extra integer parameter from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| const char\* key | Pointer to the key of the parameter to set. |
| int defaultValue | Default value to be returned if the parameter fails to be obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the integer value obtained if the operation is successful; returns **defaultValue** if the operation fails. |

#### \[h2\]OH\_UdmfProperty\_GetExtrasStringParam()

const char\* OH\_UdmfProperty\_GetExtrasStringParam(OH\_UdmfProperty\* pThis, const char\* key)

**Description**

Obtains the customized extra string parameter from an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| const char\* key | Pointer to the key of the parameter to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the string value obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfProperty\_SetTag()

int OH\_UdmfProperty\_SetTag(OH\_UdmfProperty\* pThis, const char\* tag)

**Description**

Sets the tag value for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| const char\* tag | Pointer to the tag value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfProperty\_SetShareOption()

int OH\_UdmfProperty\_SetShareOption(OH\_UdmfProperty\* pThis, Udmf\_ShareOption option)

**Description**

Sets the [Udmf\_ShareOption](#udmf_shareoption) for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance. |
| [Udmf\_ShareOption](#udmf_shareoption) option | Pointer to the [Udmf\_ShareOption](#udmf_shareoption) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfProperty\_SetExtrasIntParam()

int OH\_UdmfProperty\_SetExtrasIntParam(OH\_UdmfProperty\* pThis, const char\* key, int param)

**Description**

Sets the extra integer parameter for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* key | Pointer to the key of the parameter to set. |
| int param | Parameter value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfProperty\_SetExtrasStringParam()

int OH\_UdmfProperty\_SetExtrasStringParam(OH\_UdmfProperty\* pThis, const char\* key, const char\* param)

**Description**

Sets the extra string parameter for an [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfProperty](../../structs/oh-udmfproperty/document.md)\* pThis | Pointer to the [OH\_UdmfRecord](../../structs/oh-udmfrecord/document.md) instance. |
| const char\* key | Pointer to the key of the parameter to set. |
| const char\* param | Parameter value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfOptions\_Create()

OH\_UdmfOptions\* OH\_UdmfOptions\_Create()

**Description**

Creates an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. If this pointer is no longer required, use [OH\_UdmfOptions\_Destroy](#oh_udmfoptions_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* | Returns a pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfOptions\_Destroy()

void OH\_UdmfOptions\_Destroy(OH\_UdmfOptions\* pThis)

**Description**

Destroys an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |

#### \[h2\]OH\_UdmfOptions\_GetKey()

const char\* OH\_UdmfOptions\_GetKey(OH\_UdmfOptions\* pThis)

**Description**

Obtains the key (unique identifier) from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the unique identifier obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfOptions\_SetKey()

int OH\_UdmfOptions\_SetKey(OH\_UdmfOptions\* pThis, const char\* key)

**Description**

Sets the key (unique identifier) in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| const char\* key | Pointer to the value of the unique identifier of the data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfOptions\_GetIntention()

Udmf\_Intention OH\_UdmfOptions\_GetIntention(OH\_UdmfOptions\* pThis)

**Description**

Obtains the data channel information from an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Udmf\_Intention](#udmf_intention) | Returns the value of [Udmf\_Intent](#udmf_intention). |

#### \[h2\]OH\_UdmfOptions\_SetIntention()

int OH\_UdmfOptions\_SetIntention(OH\_UdmfOptions\* pThis, Udmf\_Intention intention)

**Description**

Sets the data channel content parameter in an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [Udmf\_Intention](#udmf_intention) intention | Data channel type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_UdmfOptions\_Reset()

int OH\_UdmfOptions\_Reset(OH\_UdmfOptions\* pThis)

**Description**

Resets an [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance to empty.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* pThis | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Udmf\_GetUnifiedData()

int OH\_Udmf\_GetUnifiedData(const char\* key, Udmf\_Intention intention, OH\_UdmfData\* unifiedData)

**Description**

Obtains an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* key | Pointer to the unique identifier of the data in the database. |
| [Udmf\_Intention](#udmf_intention) intention | Data channel type [Udmf\_Intent](#udmf_intention). |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* unifiedData | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_GetUnifiedDataByOptions()

int OH\_Udmf\_GetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize)

**Description**

Obtains an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database by data channel type.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* options | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\*\* dataArray | 
Double pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance.

You should use the [OH\_UDMF\_GetDataElementAt](#oh_udmf_getdataelementat) function to access each element by subscript.

This double pointer should be released by using the [OH\_Udmf\_DestroyDataArray](#oh_udmf_destroydataarray) function.

 |
| unsigned int\* dataSize | Pointer to the data size obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_SetUnifiedData()

int OH\_Udmf\_SetUnifiedData(Udmf\_Intention intention, OH\_UdmfData\* unifiedData, char\* key, unsigned int keyLen)

**Description**

Sets an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Udmf\_Intention](#udmf_intention) intention | Data channel type [Udmf\_Intent](#udmf_intention). |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* unifiedData | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| char\* key | Pointer to the key that uniquely identifies the data in the database. |
| unsigned int keyLen | Length of the key. The memory size must be greater than or equal to 512 bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_SetUnifiedDataByOptions()

int OH\_Udmf\_SetUnifiedDataByOptions(OH\_UdmfOptions\* options, OH\_UdmfData \*unifiedData, char \*key, unsigned int keyLen)

**Description**

Sets an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* options | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md) \*unifiedData | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| char \*key | Pointer to the key that uniquely identifies the data in the database. The memory size must be greater than [UDMF\_KEY\_BUFFER\_LEN](#udmf_key_buffer_len). |
| unsigned int keyLen | Length of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_UpdateUnifiedData()

int OH\_Udmf\_UpdateUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\* unifiedData)

**Description**

Updates an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance in the UDMF database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* options | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\* unifiedData | Pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_DeleteUnifiedData()

int OH\_Udmf\_DeleteUnifiedData(OH\_UdmfOptions\* options, OH\_UdmfData\*\* dataArray, unsigned int\* dataSize)

**Description**

Deletes an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance from the UDMF database.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md)\* options | Pointer to the [OH\_UdmfOptions](../../structs/oh-udmfoptions/document.md) instance. |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\*\* dataArray | Double pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. You should use the [OH\_UDMF\_GetDataElementAt](#oh_udmf_getdataelementat) function to access each element by subscript. This double pointer should be released by using the [OH\_Udmf\_DestroyDataArray](#oh_udmf_destroydataarray) function. |
| unsigned int\* dataSize | Pointer to the data size obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error codes. For details, see [Udmf\_ErrCode](../udmf-err-code-h/document.md#udmf_errcode).

Returns **UDMF\_E\_OK** if the operation is successful.

Returns **UDMF\_E\_INVALID\_PARAM** if an invalid parameter is passed in.

Returns **UDMF\_ERR** if an internal data error occurs. The possible cause may be the service error or insufficient memory.

 |

#### \[h2\]OH\_Udmf\_DestroyDataArray()

void OH\_Udmf\_DestroyDataArray(OH\_UdmfData\*\* dataArray, unsigned int dataSize)

**Description**

Destroys the memory of the data array.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\*\* dataArray | Double pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance. |
| unsigned int dataSize | Data size. |

**See**

OH\_UdmfData

#### \[h2\]OH\_UdmfProgressInfo\_GetProgress()

int OH\_UdmfProgressInfo\_GetProgress(OH\_Udmf\_ProgressInfo\* progressInfo)

**Description**

Obtains the progress (in percentage) from an [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md)\* progressInfo | Pointer to the [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Progress obtained, in percentage. |

#### \[h2\]OH\_UdmfProgressInfo\_GetStatus()

int OH\_UdmfProgressInfo\_GetStatus(OH\_Udmf\_ProgressInfo\* progressInfo)

**Description**

Obtains the status information from an [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md)\* progressInfo | Pointer to the [OH\_Udmf\_ProgressInfo](../../structs/oh-udmf-progressinfo/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Status information obtained. |

#### \[h2\]OH\_UdmfGetDataParams\_Create()

OH\_UdmfGetDataParams\* OH\_UdmfGetDataParams\_Create()

**Description**

Creates an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_UdmfGetDataParams\_Destroy](#oh_udmfgetdataparams_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* | Returns a pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance created if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_UdmfGetDataParams\_Destroy()

void OH\_UdmfGetDataParams\_Destroy(OH\_UdmfGetDataParams\* pThis)

**Description**

Destroys an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* pThis | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |

#### \[h2\]OH\_UdmfGetDataParams\_SetDestUri()

void OH\_UdmfGetDataParams\_SetDestUri(OH\_UdmfGetDataParams\* params, const char\* destUri)

**Description**

Sets the destination directory in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

If the destination directory is set, data of the file type will be copied to the specified directory. The file type data obtained in the callback will be replaced with the URI of the destination directory.

If the destination directory is not specified, the file will not be copied. The file type data obtained in the callback is the URI of the source directory.

If the application involves complex file processing or files need to be copied to multiple directories, you are advised to leave this parameter unspecified and let the application handle the file copy.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* params | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| const char\* destUri | Destination directory to set. |

#### \[h2\]OH\_UdmfGetDataParams\_SetFileConflictOptions()

void OH\_UdmfGetDataParams\_SetFileConflictOptions(OH\_UdmfGetDataParams\* params, const Udmf\_FileConflictOptions options)

**Description**

Sets the policy for resolving file conflicts in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* params | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| const [Udmf\_FileConflictOptions](#udmf_fileconflictoptions) options | Policy to set. |

#### \[h2\]OH\_UdmfGetDataParams\_SetProgressIndicator()

void OH\_UdmfGetDataParams\_SetProgressIndicator(OH\_UdmfGetDataParams\* params, const Udmf\_ProgressIndicator progressIndicator)

**Description**

Sets the progress indicator in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* params | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| const [Udmf\_ProgressIndicator](#udmf_progressindicator) progressIndicator | Whether to use the default progress indicator. |

#### \[h2\]OH\_UdmfGetDataParams\_SetDataProgressListener()

void OH\_UdmfGetDataParams\_SetDataProgressListener(OH\_UdmfGetDataParams\* params, const OH\_Udmf\_DataProgressListener dataProgressListener)

**Description**

Sets the callback used to return the progress obtained in an [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md)\* params | Pointer to the [OH\_UdmfGetDataParams](../../structs/oh-udmfgetdataparams/document.md) instance. |
| const [OH\_Udmf\_DataProgressListener](#oh_udmf_dataprogresslistener) dataProgressListener | Callback to set. |

#### \[h2\]OH\_UDMF\_GetDataElementAt()

OH\_UdmfData\* OH\_UDMF\_GetDataElementAt(OH\_UdmfData\*\* dataArray, unsigned int index)

**Description**

Obtains the unified data object with the specified index from an [OH\_UdmfData](../../structs/oh-udmfdata/document.md) array.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_UdmfData](../../structs/oh-udmfdata/document.md)\*\* dataArray | 
Double pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) array.

Only the arrays obtained from the [OH\_Udmf\_GetUnifiedDataByOptions](#oh_udmf_getunifieddatabyoptions) and [OH\_Udmf\_DeleteUnifiedData](#oh_udmf_deleteunifieddata) APIs are accepted.

 |
| unsigned int index | Index of the unified data object to be obtained. Ensure that the value does not exceed the array range. Otherwise, out-of-bounds array occurs. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfData\*](../../structs/oh-udmfdata/document.md) | Returns a pointer to the [OH\_UdmfData](../../structs/oh-udmfdata/document.md) instance if the execution is successful; returns null if the input array is empty. |
