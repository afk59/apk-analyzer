# What should I do when the OpenSL ES audio recording sample crashes?

**Symptom**

The OpenSL ES audio recording API fails to be called. Consequently, the program breaks down. The error log information is as follows:

08-06 00:39:20.042 5198-5219/? E C02b00/AudioFramework: \[audio\_service\_client.cpp\] Client doesn't have MICROPHONE permission

**Solution**

You must apply for the **ohos.permission.MICROPHONE** permission. For details, please refer to [Open user\_grant Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user).
