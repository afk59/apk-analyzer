# Unsupported Shared Data Type

**Symptom:**

1.  Data is discarded during sharing, or a message is displayed indicating invalid data type.
2.  The file is of an unknown type and cannot be shared to other apps.

**Possible causes**:

1.  Mixed file and plain text sharing is not supported; multiple plain text records cannot be shared at the same time.
2.  The file type is not preset and does not match any target apps.

**Procedure:**

1.  Modify the shared content to meet the requirements.
2.  For a common data type, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) to add it to the preset data types. For a user-defined data type, [customize the UTD](../../../../application-framework/arkdata/unified-data-definition/utds-arkts/document.md#custom-utds) to register the data type.
