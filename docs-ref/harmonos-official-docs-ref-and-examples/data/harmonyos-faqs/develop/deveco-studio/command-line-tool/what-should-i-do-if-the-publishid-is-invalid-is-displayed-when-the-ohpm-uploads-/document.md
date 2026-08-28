# What should I do if "The publishId is invalid!" is displayed when the ohpm uploads a HAR file?

1.  Log in to the ohpm-repo management page and copy the latest release code. For details about how to obtain the release code, see [Publishing with the CLI Tool](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-ohpm-repo-quickstart#en-us_topic_0000001792256157_使用命令行工具发布).
2.  Run the **ohpm config set publish\_id _release code_** command again. After the command is executed, check whether **publish\_id** in the **.ohpmrc** file is updated accordingly.
3.  Upload the HAR file again.
