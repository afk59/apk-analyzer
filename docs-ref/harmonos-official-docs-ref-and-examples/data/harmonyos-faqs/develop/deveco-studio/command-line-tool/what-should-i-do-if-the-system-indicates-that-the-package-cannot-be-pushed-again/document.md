# What should I do if the system indicates that the package cannot be pushed again within 24 hours after I removed a component by mistake?

**Symptom**

When version uploading, an error was found in the version number. The version was unpublished and corrected. When another attempt is made to upload the version, a message is displayed to indicate that publishing is prohibited within the specified time frame. Can the restriction be lifted? How long is the waiting time?

**Solution**

In the configuration file of **ohpm-repo**, set the number of hours for releasing a removed component to **0.00x**, then run **ohpm install** and restart **ohpm-repo**. However, when this method is used, the version number of the released component must be increased by **1**. For details, see [Setting the Configuration File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo-configuration).
