# Manually Triggering Page Turning

Reader Kit has integrated the tap and swipe page turning. You can use the manual page-turning API to implement other page-turning methods such as earphone-controlled page turning.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/XcjGzQDjS9aJs-G7NyS8mg/en-us_image_0000002224175598.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFDD9F6BC060618977D17CD3752BA9122557A616774CD40028A53CB764DD50E0 "Click to enlarge")

#### API Description

This function involves one API. See the following table for detailed API information.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[flipPage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/reader-read-core#section444911141952)(isNext: boolean): void

 | 

Trigger **ReadPageComponent** to turn pages.

 |

#### Preparations

Before manually triggering page turning, ensure that you have [built a reader](../../book-content-typesetting/building-a-reader/document.md).

#### Development Procedure

1.  Before calling the page-turning API, construct a scenario where page turning needs to be manually triggered, for example, earphone-controlled page turning.
2.  Call the **flipPage** API to implement page turning when page turning is triggered.
    
    let isNext: boolean = true; // **true** indicates the next page, and **false** indicates the previous page.
    this.readerComponentController.flipPage(isNext);
