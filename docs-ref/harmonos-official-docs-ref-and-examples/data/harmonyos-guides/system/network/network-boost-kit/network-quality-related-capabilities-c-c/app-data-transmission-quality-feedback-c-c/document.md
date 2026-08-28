# App Data Transmission Quality Feedback (C/C++)

#### Use Case

When the data transmission performance of your app changes, your app can send the transmission quality and service type data to the network service module of the device via the real-time feedback API. If the performance deteriorates, the module can refine resource scheduling to implement network acceleration.

If frame freezing occurs during video streaming in your app, Network Boost Kit will receive this issue and report it to the network service module. The module will then optimize resource scheduling to accelerate the network.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_ReportQoe(NetworkBoost\_ServiceType serviceType, NetworkBoost\_QoeType qoeType)

 | 

Sends transmission quality data to the device.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost\_quality.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Call the **ReportQoe** API to notify the device of your app's data transmission quality.
    
    int32\_t ReportQoe()
    {
        NetworkBoost\_ServiceType serviceType = NB\_SERVICE\_SHORT\_VIDEO;
        NetworkBoost\_QoeType qoeType = NB\_QOE\_BAD\_SERVER\_ERROR;
        int32\_t ret = HMS\_NetworkBoost\_ReportQoe(serviceType, qoeType);
        printf("Transmission experience feedback result: %d\\n", ret);
        return ret;
    }
