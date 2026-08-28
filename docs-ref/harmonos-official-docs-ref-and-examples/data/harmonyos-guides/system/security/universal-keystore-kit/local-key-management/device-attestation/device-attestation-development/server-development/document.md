# Server Development

#### Verifying the Key Attestation Certificate Chain

The key attestation certificate chain (certificate array) uses the X.509 format. The first certificate is the **key attestation certificate**, the last one is the root CA certificate, with the intermediate CA certificates in the middle.

The application server verifies the key attestation certificate chain as follows:

1.  Use the root CA certificate provided by the Universal Keystore Kit official website to verify the validity of the certificate chain. ([URL for downloading the root CA certificate](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer))
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/qcx_JFWnSRePUi5ZdjJpDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C62AA14E5A6304A6C54816ABC8DDA838CB0749644641108FADC3B2544A1ED057)
    
    Do not use an intermediate CA certificate to verify the key attestation certificate chain on the application server. Unexpected result may be caused if the intermediate CA certificate has expired or is revoked.
    
2.  Parse the **key attestation certificate** to obtain the application public key, challenge value, application ID, and key management component ID.
    
    The application public key is directly obtained from the **subjectPublicKeyInfo** field in the key attestation certificate.
    
    Other fields are obtained from the **Extensions** field of the key attestation certificate. The **Extensions** field OID is 1.3.6.1.4.1.2011.2.376.1.3 (key attestation extension field).
    
3.  Check whether the challenge value is valid.
4.  Check whether the application ID is the same as expected. Check whether the request is from the expected HarmonyOS application based on the application ID.
5.  Check whether the key source is the same as expected.

**The key attestation certificate format is described as follows.**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/HFtNLr_pR5aLK9-tfnFokQ/en-us_image_0000002335938161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71727CB619D598ED8162DE1CAFFF6A89FF14CAA572948BC400CC8F0D46700DDB)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/dBP0KnwVQ7eS6cfPN6cy3w/en-us_image_0000002302018750.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062012Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3F2B9C0DE597CD564C2052EF45FE7CF16B2C589BBC4EB4D171C95A512D1EBCC "Click to enlarge")

The **Extensions** field is in the ASN.1 DER encoding format. The data structure is defined as follows:

HuaweiAttestation ::= SEQUENCE {
 version             AttestationVersion DEFAULT v1,
 claim1             AttestationClaim,
 claim2             AttestationClaim,
 claim3             AttestationClaim,
 ... ...
}

AttestationVersion ::= INTEGER { v1(0) }

AttestationClaim ::= SEQUENCE {
   securityLevel       SecurityLevel,
   type             AttestationType,
   value            AttestationValue
}

SecurityLevel ::= INTEGER
AttestationType ::= OBJECT IDENTIFIER
AttestationValue ::= ANY -- DEFINED BY AttestationType

ApplicationIDType ::= SEQUENCE {
   type                         OBJECT IDENTIFIER,
   value                        OCT\_STR
}

**Values of the AttestationClaim:**

| 
**No.**

 | 

Value of Type (**OID**)

 | 

Data Type of Value

 | 

securityLevel

 | 

**Claim Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

1

 | 

1.3.6.1.4.1.2011.2.376.2.1.4

 | 

OCT\_STR

 | 

This field is reserved.

 | 

Challenge value passed in by the application.

 |
| 

2

 | 

1.3.6.1.4.1.2011.2.376.2.1.3

 | 

ApplicationIDType

 | 

This field is reserved.

 | 

Application ID.

 |
| 

3

 | 

1.3.6.1.4.1.2011.2.376.2.2.2.6

 | 

OCT\_STR

 | 

This field is reserved.

 | 

The key management component ID. The value is **0x28c4fb4944afec11b9090242ac120002**.

 |
| 

4

 | 

1.3.6.1.4.1.2011.2.376.2.2.4.8

 | 

UTF8String

 | 

2

 | 

Product model of the device, which is supported since API 20. The product model is used in device risk control scenarios to identify the device activities in black and gray industries. Do not use this field to authenticate device identities.

 |

**Values of securityLevel:**

| 
**securityLevel**

 | 

Description

 |
| :-- | :-- |
| 

2

 | 

REE (framework layer), whose data comes from the HarmonyOS system layer.

 |
| 

3

 | 

TEE, which protects data.

 |

**Values of the ApplicationIDType:**

| 
Value of Type (OID)

 | 

Value Description

 |
| :-- | :-- |
| 

1.3.6.1.4.1.2011.2.376.2.1.3.1

 | 

HarmonyOS HAP application information, including the following fields:

1.  appId: bundleName of the HAP application and hash of the public key of the signature certificate.
2.  bundleName: bundle name of the HAP application.
3.  appIdentifier: unified app ID allocated to the HAP application in AppGallery Connect. This field is supported since API version 20.
4.  appMode: status of the HAP application, which can be **debug** or **release**. This field is supported since API version 20.
    
    The value is a JSON string. An example is as follows:
    
    {
      "appId":"com.example.attesthcts\_BDmjsOezxRmguzlYRVhQavW22Eswi5sX61wOAysWPOGS8TZ5tY1u1A9EcvarzyrfOEj5zT8BCGkfFkVjn0m5wzo=",  
      "bundleName":"com.example.attesthcts",
      "appIdentifier":"5765880207853009781",
      "appMode":"release"
    }
    

 |
| 

1.3.6.1.4.1.2011.2.376.2.1.3.2

 | 

System ability ID. An example is as follows:

{processName: "huawei\_share"}

 |

**Sample code:**

import org.bouncycastle.asn1.\*;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.io.ByteArrayInputStream;
import java.io.FileOutputStream;
import java.security.PublicKey;
import java.security.Security;
import java.security.cert.CertPath;
import java.security.cert.CertPathValidator;
import java.security.cert.CertificateFactory;
import java.security.cert.PKIXCertPathValidatorResult;
import java.security.cert.PKIXParameters;
import java.security.cert.TrustAnchor;
import java.security.cert.X509Certificate;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.List;

import com.alibaba.fastjson.JSON;

public class ParseAttestation {
    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    // Key attestation certificate chain data obtained by a HarmonyOS HAP application by using the anonAttestKeyItem API.
    static String\[\] g\_attestCertStr = new String\[\]{"-----BEGIN CERTIFICATE-----\\nMIIEUDCCA/WgAwIBAgIOCfv5Xf9hjA2u32gjpG8wCgYIKoZIzj0EAwIwXTE5MDcGA1UEAwwwSHVhd2VpIENCRyBFQ0MgRGV2aWNlIEFub255bW91cyBBdHRlc3RhdGlvbiBDQSAxMRMwEQYDVQQKDApIdWF3ZWkgQ0JHMQswCQYDVQQGEwJDTjAeFw0yNTA1MTMwNjI3NDlaFw0yNTA1MjAwNjI3NDlaMCwxKjAoBgNVBAMMIURldmljZSBDZXJ0aWZpY2F0ZSBNYW5hZ2VtZW50IEtleTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALd0wgFgvDF5uPq2hh69LdRHnIX3+mzdAzf10L9Jk6bWPZqqTvz88ZX7e12Su1Myf5iyT3TMKjZ+Y2SnsWpHG/7Dpx990u7/CxeeRY0qziIqMTEbrLFaSHY++///9SxmEiM7a3z2Ged2FzDSvOTj1JVmm2hk+bUcceTVuHAmRwidFIQrL5h/lxaO3uPFqbTdiW6ocz06pEbi8mg6LAafik1pfsO30a3yIGiH1f4uZhCEFjHQxQdSFsRPh04Ehclx6lQ196tO0d3RHR8dxL7ghGNxs9rB1Sq/0TH2mK1vKAY/YgvBs5nypOnDY+0MXN7j5NucvJ32wssGI7CbmMxVeZMCAwEAAaOCAf0wggH5MB0GA1UdDgQWBBQA6HLpfdJvtiqPqQXenry8b6qjYzAMBgNVHRMBAf8EAjAAMAkGA1UdOAQCBQAwHwYDVR0jBBgwFoAU4yzL/3aHOxL7QyI/P/sCBoHfJ6cwggGcBgwrBgEEAY9bAoJ4AQMEggGKMIIBhgIBADCB/AIBAgYNKwYBBAGPWwKCeAIBAzCB5wYOKwYBBAGPWwKCeAIBAwEEgdR7ImFwcElkIjoiY29tLmV4YW1wbGUubXlhcHBsaWNhdGlvbl9CS3BOWWR2UU0yYkNLYklwRERuWmdkdGNYdEtnZUg5M2FwVm1aOWdpcTFoeUt2elNzVVNFZTFsT3VsK3N2bXhZS2ltb0dNWnF0U0o3eGxpRkVZd2NRK0E9IiwiYnVuZGxlTmFtZSI6ImNvbS5leGFtcGxlLm15YXBwbGljYXRpb24iLCJhcHBJZGVudGlmaWVyIjoiMTU3MzU0NjgiLCJhcHBNb2RlIjoiZGVidWcifTAiAgEABg0rBgEEAY9bAoJ4AgEEBA5jaGFsbGVuZ2VfZGF0YTAYAgEDBg0rBgEEAY9bAoJ4AgEFBAQCAAAAMB0CAQIGDisGAQQBj1sCgngCAgQIDAhDTFMtQUwwMDAlAgEDBg4rBgEEAY9bAoJ4AgICBgQQKMT7SUSv7BG5CQJCrBIAAjAKBggqhkjOPQQDAgNJADBGAiEAko1y6sf7Fg48oWZC8FoP5WtmzKiVk5AOOvuhwaK0CQcCIQD8HymOzkzmOOjUuz/rdVrTM4191dpGr3jfU1u5rBpNIw==\\n-----END CERTIFICATE-----", "-----BEGIN CERTIFICATE-----\\nMIICyjCCAlCgAwIBAgIREj5jzbLehL8yzkDm5uwcSJUwCgYIKoZIzj0EAwMwSzETMBEGA1UEChMKSHVhd2VpIENCRzE0MDIGA1UEAxMrSHVhd2VpIENCRyBFQ0MgRGV2aWNlIEF0dGVzdGF0aW9uIFJvb3QgQ0EgMTAeFw0yMzEyMDUwMzE4MDRaFw0zMzEyMDUwMzE4MDRaMF0xOTA3BgNVBAMMMEh1YXdlaSBDQkcgRUNDIERldmljZSBBbm9ueW1vdXMgQXR0ZXN0YXRpb24gQ0EgMTETMBEGA1UECgwKSHVhd2VpIENCRzELMAkGA1UEBhMCQ04wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATYjeQrfijuZ/9HJPLlsfJ4/wnXbQXaxy5f5fEcMN+pTZ5RekpY7PnDp2zEdibvkSzjv1MuRs8JzORyGatSOrYFo4IBATCB/jAfBgNVHSMEGDAWgBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAdBgNVHQ4EFgQU4yzL/3aHOxL7QyI/P/sCBoHfJ6cwRgYDVR0gBD8wPTA7BgRVHSAAMDMwMQYIKwYBBQUHAgEWJWh0dHA6Ly9wa2kuY29uc3VtZXIuaHVhd2VpLmNvbS9jYS9jcHMwEgYDVR0TAQH/BAgwBgEB/wIBATAOBgNVHQ8BAf8EBAMCAQYwUAYDVR0fBEkwRzBFoEOgQYY/aHR0cDovL3BraS5jb25zdW1lci5odWF3ZWkuY29tL2NhL2NybC9yb290X2RldmljZUF0dGVzdF9jcmwuY3JsMAoGCCqGSM49BAMDA2gAMGUCMQCE9qqNREq3AvCuznKeBl8biwC5GpV/Z1B0rsU4RqeTqNJ0Gvyz3g8Noaf4SpWzsLUCMBm5nr39UEOq89kx7QQjgYWLEWKcuSsgw2/6MckKP/6zrxjVld2SMtqiphKnrv1EkA==\\n-----END CERTIFICATE-----","-----BEGIN CERTIFICATE-----\\nMIICCTCCAY6gAwIBAgIDVxAsMAoGCCqGSM49BAMDMEsxEzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwIBcNMjMxMTMwMDIwNjU1WhgPMjA3MzExMzAwMjA2NTVaMEsxEzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAATDJzRdruaBeMoQBbdqCe51ezvkQn3OPYBoRmpL5KPktdFtD0b97FRp8jGLiUhPKyo8M15fxW5Ams4s80E8I1BSXoovDnkKllFfUadD8URgwEfOk5qttYNKzJcULavOhbijQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAKBggqhkjOPQQDAwNpADBmAjEA2zDQREvORPqcZyjwKDltu0T9zN8Cd3/hi4DQZvuRJdJOY57yIIO/LKxezzEcGiMMAjEAkX7r0U4Mcaw4uURMh+7tLMyvyxnlW8yJqBEOnZfqS8I8t0bQIY2r/5TQAPC0JhBm\\n-----END CERTIFICATE-----"};

    // Root CA certificate downloaded from the HarmonyOS official website.
    static String g\_rootCertStr = "-----BEGIN CERTIFICATE-----\\n" +
            "MIICCTCCAY6gAwIBAgIDVxAsMAoGCCqGSM49BAMDMEsxEzARBgNVBAoTCkh1YXdl\\n" +
            "aSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERldmljZSBBdHRlc3RhdGlv\\n" +
            "biBSb290IENBIDEwIBcNMjMxMTMwMDIwNjU1WhgPMjA3MzExMzAwMjA2NTVaMEsx\\n" +
            "EzARBgNVBAoTCkh1YXdlaSBDQkcxNDAyBgNVBAMTK0h1YXdlaSBDQkcgRUNDIERl\\n" +
            "dmljZSBBdHRlc3RhdGlvbiBSb290IENBIDEwdjAQBgcqhkjOPQIBBgUrgQQAIgNi\\n" +
            "AATDJzRdruaBeMoQBbdqCe51ezvkQn3OPYBoRmpL5KPktdFtD0b97FRp8jGLiUhP\\n" +
            "Kyo8M15fxW5Ams4s80E8I1BSXoovDnkKllFfUadD8URgwEfOk5qttYNKzJcULavO\\n" +
            "hbijQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQW\\n" +
            "BBTaRGLD5yvof1E6XEuPQ3w5JMPOrDAKBggqhkjOPQQDAwNpADBmAjEA2zDQREvO\\n" +
            "RPqcZyjwKDltu0T9zN8Cd3/hi4DQZvuRJdJOY57yIIO/LKxezzEcGiMMAjEAkX7r\\n" +
            "0U4Mcaw4uURMh+7tLMyvyxnlW8yJqBEOnZfqS8I8t0bQIY2r/5TQAPC0JhBm\\n" +
            "-----END CERTIFICATE-----\\n";

    // Name of the file for storing the certificate public key generated by the HarmonyOS HAP application.
    static String g\_publicKeyFileName = "d:\\\\attestPublicKey.pem";

    public static void main(String\[\] args) {
        ParseAttestation parseAttestation = new ParseAttestation();
        parseAttestation.parseAndValidateAttestCertChain(g\_attestCertStr, g\_rootCertStr, g\_publicKeyFileName);
    }

    void parseAndValidateAttestCertChain(String\[\] attestCertStr, String rootCertStr, String publicKeyFileName) {
        try {
            // Parse the key attestation certificate chain.
            List<X509Certificate> attestCerts = parseAttestationCerts(attestCertStr);
            // Verify the key attestation certificate chain.
            Date curDate = new Date();
            validateAttestationCertChain(attestCerts, rootCertStr, curDate);
            // Parse the key attestation certificate.
            AttestationInfo attestInfo = extractAttestaionField(attestCerts.get(0));
            // Check whether the key attestation information is correct.
            if (!checkAttestInfo(attestInfo)) {
                // TODO: Handle exceptions.
            }
            // Save the public key generated by the HarmonyOS HAP application.
            saveAttestPublicKey(attestInfo.publicKey, publicKeyFileName);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    List<X509Certificate> parseAttestationCerts(String\[\] certStr) throws Exception {
        List<X509Certificate> certificateList = new ArrayList<>(certStr.length);
        CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509", "BC");
        for (int i = 0; i < certStr.length; i++) {
            certificateList.add((X509Certificate) certificateFactory.generateCertificate(
                    new ByteArrayInputStream(certStr\[i\].getBytes())));
        }
        return certificateList;
    }

    void validateAttestationCertChain(List<X509Certificate> certs, String trustCAStr, Date date) throws Exception {
        // Construct a certificate chain.
        CertificateFactory factory = CertificateFactory.getInstance("X.509", "BC");
        CertPath certPath = factory.generateCertPath(certs);

        // Read the trust root certificate and construct a trustAnchor object.
        X509Certificate trustCA = (X509Certificate) factory.generateCertificate(
                new ByteArrayInputStream(trustCAStr.getBytes()));

        TrustAnchor trustAnchor = new TrustAnchor(trustCA, null);
        HashSet trustAnchorSet = new HashSet<TrustAnchor>();
        trustAnchorSet.add(trustAnchor);

        // Construct the validator and corresponding parameters.
        PKIXParameters params = new PKIXParameters(trustAnchorSet);
        params.setDate(date);
        // The key attestation certificate has a short validity period and does not require certificate revocation verification.
        params.setRevocationEnabled(false);

        CertPathValidator validator = CertPathValidator.getInstance("PKIX", "BC");
        try {
            PKIXCertPathValidatorResult result = (PKIXCertPathValidatorResult) validator.validate(certPath, params);
            System.out.println("Cert Chain validate success!");
        } catch (Exception e) {
            System.out.println("Cert Chain validate fail!" + e.getMessage());
        }
    }

    int getInteger(ASN1Encodable value) {
        if (value instanceof ASN1Integer) {
            return ((ASN1Integer) value).getValue().intValue();
        } else if (value instanceof ASN1Enumerated) {
            return ((ASN1Enumerated) value).getValue().intValue();
        } else {
            throw new IllegalArgumentException(
                    "expected Integer value ; found " + value.getClass().getName() + " instead.");
        }
    }

    byte\[\] getOctetString(ASN1Encodable value) {
        if (value instanceof ASN1OctetString) {
            return ((ASN1OctetString) value).getOctets();
        } else {
            throw new RuntimeException(
                    "expected OctetString value ; found " + value.getClass().getName() + " instead.");
        }
    }

    void printBytes(byte\[\] byteArray) {
	if (byteArray == null) {
	    System.out.println("null");
        }
        for (int i = 0; i < byteArray.length; i++) {
            System.out.printf("%02X ", byteArray\[i\]);
        }
        System.out.println();
    }

    AttestationInfo extractAttestaionField(X509Certificate certificate) {
        AttestationInfo attestInfo = new AttestationInfo();
        // Obtain the application public key.
        attestInfo.publicKey = certificate.getPublicKey();
        // Obtain the Extensions field from the key attestation certificate.
        byte\[\] attestationValue = certificate.getExtensionValue("1.3.6.1.4.1.2011.2.376.1.3");
        if (attestationValue == null || attestationValue.length == 0) {
            throw new IllegalArgumentException("Cann't found the attestation extension!");
        }
        ASN1Sequence attestSequence = ASN1Sequence.getInstance(
                ASN1OctetString.getInstance(attestationValue).getOctets());

        // Obtain the attestation version.
        attestInfo.version = getInteger(attestSequence.getObjectAt(0));

        for (int i = 1; i < attestSequence.size(); i++) {
            ASN1Sequence attestClaim = ASN1Sequence.getInstance(attestSequence.getObjectAt(i));
            // Obtain the claim OID.
            ASN1ObjectIdentifier attestClaimOid = (ASN1ObjectIdentifier) attestClaim.getObjectAt(1);
            if ("1.3.6.1.4.1.2011.2.376.2.1.4".equalsIgnoreCase(attestClaimOid.getId())) {
                // Read the challenge.
                attestInfo.challenge = getOctetString(attestClaim.getObjectAt(2));
            } else if ("1.3.6.1.4.1.2011.2.376.2.1.3".equalsIgnoreCase(attestClaimOid.getId())) {
                // Read appInfo.
                ASN1Sequence appInfoAsn1 = (ASN1Sequence) attestClaim.getObjectAt(2);
                // Obtain the OID of appInfo.
                ASN1ObjectIdentifier appidOid = (ASN1ObjectIdentifier) appInfoAsn1.getObjectAt(0);
                if (!"1.3.6.1.4.1.2011.2.376.2.1.3.1".equalsIgnoreCase(appidOid.getId())) {
                    continue;
                }
                // Read the HAP application information.
                String appInfo = new String(getOctetString(appInfoAsn1.getObjectAt(1)));
                System.out.println("appInfo is:\\n" + appInfo);
                attestInfo.appInfo = JSON.parseObject(appInfo, AppInfo.class);
            } else if ("1.3.6.1.4.1.2011.2.376.2.2.2.6".equalsIgnoreCase(attestClaimOid.getId())) {
                // Read the key management component ID. The correct value is 0x28c4fb4944afec11b9090242ac120002.
                attestInfo.keyManagerId = getOctetString(attestClaim.getObjectAt(2));
            } else if ("1.3.6.1.4.1.2011.2.376.2.2.4.8".equalsIgnoreCase(attestClaimOid.getId())) {
                // Read the device model.
                attestInfo.model = attestClaim.getObjectAt(2).toString();
            }
        }
        return attestInfo;
    }

    boolean checkAttestInfo(AttestationInfo attestInfo) {
        // TODO: Verify the challenge.
        System.out.println("challenge is:");
        printBytes(attestInfo.challenge);

        // TODO: Verify the information in appInfo.
        System.out.println("appInfo.appId is:\\n" + attestInfo.appInfo.appId);
        System.out.println("appInfo.bundleName is:\\n" + attestInfo.appInfo.bundleName);
        System.out.println("appInfo.appIdentifier is:\\n" + attestInfo.appInfo.appIdentifier);
        System.out.println("appInfo.appMode is:\\n" + attestInfo.appInfo.appMode);

        // TODO: Verify keyManagerId. The value must be 0x28c4fb4944afec11b9090242ac120002.
        System.out.println("key manager id is:");
        printBytes(attestInfo.keyManagerId);

        return true;
    }

    void saveAttestPublicKey(PublicKey publicKey, String publicKeyFileName) throws Exception {
        // TODO: Save attestInfo.publicKey.getEncoded() to database.
        FileOutputStream file = new FileOutputStream(publicKeyFileName);
        file.write(publicKey.getEncoded());
        file.close();
        System.out.println("the app public key: \\n" + publicKey);
    }

    class AttestationInfo {
        public PublicKey publicKey;
        public int version;
        public byte\[\] challenge;
        public AppInfo appInfo;
        public byte\[\] keyManagerId;
        public String model;
    }

    static class AppInfo {
        public String appId;
        public String bundleName;
        public String appIdentifier;
        public String appMode;
    }
}

#### Saving the Public Key to the Database

After verifying the key attestation certificate chain, the application server saves the application public key contained in the key attestation certificate to the server database. For details about the sample code, see the sample code in "Verifying the Key Attestation Certificate Chain." The public key can be used to verify service requests. Before saving the application public key, ensure that the public key is unique. The system cannot have identical public keys.

**For security purposes, generate a unique key pair for each user who logs in to the device, and store the mappings between each user and the public key of the application in the application server for the applications involved user logins.**

**Implementation note**: Before verifying the signature of a service request, you need to find the application public key. You are advised to calculate the ID of the application public key (for example, calculate the hash for the application public key), store the relationship between the key ID and the application public key, and search for the application public key based on the key ID.

#### Verifying the Service Request Signature Using the Application Public Key

The application server first verifies the challenge value, and locates the application public key based on the key ID.

**If your application requires user login and the user IDs are associated with application public keys, locate the public key based on the public key ID and the user ID.**

Then, the application server uses the application public key to verify the signature in the request.

**Sample code:**

import org.bouncycastle.jce.provider.BouncyCastleProvider;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.PublicKey;
import java.security.Security;
import java.security.Signature;
import java.security.SignatureException;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

public class VerifySignature {
    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    // Name of the file for storing the certificate public key generated by the HarmonyOS HAP application.
    static String g\_publicKeyFileName = "d:\\\\attestPublicKey.pem";
    // Base64-encoded signature data generated by the HarmonyOS HAP application using the private key.
    static String g\_signedData = "MEUCIQDtlrQa7HQccprCkR0nWTL7N6HEKY9PKN3DTk3aeN0/fQIgeqTrQ+7exiJhwTY3LwT7XhRHV1emOfTYho5qxyektho=";
    // Data to be signed.
    static String g\_plaintext = "123456";
    // Signing algorithm, which must be the same as the algorithm used by the application. Example values: SM3WITHSM2 and SHA256withECDSA.
    static String g\_signAlg = "SHA256withECDSA";

    public static void main(String\[\] args) {
        VerifySignature verifySignature = new VerifySignature();
        verifySignature.verifySignature(g\_publicKeyFileName, g\_plaintext, g\_signedData, g\_signAlg);
    }

    void verifySignature(String publicKeyFile, String plainText, String signedData, String signAlg) {
        try {
            PublicKey publicKey = readAttestPublicKey(publicKeyFile);
            byte\[\] signedDataByte = Base64.getDecoder().decode(signedData);
            System.out.println("signedDataByte len=" + signedDataByte.length);
            printBytes(signedDataByte);
            byte\[\] plainTextBytes = plainText.getBytes();
            System.out.println("plainTextBytes len=" + plainTextBytes.length);
            printBytes(plainTextBytes);
            boolean result = doVerify(publicKey, plainTextBytes, signedDataByte, signAlg);
            System.out.println("Verify signature result: " + result);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    PublicKey readAttestPublicKey(String publicKeyFileName) throws Exception {
        // TODO: Read the attestation public key from database.
        KeyFactory keyFactory = KeyFactory.getInstance("EC", "BC");
        X509EncodedKeySpec spec = new X509EncodedKeySpec(readFromFile(publicKeyFileName));
        PublicKey publicKey = keyFactory.generatePublic(spec);
        System.out.println("the app public key: \\n" + publicKey);
        return publicKey;
    }

    byte\[\] readFromFile(String fn) throws Exception {
        FileInputStream inputStream = new FileInputStream(fn);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        byte\[\] bytes = new byte\[1024\];
        int len;
        do {
            len = inputStream.read(bytes);
            outputStream.write(bytes, 0, len);
        } while (bytes.length == len);
        inputStream.close();
        return outputStream.toByteArray();
    }

    boolean doVerify(PublicKey publickey, byte\[\] unsignedData, byte\[\] signedData, String signAlg) {
        boolean verifyResult = false;
        try {
            Signature signature = Signature.getInstance(signAlg, "BC");
            signature.initVerify(publickey);
            signature.update(unsignedData);
            verifyResult = signature.verify(signedData);
            return verifyResult;
        } catch (NoSuchAlgorithmException | NoSuchProviderException | InvalidKeyException | SignatureException e) {
            e.printStackTrace();
        }
        return verifyResult;
    }

    void printBytes(byte\[\] byteArray) {
        for (int i = 0; i < byteArray.length; i++) {
            System.out.printf("%02X ", byteArray\[i\]);
        }
        System.out.println();
    }
}
