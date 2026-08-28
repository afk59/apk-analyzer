# Accessing Images/Videos Using PhotoPickerComponent

**PhotoPickerComponent** is a UI component that allows an application to access the image/video selected by the user without the permission for reading images/videos.

The following figures show the UI effects.

<table class="simpletableborder"><tbody><tr><td valign="top"><p>Grid page</p></td><td valign="top"><p>Full image page</p></td></tr><tr><td valign="top"><p><span><img height="493.00745900000004" originheight="942" originwidth="550" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/8qRV7n2jSrywfgQC0jnlFA/en-us_image_0000002291138533.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062044Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=9CF64B416A6069691276FEA9DD5B00F5F3F59C4FD45747DFC5553B7BC2B12758" title="Click to enlarge" width="316.20750000000004"></span></p></td><td valign="top"><p><span><img height="482.1915" originheight="1944" originwidth="1252" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/zNSQIwa5Rayt2EIzO2bXog/en-us_image_0000002256408340.jpg?HW-CC-KV=V1&amp;amp;HW-CC-Date=20260410T062044Z&amp;amp;HW-CC-Expire=86400&amp;amp;HW-CC-Sign=E8A3027E3E206350EAD5064A70309ED5D66128F36BB841F34D236CC5D7039F63" title="Click to enlarge" width="314.677335"></span></p></td></tr></tbody></table>

#### How to Develop

1.  Import the **PhotoPickerComponent** and related modules.
    
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
      ReminderMode,
      photoAccessHelper
    } from '@kit.MediaLibraryKit';
    
2.  Create a **PickerOptions** instance and a **PickerController** instance.
    
    In **PickerOptions**, you can set the grid style (such as the check box background color and text color), preview direction, and maximum number of photos/videos that can be selected. For details, see [PickerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#pickeroptions).
    
    You can use **PickerController** to send data to **PhotoPickerComponent**.
    
      // Set parameters for initializing PhotoPickerComponent.
      pickerOptions: PickerOptions = new PickerOptions();
    
      // Initialize PickerController to control the behavior of PhotoPickerComponent.
      @State pickerController: PickerController = new PickerController();
    
      // Selected images.
      @State selectUris: Array<string> = new Array<string>();
    
      // Currently selected image.
      @State currentUri: string = '';
      
      // Whether to display the photo browser.
      @State isBrowserShow: boolean = false;
    
3.  Initialize **PickerOptions**.
    
    The following contains only the parameters used in the sample code. For details about the supported parameters and value ranges, see [PickerOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#pickeroptions).
    
      // Set the data type for the Picker grid page.
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE // Both images and videos are displayed.
    // Set the maximum number of selections.
    this.pickerOptions.maxSelectNumber = 5;
    // Set the mode of the reminder when the number of selected items exceeds the maximum.
    this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
    // Set whether to display a search box. The default value is true.
    this.pickerOptions.isSearchSupported = false;
    // Set whether to enable photographing. The default value is true.
    this.pickerOptions.isPhotoTakingSupported = false;
    
4.  Implement the callback functions.
    
    Implement the following callbacks to respond to user operations on the UI.
    
    -   Callbacks to be invoked when the photo browser page is displayed or exits. For details about the information reported, see [PhotoBrowserInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#photobrowserinfo).
    -   Callbacks to be invoked when images/videos are selected. The image/video URIs will be returned to the application.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/ip3VdwXQRoCO3ojZSTWa6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32DC0BE36E8239C8B2A922A225DAB3063D68A4B7D6CC0FEB7B58DE4D8F85AAAF)
        
        -   All URIs returned by the callback are read-only. You can read file data based on the URIs in the result set. However, you cannot directly use the URI to open an image/video in the Picker callback. Instead, you need to define a global variable to save the URI. For details, see [Reading File Data by URI](../selecting-media-assets-using-picker/document.md#reading-file-data-by-uri) and [Obtaining an Image or Video by URI](../selecting-media-assets-using-picker/document.md#obtaining-an-image-or-video-by-uri).
        -   To obtain metadata such as the file size, access time, modification time, file name, and file path, you can use [@ohos.file.fs (File Management)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) and [@ohos.file.fileuri (File URI)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fileuri) APIs based on the URI.
        
    -   Callbacks to be invoked when an image (thumbnail item) or camera item is clicked. If a thumbnail item is clicked, the callback returns [ItemInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#iteminfo). If a camera item is clicked, the callback starts the system camera or application for subsequent processing.
    
    For details about the supported callback events and their parameters, see [PhotoPickerComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#photopickercomponent).
    
    // Callback to be invoked when a resource is selected. The resource information and selection mode are returned.
    private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
      if (!itemInfo) {
        return false;
      }
      let type: ItemType | undefined = itemInfo.itemType;
      let uri: string | undefined = itemInfo.uri;
      if (type === ItemType.CAMERA) {
        // Click a camera item.
        return true; // Return true to start the system camera; return false to allow the application to process the request.
      } else {
        if (clickType === ClickType.SELECTED) {
          // The application processes its services.
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
    
    // Callback to be invoked when the photo browser is displayed.
    private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
      this.isBrowserShow = true;
      return true;
    }
    
    // Callback to be invoked when the photo browser exits.
    private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
      this.isBrowserShow = false;
      return true;
    }
    
    // After the callback is called, pickerController APIs can be called to send data to the Picker. Before the callback is called, pickerController APIs do not take effect.
    private onPickerControllerReady(): void {
      let elements: number\[\] = \[PhotoBrowserUIElement.BACK\_BUTTON\];
      this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // Hide the Back button on the photo browser page.
    }
    
    // Callback to be invoked when the photo browser is swiped left or right.
    private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
      this.currentUri = browserItemInfo.uri ?? '';
      return true;
    }
    
    // Callback to be invoked when the selected image is deleted.
    private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
    }
    
    // Callback to be invoked when the number of selected items exceeds the maximum.
    private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
    }
    
    // Callback to be invoked when the current album is deleted.
    private onCurrentAlbumDeleted(): void {
    }
    
5.  Create a [PhotoPickerComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#photopickercomponent).
    
      PhotoPickerComponent({
        pickerOptions: this.pickerOptions,
        onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
        onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
        onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
        onPickerControllerReady: (): void => this.onPickerControllerReady(),
        onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
        onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
        onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
        onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
        pickerController: this.pickerController,
      })
    
6.  Use PickerController APIs to send data to the Picker component to control the behavior of **PhotoPickerComponent**.
    
    There are multiple usages. For details, see [PickerController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-file-photopickercomponent#pickercontroller).
    

#### Sample Code

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
  ReminderMode,
  photoAccessHelper
} from '@kit.MediaLibraryKit';

@Entry
@Component
struct PhotoPickerComponentDemo {
  // Set parameters for initializing PhotoPickerComponent.
  pickerOptions: PickerOptions = new PickerOptions();

  // Initialize PickerController to control the behavior of PhotoPickerComponent.
  @State pickerController: PickerController = new PickerController();

  // Selected images.
  @State selectUris: Array<string> = new Array<string>();

  // Currently selected image.
  @State currentUri: string = '';

  // Whether to display the photo browser.
  @State isBrowserShow: boolean = false;

  aboutToAppear() {
    // Set the data type for the Picker grid page.
    this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_VIDEO\_TYPE // Both images and videos are displayed.
    // Set the maximum number of selections.
    this.pickerOptions.maxSelectNumber = 5;
    // Set the mode of the reminder when the number of selected items exceeds the maximum.
    this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
    // Set whether to display a search box. The default value is false.
    this.pickerOptions.isSearchSupported = true;
    // Set whether to enable photographing. The default value is false.
    this.pickerOptions.isPhotoTakingSupported = true;

  }

  // Callback to be invoked when a resource is selected. The resource information and selection mode are returned.
  private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
    if (!itemInfo) {
      return false;
    }
    let type: ItemType | undefined = itemInfo.itemType;
    let uri: string | undefined = itemInfo.uri;
    if (type === ItemType.CAMERA) {
      // Click a camera item.
      return true; // Return true to start the system camera; return false to allow the application to process the request.
    } else {
      if (clickType === ClickType.SELECTED) {
        // The application processes its services.
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

  // Callback to be invoked when the photo browser is displayed.
  private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = true;
    return true;
  }

  // Callback to be invoked when the photo browser exits.
  private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
    this.isBrowserShow = false;
    return true;
  }

// After the callback is called, pickerController APIs can be called to send data to the Picker. Before the callback is called, pickerController APIs do not take effect.
  private onPickerControllerReady(): void {
  }

  // Callback to be invoked when the photo browser is swiped left or right.
  private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
    this.currentUri = browserItemInfo.uri ?? '';
    return true;
  }

  // Callback to be invoked when the selected image is deleted.
  private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
  }

  // Callback to be invoked when the number of selected items exceeds the maximum.
  private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
  }

  // Callback to be invoked when the current album is deleted.
  private onCurrentAlbumDeleted(): void {
  }

  build() {
    Flex({
      direction: FlexDirection.Column,
      alignItems: ItemAlign.Start
    }) {
      PhotoPickerComponent({
        pickerOptions: this.pickerOptions,
        onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
        onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
        onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
        onPickerControllerReady: (): void => this.onPickerControllerReady(),
        onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
        onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
        onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
        onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
        pickerController: this.pickerController,
      })

      // Simulate the selection bar at the bottom of the application.
      if (this.isBrowserShow) {
        // Thumbnail of the selected image.
        Row() {
          ForEach(this.selectUris, (uri: string) => {
            if (uri === this.currentUri) {
              Image(uri).height(50).width(50)
                .onClick(() => {
                })
                .borderWidth(1)
                .borderColor('red')
            } else {
              Image(uri).height(50).width(50).onClick(() => {
                this.pickerController.setData(DataType.SET\_SELECTED\_URIS, this.selectUris);
                this.pickerController.setPhotoBrowserItem(uri, PhotoBrowserRange.ALL);
              })
            }
          }, (uri: string) => JSON.stringify(uri))
        }.alignSelf(ItemAlign.Center).margin(this.selectUris.length ? 10 : 0)
      } else {
        // Access the photo browser and preview the selected image.
        Button('Preview').width('33%').alignSelf(ItemAlign.Start).height('5%').margin(10).onClick(() => {
          if (this.selectUris.length > 0) {
            this.pickerController.setPhotoBrowserItem(this.selectUris\[0\], PhotoBrowserRange.SELECTED\_ONLY);
          }
        })
      }
    }
  }
}
