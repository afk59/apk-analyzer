# How do I edit and crop photos in an album?

You can edit and crop an image by using the APIs of the [pixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) class of the [image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-image) module.

The APIs include:

-   [pixelMap.crop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9): used to crop an image based on the input size.
-   [pixelMap.opacity](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#opacity9): used to set the opacity of an image by setting the opacity rate.
-   [pixelMap.scale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#scale9): used to resize an image based on the input width and height.
-   [pixelMap.rotate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#rotate9): used to rotate an image based on the input angle.
-   [pixelMap.flip](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#flip9): used to flip an image based on the input conditions.

The following sample code uses [pixelMap.crop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9) to crop an image:

// Crop 4:3
class RegionItem {
  /\*\*
   \* width coordinate.
   \*/
  x: number;

  /\*\*
   \* height coordinate.
   \*/
  y: number;

  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

export async function cropCommon(pixelMap: PixelMap, cropWidth: number, cropHeight: number, cropPosition: RegionItem) {
  pixelMap.crop({
    size: {
      width: cropWidth,
      height: cropHeight
    },
    x: cropPosition.x,
    y: cropPosition.y
  });
}

// Pass in three parameters: image. PixelMap, image width, and image height. After obtaining the cropped image width and height,
// pass the parameters into the cropCommon method
export async function banner(pixelMap: PixelMap, width: number, height: number) {
  if (width <= height) {
    const cropWidth = width;
    const cropHeight = Math.floor(width \* 0.75);
    const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
    cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
    return;
  }
  if (width \* 0.75 >= height) {
    const cropWidth = Math.floor(height / 0.75);
    const cropHeight = height;
    const cropPosition = new RegionItem(Math.floor((width - cropWidth) / 2), 0);
    cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
    return;
  }
  const cropWidth = width;
  const cropHeight = Math.floor(width \* 0.75);
  const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
  cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
}
