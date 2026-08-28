# How do I obtain elements in an ArrayList using indexes?

-   Method 1:
    
    In JS, you can directly use the element index to access the object in an array. Refer to the code snippet below.
    
    import { ArrayList } from '@kit.ArkTS';
    
    let arrayList: ArrayList<number> = new ArrayList();
    arrayList.add(0);
    arrayList.add(1);
    arrayList.add(2);
    arrayList.add(3);
    arrayList.add(4);
    arrayList.add(5);
    arrayList.add(6);
    arrayList.add(7);
    arrayList.add(8);
    arrayList.add(9);
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'get arrayList value';
    
      build() {
        Row() {
          Column() {
            Button(this.message)
              .onClick(() => {
                console.info('arrayList\[6\]:', arrayList\[6\]);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Method 2:
    
    Use [subArrayList](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arraylist#subarraylist), which can be used to intercept a range of elements in an ArrayList and return an ArrayList instance containing the elements of the selected range. Refer to the code snippet below.
    
    import { ArrayList } from '@kit.ArkTS';
    
    let arrayList: ArrayList<number> = new ArrayList();
    arrayList.add(0);
    arrayList.add(1);
    arrayList.add(2);
    arrayList.add(3);
    arrayList.add(4);
    arrayList.add(5);
    arrayList.add(6);
    arrayList.add(7);
    arrayList.add(8);
    arrayList.add(9);
    
    let result: ArrayList<number> = arrayList.subArrayList(2, 4);
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'subArrayList result';
    
      build() {
        Row() {
          Column() {
            Button(this.message)
              .onClick(() => {
                console.info('subArrayList result:', JSON.stringify(result)); // subArrayList result {"0":"2","1":"3"}
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
