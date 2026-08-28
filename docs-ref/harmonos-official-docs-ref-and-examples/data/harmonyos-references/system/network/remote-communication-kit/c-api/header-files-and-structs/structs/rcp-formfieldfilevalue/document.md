# Rcp\_FormFieldFileValue

#### Overview

Form field file value.

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

char [contentType](#a392fa25d67da5371742d2e837b582660) \[[RCP\_MAX\_CONTENT\_TYPE\_LEN](../../../modules/remotecommunication/document.md#ga994193494eac9591a85c49f1e3200930)\]

 | 

Content type of multi-part form data.

 |
| 

char [remoteFileName](#ac5dc6ae6cece1f6b6ecbab3f2fa65153) \[[RCP\_MAX\_FILENAME\_LEN](../../../modules/remotecommunication/document.md#gaef0f15d9c2cacf9df70ba148cfff171b)\]

 | 

Remote file name of multi-part form data.

 |
| 

[Rcp\_ContentOrPathOrCallback](../rcp-contentorpathorcallback/document.md) [contentOrPathOrCb](#ae23c275b9e2f237b5e4492f998a7e7e4)

 | 

Content of multi-part form data.

 |

#### Member Variable Description

#### \[h2\]contentOrPathOrCb

[Rcp\_ContentOrPathOrCallback](../rcp-contentorpathorcallback/document.md) Rcp\_FormFieldFileValue::contentOrPathOrCb

**Description**

Content of multi-part form data.

#### \[h2\]contentType

char Rcp\_FormFieldFileValue::contentType\[[RCP\_MAX\_CONTENT\_TYPE\_LEN](../../../modules/remotecommunication/document.md#ga994193494eac9591a85c49f1e3200930)\]

**Description**

Content type of multi-part form data.

#### \[h2\]remoteFileName

char Rcp\_FormFieldFileValue::remoteFileName\[[RCP\_MAX\_FILENAME\_LEN](../../../modules/remotecommunication/document.md#gaef0f15d9c2cacf9df70ba148cfff171b)\]

**Description**

Remote file name of multi-part form data.
