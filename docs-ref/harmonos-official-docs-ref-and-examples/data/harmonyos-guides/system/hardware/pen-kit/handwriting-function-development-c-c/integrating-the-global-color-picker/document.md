# Integrating the Global Color Picker

After the global color picker is integrated, users can use their finger or stylus to pick up an onscreen color after they lift the finger or stylus. The image information corresponding to the color value is generated.

#### Use Case

Use the global color picker in the app. The effect is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/auXlfk91SbOob_5YBOKhQA/en-us_image_0000002535542347.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2610845A834EE45C6B6F789488FFD21591E45184A205C9568379EB22B1140263 "Click to enlarge")

The color value and color gamut of the selected position on the screen can be obtained.

#### Restrictions

The global color picker capability supports tablets and PCs/2-in-1 devices. Starting from version 5.1.1(19), phones (only some models) are also supported.

#### API Description

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t [HMS\_GCP\_StartColorPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker-c#ga4c202f3df255013b9920f26027065176) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker-c#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker. This API is used to start the color picker. The color value is not displayed when the color picker is moved.

 |
| 

int32\_t [HMS\_GCP\_StartColorPickerWithColorValue](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker-c#ga8b044a1cfcd3b6eb8461e70c66d2c578) (int32\_t initialPosX, int32\_t initialPosY, [HMS\_GCP\_OnResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-imagefeaturepicker-c#gac06acd25757a5a72f4f8d0aec5821a52) onResultCallback, void \*userData)

 | 

Starts the global color picker. This API is used to start the color picker. The color value is displayed when the color picker is moved.

 |

#### Integration Procedure

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libcolorpicker\_ndk.z.so  libhilog\_ndk.z.so)

## Module Import

#include "color\_picker/native\_gcp\_api.h"
#include "hilog/log.h"

## Sample Code

**native\_gcp\_api.h** provides two methods, **HMS\_GCP\_StartColorPicker()** and **HMS\_GCP\_StartColorPickerWithColorValue()**, to start the global color picker.

Call **HMS\_GCP\_StartColorPicker()** to start the color picker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/4DdZ0BT4R3e5elkALmatwQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B61A9067CD8C864A0EC6733367B584D36A68DBB0ECC544B326E84ED39A7FC43F)

This method does not support real-time color value display.

void onSuccessCallback(void \*userData, HMS\_GCP\_PickedColorInfo pickedColorInfo, const int32\_t code) {
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked code is: %{public}d", code);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Red is: %{public}d", pickedColorInfo.color.red);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Green is:%{public}d ", pickedColorInfo.color.green);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Blue is: %{public}d", pickedColorInfo.color.blue);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Alpha is:%{public}d ", pickedColorInfo.color.alpha);
    delete userData;
}
void startPick() {
    int32\_t posX = 200;
    int32\_t posY = 200;
    void \*userData = nullptr;
    HMS\_GCP\_StartColorPicker(posX, posY, onSuccessCallback, userData);
}

Call **HMS\_GCP\_StartColorPickerWithColorValue()** to start the color picker.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/zM_RDRnkQ3G6VaKU5__03Q/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D45DC36D7F69BB763689D58EDCAB14B86A37502BB9CA86D541D2967DBB101527)

This method supports real-time color value display.

void onSuccessCallback(void \*userData, HMS\_GCP\_PickedColorInfo pickedColorInfo, const int32\_t code) {
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked code is: %{public}d", code);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Red is: %{public}d", pickedColorInfo.color.red);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Green is:%{public}d ", pickedColorInfo.color.green);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Blue is: %{public}d", pickedColorInfo.color.blue);
    OH\_LOG\_Print(LOG\_APP, LOG\_INFO, 0x0000, "penkit", "picked Alpha is:%{public}d ", pickedColorInfo.color.alpha);
    delete userData;
}
void startPickWithColorValue() {
    int32\_t posX = 200;
    int32\_t posY = 200;
    void \*userData = nullptr;
    HMS\_GCP\_StartColorPickerWithColorValue(posX, posY, onSuccessCallback, userData);
}
