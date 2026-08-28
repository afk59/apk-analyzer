# Setting Tab Bar Dividers

#### Use Case

The function of setting tab bar dividers is available since version 6.0.0(20) Beta1.

The [HdsTabs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdstabs) container component can be extended to support a tab area divider that can be permanently hidden, permanently visible, or displayed or hidden with motion. You can set the **HdsTabs** component's divider mode to make the divider always visible, always hidden, or to vanish when the content area scrolls 8 vp or more past the tab bar. Divider style customization is also supported.

| 
Always Visible

 | 

Always Hidden

 | 

Visible/Hidden with Scrolling Motion

 |
| :-- | :-- | :-- |
| 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/rbgnWj9xQzeAtVaQzB4brA/en-us_image_0000002500304244.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB5BB5A68A48A685FE540D499D08D0BCA9C023B1B5044525CF8D03876F7341FD "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/jOcVSeK2ROWpgdmXgXkrNg/en-us_image_0000002532144153.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60ABC330B1CD660EB0D681D5D8CF094E9582C27176DD604773BF5B55406EDA5E "Click to enlarge")

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/U2fDNrLWTzaqDF6a5fHXAA/en-us_image_0000002532144157.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061956Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F296FD67ED0791C40E8A466A0BB40D8B1530C92FA41E1EEAE2B83173309C1108 "Click to enlarge")

 |

#### Constraints

1.  The tab bar has been placed at the bottom of the container and supports blur effects. That is, **barPosition** is set to **BarPosition.End**, **vertical** is set to **false**, and **barOverlap** is set to **true**.
2.  If the tab area divider is configured as to display/hide with scrolling motion, only components that use common APIs for scrolling can support this functionality by default. For other types of components, you need to implement this functionality by yourself.
3.  To support the effect of display/hiding with scrolling motion, the corresponding list scrolling controller needs to be bound to the **HdsTabs** controller.

#### Development Procedure

1.  Import required modules.
    
    // Starting from version 6.0.2(22), you do not need to manually import HdsTabsAttribute. For details, refer to the "Modules to Import" section of the HdsTabs reference document.
    import { HdsTabs, HdsTabsController, DividerMode, HdsTabsAttribute } from '@kit.UIDesignKit';
    
2.  Create an Hds level-1 container component and configure the divider style for buttons to support always visible, always hidden, and visible/hidden with scrolling motion.
    
    -   Initialize the list scrolling controller and **HdsTabs** controller, and bind them to ensure proper linkage. Otherwise, the display/hiding of the divider cannot be achieved as the content scrolls.
        
          private controller: HdsTabsController = new HdsTabsController();
          listScroller0: ListScroller = new ListScroller();
          listScroller1: ListScroller = new ListScroller();
        
         aboutToAppear(): void {
            this.controller.bindScroller(0, this.listScroller0);
            this.controller.bindScroller(1, this.listScroller1);
          }
        
          aboutToDisappear(): void {
            this.controller.unbindScroller(this.listScroller0);
            this.controller.unbindScroller(this.listScroller1);
          }
        
    
    -   Place the tab bar to the bottom of the container and support blur effects for the tab bar. Otherwise, the display/hiding of the divider cannot be achieved as the content scrolls.
        
         .barOverlap(true)
         .barPosition(BarPosition.End)
         .vertical(false)
         .divider({
           mode: DividerMode.FOLLOW\_SCROLL,
           style: {
             color: Color.Black,
             strokeWidth: 1,
             startMargin: 0,
             endMargin: 0
           }
         })
        
    
    -   Only components that use common APIs that support scrolling, for example, **List** and **Scroll**, can support displaying/hiding the tab area divider with scrolling motion.
        
        HdsTabs({ controller: this.controller }) {
                TabContent() {
                  List({ scroller: this.listScroller0 }) {} // **listScroller** is a scroll controller that you need to define. You can customize child components for this list
                }
                .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar 1' })
                TabContent() {
                  List({ scroller: this.listScroller1 }) {}
                }
                .tabBar({ icon: $r('app.media.startIcon'), text: 'tabBar2' })
        }
