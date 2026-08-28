# About This Kit

Preview Kit provides convenient file preview and opening boost functions for apps.

-   Apps can use the preview APIs provided by Preview Kit to quickly display the preview page, so that users can preview various types of files.
    
    With Preview Kit, users can view files, including images, videos, audios, texts, and HTML pages. In addition, users can redirect to an app to view files through the **Open in another app** button in the upper right corner, after which they can perform operations on the files, such as rotating and zooming in an image.
    
    Currently, Preview Kit uses WPS Office to implement preview capabilities. The preview screen displays "Powered by WPS Office", and provides an entry that allows users to open files with WPS Office and consistent preview style.
    
-   Preview Kit provides the File Open Boost feature. Opening a large file typically takes several to tens of seconds. The file open boost service loads files in advance, shortening the file opening time and providing smooth and seamless experience for users. For details, see [File Open Boost](../file-open-boost-c-c/document.md).

#### File Preview Scenarios

Preview Kit, catering to a majority of office development needs, enables users to preview a variety of file types including images, videos, audios, texts, and HTML pages. It provides the following capabilities:

-   Preview display: displays basic content of a file, such as texts and images. Multiple files can be selected and displayed in the preview list.
-   File sharing: shares a file with another software.
-   Opening through another software: redirects users to an app to view files through the **Open in another app** button. (When a preview request is initiated, your app will obtain the default software that can open this type of file.)
-   Image rotating and zooming in: allows users to rotate and zoom in images during preview on devices except 2-in-1 devices.

#### File Open Boost Scenarios

After your document app integrates the file open boost service, it will recommend files that you may open to your app based on algorithms. The app can then preload files in the background in advance so that you can open the preloaded files in an extremely short time. This provides users with smooth file opening experience.

#### Constraints

## Supported Countries and Regions

Currently, Preview Kit is available only in the Chinese mainland.

## Supported Devices

Preview Kit supports development on the Emulator, but there are some differences compared to real devices. Please refer to [Differences Between the Emulator and the Real Device](../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section38231424133213) for details.

The file preview function is supported on Huawei phones, tablets, and 2-in-1 devices, while the file open boost function is supported only on 2-in-1 devices.

#### File Types Supported by File Preview

Preview Kit supports the preview of images, videos, audios, texts, and HTML files. The following table lists some common formats. You can use the [canPreview](https://developer.huawei.com/consumer/en/doc/harmonyos-references/preview-arkts#section3643113161616) API to check whether a file can be previewed.

| 
Type

 | 

File Name Extension

 | 

mimeType

 |
| :-- | :-- | :-- |
| 

Text

 | 

txt, cpp, c, h, java, xhtml, xml

 | 

text/plain, text/x-c++src, text/x-csrc, text/x-chdr, text/x-java, application/xhtml+xml, text/xml

 |
| 

Web page

 | 

html, htm

 | 

text/html

 |
| 

Image

 | 

jpg, png, gif, webp, bmp, svg

 | 

image/jpeg, image/png, image/gif, image/webp, image/bmp, image/svg+xml

 |
| 

Audio

 | 

m4a, aac, mp3, ogg, wav

 | 

audio/mp4a-latm, audio/aac, audio/mpeg, audio/ogg, audio/x-wav

 |
| 

Video

 | 

mp4, mkv, ts

 | 

video/mp4, video/x-matroska, video/mp2ts

 |
| 

Folder

 | 

N/A

 | 

N/A

 |
| 

Document

 | 

pdf

 | 

application/pdf

 |
| 

Office document

 | 

doc, docx, xls, xlsx, ppt, pptx, csv, ofd

 | 

application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, text/csv, general.ofd

 |

#### File Types Supported by File Open Boost

.doc, .docx, .xls, .xlsx, .ppt, and .pptx files.

#### Basic Concept of File Preview

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/ckAvEYxiTY-9-XLol5UYkQ/en-us_image_0000002263162285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062115Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A1F9FB1703B686BBE27B38808FEDC2C7C9658B564C2D9E8CB2CE1F19AC32C27)

-   Modal window: bound to the parent window. When a modal window exists, the parent window cannot be moved or operated. The modal window consistently remains in front of the parent window.
-   App window: can be started through AMS.
-   AMS: AbilityManagerService, which is a system service for orchestrating the interactions among various abilities and managing their lifecycle stages.
