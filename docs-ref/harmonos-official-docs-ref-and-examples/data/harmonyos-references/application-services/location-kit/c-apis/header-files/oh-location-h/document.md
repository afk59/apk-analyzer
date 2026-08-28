# oh\_location.h

#### Overview

Defines APIs for querying the location switch status, and starting and stopping location.

**File to include**: <LocationKit/oh\_location.h>

**Library**: liblocation\_ndk.so

**System capability**: SystemCapability.Location.Location.Core

**Since**: 13

**Related module**: \[Location\] (capi-location.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Location\_ResultCode OH\_Location\_IsLocatingEnabled(bool\* enabled)](#oh_location_islocatingenabled) | Checks whether the location switch is enabled. |
| [Location\_ResultCode OH\_Location\_StartLocating(const Location\_RequestConfig\* requestConfig)](#oh_location_startlocating) | Starts the location process and subscribes to location changes. |
| [Location\_ResultCode OH\_Location\_StopLocating(const Location\_RequestConfig\* requestConfig)](#oh_location_stoplocating) | Stops the location process and unsubscribes from location changes. |

#### Function Description

#### \[h2\]OH\_Location\_IsLocatingEnabled()

Location\_ResultCode OH\_Location\_IsLocatingEnabled(bool\* enabled)

**Description**

Checks whether the location switch is enabled.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| bool\* enabled | 
Pointer of the bool type, which is used to receive the location switch status.

If the value is **true**, the location switch is enabled. If the value is **false**, the location switch is disabled.

A null pointer is prohibited. If a null pointer is passed in, an error is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode) | 
Operation result. For details, see [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode).

[LOCATION\_SUCCESS](../oh-location-type-h/document.md#location_resultcode) if the location switch status is queried successfully;

[LOCATION\_INVALID\_PARAM](../oh-location-type-h/document.md#location_resultcode) if the input parameter is a null pointer;

[LOCATION\_SERVICE\_UNAVAILABLE](../oh-location-type-h/document.md#location_resultcode) if the location service is abnormal.

 |

#### \[h2\]OH\_Location\_StartLocating()

Location\_ResultCode OH\_Location\_StartLocating(const Location\_RequestConfig\* requestConfig)

**Description**

Starts the location process and subscribes to location changes.

**Required permission**: ohos.permission.APPROXIMATELY\_LOCATION

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [const Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the **Location\_RequestConfig** instance, which can be created using [OH\_Location\_CreateRequestConfig](../oh-location-type-h/document.md#oh_location_createrequestconfig). This parameter is used to specify the location scene and location reporting interval.

For details, see [Location\_RequestConfig](../../structs/location-requestconfig/document.md).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode) | 
Operation result. For details, see [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode).

[LOCATION\_SUCCESS](../oh-location-type-h/document.md#location_resultcode) if the location process is started successfully;

[LOCATION\_INVALID\_PARAM](../oh-location-type-h/document.md#location_resultcode) if the input **requestConfig** is a null pointer;

[LOCATION\_PERMISSION\_DENIED](../oh-location-type-h/document.md#location_resultcode) if the permission verification failed;

[LOCATION\_NOT\_SUPPORTED](../oh-location-type-h/document.md#location_resultcode) if the device does not support this function;

[LOCATION\_SERVICE\_UNAVAILABLE](../oh-location-type-h/document.md#location_resultcode) if the location service is abnormal;

[LOCATION\_SWITCH\_OFF](../oh-location-type-h/document.md#location_resultcode) if the location switch is disabled.

 |

#### \[h2\]OH\_Location\_StopLocating()

Location\_ResultCode OH\_Location\_StopLocating(const Location\_RequestConfig\* requestConfig)

**Description**

Stops the location process and unsubscribes from location changes.

**Required permission**: ohos.permission.APPROXIMATELY\_LOCATION

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [const Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the **Location\_RequestConfig** instance.

The value of this parameter must be the same as the pointer to **requestConfig** in [OH\_Location\_StartLocating](#oh_location_startlocating).

For details, see [Location\_RequestConfig](../../structs/location-requestconfig/document.md).

A null pointer is prohibited. If a null pointer is passed in, an error is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode) | 
Operation result. For details, see [Location\_ResultCode](../oh-location-type-h/document.md#location_resultcode).

[LOCATION\_SUCCESS](../oh-location-type-h/document.md#location_resultcode) if the location process is stopped successfully;

[LOCATION\_INVALID\_PARAM](../oh-location-type-h/document.md#location_resultcode) if the input parameter is a null pointer,

2\. or the input parameter is different from the pointer to **requestConfig** in [OH\_Location\_StartLocating](#oh_location_startlocating);

[LOCATION\_PERMISSION\_DENIED](../oh-location-type-h/document.md#location_resultcode) if the permission verification failed;

[LOCATION\_NOT\_SUPPORTED](../oh-location-type-h/document.md#location_resultcode) if the device does not support this function;

[LOCATION\_SERVICE\_UNAVAILABLE](../oh-location-type-h/document.md#location_resultcode) if the location service is abnormal;

[LOCATION\_SWITCH\_OFF](../oh-location-type-h/document.md#location_resultcode) if the location switch is disabled.

 |
