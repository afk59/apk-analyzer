# Calling a Function

#### Restrictions

This kit supports phones and tablets by default. Support for wearables is available starting from 5.1.0(18), and for TVs starting from 5.1.1(19).

#### Setting Configuration Items of a Cloud Function

Add the network permission to the **entry/src/main/module.json5** file.

"requestPermissions": \[
  {
    "name": "ohos.permission.INTERNET"
  }
\]

#### Querying the Name and Version of a Function

On the trigger list page of a function, click **HTTP trigger** and view the suffix of the value of **Trigger URL**. The suffix is the trigger identifier, which is in _Function name_\-_Version number_ format. As shown in the following figure, **myhandlerxxxx-$_latest_** is the HTTP trigger identifier, in which **myhandlerxxxx** is the function name, and **$_latest_** is the version number.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/BlWDekiQTcGV1IHMFjYfIw/en-us_image_0000002474214313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062102Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EDE30D1959157D49DF6036831D666BEDA36DA2055C83DF2549C1A55DF41D025)

#### Calling a Function in an App

1.  Import the **cloudFunction** component to the project.
    
    import { cloudFunction } from '@kit.CloudFoundationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    

2.  Call [call()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cloudfoundation-cloudfunction#section251833512544) to set a function and pass the function name to the method. The execution result will be returned.
    
    -   (Optional) Set **timeout** to the timeout interval for calling the function, in milliseconds.
    -   (Optional) Set **version** to the function version. The default value is **$latest**.
    -   (Optional) If the function has input parameters, the **data** parameter can be converted into a JSON object or JSON character string.
    
    Return the result asynchronously through a promise:
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { cloudFunction } from '@kit.CloudFoundationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function callFunction() {
      cloudFunction.call({
        name: 'functionName', // Replace **functionName** with the actual function name.
         version: '$latest',   // If no version number is specified, the default value **$latest** is used.
        timeout: 10 \* 1000,   // Timeout interval, in milliseconds. The default interval is 70 x 1000 milliseconds.
        data: {               // Function request body.
          param1: 'val1', 
          param2: 'val2'
        }
      }).then((value: cloudFunction.FunctionResult) => {
        hilog.info(0x0000, 'testTag', \`Succeeded in calling the function, result: ${JSON.stringify(value.result)}\`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to call the function, code: ${err.code}, message: ${err.message}\`);
      })
    }
    
    Or return the result asynchronously through a callback:
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { cloudFunction } from '@kit.CloudFoundationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function callFunction() {
      cloudFunction.call({
        name: 'functionName', // Replace **functionName** with the actual function name.
        version: '$latest',  // If no version number is specified, the default value **$latest** is used.
        timeout: 10 \* 1000,  // Timeout interval, in milliseconds. The default interval is 70 x 1000 milliseconds.
        data: {              // Function request body.
          param1: 'val1',
          param2: 'val2'
        }
      }, (err: BusinessError, value: cloudFunction.FunctionResult) => {
        if (err) {
          hilog.error(0x0000, 'testTag', \`Failed to call the function, code: ${err.code}, message: ${err.message}\`);
          return;
        }
        hilog.info(0x0000, 'testTag', \`Succeeded in calling the function, result: ${JSON.stringify(value.result)}\`);
      })
    }
    

3.  Call the **result** attribute if you want to obtain the return value of the function.
    
    let returnValue = value.result;
    
    **value** is the **cloudFunction.FunctionResult** object returned by the **call()** method in step 2. The return value is the result returned by the body of the cloud function. For example, during the [function testing process](../testing-a-function/document.md), **value.result** is **{"simple":"example"}**.
