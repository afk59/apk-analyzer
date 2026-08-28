# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/WNrcGYz6Tj6v5pfCc57pDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062522Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4E9C0AADB32E03E420993D07A1575CF4F1C83A19D29DCB6B8F9F20651FE7514)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1002200001 Engine Creation Failed

**Message**

Create engine failed.

**Description**

Engine creation failed.

**Possible causes**

1.  The language is not supported.
2.  The mode is not supported.
3.  The needed resource does not exist, or the initialization times out.

**Solution**

1.  Call the [listLanguages](../speechrecognizer-speech-recognition/document.md#section813761871119) method to query the supported languages. Then try again.
2.  Confirm the mode (only [CreateEngineParams](../speechrecognizer-speech-recognition/document.md#section1638144844811) is supported currently) and try again.
3.  If the needed resource does not exist or the initialization times out, try again later.

#### 1002200002 Failed to Start Recognition

**Message**

Start listening failed.

**Description**

Failed to start recognition.

**Possible causes**

Speech recognition has already been started and is started again.

**Solution**

Check whether speech recognition has been started. Do not start it repeatedly.

#### 1002200003 Audio Too Long

**Message**

Exceeded the maximum audio length supported.

**Description**

The audio length exceeds the maximum.

**Possible causes**

The audio length exceeds the maximum.

**Solution**

It is recommended that the audio not exceed 60,000 ms. Adjust the length and try again.

#### 1002200004 Failed to End Recognition

**Message**

Finish recognition failed.

**Description**

Failed to end recognition.

**Possible causes**

No recognition task exists.

**Solution**

Call the [startListening](../speechrecognizer-speech-recognition/document.md#section140216144119) method to start the speech recognition task and try again.

#### 1002200005 Failed to Cancel Recognition

**Message**

Cancel recognition failed.

**Description**

Failed to cancel recognition.

**Possible causes**

No recognition task exists.

**Solution**

Call the [startListening](../speechrecognizer-speech-recognition/document.md#section140216144119) method to start the speech recognition task and try again.

#### 1002200006 Service Busy

**Message**

The engine of SpeechRecognition is busy.

**Description**

The recognition service is busy.

**Possible causes**

The engine is performing a recognition task.

**Solution**

Call the [isBusy](../speechrecognizer-speech-recognition/document.md#section35361720111113) method to query the service status and try again when the service is idle.

#### 1002200007 Engine Not Initialized

**Message**

The engine is not initialized.

**Description**

The engine has not been initialized.

**Possible causes**

The engine has not been initialized.

**Solution**

Call the [speechRecognizer.createEngine](../speechrecognizer-speech-recognition/document.md#section53411946183318) method to initialize the engine and try again.

#### 1002200008 Engine Destroyed

**Message**

The engine of SpeechRecognition is being destroyed.

**Description**

The engine has been destroyed.

**Possible causes**

The engine has been destroyed.

**Solution**

Call the [speechRecognizer.createEngine](../speechrecognizer-speech-recognition/document.md#section53411946183318) method to initialize the engine and try again.

#### 1002200009 Internal Service Error

**Message**

Internal Service Error.

**Description**

Internal service error.

**Possible causes**

An internal service error occurred, preventing the engine function from being called.

**Solution**

Rectify the fault based on the error information.

If the fault persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1002200010 Speech Recognition Not Started

**Message**

Write audio failed because the start listening is failed.

**Description**

The engine has not started recognition.

**Possible causes**

The engine has not started recognition.

**Solution**

Call the [startListening](../speechrecognizer-speech-recognition/document.md#section140216144119) method to start the speech recognition task and try again.

#### 1002200011 Speech Recognition Exception

**Message**

Error in recognition.

**Description**

An exception occurs during speech recognition.

**Possible causes**

The engine encounters an exception during speech recognition.

**Solution**

Call the [startListening](../speechrecognizer-speech-recognition/document.md#section140216144119) method again.

#### 1002200012 No Microphone Permission

**Message**

AudioCapturer create failed, please check the permission of MICROPHONE.

**Description**

Failed to create [AudioCapturer](../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/interface-audiocapturer/document.md). Ensure that the microphone permission has been obtained.

**Possible causes**

No microphone permission is obtained.

**Solution**

Check whether the microphone permission can be obtained. For details, please refer to the speech recognition part in the [Development Guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#li1723555443715).

#### 1002300001 Invalid Text Length

**Message**

The length of text is out of range or empty.

**Description**

Invalid text length.

**Possible causes**

The text length is 0 or exceeds 10,000 characters.

**Solution**

Modify the text and try again.

#### 1002300002 Unsupported Language

**Message**

The language is not supported.

**Description**

The language is not supported.

**Possible causes**

An unsupported language is used.

**Solution**

Call the [listVoices](../texttospeech-text-to-speech/document.md#section125219451411) method to query the supported languages. Use a supported language and try again.

#### 1002300003 Unsupported Timbre

**Message**

The person is not supported.

**Description**

The timbre is not supported.

**Possible causes**

An unsupported timbre is used.

**Solution**

Call the [listVoices](../texttospeech-text-to-speech/document.md#section125219451411) method to query the supported timbres. Use a supported timbre and try again.

#### 1002300005 Engine Creation Failed

**Message**

Create engine failed.

**Description**

Engine creation failed.

**Possible causes**

1\. The engine service is abnormal.

2\. Failed to load engine resources.

**Solution**

Try again later.

#### 1002300008 Failed to Download a Timbre

**Message**

Failed to download voice.

**Description**

The API provided by the TTS capability for downloading a timbre does not work.

**Possible causes**

The network is unavailable, or an internal service error occurs.

**Solution**

Try again later.

#### 1002300009 Invalid Download Parameters

**Message**

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

**Description**

The parameters passed to the download API of the TTS capability are invalid.

**Possible causes**

The parameters are not passed according to the requirements.

**Solution**

Ensure that the input parameters are correct and try again.

#### 1002300010 Timbre Already Downloaded

**Message**

Voice has already been downloaded.

**Description**

The TTS timbre has already been downloaded.

**Possible causes**

The timbre has already been downloaded.

**Solution**

Query timbres that have not been downloaded through the query API.
