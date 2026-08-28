# Content Cards Based on Uniform Data Structs (ArkTS)

#### When to Use

Preset cards provided by the system allow you to quickly display data of uniform data structs.

#### Content Card

You can use the content cards to quickly display information (including the title, description, image, and application information) and redirect to the corresponding source upon a tap. Passing the [ContentForm](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-uniformdatastruct#contentform14) data, card width and height, and tap event callback in the [ContentFormCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-udmfcomponents#contentformcard) API can achieve a good display effect.

Since API version 20, [Content card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-udmfcomponents) is available.

## Available APIs

The following table describes the **ContentFormCard** API.

| Name | Description |
| :-- | :-- |
| ContentFormCard({contentFormData: uniformDataStruct.ContentForm, formType: FormType, formWidth?: number, formHeight?: number, handleOnClick?: Function}) | Displays the passed content card data in a fixed style, invokes the callback upon a tap, and redirects to the configured page. |

## How to Develop

// 1. Import required modules.
import { ContentFormCard, FormType, uniformDataStruct } from '@kit.ArkData';
import hilog from '@ohos.hilog';

@Entry
@Component
struct Index {
  @State contentForm: uniformDataStruct.ContentForm = {
    uniformDataType: 'general.content-form',
    title: ''
  };
  @State startToShow: boolean = false;

  aboutToAppear(): void {
    // 2. Initialize data.
    this.initData();
  }

  async initData() {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return;
    }
    try {
      let appIcon = await context.resourceManager.getMediaContent($r('app.media.startIcon').id);
      let thumbImage = await context.resourceManager.getMediaContent($r('app.media.foreground').id);
      this.contentForm = {
        uniformDataType: 'general.content-form',
        title: 'Content form title',
        thumbData: appIcon,
        description: 'Content form description',
        appIcon: thumbImage,
        appName: 'com.test.demo'
      };
    } catch (err) {
      hilog.error(0xFF00, '\[Sample\_Udmf\]', 'Init data error');
    }
  }

  build() {
    Column() {
      Button('show card').fontSize(30)
        .onClick(() => {
          // 3. startToShow is changed to true upon a tap, and the page is re-rendered.
          this.startToShow = true;
        })
      if (this.startToShow) {
        // 4. Pass in corresponding parameters to the ContentFormCard API.
        ContentFormCard({
          contentFormData: this.contentForm,
          formType: FormType.TYPE\_SMALL,
          formWidth: 220,
          formHeight: 100,
          handleOnClick: () => {
            hilog.info(0xFF00, '\[Sample\_Udmf\]', 'Clicked card');
          }
        })
      }
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
