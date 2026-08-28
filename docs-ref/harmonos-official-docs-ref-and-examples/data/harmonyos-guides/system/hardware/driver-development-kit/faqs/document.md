# FAQs

#### Failed to Find the Header File During Compilation or Running

## Symptom

The message "usb/usb\_ddk\_api.h not found" or "hid/hid\_ddk\_api.h not found" is displayed during compilation or running.

## Solution

-   If an error is reported during compilation, check whether the HarmonyOS version is the latest.
-   If an error is reported during running, check whether the SDK version is API11 or later.

#### Version Mismatch Displayed During HAP Installation

## Symptom

The message "compileSdkVersion and releaseType of the app do not match the apiVersion and releaseType on the device" is displayed during HAP installation.

## Solution

Check whether the system version of the device is correct according to the mapping provided in [Version Mapping](#version-mapping).

## Version Mapping

| API Type | Minimum API Version |
| :-- | :-- |
| Application development APIs (ArkTS APIs) | API10 |
| USB DDK APIs | API10 |
| HID DDK APIs | API11 |

#### Failed to Parse the Local .so File During HAP Installation

## Symptom

The message "code:9568347 error: install parse native so failed" is displayed during HAP installation.

## Solution

Configure the value of abiFilters in buildOption/externalNativeOptions in the build-profile.json5 file. For details, see \[Application Debugging\] ([https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-app-debugging-14-V5](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs-V5/faqs-app-debugging-14-V5)).
