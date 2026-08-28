# @hw-stylistic/brace-style

Require the opening brace of a block to be placed on the same line as its corresponding statement or declaration. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/brace-style": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

try {
  // doSomething
} catch (e) {
  // doSomething
} finally {
  // doSomething
}

#### Example of Incorrect Code

try
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
catch (e)
// Opening curly brace does not appear on the same line as statement before.
{

// Closing curly brace does not appear on the same line as statement after.
}
finally
// Opening curly brace does not appear on the same line as statement before.
{

}

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
