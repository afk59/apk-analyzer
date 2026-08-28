# Handover Mode Setting (C/C++)

#### Use Case

Your app can call the **SetHandoverMode** API to change the network handover mode between delegation mode and proactive mode. The delegation mode is used by default. In this case, your app can call the **SetHandoverMode** API to set the mode to proactive mode, forbidding the device to initiate handovers by itself. However, in some cases, for example, when the app is switched to the background, the device may still initiate network handover even if the API is called.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_SetHandoverMode(NetworkBoost\_HandoverMode mode)

 | 

Sets the network handover mode for your app. The delegation mode is used by default.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost\_handover.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Call the **SetHandoverMode** API to set the mode to proactive mode, forbidding the device to initiate handovers by itself.
    
    int32\_t SetHandoverMode()
    {
        NetworkBoost\_HandoverMode mode = NB\_MODE\_DISCRETION;
        int32\_t ret = HMS\_NetworkBoost\_SetHandoverMode(mode);
        printf("Network handover mode setting result: %d\\n", ret);
        return ret;
    }
