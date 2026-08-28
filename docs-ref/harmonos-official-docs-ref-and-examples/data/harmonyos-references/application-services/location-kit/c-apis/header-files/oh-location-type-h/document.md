# oh\_location\_type.h

#### Overview

Defines common attributes of the location service.

**Reference file**: <LocationKit/oh\_location\_type.h>

**Library**: liblocation\_ndk.so

**System capability**: SystemCapability.Location.Location.Core

**Since**: 13

**Related module**: \[Location\] (capi-location.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Location\_BasicInfo](../../structs/location-basicinfo/document.md) | Location\_BasicInfo | Defines the struct for the basic location information. |
| [Location\_Info](../../structs/location-info/document.md) | Location\_Info | Defines the struct for the location information. |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md) | Location\_RequestConfig | Defines the struct for the location request configuration. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Location\_ResultCode](#location_resultcode) | Location\_ResultCode | Enumerates error codes of the location service. |
| [Location\_UseScene](#location_usescene) | Location\_UseScene | Enumerates use scenes in a location request. |
| [Location\_PowerConsumptionScene](#location_powerconsumptionscene) | Location\_PowerConsumptionScene | Enumerates power consumption scenarios in a location request. |
| [Location\_SourceType](#location_sourcetype) | Location\_SourceType | Defines the source of location information. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Location\_BasicInfo OH\_LocationInfo\_GetBasicInfo(Location\_Info\* location)](#oh_locationinfo_getbasicinfo) | \- | Obtains basic location information. |
| [Location\_ResultCode OH\_LocationInfo\_GetAdditionalInfo(Location\_Info\* location, char\* additionalInfo, uint32\_t length)](#oh_locationinfo_getadditionalinfo) | \- | Obtains the additional information in the location information. |
| [typedef void (\*Location\_InfoCallback)(Location\_Info\* location, void\* userData)](#location_infocallback) | Location\_InfoCallback | Defines the callback for receiving reported location information. |
| [Location\_RequestConfig\* OH\_Location\_CreateRequestConfig(void)](#oh_location_createrequestconfig) | \- | Creates a **Location\_RequestConfig** instance. |
| [void OH\_Location\_DestroyRequestConfig(Location\_RequestConfig\* requestConfig)](#oh_location_destroyrequestconfig) | \- | Destroys the **Location\_RequestConfig** instance and reclaims the memory. |
| [void OH\_LocationRequestConfig\_SetUseScene(Location\_RequestConfig\* requestConfig, Location\_UseScene useScene)](#oh_locationrequestconfig_setusescene) | \- | 
Sets the use scene in the location request configuration.

**useScene** takes precedence over **powerConsumptionScene** in [Location\_RequestConfig](../../structs/location-requestconfig/document.md).

If **useScene** is set, **powerConsumptionScene** is invalid.

Otherwise, **powerConsumptionScene** takes effect.

If neither of the two parameters is set, the default value of **useScene** is [LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](#location_usescene) and **powerConsumptionScene** is invalid.

 |
| [void OH\_LocationRequestConfig\_SetPowerConsumptionScene(Location\_RequestConfig\* requestConfig, Location\_PowerConsumptionScene powerConsumptionScene)](#oh_locationrequestconfig_setpowerconsumptionscene) | \- | Sets the power consumption scene in the location request configuration. |
| [void OH\_LocationRequestConfig\_SetInterval(Location\_RequestConfig\* requestConfig, int interval)](#oh_locationrequestconfig_setinterval) | \- | Sets the location reporting interval in the location request configuration. |
| [void OH\_LocationRequestConfig\_SetCallback(Location\_RequestConfig\* requestConfig, Location\_InfoCallback callback, void\* userData)](#oh_locationrequestconfig_setcallback) | \- | Sets the callback function. |

#### Enum Description

#### \[h2\]Location\_ResultCode

enum Location\_ResultCode

**Description**

Enumerates error codes of the location service.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| LOCATION\_SUCCESS = 0 | Operation success. |
| LOCATION\_PERMISSION\_DENIED = 201 | Permission denied. |
| LOCATION\_INVALID\_PARAM = 401 | 
The parameter is invalid.

Possible causes: 1. The input parameter is a null pointer. 2. The parameter value is out of the value range.

 |
| LOCATION\_NOT\_SUPPORTED = 801 | Function not supported. due to limited device capabilities. |
| LOCATION\_SERVICE\_UNAVAILABLE = 3301000 | Location service unavailable. |
| LOCATION\_SWITCH\_OFF = 3301100 | Location switch disabled. |

#### \[h2\]Location\_UseScene

enum Location\_UseScene

**Description**

Enumerates use scenes in a location request.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| LOCATION\_USE\_SCENE\_NAVIGATION = 0x0401 | 
Navigation scenario.

This option is applicable when your application needs to obtain the real-time location of a mobile device outdoors, such as navigation for driving or walking.

This option mainly uses the GNSS positioning technology and therefore the power consumption is relatively high.

 |
| LOCATION\_USE\_SCENE\_SPORT = 0x0402 | 

Sport scenario.

Applicable when your application needs to record user trajectories, for example, the track recording function of sports applications.

This option mainly uses the GNSS positioning technology and therefore the power consumption is relatively high.

 |
| LOCATION\_USE\_SCENE\_TRANSPORT = 0x0403 | 

Travel scenario.

This option is applicable to user travel scenarios, such as taxi hailing and public transportation.

This option mainly uses the GNSS positioning technology and therefore the power consumption is relatively high.

 |
| LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE = 0x0404 | 

Daily life services.

This option is applicable when your application only needs the approximate location in scenarios such as when the user is browsing news, shopping online, and ordering food.

It mainly uses the network positioning technology and therefore the power consumption is relatively low.

 |

#### \[h2\]Location\_PowerConsumptionScene

enum Location\_PowerConsumptionScene

**Description**

Enumerates power consumption scenarios in a location request.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| LOCATION\_HIGH\_POWER\_CONSUMPTION = 0x0601 | 
High power consumption.

The mode mainly uses the GNSS positioning technology. The system uses the network positioning technology as an alternative to provide the location service for your application until the GNSS can provide stable location results.

During the continuous location process, the network positioning technology is used if the GNSS location result cannot be obtained within 30 seconds.

This policy can lead to significant hardware resource consumption and power consumption.

 |
| LOCATION\_LOW\_POWER\_CONSUMPTION = 0x0602 | 

Low power consumption.

This mode is applicable when your application only needs the approximate location in scenarios such as when the user is browsing news, shopping online, and ordering food.

It mainly uses the network positioning technology and therefore the power consumption is relatively low.

 |
| LOCATION\_NO\_POWER\_CONSUMPTION = 0x0603 | 

No power consumption.

Your application does not proactively start the location service. When responding to another application requesting the same location service, the system marks a copy of the location result to your application.

 |

#### \[h2\]Location\_SourceType

enum Location\_SourceType

**Description**

Defines the source of location information.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| LOCATION\_SOURCE\_TYPE\_GNSS = 1 | GNSS positioning technology. |
| LOCATION\_SOURCE\_TYPE\_NETWORK = 2 | Network positioning technology. |
| LOCATION\_SOURCE\_TYPE\_INDOOR = 3 | Indoor high-precision positioning technology. |
| LOCATION\_SOURCE\_TYPE\_RTK = 4 | Outdoor high-precision positioning technology. |

#### Function Description

#### \[h2\]OH\_LocationInfo\_GetBasicInfo()

Location\_BasicInfo OH\_LocationInfo\_GetBasicInfo(Location\_Info\* location)

**Description**

Obtains basic location information.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_Info](../../structs/location-info/document.md)\* location | 
Pointer to the [Location\_Info](../../structs/location-info/document.md) instance.

A non-null pointer must be passed. The pointer can be obtained from [Location\_InfoCallback](#location_infocallback).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_BasicInfo](../../structs/location-basicinfo/document.md) | Struct for the basic location information. For details, see [Location\_BasicInfo](../../structs/location-basicinfo/document.md). |

#### \[h2\]OH\_LocationInfo\_GetAdditionalInfo()

Location\_ResultCode OH\_LocationInfo\_GetAdditionalInfo(Location\_Info\* location, char\* additionalInfo, uint32\_t length)

**Description**

Obtains the additional information in the location information.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_Info](../../structs/location-info/document.md)\* location | 
Pointer to the [Location\_Info](../../structs/location-info/document.md) instance.

A non-null pointer needs to be passed in. This pointer can be obtained from [Location\_InfoCallback](#location_infocallback).

 |
| char\* additionalInfo | 

Non-null pointer of the char type. This variable is used to store the additional location information in JSON format.

The pointer and the corresponding memory are created by the caller. It is recommended that the memory be greater than or equal to 256 bytes.

If a null pointer is passed in, an error code is returned.

 |
| uint32\_t length | Memory size of **additionalInfo**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_ResultCode](#location_resultcode) | 
Operation result. For details, see [Location\_ResultCode](#location_resultcode).

[LOCATION\_SUCCESS](#location_resultcode) if additional information obtained successfully;

[LOCATION\_INVALID\_PARAM](#location_resultcode) if the input **location** or **additionalInfo** is a null pointer,

2\. or the value of the input **length** is too small, that is, the memory size of **additionalInfo** is too small, which is unable to save the complete additional information.

 |

#### \[h2\]Location\_InfoCallback()

typedef void (\*Location\_InfoCallback)(Location\_Info\* location, void\* userData)

**Description**

Defines the callback for receiving reported location information.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_Info](../../structs/location-info/document.md)\* location | 
Pointer to the [Location\_Info](../../structs/location-info/document.md) instance, which carries the latest location information.

The memory occupied by the instance will be reclaimed when [Location\_InfoCallback](#location_infocallback) is complete. Before that, call APIs such as [OH\_LocationInfo\_GetBasicInfo](#oh_locationinfo_getbasicinfo) to obtain the location information.

 |
| void\* userData | Pointer to the **userData** struct or object. This parameter is passed in through [OH\_LocationRequestConfig\_SetCallback](#oh_locationrequestconfig_setcallback). |

#### \[h2\]OH\_Location\_CreateRequestConfig()

Location\_RequestConfig\* OH\_Location\_CreateRequestConfig(void)

**Description**

Creates a **Location\_RequestConfig** instance.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [Location\_RequestConfig\*](../../structs/location-requestconfig/document.md) | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance.

If **NULL** is returned, the operation has failed. The probable cause is that the application address space is full.

 |

#### \[h2\]OH\_Location\_DestroyRequestConfig()

void OH\_Location\_DestroyRequestConfig(Location\_RequestConfig\* requestConfig)

**Description**

Destroys the **Location\_RequestConfig** instance and reclaims the memory.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance,

which is created using [OH\_Location\_CreateRequestConfig](#oh_location_createrequestconfig).

 |

#### \[h2\]OH\_LocationRequestConfig\_SetUseScene()

void OH\_LocationRequestConfig\_SetUseScene(Location\_RequestConfig\* requestConfig, Location\_UseScene useScene)

**Description**

Sets the use scene in the location request configuration.

**useScene** takes precedence over **powerConsumptionScene** in [Location\_RequestConfig](../../structs/location-requestconfig/document.md).

If **useScene** is set, **powerConsumptionScene** is invalid.

Otherwise, **powerConsumptionScene** takes effect.

If neither of the two parameters is set, the default value of **useScene** is [LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](#location_usescene) and **powerConsumptionScene** is invalid.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance,

which is created using [OH\_Location\_CreateRequestConfig](#oh_location_createrequestconfig).

 |
| [Location\_UseScene](#location_usescene) useScene | 

Use scene in the location request.

The default value is [LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](#location_usescene).

For details, see [Location\_UseScene](#location_usescene).

 |

#### \[h2\]OH\_LocationRequestConfig\_SetPowerConsumptionScene()

void OH\_LocationRequestConfig\_SetPowerConsumptionScene(Location\_RequestConfig\* requestConfig, Location\_PowerConsumptionScene powerConsumptionScene)

**Description**

Sets the power consumption scene in the location request configuration.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance,

which is created using [OH\_Location\_CreateRequestConfig](#oh_location_createrequestconfig).

 |
| [Location\_PowerConsumptionScene](#location_powerconsumptionscene) powerConsumptionScene | 

Power consumption scene in the location request.

The default value is [LOCATION\_LOW\_POWER\_CONSUMPTION](#location_powerconsumptionscene).

For details, see [Location\_PowerConsumptionScene](#location_powerconsumptionscene).

 |

#### \[h2\]OH\_LocationRequestConfig\_SetInterval()

void OH\_LocationRequestConfig\_SetInterval(Location\_RequestConfig\* requestConfig, int interval)

**Description**

Sets the location reporting interval in the location request configuration.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance,

which is created using [OH\_Location\_CreateRequestConfig](#oh_location_createrequestconfig).

 |
| int interval | Location reporting interval, in seconds. The value must be greater than or equal to **1**. The default value is **1**. |

#### \[h2\]OH\_LocationRequestConfig\_SetCallback()

void OH\_LocationRequestConfig\_SetCallback(Location\_RequestConfig\* requestConfig, Location\_InfoCallback callback, void\* userData)

**Description**

Sets a callback for sign generation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Location\_RequestConfig](../../structs/location-requestconfig/document.md)\* requestConfig | 
Pointer to the [Location\_RequestConfig](../../structs/location-requestconfig/document.md) instance,

which is created using [OH\_Location\_CreateRequestConfig](#oh_location_createrequestconfig).

 |
| [Location\_InfoCallback](#location_infocallback) callback | 

Pointer to the callback function, which is used to receive location information changes.

For details, see [Location\_InfoCallback](#location_infocallback).

 |
| void\* userData | Pointer to the **userData** struct or object. This pointer is returned to the caller as an input parameter when the callback function is executed. |
