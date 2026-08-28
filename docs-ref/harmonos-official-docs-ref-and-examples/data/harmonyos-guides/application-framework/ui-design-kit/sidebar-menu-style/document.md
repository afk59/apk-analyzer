# Sidebar Menu Style

#### Use Case

The function of configuring the sidebar menu style is available since version 6.0.0(20) Beta1.

The [HdsSideMenu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdssidemenu) component allows menu bar style configuration, for you to set a two-level menu for the sidebar and display the number of new messages for each menu item.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/KIhQnpwiQvS3p1pLAzCicw/en-us_image_0000002532304135.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8A3C29EF5BF3B89D53820E2CA9FB4AE84D9E7C3C8F968A1D940763D8BAE0669 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { HdsSideMenu, HdsSideMenuMainItem, HdsSideMenuSubItem, HdsSideMenuBadgeParam, HdsSideBar } from '@kit.UIDesignKit';
    import { SymbolGlyphModifier } from '@kit.ArkUI';
    
2.  Set the level-1 and level-2 menu items for the sidebar and display the number of new messages for each item.
    
    @Entry
    @ComponentV2
    struct Index {
      @Local showControlButton: boolean = true;
      @Local sideBarMask: boolean = false;
      @Local autoHide: boolean = true;
      @Local barStateTypeText: string = "Select BarState";
      @Local widthIndex: number = 0;
      @Local badgeNumber: HdsSideMenuBadgeParam = { count: 50 };
      @Local useTheme: boolean = false;
      @Local selectedIndex: number = 2;
      @Local selectedTransparency: number = 0.6;
      @Local str: string = "Text message";
      @Local isShowSidebar: boolean = true;
      listOptionsDefault?: HdsSideMenuMainItem\[\] = \[
        new HdsSideMenuMainItem(
          {
            symbol: new SymbolGlyphModifier($r('sys.symbol.ohos\_folder\_badge\_plus')).fontSize(14),
            label: $r('sys.string.TextView\_engr\_phone'),
          }),
        new HdsSideMenuMainItem({
          icon: $r('sys.symbol.person\_wave\_3'),
          label: 'Tuesday',
          hdsSideMenuSubItem: \[
            new HdsSideMenuSubItem({ label: this.str, badge: this.badgeNumber })\],
        }),
        new HdsSideMenuMainItem({
          symbol: new SymbolGlyphModifier($r('sys.symbol.person\_crop\_circle\_fill\_1')),
          label: 'Wednesday',
        }),
      \]
      @Builder
      SideBarPanelBuilder() {
        Column() {
          HdsSideMenu({
            items: this.listOptionsDefault,
            selectedIndex: this.selectedIndex,
            $selectedIndex: (selectedIndex: number) => {
              this.selectedIndex = selectedIndex;
            },
          })
        }
        .height('100%')
      }
      // Content area on the right.
      @Builder
      ContentPanelBuilder() {
        Column() {
          Column() {
            Button() {
              SymbolGlyph(this.isShowSidebar ? $r('sys.symbol.open\_sidebar') : $r('sys.symbol.close\_sidebar'))
                .fontWeight(FontWeight.Normal)
                .fontSize($r('sys.float.ohos\_id\_text\_size\_headline7'))
                .fontColor(\[$r('sys.color.ohos\_id\_color\_titlebar\_icon')\])
                .hitTestBehavior(HitTestMode.None)
            }
            .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
            .height(24)
            .width(24)
            .animation({ curve: Curve.Sharp, duration: 100 })
            .onClick(() => {
              this.isShowSidebar = !this.isShowSidebar;
            })
          }
        }
        .height('100%')
        .width('100%')
      }
      @BuilderParam sideBarBuilder: () => void = this.SideBarPanelBuilder
      @BuilderParam contentBuilder: () => void = this.ContentPanelBuilder
      @Builder
      build() {
        Column() {
          HdsSideBar({
            sideBarPanelBuilder: (): void => {
              this.sideBarBuilder()
            },
            contentPanelBuilder: (): void => {
              this.contentBuilder()
            },
            isShowSideBar: this.isShowSidebar,
            $isShowSideBar: (isShowSidebar: boolean) => {
              this.isShowSidebar = !isShowSidebar
            },
          })
        }
      }
    }
