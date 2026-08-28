# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/CgIBAvDCS1CMOYDXopAWKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF1DABA2B69688DD0C093FE64770F24A9E301CB866BDC87DC1E7C1269F0A2096)

This section describes only error codes related to this module. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md)

#### 1010710001 Invalid Image Size

**Error message**

Maximum number of categories reached

**Description**

When the API for actions such as adding an icon is called, the input icon image size does not meet the required specifications.

**Possible causes**

-   Unknown cause.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/yeO4P1l4SuqRDfbQAGG-IQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA786E7527CEB6FDAB97ACE99CD80E3716EE39444F9D1CE5EFCD65A60A1202F5)

The current icon dimensions are not strictly limited.

**Solution**

Change the image data or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1010710002 The Number of Menu Items Exceeding the Upper Limit

**Error message**

The number of menu items or submenu items exceeds the limit.

**Description**

When the API for actions such as adding an icon is called, the number of input menu items exceeds the upper limit.

**Possible causes**

-   The number of all level-1 menu items exceeds the upper limit 20.
-   The number of submenu items under a level-1 menu exceeds the upper limit 20.

**Solution**

Change the level-1 and level-2 menu item settings or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1010710003 Too Frequent API Calls

**Error message**

The API is being called too frequently.

**Description**

The API is called too frequently.

**Possible causes**

The interval between **addToStatusBar**, **removeFromStatusBar**, **updateStatusBarIcon**, **updateQuickOperationHeight**,

and **updateStatusBarMenu** calls is less than 20 ms.

**Solution**

Adjust the API calling interval settings or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1010710004 Cannot Remove Icon When No Window Is in the Foreground

**Error message**

The icon cannot be deleted when no window is in the foreground.

**Description**

There are no app windows in the foreground. The **removeFromStatusBar** API cannot be called to remove the status bar icon.

**Possible causes**

The **removeFromStatusBar** API is called after the app is switched to the background.

**Solution**

Adjust the time when the API is called or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1010710005 String Length Exceeding Threshold

**Error message**

The string length exceeds the threshold.

**Description**

The string length exceeds the threshold.

**Possible causes**

-   The string length of **hoverTips** configured in [StatusBarItem](../statusbarmanager-status-bar-management-service/document.md#section105181855219) is **0** or greater than **128**.
-   The input string length in the [updateStatusBarHoverTips](../statusbarmanager-status-bar-management-service/document.md#section0391124717248) call is **0** or greater than **128**.

**Solution**

Verify that the string length is within the valid range. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1010720001 The Passed Level-1 Menu Data Does Not Meet Requirements

**Error message**

A menu item contains neither submenu nor menuAction.

**Description**

When the API for actions such as adding an icon or updating the menu item is called, the passed level-1 menu item data does not meet the requirements.

**Possible causes**

A passed level-1 menu item does not contain [menuAction](../statusbarmanager-status-bar-management-service/document.md#section3627115133810) or [subMenu](../statusbarmanager-status-bar-management-service/document.md#section3627115133810).

**Solution**

Check the input parameters for level-1 menu items or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210001 Maximum Number of Categories Reached

**Error message**

Maximum number of categories reached.

**Description**

When the API for adding a category is called, the number of added categories exceeds the upper limit.

**Possible causes**

The maximum number of categories is 3. The number of added categories exceeds the upper limit.

**Solution**

Change the menu category number or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210002 Duplicate Category Name

**Error message**

Duplicate category name.

**Description**

When the API for adding a category is called, the passed category name is the same as that of another category.

**Possible causes**

The passed category name is the same as that of an existing category.

**Solution**

Change the menu category name or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210003 Category Not Found

**Error message**

Category not found.

**Description**

When the API for obtaining, updating, or deleting a category is called, the corresponding menu category is not found.

**Possible causes**

-   All menu categories are obtained without adding any menu category.
-   When the API for updating a category is called, the input category ID is incorrect, and the corresponding menu category is not found.
-   When the API for deleting a category is called, the input category ID is incorrect, and no corresponding menu category can be found.
-   When the API for obtaining all tasks in a category is called, the input category ID is incorrect, and no corresponding menu category can be found.
-   When the API for adding a task is called, the input category ID is incorrect, and no corresponding menu category can be found.

**Solution**

Change the category IDs or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210004 Quick Task Not Found

**Error message**

Quick task not found.

**Description**

When the API for obtaining, updating, or deleting a task is called, the corresponding menu task is not found.

**Possible causes**

-   When the API for deleting a task is called, the input task ID is incorrect, and no corresponding menu task can be found.
-   When the API for obtaining all tasks in a category is called, the number of obtained tasks is 0.
-   When the API for updating a task is called, the input task ID is incorrect, and no corresponding menu task can be found.

**Solution**

Change the task IDs or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210008 String Length Exceeding Threshold

**Error message**

The string length exceeds the threshold.

**Description**

The input string length exceeds the threshold.

**Possible causes**

-   The input string in the [addCustomCategory](../quickbarmanager-quick-bar-management-service/document.md#section665018220561) call is either longer than 512 characters or empty.
-   The input string in the [updateCustomCategory](../quickbarmanager-quick-bar-management-service/document.md#section1623472312366) call is either longer than 512 characters or empty.
-   The input string in the [addQuickTask](../quickbarmanager-quick-bar-management-service/document.md#section13991750101114) call is either longer than 512 characters or empty.
-   The input string in the [updateQuickTask](../quickbarmanager-quick-bar-management-service/document.md#section1427319917408) call is either longer than 512 characters or empty.

**Solution**

Reconfigure the string or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1020210009 Invalid Parameter

**Error message**

Invalid parameter.

**Description**

The size of the **parameters** array exceeds the upper limit.

**Possible causes**

-   The size of the **parameters** array passed in the [addQuickTask](../quickbarmanager-quick-bar-management-service/document.md#section13991750101114) call exceeds 64.
-   The size of the **parameters** array passed in the [updateQuickTask](../quickbarmanager-quick-bar-management-service/document.md#section1427319917408) call exceeds 64.

**Solution**

Adjust the number of elements in the **parameters** array or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
