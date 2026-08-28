# Classes (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/VeYwgS6FQeuC-pchcfye0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2944D6A8FCD2739F2DC03A6F723897C30BBF7D61E6F51206C55B8C4F1CE0A7CA)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### RecommendationOptions11+

Defines the image recommendation options. The image recommendation feature depends on the image data analysis capability, which varies with devices.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| recommendationType | [RecommendationType](../enums/document.md#recommendationtype11) | No | Yes | 
Type of the recommended image.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| textContextInfo12+ | [TextContextInfo](../interfaces-others/document.md#textcontextinfo12) | No | Yes | 

Text based on which images are recommended. If both **recommendationType** and **textContextInfo** are set, **textContextInfo** takes precedence over **recommendationType**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### BaseSelectOptions

Defines the basic options for selecting media files from Gallery.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| MIMEType | [PhotoViewMIMETypes](../enums/document.md#photoviewmimetypes) | No | Yes | 
Available media file types. **IMAGE\_VIDEO\_TYPE** is used by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| maxSelectNumber | number | No | Yes | 

Maximum number of media files that can be selected. The maximum value is **500**, and the default value is **50**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isPhotoTakingSupported11+ | boolean | No | Yes | 

Whether photo taking is supported. **true** if supported, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isSearchSupported11+ | boolean | No | Yes | 

Whether the image is searchable. **true** if searchable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| recommendationOptions11+ | [RecommendationOptions](#recommendationoptions11) | No | Yes | 

Image recommendation parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| preselectedUris11+ | Array<string> | No | Yes | 

URI of the preselected image.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isPreviewForSingleSelectionSupported12+ | boolean | No | Yes | 

Whether to enable full image preview if a single image is selected. **true** to enable, **false** otherwise. The default value is **true**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| singleSelectionMode18+ | [SingleSelectionMode](../enums/document.md#singleselectionmode18) | No | Yes | 

Single selection mode. The default value is **SingleSelectionMode.BROWSER\_MODE**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| mimeTypeFilter19+ | [MimeTypeFilter](#mimetypefilter19) | No | Yes | 

Configuration for file type filtering. Multiple types can be specified.

When this parameter is set, the **MIMEType** configuration automatically becomes invalid.

When this parameter is set, only media files of the configured filter type are displayed. You are advised to notify users that only images or videos of the specified type can be selected.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| fileSizeFilter19+ | [FileSizeFilter](#filesizefilter19) | No | Yes | 

Configuration for file size filtering.

When this parameter is set, only media files within the specified size range are displayed. You are advised to notify users that only images or videos of the specified size can be selected.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| videoDurationFilter19+ | [VideoDurationFilter](#videodurationfilter19) | No | Yes | 

Configuration for video duration filtering.

When this parameter is set, only media files within the specified duration range are displayed. You are advised to notify users that only videos of the specified length can be selected.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| combinedMediaTypeFilter20+ | Array<string> | No | Yes | 

A string array of filter criteria, supporting combinations of various types.

The format for the strings is follows: photoType | photoSubType1,photoSubType2, ... | mimeType1,mimeType2, ....

\- The first part specifies a single **photoType**, which is fixed at **image** or **video**.

\- The second part lists 1 to N photoSubTypes, separated by commas, with an OR relationship. Currently, the maximum value of N is **1**. Options include **movingPhoto** or "\*" (ignore).

\- The third part lists 1 to N mimeTypes, separated by commas, with an OR relationship. Currently, the maximum value of N is **10**. The format is similar to [MimeTypeFilter](#mimetypefilter19).

Filters are combined using intersection logic.

The NOT logic is supported. To exclude types, use parentheses. Each string can have only one set.

If the filter string does not match the specifications, the result is empty.

Only the first three array elements are used; **MIMETypes** and **mimeTypeFilter** are ignored.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| photoViewMimeTypeFileSizeFilters20+ | Array<[PhotoViewMimeTypeFileSizeFilter](#photoviewmimetypefilesizefilter20)\> | No | Yes | 

An array used to filter media files by type and size.

Only the first three array elements are used; **MIMETypes** and **fileSizeFilter** are ignored.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| isMovingPhotoBadgeShown22+ | boolean | No | Yes | 

Whether the moving photo badge is displayed in the photo browser page. **true** to display the badge, **false** to hide it. The default is **false**.

If this parameter is set to **true**, [Photoselectresult](#photoselectresult) returns the **movingPhotoBadgeStates** array. The default status of a moving photo is [MOVING\_PHOTO\_ENABLED](../enums/document.md#movingphotobadgestatetype22).

Note: Use both **isMovingPhotoBadgeShown** and **MovingPhotoBadgeStateType** to determine whether a photo is a moving photo.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| assetFilter22+ | Array<[OperationItem](#operationitem22)\> | No | Yes | 

Media asset filter, with a maximum length of 50 items. If the limit is exceeded, only the first 50 items are used.

**NOTE**

1\. When this filter is applied, other filters become invalid.

2\. When setting multiple conditions, enclose the filter conditions in parentheses to prevent conflicts with internal filter items.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### PhotoSelectOptions

PhotoSelectOptions extends BaseSelectOptions

Defines additional options for selecting media files from Gallery. It inherits from [BaseSelectOptions](#baseselectoptions).

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isEditSupported11+ | boolean | No | Yes | 
Whether the image can be edited. **true** if editable, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isOriginalSupported12+ | boolean | No | Yes | 

Whether to display the button for selecting the original image. **true** to display, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| subWindowName12+ | string | No | Yes | 

Name of the child window.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| completeButtonText14+ | [CompleteButtonText](../enums/document.md#completebuttontext14) | No | Yes | 

Text displayed on the complete button.

The complete button is located in the lower-right corner of the page. It is used by users to signify that they have finished selecting images.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| contextRecoveryInfo21+ | [ContextRecoveryInfo](#contextrecoveryinfo21) | No | Yes | 

Information for restoring the PhotoPicker's state from the last exit.

When the selection process is complete, the PhotoPicker returns **contextRecoveryInfo** to the application. The application can then use the information to restore the PhotoPicker's state and the last viewed grid interface the next time it starts the PhotoPicker.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### PhotoSelectResult

Defines information about the images or videos selected.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| photoUris | Array<string> | No | No | 
URIs of the media files selected.

This URI array can be used only by calling the [photoAccessHelper.getAssets](../interface-photoaccesshelper/document.md#getassets) API through temporary authorization. For details, see [Using a Media File URI](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/user-file-uri-intro#using-a-media-file-uri).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isOriginalPhoto | boolean | No | No | 

Whether the selected media file is the original image. **true** if yes, **false** otherwise. The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| contextRecoveryInfo21+ | [ContextRecoveryInfo](#contextrecoveryinfo21) | No | No | 

Information about the context of exiting the PhotoPicker. This information is returned when the selection process is complete and is used by the application within **PhotoSelectOptions** during the subsequent launch of the PhotoPicker to restore the state from the previous exit.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |
| movingPhotoBadgeStates22+ | Array<[MovingPhotoBadgeStateType](../enums/document.md#movingphotobadgestatetype22)\> | No | No | 

Array of moving photo badge states for the media files selected from Gallery.

If **isMovingPhotoBadgeShown** is set to **true**, this array contains the moving photo badge states. Otherwise, it is empty.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### MimeTypeFilter19+

Describes the configuration for file type filtering.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mimeTypeArray | Array<string> | No | No | 
Types of media files that PhotoPicker allows users to filter by. The maximum array length is 10, thus supporting up to 10 specified types.

The filter type is defined by the MIME type, for example, image/jpeg and video/mp4.

 |

#### FileSizeFilter19+

Describes the configuration for file size filtering.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filterOperator | [FilterOperator](../enums/document.md#filteroperator19) | No | No | 
Filter operator.

For example, files can be filtered based on being greater than or less than a certain file size.

 |
| fileSize | number | No | No | 

File size used for filtering.

The unit is bytes.

 |
| extraFileSize | number | No | Yes | 

Maximum file size in **FilterOperator.BETWEEN** mode. The default value is **\-1**.

The unit is bytes.

 |

#### VideoDurationFilter19+

Describes the configuration for video duration filtering.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| filterOperator | [FilterOperator](../enums/document.md#filteroperator19) | No | No | 
Filter operator.

For example, videos can be filtered based on being greater than or less than a certain duration.

 |
| videoDuration | number | No | No | 

Video duration used for filtering.

The unit is milliseconds (ms).

 |
| extraVideoDuration | number | No | Yes | 

Maximum video duration in **FilterOperator.BETWEEN** mode. The default value is **\-1**.

The unit is milliseconds (ms).

 |

#### RecentPhotoOptions20+

Represents the configuration options of the recent images or videos.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| period | number | No | Yes | 
Time range for displaying the recent images or videos, measured in seconds. After setting, the system shows images or videos taken within the specified time from the current moment. The longest duration you can set is 1 day (86400s).

If the value is less than or equal to 0, greater than 86400, or not set, the system uses the longest duration (1 day) by default. If there are no images or videos within the set time range, the component does not show anything.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MIMEType | [photoAccessHelper.PhotoViewMIMETypes](../enums/document.md#photoviewmimetypes) | No | Yes | 

Types of the file displayed. The default value is **PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE**.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| photoSource | [PhotoSource](../enums/document.md#photosource20) | No | Yes | 

Source of the recent image or video, for example, image or video taken by the camera or screenshot. By default, the source is not restricted.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### RecentPhotoInfo20+

Describes the information about the recent image or video.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dateTaken | number | No | Yes | 
Time when the recent image or video was shot (in milliseconds since January 1, 1970). The unit is ms.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| identifier | string | No | Yes | 

Hash value of the name of the recent image or video, which is used to help the application determine whether the image or video to be displayed is the same as the one displayed before.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### PhotoViewMimeTypeFileSizeFilter20+

Describes the configuration for filtering media files by type and size.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| photoViewMimeType | [PhotoViewMIMETypes](../enums/document.md#photoviewmimetypes) | No | No | Media file types used for filtering. |
| sizeFilter | [FileSizeFilter](#filesizefilter19) | No | No | Media file size used for filtering. |

#### ContextRecoveryInfo21+

Describes the information about the context of exiting the PhotoPicker. It can be used during the subsequent launch of the PhotoPicker to restore the state from the previous exit.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| albumUri | string | No | No | 
URI of the album in the media library when the user selects an image and exits.

\- If the user selects from all images, **albumUri** is a fixed **"allPhotos"** string.

\- If the user exits after selecting from search results, text recommendations, or avatar recommendations, the next restoration is not supported, and the returned **albumUri** is an empty string.

The default value is an empty string.

 |
| time | number | No | No | 

Time of the top-left image in the grid interface when the user last selected an image.

\- For albums sorted by capture time, the capture time is returned.

\- For albums sorted by save time, the save time is returned. The default value is **0**.

 |
| displayName | string | No | No | File name of the top-left image in the grid interface when the user last selected an image. The default value is an empty string. |
| recommendationType | number | No | No | 

Enumerated value of the recommended content set by the user during the last selection. For details, see [RecommendationType](../enums/document.md#recommendationtype11).

If no recommendation was set during the last selection, the default value is **0**.

 |
| selectedRecommendationType | number | No | No | 

Enumerated value of the recommended content selected by the user during the last selection. For details, see [RecommendationType](../enums/document.md#recommendationtype11).

If no recommendation was selected during the last selection or **All** was selected, the default value is **0**.

 |
| version | number | No | No | 

Version number of the state data, used to verify the compatibility of the state information data with the state recovery capability.

The version number must be greater than or equal to 1.0.

 |

#### OperationItem22+

Describes the settings for filtering media files.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| operationType | [OperationType](../enums/document.md#operationtype22) | No | No | Predicates. |
| field | [PhotoKeys](../enums/document.md#photokeys) | No | Yes | 
Column name in the data table.

Currently, only the following key fields are supported: **URI**, **PHOTO\_TYPE**, **DISPLAY\_NAME**, **SIZE**, **DURATION**, **WIDTH**, **HEIGHT**, **ORIENTATION**, **FAVORITE**, **TITLE**, **POSITION**, **PHOTO\_SUBTYPE**, **DYNAMIC\_RANGE\_TYPE**, **COVER\_POSITION**, **BURST\_KEY**, **LCD\_SIZE**, **THM\_SIZE**, **DETAIL\_TIME**, **MEDIA\_SUFFIX**, **OWNER\_ALBUM\_ID**, and **ASPECT\_RATIO**.

When [select](../class-photoviewpicker/document.md#select) is used to set this parameter, an invalid field results in error code 401. When [@ohos.file.PhotoPickerComponent (PhotoPickerComponent)](../../../arkts-components/ohos-file-photopickercomponent-photopickercomponent/document.md) is used to set this parameter, an invalid field does not trigger the **onPickerControllerReady** callback.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

 |
| value | Array<[OperationValueType](../types/document.md#operationvaluetype22)\> | No | Yes | 

Values needed for matching different predicates.

This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.

The maximum length is 10; if exceeded, only the first 10 values are considered.

 |
