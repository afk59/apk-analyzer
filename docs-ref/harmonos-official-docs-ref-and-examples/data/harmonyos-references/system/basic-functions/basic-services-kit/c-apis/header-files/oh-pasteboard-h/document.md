# oh\_pasteboard.h

#### Overview

Provides data structure, enum types, and APIs for accessing the system pasteboard.

**File to include**: <database/pasteboard/oh\_pasteboard.h>

**Library**: libpasteboard.so

**System capability**: SystemCapability.MiscServices.Pasteboard

**Since**: 13

**Related module**: [Pasteboard](../../modules/pasteboard/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md) | Pasteboard\_ProgressInfo | Defines a struct for the progress information. |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) | Pasteboard\_GetDataParams | Defines a struct for the parameters required for obtaining the pasteboard data and paste progress. |
| [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) | OH\_PasteboardObserver | Defines a struct for the pasteboard observer. |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) | OH\_Pasteboard | Defines a struct for the pasteboard object to operate the system pasteboard. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN](#pasteboard_mimetype_text_plain) "text/plain" | Plain text type. |
| [PASTEBOARD\_MIMETYPE\_TEXT\_URI](#pasteboard_mimetype_text_uri) "text/uri" | URI type. |
| [PASTEBOARD\_MIMETYPE\_TEXT\_HTML](#pasteboard_mimetype_text_html) "text/html" | HTML type. |
| [PASTEBOARD\_MIMETYPE\_PIXELMAP](#pasteboard_mimetype_pixelmap) "pixelMap" | pixelMap type. |
| [PASTEBOARD\_MIMETYPE\_TEXT\_WANT](#pasteboard_mimetype_text_want) "text/want" | Want type. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Pasteboard\_NotifyType](#pasteboard_notifytype) | Pasteboard\_NotifyType | Enumerates the data change types of the pasteboard. |
| [Pasteboard\_FileConflictOptions](#pasteboard_fileconflictoptions) | Pasteboard\_FileConflictOptions | Enumerates the options used to resolve file copy conflicts. |
| [Pasteboard\_ProgressIndicator](#pasteboard_progressindicator) | Pasteboard\_ProgressIndicator | Enumerates the progress indicator options. You can use the default progress indicator as required. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_Pasteboard\_ProgressListener)(Pasteboard\_ProgressInfo\* progressInfo)](#oh_pasteboard_progresslistener) | OH\_Pasteboard\_ProgressListener | Defines a callback to be invoked to obtain the progress information when the default progress indicator is not used. |
| [typedef void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type)](#pasteboard_notify) | Pasteboard\_Notify | Defines a callback to be invoked when the pasteboard content changes. |
| [typedef void (\*Pasteboard\_Finalize)(void\* context)](#pasteboard_finalize) | Pasteboard\_Finalize | Defines a callback to be invoked to release the context when the pasteboard observer object is destroyed. |
| [OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create()](#oh_pasteboardobserver_create) | \- | Creates an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance and a pointer to it. |
| [int OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer)](#oh_pasteboardobserver_destroy) | \- | Destroys the [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance. |
| [int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context,const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize)](#oh_pasteboardobserver_setdata) | \- | Sets a callback for the pasteboard observer. |
| [OH\_Pasteboard\* OH\_Pasteboard\_Create()](#oh_pasteboard_create) | \- | Creates an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance and a pointer to it. |
| [void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_destroy) | \- | Destroys the [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| [int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](#oh_pasteboard_subscribe) | \- | Subscribes to the pasteboard observer. |
| [int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](#oh_pasteboard_unsubscribe) | \- | Unsubscribes from the pasteboard observer. |
| [bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_isremotedata) | \- | Checks whether the pasteboard data comes from remote devices. |
| [int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len)](#oh_pasteboard_getdatasource) | \- | Obtains the pasteboard data source. |
| [bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type)](#oh_pasteboard_hastype) | \- | Checks whether the pasteboard contains data of the specified type. |
| [bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_hasdata) | \- | Checks whether the pasteboard contains data. |
| [OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status)](#oh_pasteboard_getdata) | \- | Obtains data from the pasteboard. |
| [int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data)](#oh_pasteboard_setdata) | \- | Sets the unified data object in the OH\_Pasteboard instance. |
| [int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard)](#oh_pasteboard_cleardata) | \- | Clears data from the pasteboard. |
| [char \*\*OH\_Pasteboard\_GetMimeTypes(OH\_Pasteboard \*pasteboard, unsigned int \*count)](#oh_pasteboard_getmimetypes) | \- | Obtains the MIME types from the pasteboard. |
| [Pasteboard\_GetDataParams \*OH\_Pasteboard\_GetDataParams\_Create(void)](#oh_pasteboard_getdataparams_create) | \- | Creates a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance and a pointer to it. |
| [void OH\_Pasteboard\_GetDataParams\_Destroy(Pasteboard\_GetDataParams\* params)](#oh_pasteboard_getdataparams_destroy) | \- | Destroys the [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance. |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressIndicator(Pasteboard\_GetDataParams\* params,Pasteboard\_ProgressIndicator progressIndicator)](#oh_pasteboard_getdataparams_setprogressindicator) | \- | Sets a progress indicator in [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md). You can use the default progress indicator as required. |
| [void OH\_Pasteboard\_GetDataParams\_SetDestUri(Pasteboard\_GetDataParams\* params, const char\* destUri, uint32\_t destUriLen)](#oh_pasteboard_getdataparams_setdesturi) | \- | Sets the destination URI in a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance for copying files. If file processing is not supported, this parameter is not required. If the application involves complex file processing policies or needs to distinguish file multipathing storage, you are advised not to set this parameter but let the application copies files by itself. |
| [void OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions(Pasteboard\_GetDataParams\* params,Pasteboard\_FileConflictOptions option)](#oh_pasteboard_getdataparams_setfileconflictoptions) | \- | Sets the options used to resolve file copy conflicts in a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance. |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressListener(Pasteboard\_GetDataParams\* params,const OH\_Pasteboard\_ProgressListener listener)](#oh_pasteboard_getdataparams_setprogresslistener) | \- | Sets a progress listener in a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance. |
| [int OH\_Pasteboard\_ProgressInfo\_GetProgress(Pasteboard\_ProgressInfo\* progressInfo)](#oh_pasteboard_progressinfo_getprogress) | \- | Obtains the paste progress in a [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md) instance. |
| [void OH\_Pasteboard\_ProgressCancel(Pasteboard\_GetDataParams\* params)](#oh_pasteboard_progresscancel) | \- | Cancels the ongoing paste operation when the pasteboard data is obtained. |
| [OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params,int\* status)](#oh_pasteboard_getdatawithprogress) | \- | Obtains the pasteboard data and paste progress. Folders cannot be copied. |
| [uint32\_t OH\_Pasteboard\_GetChangeCount(OH\_Pasteboard \*pasteboard)](#oh_pasteboard_getchangecount) | \- | Obtains the number of pasteboard content changes. |
| [void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode))](#oh_pasteboard_syncdelayeddataasync) | \- | Syncs all delayed data from the application to the pasteboard. Use this API together with the [OH\_UdmfRecordProvider\_SetData](../../../../../../application-framework/arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfrecordprovider_setdata) API. When the application uses the delayed copy feature, only the data types supported by the application are written to the pasteboard. Before the application exits, it should call the [OH\_Pasteboard\_SetData](#oh_pasteboard_setdata) API to submit all copied data or call the **OH\_Pasteboard\_SyncDelayedDataAsync** API to notify the pasteboard to obtain all data. The application can exit only after the data sync is complete. Otherwise, other applications may fail to obtain the data. |

#### Macro Description

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN

#define PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN "text/plain"

**Description**

Defines the plain text type.

**Since**: 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_URI

#define PASTEBOARD\_MIMETYPE\_TEXT\_URI "text/uri"

**Description**

Defines the URI type.

**Since**: 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_HTML

#define PASTEBOARD\_MIMETYPE\_TEXT\_HTML "text/html"

**Description**

Defines the HTML type.

**Since**: 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_PIXELMAP

#define PASTEBOARD\_MIMETYPE\_PIXELMAP "pixelMap"

**Description**

Defines the pixelMap type.

**Since**: 22

#### \[h2\]PASTEBOARD\_MIMETYPE\_TEXT\_WANT

#define PASTEBOARD\_MIMETYPE\_TEXT\_WANT "text/want"

**Description**

Defines the Want type.

**Since**: 22

#### Enum Description

#### \[h2\]Pasteboard\_NotifyType

enum Pasteboard\_NotifyType

**Description**

Enumerates the data change types of the pasteboard.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| NOTIFY\_LOCAL\_DATA\_CHANGE = 1 | The pasteboard data of the local device is changed. |
| NOTIFY\_REMOTE\_DATA\_CHANGE = 2 | The pasteboard data of a non-local device on the network is changed. |

#### \[h2\]Pasteboard\_FileConflictOptions

enum Pasteboard\_FileConflictOptions

**Description**

Enumerates the options used to resolve file copy conflicts.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| PASTEBOARD\_OVERWRITE = 0 | Overwrites the file with the same name in the destination directory. |
| PASTEBOARD\_SKIP = 1 | Skips the file if there is a file with the same name in the destination directory. |

#### \[h2\]Pasteboard\_ProgressIndicator

enum Pasteboard\_ProgressIndicator

**Description**

Enumerates the progress indicator options. You can use the default progress indicator as required.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| PASTEBOARD\_NONE = 0 | The default progress indicator is not used. |
| PASTEBOARD\_DEFAULT = 1 | The default progress indicator is used. |

#### Function Description

#### \[h2\]OH\_Pasteboard\_ProgressListener()

typedef void (\*OH\_Pasteboard\_ProgressListener)(Pasteboard\_ProgressInfo\* progressInfo)

**Description**

Defines a callback to be invoked to obtain the progress information when the default progress indicator is not used.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md)\* progressInfo | A struct for the progress information. This information is reported only when [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md) is set to **NONE**. |

#### \[h2\]Pasteboard\_Notify()

typedef void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type)

**Description**

Defines a callback to be invoked when the pasteboard content changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* context | Context information, which is passed by the [OH\_PasteboardObserver\_SetData](#oh_pasteboardobserver_setdata) function. |
| [Pasteboard\_NotifyType](#pasteboard_notifytype) type | Data change type. For details, see [Pasteboard\_NotifyType](#pasteboard_notifytype). |

#### \[h2\]Pasteboard\_Finalize()

typedef void (\*Pasteboard\_Finalize)(void\* context)

**Description**

Defines a callback to be invoked to release the context when the pasteboard observer object is destroyed.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* context | Pointer to the context to release. |

#### \[h2\]OH\_PasteboardObserver\_Create()

OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create()

**Description**

Creates an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance and a pointer to it.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md)\* | 
Returns a pointer to the [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance created if the operation is successful; returns **nullptr** otherwise.

If this pointer is no longer required, use [OH\_PasteboardObserver\_Destroy](#oh_pasteboardobserver_destroy) to destroy it. Otherwise, memory leaks may occur.

 |

#### \[h2\]OH\_PasteboardObserver\_Destroy()

int OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer)

**Description**

Destroys the [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md)\* observer | Pointer to an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_PasteboardObserver\_SetData()

int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context,const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize)

**Description**

Sets a callback for the pasteboard observer.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md)\* observer | Pointer to an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance. |
| void\* context | Pointer to the context, which is passed to [Pasteboard\_Notify](#pasteboard_notify) as the first parameter. |
| const [Pasteboard\_Notify](#pasteboard_notify) callback | Callback to be invoked when the data changes. For details, see [Pasteboard\_Notify](#pasteboard_notify). |
| const [Pasteboard\_Finalize](#pasteboard_finalize) finalize | Optional callback, which can be used to release context data when the pasteboard observer is destroyed. For details, see [Pasteboard\_Finalize](#pasteboard_finalize). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_Create()

OH\_Pasteboard\* OH\_Pasteboard\_Create()

**Description**

Creates an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance and a pointer to it.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* | 
Returns a pointer to the [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance created if the operation is successful; returns **nullptr** otherwise.

If this pointer is no longer required, use [OH\_PasteboardObserver\_Destroy](#oh_pasteboard_destroy) to destroy it. Otherwise, memory leaks may occur.

 |

#### \[h2\]OH\_Pasteboard\_Destroy()

void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard)

**Description**

Destroys the [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |

#### \[h2\]OH\_Pasteboard\_Subscribe()

int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)

**Description**

Subscribes to the pasteboard observer.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| int type | Subscribed data change type of the pasteboard. For details, see [Pasteboard\_NotifyType](#pasteboard_notifytype). |
| const [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md)\* observer | Pointer to an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance. It specifies the callback to be invoked when the pasteboard data changes. For details, see [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_Unsubscribe()

int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)

**Description**

Unsubscribes from the pasteboard observer.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| int type | Subscribed data change type of the pasteboard. For details, see [Pasteboard\_NotifyType](#pasteboard_notifytype). |
| const [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md)\* observer | Pointer to an [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md) instance. It specifies the callback to be invoked when the pasteboard data changes. For details, see [OH\_PasteboardObserver](../../structs/oh-pasteboardobserver/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_IsRemoteData()

bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard)

**Description**

Checks whether the pasteboard data comes from remote devices.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns a Boolean value indicating whether the data comes from a remote device. The value **true** means the data is from a remote device; **false** means the data is from the local device. |

#### \[h2\]OH\_Pasteboard\_GetDataSource()

int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len)

**Description**

Obtains the pasteboard data source.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| char\* source | Pointer to the pasteboard data source instance. You need to allocate the memory for the pointer before calling this API. |
| unsigned int len | Memory length corresponding to the source. If the memory length is insufficient, the API call will fail. The recommended length is 128 bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_HasType()

bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type)

**Description**

Checks whether the pasteboard contains data of the specified type.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| const char\* type | Data type to be checked, which includes the basic data types and custom data types. The options of the basic data types are as follows: **"text/plain"**, **"text/html"**, **"text/uri"**, **"text/want"**, and **"pixelMap"**. For details, see [Macros](#macros). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns a Boolean value indicating whether the pasteboard contains data of the specified type. The value **true** means the pasteboard contains data of the specified type; the value **false** means the opposite. |

#### \[h2\]OH\_Pasteboard\_HasData()

bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard)

**Description**

Checks whether the pasteboard contains data.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns a Boolean value indicating whether the pasteboard contains data. The value **true** means the pasteboard contains data; the value **false** means the opposite. |

#### \[h2\]OH\_Pasteboard\_GetData()

OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status)

**Description**

Obtains data from the pasteboard.

**Since**: 13

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| int\* status | Output parameter, indicating the error code of the operation. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfData](../../../../../../application-framework/arkdata/c-apis/structs/oh-udmfdata/document.md)\* | Returns the pointer to an [OH\_UdmfData](../../../../../../application-framework/arkdata/c-apis/structs/oh-udmfdata/document.md) instance obtained if the operation is successful; returns a null pointer otherwise. |

#### \[h2\]OH\_Pasteboard\_SetData()

int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data)

**Description**

Sets the unified data object in the OH\_Pasteboard instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| [OH\_UdmfData](../../../../../../application-framework/arkdata/c-apis/structs/oh-udmfdata/document.md)\* data | Pointer to an [OH\_UdmfData](../../../../../../application-framework/arkdata/c-apis/structs/oh-udmfdata/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_ClearData()

int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard)

**Description**

Clears data from the pasteboard.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode).

Returns **ERR\_OK** if the operation is successful.

Returns **ERR\_INVALID\_PARAMETER** if an invalid parameter is passed in.

 |

#### \[h2\]OH\_Pasteboard\_GetMimeTypes()

char \*\*OH\_Pasteboard\_GetMimeTypes(OH\_Pasteboard \*pasteboard, unsigned int \*count)

**Description**

Obtains the MIME types from the pasteboard.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) \*pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| unsigned int \*count | Pointer to the number of MIME types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| char | Returns the MIME types obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_Create()

Pasteboard\_GetDataParams \*OH\_Pasteboard\_GetDataParams\_Create(void)

**Description**

Creates a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance and a pointer to it.

**Since**: 15

**Returns**

| Type | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) | 
Returns a pointer to the [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance created if the operation is successful; returns **nullptr** otherwise.

If this pointer is no longer required, use [OH\_Pasteboard\_GetDataParams\_Destroy](#oh_pasteboard_getdataparams_destroy) to destroy it. Otherwise, memory leaks may occur.

 |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_Destroy()

void OH\_Pasteboard\_GetDataParams\_Destroy(Pasteboard\_GetDataParams\* params)

**Description**

Destroys the [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetProgressIndicator()

void OH\_Pasteboard\_GetDataParams\_SetProgressIndicator(Pasteboard\_GetDataParams\* params,Pasteboard\_ProgressIndicator progressIndicator)

**Description**

Sets a progress indicator in [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md). You can use the default progress indicator as required.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |
| [Pasteboard\_ProgressIndicator](#pasteboard_progressindicator) progressIndicator | Progress indicator to set. |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetDestUri()

void OH\_Pasteboard\_GetDataParams\_SetDestUri(Pasteboard\_GetDataParams\* params, const char\* destUri, uint32\_t destUriLen)

**Description**

Sets the destination URI for copying files. If file processing is not supported, this parameter is not required. If the application involves complex file processing policies or needs to distinguish file multipathing storage, you are advised not to set this parameter but let the application copies files by itself.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |
| const char\* destUri | Destination URI of the copied file. |
| uint32\_t destUriLen | Length of the destination URI of the copied file. |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions()

void OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions(Pasteboard\_GetDataParams\* params,Pasteboard\_FileConflictOptions option)

**Description**

Sets the options used to resolve file copy conflicts in a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |
| [Pasteboard\_FileConflictOptions](#pasteboard_fileconflictoptions) option | Options used to resolve file copy conflicts. The default value is **PASTEBOARD\_OVERWRITE**. |

#### \[h2\]OH\_Pasteboard\_GetDataParams\_SetProgressListener()

void OH\_Pasteboard\_GetDataParams\_SetProgressListener(Pasteboard\_GetDataParams\* params,const OH\_Pasteboard\_ProgressListener listener)

**Description**

Sets a progress listener in a [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |
| const [OH\_Pasteboard\_ProgressListener](#oh_pasteboard_progresslistener) listener | Progress listener. |

#### \[h2\]OH\_Pasteboard\_ProgressInfo\_GetProgress()

int OH\_Pasteboard\_ProgressInfo\_GetProgress(Pasteboard\_ProgressInfo\* progressInfo)

**Description**

Obtains the paste progress in a [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md) instance.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md)\* progressInfo | Pointer to a [Pasteboard\_ProgressInfo](../../structs/pasteboard-progressinfo/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Percentage of the paste progress. |

#### \[h2\]OH\_Pasteboard\_ProgressCancel()

void OH\_Pasteboard\_ProgressCancel(Pasteboard\_GetDataParams\* params)

**Description**

Cancels the ongoing paste operation when the pasteboard data is obtained.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |

#### \[h2\]OH\_Pasteboard\_GetDataWithProgress()

OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params,int\* status)

**Description**

Obtains the pasteboard data and paste progress. Folders cannot be copied.

**Since**: 15

**Required permissions**: ohos.permission.READ\_PASTEBOARD. While most applications must [request permissions to access the pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/get-pastedata-permission-guidelines), those using [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pastebutton) can access the pasteboard content without permission requests.

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md)\* pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| [Pasteboard\_GetDataParams](../../structs/pasteboard-getdataparams/document.md)\* params | Pointer to an **OH\_Pasteboard\_GetDataParams** instance. |
| int\* status | Output parameter, indicating the error code of the operation. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_UdmfData](../../../../../../application-framework/arkdata/c-apis/structs/oh-udmfdata/document.md)\* | Returns a pointer to the **OH\_UdmfData** instance obtained if the operation is successful; returns a null pointer otherwise. |

#### \[h2\]OH\_Pasteboard\_GetChangeCount()

uint32\_t OH\_Pasteboard\_GetChangeCount(OH\_Pasteboard \*pasteboard)

**Description**

Obtains the number of pasteboard content changes.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) \*pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | 
Returns the number of pasteboard content changes if this API is called successfully; otherwise, returns **0**.

Even though the pasteboard data expires, or the data becomes empty because of the called **OH\_Pasteboard\_ClearData** API, the number of data changes remains.

When the system is restarted, or the pasteboard service is restarted due to an exception, the number of pasteboard data changes counts from 0. In addition, copying the same data repeatedly is considered to change the data for multiple times. Therefore, each time the data is copied, the number of data changes increases.

 |

#### \[h2\]OH\_Pasteboard\_SyncDelayedDataAsync()

void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode))

**Description**

Syncs all delayed data from the application to the pasteboard. Use this API together with the [OH\_UdmfRecordProvider\_SetData](../../../../../../application-framework/arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfrecordprovider_setdata) API. When the application uses the delayed copy feature, only the data types supported by the application are written to the pasteboard. Before the application exits, it should call the [OH\_Pasteboard\_SetData](#oh_pasteboard_setdata) API to submit all copied data or call the **OH\_Pasteboard\_SyncDelayedDataAsync** API to notify the pasteboard to obtain all data. The application can exit only after the data sync is complete. Otherwise, other applications may fail to obtain the data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/vZ6ZLqRVSCykTUbeLBjw5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062359Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47C26A85FEBD1AF0CB63A7ED5BC4C10C90544BA57CE04E884D4FF9E999ECE119)

-   Calling this API prolongs the exit process. You are advised to directly set data to the pasteboard instead of calling the [OH\_UdmfRecordProvider\_SetData](../../../../../../application-framework/arkdata/c-apis/header-files/udmf-h/document.md#oh_udmfrecordprovider_setdata) and **OH\_Pasteboard\_SyncDelayedDataAsync** APIs.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) \*pasteboard | Pointer to an [OH\_Pasteboard](../../structs/oh-pasteboard/document.md) instance. |
| void (\*callback)(int errorCode) | Pointer to the callback invoked when data sync is complete. **errorCode** indicates the result of the sync task. For details about the error codes, see [PASTEBOARD\_ErrCode](../oh-pasteboard-err-code-h/document.md#pasteboard_errcode). |
