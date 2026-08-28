# Quick Adaptation

The ArkUI [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput) component provides components for login scenarios, while Password Vault integrates functions such as autofill. You only need to use standard ArkUI components in the UI to implement convenient login for users via Password Vault.

#### Constraints

To implement the password autofill service, you must use the ArkUI [TextInput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-textinput) component to implement the input box and specify the input box type (**InputType**). The following table describes the input box types and when to use them.

**Table 1** Description of input box types
| 
InputType

 | 

Description

 | 

Scenario

 |
| :-- | :-- | :-- |
| 

USER\_NAME

 | 

Username input mode.

 | 

Used for the user to enter the username in scenarios such as login and registration.

 |
| 

Password

 | 

Password input mode. This input box allows only digits, letters, underscores (\_), spaces, and special characters.

An eye icon is used to show or hide the password, and the password is hidden behind dots by default.

 | 

Used for the user to enter the password in scenarios such as login and registration.

 |
| 

NUMBER\_PASSWORD

 | 

Numeric password input mode. Only numbers are allowed.

An eye icon is used to show or hide the password, and the password is hidden behind dots by default.

 | 

Used for the user to enter the password in scenarios such as login and registration.

 |
| 

NEW\_PASSWORD

 | 

New password input mode.

 | 

Used for the user to enter the new password in scenarios such as registration and password change.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/1aC3rLCgTQ2EfSHh_0cs_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32A870D589104CF9934E791119972906244A2542AB7677ACDB75CA9D63734417)

The **Password** type mentioned in this topic can be replaced with the **NUMBER\_PASSWORD** type.

#### Quick Adaptation Guide

To use autosave and autofill on the username and password login page, set **type** of the **TextInput** component to **InputType.USER\_NAME** for username input and to **InputType.Password** for password input.

To use strong password autofill on the account and password registration page, set **type** of the **TextInput** component to **InputType.NEW\_PASSWORD**. If the application has special requirements on the password strength, see [Suggestions on Automatically Generating Strong Passwords for Applications](../autofill/suggestions-on-automatically-generating-strong-passwords-for-applications/document.md).

Example:

TextInput({ placeholder: 'Username' })
  .opacity(0.6)
  .type(InputType.USER\_NAME)
  .placeholderColor(0x182431)
  .width('100%')
  .placeholderFont({ size: 16, weight: FontWeight.Regular })
  .margin({ top: 32, bottom: 8 })
