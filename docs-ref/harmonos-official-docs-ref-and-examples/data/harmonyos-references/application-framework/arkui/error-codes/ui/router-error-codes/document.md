# Router Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/sCAAQGB9SSeWsvI_O0-quQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99E46267B01DBB2E2CB8D16419DC23C560FF1A6999235BA67552AE506BBCF7E5)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 100002 Incorrect URI During Page Redirection

**Error Message**

Uri error. The URI of the page to redirect is incorrect or does not exist.

**Description**

This error code is reported when the URI of the page to redirect is incorrect or does not exist. This error code is represented as a string type.

**Possible Causes**

The entered URI is incorrect or does not exist.

**Solution**

Ensure that the URI is correct.

#### 100003 Too Many Pages Are Pushed into the Page Stack

**Error Message**

Page stack error. Too many pages are pushed.

**Description**

This error code is reported when more than 32 pages are pushed into the page stack. This error code is represented as a string type.

**Possible Causes**

Too many pages are pushed.

**Solution**

Delete unnecessary or invalid pages.

#### 100004 Incorrect Route Name

**Error Message**

Named route error. The named route does not exist.

**Description**

This error code is reported when the specified route name for redirection is incorrect or does not exist. This error code is represented as a string type.

**Possible Causes**

The specified route name for redirection is incorrect or does not exist.

**Solution**

Verify that the specified route name for redirection is correct and exists.

#### 100005 Builder Function Not Registered During Navigation

**Error Message**

Builder function not registered.

**Description**

This error code is reported during navigation when the builder function for creating the **NavDestination** component is not registered.

**Possible Causes**

-   The builder function for creating the **NavDestination** component is not registered at the time of navigation.
    
-   The target page does not contain the **Navigation** component.
    
-   The routing table is not configured.
    

**Solution**

Check whether the **Navigation** component provides the builder function for creating **NavDestination**. Ensure that the routing table is correctly configured and the target page contains the **Navigation** component.

#### 100006 NavDestination Not Found

**Error Message**

NavDestination not found.

**Description**

This error code is reported when no **NavDestination** component is found for navigation.

**Possible Causes**

No **NavDestination** component is available for navigation.

**Solution**

Make sure there is a **NavDestination** component for navigation.

#### 106200 Invalid Index Value

**Error Message**

index value is invalid.

**Description**

This error code is reported when an invalid index value is provided.

**Possible Causes**

The index value is invalid.

**Solution**

Check the provided index value.

#### 106201 Failed to Obtain Route Navigation Information

**Error Message**

Failed to query route navigation information.

**Description**

This error code is reported when the system fails to obtain route navigation information.

**Possible Causes**

The current node is not within a **Navigation** component.

**Solution**

Check whether the current node is within a **Navigation** component.

#### 106202 Invalid Buffer Size

**Error Message**

buffer size is not large enough.

**Description**

This error code is reported when an invalid buffer size is provided.

**Possible Causes**

The provided buffer size is smaller than the minimum required to accommodate the target data.

**Solution**

Check the provided buffer size.

#### 200002 Incorrect URI During Page Replacement

**Error Message**

Uri error. The URI of the page to be used for replacement is incorrect or does not exist.

**Description**

This error code is reported when the URI of the page to be used for replacement is incorrect or does not exist. This error code is represented as a string type.

**Possible Causes**

The entered URI is incorrect or does not exist.

**Solution**

Ensure that the URI is correct.

#### 300001 HSP Download Failure Before Redirection

**Error Message**

hsp silent install fail.

**Description**

This error code is reported when the download of the HSP, which contains the target page, fails before **Navigation** performs the redirection.

**Possible Causes**

The target HSP to be downloaded does not exist.

**Solution**

Verify that the HSP for the target navigation page actually exists. Make sure the value of **moduleName** passed in is correct.
