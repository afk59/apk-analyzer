# Word Segmentation

#### Application Scenario

Word segmentation is to convert Chinese characters, English characters, and digits in a text file into words or phrases, providing a basis for subsequent conversion into word vectors. Word segmentation is applied in various scenarios, for example, when the search engine extracts keywords from the user's input text after segmentation and sends them to the search engine.

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Word segmentation

 | 

-   Supported languages: simplified Chinese, English, and traditional Chinese
-   Text length: no more than 1,000 characters

 |

#### Development Procedure

1.  Reference related classes and add them to the project.
    
    import { textProcessing } from '@kit.NaturalLanguageKit';
    
2.  Configure the input text box and button and call the word segmentation API [textProcessing.getWordSegment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/natural-language-text-processing-api#section4612914419).
    
    private inputText: string = '';
    @State outputText: string = '';
    
    TextInput({ placeholder: 'Enter text' })
      .height(40)
      .fontSize(16)
      .width('90%')
      .margin(10)
      .onChange((value: string) => {
        this.inputText = value;
      })
    
    Button('Segment Word')
      .type(ButtonType.Capsule)
      .fontColor(Color.White)
      .width('45%')
      .margin(10)
      .onClick(async () => {
        try {
          let result = await textProcessing.getWordSegment(this.inputText);
          this.outputText = this.formatWordSegmentResult(result);
        } catch (err) {
          console.error(\`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}\`);
        }
      })
    
3.  Display the word segmentation result ([WordSegment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/natural-language-text-processing-api#section12706154134017)) on the GUI.
    
    private formatWordSegmentResult(segments: textProcessing.WordSegment\[\]): string {
      let output = 'Word Segments:\\n';
      segments.forEach((segment, index) => {
        output += \`Word\[${index}\]: ${segment.word}, Tag: ${segment.wordTag}\\n\`;
      });
      return output;
    }
    

#### Development Example

import { textProcessing } from '@kit.NaturalLanguageKit';

@Entry
@Component
struct Index {
  private inputText: string = '';
  @State outputText: string = '';

  build() {
    Column() {
      TextInput({ placeholder: 'Enter text' })
        .height(40)
        .fontSize(16)
        .width('90%')
        .margin(10)
        .onChange((value: string) => {
          this.inputText = value;
        })

      Scroll() {
        Text(this.outputText)
          .fontSize(16)
          .width('90%')
          .margin(10)
      }
      .height('40%')

      // Call the word segmentation API.
      Row() {
        Button('Segment Word')
          .type(ButtonType.Capsule)
          .fontColor(Color.White)
          .width('45%')
          .margin(10)
          .onClick(async () => {
            try {
              let result = await textProcessing.getWordSegment(this.inputText);
              this.outputText = this.formatWordSegmentResult(result);
            } catch (err) {
              console.error(\`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}\`);
            }
          })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // Escape the word segmentation result.
  private formatWordSegmentResult(segments: textProcessing.WordSegment\[\]): string {
    let output = 'Word Segments:\\n';
    segments.forEach((segment, index) => {
      output += \`Word\[${index}\]: ${segment.word}, Tag: ${segment.wordTag}\\n\`;
    });
    return output;
  }
}
