# @ohos.file.PhotoPickerComponent (PhotoPickerComponent)

You can embed the **PhotoPickerComponent** in your application's layout to let users pick images or videos without requiring extra permissions. Once the users have made their selection, your application gets read-only access to the chosen images or videos.

Note that the **PhotoPickerComponent** does not support nesting. Additionally, avoid overlaying components with the **overlay** attribute on top of the **PhotoPickerComponent**, as this will prevent the **PhotoPickerComponent** from receiving gesture events.

Once embedded, users can directly select images or videos within the **PhotoPickerComponent**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/PcwlW8wXQHKBQ5eEmPHxug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44D85B4E0E485555E68E2D0EAF5555B7C8B12717A3ED5CF70E0FBEC0D91AE079)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import {
  PhotoPickerComponent, PickerController, PickerOptions,
  DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, ItemType, ClickType,
  MaxCountType, PhotoBrowserRange, PhotoBrowserUIElement,
  ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, SingleLineConfig,
  BadgeConfig, PreselectedInfo, SaveMode, BadgeType, ItemDisplayRatio,VideoPlayerState
} from '@ohos.file.PhotoPickerComponent';

#### Attributes

The [universal attributes](../../../../application-framework/arkui/arkts-components/universal-attributes/document.md) are supported.

#### PhotoPickerComponent

PhotoPickerComponent({ pickerOptions?: PickerOptions, onSelect?: (uri: string) => void, onDeselect?: (uri: string) => void, onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean, onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean, onPickerControllerReady?: () => void, onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean, onSelectedItemsDeleted?: ItemsDeletedCallback, onExceedMaxSelected?: ExceedMaxSelectedCallback, onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback, onVideoPlayStateChanged?: videoPlayStateChangedCallback, pickerController: PickerController })

Allows the application to access images or videos in the user directory without any permission.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/4cXfIOROQ8ql6fp6gcpn4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B32FB8F812938C4461F9DC034CA5CFA125D40FEA4CE2A2D942639A6F12C2AC08)

If the **PhotoPickerComponent** is used with the **Tabs** component, the swipe gestures of the **Tabs** component conflict with those of the photo browser page.

To prevent this problem, you can disable the swipe operation for the **Tabs** component in **onEnterPhotoBrowser()** and enable it in **onExitPhotoBrowser()**. This conflict will be resolved in later versions.

**Decorator**: @Component

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Decorator Type | Description |
| :-- | :-- | :-- | :-- | :-- |
| pickerOptions | [PickerOptions](#pickeroptions) | No | \- | 
Picker configuration parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onSelect | (uri: string) => void | No | \- | 

Callback to be invoked when an image is selected by using **PhotoPickerComponent**. This callback returns the URI of the image selected to the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onDeselect | (uri: string) => void | No | \- | 

Callback to be invoked when an image is deselected by using **PhotoPickerComponent**. This callback returns the URI of the image deselected to the application.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onItemClicked | (itemInfo: [ItemInfo](#iteminfo), clickType: [ClickType](#clicktype)) => boolean | No | \- | 

Callback to be invoked when an item in a **PhotoPickerComponent** is clicked.

For an image (thumbnail item), if **true** is returned, the image is selected. Otherwise, the image is not selected and the URI is not granted with the permission. For a camera item, if **true** is returned, the system camera is started. Otherwise, the camera is not started and the application handles the request.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onEnterPhotoBrowser | (photoBrowserInfo: [PhotoBrowserInfo](#photobrowserinfo)) => boolean | No | \- | 

Callback to be invoked when the photo browser page is displayed. The callback returns photo browser information to the application. No special processing is performed on the return value.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onExitPhotoBrowser | (photoBrowserInfo: [PhotoBrowserInfo](#photobrowserinfo)) => boolean | No | \- | 

Callback to be invoked when the photo browser page exits. The callback returns photo browser information to the application. No special processing is performed on the return value.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onPickerControllerReady | () => void | No | \- | 

Callback to be invoked when **pickerController** is available.

The **PickerController** APIs can be called only after this callback is invoked.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onPhotoBrowserChanged | (browserItemInfo: [BaseItemInfo](#baseiteminfo)) => boolean | No | \- | 

Callback to be invoked when the photo browser page is swiped left or right. The callback returns photo browser information to the application. The setting takes effect only in multi-selection mode. No special processing is performed on the return value.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onSelectedItemsDeleted13+ | [ItemsDeletedCallback](#itemsdeletedcallback13) | No | \- | 

Callback to be invoked when the selected items are deleted. This callback returns information about the deleted items to the application.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| onExceedMaxSelected13+ | [ExceedMaxSelectedCallback](#exceedmaxselectedcallback13) | No | \- | 

Callback to be invoked when the number of selected media assets exceeds the limit (maximum number of selected images, selected videos, or selected items).

\- If the number of selected images reaches the maximum but does not reach the maximum count of selected items, **exceedMaxCountType** in the callback is [MaxCountType](#maxcounttype).PHOTO\_MAX\_COUNT.

\- If the number of selected videos reaches the maximum but does not reach the maximum count of selected items, **exceedMaxCountType** in the callback is [MaxCountType](#maxcounttype).VIDEO\_MAX\_COUNT.

\- If the number of selected media assets reaches the maximum count of selected items, **exceedMaxCountType** in the callback is [MaxCountType](#maxcounttype).TOTAL\_MAX\_COUNT.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| onCurrentAlbumDeleted13+ | [CurrentAlbumDeletedCallback](#currentalbumdeletedcallback13) | No | \- | 

Callback to be invoked when the current album is deleted.

The album is specified by **currentAlbumUri** in pickerController.[setData](#setdata)([DataType](#datatype).SET\_ALBUM\_URI, currentAlbumUri).

To refresh the grid page to display the default album after the current album is deleted, you can set the title bar name to the default album name, for example, **Photos and videos**, **Photos**, or **Videos**, and call pickerController.[setData](#setdata)([DataType](#datatype).SET\_ALBUM\_URI, '') with an empty string.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| onVideoPlayStateChanged14+ | [videoPlayStateChangedCallback](#videoplaystatechangedcallback14) | No | \- | 

Callback to be invoked when the video playback state on a photo browser page changes.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| pickerController | [PickerController](#pickercontroller) | Yes | @ObjectLink | 

Instance used to send data to the **PhotoPickerComponent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onMovingPhotoBadgeStateChanged22+ | [MovingPhotoBadgeStateChangedCallback](#movingphotobadgestatechangedcallback22) | No | \- | 

Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled. This callback reports the image's URI and its new moving photo badge state to the application.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### PickerOptions

Describes the configuration of a Picker. It inherits from [photoAccessHelper.BaseSelectOptions](../../arkts-apis/ohos-file-photoaccesshelper-album-management/classes-others/document.md#baseselectoptions).

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| checkBoxColor | string | No | Yes | 
Background color of the check box. The value is an 8-digit hexadecimal color code.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor | string | No | Yes | 

Background color of the Picker grid page. The value is an 8-digit hexadecimal color code.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isRepeatSelectSupported | boolean | No | Yes | 

Whether a single image can be repeatedly selected. The value **true** means that a single image can be repeatedly selected. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| checkboxTextColor | string | No | Yes | 

Text color in the check box. The value is an 8-digit hexadecimal color code. (This parameter is supported since API version 19. In earlier versions, the system defaults to white.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| photoBrowserBackgroundColorMode | [PickerColorMode](#pickercolormode) | No | Yes | 

Background color of the photo browser page. The options are **AUTO**, **LIGHT**, and **DARK**. The default value is **AUTO**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxSelectedReminderMode | [ReminderMode](#remindermode) | No | Yes | 

Mode of the reminder when the number of selected items reaches the maximum. The options are **NONE**, **TOAST**, and **MASK**. The default value **TOAST**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| orientation | [PickerOrientation](#pickerorientation) | No | Yes | 

Sliding preview direction of the grid page. The options are **HORIZONTAL** and **VERTICAL**. The default value is **VERTICAL**. (This parameter is supported since API version 20. In earlier versions, the system defaults to vertical.)

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectMode | [SelectMode](#selectmode) | No | Yes | 

Select mode, which can be **SINGLE\_SELECT** or **MULTI\_SELECT**. The default value is **MULTI\_SELECT**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxPhotoSelectNumber | number | No | Yes | 

Maximum number of images that can be selected. The maximum value is **500**, which is limited by **MaxSelected**. The default value is **500**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| maxVideoSelectNumber | number | No | Yes | 

Maximum number of videos that can be selected. The maximum value is **500**, and it is restricted by the maximum number of media files that can be selected in the system. The default value is **500**.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isSlidingSelectionSupported13+ | boolean | No | Yes | 

Whether sliding selection (selecting multiple items by sliding finger across the screen) is supported. The value **true** means that sliding selection is supported. The default value is **false**. This parameter is not available for repeat selection.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| photoBrowserCheckboxPosition13+ | \[number, number\] | No | Yes | 

Position of the check box on the photo browser page. The first parameter specifies the offset in the X direction, and the second parameter specifies the offset in the Y direction. The value range is \[0, 1\], which indicates the offset (from 0% to 100%) to the upper-left corner of the component. The default value is \[0, 0\].

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| gridMargin14+ | [Margin](../../../../application-framework/arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#margin) | No | Yes | 

Margin of the component on a grid page.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| photoBrowserMargin14+ | [Margin](../../../../application-framework/arkui/arkts-components/universal-attributes/layout-and-borders/sizing/document.md#margin) | No | Yes | 

Margin of the component on a photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| singleLineConfig20+ | [SingleLineConfig](#singlelineconfig20) | No | Yes | 

Single-line display mode of a grid page. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| uiComponentColorMode20+ | [PickerColorMode](#pickercolormode) | No | Yes | 

Picker color mode. Dark/Light color mode (excluding the background color) of other components on the Picker grid page, including the search box, camera entry, safety tips for using Gallery, and recommendation bubble. This attribute is usually used together with **backgroundColor**. The default value is **PickerColorMode.AUTO**, which follows the system's dark/light color mode.

When setting this attribute, avoid using **PickerColorMode.LIGHT** with a dark backgroundColor, as it may make components or text hard to see. Avoid using **PickerColorMode.DARK** with a light backgroundColor for the same reason.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| gridStartOffset20+ | number | No | Yes | 

Space between the top of the component and the first row of the grid thumbnail. The default value is **0**, in vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| gridEndOffset20+ | number | No | Yes | 

Space between the bottom of the component and the last row of the grid thumbnail. The default value is **0**, in vp.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| pickerIndex21+ | number | No | Yes | 

Unique serial number used to distinguish different picker components. The default value is **\-1**, indicating that no distinction is made.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| preselectedInfos21+ | Array<[PreselectedInfo](#preselectedinfo21)\> | No | Yes | 

Array of information previously selected by the user, so that the PhotoPickerComponent identified by **pickerIndex** can display the information.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| badgeConfig21+ | [BadgeConfig](#badgeconfig21) | No | Yes | 

Badge configuration. Currently, the **PhotoPickerComponent** supports only one type of badge. For details, see [BadgeType](#badgetype21).

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### ItemsDeletedCallback13+

type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void

Called when the selected items are deleted.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| baseItemInfos | Array<[BaseItemInfo](#baseiteminfo)\> | Yes | Basic information about the selected items. |

#### ExceedMaxSelectedCallback13+

type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void

Called when items are selected after the maximum count has been reached.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| exceedMaxCountType | [MaxCountType](#maxcounttype) | Yes | Type of the maximum count that has been reached. It can be the maximum count of selected images, maximum count of selected videos, or maximum count of selected images and videos. |

#### CurrentAlbumDeletedCallback13+

type CurrentAlbumDeletedCallback = () => void

Called when the current album is deleted.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### videoPlayStateChangedCallback14+

type videoPlayStateChangedCallback = (state: VideoPlayerState) => void

Callback to be invoked when the video playback state on a photo browser page changes.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| state | [VideoPlayerState](#videoplayerstate14) | Yes | Enumerates the video playback states. |

#### MovingPhotoBadgeStateChangedCallback22+

type MovingPhotoBadgeStateChangedCallback = (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void

Callback to be invoked when the moving photo effect of the **PhotoPickerComponent** is enabled or disabled.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the moving photo. |
| state | [photoAccessHelper.MovingPhotoBadgeStateType](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#movingphotobadgestatetype22) | Yes | State of the moving photo badge. |

#### PickerController

Defines an instance used to send data to the **PhotoPickerComponent**.

**Decorator Type**: @Observed

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### \[h2\]setData

setData(dataType: DataType, data: Object): void

Sends data of the specified type to the **PhotoPickerComponent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataType | [DataType](#datatype) | Yes | Type of the data to send. |
| data | Object | Yes | Data to send. |

#### \[h2\]addData21+

addData(dataType: DataType, data: Object): void

Sends additional configuration data to the **PhotoPickerComponent**. The [DataType](#datatype) parameter identifies the type of data to send, and only the **SET\_BADGE\_CONFIGS** type is supported currently.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataType | [DataType](#datatype) | Yes | Type of additional configuration data to send. |
| data | Object | Yes | Additional configuration data to send. |

#### \[h2\]deleteData21+

deleteData(dataType: DataType, data: Object): void

Sends removal configuration data to the **PhotoPickerComponent**. The [DataType](#datatype) parameter identifies the type of data to send, and only the **SET\_BADGE\_CONFIGS** type is supported currently.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dataType | [DataType](#datatype) | Yes | Type of removal configuration data to send. |
| data | Object | Yes | Removal configuration data to send. |

#### \[h2\]setMaxSelected

setMaxSelected(maxSelected: MaxSelected): void

Sets the maximum number of images, videos, or images and videos that can be selected on a real-time basis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| maxSelected | [MaxSelected](#maxselected) | Yes | Maximum number of media assets that can be selected at a time. |

#### \[h2\]setPhotoBrowserItem

setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void

Switches from the **PhotoPickerComponent** to the photo browser page or from the photo browser page to the image to be viewed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the image to view. Only the images selected by the user are supported. |
| photoBrowserRange | [PhotoBrowserRange](#photobrowserrange) | No | View range on the photo browser page. The value can be **ALL** or **SELECTED\_ONLY**. The default value is **ALL**, which means to view all images and videos. |

#### \[h2\]exitPhotoBrowser13+

exitPhotoBrowser(): void

Exits the photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### \[h2\]setPhotoBrowserUIElementVisibility13+

setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void

Sets whether other UI elements are visible on the photo browser page. By default, other UI elements are visible.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elements | Array<[PhotoBrowserUIElement](#photobrowseruielement13)\> | Yes | Other UI elements on the photo browser page. |
| isVisible | boolean | Yes | Whether the specified UI elements are visible. The value **true** means that they are visible. The default value is **false**. |

#### \[h2\]replacePhotoPickerPreview15+

replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void

Replaces the image selected by the user in the **PhotoPickerComponent** with the image edited by the application.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| originalUri | string | Yes | URI of the original image, which will be replaced. |
| newUri | string | Yes | URI of the new image. The new image is temporarily stored in the application sandbox path. Therefore, this URI specifies a directory in the application sandbox path. |
| callback | AsyncCallback<void> | Yes | Callback invoked when image replacement is complete. |

#### \[h2\]saveTrustedPhotoAssets15+

saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void

Saves files in a URI list. Generally, this API is used together with [replacePhotoPickerPreview](#replacephotopickerpreview15) to save the new images or videos in the application sandbox path to Gallery.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| trustedUris | Array<string> | Yes | URIs of the images or videos in the application sandbox path. Generally, **trustedUris** comes from **newUri** of new images generated by [replacePhotoPickerPreview](#replacephotopickerpreview15). |
| callback | AsyncCallback<Array<string>> | Yes | URIs of the new files in Gallery. |
| configs | Array<[photoAccessHelper.PhotoCreationConfig](../../arkts-apis/ohos-file-photoaccesshelper-album-management/interfaces-others/document.md#photocreationconfig12)\> | No | 
Configuration parameters corresponding to the original files.

**NOTE**

If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can be saved.

By default, the values of **title**, **fileNameExtension**, and **photoType** of **mediaItem** corresponding to **trustedUris** are used, and the value of **subtype** is fixed to **DEFAULT**.

 |
| saveMode | [SaveMode](#savemode15) | No | 

Mode for saving the files.

By default, the **SAVE\_AS** mode is used to save the files as new files.

 |

#### \[h2\]updatePickerOptions22+

updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>

Updates the attributes of the **PhotoPickerComponent**. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| updateConfig | [UpdatablePickerConfigs](#updatablepickerconfigs22) | Yes | New attributes, which are a subset of [PickerOptions](#pickeroptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

#### BaseItemInfo

Represents basic image and video information.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | Yes | 
URI of the image or video.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mimeType | string | No | Yes | 

MIME type of the image or video.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| width | number | No | Yes | 

Width of the image or video, in px.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| height | number | No | Yes | 

Height of the image or video, in px.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| size | number | No | Yes | 

Size of the image or video, in bytes.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| duration | number | No | Yes | 

Video duration, in milliseconds. For an image or a moving photo, the value **\-1** is returned.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| photoSubType21+ | [photoAccessHelper.PhotoSubtype](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photosubtype12) | No | Yes | 

Subtype of the photo. The options are **DEFAULT**, **MOVING\_PHOTO**, and **BURST**.

The default value is **DEFAULT (0)**.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| dynamicRangeType21+ | [photoAccessHelper.DynamicRangeType](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#dynamicrangetype12) | No | Yes | 

Dynamic range type of the media file. The options are **HDR** and **SDR**.

For moving photos, this parameter specifies the dynamic range type of the cover image.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| orientation21+ | number | No | Yes | 

Image or video direction information.

1: **TOP-left**: The image is not rotated.

2: **TOP-right**: The image is flipped horizontally.

3: **Bottom-right**: The image is rotated by 180°.

4: **Bottom-left**: The image is flipped vertically.

5: **Left-top**: The image is flipped horizontally and then rotated clockwise by 270°.

6: **Right-top**: The image is rotated clockwise by 90°.

7: **Right-bottom**: The image is vertically flipped and then rotated clockwise by 90°.

8: **Left-bottom**: The image is rotated clockwise by 270°.

Images with mirroring information retain their original width and height attributes regardless of rotation, whereas images without such information have these attributes updated to reflect the post-rotation dimensions.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| movingPhotoBadgeState22+ | [photoAccessHelper.MovingPhotoBadgeStateType](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#movingphotobadgestatetype22) | No | Yes | 

State of the moving photo badge.

This parameter is supported only when [ItemType](#itemtype) is set to **THUMBNAIL**. Otherwise, it is left empty.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| videoMode22+ | [photoAccessHelper.VideoMode](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#videomode22) | No | Yes | 

Log mode of a video file.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### ItemInfo

Represents the image and video information. It inherits from [BaseItemInfo](#baseiteminfo), adding the parameter **itemType**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| itemType | [ItemType](#itemtype) | No | Yes | Type of the item, which can be **THUMBNAIL** or **CAMERA**. |

#### PhotoBrowserInfo

Represents information about the photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| animatorParams | [AnimatorParams](#animatorparams) | No | Yes | Animation for entering or exiting the photo browser page. |

#### AnimatorParams

Animation parameters for entering or exiting the photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | Yes | Animation duration, in ms. |
| curve | [Curve](../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#curve) | [ICurve](../../../../application-framework/arkui/arkts-api/ui/ohos-curves-interpolation-calculation/document.md#icurve9) | string | No | Yes | Animation curve. |

#### MaxSelected

Represents the maximum number of media assets that can be selected at a time.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | Map<[MaxCountType](#maxcounttype), number> | No | Yes | Maximum number of media assets (images, videos, or both) that can be selected at a time. |

#### SingleLineConfig20+

Represents the single-line display mode. In single-line mode, the component does not provide functions for viewing a larger image. The component does not support callbacks related to large images, and the PickerController does not support APIs related to large images, making API calls ineffective.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| itemDisplayRatio | [ItemDisplayRatio](#itemdisplayratio20) | No | Yes | Aspect ratio for grid display. Both 1:1 and the original image aspect ratio are supported. The default value is 1:1. |
| itemBorderRadius | [Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length) | [BorderRadiuses](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#borderradiuses9) | [LocalizedBorderRadiuses](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#localizedborderradiuses12) | No | Yes | Rounded corner radius for grid items. |
| itemGap | [Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length) | No | Yes | Spacing between grid items. |

#### BadgeConfig21+

Describes the badge configuration.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| badgeType | [BadgeType](#badgetype21) | No | Yes | Badge type. |
| uris | Array<string> | No | Yes | URIs of the assets for the badge. |

#### PreselectedInfo21+

Describes the information about the preselected files and their corresponding **PhotoPickerComponent** index.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the preselected media file. |
| preselectablePickerIndex | number | No | Yes | Index of the **PhotoPickerComponent** that can be used in automatic selection. The default value is **\-1**, which allows automatic selection in any **PhotoPickerComponent**. |

#### UpdatablePickerConfigs22+

Describes the updatable attributes of the **PhotoPickerComponent**. These attributes are a subset of [PickerOptions](#pickeroptions).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mimeType | [photoAccessHelper.PhotoViewMIMETypes](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#photoviewmimetypes) | No | Yes | 
MIME types.

If this parameter is not specified, **IMAGE\_VIDEO\_TYPE** is used by default.

 |
| mimeTypeFilter | [photoAccessHelper.MimeTypeFilter](../../arkts-apis/ohos-file-photoaccesshelper-album-management/classes-others/document.md#mimetypefilter19) | No | Yes | 

Configuration for file type filtering. Multiple types can be specified.

\- When this parameter is set, the **mimeType** configuration automatically becomes invalid.

\- When this parameter is set, only media files of the configured filter type are displayed. You are advised to notify users that only images or videos of the specified type can be selected.

 |
| maxSelectNumber | number | No | Yes | 

Maximum number of media files that can be selected.

The maximum value is 500, and the default value is 50.

 |
| maxPhotoSelectNumber | number | No | Yes | 

Maximum number of images that can be selected (unit: number).

The maximum value is **500**, which is limited by **MaxSelected**. The default value is **500**.

 |
| maxVideoSelectNumber | number | No | Yes | 

Maximum number of videos that can be selected (unit: number).

The maximum value is **500**, and it is restricted by the maximum number of media files that can be selected in the system. The default value is **500**.

 |
| selectMode | [SelectMode](#selectmode) | No | Yes | 

Picker selection mode.

**SINGLE\_SELECT** or **MULTI\_SELECT**. The default value is **MULTI\_SELECT**.

 |
| singleSelectionMode | [photoAccessHelper.SingleSelectionMode](../../arkts-apis/ohos-file-photoaccesshelper-album-management/enums/document.md#singleselectionmode18) | No | Yes | Single selection mode. The default value is **SingleSelectionMode.BROWSER\_MODE**. |
| isRepeatSelectSupported | boolean | No | Yes | 

Whether a single image can be repeatedly selected.

**true** if supported, **false** otherwise. The default value is **false**.

 |
| preselectedUris | Array<string> | No | Yes | URIs of the selected images. |
| checkBoxColor | string | No | Yes | 

Background color of the check box.

The value is an 8-digit hexadecimal color code.

 |
| backgroundColor | string | No | Yes | 

Background color of the Picker grid page.

The value is an 8-digit hexadecimal color code.

 |
| checkboxTextColor | string | No | Yes | 

Text color in the check box.

The value is an 8-digit hexadecimal color code.

 |
| photoBrowserBackgroundColorMode | [PickerColorMode](#pickercolormode) | No | Yes | 

Background color of the photo browser page.

The options are **AUTO**, **LIGHT**, and **DARK**. The default value is **AUTO**.

 |
| uiComponentColorMode | [PickerColorMode](#pickercolormode) | No | Yes | 

Color mode of the Picker UI component.

Dark/Light color mode (excluding the background color) of other components on the Picker grid page, including the search box, camera entry, safety tips for using Gallery, and recommendation bubble. This attribute is usually used together with **backgroundColor**. The default value is **PickerColorMode.AUTO**, which follows the system's dark/light color mode.

When setting this attribute, avoid using **PickerColorMode.LIGHT** with a dark background color, as it may make components or text hard to see. Avoid using **PickerColorMode.DARK** with a light background color for the same reason.

 |

#### DataType

Enumerates the types of data sent from **PickerController** to the **PhotoPickerComponent**.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SET\_SELECTED\_URIS | 1 | 
Sends a list of selected items to instruct the **PhotoPickerComponent** to refresh the selection status. A string array needs to be passed in.

For example, after an image is deleted from an application's page, the application calls **setData()** to notify the **PhotoPickerComponent** of the remaining selected items. Then, the **PhotoPickerComponent** refreshes the check box status.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SET\_ALBUM\_URI | 2 | 

Sends the selected album to instruct the **PhotoPickerComponent** to refresh the album data. A string array needs to be passed in.

For example, after an album is selected from an application's page, the application calls **setData** to notify the **PhotoPickerComponent** of the URI of the selected album. Then, the **PhotoPickerComponent** refreshes the album data.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SET\_SELECTED\_INFO21+ | 3 | 

Sends the URI of the selected file and the index of the selected **PhotoPickerComponent**. If the index of a **PhotoPickerComponent** matches the one provided in the parameter, the selected file is automatically highlighted in that **PhotoPickerComponent**.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| SET\_BADGE\_CONFIGS21+ | 4 | 

Sends the badge configurations, which are of the [badgeConfig](#badgeconfig21) type and include a list of data with badge types and corresponding file URIs. Once configured, the badge of the configured type is displayed in the specified file.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### ItemType

Enumerates the types of the item clicked.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| THUMBNAIL | 0 | Image or video (thumbnail). |
| CAMERA | 1 | Camera item. |

#### ClickType

Enumerates the click operation types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SELECTED | 0 | Select (select an image or click a camera item). |
| DESELECTED | 1 | Deselect (deselect an image). |

#### PickerOrientation

Enumerates the sliding preview directions of the Picker grid page.

This capability can be configured since API version 20. If this capability is set since API version 12 to 19, the setting does not take effect and the default direction (vertical) is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| VERTICAL | 0 | Vertical direction. |
| HORIZONTAL | 1 | Horizontal direction. |

#### SelectMode

Enumerates the select modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SINGLE\_SELECT | 0 | Select a single option. |
| MULTI\_SELECT | 1 | Select multiple options. |

#### PickerColorMode

Enumerates the Picker color modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Same with the system. |
| LIGHT | 1 | Light mode. |
| DARK | 2 | Dark mode. |

#### ReminderMode

Enumerates the types of the reminder when the number of selected items reaches the maximum.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No reminder. |
| TOAST | 1 | Toast message. |
| MASK | 2 | Grayed-out hint. |

#### MaxCountType

Enumerates the types of the maximum count.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TOTAL\_MAX\_COUNT | 0 | Total number of media assets (images and videos) that can be selected. |
| PHOTO\_MAX\_COUNT | 1 | Total number of images that can be selected. The value cannot be greater than **Total\_MAX\_Count**. |
| VIDEO\_MAX\_COUNT | 2 | Total number of videos that can be selected. The value cannot be greater than **Total\_MAX\_Count**. |

#### PhotoBrowserRange

Enumerates the view range on the photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | View all images and videos. |
| SELECTED\_ONLY | 1 | View selected images and videos only. |

#### PhotoBrowserUIElement13+

Represents other UI elements except the image preview component on the photo browser page.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CHECKBOX | 0 | Check box on the photo browser page. |
| BACK\_BUTTON | 1 | **Back** button on the photo browser page. |

#### SaveMode15+

Enumerates the modes for saving images or videos.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SAVE\_AS | 0 | Saves the image or video as a new one. |
| OVERWRITE | 1 | Replaces the original image or video. After the replacements, you can roll back the saved content in Gallery to restore the original image or video. |

#### BadgeType21+

Enumerates the badge types.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BADGE\_UPLOADED | 0 | Uploaded. |

#### VideoPlayerState14+

Enumerates the video playback states.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PLAYING | 0 | The video is being played. |
| PAUSED | 1 | Video playback is paused. |
| STOPPED | 2 | Video playback is stopped. |
| SEEK\_START | 3 | Started dragging the progress bar. |
| SEEK\_FINISH | 4 | Finished dragging the progress bar. |

#### ItemDisplayRatio20+

Enumerates the aspect ratios for grid display in single-line display mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SQUARE\_RATIO | 0 | 1:1 ratio. |
| ORIGINAL\_SIZE\_RATIO | 1 | Original image aspect ratio. |

#### Example

// xxx.ets
import {
  PhotoPickerComponent,
  PickerController,
  PickerOptions,
  DataType,
  BaseItemInfo,
  ItemInfo,
  PhotoBrowserInfo,
  ItemType,
  ClickType,
  MaxCountType,
  PhotoBrowserRange,
  PhotoBrowserUIElement,
  ItemsDeletedCallback,
  ExceedMaxSelectedCallback,
  CurrentAlbumDeletedCallback,
  videoPlayStateChangedCallback,
  VideoPlayerState
} from '@ohos.file.PhotoPickerComponent';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct PickerDemo {
  pickerOptions: PickerOptions = new PickerOptions();
  @State pickerController: PickerController = new PickerController();
  @State selectUris: string\[\] = \[\];
  @State currentUri: string = '';
  @State isBrowserShow: boolean = false;
  private selectedItemsDeletedCallback: ItemsDeletedCallback =
    (baseItemInfos: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(baseItemInfos);
  private exceedMaxSelectedCallback: ExceedMaxSelectedCallback =
    (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType);
  private currentAlbumDeletedCallback: CurrentAlbumDeletedCallback = () => this.onCurrentAlbumDeleted();
  private videoPlayStateChangedCallback: videoPlayStateChangedCallback =
    (state: VideoPlayerState) => this.videoPlayStateChanged(state);
  private thumbnail: PixelMap\[\] = \[\];
  private assets: photoAccessHelper.PhotoAsset\[\] = \[\];

  aboutToAppear() {
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
    this.pickerOptions.maxSelectNumber = 5;
    this.pickerOptions.isSearchSupported = false;
    this.pickerOptions.isPhotoTakingSupported = false;
    this.pickerOptions.photoBrowserCheckboxPosition = \[0.5, 0.5\];
    // Other attributes
  }

  private onSelect(uri: string): void {
    // Add
    if (uri) {
      this.selectUris.push(uri);
    }
  }

  private onDeselect(uri: string): void {
    // Remove
    if (uri) {
      this.selectUris = this.selectUris.filter((item: string) => {
        return item != uri;
      })
    }
  }

  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // Click a camera item.
      return true; // If true is returned, the system camera is started. If false is returned, the app processes its services.
    } else {
      if (clickType === ClickType.SELECTED) {
        // The application performs its own service logic (not time-consuming operations, such as opening a large file using OpenSync).
        if (uri) {
          this.selectUris.push(uri);
          this.pickerOptions.preselectedUris = \[...this.selectUris\];
        }
        return true; // If true is returned, the check box is selected. Otherwise, the check box is not selected.
      } else {
        if (uri) {
          this.selectUris = this.selectUris.filter((item: string) => {
            return item != uri;
          });
          this.pickerOptions.preselectedUris = \[...this.selectUris\];
        }
      }
      return true;
    }
  }

  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    // Callback to be invoked when the photo browser page is displayed.
    this.isBrowserShow = true;
    return true;
  }

  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    // Callback to be invoked when the photo browser page is closed.
    this.isBrowserShow = false;
    return true;
  }

  private onPickerControllerReady(): void {
    // After the callback is called, pickerController APIs can be called to send data to Picker. Before the callback is called, pickerController APIs do not take effect.
    let elements: number\[\] = \[PhotoBrowserUIElement.BACK\_BUTTON\];
    this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // Hide the Back button on the photo browser page.
  }

  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    // Callback to be invoked when the photo browser is swiped left or right.
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }

  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
    // Callback to be invoked when the selected image is deleted.
  }

  private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
    // Callback to be invoked when the number of selected items exceeds the maximum.
  }

  private onCurrentAlbumDeleted(): void {
    // Callback to be invoked when the current album is deleted.
  }

  private videoPlayStateChanged(state: VideoPlayerState): void {
    // Called when the video playback state changes.
  }
  build() {
    Flex({
      direction: FlexDirection.Column,
      justifyContent: FlexAlign.Center,
      alignItems: ItemAlign.Center
    }) {
      Column() {
        if (this.isBrowserShow) {
          // Back button of the application on the photo browser page.
          Row() {
            Button("Exit photo browser page").width('33%').height('8%').onClick(() => {
              this.pickerController.exitPhotoBrowser();
            })
          }.margin({ bottom: 20 })
        }

        PhotoPickerComponent({
          pickerOptions: this.pickerOptions,
          onSelect: (uri: string): void => this.onSelect(uri),
          onDeselect: (uri: string): void => this.onDeselect(uri),
          onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
            clickType), // This API can replace the preceding two APIs.
          onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
          onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
          onPickerControllerReady: (): void => this.onPickerControllerReady(),
          onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
          onSelectedItemsDeleted: this.selectedItemsDeletedCallback,
          onExceedMaxSelected: this.exceedMaxSelectedCallback,
          onCurrentAlbumDeleted: this.currentAlbumDeletedCallback,
          onVideoPlayStateChanged: this.videoPlayStateChangedCallback,
          pickerController: this.pickerController,
        }).height('60%').width('100%')

        // Simulate the selection bar at the bottom of the application.
        if (this.isBrowserShow) {
          Row() {
            ForEach(this.assets, async (asset: photoAccessHelper.PhotoAsset, index) => {
              if (asset.uri === this.currentUri) {
                Image(this.thumbnail\[index\])
                  .height('10%')
                  .width('10%')
                  .onClick(() => {
                  })
                  .borderWidth(1)
                  .borderColor('red')
              } else {
                Image(this.thumbnail\[index\]).height('10%').width('10%').onClick(() => {
                  this.pickerController.setData(DataType.SET\_SELECTED\_URIS, this.selectUris);
                  this.pickerController.setPhotoBrowserItem(asset.uri, PhotoBrowserRange.ALL);
                })
              }
            }, (uri: string) => JSON.stringify(uri))
          }
        } else {
          Button('Preview').width('33%').height('5%').onClick(async () => {
            if (this.selectUris.length > 0) {
              this.thumbnail = \[\];
              this.assets = \[\];
              for (let selectUri of this.selectUris) {
                let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
                predicates.equalTo(photoAccessHelper.PhotoKeys.URI, selectUri);
                let fetchOptions: photoAccessHelper.FetchOptions = {
                  fetchColumns: \[\],
                  predicates: predicates
                };
                let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                let photoHelper = photoAccessHelper.getPhotoAccessHelper(context);
                let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
                  await photoHelper.getAssets(fetchOptions);
                let asset = await fetchResult.getFirstObject()
                this.assets.push(asset);
                this.thumbnail.push(await asset.getThumbnail())
              }
              this.pickerController.setPhotoBrowserItem(this.selectUris\[0\], PhotoBrowserRange.SELECTED\_ONLY);
            }
          })
        }
      }
    }
  }
}
