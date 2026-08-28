# eqeqeq

Require the use of **\===** and **!==**.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "eqeqeq": "error"
  }
}

#### Options

For details, see [eslint/eqeqeq](https://eslint.nodejs.cn/docs/latest/rules/eqeqeq#选项).

#### Example of Correct Code

export function test(a: string, b: string) {
  return a === b;
}

#### Example of Incorrect Code

export function test(a: string, b: string) {
  // Expected '===' and instead saw '=='.
  return a == b;
}

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
