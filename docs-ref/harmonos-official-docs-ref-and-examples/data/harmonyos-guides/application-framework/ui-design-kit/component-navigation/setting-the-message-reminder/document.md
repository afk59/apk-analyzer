# Setting the Message Reminder

#### Use Case

The navigation component supports the message reminder capability in the menu bar since version 5.1.0 (18).

To add a message reminder to the upper right corner of a menu item, set the [badge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdsnavigation#section7349101217489) attribute in menu item settings of the title bar.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Wn9v86cnTSOdOsTeDQiTMA/en-us_image_0000002532304133.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=414144B13703F81ACC1394DC15407B8B8868809B6626CE4F6AA52BD72D1A0EF9 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsNavigationAttribute. For details, refer to the "Modules to Import" section of the HdsNavigation reference document.
    import { HdsNavigation, HdsNavigationAttribute } from '@kit.UIDesignKit';
    
2.  Create a level-1 navigation component, and set the **badge** attribute under **menu** in **titleBar** to define the message reminder style.
    
    @Entry
    @Component
    struct Index {
      build() {
        HdsNavigation() { // Create the **HdsNavigation** component.
        }.titleBar({
          content: { // Set the title bar content for the **HdsNavigation** component.
            menu: { // Set the menu area content for the title bar of the **HdsNavigation** component.
              value: \[{
                content: { // Set the first menu item.
                  label: 'menu1',
                  icon: 'resources/base/media/startIcon.png',
                  isEnabled: true,
                },
                badge: { // Set the reminder badge for the first menu item.
                  count: 1,
                }
              },{
                content: { // Set the second menu item.
                  label: 'menu2',
                  icon: 'resources/base/media/startIcon.png',
                  isEnabled: true,
                },
                badge: { // Set the reminder badge for the second menu item.
                  count: 100,
                }
              }\]
            },
            title: { mainTitle: 'MainTitle', subTitle: 'SubTitle' },
          }
        })
      }
    }
