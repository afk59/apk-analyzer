# How do I implement a loading effect when the page is loaded?

You can use the **Stack** and **LoadingProgress** components to implement the loading effect when the page is first accessed. The code snippet is as follows:

@Entry
@Component
struct PageLoading {
  @State isLoading: boolean = true;

  aboutToAppear(): void {
    // Simulate network request operation, request data from the network 3 seconds later, notify the component, and change the list data
    setTimeout(() => {
      this.isLoading = false;
    }, 3000);
  }

  build() {
    Stack() {
      if (this.isLoading) {
        Column() {
          LoadingProgress()
            .color(Color.White)
            .width(80).height(80)
          Text('Effortlessly loading..')
            .fontSize(16)
            .fontColor(Color.White)
        }
        .width('100%')
        .height('100%')
        .backgroundColor('#40000000')
        .justifyContent(FlexAlign.Center)
      } else {
        Column(){
          Text('Home')
        }
      }
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
  }
}
