# NavRouter

The **NavRouter** component provides default processing logic for responding to clicks, eliminating the need for manual logic definition.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/SQizqZ3ySMiMpaCJnYOPnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BB813C5F7600DFD9036692E55AC4F1292C3DCB07AD9AF67B290BB16C945B84E)

This component is deprecated since API version 13. You are advised to use [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10) in conjunction with the **navDestination** attribute for page routing.

This component is supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component must contain two child components, the second of which must be [NavDestination](../../navigation-and-switching/navdestination/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/n-dE7Y8MT5ebkQixI7XLtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EEBE9AB3BEAD5638E6B6F1338E6E7C74ECE44A4954A593515DAC0A078002367)

1.  If there is only one child component, the navigation to the **NavDestination** component does not work.
2.  If there is only the **NavDestination** child component, the navigation does not work.
3.  If there are more than two child components, the excess child components are not displayed.
4.  If the second child component is not **NavDestination**, the navigation does not work.

#### APIs

#### \[h2\]NavRouter(deprecated)

NavRouter()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/NBO4LXkCQUSRPUfBRhH0pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A1B4FFD11AEEFDEB5D35F5B4F52416D1EE64BFBAF33B47E00747F79FC5B5E24)

This API is supported since API version 9 and deprecated since API version 13. You are advised to use [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10) and [navDestination](../../navigation-and-switching/navigation/document.md#navdestination10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]NavRouter(deprecated)

NavRouter(value: RouteInfo)

Provides route information so that clicking the **NavRouter** component redirects the user to the specified navigation destination page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/H-9zMG4QT4yBw0K79HaW0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4A533F7B37F1238D932B68EE058E22EFF422987CEFFD3887A3E85DE3330D9BA)

This API is supported since API version 10 and deprecated since API version 13. You are advised to use [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10) and [navDestination](../../navigation-and-switching/navigation/document.md#navdestination10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [RouteInfo](#routeinfodeprecated) | Yes | Route information. |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]mode(deprecated)

mode(mode: NavRouteMode)

Sets the route mode used for redirecting the user from the **NavRouter** component to the specified navigation destination page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/kQBVCIHCQIOOMxrw6ooEmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=740F1D79FA80A259A78B24D1B65E3162629F390392190AC1D2DE25E7BE8BE691)

This API is supported since API version 10 and deprecated since API version 13. You are advised to use [LaunchMode](../../navigation-and-switching/navigation/document.md#launchmode12) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [NavRouteMode](#navroutemodedeprecated) | Yes | 
Route mode used for redirection.

Default value: **NavRouteMode.PUSH\_WITH\_RECREATE**

 |

#### RouteInfo(deprecated)

Route information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | 
Name of the navigation destination page to be redirected to.

**NOTE**

This API is supported since API version 10 and deprecated since API version 13. You are advised to use [name](../../navigation-and-switching/navigation/document.md#properties-1) instead.

 |
| param | unknown | No | Yes | 

Parameter transferred during redirection.

**NOTE**

This API is supported since API version 10 and deprecated since API version 13. You are advised to use [param](../../navigation-and-switching/navigation/document.md#properties-1) instead.

 |

#### NavRouteMode(deprecated)

Defines the routing policy.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/2rigVpxaRQS9XoQTM2C8KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B088ADB2FAC2CD74ED1AD1813DC8ADA5A9D978FC7E79E7E2478D1F3552DFF10C)

This API is supported since API version 10 and deprecated since API version 13. You are advised to use [NavPathStack](../../navigation-and-switching/navigation/document.md#navpathstack10) and [navDestination](../../navigation-and-switching/navigation/document.md#navdestination10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| PUSH\_WITH\_RECREATE | The new navigation destination page replaces the current one. The current page is destroyed, but the information about this page is retained in the navigation stack. |
| PUSH | The new navigation destination page overwrites the current one. The current page is not destroyed, and the information about this page is retained in the navigation stack. |
| REPLACE | The new navigation destination page replaces the current one. The current page is destroyed, and the information about this page is removed from the navigation stack. |

#### Events

#### \[h2\]onStateChange(deprecated)

onStateChange(callback: (isActivated: boolean) => void)

Called when the component activation status changes. **onStateChange(true)** is called when the **NavRouter** component is activated and its **NavDestination** child component is loaded. **onStateChange(false)** is called when the **NavDestination** child component is not displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/eWo0IyshR9Wjy8vk3mI3oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5185C955186CDEBCA9A443FA1D3801E40326FB3D74CAC93B3A74DD4E6C52D765)

This API is supported since API version 9 and deprecated since API version 13. You are advised to use [onShown](../../navigation-and-switching/navdestination/document.md#onshown10) and [onHidden](../../navigation-and-switching/navdestination/document.md#onhidden10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isActivated | boolean | Yes | Component activation status. The value **true** means that component is activated, and **false** means the opposite. |

#### Example

// xxx.ets
@Entry
@Component
struct NavRouterExample {
  @State isActiveWLAN: boolean = false
  @State isActiveBluetooth: boolean = false

  build() {
    Navigation() {
      NavRouter() {
        Row() {
          Row()
            .width(30)
            .height(30)
            .borderRadius(30)
            .margin({ left: 3, right: 10 })
            .backgroundColor(Color.Pink)
          Text(\`WLAN\`)
            .fontSize(22)
            .fontWeight(500)
            .textAlign(TextAlign.Center)
        }
        .width('90%')
        .height(60)

        NavDestination() {
          Flex({ direction: FlexDirection.Row }) {
            Text('No WLAN available.').fontSize(30).padding({ left: 15 })
          }
        }.title("WLAN")
      }
      .margin({ top: 10, bottom: 10 })
      .backgroundColor(this.isActiveWLAN ? '#ccc' : '#fff')
      .borderRadius(20)
      .mode(NavRouteMode.PUSH\_WITH\_RECREATE)
      .onStateChange((isActivated: boolean) => {
        this.isActiveWLAN = isActivated
      })

      NavRouter() {
        Row() {
          Row()
            .width(30)
            .height(30)
            .borderRadius(30)
            .margin({ left: 3, right: 10 })
            .backgroundColor(Color.Pink)
          Text(\`Bluetooth\`)
            .fontSize(22)
            .fontWeight(500)
            .textAlign(TextAlign.Center)
        }
        .width('90%')
        .height(60)

        NavDestination() {
          Flex({ direction: FlexDirection.Row }) {
            Text('No Bluetooth device available.').fontSize(30).padding({ left: 15 })
          }
        }.title("Bluetooth")
      }
      .margin({ top: 10, bottom: 10 })
      .backgroundColor(this.isActiveBluetooth ? '#ccc' : '#fff')
      .borderRadius(20)
      .mode(NavRouteMode.REPLACE)
      .onStateChange((isActivated: boolean) => {
        this.isActiveBluetooth = isActivated
      })
    }
    .height('100%')
    .width('100%')
    .title('Settings')
    .backgroundColor("#F2F3F5")
    .titleMode(NavigationTitleMode.Free)
    .mode(NavigationMode.Auto)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/0H1d46YIRi6rgmaytWhbZg/en-us_image_0000002537766028.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3051A903FDE466434D3E19F26746742D9B804C8DBBFEF6E78458A448F608EC65)
