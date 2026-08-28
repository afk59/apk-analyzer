# Obtaining and Accessing a User Directory

#### Obtaining and Accessing a User Directory (ArkTS)

You can use [ohos.file.environment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-environment) to allow a third-party application to access files in a user directory.

**Constraints**

-   The device must have the SystemCapability.FileManagement.File.Environment.FolderObtain system capability. Currently, only 2-in-1 devices are supported.
    
    if (!canIUse('SystemCapability.FileManagement.File.Environment.FolderObtain')) {
        console.error('this api is not supported on this device');
        return;
    }
    
-   The APIs for obtaining user directories do not verify the permissions for accessing the related user directories. To access the user directories, the caller must have the related permissions. If a third-party application needs to access a user directory, user authorization for access to the **Download**, **Documents**, or **Desktop** directory is required via a dialog box. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

   "requestPermissions" : \[
       "ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY",
       "ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY",
   \]

## Example

1.  Obtain a user directory.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { Environment } from '@kit.CoreFileKit';
    
    function getUserDirExample() {
      try {
        const downloadPath = Environment.getUserDownloadDir();
        console.info(\`success to getUserDownloadDir: ${downloadPath}\`);
        const documentsPath = Environment.getUserDocumentDir();
        console.info(\`success to getUserDocumentDir: ${documentsPath}\`);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(\`failed to get user dir, Error code: ${err.code}, message: ${err.message}\`);
      }
    }
    
2.  Access files in the **Download** directory.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { Environment } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { common } from '@kit.AbilityKit';
    
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
    function readUserDownloadDirExample(context: common.UIAbilityContext) {
      try {
        // Obtain the path to the Download directory.
        const downloadPath = Environment.getUserDownloadDir();
        console.info(\`success to getUserDownloadDir: ${downloadPath}\`);
        const dirPath = context.filesDir;
        console.info(\`success to get filesDir: ${dirPath}\`);
        // List the files in the Download directory and copy them to the sandbox directory.
        let fileList: string\[\] = fs.listFileSync(downloadPath);
        fileList.forEach((file, index) => {
          console.info(\`${downloadPath} ${index}: ${file}\`);
          if (fs.statSync(\`${downloadPath}/${file}\`).isFile()) {
            fs.copyFileSync(\`${downloadPath}/${file}\`, \`${dirPath}/${file}\`);
          }
        });
        // List the files in the sandbox directory.
        fileList = fs.listFileSync(dirPath);
        fileList.forEach((file, index) => {
          console.info(\`${dirPath} ${index}: ${file}\`);
        });
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(\`Error code: ${err.code}, message: ${err.message}\`);
      }
    }
    
3.  Save the file to the **Download** directory.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { Environment } from '@kit.CoreFileKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
    function writeUserDownloadDirExample() {
      // Check whether the caller has the READ\_WRITE\_DOWNLOAD\_DIRECTORY permission. If not, apply for the permission from the user.
      try {
        // Obtain the path to the Download directory.
        const downloadPath = Environment.getUserDownloadDir();
        console.info(\`success to getUserDownloadDir: ${downloadPath}\`);
        // Save temp.txt to the Download directory.
        const file = fs.openSync(\`${downloadPath}/temp.txt\`, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE);
        fs.writeSync(file.fd, 'write a message');
        fs.closeSync(file);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(\`Error code: ${err.code}, message: ${err.message}\`);
      }
    }
    

#### Obtaining and Accessing a User Directory (C/C++)

In addition to ArkTS APIs, you can use C/C++ APIs for user directory access. For details about the APIs, see [oh\_environment.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-environment-h).

**Constraints**

-   The device must have SystemCapability.FileManagement.File.Environment.FolderObtain.
-   If a third-party application needs to access a user directory, user authorization for access to the **Download**, **Documents**, or **Desktop** directory is required via a dialog box. For details, see [Requesting User Authorization](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## Available APIs

For details about the APIs, see [oh\_environment.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-environment-h).

| API | Description |
| :-- | :-- |
| FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir (char \*\*result) | Obtains the sandbox path of the **Download** directory. This API is available only for 2-in-1 devices. |
| FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir (char \*\*result) | Obtains the sandbox path of the **Desktop** directory. This API is available only for 2-in-1 devices. |
| FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir (char \*\*result) | Obtains the sandbox path of the **Documents** directory. This API is available only for 2-in-1 devices. |

## How to Develop

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

target\_link\_libraries(sample PUBLIC libohenvironment.so libhilog\_ndk.z.so)

**Adding Header Files**

#include <filemanagement/environment/oh\_environment.h>
#include <filemanagement/fileio/oh\_fileio.h>
#include <hilog/log.h>

1.  Call **OH\_Environment\_GetUserDownloadDir** to obtain the sandbox path of the user **Download** directory. The memory allocated by **malloc()** must be released using **free()**.
    
    Example:
    
    #include <cstdlib>
    
    void GetUserDownloadDirExample()
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
    
2.  Call **OH\_Environment\_GetUserDownloadDir** to obtain the sandbox path of the **Download** directory and view the files in it.
    
    Example:
    
    #include <cstdlib>
    #include <dirent.h>
    
    void ScanUserDownloadDirPathExample()
    {
        // Obtain the Download path.
        char \*downloadPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDownloadDir(&downloadPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Download Path=%{public}s", downloadPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDownloadPath fail, error code is %{public}d", ret);
            return;
        }
        // View the files in the Download directory.
        struct dirent \*\*namelist = nullptr;
        int num = scandir(downloadPath, &namelist, nullptr, nullptr);
        if (num < 0) {
            free(downloadPath);
            OH\_LOG\_ERROR(LOG\_APP, "Failed to scan dir");
            return;
        }
    
        for (int i = 0; i < num; i++) {
            OH\_LOG\_INFO(LOG\_APP, "%{public}s", namelist\[i\]->d\_name);
        }
        free(downloadPath);
        for (int i = 0; i < num; i++) {
            free(namelist\[i\]);
        }
        free(namelist);
    }
    
3.  Call **OH\_Environment\_GetUserDownloadDir** to obtain the sandbox path of the user **Download** directory and save **temp.txt** to this directory.
    
    Example:
    
    #include <fstream>
    
    void WriteUserDownloadDirPathExample()
    {
        // Obtain the Download path.
        char \*downloadPath = nullptr;
        FileManagement\_ErrCode ret = OH\_Environment\_GetUserDownloadDir(&downloadPath);
        if (ret == 0) {
            OH\_LOG\_INFO(LOG\_APP, "Download Path=%{public}s", downloadPath);
        } else {
            OH\_LOG\_ERROR(LOG\_APP, "GetDownloadPath fail, error code is %{public}d", ret);
            return;
        }
        // Save a file to the Download directory.
        std::string filePath = std::string(downloadPath) + "/temp.txt";
        free(downloadPath);
    
        std::ofstream outfile;
        outfile.open(filePath.c\_str());
        if (!outfile) {
            OH\_LOG\_ERROR(LOG\_APP, "Failed to open file");
            return;
        }
        std::string msg = "Write a message";
        outfile.write(msg.c\_str(), msg.size());
        outfile.close();
    }
