# HdsListItemCard

This module provides the **HdsListItemCard** component to enhance the visual experience and unify component styles for list items. Apps can use the **HdsListItemCard** component to achieve consistent system list styles across multiple devices.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsListItemCard } from '@kit.UIDesignKit';

#### API

HdsListItemCard(options: HdsListItemCardOptions)

Sets the list item options of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Abnormal device behavior**: The styles implemented by this API are inconsistent with the UX specifications for TVs. For example, a focused and hovered component cannot be enlarged, the background color of the focused component does not change, and the text default color within a button is different. This API can work properly for other device types.

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[HdsListItemCardOptions](#section6323195713321)

 | 

Yes

 | 

List item options of the **HdsListItemCard** component.

 |

#### PrefixItem

Defines the **PrefixItem** class, which is used to configure elements in area A (on the left side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### PrefixImage

**PrefixImage** inherits from the parent class [PrefixItem](#section68021033134910) and represents the **Image** element in area A (on the left side of the list). The image size cannot be changed for wearables and is fixed at 46 x 46 vp.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ImageClickOptions](#section4353179193911)

 | 

No

 | 

Yes

 | 

Options of the **Image** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: ImageClickOptions)

Constructor for **PrefixImage**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ImageClickOptions](#section4353179193911)

 | 

No

 | 

Options of the **Image** element in area A (on the left side of the list).

 |

#### PrefixIcon

**PrefixIcon** inherits from the parent class [PrefixItem](#section68021033134910) and represents the icon element in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[PrefixIconOptions](#section232815719440)

 | 

No

 | 

Yes

 | 

Options of the **Icon** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: PrefixIconOptions)

Constructor for **PrefixIcon**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[PrefixIconOptions](#section232815719440)

 | 

No

 | 

Options of the **Icon** element in area A (on the left side of the list).

 |

#### PrefixBadge

**PrefixBadge** inherits from the parent class [PrefixItem](#section68021033134910) and represents the **Badge** element in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Yes

 | 

Options of the **Badge** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: BadgeOptions)

Constructor for **PrefixBadge**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Options of the **Badge** element in area A (on the left side of the list).

 |

#### PrefixSwitch

**PrefixSwitch** inherits from the parent class [PrefixItem](#section68021033134910) and represents the **Switch** element in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Yes

 | 

Options of the **Switch** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: CheckOptions)

Constructor for **PrefixSwitch**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Options of the **Switch** element in area A (on the left side of the list).

 |

#### PrefixToggleButton

**PrefixToggleButton** inherits from the parent class [PrefixItem](#section68021033134910) and represents the **ToggleButton** element in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ToggleButtonOptions](#section168210477514)

 | 

No

 | 

Yes

 | 

Options of the **ToggleButton** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: ToggleButtonOptions)

Constructor for **PrefixToggleButton**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ToggleButtonOptions](#section168210477514)

 | 

No

 | 

Options of the **ToggleButton** element in area A (on the left side of the list).

 |

#### PrefixButton

**PrefixButton** inherits from the parent class [PrefixItem](#section68021033134910) and represents the **Button** element in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ButtonOptions](#section35631920155512)

 | 

No

 | 

Yes

 | 

Options of the **Button** element in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(options?: ButtonOptions)

Constructor for **PrefixButton**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ButtonOptions](#section35631920155512)

 | 

No

 | 

Options of the **Button** element in area A (on the left side of the list).

 |

#### PrefixCustomBuilder

**PrefixCustomBuilder** inherits from the parent class [PrefixItem](#section68021033134910) and represents the custom content in area A (on the left side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

customBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom content in area A (on the left side of the list).

 |

#### \[h2\]constructor

constructor(customBuilder?: CustomBuilder)

Constructor for **PrefixCustomBuilder**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

customBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Custom content in area A (on the left side of the list).

 |

#### SuffixItem

Defines the **SuffixItem** class, which is used to configure elements in area C (on the right side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### SuffixText

**SuffixText** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Text** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Options of the **Text** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: TextOptions)

Constructor for **SuffixText**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Options of the **Text** element in area C (on the right side of the list).

 |

#### SuffixImage

**SuffixImage** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Image** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ImageClickOptions](#section4353179193911)

 | 

No

 | 

Yes

 | 

Options of the **Image** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: ImageClickOptions)

Constructor for **SuffixImage**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ImageClickOptions](#section4353179193911)

 | 

No

 | 

Options of the **Image** element in area C (on the right side of the list).

 |

#### SuffixLoadingProgress

**SuffixLoadingProgress** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **LoadingProgress** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Yes

 | 

Options of the **LoadingProgress** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: ColorOptions)

Constructor for **SuffixLoadingProgress**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Options of the **LoadingProgress** element in area C (on the right side of the list).

 |

#### SuffixRadio

**SuffixRadio** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Radio** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Yes

 | 

Options of the **Radio** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: CheckOptions)

Constructor for **SuffixRadio**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Options of the **Radio** element in area C (on the right side of the list).

 |

#### SuffixCheckbox

**SuffixCheckbox** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Checkbox** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Yes

 | 

Options of the **Checkbox** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: CheckOptions)

Constructor for **SuffixCheckbox**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Options of the **Checkbox** element in area C (on the right side of the list).

 |

#### SuffixSwitch

**SuffixSwitch** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Switch** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Yes

 | 

Options of the **Switch** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: CheckOptions)

Constructor for **SuffixSwitch**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[CheckOptions](#section740053134818)

 | 

No

 | 

Options of the **Switch** element in area C (on the right side of the list).

 |

#### SuffixArrow

**SuffixArrow** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Arrow** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Yes

 | 

Options of the **Arrow** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: ColorOptions)

Constructor for **SuffixArrow**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Options of the **Arrow** element in area C (on the right side of the list).

 |

#### SuffixBadge

**SuffixBadge** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Badge** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Yes

 | 

Options of the **Badge** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: BadgeOptions)

Constructor for **SuffixBadge**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Options of the **Badge** element in area C (on the right side of the list).

 |

#### SuffixButton

**SuffixButton** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Button** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ButtonOptions](#section35631920155512)

 | 

No

 | 

Yes

 | 

Options of the **Button** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: ButtonOptions)

Constructor for **SuffixButton**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ButtonOptions](#section35631920155512)

 | 

No

 | 

Options of the **Button** element in area C (on the right side of the list).

 |

#### SuffixIcon

**SuffixIcon** inherits from the parent class [SuffixItem](#section3859111120123) and represents the single **Icon** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Yes

 | 

Options of the single **Icon** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: SuffixIconOptions)

Constructor for **SuffixIcon**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Options of the single **Icon** element in area C (on the right side of the list).

 |

#### SuffixSubIcon

**SuffixSubIcon** inherits from the parent class [SuffixItem](#section3859111120123) and represents the two **Icon** elements in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Yes

 | 

Options of the first nearest **Icon** element in area C (on the right side of the list).

 |
| 

subOptions

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Yes

 | 

Options of the second nearest **Icon** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: SuffixIconOptions, subOptions?: SuffixIconOptions)

Constructor for **SuffixSubIcon**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Options of the first nearest **Icon** element in area C (on the right side of the list).

 |
| 

subOptions

 | 

[SuffixIconOptions](#section4745511195712)

 | 

No

 | 

Options of the second nearest **Icon** element in area C (on the right side of the list).

 |

#### SuffixSelect

**SuffixSelect** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Select** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[SelectStyle](#section1585419719586)

 | 

No

 | 

Yes

 | 

Options of the **Select** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: SelectStyle)

Constructor for **SuffixSelect**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[SelectStyle](#section1585419719586)

 | 

No

 | 

Options of the **Select** element in area C (on the right side of the list).

 |

#### SuffixToggleButton

**SuffixToggleButton** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **ToggleButton** element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[ToggleButtonOptions](#section168210477514)

 | 

No

 | 

Yes

 | 

Options of the **ToggleButton** element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: ToggleButtonOptions)

Constructor for **SuffixToggleButton**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[ToggleButtonOptions](#section168210477514)

 | 

No

 | 

Options of the **ToggleButton** element in area C (on the right side of the list).

 |

#### SuffixBadgeAndArrow

**SuffixBadgeAndArrow** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Badge-Arrow** combined element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

badgeOptions

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Yes

 | 

Options of **Badge** in the **Badge-Arrow** combined element in area C (on the right side of the list).

 |
| 

arrowOptions

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Yes

 | 

Options of **Arrow** in the **Badge-Arrow** combined element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(badgeOptions?: BadgeOptions, arrowOptions?: ColorOptions)

Constructor for **SuffixBadgeAndArrow**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

badgeOptions

 | 

[BadgeOptions](#section1862211717471)

 | 

No

 | 

Options of **Badge** in the **Badge-Arrow** combined element in area C (on the right side of the list).

 |
| 

arrowOptions

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Options of **Arrow** in the **Badge-Arrow** combined element in area C (on the right side of the list).

 |

#### SuffixTextAndArrow

**SuffixTextAndArrow** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Text-Arrow** combined element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

textOptions

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Options of **Text** in the **Text-Arrow** combined element in area C (on the right side of the list).

 |
| 

arrowOptions

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Yes

 | 

Options of **Arrow** in the **Text-Arrow** combined element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(textOptions?: TextOptions, arrowOptions?: ColorOptions)

Constructor for **SuffixTextAndArrow**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

textOptions

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Options of **Text** in the **Text-Arrow** combined element in area C (on the right side of the list).

 |
| 

arrowOptions

 | 

[ColorOptions](#section169543387546)

 | 

No

 | 

Options of **Arrow** in the **Text-Arrow** combined element in area C (on the right side of the list).

 |

#### SuffixArrowIconText

**SuffixArrowIconText** inherits from the parent class [SuffixItem](#section3859111120123) and represents the **Arrow-Text-Arrow** combined element in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

options

 | 

[SuffixArrowIconTextOptions](#section1946963582419)

 | 

No

 | 

Yes

 | 

Options of the **Text-Arrow-Icon** combined element in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(options?: SuffixArrowIconTextOptions)

Constructor for **SuffixArrowIconText**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

options

 | 

[SuffixArrowIconTextOptions](#section1946963582419)

 | 

No

 | 

Options of the **Text-Arrow-Icon** combined element in area C (on the right side of the list).

 |

#### SuffixCustomBuilder

**SuffixCustomBuilder** inherits from the parent class [SuffixItem](#section3859111120123) and represents the custom content in area C (on the right side of the list).

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### \[h2\]Attributes

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

customBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom content in area C (on the right side of the list).

 |

#### \[h2\]constructor

constructor(customBuilder?: CustomBuilder)

Constructor for **SuffixCustomBuilder**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

customBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Custom content in area C (on the right side of the list).

 |

#### HdsListItemCardOptions

Sets the element options of an **HdsListItemCard** list item.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Abnormal device behavior**: The styles implemented by this API are inconsistent with the UX specifications for TVs. For example, a focused and hovered component cannot be enlarged, the background color of the focused component does not change, and the text default color within a button is different. This API can work properly for other device types.

**Start version**: 6.0.0(20)

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

prefixItem

 | 

[PrefixItem](#section68021033134910)

 | 

No

 | 

Yes

 | 

Elements in area A (on the left side) of an **HdsListItemCard** list item.

 |
| 

textItem

 | 

[TextItemOptions](#section1905201905812)

 | 

No

 | 

Yes

 | 

Elements in area B (in the middle) of an **HdsListItemCard** list item.

 |
| 

suffixItem

 | 

[SuffixItem](#section3859111120123)

 | 

No

 | 

Yes

 | 

Elements in area C (on the right side) of an **HdsListItemCard** list item.

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Triggered when an **HdsListItemCard** list item is tapped.

 |
| 

cardHeight

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Height of an **HdsListItemCard** list item. Currently, percentages are not supported.

 |
| 

cardWidth

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Width of an **HdsListItemCard** list item. Currently, percentages are not supported.

 |
| 

cardBackgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of an **HdsListItemCard** list item.

 |
| 

cardBorderRadius

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Border radius of an **HdsListItemCard** list item.

 |
| 

cardPrefixMargin

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Distance between an **HdsListItemCard** list item and the left screen edge.

 |
| 

cardSuffixMargin

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Distance between an **HdsListItemCard** list item and the right screen edge.

 |
| 

hoverBorderRadius

 | 

[Dimension](../../../arkui/arkts-components/common-definitions/basic-types/document.md#dimension10)

 | 

No

 | 

Yes

 | 

Border radius of an **HdsListItemCard** list item in floating state.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether an **HdsListItemCard** list item is enabled.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

cardId

 | 

string

 | 

No

 | 

Yes

 | 

ID of an **HdsListItemCard** list item.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of an **HdsListItemCard** list item.

 |

#### TextItemOptions

Sets options for elements in area B (in the middle) of an **HdsListItemCard** list item.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

primaryText

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Title in area B (in the middle of the list).

 |
| 

primaryPrefixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the left of the title.

 |
| 

primarySuffixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the right of the title.

 |
| 

primaryPrefixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the left of the title. This icon is displayed only when the first nearest icon on the left exists.

 |
| 

primarySuffixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the right of the title. This icon is displayed only when the first nearest icon on the right exists.

 |
| 

secondaryText

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Subtitle in area B (in the middle of the list).

 |
| 

secondaryPrefixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the left of the subtitle.

 |
| 

secondarySuffixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the right of the subtitle.

 |
| 

secondaryPrefixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the left of the subtitle. This icon is displayed only when the first nearest icon on the left exists.

 |
| 

secondarySuffixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the right of the subtitle. This icon is displayed only when the first nearest icon on the right exists.

 |
| 

description

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Element description in area B (in the middle of the list).

 |
| 

descriptionPrefixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the left of the description.

 |
| 

descriptionSuffixSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

First nearest symbol icon on the right of the description.

 |
| 

descriptionPrefixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the left of the description. This icon is displayed only when the first nearest icon on the left exists.

 |
| 

descriptionSuffixSubSymbol

 | 

[TextSymbolGlyphOptions](#section9694202504117)

 | 

No

 | 

Yes

 | 

Second nearest symbol icon on the right of the description. This icon is displayed only when the first nearest icon on the right exists.

 |
| 

customBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

Yes

 | 

Custom content in area B (in the middle of the list).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/bFp1lK2JRNK3gYEdD3K8mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59C493956F5F124F0D6942DCDFD030A624FC30B7B4387DBC5E90F4EE36D078FC)

The priority of **customBuilder** in **TextItemOptions** is higher than that of other APIs.

#### AccessibilityOptions

Accessibility options of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

accessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text of a list. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

 |
| 

accessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility description of a list. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: For a **Switch** element, the default value is "Double-tap to enable/close"; for a **Checkbox** element, the default value is "Double-tap to select/deselect"; for other elements, the default value is "Double-tap to activate".

 |
| 

accessibilityLevel

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility level, which specifies whether this component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

The default value is **"auto"**.

 |

#### ImageOptions

Sets style options of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

image

 | 

[ImageType](#section1650110443168)

 | 

No

 | 

Yes

 | 

Image resource type.

 |
| 

modifier

 | 

[ImageModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Image style modifier.

 |

#### ImageClickOptions

Sets style options for a tappable **Image** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

image

 | 

[ImageType](#section1650110443168)

 | 

No

 | 

Yes

 | 

Image resource type.

 |
| 

modifier

 | 

[ImageModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Image style modifier.

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Image tap callback.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the **Image** element.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of an **Image** element.

 |

#### SymbolGlyphOptions

Sets style options for a **Symbol** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

symbol

 | 

[SymbolType](#section19341944531)

 | 

No

 | 

Yes

 | 

Symbol resource type.

 |

#### TextSymbolGlyphOptions

Sets style options for a **Symbol** element on the left and right sides of the text in area B (in the middle of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

symbol

 | 

[SymbolType](#section19341944531)

 | 

No

 | 

Yes

 | 

Symbol resource type on the left and right sides of the text in area B (in the middle of the list).

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Tap callback of the **Symbol** element on the left and right sides of the text in area B (in the middle of the list).

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the **Symbol** element on the left and right sides of the text in area B (in the middle of the list).

**true**: yes

**false**: no

The default value is **true**.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of the **Symbol** element on the left and right sides of the text in area B (in the middle of the list).

 |

#### PrefixIconOptions

Sets icon style options in area A (on the left side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

iconSize

 | 

[IconSize](#section6603131919318)

 | 

No

 | 

Yes

 | 

Style of the **Icon** element in area A (on the left side of the list).

Default value: [IconSize](#section6603131919318).SYSTEM\_ICON

 |
| 

iconValue

 | 

[PrefixIconType](#section9201529151513)

 | 

No

 | 

Yes

 | 

Icon resource type in area A (on the left side of the list).

 |

#### BadgeOptions

Sets style options for a **Badge** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

badgeValue

 | 

number

 | 

No

 | 

Yes

 | 

Message quantity displayed on the reminder badge. If the number is greater than 99, **99+** is displayed.

The default value is **–1**.

If this parameter is set to a value less than 0, no reminder badge is displayed.

 |
| 

badgeColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Badge background color.

Default value if a message reminder badge is displayed: **$r('sys.color.warning')**

Default value if a message reminder badge is not displayed: **$r('sys.color.comp\_background\_emphasize')**

 |
| 

textColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Number color on the badge.

Default value: **$r('sys.color.font\_on\_primary')**

 |
| 

badgeId

 | 

string

 | 

No

 | 

Yes

 | 

Badge ID.

 |

#### CheckOptions

Sets style options for a **Select** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

isCheck

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a **Select** element is initially in selected state.

**true**: yes

**false**: no

The default value is **false**.

 |
| 

selectColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of a **Select** element after it is selected.

 |
| 

onChange

 | 

[OnChangeCallback](#section1370591018245)

 | 

No

 | 

Yes

 | 

**onChange** callback of a **Select** element.

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Tap event callback of a **Select** element.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable a **Select** element.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

checkId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a **Select** element.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of a **Select** element.

 |

#### ToggleButtonOptions

Sets style options for a **ToggleButton** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

isCheck

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether a **ToggleButton** element is initially selected.

**true**: yes

**false**: no

The default value is **false**.

 |
| 

iconValue

 | 

[SymbolType](#section19341944531)

 | 

No

 | 

Yes

 | 

Symbol resource of an icon in a **ToggleButton** element.

 |
| 

selectColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of a **ToggleButton** element after it is selected.

Default value: **#00000000**

 |
| 

onChange

 | 

[OnChangeCallback](#section1370591018245)

 | 

No

 | 

Yes

 | 

**onChange** callback of a **ToggleButton** element.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable a **ToggleButton** element.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

toggleButtonId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a **ToggleButton** element.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of a **ToggleButton** element.

 |

#### TextOptions

Sets style options for a **Text** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

text

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Text resource type.

 |
| 

modifier

 | 

[TextModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

Yes

 | 

Text style modifier.

 |

#### ColorOptions

Sets style options for a **Color** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

color

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

New color of a specified element.

 |
| 

componentId

 | 

string

 | 

No

 | 

Yes

 | 

ID of the element for which the color is changed.

 |

#### ButtonOptions

Sets style options for a **Button** element of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Abnormal device behavior**: The styles implemented by this API are inconsistent with the UX specifications for TVs. For example, a focused and hovered component cannot be enlarged, the background color of the focused component does not change, and the text default color within a button is different. This API can work properly for other device types.

**Start version**: 6.0.0(20)

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

text

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Text on a **Button** element.

 |
| 

textColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Font color on a **Button** element.

The default value is **$r('sys.color.font\_primary')** for TVs and **$r('sys.color.font\_emphasize')** for other device types.

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Button tap callback.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable a **Button** element.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

buttonId

 | 

string

 | 

No

 | 

Yes

 | 

Button ID.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of a **Button** element.

 |

#### SuffixIconOptions

Sets style options for an **Icon** element in area C (on the right side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

iconValue

 | 

[PrefixIconType](#section9201529151513)

 | 

No

 | 

Yes

 | 

Icon resource in area C (on the right side of the list).

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Icon tap callback in area C (on the right side of the list).

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable an **Icon** element in area C (on the right side of the list).

**true**: yes

**false**: no

The default value is **true**.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of an icon in area C (on the right side of the list).

 |

#### SuffixArrowIconTextOptions

Sets style options for an arrow-text combined element in area C (on the right side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

startArrow

 | 

[SuffixArrowIconOptions](#section1042613291512)

 | 

No

 | 

Yes

 | 

Options of the start arrow in area C (on the right side of the list).

 |
| 

text

 | 

[TextOptions](#section4754175319)

 | 

No

 | 

Yes

 | 

Options of the text in area C (on the right side of the list).

 |
| 

endArrow

 | 

[SuffixArrowIconOptions](#section1042613291512)

 | 

No

 | 

Yes

 | 

Options of the end arrow in area C (on the right side of the list).

 |

#### SuffixArrowIconOptions

Sets style options for an arrow icon in area C (on the right side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

arrowColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Color of an arrow icon in area C (on the right side of the list).

 |
| 

onClick

 | 

[OnClickCallback](#section975195614188)

 | 

No

 | 

Yes

 | 

Arrow tap callback in area C (on the right side of the list).

 |
| 

arrowId

 | 

string

 | 

No

 | 

Yes

 | 

ID of an arrow icon in area C (on the right side of the list).

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable an arrow icon in area C (on the right side of the list).

**true**: yes

**false**: no

The default value is **true**.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of an arrow icon in area C (on the right side of the list).

 |

#### SelectStyle

Sets style options for a drop-down button of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

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

value

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

No

 | 

Text of a drop-down button.

 |
| 

valueColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Font color of a drop-down button.

Default value: **$r('sys.color.font\_secondary')**

 |
| 

arrowColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Color of the drop-down button arrow.

Default value: **$r('sys.color.icon\_secondary')**

 |
| 

optionValues

 | 

Array<[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)\>

 | 

No

 | 

No

 | 

Options of a drop-down button.

 |
| 

optionSymbol

 | 

Array<[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)\>

 | 

No

 | 

No

 | 

Array of symbol icons of drop-down options.

 |
| 

onSelect

 | 

[OnSelectCallback](#section213423822518)

 | 

No

 | 

Yes

 | 

Triggered when a drop-down option is selected.

 |
| 

showDefaultSelectedIcon

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to display the default icon in selected mode.

true: **yes**

false: **no**

The default value is **false**.

 |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable a drop-down button.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

selectId

 | 

string

 | 

No

 | 

Yes

 | 

ID of a drop-down button.

 |
| 

accessibilityOptions

 | 

[AccessibilityOptions](#section16412175163116)

 | 

No

 | 

Yes

 | 

Accessibility options of a drop-down button.

 |

#### SymbolType

type SymbolType= ResourceStr | SymbolGlyphModifier

Defines the symbol icon resource types supported for the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

Character string type.

 |
| 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

SymbolGlyph style modifier.

 |

#### PrefixIconType

type PrefixIconType= ImageOptions | SymbolGlyphOptions

Defines icon resource types supported in area A (on the left side of the list) of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ImageOptions](#section3582112115362)

 | 

Image type.

 |
| 

[SymbolGlyphOptions](#section171912040174014)

 | 

SymbolGlyph type.

 |

#### ImageType

type ImageType = ResourceStr | image.PixelMap

Defines the image resource types supported for the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

Character string type.

 |
| 

image.[PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

PixelMap type.

 |

#### IconSize

Enumerates the sizes supported for a **PrefixIcon**.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SMALL\_ICON

 | 

1

 | 

Icon type in area A (on the left side of the list): small icon with a size of 16 x 16 vp (28 x 28 vp on wearables specifically).

 |
| 

SYSTEM\_ICON

 | 

2

 | 

Icon type in area A (on the left side of the list): system icon with a size of 24 x 24 vp (32 x 32 vp on wearables specifically).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/vGKHhxu4T7eM9vkNBCgxyg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ECED9F3EFC7204A1E9195C1716EFE97176DE4702C268FE70057496C74E228D8)

All the left, middle, and right sides described above are in LTR mode.

#### OnClickCallback

type OnClickCallback = () => void

Tap event callback of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

#### OnChangeCallback

type OnChangeCallback = (isOn: boolean) => void

**onChange** event callback of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

isOn

 | 

boolean

 | 

Yes

 | 

Selected state of a **Switch**/**CheckBox**/**Radio**/**ToggleButton** element of the **HdsListItemCard** component.

-   **true**: The target changes from unselected to selected.
-   **false**: The target changes from selected to unselected.

 |

#### OnSelectCallback

type OnSelectCallback = (index: number, text: string) => void

**onSelect** event callback of the **HdsListItemCard** component.

**System capability**: SystemCapability.UIDesign.HDSComponent.Full

**Start version**: 6.0.0(20)

**Parameters:**

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

index

 | 

number

 | 

Yes

 | 

Index of the selected item. The value is greater than or equal to 0.

 |
| 

text

 | 

string

 | 

Yes

 | 

Value of the selected item. There is no requirement on the number of digits.

 |

#### Example

The following example illustrates the configuration of a simple list with items:

import {
  HdsListItemCard,
  IconSize,
  PrefixImage,
  PrefixIcon,
  SuffixIcon,
  SuffixSwitch,
  SuffixBadgeAndArrow
} from '@kit.UIDesignKit';
import { promptAction, ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@Component
struct HdsListItemCardExample {
  private scroller: ListScroller = new ListScroller();

  build() {
    Column() {
      List({ space: 5, scroller: this.scroller }) {
        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixIcon({
              iconSize: IconSize.SYSTEM\_ICON,
              iconValue: {
                image: $r('app.media.startIcon')
              },
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text'
              },
              secondaryText: {
                text: 'Secondary Text'
              },
              description: {
                text: 'Description Text'
              },
            },
            suffixItem: new SuffixIcon({
              iconValue: {
                symbol: $r('sys.symbol.circle\_dashed')
              },
              onClick: () => {
                promptAction.openToast({ message: 'onclick icon' });
              }
            }),
            onClick: () => {
              promptAction.openToast({ message: 'onclick hdslistitem' });
            },
          })
        }

        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixImage({
              image: $r('app.media.startIcon'),
              modifier: new ImageModifier().width(70).height(70).borderRadius(20)
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text'
              },
              secondaryText: {
                text: 'Secondary Text'
              },
              description: {
                text: 'Description Text'
              },
            },
            suffixItem: new SuffixSwitch({
              isCheck: false,
              selectColor: Color.Orange,
              onChange: (num: boolean) => {
                if (num) {
                  promptAction.openToast({ message: 'switch is true' });
                } else {
                  promptAction.openToast({ message: 'switch is false' });
                }
              },
            })
          })
        }

        ListItem() {
          HdsListItemCard({
            prefixItem: new PrefixIcon({
              iconSize: IconSize.SYSTEM\_ICON,
              iconValue: {
                symbol: $r('sys.symbol.ohos\_trash')
              },
            }),
            textItem: {
              primaryText: {
                text: 'Primary Text',
                modifier: new TextModifier().fontColor(Color.Pink),
              }
            },
            suffixItem: new SuffixBadgeAndArrow({
              badgeValue: 9,
              badgeColor: Color.Orange,
              textColor: Color.Blue,
            }, {
              color: Color.Orange
            })
          })
        }
      }
      .width('100%')
      .height('100%')
      .margin(10)
    }.backgroundColor(0x1a0a59f7).height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/gHeGi42NQvONLve23_LLPQ/en-us_image_0000002500424084.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B7B8A728DC1F07C1DB934B625717B0263D409DFAF7A87B88CDB73C3FA283CC1 "Click to enlarge")
