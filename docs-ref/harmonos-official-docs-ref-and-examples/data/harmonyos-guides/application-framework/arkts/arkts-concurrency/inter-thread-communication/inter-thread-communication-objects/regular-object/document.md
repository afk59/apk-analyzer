# Regular Object

Regular objects are passed by copy (serialization) between threads. The objects in the two threads have the same content but point to isolated memory areas in their respective threads, allocated in the local heap of each thread's virtual machine. The following object types are supported: basic types except Symbol, Date, String, RegExp, Array, Map, Set, Object (simple objects only, for example, objects created using **{}** or **new Object**), ArrayBuffer, and TypedArray. (Note that only properties can be transferred for regular objects. Prototypes and methods cannot be transferred.) The following figure shows the communication process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/-V3VxH7fRGSjOZkQ-P6nkw/en-us_image_0000002568684095.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061923Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=727801EA6202742F4B9E59F7E9736E1745F2BEC2BA4C5E2012902E6CDC1C9091)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/OS1R64_wSvaHnQILJRJ3cQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061923Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BBC1B3E4573A8CD3027CBC52A80B1581D182C9C30E22468E4B46FC2C53AC843)

Regular class instances are passed by copy across threads, which means only data is passed, and any class methods are lost. To enable class instances to retain their methods when being passed across threads, you can use the [@Sendable decorator](../sendable-object/overview-of-sendable-objects/document.md#sendable-decorator) to mark the class as Sendable.

#### Usage Example

The following is an example of passing a regular object.

// Test.ets
// Custom class TestA.
export class TestA {
  constructor(name: string) {
    this.name = name;
  }
  name: string = 'ClassA';
}

// Index.ets
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { TestA } from './Test';

@Concurrent
async function test1(arg: TestA) {
  console.info("TestA name is: " + arg.name);
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          // 1. Create a test instance objA.
          let objA = new TestA("TestA");
          // 2. Create a task and transfer objA to the task. objA is not a Sendable object and is transferred to the child thread through serialization.
          let task = new taskpool.Task(test1, objA);
          // 3. Execute the task.
          taskpool.execute(task).then(() => {
            console.info("taskpool: execute task success!");
          }).catch((e:BusinessError) => {
            console.error(\`taskpool: execute task: Code: ${e.code}, message: ${e.message}\`);
          })
        })
    }
    .height('100%')
    .width('100%')
  }
}
