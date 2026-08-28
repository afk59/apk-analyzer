# How do I obtain system logs when an application fault occurs?

Use the **faultLogger.query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>)** API to obtain fault logs. The values of **FaultType** are as follows:

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NO\_SPECIFIC

 | 

0

 | 

No specific fault.

 |
| 

CPP\_CRASH

 | 

2

 | 

C++ program crash.

 |
| 

JS\_CRASH

 | 

3

 | 

JS program crash.

 |
| 

APP\_FREEZE

 | 

4

 | 

Application freezing.

 |

The second parameter **callback** is a callback used to obtain the fault information array.

In the sample code, the value of **FaultType** is **JS\_CRASH**, and **queryFaultLogCallback** is the callback used to print related log information.

import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
  if (error) {
    console.info('error is ' + error);
  } else {
    console.info("value length is " + value.length);
    let len: number = value.length;
    for (let i = 0; i < len; i++) {
      console.info("log: " + i);
      console.info("Log pid: " + value\[i\].pid);
      console.info("Log uid: " + value\[i\].uid);
      console.info("Log type: " + value\[i\].type);
      console.info("Log timestamp: " + value\[i\].timestamp);
      console.info("Log reason: " + value\[i\].reason);
      console.info("Log module: " + value\[i\].module);
      console.info("Log summary: " + value\[i\].summary);
      console.info("Log text: " + value\[i\].fullLog);
    }
  }
}

try {
  FaultLogger.query(FaultLogger.FaultType.JS\_CRASH, queryFaultLogCallback);
} catch (err) {
  console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
}

**Reference**

[@ohos.faultLogger (FaultLogger)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-faultlogger)
