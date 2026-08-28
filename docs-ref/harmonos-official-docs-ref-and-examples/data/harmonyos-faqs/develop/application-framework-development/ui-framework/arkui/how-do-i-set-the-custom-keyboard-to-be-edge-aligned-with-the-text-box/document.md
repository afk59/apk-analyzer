# How do I set the custom keyboard to be edge-aligned with the text box?

A custom keyboard can be implemented using a custom dialog box. The custom dialog box maintains a default distance from the bottom edge, you can set the offset property to achieve edge alignment, and set **keyboardAvoidDistance** to align it with the keyboard. Refer to the code snippet below.

@Entry
@Component
struct CustomDialogPage {
  @State message: string = 'CustomDialogPage';
  customDialogController: CustomDialogController = new CustomDialogController({
    builder: CustomEditDialogWidget({
      inputType: InputType.Normal,
      textInputConString: () => {
      }
    }),
    alignment: DialogAlignment.Bottom,
    maskColor: Color.White,
    customStyle: true
  });

  build() {
    Row() {
      Column() {
        Button(this.message).onClick(() => {
          this.customDialogController.open();
        });
      }
      .width('100%');
    }
    .height('100%');
  }
}

@CustomDialog
@Component
export struct CustomEditDialogWidget {
  controller?: CustomDialogController;
  @State textInputString: string = '';
  textInputConString = () => {
  };
  inputType: InputType = InputType.Normal;

  build() {
    Column() {
      TextArea({ placeholder: 'please input' })
        .width('80%')
        .backgroundColor(Color.Transparent)
        .defaultFocus(true)
        .onChange((value: string) => {
          this.textInputString = value;
        });
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Start)
    .width('80%')
    .height(450)
    .borderRadius(10)
    .backgroundColor('#fffaf7f7')
    .offset({ x: 0, y: 16 });
  }
}
