# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/8FurwLFiSaKYSCegNMmfDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B1F4F7C56D89FE9B1F21FBCB0D1D1893A8DF183E15952EFF81A4EDEA13C6301)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 200 Running Timeout

**Message**

Run timed out, please try again later.

**Description**

Running times out. Please try again.

**Possible causes**

A large number of requests cannot be processed in a timely manner.

**Solution**

Wait for a period of time and try again. Perform related logical judgement.

#### 1011200001 Running Failure

**Message**

Failed to run, please try again.

**Description**

Running failed. Please try again.

**Possible causes**

The input does not meet the requirements, or the service is abnormal.

**Solution**

Wait for a period of time and try again. Perform related logical judgement.

#### 1011200002 Service Exception

**Message**

The service is abnormal.

**Description**

The service is abnormal.

**Possible causes**

A service error occurs.

**Solution**

Restart the system and try again.
