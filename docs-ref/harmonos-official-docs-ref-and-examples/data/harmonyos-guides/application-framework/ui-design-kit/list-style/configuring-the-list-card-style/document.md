# Configuring the List Card Style

#### Use Case

The function of configuring the list card style is available since version 6.0.0(20) Beta1.

Your app can leverage the [HdsListItemCard](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdslistitemcard) component to implement the system list style across multiple devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/K5i4nzi2RdmcDwmpsKv4Cg/en-us_image_0000002532144147.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C23B8914789F1D2E076F735540A968913170A293AC25B5771417F80C2392217 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { HdsListItemCard, PrefixImage, SuffixSwitch} from '@kit.UIDesignKit';
    import { promptAction } from '@kit.ArkUI';
    
2.  Create the **HdsListItemCard** component and configure the layout as displaying an image on the left, text in the middle, and the switch on the right.
    
    @Entry
    @Component
    struct Test {
      private scroller: ListScroller = new ListScroller();
    
      build() {
        Column() {
          List({ space: 10, scroller: this.scroller }) {
            ListItem() {
              HdsListItemCard({
                // Image in area A
                prefixItem: new PrefixImage({
                  image: $r('app.media.background'),
                  onClick: () => {
                    promptAction.openToast({ message: 'left image' });
                  }
                }),
                // Text in area B
                textItem: {
                  primaryText: {
                    text: 'Primary Text'
                  },
                  secondaryText: {
                    text: 'Secondary Text'
                  },
                  description: {
                    text: 'Description Text'
                  }
                },
                // Switch in area C
                suffixItem: new SuffixSwitch({
                  isCheck: false,
                  onChange: (num: boolean) => {
                    if (num) {
                      promptAction.openToast({ message: 'switch is true' });
                    } else {
                      promptAction.openToast({ message: 'switch is false' });
                    }
                  }
                }),
                onClick: () => {
                  promptAction.openToast({ message: 'hdslistitem' });
                }
              })
            }
          }
          .width('100%')
          .height('100%')
          .margin(10)
        }.backgroundColor(0x1a0a59f7).height('100%')
      }
    }
