# What should I do when the AVPlayer occasionally reports error codes 5400104 and 5400103?

**Symptom**

The error code 5400103 is reported when the data interaction between the media and other modules (graphics, audio, network, HDI, and camera) is abnormal. It may be related to flow control on the server.

The error code 5400104 is reported when networking or accessing other modules times out. The default network timeout period is 15 seconds, and the timer starts after the buffered event is reported.

**Solution**

1.  Check whether the network connection is normal.
2.  Destroy this instance and re-create it. Destroy this instance and re-create it.
3.  Try to optimize the rate limit of the server corresponding to the stream to avoid the strict conditions caused by the system player.

**Reference**

[Error code 5400103](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-media#section5400103-io-error)

[Error code 5400104](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-media#section5400104-operation-timeout)
