# What should I do if "platform/OHOS to use this system, please post your config file on discourse.cmake.org so it can be added to cmake" is reported?

**Symptom**

Multiple warnings are reported during the compilation of the C++ library.

To use this system, release the configuration file to **discourse.cmake.org**.

Does this have any impact?

**Solution**

The problem is caused by the missing **OHOS.cmake** file in the SDK of macOS.

You need to create a **OHOS.cmake** file in the **default/base/native/build-tools/cmake/share/cmake-3.16/Modules/Platform** directory of the SDK and write **include(Platform/Linux)** in the file.
