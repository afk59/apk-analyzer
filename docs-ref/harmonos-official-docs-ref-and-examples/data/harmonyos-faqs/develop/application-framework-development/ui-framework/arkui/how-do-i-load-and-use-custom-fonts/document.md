# How do I load and use custom fonts?

1.  Use [@ohos.font (Custom Font Registration)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-font).
2.  Set the font family for the text. The code snippet is as follows:
    
    // xxx.ets
    import { Font } from '@kit.ArkUI';
    
    @Entry
    @Component
    struct FontExample {
      @State message: string = 'Hello World';
    
      aboutToAppear() {
        // Register in black font
        let font: Font = this.getUIContext().getFont()
        font.registerFont({
          familyName: 'Condensed\_Black', // Registered font name
          familySrc: '/font/Sans\_Condensed\_Black.ttf' // The font folder is at the same level as the pages directory
        })
    
        // Register in black oblique font
        font.registerFont({
          familyName: 'Condensed\_Black\_Italic', // Registered font name
          familySrc: '/font/Sans\_Condensed\_Black\_Italic.ttf' // The font folder is at the same level as the pages directory
        })
      }
    
      build() {
        Column() {
          Text(this.message)
            .align(Alignment.Center)
            .fontSize(50)
            .fontFamily('Condensed\_Black') // Use black font
          Text(this.message)
            .align(Alignment.Center)
            .fontSize(50)
            .fontFamily('Condensed\_Black\_Italic') // Use black oblique font
          Text(this.message)
            .align(Alignment.Center)
            .fontSize(50)
        }
        .width('100%')
        .margin({ top: 30 })
      }
    }
    

The figure below shows the preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/shVgr8ANRyCG7GUEdtSUag/en-us_image_0000002194158888.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062548Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3247A03B5DC682EBFD994511B0D555EF47289832F7D507308272B61356259200 "Click to enlarge")
