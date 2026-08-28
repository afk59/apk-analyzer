# What should I do if the modification of **upload\_max\_times** does not take effect in the ohpm private repository?

**Symptom**

The default value is 100. After the value is modified to 9999, the limit remains at 100.

**Solution**

\[2024-03-05T19:17:41.123\] \[INFO\] default - "deploy\_root" environment variables: "OHPM\_REPO\_DEPLOY\_ROOT = C:\\Users\\uhamc\\AppData\\Roaming\\Huawei\\ohpm-repo". PS C:\\Users\\uhamc> ohpm-repo start

\[2024-03-05T19:18:10.555\] \[INFO\] default - config file path: "C:\\Users\\uhamc\\AppData\\Roaming\\Huawei\\ohpm-repo\\conf\\config.yaml".

When ohpm-repo is started, it will print the configuration file path. Modify the configuration file and restart the service for changes to take effect.

**Reference**

[Setting the Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo-configuration)
