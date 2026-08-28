# Network Quality Assessment (C/C++)

#### Use Case

Your app can subscribe to network quality QoS evaluation data. The device will periodically send updates or notify you when QoS changes. The returned QoS data includes the link type, real-time bandwidth and speed of the uplink and downlink air interface, and RTT delay.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_RegisterNetQosCallback(HMS\_NetworkBoost\_NetQosChange callback, uint32\_t\* callbackId)

 | 

Registers the QoS information change callback.

 |
| 

int32\_t HMS\_NetworkBoost\_UnregisterNetQosCallback(uint32\_t callbackId)

 | 

Deregisters the QoS information change callback.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost\_quality.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Register the network quality assessment information callback.
    
    uint32\_t callbackId = 0;
    void onNetworkQoSChanged(NetworkBoost\_NetworkQosArray \*msg)
    {
        for (int32\_t i = 0; i < msg->pathNum; i++) {
            // Callback information processing.
            printf("Data link type: %d\\n", msg->networkQos\[i\].pathType);
            printf("Uplink bandwidth of this data link type: %ld\\n", msg->networkQos\[i\].linkUpBandwidth);
            printf("Downlink bandwidth of the data link type: %ld\\n", msg->networkQos\[i\].linkDownBandwidth);
            // The unit is bit/s. You can divide the value by 8 to convert it to byte/s.
            printf("Uplink rate of this data link type: %ld\\n", msg->networkQos\[i\].linkUpRate);
            // The unit is bit/s. You can divide the value by 8 to convert it to byte/s.
            printf("Downlink rate of this data link type: %ld\\n", msg->networkQos\[i\].linkDownRate);
            // The real-time rate is the sum of the uplink and downlink rates.
            printf("Real-time rate of the data link type (in byte/s): %ld\\n", (msg->networkQos\[i\].linkUpRate + msg->networkQos\[i\].linkDownRate) / 8);
            printf("RTT delay of this data link type: %d\\n", msg->networkQos\[i\].rttMs);
            printf("Uplink transmission air-interface buffer delay of this data link type: %d\\n", msg->networkQos\[i\].linkUpBufferDelayMs);
        }
    }
    
    int32\_t RegisterNetQualityCallback()
    {
        HMS\_NetworkBoost\_NetQosChange callback;
        callback = onNetworkQoSChanged;
        // Register the callback and obtain the callback ID.
        int32\_t ret = HMS\_NetworkBoost\_RegisterNetQosCallback(callback, &callbackId);
        printf("Network quality callback registration result: %d, Id:%d\\n", ret, callbackId);
        return ret;
    }
    
4.  After the service process ends, deregister the callback of the network quality assessment information.
    
    int32\_t UnregisterNetQualityCallback()
    {
        // Deregister the callback using the callback ID obtained during registration.
        int32\_t ret = HMS\_NetworkBoost\_UnregisterNetQosCallback(callbackId);
        printf("Network quality callback deregistration result: %d\\n", ret);
        return ret;
    }
