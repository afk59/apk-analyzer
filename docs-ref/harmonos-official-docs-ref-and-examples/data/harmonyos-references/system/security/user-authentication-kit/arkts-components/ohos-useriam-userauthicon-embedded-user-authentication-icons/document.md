# @ohos.userIAM.userAuthIcon (Embedded User Authentication Icons)

**userAuthIcon** provides user identity authentication icons used on the application UI. With **userAuthIcon**, you can:

1.  Easily integrate the facial authentication and fingerprint authentication icons into your applications.
    
2.  Customize the color and size of the icons. The icon style cannot be changed.
    
3.  Start the facial or fingerprint authentication pop-up component once the icon is tapped.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Gxvy7wG4TwOORJ1UeEvwwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F059424ABD12EC79E38B90CE5F36CE9512EC52D3D21DCCDFE50B99F7FA4EDBAD)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

#### Child Components

None.

#### Attributes

The universal attributes are not supported.

#### UserAuthIcon

UserAuthIcon({
  authParam: userAuth.AuthParam,
  widgetParam: userAuth.WidgetParam,
  iconHeight?: Dimension,
  iconColor?: ResourceColor,
  onIconClick?: ()=>void,
  onAuthResult: (result: userAuth.UserAuthResult)=>void
})

**Decorator**: @Component

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.UserIAM.UserAuth.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authParam | [userAuth.AuthParam](../../arkts-apis/ohos-useriam-userauth-user-authentication/document.md#authparam10) | Yes | User authentication parameters. |
| widgetParam | [userAuth.WidgetParam](../../arkts-apis/ohos-useriam-userauth-user-authentication/document.md#widgetparam10) | Yes | Parameters on the user authentication page. |
| iconHeight | [Dimension](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#dimension10) | No | Height of the icon. The aspect ratio is 1:1. The default value is **64fp**. Percentage strings are not supported. |
| iconColor | [ResourceColor](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor) | No | Color of the icon. The default value is **$r('sys.color.ohos\_id\_color\_activated')**. |
| onIconClick | ()=>void | No | Callback to be invoked when the icon is tapped. |
| onAuthResult | (result: [userAuth.UserAuthResult](../../arkts-apis/ohos-useriam-userauth-user-authentication/document.md#userauthresult10))=>void | Yes | 
Callback used to return the user authentication result.

The application must request the ohos.permission.ACCESS\_BIOMETRIC permission. Otherwise, it will only display the icon and cannot start the identity authentication components.

 |

#### Events

Universal events are not supported.

#### Example

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

@Entry
@Component
struct Index {
  rand = cryptoFramework.createRandom();
  len: number = 16;
  randData: Uint8Array = this.rand?.generateRandomSync(this.len)?.data;
  authParam: userAuth.AuthParam = {
    challenge: this.randData,
    authType: \[userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN\],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3
  };
  widgetParam: userAuth.WidgetParam = {
    title: 'Verify identity'
  };

  build() {
    Row() {
      Column() {
        UserAuthIcon({
          authParam: this.authParam,
          widgetParam: this.widgetParam,
          iconHeight: 200,
          iconColor: Color.Blue,
          onIconClick: () => {
            console.info('The user clicked the icon.');
          },
          onAuthResult: (result: userAuth.UserAuthResult) => {
            console.info(\`Get user auth result, result = ${JSON.stringify(result)}\`);
          }
        })
      }
    }
  }
}

Calling **onAuthResult** may throw an error code. For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [User Authentication Error Codes](../../error-codes/user-authentication-error-codes/document.md).

**Facial authentication icon**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yWTirdQPRaOZIvk8rb1EVw/en-us_image_0000002537926316.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE5E6E0D86DA0CBA8E7FBBB4B8664B30E07B1D76C470EAE6AA91D3EC27A2528D)

**Fingerprint authentication icon**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/9zHH7HzHTAiOexTO6XYErg/en-us_image_0000002568686093.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062340Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6A5AA1D4237A6B1AABFADF2C74D249412DFF82F5FDC6241A9C880737C39F57D)
