# @ohos.file.RecentPhotoComponent (RecentPhotoComponent)

The RecentPhotoComponent embedded in the UI of an application allows the application to access the recent image or video in the user directory without the required permission. This component grants the application only the read permission.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Fhm3e7LXSbSy5S4tlDBb4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B798776086E8EE6BE80D1457882F6572C754C7015B449861FEBB9495C5B485A2)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {
  RecentPhotoComponent, RecentPhotoOptions, RecentPhotoCheckResultCallback,
  RecentPhotoClickCallback, PhotoSource, RecentPhotoInfo,
  RecentPhotoCheckInfoCallback
} from '@ohos.file.RecentPhotoComponent';

#### Properties

The [universal properties](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### RecentPhotoComponent

RecentPhotoComponent({ recentPhotoOptions?: RecentPhotoOptions, onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback, onRecentPhotoClick: RecentPhotoClickCallback, onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback, })

Allows an application to access the latest image or video file in the public directory to access the recent image or video in the user directory without the media access permission.

**Decorator**: @Component

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recentPhotoOptions | [RecentPhotoOptions](#recentphotooptions) | No | 
Configuration of the recent image or video.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onRecentPhotoCheckResult | [RecentPhotoCheckResultCallback](#recentphotocheckresultcallback) | No | 

Callback used to return the query result of the recent image or video.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onRecentPhotoClick | [RecentPhotoClickCallback](#recentphotoclickcallback) | Yes | 

Callback to be invoked when the recent image or video is selected.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onRecentPhotoCheckInfo13+ | [RecentPhotoCheckInfoCallback](#recentphotocheckinfocallback13) | No | 

Callback used to return information about the recent image or video obtained.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### RecentPhotoOptions

Represents the configuration of the recent image or video.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| period | number | No | Yes | 
Time period for displaying the latest image sorted by creation time, in seconds. The longest duration you can set is 1 day (86400s).

If the value is less than or equal to 0, greater than 86400, or not set, the most recent photos over the longest period of up to one day is displayed by default. If there is no image or video in the specified period, the component is not displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| MIMEType | [photoAccessHelper.PhotoViewMIMETypes](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photoviewmimetypes) | No | Yes | 

Types of the file displayed. The default value is **PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| photoSource | [PhotoSource](#photosource) | No | Yes | 

Source of the recent image or video, for example, image or video taken by the camera or screenshot. By default, the source is not restricted.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isAutoRefreshSupported20+ | boolean | No | Yes | 

Whether the **RecentPhotoComponent** automatically refreshes when there are changes (including additions, deletions, or modifications) to the recent images or videos that meet the requirements.

If the component's originally displayed image or video is deleted and there are no other images or videos that meet the requirements, a placeholder is displayed and the component does not automatically close.

The default value is **false**, indicating that the component does not automatically refresh. If this parameter is set to **true**, all images are displayed, and the **period** parameter is invalid.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| colorMode20+ | [PickerColorMode](../ohos-file-photopickercomponent-photopickercomponent/document.md#pickercolormode) | No | Yes | 

Color mode of the placeholder.

This setting is used when **isAutoRefreshSupported** is set to **true** and no recent image or video meets the requirements, showing a placeholder instead.

By default, it follows the system's dark/light color mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### RecentPhotoInfo13+

Represents information about the recent image or video.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dateTaken | number | No | Yes | Time when the recent image or video is taken, in ms. The value is the number of milliseconds elapsed since the Unix epoch (00:00:00 UTC on January 1, 1970). |
| identifier | string | No | Yes | Hash value of the name of the recent image or video, which is used to help the application determine whether the image or video to be displayed is the same as the one displayed before. |

#### RecentPhotoCheckResultCallback

type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void

Called to return the query result of the recent image or video.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recentPhotoExists | boolean | Yes | Whether the recent image or video exists. **true** if it exists, **false** otherwise. The default value is **true**. |

#### RecentPhotoClickCallback

type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean

Called when the recent image or video is selected.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recentPhotoInfo | [BaseItemInfo](../ohos-file-photopickercomponent-photopickercomponent/document.md#baseiteminfo) | Yes | Information about the recent image or video. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Processing result of the recent image or video. The value **true** means that the processing is complete. |

#### RecentPhotoCheckInfoCallback13+

type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void

Called to return whether the recent image or video exists and the information about it.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| recentPhotoExists | boolean | Yes | Whether the recent image or video exists. **true** if it exists, **false** otherwise. The default value is **true**. |
| info | [RecentPhotoInfo](#recentphotoinfo13) | Yes | Information about the recent image or video. |

#### PhotoSource

Enumerates the sources of the image or video data.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | Image or video from all sources. |
| CAMERA | 1 | Image or video taken by the camera. |
| SCREENSHOT | 2 | Screenshot or screen capture video. |

#### Example

// xxx.ets
import {
  RecentPhotoComponent,
  RecentPhotoOptions,
  PhotoSource,
  RecentPhotoCheckResultCallback,
  RecentPhotoClickCallback,
  RecentPhotoInfo,
  RecentPhotoCheckInfoCallback,
} from '@ohos.file.RecentPhotoComponent';
import {
  photoAccessHelper,
  BaseItemInfo
} from '@kit.MediaLibraryKit'

@Entry
@Component
struct PickerDemo {
  private recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions();
  private recentPhotoCheckResultCallback: RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => this.onRecentPhotoCheckResult(recentPhotoExists);
  private recentPhotoClickCallback: RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo);
  private recentPhotoCheckInfoCallback: RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => this.onRecentPhotoCheckInfo(recentPhotoExists, info);

  aboutToAppear() {
    this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
    this.recentPhotoOptions.period = 30;
    this.recentPhotoOptions.photoSource = PhotoSource.ALL;
  }

  private onRecentPhotoCheckResult(recentPhotoExists: boolean): void {
    // Image or video that meets the search criteria exists.
    if (recentPhotoExists) {
      console.info('The photo is exist.');
    }
  }

  private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {
    // Return the image or video.
    if (recentPhotoInfo) {
      console.info('The photo uri is ' + recentPhotoInfo.uri);
      return true;
    }
    return true;
  }

  private onRecentPhotoCheckInfo(recentPhotoExists: boolean, info: RecentPhotoInfo): void {
    // Check whether an image or video that meets the conditions exists. If yes, obtain information about the image or video.
  }

  build() {
    Stack() {
      RecentPhotoComponent({
        recentPhotoOptions: this.recentPhotoOptions,
        onRecentPhotoCheckResult: this.recentPhotoCheckResultCallback,
        onRecentPhotoClick: this.recentPhotoClickCallback,
        onRecentPhotoCheckInfo: this.recentPhotoCheckInfoCallback,
      }).height('100%').width('100%')
    }
  }
}
