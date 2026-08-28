# Configuring the Sidebar in Overlay Mode

#### Use Case

The function of configuring the sidebar in overlay mode is available since version 6.0.0(20) Beta1.

The [HdsSideBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdssidebar) component contains a sidebar and a content area as its child components. The sidebar is the first child component and can be shown or hidden as needed. The content area is the second child component. You can set **sideBarContainerType** to [SideBarContainerType.Overlay](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-container-sidebarcontainer#sidebarcontainertype) to make the current **HdsSideBar** component hover.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ylaCY5hlTeOAAml2Qio2uw/en-us_image_0000002500304238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C6D82C1E8A6E2ED66AB98E756907221F4E05EA239EED0CC54ABC597AFCF6AAA "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { HdsSideBar } from '@kit.UIDesignKit';
    
2.  Configure the image.
    
    Place the image resource in **entry/src/main/resources/base/media**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/dJV34EHsQ9S6LTnxWzTcjA/en-us_image_0000002500424086.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A39C6FB0598A09977001B184FE079CD2C1956BE16D86BB4214BA4E6953243BB "Click to enlarge")
    
3.  Create the **HdsSideBar** component and set its **sideBarContainerType** to **SideBarContainerType.Overlay**.
    
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
          sideBarContainerType: SideBarContainerType.Overlay,
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
