# oh\_commonevent.h

#### Overview

Defines the APIs for subscribing to and unsubscribing from common events and enumerates the error codes.

**Library**: libohcommonevent.so

**File to include**: <BasicServicesKit/oh\_commonevent.h>

**System capability**: SystemCapability.Notification.CommonEvent

**Since**: 12

**Related module**: [OH\_CommonEvent](../../modules/oh-commonevent/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md) | CommonEvent\_SubscribeInfo | Defines a struct for the subscriber information. |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md) | CommonEvent\_PublishInfo | Defines the property object used for publishing a common event. |
| [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md) | CommonEvent\_RcvData | Defines a struct for the common event data. |

#### \[h2\]Variables

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| void | CommonEvent\_Subscriber | Defines a struct for the subscriber. |
| void | CommonEvent\_Parameters | Defines a struct for the additional information of a common event. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | CommonEvent\_ErrCode | Enumerates the error codes. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*CommonEvent\_ReceiveCallback)(const CommonEvent\_RcvData \*data)](#commonevent_receivecallback) | CommonEvent\_ReceiveCallback | Defines the callback function of a common event. |
| [CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events\[\], int32\_t eventsNum)](#oh_commonevent_createsubscribeinfo) | \- | Creates the subscriber information. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherPermission(CommonEvent\_SubscribeInfo\* info, const char\* permission)](#oh_commonevent_setpublisherpermission) | \- | Sets the subscriber permission. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherBundleName(CommonEvent\_SubscribeInfo\* info, const char\* bundleName)](#oh_commonevent_setpublisherbundlename) | \- | Sets a bundle name of the publisher. |
| [void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)](#oh_commonevent_destroysubscribeinfo) | \- | Destroys the subscriber information. |
| [CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info,CommonEvent\_ReceiveCallback callback)](#oh_commonevent_createsubscriber) | \- | Creates a subscriber. |
| [void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_destroysubscriber) | \- | Destroys a subscriber. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_subscribe) | \- | Subscribes to a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_unsubscribe) | \- | Unsubscribes from a common event. |
| [const char\* OH\_CommonEvent\_GetEventFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_geteventfromrcvdata) | \- | Obtains the name of a common event. |
| [int32\_t OH\_CommonEvent\_GetCodeFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getcodefromrcvdata) | \- | Obtains the result data (integer type) of a common event. |
| [const char\* OH\_CommonEvent\_GetDataStrFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getdatastrfromrcvdata) | \- | Obtains the result data (string type) of a common event. |
| [const char\* OH\_CommonEvent\_GetBundleNameFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getbundlenamefromrcvdata) | \- | Obtains the bundle name of a common event. |
| [const CommonEvent\_Parameters\* OH\_CommonEvent\_GetParametersFromRcvData(const CommonEvent\_RcvData\* rcvData)](#oh_commonevent_getparametersfromrcvdata) | \- | Obtains the additional information of a common event. |
| [CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)](#oh_commonevent_createpublishinfo) | \- | Creates a property object of a common event. |
| [void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)](#oh_commonevent_destroypublishinfo) | \- | Destroys a property object of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoBundleName(CommonEvent\_PublishInfo\* info, const char\* bundleName)](#oh_commonevent_setpublishinfobundlename) | \- | Sets the bundle name of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoPermissions(CommonEvent\_PublishInfo\* info,const char\* permissions\[\], int32\_t num)](#oh_commonevent_setpublishinfopermissions) | \- | Sets permissions for a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoCode(CommonEvent\_PublishInfo\* info, int32\_t code)](#oh_commonevent_setpublishinfocode) | \- | Sets the result code (integer type) of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoData(CommonEvent\_PublishInfo\* info,const char\* data, size\_t length)](#oh_commonevent_setpublishinfodata) | \- | Sets the result data (string type) of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoParameters(CommonEvent\_PublishInfo\* info,CommonEvent\_Parameters\* param)](#oh_commonevent_setpublishinfoparameters) | \- | Sets the additional information of a common event. |
| [CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()](#oh_commonevent_createparameters) | \- | Creates an additional information object of a common event. |
| [void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)](#oh_commonevent_destroyparameters) | \- | Destroys the additional information object of a common event. |
| [bool OH\_CommonEvent\_HasKeyInParameters(const CommonEvent\_Parameters\* para, const char\* key)](#oh_commonevent_haskeyinparameters) | \- | Checks whether the additional information of a common event contains a KV pair. |
| [int OH\_CommonEvent\_GetIntFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const int defaultValue)](#oh_commonevent_getintfromparameters) | \- | Obtains the int data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntToParameters(CommonEvent\_Parameters\* param, const char\* key, int value)](#oh_commonevent_setinttoparameters) | \- | Sets the int data with a specific key for the additional information of a common event. |
| [int32\_t OH\_CommonEvent\_GetIntArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, int\*\* array)](#oh_commonevent_getintarrayfromparameters) | \- | Obtains the int array with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const int\* value, size\_t num)](#oh_commonevent_setintarraytoparameters) | \- | Sets the int array with a specific key for the additional information of a common event. |
| [long OH\_CommonEvent\_GetLongFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const long defaultValue)](#oh_commonevent_getlongfromparameters) | \- | Obtains the long data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongToParameters(CommonEvent\_Parameters\* param, const char\* key, long value)](#oh_commonevent_setlongtoparameters) | \- | Sets the long data with a specific key for the additional information of a common event. |
| [int32\_t OH\_CommonEvent\_GetLongArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, long\*\* array)](#oh_commonevent_getlongarrayfromparameters) | \- | Obtains the long array with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const long\* value, size\_t num)](#oh_commonevent_setlongarraytoparameters) | \- | Sets the long array for the additional information of a common event. |
| [bool OH\_CommonEvent\_GetBoolFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const bool defaultValue)](#oh_commonevent_getboolfromparameters) | \- | Obtains the Boolean data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolToParameters(CommonEvent\_Parameters\* param, const char\* key, bool value)](#oh_commonevent_setbooltoparameters) | \- | Sets the Boolean data with a specific key for the additional information of a common event. |
| [int32\_t OH\_CommonEvent\_GetBoolArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, bool\*\* array)](#oh_commonevent_getboolarrayfromparameters) | \- | Obtains the Boolean array with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const bool\* value, size\_t num)](#oh_commonevent_setboolarraytoparameters) | \- | Sets the Boolean array with a specific key for the additional information of a common event. |
| [char OH\_CommonEvent\_GetCharFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const char defaultValue)](#oh_commonevent_getcharfromparameters) | \- | Obtains the character data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharToParameters(CommonEvent\_Parameters\* param, const char\* key, char value)](#oh_commonevent_setchartoparameters) | \- | Sets the character data with a specific key for the additional information of a common event. |
| [int32\_t OH\_CommonEvent\_GetCharArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, char\*\* array)](#oh_commonevent_getchararrayfromparameters) | \- | Obtains the character array with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const char\* value, size\_t num)](#oh_commonevent_setchararraytoparameters) | \- | Sets the character array with a specific key for the additional information of a common event. |
| [double OH\_CommonEvent\_GetDoubleFromParameters(const CommonEvent\_Parameters\* para, const char\* key,const double defaultValue)](#oh_commonevent_getdoublefromparameters) | \- | Obtains the double data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleToParameters(CommonEvent\_Parameters\* param, const char\* key,double value)](#oh_commonevent_setdoubletoparameters) | \- | Sets the double data with a specific key for the additional information of a common event. |
| [int32\_t OH\_CommonEvent\_GetDoubleArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key,double\*\* array)](#oh_commonevent_getdoublearrayfromparameters) | \- | Obtains the double array data with a specific key from the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const double\* value, size\_t num)](#oh_commonevent_setdoublearraytoparameters) | \- | Sets the double array with a specific key for the additional information of a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)](#oh_commonevent_publish) | \- | Publishes a common event. |
| [CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)](#oh_commonevent_publishwithinfo) | \- | Publishes a common event with specified properties. |
| [bool OH\_CommonEvent\_IsOrderedCommonEvent(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_isorderedcommonevent) | \- | Checks whether a common event is an ordered one. |
| [bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_finishcommonevent) | \- | Finishes an ordered common event. |
| [bool OH\_CommonEvent\_GetAbortCommonEvent(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getabortcommonevent) | \- | Checks whether an ordered common event is aborted. |
| [bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_abortcommonevent) | \- | Aborts an ordered common event when used with [OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent). After the abort, the common event is not sent to the next subscriber. |
| [bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_clearabortcommonevent) | \- | Clears the abort state of an ordered common event when used with [OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent). After the clearance, the common event is sent to the next subscriber. |
| [int32\_t OH\_CommonEvent\_GetCodeFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getcodefromsubscriber) | \- | Obtains the result code (integer type) of an ordered common event. |
| [bool OH\_CommonEvent\_SetCodeToSubscriber(CommonEvent\_Subscriber\* subscriber, int32\_t code)](#oh_commonevent_setcodetosubscriber) | \- | Sets the result code (string type) of an ordered common event. |
| [const char\* OH\_CommonEvent\_GetDataFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](#oh_commonevent_getdatafromsubscriber) | \- | Obtains the result data (string type) of an ordered common event. |
| [bool OH\_CommonEvent\_SetDataToSubscriber(CommonEvent\_Subscriber\* subscriber, const char\* data, size\_t length)](#oh_commonevent_setdatatosubscriber) | \- | Sets the result data (string type) of an ordered common event. |

#### Enum Description

#### \[h2\]CommonEvent\_ErrCode

enum CommonEvent\_ErrCode

**Description**

Enumerates the error codes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| COMMONEVENT\_ERR\_OK = 0 | Operation successful. |
| COMMONEVENT\_ERR\_PERMISSION\_ERROR = 201 | Permission denied. |
| COMMONEVENT\_ERR\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED = 1500003 | 
Event sending frequency is too high.

**Since**: 20

 |
| COMMONEVENT\_ERR\_NOT\_SYSTEM\_SERVICE = 1500004 | The third-party application fails to send system common events. |
| COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED = 1500007 | Failed to send IPC requests. |
| COMMONEVENT\_ERR\_INIT\_UNDONE = 1500008 | Services not initialized. |
| COMMONEVENT\_ERR\_OBTAIN\_SYSTEM\_PARAMS = 1500009 | System error. |
| COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED = 1500010 | The number of subscribers exceeds the upper limit. |
| COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED = 1500011 | Failed to allocate memory. |

#### Function Description

#### \[h2\]CommonEvent\_ReceiveCallback()

typedef void (\*CommonEvent\_ReceiveCallback)(const CommonEvent\_RcvData \*data)

**Description**

Defines the callback function of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md) \*data | Pointer to the callback data of a common event. |

#### \[h2\]OH\_CommonEvent\_CreateSubscribeInfo()

CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events\[\], int32\_t eventsNum)

**Description**

Creates the subscriber information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* events\[\] | Pointer to the common events. The valid number of subscribed common events is the smaller value between **eventsNum** and **events\[\]**. |
| int32\_t eventsNum | Number of common events to subscribe. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md)\* | Returns the subscriber information created if the operation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_CommonEvent\_SetPublisherPermission()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherPermission(CommonEvent\_SubscribeInfo\* info, const char\* permission)

**Description**

Sets the subscriber permission.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md)\* info | Pointer to the subscriber information. |
| const char\* permission | Pointer to the permission name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_SetPublisherBundleName()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherBundleName(CommonEvent\_SubscribeInfo\* info, const char\* bundleName)

**Description**

Sets a bundle name of the publisher.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md)\* info | Pointer to the subscriber information. |
| const char\* bundleName | Pointer to the bundle name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_DestroySubscribeInfo()

void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)

**Description**

Destroys the subscriber information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md)\* info | Pointer to the subscriber information. |

#### \[h2\]OH\_CommonEvent\_CreateSubscriber()

CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info,CommonEvent\_ReceiveCallback callback)

**Description**

Creates a subscriber.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_SubscribeInfo](../../structs/commonevent-subscribeinfo/document.md)\* info | Pointer to the subscriber information. |
| [CommonEvent\_ReceiveCallback](#commonevent_receivecallback) callback | Callback to be invoked when a common event is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* | Returns the subscriber created if the operation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_CommonEvent\_DestroySubscriber()

void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)

**Description**

Destroys a subscriber.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

#### \[h2\]OH\_CommonEvent\_Subscribe()

CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)

**Description**

Subscribes to a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](#commonevent_errcode): Failed to send IPC requests.

[COMMONEVENT\_ERR\_INIT\_UNDONE](#commonevent_errcode): The common event service is not initialized.

[COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED](#commonevent_errcode): The number of subscribers exceeds 200.

[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](#commonevent_errcode): Failed to allocate memory.

 |

#### \[h2\]OH\_CommonEvent\_UnSubscribe()

CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)

**Description**

Unsubscribes from a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](#commonevent_errcode): Failed to send IPC requests.

[COMMONEVENT\_ERR\_INIT\_UNDONE](#commonevent_errcode): The common event service is not initialized.

 |

#### \[h2\]OH\_CommonEvent\_GetEventFromRcvData()

const char\* OH\_CommonEvent\_GetEventFromRcvData(const CommonEvent\_RcvData\* rcvData)

**Description**

Obtains the name of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md)\* rcvData | Pointer to the callback data of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Event name obtained. |

#### \[h2\]OH\_CommonEvent\_GetCodeFromRcvData()

int32\_t OH\_CommonEvent\_GetCodeFromRcvData(const CommonEvent\_RcvData\* rcvData)

**Description**

Obtains the result code (integer type) of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md)\* rcvData | Pointer to the callback data of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Result code obtained. |

#### \[h2\]OH\_CommonEvent\_GetDataStrFromRcvData()

const char\* OH\_CommonEvent\_GetDataStrFromRcvData(const CommonEvent\_RcvData\* rcvData)

**Description**

Obtains the result data (string type) of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md)\* rcvData | Pointer to the callback data of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Result data obtained. |

#### \[h2\]OH\_CommonEvent\_GetBundleNameFromRcvData()

const char\* OH\_CommonEvent\_GetBundleNameFromRcvData(const CommonEvent\_RcvData\* rcvData)

**Description**

Obtains the bundle name of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md)\* rcvData | Pointer to the callback data of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Bundle name obtained. |

#### \[h2\]OH\_CommonEvent\_GetParametersFromRcvData()

const CommonEvent\_Parameters\* OH\_CommonEvent\_GetParametersFromRcvData(const CommonEvent\_RcvData\* rcvData)

**Description**

Obtains the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_RcvData](../../structs/commonevent-rcvdata/document.md)\* rcvData | Pointer to the callback data of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables) \* | Additional information obtained. |

#### \[h2\]OH\_CommonEvent\_CreatePublishInfo()

CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)

**Description**

Creates a property object of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| bool ordered | 
Whether the common event is an ordered one.

\- **true**: ordered common event.

\- **false**: unordered common event.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* | Returns the property object if the operation is successful; returns **null** otherwise. |

#### \[h2\]OH\_CommonEvent\_DestroyPublishInfo()

void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)

**Description**

Destroys a property object of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of the common event to destroy. |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoBundleName()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoBundleName(CommonEvent\_PublishInfo\* info, const char\* bundleName)

**Description**

Sets the bundle name of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |
| const char\* bundleName | Pointer to the bundle name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoPermissions()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoPermissions(CommonEvent\_PublishInfo\* info,const char\* permissions\[\], int32\_t num)

**Description**

Sets permissions for a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |
| const char\* permissions\[\] | Pointer to the array of permission names. The valid number of permissions is the smaller value between **num** and **permissions\[\]**. |
| int32\_t num | Number of permissions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoCode()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoCode(CommonEvent\_PublishInfo\* info, int32\_t code)

**Description**

Sets the result code (integer type) of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |
| int32\_t code | Result code to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoData()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoData(CommonEvent\_PublishInfo\* info,const char\* data, size\_t length)

**Description**

Sets the result data (string type) of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |
| const char\* data | Pointer to the result data to set. The valid data length is the smaller value between **length** and **data**. |
| size\_t length | Length of the result data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_SetPublishInfoParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoParameters(CommonEvent\_PublishInfo\* info,CommonEvent\_Parameters\* param)

**Description**

Sets the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |
| CommonEvent\_Parameters\* param | Pointer to the additional information to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_CreateParameters()

CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()

**Description**

Creates an additional information object of a common event.

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* | Returns additional information of the common event if operation is successful; returns **null** otherwise. |

#### \[h2\]OH\_CommonEvent\_DestroyParameters()

void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)

**Description**

Destroys the additional information object of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information to destroy. |

#### \[h2\]OH\_CommonEvent\_HasKeyInParameters()

bool OH\_CommonEvent\_HasKeyInParameters(const CommonEvent\_Parameters\* para, const char\* key)

**Description**

Checks whether the additional information of a common event contains a KV pair.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information to check. |
| const char\* key | Pointer to the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Returns the check result.

\- **true**: The key exists.

\- **false**: The key does not exist.

 |

#### \[h2\]OH\_CommonEvent\_GetIntFromParameters()

int OH\_CommonEvent\_GetIntFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const int defaultValue)

**Description**

Obtains the int data with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const int defaultValue | Default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | The int data obtained. |

#### \[h2\]OH\_CommonEvent\_SetIntToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetIntToParameters(CommonEvent\_Parameters\* param, const char\* key, int value)

**Description**

Sets the int data with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| int value | The int data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetIntArrayFromParameters()

int32\_t OH\_CommonEvent\_GetIntArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, int\*\* array)

**Description**

Obtains the int array with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| int\*\* array | Double pointer to the int array to obtain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Length of the array obtained. The default value is **0**. |

#### \[h2\]OH\_CommonEvent\_SetIntArrayToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetIntArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const int\* value, size\_t num)

**Description**

Sets the int array with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const int\* value | The int array to set. |
| size\_t num | Number of elements in the int array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](#commonevent_errcode): Failed to allocate memory.

 |

#### \[h2\]OH\_CommonEvent\_GetLongFromParameters()

long OH\_CommonEvent\_GetLongFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const long defaultValue)

**Description**

Obtains the long data with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const long defaultValue | Default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| long | The long data obtained. |

#### \[h2\]OH\_CommonEvent\_SetLongToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetLongToParameters(CommonEvent\_Parameters\* param, const char\* key, long value)

**Description**

Sets the long data with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| long value | The long data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetLongArrayFromParameters()

int32\_t OH\_CommonEvent\_GetLongArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, long\*\* array)

**Description**

Obtains the long array with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| long\*\* array | Double pointer to the long array to obtain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Length of the array obtained. The default value is **0**. |

#### \[h2\]OH\_CommonEvent\_SetLongArrayToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetLongArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const long\* value, size\_t num)

**Description**

Sets the long array for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const long\* value | Pointer to the long array to set. |
| size\_t num | Number of elements in the long array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](#commonevent_errcode): Failed to allocate memory.

 |

#### \[h2\]OH\_CommonEvent\_GetBoolFromParameters()

bool OH\_CommonEvent\_GetBoolFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const bool defaultValue)

**Description**

Obtains the Boolean data with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const bool defaultValue | Default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | The Boolean data obtained. |

#### \[h2\]OH\_CommonEvent\_SetBoolToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolToParameters(CommonEvent\_Parameters\* param, const char\* key, bool value)

**Description**

Sets the Boolean data with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| bool value | The Boolean data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetBoolArrayFromParameters()

int32\_t OH\_CommonEvent\_GetBoolArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, bool\*\* array)

**Description**

Obtains the Boolean array with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| bool\*\* array | Double pointer to the Boolean array to obtain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Length of the array obtained. The default value is **0**. |

#### \[h2\]OH\_CommonEvent\_SetBoolArrayToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const bool\* value, size\_t num)

**Description**

Sets the Boolean array with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const bool\* value | Pointer to the Boolean array to set. |
| size\_t num | Number of elements in the Boolean array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](#commonevent_errcode): Failed to allocate memory.

 |

#### \[h2\]OH\_CommonEvent\_GetCharFromParameters()

char OH\_CommonEvent\_GetCharFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const char defaultValue)

**Description**

Obtains the character data with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const char defaultValue | Default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| char | The character data obtained. |

#### \[h2\]OH\_CommonEvent\_SetCharToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetCharToParameters(CommonEvent\_Parameters\* param, const char\* key, char value)

**Description**

Sets the character data with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| char value | The character data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetCharArrayFromParameters()

int32\_t OH\_CommonEvent\_GetCharArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, char\*\* array)

**Description**

Obtains the character array with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| char\*\* array | Double pointer to the character array to obtain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Length of the array obtained. The default value is **0**. |

#### \[h2\]OH\_CommonEvent\_SetCharArrayToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetCharArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const char\* value, size\_t num)

**Description**

Sets the character array with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const char\* value | Pointer to the character array to set. |
| size\_t num | Number of elements in the character array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetDoubleFromParameters()

double OH\_CommonEvent\_GetDoubleFromParameters(const CommonEvent\_Parameters\* para, const char\* key,const double defaultValue)

**Description**

Obtains the double data with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const double defaultValue | Default value. |

**Returns**

| Type | Description |
| :-- | :-- |
| double | The double data obtained. |

#### \[h2\]OH\_CommonEvent\_SetDoubleToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleToParameters(CommonEvent\_Parameters\* param, const char\* key,double value)

**Description**

Sets the double data with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| double value | The double data to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

 |

#### \[h2\]OH\_CommonEvent\_GetDoubleArrayFromParameters()

int32\_t OH\_CommonEvent\_GetDoubleArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key,double\*\* array)

**Description**

Obtains the double array with a specific key from the additional information of a common event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Parameters](#variables)\* para | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| double\*\* array | Double pointer to the double array to obtain. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Length of the array obtained. The default value is **0**. |

#### \[h2\]OH\_CommonEvent\_SetDoubleArrayToParameters()

CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const double\* value, size\_t num)

**Description**

Sets the double array with a specific key for the additional information of a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Parameters](#variables)\* param | Pointer to the additional information of a common event. |
| const char\* key | Pointer to the key. |
| const double\* value | Pointer to the double array to set. |
| size\_t num | Number of elements in the double array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](#commonevent_errcode): Failed to allocate memory.

 |

#### \[h2\]OH\_CommonEvent\_Publish()

CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)

**Description**

Publishes a common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* event | Pointer to the name of the common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](#commonevent_errcode): Event sending frequency is too high.

[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](#commonevent_errcode): Failed to send IPC requests.

[COMMONEVENT\_ERR\_INIT\_UNDONE](#commonevent_errcode): The common event service is not initialized.

 |

#### \[h2\]OH\_CommonEvent\_PublishWithInfo()

CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)

**Description**

Publishes a common event with specified properties.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* event | Pointer to the name of the common event. |
| const [CommonEvent\_PublishInfo](../../structs/commonevent-publishinfo/document.md)\* info | Pointer to the property object of a common event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CommonEvent\_ErrCode](#commonevent_errcode) | 
Returns an execution result.

[COMMONEVENT\_ERR\_OK](#commonevent_errcode): Operation is successful.

[COMMONEVENT\_ERR\_INVALID\_PARAMETER](#commonevent_errcode): The parameter is invalid.

[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](#commonevent_errcode): Event sending frequency is too high.

[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](#commonevent_errcode): Failed to send IPC requests.

[COMMONEVENT\_ERR\_INIT\_UNDONE](#commonevent_errcode): The common event service is not initialized.

 |

#### \[h2\]OH\_CommonEvent\_IsOrderedCommonEvent()

bool OH\_CommonEvent\_IsOrderedCommonEvent(const CommonEvent\_Subscriber\* subscriber)

**Description**

Checks whether a common event is an ordered one.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the common event is an ordered one; returns **false** if the common event is an unordered one. |

#### \[h2\]OH\_CommonEvent\_FinishCommonEvent()

bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)

**Description**

Finishes an ordered common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the operation is successful; returns **false** otherwise. |

#### \[h2\]OH\_CommonEvent\_GetAbortCommonEvent()

bool OH\_CommonEvent\_GetAbortCommonEvent(const CommonEvent\_Subscriber\* subscriber)

**Description**

Checks whether an ordered common event is aborted.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the ordered common event is in the abort state; returns **false** otherwise. |

#### \[h2\]OH\_CommonEvent\_AbortCommonEvent()

bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)

**Description**

Aborts an ordered common event when used with [OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent). After the abort, the common event is not sent to the next subscriber.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the operation is successful; returns **false** otherwise. |

#### \[h2\]OH\_CommonEvent\_ClearAbortCommonEvent()

bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)

**Description**

Clears the abort state of an ordered common event when used with [OH\_CommonEvent\_FinishCommonEvent](#oh_commonevent_finishcommonevent). After the clearance, the common event is sent to the next subscriber.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the operation is successful; returns **false** otherwise. |

#### \[h2\]OH\_CommonEvent\_GetCodeFromSubscriber()

int32\_t OH\_CommonEvent\_GetCodeFromSubscriber(const CommonEvent\_Subscriber\* subscriber)

**Description**

Obtains the result code (integer type) of an ordered common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the result code obtained if the operation is successful; returns **0** otherwise. |

#### \[h2\]OH\_CommonEvent\_SetCodeToSubscriber()

bool OH\_CommonEvent\_SetCodeToSubscriber(CommonEvent\_Subscriber\* subscriber, int32\_t code)

**Description**

Sets the result code (integer type) of an ordered common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |
| int32\_t code | Result code to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the operation is successful; returns **false** otherwise. |

#### \[h2\]OH\_CommonEvent\_GetDataFromSubscriber()

const char\* OH\_CommonEvent\_GetDataFromSubscriber(const CommonEvent\_Subscriber\* subscriber)

**Description**

Obtains the result data (string type) of an ordered common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns the result data obtained if the operation is successful; returns **null** otherwise. |

#### \[h2\]OH\_CommonEvent\_SetDataToSubscriber()

bool OH\_CommonEvent\_SetDataToSubscriber(CommonEvent\_Subscriber\* subscriber, const char\* data, size\_t length)

**Description**

Sets the result data (string type) of an ordered common event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [CommonEvent\_Subscriber](#variables)\* subscriber | Pointer to the common event subscriber. |
| const char\* data | Pointer to the result data to set. The valid data length is the smaller value between **length** and **data**. |
| size\_t length | Data length. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the operation is successful; returns **false** otherwise. |
