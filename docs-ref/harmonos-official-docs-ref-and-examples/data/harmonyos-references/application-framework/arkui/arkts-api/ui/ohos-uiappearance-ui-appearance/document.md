# @ohos.uiAppearance (UI Appearance)

This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/light) settings, font size scale factors, and font weight scale factors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/x1mi2jbZT3iux6Z-pvuQQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D32FFB21B6240D3C015E9A9A53790BAF407D78C4F2C72DF9CB07CA6F0C9DE6E)

The initial APIs of this module are supported since API version 20. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { uiAppearance } from '@kit.ArkUI';

#### DarkMode

Enumerates the color modes.

**System capability**: SystemCapability.ArkUI.UiAppearance

| Name | Value | Description |
| :-- | :-- | :-- |
| ALWAYS\_DARK | 0 | The system is always in dark mode. |
| ALWAYS\_LIGHT | 1 | The system is always in light mode. |

#### uiAppearance.getDarkMode

getDarkMode(): DarkMode

Obtains the current system dark mode configuration.

**System capability**: SystemCapability.ArkUI.UiAppearance

**Return value**

| Type | Description |
| :-- | :-- |
| [DarkMode](#darkmode) | Dark mode. |

**Error codes**

For details about the error codes, see [UI Appearance Error Codes](../../../error-codes/ui/ui-appearance-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 500001 | Internal error. |

**Example**

import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get dark-mode failed, ' + message);
}

#### uiAppearance.getFontScale

getFontScale(): number

Obtains the current font size scale factor.

**System capability**: SystemCapability.ArkUI.UiAppearance

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current font size scale factor. |

**Error codes**

For details about the error codes, see [UI Appearance Error Codes](../../../error-codes/ui/ui-appearance-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 500001 | Internal error. |

**Example**

import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontScale = uiAppearance.getFontScale();
  console.info('Get fontScale ' + fontScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontScale failed, ' + message);
}

#### uiAppearance.getFontWeightScale

getFontWeightScale(): number

Obtains the current font weight scale factor.

**System capability**: SystemCapability.ArkUI.UiAppearance

**Return value**

| Type | Description |
| :-- | :-- |
| number | Current font weight scale factor. |

**Error codes**

For details about the error codes, see [UI Appearance Error Codes](../../../error-codes/ui/ui-appearance-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 500001 | Internal error. |

**Example**

import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontWeightScale = uiAppearance.getFontWeightScale();
  console.info('Get fontScale ' + fontWeightScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontWeightScale failed, ' + message);
}
