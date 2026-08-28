# @hw-stylistic/max-len

Enforce a maximum line length of 120 characters. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/max-len": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

@Entry
@Component
struct Index {
  message: string = 'hello';

  build() {
    Text(this.message)
  }
}

#### Example of Incorrect Code

// This line has a length of 135. Maximum allowed is 120.
export const longLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongLongName = 10;

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
