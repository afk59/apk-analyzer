# UDMF Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/pY-62JaoTQWT1S_BlZ2DjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062221Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A98614E4AD1300F2B8396F578EC75A82746235FDA585674F0E7FFB213CC84140)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 20400001 Settings Already Exist

**Error Message**

Settings already exist. To reconfigure, remove the existing sharing options.

**Description**

The data to be set by **setAppShareOptions()** already exists.

**Possible Causes**

This error code is reported when [setAppShareOptions](../../arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddatachannelsetappshareoptions14) is called repeatedly to set **ShareOptions** of the drag-and-drop channel data.

**Solution**

Call [removeAppShareOptions](../../arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddatachannelremoveappshareoptions14) to clear the **ShareOptions** of the current drag-and-drop channel data, and then call [setAppShareOptions](../../arkts-apis/ohos-data-unifieddatachannel-unified-data-channel/document.md#unifieddatachannelsetappshareoptions14) to set **ShareOptions**.
