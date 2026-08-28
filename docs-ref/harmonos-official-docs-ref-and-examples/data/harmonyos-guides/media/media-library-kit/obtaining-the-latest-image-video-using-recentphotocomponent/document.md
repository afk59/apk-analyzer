# Obtaining the Latest Image/Video Using RecentPhotoComponent

**RecentPhotoComponent** is a UI component that allows an application to access the latest image/video in the user directory without the required permission. This component grants the application only the read permission.

The following figure shows the UI effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/_wt2jZ5nTR6WDq8UOcsroA/en-us_image_0000002418361113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D1A07D559A5E587E7A73B5C877528194185B8C2BACECD786A22CB5CEC24311E "Click to enlarge")

#### How to Develop

1.  Import modules.
    
    import { BaseItemInfo } from '@ohos.file.PhotoPickerComponent';
    import {
      PhotoSource,
      RecentPhotoComponent,
      RecentPhotoOptions,
      photoAccessHelper
    } from '@kit.MediaLibraryKit';
    
2.  Create a **RecentPhotoOptions** instance.
    
    You can use **RecentPhotoOptions** to set the time period, file types, and source of the file to display. For details, see [RecentPhotoOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-recentphotocomponent#recentphotooptions).
    
    // Initialize RecentPhotoComponent.
    recentPhotoOptions: RecentPhotoOptions = new RecentPhotoOptions();
    
3.  Initialize the **RecentPhotoOptions** instance.
    
    // Set the data type. IMAGE\_VIDEO\_TYPE (default value) indicates image and video; IMAGE\_TYPE indicates image; VIDEO\_TYPE indicates video; MOVING\_PHOTO\_IMAGE\_TYPE indicates moving photo.
    this.recentPhotoOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE;
    
    // Set the time period of the latest image/video, in seconds. The value 0 means there is no time limit.
    this.recentPhotoOptions.period = 0;
    
    // Set the resource source. The value ALL indicates all resources; CAMERA indicates resources related to the camera; SCREENSHOT indicates screenshots.
    this.recentPhotoOptions.photoSource = PhotoSource.ALL;
    
4.  Create a [RecentPhotoComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-recentphotocomponent#recentphotocomponent).
    
    RecentPhotoComponent({
        // Set recentPhotoOptions.
        recentPhotoOptions: this.recentPhotoOptions,
        
         /\*\*
         \* Callback to be invoked when the latest image/video is selected.
         \* BaseItemInfo(uri, mimeType, width, height, size, duration)
         \* If true is returned, the URL is granted with the permission and the latest image/video is displayed.
         \*/
        onRecentPhotoClick: (recentPhotoInfo: BaseItemInfo): boolean => this.onRecentPhotoClick(recentPhotoInfo),
    
        // Check whether the latest resource exists.
        onRecentPhotoCheckResult: (recentPhotoExists: boolean) => this.onReceiveCheckResult(recentPhotoExists),
    })
    
5.  Implement related callbacks.
    
    Implement the **onReceiveCheckResult** callback to check whether the latest image/video exists. The logic for whether to display the latest image/video is executed only when **true** is returned.
    
    Implement the **onRecentPhotoClick** callback to return the image/video information in [BaseItemInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#baseiteminfo).
    
    // The URI is granted with the permission only when the return value is true.
    private onRecentPhotoClick(recentPhotoInfo: BaseItemInfo): boolean {
        if (!recentPhotoInfo) {
          return false;
        }
        return true;
      }
    
    private onReceiveCheckResult(recentPhotoExists: boolean): void {
        if (!recentPhotoExists) {
          console.info('not exist recent photo');
        }
        // If the latest image/video exists, implement the subsequent service logic, for example, whether to display RecentPhotoComponent.
     }
    

#### Sample Code

For details, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-recentphotocomponent#example) .
