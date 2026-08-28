# How do I use AOP to count the method execution time?

To measure execution time, use the **addBefore** API for recording the start time and the **addAfter** API for recording the end time after the method execution.

Refer to the code snippet below.

import { util } from '@kit.ArkTS';
import { systemDateTime } from '@kit.BasicServicesKit';

class Utils {
  Add(len: number): number {
    let num = 0;
    for (let index = 1; index <= len; index++) {
      num += index;
    }
    return num;
  }
}

let startTime = 0; // Initialization start time
let endTime = 0; // Initialization end time

util.Aspect.addBefore(Utils, 'Add', false, () => {
  startTime = systemDateTime.getTime(true); // Return the start time in nanoseconds
})

util.Aspect.addAfter(Utils, 'Add', false, () => {
  endTime = systemDateTime.getTime(true); // Return the end time in nanoseconds
})

let utilsObj = new Utils();
utilsObj.Add(1000);

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get execution time')
          .onClick(() => {
            console.log('startTime:', startTime);
            console.log('endTime:', endTime);
            console.log('endTime - startTime = ', endTime - startTime);
          })
      }
      .width('100%')
    }.height('100%')
  }
}
