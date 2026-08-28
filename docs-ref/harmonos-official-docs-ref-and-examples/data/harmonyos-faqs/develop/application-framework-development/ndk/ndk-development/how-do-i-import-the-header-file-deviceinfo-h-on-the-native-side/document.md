# How do I import the header file deviceinfo.h on the native side?

**Symptom**

After the **deviceinfo.h** file is included in the C++ file, it cannot be found during compilation. The log indicates that the deviceinfo library is not linked.

**Solution**

Currently, the public SDK does not contain the **deviceinfo.h** header file. This header file can be used only in the full SDK. In addition, the header file can be found only after the **libdeviceinfo\_ndk.z.so** library is added to **CMakeLists.txt** as follows:

\# CMakeLists.txt
# ...
target\_link\_libraries(cpplib PUBLIC libace\_napi.z.so libdeviceinfo\_ndk.z.so)
