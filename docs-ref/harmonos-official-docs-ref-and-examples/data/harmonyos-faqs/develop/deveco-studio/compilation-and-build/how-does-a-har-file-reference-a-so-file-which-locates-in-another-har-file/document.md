# How does a HAR file reference a .so file which locates in another HAR file?

You can export the .so library to the **libs** directory and add the following code to the **CMakeLists.txt** file. For example, a **libnativeSub.so** is added to the .har file in the sample code.

target\_link\_directories(entry PUBLIC ${CMAKE\_CURRENT\_SOURCE\_DIR}/../../../libs/${OHOS\_ARCH}/)
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libc++.a libnativeSub.so)
