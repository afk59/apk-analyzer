# License Plate Number Filling Suggestion

SmartFill supports license plate number filling suggestions since version 5.1.0(18).

To enhance license plate number form filling, you can implement SmartFill to provide input suggestions based on historical license plate number inputs saved in recent forms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/nFCGlPvKQeSVyZ3uE57DEA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85FB1858A2220103FC16F5A6E6FBF62548E73F0563C64A37EE23E0B8C215DDDE)

Suggestions are made only based on the device owner's recent form information. (The owner is identified by the signed-in HUAWEI ID, which is the combination of real name + mobile number/email address. To determine the real name information, the Account Kit data source needs to be enabled.)

#### Display Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/ZqXUXQvqTH-fZunq5S2oRw/en-us_image_0000002503412161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062119Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3081AF3E19E70A6CBDBD53EC53D90A84CB6C8A7F4EF604EEBFCD163385A7123E "Click to enlarge")

#### Sample Code

import { display } from '@kit.ArkUI';

const NEW\_ENERGY\_TEXT = 'New energy';

@Extend(Text)
function extendStyles(value: string, width: number, height: number, active: boolean) {
  .fontSize(value === NEW\_ENERGY\_TEXT ? 10 : 18)
  .fontWeight(FontWeight.Medium)
  .textAlign(TextAlign.Center)
  .width(width)
  .height(height)
  .borderWidth('3px')
  .borderColor(active ? Color.Blue : '#ccc')
  .borderRadius(5)
}

@Entry
@Component
struct LicensePlate {
  // Number of input boxes for license plate number input.
  private length = 8;
  private licenseItemId = '\_license\_item';
  @State licensePlateVal: string\[\] = \[\];
  @State activeIndex: number = -1;
  @State itemWidth: number = 30;
  @State itemHeight: number = 30;
  @State inputText: string = '';
  // Whether the user has activated information input.
  @State isUserInput: boolean = false;
  // Match the value of the previous input box in the saved form.
  private beforeValue: string = '';

  aboutToAppear(): void {
    this.licensePlateVal = new Array(this.length).fill('');
    let displayClass = display.getDefaultDisplaySync();
    let width = displayClass.width;
    // Calculate the width of each input box based on the screen width.
    this.itemWidth = this.getUIContext().px2vp(width) / (this.length + 1) - 4;
    this.itemHeight = this.itemWidth \* 1.2;
  }

  setValue(val: string): void {
    if (!this.isUserInput) {
      // Fill in the license plate number based on SmartFill suggestions.
      this.handleAutoFill(val);
      this.beforeValue = val;
      return;
    }
    if (!val || val.length === 0 || this.beforeValue.length > val.length) {
      let licensePlate = this.getLicensePlate();
      if (licensePlate.length > 0) {
        this.inputText = licensePlate;
      }
      this.beforeValue = this.inputText;
      return;
    }
    let inputData = val.substring(this.beforeValue.length);
    if (inputData.length > this.length) {
      inputData = inputData.substring(0, this.length);
    }
    // A user can only change the number of a selected input box at a time; while a suggestion from SmartFill will replace the values of all input boxes.
    this.handleUserInput(inputData);
    this.beforeValue = val;
  }

  getLicensePlate(): string {
    return this.licensePlateVal.join('');
  }

  handleUserInput(val: string): void {
    if (val.length > this.length - this.activeIndex) {
      val = val.substring(0, this.length - this.activeIndex);
    }
    for (let i = 0; i < val.length; i++) {
      this.licensePlateVal\[this.activeIndex\] = val\[i\];
      this.activeIndex = Math.min(this.activeIndex + 1, this.length - 1);
    }
  }

  handleAutoFill(val: string): void {
    let value = val.split('');
    this.licensePlateVal.fill('');
    for (let i = 0; i < this.length; i++) {
      this.licensePlateVal\[i\] = i < value.length ? value\[i\] : this.licensePlateVal\[i\];
    }
    this.activeIndex = Math.min(value.length + 1, this.length - 1);
  }

  handleDelete() {
    if (!this.licensePlateVal\[this.activeIndex\]) {
      this.licensePlateVal\[this.activeIndex - 1\] = '';
    } else {
      this.licensePlateVal\[this.activeIndex\] = '';
    }
    this.activeIndex = Math.max(0, this.activeIndex - 1);
  }

  getValue(index: number): string {
    return (index === this.length - 1 && !this.licensePlateVal\[index\]) ? NEW\_ENERGY\_TEXT : this.licensePlateVal\[index\];
  }

  handleLicenseClick(screenX: number) {
    for(let index = 0; index <= 7; index++) {
      let id = index + this.licenseItemId;
      let position = this.getUIContext().getComponentUtils().getRectangleById(id);
      // Position relative to the screen, in px.
      let left = position?.screenOffset?.x ?? 0;
      let right = left + (position?.size?.width ?? 0);
      if (screenX >= left && screenX <= right) {
        this.activeIndex = index;
      }
    }
  }

  @Builder
  displayItem(index: number) {
    Column() {
      Text(this.getValue(index))
        .extendStyles(this.getValue(index), this.itemWidth, this.itemHeight, this.activeIndex === index)
    }
    .id(index + this.licenseItemId)
    .padding({
      left: 2,
      right: 2
    })
  }

  @Builder
  buildLicensePlateNumber() {
    Flex({
      direction: FlexDirection.Row,
      alignItems: ItemAlign.Center,
      justifyContent: FlexAlign.SpaceBetween
    }) {
      Column() {
        Row() {
          Text("License plate")
        }.height(30)

        Stack({ alignContent: Alignment.BottomStart }) {
          Row() {
            this.displayItem(0)
            this.displayItem(1)
            Text('·')
              .fontSize(22)
              .fontWeight(600)
              .height(this.itemHeight)
            this.displayItem(2)
            this.displayItem(3)
            this.displayItem(4)
            this.displayItem(5)
            this.displayItem(6)
            this.displayItem(7)
          }

          TextInput({ text: $$this.inputText })
            .width('100%')
            .height('100%')
            .opacity(0)
            .contentType(ContentType.LICENSE\_PLATE)
            .onClick((event) => {
              // X-axis coordinate relative to the screen, in px.
              let displayX = this.getUIContext().vp2px(event.displayX);
              this.handleLicenseClick(displayX);
              if (this.activeIndex < 0) {
                this.activeIndex = 0;
              }
            })
            .onChange((val: string) => {
              if (val === this.beforeValue) {
                return;
              }
              this.setValue(val);
              this.isUserInput = false;
            })
            .onDidInsert(() => {
              // Triggered when information is entered using the input method. If the input method is user-defined, set **isUserInput** to **true** when a user enters information.
              this.isUserInput = true;
            })
            .onDidDelete((val: DeleteValue) => {
              // Triggered when information is deleted using the input method. If the input method is user-defined, set **isUserInput** to **true** when a user deletes information and call the required function for processing.
              if (val?.deleteValue?.length > 0) {
                this.isUserInput = true;
              }
              this.handleDelete();
            })
        }
        .height(this.itemHeight)
        .margin({ top: 20 })
      }
    }
    .backgroundColor(Color.White)
    .height(50)
    .margin({ left: 15, right: 15 })
    .id("customInput")
    .defaultFocus(false)
  }

  build() {
    Column() {
      this.buildLicensePlateNumber()
    }
  }
}
