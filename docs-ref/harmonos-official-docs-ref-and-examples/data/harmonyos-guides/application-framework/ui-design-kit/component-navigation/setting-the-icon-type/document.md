# Setting the Icon Type

#### Use Case

The navigation component supports setting the icon type to either text or image since version 6.0.0(20) Beta1.

You can set the [type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section74312125454) attribute in the icon settings under **titleBar** to specify the size of an image icon or to use a text icon (capsule button) or single-character icon (round button).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/1VEKjnodRMuEZYn8tfA6fA/en-us_image_0000002532144165.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7879DBB3858907F35E568D1D928755414BF9BA69A9DBFB5A7CB1105A3AD91544)

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, HdsNavigationTitleMode, TextStyleMode, IconStyleMode, HdsNavigationAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 navigation component. Then set the **type** attribute under **menu** in **titleBar** to set a text icon or specify the size of an image icon.
    
    @Entry
    @Component
    struct Index {
      build() {
        HdsNavigation() { // Create the **HdsNavigation** component.
        }
        .titleBar({
          content: {
            title: { mainTitle: 'MainTitle', subTitle: 'SubTitle' },
            menu: { // Configure the menu content of the **HdsNavigation** component.
              value: \[{
                content: { // Configure the first menu item as a common text icon.
                  label: 'Text icon',
                  type: TextStyleMode.NORMAL,
                }
              }, {
                  content: { // Set the second menu item as a single-character icon.
                  label: '4',
                  type: TextStyleMode.SINGLE\_CHARACTER,
                }
              }, {
                content: { // Set the third menu item as a large image icon.
                  label: 'largeIcon',
                  icon: 'resources/base/media/app\_icon.png',
                  type: IconStyleMode.LARGE,
                }
              }, {
                content: { // Configure the fourth menu item as a small image icon.
                  label: 'smallIcon',
                  icon: 'resources/base/media/app\_icon.png',
                  type: IconStyleMode.SMALL,
                }
              }\],
              maxCount: 4 // Set the maximum number of menu items that can be displayed.
            },
          }
        })
        .titleMode(HdsNavigationTitleMode.MODAL)
      }
    }
