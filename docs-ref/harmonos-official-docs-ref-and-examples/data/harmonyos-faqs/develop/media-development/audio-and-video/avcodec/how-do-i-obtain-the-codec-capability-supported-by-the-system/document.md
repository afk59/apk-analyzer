# How do I obtain the codec capability supported by the system?

You can use either of the following methods to obtain the codec capability instance:

Method 1: Call **OH\_AVCodec\_GetCapability** to obtain the codec capability instance recommended by the system. The recommendation policy is the same as that of the **OH\_XXX\_CreateByMime** series APIs.

// Obtain an example of the recommended audio AAC decoder capability from the system
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, false);

Method 2: Call **OH\_AVCodec\_GetCapabilityByCategory** to obtain the codec capability instance of the specified software or hardware.

// Obtain an instance of video AVC encoder capability for the specified hardware
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true, HARDWARE);

After the capability instance is obtained, continue to execute. Once the capability instance is obtained, you can proceed with the execution. The system automatically reclaims the **OH\_AVCapability** instance. You do not need to worry about it.

**Reference**

[Obtaining Supported Codecs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/obtain-supported-codecs)
