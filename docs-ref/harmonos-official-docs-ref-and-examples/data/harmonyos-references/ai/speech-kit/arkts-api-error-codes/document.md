# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/QyhP_hAAQnm2AV-_hslyRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062525Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8C113DF4532A352F134E151178EB60CA5BB683A8445634E706DA0853ABD47D7)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

#### 201 Permission Verification Failed

**Message**

Permission denied.

**Description**

Permission verification failed.

**Possible causes**

The **ohos.permission.KEEP\_BACKGROUND\_RUNNING** permission is not configured.

**Solution**

Configure the related permission and try again.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 401 Parameter Check Failed

**Message**

Parameter error.

**Description**

Parameter check failed.

**Possible causes**

A mandatory parameter is not passed, or a parameter type is incorrect.

**Solution**

Verify that mandatory parameters are passed and the parameter types are correct.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600011 Initialization Failed

**Message**

Initialize failed.

**Description**

The TextReader initialization failed.

**Possible causes**

1.  Failed to initialize the TTS engine or player.
2.  Some device models are not supported.

**Solution**

1.  For PCs, you need to call [setWindowStage](../arkts-apis/windowmanager-window-management/document.md#section6867019205916) before initialization when launching the reading details page. For other types of devices, skip this step.
2.  Check whether the initialization has been performed. Repeated initialization will cause this error.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600012 Not Initialized

**Message**

The TextReader is not initialized.

**Description**

Not Initialized.

**Possible causes**

The TextReader is not initialized when called for playback.

**Solution**

Call the [init](../arkts-apis/textreader-reading-control/document.md#section173751154134515) method to initialize the TextReader.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600013 TTS Audio Synthesis Error

**Message**

Text-to-speech engine error.

**Description**

TTS audio synthesis error.

**Possible causes**

Abnormal audio synthesis on the TTS engine side.

**Solution**

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600014 Player Error

**Message**

AudioRenderer play error.

**Description**

Player error.

**Possible causes**

The AudioRenderer player encountered an error.

**Solution**

Verify that the format and content of the **readInfoList** parameter are correct.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600015 Decoding Error

**Message**

Audio decode error.

**Description**

Decoding error.

**Possible causes**

Audio decoding failed on the TTS engine side.

**Solution**

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600016 Media Controller Synchronization Error

**Message**

AVSession error.

**Description**

Media controller synchronization error.

**Possible causes**

An error occurs when the AVSession media controller synchronizes the cover image or playback status.

**Solution**

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600017 Other Errors

**Message**

Other error.

**Description**

Other errors.

**Possible causes**

There was an exception caused by other factors.

**Solution**

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600018 Failed to Play the Previous Track

**Message**

playPrev failed.

**Description**

Failed to play the previous track.

**Possible causes**

Abnormal data.

**Solution**

Verify that the **readInfo** parameter of the previous track is correct.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600019 Failed to Play the Next Track

**Message**

playNext failed.

**Description**

Failed to play the next track.

**Possible causes**

Abnormal data.

**Solution**

Verify that the **readInfo** parameter of the next track is correct.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1010600020 Abnormal Release

**Message**

Release error.

**Description**

Failed to release TextReader resources.

**Possible causes**

Resources failed to be released.

**Solution**

Set a delay and call the **release** API again.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1012900010 AI Caption Service Is Busy

**Message**

AI caption service is busy.

**Description**

The AI caption service is busy.

**Possible causes**

The AI caption service is busy.

**Solution**

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1012900011 AI Caption Controller Initialization Failed

**Message**

AI caption controller initialized failed.

**Description**

AI caption controller initialization failed.

**Possible causes**

The AI caption controller failed to be initialized.

**Solution**

Check whether other apps are using the caption tool.

You are advised to [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1012900012 Audio Recognition Failed

**Message**

Audio recognition failed.

**Description**

Audio recognition failed.

**Possible causes**

An error occurred during the AI-based audio recognition.

**Solution**

1.  Check whether the input audio is less than 640 bytes or greater than 1280 bytes.
2.  Check whether the AI engine is successfully initialized.

If the issue persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
