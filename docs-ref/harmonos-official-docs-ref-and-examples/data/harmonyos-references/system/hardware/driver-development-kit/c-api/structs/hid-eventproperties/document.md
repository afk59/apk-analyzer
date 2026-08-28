# Hid\_EventProperties

#### Overview

Defines a struct for the event properties of a device.

**Since**: 11

**Related module**: [HidDdk](../../modules/hidddk/document.md)

**Header file:** [hid\_ddk\_types.h](../../header-files/hid-ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| struct Hid\_EventTypeArray hidEventTypes | Array of event types. |
| struct Hid\_KeyCodeArray hidKeys | Array of key codes. |
| struct Hid\_AbsAxesArray hidAbs | Array of absolute coordinate properties. |
| struct Hid\_RelAxesArray hidRelBits | Array of relative coordinate properties. |
| struct Hid\_MscEventArray hidMiscellaneous | Array of miscellaneous events. |
| int32\_t hidAbsMax\[64\] | Maximum values of the absolute coordinates. |
| int32\_t hidAbsMin\[64\] | Minimum values of the absolute coordinates. |
| int32\_t hidAbsFuzz\[64\] | Fuzzy values of the absolute coordinates. |
| int32\_t hidAbsFlat\[64\] | Fixed values of the absolute coordinates. |
