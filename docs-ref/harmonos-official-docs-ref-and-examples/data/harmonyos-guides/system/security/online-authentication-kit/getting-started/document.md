# Getting Started

#### Preparing for FIDO Development

Your services must adopt the protocols that comply with the FIDO Universal Authentication Framework (UAF), and you need to deploy a FIDO server that complies with the FIDO UAF. FIDO website: [https://fidoalliance.org/](https://fidoalliance.org/) (here is the [website link disclaimer](../website-link-disclaimer/document.md))

#### Preparing for IFAA Development

Your services must access the IIFAA and the IIFAA central server. IIFAA website: [https://www.iifaa.org.cn/technical#paper](https://www.iifaa.org.cn/technical#paper) (here is the [website link disclaimer](../website-link-disclaimer/document.md))

#### Preparing for SOTER Development

Your services must access the SOTER server. SOTER GitHub: [https://github.com/Tencent/soter](https://github.com/Tencent/soter) (here is the [website link disclaimer](../website-link-disclaimer/document.md))

#### Preparing for Passkey Development

-   For FIDO2-based CAPI development, you need to apply for the passkey service permission listed in the table below. The permission is not required for ArkTS API calls. Ensure that your permission application complies with the [Basic Principles for Using Permissions](../../application-access-control/application-permission-management/application-permission-management-overview/document.md). For details about how to apply for a restricted permission, please refer to [Requesting Restricted Permissions](../../application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).

| 
App Capability

 | 

Required Permission

 |
| :-- | :-- |
| 

Passkeys

 | 

ohos.permission.ACCESS\_FIDO2\_ONLINEAUTH

 |

-   The FIDO2 protocol enables passkey registration based on an app's domain name. To use the passkey service, your app must be associated with a valid website domain as follows: [Enable App Linking in AppGallery Connect](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section189581229144811), [associate an app on your website](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section6903241628), [create an associated website domain name in AppGallery Connect](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section1101111611317), and then [configure the associated website domain name in DevEco Studio](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section13808113610362).
