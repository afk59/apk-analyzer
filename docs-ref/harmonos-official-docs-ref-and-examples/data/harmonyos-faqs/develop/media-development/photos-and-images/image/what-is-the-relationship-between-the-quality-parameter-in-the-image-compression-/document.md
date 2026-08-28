# What is the relationship between the quality parameter in the image compression APIs and the original size and compressed size of an image?

The **quality** parameter affects the target image size for lossy compression image formats (such as JPEG), but not for lossless compression image formats (such as PNG). Note that reducing the **quality** parameter only makes the compressed image file smaller and does not change the image dimensions.

How should I set the **quality** parameter? The ideal image quality setting depends on the image details, color, and contrast, as well as user experience you want to achieve. Some images can be further compressed without noticeable quality loss, whereas others may quickly show artifacts. Generally:

-   A quality setting of 90 can provide extremely high-quality images and also notably shrinks the original file size.
-   A quality setting of **80** achieves an even greater reduction in file size with virtually no compromise on image quality.
-   Lowering the quality below 80 may lead to noticeable artifacts in the image, so it is not recommended.

The system also provides the **scale** API that can resize images based on the input width and height scaling factors, directly changing the image dimensions to achieve a compression effect. You are advised to scale the width and height proportionally to avoid image distortion. Before using the **scale** API, you need to obtain the PixelMap through image decoding. After scaling, the image should be re-compressed and encoded into an image file. Alternatively, you can specify **desiredSize** during image decoding to directly decode the image into a PixelMap of a specific size.

**Reference**

[scale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#scale9)
