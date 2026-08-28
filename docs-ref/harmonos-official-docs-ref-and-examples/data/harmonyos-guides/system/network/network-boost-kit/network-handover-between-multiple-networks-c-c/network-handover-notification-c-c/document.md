# Network Handover Notification (C/C++)

#### Use Case

When the network signal is weak and the device initiates a network handover (such as from Wi-Fi to cellular or between primary and secondary SIM cards), the device will notify your app upon the start and end of the handover. Then your app can re-establish the link accordingly and swiftly restore services, providing users with a smooth, fast, and low-latency network experience.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_RegisterHandoverChangeCallback(HMS\_NetworkBoost\_HandoverCallback\* callback, uint32\_t\* callbackId)

 | 

Registers the network handover callback.

 |
| 

int32\_t HMS\_NetworkBoost\_UnregisterHandoverChangeCallback(uint32\_t callbackId)

 | 

Deregisters the network handover callback.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost\_handover.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Register the network handover information callback.
    
    uint32\_t callbackId = 0;
    void onNetworkHandoverStart(NetworkBoost\_HandoverStart\* handoverStart)
    {
        // Callback for the start of network handover. Adjust the data transmission policy based on the suggestion in HandoverStart.
    }
    
    void onNetworkHandoverComplete(NetworkBoost\_HandoverComplete\* handoverComplete)
    {
        // Callback for the end of network handover. Adjust the network speed and re-establish the link based on the suggestion in HandoverComplete.
    }
    
    int32\_t RegisterNetworkHandoverCallback()
    { 
        HMS\_NetworkBoost\_HandoverCallback callback;
        callback.onNetworkHandoverStart = onNetworkHandoverStart;
        callback.onNetworkHandoverComplete = onNetworkHandoverComplete;
        // Register the callback and obtain the callback ID.
        int32\_t ret = HMS\_NetworkBoost\_RegisterHandoverChangeCallback(&callback, &callbackId);
        printf("Network handover callback registration result: %d, Id:%d\\n", ret, callbackId);
        return ret;
    }
    
4.  After the service process ends, deregister the network handover information callback.
    
    int32\_t UnregisterNetworkHandoverCallback() {
        // Deregister the callback using the callback ID obtained during registration.
        int32\_t ret = HMS\_NetworkBoost\_UnregisterHandoverChangeCallback(callbackId);
        printf("Network handover callback deregistration result: %d\\n", ret);
        return ret;
    }
