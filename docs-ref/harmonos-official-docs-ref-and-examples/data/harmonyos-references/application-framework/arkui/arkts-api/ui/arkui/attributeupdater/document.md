# AttributeUpdater

**AttributeUpdater** directly set attributes to a component to trigger UI re-renders, without marking them as state variables.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/WIrpEfYNRQ2d8-jmgPbDFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2091830FDDFBE1C3C028E1D4CFB63EA9FFB58BD16A1513C91E2EEDB2F28CCA09)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { AttributeUpdater } from '@kit.ArkUI';

**Instructions**

1.  Whenever possible, avoid using **AttributeUpdater** in conjunction with attribute methods or implementing methods like **applyNormalAttribute** in **AttributeUpdater** to update the same attribute on the same component. Doing so involves mixed use of the state management update mechanism, which can be confusing.
    
2.  When **AttributeUpdater** is used together with an attribute method, the one that is used later takes effect. Specifically:
    
    If use of **AttributeUpdater** is followed by an attribute method call, the attribute method takes effect under the state management mechanism.
    
    If use of **AttributeUpdater** follows an attribute method call, it takes effect.
    
3.  An **AttributeUpdater** object can only be associated with one component at a time; otherwise, the set attributes may only take effect on one component.
    
4.  You need to ensure the type matching of **T** and **C** in **AttributeUpdater** yourself. For example, if **T** is ImageAttribute, **C** should be ImageInterface;
    
    otherwise, it may cause functionality issues when **updateConstructorParams** is used.
    
5.  Currently, **updateConstructorParams** supports only the following components: **Button**, **Image**, **Text**, **Span**, **SymbolSpan**, **ImageSpan**.
    
6.  **AttributeUpdater** does not support operations related to state management, such as switching between light and dark modes.
    
7.  When the API of the [AttributeUpdater](#attributeupdatert-c--initializert) object is invoked in the scenario of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context), you are advised to use the [runScopedTask](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#runscopedtask) API of [UIContext](../../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to specify the UI context. For details, see [Executing the Closure Bound to a UI Instance](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#executing-the-closure-bound-to-a-ui-instance).
    

#### Initializer<T>

type Initializer<T> = () => T

Defines a decorator for updating attributes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AttributeUpdater<T, C = Initializer<T>>

Represents the implementation class of [AttributeModifier](../../../../arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifiert). You need to customize a class to inherit **AttributeUpdater**.

**C** indicates the constructor type of the component, for example, **TextInterface** of the **Text** component and **ImageInterface** of the **Image** component. It is required only when **updateConstructorParams** is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]applyNormalAttribute

applyNormalAttribute?(instance: T): void

Defines the function for updating attributes in normal state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

#### \[h2\]initializeModifier

initializeModifier(instance: T): void

Initializes the component's attributes to the default values defined in this **AttributeUpdater**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

**Example**

This example shows how to use **initializeModifier** to initialize attribute values.

// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  // Triggered when the AttributeUpdater object is used for the first time.
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ffd5d5d5')
      .labelStyle({ maxLines: 3 })
      .width('80%')
  }

  // Triggered when the AttributeUpdater object is applied or updated.
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.borderWidth(1);
  }
}

@Entry
@Component
struct Index {
  modifier: MyButtonModifier = new MyButtonModifier();
  @State flushTheButton: string = 'Button';

  build() {
    Row() {
      Column() {
        Button(this.flushTheButton)
          .attributeModifier(this.modifier)
          .onClick(() => {
            // Update component attributes via AttributeUpdater's attribute property.
            // Note: The component must be bound to the AttributeUpdater via its attributeModifier attribute method.
            this.modifier.attribute?.backgroundColor('#ff2787d9').labelStyle({ maxLines: 5 });
          })
          .margin('10%')
        Button('Trigger Button Update')
          .width('80%')
          .labelStyle({ maxLines: 2 })
          .onClick(() => {
            this.flushTheButton = this.flushTheButton + ' Updated';
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fXuU_ctKQZ6xA4iwjLgCng/en-us_image_0000002537925310.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B079712B272CB24E573D02B2F1004382FF0CF013B119E3D23879C23CDC4C644)

#### \[h2\]attribute

get attribute(): T | undefined

Obtains the attribute class instance corresponding to the component in **AttributeUpdater**. The instance can then be used to directly update attributes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| T | undefined | Returns the attribute class instance of the component in **AttributeUpdater** if it exists; returns **undefined** otherwise. |

**Example**

This example shows how to directly update attributes through **AttributeUpdater**.

// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ffd5d5d5')
      .width('50%')
      .height(30);
  }
}

@Entry
@Component
struct updaterDemo2 {
  modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button("Button")
          .attributeModifier(this.modifier)
          .onClick(() => {
            this.modifier.attribute?.backgroundColor('#ff2787d9').width('30%');
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/LWTxmDpDQoOZDrMk1GjWnw/en-us_image_0000002568685087.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A134F32C2178FF997E988D9BA22319A2BADCEC00B604CBAF718E3FF75D4A9135)

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| updateConstructorParams | [C](#attributeupdatert-c--initializert) | No | No | **C** indicates the constructor type of the component, for example, **TextInterface** of the **Text** component and **ImageInterface** of the **Image** component. The type is used to change the constructor input parameters of the component. |

**Example**

This example demonstrates how to use **updateConstructorParams**.

// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyTextModifier extends AttributeUpdater<TextAttribute, TextInterface> {
  initializeModifier(instance: TextAttribute) {
  }
}

@Entry
@Component
struct attributeDemo3 {
  private modifier: MyTextModifier = new MyTextModifier();

  build() {
    Row() {
      Column() {
        Text("Initialize")
          .attributeModifier(this.modifier)
          .fontSize(14).border({ width: 1 }).textAlign(TextAlign.Center).lineHeight(20)
          .width(200).height(50)
          .backgroundColor('#fff7f7f7')
          .onClick(() => {
            this.modifier.updateConstructorParams("Updated");
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4_RaEx0HRSmHN6s2MNzE5g/en-us_image_0000002568765097.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48D278002E59B81D1C2E98F945BF58DD808646EEDBB45D745BBA4A6A2FA63B2E)

#### \[h2\]onComponentChanged

onComponentChanged(component: T): void

Invoked to notify the application that the component bound to the same custom **Modifier** object changes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| component | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, **ButtonAttribute** for the **Button** component and **TextAttribute** for the **Text** component. |

**Example**

// xxx.ets
import { AttributeUpdater } from '@kit.ArkUI';

class MyButtonModifier extends AttributeUpdater<ButtonAttribute> {
  initializeModifier(instance: ButtonAttribute): void {
    instance.backgroundColor('#ff2787d9')
      .width('50%')
      .height(30);
  }

  onComponentChanged(instance: ButtonAttribute): void {
    instance.backgroundColor('#ff519db4')
      .width('50%')
      .height(30);
  }
}

@Entry
@Component
struct updaterDemo4 {
  @State btnState: boolean = false;
  modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button("Test")
          .onClick(() => {
            this.btnState = !this.btnState;
          }).margin({ bottom: 20 })

        if (this.btnState) {
          Button("Button")
            .attributeModifier(this.modifier)
        } else {
          Button("Button")
            .attributeModifier(this.modifier)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/ysf5zUYQTgGvMknkReoHUQ/en-us_image_0000002537765372.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FADB389AB7F5AB723428F465E15E58AD22345A889E74AED09277244E6EC85022)
