# NetworkBoost\_NetworkQos

#### Overview

Defines network quality data that is returned.

**Start version**: 5.1.0(18)

**Related module**: [NetworkBoost](../../../modules/networkboost/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[NetworkBoost\_PathType](../../../modules/networkboost/document.md#gae8474ae83c3add50ac3fa7702c089ea8) [pathType](#aa2c0dbab80006b4f907cc4ed6ba1069e)

 | 

Type of the path for which the network quality data needs to be returned.

 |
| 

uint64\_t [linkUpBandwidth](#aa52e26c49ee8385d48729c92944aa76e)

 | 

Uplink bandwidth, in bit/s.

 |
| 

uint64\_t [linkDownBandwidth](#ad718456602334a20ef9a527cf32f736e)

 | 

Downlink bandwidth, in bit/s.

 |
| 

uint64\_t [linkUpRate](#adea87b33659ab8d87566b97d9f4afdc8)

 | 

Uplink rate, in bit/s.

 |
| 

uint64\_t [linkDownRate](#ad607a0c7adddc87641499a1c21501e9a)

 | 

Downlink rate, in bit/s.

 |
| 

uint32\_t [rttMs](#a77a16170d4a0ab235de7c0ca59db88dc)

 | 

RTT delay, in milliseconds. The value is any positive number.

 |
| 

uint32\_t [linkUpBufferDelayMs](#a13c017d5d078e43588c9be922c6b39dd)

 | 

Uplink air interface buffer delay, in milliseconds. The value is any positive number.

 |
| 

uint32\_t [linkUpBufferCongestionPercent](#aa5d0ece94735554c3c0c8296a6e4d1d1)

 | 

Percentage of the uplink air interface buffer delay to the total buffering time. The value range is \[0, 100\].

 |

#### Member Variable Description

#### \[h2\]linkDownBandwidth

uint64\_t NetworkBoost\_NetworkQos::linkDownBandwidth

**Description**

Downlink bandwidth, in bit/s.

#### \[h2\]linkDownRate

uint64\_t NetworkBoost\_NetworkQos::linkDownRate

**Description**

Downlink rate, in bit/s.

#### \[h2\]linkUpBandwidth

uint64\_t NetworkBoost\_NetworkQos::linkUpBandwidth

**Description**

Uplink bandwidth, in bit/s.

#### \[h2\]linkUpBufferCongestionPercent

uint32\_t NetworkBoost\_NetworkQos::linkUpBufferCongestionPercent

**Description**

Percentage of the uplink air interface buffer delay to the total buffering time. The value range is \[0, 100\].

#### \[h2\]linkUpBufferDelayMs

uint32\_t NetworkBoost\_NetworkQos::linkUpBufferDelayMs

**Description**

Uplink air interface buffer delay, in milliseconds. The value is any positive number.

#### \[h2\]linkUpRate

uint64\_t NetworkBoost\_NetworkQos::linkUpRate

**Description**

Uplink rate, in bit/s.

#### \[h2\]pathType

[NetworkBoost\_PathType](../../../modules/networkboost/document.md#gae8474ae83c3add50ac3fa7702c089ea8) NetworkBoost\_NetworkQos::pathType

**Description**

Type of the path for which the network quality data needs to be returned.

#### \[h2\]rttMs

uint32\_t NetworkBoost\_NetworkQos::rttMs

**Description**

RTT delay, in milliseconds. The value is any positive number.
