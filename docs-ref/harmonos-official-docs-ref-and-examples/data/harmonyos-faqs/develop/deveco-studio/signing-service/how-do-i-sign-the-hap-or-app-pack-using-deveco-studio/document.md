# How do I sign the HAP or App Pack using DevEco Studio?

You can use the signing tool provided by DevEco Studio to sign the packaged HAP or App Pack. The procedure is as follows:

1.  Use DevEco Studio to generate a key and a CSR file. Then, apply for a release certificate and profile from the AppGallery Connect. For details, see [Preparing Signature Files](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-publish-app#section793484619307).
2.  Prepare the signing tool **hap\_sign\_tool.jar**, which is located in **${_DevEco Studio installation path_}/sdk/default/openharmony/toolchains/lib**.
3.  In the signing tool directory, run the following command. For details about the signing tool, see [hapsigner](https://gitcode.com/openharmony/developtools_hapsigner).
    
    java -jar hap-sign-tool.jar sign-app -keyAlias "D:\\test\_key" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "D:\\test.cer" -profileFile "D:\\test.p7b" -inFile "D:\\hap-unsigned.hap" -keystoreFile "D:\\test.p12" -outFile "D:\\hap-signed.hap" -keyPwd "123456Abc" -keystorePwd "123456Abc"
    
    In the preceding command, modify settings of the following parameters and keep the other parameters as they are:
    
    -   **keyAlias**: key alias.
    -   **appCertFile**: release certificate file in .cer format.
    -   **profileFile**: release profile file in .p7b format.
    -   **inFile**: HAP to sign.
    -   **keystoreFile**: keystore file in .p12 format.
    -   **outFile**: HAP that carries the signature information, to be generated after the signing.
    -   **keyPwd**: key password.
    -   **keystorePwd**: keystore password.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/iMbvCd3pQb2Ffunj2xWLFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9224678E6AB69D8D01D57E2E3C61B8FEE1E540A581BACB844AD3B70B62E52649)
    
    To sign an APP Pack, modify the **inFile** and **outFile** parameters in the preceding command to point to the APP Pack.
