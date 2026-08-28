# Before You Start

Before you get started, learn about the development process.

-   [Obtain supported authentication capabilities](../obtaining-supported-authentication-capabilities/document.md).
    
-   [Initiate a request for user authentication and obtain the authentication result](../initiating-user-authentication/document.md).
    
-   Verify and use the authentication result. For details, see [Key Access Control via Secondary Authentication](../../../universal-keystore-kit/local-key-management/key-use/access-control/huks-access-control-overview/document.md).
    
-   (Optional) [Cancel authentication](../canceling-user-authentication/document.md).
    
-   (Optional) [Apply custom authentication](../applying-custom-authentication/document.md).
    

#### Requesting Permissions

The application capable of user authentication based on biometric features (such as face and fingerprints) must have the ohos.permission.ACCESS\_BIOMETRIC permission.

This permission is a system\_grant permission and must be declared in the **requestPermissions** tag in the **module.json5** file. For details, see [Declaring Permissions](../../../application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
