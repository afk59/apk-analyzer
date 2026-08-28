# Raw File Development

#### When to Use

This document describes how to use native RawFile APIs to manage raw file directories and files in HarmonyOS. You can use the APIs to perform operations such as traversing a file list and opening, searching for, reading, and closing raw files.

The APIs ended with **64** are new APIs. These APIs can be used to open rawfiles larger than 2 GB. For details, see [Rawfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-rawfile). The development procedure is the same for the API ended with **64** and the one does not. For example, you can use **OH\_ResourceManager\_OpenRawFile** and **OH\_ResourceManager\_OpenRawFile64** in the same way.

#### Available APIs

| API | Description |
| :-- | :-- |
| NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr) | Initializes the native resource manager. |
| RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName) | Opens a raw file directory. |
| int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir) | Obtains the number of raw files in a directory. |
| const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index) | Obtains the name of a raw file. |
| RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName) | Opens a raw file. |
| long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile) | Obtains the size of a raw file. |
| int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length) | Reads a raw file. |
| void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile) | Closes a raw file to release resources. |
| void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir) | Closes a raw file directory to release resources. |
| bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor) | Obtains the file descriptor (FD) of a raw file. |
| void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr) | Releases the native resource manager. |
| bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path) | Checks whether a path is a subdirectory in the **rawfile** directory. |

For details about the APIs, see [rawfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-rawfile).

#### How to Develop

The following uses the ArkTS as an example to describe how to obtain the rawfile list, rawfile content, rawfile descriptor (**fd**, **offset**, and **length**), and determine whether the path of a rawfile is a subdirectory in the **rawfile** directory.

1.  Create a project on DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/qg97t76qTIai0wQV5EkqsA/en-us_image_0000002537925242.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE94E2EC2E75606F2EEC36AA8FD69E01DDED3F3EA825BFF2AE22FDCB3092F690)

1.  Add dependencies.

After the project is created, the **cpp** directory is created in the project directory. In the **cpp** directory, there are files such as **libentry/index.d.ts**, **hello.cpp**, and **CMakeLists.txt**.

1.  Open the **src/main/cpp/CMakeLists.txt** file, and add **librawfile.z.so** (rawfile dependency) and **libhilog\_ndk.z.so** (log dependency) to **target\_link\_libraries**.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
    
2.  Open the **src/main/cpp/types/libentry/index.d.ts** file and declare the ArkTS APIs **getFileList**, **getRawFileContent**, **getRawFileDescriptor**, and **isRawDir** in this file.
    
    import { resourceManager } from '@kit.LocalizationKit';
    export const getFileList: (resMgr: resourceManager.ResourceManager, path: string) => Array<String>;
    export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
    export const getRawFileDescriptor: (resMgr: resourceManager.ResourceManager, path: string) => resourceManager.RawFileDescriptor;
    export const isRawDir: (resMgr: resourceManager.ResourceManager, path: string) => boolean;
    
3.  Modify the source file.
    
4.  Open the **src/main/cpp/hello.cpp** file, and add the mapping between ArkTS APIs and C++ APIs in the **Init** method. The ArkTS APIs **getFileList**, **getRawFileContent**, **getRawFileDescriptor**, and **isRawDir** map to the C++ APIs **GetFileList**, **GetRawFileContent**, **GetRawFileDescriptor**, and **IsRawDir**, respectively.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "getFileList", nullptr, GetFileList, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "getRawFileContent", nullptr, GetRawFileContent, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "getRawFileDescriptor", nullptr, GetRawFileDescriptor, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "isRawDir", nullptr, IsRawDir, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
    
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
5.  Create the **hello.h** file in the **src/main/cpp/** directory and add the following four methods to the **hello.h** file:
    
    #ifndef RAWFILE\_HELLO\_H
    #define RAWFILE\_HELLO\_H
    
    #include <js\_native\_api.h>
    #include <js\_native\_api\_types.h>
    #include <string>
    #include <vector>
    #include <cstdlib>
    #include "napi/native\_api.h"
    
    napi\_value GetFileList(napi\_env env, napi\_callback\_info info);
    napi\_value GetRawFileContent(napi\_env env, napi\_callback\_info info);
    napi\_value GetRawFileDescriptor(napi\_env env, napi\_callback\_info info);
    napi\_value IsRawDir(napi\_env env, napi\_callback\_info info);
    
    #endif // RAWFILE\_HELLO\_H
    
6.  Implement the four APIs in the **hello.cpp** file. Obtain the JS **resourceManager** object through the specified **env** and **info**, and convert it into the native **resourceManager** object. Then, you can call the APIs of the native **resourceManager** object to implement resource management. The sample code is as follows:
    
    Import the header files.
    
    #include "hello.h"
    #include "rawfile/raw\_file\_manager.h"
    #include "rawfile/raw\_file.h"
    #include "rawfile/raw\_dir.h"
    #include "hilog/log.h"
    
    Declare the **DOMAIN** and **TAG** constants of HiLog.
    
    const int GLOBAL\_RESMGR = 0xFF00;
    const char \*TAG = "\[Sample\_rawfile\]";
    
    Examples:
    
    // Example 1: Use GetFileList to obtain the raw file list.
    napi\_value GetFileList(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest GetFileList Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // Obtain arguments of the native API.
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\] is the first parameter of the function, which is a JS resource object. The  OH\_ResourceManager\_InitNativeResourceManager function converts this JS resource object into a native object.
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        // Obtain argv\[1\], which specifies the relative path of the rawfile.
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string dirName(strBuf, strSize);
    
        // Obtain the corresponding rawDir pointer object.
        RawDir\* rawDir = OH\_ResourceManager\_OpenRawDir(mNativeResMgr, dirName.c\_str());
    
        // Obtain the number of files and folders in rawDir.
        int count = OH\_ResourceManager\_GetRawFileCount(rawDir);
    
        // Traverse rawDir to obtain the list of file names and save it.
        std::vector<std::string> tempArray;
        for (int i = 0; i < count; i++) {
            std::string filename = OH\_ResourceManager\_GetRawFileName(rawDir, i);
            tempArray.emplace\_back(filename);
        }
    
        // Convert the object to a JS array.
        napi\_value fileList;
        napi\_create\_array(env, &fileList);
        for (size\_t i = 0; i < tempArray.size(); i++) {
            napi\_value jsString;
            napi\_create\_string\_utf8(env, tempArray\[i\].c\_str(), NAPI\_AUTO\_LENGTH, &jsString);
            napi\_set\_element(env, fileList, i, jsString);
        }
    
        // Close the rawDir pointer object.
        OH\_ResourceManager\_CloseRawDir(rawDir);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        return fileList;
    }
    
    // Example 2: Use GetRawFileContent to obtain the content of the raw file.
    napi\_value CreateJsArrayValue(napi\_env env, std::unique\_ptr<uint8\_t\[\]> &data, long length)
    {
        // Create a JS ArrayBuffer object with external data.
        napi\_value buffer;
        napi\_status status = napi\_create\_external\_arraybuffer(env, data.get(), length,
            \[\](napi\_env env, void \*data, void \*hint) {
                delete\[\] static\_cast<char\*>(data);
            }, nullptr, &buffer);
        // Check whether the ArrayBuffer object is successfully created.
        if (status != napi\_ok) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create external array buffer");
            return nullptr;
        }
        // Create a JS TypedArray object and bind it to the TypedArray object.
        napi\_value result = nullptr;
        status = napi\_create\_typedarray(env, napi\_uint8\_array, length, buffer, 0, &result);
        if (status != napi\_ok) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create media typed array");
            return nullptr;
        }
        data.release();
        return result;
    }
    
    napi\_value GetRawFileContent(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "GetFileContent Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // Obtain arguments of the native API.
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\] is the first parameter of the function, which is a JS resource object. The  OH\_ResourceManager\_InitNativeResourceManager function converts this JS resource object into a native object.
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
    
        // Obtain the raw file pointer object.
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, filename.c\_str());
        if (rawFile != nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "OH\_ResourceManager\_OpenRawFile success");
        }
        // Obtain the size of the raw file and apply for memory.
        long len = OH\_ResourceManager\_GetRawFileSize(rawFile);
        std::unique\_ptr<uint8\_t\[\]> data = std::make\_unique<uint8\_t\[\]>(len);
    
        // Read all content of the raw file at a time.
        int res = OH\_ResourceManager\_ReadRawFile(rawFile, data.get(), len);
    
        // Close the rawDir pointer object.
        OH\_ResourceManager\_CloseRawFile(rawFile);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        // Convert the native object to a JS object.
        return CreateJsArrayValue(env, data, len);
    }
    
    // Example 3: Use GetRawFileDescriptor to obtain the FD of the raw file.
    // Define a function to convert RawFileDescriptor to a JS object.
    napi\_value createJsFileDescriptor(napi\_env env, RawFileDescriptor& descriptor)
    {
        // Create a JS object.
        napi\_value result;
        napi\_status status = napi\_create\_object(env, &result);
        if (status != napi\_ok) {
            return result;
        }
    
        // Save fd to the result object.
        napi\_value fd;
        status = napi\_create\_int32(env, descriptor.fd, &fd);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "fd", fd);
        if (status != napi\_ok) {
            return result;
        }
    
        // Save offset (file offset) to the result object.
        napi\_value offset;
        status = napi\_create\_int64(env, descriptor.start, &offset);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "offset", offset);
        if (status != napi\_ok) {
            return result;
        }
    
        // Save length (file length) to the result object.
        napi\_value length;
        status = napi\_create\_int64(env, descriptor.length, &length);
        if (status != napi\_ok) {
            return result;
        }
        status = napi\_set\_named\_property(env, result, "length", length);
        if (status != napi\_ok) {
            return result;
        }
        return result;
    }
    
    napi\_value GetRawFileDescriptor(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest GetRawFileDescriptor Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // Obtain arguments of the native API.
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\] is the first parameter of the function, which is a JS resource object. The  OH\_ResourceManager\_InitNativeResourceManager function converts this JS resource object into a native object.
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
        // Obtain the raw file pointer object.
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, filename.c\_str());
        if (rawFile != nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "OH\_ResourceManager\_OpenRawFile success");
        }
        // Obtain the FD of the rawfile, that is, RawFileDescriptor {fd, offset, length}.
        RawFileDescriptor descriptor;
        OH\_ResourceManager\_GetRawFileDescriptor(rawFile, descriptor);
        // Close the rawDir pointer object.
        OH\_ResourceManager\_CloseRawFile(rawFile);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        // Convert the native object to a JS object.
        return createJsFileDescriptor(env, descriptor);
    }
    
    // Example 4: Use IsRawDir to check whether the path is a subdirectory in the rawfile directory.
    napi\_value CreateJsBool(napi\_env env, bool &bValue)
    {
        napi\_value jsValue = nullptr;
        if (napi\_get\_boolean(env, bValue, &jsValue) != napi\_ok) {
            return nullptr;
        }
        return jsValue;
    }
    
    napi\_value IsRawDir(napi\_env env, napi\_callback\_info info)
    {
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, GLOBAL\_RESMGR, TAG, "NDKTest IsRawDir Begin");
        size\_t argc = 2;
        napi\_value argv\[2\] = { nullptr };
        // Obtain arguments of the native API.
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\] is the first parameter of the function, which is a JS resource object. The  OH\_ResourceManager\_InitNativeResourceManager function converts this JS resource object into a native object.
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        napi\_valuetype fileNameType;
        napi\_typeof(env, argv\[1\], &fileNameType);
        if (fileNameType == napi\_undefined || fileNameType == napi\_null) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "NDKTest file name is null");
            bool temp = false;
            return CreateJsBool(env, temp);
        }
        size\_t strSize;
        char strBuf\[256\];
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize);
        std::string filename(strBuf, strSize);
        // Check whether the path is a subdirectory in the rawfile directory.
        bool result = OH\_ResourceManager\_IsRawDir(mNativeResMgr, filename.c\_str());
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        return CreateJsBool(env, result);
    }
    

**4\. Calling ArkTS APIs**

1.  Open the **src\\main\\ets\\pages\\index.ets** file, and import **libentry.so**.
    
2.  Obtain intra-package resources and cross-package resources within an application and cross-application package resources.
    
    Call **context.resourceManager** to obtain a **resourceManager** object for intra-package resources within the application.
    
    Call **context.createModuleContext().resourceManager** to obtain a **resourceManager** object for cross-package resources within the application.
    
    For details about **Context**, see [Context (Stage Model)](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md).
    
3.  Call the APIs declared in **src/main/cpp/types/libentry/index.d.ts**. For example, call **getFileList** with the JS resource object and the relative path of the rawfile specified.
    
    Example: Obtain a **resourceManager** object for intra-package resources within the application.
    
    import { util } from '@kit.ArkTS';
    import { resourceManager } from '@kit.LocalizationKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so'; // Import the libentry.so file.
    
    const DOMAIN = 0x0000;
    const TAG = '\[Sample\_rawfile\]';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';
      private resMgr = this.getUIContext().getHostContext()?.resourceManager; // Obtain the resourceManager object for intra-package resources within the application.
      @State rawfileListMsg: string = 'FileList = ';
      @State retMsg: string = 'isRawDir = ';
      @State rawfileContentMsg: string = 'RawFileContent = ';
      @State rawfileDescriptorMsg: string = 'RawFileDescriptor.length = ';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .id('hello\_world')
              .fontSize(30)
              .fontWeight(FontWeight.Bold)
              .onClick(async () => {
                // Pass in the JS resource object and the relative path of the rawfile.
                let rawFileList: Array<String> = testNapi.getFileList(this.resMgr, '');
                this.rawfileListMsg = 'FileList = ' + rawFileList;
                hilog.info(DOMAIN, TAG, this.rawfileListMsg);
    
                // Replace 'sub\_rawfile' with the actual resource.
                let ret: boolean = testNapi.isRawDir(this.resMgr, 'sub\_rawfile');
                this.retMsg = 'isRawDir = ' + ret;
                hilog.info(DOMAIN, TAG, this.retMsg);
    
                // Pass in the JS resource object and the relative path of the rawfile.
                // Replace 'rawfile1.txt' with the actual resource.
                let rawfileArray: Uint8Array = testNapi.getRawFileContent(this.resMgr, 'rawfile1.txt');
                // Convert Uint8Array to a string.
                let textDecoder: util.TextDecoder = new util.TextDecoder();
                let rawfileContent: string = textDecoder.decodeToString(rawfileArray);
                this.rawfileContentMsg = 'RawFileContent = ' + rawfileContent;
                hilog.info(DOMAIN, TAG, this.rawfileContentMsg);
    
                // Pass in the JS resource object and the rawfile name.
                // Replace 'rawfile1.txt' with the actual resource.
                let rawfileDescriptor: resourceManager.RawFileDescriptor =
                  testNapi.getRawFileDescriptor(this.resMgr, 'rawfile1.txt');
                this.rawfileDescriptorMsg = 'RawFileDescriptor.length = ' + rawfileDescriptor.length;
                hilog.info(DOMAIN, TAG, this.rawfileDescriptorMsg);
              })
            Text(this.rawfileListMsg).id('get\_file\_list').fontSize(30);
            Text(this.retMsg).id('is\_raw\_dir').fontSize(30);
            Text(this.rawfileContentMsg).id('get\_raw\_file\_content').fontSize(30);
            Text(this.rawfileDescriptorMsg).id('get\_raw\_file\_descriptor').fontSize(30);
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

-   [Native Rawfile](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/NdkRawfile)
