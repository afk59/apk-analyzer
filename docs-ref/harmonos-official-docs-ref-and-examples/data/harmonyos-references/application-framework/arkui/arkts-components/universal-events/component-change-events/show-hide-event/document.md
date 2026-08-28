# Show/Hide Event

The show/hide event is triggered when a component is mounted or unmounted from the component tree. A component appears when mounted to the component tree and disappears when unmounted from the component tree.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/LZH72d5mRzeOrF9i1yWEkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF942A93435EF526ED0FDDBB81D3BD53DCEFDFFC32610740DA672B47C062B015)

The event is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### onAttach12+

onAttach(callback: Callback<void>): T

Triggered when this component is mounted to the component tree. Due to the following limitations, it is recommended that you use [onAppear](#onappear) instead of this callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/h5Am31VmQiWEg2ae3qfb1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=060CE479C2B78FB62B9B889B135C9E9C962ECD915CD627F7E5B69226AA7C9687)

-   This callback is triggered before the component layout and rendering process.
    
-   Modifying the component tree within the callback is prohibited, including initiating animations or altering the component structure through conditional statements like **if-else**.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback function of the **onAttach** event, indicating that the component has been mounted to the component tree. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDetach12+

onDetach(callback: Callback<void>): T

Triggered when this component is unmounted from the component tree. You are advised to use [onDisAppear](#ondisappear) instead.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [Callback](../../../common-definitions/basic-types/document.md#callback12)<void> | Yes | Callback function of the **onDetach** event, indicating that the component has been unmounted from the component tree. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onAppear

onAppear(event: () => void): T

Triggered when this component appears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/e5tgOlWdQMmxmHHT6rDEuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F04BDCB4CF14DF74EEC0357AFE2D16E13F2402E1EFFB73EEC7F32D968D1E745)

This callback may be called after the component layout and rendering process.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback function of the **onAppear** event, which indicates that the component is displayed. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### onDisAppear

onDisAppear(event: () => void): T

Triggered when this component disappears.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Callback function of the **onDisAppear** event, which indicates that the component is hidden. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to control the mounting and unmounting of a component using a button, triggering **onAttach** and **onDetach** events.

// xxx.ets
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct AppearExample {
  @State isShow: boolean = true;
  @State changeAppear: string = 'Show/Hide';
  private myText: string = 'Text for onAppear';

  build() {
    Column() {
      Button(this.changeAppear)
        .onClick(() => {
          this.isShow = !this.isShow
        }).margin(15)
      if (this.isShow) {
        Text(this.myText).fontSize(26).fontWeight(FontWeight.Bold)
          .onAttach(() => {
            this.getUIContext().getPromptAction().showToast({
              message: 'Text shown.',
              duration: 2000,
              bottom: 500
            })
          })
          .onDetach(() => {
            this.getUIContext().getPromptAction().showToast({
              message: 'Text hidden.',
              duration: 2000,
              bottom: 500
            })
          })
      }
    }.padding(30).width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/g5nS_jBrQAun4WlorUYI3A/en-us_image_0000002537765386.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062232Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A39A567BEB4195538FA1584AC9FD450688AA00640E589B2CCF527E3C1809A96)
