# @security/no-commented-code

Disallow commented-out code.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-commented-code": "warn"
  }
}

#### Options

This rule is not configurable.

#### Examples of Correct Code

// this is a comment

#### Examples of Incorrect Code

// console.log('info')

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
