# Development Example

1.  Create a level-1 navigation component on the home page. Call the **titleBar** API to configure the title bar style and content of the **HdsNavigation** component. Then implement navigation to level-2 pages through pushPath routing.
    
    // Import required modules.
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, ScrollEffectType, HdsNavigationTitleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
    import { LengthMetrics } from '@kit.ArkUI';
    
    const  TITLE\_BAR\_HEIGHT\_MINI: number = 64;
    
    @Entry
    @Component
    struct Index {
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
      @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
      scroller: Scroller = new Scroller();
      @State blankHeight: number = TITLE\_BAR\_HEIGHT\_MINI;
      @State isHideBackButton: boolean = false;
      @State titleMode: HdsNavigationTitleMode = HdsNavigationTitleMode.MINI;
      @State subTitle: string = 'Sub';
    
      build() {
        HdsNavigation(this.pageInfos) { // Create the **HdsNavigation** component.
          Column() {
            Stack() {
              Scroll(this.scroller) { // Set a scrollable container component in the content area to implement a dynamic title bar blur effect that synchronizes with content scrolling.
                Column() {
                  // By default, the title bar and content area of the **HdsNavigation** component are arranged in a stacked layout. You can leave a blank area of the same height as the title bar in the content area, to prevent the content area from being obscured by the title bar.
                  Blank().height(this.blankHeight)
                  Image($r('app.media.background1')) // **background1** is a custom resource. You need to replace it with your local resource.
                    .width('100%')
                  Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
                    .width('80%')
                    .height(40)
                    .margin({ top: '5%', right: '50vp', left: '50vp'})
                    .onClick(() => {
                      console.info('HDS\_BASE\_COMPONENT', \`onClick firstPage\`);
                      this.pageInfos.pushPath({ name: 'pageOne' })
                    })
                  Button('hide backButton ' + this.isHideBackButton)
                    .onClick(() => {
                      this.isHideBackButton = !this.isHideBackButton
                    })
                    .width('80%')
                    .height(40)
                    .margin({ top: '5%', right: '50vp', left: '50vp' , bottom: '5%'})
                  List({ space: 12, initialIndex: 0 }) {
                    ForEach(this.arr, (item: number) => {
                      ListItem() {
                        Text('' + item)
                          .width('100%')
                          .height(72)
                          .fontSize(16)
                          .fontWeight(500)
                          .textAlign(TextAlign.Center)
                      }
                      .height(120)
                      .backgroundColor(Color.Orange)
                      .borderRadius(24)
                    }, (item: number) => item.toString())
                  }
                  .edgeEffect(EdgeEffect.None)
                  .width('100%')
                  .height('100%')
                  .nestedScroll({scrollForward:NestedScrollMode.PARENT\_FIRST, scrollBackward: NestedScrollMode.PARENT\_FIRST})
                }
              }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
            }
          }
        }
        .titleBar( { // Set the title bar of the **HdsNavigation** component.
          style: { // Set the style for the title bar of the **HdsNavigation** component.
            // Set the dynamic blur style for the title bar, including whether to enable dynamic blur during content scrolling, dynamic blur type, and the minimum scrolling distance for the dynamic blur to take effect.
            scrollEffectOpts: {
              enableScrollEffect: true,
              scrollEffectType: ScrollEffectType.COMMON\_BLUR,
              blurEffectiveStartOffset: LengthMetrics.vp(0),
              blurEffectiveEndOffset: LengthMetrics.vp(20)
            },
          },
          content: { // Set the title bar content for the **HdsNavigation** component.
            title: { // Set the title of the title bar for the **HdsNavigation** component.
              mainTitle: 'Main',
              subTitle: this.subTitle
            },
            menu: { // Set the menu items for the title bar of the **HdsNavigation** component.
              value: \[{ // Set the first menu item.
                content: {
                  label: 'menu1',
                  icon: $r('sys.symbol.ohos\_wifi'),
                  isEnabled: true,
                },
                badge: {
                  count: 1,
                }
              }, { // Set the second menu item.
                content: {
                  label: 'menu2',
                  icon: $r('sys.symbol.ohos\_lock'),
                  isEnabled: true,
                  action: () => {
                    console.info("HDS\_NAV HELLO 2");
                  }
                }
              }, { // Set the third menu item.
                content: {
                  label: 'menu3',
                  icon: $r('sys.symbol.speaker\_plus'),
                }
              }, {
                content: { // Set the third menu item.
                  label: 'menu4',
                  icon: $r('sys.symbol.ohos\_star'),
                }
              }\]
            },
            backIcon: { // Set the back button of the **HdsNavigation** component.
              label: 'backButton',
              icon: $r('sys.symbol.ohos\_mic'),
              isEnabled: true,
            }
          }
        })
        .titleMode(this.titleMode)
        .hideBackButton(this.isHideBackButton)
      }
    }
    
2.  Create a level-2 navigation component on the **PageOne** page. Call the **titleBar** API to adapt the title bar of the **HdsNavDestination** component to the HarmonyOS style and configure the title bar content. The following uses NavPathStack routing as an example.
    
    // PageOne.ets
    // Import required modules.
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavDestinationAttribute. For details, refer to the "Modules to Import" section of the HdsNavDestination reference document.
    import { HdsNavDestination, ScrollEffectType, HdsNavDestinationAttribute } from '@kit.UIDesignKit';
    import { LengthMetrics } from '@kit.ArkUI';
    
    @Builder
    export function PageOneBuilder() {
      PageOne()
    }
    
    const  TITLE\_BAR\_HEIGHT\_MINI: number = 56;
    
    @Component
    export struct PageOne {
      @Consume("pageInfos")pageInfos: NavPathStack;
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\];
      scroller: Scroller = new Scroller();
    
      build() {
        HdsNavDestination() { // Create the **HdsNavDestination** component.
          Scroll(this.scroller) { // Set a scrollable container component in the content area to implement a dynamic title bar blur effect that synchronizes with content scrolling.
            Column() {
              Blank().height(TITLE\_BAR\_HEIGHT\_MINI)
              Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
                .width('80%')
                .height(40)
                .margin({ top: '5%', right: '50vp', left: '50vp' , bottom: '5%'})
                .onClick(() => {
                  console.info('HDS\_BASE\_COMPONENT', \`onClick pageOne\`);
                  this.pageInfos.pushPath({ name: 'pageTwo' }) // Push the navigation destination page information identified by **name** onto the navigation stack.
                })
              Button('popToName', { stateEffect: true, type: ButtonType.Capsule })
                .width('80%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  this.pageInfos.popToName('pageTwo') // Pop the first navigation destination page with the specified name to the top of the navigation stack.
                  console.info('popToName' + JSON.stringify(this.pageInfos),
                    'Return value' + JSON.stringify(this.pageInfos.popToName('pageTwo')))
                })
              Button('popToIndex', { stateEffect: true, type: ButtonType.Capsule })
                .width('80%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  this.pageInfos.popToIndex(1) // Pop the page specified by **index** to the top of the navigation stack.
                  console.info('popToIndex' + JSON.stringify(this.pageInfos))
                })
              Button('moveIndexToTop', { stateEffect: true, type: ButtonType.Capsule })
                .width('80%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  this.pageInfos.moveIndexToTop(1) // Move the navigation page at the specified index to the top of the stack.
                  console.info('moveIndexToTop' + JSON.stringify(this.pageInfos))
                })
              Button('clear', { stateEffect: true, type: ButtonType.Capsule })
                .width('80%')
                .height(40)
                .margin(20)
                .onClick(() => {
                  this.pageInfos.clear() // Clear the navigation stack.
                })
              List({ space: 12, initialIndex: 0 }) {
                ForEach(this.arr, (item: number) => {
                  ListItem() {
                    Text('' + item)
                      .width('100%')
                      .height(72)
                      .fontSize(16)
                      .fontWeight(500)
                      .textAlign(TextAlign.Center)
                  }
                  .height(120)
                  .backgroundColor(Color.Orange)
                  .borderRadius(24)
                }, (item: number) => item.toString())
              }
              .edgeEffect(EdgeEffect.None)
              .width('100%')
              .height('100%')
              .nestedScroll({scrollForward:NestedScrollMode.PARENT\_FIRST, scrollBackward: NestedScrollMode.PARENT\_FIRST})
            }
          }.edgeEffect(EdgeEffect.Spring).scrollBar(BarState.Off)
        }
        .titleBar({ // Set the title bar of the **HdsNavDestination** component.
            style: { // Set the style for the title bar of the **HdsNavDestination** component.
              // Set the dynamic blur style for the title bar, including whether to enable dynamic blur during content scrolling, dynamic blur type, and the minimum scrolling distance for the dynamic blur to take effect.
              scrollEffectOpts: {
                enableScrollEffect: true,
                scrollEffectType: ScrollEffectType.COMMON\_BLUR,
                blurEffectiveStartOffset: LengthMetrics.vp(0),
                blurEffectiveEndOffset: LengthMetrics.vp(20)
              },
            },
            content: { // Set the title bar content for the **HdsNavigation** component.
              title: { // Set the title of the title bar for the **HdsNavigation** component.
                mainTitle: "PageOne",
              },
              menu: { // Set the menu items for the title bar of the **HdsNavigation** component.
                value: \[{ // Set the first menu item.
                  content: {
                    label: 'menu1',
                    icon: $r('sys.symbol.ohos\_star'),
                  }
                }, { // Set the second menu item.
                  content: {
                    label: 'menu2',
                    icon: $r('sys.symbol.ohos\_circle'),
                  },
                  badge: {
                      value: '66'
                  }
                }\]
              },
            }
          })
        .hideBackButton(false)
      }
    }
    
3.  Create a level-2 navigation component on the **PageTwo** page.
    
    // PageTwo.ets
    // Import required modules.
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavDestinationAttribute. For details, refer to the "Modules to Import" section of the HdsNavDestination reference document.
    import { HdsNavDestination, HdsNavDestinationAttribute } from '@kit.UIDesignKit';
    
    @Builder
    export function PageTwoBuilder() {
      PageTwo()
    }
    const  TITLE\_BAR\_HEIGHT\_MINI: number = 56;
    @Component
    export struct PageTwo {
      @Consume("pageInfos")pageInfos: NavPathStack;
    
      build() {
        HdsNavDestination() { // Create the **HdsNavDestination** component.
          Column() { // Set the content area of the **HdsNavDestination** component.
            Blank().height(TITLE\_BAR\_HEIGHT\_MINI)
            Button('pushPathByName', { stateEffect: true, type: ButtonType.Capsule })
              .width('80%')
              .height(40)
              .margin(20)
              .onClick(() => {
                this.pageInfos.pushPathByName('pageOne', null) // Push the navigation destination page information identified by **name** onto the navigation stack.
              })
          }.width('100%').height('100%')
        }
        .titleBar({ // Set the title bar of the **HdsNavDestination** component.
          content: {
            title: {
              mainTitle: 'PageTwo'
            },
            menu: {
              value: \[{
                content: {
                  label: 'menu1',
                  icon: $r('sys.symbol.trunk'),
                }
              }\]
            },
          },
        })
        .onReady((context: NavDestinationContext) => {
          this.pageInfos = context.pathStack;
          console.log('current page config info is ' + JSON.stringify(context.getConfigInRouteMap()))
        })
      }
    }
    
4.  Add configurations to the **module** selection of the **entry/src/main/module.json5** configuration file of the project for page navigation.
    
    "routerMap": "$profile:route\_map"
    
5.  Add the **route\_map.json** file to the **entry/src/main/resources/base/profile** directory of the project.
    
    {
      "routerMap": \[
        {
          "name": "pageOne",
          "pageSourceFile": "src/main/ets/pages/PageOne.ets",
          "buildFunction": "PageOneBuilder",
          "data": {
            "description": "this is pageOne"
          }
        },
        {
          "name": "pageTwo",
          "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
          "buildFunction": "PageTwoBuilder"
        }
      \]
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/c9WvyXQYQGardDFy5kETFQ/en-us_image_0000002500424082.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D412D616A4D2AE4F83EE8C0801378483832B379E44F427742FB4144395F17977 "Click to enlarge")
