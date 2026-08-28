# Preparations

#### Applying for Permissions

Before using Remote Communication Kit capabilities, check whether you have applied for corresponding permissions for your app. If your app has not been granted some permissions, you need to declare these permissions.

Relevant permissions are required for all requests, except for those for canceling network requests and closing sessions. Specifically, Remote Communication Kit requires the following permissions:

-   **ohos.permission.INTERNET**: allows your app to access the Internet.
-   **ohos.permission.GET\_NETWORK\_INFO**: allows your app to request device network information.

You must manually configure the preceding permissions before using the kit. For details, please refer to the [procedure for applying for permissions](#section178884218124).

## Procedure

Configure the permission in the **module.json5** file in **entry/src/main**. The sample code is as follows:

{
  "module": {
    "requestPermissions": \[
      {
        "name": "ohos.permission.INTERNET"
      },
      {
        "name": "ohos.permission.GET\_NETWORK\_INFO" // Request this permission if you need to use the **cellular** mode defined in [PathPreference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/remote-communication-rcp#section828055885811).
      }
    \]
  }
}

#### Preparations for C API Development

In addition to the aforementioned permission configuration, when using the C API, you also need to set the dynamic library path and header file path in **CMakeLists.txt**, and then link to them.

If the compilation target is **entry**, add the following commands:

target\_include\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/include)
target\_link\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
target\_link\_libraries(entry PUBLIC librcp\_c.so) # Link to **librcp\_c.so** and other depended SO files.
