# Video Component Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/6iSQeXE5Q-OcKcGT3e7AKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A01DB05F72C7C4F4504321BFA623294A43D07F30DE4584B0956A04CBB0B8324B)

This topic describes only module-specific error codes. For details about media error codes, see [Media Error Codes](../../../../../media/media-kit/error-codes/media-error-codes/document.md). For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 103601 Failed to Create the Player

**Error Message**

Failed to create the media player.

**Description**

This error code is reported when the player fails to be created.

**Possible Causes**

The media service does not exist, or the memory is insufficient.

**Solution**

Destroy the current instance and re-create an instance. If re-creation fails, stop the related operations.

#### 103602 Invalid Video Resource

**Error Message**

Not a valid source.

**Description**

This error code is reported when the configured video source is invalid.

**Possible Causes**

The system cannot locate the resource file, or the resource file is corrupted.

**Solution**

Ensure that the resource file exists and is intact, and then reset the video source for the **Video** component.
