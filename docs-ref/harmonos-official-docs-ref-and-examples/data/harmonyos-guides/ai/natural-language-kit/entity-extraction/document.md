# Entity Extraction

#### Application Scenario

Entity extraction is a key capability of Natural Language Kit. This kit can accurately identify the following types of entities from text based on context information:

1.  **DATETIME**: date and time, for example, June 18, 2024.
2.  **EMAIL**: email address, for example, **_\*\*\*_@example.com**.
3.  **EXPRESS\_NO**: courier number.
4.  **FLIGHT\_NO**: flight number, for example, CA1234.
5.  **LOCATION**: address.
6.  **NAME**: name of a person.
7.  **PHONE\_NO**: mobile number.
8.  **URL**: website link.
9.  **VERIFICATION\_CODE**: verification code number.
10.  **ID\_NO**: ID card number.
     
     By accurately extracting the preceding types of entities, this capability can be widely used in various scenarios, such as news reading, information retrieval, customer service, social chat, and financial operation. For example, in a news reading scenario, entities can be extracted from the news body, and key entity information such as the person's name, place name, date and time, and website link can be highlighted to help readers quickly obtain the key points of the article. In the customer service scenario, information such as mobile numbers, courier numbers, and verification codes can be extracted from users' messages, helping customer service personnel efficiently locate faults and provide solutions. Entity extraction provides solid basic support for intelligent apps in various industries.
     

#### Restrictions

This capability is currently not supported on emulators.

| 
AI Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Entity extraction

 | 

-   Supported languages: simplified Chinese, English, and traditional Chinese
-   Supported entities: time, location, email address, courier number, flight number, person's name, mobile number, website link, verification code, and certificate number
-   Text length: no more than 1,000 characters

 |

#### Development Procedure

1.  Add the entity extraction class to the project.
    
    import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
    
2.  Configure the input text box.
    
    private inputText: string = 'The phone number of Zhang San is 12345.';
    @State outputText: string = '';
    
    TextInput({ placeholder: 'Enter text', text: this.inputText })
      .height(40)
      .fontSize(16)
      .width('90%')
      .margin(10)
      .onChange((value: string) => {
        this.inputText = value;
      })
    
3.  Configure the button that calls the entity extraction API [textProcessing.getEntity](https://developer.huawei.com/consumer/en/doc/harmonyos-references/natural-language-text-processing-api#section6469197174917).
    
    Button ('Extract Entity')
      .type(ButtonType.Capsule)
      .fontColor(Color.White)
      .width('45%')
      .margin(10)
      .onClick(async () => {
        try {
          let result = await textProcessing.getEntity(this.inputText, {entityTypes: \[EntityType.NAME, EntityType.PHONE\_NO\]});
          this.outputText = this.formatEntityResult(result);
        } catch (err) {
          console.error(\`getEntity errorCode: ${err.code}, errorMessage: ${err.message}\`);
          this.outputText = 'Error occurred while getting entities.';
        }
      })
    
4.  Display the entity extraction result on the GUI.
    
    private formatEntityResult(entities: textProcessing.Entity\[\]): string {
      if (!entities || !entities.length) {
        return 'No entities found.';
      }
    
      let output = 'Entities:\\n';
      for (let i = 0; i < entities.length; i++) {
        let entity = entities\[i\];
        output += \`Entity\[${i}\]:\\n\`;
        output += \`  oriText: ${entity.text}\\n\`;
        output += \`  charOffset: ${entity.charOffset}\\n\`;
        output += \`  entityType: ${entity.type}\\n\`;
        output += \`  jsonObject: ${entity.jsonObject}\\n\\n\`;
      }
      return output;
    }
    

#### Development Example

import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';

@Entry
@Component
struct Index {
  private inputText: string = 'The phone number of Zhang San is 12345.';
  @State outputText: string = '';

  build() {
    Column() {
      TextInput({ placeholder: 'Enter text', text: this.inputText })
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

      // Call the entity extraction API.
      Row() {
        Button('Extract Entity')
          .type(ButtonType.Capsule)
          .fontColor(Color.White)
          .width('45%')
          .margin(10)
          .onClick(async () => {
            try {
              let result = await textProcessing.getEntity(this.inputText, {entityTypes: \[EntityType.NAME, EntityType.PHONE\_NO\]});
              this.outputText = this.formatEntityResult(result);
            } catch (err) {
              console.error(\`getEntity errorCode: ${err.code}, errorMessage: ${err.message}\`);
              this.outputText = 'Error occurred while getting entities.';
            }
          })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // Escape the entity extraction result.
  private formatEntityResult(entities: textProcessing.Entity\[\]): string {
    if (!entities || !entities.length) {
      return 'No entities found.';
    }

    let output = 'Entities:\\n';
    for (let i = 0; i < entities.length; i++) {
      let entity = entities\[i\];
      output += \`Entity\[${i}\]:\\n\`;
      output += \`  oriText: ${entity.text}\\n\`;
      output += \`  charOffset: ${entity.charOffset}\\n\`;
      output += \`  entityType: ${entity.type}\\n\`;
      output += \`  jsonObject: ${entity.jsonObject}\\n\\n\`;
    }
    return output;
  }
}
