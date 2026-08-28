# @ohos.net.networkSecurity (Network Security)

The **networkSecurity** module provides the network security verification capability. Specifically, it provides APIs for applications to verify the certificates in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/BHpomKJ2QhGCyZ-90j-R0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E4A70092FC62FFD1E796C3724B795835D32CEA275CE724DB2DD3855EBF9B67C)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { networkSecurity } from '@kit.NetworkKit';

#### Sample Code

import { networkSecurity } from '@kit.NetworkKit';

// Define certificate blobs
const cert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n... (certificate data) ...\\n-----END CERTIFICATE-----',
};

const caCert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n... (CA certificate data) ...\\n-----END CERTIFICATE-----',
};

// Perform asynchronous certificate verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Certificate verification result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Certificate verification failed:', error);
  });

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/I7obxWN1SFO40-JGaCO-9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D71741035958E7AA8C4647056F70D7EF86370ADD82BB68C35BDBD34001BF2BD)

Be sure to replace the certificate data in the example with the actual certificate data.

#### CertType

Enumerates certificate types.

**System capability**: SystemCapability.Communication.NetStack

| Name | Value | Description |
| :-- | :-- | :-- |
| CERT\_TYPE\_PEM | 0 | PEM certificate |
| CERT\_TYPE\_DER | 1 | DER certificate. |

#### CertBlob

Defines the certificate data.

**System capability**: SystemCapability.Communication.NetStack

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | CertType | No | No | Certificate type. |
| data | string | ArrayBuffer | No | No | Certificate data. |

#### networkSecurity.certVerification

certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>

Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed by the user in the certificate management. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cert | CertBlob | Yes | Certificate to be verified. |
| caCert | CertBlob | No | Custom CA certificate. |

**Return values:**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. The value **0** indicates that the certificate verification is successful, and a non-0 value indicates that the verification has failed. |

**Error codes**

For details about the error codes, see [Network Security Error Codes](../../error-codes/network-security-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/f8sW4sFZRgavoYFwEcdhaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81BB618FD5C055468E52AFD629AB0C0DBC23A5E2DA0AFAEFFF69DEDF73A636C4)

The preceding error codes indicate errors that may occur during certificate verification.

**Example**

import { networkSecurity } from '@kit.NetworkKit';

// Define certificate blobs
const cert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n... (certificate data) ...\\n-----END CERTIFICATE-----',
};

const caCert:networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n... (CA certificate data) ...\\n-----END CERTIFICATE-----',
};

// Perform asynchronous certificate verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Certificate verification result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Certificate verification failed:', error);
  });

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Ngh98i3NSSOgHOfRPsjm5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14B203B2774426DC10BC7328C02464E0345F0CF134017F9C3C3A9C82B0BDC9E5)

Be sure to replace the certificate data in the example with the actual certificate data.

#### networkSecurity.certVerificationSync

certVerificationSync(cert: CertBlob, caCert?: CertBlob): number

Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed by the user in the certificate management. This API returns the result synchronously.

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| cert | CertBlob | Yes | Certificate to be verified. |
| caCert | CertBlob | No | Custom CA certificate. |

**Return values:**

| Type | Description |
| :-- | :-- |
| number | Certificate verification result. The value **0** indicates that the certificate verification is successful, and a non-0 value indicates that the verification has failed. |

**Error codes**

For details about the error codes, see [Network Security Error Codes](../../error-codes/network-security-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/T5nUKkM6R6iICV8mu-bm_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF3E641E076F6892ACA56EAA5C84309C57679CD5E087D83F60EE0175DF0820DD)

The preceding error codes indicate errors that may occur during certificate verification.

**Example**

import { networkSecurity } from '@kit.NetworkKit';

// Create certificate blobs
const cert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n...'
};

const caCert: networkSecurity.CertBlob = {
  type: networkSecurity.CertType.CERT\_TYPE\_PEM,
  data: '-----BEGIN CERTIFICATE-----\\n...'
};

// Asynchronous verification
networkSecurity.certVerification(cert, caCert)
  .then((result) => {
    console.info('Verification Result:', result);
  })
  .catch((error: BusinessError) => {
    console.error('Verification Error:', error);
  });

// Synchronous verification
let resultSync: number = networkSecurity.certVerificationSync(cert, caCert);
console.info('Synchronous Verification Result:', resultSync);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/MQORoVpCTc6V0f4cF4E-SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062346Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B147C8CE0FD363AB8477EA92B9A3651C4D51A99EBB1F4B5B9C4C48D210A3BEA)

Be sure to replace the certificate data in the example with the actual certificate data.

#### networkSecurity.isCleartextPermitted18+

isCleartextPermitted(): boolean

Checks whether plaintext HTTP access is allowed from the preset **network\_config.json** file of the application. By default, plaintext HTTP access is allowed.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Return values:**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value indicating whether plaintext HTTP is allowed. The value **true** indicates that plaintext HTTP is allowed, and the value **false** indicates the opposite. The default value is **true**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermitted();
  console.info(\`isCleartextPermitted Result: ${JSON.stringify(result)}\`);
} catch (error) {
  console.error(\`isCleartextPermitted Error: ${JSON.stringify(error)}\`);
}

#### networkSecurity.isCleartextPermittedByHostName18+

isCleartextPermittedByHostName(hostName: string): boolean

Checks whether host name–based plaintext HTTP access is allowed from the preset **network\_config.json** file of the application. By default, plaintext HTTP access is allowed.

**Required permissions**: ohos.permission.INTERNET

**System capability**: SystemCapability.Communication.NetStack

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| hostName | string | Yes | Host name. |

**Return values:**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value indicating whether host name–based plaintext HTTP is allowed. The value **true** indicates that plaintext HTTP is allowed, and the value **false** indicates the opposite. The default value is **true**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermittedByHostName("xxx");
  console.info(\`isCleartextPermitted Result: ${JSON.stringify(result)}\`);
} catch (error) {
  console.error(\`isCleartextPermitted Error: ${JSON.stringify(error)}\`);
}
