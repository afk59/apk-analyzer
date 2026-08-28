# Obtaining Device Location Information (C/C++)

#### When to Use

You can call location-related APIs to listen for device location changes.

#### Function Description

| Name | Description |
| :-- | :-- |
| OH\_Location\_IsLocatingEnabled(bool\* enabled) | Checks whether the location switch is enabled. |
| OH\_Location\_StartLocating(const Location\_RequestConfig\* requestConfig) | Starts locating and subscribes to location changes. |
| Location\_ResultCode OH\_Location\_StopLocating(const Location\_RequestConfig\* requestConfig) | Stops locating and unsubscribes from location changes. |
| OH\_LocationInfo\_GetBasicInfo(Location\_Info\* location) | Obtains basic information from the location result, such as the longitude, latitude, altitude, and speed. |
| OH\_LocationInfo\_GetAdditionalInfo(Location\_Info\* location, char\* additionalInfo, uint32\_t length) | Obtains additional information from the location result. The additional information is a string in JSON format. |
| OH\_Location\_CreateRequestConfig(void) | Creates a **Location\_RequestConfig** instance. |
| OH\_Location\_DestroyRequestConfig(Location\_RequestConfig\* requestConfig) | Destroys the **Location\_RequestConfig** instance and reclaims the memory. |
| OH\_LocationRequestConfig\_SetUseScene(Location\_RequestConfig\* requestConfig, Location\_UseScene useScene) | 
Sets the user activity scenario in a location request.

If **useScene** is set, **powerConsumptionScene** is invalid.

Otherwise, **powerConsumptionScene** takes effect.

If neither of the two parameters is set, **useScene** is defaulted to **LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE**, and **powerConsumptionScene** is invalid.

 |
| OH\_LocationRequestConfig\_SetPowerConsumptionScene(Location\_RequestConfig\* requestConfig, Location\_PowerConsumptionScene powerConsumptionScene) | Sets the power consumption scenario in a location request. |
| OH\_LocationRequestConfig\_SetInterval(Location\_RequestConfig\* requestConfig, int interval) | Sets the interval for reporting location results. |
| OH\_LocationRequestConfig\_SetCallback(Location\_RequestConfig\* requestConfig, Location\_InfoCallback callback, void\* userData) | Sets the callback for receiving reported location information. |

#### How to Develop

1.  Create a native C++ project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/w-Ub-uyJQleupx7aMvTeTQ/en-us_image_0000002568764995.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2B97B4143A7E758C68D9A6D09833C90ECBF4B65D4CC1A70457F2714E02D15E6)
    
2.  Before using system basic location capabilities, check whether your application has been granted the permission to access the device location information. If not, your application first needs to apply for the required permission. For details, see [Applying for Location Permissions](../applying-for-location-permissions-arkts/document.md).
    
3.  Add the dynamic dependency libraries into the **CMakeLists.txt** file.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC liblocation\_ndk.so)
    
4.  Write the **napi\_init.cpp** file to import related modules.
    
    #include "napi/native\_api.h"
    #include "LocationKit/oh\_location.h"
    #include "LocationKit/oh\_location\_type.h"
    #include "hilog/log.h"
    #include <stdlib.h>
    
5.  Call **isLocationEnabled** to check whether the location switch is enabled.
    
    The return result is a Boolean value. The value **true** indicates that the location switch is enabled, and the value **false** indicates the opposite.
    
     static napi\_value OhLocationIsEnabled(napi\_env env, napi\_callback\_info info)
     {
         bool isEnabled = false;
         int resultCode = OH\_Location\_IsLocatingEnabled(&isEnabled);
         napi\_value result = NULL;
         napi\_get\_boolean(env, isEnabled, &result);
         return result;
     }
     // Add related APIs to the Init function.
     EXTERN\_C\_START
     static napi\_value Init(napi\_env env, napi\_value exports)
     {
         napi\_property\_descriptor desc\[\] = {
             {"ohLocationIsEnabled", NULL, OhLocationIsEnabled, NULL, NULL, NULL, napi\_default, NULL},
         };
         napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
         return exports;
     }
     EXTERN\_C\_END
    
6.  Start positioning and subscribe to location changes.
    
    // Define a location request.
    struct Location\_RequestConfig \*g\_requestConfig = NULL;
    void \*mydata = NULL;
    
    // Define a callback to receive location information.
    void reportLocation(Location\_Info\* location, void\* userData)
    {
        Location\_BasicInfo baseInfo = OH\_LocationInfo\_GetBasicInfo(location);
        char additionalInfo\[1024\] = "";
        Location\_ResultCode result = OH\_LocationInfo\_GetAdditionalInfo(location, additionalInfo, sizeof(additionalInfo));
        if (mydata == userData) {
         OH\_LOG\_INFO(LOG\_APP, "userData is mydata");
        }
        return;
    }
    
    // Subscribe to location information.
    static napi\_value OhLocationStartLocating(napi\_env env, napi\_callback\_info info)
    {
        if (g\_requestConfig == NULL) {
         g\_requestConfig = OH\_Location\_CreateRequestConfig();
        }
        OH\_LocationRequestConfig\_SetUseScene(g\_requestConfig, LOCATION\_USE\_SCENE\_NAVIGATION);
        OH\_LocationRequestConfig\_SetInterval(g\_requestConfig, 1);
        mydata = (void \*)malloc(sizeof("mydata")); // Custom data, which is transparently returned through callback.
        OH\_LocationRequestConfig\_SetCallback(g\_requestConfig, reportLocation, mydata);
        OH\_Location\_StartLocating(g\_requestConfig);
        int32\_t ret = 0;
        napi\_value result = NULL;
        napi\_create\_int32(env, ret, &result);
        return result;
    }
    
    // Unsubscribe from location information. The value of g\_requestConfig must be the same as the object passed during subscription.
    static napi\_value OhLocationStopLocating(napi\_env env, napi\_callback\_info info)
    {
        OH\_Location\_StopLocating(g\_requestConfig);
        if (g\_requestConfig != NULL) {
            OH\_Location\_DestroyRequestConfig(g\_requestConfig);
            g\_requestConfig = NULL;
        }
        free(mydata);
        mydata = NULL;
        int32\_t ret = 0;
        napi\_value result = NULL;
        napi\_create\_int32(env, ret, &result);
        return result;
    }
    
    // Add related APIs to the Init function.
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"ohLocationStartLocating", NULL, OhLocationStartLocating, NULL, NULL, NULL, napi\_default, NULL},
            {"ohLocationStopLocating", NULL, OhLocationStopLocating, NULL, NULL, NULL, napi\_default, NULL},
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
7.  Introduce the NAPI APIs to the **index.d.ts** file in **types/libentry**.
    
        export const ohLocationIsEnabled: () => boolean;
        export const ohLocationStartLocating: () => number;
        export const ohLocationStopLocating: () => number;
    
8.  Delete deprecated functions from the **Index.ets** file.
    
    .onClick(() => {
        hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
    })
