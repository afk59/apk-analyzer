# SecurityAudit\_Event

#### Overview

This struct defines the audit event information.

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

int64\_t [eventId](#en-us_topic_0000002382857565_a2601bc18ab6afae9e11dc9dc0074f87a)

 | 

Audit event ID.

 |
| 

const char \* [metadata](#en-us_topic_0000002382857565_a1b4c390813d35ca2f1cd385517c6fc20)

 | 

JSON string that contains the event version number, time when an event is received, device ID, and user ID.

 |
| 

const char \* [content](#en-us_topic_0000002382857565_ab436f59837fd0ecf41248425172d39da)

 | 

Event content.

 |

#### Member Variable Description

#### \[h2\]content

const char\* SecurityAudit\_Event::content

**Description**

Event content.

#### \[h2\]eventId

int64\_t SecurityAudit\_Event::eventId

**Description**

Audit event ID.

#### \[h2\]metadata

const char\* SecurityAudit\_Event::metadata

**Description**

JSON string that contains the event version number, time when an event is received, device ID, and user ID.
