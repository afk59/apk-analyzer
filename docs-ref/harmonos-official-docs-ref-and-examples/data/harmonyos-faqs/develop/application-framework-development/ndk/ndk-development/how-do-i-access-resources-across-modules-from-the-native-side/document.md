# How do I access resources across modules from the native side?

**Solution**

You can use **createModuleContext(moduleName)** to create contexts of different modules in the same application. After obtaining the **resourceManager** object, you can use the native RawFile APIs to access resources across modules.

The procedure is as follows:

1.  Add the **librawfile.z.so** dependency to the **CMakeLists.txt** file.
    
    target\_link\_libraries(nativecrossmoduleaccessres PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
    
2.  In the **src/main/cpp/types/libentry/index.d.ts** file, declare the application function **getRawFileContent**.
    
    import { resourceManager } from "@kit.LocalizationKit";
    export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
    
3.  Implement the function code in the **napi\_init.cpp** file.
    
    #include <memory>
    #include "string"
    #include "napi/native\_api.h" 
    #include <rawfile/raw\_file.h> 
    #include <rawfile/raw\_file\_manager.h> 
    #include "hilog/log.h" 
     
    const int GLOBAL\_RESMGR = 0xFF00; 
    const char \*TAG = "\[Sample\_rawfile\]"; 
    namespace { 
        napi\_value CreateJsArrayValue(napi\_env env, std::unique\_ptr<uint8\_t\[\]> &data, long length) 
        { 
            napi\_value buffer; 
            napi\_status status = napi\_create\_external\_arraybuffer( 
                env, data.get(), length, 
                \[\](napi\_env env, void \*data, void \*hint) { 
                    delete\[\] static\_cast<char \*>(data); 
                }, 
                nullptr, &buffer); 
            if (status != napi\_ok) { 
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create external array buffer"); 
                return nullptr; 
            } 
            napi\_value result = nullptr; 
            status = napi\_create\_typedarray(env, napi\_uint8\_array, length, buffer, 0, &result); 
            if (status != napi\_ok) { 
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "Failed to create media typed array"); 
                return nullptr; 
            } 
            data.release(); 
            return result; 
        } 
    } 
    static napi\_value GetRawFileContent(napi\_env env, napi\_callback\_info info) 
    { 
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "GetFileContent Begin"); 
        size\_t requireArgc = 3; 
        size\_t argc = 2; 
        napi\_value argv\[2\] = { nullptr }; 
        // Obtain parameter information 
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr); 
        // argv\[0\] is the first parameter of the function, the js resource object. OH\_ResourceManager\_InitNativeResourceManager convert to Native object. 
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]); 
        size\_t strSize; 
        char strBuf\[256\]; 
        napi\_get\_value\_string\_utf8(env, argv\[1\], strBuf, sizeof(strBuf), &strSize); 
        std::string filename(strBuf, strSize); 
        // Get rawfile pointer object 
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, filename.c\_str()); 
        if (rawFile != nullptr) { 
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, GLOBAL\_RESMGR, TAG, "OH\_ResourceManager\_OpenRawFile success"); 
        } 
        // Obtain the size of the rawfile and allocate memory 
        long len = OH\_ResourceManager\_GetRawFileSize(rawFile); 
        std::unique\_ptr<uint8\_t\[\]> data= std::make\_unique<uint8\_t\[\]>(len); 
        // Read the entire content of the rawfile one-off 
        int res = OH\_ResourceManager\_ReadRawFile(rawFile, data.get(), len); 
        // Close the open pointer object  
        OH\_ResourceManager\_CloseRawFile(rawFile); 
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr); 
        // Convert to js object  
        return CreateJsArrayValue(env, data, len);
    }
    
4.  Call the function code from ArkTS. The resource object needs to be passed in here.
    
    import { application } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import testNapi from 'libnativecrossmoduleaccessres.so';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Native Cross Module Access Resource';
    
      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                application.createModuleContext(this.getUIContext().getHostContext(), 'NativeAccessRes')
                  .then((data: Context) => {
                    if (data) {
                      let rawfileContext: Uint8Array = testNapi.getRawFileContent(data.resourceManager, 'rawfile.txt');
                      console.log("rawfileContext" + rawfileContext);
                    }
                  })
                  .catch((error: BusinessError) => {
                    let code: number = (error as BusinessError).code;
                    let message: string = (error as BusinessError).message;
                    console.error(\`createModuleContext failed, error.code: ${code}, error.message: ${message}\`);
                  })
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

**Reference**

[Raw File Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/rawfile-guidelines)
