# Hid\_Device

typedef struct Hid\_Device {...} Hid\_Device

#### Overview

Defines a struct for basic device information.

**Since**: 11

**Related module**: [HidDdk](../../modules/hidddk/document.md)

**Header file:** [hid\_ddk\_types.h](../../header-files/hid-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* deviceName | Device name. |
| uint16\_t vendorId | Vendor ID. |
| uint16\_t productId | Product ID. |
| uint16\_t version | Version number. |
| uint16\_t bustype | Bus type. |
| Hid\_DeviceProp\* properties | Device properties indicated by [Hid\_DeviceProp](../../header-files/hid-ddk-types-h/document.md#hid_deviceprop). |
| uint16\_t propLength | Number of device properties. |
