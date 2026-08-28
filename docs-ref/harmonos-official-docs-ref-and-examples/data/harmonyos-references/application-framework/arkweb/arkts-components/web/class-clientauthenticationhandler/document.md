# Class (ClientAuthenticationHandler)

Implements a **ClientAuthenticationHandler** object to handle SSL client certificate request events returned by the **Web** component. For details about the sample code, see [onClientAuthenticationRequest](../events/document.md#onclientauthenticationrequest9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Evmu24TNRZa_uu1AXPAL9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0682950D388396BE63E68E622E80A5834B94DA754322F6AA9C762A350AD807D)

-   This component is supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **ClientAuthenticationHandler**.

**System capability**: SystemCapability.Web.Webview.Core

#### confirm9+

confirm(priKeyFile : string, certChainFile : string): void

Uses the specified private key and client certificate chain.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| priKeyFile | string | Yes | Full path for storing the private key file. |
| certChainFile | string | Yes | Full path for storing the certificate chain file. |

#### confirm10+

confirm(authUri : string): void

Instructs the **Web** component to use the specified credentials (obtained from the certificate management module).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/JTOv8wFYTgCFTQJGGDqVww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AC7DB59C6A4ED89D5ECEE319091FDC71DD06A6F39C89A68AB9576BC92644502)

The **ohos.permission.ACCESS\_CERT\_MANAGER** permission must be declared.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| authUri | string | Yes | Key value of the credentials. |

The following table lists the supported certificate signature algorithms and key lengths.

| Signing Algorithm | Key Length |
| :-- | :-- |
| SSL\_SIGN\_RSA\_PKCS1\_SHA256 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_RSA\_PKCS1\_SHA384 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_RSA\_PKCS1\_SHA512 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_RSA\_PSS\_SHA256 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_RSA\_PSS\_SHA384 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_RSA\_PSS\_SHA512 | 1024 (supported since API version 18), 2048, 3072, and 4096 |
| SSL\_SIGN\_ECDSA\_SECP256R1\_SHA256 | 256 |
| SSL\_SIGN\_ECDSA\_SECP384R1\_SHA384 | 384 |
| SSL\_SIGN\_ECDSA\_SECP521R1\_SHA512 | 521 |

#### confirm22+

confirm(identity: string, credentialTypeOrCertChainFile: CredentialType | string): void

Instructs the **Web** component to use the specified credential and credential type obtained from the certificate management module.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| identity | string | Yes | Unique ID of a credential. |
| credentialTypeOrCertChainFile | [CredentialType](../enums/document.md#credentialtype22) | string | Yes | [CredentialType](../enums/document.md#credentialtype22) indicates the credential type. **string** indicates the certificate chain file path. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

#### cancel9+

cancel(): void

Cancels the client certificate request sent by the same host and port server. No additional event will be reported for requests from the same host and port server.

**System capability**: SystemCapability.Web.Webview.Core

#### ignore9+

ignore(): void

Ignores this request.

**System capability**: SystemCapability.Web.Webview.Core
