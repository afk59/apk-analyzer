# time\_service.h

#### Overview

Declares the APIs for obtaining the time and time zone.

**Library**: libtime\_service\_ndk.so

**File to include**: <BasicServicesKit/time\_service.h>

**System capability**: SystemCapability.MiscServices.Time

**Since**: 12

**Related module**: [TimeService](../../modules/timeservice/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [TimeService\_ErrCode](#timeservice_errcode) | TimeService\_ErrCode | Enumerates the error codes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [TimeService\_ErrCode OH\_TimeService\_GetTimeZone(char \*timeZone, uint32\_t len)](#oh_timeservice_gettimezone) | Obtains the current system time zone. |

#### Enum Description

#### \[h2\]TimeService\_ErrCode

enum TimeService\_ErrCode

**Description**

Enumerates the error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| TIMESERVICE\_ERR\_OK = 0 | Operation successful. |
| TIMESERVICE\_ERR\_INTERNAL\_ERROR = 13000001 | Failed to obtain system parameters. |
| TIMESERVICE\_ERR\_INVALID\_PARAMETER = 13000002 | Invalid parameter. |

#### Function Description

#### \[h2\]OH\_TimeService\_GetTimeZone()

TimeService\_ErrCode OH\_TimeService\_GetTimeZone(char \*timeZone, uint32\_t len)

**Description**

Obtains the current system time zone.

**System capability**: SystemCapability.MiscServices.Time

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*timeZone | Pointer to the string array of time zone IDs. If the timezone is obtained, its ID is written. Otherwise, an empty string is written. The string ends with **\\0**. |
| uint32\_t len | Length of a string array of time zone IDs without maximum limit. You are advised to apply for sufficient memory for at least 31 bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [TimeService\_ErrCode](#timeservice_errcode) | 
Returns **TIMESERVICE\_ERR\_OK** if the operation is successful;

returns **TIMESERVICE\_ERR\_INTERNAL\_ERROR** if the system parameters fail to be obtained;

returns **TIMESERVICE\_ERR\_INVALID\_PARAMETER** if **timeZone** is a null pointer or the length of the time zone name (excluding the end character **\\0**) is greater than or equal to the value of **len**.

 |
