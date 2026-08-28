# Creating an Application Multi-Instance

Multi-instance allows an application to run on multiple processes so that a user can log in multiple accounts and run the application at the same time without affecting each other. For example, a user can run several social accounts, or primary and secondary game accounts simultaneously without frequent log-in and log-out.

Multiple application instances on the home screen are independent in terms of the running, notification, and more. Instances share data with each other and can be switched using accounts.

Relationship between multiple application instances:

-   The application icons of multiple instances are the same.
-   All instances share the file data in the [application file directory](../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md#application-file-directory-and-application-file-path).
-   You can switch between accounts. A single instance supports logging in with different accounts.

#### Constraints

Application multi-instance can run on only 2-in-1 devices.

#### How to Develop

1.  Configure the multi-instance.
    
    Configure the [multiAppMode](../../application-configuration-files-in-stage-model/app-json5-configuration-file/document.md#multiappmode) field in the **App/app.json5** configuration file in the project. The code snippet is as follows:
    
    {
      "app": {
        // ...
        "multiAppMode": {
          "multiAppModeType": "multiInstance",
          "maxCount": 5
        }
      }
    }
    
2.  Create a multi-instance.
    

-   Build and package the configured project and install it on the device.
-   Right-click an application icon on the home screen to open an application process. Then right-click the application icon again and choose **Open**. In this case, two application process pages of the same application are displayed on the home screen.
