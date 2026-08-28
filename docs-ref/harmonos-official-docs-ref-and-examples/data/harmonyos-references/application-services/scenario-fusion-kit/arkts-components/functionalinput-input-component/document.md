# FunctionalInput (Input Component)

This module provides the FunctionalInput component for your app to quickly display a region selection page for users to select a region.

The FunctionalInput component needs to work with the [functionalInputComponentManager](../functionalinputcomponentmanager-scenario-specific-convergent-input-component-man/document.md) component to implement relevant functions.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 5.1.0(18)

#### Module Import

import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';

#### FunctionalInput

Scenario-specific input component.

This module provides the FunctionalInput component for HarmonyOS apps and atomic services to implement functions such as selecting a province/district/city and modifying the text and style of an input box.

The FunctionalInput component needs to work with the [functionalInputComponentManager](../functionalinputcomponentmanager-scenario-specific-convergent-input-component-man/document.md) component to implement relevant functions.

**Decorator type**: @Component

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 5.1.0(18)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

params

 | 

functionalInputComponentManager.[FunctionalInputParams](../functionalinputcomponentmanager-scenario-specific-convergent-input-component-man/document.md#section19784874147)

 | 

Yes

 | 

@Prop

 | 

FunctionalInput component parameters.

 |
| 

controller

 | 

functionalInputComponentManager.[FunctionalInputController](../functionalinputcomponentmanager-scenario-specific-convergent-input-component-man/document.md#section942719311715)

 | 

Yes

 | 

\-

 | 

FunctionalInput component controller, which is used to receive click events of the component.

 |

#### \[h2\]build

build(): void

Constructor used to create a **FunctionalInput** object.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.0(18).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 5.1.0(18)

**Example:**

import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { SymbolGlyphModifier, TextInputModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State inputContent: string = '';

  build() {
    Column() {
      Row() {
        Text('Region').width(64)
        // Declare FunctionalInput.
        FunctionalInput({
          params: {
            // **InputType.SELECT\_DISTRICT** indicates the province/city/district selector input type.
            inputType: functionalInputComponentManager.InputType.SELECT\_DISTRICT,
            textInputValue: {
              text: this.inputContent,
              placeholder: 'Province, city, district, street',
            },
            // Adjust the TextInput style.
            inputAttributeModifier: new TextInputModifier()
              .fontColor($r('sys.color.ohos\_id\_color\_badge\_red'))
              .onChange((value) => {
                if (value !== this.inputContent) {
                  this.inputContent = value;
                }
              }),
            // Place the icon at the end.
            icon: $r('sys.symbol.xmark'),
            // Set the event and style of the icon.
            iconSymbolModifier: new SymbolGlyphModifier()
              .onClick(() => {
                this.inputContent = '';
              })
              .fontSize(32),
          },
          // When **InputType** is set to **SELECT\_DISTRICT**, the callback must be **onSelectDistrict**.
          controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
            data: functionalInputComponentManager.DistrictSelectResult) => {
            if (err) {
              // Error processing.
              hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
              return;
            }
            // Success processing.
            hilog.info(0x0000, "testTag", "succeeded in selecting district");
            // Display the selected region information in the input component.
            this.inputContent = data.inputContent;
          })
        })
          .layoutWeight(1)
      }.height('100%')
    }.width('100%')
  }
}
