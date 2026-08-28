# How does an application update the progress bar?

If an application expects to display and control the playback progress in the media controller, it must set the resource duration to the AVSession and register a callback for seek commands to respond to the progress control from the media controller. An application can update the progress bar when the playback speed or status changes, thereby conserving system resources.

**Reference**

[Performing Progress Control](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avsession-access-scene#performing-progress-control)
