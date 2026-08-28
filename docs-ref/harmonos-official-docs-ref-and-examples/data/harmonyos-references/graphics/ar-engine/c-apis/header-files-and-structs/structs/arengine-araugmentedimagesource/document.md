# AREngine\_ARAugmentedImageSource

#### Overview

Image data.

**Start version**: 5.1.0(18)

**Related module**: [AR Engine](../../../modules/ar-engine/document.md)

#### Summary

#### \[h2\]Member Variables

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

const char \*[imageName](#a8fd160424c15bc17d2860f26b1f67d3f)

 | 

Indicates the image name, which cannot be empty. The value can contain a maximum of 255 characters. If the value contains more than 255 characters, the excess characters will be discarded.

 |
| 

const uint8\_t \*[imageData](#a60bbc989bbfdd3ea9f45d9eafe7e8e35)

 | 

Indicates the address of the grayscale image element array.

 |
| 

int32\_t [pixelWidth](#section144101439164014)

 | 

Indicates the image pixel width.

 |
| 

int32\_t [pixelHeight](#section1841210401406)

 | 

Indicates the image pixel height.

 |
| 

int32\_t [stride](#section116614412407)

 | 

Indicates the image stride.

 |
| 

float [realWidthInMeters](#section556412567413)

 | 

Indicates the actual physical width of an object in an image. The width is not limited. The default value is the dimensions of an A4 paper.

 |

#### Struct Member Variable Description

#### \[h2\]imageName

const char\* AREngine\_ARAugmentedImageSource::imageName

**Description**

Indicates the image name, which cannot be empty. The value can contain a maximum of 255 characters. If the value contains more than 255 characters, the excess characters will be discarded.

#### \[h2\]imageData

const uint8\_t\* AREngine\_ARAugmentedImageSource::imageData

**Description**

Indicates the address of the grayscale image element array.

#### \[h2\]pixelWidth

int32\_t AREngine\_ARAugmentedImageSource::pixelWidth

**Description**

Indicates the image pixel width.

#### \[h2\]pixelHeight

int32\_t AREngine\_ARAugmentedImageSource::pixelHeight

**Description**

Indicates the image pixel height.

#### \[h2\]stride

int32\_t AREngine\_ARAugmentedImageSource::stride

**Description**

Indicates the image stride.

#### \[h2\]realWidthInMeters

float AREngine\_ARAugmentedImageSource::realWidthInMeters

**Description**

Indicates the actual physical width of an object in an image. The width is not limited. The default value is the dimensions of an A4 paper.
