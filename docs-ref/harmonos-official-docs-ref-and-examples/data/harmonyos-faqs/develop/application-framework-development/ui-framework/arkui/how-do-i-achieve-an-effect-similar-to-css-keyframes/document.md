# How do I achieve an effect similar to CSS keyframes?

Use delayed animations (delay) or trigger a new animation within the **onFinish** callback of the current animation. The code snippet is as follows:

@Entry
@Component
struct AnimateToExample {
  @State widthSize: number = 250;
  @State heightSize: number = 100;
  @State rotateAngle: number = 0;
  private flag: boolean = true;
  @State opacityValue: number = 1;

  build() {
    Column() {
      Button('change size')
        .width(this.widthSize)
        .height(this.heightSize)
        .margin(30)
        .opacity(this.opacityValue)
        .onClick(() => {
          if (this.flag) {
            // Implement multi-stage animations by animateTo
            this.getUIContext().animateTo({
              duration: 2000,
              curve: Curve.EaseOut,
              iterations: 1,
              playMode: PlayMode.Normal,
              onFinish: () => {
                this.getUIContext().animateTo({
                  duration: 2000,
                  curve: Curve.EaseOut,
                  iterations: 1,
                  playMode: PlayMode.Normal,
                  onFinish: () => {
                  }
                }, () => {
                  // Second stage, opacityValue becomes 0.2
                  this.opacityValue = 0.2;
                })
              }
            }, () => {
              // First stage, opacityValue becomes 0.5 
              this.opacityValue = 0.5;
            })
          }
        })
    }.width('100%').margin({ top: 5 })
  }
}

**Reference**

[Explicit Animation (animateTo)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-explicit-animation)
