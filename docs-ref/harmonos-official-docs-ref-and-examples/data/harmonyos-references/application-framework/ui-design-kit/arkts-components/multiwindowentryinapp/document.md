# MultiWindowEntryInAPP

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/5EdQx4oUSRGez51Q81wqGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=170DBC592D9078055388AFE02244C8C87619831AC70976447759BBE4A0E6F9BC)

This capability is applicable only when the current device and its screen state support the multitask view. Currently, the following device types support the multitask view:

-   Bi-fold phones in unfolded state
-   Tri-fold phones in Dual screen mode or Triple screen mode (in landscape mode)
-   Tablets in landscape mode

For other device types or states, this component will not respond to any taps on the in-app multi-window icon.

The **MultiWindowEntryInAPP** component is responsible for implementing the logic for simultaneously running a single app in multiple windows. You can leverage this component to develop this feature for your app based on your service needs.

**Device behavior differences**: This component is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

#### Modules to Import

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/AO4UwaTKSlSjCJ8kHxXwZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D386F1FAE23E4683B51FBCDD05B04016A4CBD87D938E6D768C53E8ED57F313D3)

-   **MultiWindowEntryInAPPAttribute** is essential for configuring the **HdsListItemCard** component. In version 6.0.1(21) and earlier, you must manually import **MultiWindowEntryInAPPAttribute** after importing the **MultiWindowEntryInAPP** component. Otherwise, a compilation error is reported. However, starting from version 6.0.2(22), the compilation toolchain automatically imports **MultiWindowEntryInAPPAttribute** when it detects the **MultiWindowEntryInAPP** component, so manual import is no longer necessary.
-   If you manually import **HdsListItemCardAttribute**, DevEco Studio shows it as disabled (grayed out). In version 6.0.1(21) and earlier, removing this import causes a compilation error. But from version 6.0.2(22) onward, removing it does not affect the functionality.

Version 6.0.1(21) and earlier:

import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';

Version 6.0.2(22) and later:

import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions } from '@kit.UIDesignKit';

#### Child Components

None

#### API

MultiWindowEntryInAPP(params: MultiWindowEntryInAPPParams)

Creates the in-app multi-window component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior differences**: This API is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[MultiWindowEntryInAPPParams](#section1967092315545)

 | 

Yes

 | 

In-app multi-window component parameters.

 |

#### MultiWindowEntryInAPPParams

Parameters of the **MultiWindowEntryInAPP** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior differences**: This API is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

want

 | 

[Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md)

 | 

No

 | 

No

 | 

Parameters for starting multiple windows. The requirements are as follows:

1\. The **abilityName**, **moduleName**, and **bundleName** fields are mandatory.

2\. App restrictions: All the specified fields (including **abilityName**, **moduleName**, and **bundleName**) must belong to the current app.

3\. Cross-app restrictions: The multi-windows function does not support cross-app capabilities.

 |
| 

isShowSubtitle

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the component text title.

**true**: yes

**false**: no

The default value is **false**.

 |
| 

multiWindowEntryInAPPStyle

 | 

[MultiWindowEntryInAPPStyle](#section126113816421)

 | 

No

 | 

Yes

 | 

Component style parameters.

 |

#### MultiWindowEntryInAPPStyle

Defines the style parameters for the **MultiWindowEntryInAPP** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior differences**: This API is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

iconOptions

 | 

[MultiWindowEntryInAPPIconOptions](#section754554610522)

 | 

No

 | 

Yes

 | 

Component icon parameters.

 |
| 

subtitleOptions

 | 

[MultiWindowEntryInAPPSubtitleOptions](#section15788112816535)

 | 

No

 | 

Yes

 | 

Component text title parameters.

 |

#### MultiWindowEntryInAPPIconOptions

Defines the icon parameters for the **MultiWindowEntryInAPP** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior differences**: This API is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

iconColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Component icon color.

Default value: **$r('sys.color.font\_primary')**

 |
| 

iconWeight

 | 

number | [FontWeight](../../../arkui/arkts-components/common-definitions/enums/document.md#fontweight) | string

 | 

No

 | 

Yes

 | 

Component icon font weight.

The default value is **400**.

NOTE:

-   For the number type, the value ranges from 100 to 900, at an interval of 100. The default value is **400**. A larger value indicates a larger font weight.
-   For the string type, only strings that represent a number, for example, **400**, and the following enumerated values of **FontWeight** are supported: **Bold**, **Bolder**, **Lighter**, **Regular**, and **Medium**.

 |
| 

iconSize

 | 

number | string | [Resource](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource)

 | 

No

 | 

Yes

 | 

Component icon size.

Default value: 24 x 24 vp

NOTE:

Percentages are not supported currently.

 |
| 

backgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of the component.

Default value: **$r('sys.color.comp\_background\_tertiary')**

 |

#### MultiWindowEntryInAPPSubtitleOptions

Defines the title text parameter of the **MultiWindowEntryInAPP** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Core

**Device behavior differences**: This API is supported only for phones and tablets in specific forms and does not apply for other devices.

**Start version**: 6.0.0(20)

**Parameters:**

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

modifier

 | 

[TextModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Component text title modifier.

 |

#### Attributes

[Universal attributes](../../../arkui/arkts-components/universal-attributes/document.md) are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/NY5Y_6dwTnS-ZW_cDvdB2Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C7C12C8529AAC773418E25683FF7757EEA45852A9F5FD6A0CFADDA7E7A76998)

The **width**, **height**, and **size** attributes do not support percentages currently.

This component does not support the **accessibilityDescription** and **accessibilityText** attributes.

#### Events

Most [universal attributes](../../../arkui/arkts-components/universal-events/document.md) are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/gNGClSf6T42rebBQOZob-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8EC9D64B544B8E98010B0D08BB0644E7632994ADA542244CBD4AD44B749051F)

This component does not support the **onClick** event. If you want to listen for tap events, use the **onTouch** event instead.

#### Example

An app can integrate the in-app multi-window component, allowing users to tap the split-screen button for multiple UIAbility components to be displayed in split-screen mode or enter Multitask view mode.

// Starting from version 6.0.2(22), you do not need to manually import MultiWindowEntryInAPPAttribute. For details, refer to the "Modules to Import" section of the MultiWindowEntryInAPP reference document.
import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
import { Want } from '@kit.AbilityKit';
import { TextModifier }  from '@kit.ArkUI';

@Entry
@Component
struct MultiWindowEntryInAPPTest {
  @State textModifier: TextModifier = new TextModifier();
  private want: Want = {
    // Replace the values of **bundleName**, **moduleName**, and **abilityName** with those of your app to start the **UIAbility** in the app.
    bundleName: "com.example.myapplication",
    moduleName: "entry",
    abilityName: "FuncAbility",
  };

  build() {
    Row() {
      MultiWindowEntryInAPP({
        want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
          iconOptions: {
            iconSize: 24,
            iconColor: $r('sys.color.font\_primary'),
            iconWeight: FontWeight.Normal,
            backgroundColor: $r('sys.color.comp\_background\_tertiary')
          },
          subtitleOptions: {
            modifier: this.textModifier.fontColor(Color.Black)
          }
        }
      })
        .size({ width: 48, height: 48 })
        .position({ x: 400, y: 30 })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/kwMT-0OlS4KQQigD81aoCQ/en-us_image_0000002500304218.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1E4338BEBDC06707AFF27DB9DA29446EB37640FCB9D056341092ADFF41664F9 "Click to enlarge")
