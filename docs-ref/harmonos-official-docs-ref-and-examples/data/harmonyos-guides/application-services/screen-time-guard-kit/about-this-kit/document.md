# About This Kit

Screen Time Guard Kit provides open capabilities such as screen time management and app usage restriction while ensuring privacy and security protections. This can help you meet different users' requirements for time management and better serve your users.

#### Capabilities

[User authorization management](../user-authorization-management/document.md): manages user authorization information, including requesting user authorization, revoking user authorization, and querying authorization information.

[AppPicker](../apppicker/document.md): provides APIs for starting half-modal pages for users to select apps for management and quickly access other apps.

[Guard strategy management](../guard-strategy-management/document.md): provides APIs for adding, modifying, querying, deleting, starting, and stopping guard strategies.

[App access restriction](../app-access-restrictions/document.md): sets or removes access restrictions for specified apps. The operations take effect immediately.

#### Basic Concepts

Token: unique identifier of an app to be managed. This token does not contain the app information, such as the package name and app name, guaranteeing user data privacy and security.

Guard strategy: Screen time guard strategies fall into three types: start/end time, total duration, and shared duration.

Start/end time strategy: The start time and end time can be specified to restrict the access to certain apps in the specific period.

Total duration strategy: A duration starting from the current time can be specified to restrict the access to all or certain apps in the specific period.

Shared duration strategy: A shared duration can be specified to restrict the total usage time of all or certain apps.

Control scope: Screen time guard can be applied to all apps except system trustlist apps (such as Clock and Phone), the current app that initiates screen time guard, other authorized screen time guard apps, and the Digital Balance app.

#### Restrictions

1.  Screen Time Guard Kit is currently available only on phones and tablets. Emulators are supported.
2.  Currently, this kit is available only in the Chinese mainland.
3.  This kit can be called only in the main space and is not supported in the private space.
4.  Access from clone apps of the app that calls Screen Time Guard Kit is not supported.
