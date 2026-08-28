# Integrating Point Prediction

Starting from version 6.0.0(20), the point prediction capability supports C APIs.

After point prediction is integrated, you can reduce the latency during drawing and writing in your app and improve stylus writing experience.

#### Use Case

Obtain a touch event on the custom screen of the app, and call the point prediction API to obtain the location information of the next predicted point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/LffmODY8Tr6QOaDGM8T_lg/en-us_image_0000002503702340.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD2355FDA9C454609F6C19160639281A738C4B8E3EA2A11E8C4CFA69EF769E7A "Click to enlarge")

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_HandWrite\_GetPredictPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-handwrite-c#section3513132112183)(const [HandWrite\_HistoricalPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-handwrite-struct-historicalpoint) \*event, int32\_t size, float \*predictPointX, float \*predictPointY)

 | 

Obtains a prediction point.

 |

#### Integration Procedure

Historical points need to be obtained by registering touch event callbacks on the custom rendering component (XComponent). For details about how to obtain historical touch points, please refer to [Custom Rendering (XComponent)](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/adding-a-component/custom-rendering-xcomponent/document.md).

## Linking the Dynamic Library in the CMake Script

target\_include\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/include) # Add this command if the header file of the point prediction API is missing during compilation.
target\_link\_directories(entry PUBLIC ${HMOS\_SDK\_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos) # Add this command if a point prediction API link exception occurs during compilation.
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libhandwrite\_ndk.z.so)

## Module Import

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <handwrite/native\_handwrite\_api.h>
#include <hilog/log.h>

## Sample Code

[native\_handwrite\_api.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-handwrite-headerfile-declare) provides the **HMS\_HandWrite\_GetPredictPoint()** API to obtain prediction points.

#include <ace/xcomponent/native\_interface\_xcomponent.h>
#include <handwrite/native\_handwrite\_api.h>
#include <hilog/log.h>

void DispatchTouchEvent(OH\_NativeXComponent \*xcomponent, void \*window)
{
    int32\_t historicalPointSize = 0;
    OH\_NativeXComponent\_HistoricalPoint \*historicalPoints = nullptr;
    if (OH\_NativeXComponent\_GetHistoricalPoints(xcomponent, window, &historicalPointSize, &historicalPoints) !=
        OH\_NATIVEXCOMPONENT\_RESULT\_SUCCESS) {
        OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, 0x0000, "PenKit", "failed to get historical points");
        return;
    }

    std::vector<HandWrite\_HistoricalPoint> handWriteHisPoints(historicalPointSize);
    for (int32\_t i = 0; i < historicalPointSize; ++i) {
        handWriteHisPoints\[i\].x = historicalPoints\[i\].x;
        handWriteHisPoints\[i\].y = historicalPoints\[i\].y;
        handWriteHisPoints\[i\].timeStamp = historicalPoints\[i\].timeStamp;
        handWriteHisPoints\[i\].force = historicalPoints\[i\].force;
    }

    float predictPointX = 0.0f;
    float predictPointY = 0.0f;
    int32\_t errcode = HMS\_HandWrite\_GetPredictPoint(handWriteHisPoints.data(), historicalPointSize, &predictPointX, &predictPointY);

    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "PenKit", "error code is %{public}d", errcode);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "PenKit", "predict point is (%{public}f, %{public}f)", predictPointX, predictPointY);
}
