# Requesting a Restricted ACL Permission

1\. Before [requesting a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) and [requesting a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090), request corresponding ACL permissions.

2\. Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/), click **Development and services**, and find and click the desired project in the project list. Click the app for which you need to request ACL permissions. On the **Project settings** page, click the **ACL permissions** tab, and request ACL permissions for your app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Nm1C0i_BS2m0KnUPT8aZQg/en-us_image_0000002504465239.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8548AA91502A909C35F95B57B13C8E56DF32680A44FF541DDC7D64FD3F30B821 "Click to enlarge")

3\. Read the precautions carefully and then select **I have read the above notes** in the **Permissions not obtained** section. Enter **ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD** in the search box, select this permission from the search result, and request it.

4\. Enter the request reason based on your business requirements and submit the request. You will receive a reply within one working day.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/O9j4Oi2eRPyqBaru9F7kmA/en-us_image_0000002504465243.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B99214F6A86C3F0BBD63F61D50A5B65950E991FA36BC2541581DF00551782F0 "Click to enlarge")

5\. When requesting a profile after your permission request is approved, select **Restricted ACL permissions (HarmonyOS API 9 or later)** for **Permissions to request**, and click **Select**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/FZjXgVq9Q1q94Yss4sQZjA/en-us_image_0000002504465245.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BC613A399636E938BC66AF77DF1FC494BCA4C06D7F22DBA298CE17586C51D64)

6\. In the displayed **Select restricted ACL permission** window, select the obtained permission, and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/AcBkUL37TNi0FLd3qbaS4w/en-us_image_0000002471625310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062120Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C63B4F634BEAEABBEA390678F2A8E673E92D865E1D3C4310CA5BD894FEE53040 "Click to enlarge")

7\. Select the permission and click **Add** to generate a new profile. Download the profile. When [manually configuring signing information](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), select this profile for use.

8\. Add the **ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD** permission to the **module.json5** file of the **entry** module in your project.

"requestPermissions": \[{
  "name": "ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"
}\]
