# How do I use the hdc command to send a local file to a remote device?

To send a local file to a remote device, run the following command:

hdc file send _local_ remote

In this command, _local_ specifies the path of the local file, and **remote** specifies the path in the remote device.

Example:

hdc file send E:\\example.txt /data/local/tmp/example.txt

**Reference**

[hdc](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hdc#transferring-files)
