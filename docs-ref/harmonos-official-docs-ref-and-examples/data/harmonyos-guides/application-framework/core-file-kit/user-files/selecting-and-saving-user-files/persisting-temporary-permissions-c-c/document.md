# Persisting Temporary Permissions (C/C++)

#### When to Use

If an application accesses a file by using Picker, the permission for accessing the file will be automatically invalidated after the application exits or the device restarts. To retain the permission for accessing the file, you need to [persist the permission](../persisting-temporary-permissions-arkts/document.md#when-to-use). You can use the **FileShare** module to manage persistent permissions on files or directories based on their URIs, including activating, deactivating, and checking these permissions.

#### Available APIs

For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-file-share-h).

| API | Description |
| :-- | :-- |
| OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | Persists the permissions on files or directories. |
| OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | Revokes the permissions from files or directories. |
| OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | Activates the persistent permissions on files or directories. |
| OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | Deactivates the persistent permissions on files or directories. |
| OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum) | Checks the persistent permissions on files or directories. |
| OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum) | Releases the memory allocated for **FileShare\_PolicyErrorResult**. |

#### Constraints

-   Before using the **FileShare** APIs, check that your device has SystemCapability.FileManagement.AppFileService.FolderAuthorization.
    
-   To call **FileShare** APIs, the application must have the **ohos.permission.FILE\_ACCESS\_PERSIST** permission. For details about how to request the permission, see [Workflow for Using Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/workflow-for-requesting-permissions/document.md).
    

#### How to Develop

The following example describes how to use the FileShare APIs.

**Adding the Dynamic Link Library**

Add the following library to **CMakeLists.txt**.

target\_link\_libraries(sample PUBLIC libohfileshare.so)

**Including Header Files**

#include <filemanagement/fileshare/oh\_file\_share.h>
#include <iostream>

1.  Create a **FileShare\_PolicyInfo** instance, and use **OH\_FileShare\_PersistPermission** to persist the permissions on files based on their URI. The maximum value of **policyNum** is **500**.
    
    static const uint32\_t policyNum = 2;
    char strTestPath1\[\] = "file://com.example.fileshare/data/storage/el2/base/files/test1.txt";
    char strTestPath2\[\] = "file://com.example.fileshare/data/storage/el2/base/files/test2.txt";
    FileShare\_PolicyInfo policy\[policyNum\] = {
        {strTestPath1, static\_cast<unsigned int>(strlen(strTestPath1)), FileShare\_OperationMode::READ\_MODE},
        {strTestPath2, static\_cast<unsigned int>(strlen(strTestPath2)), FileShare\_OperationMode::WRITE\_MODE}};
    FileShare\_PolicyErrorResult\* result = nullptr;
    uint32\_t resultNum = 0;
    napi\_value napiResult;
    std::string resultStr;
    auto ret = OH\_FileShare\_PersistPermission(policy, policyNum, &result, &resultNum);
    if (ret != ERR\_OK) {
        if (ret == ERR\_EPERM && result != nullptr) {
            for (uint32\_t i = 0; i < resultNum; i++) {
                std::cout << "error uri: " <<  result\[i\].uri << std::endl;
                std::cout << "error code: " <<  result\[i\].code << std::endl;
                std::cout << "error message: " << result\[i\].message << std::endl;
                // ···
            }
        }
    }
    OH\_FileShare\_ReleasePolicyErrorResult(result, resultNum);
    
2.  Call **OH\_FileShare\_ActivatePermission** to activate the persistent permissions on files. The maximum value of **policyNum** is **500**.
    
    auto ret = OH\_FileShare\_ActivatePermission(policy, policyNum, &result, &resultNum);
    if (ret != ERR\_OK) {
        if (ret == ERR\_EPERM && result != nullptr) {
            for (uint32\_t i = 0; i < resultNum; i++) {
                std::cout << "error uri: " <<  result\[i\].uri << std::endl;
                std::cout << "error code: " <<  result\[i\].code << std::endl;
                std::cout << "error message: " << result\[i\].message << std::endl;
                // ···
            }
        }
    }
    OH\_FileShare\_ReleasePolicyErrorResult(result, resultNum);
    
3.  Call **OH\_FileShare\_DeactivatePermission** to deactivate the persistent permissions on files. The maximum value of **policyNum** is **500**.
    
    auto ret = OH\_FileShare\_DeactivatePermission(policy, policyNum, &result, &resultNum);
    if (ret != ERR\_OK) {
        if (ret == ERR\_EPERM && result != nullptr) {
            for (uint32\_t i = 0; i < resultNum; i++) {
                std::cout << "error uri: " <<  result\[i\].uri << std::endl;
                std::cout << "error code: " <<  result\[i\].code << std::endl;
                std::cout << "error message: " << result\[i\].message << std::endl;
                // ···
            }
        }
    }
    OH\_FileShare\_ReleasePolicyErrorResult(result, resultNum);
    
4.  Call **OH\_FileShare\_RevokePermission** to revoke the persistent permissions from files. The maximum value of **policyNum** is **500**.
    
    auto ret = OH\_FileShare\_RevokePermission(policy, policyNum, &result, &resultNum);
    if (ret != ERR\_OK) {
        if (ret == ERR\_EPERM && result != nullptr) {
            for (uint32\_t i = 0; i < resultNum; i++) {
                std::cout << "error uri: " <<  result\[i\].uri << std::endl;
                std::cout << "error code: " <<  result\[i\].code << std::endl;
                std::cout << "error message: " << result\[i\].message << std::endl;
                // ···
            }
        }
    }
    OH\_FileShare\_ReleasePolicyErrorResult(result, resultNum);
    
5.  Call **OH\_FileShare\_CheckPersistentPermission** to check the persistent permissions on files. The maximum value of **policyNum** is **500**.
    
    bool \*result = nullptr;
    auto ret = OH\_FileShare\_CheckPersistentPermission(policy, policyNum, &result, &resultNum);
    if (ret != ERR\_OK) {
        if (ret == ERR\_EPERM && result != nullptr) {
            for (uint32\_t i = 0; i < resultNum && resultNum <= policyNum; i++) {
                std::cout << "uri: " <<  policy\[i\].uri << std::endl;
                std::cout << "result: " <<  result\[i\] << std::endl;
                // ···
            }
        }
    }
    std::cout << "retCode: " <<  ret << std::endl;
    free(result);
