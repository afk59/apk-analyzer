# How do I obtain information printed by printf in native code?

**Question**

How do I obtain the **stdout** and **stderr** information printed by the **printf** function provided by a third-party library? How do I view the standard logs printed by **fprintf** and **std::cout printf** in C/C++ when developing applications in ArkTS?

**Answer**

**cout/printf** is a print function provided by C/C++ and cannot be populated in hilog. You can redirect the logs to a file and obtain the print information.

Sample code:

Redirect the method body in native code.

#include "napi/native\_api.h" 
#include <hilog/log.h> 
#include <string> 
#include "iostream" 
#include "fstream" 
#define LOG\_TAG "Pure" 
 
static napi\_value Redirect(napi\_env env, napi\_callback\_info info) { 
    // Get the JS parameters of the function 
    size\_t argc = 1; 
    napi\_value argv\[1\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr); 
    // Resolve parameter 1, the destination directory for saving the file
    size\_t targetDirectoryNameSize; 
    char targetDirectoryNameBuf\[512\]; 
    napi\_get\_value\_string\_utf8(env, argv\[0\], targetDirectoryNameBuf, sizeof(targetDirectoryNameBuf), 
                               &targetDirectoryNameSize); 
    std::string targetDirectoryName(targetDirectoryNameBuf, targetDirectoryNameSize); // target directory 
    OH\_LOG\_INFO(LOG\_APP, "C++Received target path on the side === %{public}s", targetDirectoryNameBuf); 
    std::string targetSandboxPath = targetDirectoryName + "/Log.log"; // Saved file path 
     
    // Use the freopen function to associate files with standard output 
    FILE \*stdoutFile = NULL; 
    FILE \*stderrFile = NULL; 
    stdoutFile = freopen(targetSandboxPath.c\_str(), "a", stdout); 
    stderrFile = freopen(targetSandboxPath.c\_str(), "a", stderr); 
    if (NULL == stdoutFile || NULL == stderrFile) { 
        OH\_LOG\_INFO(LOG\_APP, "Recreate!"); 
        // Opening the file output stream of the sandbox file will create a file
        std::ofstream outputFile(targetSandboxPath, std::ios::binary); 
        if (!outputFile) { 
            OH\_LOG\_ERROR(LOG\_APP, "Unable to create target file!"); 
            return nullptr; 
        } 
        stdoutFile = freopen(targetSandboxPath.c\_str(), "a", stdout); 
        stderrFile = freopen(targetSandboxPath.c\_str(), "a", stderr); 
        if (NULL == stdoutFile || NULL == stderrFile) { 
            OH\_LOG\_ERROR(LOG\_APP, "fail!"); 
            return nullptr; 
        } 
    } 
    OH\_LOG\_WARN(LOG\_APP, "redirect!"); 
    printf("\\n\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Redirect dividing line\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\n"); 
    return 0; 
}

Call and pass the path from ArkTS.

Call **redirect** in **onCreate()** of EntryAbility.

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  let file : string = this.context.getApplicationContext().filesDir;
  testNapi.redirect(file);
  hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
}
