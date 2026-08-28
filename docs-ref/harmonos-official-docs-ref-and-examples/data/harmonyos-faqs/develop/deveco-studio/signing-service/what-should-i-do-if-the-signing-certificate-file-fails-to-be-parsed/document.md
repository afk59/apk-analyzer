# What should I do if the signing certificate file fails to be parsed?

**Symptom**

The error message "DerValue.getOID, not an OID 49 Detail: Please check the message from tools" is displayed during packaging and signing.

**Possible Causes**

The parsing failure may be caused by a non-standard certificate file or damaged certificate file.

**Common Error Scenarios**

An incorrect certificate file is configured in **Certpath file**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/OUhVhljdQ8Kf-cuzed0D6A/en-us_image_0000002342518434.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BE95A1C5091C70A5C86E3C055B2949D6FAC9622D6773748E6B1FEAAD8CA24F0)

**Solution**

Check whether the certificate file configured in **Certpath file** is a standard certificate file as follows:

Run the **keytool -printcert -file ${Certpath file}** command in the **Terminal** window of DevEco Studio.

-   Correct certificate file format

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/MXGW1BCiR4qVoDJHGK5WfA/en-us_image_0000002376516257.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A79781002CB04ECC882D45B0E21C5F9CCA27F7DC851A0B32BBBB19957CE9929)

-   Incorrect certificate file format

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/_hxoFVBYSdKrhFJIfdyg9w/en-us_image_0000002376396377.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=503D1E67DB0AA344AC1851BEE1E13D5332DFC3E02AA950150601666AD1056C0A)
