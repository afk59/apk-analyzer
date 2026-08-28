# Verifying the Anonymous Certificate Chain

To prevent third parties from forging data, a device and the cloud must verify the anonymous certificate chain before verifying a data signature. For details about the API for on-device verification of the anonymous certificate chain, please refer to [Certificate Chain Validator Development](../../../../device-certificate-kit/certificate-framework/certificate-chain-validator-development/document.md). For details about the API for cloud-side verification of the anonymous certificate chain, please refer to [Device Authenticity Attestation](../../../../universal-keystore-kit/local-key-management/device-attestation/document.md).

The anonymous certificate chain returned during the attestation session initialization contains three levels of certificates. The verification procedure is as follows:

1.  Use the root CA certificate provided by the [Universal Keystore Kit](../../../../universal-keystore-kit/about-this-kit/document.md) official website to verify the validity of the anonymous certificate chain. ([Click here to download the root CA certificate](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer).)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/Z-hu8acMSc6esJBeZ_TkKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7118FBF81FF96D08C3CBD2285A005907C99C5F5E1CFF2E137D26608900546FE)
    
    Do not use the subordinate CA certificate to verify the key attestation certificate chain on the app server. The subordinate CA certificate may change due to expiration or certificate revocation.
    
2.  Parse the level-3 certificate to obtain the app public key, value of **AppID**, and key management component ID.
    
    1.  Obtain the app public key from the **subjectPublicKeyInfo** field in the key attestation certificate.
    2.  Obtain the value of **AppID** from the extended field **1.3.6.1.4.1.2011.2.376.2.1.3.1**.
    3.  Obtain the key management component ID from the extended field **1.3.6.1.4.1.2011.2.376.2.2.2.6**.
    
3.  Check whether the values of the extended fields in the level-3 certificate are correct.
    
    1.  The key management component ID should be **0E01669E9CFF3848A9538568F1A483E3**.
    2.  The value of **AppID** should be the ID of the app that calls the attestation key creation API.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/GFP51PzDStuMegkRcBiWOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062006Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2334E9F8B450D615520D2EF37D24AC5C147A7B7D93223F700B269CE42BE92A38)
    
    The **AppID** field indicates the ID of a HarmonyOS app, including the value of **bundleName** and the hash value of the public key of the signing certificate. For details about how to obtain the **AppID**, please refer to [bundleManager Module](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself-1).
