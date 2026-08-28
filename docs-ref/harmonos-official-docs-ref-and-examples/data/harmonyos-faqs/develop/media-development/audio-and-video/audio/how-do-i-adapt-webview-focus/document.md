# How do I adapt WebView focus?

1.  Applications can use the standard HTML interface to listen for the current streaming media playback status, respond to stream interruptions, and refresh the UX page.
2.  Applications can configure the **mediaOptions** attribute to enable automatic playback resumption. If an application has its own playback button UI, it must monitor the video playback status to refresh the UI accordingly. **resumeInterval**: The value ranges from 0 to 60. The default value is **0**, which means no resumption. The value **60** means that the playback can resume within 60 seconds after interruption). **audioExclusive**: The default value is **true**, indicating exclusive playback. If it is set to **false** within an application, concurrent playback is allowed.

**Reference**

[mediaOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#mediaoptions10)
