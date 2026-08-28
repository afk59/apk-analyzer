# @ohos.application.formError (formError)

The **formError** module provides error codes for widgets.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/tgZUAm-8Rj2HSeNOj8R9hA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2702537AD0F1CC90B6DC66B0CA356EA4099663A091C49A24C334479D04B6A704)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module is deprecated since API version 9. You are advised to use [Widget Error Codes](../../error-codes/widget-error-codes/document.md) instead.

#### Modules to Import

import { formError } from '@kit.FormKit';

#### Required Permissions

None.

#### FormError

Enumerates the widget types.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| ERR\_COMMON | 1 | Default error code. |
| ERR\_PERMISSION\_DENY | 2 | You are not authorized to perform the operation. |
| ERR\_GET\_INFO\_FAILED | 4 | Failed to obtain the widget information. |
| ERR\_GET\_BUNDLE\_FAILED | 5 | Failed to obtain the bundle information. |
| ERR\_GET\_LAYOUT\_FAILED | 6 | Failed to obtain the layout information. |
| ERR\_ADD\_INVALID\_PARAM | 7 | Invalid parameters are detected. |
| ERR\_CFG\_NOT\_MATCH\_ID | 8 | The widget ID does not match any widget. |
| ERR\_NOT\_EXIST\_ID | 9 | The widget ID does not exist. |
| ERR\_BIND\_PROVIDER\_FAILED | 10 | Failed to bind to the widget provider. |
| ERR\_MAX\_SYSTEM\_FORMS | 11 | The number of system widgets exceeds the upper limit. |
| ERR\_MAX\_INSTANCES\_PER\_FORM | 12 | The number of instances per widget exceeds the upper limit. |
| ERR\_OPERATION\_FORM\_NOT\_SELF | 13 | The application is not allowed to operate widgets provided by other applications. |
| ERR\_PROVIDER\_DEL\_FAIL | 14 | The widget provider failed to delete the widget. |
| ERR\_MAX\_FORMS\_PER\_CLIENT | 15 | The number of widgets applied for by the widget host exceeds the upper limit. |
| ERR\_MAX\_SYSTEM\_TEMP\_FORMS | 16 | The number of temporary widgets exceeds the upper limit. |
| ERR\_FORM\_NO\_SUCH\_MODULE | 17 | The module does not exist. |
| ERR\_FORM\_NO\_SUCH\_ABILITY | 18 | The ability component does not exist. |
| ERR\_FORM\_NO\_SUCH\_DIMENSION | 19 | The widget dimension does not exist. |
| ERR\_FORM\_FA\_NOT\_INSTALLED | 20 | The FA where the widget is located is not installed. |
| ERR\_SYSTEM\_RESPONSES\_FAILED | 30 | The system service failed to respond. |
| ERR\_FORM\_DUPLICATE\_ADDED | 31 | The widget has been added. |
| ERR\_IN\_RECOVERY | 36 | Failed to overwrite the widget data. |
