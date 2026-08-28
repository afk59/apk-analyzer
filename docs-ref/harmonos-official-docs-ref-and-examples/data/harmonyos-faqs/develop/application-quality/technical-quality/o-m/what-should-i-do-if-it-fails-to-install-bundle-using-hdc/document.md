# What should I do if it fails to install bundle using hdc?

**Symptom**

1.  After running the **hdc list targets** command, it shows that only one mobile phone is connected. However, the error message "\[Fail\]ExecuteCommand need connect-key? please confirm a device by help info" is still displayed when the **hdc install** command is executed.
2.  An error message "code:9568xxx error:..." is displayed after the install command is executed.

**Possible Causes**

1.  The device is not properly identified.
2.  An error message is returned after the bm command is executed.

**Solution**

1.  For details, see [What should I do if the device cannot be identified](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#what-should-i-do-if-the-device-cannot-be-identified). After the device can be identified properly by running the **hdc list targets** command, install the bundle again.
2.  For bm tool issues, see [Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#error-codes).
