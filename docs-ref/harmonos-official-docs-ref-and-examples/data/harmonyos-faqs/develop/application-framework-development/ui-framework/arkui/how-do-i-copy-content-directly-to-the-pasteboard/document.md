# How do I copy content directly to the pasteboard?

Use the APIs provided by the [Pasteboard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard) module, which allows operations for text, HTML, URI, Want, PixelMap, and other content types.

Example:

1.  Use **pasteboard.createData** to create a pasteboard data object by passing in the data type and content.
2.  Use **pasteboard.getSystemPasteboard** to obtain a system pasteboard object.
3.  Obtain the system pasteboard object and call the **setData** method to write data to the pasteboard. Call the **getData** method to read the pasteboard data.
    
    import { pasteboard } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct CopyText {
      private textContent: string = 'Copy me';
    
      aboutToAppear(): void {
        AppStorage.setOrCreate('context', this.getUIContext());
      }
    
      build() {
        Column() {
          Text(this.textContent)
            .fontSize(20)
            .borderRadius(9)
            .borderWidth(1)
            .padding({
              left: 8,
              right: 8
            })
            .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
            .fontWeight(FontWeight.Medium)
            .opacity($r('sys.float.ohos\_id\_alpha\_content\_secondary'))
            .onClick(() => copyText(this.textContent))
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
        .alignSelf(ItemAlign.Center)
      }
    }
    
    /\*
     \* Copy the text to the system clipboard
     \* @param text - text
     \* @returns void
     \*/
    function copyText(text: string) {
      const uiContext: UIContext | undefined = AppStorage.get('context');
      // Create clipboard content object
      const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE\_TEXT\_PLAIN, text);
      // Get system clipboard object
      const systemPasteboard = pasteboard.getSystemPasteboard();
      systemPasteboard.setData(pasteboardData); // Put data into clipboard
      systemPasteboard.getData().then((data) => { // Read clipboard content
        if (data) {
          uiContext?.getPromptAction().showToast({ message: 'Copy succeeded' });
        } else {
          uiContext?.getPromptAction().showToast({ message: 'Copy failed' });
        }
      })
    }
