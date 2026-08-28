# Verifying the Signature in the Returned Result

#### Function

The IAP server API response and server-side key event notifications are returned in JWS format. JWS is primarily used to ensure the integrity of data by verifying that it has not been altered during transmission.

#### JWS Structure

JWS consists of three parts:

1.  Header
2.  Payload
3.  Signature

The three parts are individually Base64 encoded before transmission.

Header after decoding:

| 
Parameter

 | 

Mandatory

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

alg

 | 

Yes

 | 

String

 | 

Algorithm type. The value is always **ES256**.

 |
| 

typ

 | 

Yes

 | 

String

 | 

The value is always **JWT**.

 |
| 

x5c

 | 

Yes

 | 

String

 | 

X.509 certificate chain, in the order of leaf certificate, intermediate certificate, and root certificate.

 |

#### JWS Decoding and Signature Verification

1.  Parse the JWS to obtain the header, payload, and signature.
2.  Obtain the certificate chain (leaf certificate, intermediate certificate, and root certificate in sequence) from **x5c** in the header and use the [Huawei CBG Root CA G2](https://pki.consumer.huawei.com/ca/cer/RootCaG2Ecdsa.cer) certificate to verify the certificate chain.
3.  Verify the leaf certificate OID **1.3.6.1.4.1.2011.2.415.1.1**.
4.  If the certificate verification is successful, the public key will be obtained from the leaf certificate.
5.  The algorithm specified in the header and public key is used for JWT signature verification through various open-source libraries at [jwt.io](https://jwt.io/).

#### Sample Code

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/UkCYSen-Qj6YnMT3tZzTRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062509Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E3561B6AFBC448872D0F6221EFFB38088B870A4FE626870512C77DF5BD19910)

The following sample code uses Java as an example. You can view the sample code of Python, PHP, JavaScript, and Golang by switching the code branch in **[IAP Kit-Sample-ServerDemo](https://gitcode.com/HarmonyOS_Samples/iapkit-sample-serverdemo/blob/Java/README_en.md)**.

**Java**
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.DecodedJWT;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.PublicKey;
import java.security.cert.CertPath;
import java.security.cert.CertPathValidator;
import java.security.cert.CertPathValidatorException;
import java.security.cert.Certificate;
import java.security.cert.CertificateFactory;
import java.security.cert.PKIXCertPathValidatorResult;
import java.security.cert.PKIXParameters;
import java.security.cert.TrustAnchor;
import java.security.cert.X509Certificate;
import java.security.interfaces.ECPublicKey;
import java.util.Base64;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class JWSChecker {
    private static final String CA\_CERT\_FILE\_PATH = "/path/to/cer/RootCaG2Ecdsa.cer";// TODO: Need to replace it with the actual value, please refer to [Huawei CBG Root CA G2](https://pki.consumer.huawei.com/ca/cer/RootCaG2Ecdsa.cer). 

    /\*\*
     \* JWS HEADER PARAM X5C: Indicates the X.509 certificate chain. The sequence is leaf certificate, intermediate certificate, and root certificate.
     \*/
    private static final String HEADER\_PARAM\_X5C = "x5c";

    private static final int X5C\_CHAIN\_LENGTH = 3;

    /\*\*
\* JWS HEADER PARAM ALG: Algorithm type. The value is always ES256.
     \*/
    private static final String HEADER\_PARAM\_ALG\_ES256 = "ES256";

    private static final String LEAF\_CERT\_OID = "1.3.6.1.4.1.2011.2.415.1.1";

    /\*\*
     \* Used to verify JWS and decode the payload.
     \* @param jwsStr JWS string
     \* @return payload string
     \* @throws Exception exception
     \*/
    public static String checkAndDecodeJWS(String jwsStr) throws Exception {
        if (jwsStr == null || jwsStr.isEmpty()) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception("jwsStr was null");
        }
        DecodedJWT decodedJWT = JWT.decode(jwsStr);
        if (!HEADER\_PARAM\_ALG\_ES256.equals(decodedJWT.getAlgorithm())) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception("alg must be ES256");
        }
        String\[\] x5cChain = decodedJWT.getHeaderClaim(HEADER\_PARAM\_X5C).asArray(String.class);
        if (x5cChain == null) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception("x5c chain was null");
        }
        // Verify the x5c certificate chain and obtain the public key.
        PublicKey publicKey = verifyChainAndGetPubKey(x5cChain);
        // Use the public key to verify the signature of the jws.
        JWTVerifier jwtVerifier = JWT.require(Algorithm.ECDSA256((ECPublicKey) publicKey)).build();
        jwtVerifier.verify(decodedJWT);
        // Decode and return the payload.
        return new String(Base64.getUrlDecoder().decode(decodedJWT.getPayload()), StandardCharsets.UTF\_8);
    }
    private static PublicKey verifyChainAndGetPubKey(String\[\] certificates) throws Exception {
        CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
        List<Certificate> certificateList = new LinkedList<>();
        for (String certificate : certificates) {
            InputStream inputStream = new ByteArrayInputStream(Base64.getDecoder().decode(certificate));
            certificateList.add(certificateFactory.generateCertificate(inputStream));
        }
        if (certificateList.size() != X5C\_CHAIN\_LENGTH) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception("invalid cert chain length");
        }
        PKIXCertPathValidatorResult certPathValidatorResult;
        try {
            PKIXParameters parameters = loadRootCAAndPKIX();
            CertPathValidator validator = CertPathValidator.getInstance("PKIX");
            
            // TODO: Need to do crl check if not ignore CRL
            parameters.setRevocationEnabled(false);
            CertPath certPath = certificateFactory.generateCertPath(certificateList.subList(0, X5C\_CHAIN\_LENGTH - 1));
            certPathValidatorResult = (PKIXCertPathValidatorResult) validator.validate(certPath, parameters);
        } catch (Exception e) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception(e);
        }
        Certificate iapCert = certificateList.get(0);
        if (!(iapCert instanceof X509Certificate)) {
            // TODO: Need to replace it with the actual business logic.
            throw new Exception("leaf certificate must be X509 format");
        }
        X509Certificate x509Certificate = (X509Certificate) iapCert;
        if (x509Certificate.getNonCriticalExtensionOIDs() == null ||
            !x509Certificate.getNonCriticalExtensionOIDs().contains(LEAF\_CERT\_OID)) {
            // TODO: Need to replace it with the actual business logic.
            throw new CertPathValidatorException("OID not found");
        }
        return certPathValidatorResult.getPublicKey();
    }
    private static PKIXParameters loadRootCAAndPKIX() throws Exception {
        PKIXParameters parameters;
        // TODO: Under Java 8, Need to close the resource in the finally block.
        try (InputStream fis = Files.newInputStream(Paths.get(CA\_CERT\_FILE\_PATH))) {
            CertificateFactory certificateFactory = CertificateFactory.getInstance("X.509");
            Certificate trustCert = certificateFactory.generateCertificate(fis);
            if (!(trustCert instanceof X509Certificate)) {
                // TODO: Need to replace it with the actual business logic.
                throw new RuntimeException("root certificate must be X509 format");
            }
            Set<TrustAnchor> trustAnchors = new HashSet<>();
            trustAnchors.add(new TrustAnchor((X509Certificate) trustCert, null));
            parameters = new PKIXParameters(trustAnchors);
        }
        return parameters;
    }
}

POM file:

<dependency>
    <groupId>com.auth0</groupId>
    <artifactId>java-jwt</artifactId>
    <version>4.4.0</version>
</dependency>
