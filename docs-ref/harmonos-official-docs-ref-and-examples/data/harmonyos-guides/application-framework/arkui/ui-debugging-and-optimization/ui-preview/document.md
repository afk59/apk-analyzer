# UI Preview

DevEco Studio provides the UI preview function, which allows you to view the UI effect and adjust the page layout at any time. You can preview both pages and components. The icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/jv0xLrV0QyK6sLu_v5s4qA/en-us_image_0000002537924914.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E44F7EF6A1BF232DFE46D907B2B32A357FF2A33DE597DEBC970C3A148B8411CD) on the left in Figure 1 indicates page preview, while the icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/fBrgXULsQ0mYuyrQUR5lPA/en-us_image_0000002568684691.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61935863D2B6B19A0E9EDC0DE6A35EE27C50B9EBF21D2AF4A422E055F4121258) on the right indicates component preview.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/wgHNtNhjRSKg1IdH0J3oEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D32FCF90FA525871848A9FB85A98CA97F09D6DCFAF8DE8EDE8DC9DC1B107F2F2)

Due to differences between the operating system and real devices, the preview effect may vary from the actual device performance. The preview is for reference only. Verify the actual performance on real devices.

**Figure 1** Preview icons

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/KBAUHqDeSwOgSlM1iysBtw/en-us_image_0000002568764701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61F6652BC40636C4F97A048CA6979442B027065B44997734FF4CEA443A0AFAA0)

#### Page Preview

Both ArkTS applications and atomic services support page preview. Page preview is achieved by adding the [@Entry](../../ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/custom-components/creating-a-custom-component/document.md#entry) decorator to the custom component in the project's .ets file, allowing you to view the current UI page effect.

-   To start page preview, select the target .ets page and click the Previewer button in the right sidebar.
    
-   Hot reload: After starting page preview, you can add, delete, or modify UI components. Press **Ctrl+S** to save changes, and the Previewer will refresh without requiring a restart.
    
-   Routing: You can switch between pages to preview different page effects.
    

In addition to basic page preview, the following enhanced features are available:

## Instant Preview

When modifying component attributes, you can view changes immediately without pressing **Ctrl+S**. Instant preview is enabled by default. To disable it, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/QTo2AbdIRCiQfrHDDXRL8Q/en-us_image_0000002537764976.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B716E9849139004168D24D3DBA24597749D29419AB71C7D7097EB1E5B51770A) in the Previewer's upper right corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/lJU119nbQY-RAJ8Dejh3Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=070674CC82D5C0E1191A7508CA33AF476B21B1750390AF4C494954AECEAB677D)

Instant preview is not supported in the following scenarios:

-   Components that are not displayed
-   Adding or deleting components
-   Components containing private variables or untyped controllers
-   Components using the decorators such as [@Builder](../../ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/component-extension/builder-decorator-custom-builder-function/document.md), [@Style](../../ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/component-extension/styles-decorator-defining-reusable-component-styles/document.md), and [@Extend](../../ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/component-extension/extend-decorator-defining-extended-component-styles/document.md).
-   Components importing external components or modules via **import**
-   Modifying state variables

Figure 2 shows the demonstration.

**Figure 2** Instant preview demonstration

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/aoQJVuB-TmClR85Fr7QoKA/en-us_image_0000002537924916.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAFA6277DE2C78420E52B0CBA43B66108DEB84EACBD6AADB9A7F7019000257EC)

## Inspector Bidirectional Preview

Bidirectional synchronization between the .ets file and Previewer is supported. Click the Previewer icon ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/8ZLkneCjTR-q4xMVmhZRtA/en-us_image_0000002568684693.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D45A05E54FA2F1435F1A57BD58FE2B19DD510C98B6992FA526F3BF9BDE13606) to enable this feature.

When this feature is enabled, the code editor, UI preview, and component tree become interconnected:

1.  Selecting a component in the Previewer highlights the corresponding component in the component tree and the relevant code block in the editor.
    
2.  Selecting a code block in the editor highlights the corresponding component in both the Previewer and component tree.
    
3.  Selecting a component in the component tree highlights the corresponding code block and Previewer component.
    
4.  Modifications made in the Previewer's attribute panel are automatically synchronized to the code editor and reflected in real time. Similarly, code changes are immediately visible in the Previewer.
    

Figure 3 shows the demonstration.

**Figure 3** Inspector bidirectional preview demonstration

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/DjoW-QZvT0yDYkSqumlCMw/en-us_image_0000002568764703.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D944F06C4406D8D1B7B925C8325E78C397DE4BFE44C6B01035EFDE2E273B5011)

#### Component Preview

Both ArkTS applications and atomic services support component preview. Add the [@Preview](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-component-previewer#preview-decorator) decorator before a custom component to enable preview. A single source file can contain up to 10 @Preview decorators. Startup modes:

-   For components decorated with both @Entry and @Preview, clicking the Previewer button starts page preview. After loading, click [ide\_previewer\_003](en-us_image_0000002568684691.png) to switch to component preview.
-   For components decorated with only @Preview, clicking the Previewer button directly starts component preview.

During component preview, the default attributes of the @Preview decorator are used. For details, see [PreviewParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-component-previewer#previewparams9). You can configure @Preview parameters to specify device attributes, including device type and screen shape.

Example of using the @Preview decorator:

@Entry
@Preview
@Component
struct ComponentPreviewOne {
  build() {
    Column() {
      Text('this is component previewer One')
        .height(80)
        .fontSize(30)
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}

@Preview
@Component
struct ComponentPreviewTwo {
  build() {
    Column() {
      Text('this is component previewer Two')
        .height(80)
        .fontSize(30)
        .fontColor(Color.Pink)
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}

Figure 4 shows the demonstration.

**Figure 4** Component preview effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Ff4F9PWRTAqzQGvwTZtXfw/en-us_image_0000002537764978.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE3A447DF9E37B9378237BAD512AB75E2C5FFA4D00947574239572DBE3FB78AC)

#### Dynamic Resolution Adjustment

Applications and atomic services can run on various devices with different screen resolutions, shapes, and sizes. The Previewer supports dynamic resolution changes, allowing you to check UI layouts and interactions across different devices. \\To use this feature: After starting page preview, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/YzwV9h5ESvCURHZZkONKKw/en-us_image_0000002537924918.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=295A39EF99EF185213F66D7BDBB92A76998895BFF26D1E21E488FFBAD8B64665) in the upper right corner and drag the selection box to adjust the screen size dynamically.

Figure 5 shows the demonstration.

**Figure 5** Dynamic resolution adjustment effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/YoaRBRuiQLW-555PGt34MA/en-us_image_0000002568684695.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061944Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14D585FE2B80F4AC0BF7FAB6224BC337BE7E05687BF847A18B88620E67D8D4C1)
