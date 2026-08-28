# How do I implement conversion between PixelMap and Base64?

PixelMap is an uncompressed bitmap object that contains pixel data and basic image information such as the image size, pixel density, and pixel format.

Base64 encoding is an encoding scheme that converts binary data into ASCII strings for storage and transmission purposes. Generally, PixelMap is not encoded using Base64. Instead, PixelMap is encoded into Uint8Array, and then the binary data of the file is encoded using Base64.

-   Converting a PixelMap file to a Base64 file
    1.  Encode the PixelMap data into an ArrayBuffer.
        
        You need to use the **packToData** method of **ImagePacker** to obtain ArrayBuffer data from the PixelMap object. It should be noted that when using **ImagePacker** to encode PixelMap, the resulting image file may not be exactly the same as the original image file. This is because differences in encoding algorithms and parameters can lead to discrepancies. For example, if the original image file is initially encoded with a quality parameter of only 80 or even lower, and **ImagePacker** is used to encode it with a quality of 100, the size of the image file will significantly increase.
        
    2.  Obtain Uint8Array data from ArrayBuffer data.
        
        You can create a Uint8Array type data from the ArrayBuffer data via **new**. For example: **let uint8buffer = new Uint8Array(arrayBuffer)**, where **arraybuffer** is the original ArrayBuffer type data and **uint8buffer** is the obtained Uint8Array type data.
        
    3.  Convert ArrayBuffer data to Base64 data.
        
        The util function of HarmonyOS provides the **Base64Helper** class, in which the **encodeToStringSync** method can convert Uint8Array data to Base64 data. If you want to ensure that the result after Base64 encoding can still be decoded into the original image file, you should directly use the **Base64Helper** class to perform binary data conversion, avoiding additional image encoding and decoding operations.
        

-   Converting a Base64 file to a PixelMap file
    1.  Parse Base64 data into ArrayBuffer data.
        
        Similarly, you can use the **decodeSync** method in the **Base64Helper** class to parse Base64 data into Uint8Array data.
        
    2.  Convert Uint8Array data into ArrayBuffer data.
        
        You can use the **slice** method to obtain ArrayBuffer data from Uint8Array data, for example, **const arraybuffer: ArrayBuffer = uint8array.buffer.slice(0)**. In the example, **uint8buffer** is the original Uint8Array data, and **arraybuffer** is the obtained ArrayBuffer data.
        
    3.  Convert ArrayBuffer data to the PixelMap type.
        
        You can use **ImageSource** to convert ArrayBuffer data to the PixelMap type. Use the **createImageSource** method of the **Image** module to construct an **ImageSource** instance from ArrayBuffer data, and then use the **createPixelMap** method of **ImageSource** to decode into PixelMap type data.
        

**Reference**

[Image Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-encoding-arts)

[Image Decoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-decoding-arts)

[Base64Helper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-util#base64helper9)
