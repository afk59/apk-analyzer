# loginComponentManager (HUAWEI ID Sign-in Component Management)

This module provides logic management for the HUAWEI ID sign-in components, helping integrate the components into your app to implement the sign-in function.

**Start version**: 4.1.0(11)

#### Module Import

import { loginComponentManager } from '@kit.AccountKit';

#### LoginType

Defines HUAWEI ID sign-in types.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

ID

 | 

0

 | 

The OpenID and UnionID are used to associate with a HUAWEI ID.

After a user successfully signs in, the corresponding data is returned.

The response data of this sign-in type contains the **openID**, **unionID**, **authorizationCode**, and **idToken** parameters.

 |
| 

PHONE\_NUMBER

 | 

1

 | 

**PhoneNumber** is used to associate with a HUAWEI ID.

After a user successfully signs in, if the user has not authorized the mobile number for quick verification, the mobile number authorization screen is displayed. If the user has authorized the mobile number, the corresponding data is returned.

This sign-in type does not require real-time verification of the mobile number bound to the HUAWEI ID. The response data contains the **openID**, **unionID**, **authorizationCode**, and **idToken** parameters.

The app uses the authorization code to call the [API for obtaining a user-level credential](../../rest-apis/api-call-credentials/obtaining-a-user-level-credential/document.md#section1085901313579) to request an access token from the Account Kit server, and then uses the access token to call the [API for obtaining HUAWEI ID user information](../../rest-apis/obtaining-user-information/obtaining-user-information-mobile-number/document.md#section2520125725115). The app then obtains the user's mobile number from the user information.

 |
| 

REAL\_TIME\_PHONE\_NUMBER

 | 

2

 | 

**PhoneNumber** is used to associate with a HUAWEI ID.

Each time a user successfully signs in, the real-time mobile number verification and authorization screen is displayed.

This sign-in type requires real-time verification of the mobile number bound to the HUAWEI ID. The response data contains the **openID**, **unionID**, **authorizationCode**, and **idToken** parameters.

The app uses the authorization code to call the [API for obtaining a user-level credential](../../rest-apis/api-call-credentials/obtaining-a-user-level-credential/document.md#section1085901313579) to request an access token from the Account Kit server, and then uses the access token to call the [API for obtaining HUAWEI ID user information](../../rest-apis/obtaining-user-information/obtaining-user-information-mobile-number/document.md#section2520125725115). The app then obtains the user's mobile number from the user information.

NOTE:

**REAL\_TIME\_PHONE\_NUMBER** is not supported currently.

 |
| 

QUICK\_LOGIN

 | 

3

 | 

**PhoneNumber** is used to associate with a HUAWEI ID.

This type does not support the **LoginWithHuaweiIDButton** component of the icon or image & text type.

If this sign-in type is used, the [AuthorizationWithHuaweiIDRequest](../../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) API is called to obtain the anonymous mobile number bound to the HUAWEI ID. If the anonymous mobile number is not obtained, use another sign-in type.

The response data of this sign-in type contains the **openID**, **unionID**, **authorizationCode**, and **idToken** parameters.

The app uses the authorization code to call the [/oauth2/v6/quickLogin/getPhoneNumber](../../rest-apis/obtaining-user-information/obtaining-the-unionid-openid-and-mobile-number-bound-to-a-huawei-id-with-one-tap/document.md#section2520125725115) API to obtain user information, from which it retrieves the user's mobile number.

**Start version**: 5.0.0(12)

**Device behavior differences**: This API works on phones, PCs/2-in-1 devices, tablets, and TVs (only for version 5.1.1). On other devices, it returns error code 1001500003.

 |

#### AppInfo

Defines the app information displayed on the sign-in panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

appIcon

 | 

[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [DrawableDescriptor](../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor)

 | 

No

 | 

No

 | 

App icon.

 |
| 

appName

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

App name, which contains 1 to 19 characters. If the value exceeds this limit or is displayed in large fonts, the exceeding part will be replaced with an ellipsis (...).

 |
| 

appDescription

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

App description, which contains 1 to 44 characters.

NOTE:

-   This parameter is mandatory in version 4.1.0(11).
-   This parameter is optional since version 5.0.0(12). You do not need to set this parameter only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

 |

#### TextType

Defines types of privacy text displayed on the sign-in panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PLAIN\_TEXT

 | 

0

 | 

Plain text, which cannot be tapped.

 |
| 

RICH\_TEXT

 | 

1

 | 

Rich text, which is displayed in blue and can be tapped. It is used to display the _HUAWEI ID User Authentication Agreement_ and the app's privacy policy.

 |

#### PrivacyText

Defines the privacy text to be displayed when the sign-in panel or button is used.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[TextType](#section7401948625)

 | 

No

 | 

No

 | 

Type of the privacy text, including plain text and rich text.

 |
| 

text

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

Privacy text to be displayed on the sign-in panel, which contains a link to redirect to the app's privacy policy and the _HUAWEI ID User Authentication Agreement_.

 |
| 

tag

 | 

string

 | 

No

 | 

Yes

 | 

This parameter is mandatory when **type** is set to [TextType.RICH\_TEXT](#section7401948625). When a user taps a text, the URL specified for the tag will be opened. The app can display privacy content based on the user's tap behavior.

 |

#### LoginIcon

Defines sign-in icons displayed in the optional sign-in area.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icon

 | 

[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr) | [DrawableDescriptor](../../../../application-framework/arkui/arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor)

 | 

No

 | 

No

 | 

Icons of other sign-in options displayed in the optional sign-in area. According to the [visual specifications for HUAWEI ID sign-in](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section61791745172816), the icon is recommended to be a circular image with a radius of 18 vp.

 |
| 

tag

 | 

string

 | 

No

 | 

Yes

 | 

When a user taps an icon, the **tag** value will be returned to the app. The app can display the sign-in screen with other sign-in options based on the user's tap behavior.

 |

#### OptionalLoginButtonAttr

Defines the optional sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

text

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

Text description of the optional sign-in button.

 |

#### OptionalLoginAreaAttr

Defines the optional sign-in area.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

iconArray

 | 

[LoginIcon](#section1248254952118)\[\]

 | 

No

 | 

No

 | 

Icons of other sign-in options passed by the app, displayed in the optional sign-in area. A maximum of five icons can be displayed.

 |

#### LoginPanelParams

Defines the information displayed on the sign-in panel.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

appInfo

 | 

[AppInfo](#section52091116105916)

 | 

No

 | 

No

 | 

App information.

 |
| 

privacyText

 | 

[PrivacyText](#section7272252193)\[\]

 | 

No

 | 

Yes

 | 

Privacy text content.

 |
| 

optionalLoginButtonAttr

 | 

[OptionalLoginButtonAttr](#section16996104113138)

 | 

No

 | 

Yes

 | 

Optional sign-in button.

 |
| 

loginType

 | 

[LoginType](#section79023235528)

 | 

No

 | 

Yes

 | 

HUAWEI ID sign-in type. The default value is [LoginType.ID](#section79023235528).

For one-tap sign-in, use [LoginType.QUICK\_LOGIN](#section79023235528).

 |
| 

anonymousPhoneNumber

 | 

string

 | 

No

 | 

Yes

 | 

Anonymous mobile number bound to a HUAWEI ID. This parameter is mandatory when the sign-in type is set to [LoginType.QUICK\_LOGIN](#section79023235528). For details, please refer to [App-Side Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-phone-unionid-login#section834212543125).

**Start version**: 5.0.0(12)

 |
| 

verifyPhoneNumber

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the SMS verification code screen provided by Account Kit if a HUAWEI ID user did not perform SMS verification in the past 90 days.

**true**: yes

**false**: no The app needs to check whether the mobile number is up-to-date.

Default value: **true**

**Start version**: 5.0.0(12)

 |
| 

optionalLoginAreaAttr

 | 

[OptionalLoginAreaAttr](#section438720171816)

 | 

No

 | 

Yes

 | 

Parameter of the optional sign-in area.

If both **optionalLoginButtonAttr** and **optionalLoginAreaAttr** exist, **optionalLoginAreaAttr** is displayed first.

**Start version**: 5.0.0(12)

 |
| 

riskLevel

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to obtain the risk level of the HUAWEI ID user.

This parameter is mandatory only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

**true**: yes. For details, please refer to [Obtaining a User's Risk Level Through One-Tap HUAWEI ID Sign-in](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-risklevel-byquicklogin).

**false**: no

The default value is **false**.

**Start version**: 5.1.0(18)

 |
| 

securityVerification

 | 

boolean

 | 

No

 | 

Yes

 | 

After enhanced authentication is enabled for an app, the app will use biometric authentication or SMS messages to authenticate users using their HUAWEI IDs to sign in. To obtain the status of enhanced authentication, set this parameter to **false**.

This parameter is mandatory only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

**true**: The **HuaweiIDCredential** response will not contain [enableSecurityVerification](#section1862534912215).

**false**: The **HuaweiIDCredential** response will contain [enableSecurityVerification](#section1862534912215).

Default value: **true**

**Start version**: 6.0.0(20)

 |

#### ClickEvent

Defines the event that a user taps the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

HUAWEI\_ID\_LOGIN\_BUTTON

 | 

0

 | 

Event that a user taps the HUAWEI ID sign-in button.

 |

#### AgreementStatus

Enumerates statuses indicating whether a user accepts the agreement set through [TextType.RICH\_TEXT](#section7401948625).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NOT\_ACCEPTED

 | 

0

 | 

The user does not accept the agreements.

 |
| 

ACCEPTED

 | 

1

 | 

The user has accepted the agreements.

 |

#### HuaweiIDCredential

Response result after successful HUAWEI ID sign-in. It is used to obtain user information and associate the HUAWEI ID.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

unionID

 | 

string

 | 

Yes

 | 

No

 | 

UnionID, which represents the identity of a HUAWEI ID user when using different products of the same developer. The same user has the same UnionID for different apps of the same developer. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

openID

 | 

string

 | 

Yes

 | 

No

 | 

OpenID, which represents the identity of a HUAWEI ID user when using different types of products. The same user has different OpenIDs for different apps. For details about the format requirements, please refer to [Formats of OpenID and UnionID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-9).

 |
| 

authorizationCode

 | 

string

 | 

Yes

 | 

No

 | 

Authorization code. It is a temporary credential used to obtain an access token. The obtained token is valid for 5 minutes and can be used only once. The value contains 1 to 1024 characters.

 |
| 

idToken

 | 

string

 | 

Yes

 | 

Yes

 | 

ID token. It is a JWT character string that contains user information, which can be used to obtain some user information and verify signatures. The value contains 1 to 2048 characters.

 |
| 

enableSecurityVerification

 | 

boolean

 | 

Yes

 | 

Yes

 | 

Indicates whether a HUAWEI ID user has enabled the enhanced authentication function during one-tap sign-in. To obtain this field, set [securityVerification](#section4717249182518) to **false**.

**enableSecurityVerification** is returned only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

**true**: The enhanced authentication function is enabled.

**false**: The enhanced authentication function is not enabled.

**Start version**: 6.0.0(20)

 |

#### Events

Common events are not supported. Only specific events are supported.

#### LoginPanelController

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which is used to register tap events in the component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

#### \[h2\]onClickLoginWithHuaweiIDButton

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginPanelController

Registers an event triggered to return the result of one-tap HUAWEI ID sign-in. This API returns the result asynchronously through a callback. You can process the sign-in response result in the callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[HuaweiIDCredential](#section1862534912215)\>

 | 

Yes

 | 

Callback function. If the HUAWEI ID sign-in is successful, **err** is **undefined** and **data** is the [HuaweiIDCredential](#section1862534912215) object. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md) and [Account Management Error Codes](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1001500002](../../arkts-error-codes/document.md#section134761318124311)

 | 

This error code is reported when a request is already being processed.

 |
| 

[1001500003](../../arkts-error-codes/document.md#section116574197436)

 | 

The scopes or permissions are not supported.

 |
| 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The application is not authorized.

 |
| 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

 |
| 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1001502012](../../arkts-error-codes/document.md#section223413481361)

 | 

The user canceled the authorization.

 |
| 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |
| 

[12300001](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md#section12300001-system-service-abnormal)

 | 

System service works abnormally.

 |
| 

[1005300001](../../arkts-error-codes/document.md#section54021153246)

 | 

The user did not accept the agreement.

 |

#### \[h2\]onClickOptionalLoginButton

onClickOptionalLoginButton(callback: AsyncCallback<void>): LoginPanelController

Registers a tap event of the optional sign-in button. This API returns the result asynchronously through a callback. It is used to switch to another sign-in method.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the user taps a displayed sign-in option, **err** is **undefined**. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickOptionalLoginIcon

onClickOptionalLoginIcon(callback: AsyncCallback<string>): LoginPanelController

Registers a tap event of the optional sign-in icon. This API returns the result asynchronously through a callback. It is used to switch to another sign-in method.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function. If the user successfully taps the sign-in button specified by [LoginIcon](#section1248254952118), **err** is **undefined** and **data** is the tag for [LoginIcon](#section1248254952118). Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickPrivacyText

onClickPrivacyText(callback: AsyncCallback<string>): LoginPanelController

Registers a tap event of privacy content in rich text format. This API returns the result asynchronously through a callback. Your app will redirect the user to the privacy policy through the callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function. If the user taps a privacy text whose type is rich text, **err** is **undefined** and **data** is the tag for [PrivacyText](#section7272252193). Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onChangeAgreementStatus

onChangeAgreementStatus(callback: AsyncCallback<AgreementStatus>): LoginPanelController

Registers a user service agreement status change event. This API returns the result asynchronously through a callback. Set statuses indicating whether the user agrees to or withdraws from the agreement using [setAgreementStatus](#section20291953195314).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[AgreementStatus](#section183397331373)\>

 | 

Yes

 | 

Callback function. If the user accepts or rejects the agreement, **err** is **undefined** and **data** is the obtained [AgreementStatus](#section183397331373). Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]setAgreementStatus

setAgreementStatus(agreementStatus: AgreementStatus): LoginPanelController

Sets the status of the user service agreement.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

agreementStatus

 | 

[AgreementStatus](#section183397331373)

 | 

Yes

 | 

If you want to use a custom agreement screen, set **agreementStatus** to **NOT\_ACCEPTED**. After the user agrees to the agreement, set **agreementStatus** to **ACCEPTED**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]setShowAgreementForOptionalLogin

setShowAgreementForOptionalLogin(): LoginPanelController

Displays the privacy policy dialog box when a user taps another sign-in option.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickEvent

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginPanelController

Registers the event of tapping the HUAWEI ID sign-in button. This API returns the result asynchronously through a callback. Your app will receive a callback after the user taps the HUAWEI ID sign-in button. This callback can be used to record operations events.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[ClickEvent](#section967316103272)\>

 | 

Yes

 | 

Callback function. When the user taps the HUAWEI ID sign-in button, **err** is **undefined**, and **data** is the [ClickEvent](#section967316103272) object obtained. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickCloseButton

onClickCloseButton(callback: AsyncCallback<void>): LoginPanelController

Registers a tap event of the close button or a swipe-back event. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the user closes the button or swipes back, **err** is **undefined**. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginPanelController](#section1419019854714)

 | 

[LoginPanel](../loginpanel-huawei-id-sign-in-panel-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

**Example**:

import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PreviewLoginPanelPage {
  // Indicates whether to display the **LoginPanel** component.
  @State show: boolean = true;
  // Define the privacy text displayed in the **LoginPanel** component.
  privacyText: loginComponentManager.PrivacyText\[\] = \[{
    text: 'I have read and agree to the',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'User Service Agreement',
    tag: 'User Service Agreement',
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'Privacy Policy',
    tag: 'Privacy Policy',
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'and',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'HUAWEI ID User Authentication Agreement',
    tag: 'HUAWEI ID User Authentication Agreement',
    type: loginComponentManager.TextType.RICH\_TEXT
  }\];
  // Define other sign-in icons displayed in the **LoginPanel** component.
  iconArray: loginComponentManager.LoginIcon\[\] = \[{
    // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
    icon: $r('app.media.app\_icon'),
    tag: 'Other sign-in options'
  }\];
  // Construct the controller of **LoginPanel**.
  controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
    // When the sign-in type is not **QUICK\_LOGIN** and no agreement is set, to display your custom agreement dialog box, set the agreement status to **NOT\_ACCEPTED**.
    .setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED)
    // Display the privacy policy dialog box when a user taps another sign-in option.
    .setShowAgreementForOptionalLogin()
    .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
      hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
      if (error) {
        this.dealAllError(error);
        return;
      }
      if (response) {
        // Send the obtained authorization code to the app server.
        const authorizationCode = response.authorizationCode;
        hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
        this.show = false;
        return;
      }
    })
    .onClickOptionalLoginButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
      this.show = false;
    })
    .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', \`onClickOptionalLoginIcon tag: ${tag}\`);
      this.show = false;
    })
    .onClickPrivacyText((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      // The app needs to implement the agreement redirection logic.
      hilog.info(0x0000, 'testTag', \`onClickPrivacyText tag: ${tag}\`);
    })
    .onClickCloseButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickCloseButton.');
      this.show = false;
    })
    .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', \`onChangeAgreementStatus agreementStatus: ${agreementStatus}\`);
    })
    .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', \`onClickEvent clickEvent: ${clickEvent}\`);
    });

  // Handle the error.
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', \`Failed to login, errorCode=${error.code}, errorMsg=${error.message}\`);
    // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
    if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
      // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
      // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
      // Failed to sign in. Try another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
      // Authorization canceled.
    } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
      // System service exception. Try again later or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
      // Repeated request. No further action is needed.
    } else if (error.code === ErrorCode.ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED) {
      // The user does not accept the agreements.
    } else {
      // Failed to sign in. Try another way.
    }
  }

  build() {
    if (this.show) {
      Stack() {
        LoginPanel({
          show: this.show,
          params: {
            appInfo: {
              // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
              appIcon: $r('app.media.app\_icon'),
              appName:'App name',
            },
            privacyText: this.privacyText,
            // Obtain the anonymous mobile number by referring to the _Account Kit Development Guide_.
            anonymousPhoneNumber: '139\*\*\*\*\*\*99',
            loginType: loginComponentManager.LoginType.QUICK\_LOGIN,
            // If both **optionalLoginAreaAttr** and **optionalLoginButtonAttr** exist, **optionalLoginAreaAttr** is displayed first.
            optionalLoginAreaAttr: { iconArray: this.iconArray },
            optionalLoginButtonAttr: { text: 'Other sign-in options' }
          },
          controller: this.controller
        })
      }
      .height('100%')
      .width('100%')
    }
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // The user does not accept the agreements.
  ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED = 1005300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

#### LoginWithHuaweiIDButtonParams

Defines the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

style

 | 

[Style](#section19823216112610)

 | 

No

 | 

No

 | 

Style of the [LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component.

 |
| 

borderRadius

 | 

number

 | 

No

 | 

Yes

 | 

Rounded corner radius of the button border.

Value range: \[0, +∞). A value less than 0 evaluates to the value **0**.

Default value: half of the **height** value.

Unit: vp

 |
| 

iconRadius

 | 

number

 | 

No

 | 

Yes

 | 

Radius of a button of the icon type.

Value range: \[0, +∞). A value less than 0 evaluates to the value **0**.

Default value: **24**

Unit: vp

 |
| 

supportDarkMode

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the button style changes along with the system dark and light color modes.

**true**: yes

**false**: no

Default value: **true**

 |
| 

loginType

 | 

[LoginType](#section79023235528)

 | 

No

 | 

Yes

 | 

HUAWEI ID sign-in type. The default value is [LoginType.ID](#section79023235528).

For one-tap sign-in, use [LoginType.QUICK\_LOGIN](#section79023235528).

 |
| 

textAndIconStyle

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the HUAWEI ID sign-in button in the icon & text style.

**true**: yes

**false**: no (the button supports only the text style)

The default value is **false**.

This parameter is valid only when **loginType** is not set to [LoginType.QUICK\_LOGIN](#section79023235528) and **style** is set to [BUTTON\_RED](#section19823216112610), [BUTTON\_WHITE](#section19823216112610), [BUTTON\_WHITE\_OUTLINE](#section19823216112610), [BUTTON\_BLACK](#section19823216112610), or [BUTTON\_GRAY](#section19823216112610).

**Start version**: 5.0.0(12)

 |
| 

customButtonParams

 | 

[CustomButtonParams](#section2938142118617)

 | 

No

 | 

Yes

 | 

Style parameters of the [BUTTON\_CUSTOM](#section19823216112610) button.

**Start version**: 5.0.0(12)

 |
| 

verifyPhoneNumber

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the SMS verification code screen provided by Account Kit if a HUAWEI ID user did not perform SMS verification in the past 90 days.

**true**: yes

**false**: no The app needs to check whether the mobile number is up-to-date.

Default value: **true**

**Start version**: 5.0.0(12)

 |
| 

extraStyle

 | 

[ExtraStyle](#section87572031102713)

 | 

No

 | 

Yes

 | 

If your app wants to use the styles other than the fixed styles provided by HUAWEI ID, you can call this API to set the desired style.

**Start version**: 5.0.0(12)

 |
| 

loginButtonTextType

 | 

[LoginButtonTextType](#section1645283915811)

 | 

No

 | 

Yes

 | 

If **loginType** is set to [LoginType.QUICK\_LOGIN](#section79023235528), this parameter can be passed to specify the button text content.

The default value is [LoginButtonTextType.QUICK\_LOGIN](#section1645283915811).

-   When the value of this parameter is [LoginButtonTextType.QUICK\_LOGIN](#section1645283915811), the button text indicates one-tap sign-in with HUAWEI ID.
-   When the value of this parameter is [LoginButtonTextType.QUICK\_REGISTRATION](#section1645283915811), the button text indicates one-tap registration with HUAWEI ID.

**Start version**: 5.0.0(12)

 |
| 

riskLevel

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to obtain the risk level of the HUAWEI ID user.

This parameter is mandatory only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

**true**: yes. For details, please refer to [Obtaining a User's Risk Level Through One-Tap HUAWEI ID Sign-in](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-get-risklevel-byquicklogin).

**false**: no

The default value is **false**.

**Start version**: 5.1.0(18)

 |
| 

securityVerification

 | 

boolean

 | 

No

 | 

Yes

 | 

After enhanced authentication is enabled for an app during one-tap HUAWEI ID sign-in, the app will use biometric authentication or SMS messages to authenticate users using their HUAWEI IDs to sign in. To obtain the status of enhanced authentication, set this parameter to **false**.

This parameter is mandatory only when the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528).

**true**: The **HuaweiIDCredential** response will not contain [enableSecurityVerification](#section1862534912215).

**false**: The **HuaweiIDCredential** response will contain [enableSecurityVerification](#section1862534912215).

Default value: **true**

**Start version**: 6.0.0(20)

 |

#### Style

Defines styles of the HUAWEI ID sign-in button.

If the HUAWEI ID sign-in button styles listed below cannot meet your requirements, please refer to [HUAWEI ID Web Login Function](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BUTTON\_RED

 | 

0

 | 

Button with white text and red background. The font size is adaptive to the width and height of the button, ranging from 9 to 16.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

BUTTON\_WHITE

 | 

1

 | 

Button with black text and white background. The font size is adaptive to the width and height of the button, ranging from 9 to 16.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

BUTTON\_WHITE\_OUTLINE

 | 

2

 | 

Button with black text, white background, and a border. The font size is adaptive to the width and height of the button, ranging from 9 to 16.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

BUTTON\_BLACK

 | 

3

 | 

Button with white text and black background. The font size is adaptive to the width and height of the button, ranging from 9 to 16.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

ICON\_RED

 | 

4

 | 

White icon with the red background.

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

ICON\_WHITE

 | 

5

 | 

Red icon with the white background.

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

ICON\_WHITE\_OUTLINE

 | 

6

 | 

Red icon with the white background and a border.

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

ICON\_BLACK

 | 

7

 | 

White icon with the black background.

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

 |
| 

ICON\_GRAY

 | 

8

 | 

Red icon with the gray background.

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

**Start version**: 5.0.0(12)

 |
| 

BUTTON\_GRAY

 | 

9

 | 

Button with black text and gray background. The font size is adaptive to the width and height of the button, ranging from 9 to 16.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

**Start version**: 5.0.0(12)

 |
| 

BUTTON\_CUSTOM

 | 

10

 | 

Button with custom effects including text color, background color, and rounded corner. The font size is adaptive to the width and height of the button, ranging from 9 to 16. You can use [CustomButtonParams](#section2938142118617) to set custom button parameters and adapt to the dark and light color modes.

Check the rules from the following links based on your development scenario.

[Rules for the one-tap HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210)

[Rules for the HUAWEI ID sign-in button](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section2624430102713)

NOTICE:

The button of this style can display plaintext only.

**Start version**: 5.0.0(12)

 |

#### LoginButtonTextType

Enumerates the text displayed on the one-tap HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

QUICK\_LOGIN

 | 

0

 | 

The button text indicates one-tap sign-in with HUAWEI ID. It is used for account sign-in.

 |
| 

QUICK\_REGISTRATION

 | 

1

 | 

The button text indicates one-tap registration with HUAWEI ID. It is used for account registration.

 |

#### CustomButtonParams

Defines parameters of the [BUTTON\_CUSTOM](#section19823216112610) button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

fontColor

 | 

[FontColor](#section1660816591873)

 | 

No

 | 

Yes

 | 

Text color of the [LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) button.

Default value: [FontColor](#section1660816591873).WHITE

 |
| 

backgroundColor

 | 

[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of the button [LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md).

The default value is **Red**.

 |

#### FontColor

Defines text colors that can be used by the [BUTTON\_CUSTOM](#section19823216112610) button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

WHITE

 | 

0

 | 

White.

 |
| 

BLACK

 | 

1

 | 

Black.

 |

#### ExtraStyle

Defines extended parameters of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

buttonStyle

 | 

[ButtonStyle](#section4742141694510)

 | 

No

 | 

Yes

 | 

Custom button style, for which you can dynamically set some attributes as needed.

 |
| 

customButtonStateStyles

 | 

[StateStyles](#section885411463712)

 | 

No

 | 

Yes

 | 

Button state styles, which you can define as needed. This parameter is valid only for buttons of the [BUTTON\_CUSTOM](#section19823216112610) type.

 |
| 

textAndIconButtonParams

 | 

[TextAndIconButtonParams](#section68654575117)

 | 

No

 | 

Yes

 | 

Used to control the icon-text spacing for the icon & text style.

 |
| 

iconButtonParams

 | 

[IconButtonParams](#section474074855419)

 | 

No

 | 

Yes

 | 

Used to control the icon radius for the icon style.

 |

#### RadialGradient

Defines the radial gradient style for the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

center

 | 

\[[Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length), [Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length)\]

 | 

No

 | 

No

 | 

Center of the radial gradient, that is, the coordinates relative to the upper left corner of the current component.

 |
| 

radius

 | 

number | string

 | 

No

 | 

No

 | 

Radius of the radial gradient.

Value range: \[0, +∞)

Values less than 0 will be treated as **0**.

 |
| 

colors

 | 

Array<\[[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor), number\]>

 | 

No

 | 

No

 | 

Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

If this parameter is not set, the effect cannot be achieved.

 |
| 

repeating

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the colors are repeated.

**true**: yes

**false**: no

The default value is **false**.

 |

#### SweepGradient

Defines the angular gradient style for the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

center

 | 

\[[Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length), [Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length)\]

 | 

No

 | 

No

 | 

Center of the angular gradient, that is, the coordinates relative to the upper left corner of the current component.

 |
| 

start

 | 

number | string

 | 

No

 | 

Yes

 | 

Start point of the angular gradient.

When **start** is a number, the default value is **0**. A value less than 0 evaluates to the value **0**, and a value greater than 360 evaluates to the value **360**.

When **start** is a string, the string must be a number or a number followed by one of the following units: deg, rad, grad, and turn. Valid value examples are **90**, **90deg**, and **1.57rad**.

 |
| 

end

 | 

number | string

 | 

No

 | 

Yes

 | 

End point of the angular gradient.

When **end** is a number, the default value is **0**. A value less than 0 evaluates to the value **0**, and a value greater than 360 evaluates to the value **360**.

When **end** is a string, the string must be a number or a number followed by one of the following units: deg, rad, grad, and turn. Valid value examples are **90**, **90deg**, and **1.57rad**.

 |
| 

rotation

 | 

number | string

 | 

No

 | 

Yes

 | 

Rotation angle of the angle gradient.

When **rotation** is a number, the default value is **0**. A value less than 0 evaluates to the value **0**, and a value greater than 360 evaluates to the value **360**.

When **rotation** is a string, the string must be a number or a number followed by one of the following units: deg, rad, grad, and turn. Valid value examples are **90**, **90deg**, and **1.57rad**.

 |
| 

colors

 | 

Array<\[[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor), number\]>

 | 

No

 | 

No

 | 

Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped.

If this parameter is not set, the effect cannot be achieved.

 |
| 

repeating

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the colors are repeated.

**true**: yes

**false**: no

The default value is **false**.

 |

#### ButtonStyle

Defines common attributes of the HUAWEI ID sign-in button. Use **new loginComponentManager.ButtonStyle()** to construct an instance.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

#### \[h2\]buttonSize

buttonSize(value: ButtonSize): ButtonStyle

Sets the width and height of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ButtonSize](#section169691441164919)

 | 

Yes

 | 

When the button type is icon-only, its width and height are the same. The non-**undefined** minimum values of **value.width** and **value.height** are used. If both **value.width** and **value.height** are **undefined**, the value is twice that of **iconRadius** in [LoginWithHuaweiIDButtonParams](#section4717249182518). If **iconRadius** is also **undefined**, the default value **48 vp** is used.

When the button type is non-icon-only, set its width and height through **value.width** and **value.height** respectively. When **value.width** or **value.height** is **undefined**, the width or height of the button is the width or height of the parent layout.

NOTICE:

When setting the width and height of the button, make sure that the width and height of the parent layout must be greater than or equal to those of the button.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]fontSize

fontSize(value: Length): ButtonStyle

Sets the font size of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

Yes

 | 

Font size of the text on the HUAWEI ID sign-in button that is an image & text button or a text-only button. According to the [visual specifications for HUAWEI ID sign-in](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section61791745172816), the recommended font size should fall within 30% to 50% of the button height.

If this parameter is not passed, the font size ranges from 9 vp to 16 vp and is adaptive to the button width.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]fontColor

fontColor(value: ResourceColor | FontColor): ButtonStyle

Sets the text color of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor) | [FontColor](#section1660816591873)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the text color of the button. If the **fontColor** attribute of [CustomButtonParams](#section2938142118617) has been set, the value of this attribute is used preferentially.

If this parameter is not set, black will be used.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]fontWeight

fontWeight(value: string | number | FontWeight): ButtonStyle

Sets the font weight of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

string | number | [FontWeight](../../../../application-framework/arkui/arkts-components/common-definitions/enums/document.md#fontweight)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the font weight of the button. The value of the **number** type is **\[100, 900\]**. The interval is **100**. A larger value indicates a thicker font. When the value is without the range, **400** is used as the value. For the string type, only strings that represent a number, for example, **400**, and the following enumerated values of **FontWeight** are supported: **bold**, **bolder**, **lighter**, **regular**, and **medium**.

The default value is **FontWeight.Medium**, and the corresponding **number** value is **500**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]fontFamily

fontFamily(value: ResourceStr): ButtonStyle

Sets the font family of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the font family of the button.

The default value is **HarmonyOS Sans**.

Currently, **HarmonyOS Sans** and [registered custom fonts](../../../../application-framework/arkui/arkts-api/ui/ohos-font-custom-font-registration/document.md) are supported.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]backgroundColor

backgroundColor(value: ResourceColor): ButtonStyle

Sets the background color of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ResourceColor](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the background color of the button.

If the **backgroundColor** attribute of [CustomButtonParams](#section2938142118617) has been set, the value of this attribute is used preferentially.

If this parameter is not set, red will be used as the background color.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]backgroundEffect

backgroundEffect(value: BackgroundEffectOptions): ButtonStyle

Sets the background attributes of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BackgroundEffectOptions](../../../../application-framework/arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter can be used to set the background attributes of the button, including the saturation, brightness, and color.

If this parameter is not set, the effect cannot be achieved.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]backgroundBrightness

backgroundBrightness(value: BackgroundBrightnessOptions): ButtonStyle

Sets the background brightness of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BackgroundBrightnessOptions](../../../../application-framework/arkui/arkts-components/universal-attributes/basic-attributes/background/document.md#backgroundbrightnessoptions12)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter can be used to set the background brightness of the button, including the brightness change rate and brightness increase degree.

If this parameter is not set, the effect cannot be achieved.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]linearGradient

linearGradient(value: LinearGradient): ButtonStyle

Sets the linear gradient effect for the background color of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[LinearGradient](../../../../application-framework/arkui/arkts-components/universal-attributes/layout-and-borders/border-image/document.md#lineargradient)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the linear gradient effect for the background color of the button. If this parameter is left unset, there will be no effect.

NOTICE:

When this attribute is used, set the button's background color to transparent to avoid jagged edges, for example, **backgroundColor(Color.Transparent)**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]sweepGradient

sweepGradient(value: SweepGradient): ButtonStyle

Sets the angular gradient effect for the background color of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[SweepGradient](#section4541924134916)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the angular gradient effect for the background color of the button.

If this parameter is not set, the effect cannot be achieved.

NOTICE:

When this attribute is used, set the button's background color to transparent to avoid jagged edges, for example, **backgroundColor(Color.Transparent)**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]radialGradient

radialGradient(value: RadialGradient): ButtonStyle

Sets the radial gradient effect for the background color of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[RadialGradient](#section17457938194018)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the radial gradient effect for the background color of the button.

If this parameter is not set, the effect cannot be achieved.

NOTICE:

When this attribute is used, set the button's background color to transparent to avoid jagged edges, for example, **backgroundColor(Color.Transparent)**.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]shadow

shadow(value: ShadowOptions | ShadowStyle): ButtonStyle

Sets the shadow effect for the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ShadowOptions](../../../../application-framework/arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../../../application-framework/arkui/arkts-components/universal-attributes/visual-effects/image-effect/document.md#shadowstyle10)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the shadow effect of the button. If this parameter is left unset, there will be no effect.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]opacity

opacity(value: number | Resource): ButtonStyle

Sets the opacity of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

number | [Resource](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

Yes

 | 

Opacity of a component. The value ranges from 0 to 1. The value **1** means opaque, and **0** means completely transparent so that the component is hidden but is placed in the layout.

The default value is **1**.

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the opacity of the button.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]border

border(value: BorderOptions): ButtonStyle

Sets the border style of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BorderOptions](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#borderoptions)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the border style of the button. If this parameter is left unset, there will be no effect.

NOTICE:

When setting an inner border, make sure to allocate enough space within the parent component to accommodate the button. The parent component's width and height should exceed the button's.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]borderImage

borderImage(value: BorderImageOption): ButtonStyle

Sets the image border style of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[BorderImageOption](../../../../application-framework/arkui/arkts-components/universal-attributes/layout-and-borders/border-image/document.md#borderimageoption)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the border style of the button. If this parameter is left unset, there will be no effect.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]outline

outline(value: OutlineOptions): ButtonStyle

Sets the outline style of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[OutlineOptions](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#outlineoptions11)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the outline style of the button. If this parameter is left unset, there will be no effect.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]hoverEffect

hoverEffect(value: HoverEffect): ButtonStyle

Sets the hover effect for the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[HoverEffect](../../../../application-framework/arkui/arkts-components/common-definitions/enums/document.md#hovereffect8)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the hover effect of the button. If this parameter is left unset, there will be no effect.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]clickEffect

clickEffect(value: ClickEffect): ButtonStyle

Sets the tap effect for the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[ClickEffect](../../../../application-framework/arkui/arkts-components/universal-attributes/visual-effects/click-feedback-effect/document.md#clickeffect-1)

 | 

Yes

 | 

When the button type is [BUTTON\_CUSTOM](#section19823216112610), this parameter is used to set the tap effect for the button. If this parameter is left unset, there will be no effect.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### \[h2\]loadingStyle

loadingStyle(value: LoadingStyle): ButtonStyle

Sets whether to display the loading state of the HUAWEI ID sign-in button during sign-in.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

value

 | 

[LoadingStyle](#section1075651914820)

 | 

Yes

 | 

Indicates whether the button is in the loading state during sign-in.

By default, the loading status does not appear.

NOTICE:

The loading status is not supported for the icon-only button. Therefore, this parameter does not take effect for such a button.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ButtonStyle](#section4742141694510)

 | 

Common attributes of the HUAWEI ID sign-in button.

 |

#### ButtonSize

Defines the dimensions of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

width

 | 

[Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

Yes

 | 

Width of the HUAWEI ID sign-in button.

 |
| 

height

 | 

[Length](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#length)

 | 

No

 | 

Yes

 | 

Height of the HUAWEI ID sign-in button.

 |

#### LoadingStyle

Defines whether to display the loading state of the HUAWEI ID sign-in button during sign-in.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

show

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the button is in the loading state during sign-in.

**true**: yes

**false**: no

The default value is **false**.

 |

#### TextAndIconButtonParams

Defines the spacing between the text and image when the HUAWEI ID sign-in button contains both text and image.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

textAndIconMargin

 | 

number

 | 

No

 | 

Yes

 | 

Spacing between the text and image on the HUAWEI ID sign-in button. The value ranges from 4 vp to 16 vp. The default value is **8 vp**. If the value is smaller than **4 vp**, it will be set to **4 vp**. If it is greater than **16 vp**, it will be set to **16 vp**.

 |

#### IconButtonParams

Defines the radius of the Huawei icon when the HUAWEI ID sign-in button is an icon-only button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

logoRadius

 | 

number

 | 

No

 | 

Yes

 | 

Radius of the Huawei icon on the HUAWEI ID sign-in button that is icon-only.

The default value is **14 vp**, and the minimum value is **8 vp**. The value range is **20%** to **32%** of the button height. If the value is smaller than **20%**, it will be set to **20%**. If it is greater than **32%**, it will be set to **32%**.

 |

#### StateStyles

Defines state styles of the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

normal

 | 

[ButtonStyle](#section4742141694510)

 | 

No

 | 

Yes

 | 

Common style of the HUAWEI ID sign-in button in normal state.

 |
| 

pressed

 | 

[ButtonStyle](#section4742141694510)

 | 

No

 | 

Yes

 | 

Common style of the HUAWEI ID sign-in button in tapped state.

 |
| 

disabled

 | 

[ButtonStyle](#section4742141694510)

 | 

No

 | 

Yes

 | 

Common style of the HUAWEI ID sign-in button in unavailable state.

 |
| 

focused

 | 

[ButtonStyle](#section4742141694510)

 | 

No

 | 

Yes

 | 

Common style of the HUAWEI ID sign-in button in focused state.

 |

#### LoginWithHuaweiIDButtonController

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md#section1624716107193) component controller, which is used to execute tap callbacks in the component.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

#### \[h2\]setAgreementStatus

setAgreementStatus(agreementStatus: AgreementStatus): LoginWithHuaweiIDButtonController

Sets the status of the user service agreement.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

agreementStatus

 | 

[AgreementStatus](#section183397331373)

 | 

Yes

 | 

When the sign-in type is [LoginType.QUICK\_LOGIN](#section79023235528), the agreement status must be set to **ACCEPTED** to complete HUAWEI ID sign-in.

When the sign-in type is not [LoginType.QUICK\_LOGIN](#section79023235528), if HUAWEI ID sign-in is allowed only after the user accepts the agreement, set the agreement status to **NOT\_ACCEPTED** first, and change the status to **ACCEPTED** after the agreement is accepted.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDButtonController](#section6921622144614)

 | 

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickEvent

onClickEvent(callback: AsyncCallback<ClickEvent>): LoginWithHuaweiIDButtonController

Tap event related to the HUAWEI ID sign-in button. This API returns the result asynchronously through a callback. Your app will receive a callback after the user taps the HUAWEI ID sign-in button. This callback can be used to record operations events.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[ClickEvent](#section967316103272)\>

 | 

Yes

 | 

Callback function. When the user taps the HUAWEI ID sign-in button, **err** is **undefined**, and **data** is the [ClickEvent](#section967316103272) object obtained. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDButtonController](#section6921622144614)

 | 

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]onClickLoginWithHuaweiIDButton

onClickLoginWithHuaweiIDButton(callback: AsyncCallback<HuaweiIDCredential>): LoginWithHuaweiIDButtonController

Registers an event triggered to return the result of one-tap HUAWEI ID sign-in. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[HuaweiIDCredential](#section1862534912215)\>

 | 

Yes

 | 

Callback function. If the HUAWEI ID sign-in is successful, **err** is **undefined** and **data** is the [HuaweiIDCredential](#section1862534912215) object. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDButtonController](#section6921622144614)

 | 

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md) and [Account Management Error Codes](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

[1001500001](../../arkts-error-codes/document.md#section1581681312511)

 | 

Failed to check the fingerprint of the app bundle.

 |
| 

[1001500002](../../arkts-error-codes/document.md#section134761318124311)

 | 

This error code is reported when a request is already being processed.

 |
| 

[1001500003](../../arkts-error-codes/document.md#section116574197436)

 | 

The scopes or permissions are not supported.

 |
| 

[1001502001](../../arkts-error-codes/document.md#section539558125020)

 | 

The user has not logged in with HUAWEI ID.

 |
| 

[1001502002](../../arkts-error-codes/document.md#section1393125918588)

 | 

The application is not authorized.

 |
| 

[1001502003](../../arkts-error-codes/document.md#section289120911112)

 | 

Invalid input parameter value.

 |
| 

[1001502005](../../arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

[1001502009](../../arkts-error-codes/document.md#section17561151616317)

 | 

Internal error.

 |
| 

[1001502012](../../arkts-error-codes/document.md#section223413481361)

 | 

The user canceled the authorization.

 |
| 

[1001502014](../../arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |
| 

[12300001](../../../../system/basic-functions/basic-services-kit/error-codes/account-management-error-codes/document.md#section12300001-system-service-abnormal)

 | 

System service works abnormally.

 |
| 

[1005300001](../../arkts-error-codes/document.md#section54021153246)

 | 

The user did not accept the agreement.

 |

#### \[h2\]setEnabled

setEnabled(enabled: boolean): LoginWithHuaweiIDButtonController

Specifies whether the HUAWEI ID sign-in button can be tapped.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

enabled

 | 

boolean

 | 

Yes

 | 

Indicates whether a button can be tapped.

**true** (default value): The HUAWEI ID sign-in button is highlighted and can be tapped; **false**: The HUAWEI ID sign-in button is dimmed and cannot be tapped.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDButtonController](#section6921622144614)

 | 

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

#### \[h2\]continueLogin

continueLogin(callback: AsyncCallback<void>): LoginWithHuaweiIDButtonController

If a user does not accept the agreements, the agreement dialog box is displayed when the user taps the sign-in button. This API is called when the user taps the accept & sign-in button. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the user successfully taps the button for both accepting the agreements and signing in, **err** is **undefined**. Otherwise, an error object will be returned.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[LoginWithHuaweiIDButtonController](#section6921622144614)

 | 

[LoginWithHuaweiIDButton](../loginwithhuaweiidbutton-huawei-id-sign-in-button-component/document.md) component controller, which can be used to register tap events in the component or call methods provided by the component.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS Error Codes](../../arkts-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1005300002](../../arkts-error-codes/document.md#section1396765353817)

 | 

The user did not click the HUAWEI ID login button.

 |

**Example**:

import { util } from '@kit.ArkTS';
import { authentication, loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct QuickLoginButtonComponent {
  logTag: string = 'QuickLoginButtonComponent';
  domainId: number = 0x0000;
  // Anonymous mobile number.
  @State quickLoginAnonymousPhone: string = '';
  // Indicates whether the agreements are accepted.
  @State isSelected: boolean = false;
  // Link to the _HUAWEI ID User Authentication Agreement_. The link here is only an example. For maintainability and security reasons, it is recommended that the domain name be not hardcoded locally during actual development.
  private static USER\_AUTHENTICATION\_PROTOCOL: string =
    'https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
  private static USER\_SERVICE\_TAG = 'User Service Agreement';
  private static PRIVACY\_TAG = 'Privacy Policy';
  private static USER\_AUTHENTICATION\_TAG = 'HUAWEI ID User Authentication Agreement';
  // Define the _Privacy Policy_, _User Service Agreement_, and _HUAWEI ID User Authentication Agreement_ related to **LoginWithHuaweiIDButton**.
  privacyText: loginComponentManager.PrivacyText\[\] = \[{
    text: 'I have read and agree to the',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'User Service Agreement',
    tag: QuickLoginButtonComponent.USER\_SERVICE\_TAG,
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'Privacy Policy',
    tag: QuickLoginButtonComponent.PRIVACY\_TAG,
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'and',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'HUAWEI ID User Authentication Agreement',
    tag: QuickLoginButtonComponent.USER\_AUTHENTICATION\_TAG,
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: '.',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }\];
  // Construct the controller of **LoginWithHuaweiIDButton**.
  controller: loginComponentManager.LoginWithHuaweiIDButtonController =
    new loginComponentManager.LoginWithHuaweiIDButtonController()
      /\*\*
       \* For an app with a custom sign-in UI, if the user does not accept the agreements, set the agreement status to **NOT\_ACCEPTED**.
       \* Set the agreement status to **ACCEPTED** once the user accepts the agreements. The one-tap HUAWEI ID sign-in function is available only when the agreement status is **ACCEPTED**.
       \*/
      .setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED)
      .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
        response: loginComponentManager.HuaweiIDCredential) => {
        this.handleLoginWithHuaweiIDButton(error, response);
      })
      .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
        if (error) {
          hilog.error(this.domainId, this.logTag,
            \`Failed to click. errCode is ${error.code}, errMessage is ${error.message}\`);
          return;
        }
        hilog.info(this.domainId, this.logTag, \`onClickEvent clickEvent: ${clickEvent}\`);
      });
  agreementDialog: CustomDialogController = new CustomDialogController({
    builder: AgreementDialog({
      privacyText: this.privacyText,
      cancel: () => {
        this.agreementDialog.close();
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED);
      },
      confirm: () => {
        this.agreementDialog.close();
        this.isSelected = true;
        this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
        // Call this method to complete accepting the agreements and signing in at the same time, with no need to tap the sign-in button again.
        this.controller.continueLogin((error: BusinessError) => {
          if (error) {
            hilog.error(this.domainId, this.logTag,
              \`Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}\`);
          } else {
            hilog.info(this.domainId, this.logTag,
              'Succeeded in clicking agreementDialog continueLogin.');
          }
        });
      },
      clickHyperlinkText: () => {
        this.agreementDialog.close();
        this.jumpToPrivacyWebView();
      }
    }),
    autoCancel: false,
    alignment: DialogAlignment.Center,
  });

  // Pass the data required for page rendering, such as the anonymous mobile number.
  aboutToAppear(): void {
    this.getQuickLoginAnonymousPhone();
  }

  // Toast message.
  showToast(resource: string) {
    try {
      this.getUIContext().getPromptAction().showToast({
        message: resource,
        duration: 2000
      });
    } catch (error) {
      const message = (error as BusinessError).message
      const code = (error as BusinessError).code
      hilog.error(this.domainId, this.logTag, \`showToast args  errCode is ${code}, errMessage is ${message}\`);
    }
  }

  // Redirect to the **HUAWEI ID User Authentication Agreement** page. This page needs to be configured in the **main\_pages.json** file of the project.
  jumpToPrivacyWebView() {
    this.getUIContext().getRouter().pushUrl({
      // Add the **ohos.permission.INTERNET** permission to **module.json5**.
      url: 'pages/WebPage',
      params: {
        isFromDialog: true,
        url: QuickLoginButtonComponent.USER\_AUTHENTICATION\_PROTOCOL,
      }
    }, (err) => {
      if (err) {
        hilog.error(this.domainId, this.logTag,
          \`Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}\`);
      }
    });
  }

  handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
    response: loginComponentManager.HuaweiIDCredential) {
    if (error) {
      hilog.error(this.domainId, this.logTag,
        \`Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}\`);
      if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
        this.getUIContext().showAlertDialog(
          {
            message: "No Internet connection. Check your network settings.",
            offset: { dx: 0, dy: -12 },
            alignment: DialogAlignment.Bottom,
            autoCancel: false,
            confirm: {
              value: "OK",
              action: () => {
              }
            }
          }
        );
      } else if (error.code === ErrorCode.ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED) {
        // If the agreements are not accepted, a dialog box that asks you to accept the agreements and sign in will be displayed. This callback way is recommended.
        this.agreementDialog.open();
      } else if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
        // Message displayed when no HUAWEI ID is signed in.
        this.showToast("HUAWEI ID not signed in. Try again.")
      } else if (error.code === ErrorCode.ERROR\_CODE\_NOT\_SUPPORTED) {
        // Message displayed when the scope or permission is not supported.
        this.showToast("Unsupported scope or permission.");
      } else if (error.code === ErrorCode.ERROR\_CODE\_PARAMETER\_ERROR) {
        // Parameter error message.
        this.showToast ("Parameter error.");
      } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
        // The user canceled the operation. No special processing is required.
      } else {
        // Messages displayed upon other exceptions.
        this.showToast('Service or network exception. Try again later.');
      }
      return;
    }
    try {
      if (this.isSelected) {
        if (response) {
          hilog.info(this.domainId, this.logTag, 'Succeeded in clicking LoginWithHuaweiIDButton.');
          // Use the information below as needed.
          const authCode = response.authorizationCode;
          const openID = response.openID;
        }
      } else {
        this.agreementDialog.open();
      }
    } catch (err) {
      hilog.error(this.domainId, this.logTag,
        \`Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}\`);
      this.getUIContext().showAlertDialog(
        {
          message: 'Service or network exception. Try again later.',
          offset: { dx: 0, dy: -12 },
          alignment: DialogAlignment.Bottom,
          autoCancel: false,
          confirm: {
            value: 'OK',
            action: () => {
            }
          }
        }
      );
    }
  }

  // Handle the error.
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', \`Failed to login, errorCode=${error.code}, errorMsg=${error.message}\`);
    // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
    if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
      // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
      // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
      // Failed to sign in. Try another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
      // Authorization canceled.
    } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
      // System service exception. Try again later or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
      // Repeated request. No further action is needed.
    } else if (error.code === ErrorCode.ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED) {
      // The user does not accept the agreements.
    } else {
      // Failed to sign in. Try another way.
    }
  }

  getQuickLoginAnonymousPhone() {
    // Create an authorization request and set parameters.
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    /\*\*
     \* To obtain an anonymous mobile number, the **quickLoginAnonymousPhone** scope must be passed. 
     \* To obtain the anonymous mobile number, make sure that your app has got the **quickLoginMobilePhone** scope first.
     \*/
    authRequest.scopes = \['quickLoginAnonymousPhone'\];
    // Used to prevent cross-site request forgery.
    authRequest.state = util.generateRandomUUID();
    // In the one-tap HUAWEI ID sign-in scenario, this parameter must be set to **false**.
    authRequest.forceAuthorization = false;
    const controller = new authentication.AuthenticationController();
    try {
      controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
      // The anonymous mobile number is obtained.
        const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
        if (anonymousPhone) {
          hilog.info(this.domainId, this.logTag, 'Succeeded in authentication.');
          this.quickLoginAnonymousPhone = anonymousPhone;
          return;
        }
        hilog.info(this.domainId, this.logTag, 'Succeeded in authentication. AnonymousPhone is empty.');
        // If the anonymous mobile number fails to be obtained, the custom sign-in screen of the app will appear.
      }).catch((error: BusinessError) => {
        this.dealAllError(error);
      })
    } catch (error) {
      this.dealAllError(error);
    }
  }

  build() {
    Scroll() {
      Column() {
        Column() {
          Column() {
            // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
            Image($r('app.media.app\_icon'))
              .width(48)
              .height(48)
              .draggable(false)
              .copyOption(CopyOptions.None)
              .onComplete(() => {
                hilog.info(this.domainId, this.logTag, 'appIcon loading success.');
              })
              .onError(() => {
                hilog.error(this.domainId, this.logTag, 'appIcon loading fail.');
              })

            Text($r('app.string.app\_name'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Medium)
              .fontWeight(FontWeight.Bold)
              .maxFontSize($r('sys.float.ohos\_id\_text\_size\_headline8'))
              .minFontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
              .maxLines(1)
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 12,
              })

            Text('App description')
              .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
              .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
              .fontWeight(FontWeight.Regular)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8,
              })
          }.margin({
            top: 100
          })

          Column() {
            Text(this.quickLoginAnonymousPhone)
              .fontSize(36)
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Bold)
              .lineHeight(48)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%', minHeight: 48 })

            Text('Mobile number bound to a HUAWEI ID')
              .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
              .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
              .fontWeight(FontWeight.Regular)
              .lineHeight(19)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8
              })
          }.margin({
            top: 64
          })

          Column() {
            LoginWithHuaweiIDButton({
              params: {
                // Styles supported by **LoginWithHuaweiIDButton**.
                style: loginComponentManager.Style.BUTTON\_RED,
                // The one-tap HUAWEI ID sign-in button is in loading state during user sign-in.
                extraStyle: {
                  buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
                    show: true
                  })
                },
                // Rounded corner radius of **LoginWithHuaweiIDButton**.
                borderRadius: 24,
                // Sign-in types supported by **LoginWithHuaweiIDButton**.
                loginType: loginComponentManager.LoginType.QUICK\_LOGIN,
                // The button style of **LoginWithHuaweiIDButton** supports switching along with the change between light and dark modes of the device system.
                supportDarkMode: true
              },
              controller: this.controller
            })
          }
          .height(40)
          .margin({
            top: 56
          })

          Column() {
            Button({
              type: ButtonType.Capsule,
              stateEffect: true
            }) {
              Text('Other sign-in options')
                .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                .fontWeight(FontWeight.Medium)
                .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
                .focusable(true)
                .focusOnTouch(true)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .maxLines(1)
                .padding({ left: 8, right: 8 })
            }
            .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
            .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
            .fontWeight(FontWeight.Medium)
            .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
            .focusable(true)
            .focusOnTouch(true)
            .constraintSize({ minHeight: 40 })
            .width('100%')
            .onClick(() => {
              hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
            })
          }.margin({ top: 16 })
        }.width('100%')

        Row() {
          Row() {
            Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
              .width(24)
              .height(24)
              .focusable(true)
              .focusOnTouch(true)
              .margin({ top: 0 })
              .select(this.isSelected)
              .onChange((value: boolean) => {
                if (value) {
                  this.isSelected = true;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
                } else {
                  this.isSelected = false;
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED);
                }
                hilog.info(this.domainId, this.logTag, \`agreementChecked: ${value}\`);
              })
          }

          Row() {
            Text() {
              ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                if (item?.type === loginComponentManager.TextType.PLAIN\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                    .fontWeight(FontWeight.Regular)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                } else if (item?.type === loginComponentManager.TextType.RICH\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                    .fontWeight(FontWeight.Medium)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                    .onClick(() => {
                      // The app needs to implement the agreement redirection logic based on **item.tag**.
                      hilog.info(this.domainId, this.logTag, \`click privacy text tag: ${item.tag}\`);
                      // HUAWEI ID User Authentication Agreement.
                      if (item.tag === QuickLoginButtonComponent.USER\_AUTHENTICATION\_TAG) {
                        this.jumpToPrivacyWebView();
                      }
                    })
                }
              }, (item: loginComponentManager.PrivacyText) => item.text.toString())
            }
            .width('100%')
          }
          .margin({ left: 12 })
          .layoutWeight(1)
          .constraintSize({ minHeight: 24 })
        }
        .alignItems(VerticalAlign.Top)
        .margin({
          bottom: 44
        })
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .constraintSize({ minHeight: '100%' })
      .margin({
        left: 16,
        right: 16
      })
    }
    .width('100%')
    .height('100%')
  }
}

@CustomDialog
export struct AgreementDialog {
  logTag: string = 'AgreementDialog';
  domainId: number = 0x0000;
  dialogController?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };
  clickHyperlinkText: () => void = () => {
  };
  privacyText: loginComponentManager.PrivacyText\[\] = \[\];
  private static USER\_AUTHENTICATION\_TAG = 'HUAWEI ID User Authentication Agreement';

  build() {
    Column() {
      Row() {
        Text('User Service Agreement and Privacy Policy')
          .id('loginPanel\_agreement\_dialog\_privacy\_title')
          .maxFontSize($r('sys.float.ohos\_id\_text\_size\_headline8'))
          .minFontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
          .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
          .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .maxLines(2)
      }
      .alignItems(VerticalAlign.Center)
      .constraintSize({ minHeight: 56, maxWidth: 400 })
      .margin({
        left: $r('sys.float.ohos\_id\_max\_padding\_start'),
        right: $r('sys.float.ohos\_id\_max\_padding\_start')
      })

      Row() {
        Text() {
          ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
            if (item?.type === loginComponentManager.TextType.PLAIN\_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
                .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
                .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                .fontWeight(FontWeight.Regular)
            } else if (item?.type === loginComponentManager.TextType.RICH\_TEXT && item?.text) {
              Span(item?.text)
                .fontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
                .fontColor('#CE0E2D')
                .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                .fontWeight(FontWeight.Medium)
                .onClick(() => {
                      // The app needs to implement the agreement redirection logic based on **item.tag**.
                  hilog.info(this.domainId, this.logTag, \`click privacy text tag: ${item.tag}\`);
                  // HUAWEI ID User Authentication Agreement.
                  if (item.tag === AgreementDialog.USER\_AUTHENTICATION\_TAG) {
                    hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
                    this.clickHyperlinkText();
                  }
                })
            }
          }, (item: loginComponentManager.PrivacyText) => item.text.toString())
        }
        .width('100%')
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .maxLines(10)
        .textAlign(TextAlign.Start)
        .focusable(true)
        .focusOnTouch(true)
        .padding({ left: 24, right: 24 })
      }.width('100%')

      Flex({
        direction: FlexDirection.Row
      }) {
        Button('Cancel',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel\_agreement\_cancel\_btn')
          .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
          .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
          .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
          .backgroundColor(Color.Transparent)
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
            this.cancel();
          })

        Button('Accept & sign in',
          { type: ButtonType.Capsule, stateEffect: true })
          .id('loginPanel\_agreement\_dialog\_huawei\_id\_login\_btn')
          .fontColor(Color.White)
          .backgroundColor('#CE0E2D')
          .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
          .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
          .fontWeight(FontWeight.Medium)
          .focusable(true)
          .focusOnTouch(true)
          .constraintSize({ minHeight: 40, maxWidth: 400 })
          .width('50%')
          .onClick(() => {
            hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
            this.confirm();
          })
      }
      .margin({
        top: 8,
        left: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_l'),
        right: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_l'),
        bottom: 16
      })
    }.backgroundColor($r('sys.color.ohos\_id\_color\_dialog\_default\_bg'))
    .padding({
      left: 16,
      right: 16
    })
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // This HUAWEI ID does not support one-tap sign-in due to some causes. For example, it is not registered in the Chinese mainland.
  ERROR\_CODE\_NOT\_SUPPORTED = 1001500003,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // The user does not accept the agreements.
  ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED = 1005300001,
  // Parameter error.
  ERROR\_CODE\_PARAMETER\_ERROR = 401,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}

import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Screen for showing the _HUAWEI ID User Authentication Agreement_.
@Entry
@Component
struct WebPage {
  @State webUrl?: string = '';
  @State progress: number = 0;
  logTag: string = 'WebPage';
  domainId: number = 0x0000;
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Column() {
        Button({ type: ButtonType.Normal }) {
          Image($r('sys.media.ohos\_ic\_compnent\_titlebar\_back'))
            .backgroundColor(Color.Transparent)
            .borderRadius(20)
            .width(24)
            .height(24)
            .draggable(false)
            .autoResize(false)
            .focusable(true)
            .fillColor($r('sys.color.ohos\_id\_color\_titlebar\_icon'))
            .matchTextDirection(true)
        }
        .alignSelf(ItemAlign.Start)
        .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
        .borderRadius(20)
        .width(40)
        .height(40)
        .onClick(() => {
          this.getUIContext().getRouter().back();
        })
      }
      .height(56)
      .width('100%')
      .justifyContent(FlexAlign.Center)

      Progress({ value: this.progress, type: ProgressType.Linear })
        .width('100%')
        .visibility(this.progress <= 99 ? Visibility.Visible : Visibility.None)

      Web({ src: this.webUrl ?? '', controller: this.controller })
        .backgroundColor(Color.Transparent)
        .onProgressChange((event) => {
          hilog.info(this.domainId, this.logTag,
            'onProgressChange: ', (event ? event.newProgress : -1));
          this.progress = event ? event.newProgress : 0;
        })
        .darkMode(WebDarkMode.Auto)
        .forceDarkAccess(true)
        .onLoadIntercept((event) => {
          hilog.info(this.domainId, this.logTag, 'onLoadIntercept');
          return false;
        })
        .onErrorReceive((event) => {
          if (event) {
            hilog.error(this.domainId, this.logTag, \`onErrorReceive,errorInfo: ${event?.error?.getErrorInfo()}\`);
          }
        })
    }
    .alignItems(HorizontalAlign.Start)
    .padding({ left: 12, right: 12 })
    .width('100%')
    .height('100%')
  }

  aboutToAppear(): void {
    hilog.info(0x0000, 'testTag', 'aboutToAppear');
    const params = this.getUIContext().getRouter().getParams() as Record<string, string>;
    this.webUrl = params.url ?? '';
    hilog.info(0x0000, 'testTag', \`webUrl: ${this.webUrl}\`);
  }

  aboutToDisappear(): void {
    hilog.info(0x0000, 'testTag', 'aboutToDisappear');
    if (this.webUrl) {
      try {
        this.controller.stop();
      } catch (error) {
        hilog.error(0x0000, 'testTag', \`stop web error, errorCode=${error.code}, errorMsg=${error.message}\`);
      }
    }
  }
}
