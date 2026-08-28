# NetworkBoost\_WeakSignalPrediction

#### Overview

Defines weak signal prediction information.

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

bool [isLastPredictionValid](#aaba94cd96106bc8e7f5474642c0d7fda)

 | 

Indicates whether the latest weak signal prediction is still valid. The options are **true** (yes) and **false** (no). When the value is **false**, the **startTime** and **duration** parameters do not take effect.

 |
| 

uint32\_t [startTime](#a63b7e6caf5bb45d7950a9c098093c7d5)

 | 

Predicted duration before the signal becomes weak, in seconds. The value is 0 or a positive number.

 |
| 

uint32\_t [duration](#a5186381056b65766101e954ae175c8a1)

 | 

Predicted duration of the weak signal, in seconds. The value is a positive number. If the value is 0, the prediction result is invalid.

 |

#### Member Variable Description

#### \[h2\]duration

uint32\_t NetworkBoost\_WeakSignalPrediction::duration

**Description**

Predicted duration of the weak signal, in seconds. The value is a positive number. If the value is 0, the prediction result is invalid.

#### \[h2\]isLastPredictionValid

bool NetworkBoost\_WeakSignalPrediction::isLastPredictionValid

**Description**

Indicates whether the latest weak signal prediction is still valid. The options are **true** (yes) and **false** (no). When the value is **false**, the **startTime** and **duration** parameters do not take effect.

#### \[h2\]startTime

uint32\_t NetworkBoost\_WeakSignalPrediction::startTime

**Description**

Predicted duration before the signal becomes weak, in seconds. The value is 0 or a positive number.
