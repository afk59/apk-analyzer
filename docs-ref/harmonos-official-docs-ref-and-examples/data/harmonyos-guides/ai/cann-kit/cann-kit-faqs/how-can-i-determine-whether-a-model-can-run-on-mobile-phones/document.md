# How can I determine whether a model can run on mobile phones?

Call [HMS\_HiAICompatibility\_CheckFromFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaicompatibility_checkfromfile) or [HMS\_HiAICompatibility\_CheckFromBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaicompatibility_checkfrombuffer) and pass the compiled model file or model buffer. If **HIAI\_COMPATIBILITY\_COMPATIBLE** is returned, it indicates that the model is compatible with the phone.
