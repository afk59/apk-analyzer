# About This Kit

Image Kit provides APIs for you to decode, encode, edit, and receive images, as well as processing metadata of images.

#### Highlights

-   Supports encoding and decoding of popular image formats, such as HEIF, JPEG, PNG, and WebP.
-   Supports HDR image encoding and decoding, providing users with a better color experience; leveraging AI to convert SDR images into HDR images.
-   Provides a variety of image editing and processing capabilities, including image transformation, PixelMap operations, and filter effects.
-   Uses efficient algorithms and optimization policies to make image processing faster and more efficient.

#### Basic Concepts

Be familiar with the following basic concepts before development:

-   [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)
    
    PixelMap object. It can be used for reading/writing pixel data and performing operations such as cropping, scaling, translating, rotating, and mirroring. It can also be directly passed to the [Image component](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/media-display/image-display-image/document.md) for display. Additionally, it provides APIs for obtaining image information, and obtaining and setting the color gamut and HDR metadata of images.
    
-   [Picture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-picture)
    
    An object that includes a main picture, auxiliary picture, and metadata. The main picture contains the primary image information; auxiliary pictures store additional information related to the main picture; metadata stores other information related to the image. Picture provides methods for obtaining the main picture, compositing HDR images, obtaining and setting auxiliary pictures, and obtaining and setting metadata.
    
-   Image decoding
    
    The operation of decoding an image in a supported format into a PixelMap or Picture for image display or processing.
    
-   Image editing and processing
    
    A series of operations on the PixelMap, such as rotation, scaling, opacity setting, image information obtaining, and pixel data reading and writing. The origin of the coordinate system is at the upper left corner.
    
-   Image encoding
    
    The operation of encoding a PixelMap or Picture into an image in different formats for subsequent processing, such as storage and transmission.
    

#### How to Use

Image Kit provides abundant image processing capabilities. You can use the entire process of image decoding, editing, processing, and encoding, or you can just pass the decoded PixelMap to the [Image component](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/media-display/image-display-image/document.md) for display without extra processing. Both decoding and encoding offer many options to fit different development needs.

You can manipulate specific parts of an image by performing [PixelMap operations](../image-development-arkts/image-editing-and-processing/using-pixelmap-for-pixelmap-operations/document.md) on the decoded PixelMap. Additionally, you can apply [image transformations](../image-development-arkts/image-editing-and-processing/using-pixelmap-to-transform-images/document.md) such as cropping, scaling, translating, rotating, flipping, and opacity setting.

Image Kit allows you to add filter effects to images using [ImageEffect](../image-development-c-c/image-editing-and-processing/using-imageeffect-to-edit-images/document.md).

Image Kit also provides the ability to read and [edit image Exif information](../image-development-arkts/image-editing-and-processing/editing-exif-data/document.md). You can get and set additional properties in image files, including basic image information such as width, height, and orientation; capture parameters such as aperture and focal length; and GPS information such as longitude and latitude.

Figure 1 and Figure 2 show the image decoding and encoding processes. The PixelMap obtained after decoding can be used for image display, editing, and processing.

**Figure 1** Image decoding process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Q_wbJHTQRmCPt9_cI_1prw/en-us_image_0000002537765180.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E4F738F6E2DBB3CFD5ABA965A94E2B78DDFF0A795EDD51EDD1209E95F9190E2)

**Figure 2** Image encoding process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GafAR8z6QiKSKryEeFcFYQ/en-us_image_0000002537925120.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=726901AE926FF30BDC8DA96C54D0941983057461A36CBCC331B160D53354FB54)

#### Constraints

-   **Constraints on read and write permissions**
    
    During image processing, applications may need to request the read and write permissions from users on images. For details about how to request the permissions, see [Requesting User Authorization](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
    
-   **Selecting appropriate C APIs**
    
    Image Kit provides two sets of C APIs: [C APIs dependent on JS objects](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image) and [C APIs independent of JS objects](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).
    
    -   C APIs that depend on JS objects
        
        These APIs are used to encode and decode images, receive images, and process image data. Example code related to these functionalities is provided in [Using Image to Decode Images (C/C++)](../image-development-dependent-on-js-objects-not-recommended/image-decoding/document.md). You can find these APIs in [Image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image). These APIs are introduced prior to API version 11, and no additional features will be included in later versions. Therefore, these APIs are not recommended.
        
    -   C APIs independent of JS objects
        
        In addition to the functionalities mentioned above, these APIs implements new features such as picture encoding and decoding. For details about the development guide, see [Using Image\_NativeModule to Decode Images](../image-development-c-c/image-decoding/using-image-nativemodule-to-decode-images/document.md). You can find these APIs in [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule). These APIs are available since API version 12 and are expected to keep evolving. You are encouraged to use them.
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/oNQG8qghTzmOSQHptIT0Gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062040Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEF409D1A66A31DE4562BC51539A445463B4D3E04A33EE9469FEE7D4A39C7585)
    
    You are not advised to use both sets of C APIs in your code. It may cause compatibility issues in some scenarios.
    

#### Related Kits

Image Kit handles image encoding, decoding, receiving, editing, and processing. It supports the **Image** component, Gallery, and other applications that have image-related requirements. The PixelMap obtained after image decoding can be passed to the [Image component](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/media-display/image-display-image/document.md) for display. The [ImageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagereceiver) can be used to implement [secondary processing of preview streams](../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/secondary-processing-of-preview-streams-c-c/document.md).
