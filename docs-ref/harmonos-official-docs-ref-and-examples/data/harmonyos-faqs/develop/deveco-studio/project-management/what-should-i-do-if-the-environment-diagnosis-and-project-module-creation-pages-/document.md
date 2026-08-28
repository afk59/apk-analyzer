# What should I do if the environment diagnosis and project/module creation pages are blank?

**Symptom**

The environment diagnosis window, the window for project or module template selection, or the project preview window is blank.

**Possible Causes**

These pages are rendered using JCEF. When JCEF fails to start, this problem occurs.

**Possible Cause 1**

The GPU compatibility of the JCEF window component is abnormal.

**Solution**

Disable GPU rendering of JCEF.

Resolve the GPU compatibility issue of the JCEF window component. Click the magnifier icon in the upper-right corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/UDNuJDS9TTqWDLmk44Eqzw/en-us_image_0000002327307086.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32996BE4B6F79427C39ACB5BB95AB5A044260CDA7A7FF0EC6185B5FF8FCF1E4A)

Enter **registry** and click **Registry...** under it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/mTfavsfZTMquP0eKJR73lw/en-us_image_0000002327147458.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F71C66CBCE5D76370D4578BC5C2A405C34284F148791762493BC99B509459EC)

Search for **gpu**, find **ide.browser.jcef.gpu.disable**, select it, and restart DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/jwZL7XVvSBe0hXOPLe9i_A/en-us_image_0000002361065777.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E4F0E8B2E1E7590A22593512246CA82E88C7A795C2608E75504CB03703ADE5B)

**Possible Cause 2**

IntelliJ IDEA is not authorized to start JCEF.

**Solution**

DevEco Studio may have insufficient permissions. In this case, find the DevEco Studio startup icon, right-click the icon, and choose **Properties** > **Compatibility**, select to run this program as an administrator, and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/UzMyCmuQTk6Cj5LMuqk9UQ/en-us_image_0000002327319882.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F2E909461808021AD0D3CB5ED87724E9DECE89368675C2D7A87E34C7734E893)

**Possible Cause 3**

The JCEF file is missing, which may be deleted by the antivirus software.

**Solution**

Check whether the JCEF file is missing.

If the JCEF file is missing, it may be deleted by the antivirus software. As a result, the JCEF process cannot be started. Check whether the two files exist. If they do not exist, reinstall the DevEco Studio.

${DevEco Studio installation directory}/jbr/bin/server/jvm.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Ql726i2xSZCoWF0AG-9uFQ/en-us_image_0000002327180308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A640678E21188C444927B86336A7203392947C2B1BC964594D48612FA8A0B886)

${DevEco Studio installation directory}/jbr/bin/chrome\_elf.dll

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/qMdvp3fJT0-msTe_gtkNgg/en-us_image_0000002327341312.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F47DCF1D2E949CCFB6C81772C7DE7BDCC642051940295F5E29DCD7F110429BD1 "Click to enlarge")

**Possible Cause 4**

The JCEF sandbox environment conflicts with the current computer environment.

**Solution**

The JCEF sandbox environment conflicts with the current computer environment. As a result, JCEF cannot work properly.

Click the magnifier icon in the upper-right corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/gLcZPBYnTiiydx-8hxHUaw/en-us_image_0000002361164509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FCC5975E24A71FDE04CD347EF8B9D997F8CE5F69F7178B4C537DDC50149F08BC)

Enter **registry** and click **Registry...** under it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WQYh92KYRiimRQHMRoVxJw/en-us_image_0000002361164813.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB6B1F13BB587B6F2EE8509639748BB37D4A87EBE1DB32FABC48C46D77269660)

Search for **sandbox**, find **ide.browser.jcef.sandbox.enable**, deselect it, and restart DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/vFcqYQrYQAeEGdbwFJoGWw/en-us_image_0000002361165633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062615Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CB9C645AC564761C959CB5AC6584444E35D1AD9398C068F886B09EECBBC5298)
