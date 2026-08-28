# JsLeakWatcher Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/PW_yRa22R664zZerxwfDpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062416Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B219E3E07C94EF85406009F645C9FC9F6812392208B01A983B3A7FDDFFB781D5)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 10801001 Invalid isEnabled

**Error Message**

The parameter isEnabled is invalid.

**Description**

When the **enableLeakWatcher** function is called, the invalid parameter **isEnabled** is input.

**Possible Causes**

1.  The type of **isEnabled** is incorrect.
    
2.  Mandatory parameters are not specified.
    

**Solution**

Ensure that the type of **isEnabled** is correct.

#### 10801002 Invalid config

**Error Message**

The parameter config is invalid.

**Description**

When the **enableLeakWatcher** function is called, the invalid parameter **config** is input.

**Possible Causes**

1.  The type of **config** is incorrect.
    
2.  Mandatory parameters are not specified.
    
3.  Parameter verification failed. This parameter is an array of strings. The array must contain one or more of **XComponent**, **NodeContainer**, **Window**, Custom Component, and Ability.
    

**Solution**

Ensure that the type of **config** is correct.

#### 10801003 Invalid callback

**Error Message**

The parameter callback is invalid.

**Description**

When the **enableLeakWatcher** function is called, the invalid parameter **callback** is input.

**Possible Causes**

1.  The type of **callback** is incorrect.
    
2.  Mandatory parameters are not specified.
    
3.  Parameter verification failed.
    

**Solution**

Ensure that the type of **callback** is correct. The input parameter of the **callback** function is an array of two strings.

Index **0** indicates the name of the leak list file, whose name extension is **.jsleaklist**. Index **1** indicates the name of the VM memory snapshot file, whose name extension is **.rawheap**.
