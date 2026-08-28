# Changing the Value of ContentType Dynamically

In form filling scenarios that involve real name registration, the form requires the input of an ID number or the number of another certificate. All certificate numbers use the same input box for fill-in. While **ContentType.ID\_CARD\_NUMBER** currently supports suggestions and auto-filling only for ID card numbers. To support other certificates, you need to dynamically change the value of **ContentType** based on your needs.

#### Display Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/KN1rot92QxyU2MGdoUiJxA/en-us_image_0000002501274198.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ADFF7D115687F567FA674ECAF3857FDFBF9F804B21DC31E1C806560513F80C6 "Click to enlarge")

#### Sample Code

import { hilog } from '@kit.PerformanceAnalysisKit';
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SmartFill {
  // Value of **ContentType** that corresponds to the ID number input component. In this case, **ContentType** is set to the value corresponding to the ID card number type by default.
  @State type: ContentType | undefined = ContentType.ID\_CARD\_NUMBER;
  @State isClicked: boolean = false;

  build() {
    Column({ space: 5 }) {
      Row() {
        Text('ID type:').textAlign(TextAlign.End).width('25%')
        Select(\[{ value: 'ID card' }, { value: 'EEP' }\])
          .width('75%')
          .selected(0)
          .value('ID card')
          .onSelect((index: number, value: string) => {
            // When a user selects the ID type, change the value of **ContentType** for the ID number input component.
            hilog.info(0x000, 'testTag', 'Select item changed, value: ' + value + ', index: ' + index);
            if (value === "ID card") {
              this.type = ContentType.ID\_CARD\_NUMBER;
            } else if (value === "EEP") {
              this.type = undefined;
            }
            hilog.info(0x000, 'testTag', 'ContentType changed, current type: ' + this.type);
          })
      }

      Row() {
        Text('Name:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PERSON\_FULL\_NAME)
      }

      Row() {
        Text('Mobile number:').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PHONE\_NUMBER)
      }

      Row() {
        Text('Certificate number').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(this.type)
      }

      Button('Save')
        .onClick(() => {
          if (!this.isClicked) {
            // Save historical form input actively.
            try {
              autoFillManager.requestAutoSave(this.getUIContext())
            } catch (err) {
              let e: BusinessError = err as BusinessError;
              hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
            }
            this.isClicked = true;
            // Set a timeout period to prevent saving historical form input repeatedly.
            setTimeout(() => {
              this.isClicked = false;
            }, 1000)
            // Or switch to another page through routing to trigger the saving of historical form input.
            this.getUIContext().getRouter().pushUrl({
              url: 'xxx'
            })
          }
        })
        .width("50%")
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
