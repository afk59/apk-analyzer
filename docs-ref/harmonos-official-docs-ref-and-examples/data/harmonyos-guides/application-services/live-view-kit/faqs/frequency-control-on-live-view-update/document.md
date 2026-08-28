# Frequency Control on Live View Update

For live view update through Push Kit, the messages of a single live view can be updated for up to 10 times every 5 minutes and 60 times every hour per device. In the ride hailing and live score scenarios, the messages of a single live view can be updated for up to 30 times every 5 minutes and 180 times every hour per device. For details, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control) of Push Kit.

The flow control mechanism for live view creation and update is as follows:

-   System-level flow control (for all apps): A maximum of 15 live view creation requests and 30 live view update requests can be processed per second. The excess requests are discarded.
-   App-level flow control (for a single app): A maximum of 10 live view creation requests and 20 live view update requests can be processed per second. The excess requests are discarded.
