# FIDO

This module provides the local passwordless authentication capability of the FIDO Universal Authentication Framework (UAF). Biometric features are used to support passwordless sign-in, passwordless payment, and other service scenarios. You can:

1\. Enable FIDO passwordless identity authentication.

2\. Perform FIDO passwordless identity authentication.

3\. Disable FIDO passwordless identity authentication.

The supported device types are phones, 2-in-1 devices, and tablets.

**Start version**: 4.1.0(11)

#### Module Import

import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext } from '@kit.ArkUI'
import { common } from '@kit.AbilityKit';
import { fido } from '@kit.OnlineAuthenticationKit';

#### ChannelBinding

Transmission channel binding parameters used to verify the channel security.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

serverEndPoint

 | 

string

 | 

No

 | 

Yes

 | 

Base64URL-encoded hash of the TLS server certificate. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty.

 |
| 

tlsServerCertificate

 | 

string

 | 

No

 | 

Yes

 | 

Set this parameter to the Base64URL-encoded, DER-encoded TLS server certificate, if the TLS server certificate is available to the FIDO UAF client. If this data is not available to the FIDO UAF client, this parameter must be absent. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty.

 |
| 

tlsUnique

 | 

string

 | 

No

 | 

Yes

 | 

Set this parameter to the Base64URL-encoded TLS channel Finished structure. If this data is not available to the FIDO UAF client, this parameter must be absent. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty.

 |
| 

cidPubkey

 | 

string

 | 

No

 | 

Yes

 | 

Set this parameter to the Base64URL-encoded serialized JwkKey structure using UTF-8 encoding. If the client TLS stack does not provide TLS ChannelID information to the processing entity, this parameter must be absent. If TLS ChannelID information is supported by the client TLS stack but has not been signaled by the TLS (web) server, this parameter must be set to **unused**. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty.

 |
| 

tokenBinding

 | 

string

 | 

No

 | 

Yes

 | 

Set this parameter to the Base64URL-encoded serialized TokenBindingID structure using UTF-8 encoding. If the client TLS stack does not provide token binding ID information to the processing entity, this parameter must be absent. If token binding ID information is supported by the client TLS stack but has not been signaled by the TLS (web) server, this parameter must be set to **unused**. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty.

 |

#### UAFMessage

UAF dictionary object, which contains the raw UAF protocol message and additional data.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

uafProtocolMessage

 | 

string

 | 

No

 | 

No

 | 

UAF protocol message. The length is subject to restrictions defined by different third-party servers. Note that if the UAF protocol message contains fields such as **challenge** and **transaction**, the Trusted App (TA) request message containing these fields must not exceed 2048 bytes.

 |
| 

additionalData

 | 

string

 | 

No

 | 

Yes

 | 

UAF additional data. The length is subject to restrictions defined by different third-party servers. By default, this parameter is left empty. The value of this parameter must be a JSON string in the format of {"key": value}.

-   When the key is set to **isGuideToSetBiometrics**, it indicates whether to use the system redirection capability to guide users to configure biometric features if they have not done so. The value can be set to **true** or **false**.
    
    -   **true**: yes
    -   **false**: no
    
    When **isGuideToSetBiometrics** is not passed, the system redirection capability will not be used.
    
    **Start version**: 6.0.0(20)
    
-   When the key is set to **navigationButtonText**, you can customize the authentication mode. If the biometric authentication fails and the user taps the button for switching the authentication mode, your app will be instructed to launch the custom authentication page.
    
    -   The value can be set to any text to enable the custom authentication function, and the passed text will be displayed on the button for switching the authentication mode.
    
    When **navigationButtonText** is not passed, the custom authentication function will not be used.
    
    **Start version**: 6.0.1(21)
    

 |

#### Version

UAF protocol version information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

major

 | 

number

 | 

No

 | 

No

 | 

Major version. The default value is **1**.

 |
| 

minor

 | 

number

 | 

No

 | 

No

 | 

Minor version. The default value is **0**.

 |

#### RgbPaletteEntry

RGB three-sample tuple palette entry.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

r

 | 

number

 | 

No

 | 

No

 | 

Red sample value, which ranges from 0 to 255.

 |
| 

g

 | 

number

 | 

No

 | 

No

 | 

Green sample value, which ranges from 0 to 255.

 |
| 

b

 | 

number

 | 

No

 | 

No

 | 

Blue sample value, which ranges from 0 to 255.

 |

#### DisplayPNGCharacteristicsDescriptor

PNG image characteristics object.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

width

 | 

number

 | 

No

 | 

No

 | 

Image width, in dpi. The value must meet the uint32 data type requirements.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Image height, in dpi. The value must meet the uint32 data type requirements.

 |
| 

bitDepth

 | 

number

 | 

No

 | 

No

 | 

Bit depth, in bits. The value must meet the uint8 data type requirements.

 |
| 

colorType

 | 

number

 | 

No

 | 

No

 | 

Color type. **0**: grayscale; **2**: true color; **3**: indexed color; **4**: grayscale with alpha; **6**: true color with alpha

 |
| 

compression

 | 

number

 | 

No

 | 

No

 | 

Compression method. Currently, only the value **0** (zlib) is defined for PNG files. Other values are reserved for future use.

 |
| 

filter

 | 

number

 | 

No

 | 

No

 | 

Filter method. **0**: None; **1**: Sub; **2**: Up; **3**: Average; **4**: Paeth

 |
| 

interlace

 | 

number

 | 

No

 | 

No

 | 

Interlace method. **0**: no interlace; **1**: Adam7

 |
| 

plte

 | 

Array<[RgbPaletteEntry](#section1237320913497)\>

 | 

No

 | 

Yes

 | 

Palette entry. By default, this parameter is left empty.

 |

#### Authenticator

Authenticator object, which describes information about an available authenticator.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

title

 | 

string

 | 

Yes

 | 

No

 | 

Name of an authenticator. The length is subject to restrictions defined by different third-party servers.

 |
| 

aaid

 | 

string

 | 

Yes

 | 

No

 | 

Authenticator Attestation ID (AAID), which uniquely identifies an authenticator. The length is subject to restrictions defined by different third-party servers. The China Financial Certification Authority (CFCA) requires that the value contain nine characters.

 |
| 

description

 | 

string

 | 

Yes

 | 

No

 | 

Description of an authenticator. The length is subject to restrictions defined by different third-party servers.

 |
| 

supportedUAFVersions

 | 

Array<[Version](#section1293122884415)\>

 | 

Yes

 | 

No

 | 

UAF protocol version supported by an authenticator.

 |
| 

assertionScheme

 | 

string

 | 

Yes

 | 

No

 | 

Assertion encoding format. The length is subject to restrictions defined by different third-party servers. The CFCA requires that the value contain eight characters.

 |
| 

authenticationAlgorithm

 | 

number

 | 

Yes

 | 

No

 | 

Supported authentication algorithm.

Currently, the ALG\_SIGN\_SECP256R1\_ECDSA\_SHA256\_RAW algorithm (value: **0x0001**) is supported.

 |
| 

attestationTypes

 | 

Array<number>

 | 

Yes

 | 

No

 | 

List of supported attestation types.

Currently, TAG\_ATTESTATION\_BASIC\_FULL (value: **0x3E07**) is supported.

 |
| 

userVerification

 | 

number

 | 

Yes

 | 

No

 | 

User verification method.

**2**: fingerprint

**16**: face

 |
| 

keyProtection

 | 

number

 | 

Yes

 | 

No

 | 

Key protection type.

Currently, KEY\_PROTECTION\_TEE (value: **0x0004**) is supported.

 |
| 

matcherProtection

 | 

number

 | 

Yes

 | 

No

 | 

Matcher protection type.

Currently, MATCHER\_PROTECTION\_TEE (value: **0x0002**) is supported.

 |
| 

attachmentHint

 | 

number

 | 

Yes

 | 

No

 | 

Mode of connection between an authenticator and the FIDO user device.

Currently, ATTACHMENT\_HINT\_INTERNAL (value: **0x0001**) is supported.

 |
| 

isSecondFactorOnly

 | 

boolean

 | 

Yes

 | 

No

 | 

Indicates whether an authenticator can only be used as a second factor.

Currently, the return value is **false**, indicating no.

 |
| 

tcDisplay

 | 

number

 | 

Yes

 | 

No

 | 

Transaction confirmation display mode.

Currently, TRANSACTION\_CONFIRMATION\_DISPLAY\_ANY (value: **0x0001**) is supported.

 |
| 

tcDisplayContentType

 | 

string

 | 

Yes

 | 

No

 | 

MIME content type supported by the transaction confirmation display.

Currently, text/plain is supported.

 |
| 

tcDisplayPNGCharacteristics

 | 

Array<[DisplayPNGCharacteristicsDescriptor](#section114741413537)\>

 | 

Yes

 | 

No

 | 

Set of PNG characteristics supported by the transaction confirmation display.

 |
| 

icon

 | 

string

 | 

Yes

 | 

No

 | 

PNG icon of an authenticator. The length is restricted by the Base64-encoded size of different PNG images.

 |
| 

supportedExtensionIDs

 | 

Array<string>

 | 

Yes

 | 

No

 | 

List of supported UAF protocol extension identifiers.

 |

#### DiscoveryData

FIDO UAF client software status and available authenticators.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

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

supportedUAFVersions

 | 

Array<[Version](#section1293122884415)\>

 | 

No

 | 

No

 | 

List of FIDO UAF protocol versions supported by a client.

 |
| 

clientVendor

 | 

string

 | 

No

 | 

No

 | 

Vendor of a UAF client. When the vendor is the CFCA, the value must contain four characters.

 |
| 

clientVersion

 | 

[Version](#section1293122884415)

 | 

No

 | 

No

 | 

FIDO UAF client version.

 |
| 

availableAuthenticators

 | 

Array<[Authenticator](#section14811192415918)\>

 | 

No

 | 

No

 | 

Array containing authenticator dictionaries describing the available UAF authenticators.

 |

#### discover

discover(context: common.Context): Promise<DiscoveryData>

Discovers the authentication capability of a device and returns the authenticator data supported by the current device software. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of an ability.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[DiscoveryData](#section11682103284015)\>

 | 

Object containing authenticator data supported by the current device software, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [FIDO](../arkts-api-error-codes/fido/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1005900015

 | 

System Interruption.

 |
| 

1005900016

 | 

Unknown error.

 |

**Call example:**

  // ...
  // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
  let uiContext = new UIContext();
  let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
  try {
    let discoverData: fido.DiscoveryData = await fido.discover(context);
    console.info("Succeeded in doing discover, discoverData:", discoverData);
    // ...
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call discover. Code is ${err.code}, message is ${err.message}\`);
    // ...
  }
  // ...

#### checkPolicy

checkPolicy(context: common.Context, uafRequest: UAFMessage): Promise<void>

Checks whether a message complies with an operation-specific policy. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of an ability.

 |
| 

uafRequest

 | 

[UAFMessage](#section2134351143710)

 | 

Yes

 | 

Policy and operation to be tested.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [FIDO](../arkts-api-error-codes/fido/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1005900005

 | 

No authenticator matching the authenticator policy specified is available.

 |
| 

1005900006

 | 

A violation of the UAF protocol occurred.

 |
| 

1005900015

 | 

System Interruption.

 |
| 

1005900016

 | 

Unknown error.

 |

**Call example:**

  // ...
  // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
  let uiContext = new UIContext();
  let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
  // Obtain the message from the FIDO server.
  let uafMessage: fido.UAFMessage = {
    uafProtocolMessage: "", // **uafProtocolMessage** is the message obtained from the FIDO server.
    additionalData: ""
  };
  try {
    await fido.checkPolicy(context, uafMessage);
    console.info("Succeeded in doing checkPolicy.");
    // ...
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call checkPolicy. Code is ${err.code}, message is ${err.message}\`);
    // ...
  }
  // ...

#### processUAFOperation

processUAFOperation(context: common.Context, uafRequest: UAFMessage, channelBindings?: ChannelBinding): Promise<UAFMessage>

User UAF operation API, which processes UAF protocol messages. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of an ability.

 |
| 

uafRequest

 | 

[UAFMessage](#section2134351143710)

 | 

Yes

 | 

[UAFMessage](#section2134351143710) used by the FIDO client software.

 |
| 

channelBindings

 | 

[ChannelBinding](#section1081123302517)

 | 

No

 | 

Transmission channel binding parameters used to verify the channel security. By default, this parameter is left empty.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[UAFMessage](#section2134351143710)\>

 | 

**UAFMessage** object containing signed response data, which is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [FIDO](../arkts-api-error-codes/fido/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1005900003

 | 

User cancels.

 |
| 

1005900005

 | 

No authenticator matching the authenticator policy specified is available.

 |
| 

1005900006

 | 

A violation of the UAF protocol occurred.

 |
| 

1005900007

 | 

No Facet\_ID is registered.

 |
| 

1005900009

 | 

The authenticator denies access to the generated request.

 |
| 

1005900014

 | 

The user does not record biometric features or the authentication module is abnormal.

 |
| 

1005900015

 | 

System Interruption.

 |
| 

1005900016

 | 

Unknown error.

 |
| 

1005900017

 | 

Switched to the custom authentication process.

 |

**Call example:**

  // ...
  // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
  let uiContext = new UIContext();
  let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
  // Obtain the message from the FIDO server.
  let uafMessage: fido.UAFMessage = {
    uafProtocolMessage: "", // **uafProtocolMessage** is the message obtained from the FIDO server.
    additionalData: '{"navigationButtonText": "Use another authentication mode"}' // This is an optional field. If you want to enable the custom authentication function, pass the text.
  };
  let channelBinding: fido.ChannelBinding = {};
  try {
    let messageResp = await fido.processUAFOperation(context, uafMessage, channelBinding);
    console.info("Succeeded in doing processUAFOperation.");
    // ...
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call processUAFOperation. Code is ${err.code}, message is ${err.message}\`);
    // ...
  }
  // ...

#### notifyUAFResult

notifyUAFResult(context: common.Context, uafResponse: UAFMessage): Promise<void>

Notifies a FIDO authenticator of the enabling result of FIDO passwordless identity authentication. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Security.FIDO

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

Context of an ability.

 |
| 

uafResponse

 | 

[UAFMessage](#section2134351143710)

 | 

Yes

 | 

UAF response message.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [FIDO](../arkts-api-error-codes/fido/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

801

 | 

Device type error.

 |
| 

1005900006

 | 

A violation of the UAF protocol occurred.

 |
| 

1005900015

 | 

System Interruption.

 |
| 

1005900016

 | 

Unknown error.

 |

**Call example:**

  // ...
  // To use **uiContext**, you need to obtain the context of the UIAbility of the screen. For each screen, you need to obtain the context only once.
  let uiContext = new UIContext();
  let context: Context = uiContext.getHostContext() as common.UIAbilityContext;
  // Obtain the message from the FIDO server.
  let uafMessage: fido.UAFMessage = {
    uafProtocolMessage: "", // **uafProtocolMessage** is the message obtained from the FIDO server.
    additionalData: ""
  };
  try {
    await fido.notifyUAFResult(context, uafMessage);
    console.info("Succeeded in doing notifyUAFResult.");
    // ...
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(\`Failed to call notifyUAFResult. Code is ${err.code}, message is ${err.message}\`);
    // ...
  }
  // ...
