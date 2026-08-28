# How do I read photos in an album?

Using the **photoAccessHelper.PhotoSelectOptions** API to read photos in an album.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  @State getAlbum: string = 'Display photos in album';
  @State pixel: image.PixelMap | undefined = undefined;
  @State albumPath: string = '';
  @State photoSize: number = 0;

  async getPictureFromAlbum() {
    // Pull up the album and select the pictures
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
    PhotoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
    this.albumPath = photoSelectResult.photoUris\[0\];

    // Read the image as a buffer
    const file = fs.openSync(this.albumPath, fs.OpenMode.READ\_ONLY);
    this.photoSize = fs.statSync(file.fd).size;
    console.info('Photo Size: ' + this.photoSize);
    let buffer = new ArrayBuffer(this.photoSize);
    fs.readSync(file.fd, buffer);
    fs.closeSync(file);

    // Decoding into PixelMap
    const imageSource = image.createImageSource(buffer);
    console.log('imageSource: ' + JSON.stringify(imageSource));
    this.pixel = await imageSource.createPixelMap({});
  }

  build() {
    Row() {
      Column() {
        Image(this.pixel)
          .width('100%')
          .aspectRatio(1)
        Button('Show Photo')
          .onClick(() => {
            this.getPictureFromAlbum();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
