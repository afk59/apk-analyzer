# Failed to open a file preview via the **openPreview** API

When the [openPreview](https://developer.huawei.com/consumer/en/doc/harmonyos-references/preview-arkts#section144826162913) API of Preview Kit passes the file preview information, only the [URI](../../../../application-framework/core-file-kit/user-files/user-file-uri/document.md) of the file can be passed. The path of the file cannot be passed.

If the preview fails after the **openPreview** API is called, check whether the URI is passed and whether the URI exists.
