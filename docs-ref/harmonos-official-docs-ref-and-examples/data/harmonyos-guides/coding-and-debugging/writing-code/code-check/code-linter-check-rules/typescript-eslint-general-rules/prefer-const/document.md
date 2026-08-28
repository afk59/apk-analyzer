# prefer-const

Require **const** declarations for variables that are never reassigned after declared.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "prefer-const": "error"
  }
}

#### Options

For details, see [eslint/prefer-const](https://eslint.nodejs.cn/docs/latest/rules/prefer-const#选项).

#### Example of Correct Code

const a = 'hello';
console.log(a);

#### Example of Incorrect Code

// As variable a is not reassigned a value after it is declared, you are advised to use the const keyword to declare it.
let a = 'hello';
console.log(a);

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
