# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/q7_CvGrLQSG3b__7Me3mqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062522Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61CA5F3F7A17880898EDEE15A823EDC67422A3D8854405D334CFECC79F43D805)

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

#### 401 Parameter Error

**Message**

The parameter check failed.

**Description**

The input parameters are incorrect.

**Possible causes**

The input image type or parameter value is incorrect. Therefore, the input image does not meet the requirements.

**Solution**

Ensure that the input image type and parameter values are correct. Then, try again.

#### 1001400001 Running Failure

**Message**

Failed to run, please try again.

**Description**

Running failed. Please try again.

**Possible causes**

The input does not meet the requirements, or the service is abnormal.

**Solution**

Wait for a period of time and try again. Perform related logical judgement.

#### 1001400002 Abnormal Service

**Message**

The service is abnormal.

**Description**

The service is abnormal.

**Possible causes**

The service is abnormal.

**Solution**

Restart the device and try again.

#### 1008400001 Running Failure

**Message**

Failed to run, please try again.

**Description**

Running failed. Please try again.

**Possible causes**

The input does not meet the requirements, or the service is abnormal.

**Solution**

Wait for a period of time and try again. Perform related logical judgement.

#### 1008400002 Abnormal Service

**Message**

The service is abnormal.

**Description**

The service is abnormal.

**Possible causes**

The service is abnormal.

**Solution**

Restart the device and try again.

#### 1008800001 Running Failure

**Message**

Failed to run, please try again.

**Description**

Running failed. Please try again.

**Possible causes**

The input does not meet the requirements, or the service is abnormal.

**Solution**

Wait for a period of time and try again. Perform related logical judgement.

#### 1008800002 Abnormal Service

**Message**

The service is abnormal.

**Description**

The service is abnormal.

**Possible causes**

The service is abnormal.

**Solution**

Restart the device and try again.

#### 1011000001 Running Failure

**Message**

Failed to run, please try again.

**Description**

Running failed. Please try again.

**Possible causes**

The input does not meet the requirements. For example, the input is an image without a prominent subject, a damaged image that cannot be opened, or a non-image.

**Solution**

Pass another image with a salient subject (the area proportion should be greater than 5‰).

#### 1011000002 Abnormal Service

**Message**

The service is abnormal.

**Description**

The service is abnormal.

**Possible causes**

The service is abnormal.

**Solution**

Restart the device and try again.

#### 1011000003 Model Running Failure

**Message**

Failed to run the model, please try again.

**Description**

Failed to run the model. Please try again.

**Possible causes**

Model loading is abnormal.

**Solution**

Try again later.

#### 1011000004 Model Running Timeout

**Message**

Running the model timed out. Try again later.

**Description**

Model running times out.

**Possible causes**

Model loading is abnormal.

**Solution**

Try again later.
