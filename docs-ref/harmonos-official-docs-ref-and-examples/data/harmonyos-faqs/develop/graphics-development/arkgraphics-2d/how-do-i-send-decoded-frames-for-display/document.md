# How do I send decoded frames for display?

Method 1: Use the [NativeImage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-image-guidelines) and [XComponent surface](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-decoding#surface-mode) modes. The steps are as follows:

1.  Bind the NativeWindow corresponding to NativeImage to the decoder (surface mode).
2.  Obtain the texture output by the decoder.
3.  Write the texture to the surface of the **XComponent** through [OpenGL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/opengl) for display.

Method 2: Use the buffer mode plus **XComponent** surface mode. The buffer output by the decoder is written to the surface of the **XComponent** through OpenGL for display.
