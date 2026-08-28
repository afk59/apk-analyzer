# @ohos.file.AlbumPickerComponent (AlbumPickerComponent)

The **AlbumPickerComponent** embedded in the UI of an application allows the application to access the albums in the user directory without any permission.

This component must be used together with [PhotoPickerComponent](../ohos-file-photopickercomponent-photopickercomponent/document.md). When a user selects an album by using the **AlbumPickerComponent**, the **PhotoPickerComponent** is instructed to update the images and videos in the album.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/AISYJQQeSP6mEDqg4K3few/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88C880EEBDF902F92017EDBA823AE3651901A177534BE4D9B4941DC3F450E3B5)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, photoAccessHelper, EmptyAreaClickCallback } from '@kit.MediaLibraryKit';

#### Attributes

The [universal attributes](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### AlbumPickerComponent

AlbumPickerComponent( {albumPickerOptions?: AlbumPickerOptions, onAlbumClick?: (albumInfo: AlbumInfo) => boolean, onEmptyAreaClick?: EmptyAreaClickCallback, albumPickerController?: AlbumPickerController })

Allows the application to access the albums in the user directory without any permission.

**Decorator**: @Component

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| albumPickerOptions | [AlbumPickerOptions](#albumpickeroptions) | No | 
**AlbumPicker** configuration.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onAlbumClick | (albumInfo: [AlbumInfo](#albuminfo)) => boolean | No | 

Callback used to return the album URI when an album is selected by a user. No special processing is performed on the return value.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onEmptyAreaClick13+ | [EmptyAreaClickCallback](#emptyareaclickcallback13) | No | 

Callback to be invoked when the blank area of the **AlbumPickerComponent** is tapped, which is used to notify the application of the tap.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| albumPickerController20+ | [AlbumPickerController](#albumpickercontroller20) | No | 

A controller that enables applications to send data to the **AlbumPickerComponent**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### AlbumPickerOptions

Represents the **AlbumPicker** configuration.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| themeColorMode | [PickerColorMode](../ohos-file-photopickercomponent-photopickercomponent/document.md#pickercolormode) | No | Yes | 
Theme color of the album page. The options are **AUTO**, **Light**, and **Dark**. The default value is **AUTO**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| filterType13+ | [photoAccessHelper.PhotoViewMIMETypes](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photoviewmimetypes) | No | Yes | 

Type of the filter. You can use it to display images, videos, or both. If this parameter is not specified, images and videos are displayed in a specific album.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| fontSize20+ | number | string | No | Yes | 

Font size. For details about the value range, see [fontSize](../../../../application-framework/arkui/arkts-components/text-and-input/text/document.md#fontsize).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### EmptyAreaClickCallback13+

type EmptyAreaClickCallback = () => void

Called when the blank area of the **AlbumPickerComponent** is tapped.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### AlbumInfo

Represents album information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | Yes | Album URI. |
| albumName | string | No | Yes | Album name. |

#### AlbumPickerController20+

A controller that enables applications to send data to the **AlbumPickerComponent**.

**Decorator Type**: @Observed

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### \[h2\]setFontSize20+

setFontSize(fontSize: number | string): void

Sets the font size of the album list.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fontSize | number | string | Yes | Font size. For details about the value range, see [fontSize](../../../../application-framework/arkui/arkts-components/text-and-input/text/document.md#fontsize). |

#### Example

// xxx.ets
import { AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, PickerColorMode, photoAccessHelper, EmptyAreaClickCallback } from '@kit.MediaLibraryKit';

@Entry
@Component
struct PickerDemo {
  albumPickerOptions: AlbumPickerOptions = new AlbumPickerOptions();
  private emptyAreaClickCallback: EmptyAreaClickCallback = (): void => this.onEmptyAreaClick();

  aboutToAppear() {
    this.albumPickerOptions.themeColorMode = PickerColorMode.AUTO;
    this.albumPickerOptions.filterType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
  }
  
  private onAlbumClick(albumInfo: AlbumInfo): boolean {
    if (albumInfo?.uri) {
      // pickerController instructs PhotoPickerComponent to refresh data.
    }
    if (albumInfo?.albumName) {
      // Perform subsequent processing based on the obtained albumName.
    }
    return true;
  }
  
  private onEmptyAreaClick(): void {
    // Callback when the blank area of the component is tapped.
  }

  build() {
    Stack() {
      AlbumPickerComponent({
        albumPickerOptions: this.albumPickerOptions,
        onAlbumClick:(albumInfo: AlbumInfo): boolean => this.onAlbumClick(albumInfo),
        onEmptyAreaClick: this.emptyAreaClickCallback,
      }).height('100%').width('100%')
    }
  }
}
