# Setting the Service Scenario (C/C++)

Starting from version 6.0.2(22), this kit supports the function of setting the service scenario.

#### Use Case

You can set the service scenario for your app before requesting multi-network concurrency, so the device can manage multi-network concurrency and perform service duration analysis accordingly.

#### API Description

For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-boost-c-module).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_NetworkBoost\_SetSceneDesc(NetworkBoost\_SceneDesc sceneDesc)

 | 

Sets the service scenario.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    #include "NetworkBoostKit/network\_boost.h"
    #include <cstdio>
    
2.  Add the following library to the **CMakeLists.txt** file. For details, please refer to [Preparations for C API Development](../../preparations/document.md#section16821202143413).
    
    libnetwork\_boost.so
    
3.  Call the **SetSceneDesc()** API.
    
    int32\_t SetSceneDesc()
    {
        NetworkBoost\_SceneDesc sceneDesc;
        sceneDesc.duration = 0;
        sceneDesc.startTime = 0;
        sceneDesc.scene = NB\_SERVICE\_LOGIN;
        sceneDesc.sceneEvent = SCENE\_EVENT\_ENTER;
        int32\_t ret = HMS\_NetworkBoost\_SetSceneDesc(sceneDesc);
        printf("Service scenario setting result: %d\\n", ret);
        return ret;
    }
