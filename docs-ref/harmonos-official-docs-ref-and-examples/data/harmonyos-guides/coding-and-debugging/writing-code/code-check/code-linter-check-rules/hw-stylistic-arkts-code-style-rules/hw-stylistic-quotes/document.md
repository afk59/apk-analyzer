# @hw-stylistic/quotes

Enforce the use of single quotation marks for strings. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/quotes": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

export {a, b};

const a = 'hello';
const b = \`hello\`;

#### Example of Incorrect Code

// Strings must use single quotes.
export const a = "hello";

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
