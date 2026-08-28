# About This Kit

Core Vision Kit provides machine vision-related foundational capabilities, including Optical Character Recognition (OCR), face detection, face verification, and subject segmentation.

You can utilize this kit together with [Vision Kit](../../vision-kit/about-this-kit/document.md)'s UI control capabilities such as face liveness detection to make your app smarter and easier to use.

#### Use Cases

Core Vision Kit fits well in various scenarios to improve user experience and empower a more efficient app. Here are some typical use cases:

-   [OCR](../ocr/document.md): Scans and recognizes text in printed materials such as documents, business cards, and receipts, helping users quickly input and store information.
-   [Face detection](../face-detection/document.md): Automatically detects and locates faces in photos. It is suitable for album management, photo beautification, and other scenarios.
-   [Face verification](../face-verification/document.md): Applies to scenarios where user identity verification is required, such as face authentication, attendance clock-in/out, and access control system.
-   [Subject segmentation](../subject-segmentation/document.md): Identifies and isolates foreground objects or regions (that is, salient subjects) that are distinct from the background in an image. It is suitable for scenarios requiring the recognition and extraction of the main information within an image and is widely used in foreground object detection and foreground subject separation tasks.
-   [Multi-object detection](../multi-object-detection/document.md): Identifies common objects (such as animals, plants, buildings, people, faces, texts, and tables) within images and provide their location information. It is commonly used as a front-end detection function in end-to-end service scenarios to trigger subsequent functions based on detection results, such as visual search and text detection.
-   [Skeleton detection](../skeleton-detection/document.md): Detects skeleton keypoints on the human body to describe skeletal information. It is primarily used in applications such as intelligent video surveillance, patient monitoring systems, human-computer interaction, virtual reality, human animation, smart home, intelligent security, and athlete training assistance.

#### Restrictions

## Supported Devices

Phones, tablets, and PCs/2-in-1 devices.

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

OCR

 | 

-   Supported formats: JPG, JPEG, and PNG
-   Supported languages: simplified Chinese, English, Japanese, Korean, and traditional Chinese
-   Text length: no more than 10,000 characters
-   Supports printed font recognition but has limitations in recognizing handwritten fonts.
-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   The shooting angle should be less than 30 degrees from the vertical direction of the plane where the text is located.

 |
| 

Face detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 224 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   It is not suitable for real-time detection because the API call takes a long period of time.

 |
| 

Face verification

 | 

-   Currently, only one-to-one face comparison is supported.
-   Both input images should have a suitable imaging quality (720p or higher recommended), with a height between 224 px and 15,210 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 10:1 (the height must be less than 10 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |
| 

Subject segmentation

 | 

-   An object will only be recognized as a "subject" and segmented from an image if it occupies at least 0.5% of the original image area.
-   It is not recommended to use this capability for images containing a large amount of text.
-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 20 px and 9000 px, a width between 20 px and 9000 px, and a height-to-width ratio preferably below 3:1 (the height must be less than 3 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |
| 

Multi-object detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 10,000 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 5:1 (the height must be less than 5 times of the width), ideally close to the height-to-width ratio of a smartphone screen.
-   The object's size must account for more than 0.1% of the total image area.

 |
| 

Skeleton detection

 | 

-   The input image should have a suitable imaging quality (720p or higher recommended), with a height between 100 px and 10,000 px, a width between 100 px and 10,000 px, and a height-to-width ratio preferably below 5:1 (the height must be less than 5 times of the width), ideally close to the height-to-width ratio of a smartphone screen.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/hrbO6-QeQJWEkfAS_IeR-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062126Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF3417E2C264413189EB79486FEE5BEC20834EE252E4F2908DE7C0A2D0084141)

Core Vision Kit supports concurrent access from multiple users but does not support concurrent calls of the same API by the same user. If a process calls the same API multiple times simultaneously, a "system busy" error will be returned. If multiple processes call the same API concurrently, only one process will succeed at a time and other processes will be queued.

#### Emulator Support

Currently, this kit does not support emulators.
