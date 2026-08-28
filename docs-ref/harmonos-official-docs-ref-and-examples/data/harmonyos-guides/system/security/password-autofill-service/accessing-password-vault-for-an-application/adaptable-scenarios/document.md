# Adaptable Scenarios

In addition to the previously mentioned scenarios, you can use Password Vault in scenarios where an email address or mobile number is used for login or registration.

The autosave and autofill features of Password Vault will be triggered when an input box of the **Password** or **NEW\_PASSWORD** type and one of the **USER\_NAME**, **Email**, and **PhoneNumber** input boxes exist on the page.

The Password Vault logic can also be triggered if the page has only two **TextInput** input boxes: one of the **Password** or **NEW\_PASSWORD** type and the other of the non-password type. For details, see [Description of input box types](../quick-adaptation/document.md#section158542054105219).

Password Vault supports the following scenarios:

-   There are only two **TextInput** input boxes on the page.
    
    | 
    Input Box Type (**InputType**)
    
     | 
    
    Password Vault Behavior
    
     |
    | :-- | :-- |
    | 
    
    **InputType.USER\_NAME**/**InputType.Email**/**InputType.PhoneNumber** + **InputType.Password**
    
     | 
    
    -   Tapping either input box will trigger a message for password autofill.
    -   Page navigation will trigger a dialog box for saving the account and password.
    
     |
    | 
    
    Non-password type + **InputType.Password**
    
     | 
    
    -   Tapping either input box will trigger a message for password autofill.
    -   Page navigation will trigger a dialog box for saving the account and password.
    
     |
    | 
    
    **InputType.USER\_NAME**/**InputType.Email**/**InputType.PhoneNumber** + **InputType.NEW\_PASSWORD**
    
     | 
    
    -   Tapping the new password input box (**InputType.NEW\_PASSWORD**) will trigger strong password filling.
    -   If the page is redirected and the generated strong password is used, the password is saved to **Password Vault** in silent mode. If a user-defined password is used (the generated strong password is not used or is changed), a dialog box for saving the password is displayed.
    
     |
    | 
    
    Non-password type + **InputType.NEW\_PASSWORD**
    
     | 
    
    -   Tapping the new password input box (**InputType.NEW\_PASSWORD**) will trigger strong password filling.
    -   If the page is redirected and the generated strong password is used, the password is saved to **Password Vault** in silent mode. If a user-defined password is used (the generated strong password is not used or is changed), a dialog box for saving the password is displayed.
    
     |
    
-   There are multiple **TextInput** input boxes on the page.
    
    | 
    Input Box Type (**InputType**)
    
     | 
    
    Password Vault Behavior
    
     |
    | :-- | :-- |
    | 
    
    One or more of **InputType.USER\_NAME**, **InputType.Email**, and **InputType.PhoneNumber** + **InputType.Password**
    
     | 
    
    -   Tapping any of the input boxes will trigger a message for password autofill.
    -   Page navigation will trigger a dialog box for saving the account and password.
    -   The content in the **USER\_NAME** input box is preferentially saved as the account name.
    
     |
    | 
    
    One or more of **InputType.USER\_NAME**, **InputType.Email**, and **InputType.PhoneNumber** + **InputType.NEW\_PASSWORD**
    
     | 
    
    -   Tapping the new password input box (**InputType.NEW\_PASSWORD**) will trigger strong password filling.
    -   If the page is redirected and the generated strong password is used, the password is saved to **Password Vault** in silent mode. If a user-defined password is used (the generated strong password is not used or is changed), a dialog box for saving the password is displayed.
    -   The content in the **USER\_NAME** input box is preferentially saved as the account name.
    
     |
    | 
    
    One or more of **InputType.USER\_NAME**, **InputType.Email**, and **InputType.PhoneNumber** + **InputType.Password** + **InputType.NEW\_PASSWORD**
    
     | 
    
    -   Tapping any of the input boxes will trigger a message for password autofill.
    -   Tapping the new password input box (**InputType.NEW\_PASSWORD**) will trigger strong password filling.
    -   If the page is redirected and the generated strong password is used, the password is saved to **Password Vault** in silent mode. If a user-defined password is used (the generated strong password is not used or is changed), a dialog box for saving the password is displayed.
    -   The content in the **USER\_NAME** input box is preferentially saved as the account name.
    
     |
