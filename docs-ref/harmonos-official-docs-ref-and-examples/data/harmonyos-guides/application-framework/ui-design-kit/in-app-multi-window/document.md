# In-App Multi-Window

#### Use Case

The in-app multi-window capability is supported since version 6.0.0(20) Beta3.

Your app can call the in-app multi-window API provided by the [MultiWindowEntryInAPP](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-multiwindowentryinapp-api) component to simultaneously run your app in multiple windows. You can also customize the size and color of the split-screen icon and the background, along with the font and size of the text.

If your app has not integrated the **HdsNavigation** component, you can use the **MultiWindowEntryInAPP** component directly to achieve the in-app multi-window effect.

#### Constraints

This capability is applicable only when the current device and its screen state support the multitask view. Currently, the following device types support the multitask view:

-   Bi-fold phones in unfolded state
-   Tri-fold phones in Dual screen mode or Triple screen mode (in landscape mode)
-   Tablets in landscape mode

For other device types or states, this component will not respond to any taps on the in-app multi-window icon.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import MultiWindowEntryInAPPAttribute. For details, refer to the "Modules to Import" section of the MultiWindowEntryInAPP reference document.
    import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
    import { Want } from '@kit.AbilityKit';
    import { TextModifier }  from '@kit.ArkUI';
    
2.  Use the **MultiWindowEntryInAPP** component and set relevant parameters.
    
    @Entry
    @Component
    struct MultiWindowEntryInAPPTest {
      @State textModifier: TextModifier = new TextModifier();
      private want: Want = {
        // Replace the values of **bundleName**, **moduleName**, and **abilityName** with those of your app to start the **UIAbility** in the app.
        bundleName: "com.example.myapplication",
        moduleName: "entry",
        abilityName: "FuncAbility",
      };
    
      build() {
        Row() {
          MultiWindowEntryInAPP({
            want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
              iconOptions: {
                iconSize: 24,
                iconColor: $r('sys.color.font\_primary'),
                iconWeight: FontWeight.Normal,
                backgroundColor: $r('sys.color.comp\_background\_tertiary')
              },
              subtitleOptions: {
                modifier: this.textModifier.fontColor(Color.Black)
              }
            }
          })
            .size({ width: 48, height: 48 })
            .position({ x: 400, y: 30 })
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/beo0Vf9FRpS_PkaIQmMhHw/en-us_image_0000002500424076.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=740236208313B240A528B9E552B11D885314ABE98218DF8F61256283EC6D1BE7 "Click to enlarge")
