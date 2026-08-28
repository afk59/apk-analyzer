# ohprint.h

#### Overview

Declares APIs for discovering and connecting to printers, printing files, and querying the list of added printers and printer information.

**File to include**: <BasicServicesKit/ohprint.h>

**Library**: libohprint.so

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Print\_StringList](../../structs/print-stringlist/document.md) | Print\_StringList | Defines a struct for the string list. |
| [Print\_Property](../../structs/print-property/document.md) | Print\_Property | Defines a struct for the printer property. |
| [Print\_PropertyList](../../structs/print-propertylist/document.md) | Print\_PropertyList | Defines a struct for the printer property list. |
| [Print\_Resolution](../../structs/print-resolution/document.md) | Print\_Resolution | Defines a struct for the printing resolution in dpi. |
| [Print\_Margin](../../structs/print-margin/document.md) | Print\_Margin | Defines a struct for the page margin to print. |
| [Print\_PageSize](../../structs/print-pagesize/document.md) | Print\_PageSize | Defines a struct for the page size. |
| [Print\_PrinterCapability](../../structs/print-printercapability/document.md) | Print\_PrinterCapability | Defines a struct for the printer capabilities. |
| [Print\_DefaultValue](../../structs/print-defaultvalue/document.md) | Print\_DefaultValue | Defines a struct for the default property value. |
| [Print\_PrinterInfo](../../structs/print-printerinfo/document.md) | Print\_PrinterInfo | Defines a struct for the printer information. |
| [Print\_PrintJob](../../structs/print-printjob/document.md) | Print\_PrintJob | Defines a struct for the print job. |
| [Print\_Range](../../structs/print-range/document.md) | Print\_Range | Defines a struct for the page range to print. |
| [Print\_PrintAttributes](../../structs/print-printattributes/document.md) | Print\_PrintAttributes | Defines a struct for the print attributes. |
| [Print\_PrintDocCallback](../../structs/print-printdoccallback/document.md) | Print\_PrintDocCallback | Defines a struct for the print job status callback. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | Print\_ErrorCode | Enumerates the error codes. |
| [Print\_PrinterState](#print_printerstate) | Print\_PrinterState | Enumerates the printer states. |
| [Print\_DiscoveryEvent](#print_discoveryevent) | Print\_DiscoveryEvent | Enumerates the printer discovery events. |
| [Print\_PrinterEvent](#print_printerevent) | Print\_PrinterEvent | Enumerates the printer change events. |
| [Print\_DuplexMode](#print_duplexmode) | Print\_DuplexMode | Enumerates the duplex modes. |
| [Print\_ColorMode](#print_colormode) | Print\_ColorMode | Enumerates the color modes. |
| [Print\_OrientationMode](#print_orientationmode) | Print\_OrientationMode | Enumerates the orientation modes. |
| [Print\_Quality](#print_quality) | Print\_Quality | Enumerates the print qualities. |
| [Print\_DocumentFormat](#print_documentformat) | Print\_DocumentFormat | Enumerates the MIME types. |
| [Print\_JobDocAdapterState](#print_jobdocadapterstate) | Print\_JobDocAdapterState | Enumerates the print job adapter states. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void(\*Print\_WriteResultCallback)(const char \*jobId, uint32\_t code)](#print_writeresultcallback) | Print\_WriteResultCallback | Defines a callback used to return the file write-back result. |
| [typedef void(\*Print\_OnStartLayoutWrite)(const char \*jobId, uint32\_t fd, const Print\_PrintAttributes \*oldAttrs, const Print\_PrintAttributes \*newAttrs, Print\_WriteResultCallback writeCallback)](#print_onstartlayoutwrite) | Print\_OnStartLayoutWrite | Defines a callback to be invoked when the file write-back starts. |
| [typedef void(\*Print\_OnJobStateChanged)(const char \*jobId, uint32\_t state)](#print_onjobstatechanged) | Print\_OnJobStateChanged | Defines a callback to be invoked when the print job state changes. |
| [typedef void (\*Print\_PrinterDiscoveryCallback)(Print\_DiscoveryEvent event, const Print\_PrinterInfo \*printerInfo)](#print_printerdiscoverycallback) | Print\_PrinterDiscoveryCallback | Defines a callback used to return the discovered printers. |
| [typedef void (\*Print\_PrinterChangeCallback)(Print\_PrinterEvent event, const Print\_PrinterInfo \*printerInfo)](#print_printerchangecallback) | Print\_PrinterChangeCallback | Defines a callback to be invoked when a printer is changed. |
| [Print\_ErrorCode OH\_Print\_Init()](#oh_print_init) | \- | Checks and starts the print service, initializes the print client, and connects it with the print service. |
| [Print\_ErrorCode OH\_Print\_Release()](#oh_print_release) | \- | Disconnects from the print service, dismisses the previous callback, and releases the print client resources. |
| [Print\_ErrorCode OH\_Print\_StartPrinterDiscovery(Print\_PrinterDiscoveryCallback callback)](#oh_print_startprinterdiscovery) | \- | Starts printer discovery. |
| [Print\_ErrorCode OH\_Print\_StopPrinterDiscovery()](#oh_print_stopprinterdiscovery) | \- | Stops printer discovery. |
| [Print\_ErrorCode OH\_Print\_ConnectPrinter(const char \*printerId)](#oh_print_connectprinter) | \- | Connects to a printer by the printer ID. |
| [Print\_ErrorCode OH\_Print\_StartPrintJob(const Print\_PrintJob \*printJob)](#oh_print_startprintjob) | \- | Starts a print job. |
| [Print\_ErrorCode OH\_Print\_RegisterPrinterChangeListener(Print\_PrinterChangeCallback callback)](#oh_print_registerprinterchangelistener) | \- | Registers a listener for printer changes. |
| [void OH\_Print\_UnregisterPrinterChangeListener()](#oh_print_unregisterprinterchangelistener) | \- | Unregisters this listener for printer changes. |
| [Print\_ErrorCode OH\_Print\_QueryPrinterList(Print\_StringList \*printerIdList)](#oh_print_queryprinterlist) | \- | Queries the list of added printers. |
| [void OH\_Print\_ReleasePrinterList(Print\_StringList \*printerIdList)](#oh_print_releaseprinterlist) | \- | Releases the memory used to query the printer list. |
| [Print\_ErrorCode OH\_Print\_QueryPrinterInfo(const char \*printerId, Print\_PrinterInfo \*\*printerInfo)](#oh_print_queryprinterinfo) | \- | Queries printer information by printer ID. |
| [void OH\_Print\_ReleasePrinterInfo(Print\_PrinterInfo \*printerInfo)](#oh_print_releaseprinterinfo) | \- | Releases the memory used to query the printer information. |
| [Print\_ErrorCode OH\_Print\_LaunchPrinterManager()](#oh_print_launchprintermanager) | \- | Starts the printer management window of the system. |
| [Print\_ErrorCode OH\_Print\_QueryPrinterProperties(const char \*printerId, const Print\_StringList \*propertyKeyList, Print\_PropertyList \*propertyList)](#oh_print_queryprinterproperties) | \- | Queries the printer properties based on the list of property keys. |
| [void OH\_Print\_ReleasePrinterProperties(Print\_PropertyList \*propertyList)](#oh_print_releaseprinterproperties) | \- | Releases the memory used to query the printer properties. |
| [Print\_ErrorCode OH\_Print\_UpdatePrinterProperties(const char \*printerId, const Print\_PropertyList \*propertyList)](#oh_print_updateprinterproperties) | \- | Updates the printer properties based on the KV pairs. |
| [Print\_ErrorCode OH\_Print\_RestorePrinterProperties(const char \*printerId, const Print\_StringList \*propertyKeyList)](#oh_print_restoreprinterproperties) | \- | Restores printer properties to the default settings based on the property key list. |
| [Print\_ErrorCode OH\_Print\_StartPrintByNative(const char \*printJobName, Print\_PrintDocCallback printDocCallback, void \*context)](#oh_print_startprintbynative) | \- | Starts the printing dialog box. |

#### Enum Description

#### \[h2\]Print\_ErrorCode

enum Print\_ErrorCode

**Description**

Enumerates the error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRINT\_ERROR\_NONE = 0 | Operation successful. |
| PRINT\_ERROR\_NO\_PERMISSION = 201 | Permission verification failed. |
| PRINT\_ERROR\_INVALID\_PARAMETER = 401 | Invalid parameter. |
| PRINT\_ERROR\_GENERIC\_FAILURE = 24300001 | Internal error. |
| PRINT\_ERROR\_RPC\_FAILURE = 24300002 | RPC communication error. |
| PRINT\_ERROR\_SERVER\_FAILURE = 24300003 | Server error. |
| PRINT\_ERROR\_INVALID\_EXTENSION = 24300004 | Invalid extension. |
| PRINT\_ERROR\_INVALID\_PRINTER = 24300005 | Invalid printer. |
| PRINT\_ERROR\_INVALID\_PRINT\_JOB = 24300006 | Invalid print job. |
| PRINT\_ERROR\_FILE\_IO = 24300007 | File I/O error. |
| PRINT\_ERROR\_UNKNOWN = 24300255 | Unknown error. |

#### \[h2\]Print\_PrinterState

enum Print\_PrinterState

**Description**

Enumerates the printer states.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRINTER\_IDLE | The printer is idle. |
| PRINTER\_BUSY | The printer is busy. |
| PRINTER\_UNAVAILABLE | The printer is unavailable. |

#### \[h2\]Print\_DiscoveryEvent

enum Print\_DiscoveryEvent

**Description**

Enumerates the printer discovery events.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRINTER\_DISCOVERED = 0 | Printer discovered. |
| PRINTER\_LOST = 1 | Printer lost. |
| PRINTER\_CONNECTING = 2 | Printer connecting. |
| PRINTER\_CONNECTED = 3 | Printer connected. |

#### \[h2\]Print\_PrinterEvent

enum Print\_PrinterEvent

**Description**

Enumerates the printer change events.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRINTER\_ADDED = 0 | Printer added. |
| PRINTER\_DELETED = 1 | Printer deleted. |
| PRINTER\_STATE\_CHANGED = 2 | Printer changed. |
| PRINTER\_INFO\_CHANGED = 3 | Printer information changed. |

#### \[h2\]Print\_DuplexMode

enum Print\_DuplexMode

**Description**

Enumerates the duplex modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DUPLEX\_MODE\_ONE\_SIDED = 0 | Single-sided mode. |
| DUPLEX\_MODE\_TWO\_SIDED\_LONG\_EDGE = 1 | Duplex mode with flipping on long edge. |
| DUPLEX\_MODE\_TWO\_SIDED\_SHORT\_EDGE = 2 | Duplex mode with flipping on short edge. |

#### \[h2\]Print\_ColorMode

enum Print\_ColorMode

**Description**

Enumerates the color modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| COLOR\_MODE\_MONOCHROME = 0 | B/W mode. |
| COLOR\_MODE\_COLOR = 1 | Color mode. |
| COLOR\_MODE\_AUTO = 2 | Auto mode. |

#### \[h2\]Print\_OrientationMode

enum Print\_OrientationMode

**Description**

Enumerates the orientation modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ORIENTATION\_MODE\_PORTRAIT = 0 | Portrait mode. |
| ORIENTATION\_MODE\_LANDSCAPE = 1 | Landscape mode. |
| ORIENTATION\_MODE\_REVERSE\_LANDSCAPE = 2 | Reverse landscape mode. |
| ORIENTATION\_MODE\_REVERSE\_PORTRAIT = 3 | Reverse portrait mode. |
| ORIENTATION\_MODE\_NONE = 4 | Not specified. |

#### \[h2\]Print\_Quality

enum Print\_Quality

**Description**

Enumerates the print qualities.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRINT\_QUALITY\_DRAFT = 3 | Draft. |
| PRINT\_QUALITY\_NORMAL = 4 | Normal quality. |
| PRINT\_QUALITY\_HIGH = 5 | High quality. |

#### \[h2\]Print\_DocumentFormat

enum Print\_DocumentFormat

**Description**

Enumerates the MIME types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| DOCUMENT\_FORMAT\_AUTO | application/octet-stream. |
| DOCUMENT\_FORMAT\_JPEG | image/jpeg. |
| DOCUMENT\_FORMAT\_PDF | application/pdf. |
| DOCUMENT\_FORMAT\_POSTSCRIPT | application/postscript. |
| DOCUMENT\_FORMAT\_TEXT | text/plain. |

#### \[h2\]Print\_JobDocAdapterState

enum Print\_JobDocAdapterState

**Description**

Enumerates the print job adapter states.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| PRINT\_DOC\_ADAPTER\_PREVIEW\_ABILITY\_DESTROY = 0 | Print job preview destroyed. |
| PRINT\_DOC\_ADAPTER\_PRINT\_TASK\_SUCCEED = 1 | Successful print job. |
| PRINT\_DOC\_ADAPTER\_PRINT\_TASK\_FAIL = 2 | Print job failed. |
| PRINT\_DOC\_ADAPTER\_PRINT\_TASK\_CANCEL = 3 | Print job canceled. |
| PRINT\_DOC\_ADAPTER\_PRINT\_TASK\_BLOCK = 4 | Print job blocked. |
| PRINT\_DOC\_ADAPTER\_PREVIEW\_ABILITY\_DESTROY\_FOR\_CANCELED = 5 | Print job preview destroyed due to cancellation. |
| PRINT\_DOC\_ADAPTER\_PREVIEW\_ABILITY\_DESTROY\_FOR\_STARTED = 6 | Print job preview destroyed due to startup. |

#### Function Description

#### \[h2\]Print\_WriteResultCallback()

typedef void(\*Print\_WriteResultCallback)(const char \*jobId, uint32\_t code)

**Description**

Defines a callback used to return the file write-back result.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*jobId | Pointer to the print job ID. |
| uint32\_t code | File write-back result. |

#### \[h2\]Print\_OnStartLayoutWrite()

typedef void(\*Print\_OnStartLayoutWrite)(const char \*jobId, uint32\_t fd, const Print\_PrintAttributes \*oldAttrs, const Print\_PrintAttributes \*newAttrs, Print\_WriteResultCallback writeCallback)

**Description**

Defines a callback to be invoked when the file write-back starts.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*jobId | Pointer to the print job ID. |
| uint32\_t fd | File descriptor to write. |
| [const Print\_PrintAttributes](../../structs/print-printattributes/document.md) \*oldAttrs | Pointer to the old attribute. |
| [const Print\_PrintAttributes](../../structs/print-printattributes/document.md) \*newAttrs | Pointer to the new attribute. |
| [Print\_WriteResultCallback](#print_writeresultcallback) writeCallback | Defines a callback used to return the file write-back result. |

#### \[h2\]Print\_OnJobStateChanged()

typedef void(\*Print\_OnJobStateChanged)(const char \*jobId, uint32\_t state)

**Description**

Defines a callback to be invoked when the print job state changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*jobId | Pointer to the print job ID. |
| uint32\_t state | Print job state. |

#### \[h2\]Print\_PrinterDiscoveryCallback()

typedef void (\*Print\_PrinterDiscoveryCallback)(Print\_DiscoveryEvent event, const Print\_PrinterInfo \*printerInfo)

**Description**

Defines a callback used to return the discovered printers.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| Print\_DiscoveryEvent event | Printer discovery event. |
| [const Print\_PrinterInfo](../../structs/print-printerinfo/document.md) \*printerInfo | Printer information when the discovery event occurs. |

#### \[h2\]Print\_PrinterChangeCallback()

typedef void (\*Print\_PrinterChangeCallback)(Print\_PrinterEvent event, const Print\_PrinterInfo \*printerInfo)

**Description**

Defines a callback to be invoked when a printer is changed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| Print\_PrinterEvent event | Printer change event during the running of the print service. |
| [const Print\_PrinterInfo](../../structs/print-printerinfo/document.md) \*printerInfo | Printer information when the change event occurs. |

#### \[h2\]OH\_Print\_Init()

Print\_ErrorCode OH\_Print\_Init()

**Description**

Checks and starts the print service, initializes the print client, and connects it with the print service.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

[PRINT\_ERROR\_SERVER\_FAILURE](#print_errorcode): Failed to start the CUPS service.

 |

#### \[h2\]OH\_Print\_Release()

Print\_ErrorCode OH\_Print\_Release()

**Description**

Disconnects from the print service, dismisses the previous callback, and releases the print client resources.

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

Currently, no other error codes will be returned.

 |

#### \[h2\]OH\_Print\_StartPrinterDiscovery()

Print\_ErrorCode OH\_Print\_StartPrinterDiscovery(Print\_PrinterDiscoveryCallback callback)

**Description**

Starts printer discovery.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_PrinterDiscoveryCallback](#print_printerdiscoverycallback) callback | [Print\_PrinterDiscoveryCallback](#print_printerdiscoverycallback) to be invoked when a printer is discovered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

[PRINT\_ERROR\_SERVER\_FAILURE](#print_errorcode): Failed to query the print extension list from the BMS.

[PRINT\_ERROR\_INVALID\_EXTENSION](#print_errorcode): No available print extension is found.

 |

#### \[h2\]OH\_Print\_StopPrinterDiscovery()

Print\_ErrorCode OH\_Print\_StopPrinterDiscovery()

**Description**

Stops printer discovery.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

 |

#### \[h2\]OH\_Print\_ConnectPrinter()

Print\_ErrorCode OH\_Print\_ConnectPrinter(const char \*printerId)

**Description**

Connects to a printer by the printer ID.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printerId | Pointer to the ID of the printer to be connected. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

[PRINT\_ERROR\_INVALID\_PRINTER](#print_errorcode): Printer does not exist in the list of discovered printers.

[PRINT\_ERROR\_SERVER\_FAILURE](#print_errorcode): Failed to find the printer extension.

 |

#### \[h2\]OH\_Print\_StartPrintJob()

Print\_ErrorCode OH\_Print\_StartPrintJob(const Print\_PrintJob \*printJob)

**Description**

Starts a print job.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const Print\_PrintJob](../../structs/print-printjob/document.md) \*printJob | Pointer to the [Print\_PrintJob](../../structs/print-printjob/document.md) instance of the specified print job information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

[PRINT\_ERROR\_INVALID\_PRINTER](#print_errorcode): Printer does not exist in the list of connected printers.

[PRINT\_ERROR\_SERVER\_FAILURE](#print_errorcode): Failed to create a print job in the print service.

[PRINT\_ERROR\_INVALID\_PRINT\_JOB](#print_errorcode): Failed to find the specified task in the task queue.

 |

#### \[h2\]OH\_Print\_RegisterPrinterChangeListener()

Print\_ErrorCode OH\_Print\_RegisterPrinterChangeListener(Print\_PrinterChangeCallback callback)

**Description**

Registers a listener for printer changes.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_PrinterChangeCallback](#print_printerchangecallback) callback | [Print\_PrinterChangeCallback](#print_printerchangecallback) to be registered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

 |

#### \[h2\]OH\_Print\_UnregisterPrinterChangeListener()

void OH\_Print\_UnregisterPrinterChangeListener()

**Description**

Unregisters this listener for printer changes.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

#### \[h2\]OH\_Print\_QueryPrinterList()

Print\_ErrorCode OH\_Print\_QueryPrinterList(Print\_StringList \*printerIdList)

**Description**

Queries the list of added printers.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_StringList](../../structs/print-stringlist/document.md) \*printerIdList | Pointer to the [Print\_StringList](../../structs/print-stringlist/document.md) instance that stores the queried printer ID list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_INVALID\_PARAMETER](#print_errorcode): printerIdList is null.

[PRINT\_ERROR\_INVALID\_PRINTER](#print_errorcode): Failed to query any connected printers.

[PRINT\_ERROR\_GENERIC\_FAILURE](#print_errorcode): Failed to copy printer ID list.

 |

#### \[h2\]OH\_Print\_ReleasePrinterList()

void OH\_Print\_ReleasePrinterList(Print\_StringList \*printerIdList)

**Description**

Releases the memory used to query the printer list.

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_StringList](../../structs/print-stringlist/document.md) \*printerIdList | Pointer to the queried printer ID list. |

#### \[h2\]OH\_Print\_QueryPrinterInfo()

Print\_ErrorCode OH\_Print\_QueryPrinterInfo(const char \*printerId, Print\_PrinterInfo \*\*printerInfo)

**Description**

Queries printer information by printer ID.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printerId | Pointer to the printer ID to be queried. |
| [Print\_PrinterInfo](../../structs/print-printerinfo/document.md) \*\*printerInfo | Double pointer to the [Print\_PrinterInfo](../../structs/print-printerinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

[PRINT\_ERROR\_INVALID\_PARAMETER](#print_errorcode): The printerId or printerInfo is null.

[PRINT\_ERROR\_INVALID\_PRINTER](#print_errorcode): Failed to find the specified printer in the list of connected printers.

 |

#### \[h2\]OH\_Print\_ReleasePrinterInfo()

void OH\_Print\_ReleasePrinterInfo(Print\_PrinterInfo \*printerInfo)

**Description**

Releases the memory used to query the printer information.

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_PrinterInfo](../../structs/print-printerinfo/document.md) \*printerInfo | Pointer to the queried printer information. |

#### \[h2\]OH\_Print\_LaunchPrinterManager()

Print\_ErrorCode OH\_Print\_LaunchPrinterManager()

**Description**

Starts the printer management window of the system.

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_GENERIC\_FAILURE](#print_errorcode): Failed to start the printer management window.

 |

#### \[h2\]OH\_Print\_QueryPrinterProperties()

Print\_ErrorCode OH\_Print\_QueryPrinterProperties(const char \*printerId, const Print\_StringList \*propertyKeyList, Print\_PropertyList \*propertyList)

**Description**

Queries the printer properties based on the list of property keys.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printerId | Pointer to the printer ID to be queried. |
| [const Print\_StringList](../../structs/print-stringlist/document.md) \*propertyKeyList | Pointer to the list of property keys. |
| [Print\_PropertyList](../../structs/print-propertylist/document.md) \*propertyList | Pointer to the queried printer properties. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_INVALID\_PARAMETER](#print_errorcode): One of the parameters is null or the key list is empty.

[PRINT\_ERROR\_INVALID\_PRINTER](#print_errorcode): Failed to find properties of the specified printer.

[PRINT\_ERROR\_GENERIC\_FAILURE](#print_errorcode): Failed to copy printer properties.

 |

#### \[h2\]OH\_Print\_ReleasePrinterProperties()

void OH\_Print\_ReleasePrinterProperties(Print\_PropertyList \*propertyList)

**Description**

Releases the memory used to query the printer properties.

**System capability**: SystemCapability.Print.PrintFramework

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Print\_PropertyList](../../structs/print-propertylist/document.md) \*propertyList | Pointer to the queried printer properties. |

#### \[h2\]OH\_Print\_UpdatePrinterProperties()

Print\_ErrorCode OH\_Print\_UpdatePrinterProperties(const char \*printerId, const Print\_PropertyList \*propertyList)

**Description**

Updates the printer properties based on the KV pairs.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printerId | Pointer to the printer ID. |
| [const Print\_PropertyList](../../structs/print-propertylist/document.md) \*propertyList | Pointer to the list of printer properties to be updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

 |

#### \[h2\]OH\_Print\_RestorePrinterProperties()

Print\_ErrorCode OH\_Print\_RestorePrinterProperties(const char \*printerId, const Print\_StringList \*propertyKeyList)

**Description**

Restores printer properties to the default settings based on the property key list.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printerId | Pointer to the printer ID. |
| [const Print\_StringList](../../structs/print-stringlist/document.md) \*propertyKeyList | Pointer to the property key list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

 |

#### \[h2\]OH\_Print\_StartPrintByNative()

Print\_ErrorCode OH\_Print\_StartPrintByNative(const char \*printJobName, Print\_PrintDocCallback printDocCallback, void \*context)

**Description**

Starts the printing dialog box.

**System capability**: SystemCapability.Print.PrintFramework

**Required permissions**: ohos.permission.PRINT

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*printJobName | Pointer to the name of the print job. |
| [Print\_PrintDocCallback](../../structs/print-printdoccallback/document.md) printDocCallback | Callback used to return the file state. |
| void \*context | Pointer to the context of the caller. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Print\_ErrorCode](#print_errorcode) | 
[PRINT\_ERROR\_NONE](#print_errorcode): Operation is successful.

[PRINT\_ERROR\_NO\_PERMISSION](#print_errorcode): The ohos.permission.PRINT permission is required.

[PRINT\_ERROR\_RPC\_FAILURE](#print_errorcode): Failed to connect to the print service.

 |
