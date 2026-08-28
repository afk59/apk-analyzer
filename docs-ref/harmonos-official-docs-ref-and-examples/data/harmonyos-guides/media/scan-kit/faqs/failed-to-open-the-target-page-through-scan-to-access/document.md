# Failed to Open the Target Page Through Scan-to-Access

**Problem**

The scan-to-access capability fails to redirect a user to the target page via barcode scanning.

**Solution**

Check your configurations in App Linking:

1.  Verify that your configurations in AppGallery Connect are correct.
2.  Verify that your domain name is correctly associated in App Linking.
3.  Verify that your domain name is correctly configured in the **module.json5** file of your app.
4.  Verify the app signature is correct. For details, please refer to [manual signature guide](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233).

For details, please refer to the [FAQs of App Linking](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section145763212066).
