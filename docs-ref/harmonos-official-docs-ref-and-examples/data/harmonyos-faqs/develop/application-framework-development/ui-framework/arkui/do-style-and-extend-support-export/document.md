# Do @Style and @Extend support export?

1\. Currently, @Styles and @Extend do not support export, and these decorators will not evolve further in the future.

2\. For style reuse, you are advised to use the **attributeModifier** attribute. By customizing a class to inherit the modifier of the corresponding base component and setting reusable attributes within the class, there is no restriction on exporting the corresponding class. Yet, **attributeModifier** is still under development, with events and gestures processing anticipated in upcoming enhancements.

**Reference**

[attributeModifier](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)
