# Navigator

The **Navigator** component provides redirection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/lIrzWTrLRZKAtr4KHdhF3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AFE320F6C7901F8C0B4CB521A8935FEDF07BB05FD20C84A64B3388679AD7B39)

This component is no longer maintained since API version 13. You are advised to use the [Navigation](../../navigation-and-switching/navigation/document.md) component for page routing.

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

#### APIs

#### \[h2\]Navigator(deprecated)

Navigator(value?: {target: string, type?: NavigationType})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/aAV9apm_SkaVbJwMPO2CEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90DA5ADF05B0DE078836FD0DE7FC33A1999A7639961B35AD9DC0BE39166F7508)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [NavPathInfo](../../navigation-and-switching/navigation/document.md#navpathinfo10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Path of the target page to be redirected to. |
| type | [NavigationType](#navigationtypedeprecated) | No | 
Navigation type.

Default value: **NavigationType.Push**

 |

#### \[h2\]Navigator(deprecated)

Navigator()

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/YsT3tPzrT2aZBHHhYEA5Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C91ECAEABABDE2DEB2EA33867FA5727445BCCB799D561F902CAE71607CBC0CA1)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [NavigationAttribute](../../navigation-and-switching/navigation/document.md#attributes) instead. **NavigationAttribute** is an attribute of the **Navigation** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### NavigationType(deprecated)

Navigation type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Push | 1 | 
Navigates to the specified page in the application.

**NOTE**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [pushPath](../../navigation-and-switching/navigation/document.md#pushpath10) instead.

 |
| Replace | 2 | 

Replaces the current page with another one in the application and destroys the current page.

**NOTE**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [replacePath](../../navigation-and-switching/navigation/document.md#replacepath11) instead.

 |
| Back | 3 | 

Returns to the specified page. If the specified page does not exist in the stack, no response is returned. If no page is specified, the previous page is returned to.

**NOTE**

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [pop](../../navigation-and-switching/navigation/document.md#pop10) instead.

 |

#### Attributes

#### \[h2\]active(deprecated)

active(value: boolean)

Sets whether the **Navigator** component is activated. If the component is activated, the corresponding navigation takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/iqhBr7paSuyvZqLx9GQNhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB8E4A483C9F22BBE555DEAC662C949BD30F38D85D09BB6FFDC00E1727F285AF)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [Navigation](../../navigation-and-switching/navigation/document.md) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | Whether the **Navigator** component is activated. The value **true** means that the component is activated, and **false** means the opposite. |

#### \[h2\]params(deprecated)

params(value: object)

Sets the data that needs to be passed to the target page during redirection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/gF4beF1TR1apX0PDJXIvow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B717BC87C7F42B3E6795E818FFEC26142AFA6361AA013FE8A9760436E18E6B0)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [param](../../navigation-and-switching/navigation/document.md#properties-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | object | Yes | Data that needs to be passed to the target page during redirection. You can use [router.getParams()](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md#routergetparamsdeprecated) to obtain the data on the target page. |

#### \[h2\]target(deprecated)

target(value: string)

Sets the path of the target page to be redirected to. The target page must be added to the **main\_pages.json** file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/1u54zpUORFCnc1WumQ7N-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F0B327A4DD2B4FC3B9346D68BFFE2C7021F6FD55294DFD55CAAB22A7AA8A5C1)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [Navigation](../../navigation-and-switching/navigation/document.md) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Path of the target page to be redirected to. |

#### \[h2\]type(deprecated)

type(value: NavigationType)

Sets the navigation type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/nASPwPZGRXqAr4wVIgmvug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0A519A9974A375AEEAD52512BCA334ECF808F830B2BAFDF752201689EF4724B)

This API is supported since API version 7 and deprecated since API version 13. You are advised to use [Navigation](../../navigation-and-switching/navigation/document.md) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [NavigationType](#navigationtypedeprecated) | Yes | 
Navigation type.

Default value: **NavigationType.Push**

 |

#### Example

// code.ets
export interface NameObject {
  name: string;
}

export class TextObject {
  text: NameObject;

  constructor(text: NameObject) {
    this.text = text;
  }
}

import { NameObject, TextObject } from '../../code';

@Entry
@Component
struct NavigatorExample {
  @State active: boolean = false
  @State name: NameObject = { name: 'news' }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Detail', type: NavigationType.Push }) {
        Text('Go to ' + this.name.name + ' page')
          .width('100%').textAlign(TextAlign.Center)
      }.params(new TextObject(this.name)) // Pass parameters to the Detail page.

      Navigator() {
        Text('Back to previous page').width('100%').textAlign(TextAlign.Center)
      }.active(this.active)
      .onClick(() => {
        this.active = true
      })
    }.height(150).width(350).padding(35)
  }
}

import { NameObject } from '../../code';

@Entry
@Component
struct DetailExample {
  // Receive the input parameters of Navigator.ets.
  params: Record<string, NameObject> = this.getUIContext().getRouter().getParams() as Record<string, NameObject>
  @State name: NameObject = this.params.text

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Navigator({ target: 'pages/container/navigator/Back', type: NavigationType.Push }) {
        Text('Go to back page').width('100%').height(20)
      }

      Text('This is ' + this.name.name + ' page')
        .width('100%').textAlign(TextAlign.Center)
    }
    .width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}

// Back.ets
@Entry
@Component
struct BackExample {
  build() {
    Column() {
      Navigator({ target: 'pages/container/navigator/Navigator', type: NavigationType.Back }) {
        Text('Return to Navigator Page').width('100%').textAlign(TextAlign.Center)
      }
    }.width('100%').height(200).padding({ left: 35, right: 35, top: 35 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/wO97pI8kRQC5uEGCW8Mq-g/en-us_image_0000002537925968.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B5A94185BE21307619B25EA1705D1EF6D11A8BA25248630A482AED815578B36)
