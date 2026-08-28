# NotificationContent

The **NotificationContent** module provides APIs for defining the notification content.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/wqXNOUGsTTqNp6rrKc8R8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E5BE5B08E7280B494E2D40C0C5FE17B5A1B5D6DCA49C26088EAC829301C53F8)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### NotificationContent

Describes the notification contents.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| contentType(deprecated) | [notification.ContentType](../../apis-no-longer-maintained/ohos-notification-notification/document.md#contenttype) | No | Yes | 
Notification content type.

This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use **notificationContentType** instead.

 |
| notificationContentType11+ | [notificationManager.ContentType](../../ohos-notificationmanager-notificationmanager/document.md#contenttype) | No | Yes | Notification content type. |
| normal | [NotificationBasicContent](#notificationbasiccontent) | No | Yes | Normal text. |
| longText | [NotificationLongTextContent](#notificationlongtextcontent) | No | Yes | Long text. |
| multiLine | [NotificationMultiLineContent](#notificationmultilinecontent) | No | Yes | Multi-line text. |
| picture | [NotificationPictureContent](#notificationpicturecontent) | No | Yes | Picture-attached. |
| systemLiveView11+ | [NotificationSystemLiveViewContent](#notificationsystemliveviewcontent) | No | Yes | System live view. A third-party application cannot directly create a notification of this type. After the system proxy creates a system live view, the third-party application releases a notification with the same ID to update the specified content. |

#### NotificationBasicContent

Describes the normal text notification.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | No | Notification title. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| text | string | No | No | Notification content. It cannot be empty or exceed 3,072 bytes. Excess content will be truncated. |
| additionalText | string | No | Yes | Additional information of the notification. It cannot exceed 3,072 bytes. Excess content will be truncated. This parameter is left empty by default. |
| lockscreenPicture12+ | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Picture displayed on the lock screen. This parameter is left empty by default. Currently, only the live view notification is supported. The total number of the icon pixel bytes cannot exceed 192 KB (which is obtained through [getPixelBytesNumber](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md#getpixelbytesnumber7)). The recommended icon size is 128 × 128 pixels. The display effect depends on the device capability and notification center UI style. |

#### NotificationLongTextContent

Describes the long text notification. This API is inherited from [NotificationBasicContent](#notificationbasiccontent).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/JX2PClZKQbuedJuOLwqRLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77B0129EA09A019B12E6618A445970BA10D63916932686861D4CF5F5DBA91423)

The display effect depends on the device capability and notification center UI style.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| longText | string | No | No | Long text of the notification. It cannot be empty or exceed 3,072 bytes. Excess content will be truncated. |
| briefText | string | No | No | Brief text of the notification. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| expandedTitle | string | No | No | Title of the notification in the expanded state. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |

#### NotificationMultiLineContent

Describes the multi-line text notification. This API is inherited from [NotificationBasicContent](#notificationbasiccontent).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/HopkgrTzSuy_q97A-fQ-Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4156B20836DB29EF3FB951961D0F56F5A5C8B0292022257FBD43D4C0E92FABC6)

-   When the multi-line text notification and another notification form a group notification, the group notification is displayed as a [normal text notification](#notificationbasiccontent) by default. After the group notification is expanded, the value of **longTitle** is used as the title, and the value of **lines** is used as the multi-line text content.
    
    When the multi-line text notification is displayed independently, the value of **longTitle** is used as the title, and the value of **lines** is used as the multi-line text content.
    
-   The display effect depends on the device capability and notification center UI style.
    

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| briefText | string | No | No | Brief text of the notification. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| longTitle | string | No | No | Title of the notification in the expanded state. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| lines | Array<string> | No | No | Multi-line text of a notification. A maximum of three lines are supported, and each line cannot exceed 1,024 bytes. Excess content will be truncated. |

#### NotificationPictureContent

Describes the picture-attached notification. This API is inherited from [NotificationBasicContent](#notificationbasiccontent).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/KmEZT-jjSje7MKW3r_OuVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062515Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B90F62F93655F679DCAD4960D4F796EEF5F42EFE0E13ECBEF116FE8EFBA8D883)

The display effect depends on the device capability and notification center UI style.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| briefText | string | No | No | Brief text of the notification. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| expandedTitle | string | No | No | Title of the notification in the expanded state. It cannot be empty or exceed 1,024 bytes. Excess content will be truncated. |
| picture | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | No | Picture content of the notification. The total pixel data size of the image cannot exceed 2 MB. |

#### NotificationSystemLiveViewContent

Describes the system live view notification. A third-party application cannot directly create a notification of this type. After the system proxy creates a system live view, the third-party application releases a notification with the same ID to update the specified content. This API is inherited from [NotificationBasicContent](#notificationbasiccontent).

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| typeCode11+ | number | No | No | Type code, which identifies the type of the service that invokes the API. |
| capsule11+ | [NotificationCapsule](#notificationcapsule11) | No | Yes | Capsule of the notification. This parameter is left empty by default. |
| button11+ | [NotificationButton](#notificationbutton11) | No | Yes | Button in the notification. This parameter is left empty by default. |
| time11+ | [NotificationTime](#notificationtime11) | No | Yes | Time of the notification. This parameter is left empty by default. |
| progress11+ | [NotificationProgress](#notificationprogress11) | No | Yes | Progress of the notification. This parameter is left empty by default. |

#### NotificationCapsule11+

Describe the notification capsule.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | Yes | Title of the capsule, with a maximum of 200 bytes. Excess part will be truncated. |
| icon | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Icon of the capsule. |
| backgroundColor | string | No | Yes | Background color of the capsule. |

#### NotificationButton11+

Describes the notification button.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| names | Array<string> | No | Yes | Button names. A maximum of three names are supported. |
| icons | Array<[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | No | Yes | Button icons. A maximum of three icons are supported. |
| iconsResource12+ | Array<[Resource](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)\> | No | Yes | Button icon resources. A maximum of three icon resources are supported. |

#### NotificationTime11+

Describes the notification timing information.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| initialTime | number | No | Yes | Start time, in milliseconds. |
| isCountDown | boolean | No | Yes | 
Whether to count down. The default value is **false**.

\- **true**: Yes.

\- **false**: No.

 |
| isPaused | boolean | No | Yes | 

Whether to pause the progress. The default value is **false**.

\- **true**: Yes.

\- **false**: No.

 |
| isInTitle | boolean | No | Yes | 

Whether the time is displayed in the title. The default value is **false**.

\- **true**: Yes.

\- **false**: No.

 |

**Example**:

// The notification counts down from three seconds and the time is displayed in the title.
time: {
    initialTime: 3000,
    isCountDown: true,
    isPaused: false,
    isInTitle: true,
}

#### NotificationProgress11+

Describes the notification progress.

**System capability**: SystemCapability.Notification.Notification

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| maxValue | number | No | Yes | Maximum progress value. |
| currentValue | number | No | Yes | Current progress value. |
| isPercentage | boolean | No | Yes | 
Whether to show the progress in percentage. The default value is **false**.

\- **true**: Yes.

\- **false**: No.

 |
