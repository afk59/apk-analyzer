# What is the caching mechanism for the Image component?

1\. Image caching strategy

The **Image** module provides a three-level cache mechanism, which includes the memory image cache before decoding, data cache before decoding, and physical disk cache. When loading images, it searches through the caches one by one, and if it finds an image that has been loaded before in the caches, it returns the corresponding result in advance.

2\. Enabling or disabling the cache for the **Image** component

-   Memory image cache: Call [setImageCacheCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-app#setimagecachecount7) to set the maximum number of decoded images that can be cached in the memory. If you want to obtain the latest resources every time you connect to the network, you can choose not to set this parameter (the default value is **0**).
-   Disk cache: The disk cache is enabled by default, with a default value of 100 MB. To disable it, call [setImageFileCacheSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-app#setimagefilecachesize7) to set the value to **0**.
-   Data cache before decoding: Call [setImageRawDataCacheSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-system-app#setimagerawdatacachesize7) to set the maximum size (in bytes) of the image data cached in the memory before decoding to speed up the loading of images from the same sources. If the input parameter is not set, the default value **0** is used, indicating that images are not cached.

The **setImageCacheCount**, **setImageRawDataCacheSize**, and **setImageFileCacheSize** APIs are not flexible enough and will not be further evolved in future developments. In light of this, consider using [ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife) for more complex scenarios.
