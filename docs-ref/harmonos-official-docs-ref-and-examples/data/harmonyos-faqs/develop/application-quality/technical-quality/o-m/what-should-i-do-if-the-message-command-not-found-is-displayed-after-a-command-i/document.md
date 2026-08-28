# What should I do if the message "command not found" is displayed after a command is executed in hdc?

**Symptom**

The message "command not found" is displayed after a command is executed in hdc.

**Possible Causes**

1\. The SDK has not been properly installed. Alternatively, the environment variables have not been configured after the installation, and the command is not executed in the directory where the hdc is located.

2\. The environment variables have been configured but have not taken effect.

3\. Multiple environment variables have been configured.

4\. The entered command is incorrect.

**Solution**

1\. Download the application and configure the environment variables correctly. For details, see hdc [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup).

2\. Update after the environment variables are configured.

2.1 Windows: The configuration does not take effect in the terminal window that is opened before the environment variable configuration. You need to open a new window for the configuration to take effect.

2.2 Linux/MacOS: After editing the configuration file by referring to hdc [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup), you need to run the **source** command to make the configuration take effect. If you want the configuration to take effect only in the current terminal window, run the **export** command and the configuration takes effect in the current window.

3\. Check the hdc path configuration.

3.1 Windows: Open the terminal window and run the **where hdc** command. If multiple paths are displayed, modify the value of **PATH** in the system environment variables to remove the redundant hdc paths.

3.2 Linux/MacOS: Open the terminal window and run the **which hdc** command. If multiple paths are displayed, modify the value of **PATH** in the configuration file by referring to hdc [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#environment-setup) to remove the redundant hdc paths.

4\. Check whether the command is correct by referring to [hdc Commands](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#hdc-commands).
