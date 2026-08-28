# Requesting Frame Rates for Animations

During application development, you can use the optional parameter [ExpectedFrameRateRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-explicit-animation#expectedframeraterange11) to set an expected frame rate range for a [property animation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-animatorproperty) or an [explicit animation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-explicit-animation).

#### Requesting a Frame Rate for a Property Animation

The code snippet below defines a property animation for the **Text** component and sets the frame rate to 60.

Text('60')
  // ...
  .animation({
    duration: 1200,
    iterations: 10,
    // ...
    expectedFrameRateRange: {
      expected: 60,
      min: 0,
      max: 120,
    },
  })

#### Requesting a Frame Rate for an Explicit Animation

The code snippet below defines an explicit animation for the **Button** component and sets the frame rate to 30.

Button('Start')
  // ...
  .onClick(() => {
    // ...

    this.uiContext?.animateTo({
      duration: 1200,
      iterations: 10,
      // ...
      expectedFrameRateRange: {
        expected: 30,
        min: 0,
        max: 120,
      },
    }, () => {
      // ...
    })

    // ...
  })
