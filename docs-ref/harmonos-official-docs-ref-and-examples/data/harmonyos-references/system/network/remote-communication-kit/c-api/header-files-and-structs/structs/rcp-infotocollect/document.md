# Rcp\_InfoToCollect

#### Overview

Request processing events to be collected. You can check the response object for collected events.

**Start version**: 5.0.0(12)

**Related module**: [RemoteCommunication](../../../modules/remotecommunication/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bool [textual](#aff60c2d577af35be42684cddc8287b23)

 | 

Indicates whether to collect unclassified text events. The default value is **false**.

 |
| 

bool [incomingHeader](#a540ee4c661375b5d261c399c2a95da03)

 | 

Indicates whether to collect HTTP header transfer-in events. The default value is **false**.

 |
| 

bool [outgoingHeader](#a3b8cc7c5c55ca74be187ea24f8788f69)

 | 

Indicates whether to collect HTTP header transfer-out events. The default value is **false**.

 |
| 

bool [incomingData](#ae80433cb5192667786963b6a8a189155)

 | 

Indicates whether to collect HTTP data transfer-in events. The default value is **false**.

 |
| 

bool [outgoingData](#a7324cc52ff8e8d7c3c0c6ec94631c986)

 | 

Indicates whether to collect HTTP data transfer-out events. The default value is **false**.

 |
| 

bool [incomingSslData](#a55f47927846a107a20ea48c32f5b1ce5)

 | 

Indicates whether to collect SSL/TLS transfer-in events. The default value is **false**.

 |
| 

bool [outgoingSslData](#a1c467842caa404c49e282ec6b76a45f1)

 | 

Indicates whether to collect SSL/TLS transfer-out events. The default value is **false**.

 |

#### Member Variable Description

#### \[h2\]incomingData

bool Rcp\_InfoToCollect::incomingData

**Description**

Indicates whether to collect HTTP data transfer-in events. The default value is **false**.

#### \[h2\]incomingHeader

bool Rcp\_InfoToCollect::incomingHeader

**Description**

Indicates whether to collect HTTP header transfer-in events. The default value is **false**.

#### \[h2\]incomingSslData

bool Rcp\_InfoToCollect::incomingSslData

**Description**

Indicates whether to collect SSL/TLS transfer-in events. The default value is **false**.

#### \[h2\]outgoingData

bool Rcp\_InfoToCollect::outgoingData

**Description**

Indicates whether to collect HTTP data transfer-out events. The default value is **false**.

#### \[h2\]outgoingHeader

bool Rcp\_InfoToCollect::outgoingHeader

**Description**

Indicates whether to collect HTTP header transfer-out events. The default value is **false**.

#### \[h2\]outgoingSslData

bool Rcp\_InfoToCollect::outgoingSslData

**Description**

Indicates whether to collect SSL/TLS transfer-out events. The default value is **false**.

#### \[h2\]textual

bool Rcp\_InfoToCollect::textual

**Description**

Indicates whether to collect unclassified text events. The default value is **false**.
