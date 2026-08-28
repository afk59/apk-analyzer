# @hw-stylistic/no-tabs

Disallow tabs for indentation. Spaces are recommended. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

export const message: string = 'Hello World';

#### Example of Incorrect Code

export	const	message:	string = 'Hello World';

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
