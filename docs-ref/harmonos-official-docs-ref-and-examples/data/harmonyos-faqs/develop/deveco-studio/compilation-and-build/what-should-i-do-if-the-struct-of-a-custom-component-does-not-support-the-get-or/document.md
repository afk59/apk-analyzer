# What should I do if the struct of a custom component does not support the get or set method for defining member variables?

**Symptom**

After the build function of DevEco Studio is used, the **get** and **set** code logic is not generated in the build result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/bNOt-tnoS4G4qIC48LBtcA/en-us_image_0000002229758625.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062617Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=677C5D6A40AD83001CC72DF87101C79CB909AD8BBF7BE3E81ACFF5D84FDD3298)

The following is an example of incorrect code:

@Entry
@Component
struct GetSetDemo {
  private get value(): string {
    return "Hello";
  }
  private set value(value: string) {
    this.value = value;
  }

  build() {
    Row() {
      Column() {
        Text("Hello World")
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
    }
  }
}

**Solution**

1\. Use the following method to replace the **get** method:

private value: string = "Hello";

2\. Use the following method to replace the **set** method:

this.value = "World";
