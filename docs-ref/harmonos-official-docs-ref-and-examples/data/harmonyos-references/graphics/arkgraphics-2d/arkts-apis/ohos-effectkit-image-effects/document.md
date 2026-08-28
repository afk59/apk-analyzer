# @ohos.effectKit (Image Effects)

This module provides basic image processing capabilities, including brightness adjustment, blurring, grayscale adjustment, and color picker. The **effectKit** module processes images (such as PixelMap, PNG, and JPEG) offline to obtain visual effects. The **uiEffect** module connects to the rendering service in real time and process the screen frame buffer to obtain dynamic visual effects.

This module provides the following classes:

-   [Filter](#filter): a class that adds a specified effect to the image source.
-   [Color](#color): a class used to store the color picked.
-   [ColorPicker](#colorpicker): a smart color picker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/buph0Ip5SpyeS8VAqw6ASw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDF1D5B990118FC15A23FA9593D8C0D0768F705C01E1382D7893C949B13A538B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { effectKit } from "@kit.ArkGraphics2D";

#### effectKit.createEffect

createEffect(source: image.PixelMap): Filter

Creates a **Filter** instance based on a pixel map.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | **PixelMap** instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see [Introduction to Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Head node of the filter linked list without any effect. If the operation fails, **null** is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  let headFilter = effectKit.createEffect(pixelMap);
})

#### effectKit.createColorPicker

createColorPicker(source: image.PixelMap): Promise<ColorPicker>

Creates a **ColorPicker** instance based on a pixel map. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | **PixelMap** instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see [Introduction to Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ColorPicker](#colorpicker)\> | Promise used to return the **ColorPicker** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Input parameter error. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})

#### effectKit.createColorPicker10+

createColorPicker(source: image.PixelMap, region: Array<number>): Promise<ColorPicker>

Creates a **ColorPicker** instance for the selected region based on a pixel map. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | **PixelMap** instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see [Introduction to Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview). |
| region | Array<number> | Yes | 
Region of the image from which the color is picked.

The array consists of four elements, representing the left, top, right, and bottom positions of the image, respectively. The value of each element must be in the range \[0, 1\]. The leftmost and topmost positions of the image correspond to **0**, and the rightmost and bottom positions correspond to **1**. In the array, the third element must be greater than the first element, and the fourth element must be greater than the second element.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ColorPicker](#colorpicker)\> | Promise used to return the **ColorPicker** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Input parameter error. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";
import { BusinessError } from "@kit.BasicServicesKit";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}

image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, \[0, 0, 1, 1\]).then(colorPicker => {
    console.info("color picker=" + colorPicker);
  }).catch( (reason : BusinessError) => {
    console.error("error=" + reason.message);
  })
})

#### effectKit.createColorPicker

createColorPicker(source: image.PixelMap, callback: AsyncCallback<ColorPicker>): void

Creates a **ColorPicker** instance based on a pixel map. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | **PixelMap** instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see [Introduction to Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview). |
| callback | AsyncCallback<[ColorPicker](#colorpicker)\> | Yes | Callback used to return the **ColorPicker** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Input parameter error. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})

#### effectKit.createColorPicker10+

createColorPicker(source: image.PixelMap, region:Array<number>, callback: AsyncCallback<ColorPicker>): void

Creates a **ColorPicker** instance for the selected region based on a pixel map. This API uses an asynchronous callback to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | **PixelMap** instance created by the image module. An instance can be obtained by decoding an image or directly created. For details, see [Introduction to Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview). |
| region | Array<number> | Yes | 
Region of the image from which the color is picked.

The array consists of four elements, representing the left, top, right, and bottom positions of the image, respectively. The value of each element must be in the range \[0, 1\]. The leftmost and topmost positions of the image correspond to **0**, and the rightmost and bottom positions correspond to **1**. In the array, the third element must be greater than the first element, and the fourth element must be greater than the second element.

 |
| callback | AsyncCallback<[ColorPicker](#colorpicker)\> | Yes | Callback used to return the **ColorPicker** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Input parameter error. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, \[0, 0, 1, 1\], (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
    }
  })
})

#### Color

A class that stores the color picked.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| red | number | No | No | Value of the red component. The value range is \[0x0, 0xFF\]. |
| green | number | No | No | Value of the green component. The value range is \[0x0, 0xFF\]. |
| blue | number | No | No | Value of the blue component. The value range is \[0x0, 0xFF\]. |
| alpha | number | No | No | Value of the alpha component. The value range is \[0x0, 0xFF\]. |

#### TileMode14+

Enumerates the tile modes of the shader effect.

**System capability**: SystemCapability.Multimedia.Image.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CLAMP | 0 | Replicates the edge color if the shader effect draws outside of its original boundary. |
| REPEAT | 1 | Repeats the shader effect in both horizontal and vertical directions. |
| MIRROR | 2 | Repeats the shader effect in both horizontal and vertical directions, alternating mirror images. |
| DECAL | 3 | Renders the shader effect only within the original boundary. |

#### ColorPicker

A class used to obtain the color from an image. Before calling any method of **ColorPicker**, use [createColorPicker](#effectkitcreatecolorpicker) to create a **ColorPicker** instance.

#### \[h2\]getMainColor

getMainColor(): Promise<Color>

Obtains the main color from the image and writes the result to a [Color](#color) instance. This API uses a promise to return the result. This API uses the image scaling algorithm to calculate the weighted average of surrounding pixels and reduces the original image to one pixel to obtain the main color.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Color](#color)\> | Promise used to return the color value of the main color. If the operation fails, an error message is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
     } else {
       console.info('Succeeded in creating color picker.');
       colorPicker.getMainColor().then(color => {
        console.info('Succeeded in getting main color.');
         console.info(\`color\[ARGB\]=${color.alpha},${color.red},${color.green},${color.blue}\`);
      })
    }
  })
})

#### \[h2\]getMainColorSync

getMainColorSync(): Color

Obtains the main color from the image and writes the result to a [Color](#color) instance. This API returns the result synchronously. This API uses the image scaling algorithm to calculate the weighted average of surrounding pixels and reduces the original image to one pixel to obtain the main color.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Color](#color) | Color value of the main color. If the operation fails, **null** is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getMainColorSync();
      console.info('get main color =' + color);
    }
  })
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/jG4CwHIKQyOy51bgmoQeKQ/en-us_image_0000002537926346.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4447BFEF24DF2A8A5FE7F035090609E0E3BFA55DBFDB86E167625C43B934B3E)

#### \[h2\]getLargestProportionColor10+

getLargestProportionColor(): Color

Obtains the color with the largest proportion from the image and writes the result to a [Color](#color) instance. This API returns the result synchronously. This API uses the median split algorithm to divide the color space and obtain the average color of the color space with the largest proportion.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Color](#color) | Color value of the color with the largest proportion. If the operation fails, **null** is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getLargestProportionColor();
      console.info('get largest proportion color =' + color);
    }
  })
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/EUDifo9pQAWzJrH25gA6dw/en-us_image_0000002568686123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E49A49048A0210EF591D8D43149F29EA494EC3D98411B464977C1135526650D1)

#### \[h2\]getTopProportionColors12+

getTopProportionColors(colorCount: number): Array<Color | null>

Obtains a given number of colors with the top proportions in the image. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorCount | number | Yes | Number of colors to be obtained. The value range is \[1, 10\]. If a non-integer is passed in, the value will be rounded down. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Color](#color) | null> | 
Array of colors, sorted by proportion.

\- If the number of colors obtained is less than the value of **colorCount**, the array size is the actual number obtained.

\- If the colors fail to be obtained or the number of colors obtained is less than 1, **\[null\]** is returned.

\- If the value of **colorCount** is greater than 10, an array holding the first 10 colors with the top proportions is returned.

 |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let colors = colorPicker.getTopProportionColors(2);
      for(let index = 0; index < colors.length; index++) {
        if (colors\[index\]) {
          console.info('get top proportion colors: index ' + index + ', color ' + colors\[index\]);
        }
      }
    }
  })
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/J3LTuofVTFWYXb1hXi04eA/en-us_image_0000002568766133.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F33B624D89DF0CC70884551C86C9B769AEC3F095A87F3C143414DFE0261CB9F)

#### \[h2\]getHighestSaturationColor10+

getHighestSaturationColor(): Color

Obtains the color with the highest saturation from the image and writes the result to a [Color](#color) instance. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Color](#color) | Color value of the color with the highest saturation. If the operation fails, **null** is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getHighestSaturationColor();
      console.info('get highest saturation color =' + color);
    }
  })
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/nxAs6IB0Q_m041Z1atP9Xw/en-us_image_0000002537766408.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DACA35E7E26A6E3C35A3A5D9A4776395BA05E548F993E31488952EFF4A2A689F)

#### \[h2\]getAverageColor10+

getAverageColor(): Color

Obtains the average color from the image and writes the result to a [Color](#color) instance. This API returns the result synchronously.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Color](#color) | Average color value. If the operation fails, **null** is returned. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let color = colorPicker.getAverageColor();
      console.info('get average color =' + color);
    }
  })
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/zq5MGh_6R66JI8pzZK7hhA/en-us_image_0000002537926348.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54CF5342836BA0A2259594ABF21D72D10B0E22CB1D60A62494E08F48BB9481B9)

#### \[h2\]isBlackOrWhiteOrGrayColor10+

isBlackOrWhiteOrGrayColor(color: number): boolean

Checks whether a color is black, white, and gray.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | number | Yes | Color to check. The value range is \[0x0, 0xFFFFFFFF\]. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if the image is black, white, and gray; returns **false** otherwise. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts: image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createColorPicker(pixelMap, (error, colorPicker) => {
    if (error) {
      console.error('Failed to create color picker.');
    } else {
      console.info('Succeeded in creating color picker.');
      let bJudge = colorPicker.isBlackOrWhiteOrGrayColor(0xFFFFFFFF);
      console.info('is black or white or gray color\[bool\](white) =' + bJudge);
    }
  })
})

#### Filter

A class used to add a specified effect to an image. Before calling any method of **Filter**, use [createEffect](#effectkitcreateeffect) to create a **Filter** instance.

#### \[h2\]blur

blur(radius: number): Filter

Adds the blur effect to the filter linked list, and returns the head node of the linked list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/6w6DBoOOQTmbsZ1DzIyDYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DD6B58AEFBEFBE5B9BFD97CD15DEDF62F5A008B41195F6E9C4AECB716045E16)

This API provides the blur effect for static images. To provide the real-time blur effect for components, use [dynamic blur](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-blur-effect).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | number | Yes | Blur radius, in pixels. The blur effect is proportional to the configured value. A larger value indicates a more obvious effect. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let radius = 5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.blur(radius);
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/B5MdWPKbS1G_FVIvNTzB6w/en-us_image_0000002568686125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDFD0882837AD2527B1EBFBE2AF9731A3CA11464662C1C2000314C6065E32D9A)

#### \[h2\]blur14+

blur(radius: number, tileMode: TileMode): Filter

Adds the blur effect to the filter linked list, and returns the head node of the linked list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/WoqGjbQKT7KgQWNjgtkRRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=108BB6CFBDBB081C57DEACC2BB52330F548907613A5EDBCD6806ABE5A4D7FF26)

This API provides the blur effect for static images. To provide the real-time blur effect for components, use [dynamic blur](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-blur-effect).

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | number | Yes | Blur radius, in pixels. The blur effect is proportional to the configured value. A larger value indicates a more obvious effect. |
| tileMode | [TileMode](#tilemode14) | Yes | Tile mode of the shader effect. The blur effect of image edges is affected. Currently, only CPU rendering is supported. Therefore, the tile mode supports only DECAL. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageBlur(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let radius = 30;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.blur(radius, effectKit.TileMode.DECAL);
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/-1nkKnhxSLG6agkcYcrsJQ/en-us_image_0000002568766135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63BF8DDDA56C59BF66B8390D4803B01CDDBD5A803213B9DDBFB9E5C93D5235AE)

#### \[h2\]invert12+

invert(): Filter

Adds the inversion effect to the filter linked list, and returns the head node of the linked list.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageInvert(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.invert();
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageInvert(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/LVnYXD7vS4mkZ6P0ww9sPA/en-us_image_0000002537766410.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49B57788840103A6E4AE5BB883B55172C5B343C2C42540A21C05FB337D4B63D7)

#### \[h2\]setColorMatrix12+

setColorMatrix(colorMatrix: Array<number>): Filter

Adds a custom effect to the filter linked list, and returns the head node of the linked list.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorMatrix | Array<number> | Yes | 
Custom color matrix.

A 5 x 4 matrix can be created. The value range of the matrix element is \[0, 1\], where **0** indicates that the color channel is not involved in the calculation, and **1** indicates that the color channel is involved in the calculation and retains the original weight.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Input parameter error. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageColorFilter(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let colorMatrix:Array<number> = \[
      0.2126,0.7152,0.0722,0,0,
      0.2126,0.7152,0.0722,0,0,
      0.2126,0.7152,0.0722,0,0,
      0,0,0,1,0
      \];
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.setColorMatrix(colorMatrix);
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageColorFilter(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

#### \[h2\]brightness

brightness(bright: number): Filter

Adds the brightness effect to the filter linked list, and returns the head node of the linked list.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bright | number | Yes | Brightness value, ranging from 0 to 1. When the value is **0**, the image brightness remains unchanged. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageBrightness(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let bright = 0.5;
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.brightness(bright);
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageBrightness(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/S34--b5GQ5q2jHB2Gkuy2g/en-us_image_0000002537926350.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ED1041391615A28BE0D213D4B077CDE39C72A0F737D17E9AF453E92306DA700)

#### \[h2\]grayscale

grayscale(): Filter

Adds the grayscale effect to the filter linked list, and returns the head node of the linked list.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [Filter](#filter) | Final image effect. |

**Example**

import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
// Pass the image data to be read.
function ImageGrayscale(Image: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(Image);
    imageSource.createPixelMap().then(async (pixelMap: image.PixelMap) => {
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // Add an effect flag to the image.
        headFilter.grayscale();
      }
      // Process the image based on the added effect flag and return the processed image data.
      headFilter.getEffectPixelMap().then(imageData => {
        resolve(imageData);
      })
    })
  })
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // Read the image file in the rawfile folder. You can also change the read mode as required to ensure that the image data in ArrayBuffer format is obtained.
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try{
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    }catch (err){
      return undefined
    }
  }

  async aboutToAppear(): Promise<void>{
    this.imageBuffer = await this.getFileBuffer();
    if(this.imageBuffer == undefined){
      return;
    }
    // Image processing is an asynchronous operation. You can perform the next step based on whether the processed image data needs to be obtained. Add await as required for synchronization.
    this.imagePixelMap = await ImageGrayscale(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/WndvFx3bR06kmyqPAejytQ/en-us_image_0000002568686127.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D53CBE12562F7A54175AE598D2C0A28B0D513CD6BE72AD4B5183C1E2C7FCE84)

#### \[h2\]getEffectPixelMap11+

getEffectPixelMap(): Promise<image.PixelMap>

Obtains **image.PixelMap** of the source image to which the filter linked list is added. This API uses a CPU for rendering and a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<image.PixelMap> | Promise used to return **image.PixelMap** of the source image. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap().then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  })
})

#### \[h2\]getEffectPixelMap20+

getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>

Obtains the **image.PixelMap** of the source image with the linked list effect. The rendering mode (CPU rendering or GPU rendering) can be specified. This API uses a promise to return the result.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Image.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| useCpuRender | boolean | Yes | Rendering mode. **true**: CPU rendering. **false**: GPU rendering. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return **image.PixelMap** of the source image. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  effectKit.createEffect(pixelMap).grayscale().getEffectPixelMap(false).then(data => {
    console.info('getPixelBytesNumber = ', data.getPixelBytesNumber());
  })
})

#### \[h2\]getPixelMap(deprecated)

getPixelMap(): image.PixelMap

Obtains **image.PixelMap** of the source image to which the filter linked list is added.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/vfSpYuvKToaUFMWPPQVxEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062446Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=173B7C11DC70235575D9A68F212AB2DBB82B1C4CC5CE4A7533C40C0D3D75346B)

This API is supported since API version 9 and deprecated since API version 11. Use [getEffectPixelMap](#geteffectpixelmap11) instead.

**System capability**: SystemCapability.Multimedia.Image.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | **image.PixelMap** of the source image. |

**Example**

import { image } from "@kit.ImageKit";
import { effectKit } from "@kit.ArkGraphics2D";

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
};
image.createPixelMap(color, opts).then((pixelMap) => {
  let pixel = effectKit.createEffect(pixelMap).grayscale().getPixelMap();
  console.info('getPixelBytesNumber = ', pixel.getPixelBytesNumber());
})
