# How do I resolve the "There are properties not initialized" error during preview?

**Symptom**

During preview, a blank screen is displayed, and the error message "Preview failed. View details in the PreviewerLog window." is displayed in the upper part.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/aTx9fbEARCSeyxOsITqhUA/en-us_image_0000002194317976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97CA77C4892369BC38B48DB9B20FF0A9424F035FC4014E20FE5CB29FA72E591F "Click to enlarge")

The error message "There are properties not initialized." is displayed in the **PreviewerLog** window.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/vj_2l5bvTiOwoBmB-Fg7Ag/en-us_image_0000002194158356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AED9E48E3D75414A5454202B54FE767CA97B65963ABD25C8B5E6A34B7D29DC45)

**Solution**

If the preview page or component contains member variables that fail to be initialized, calling the properties or methods of these member variables will result in errors and a blank screen during preview. The following are possible causes:

Scenario 1: Global variables are set in AppStorage.

Scenario 2: **router.getParams()** is used to obtain route parameters.

Use custom mock.

1.  Add the following dependencies to the **oh-package.json5** file:
    
    "dependencies": {
      // The version number needs to be modified according to the relationship between hvigor and the SDK
      "@ohos/hamock": "1.0.0"
    }
    
2.  Import the mock dependency on the preview page.
    
    import { MockSetup } from '@ohos/hamock';
    
3.  Set the mock data.
    
    @MockSetup
    mock(){
      this.fruit = new Fruit("apple");
    }
    

For scenario 1 where global variables are set in AppStorage, modify the code as follows:

import { MockSetup } from '@ohos/hamock';

export default class Fruit{
  public name: string;

  getName(): string{
    return this.name;
  }

  constructor(name: string) {
    this.name = name;
  }

}

@Entry
@Component
struct GlobalData {
  @State fruit:Fruit = AppStorage.get("fruit") as Fruit;

  @MockSetup
  mock(){
    this.fruit = new Fruit("apple");
  }

  build() {
    Row() {
      Column() {
        Text(this.fruit.name)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

For scenario 2 where the route parameters are used, modify the code as follows:

import { MockSetup } from '@ohos/hamock';

@Entry
@Component
struct Page {
  @State params: object = this.getUIContext().getRouter().getParams();

  @MockSetup
  mock(){
    this.params = \[\];
    this.params\["path"\] = "path";
  }

  build() {
    Row() {
      Column() {
        Text(this.params\['path'\])
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
