# Mock

In real-world development, some APIs or objects depend on external resources or complex logic, which can be tricky to set up in a test environment, making them difficult to test. In such cases, you can use mock capabilities to simulate these APIs or objects. Currently, both instrument and local tests support module mocking. For system module APIs or external dependency modules, use **import mock** to simulate them. For local modules, use the mock APIs provided by the hamock or hypium plugin package, or also use **import mock**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/5HCcs-fKSJKCUrR7-EYx2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B58643872A9A3D87825355EE21BE8034E7E2A25A4611E6AE1BC0E8F74AD37286)

This feature is available only for projects developed using API version 11 or later based on the stage model.

#### Mocking System Modules or External Dependency Modules

You can mock system module APIs or methods of dependency modules using **import mock**. In the **mock-config.json5** configuration file, define a mapping between the target module and the mock implementation file. At runtime, all imports of the target module will redirect to the mock implementation. The following uses the system API **bluetoothManager** as an example to describe the implementation.

1.  In the **src/mock** directory, create an ArkTS test file, for example, **bluetooth\_manager.mock.ets**, and define the mock implementation of the target module in this file.
    
    // src/mock/bluetooth\_manager.mock.ets
    enum BluetoothState {
      /\*\* Indicates the local Bluetooth is off \*/
      STATE\_OFF = 0,
      /\*\* Indicates the local Bluetooth is turning on \*/
      STATE\_TURNING\_ON = 1,
      /\*\* Indicates the local Bluetooth is on, and ready for use \*/
      STATE\_ON = 2,
      /\*\* Indicates the local Bluetooth is turning off \*/
      STATE\_TURNING\_OFF = 3,
      /\*\* Indicates the local Bluetooth is turning LE mode on \*/
      STATE\_BLE\_TURNING\_ON = 4,
      /\*\* Indicates the local Bluetooth is in LE only mode \*/
      STATE\_BLE\_ON = 5,
      /\*\* Indicates the local Bluetooth is turning off LE only mode \*/
      STATE\_BLE\_TURNING\_OFF = 6
    }
    interface BluetoothInfo {
      state: number
    }
    const MockBluetoothManager: Record<string, Object> = {
      'getBluetoothInfo': () => {
        return { state : BluetoothState.STATE\_BLE\_TURNING\_ON } as BluetoothInfo;
      },
    };
    export default MockBluetoothManager;
    
2.  In the **src/mock/mock-config.json5** file, define the mapping between the target module and mock implementation file.
    
    "@ohos.enterprise.bluetoothManager": {  // Name of the module to be replaced.
      "source": "src/mock/bluetooth\_manager.mock.ets"  // Path to the mock implementation code, relative to the root directory of the module.
    }
    
3.  Write the following code in the test file:
    
    // bluetoothManager.test.ets
    import { describe, it, expect } from '@ohos/hypium';
    import { bluetoothManager } from '@kit.MDMKit';
    
    export default function mock\_system\_api() {   
      describe('mock\_system\_api', () => {
        /\* Mock the system API. \*/
        it('mock\_system\_api', 0, () => {
          let bluetoothInfo = bluetoothManager.getBluetoothInfo({
            bundleName: "com.example.myapplication"
          })
          expect(bluetoothInfo.state).assertEqual(4)
        });
      });
    }
    
4.  If the test file is manually created, add the test case class **mock\_system\_api** to the **List.test.ets** file.
    
    import mock\_system\_api from './bluetoothManager.test';
    
    export default function testsuite() {
      mock\_system\_api();
    }
    
5.  Perform the test. The test case should be passed.

#### Mocking Local Modules

You can mock local modules using the mock APIs provided by the hamock or hypium plugin package or using **import mock**.

## Using the mock APIs in the hamock or hypium Plugin Package

The following example demonstrates how to use the mock APIs to mock a specific method in a local module. For details, see [Mock](https://gitcode.com/openharmony/testfwk_arkxtest/blob/master/README_en.md#mock).

1.  Create an ArkTS test file, for example, **ClassForMock.ets**, under **src/main/ets**, and export a class from the file.
    
    export class ClassForMock {
      constructor() {
      }
      method\_1(arg: string) {
        return '888888';
      }
      method\_2(arg: string) {
        return '999999';
      }
    }
    
2.  Write the following code in the test file:
    
    // afterReturnTest.test.ets
    import { describe, expect, it, MockKit, when } from '@ohos/hypium';
    import { ClassForMock } from '../../../main/ets/ClassForMock';
    
    export default function afterReturnTest() {
      describe('afterReturnTest', () => {
        it('afterReturnTest', 0, () => {
          console.info("it begin");
          // 1. Create a MockKit object.
          let mocker: MockKit = new MockKit();
          // 2. Define the ClassForMock class, which contains two functions, and then create a classForMock object.
          let classForMock: ClassForMock = new ClassForMock();
          // 3. Mock method\_1 of the ClassForMock class.
          let mockFunc: Function = mocker.mockFunc(classForMock, classForMock.method\_1);
          // 4. It is expected that, after the classForMock.method\_1 function is mocked, the result '1' is returned when the function is called with 'test' passed in.
          when(mockFunc)('test').afterReturn('1');
          // 5. Assert whether the mocked function is implemented as expected.
          // The operation is successful if 'test' is passed in.
          expect(classForMock.method\_1('test')).assertEqual('1'); // The operation is successful.
        })
      })
    }
    
3.  If the test file is manually created, add the test case class **afterReturnTest** to the **List.test.ets** file.
    
    import afterReturnTest from './afterReturnTest.test';
    
    export default function testsuite() {
      afterReturnTest();
    }
    
4.  Perform the test. The test case should be passed.

## Using import mock

You can mock local modules using **import mock**, following a process similar to mocking system or external dependency modules: In the **mock-config.json5** configuration file, define a mapping between the target module and the mock implementation file. At runtime, all imports of the target module will redirect to the mock implementation. The following example demonstrates how to mock the **sum** function from a local module located at **entry/src/main/ets/common/calc.ets**.

1.  In the **src/mock** directory, create a **common** directory and an ArkTS test file, for example, **calc.mock.ets**, and define the mock implementation of the target module in this file.
    
    // src/mock/common/calc.mock.ets
    export function sum() {
      return "this is mock sum";
    }
    
    Original implementation of **calc.ets**:
    
    // src/main/ets/common/calc.ets
    export function sum() {
      return 1;
    }
    
2.  In the **src/mock/mock-config.json5** file, define the mapping between the target module and mock implementation file.
    
    {
      "common/calc.ets": { // Specify the path of the file relative to the ets directory, including the file name extension.
        "source": "src/mock/common/calc.mock.ets"  // Path to the mock implementation code, relative to the root directory of the module.
      },
    }
    
3.  Write the following code in the test file:
    
    // test\_mock\_local\_method.test.ets
    import { describe, it, expect } from '@ohos/hypium'
    import { sum } from '../../../main/ets/common/calc';
    
    export default function test\_mock\_local\_method() {
      describe('test\_mock\_local\_method', () => {
        it("test\_mock\_local\_method", 0, () => {
          expect(sum()).assertEqual("this is mock sum")
        })
      })
    }
    
4.  If the test file is manually created, add the test case class **test\_mock\_local\_method** to the **List.test.ets** file.
    
    import test\_mock\_local\_method from './test\_mock\_local\_method.test';
    
    export default function testsuite() {
      test\_mock\_local\_method();
    }
    
5.  Perform the test. The test case should be passed.
