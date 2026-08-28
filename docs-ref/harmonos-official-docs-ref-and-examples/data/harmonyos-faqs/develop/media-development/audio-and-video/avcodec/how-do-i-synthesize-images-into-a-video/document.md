# How do I synthesize images into a video?

You can use the AVCodec Kit to synthesize images into a video. The procedure is as follows:

1.  On the ArkTS side, use **ImageSource** to decode images into PixelMap objects. For details, see [Using ImageSource to Decode Images](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-decoding).
2.  Pass the PixelMap object to the native side through the NDK cross-language interaction process.
3.  On the native side, obtain the PixelMap object passed from the ArkTS side through **OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi** and save the object to the **OH\_PixelmapNative** variable.
4.  Obtain the pixel information of the PixelMap, including the width, height, line stride, pixel format, and whether HDR is supported, through **OH\_PixelmapImageInfo\_Create and OH\_PixelmapNative\_GetImageInfo**. The **get** APIs are **OH\_PixelmapImageInfo\_GetWidth**, **OH\_PixelmapImageInfo\_GetHeight**, and **OH\_PixelmapImageInfo\_GetPixelFormat**. For details, see [Using Image\_NativeModule for PixelMap Operations](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/pixelmap-c).
5.  Read the image pixel data by using the **OH\_PixelmapNative\_ReadPixels** and write the data to the buffer based on the pixel format of the PixelMap.
6.  Create a **VideoEncoder** and a media encapsulator **Muxer** based on the pixel information, and initialize the encoding environment, including encoding parameter setting and callback registration (**OnNeedInputBuffer** and **OnNewOutputBuffer**). For details about the development, see Sample: [AVCodec Based Video Codec](https://gitcode.com/harmonyos_samples/AVCodecVideo).
7.  Start the encoding input thread and encoding output thread. In the input thread, write the PixelMap data in the buffer into the video encoder by calling **OH\_VideoEncoder\_PushInputBuffer**. In the output thread, write the data processed by the video encoder into the media encapsulator by calling **OH\_AVMuxer\_WriteSampleBuffer**, so that the encapsulator can encapsulate the video file. Finally, release the encoder buffer by calling **OH\_VideoEncoder\_FreeOutputBuffer** and implement rotation.
