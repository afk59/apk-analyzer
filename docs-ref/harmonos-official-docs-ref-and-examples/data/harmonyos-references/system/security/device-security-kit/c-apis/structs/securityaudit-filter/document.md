# SecurityAudit\_Filter

#### Overview

This struct provides filters.

**Start version**: 6.0.0(20)

**Related module**: [SecurityAudit](../../modules/securityaudit/document.md)

**Header file**: [security\_audit.h](../../header-files/security-audit-h/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bool [isInclude](#en-us_topic_0000002349177176_a165e68661c3730398273e1481d7f37f9)

 | 

**TRUE**: Events that meet the filter are returned to the client. **FALSE**: Events that meet the filter are not returned to the client.

 |
| 

[SecurityAudit\_FilterType](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) [type](#en-us_topic_0000002349177176_ae66aa2161522f515b0ec6e1a5e4732e0)

 | 

Filter type.

 |
| 

const char \*\* [value](#en-us_topic_0000002349177176_ad881f23acdd73fe7a76280224ecf86fd)

 | 

Event filter value.

 |
| 

uint64\_t [valueCount](#en-us_topic_0000002349177176_ad1c517c207ac47500554a4da337c7ecf)

 | 

Number of filter values.

 |

#### Member Variable Description

#### \[h2\]isInclude

bool SecurityAudit\_Filter::isInclude

**Description**

**TRUE**: Events that meet the filter are returned to the client. **FALSE**: Events that meet the filter are not returned to the client.

#### \[h2\]type

[SecurityAudit\_FilterType](../../modules/securityaudit/document.md#en-us_topic_0000002349017400_gaafa97d3ddf5b088ba32af03ca827ff5f) SecurityAudit\_Filter::type

**Description**

Filter type.

#### \[h2\]value

const char\*\* SecurityAudit\_Filter::value

**Description**

Event filter value.

## valueCount

uint64\_t SecurityAudit\_Filter::valueCount

**Description**

Number of filter values.
