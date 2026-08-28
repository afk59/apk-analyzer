# @typescript-eslint/typedef

Require type annotations in certain places.

For the check scope, see the **Options** section.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/typedef": "error"
  }
}

#### Options

For details, see [@typescript-eslint/typedef](https://typescript-eslint.io/rules/typedef/#options).

#### Example of Correct Code

export const text = 'text';

#### Example of Incorrect Code

// By default, no alarm is generated for this rule.

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
