# What should I do if "decrypt data failed. error: Unsupported state or unable to authenticate data" is displayed when ohpm-repo uses the mysqlDB plugin to connect to MySQL?

Delete the **.deploy\_root** file in the root directory of the ohpm-repo private repository, specify the encryption component, and execute the **start** command again.

**Reference**

[ohpm-repo start](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo-start)
