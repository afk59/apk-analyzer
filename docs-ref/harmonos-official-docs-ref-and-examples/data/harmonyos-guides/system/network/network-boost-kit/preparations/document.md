# Preparations

#### Applying for Permissions

## Scenario

Before using Network Boost Kit capabilities, check whether you have applied for corresponding permissions for your app. If your app has not been granted some permissions, you need to declare these permissions.

Specifically, Network Boost Kit requires the following permission:

**ohos.permission.GET\_NETWORK\_INFO**: allows your app to request device network information.

**ohos.permission.INTERNET**: allows your app to access the Internet.

**ohos.permission.LINKTURBO**: allows your app to use the multi-network concurrency capability for network acceleration. APIs related to network handover require this permission. Request it only when necessary.

You must manually configure this permission before using Network Boost Kit capabilities. For details, please refer to the [procedure for applying for permissions](#section1648815561221).

The **ohos.permission.LINKTURBO** permission is a restricted ACL permission that requires special configuration and approval. For details, please refer to [Configuring Signing Information](#section94731428358) and [Requesting a Restricted ACL Permission](#section13192154213515).

## Procedure

Configure the permission in the **module.json5** file in **entry/src/main**. The sample code is as follows:

{
  "module": {
    "requestPermissions": \[
      {
        "name": "ohos.permission.GET\_NETWORK\_INFO"
      },
      {
        "name": "ohos.permission.INTERNET"
      },
      {
        "name": "ohos.permission.LINKTURBO"
      }
    \]
  }
}

## Preparations for C API Development

In addition to the aforementioned permission configuration, when using the C API, you also need to set the dynamic library path and header file path in **CMakeLists.txt**, and then link to them.

If the compilation target is **entry**, add the following commands:

target\_include\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/include)
target\_link\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
target\_link\_libraries(entry PUBLIC libnetwork\_boost.so) # Link to **libnetwork\_boost.so** and other depended SO files.

#### Configuring Signing Information

-   In the debugging phase, [request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178), [register a debugging device](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-device-0000001946142249), and [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102) in AppGallery Connect. Then, [manually sign your app](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233). You can also use DevEco Studio to automatically sign your app. During the automatic signing process, DevEco Studio requests restricted permissions from AppGallery Connect. For details, please refer to [Signing an App Not Associated with a Registered App - Procedure](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section151231211105010).
-   In the release phase, [request a release certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-releasecert-0000001946273961) and [a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-releaseprofile-0000001914714796) in AppGallery Connect. Then, [manually sign your app](../../../../app-release/release/document.md#section280162182818).

#### Requesting a Restricted ACL Permission

1\. When [requesting a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102) or [requesting a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-releaseprofile-0000001914714796), the fourth step is mandatory. Set **Permissions to request** to **Restricted ACL permissions** and click **Select**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/re6PxejGSpq8gHMGtFS_fQ/en-us_image_0000002496814629.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E16B20B52D7D32E033BC904DEBD27A7CB75B65363B4B4059240BA95CB61C71DF)

2\. Enter **ohos.permission.LINKTURBO** in the search box, find and select the required permission, and click **Submit**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/S6tAs6f8R36naQOjWxJ3_Q/en-us_image_0000002496814633.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4874B9B64277D90FBE073C44EC75824AF13756F88F7702E41314BC11F080725E)

3\. Enter the request reason based on your actual service requirements and submit the request. The request will be replied within one working day. You can view the request status in the [interaction center](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/interactive).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/tbGNi2n2TNeSVqCbfyWmGg/en-us_image_0000002496694657.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F640E8F75334AF58EED795C46EBCE8C604E53A91B9DDB83D668D8431F7D48629)

4\. After the permission request is approved, view the permission on the **Obtained** tab page. Select the permission and click **OK**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/A_t7kTvyRdqCzzRFugC10Q/en-us_image_0000002463535610.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1A302AC3EE0F1B74CED980E09433C5EBE895FC9A8789EBB30663AB09BCD7A7C)

5\. Select the permission and click **Add** to generate a new profile. Download the profile. When [manually signing your app](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), select this profile for use.

6\. Add the **ohos.permission.LINKTURBO** permission to the **requestPermissions** node in the **module.json5** file of the **entry** module in your project.

"requestPermissions": \[{
  "name": "ohos.permission.LINKTURBO"
}\]
