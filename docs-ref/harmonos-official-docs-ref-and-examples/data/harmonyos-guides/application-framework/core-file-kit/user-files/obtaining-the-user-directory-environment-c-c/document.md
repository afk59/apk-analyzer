# Obtaining the User Directory Environment (C/C++)

#### When to Use

You can use [Environment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-environment-h) to allow a third-party application to access files in a user directory.

#### Constraints

-   Before using the APIs of the **Environment** module, ensure that the device has SystemCapability.FileManagement.File.Environment.FolderObtain.
-   The APIs provided by the **Environment** module can be used to obtain the application sandbox paths of the user directories. To operate the related directory and its subdirectories, user authorization is required via a dialog box. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

#### Available APIs

For details about the APIs, see [oh\_environment.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-environment-h).

| API | Description |
| :-- | :-- |
| FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir (char \*\*result) | Obtains the sandbox path of the **Download** directory. This function supports only 2-in-1 devices. |
| FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir (char \*\*result) | Obtains the sandbox path of the **Desktop** directory. This function supports only 2-in-1 devices. |
| FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir (char \*\*result) | Obtains the sandbox path of the **Documents** directory. This function supports only 2-in-1 devices. |

#### How to Develop

**Adding the Dynamic Link Library**

Add the following library to **CMakeLists.txt**.

target\_link\_libraries(sample PUBLIC libohenvironment.so libhilog\_ndk.z.so)

**Adding Header Files**

#include <cstdlib>
#include <filemanagement/environment/oh\_environment.h>
#include <filemanagement/fileio/oh\_fileio.h>
#include <hilog/log.h>

1.  Call **OH\_Environment\_GetUserDownloadDir** to obtain the sandbox path of the user **Download** directory. The memory allocated must be released using **free()**.
    
    Example:
    
    void GetUserDownloadDirPathExample()
    {
        char \*downloadPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDownloadDir(&downloadPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Download Path=%{public}s", downloadPath);
            free(downloadPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDownloadPath fail, error code is %{public}d", ret);
        }
    }
    
2.  Call **OH\_Environment\_GetUserDesktopDir** to obtain the sandbox path of the user **Desktop** directory. The memory allocated must be released using **free()**.
    
    Example:
    
    void GetUserDesktopDirPathExample()
    {
        char \*desktopPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDesktopDir(&desktopPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Desktop Path=%{public}s", desktopPath);
            free(desktopPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDesktopPath fail, error code is %{public}d", ret);
        }
    }
    
3.  Call **OH\_Environment\_GetUserDocumentDir** to obtain the sandbox path of the user **Document** directory. The memory allocated must be released using **free()**.
    
    Example:
    
    void GetUserDocumentDirPathExample()
    {
        char \*documentPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDocumentDir(&documentPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Document Path=%{public}s", documentPath);
            free(documentPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDocumentPath fail, error code is %{public}d", ret);
        }
    }
    
4.  Call **OH\_Environment\_GetUserDocumentDir** to obtain the sandbox path of the user **Document** directory, and use the **stat** function to determine the space of the **Document** directory. When using the **stat** function in the API, you need to include the **<sys/stat.h>** header file.
    
    Example:
    
    Include the following header file before using the API.
    
    #include <sys/stat.h>
    
    void GetUserDownloadDirSizeExample()
    {
        char \*documentPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDocumentDir(&documentPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Document Path=%{public}s", documentPath);
            struct stat fileStat;
            int result = stat(documentPath, &fileStat);
            if (result == 0) {
                OH\_LOG\_INFO(LOG\_APP, "Document Size=%{public}ld", fileStat.st\_size);
            } else {
                OH\_LOG\_ERROR(LOG\_APP, "GetDocumentSize fail, error code is %{public}ld", result);
            }
            free(documentPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDocumentPath fail, error code is %{public}d", ret);
        }
    }
