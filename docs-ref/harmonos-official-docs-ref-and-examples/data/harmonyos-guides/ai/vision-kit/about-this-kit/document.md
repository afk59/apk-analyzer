# About This Kit

Vision Kit integrates visual AI capabilities, including face liveness detection (interactiveLiveness), card recognition (CardRecognition), document scanning (DocumentScanner), and AI image recognition control (visionImageAnalyzer). The face liveness detection capability checks whether a user is a real live person by enabling users to interact with devices. The card recognition capability enables structured recognition for certificates such as ID cards, vehicle licenses, driver's licenses, passports, and bank cards. The document scanning capability takes photos of documents and converts them into high-definition scanned copies. The AI image recognition control enables scenario-specific text recognition, subject segmentation, and image search. The interactive liveness detection and card recognition capabilities are free of charge during the trial period by December 31, 2026. Before starting to charge these capabilities, Huawei will publish a formal charging adjustment notice in advance.

#### Use Cases

Vision Kit provides the following capabilities:

-   [Face liveness detection](../face-liveness-detection/document.md): checks whether a user is a real live person based on interactions with the user.
-   [Card recognition](../card-recognition/document.md): structured recognition of different certificates.
-   [Document scanning](../document-scanning/document.md): takes photos of documents and converts them into high-definition scanned copies.
-   [AI image recognition](../ai-image-recognition/document.md): enables scenario-specific text recognition, subject segmentation, and image search.

#### Restrictions

## Supported Devices

| 
Capability

 | 

Supported Devices

 |
| :-- | :-- |
| 

Face liveness detection

 | 

Phones and tablets

 |
| 

Card recognition

 | 

Phones and tablets

 |
| 

Document scanning

 | 

Phones and tablets

 |
| 

AI image recognition

 | 

Phones, tablets, and PCs/2-in-1 devices

 |

## Supported Countries/Regions

Currently, this kit is available only in the Chinese mainland.

## Restrictions on Capabilities

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Face liveness detection

 | 

-   Languages supported for text: simplified Chinese, traditional Chinese, English, Uyghur, and Tibetan
-   Languages supported for voice broadcast: simplified Chinese and English
-   Currently, this capability does not support the landscape mode or split-screen mode.

 |
| 

Card recognition

 | 

-   Supported languages: simplified Chinese and English
-   Currently, this capability supports only ID cards, vehicle licenses, driver's licenses, passports, and bank cards.
-   This control should not be blocked by another component or window.

 |
| 

Document scanning

 | 

-   Supported languages: simplified Chinese and English
-   Currently, document scanning supports only phones and tablets.
-   This control should not be blocked by another component or window.

 |
| 

AI image recognition

 | 

-   Languages supported for text: simplified Chinese, traditional Chinese, English, Uyghur, and Tibetan
-   The minimum image resolution is 100 x 100.
-   Image analysis supports only static non-vector images, which means that SVG and GIF images cannot be analyzed. The image [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) can be passed for analysis. Currently, only [RGBA\_8888](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-e#pixelmapformat7) images are supported.
-   The minimum aspect ratio is 1:3 (the height must be less than 3 times of the width) for images to be translated and 1:7 (the height must be less than 7 times of the width) for images to have their text recognized.
-   For details about the supported devices, please refer to [Restrictions](../ai-image-recognition/document.md#section2020122517405).

 |

#### Emulator Support

Currently, this kit does not support emulators.
