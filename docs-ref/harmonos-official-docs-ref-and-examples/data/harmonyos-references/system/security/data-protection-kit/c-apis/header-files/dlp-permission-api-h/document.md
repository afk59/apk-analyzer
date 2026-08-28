# dlp\_permission\_api.h

#### Overview

Defines the APIs for cross-device file access management, encrypted storage, and access authorization.

**Library**: libohdlp\_permission.so

**File to include**: <DataProtectionKit/dlp\_permission\_api.h>

**System capability**: SystemCapability.Security.DataLossPrevention

**Since**: 14

**Related module**: [DlpPermissionApi](../../modules/dlppermissionapi/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | DLP\_ErrCode | Enumerates the DLP error codes. |
| [DLP\_FileAccess](#dlp_fileaccess) | DLP\_FileAccess | Enumerates the permissions on a DLP file. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [DLP\_ErrCode OH\_DLP\_GetDlpPermissionInfo(DLP\_FileAccess \*dlpFileAccess, uint32\_t \*flags)](#oh_dlp_getdlppermissioninfo) | Obtains the permission information of this DLP file. |
| [DLP\_ErrCode OH\_DLP\_GetOriginalFileName(const char \*fileName, char \*originalFileName)](#oh_dlp_getoriginalfilename) | Obtains the original file name of a DLP file. |
| [DLP\_ErrCode OH\_DLP\_IsInSandbox(bool \*isInSandbox)](#oh_dlp_isinsandbox) | Checks whether this application is running in a DLP sandbox environment. |
| [DLP\_ErrCode OH\_DLP\_SetSandboxAppConfig(const char \*configInfo)](#oh_dlp_setsandboxappconfig) | Sets sandbox application configuration. |
| [DLP\_ErrCode OH\_DLP\_GetSandboxAppConfig(char \*configInfo)](#oh_dlp_getsandboxappconfig) | Obtains the sandbox application configuration. |
| [DLP\_ErrCode OH\_DLP\_CleanSandboxAppConfig()](#oh_dlp_cleansandboxappconfig) | Cleans the sandbox application configuration. |

#### Enum Description

#### \[h2\]DLP\_ErrCode

enum DLP\_ErrCode

**Description**

Enumerates the DLP error codes.

**Since**: 14

| Enum | Description |
| :-- | :-- |
| ERR\_OH\_SUCCESS = 0 | The operation is successful. |
| ERR\_OH\_INVALID\_PARAMETER = 19100001 | Invalid parameters are specified. |
| ERR\_OH\_API\_ONLY\_FOR\_SANDBOX = 19100006 | The caller is not a DLP sandbox application. |
| ERR\_OH\_API\_NOT\_FOR\_SANDBOX = 19100007 | The API is not available to a DLP sandbox application. |
| ERR\_OH\_SYSTEM\_SERVICE\_EXCEPTION = 19100011 | The system service is abnormal. |
| ERR\_OH\_OUT\_OF\_MEMORY = 19100012 | The memory allocation fails. |
| ERR\_OH\_APPLICATION\_NOT\_AUTHORIZED = 19100018 | The application is not authorized to perform the operation. |

#### \[h2\]DLP\_FileAccess

enum DLP\_FileAccess

**Description**

Enumerates the permissions on a DLP file.

**Since**: 14

| Enum | Description |
| :-- | :-- |
| NO\_PERMISSION = 0 | No permission on the file. |
| READ\_ONLY = 1 | Read-only permission. |
| CONTENT\_EDIT = 2 | Editing permission. |
| FULL\_CONTROL = 3 | Full control. |

#### Function Description

#### \[h2\]OH\_DLP\_GetDlpPermissionInfo()

DLP\_ErrCode OH\_DLP\_GetDlpPermissionInfo(DLP\_FileAccess \*dlpFileAccess, uint32\_t \*flags)

**Description**

Obtains the permission information of this DLP file.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [DLP\_FileAccess](#dlp_fileaccess) \*dlpFileAccess | User permission on the DLP file, for example, read-only. |
| uint32\_t \*flags | 
Pointer to the operation permissions allowed for the DLP file. The options are as follows:

**0x00000000** indicates no permission on the file.

**0x00000001** indicates the permission for viewing the file.

**0x00000002** indicates the permission for saving the file.

**0x00000004** indicates the permission for saving the file as another file.

**0x00000008** indicates the permission for editing the file.

**0x00000010** indicates the permission for capturing screenshots of the file.

**0x00000020** indicates the permission for sharing the screen, on which the file is open.

**0x00000040** indicates the permission for recording the screen, on which the file is open.

**0x00000080** indicates the permission for copying the file.

**0x00000100** indicates the permission for printing the file.

**0x00000200** indicates the permission for exporting the file.

**0x00000400** indicates the permission for modifying the permissions on the file.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100001** if invalid parameters are detected.

Returns **19100006** when the access is denied for a non-DLP sandbox application.

Returns **19100011** when the system service is abnormal.

Returns **19100012** if the memory allocation fails.

 |

#### \[h2\]OH\_DLP\_GetOriginalFileName()

DLP\_ErrCode OH\_DLP\_GetOriginalFileName(const char \*fileName, char \*originalFileName)

**Description**

Obtains the original file name of a DLP file.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const char \*fileName | Pointer to the target file whose original file name is to be obtained. |
| char \*originalFileName | Double pointer to the original file name obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100001** if invalid parameters are detected.

Returns **19100012** if the memory allocation fails.

 |

#### \[h2\]OH\_DLP\_IsInSandbox()

DLP\_ErrCode OH\_DLP\_IsInSandbox(bool \*isInSandbox)

**Description**

Checks whether this application is running in a DLP sandbox environment.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| bool \*isInSandbox | Pointer to the value indicating whether the application is running in a DLP sandbox environment. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100011** when the system service is abnormal.

Returns **19100012** if the memory allocation fails.

 |

#### \[h2\]OH\_DLP\_SetSandboxAppConfig()

DLP\_ErrCode OH\_DLP\_SetSandboxAppConfig(const char \*configInfo)

**Description**

Sets sandbox application configuration.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const char \*configInfo | Pointer to the sandbox application configuration obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100001** if invalid parameters are detected.

Returns **19100007** if the API cannot be called by a DLP sandbox application.

Returns **19100011** when the system service is abnormal.

Returns **19100018** if the application is unauthorized.

 |

#### \[h2\]OH\_DLP\_GetSandboxAppConfig()

DLP\_ErrCode OH\_DLP\_GetSandboxAppConfig(char \*configInfo)

**Description**

Obtains the sandbox application configuration.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| char \*configInfo | Pointer to the sandbox application configuration obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100011** when the system service is abnormal.

Returns **19100012** if the memory allocation fails.

Returns **19100018** if the application is unauthorized.

 |

#### \[h2\]OH\_DLP\_CleanSandboxAppConfig()

DLP\_ErrCode OH\_DLP\_CleanSandboxAppConfig()

**Description**

Cleans the sandbox application configuration.

**Since**: 14

**Return value**

| Type | Description |
| :-- | :-- |
| [DLP\_ErrCode](#dlp_errcode) | 
Returns **0** if the operation is successful.

Returns **19100007** if the API cannot be called by a DLP sandbox application.

Returns **19100011** when the system service is abnormal.

Returns **19100018** if the application is unauthorized.

 |
