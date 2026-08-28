# Mocking Preview Data

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/q7kvoVRuSZacRE6haMwKCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B9D82AEFC41FB69BD1CAA38F9C821F8A5779F6EEB1840937FFE3DB8925348E7)

This feature is available only for projects developed using API version 11 or later based on the stage model.

When previewing a UI, you may not be able to view UI changes resulting from changes of return values. This is because the code runtime environment differs from that of the real device, and valid return values cannot be obtained for certain API calls. For example, when **batteryInfo.voltage** is called to obtain the battery power level during the preview, a fixed value **0**, rather than the actual value, is returned. This is where Hamock comes into the picture. Without changing the service logic, you can mock the attributes or methods of UI components or the imported module APIs.

#### Prerequisites

A dependency on hamock is added to the project- or module-level **oh-package.json5** file, and the project sync is complete.

"devDependencies": {
    "@ohos/hamock": "1.0.0"
}

#### Mocking on UI Components

For any component developed with the declarative paradigm, you can use @MockSetup to decorate a method. When you preview the component, the decorated method is executed during component initialization. Within this method, you can redefine a component method or reassign a value to a component attribute, both taking effect during the preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/EvY8elrVTCal3-mgt5ev0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD99C8C593E1DA9DD7F4529F557BBF9D7605578E6CA519B83EA9D78511B8C8BC)

The method decorated by @MockSetup is automatically triggered only in the preview scenario and is executed before the **aboutToAppear** lifecycle callback of the component.

## UI Component Methods

1.  Import **Hamock** to the ArkTS page code.
    
    import { MockKit, when, MockSetup } from '@ohos/hamock';
    
2.  Define a method in the target component and decorate it with @MockSetup. In this method, **MockKit** is used to mock the target method.
    
    import { MockKit, when, MockSetup } from '@ohos/hamock';
    
    @Entry
    @Component
    struct Index {
     ...
     @MockSetup
     randomName() {
      let mocker: MockKit = new MockKit();
      let mockfunc: Object = mocker.mockFunc(this, this.method1);
      // Mock the return value of the specified method in the specified input parameter.
      when(mockfunc)('test').afterReturn(1);
     }
     ...
    // Invoke the method in the service scenario.
     const result = this.method1('test'); // in previewer, result = 1
    }
    

## UI Component Attributes

1.  Import **Hamock** to the ArkTS page code.
    
    import { MockSetup } from '@ohos/hamock';
    
2.  Define a method in the target component and decorate it with @MockSetup. In this method, you can reassign a value to the attribute you want to mock.
    
    import { MockSetup } from '@ohos/hamock';
    
    @Component
    struct Person {
     @Prop species: string;
     // Define the target attribute in the @MockSetup fragment.
     @MockSetup
     randomName() {
      this.species = 'primates'
     }
     ...
    // Invoke the attribute. (This attribute does not change during the period from initialization to invoking.)
     const result = this.species // in previewer, result = primates
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/PwRmxl-cSi20Hdlpigp2fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3417FFAD696E46D1F2CC1BF85F6303793DFD98B061F70CEB6F7A3D79FE6DF97D)

-   Some ArkUI type attributes, such as **readonly** and @ObjectLink, do not support mocking.
-   For variables decorated by @Link, @Consume, @Prop, or @BuilderParam, the ArkUI syntax requires that their parent container should have the corresponding attribute definition. Therefore, it is recommended that you define a parent container (and pass in appropriate data through the container) for previewing components that contain such variables.

#### Mocking Modules

You can mock system modules, dependent modules, and local modules to facilitate testing and previewing. Just create an ArkTS file that contains the mock implementation code, and define the mapping between the real module and its mock in the **mock-config.json5** configuration file. The target module and mock implementation code file are in one-to-one mapping. That is, only one mock implementation code file can be used for a target module. During preview, all pages that import the target module will point to the mock implementation code file.

## System Module/Dependent Module

1.  Create an ArkTS file under **src/mock** and define the mock implementation of the target module in the file.
    
    // src/mock/MeasureText.mock.ets
    import MeasureText from '@ohos.measure'
    
    // Mock the class via inheritance (using extends).
    class MockMeasureText extends MeasureText {
      // Define the mock implementation.
      static measureText(): number {
        console.log('Return value of the mock measureText function')
        return 100;
      }
    };
    
    export default MockMeasureText;
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/rQRg0TKBQlOrM33XEfByrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C50A11511C328CB5D6E076E048A16D7FBA6A9AABE1D1AB27843161AA499E5973)
    
    It is recommended that mocking a class be implemented via inheritance (using **extends**). If inheritance is not used, provide mock implementations for all methods using the dependency module in the code.
    
2.  Define the mapping between the target module and mock implementation in the **src/mock/mock-config.json5** file. The mapping takes effect in previews.
    
    {
      "@ohos.measure": { // Name of the module to be replaced.
        "source": "src/mock/MeasureText.mock.ets" // Path of the mock implementation code, relative to the root directory of the module.
      },
     ...
    }
    
3.  Add **Hilog** to the location where the original method is called, so that the return value can be printed in **Log** during previews to verify whether the mocking takes effect.
    
    hilog.debug(DomainNumber, logTag, 'Mock %{public}s', \`${MeasureText.measureText({textContent: 'Hello World'})}\`)
    

## Local Module

1.  Create an ArkTS file under **src/mock** and define the mock implementation of the target module in the file.
    
    // src/mock/module/utils/CommonUtils.mock.ets
    // Import the local module.
    import LibDefaultExport from '../../../main/ets/utils/CommonUtils'; // get origin default export
    import { methodA, ObjectB } from '../../../main/ets/utils/CommonUtils'; // get origin export on demand
    
    class DefaultExportMock extends LibDefaultExport {
      // Define the mock implementation.
      public static getName(): String {
        return "Mocked Name";
      }
    };
    
    // Mock methodA.
    export const methodAMock = (): string => {
      return "methodA Mocked"
    }
    export {
      methodAMock as methodA,
      ObjectB,
    }
    
    export default DefaultExportMock;
    
    The following is an example of the **CommonUtils.ets** file:
    
    export default class CommonUtils {
      public static getName(): String {
        return "origin name";
      }
    
      public static getTitle(): String {
        return "origin title";
      }
    }
    
    export const methodA = (): string => {
      return "methodA"
    }
    
    export const ObjectB: Object = new Object();
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kXXXYGBnQS-oLU0HvbCgNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0D2698AFF10569D89D6BD33B353542C3D0DC026A9E10F43D67B46A6106BC04C)
    
    Mocking local modules is only available for the ArkTS and TS file in the **src/main/ets** directory.
    
2.  Define the mapping between the target module and mock implementation in the **src/mock/mock-config.json5** file. The mapping takes effect in previews.
    
    {
     "utils/CommonUtils.ets": { // Specify the path of the file relative to the ets directory, including the file name extension.
      "source": "src/mock/module/utils/CommonUtils.mock.ets"
     },
     ...
    }
    
3.  Add **Hilog** to the location where the original method is called, so that the return value can be printed in **Log** during previews to verify whether the mocking takes effect.
    
    hilog.debug(DomainNumber, logTag, 'Mock %{public}s', CommonUtils.getName());
