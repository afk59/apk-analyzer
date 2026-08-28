# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/Bc6Jcxb2Qb60rxUCAizQWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062526Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6015EABB6053EF2B9BC2E8AB483521F6D2CEEF2E0741C6C24F3F69B784CCA5A7)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

#### 1008301002 Route Redirection Failure

**Message**

Route switching failed.

**Description**

Route switching failed.

**Possible causes**

The input parameters do not meet requirements, or the route switching is abnormal.

**Solution**

Check whether the input parameters meet the requirements of [InteractiveLivenessConfig](../arkts-apis/interactiveliveness-face-liveness-detection/document.md#section16532153115517). Try again after a period of time and perform related logic judgment.

#### 1008302000 Detection Algorithm Initialized

**Message**

Detection algorithm initialization.

**Description**

No detection data returned because the detection algorithm initialization has not finished.

**Possible causes**

Liveness detection has not been performed when the detection result is requested.

**Solution**

Obtain the result after the liveness detection is complete.

#### 1008302001 Detection Timeout

**Message**

Detection timeout.

**Description**

The detection times out. As a result, the failure screen is displayed. If you have configured your own failure screen or back route redirection, you are advised to perform the detection again.

**Possible causes**

During the detection, related actions are not completed as prompted for a long time. As a result, the detection times out.

**Solution**

Perform related actions as prompted.

#### 1008302002 Incorrect Actions

**Message**

Action mutual exclusion error.

**Description**

Actions are incorrect. As a result, the failure screen is displayed. If you have configured your own failure screen or back route redirection, you are advised to perform the detection again.

**Possible causes**

During the detection, related actions are not completed as prompted. As a result, the detection fails.

**Solution**

Perform related actions as prompted.

#### 1008302003 Continuity Check Failure

**Message**

Continuity Check Failure.

**Description**

The continuity check fails. As a result, the failure screen is displayed. If you have configured your own failure screen or back route redirection, you are advised to perform the detection again.

**Possible causes**

During check of multiple actions, related actions are not completed as prompted. As a result, the continuity check fails.

**Solution**

Perform related actions as prompted.

#### 1008302004 Incomplete Detection

**Message**

The test is not complete.

**Description**

The detection is incomplete. If you have configured your own failure screen or back route redirection, you are advised to perform the detection again.

**Possible causes**

The user exits the detection before the detection is complete.

**Solution**

Perform related actions as prompted.
