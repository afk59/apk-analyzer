# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/BJ6gBfLnSgC_fTuqHTL-Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFC615E41E74D37A6FED3A4C9A040E53586AD66695EF1FB966070CD124E286C3)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 1003810001 Invalid Parameter Value

**Message**

Invalid parameter value.

**Description**

Invalid parameter value.

**Possible causes**

1.  The length of the destination or waypoint name specified when setting the navigation status exceeds 1024 bytes.
2.  The length of the current road name or next road name specified when setting the navigation metadata exceeds 1024 bytes.
3.  The parameter value is out of range. For example, the latitude or longitude specified when setting the navigation status is not within the valid range (latitude: \[–90, 90\]; longitude: \[–180, 180\]).

**Solution**

Ensure that valid parameter values are passed when setting the navigation status and navigation metadata.

#### 1003810002 Total Size of All Parameters Exceeds the Limit

**Message**

The total size of all parameters exceeds the limit.

**Description**

The total size of all parameters exceeds the limit.

**Possible causes**

1.  Too many waypoints are added when setting the navigation status.
2.  If an intersection zoom-in view is passed when setting the navigation metadata, the total size of all parameters may exceed the limit (200 KB).

**Solution**

1.  Verify that the number of waypoints added when setting the navigation status does not exceed 20.
2.  If an intersection zoom-in view with a large size needs to be passed when setting the navigation metadata, you are advised to compress the image.
