# Setting the Dynamic Blur Style

#### Use Case

The navigation component supports the [common blur style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section21731754221) for the title bar since version 5.1.0(18).

The navigation component supports the [transition blur style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section21731754221) and [gradient blur style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section21731754221) since version 6.0.0(20) Beta1.

To use the navigation component that supports title bar styles that dynamically change as the content area scrolls, set [style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section1867665412513) in the **titleBar** attribute, where you can customize the title bar style displayed before and after scrolling.

## Common Blur Style

Using this style, the background of the title bar can also be uniformly blurred with consistent intensity and sharp boundaries, emphasizing the hierarchical division between controls and content. As content slides into or out of the title bar area, the blurred background and divider line will gradually fade in or out. This style is applicable to non-immersive scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/rXeVtXAvSHC5pBqcLCpzqw/en-us_image_0000002532304117.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AC313C91F682F96698A1AF957BF531B16DD0DDC825D39C02371A8EA59836EB8 "Click to enlarge")

## Transition Blur Style

Using this style, the background of the title bar can also be uniformly blurred with consistent intensity and sharp boundaries, emphasizing the hierarchical division between controls and content. As content scrolls, the title bar undergoes color and state changes, which linearly animate synchronously with the scrolling motion. This style is only applicable for scenarios involving transitions between immersive and non-immersive modes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/IPGcXqm6RZGyCw49Bo-tzA/en-us_image_0000002500304228.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=340289ECF01BC816BE7495BF62E0582E42F27E08D40627994BC5DD1D8AAC16AC "Click to enlarge")

## Gradient Blur Style

This blur effect gradually intensifies or lessens across the screen, featuring soft, seamless edges to create a more immersive page experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4VX4H5kWRDWmxnTBiU6H8Q/en-us_image_0000002532144151.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1BDCD64EC02B962ACB49F7B52488386A839DE100E3EE816399EC142C4345CF8 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, ScrollEffectType, HdsNavigationAttribute } from '@kit.UIDesignKit';
    import { LengthMetrics } from '@kit.ArkUI';
    
2.  Create a level-1 navigation component and set the **scrollEffectType** attribute under **titleBar** to implement the common blur, transition blur, or gradient blur effect.
    
    @Entry
    @Component
    struct Index {
      build() {
        HdsNavigation() { // Create the **HdsNavigation** component.
          // Content area of the **HdsNavigation** component.
        }.titleBar({
          style: { // Set the title bar style of the navigation component.
            // Set the dynamic blur style for the title bar, including whether to enable dynamic blur during content scrolling, dynamic blur type, and the minimum scrolling distance for the dynamic blur to take effect.
            scrollEffectOpts: {
              enableScrollEffect: true,
              scrollEffectType: ScrollEffectType.COMMON\_BLUR,
              blurEffectiveStartOffset: LengthMetrics.vp(0),
              blurEffectiveEndOffset: LengthMetrics.vp(20)
            },
            originalStyle: { // Set the initial style of the content area before scrolling.
              backgroundStyle: { // Set the background style of the title bar.
                backgroundColor: $r('sys.color.ohos\_id\_color\_background'),
              },
              contentStyle: { // Set the style of the content area of the title bar, including the title area, menu area, and back button area.
                titleStyle: {
                  mainTitleColor: $r('sys.color.font\_primary'),
                  subTitleColor: $r('sys.color.font\_secondary')
                },
                menuStyle: {
                  backgroundColor: $r('sys.color.comp\_background\_tertiary'),
                  iconColor: $r('sys.color.icon\_primary')
                },
                backIconStyle: {
                  backgroundColor: $r('sys.color.comp\_background\_tertiary'),
                  iconColor: $r('sys.color.icon\_primary')
                }
              }
            },
            scrollEffectStyle: { // Set the style that appears after the scrolling distance exceeds **blurEffectiveEndOffset**.
              backgroundStyle: {
                backgroundColor: $r('sys.color.ohos\_id\_color\_background\_transparent'),
              },
              contentStyle: {
                titleStyle: {
                  mainTitleColor: $r('sys.color.font\_primary'),
                  subTitleColor: $r('sys.color.font\_secondary')
                },
                menuStyle: {
                  backgroundColor: $r('sys.color.comp\_background\_tertiary'),
                  iconColor: $r('sys.color.icon\_primary')
                },
                backIconStyle: {
                  backgroundColor: $r('sys.color.comp\_background\_tertiary'),
                  iconColor: $r('sys.color.icon\_primary')
                }
              }
            }
          },
          content: { // Set the title bar content.
            title: { mainTitle: 'Main', subTitle: 'Sub' },
          }
        })
      }
    }
