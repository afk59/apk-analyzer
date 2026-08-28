# Bundle Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/itp6vj_KQNqSGSfKhd2V0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B20656D1600A97F4DBD7EF1BCBA7249539AAEFE927FC762BBE609554EEF9E83F)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 17700001 Bundle Name Does Not Exist

**Error Message**

The specified bundle name is not found.

**Description**

The specified bundle name does not exist.

**Possible Causes**

1.  The bundle name is misspelled.
2.  The corresponding bundle is not installed.

**Solution**

1.  Check whether the spelling of the bundle name is correct.
2.  Run the [dump command](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#dump), and check the command output. If the bundle is not installed, an error is reported.
    
    \# Replace \*\*com.xxx.demo\*\* with the actual bundle name.
    hdc shell bm dump -n com.xxx.demo
    

#### 17700002 Module Name Does Not Exist

**Error Message**

The specified module name is not found.

**Description**

The specified module name does not exist.

**Possible Causes**

1.  The module name is misspelled.
2.  The module is not installed.

**Solution**

1.  Check whether the spelling of the module name is correct.
2.  Run the [dump command](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#dump), and check whether the module name exists in the list of the **hapModuleNames** field in the output. If not, the module is not installed.
    
    \# Replace \*\*com.xxx.demo\*\* with the actual bundle name.
    hdc shell bm dump -n com.xxx.demo
    

#### 17700003 Ability Name Does Not Exist

**Error Message**

The specified ability name is not found.

**Description**

The specified ability name does not exist.

**Possible Causes**

1.  The ability name is misspelled.
2.  The application does not have the ability specified by **abilityName**.
3.  When [bundleManager.getProfileByAbility](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetprofilebyability) or [bundleManager.getProfileByExtensionAbility](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetprofilebyextensionability) is used for query based on a combination of ability name and module name, the application does not have the module specified by **moduleName** or the specified ability under that module.

**Solution**

1.  Check whether the spelling of the ability name is correct.
2.  Run the [dump command](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#dump), and check whether **abilityInfos** under the **hapModuleInfos** field in the output contains an entry where the name equals this ability name. If no such entry is found, the ability name does not exist.
3.  Run the [dump command](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#dump), and check the **hapModuleNames** field in the output. If the specified module name is not in the list, the application has not installed the module, and the ability under that module also does not exist.
    
    \# Replace \*\*com.xxx.demo\*\* with the actual bundle name.
    hdc shell bm dump -n com.xxx.demo
    

#### 17700004 User ID Does Not Exist

**Error Message**

The specified user ID is not found.

**Description**

When a user-related API is called, the user ID passed in does not exist.

**Possible Causes**

1.  Incorrect username.
2.  The user does not exist in the system.

**Solution**

1.  Check whether the user ID is correct.
2.  Check whether the user exists.

#### 17700021 Invalid UID

**Error Message**

The specified uid is invalid.

**Description**

When the [getBundleNameByUid](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetbundlenamebyuid14) API of the bundleManager module is called, the UID passed in is invalid.

**Possible Causes**

The application corresponding to the UID does not exist.

**Solution**

Check whether the UID exists in the system. Run the [dump command](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool#dump), and check the UID of the installed application. If multiple UIDs are displayed, select the one greater than 0. If no result is displayed, the application is not installed.

\# Replace \*\*com.xxx.demo\*\* with the actual bundle name.
hdc shell "bm dump -n com.xxx.demo |grep uid"

#### 17700024 Profile Does Not Exist

**Error Message**

Failed to get the profile because the specified profile is not found in the HAP.

**Description**

When an API for querying the profile is called, the profile does not exist.

**Possible Causes**

1.  The metadata name passed in the API does not exist in the profile.
2.  The content of the profile is not in JSON format.

**Solution**

1.  Check whether the metadata name in the **ability** or **extensionAbility** to be queried exists.
2.  Check whether the content of the profile to be queried is in JSON format.

#### 17700026 Bundle Disabled

**Error Message**

The specified bundle is disabled.

**Description**

When an API for querying bundle information is called, the specified bundle is disabled.

**Possible Causes**

The bundle on the device has been disabled and cannot be queried.

**Solution**

Check whether the bundle on the device is disabled.

#### 17700029 Disabled Ability

**Error Message**

The specified ability is disabled.

**Description**

When an API for querying ability information is called, the specified ability is disabled.

**Possible Causes**

The specified ability is disabled.

**Solution**

Check whether the ability is disabled. You can use [Bundle Manager](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/bm-tool) to query the information.

#### 17700032 Application Does Not Contain a Module with the Overlay Feature

**Error Message**

The specified bundle does not contain any overlay module.

**Description**

An API is called to obtain the overlayModuleInfo object of another application, but that application does not contain a module with the overlay feature.

**Possible Causes**

The specified application does not contain a module with the overlay feature.

**Solution**

Check whether the application contains a module with the overlay feature.

#### 17700033 Module Is Not Configured with the Overlay Feature

**Error Message**

The specified module is not an overlay module.

**Description**

An API is called to obtain the overlayModuleInfo object of a module, but the module is not configured with the overlay feature.

**Possible Causes**

The specified module is not a module with the overlay feature.

**Solution**

Check whether the module is configured with the overlay feature.

#### 17700034 Module Is Configured with the Overlay Feature

**Error Message**

The specified module is an overlay module.

**Description**

An API is called to obtain the overlayModuleInfo object based on the target module name, but that module is configured with the overlay feature.

**Possible Causes**

The specified module is configured with the overlay feature.

**Solution**

Check whether the module is configured with the overlay feature.

#### 17700055 Invalid Link

**Error Message**

The specified link is invalid.

**Description**

When the [canOpenLink](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagercanopenlink12) API of the bundleManager module is called, the link passed in is invalid.

**Possible Causes**

The format of the link is incorrect.

**Solution**

Check whether the link format is correct.

#### 17700056 Scheme of the Link Not Configured in querySchemes

**Error Message**

The scheme of the specified link is not in the querySchemes.

**Description**

When the [canOpenLink](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagercanopenlink12) API of the bundleManager module is called, the scheme of the link is not configured in the **querySchemes** field.

**Possible Causes**

The scheme of the link is not configured in the **querySchemes** field.

**Solution**

Check whether the URL scheme is configured in the **querySchemes** field. For details, see [Using canOpenLink to Check Application Accessibility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/canopenlink).

#### 17700070 Invalid Shortcut ID

**Error Message**

The specified shortcut id is illegal.

**Description**

The specified shortcut ID is invalid.

**Possible Causes**

A shortcut with the same bundle name, clone index, user ID, and shortcut ID already exists, or the passed-in shortcut ID does not exist or is empty.

**Solution**

1.  Check whether the bundle name and shortcut ID are correct.

#### 17700072 Launch Want Does Not Exist

**Error Message**

The launch want is not found.

**Description**

The Want information in the [bundleManager.getLaunchWant](../../arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#bundlemanagergetlaunchwant13) API does not exist.

**Possible Causes**

The application does not have a UIAbility with **entities** containing **"entity.system.home"** and **actions** containing **"ohos.want.action.home"**.

**Solution**

Configure a UIAbility with **entities** containing **"entity.system.home"** and **actions** containing **"ohos.want.action.home"** for the application.

#### 17700101 Bundle Manager Service Abnormal

**Error Message**

Bundle manager service exception.

**Description**

The Bundle Manager service is abnormal.

**Possible Causes**

Scenario 1:

An unknown system exception occurs.

Scenario 2:

The system throws an uncaught error code, such as IPC failure or file copy failure.

**Solution**

1.  Restart the phone and try again.
    
2.  If the request still fails after the preceding steps are performed for three to five times, check whether a crash file containing **foundation** exists in the **/data/log/faultlog/faultlogger/** directory of the device.
    
    hdc shell
    cd /data/log/faultlog/faultlogger/
    ls -ls
    
3.  Export the crash file and log file and submit them to [online tickets](https://developer.huawei.com/consumer/en/support/feedback/#/) for help.
    
    hdc file recv /data/log/faultlog/faultlogger/
    hdc file recv /data/log/hilog/
