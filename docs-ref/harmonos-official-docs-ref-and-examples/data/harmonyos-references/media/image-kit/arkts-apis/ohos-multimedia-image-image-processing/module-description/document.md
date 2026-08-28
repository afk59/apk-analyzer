# Module Description

The module provides capabilities for image decoding, encoding, editing, metadata processing, and image receiving.

This module contains the following classes:

-   [ImageSource](../interface-imagesource/document.md): provides the capabilities of obtaining [image information](../interfaces-others/document.md#imageinfo), decoding images to PixelMaps or Pictures, and reading and modifying [image properties](../enums/document.md#propertykey7). [Supported image formats for decoding](../interface-imagesource/document.md#properties) include png, jpeg, bmp, gif, webp, dng, and heic12+.
    
-   [ImagePacker](../interface-imagepacker/document.md): provides the capability of encoding images into compressed data streams or files. Encoding requires the ImageSource, PixelMap, or Picture of an image as the input. [Supported image formats for encoding](../interface-imagepacker/document.md#properties) include jpeg, webp, png, heic12+, and gif18+.
    
-   [PixelMap](../interface-pixelmap/document.md): contains pixel data and [image information](../interfaces-others/document.md#imageinfo). It can be used for reading/writing pixel data and performing operations such as cropping, scaling, translating, rotating, and mirroring. It can also be directly passed to the [Image component](../../../../../application-framework/arkui/arkts-components/images-and-videos/image/document.md) for display. Additionally, it provides APIs for obtaining and setting the color gamut and HDR metadata of images.
    
-   [Picture](../interface-picture/document.md): a multi-picture object composed of a main picture, auxiliary pictures, and metadata. The main picture contains the primary image information; auxiliary pictures store additional information related to the main picture; metadata stores other information related to the image. Picture provides methods for obtaining the main picture, compositing HDR images, obtaining and setting auxiliary pictures, and obtaining and setting metadata.
    
-   [AuxiliaryPicture](../interface-auxiliarypicture/document.md): used to display special information alongside the main picture, enriching the overall content of the image. The supported types of auxiliary pictures can be found in [AuxiliaryPictureType](../enums/document.md#auxiliarypicturetype13).
    
-   [Metadata](../interface-metadata/document.md): used to store image metadata. For details about the supported metadata types, see [MetadataType](../enums/document.md#metadatatype13). It includes Exif metadata and watermark cropping metadata, both stored in Key-Value pairs. The keys for Exif metadata can be found in [PropertyKey](../enums/document.md#propertykey7), and the keys for watermark cropping metadata can be found in [FragmentPropertyKey](../enums/document.md#fragmentmappropertykey13).
    
-   [ImageReceiver](../interface-imagereceiver/document.md): acts as a consumer of images, used for receiving and reading images from a surface.
    
-   [ImageCreator](../interface-imagecreator/document.md): acts as a producer of images, used for writing images into a surface.
    
-   [Image](../interface-image/document.md): used by ImageReceiver and ImageCreator for transferring image objects, with the actual content determined by the producer. For example, the Image object provided by a camera preview stream contains YUV data, whereas the Image object provided by a camera photo contains a JPEG file.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/BETQMQxYQ0qam8kC9inRoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062432Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32FB51E3FB3EF5472E8CBA5CFFFC75D64ECA32520CEB3FD838532F50FBF2A979)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { image } from '@kit.ImageKit';
