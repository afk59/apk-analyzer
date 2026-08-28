# Is there a limit on the length of logs printed by HiLog?

The maximum size of a log file is 4096 bytes. Excess content will be discarded.

To prevent incomplete log information, you can encapsulate the **LogUtil** class in HiLog.

Refer to the sample code below.

Encapsulate the **LogUtil** class:

import { hilog } from '@kit.PerformanceAnalysisKit';

class LogUtil {
  private static instance: LogUtil;
  private static DOMAIN: number = 0x0000;

  private constructor() {
    // Private constructor to prevent external instantiation
  }

  public static getInstance(): LogUtil {
    if (!LogUtil.instance) {
      LogUtil.instance = new LogUtil();
    }
    return LogUtil.instance;
  }

  public logError(logTag: string, content: string) {
    const maxSize = 1024;
    if (content.length <= maxSize) {
      // Length less than or equal to the limit for direct printing
    } else {
      while (content.length > maxSize) {
        // Loop segmented printing
        let logContent = content.substring(0, maxSize);
        content = content.replace(logContent, '');
        hilog.error(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
        // Print remaining logs
      }
    }
    hilog.error(LogUtil.DOMAIN, logTag, '%{public}s', content);
  }

  public logDebug(logTag: string, content: string) {
    const maxSize = 1024;
    if (content.length <= maxSize) {
      // Length less than or equal to the limit for direct printing
    } else {
      while (content.length > maxSize) {
        //Loop segmented printing
        let logContent = content.substring(0, maxSize);
        content = content.replace(logContent, '');
        hilog.debug(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
        // Print remaining logs
      }
    }
    hilog.debug(LogUtil.DOMAIN, logTag, '%{public}s', content);
  }

  public logInfo(logTag: string, content: string) {
    const maxSize = 1024;
    if (content.length <= maxSize) {
      // Length less than or equal to the limit for direct printing
    } else {
      while (content.length > maxSize) {
        //Loop segmented printing
        let logContent = content.substring(0, maxSize);
        content = content.replace(logContent, '');
        hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', logContent);
        // Print remaining logs
      }
    }
    hilog.info(LogUtil.DOMAIN, logTag, '%{public}s', content);
  }
}

export default LogUtil;

Sample code:

import LogUtil from './LogUtilClass';

@Entry
@Component
struct HiLogIsThereALengthLimit {
  build() {
    Row() {
      Column() {
        Button('hilog util')
          .onClick(() => {
            let str = 'Long log content';
            let utilInfo = LogUtil.getInstance();
            utilInfo.logInfo('testTag', str);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
