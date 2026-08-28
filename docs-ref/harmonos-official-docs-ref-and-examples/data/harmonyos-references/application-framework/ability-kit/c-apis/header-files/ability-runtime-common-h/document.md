# ability\_runtime\_common.h

#### Overview

The file declares the error codes of the AbilityRuntime module.

**File to include**: <AbilityKit/ability\_runtime/ability\_runtime\_common.h>

**Library**: libability\_runtime.so

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 13

**Related module**: [AbilityRuntime](../../modules/abilityruntime/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AbilityRuntime\_ErrorCode](#abilityruntime_errorcode) | AbilityRuntime\_ErrorCode | Enumerates the error codes of the AbilityRuntime module. |

#### Enum Description

#### \[h2\]AbilityRuntime\_ErrorCode

enum AbilityRuntime\_ErrorCode

**Description**

Enumerates the error codes of the AbilityRuntime module.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR = 0 | Operation successful. |
| ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED = 201 | 
Permission verification fails.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID = 401 | Invalid parameter. |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED = 801 | 

The device type is not supported.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY = 16000001 | 

The specified ability name does not exist.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE = 16000002 | 

The ability type is incorrect.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED = 16000008 | 

The crowdtesting application expires.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE = 16000009 | 

An ability cannot be started or stopped in Wukong mode.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST = 16000011 | The context does not exist. |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED = 16000012 | 

The application is under control.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED = 16000013 | 

The application is under control by EDM.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP = 16000018 | 

Redirection to third-party applications is not allowed in API versions later than 11.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL = 16000050 | 

Internal server error.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY = 16000053 | 

The application is not on top.

**Since**: 15

 |
| ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED = 16000067 | 

Setting the window visibility during startup is not allowed.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED = 16000072 | 

The application does not support clone or multi-instance mode.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY = 16000076 | 

The multi-instance key is invalid.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED = 16000077 | 

The number of instances has reached the upper limit.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED = 16000078 | 

The application does not support multi-instance mode.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED = 16000079 | 

Setting **APP\_INSTANCE\_KEY** is not supported.

**Since**: 17

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_GET\_APPLICATION\_INFO\_FAILED = 16000081 | 

Failed to obtain the application information.

**Since**: 21

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_START\_TIMEOUT = 16000133 | 

Starting the UIAbility times out.

**Since**: 21

 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED = 16000134 | 

The function cannot be called on the main thread of the application.

**Since**: 21

 |
