# FunctionalButton (Button Component)

This module provides the FunctionalButton component that can help you develop scenario-specific capabilities, including mobile number quick verification, real-time mobile number verification, avatar selection, authorization setting page display, app launch, shipping address selection, invoice title selection, map location selection, real-name information verification, identity verification by face, live view subscription, permission settings, service updates authorization code retrieval, atomic service sharing, feedback, and mobile number and risk level retrieval.

The FunctionalButton component must work with the [functionalButtonComponentManager](../functionalbuttoncomponentmanager-scenario-specific-convergent-button-component-m/document.md) component to implement relevant functions.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 4.1.0(11)

#### Modules to Import

import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';

#### FunctionalButton

Scenario-specific button component.

This module provides the scenario-specific button component FunctionalButton for HarmonyOS apps and atomic services to integrate for implementing relevant functions.

The button component needs to work with the [functionalButtonComponentManager](../functionalbuttoncomponentmanager-scenario-specific-convergent-button-component-m/document.md) component to implement relevant functions.

**Decorator type**: @Component

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 4.1.0(11)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator type.

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

params

 | 

functionalButtonComponentManager.[FunctionalButtonParams](../functionalbuttoncomponentmanager-scenario-specific-convergent-button-component-m/document.md#section684371910189)

 | 

Yes

 | 

@Prop

 | 

FunctionalButton component parameters.

 |
| 

controller

 | 

functionalButtonComponentManager.[FunctionalButtonController](../functionalbuttoncomponentmanager-scenario-specific-convergent-button-component-m/document.md#section942719311715)

 | 

Yes

 | 

\-

 | 

FunctionalButton component controller, which is used to receive click events of the component.

 |

#### \[h2\]build

build(): void

Constructor used to create a **FunctionalButton** object.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.AtomicserviceComponent.UIComponent

**Start version**: 4.1.0(11)

**Example:**

import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // Declare FunctionalButton.
        FunctionalButton({
          params: {
            // **OpenType.GET\_PHONE\_NUMBER** indicates that the button is used to verify a mobile number quickly.
            openType: functionalButtonComponentManager.OpenType.GET\_PHONE\_NUMBER,
            label: 'Verify mobile number quickly',
            // Adjust the button style.
            styleOption: {
              bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
              size: functionalButtonComponentManager.SizeType.DEFAULT,
              plain: false,
              disabled:false,
              loading: false,
              hoverClass: functionalButtonComponentManager.HoverClassType.HOVER\_CLASS,
              hoverStartTime: 0,
              hoverStayTime: 0,
              styleConfig: new functionalButtonComponentManager.ButtonConfig()
                .fontSize(20)
            },
          },
          // When **OpenType** is set to **GET\_PHONE\_NUMBER**, the callback must be **onGetPhoneNumber**.
          controller: new functionalButtonComponentManager.FunctionalButtonController()
            .onGetPhoneNumber((err, data) => {
              if (err) {
                // Error processing.
                hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
                return;
              }
              // Success processing.
              hilog.info(0x0000, "testTag", "succeeded in authenticating");
              // Obtain an authorization code.
              let authorizationCode = data.code;
            })
        })
      }.width('100%')
    }.height('100%')
  }
}
