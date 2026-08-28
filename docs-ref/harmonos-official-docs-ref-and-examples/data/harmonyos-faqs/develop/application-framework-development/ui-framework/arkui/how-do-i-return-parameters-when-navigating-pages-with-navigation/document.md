# How do I return parameters when navigating pages with Navigation?

When navigating pages, use [pushPath()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#pushpath12) and add the onPop callback to receive the return result of the stacking page. When the page is returned, the [pop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-navigation#pop11) method is used to set the result parameter and pass the parameter to the target page. The onPop callback receives the returned parameter. The sample code snippet is as follows:

interface paramType {
  param: string
}

let paramA: paramType = {
  param: 'test1'
}

@Entry
@Component
struct Index {
  @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();

  @Builder
  myRouter(name: string) {
    if (name === 'MyFirstNavDestination') {
      MyFirstNavDestination()
    } else if (name === 'MySecondNavDestination') {
      MySecondNavDestination()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Row() {
        Column() {
          Text('hello world')
        }
        .height('100%')
      }
      .onClick(() => {
        this.pathInfos.pushPathByName('MyFirstNavDestination', paramA);
      })
    }
    .navDestination(this.myRouter)
  }
}

@Component
export struct MyFirstNavDestination {
  @Consume('pathInfos') pathInfos: NavPathStack;

  getParamsPrint() {
    console.info('param is ' + JSON.stringify(this.pathInfos.getParamByName('MyFirstNavDestination')));
  }

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('MyFirstNavDestination')
        }
        .width('100%')
      }
      .height('100%')
      .onClick(() => {
        this.pathInfos.pushPath({
          name: 'MySecondNavDestination', param: null, onPop: (popInfo: PopInfo) => {
            console.info(\`\[pushPath\]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}\`);
          }
        });
      })
    }.onShown(() => {
      this.getParamsPrint();
    })
  }
}

@Component
export struct MySecondNavDestination {
  @Consume('pathInfos') pathInfos: NavPathStack;
  private routerParams: paramType = { param: 'test 2' };

  build() {
    NavDestination() {
      Row() {
        Text('MySecondNavDestination')
      }
      .height('100%')
    }.onBackPressed(() => {
      this.pathInfos.pop(this.routerParams);
      return true;
    })
  }
}
