# @ohos.hichecker (HiChecker)

The HiChecker module allows you to check issues that may be easily ignored during development of applications (including system-built and third-party applications). Such issues include calling of time-consuming functions by key application threads, event distribution and execution timeout in application processes, and ability resource leakage in application processes. The issues are recorded in logs or lead to process crashes explicitly so that you can find and rectify them.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/dNBeDfoWS3mavXLE2oypAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66C4446C7FE403AFE98D21689224EA2D600FF7FA106D3C7D317BA558CA2276FE)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { hichecker } from '@kit.PerformanceAnalysisKit';

#### Constants

Provides the constants of all rule types.

**System capability**: SystemCapability.HiviewDFX.HiChecker

| Name | Type | Value | Description |
| :-- | :-- | :-- | :-- |
| RULE\_CAUTION\_PRINT\_LOG | bigint | 1ULL << 63 | Alarm rule, which is programmed to print a log when an alarm is generated. |
| RULE\_CAUTION\_TRIGGER\_CRASH | bigint | 1ULL << 62 | Alarm rule, which is programmed to force the application to exit when an alarm is generated. |
| RULE\_THREAD\_CHECK\_SLOW\_PROCESS | bigint | 1ULL | Caution rule, which is programmed to detect whether any time-consuming function is invoked. |
| RULE\_CHECK\_ABILITY\_CONNECTION\_LEAK | bigint | 1ULL << 33 | Caution rule, which is programmed to detect whether ability leakage has occurred. |
| RULE\_CHECK\_ARKUI\_PERFORMANCE11+ | bigint | 1ULL << 34 | Caution rule, which is programmed to detect the ArkUI performance. |

#### hichecker.addCheckRule9+

addCheckRule(rule: bigint): void

Adds one or more check rules. HiChecker detects unexpected operations or gives feedback based on the added rules. You can use **grep HiChecker** to check for the application running information in the hilog.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be added. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Add a rule.
    hichecker.addCheckRule(hichecker.RULE\_CAUTION\_PRINT\_LOG);
    // Add multiple rules.
    // hichecker.addCheckRule(
    //     hichecker.RULE\_CAUTION\_PRINT\_LOG | hichecker.RULE\_CAUTION\_TRIGGER\_CRASH);
} catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
}

#### hichecker.removeCheckRule9+

removeCheckRule(rule: bigint): void

Removes one or more rules. The removed rules will become ineffective.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be removed. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Remove a rule.
    hichecker.removeCheckRule(hichecker.RULE\_CAUTION\_PRINT\_LOG);
    // Remove multiple rules.
    // hichecker.removeCheckRule(
    //     hichecker.RULE\_CAUTION\_PRINT\_LOG | hichecker.RULE\_CAUTION\_TRIGGER\_CRASH);
} catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
}

#### hichecker.containsCheckRule9+

containsCheckRule(rule: bigint): boolean

Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. If the rule exists in the collection of added rules, **true** is returned; otherwise, **false** is returned. |

**Error codes**

| ID | Error Message |
| :-- | :-- |
| 401 | the parameter check failed, only one bigint type parameter is needed |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    // Add a rule.
    hichecker.addCheckRule(hichecker.RULE\_THREAD\_CHECK\_SLOW\_PROCESS);

    // Check whether the added rule exists in the collection of added rules.
    hichecker.containsCheckRule(hichecker.RULE\_THREAD\_CHECK\_SLOW\_PROCESS); // return true;
    hichecker.containsCheckRule(hichecker.RULE\_CAUTION\_PRINT\_LOG); // return false;
} catch (err) {
    console.error(\`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}\`);
}

#### hichecker.addRule(deprecated)

addRule(rule: bigint): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/cjkbjtwmQMGpyLRSvtWpsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1CD6170F49A1936FB1CCF797B8F24CA189B052BEDCFEBBC87861D07AFD838C5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hichecker.addCheckRule](#hicheckeraddcheckrule9) instead.

Adds one or more rules. HiChecker detects unexpected operations or gives feedback based on the added rules.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be added. |

**Example**

// Add a rule.
hichecker.addRule(hichecker.RULE\_CAUTION\_PRINT\_LOG);

// Add multiple rules.
hichecker.addRule(
          hichecker.RULE\_CAUTION\_PRINT\_LOG | hichecker.RULE\_CAUTION\_TRIGGER\_CRASH);

#### hichecker.removeRule(deprecated)

removeRule(rule: bigint): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/-qhUH9c6QUqCnJeAvE-UGA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36D55DC6E45F8519F9C1CF3FB751737137469886F6E9C9410342512F509D6848)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hichecker.removeCheckRule](#hicheckerremovecheckrule9) instead.

Removes one or more rules. The removed rules will become ineffective.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be removed. |

**Example**

// Remove a rule.
hichecker.removeRule(hichecker.RULE\_CAUTION\_PRINT\_LOG);

// Remove multiple rules.
hichecker.removeRule(
          hichecker.RULE\_CAUTION\_PRINT\_LOG | hichecker.RULE\_CAUTION\_TRIGGER\_CRASH);

#### hichecker.getRule

getRule(): bigint

Obtains a collection of thread, process, and alarm rules that have been added.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | Collection of added rules. |

**Example**

// Add a rule.
hichecker.addCheckRule(hichecker.RULE\_CAUTION\_PRINT\_LOG);

// Obtain the collection of added rules.
hichecker.getRule();   // return 1n;

#### hichecker.contains(deprecated)

contains(rule: bigint): boolean

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/f11cds2gQO-5uJ3AsWsPAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF44083179B0A36C6E313A7D36EE8563403634EA7015BA211A2CA1037B86956A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [hichecker.containsCheckRule](#hicheckercontainscheckrule9) instead.

Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this operation is performed only on the current thread.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rule | bigint | Yes | Rule to be checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. If the rule exists in the collection of added rules, **true** is returned; otherwise, **false** is returned. |

**Example**

// Add a rule.
hichecker.addRule(hichecker.RULE\_THREAD\_CHECK\_SLOW\_PROCESS);

// Check whether the added rule exists in the collection of added rules.
hichecker.contains(hichecker.RULE\_THREAD\_CHECK\_SLOW\_PROCESS); // return true;
hichecker.contains(hichecker.RULE\_CAUTION\_PRINT\_LOG); // return false;
