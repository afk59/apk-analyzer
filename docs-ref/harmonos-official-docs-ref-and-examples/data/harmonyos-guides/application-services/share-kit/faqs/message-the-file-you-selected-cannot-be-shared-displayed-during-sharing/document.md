# Message "The file you selected cannot be shared." Displayed During Sharing

**Symptom:**

The content cannot be properly displayed in the preview area. When you tap the sharing mode area or operation area, the message "The file you selected cannot be shared." is displayed.

**Possible causes:**

Share Kit cannot access the file URI provided by the app. The possible causes are as follows:

1.  The file URI format is incorrect.
2.  The file URI does not exist or the app does not have permission to access the file.

**Procedure:**

1.  Verify that the file URI format is correct. For details, please refer to [File URI Specifications](../../../../application-framework/core-file-kit/application-files/sharing-an-application-file/document.md#file-uri-specifications).
2.  Verify that the file exists and the app has permission to access the file. You can use [fs.stat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsstat) to try accessing the file, and compare the file creation time with the sharing initiation time to confirm the existence of the file.
