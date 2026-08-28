# UITest User Guide

#### Overview

UITest provides UI search and operation simulation capabilities for key scenarios of automated UI tests, including accurate UI component search, UI interaction operations (such as tap, swipe, and text input), and peripheral behavior simulation (such as keyboard input, mouse operation, touchpad gesture, and stylus action).

#### Capabilities

UITest supports both ArkTS APIs and commands, providing flexible and efficient technical support for automated UI tests.

**ArkTS script development**:

UITest provides simple and easy-to-use APIs for various test scenarios. It supports common UI interaction operations, such as tap, double-tap, long press, and swipe, helping you quickly develop automated test scripts based on UI interaction logic.

**Command line testing**:

UITest supports diversified test operations through commands, including obtaining the current screen screenshot, obtaining the component tree, recording the screen operation process, and easily injecting UI simulation events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/v3i2r3LQScqkKOf8Ng2xtQ/en-us_image_0000002568684849.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC57DEE3FB83DE9C2B17FC553E6B6DFD03F84FDCB446386D876489DE0A1F6529)

UITest consists of the client and server.

**Client**:

Provides a cross-language communication layer and IPC module to export APIs and launch UITest. The client is loaded by the test application and runs in the application process. The cross-language communication layer exports APIs, processes JSON serialization objects, converts ArkTS APIs into C++ APIs, and parses and verifies parameters. In addition, this module involves invoking ArkTS callback functions from the C++ layer. Therefore, the cross-language communication layer manages and invokes ArkTS callbacks.

**Server**:

Runs as an independent process and communicates with the client through IPC. After the server starts, it establishes a connection with the client through broadcast. The IPC ensures that the connection is not interrupted. The server listens for the client process status and starts or stops the client process as required. The server processes the core logic of UITest, which consists of the following parts:

1.  General framework running capability: processes IPC messages, manages processes, C++ APIs, and error codes, and listens for API calling.
2.  UI test capability: parses accessibility nodes to build a page component tree, matches and searches for components, constructs operation events, injects multimodal events, listens for UI events, and controls screen display.

#### Using ArkTS APIs to Perform UI Tests

The following describes how to use the ArkTS APIs of UITest.

The UITest API is called based on [unit tests](../jsunit-user-guide/document.md). For details about the APIs and parameters, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-uitest).

## UI Test Example

The following example describes how to develop a UI test based on the JsUnit script. The functionalities are as follows:

1.  Call the [program framework service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-abilitydelegator) capability to start the target application and check the application running status.
2.  Call the UITest capability to perform a tap operation on the page.
3.  Add an [assertion capability](../jsunit-user-guide/document.md#assertion) to check whether the actual changes on the current page are as expected.

Perform the following steps:

1.  Write the **Index.ets** page code in the **main** > **ets** > **pages** folder as the test demo.
    
    @Entry
    @Component
    struct Index {
        @State message: string = 'Hello World';
        @State text: string = '';
        build() {
        Row() {
            Column() {
            Text(this.message)
                .fontSize(50)
                .fontWeight(FontWeight.Bold)
            Text("Next")
                .fontSize(50)
                .margin({top:20})
                .fontWeight(FontWeight.Bold)
                .onClick((event?: ClickEvent) => {
                    if(event){
                        this.text = "after click";
                    }
                })
            .width('100%')
            Text(this.text).margin(15)
            }
        }
        .height('100%')
        }
    }
    
2.  Create the **uitest.test.ets** file in the **ohosTest** > **ets** > **test** folder and write the test code.
    
    import { describe, it, expect, Level } from '@ohos/hypium';
    // Import the test dependencies.
    import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';
    import { UIAbility, Want } from '@kit.AbilityKit';
    
    const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
    export default function abilityTest() {
      describe('ActsAbilityTest', () => {
        it('testUiExample',Level.LEVEL3, async (done: Function) => {
          console.info("uitest: TestUiExample begin");
          // Initialize the Driver object.
          const driver = Driver.create();
          const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
          // Specify the bundle name and ability name of the application to be tested.
          const want: Want = {
              bundleName: bundleName,
              abilityName: 'EntryAbility'
          }
          // Start the application to be tested.
          await delegator.startAbility(want);
          // Wait until the application starts.
          await driver.waitForIdle(4000,5000);
          // Ensure that the top ability of the application is the specified ability.
          const ability: UIAbility = await delegator.getCurrentTopAbility();
          console.info("get top ability");
          expect(ability.context.abilityInfo.name).assertEqual('EntryAbility');
    
          // Search for the target component based on the specified text Next.
          const next = await driver.findComponent(ON.text('Next'));
          // Tap the target component.
          await next.click();
          await driver.waitForIdle(4000,5000);
          // Assert the component with text "after click" exists to ensure the page changes as expected.
          await driver.assertComponentExist(ON.text('after click'));
          await driver.pressBack();
          done();
        })
      })
    }
    

## Searching for and Operating Components

With UITest, you can [creating a matcher based on multiple attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-uitest#on9) to search for one or more target components on the current page and return the component object. You can also search for target component inside the scroll component and [perform operations on control objects or obtain control attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-uitest#component9).

The following example shows how to search for and operate a component. Before executing the following code, implement the code of the **Index.ets** page by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, Component, ON, On } from '@kit.TestKit';

export default function abilityTest() {
  describe('componentOperationTest', () => {
    /\*\*
     \* Search for the Button component and click it.
     \*/
    it("componentSearchAndOperation", TestType.FUNCTION, async () => {
      let driver: Driver = Driver.create();
      let button: Component = await driver.findComponent(ON.type('Button'));
      await button.click();
    })

    /\*\*
     \* Search for the Scroll component whose text is "123" using relative position.
     \*/
    it("relativePositioncomponentSearch", TestType.FUNCTION, async () => {
      let driver: Driver = Driver.create();
      let on: On = ON.text('123').within(ON.type('Scroll'));
      let items: Array<Component> = await driver.findComponents(on);
    })

    /\*\*
     \* Search for the Image component and pinch it out.
     \*/
    it("componentPinch", TestType.FUNCTION, async () => {
      let driver: Driver = Driver.create();
      let image: Component = await driver.findComponent(ON.type('Image'));
      await image.pinchOut(1.5);
    })
  })
}

## Simulating Touch Operations

UITest supports simulating events such as tap, double-tap, long press, swipe, drag, and multi-finger operations.

The following example shows how to simulate touch operations at the coordinate level. Before executing the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, PointerMatrix, UiDirection } from '@kit.TestKit';

export default function abilityTest() {
  describe('screenOperationTest', () => {
    /\*\*
     \* Simulate touch operations based on coordinates.
     \*/
    it("touchScreenOperation", TestType.FUNCTION, async () => {
      let driver: Driver = Driver.create();
      // Tap.
      await driver.click(100,100);
      // Tap the specified display.
      await driver.clickAt({ x: 100, y: 100, displayId: 0 });
      // Swipe.
      await driver.swipe(100, 100, 200, 200, 600);
      // Swipe the specified display.
      await driver.swipeBetween({x: 100, y: 100, displayId: 0}, {x: 1000, y: 1000, displayId: 0}, 800);
      // Fling.
      await driver.fling({x: 100, y: 100},{x: 200, y: 200}, 5, 600);
      // Fling in a specified direction.
      await driver.fling(UiDirection.DOWN, 10000);
      // Drag.
      await driver.drag(100, 100, 200, 200, 600);
      // Specify the display ID and the long press duration before dragging.
      await driver.dragBetween( {x: 100, y: 100, displayId: 0}, {x: 1000, y: 1000, displayId: 0}, 800, 1500);
      // Simulate a two-finger operation, with each finger scrolling based on two coordinates.
      let pointers: PointerMatrix = PointerMatrix.create(2, 2);
      pointers.setPoint(0, 0, {x: 100, y: 100});
      pointers.setPoint(0, 1, {x: 200, y: 100});
      pointers.setPoint(1, 0, {x: 100, y: 200});
      pointers.setPoint(1, 1, {x: 200, y: 200});
      await driver.injectMultiPointerAction(pointers);
    })
  })
}

## Waiting for Page Loading Completion

When interacting with a page, you can determine whether the page redirection is complete by waiting for a component to appear or waiting for the page to be idle within a specified period of time.

The following example describes how to wait for page loading completion. Before executing the following code, implement the **Index.ets** page code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, Level, TestType, Size } from '@ohos/hypium';
// Import the test dependencies.
import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';

const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
// Specify the bundle name and ability name of the application to be tested.
const bundleName: string = 'com.uitestScene.acts'
const abilityName: string = 'com.uitestScene.acts.MainAbility'
export default function abilityTest() {
  describe('ActsAbilityTest', () => {
    it('testWaitForComponent\_static', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async (): Promise<void> => {
      let driver = Driver.create();
      // Start the target application.
      await delegator.executeShellCommand(\`aa start -b ${bundleName} -a ${abilityName}\`).then(result => {
        console.info(\`UITestCase, start abilityFinished: ${result}\`)
      }).catch((err: Error) => {
          console.error(\`UITestCase, start abilityFailed: ${err}\`)
      })
      // Wait for the specified component on the target application's home screen to appear, confirming that the application has started.
      let button = await driver.waitForComponent(ON.text('StartAbility Success!'), 1000);
    })
  })
}

## Simulating Text Input

UITest supports text input at a specified coordinate or to a specified component. [Specify the input mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-uitest#inputtextmode20) is also supported, that is, whether to copy and paste the text or add the text.

The following example describes how to input text based on components and coordinates. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, ON } from '@kit.TestKit';

export default function abilityTest() {
  describe('inputTextTest', () => {
    /\*\*
     \* Clear the text by default and then inputs the specified text based on the component.
     \* If the input text does not contain Chinese characters or special characters and its length does not exceed 200 characters, it is input word by word by default.
     \*/
    it('componentInputText', TestType.FUNCTION, async () => {
      let driver = Driver.create();
      let input = await driver.findComponent(ON.type('TextInput'));
      await input.inputText('abc');
    })
    /\*\*
     \* Inject specified text in copy and paste mode based on the component.
     \* Input text in addition mode. That is, the original content is not cleared when the text is input.
     \*/
    it('componentInputTextAddition', TestType.FUNCTION, async () => {
      let driver = Driver.create();
      let input = await driver.findComponent(ON.type('TextInput'));
      await input.inputText('abc', {paste: true, addition: true});
    })

    /\*\*
     \* Focus the text box by tapping the specified position and input the specified text at the cursor based on the coordinates.
     \* If the input text does not contain Chinese characters or special characters and its length does not exceed 200 characters, it is input word by word by default.
     \*/
    it('pointInputText', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create()
      let input = await driver.findComponent(ON.type('TextInput'))
      let center = await input.getBoundsCenter()
      await driver.inputText(center, 'abc')
    })

    /\*\*
     \* Inject specified text in copy and paste mode based on the coordinates.
     \* Input in addition mode, that is, after the text box is focused by tapping the specified position, the cursor is moved to the end of the original text and then the specified text is input.
     \*/
    it('pointInputTextAddition', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create()
      let input = await driver.findComponent(ON.type('TextInput'))
      let center = await input.getBoundsCenter()
      await driver.inputText(center, '123', {paste: true, addition: true})
    })

    /\*\*
     \* Inject specified text in copy and paste mode based on the coordinates.
     \* Input in addition mode, that is, after the text box is focused by tapping the specified position, the cursor is moved to the end of the original text and then the specified text is input.
     \* If the input content contains Chinese characters or special characters, the text can be input only in copy and paste mode, and the paste field does not take effect.
     \*/
    it('pointInputTextChinese', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create()
      let input = await driver.findComponent(ON.type('TextInput'))
      let center = await input.getBoundsCenter()
      await driver.inputText(center, 'Hello', {paste: false, addition: true})
    })
  })
}

## Capturing Screenshots

**Note**:

1.  You need to specify the path for saving screenshots to [sandbox path](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md) of the application.
2.  The [APL Level](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-concepts-in-the-permission-mechanism) of the test HAP is **normal**. Therefore, the application sandbox path in the user-level encryption area must be used. In addition, the file should be saved in the subdirectory for saving the application's persistent data on the device.

The following example shows how to capture a screenshot with the display ID and area specified and save the screenshot to a specified path. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example". In the multi-display scenario, to capture a screenshot of a specified display, you can call the API of the display module to [obtain the display object](../../../../../application-framework/arkui/display-management/using-display-to-obtain-display-properties-and-listen-for-status-changes-arkts/document.md#obtaining-a-display-object), and then [obtain screen-related attributes](../../../../../application-framework/arkui/display-management/using-display-to-obtain-display-properties-and-listen-for-status-changes-arkts/document.md#obtaining-display-properties).

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver } from '@kit.TestKit';
import { display } from '@kit.ArkUI';

export default function abilityTest() {
  describe('screenCaptureTest', () => {
    /\*\*
     \* Capture the screen of a specified area and save the screenshot to a specified path.
     \*/
    it('screenCapture', TestType.FUNCTION, async () => {
      let driver = Driver.create();
      // Application sandbox path. el2 indicates the user-level encryption, and base indicates the subdirectory for saving the application's persistent data on the device.
      // Use the actual path.
      let savePath = '/data/storage/el2/base/cache/1.png';
      let res = await driver.screenCapture(savePath, {left: 0, top: 0, right: 100, bottom: 100});
    })

    /\*\*
     \* Capture the full screen based on the specified display ID and save it to the specified path.
     \*/
    it('screenCapWithId', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Obtain the default display object.
      let disPlay = display.getDefaultDisplaySync();
      let savePath = '/data/storage/el2/base/cache/1.png'
      let res = await driver.screenCap(savePath, disPlay.id);// Obtain the default display ID.
    })
  })
}

## Listening for UI Events

The following example describes how to listen for UI events, including setting the listening callback, listening for the **Toast** and **Dialog** components, and proceeding after an event occurs. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, UIElementInfo } from '@kit.TestKit';

export default function abilityTest() {
  describe('observerTest', () => {
    // Listen for the display of the Toast component.
    it("toastObserver", TestType.FUNCTION, async () => {
      let driver = Driver.create();
      let observer = driver.createUIEventObserver();
      let callback = (uiElementInfo : UIElementInfo) => {
        let bundleName = uiElementInfo.bundleName;
        let text = uiElementInfo.text;
        let type = uiElementInfo.type;
      }
      observer.once('toastShow', callback);
    })
  })
}

## Simulating Keyboard and Mouse Operations

The following example describes how to simulate keyboard and mouse operations, including single key and combination key input, mouse click, move, and drag, and key and mouse combination operations. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, MouseButton } from '@kit.TestKit';
import { KeyCode } from '@ohos.multimodalInput.keyCode';

export default function abilityTest() {
  describe('KeyboardMouseTest', () => {
    // Simulate key input and combination key input.
    it('keyBoardOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Simulate key input (inject the Back key).
      await driver.triggerKey(KeyCode.KEYCODE\_BACK);
      // Simulate combination key input (inject the Save combination key).
      await driver.triggerCombineKeys(KeyCode.KEYCODE\_CTRL\_LEFT,  KeyCode.KEYCODE\_S);
    })

    // Simulate the operations of left-clicking, moving, and dragging the mouse.
    it('mouseOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Left-click the mouse.
      await driver.mouseClick({x: 100, y: 100}, MouseButton.MOUSE\_BUTTON\_LEFT);
      // Move the mouse.
      await driver.mouseMoveTo({x: 100, y: 100});
      // Drag the mouse.
      await driver.mouseDrag({x: 100, y: 100}, {x: 200, y: 200}, 600);
    })

    // Simulate key and mouse combination operations.
    it('combinedOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Press the left Ctrl key and scroll the mouse wheel.
      await driver.mouseScroll({x:100, y:100}, true, 30, KeyCode.KEYCODE\_CTRL\_LEFT);
      // Press the left Ctrl key and long-click the left mouse button.
      await driver.mouseLongClick({x:100, y:100}, MouseButton.MOUSE\_BUTTON\_LEFT, KeyCode.KEYCODE\_CTRL\_LEFT);
    })
  })
}

## Searching for and Operating Windows

The following example describes how to search for and minimize a window based on the window properties. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, expect } from '@ohos/hypium';
// Import the test dependencies.
import { Driver } from '@kit.TestKit';
const DeviceErrorCode = 17000005;

export default function abilityTest() {
  describe('windowOperationTest', () => {
    // Search for an active window based on specified properties and minimize the window.
    it("windowSearchAndOperation", TestType.FUNCTION, async () => {
      let driver = Driver.create();
      try {
        let window = await driver.findWindow({active: true});
        await window.minimize();
      } catch (error) {
        // If the minimize API is called on a device that does not support window operations, the 17000005 error code will be thrown.
        console.log(\`$ windowSearchAndOperation error is: ${JSON.stringify(error)}\`);
        expect(error.code).assertEqual(DeviceErrorCode);
      }
    })
  })
}

## Simulating Touchpad Operations

The following example describes how to simulate the touchpad operations of swiping up with three fingers to return to the home screen and swiping down with three fingers to return to the application window. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level, expect } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, UiDirection } from '@kit.TestKit';
const DeviceErrorCode = 17000005;

export default function abilityTest() {
  describe('touchPadOperationTest', () => {
    // Simulate the three-finger swipe up (to return to the home screen) and three-finger swipe down (to restore the window) operations on the touchpad in the PC/2-in-1 device.
    it('touchPadOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      try {
        // Swipe up with three fingers to return to the home screen.
        await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
        // Swipe down with three fingers to restore the application window.
        await driver.touchPadMultiFingerSwipe(3, UiDirection.DOWN);
      } catch (error) {
        // If this API is called on a device that does not support touchpad operations, the 17000005 error code will be thrown.
        console.log(\`$ windowSearchAndOperation error is: ${JSON.stringify(error)}\`);
        expect(error.code).assertEqual(DeviceErrorCode);
      }
    })
  })
}

## Simulating Stylus Operations

The following example describes how to simulate stylus operations such as clicking, swiping, and setting pressure. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver } from '@kit.TestKit';

export default function abilityTest() {
  describe('penOperationTest', () => {
    // Simulate stylus operations such as click, double-click, long-click, and swipe.
    it('penOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Click with the stylus.
      await driver.penClick({x: 100, y: 100});
      // Double-click with the stylus.
      await driver.penDoubleClick({x: 100, y: 100});
      // Long-click with the stylus.
      await driver.penLongClick({x: 100, y: 100}, 0.5);
      // Swipe with the stylus.
      await driver.penSwipe({x: 100, y: 100}, {x: 100, y: 500}, 600, 0.5);
    })
  })
}

## Simulating Crown Operations

The following example shows how to simulate clockwise and counter-clockwise crown rotations. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level, expect } from '@ohos/hypium';
// Import the test dependencies.
import { Driver } from '@kit.TestKit';
const CapabilityCode = 801;

export default function abilityTest() {
  describe('crownRotateTest', () => {
    // Simulate clockwise and counter-clockwise crown rotations.
    it('crownRotate', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      try {
        // Rotate 50 ticks clockwise at a speed of 30 ticks per second.
        await driver.crownRotate(50, 30);
        // Rotate 20 ticks counterclockwise at a speed of 30 ticks per second.
        await driver.crownRotate(-20, 30);
      } catch (error) {
        // driver.crownRotate is valid only on smart watches. If it is called on other devices, error code 801 will be thrown.
        console.log(\`$ testCrownRotate error is: ${JSON.stringify(error)}\`);
        expect(error.code).assertEqual(CapabilityCode);
      }
    })
  })
}

## Simulating Display Operations

The following example shows how to simulate display operations, including obtaining display properties such as size and density, waking up the display, and rotating it. Before running the following code, implement the **Index.ets page** code by referring to "UI Test Example".

// ohosTest/ets/test/uitest.test.ets
import { describe, it, TestType, Size, Level } from '@ohos/hypium';
// Import the test dependencies.
import { Driver, Point } from '@kit.TestKit';

export default function abilityTest() {
  describe('crownRotateTest', () => {
    // Obtain display properties and operate the display.
    it('displayOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
      let driver = Driver.create();
      // Obtain the display size.
      let size: Point = await driver.getDisplaySize();
      // Obtain the display density.
      let density: Point = await driver.getDisplayDensity();
      // Wake up the display.
      await driver.wakeUpDisplay();
      // Rotate the display clockwise by 90 degrees.
      await driver.setDisplayRotation(DisplayRotation.ROTATION\_90);
    })
  })
}

#### Using Commands to Perform UI Tests

During development, you can use commands to quickly perform test operations such as capturing screenshots, recording UI operations, injecting UI simulation operations, and obtaining the component tree.

## Environment Setup

The environment for HarmonyOS Device Connector (hdc) has been set up. For details, see [Environment Setup](../../../performance-analysis-kit/command-line-tools/hdc/document.md#environment-setup). The devices are properly connected and **hdc shell** is executed.

## Commands

| Command | Parameter | Description |
| :-- | :-- | :-- |
| help | \- | Displays the commands supported by the UITest tool. |
| screenCap | \[-p\] \[-d\] | 
Captures a screenshot.

For details about the parameters, see [Obtaining a Screenshot](#obtaining-a-screenshot).

 |
| dumpLayout | \[-p\] <-i | -a | -b | -w | -m | -d> | 

Obtains the component tree.

For details about the parameters, see [Obtaining the Component Tree](#obtaining-the-component-tree).

 |
| uiRecord | <record | read> | 

Records UI operations.

**record**: starts recording the operations on the current page to **/data/local/tmp/record.csv**. To stop recording, press **Ctrl+C**.

**read**: reads and prints recorded data.

For details about the parameters, see [Recording UI Operations](#recording-ui-operations).

 |
| uiInput | <help | click | doubleClick | longClick | fling | swipe | drag | dircFling | inputText | keyEvent | text> | 

Injects UI simulation operations.

For details about the parameters, see [Injecting UI Simulation Operations](#injecting-ui-simulation-operations).

 |
| \--version | \- | Obtains the version information about the current UITest tool. |
| start-daemon | \- | Starts the UITest process. |

## Obtaining a Screenshot

| Parameter | Level-2 Parameter | Description |
| :-- | :-- | :-- |
| \-p | <savePath> | Used to specify storage path and file name, which must be **/data/local/tmp/**. The default path is **/data/local/tmp**, and the file name format is **Timestamp+.png**. |
| \-d | <displayId> | 
Used to specify the ID of the display to capture in the multi-display scenario.

**Note**: This command is supported since API version 20.

 |

\# Save the file in the format of Timestamp + .png in /data/local/tmp.
hdc shell uitest screenCap
# Specify the file name and save the file in /data/local/tmp/.
hdc shell uitest screenCap -p /data/local/tmp/1.png

## Obtaining the Component Tree

| Parameter | Level-2 Parameter | Description |
| :-- | :-- | :-- |
| \-p | <savePath> | Used to specify storage path and file name, which must be **/data/local/tmp/**. The default path is **/data/local/tmp**, and the file name format is **Timestamp+.json**. |
| \-i | \- | Used to disable filtering of invisible components and window merging. |
| \-a | \- | 
Used to save the **BackgroundColor**, **Content**, **FontColor**, **FontSize**, and **extraAttrs** attributes of the component.

**Note**: By default, the preceding attributes are not saved. The **\-a** and **\-i** parameters cannot be used at the same time.

 |
| \-b | <bundleName> | Used to obtain the component tree information of the target window based on the specified bundle name. |
| \-w | <windowId> | 

Used to obtain the component tree information of the target window based on the specified window ID.

**Note**:

You can use hidumper to obtain the window ID of an application. For details, see [Obtaining Application Window Information](../../../performance-analysis-kit/command-line-tools/hidumper/hidumper/document.md#obtaining-application-window-information).

 |
| \-m | <true|false> | Used to specify whether to merge the window information when the component tree information is obtained. The value **true** means to merge window information, and **false** means the opposite. If this parameter is not set, the default value **true** is used. |
| \-d | <displayId> | 

Used to specify the ID of the display whose component tree is to be obtained in the multi-display scenario.

**Note**:

1\. This command is supported since API version 20.

2\. You can use hidumper to obtain the display ID of an application. For details, see [Obtaining Application Window Information](../../../performance-analysis-kit/command-line-tools/hidumper/hidumper/document.md#obtaining-application-window-information).

 |

\# Specify the file name and save the file in /data/local/tmp/.
hdc shell uitest dumpLayout -p /data/local/tmp/1.json

## Recording UI Operations

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/TJEU1-iQRGGM2hL0CpMYAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E73495F45DE99E8C74CF2CAB73B6351CDE9FCD263B77D486CC36B149068B6DB)

During the recording, you should perform the next operation after the recognition result of the current operation is displayed in the CLI.

**Parameters**

| Parameter | Level-2 Parameter | Description |
| :-- | :-- | :-- |
| \-W | <true/false> | 
Used to specify whether to save the component information corresponding to the operation coordinates to the **/data/local/tmp/record.csv** file during recording. The value **true** means to save the component information, and **false** means to record only the coordinate information. The default value is **true**.

**Note**: This command is supported since API version 20.

 |
| \-l | \- | 

Used to save the current layout information after each operation. The file storage path is **/data/local/tmp/layout\_Recording start timestamp\_Operation ID.json**.

**Note**: This command is supported since API version 20.

 |
| \-c | <true/false> | 

Used to specify whether to print the recorded operation event information to the console. The value **true** means to print the information, and **false** means the opposite. The default value is **true**.

**Note**: This command is supported since API version 20.

 |

\# Record the current UI operations to /data/local/tmp/record.csv and press Ctrl+C to stop the recording.
hdc shell uitest uiRecord record
# Record only the coordinates of the operation and do not match the target component.
hdc shell uitest uiRecord record -W false
# Save the page layout in /data/local/tmp/layout\_Recording start timestamp\_Operation ID.json after each operation.
hdc shell uitest uiRecord record -l
# Do not print the recorded operation event information to the console.
hdc shell uitest uiRecord record -c false
# Read and print record data.
hdc shell uitest uiRecord read

The fields in the record data are as follows:

{
  "ABILITY": "com.ohos.launcher.MainAbility", // Ability name of the target application
  "BUNDLE": "com.ohos.launcher", // Bundle name of the target application
  "CENTER\_X": "", // Reserved field.
  "CENTER\_Y": "", // Reserved field.
  "EVENT\_TYPE": "pointer", // Operation type.
  "LENGTH": "0", // Total length.
  "OP\_TYPE": "click", // Event type. Currently, click, double-click, long-press, drag, pinch, swipe, and fling events are supported.
  "VELO": "0.000000", // Hands-off velocity.
  "direction.X": "0.000000",// Movement along the x-axis.
  "direction.Y": "0.000000", // Movement along the y-axis.
  "duration": 33885000.0, // Gesture duration.
  "fingerList": \[{
    "LENGTH": "0", // Total length.
    "MAX\_VEL": "40000", // Maximum velocity.
    "VELO": "0.000000", // Hands-off velocity.
    "W1\_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // Bounds of the start component.
    "W1\_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // Page level of the start component.
    "W1\_ID": "", // ID of the start component.
    "W1\_Text": "", // Text of the start component.
    "W1\_Type": "Image", // Type of the start component.
    "W2\_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // Bounds of the end component.
    "W2\_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // Page level of the end component.
    "W2\_ID": "", // ID of the end component.
    "W2\_Text": "", // Text of the end component.
    "W2\_Type": "Image", // Type of the end component.
    "X2\_POSI": "47", // X coordinate of the end point.
    "X\_POSI": "47", // X coordinate of the start point.
    "Y2\_POSI": "301", // Y coordinate of the end point.
    "Y\_POSI": "301", // Y coordinate of the start point.
    "direction.X": "0.000000", // Movement along the x-axis.
    "direction.Y": "0.000000" // Movement along the y-axis.
  }\],
  "fingerNumber": "1" // Number of fingers.
}

## Injecting UI Simulation Operations

| Parameter | Description |
| :-- | :-- |
| help | Used to display the help information about the uiInput command. |
| click | Used to simulate a click. For details, see **Examples of Running the uiInput-click/doubleClick/longClick Command**. |
| doubleClick | Used to simulate a double-click. For details, see **Examples of Running the uiInput click/doubleClick/longClick Command**. |
| longClick | Used to simulate a long-click. For details, see **Examples of Running the uiInput click/doubleClick/longClick Command**. |
| fling | Used to simulate a fling. That is, the page scrolls inertially after the operation is complete. For details, see **Examples of Running the uiInput fling Command**. |
| swipe | Used to simulate a swipe. For details, see **Examples of Running the uiInput swipe/drag Command**. |
| drag | Used to simulate a drag. For details, see **Examples of Running the uiInput swipe/drag Command**. |
| dircFling | Used to simulate a directional fling. For details, see **Examples of Running the uiInput dircFling Command**. |
| inputText | Used to simulate text input in a text box at specified coordinates. For details, see **Examples of Running the uiInput inputText Command**. |
| text | 
Used to simulate text input in a text box at the focused position without specified coordinates. For details, see **Examples of Running the uiInput text Command**.

**Note**: This command is supported since API version 18.

 |
| keyEvent | Used to simulate a physical key event (such as pressing a keyboard key, pressing the power key, returning to the previous page, and returning to the home screen) or a combination key operation. For details, see **Examples of Running the uiInput keyEvent Command**. |

-   Example of Running the **click**/**doubleClick**/**longClick** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| point\_x | Yes | X-coordinate point to click. |
| point\_y | Yes | Y-coordinate point to click. |

\# Execute the click event.
hdc shell uitest uiInput click 100 100

# Execute the double-click event.
hdc shell uitest uiInput doubleClick 100 100

# Execute a long-click event.
hdc shell uitest uiInput longClick 100 100

-   Example of Running the **uiInput fling** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| from\_x | Yes | X-coordinate of the start point. |
| from\_y | Yes | Y-coordinate of the start point. |
| to\_x | Yes | X-coordinate of the end point. |
| to\_y | Yes | Y-coordinate of the end point. |
| swipeVelocityPps\_ | No | 
Swipe speed, in px/s. The value ranges from 200 to 40000.

Default value: **600**. If the value is out of the range, the default value is used.

 |
| stepLength\_ | No | 

Step length, in pixels. The default value is the swipe distance divided by 50.

**Note**:

The swipe distance is calculated based on the specified start and end coordinates.

To achieve better simulation effect, you are advised to use the default value.

 |

\# Execute the fling operation with the default stepLength\_ value.
hdc shell uitest uiInput fling 10 10 200 200 500

-   Example of Running the **uiInput swipe**/**drag** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| from\_x | Yes | X-coordinate of the start point. |
| from\_y | Yes | Y-coordinate of the start point. |
| to\_x | Yes | X-coordinate of the end point. |
| to\_y | Yes | Y-coordinate of the end point. |
| swipeVelocityPps\_ | No | 
Swipe speed, in px/s. The value ranges from 200 to 40000.

Default value: **600**. If the value is out of the range, the default value is used.

 |

\# Execute the swipe operation.
hdc shell uitest uiInput swipe 10 10 200 200 500

# Execute the drag operation.
hdc shell uitest uiInput drag 10 10 100 100 500

-   Example of Running the **uiInput dircFling** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| direction | No | 
Swipe direction, which can be **0**, **1**, **2**, or **3**. The default value is **0**.

The value **0** indicates leftward, **1** indicates rightward, **2** indicates upward, and **3** indicates downward.

 |
| swipeVelocityPps\_ | No | 

Swipe speed, in px/s. The value ranges from 200 to 40000.

Default value: **600**. If the value is out of the range, the default value is used.

 |
| stepLength | No | 

Step length, in pixels.

Default value: When the swipe direction is **0** or **1**, the default value is the screen width divided by 200. When the swipe direction is **2** or **3**, the default value is the screen height divided by 200. To achieve better simulation effect, you are advised to use the default value.

 |

\# Execute the leftward fling operation.
hdc shell uitest uiInput dircFling 0 500
# Execute the rightward fling operation.
hdc shell uitest uiInput dircFling 1 600
# Execute the upward fling operation.
hdc shell uitest uiInput dircFling 2
# Execute the downward fling operation.
hdc shell uitest uiInput dircFling 3

-   Example of Running the **uiInput inputText** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| point\_x | Yes | X-coordinate of the text box. |
| point\_y | Yes | Y-coordinate of the text box. |
| text | Yes | Text in the text box. |

\# Execute the text input operation.
hdc shell uitest uiInput inputText 100 100 hello

-   Example of Running the **uiInput text** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| text | Yes | Text in the text box. |

\# Execute the text input operation at the focused position. If the current focused position does not support text input, the operation does not take effect.
hdc shell uitest uiInput text hello

-   Example of Running the **uiInput keyEvent** Command

| Parameter | Mandatory | Description |
| :-- | :-- | :-- |
| keyID1 | Yes | 
ID of a physical key, which can be **Back**, **Home**, **Power**, or [KeyCode key code value](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-keycode#keycode).

When the value is set to **Back**, **Home**, or **Power**, combination keys are not supported.

Currently, the Caps Lock key (**KeyCode** = **2074**) does not take effect. Use composition keys to input uppercase letters. For example, press **Shift+V** to input uppercase letter V.

 |
| keyID2 | No | ID of the physical key. For details about the value range, see [KeyCode key code value](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-keycode#keycode). This parameter is left empty by default. |
| keyID3 | No | ID of the physical key. For details about the value range, see [KeyCode key code value](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-keycode#keycode). This parameter is left empty by default. |

\# Back to home page.
hdc shell uitest uiInput keyEvent Home
# Back to the previous page.
hdc shell uitest uiInput keyEvent Back
# Use combination keys to paste.
hdc shell uitest uiInput keyEvent 2072 2038
# Input the lowercase letter v.
hdc shell uitest uiInput keyEvent 2038
# Input the uppercase letter V.
hdc shell uitest uiInput keyEvent 2047 2038

## Obtain the version information.

hdc shell uitest --version

## Starting the UItest Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/-PmjCamiSC2PAx8xDSLB1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA90ECBAE9D48F4A7C31DA7E8714CE24873E864B859F2955BF4F91AC952D7E8D)

The UITest capability can be called only by the test HAP started by ability via **aa test**, and the [APL Level](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-concepts-in-the-permission-mechanism) of the test HAP must be **normal**.

hdc shell uitest start-daemon

#### FAQs

## What should I do if the failure log contains "uitest-api does not allow calling concurrently"?

**Symptom**

The UI test fails. The HiLog file contains the error message "uitest-api does not allow calling concurrently".

**Possible Causes**

1.  The **await** syntax sugar is not added to the asynchronous API provided by UITest.
2.  The UI test case is executed in multiple processes. As a result, multiple UITest processes are started, which is not supported.

**Solution**

1.  Check the case implementation and add the **await** syntax sugar to the asynchronous API.
2.  Do not execute UI test cases in multiple processes.

## What should I do if the failure log contains "does not exist on current UI! Check if the UI has changed after you got the widget object"?

**Symptom**

The UI test case fails. The HiLog file contains the error message "does not exist on current UI! Check if the UI has changed after you got the widget object".

**Possible Causes**

After the target component is found, the device UI changes, resulting in component loss and simulation failure.

**Solution**

Run the UI test case again to ensure that the component exists on the UI during the simulation operation.

## What should I do if the failure log contains "Cannot connect to AAMS, RET\_ERR\_CONNECTION\_EXIST"?

**Symptom**

The UI test case fails. The HiLog contains the error message "Cannot connect to AAMS, RET\_ERR\_CONNECTION\_EXIST".

**Possible Causes**

Other test tools that depend on UITest are used during the case execution.

**Solution**

Disable the test tools that depend on UITest or restart the device.
