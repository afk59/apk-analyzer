# Preparations

Make [necessary preparations](../../../../../getting-prepared/application-development-preparations/document.md) before you start app development.

#### Configuring Network Permissions

Add the network permission under **requestPermissions** in the **src/main/module.json5** file.

{
  "module": {
    // ...
    "requestPermissions": \[
      {
        "name": "ohos.permission.INTERNET"
      }
    \]
  }
}
