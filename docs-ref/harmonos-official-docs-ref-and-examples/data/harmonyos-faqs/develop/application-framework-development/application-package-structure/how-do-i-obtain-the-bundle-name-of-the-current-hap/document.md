# How do I obtain the bundle name of the current HAP?

Call the **getBundleInfoForSelf** API of the **bundleManager** module. Depending on the value of the **bundleFlags** parameter passed in the API, you can obtain different information about the application:

**GET\_BUNDLE\_INFO\_DEFAULT**: default value. The **name** field in the returned result represents the bundle name.

**GET\_BUNDLE\_INFO\_WITH\_APPLICATION**: used to obtain the default information with the application information. The **name** field in **ApplicationInfo** represents the bundle name.

The following code uses **GET\_BUNDLE\_INFO\_DEFAULT** as an example:

import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
let bundleFlags = bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_DEFAULT;
try {
  bundleManager.getBundleInfoForSelf(bundleFlags).then((data) => {
    hilog.info(0x0000, 'testTag', 'getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelf failed: %{public}s', message);
}
