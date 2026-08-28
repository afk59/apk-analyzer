# Managing AR Sessions

#### Overview

For any AR app, an AR session ([AREngine\_ARSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga2dbf3585f50628750ec855501c043650)) needs to be created in the first place for managing the system status of AR Engine.

#### Importing AR Engine

1.  Import the header file.
    
    #include "ar/ar\_engine\_core.h" 
    
2.  Compile **CMakeLists.txt**.
    
    find\_library(
        # Sets the name of the path variable.
        arengine-lib
        # Specifies the name of the NDK library that
        # you want CMake to locate.
        libarengine\_ndk.z.so
    )
    
    target\_link\_libraries(entry PUBLIC
        ${arengine-lib}
    )
    

#### Creating an AR Session

Call [HMS\_AREngine\_ARSession\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga47713cb18234569e03b5216b6c8442d3) to create an AR session when the app process starts.

AREngine\_ARSession \*arSession = nullptr;
HMS\_AREngine\_ARSession\_Create(nullptr, nullptr, &arSession);

#### Customizing the AR Session

Create an [AREngine\_ARConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#gab0b32ef6018535fd30000f4b6d65f619) object to configure the current AR session. The default configuration applies if you do not configure it. For details, please refer to [HMS\_AREngine\_ARConfig\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga97376432184fe702f2451e32b52298fb).

// Create a configuration object with a proper default configuration.
AREngine\_ARConfig \*arConfig = nullptr;
HMS\_AREngine\_ARConfig\_Create(arSession, &arConfig);

// Set **arConfig**.

// Configure the **AREngine\_ARSession** session.
HMS\_AREngine\_ARSession\_Configure(arSession, arConfig);

// Release the memory used by the specified configuration object.
HMS\_AREngine\_ARConfig\_Destroy(arConfig);

For details about each configurable item, please refer to [AR Engine API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi).

#### Destroying the AR Session

Call [HMS\_AREngine\_ARSession\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arengine-capi-arengine#ga3a2be9998c9cd6373ff1f5209b645a95) to destroy the current AR session when the app process ends.

HMS\_AREngine\_ARSession\_Destroy(arSession);
