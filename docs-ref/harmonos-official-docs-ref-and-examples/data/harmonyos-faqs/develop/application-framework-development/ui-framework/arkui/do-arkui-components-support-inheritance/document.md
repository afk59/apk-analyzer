# Do ArkUI components support inheritance?

1\. In the ArkUI declarative syntax, components are defined as structs and do not support inheritance. There are no plans to support inheritance-related features in the future.

2\. To extract a common base class for component reuse, consider using **attributeModifier** to achieve component reuse and extension. **attributeModifier** has implemented some capabilities, and more will be provided to meet diverse needs.

3\. To perform unified service processing during the lifecycle of the base class page, you can achieve this by using the observer to listen for the page's lifecycle.

**Reference**

[Attribute Modifier (AttributeModifier)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier)

[@ohos.arkui.observer (Observer)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkui-observer)
