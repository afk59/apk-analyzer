# How do I use bindSheet with ForEach?

**Answer**

When **bindSheet** is used together with **ForEach**, with **$$this.isShow**, the sheet pops up twice; with **this.isShow**, the number of sheet pop-up times is the length of the array. How do I ensure that the click event of each item in **ForEach** triggers only the pop-up window of the corresponding item without affecting other items?

**Solution**

Bind an @State decorated variable to each sheet.

The code snippet is as follows:

@Entry
@Component
export struct BindSheetAndForEach {
  @State isShow: boolean = false;
  @State arr: number\[\] = \[1, 2, 3, 4\];
  @State isSheetVisible: Array<boolean> = new Array<boolean>(this.arr.length).fill(false);

  @Builder
  myBuilder() {
    Column() {
      Button('content1')
        .margin(10)
        .fontSize(20)
    }
    .width('100%')
  }

  // Each array item corresponds to an independent pop-up window displaying the status, which is index bound
  build() {
    Column() {
      ForEach(this.arr, (item: number, idx: number) => {
        Row() {
          Text('item')
          Button('Bullet Frame')
            .onClick(() => {
              this.isSheetVisible\[idx\] = true;
            })
            .fontSize(15)
            .margin(10)
            .bindSheet(this.isSheetVisible\[idx\], this.myBuilder(), {
              backgroundColor: Color.Gray,
              height: SheetSize.MEDIUM,
              showClose: true,
              onWillDisappear: () => {
                this.isSheetVisible\[idx\] = false;
              }
            })
          Checkbox()
        }
        .border({ width: 1, radius: 5 })
      })
    }
    .justifyContent(FlexAlign.Start)
    .width('100%')
    .height('100%')
  }
}
