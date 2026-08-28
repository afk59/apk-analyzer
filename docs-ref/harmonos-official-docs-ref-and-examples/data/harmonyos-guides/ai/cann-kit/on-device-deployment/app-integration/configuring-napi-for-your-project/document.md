# Configuring NAPI for Your Project

When compiling the HAP, add build dependencies **libneural\_network\_core.so** and **libhiai\_foundation.so** in the NDK for the .so files at the NAPI layer.

#### Including Header Files

Include the header files of [NNCore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neuralnetworkruntime) and [CANN Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit-hiai-aipp-param-8h) as needed.

#include "neural\_network\_runtime/neural\_network\_core.h"
#include "CANNKit/hiai\_options.h"

#### Compiling CMakeLists.txt

The sample code for compiling **CMakeLists.txt** is as follows:

\# the minimum version of CMake.
cmake\_minimum\_required(VERSION 3.4.1)
project(CANNDemo)

set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})

include\_directories(${NATIVERENDER\_ROOT\_PATH}
                    ${NATIVERENDER\_ROOT\_PATH}/include)

include\_directories(${HMOS\_SDK\_NATIVE}/sysroot/usr/lib)
FIND\_LIBRARY(cann-lib hiai\_foundation)

add\_library(entry SHARED Classification.cpp HIAIModelManager.cpp)

target\_link\_libraries(entry PUBLIC libace\_napi.z.so
    libhilog\_ndk.z.so
    librawfile.z.so
    ${cann-lib}
    libneural\_network\_core.so
    )
