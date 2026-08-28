# Network Scenario Identification (C/C++)

#### Use Case

Your app can subscribe to network scenario updates. When the real-time or predicted scenario changes, the device will send information to your app, including link type, network scenario type, data transmission policy suggestions, and weak signal information.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_RegisterNetSceneCallback(HMS\_NetworkBoost\_NetSceneChange callback, uint32\_t\* callbackId)

 | 

Registers the network scenario change callback.

 |
| 

int32\_t HMS\_NetworkBoost\_UnregisterNetSceneCallback(uint32\_t callbackId)

 | 

Deregisters the network scenario change callback.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost\_quality.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Register the network scenario identification information callback.
    
    uint32\_t callbackId = 0;
    void onNetworkSceneChanged(NetworkBoost\_NetworkScene \*ns)
    {
        // Process the network scenario identification callback information.
        printf("Data link type: %d\\n", ns->pathType);
        printf("Network scenario: %d\\n", ns->scene);
        switch (ns->scene) {
            case NB\_SCENE\_NORMAL:
                // Common scenario processing.
                break;
            case NB\_SCENE\_CONGESTION:
                // Congestion scenario processing.
                break;
            case NB\_SCENE\_FREQUENT\_HANDOVER:
                // Signal fast switching scenario handling.
                break;
            case NB\_SCENE\_WEAK\_SIGNAL:
                // Weak signal scenario processing.
                break;
        }
        printf("Suggested data transmission policy: %d\\n", ns->recommendedAction);
        if (ns->weakSignalPrediction.duration > 0) {
            // Weak signal prediction processing.
        }
    }
    
    int32\_t RegisterNetSceneCallback()
    { 
        HMS\_NetworkBoost\_NetSceneChange callback;
        callback = onNetworkSceneChanged;
        // Register the callback and obtain the callback ID.
        int32\_t ret = HMS\_NetworkBoost\_RegisterNetSceneCallback(callback, &callbackId);
        printf("Network scenario callback registration result: %d, Id:%d\\n", ret, callbackId);
        return ret;
    }
    
4.  After the service process ends, deregister the callback of the network scenario identification information.
    
    int32\_t UnregisterNetSceneCallback()
    {
        // Deregister the callback using the callback ID obtained during registration.
        int32\_t ret = HMS\_NetworkBoost\_UnregisterNetSceneCallback(callbackId);
        printf("Network scenario callback deregistration result: %d\\n", ret);
        return ret;
    }
