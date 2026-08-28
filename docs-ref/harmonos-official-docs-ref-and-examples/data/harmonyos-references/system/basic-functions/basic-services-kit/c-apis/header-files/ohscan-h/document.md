# ohscan.h

#### Overview

Declares APIs for discovering and connecting to scanners, scanning pictures, querying the scan progress, and setting parameters for scanning.

**File to include**: <BasicServicesKit/ohscan.h>

**Library**: libohscan.so

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Related module**: [OH\_Scan](../../modules/oh-scan/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Scan\_ScannerDevice](../../structs/scan-scannerdevice/document.md) | Scan\_ScannerDevice | Defines scanner information. |
| [Scan\_PictureScanProgress](../../structs/scan-picturescanprogress/document.md) | Scan\_PictureScanProgress | Defines the progress of scanning a picture by the scanner. |
| [Scan\_ScannerOptions](../../structs/scan-scanneroptions/document.md) | Scan\_ScannerOptions | Defines all parameter options of a scanner. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Scan\_ErrorCode](#scan_errorcode) | Scan\_ErrorCode | Enumerates the error codes. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*Scan\_ScannerDiscoveryCallback)(Scan\_ScannerDevice\*\* devices, int32\_t deviceCount)](#scan_scannerdiscoverycallback) | Scan\_ScannerDiscoveryCallback | Discovers scanners. The memory pointed to by the pointer registered via [OH\_Scan\_StartScannerDiscovery](#oh_scan_startscannerdiscovery) will be released when the callback function ends. |
| [int32\_t OH\_Scan\_Init()](#oh_scan_init) | \- | Initiates the scan service, initializes the scan client, and connects the client to the scan service. |
| [int32\_t OH\_Scan\_StartScannerDiscovery(Scan\_ScannerDiscoveryCallback callback)](#oh_scan_startscannerdiscovery) | \- | Starts scanner discovery and registers a callback used to process the discovered scanners. |
| [int32\_t OH\_Scan\_OpenScanner(const char\* scannerId)](#oh_scan_openscanner) | \- | Opens a scanner. |
| [int32\_t OH\_Scan\_CloseScanner(const char\* scannerId)](#oh_scan_closescanner) | \- | Closes a connected scanner. |
| [Scan\_ScannerOptions\* OH\_Scan\_GetScannerParameter(const char\* scannerId, int32\_t\* errorCode)](#oh_scan_getscannerparameter) | \- | Obtains the scanner setting options. The memory to which the returned struct pointer points is automatically released when [OH\_Scan\_Exit](#oh_scan_exit) is called. Only one copy of each scanner model is stored in the memory. |
| [int32\_t OH\_Scan\_SetScannerParameter(const char\* scannerId, const int32\_t option, const char\* value)](#oh_scan_setscannerparameter) | \- | Sets the option parameters of a scanner. The option values are obtained through the [OH\_Scan\_GetScannerParameter](#oh_scan_getscannerparameter) API. |
| [int32\_t OH\_Scan\_StartScan(const char\* scannerId, bool batchMode)](#oh_scan_startscan) | \- | Starts scanning. |
| [int32\_t OH\_Scan\_CancelScan(const char\* scannerId)](#oh_scan_cancelscan) | \- | Cancels scanning. |
| [int32\_t OH\_Scan\_GetPictureScanProgress(const char\* scannerId, Scan\_PictureScanProgress\* prog)](#oh_scan_getpicturescanprogress) | \- | Obtains the progress of scanning a picture by the scanner. A non-null value must be passed. The scan progress will be written into the struct pointed to by the pointer. |
| [int32\_t OH\_Scan\_Exit()](#oh_scan_exit) | \- | Exits the scan service, releases the memory of the scan framework, and deregisters the scanner discovery callback. |

#### Enum Description

#### \[h2\]Scan\_ErrorCode

enum Scan\_ErrorCode

**Description**

Enumerates the error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| SCAN\_ERROR\_NONE = 0 | Operation successful. |
| SCAN\_ERROR\_NO\_PERMISSION = 201 | Permission verification failed. |
| SCAN\_ERROR\_INVALID\_PARAMETER = 401 | Invalid parameter. For example, the pointer or string is null. |
| SCAN\_ERROR\_GENERIC\_FAILURE = 24300101 | Internal error. |
| SCAN\_ERROR\_RPC\_FAILURE = 24300102 | RPC communication error. |
| SCAN\_ERROR\_SERVER\_FAILURE = 24300103 | Server error. |
| SCAN\_ERROR\_UNSUPPORTED = 24300104 | Unsupported operation. |
| SCAN\_ERROR\_CANCELED = 24300105 | Operation canceled. |
| SCAN\_ERROR\_DEVICE\_BUSY = 24300106 | Device busy. |
| SCAN\_ERROR\_INVALID = 24300107 | Invalid data (for example, no device is available when the scanner is started). |
| SCAN\_ERROR\_JAMMED = 24300108 | Paper jam in feeder. |
| SCAN\_ERROR\_NO\_DOCS = 24300109 | Out of paper. |
| SCAN\_ERROR\_COVER\_OPEN = 24300110 | Scanner cover open. |
| SCAN\_ERROR\_IO\_ERROR = 24300111 | Scanner I/O error. |
| SCAN\_ERROR\_NO\_MEMORY = 24300112 | Insufficient memory. |

#### Function Description

#### \[h2\]Scan\_ScannerDiscoveryCallback()

typedef void (\*Scan\_ScannerDiscoveryCallback)(Scan\_ScannerDevice\*\* devices, int32\_t deviceCount)

**Description**

Discovers scanners. The memory pointed to by the pointer registered via [OH\_Scan\_StartScannerDiscovery](#oh_scan_startscannerdiscovery) will be released when the callback function ends.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Scan\_ScannerDevice](../../structs/scan-scannerdevice/document.md)\*\* devices | Double pointer to the list of all discovered scanners. |
| int32\_t deviceCount | Number of scanners discovered. |

#### \[h2\]OH\_Scan\_Init()

int32\_t OH\_Scan\_Init()

**Description**

Initiates the scan service, initializes the scan client, and connects the client to the scan service.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

 |

#### \[h2\]OH\_Scan\_StartScannerDiscovery()

int32\_t OH\_Scan\_StartScannerDiscovery(Scan\_ScannerDiscoveryCallback callback)

**Description**

Starts scanner discovery and registers a callback used to process the discovered scanners.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Scan\_ScannerDiscoveryCallback](#scan_scannerdiscoverycallback) callback | [Scan\_ScannerDiscoveryCallback](#scan_scannerdiscoverycallback) used to discover scanners. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

 |

#### \[h2\]OH\_Scan\_OpenScanner()

int32\_t OH\_Scan\_OpenScanner(const char\* scannerId)

**Description**

Opens a scanner.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_DEVICE\_BUSY](#scan_errorcode): device busy.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

[SCAN\_ERROR\_IO\_ERROR](#scan_errorcode): scanner I/O error.

[SCAN\_ERROR\_NO\_MEMORY](#scan_errorcode): insufficient memory.

 |

#### \[h2\]OH\_Scan\_CloseScanner()

int32\_t OH\_Scan\_CloseScanner(const char\* scannerId)

**Description**

Closes a connected scanner.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

 |

#### \[h2\]OH\_Scan\_GetScannerParameter()

Scan\_ScannerOptions\* OH\_Scan\_GetScannerParameter(const char\* scannerId, int32\_t\* errorCode)

**Description**

Obtains the scanner setting options. The memory to which the returned struct pointer points is automatically released when [OH\_Scan\_Exit](#oh_scan_exit) is called. Only one copy of each scanner model is stored in the memory.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |
| int32\_t\* errorCode | Pointer to the error code. If the operation is successful, [SCAN\_ERROR\_NONE](#scan_errorcode) is returned; otherwise, a specific error code is returned. For details, see [Print\_ErrorCode](../ohprint-h/document.md#print_errorcode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Scan\_ScannerOptions\*](../../structs/scan-scanneroptions/document.md) | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

 |

#### \[h2\]OH\_Scan\_SetScannerParameter()

int32\_t OH\_Scan\_SetScannerParameter(const char\* scannerId, const int32\_t option, const char\* value)

**Description**

Sets the option parameters of a scanner. The option values are obtained through the [OH\_Scan\_GetScannerParameter](#oh_scan_getscannerparameter) API.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |
| const int32\_t option | ID of the option to be set. The value, obtained from [Scan\_ScannerOptions](../../structs/scan-scanneroptions/document.md), ranges from 0 to optionCount – 1. |
| const char\* value | Pointer to the option value to be set. The valid value is obtained from **ranges** of [Scan\_ScannerOptions](../../structs/scan-scanneroptions/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

 |

#### \[h2\]OH\_Scan\_StartScan()

int32\_t OH\_Scan\_StartScan(const char\* scannerId, bool batchMode)

**Description**

Starts scanning.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |
| bool batchMode | Whether to start the scanner in batch processing mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_JAMMED](#scan_errorcode): paper jam in feeder.

[SCAN\_ERROR\_NO\_DOCS](#scan_errorcode): out of paper.

[SCAN\_ERROR\_COVER\_OPEN](#scan_errorcode): scanner cover open.

[SCAN\_ERROR\_IO\_ERROR](#scan_errorcode): scanner I/O error.

[SCAN\_ERROR\_NO\_MEMORY](#scan_errorcode): insufficient memory.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

[SCAN\_ERROR\_DEVICE\_BUSY](#scan_errorcode): device busy.

 |

#### \[h2\]OH\_Scan\_CancelScan()

int32\_t OH\_Scan\_CancelScan(const char\* scannerId)

**Description**

Cancels scanning.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

 |

#### \[h2\]OH\_Scan\_GetPictureScanProgress()

int32\_t OH\_Scan\_GetPictureScanProgress(const char\* scannerId, Scan\_PictureScanProgress\* prog)

**Description**

Obtains the progress of scanning a picture by the scanner. A non-null value must be passed. The scan progress will be written into the struct pointed to by the pointer.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* scannerId | Pointer to the scanner ID. |
| [Scan\_PictureScanProgress](../../structs/scan-picturescanprogress/document.md)\* prog | Pointer to [Scan\_PictureScanProgress](../../structs/scan-picturescanprogress/document.md). The value cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_INVALID\_PARAMETER](#scan_errorcode): invalid parameter.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

[SCAN\_ERROR\_JAMMED](#scan_errorcode): paper jam in feeder.

[SCAN\_ERROR\_NO\_DOCS](#scan_errorcode): out of paper.

[SCAN\_ERROR\_COVER\_OPEN](#scan_errorcode): scanner cover open.

[SCAN\_ERROR\_IO\_ERROR](#scan_errorcode): scanner I/O error.

[SCAN\_ERROR\_NO\_MEMORY](#scan_errorcode): insufficient memory.

[SCAN\_ERROR\_DEVICE\_BUSY](#scan_errorcode): device busy.

 |

#### \[h2\]OH\_Scan\_Exit()

int32\_t OH\_Scan\_Exit()

**Description**

Exits the scan service, releases the memory of the scan framework, and deregisters the scanner discovery callback.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
[SCAN\_ERROR\_NONE](#scan_errorcode): operation successful.

[SCAN\_ERROR\_NO\_PERMISSION](#scan_errorcode): permission denied.

[SCAN\_ERROR\_RPC\_FAILURE](#scan_errorcode): RPC communication error.

[SCAN\_ERROR\_SERVER\_FAILURE](#scan_errorcode): server error.

 |
