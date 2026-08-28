# Using PixelMap to Transform Images

Image processing refers to a series of operations performed on the PixelMap, such as obtaining image information, cropping, scaling, translating, rotating, flipping, setting opacity, and reading and writing pixel data. These operations can be classified into image transformation and [PixelMap operation](../using-pixelmap-for-pixelmap-operations/document.md). This topic describes the image transformation operations that you can perform.

#### How to Develop

Read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) for APIs related to image transformation.

1.  Complete [image decoding](../../image-decoding/using-imagesource-to-decode-images/document.md) and obtain a PixelMap object.
    
2.  Obtain image information.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    // Obtain the image size.
    pixelMap.getImageInfo().then( (info : image.ImageInfo) => {
      console.info('info.width = ' + info.size.width);
      console.info('info.height = ' + info.size.height);
    }).catch((err : BusinessError) => {
      console.error("Failed to obtain the image pixel map information.And the error is: " + err);
    });
    
3.  Perform image transformation.
    
    Original image:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/VJr0bQwWQaePEgwmWp8Afg/en-us_image_0000002568684897.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A97EB75290BB8EB45472AEC9C3C6382DF7C88764BBC2C24D70808CA32BE8A5E8)
    
    -   Crop the image.
        
        // x: x-axis coordinate of the start point for cropping (0).
        // y: y-axis coordinate of the start point for cropping (0).
        // height: height after cropping (400), cropping from top to bottom.
        // width: width after cropping (400), cropping from left to right.
        pixelMap.crop({x: 0, y: 0, size: { height: 400, width: 400 } });
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/QB-EUAjbQZ6PAtw5Bj3v1g/en-us_image_0000002568764907.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8C85681EF48C715A9282F30DFA63193401DBA2C9D1918E716AD781F8EFA2BF8)
        
    -   Scale the image.
        
        // The width of the image after scaling is 0.5 of the original width.
        // The height of the image after scaling is 0.5 of the original height.
        pixelMap.scale(0.5, 0.5);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/U64dafV-S5yk7NA8LDV40A/en-us_image_0000002537765182.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CCF7195AE02C77EC28FB10FB20975D7528B7FE8870950F425CEECB608A9347A)
        
    -   Translate the image.
        
        // Translate the image by 100 units downwards.
        // Translate the image by 100 units rightwards.
        pixelMap.translate(100, 100);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Bxl0vGMqSmehuE1JGQj_1Q/en-us_image_0000002537925122.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A905DD0356C568716A427F1A05374E35A60B608B758F0FE420535B8A73790283)
        
    -   Rotate the image.
        
        // Rotate the image clockwise by 90°.
        pixelMap.rotate(90);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/x2veV_65QqyMFOr3vvacnw/en-us_image_0000002568684899.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82F2F15A8927EEA69FD2E2D3C5944DCEB0F10991B82B6C07FB9C0FA641278A58)
        
    -   Flip the image.
        
        // Flip the image vertically.
        pixelMap.flip(false, true);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/WlgDYfufQ5qnmtYgTxLFCQ/en-us_image_0000002568764909.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3C6274825016CC0E967B73C1F1A091EAF8C4F67BD55D8787AD33EFCDE50D1E0)
        
        // Flip the image horizontally.
        pixelMap.flip(true, false);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/0Es3QprcSVqQw3KAl19dvw/en-us_image_0000002537765184.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93AC50CBDCA7D62C6B154EADBF1044C9825D1CFB7BA5D8730DCFD526D9DCB52C)
        
    -   Set the opacity of the image.
        
        // Set the opacity to 0.5.
        pixelMap.opacity(0.5);
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/O--8AOf_ReCH_zLffwxHnw/en-us_image_0000002537925124.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72C0E0F168393A8077CFF61DA19B640C9155EDDBC9255550866458AA928DCCAA)
