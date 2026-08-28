# What should I do if the keystore file is incompatible with the JDK version?

**Symptom**

The error message "init keystore failed: parseAlgParameters failed:ObjectIdentifier()" is displayed during packaging and signing.

**Possible Causes**

The keystore file is generated using a later JDK version, but the signing is performed using an earlier JDK version. As a result, the keystore file cannot be parsed due to compatibility issues, and the signing fails.

**Common Error Scenarios**

1.  DevEco Studio automatically generates a keystore file (**\*.p12**) using its preset JDK. However, the user uses a local JDK of an earlier version for signing. As a result, the signing fails.
2.  The user uses a local JDK of a later version to generate a keystore file (\*.p12), but uses DevEco Studio for packaging and signing. The preset JDK version in DevEco Studio is earlier than the user's JDK version. As a result, the signing fails.

**Solution**

Check the JDK version in use and the JDK version used to generate the keystore file to ensure that they match. To check the JDK version, perform the following steps:

1.  Run the **java -version** command in the **Terminal** tab of DevEco Studio to view its preset JDK version. In this example, the preset JDK version in DevEco Studio is 21.0.6.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/oI37aND3RIOZIyz71a9szQ/en-us_image_0000002422340574.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A78F7D335A1BD2837FC9FDC31EE3A583D6B54B7531B1FBE7B8EDB555F322C8D9)
    
2.  Run the **java -version** command in the CMD window to view the JDK version in the local system. In this example, the JDK version in the local system is 1.8.0\_292, which is different from the preset JDK version in DevEco Studio in step 1.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/9eI1GSejTCO1NMSb1-pIVQ/en-us_image_0000002342518430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F70979C7E2CAC837D1FC6A2C2FDFF09C4A9AFFFFD0E7609A3439100015204999)
