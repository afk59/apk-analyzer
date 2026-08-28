# Key Attestation Overview and Algorithm Specifications

HUKS provides attestation for the public keys of asymmetric key pairs.

HUKS issues a certificate for the public key of an asymmetric key pair stored in HUKS using the public key infrastructure (PKI) certificate chain technology. The certificate can prove the validity of the public key. The service can use the root CA certificate provided by the system to verify the key certificates issued by HUKS level by level to ensure that the public key and private key in the certificates are from a trusted hardware device and stored in HUKS.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/KOy94fqxTSS2SYNPDagtPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DE3DBA6EBC7D5A736539CE51B2E4AC17AC26C1F83A445993C9371B44BD817F0)

1.  Key attestation is not supported if the caller is a system service with APL of **normal**. In this case, **processName** and **APL** are left empty.
2.  Key attestation is not supported in Emulator scenarios.
3.  Lite wearables do not support key attestation.
4.  Key attestation is available to both the keys generated and imported. The service side needs to check whether the key source meets the expectation based on the key source field in the service certificate on the server.

The **Extensions** field is in the ASN.1 DER encoding format. The data structure is defined as follows:

KeyAttestation ::= SEQUENCE {
  version            AttestationVersion DEFAULT v1,
  claim1             AttestationClaim,
  claim2             AttestationClaim,
  claim3             AttestationClaim,
  ... ...
}
AttestationVersion ::= INTEGER { v1(0) }
AttestationClaim ::= SEQUENCE {
  securityLevel      SecurityLevel,
  type               AttestationType,
  value              AttestationValue
}
SecurityLevel ::= INTEGER
AttestationType ::= OBJECT IDENTIFIER
AttestationValue ::= ANY -- DEFINED BY AttestationType
ApplicationIDType ::= SEQUENCE {
  type               OBJECT IDENTIFIER,
  value              OCT\_STR
}

**AttestationClaim** types and values:

| type (OID) | Data Type of value | securityLevel | Claim Description |
| :-- | :-- | :-- | :-- |
| 1.3.6.1.4.1.2011.2.376.2.1.4 | OCT\_STR | Reserved. | Challenge passed in by the application. |
| 1.3.6.1.4.1.2011.2.376.2.1.3 | ApplicationIDType | Reserved. | Application ID. |
| 1.3.6.1.4.1.2011.2.376.2.1.5 | OCT\_STR | Reserved. | Key source, which is generated or imported. |
| 1.3.6.1.4.1.2011.2.376.2.2.4.8 | UTF8\_STR | Reserved. | Product model, supported since API version 20. |

ApplicationIDType types and values:

| type (OID) | value |
| :-- | :-- |
| 1.3.6.1.4.1.2011.2.376.2.1.3.1 | 
Example: {appId:"xxx", bundleName:"xxx", appIdentifier:"xxx", appMode:"xxx"},

where **appIdentifier** and **appMode** are supported since API version 20.

 |
| 1.3.6.1.4.1.2011.2.376.2.1.3.2 | 

Example: {processName:"xxx", APL:"system\_basic | system\_core"}

APL is [Ability Privilege Level](../../../../application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-concepts-in-the-permission-mechanism).

 |

The key attestation process is as follows:

1.  The service transfers the key alias and properties to HUKS.
    
2.  HUKS issues an X.509 certificate chain, which consists of the root CA certificate, device CA certificate, device certificate, and key certificate in sequence, for the application.
    
3.  The certificate chain is sent to a trusted server. The server parses the certificate chain and verifies the certificate chain validity and whether a single certificate is revoked.
    

The anonymous key attestation is now provided, which does not disclose device information and the caller does not require any permission. Anonymous key attestation is available to all applications. To protect user device information, third-party applications can use anonymous attestation only.

Currently, emulators support anonymous certificates. The certificate used in the debugging environment is not a real device certificate. You need to note this in cloud scenarios and avoid misuse.

#### Supported Algorithms

The following table lists the supported key attestation specifications.

| Algorithm | Description | API Version |
| :-- | :-- | :-- |
| RSA | The padding mode can be PSS or PKCS1\_V1\_5. | 11+ |
| ECC | \- | 11+ |
| X25519 | \- | 16+ |
| ED25519 | \- | 16+ |
| SM2 | \- | 11+ |
