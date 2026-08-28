# @performance/foreach-args-check

Enforce the use of **keyGenerator** in the **ForEach** parameter.

In [scenarios where frame loss occurs during scrolling](../../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-rendering-control/foreach-rendering-repeated-content/document.md#key-generation-rules), modify the code according to this rule.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/foreach-args-check": "warn",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

@Entry
@Component
struct ForeachTest {
  private data: string\[\] = \['1', '2', '3'\];
  build() {
    RelativeContainer() {
      List() {
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        }, (item: string, index: number) => item)
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}

#### Example of Incorrect Code

@Entry
@Component
struct ForeachTest {
  private data: string\[\] = \['1', '2', '3'\];
  build() {
    RelativeContainer() {
      List() {
        // Error: ForEach lacks the third parameter.
        ForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text(item);
          }
        })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}

#### Rule Set

plugin:@performance/recommended
plugin:@performance/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
