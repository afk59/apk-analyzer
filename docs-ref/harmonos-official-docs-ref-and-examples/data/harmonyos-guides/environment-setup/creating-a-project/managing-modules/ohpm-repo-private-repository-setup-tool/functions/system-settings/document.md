# System Settings

**System setting** is used to manage the ohpm-repo system. Currently, the **oh-package.json5 validation rule** and **System safety** functions are supported.

#### oh-package.json5 Validation Rule

**oh-package.json5 validation rule** is used by ohpm-repo to verify the **oh-package.json5** file of the uploaded package. Currently, rules are set for the **category**, **repository**, and **name** fields.

**Whitelist of category**: If this parameter is left empty, the system does not verify the **category** field. If this parameter is set, the value of category must exist in the whitelist.

**Is repository required**: determines whether the **repository** field is mandatory in the **oh-package.json5** file. If this parameter is set to **Yes**, the **oh-package.json5** file must contain the **repository** field when the package is uploaded.

**Whether the name field must contain the organization**: indicates whether the **name** field in the **oh-package.json5** file must contain the organization name. If this parameter is set to **Yes**, the **name** field must contain an organization name when a package is uploaded. Otherwise, the package uploading fails.

The following figure shows the page effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/1g_7YiUGTX-XPUi4mdhbig/en-us_image_0000002501068660.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A5DECECA19B8694674B2CF70BEA56D0195AB23B32AE77AC5EA0AF48DACE1C260 "Click to enlarge")

#### System Safety

On the **System safety** page, you can reset system password and configure whether to support anonymous access, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/16xblVetQjiXohDHE9Xw8g/en-us_image_0000002500908818.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2E22E6679A06CA9DF37B41CF54C2022CC24F6D0952DF53A9306E21CC914FC39 "Click to enlarge")

1.  Resetting the System Password
    
    The system password is used to re-encrypt the public key uploaded by the user in the ohpm-repo service and the network proxy password of uplinks. The system password cannot be reset when ohpm-repo is deployed across multiple instances. Click **Reset system password**. A message is displayed for you to confirm the resetting. Click **Yes**, and the password text box is displayed, as shown in the following figure. You need to enter the password of the current login account for authentication because resetting the system password is a sensitive operation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/XqKpG-8DQ9mtNYS3STV7tA/en-us_image_0000002504296812.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=618A2D0B848A60CB90E3AF2BEB6331A6E02C2E2D4B19D13C569A2726EC775DA0 "Click to enlarge")
    
2.  Configuring Anonymous Access
    
    ohpm-repo 5.0.5 and later versions support anonymous access. By default, anonymous access is enabled. To disable anonymous access, click **No** under **Support anonymous access** and then click **Submit**, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/a3mu45cCRvyBwQHWnVFrHw/en-us_image_0000002504136980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D99E04AA5B5F2EFBDCC16EE997A037CFE414DA55CC30F86312A9F7DEF64649E "Click to enlarge")
    
    -   When anonymous access is disabled, users can access the package list page and package details page from the ohpm-repo management home page only after logging in. In addition, the home page does not provide a user registration option and displays only the login entry.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/FmFmkwrdR_mgZ_LO-kzBbw/en-us_image_0000002536096795.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062138Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68AF00E6BD23C7BA6D8A3E4E596823D02A9796DFF4638C59A194E7E26BB1B6D6 "Click to enlarge")
        
    -   When anonymous access is disabled, if the AccessToken authentication information is not correctly configured in the **.ohpmrc** file, ohpm does not have permission to execute the **install**, **info**, and **update** commands that require the read permission. The read-write or read-only AccessToken authentication information must be correctly configured in the **.ohpmrc** file.
    -   When anonymous access is disabled, if the [authentication plugin](../../appendix/authentication-plug-in-customization/document.md) template from a version earlier than ohpm-repo 5.0.5 is used, the authentication plugin must be upgraded by adding the **authWithReadOnly** method to implement read-only AccessToken authentication.
