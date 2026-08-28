# Page-Level Pixel Rounding

The goal of page-level pixel rounding is to set the pixel rounding mode as a context property of the page, enabling the configuration of pixel rounding at the page level.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/eITcHmEXSQuUPU5sF9AvJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B9FD774507E7F96405719227D2BC2F5C3E8F2736FC0B184967101572C0DF422)

-   The initial APIs of this module are supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.
-   If pixel rounding [issues](../component-level-pixel-rounding/document.md#faqs) occur and cannot be resolved using [component-level pixel rounding](../component-level-pixel-rounding/document.md), consider using the **PIXEL\_ROUND\_AFTER\_MEASURE** mode.
-   In **PIXEL\_ROUND\_AFTER\_MEASURE** mode, components perform rounding after size measurement is completed. As a result, the final size may be 1 px larger compared to the **PIXEL\_ROUND\_ON\_LAYOUT\_FINISH** mode.
-   The difference between page-level and component-level pixel rounding is: Page-level pixel rounding adjusts the rounding timing for the entire page, while component-level pixel rounding adjusts the rounding alignment method for specific components in specific directions.

#### setPixelRoundMode

setPixelRoundMode(mode: PixelRoundMode): void

Sets the pixel rounding mode for this page.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [PixelRoundMode](../../../common-definitions/enums/document.md#pixelroundmode18) | Yes | 
Pixel rounding mode.

Default value: **PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH**.

If this parameter is set to an invalid value, the default value will be used.

 |

**Example**

// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

onWindowStageCreate(windowStage: window.WindowStage) {
   windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
      uiContext.setPixelRoundMode(PixelRoundMode.PIXEL\_ROUND\_AFTER\_MEASURE);
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

#### getPixelRoundMode

getPixelRoundMode(): PixelRoundMode

Obtains the pixel rounding mode for this page.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [PixelRoundMode](../../../common-definitions/enums/document.md#pixelroundmode18) | Pixel rounding mode of the current page. |

**Example**

// EntryAbility.ets
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }
