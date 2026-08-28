# Does armeabi-v7a support Neon instruction extensions?

**Symptom**

An error occurs when CMake is used to compile the existing project with the armeabi-v7a architecture.

D:/DeveloperTools/Huawei/SDK/default/base/native/llvm/lib/clang/15.0.4/include/arm\_neon.h:28:2: error: "NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard" #error "NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard"

**Solution**

You can import the Neon instruction set as follows:

Add the following configuration items to **entry** > **build-profile.json5** > **externalNativeOptions** node:

"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  "arguments": "",
  "abiFilters": \[
    "x86\_64",
    "arm64-v8a"
  \],
  // This is a configuration item to be added
  "cppFlags": "-mfloat-abi=hard",
  // This is a configuration item to be added
},

Import the header file **#include <arm\_neon.h>**.
