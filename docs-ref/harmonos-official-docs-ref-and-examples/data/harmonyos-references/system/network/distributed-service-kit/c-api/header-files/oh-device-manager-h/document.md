# oh\_device\_manager.h

#### Overview

Provides APIs to obtain information about trusted devices and local devices.

**File to include**: <distributedhardware/device\_manager/oh\_device\_manager.h>

**Library**: libdevicemanager\_ndk.so

**System capability**: SystemCapability.DistributedHardware.DeviceManager

**Since**: 20

**Related module**: [DeviceManager](../../modules/devicemanager/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_DeviceManager\_GetLocalDeviceName(char \*\*localDeviceName, unsigned int &len)](#oh_devicemanager_getlocaldevicename) | 
Obtains the display name of the local device.

The device display name involves user privacy. You need to provide a privacy statement to declare the purpose of the device display name.

 |

#### Function Description

#### \[h2\]OH\_DeviceManager\_GetLocalDeviceName()

int32\_t OH\_DeviceManager\_GetLocalDeviceName(char \*\*localDeviceName, unsigned int &len)

**Description**

Obtains the display name of the local device.

The device display name involves user privacy. You need to provide a privacy statement to declare the purpose of the device display name.

**Required permissions**: ohos.permission.READ\_LOCAL\_DEVICE\_NAME

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| char \*\*localDeviceName | Pointer to the display name of the local device. After using this API, you need to manually release resources to free up space. If the application has the **ohos.permission.READ\_LOCAL\_DEVICE\_NAME** permission, the device display name is returned. Otherwise, the default device name is returned. |
| unsigned int &len | Length of the display name of the local device. |

**Return value**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Error code. For details about the error code definitions, see [DeviceManager\_ErrorCode](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode).

[ERR\_OK](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode) is returned if the execution is successful.

[DM\_ERR\_FAILED](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode) is returned if the function fails to be executed.

[DM\_ERR\_OBTAIN\_SERVICE](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode) is returned if the device management service fails to be obtained.

[DM\_ERR\_OBTAIN\_BUNDLE\_NAME](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode) is returned if the bundle name fails to be obtained.

[ERR\_INVALID\_PARAMETER](../oh-device-manager-err-code-h/document.md#devicemanager_errorcode) is returned if the parameter **localDeviceName** is a null pointer or \***localDeviceName** is not a null pointer.

 |

**Example**

#include "napi/native\_api.h"
#include "hilog/log.h"
#include <distributedhardware/device\_manager/oh\_device\_manager.h>
#include <distributedhardware/device\_manager/oh\_device\_manager\_err\_code.h>
static napi\_value GetDeviceName(napi\_env env, napi\_callback\_info info) {
    napi\_value result = nullptr;
    napi\_create\_object(env, &result);
    char \*localDeviceName = nullptr; // Declare an empty string. You do not need to allocate the address in advance. The address is allocated internally.
    unsigned int len = 0;
    // Pass the address of the empty string to the API.
    int32\_t ret = OH\_DeviceManager\_GetLocalDeviceName(&localDeviceName, len);
    if (ret != ERR\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "ret:%{public}d", ret);
    }

    napi\_value code = nullptr;
    napi\_create\_int32(env, ret, &code);
    napi\_set\_named\_property(env, result, "code", code);

    if (ret == ERR\_OK && localDeviceName != nullptr) {
        napi\_value deviceName = nullptr;
        napi\_create\_string\_utf8(env, localDeviceName, NAPI\_AUTO\_LENGTH, &deviceName);
        napi\_set\_named\_property(env, result, "deviceName", deviceName);
        delete\[\] localDeviceName; // Free the memory.

        napi\_value deviceNameLen = nullptr;
        napi\_create\_int32(env, len, &deviceNameLen);
        napi\_set\_named\_property(env, result, "deviceNameLen", deviceNameLen);
    }
    return result;
}
