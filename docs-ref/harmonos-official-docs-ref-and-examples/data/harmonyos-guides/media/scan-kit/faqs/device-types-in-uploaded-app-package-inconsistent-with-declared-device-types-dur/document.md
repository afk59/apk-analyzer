# Device Types in Uploaded App Package Inconsistent with Declared Device Types During Package Upload

**Problem**

When I upload my app package to release my app, AppGallery Connect displays an error message indicating that the device types in the uploaded app package are inconsistent with the declared device types, and asks me to upload a correct app package or modify the declared device types.

**Solution**

1.  Verify that **deviceTypes** in the **module.json5** file in the **entry** directory of your project is consistent with the supported device types that you select in AppGallery Connect. For example, if mobile phone is selected as a supported device type, include **phone** in the settings of **deviceTypes** in the **module.json5** file.
2.  If the fault persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
