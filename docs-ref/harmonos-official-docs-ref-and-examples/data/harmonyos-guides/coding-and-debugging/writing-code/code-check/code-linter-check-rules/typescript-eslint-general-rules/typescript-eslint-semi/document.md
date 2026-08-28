# @typescript-eslint/semi

Require or disallow semicolons.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}

#### Options

For details, see [@typescript-eslint/semi](https://eslint.nodejs.cn/docs/rules/semi#选项).

#### Example of Correct Code

export const name = 'ESLint';

export class Foo {
  public bar = '1';
}

#### Example of Incorrect Code

// By default, a semicolon (;) is required at the end of a statement.
export const name = 'ESLint'

export class Foo {
  // By default, a semicolon (;) is required at the end of a statement.
  public bar = '1'
}

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
