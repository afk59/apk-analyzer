# TextReaderIcon (Read Receiver Icon)

The read receiver icon can be loaded as a dynamic component and configured as the main entry of the playback panel.

**Start version**: 5.0.0(12)

#### Module Import

import { TextReaderIcon } from '@kit.SpeechKit';

#### TextReaderIcon

Read receiver icon, which can be loaded as a dynamic component. The **onClick** callback is set to start the reading control when a user taps the receiver icon.

**Decorator type**: @Component

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

readState

 | 

[ReadStateCode](../../arkts-apis/readstatecode-reading-status/document.md)

 | 

Yes

 | 

@Link

 | 

Reading status.

**Note**:

The **ReadState** class uses the @Link decorator. For details, please refer to [@Link Decorator: Implementing Two-Way Synchronization Between Parent and Child Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-link).

 |

#### \[h2\]build

build(): void

Constructor used to create a [TextReaderIcon](#section71306437290) object.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Example**:

import { TextReader, TextReaderIcon, ReadStateCode } from '@kit.SpeechKit';

@Entry
@Component
struct Index {

  /\*\*
   \* Articles to load.
   \*/
  @State readInfoList: TextReader.ReadInfo\[\] = \[\];
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList\[0\];

  /\*\*
   \* Playback state.
   \*/
  @State readState: ReadStateCode = ReadStateCode.WAITING;

  /\*\*
   \* Display the button status on the current page.
   \*/
  @State isInit: boolean = false;

  async aboutToAppear(){
    /\*\*
     \* Load the data.
     \*/
    let readInfoList: TextReader.ReadInfo\[\] = \[{
      id: '001',
      title: {
        text:'_Title of the text to read_',
        isClickable:true
      },
      author:{
        text:'_Author of the text to read_',
        isClickable:true
      },
      date: {
        text:'2024/01/01',
        isClickable:false
      },
      bodyInfo: '_Text body to read_'
    }\];
    this.readInfoList = readInfoList;
    this.selectedReadInfo = this.readInfoList\[0\];
    this.init();
  }

  /\*\*
   \* Initialization
   \*/
  async init() {
    const readerParam: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: 'AI Reader',
        panelIcon: $r('app.media.startIcon')
      }
    }
    try {
      let context: Context | undefined = this.getUIContext().getHostContext()
      if (context) {
        await TextReader.init(context, readerParam);
        this.isInit = true;
      }
    } catch (err) {
      console.error(\`TextReader failed to init. Code: ${err.code}, message: ${err.message}\`);
    }
  }

  // Set action listeners.
  setActionListener() {
    TextReader.on('stateChange', (state: TextReader.ReadState) => {
      this.onStateChanged(state)
    });
    TextReader.on('requestMore', () => this.onStateChanged);
  }

  onStateChanged = (state: TextReader.ReadState) => {
    if (this.selectedReadInfo?.id === state.id) {
      this.readState = state.state;
    } else {
      this.readState = ReadStateCode.WAITING;
    }
  }

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(async () => {
          try {
            this.setActionListener();
            await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch (err) {
            console.error(\`TextReader failed to start. Code: ${err.code}, message: ${err.message}\`);
          }
        })
    }
    .height('100%')
  }
}
