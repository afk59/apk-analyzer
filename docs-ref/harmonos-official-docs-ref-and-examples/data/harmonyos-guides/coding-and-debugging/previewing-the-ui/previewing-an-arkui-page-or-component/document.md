# Previewing an ArkUI Page or Component

For ArkTS apps/atomic services with ArkUI, you can preview individual pages, components, and widgets. Simply click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/TeKAen7wSWmSqgUdDLs4MQ/en-us_image_0000002532670333.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C78E3C88B0C262D26BC80697E35FBBCF9046768AF2E38ECB721D287700770F1) to preview a page, or ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/J1ACQM7FQpuKGDGXD4Xouw/en-us_image_0000002532670329.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE63F6106CD0D97D8638AE9CEE91C950959E731811FAC2EB0B42E2566E56FAAD) to preview a component, as shown in the following figure. Widget preview is automatically enabled once the widget file is created.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/wSgWN6fRRPC-r_Ew5oTasg/en-us_image_0000002500910412.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11EF5A8CBE5981B12BE44B20EB86BB532DD98F2C5C36BCCF7AA4D6CA654DAD66)

#### Previewing a Page

ArkTS apps/atomic services support page preview. To use this feature, add the @Entry decorator at the top of the project's .ets file.

The following exemplifies how to use the @Entry decorator:

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### Previewing a Component

ArkTS apps/atomic services support component preview. Component preview supports real-time preview, but not dynamic pictures or dynamic preview. Before previewing a component, you must decorate it with the @Preview decorator. In a single source file, you can use up to 10 @Preview decorators to decorate custom components.

The following exemplifies how to decorate a component with the @Preview decorator:

@Preview({
  title: 'ContentTable'
})
@Component
struct ContentTablePreview {
  build() {
    Flex() {
      ContentTable({ foodItem: getDefaultFoodData() })
    }
  }
}

Below is a preview of the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Dr-4mzwGRYSXKWSAOshM0Q/en-us_image_0000002501070258.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD4B5C6650F6DE904CE3459B40373A1EFC1AC8F1995901B49A8EFC79010DC948 "Click to enlarge")

The preset device for preview is a phone in the following settings. To preview your app/atomic service on a different device, modify the fields under @Preview.

@Preview({
  title: 'Component1',  // Name of the component to preview.
  deviceType: 'phone',  // Type of the device for rendering and previewing the component. The default value is phone.
  width: 1080,  // Width of the preview device, in pixels.
  height: 2340, // Height of the preview device, in px.
  colorMode: 'light',  // Color mode of the preview device. The value can only be light.
  dpi: 480, // Screen DPI value of the preview device.
  locale: 'zh\_CN', // Language of the preview device, for example, zh\_CN or en\_US.
  orientation: 'portrait',  // Screen orientation of the preview device. The value can be portrait or landscape.
  roundScreen: false  // Whether the screen shape of the preview device is round.
})

If the component you want to preview depends on parameter injection, add the @Preview decorator as follows: Define a component fragment, declare in the fragment the component to be previewed and parameter dependency, and add the **@Preview** decorator to the component fragment. For example, to preview the component below:

@Component
struct Title {
  @Prop context: string; 
  build() {
    Text(this.context)
  }
}

Add @Preview as follows:

@Preview
@Component    // Define the component fragment TitlePreview.
struct TitlePreview {
  build() {
    Title({ context: 'MyTitle' })    // Declare the component to preview, Title in this case, and the parameter {context: 'MyTitle'} on which the component depends.
  }
}

#### Previewing a Widget

After creating a widget and selecting the widget file, click **Previewer** on the right to preview the effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/azjheAICQRa2IMzoKYPaNA/en-us_image_0000002532750279.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A13BC411F4C10615FA69D0F096D36DFD6887B59441CA4AC6414D46502E2BE190 "Click to enlarge")
