# Configuring the Sidebar in Embed Mode

#### Use Case

The function of configuring the sidebar in embed mode is available since version 6.0.0(20) Beta1.

The [HdsSideBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdssidebar) component contains a sidebar and a content area as its child components. The sidebar is the first child component and can be shown or hidden as needed. The content area is the second child component. You can set **sideBarContainerType** to [SideBarContainerType.Embed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-sidebarcontainer#sidebarcontainertype) to display the **HdsSideBar** component in embed mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/U7kq2cV-RNOqgBZ7Mh3HUA/en-us_image_0000002500424094.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EC59AA362A084AE2571D2C133991B33E06E6C868AD9A0120B2C4CD8B93F7929 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { HdsSideBar } from '@kit.UIDesignKit';
    
2.  Configure the image.
    
    Place the image resource in **entry/src/main/resources/base/media**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/2upllPldRvO27va9n4iLCw/en-us_image_0000002532144161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8810CB98742F1A5225B20626476E13B164DCBE05EA355E53F3249D969BD1F95D "Click to enlarge")
    
3.  Create the **HdsSideBar** component and set its **sideBarContainerType** to **SideBarContainerType.Embed**.
    
    @Entry
    @ComponentV2
    struct Index {
      @Local isSideBarContainerMask: boolean = true;
      @Local blankHeight: number = 48;
      @Local isAutoHide: boolean = false;
      @Local isShowSidebar: boolean = true;
      @Local triggerValueReplace: number = 0;
      // Sidebar area on the left.
      @Builder
      SideBarPanelBuilder() {
        Column() {
          Blank().height(this.blankHeight)
          Text('HdsSideBar Menu 1')
            .fontSize(14)
          Text('HdsSideBar Menu 2')
            .fontSize(14)
        }
        .width('100%')
        .height('100%')
      }
      // Content area on the right.
      @Builder
      ContentPanelBuilder() {
        Column(){
          Blank().height(this.blankHeight)
          Image($r('app.media.view')) // **view** is a custom resource. You need to replace it with your local resource.
            .width('80%')
            .height('50%')
            .margin({ top: 8 })
            .padding({
              right: '16vp',
              left: '16vp',
              bottom: '16vp',
            })
            .borderRadius(8)
          Column() {
            Text('HdsSideBar content text1')
              .fontSize(14)
            Text('HdsSideBar content text2')
              .fontSize(14)
          }
          Button() {
            SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open\_sidebar') : $r('sys.symbol.close\_sidebar'))
              .fontWeight(FontWeight.Normal)
              .fontSize($r('sys.float.ohos\_id\_text\_size\_headline7'))
              .fontColor(\[$r('sys.color.ohos\_id\_color\_titlebar\_icon')\])
              .hitTestBehavior(HitTestMode.None)
          }
          .id('side\_bar\_button')
          .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
          .height(24)
          .width(24)
          .animation({ curve: Curve.Sharp, duration: 100 })
          .onClick(() => {
            this.isShowSidebar = !this.isShowSidebar;
          })
        }
      }
      @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
      @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
      @Builder
      HDSSideBarBuilder() {
        HdsSideBar({
          sideBarPanelBuilder: (): void => {
            this.sideBarBuilder()
          },
          contentPanelBuilder: (): void => {
            this.contentBuilder()
          },
          autoHide: this.isAutoHide,
          contentAreaMask: this.isSideBarContainerMask,
          sideBarContainerType: SideBarContainerType.Embed,
          isShowSideBar: this.isShowSidebar,
          $isShowSideBar: (isShowSidebar: boolean) => {
            this.isShowSidebar = !isShowSidebar
          },
        })
      }
      @Builder
      build() {
        Stack() {
          this.HDSSideBarBuilder()
        }
      }
    }
