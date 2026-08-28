# NearLink Kit FAQs

#### Repeated Data Transfer Failures

Calling the [writeData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/nearlink-data-transfer-api#section5484100194119) API repeatedly may congest the transfer queue, leading to data transfer failures.

To solve this, you can set the data transfer interval through [setInterval](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-timer#setinterval). 10 ms is recommended.

#### UUID Format for a Standard NearLink Service

UUID is used to indicate the specific content described in an entry. A standard service or a member of a standard service uses a 16-bit UUID.

Currently, NearLink supports UUIDs in the format of 37BEA880-FC70-11EA-B720-00000000_FDEE_, which contains 128 bits. The first 112 bits are a fixed value determined by the 128-bit base UUID (**37BEA880-FC70-11EA-B720-000000000000**), and the remaining 16 bits indicate either a standard service or a member of a standard service.

The 16-bit UUID that indicates a standard service or standard service member is allocated by the SparkLink Alliance and is globally unique. Through the identifier, the client can determine whether the entry carries a service, an attribute, a method, an event, or references a service.
