# XEG\_ExtensionProperties

#### Overview

This structure describes the set of XEngine extensions queried through the [HMS\_XEG\_EnumerateDeviceExtensionProperties](../../../modules/xengine/document.md#hms_xeg_enumeratedeviceextensionproperties) API.

**Since:** 5.0.0(12)

**Related Modules:**[XEngine](../../../modules/xengine/document.md)

**Header file**: [xeg\_vulkan\_extension.h](../../header-files/xeg-vulkan-extension-h/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

char [extensionName](#extensionname) \[[XEG\_MAX\_EXTENSION\_NAME\_SIZE](../../../modules/xengine/document.md#xeg_max_extension_name_size)\]

 | 

Extension name supported by XEngine.

 |
| 

uint32\_t [version](#version)

 | 

Extension version number supported by XEngine.

 |

#### Field

#### \[h2\]extensionName

char XEG\_ExtensionProperties::extensionName\[XEG\_MAX\_EXTENSION\_NAME\_SIZE\]

**Description**

Extension name supported by XEngine.

#### \[h2\]version

uint32\_t XEG\_ExtensionProperties::version

**Description**

Extension version number supported by XEngine.
