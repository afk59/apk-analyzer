# Certificate Framework Overview

The certificate framework shields the differences between third-party certificate algorithm libraries. It provides the capabilities of parsing and validating a certificate, certificate extensions, and a certificate revocation list (CRL), and validating a certificate chain.

You can use the APIs provided by the certificate framework to easily complete your development.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/g3I0kdJ3S06uyhb7Zxzm6Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062005Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EA184A7D9F69A7512B895F37B9D8B6F933CE1E48EB73AA3D010575E961BD5D5)

The certificate framework provides the capabilities of processing certificates and CRL data, but does not provide the capabilities of generating or issuing certificates or CRLs. Certificates and CRLs are issued by a certificate authority (CA) rather than a single application.

#### Basic Concepts

The certificate framework provides APIs for parsing, serializing, signing an X.509 certificate, verifying the signature of an X.509 certificate, and operating X.509 CRLs and the certificate chain validator.

Before you get started, familiarity with the basic certificate concepts is helpful, which include but are not limited to the following:

-   Digital certificate
    
    \- X.509 (also referred to as "X509" in this document)
    
    \- Certificate chain
    
    \- To Be Signed (TBS, which refers to the data structure to be signed in an X.509 certificate, including the version number, serial number, signature algorithm identifier, issuer, validity period, subject, subject public key information, and extension)
    
    \- CRL
    

#### Certificate Specifications

The following describes certificate specifications.

## Certificate Chain Validation

The certificate chain validator does not verify the certificate validity period because the device system time is always untrusted. To check the validity of a certificate, use [checkValidityWithDate()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#checkvaliditywithdate) of **X509Cert**.

## Certificate Format

Currently, only the certificates in DER and PEM formats are supported.

## X.509 Certificate Structure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/-bkGp7g7S9e4_7gKc8SAAw/en-us_image_0000002537925022.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062005Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E1CFD28F2EA62148BE7ACEB5907A95701A4A47B9DE46346C7093A73D4BCAB30)

Certificate example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/fCFeU9RjQFWvrZpmewEJaw/en-us_image_0000002568684799.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062005Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BE2852C765C8C85B6299F31771C6F5D49D8E6597134EEFD7EEC4E150EF48D29)

## X.509 CRL Structure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/QZgOA2GpS7S3eBCP1S0AVg/en-us_image_0000002568764809.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062005Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F953EF65058A288BD4F18A34A04228585A3C8A5360E8F58A88485E961968444E)

CRL example:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/lMfuaJp5QIifHSdASDceWg/en-us_image_0000002537765084.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062005Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BE40F4865518ECC717FD7A02623D080CD50F0A2A8DD06CB0279EC5E6937E5ED)

#### Constraints

The certificate framework depends on the basic algorithm capabilities of the Crypto Architecture Kit, which does not support multi-thread concurrent operations. For details, see [Constraints](../../../crypto-architecture-kit/about-this-kit/document.md#constraints).

#### Development

You can use the certificate framework to implement the following functionalities. Before you start, be sure to familiarize yourself with [Certificate Specifications](#certificate-specifications).

-   [Certificate Development](../certificate-development/document.md)
-   [Certificate Extension Development](../certificate-extension-development/document.md)
-   [CRL Development](../crl-development/document.md)
-   [Certificate Chain Validator Development](../certificate-chain-validator-development/document.md)
-   [Certificate and CRL Collection Development](../certificate-and-crl-collection-development/document.md)
-   [Certificate Chain Development](../certificate-chain-development/document.md)
-   [Creating a TrustAnchor Object Array from a p12 File](../creating-a-trustanchor-object-array-from-a-p12-file/document.md)

The following table lists the classes provided by the certificate framework. Based on the classes, you can learn the related APIs.

| Name | Class | Description |
| :-- | :-- | :-- |
| X.509 certificate | [X509Cert](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#x509cert) | Parses and serializes X.509 certificates, verifies X.509 certificate signatures, and queries certificate information. |
| Certificate extension | [CertExtension](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#certextension10) | Obtains the extended fields in the X.509 certificate, such as whether the CA is used and the CRL distribution point. |
| X.509 CRL | [X509CRL](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#x509crl11) | Provides features such as X.509 certificate revocation list parsing, serialization, and information query. |
| Certificate chain validator | [CertChainValidator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#certchainvalidator) | Verifies the certificate chain (excluding the certificate validity period) and queries the certificate chain algorithm name. |
| Certificate and CRL collection | [CertCRLCollection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#certcrlcollection11) | Queries certificates and certificate revocation lists (CRLs). |
| X.509 certificate chain | [X509CertChain](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cert#x509certchain11) | Verifies the certificate chain and obtains the certificate list. |
