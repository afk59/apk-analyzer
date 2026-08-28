# Print Service Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/7hRcblbURgqNHjZEWKnsUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062401Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0089ED47B5FE7DD2DAB33C936BB7573352A85F14004ED119803CB4228EDE6E68)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 13100001 Generic Print Error

**Error Message**

Generic failure of print.

**Possible Causes**

1.  Failed to create a task object in the **print** module.

**Solution**

Close the print page and try again later, or restart the device.

#### 13100002 RPC Error

**Error Message**

RPC failure.

**Possible Causes**

1.  Failed to obtain the SA service object.
2.  Failed to conduct inter-process communication.

**Solution**

Close the print page and try again later, or restart the device.

#### 13100003 Print Service Error

**Error Message**

Failure of print service.

**Possible Causes**

1.  Failed to start the print service.
2.  Failed to start the cups service.

**Solution**

Close the print page and try again later, or restart the device.

#### 13100004 Invalid Print Extension

**Error Message**

Invalid print extension.

**Possible Causes**

1.  Cannot find the print extension.
2.  An error occurred when printing extended parameters.
3.  An error occurred when printing the extended status.

**Solution**

Close the print page and try again later, or restart the device.

#### 13100005 Invalid Printer

**Error Message**

Invalid printer.

**Possible Causes**

1.  Incorrect printer ID.
2.  The cups failed to query the printer list.
3.  The cups failed to query the printer information.

**Solution**

Close the print page and try again later, or restart the device.

#### 13100006 Invalid Print Job

**Error Message**

Invalid print job.

**Possible Causes**

1.  Incorrect print job ID.
2.  Incorrect print job status.
3.  Cannot find the print job.

**Solution**

Cancel the job, close the print page, or restart the device.
