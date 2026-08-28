# What should I do if the signature verification fails?

**Symptom**

The error message "Verify Signature failed" is displayed during packaging and signing.

**Possible Causes**

The private key in the keystore file used for signing does not match the certificate. As a result, the tool fails to verify the signature.

**Scenario**

1\. In the packing and signing scenario, the public key in the certificate file does not match the private key corresponding to **keyalias** in the keystore file.

2\. In the package integrity verification scenario, the signed HAP file is tampered with.

**Solution**

Scenario 1: Check whether the configured certificate file matches the keystore file. Perform the following steps:

1\. Check the signature configuration.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/hllsj2YNQi2a-i5HH-ISSg/en-us_image_0000002342678238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C83F637A4080D262091EF3D77213AB5FE265FAB05EB2C49E0A41D5BB1293FB7F)

2\. View the certificate public key information (**SubjectKeyIdentifier**) associated with the signature key in the keystore file. For example, run the **keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}** command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/K9b5mYWsRiSlkAKLUctzfQ/en-us_image_0000002342518438.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA8E561F0FEFAA01289283F5890ED35A9E863F388A2D9ECB96651874C687451A)

3\. Check the public key information in the configured certificate file. The certificate applied for from AppGallery has the following information: **CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN**. For example, run the **keytool -printcert -file ${Certpath file}** command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/NChyrEQ9Q8-cYu0L9Q8YqA/en-us_image_0000002376516261.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16EFAB506EBF311244BA29A53792CE93AFCFEF7DB183902318A86A5927B81375)

If the public key information (**SubjectKeyIdentifier**) in step 2 does not match that in step 3, the configured certificate file does not match the keystore file.

Scenario 2: Repackage and resign.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/WBd0bgllQ_Oi7jQGu1wEFA/en-us_image_0000002376396381.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCF4B215F46D777BA639ED213EC428003681F4BC8E949B36FA16956C743DFDB0)
