# What should I do if "keystore password was incorrect" is reported during compilation?

**Symptom**

"ERROR - hap-sign-tool: error: ACCESS\_ERROR, code: 109. Details: Init keystore failed: keystore password was incorrect" is reported during compilation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/trqHJRuRRwCPZlWNesh3PQ/en-us_image_0000002229603737.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D664F6A81CB43EA878621B695C47F1DBF0A745640B0FB9825884916FA94B2B81)

**Possible Causes**

The keystore (.p12) password is incorrect. The signature password in the signature file is incorrect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/a0yUEo7ZRkmYx5D2_KX-qw/en-us_image_0000002436501498.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=769DC1234379C1B6D99B876DC0DC5EF43D842AF9C42EF524252DC1DE0C672C5B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ijB-evm0QJSJSkbQRWZ-ng/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D157CA772740373A648A70E6189275EFD7B4CAFD8B6E099BBA9E33619397195B)

**storePassword** and **keyPassword** are customized when the .p12 file is created. It is important to remember these passwords. The **build-profile.json5** file records the passwords in ciphertexts, but the signing tool requires plaintext passwords. This means the ciphertext values in the **build-profile.json5** file cannot be used directly in signing.

**Common Scenarios**

1.  The entered password is incorrect.
2.  The ciphertext is entered on the command line.
3.  The **keyAlias** password is obfuscated with the keystore (.p12) password.

**Solution**

Resolve this issue by performing the following operations:

1\. Choose **File** > **Project Structure** > **Project** > **Signing Configs**.

2\. Select **Automatically generate signature** (for a HarmonyOS project, select **Support HarmonyOS** as well), wait for the re-signing, and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Rdc7SL3mTDCEYyz91YOGqQ/en-us_image_0000002229758209.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A49A9CD9850BA55A3246D0D2817297BF2579BD5679BA8FD3265038A37441CA7)
