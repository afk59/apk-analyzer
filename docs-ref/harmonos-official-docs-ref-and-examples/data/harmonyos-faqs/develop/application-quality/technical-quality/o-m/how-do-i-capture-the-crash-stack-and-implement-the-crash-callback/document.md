# How do I capture the crash stack and implement the crash callback?

You can use **faultLogger.querySelfFaultLog** to capture various faults (such as C++ program faults, JS program faults, and application freezing), and obtain fault log information (ID and user ID of the faulty process, fault type, second-level timestamp when the log is generated, fault cause, faulty module, fault summary, and full text of the fault log). For details, see the following sample code:

import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit'

async function getLog() {
  try {
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS\_CRASH);
    if (value) {
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
  } catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
  }
}

**Reference**

[@ohos.faultLogger (FaultLogger)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-faultlogger)
