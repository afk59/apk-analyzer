# Can a custom component be saved through a container?

No. Custom components are structs, not classes. This means they cannot be stored in containers. You can encapsulate the custom component in a **Builder** function and complete the storage through the **Builder**'s encapsulation.

The code snippet is as follows:

@Component
struct ComA {
  build() {
    Text('ComA').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

@Component
struct ComB {
  build() {
    Text('ComB').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

@Component
struct ComC {
  build() {
    Text('ComC').fontSize(50).fontWeight(FontWeight.Bold)
  }
}

//if else logical branch writing
@Builder
function buildCom(param: string) {
  if (param == 'ComA') {
    ComA()
  } else if (param == 'ComB') {
    ComB()
  } else if (param == 'ComC') {
    ComC()
  }
}

@Builder
function buildComA() {
  ComA()
}

@Builder
function buildComB() {
  ComB()
}

@Builder
function buildComC() {
  ComC()
}

//Encapsulate in container through map
let map: Map<string, WrappedBuilder<\[\]>> = new Map();
map.set('ComA', wrapBuilder(buildComA));
map.set('ComB', wrapBuilder(buildComB));
map.set('ComC', wrapBuilder(buildComC));

@Component
struct Page12 {
  @State message: string = 'Hello World';
  @State arr: string\[\] = \['ComA', 'ComB', 'ComC'\];

  build() {
    Column() {
      ForEach(this.arr, (item: string) => {
        //Retrieve based on the key during use
        map.get(item)?.builder()
      })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

**Reference**

[@BuilderParam Decorator: Referencing the @Builder Function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builderparam)
