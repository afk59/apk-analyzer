# Overview

#### Use Case

Share Kit supports Tap to Transfer between a phone and a PC/2-in-1 device. The PC/2-in-1 device can sense screen touch and identify the touch action and position, implementing window-level interaction with the phone.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ijQO1zifRUe5NF5NofZamA/en-us_image_0000002513289541.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB9A0DDB014D33292548B644EF1AC305D6F30A5E42148EA912D79BBD753CC6AA "Click to enlarge")

#### Service Process

-   PC/2-in-1 device as the data receiver
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/-Ygnh3dHREykp1pw7Di3yA/en-us_image_0000002513289539.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB8193D9B542AD18418E6D3ABA6DAE41A027C5798FBCC1202F304D0DC2A9E0BD "Click to enlarge")
    
-   PC/2-in-1 device as the data sender
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/WZP2Z6O4QcG3K8tXLYbkMA/en-us_image_0000002513289543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA4375C8A0C55668F0184F11469274E923DDC766DF62F1B1ABD0DFE6E6920CD6 "Click to enlarge")
    

#### Restrictions on Two-Way Sharing

Starting from 6.0.0(20) Beta5, two-way sharing is not supported between a phone and a PC/2-in-1 device. The following mechanism is used:

-   When a phone has shareable content in the foreground, the phone is preferentially used as the sender and the PC/2-in-1 device as the receiver, regardless of whether the PC/2-in-1 device has shareable content in the foreground.
-   When a phone does not have shareable content in the foreground but the PC/2-in-1 device does, the PC/2-in-1 device is used as the sender and the phone as the receiver.
-   When no shareable content is available in the foreground of both a phone and a PC/2-in-1 device, the no-content-sharing logic is applied.

For 6.0.0(20) Beta3 and earlier versions, if both a phone and a PC/2-in-1 device have shareable content in the foreground, two-way sharing is supported (a device can send and receive shared content at the same time).

#### Restrictions

-   Both the phone and PC/2-in-1 device must be signed in to the same HUAWEI ID to share content using Tap to Transfer.
-   Only bar-type phones or foldable phones in bar mode can share content with PCs/2-in-1 devices using Tap to Transfer.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/mHZdeUO-TOi88rn15fVOkA/en-us_image_0000002481329640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64D617C000F149BC05F3CA83FE99178E979C879A9B8F8C879D4F1F5385D43ADC "Click to enlarge")
    
-   Restrictions on screen touch interaction:
    -   The top-down angle between the phone and the PC/2-in-1 device screen must be less than or equal to 5°.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Y58_Zij1T1y_n6xJS-s4VA/en-us_image_0000002481329644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=470D4376D50153AF3F97910FF411FF240A4D4AAA390AF4A447C7FB3E9CB772DA "Click to enlarge")
        
    -   The side-view angle between the phone and the PC/2-in-1 device screen must be greater than 35°.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/FWpjB6jhT2Kwiguqow_a6A/en-us_image_0000002481329636.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52CA8224EF42852C49895967D13094B277137DCFDCFF691497057F38F7C9619B "Click to enlarge")
        
    -   The front-view angle between the phone and the PC/2-in-1 device screen must be less than or equal to 25°.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/-yFfVzioTLWA0J1dgrbRWA/en-us_image_0000002513289545.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEDFDF0B1BB9C4468E43247D48F8BBFE1E9E005339C434067F93306CDBC7564B "Click to enlarge")
        
    -   The phone cannot extend beyond the PC/2-in-1 device screen.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/3mc7jSB5RdSCuLHqYlrSkQ/en-us_image_0000002513409507.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E72B9FE218BF5AFB347CDF9F88E581DE6D6E01BFCC69B26F6DD2495A09EBAED9 "Click to enlarge")
        
-   Official phone cases are supported; overly thick cases are not compatible.

#### Environment Requirements

-   Supported PC/2-in-1 device systems: HarmonyOS 6.0.0 Beta1 or later.

-   Integrated development environment: DevEco Studio 6.0.0 Beta1 or later.

#### Sample Code

-   When a PC/2-in-1 device functions as the sender, please refer to [Sending the Shared Data](../../tap-to-transfer-between-phones/sharing-content/document.md#section1083592311502).
-   When a PC/2-in-1 device functions as the receiver, please refer to [Sharing Content to a Specified In-app Page](../sharing-content-to-a-specified-in-app-page/document.md).
