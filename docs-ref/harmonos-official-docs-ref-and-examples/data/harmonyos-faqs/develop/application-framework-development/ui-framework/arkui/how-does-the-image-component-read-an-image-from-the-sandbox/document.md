# How does the Image component read an image from the sandbox?

For the **Image** component to read an image from the sandbox, you cannot directly pass the application sandbox path; instead, you need to pass the application sandbox URI.

1.  Use the **fileUri** module to obtain the sandbox path of the file.
2.  Call the **fileUri.getUriFromPath** method to convert the sandbox path to a sandbox URI. Then, pass this URI to the **Image** component.

**Reference**

[@ohos.file.fileuri (File URI)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri)
