# Device Interconnectivity NDK Development Guide

Device Interconnectivity enables a TV, tablet, or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

#### Use Case

You can leverage this capability to implement cross-device interaction and enable the use of camera, scanning, and gallery functions of different devices.

#### Restrictions

This feature is available only when the following conditions are met:

-   **Restrictions on devices**
    -   Local device: a TV, tablet, or 2-in-1 device running HarmonyOS NEXT or later
    -   Remote device: a phone or tablet that runs HarmonyOS NEXT or later and supports the camera function
-   **Restrictions on usage**
    -   The same HUAWEI ID is signed in on both devices.
    -   Device Interconnectivity APIs can be used to invoke devices based on specific invoking policies: A TV or 2-in-1 device can invoke tablets and phones, while a tablet can only invoke phones. The local device and remote device cannot be of the same type.
    -   Wi-Fi and Bluetooth are enabled on both devices.
        
        It is recommended that the two devices be connected to the same LAN to improve the camera wake-up speed.
        

#### Service Process

1.  Obtain the device-specific capability list by calling the [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#gaeffea1546cbe64aeba533e5b72bca7ba) API.
2.  Start Device Interconnectivity by calling [HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section4531193410296).
3.  Process the image returned by the remote device on the local device.

#### API Description

Please read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-model) before developing a specific function.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#gaeffea1546cbe64aeba533e5b72bca7ba)

 | 

Obtains information about devices available for Device Interconnectivity.

 |
| 

[HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section4531193410296)

 | 

Starts the Device Interconnectivity capability.

 |
| 

[HMS\_ServiceCollaboration\_StopCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section67211235132913)

 | 

Stops the Device Interconnectivity capability.

 |

#### Development Procedure

1\. Import the header file.

#include "service\_collaboration/service\_collaboration\_api.h"

2\. Compile **CMakeLists.txt**.

find\_library(
    # Sets the name of the path variable.
    service\_collaboration-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    libservice\_collaboration\_ndk.z.so
)
target\_link\_libraries(entry PUBLIC
    ${service\_collaboration-lib}
)

3\. Call APIs using the sample code as follows:

1.  Call the **HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos** API to obtain the device-specific capability list and pass the required **ServiceCollaborationFilterType** capability array. The API returns the information of devices that support the required capabilities.
2.  Create **ServiceCollaborationCallback**, which includes the event callback **OnEventProc** and image data callback **OnDataCallbackProc**. Create **ServiceCollaboration\_SelectInfo**. In the sample code, the **TAKE\_PHOTO** capability is passed and the first device in the list is selected.
3.  Pass the **ServiceCollaborationCallback** and **ServiceCollaboration\_SelectInfo** created in step 2 as the input parameters of **HMS\_ServiceCollaboration\_StartCollaboration**. The remote device then starts the camera, and the user can take a photo with the device. The event and image data are sent to the app through the callback created in step 2.

#include "service\_collaboration/service\_collaboration\_api.h"
#include <thread>

static int32\_t OnEventProc(ServiceCollaborationEventCode code, uint32\_t extraCode)
{
    return 0;
}
static int32\_t OnDataCallbackProc(
    ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32\_t dataSize, char\* data)
{
    return 0;
}
int main(int argc, char\* argv\[\])
{
    int two = 2;
    int three = 3;
    int filter = 1;
    const int size = 3;
    int shouldCancel = 0;
    
    // Build the required capability of Device Interconnectivity and call **HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos** to obtain device information.
    ServiceCollaborationFilterType serviceFilterTypes\[size\] = {TAKE\_PHOTO, SCAN\_DOCUMENT, IMAGE\_PICKER};
    ServiceCollaboration\_CollaborationDeviceInfoSets\* info = HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos(3, serviceFilterTypes);
    // Build a callback.
    ServiceCollaboration\_SelectInfo taskInfo = { TAKE\_PHOTO, { 0 } };
    for (uint32\_t i = 0; i < info->size; i++) {
        ServiceCollaboration\_CollaborationDeviceInfo \*deviceInfo =
            (ServiceCollaboration\_CollaborationDeviceInfo \*)&(info->deviceInfoSets\[i\]);
        if (filter == 1) {
            taskInfo.serviceFilterType = TAKE\_PHOTO;
        }
        if (filter == two) {
            taskInfo.serviceFilterType = SCAN\_DOCUMENT;
        }
        if (filter == three) {
            taskInfo.serviceFilterType = IMAGE\_PICKER;
        }
        std::memcpy(taskInfo.deviceNetworkId, deviceInfo->deviceNetworkId, COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH-1);
    }
    ServiceCollaborationCallback callback = {.OnEvent = OnEventProc, .OnDataCallback = OnDataCallbackProc};
    // Pass the photographing parameters and a callback, and call **HMS\_ServiceCollaboration\_StartCollaboration**.
    uint32\_t id = HMS\_ServiceCollaboration\_StartCollaboration(&taskInfo, &callback);
    std::this\_thread::sleep\_for(std::chrono::seconds(three));
    if (shouldCancel) {
        // Call **HMS\_ServiceCollaboration\_StopCollaboration** to disable Device Interconnectivity after three seconds.
        int32\_t ret = HMS\_ServiceCollaboration\_StopCollaboration(id);
    }
}
