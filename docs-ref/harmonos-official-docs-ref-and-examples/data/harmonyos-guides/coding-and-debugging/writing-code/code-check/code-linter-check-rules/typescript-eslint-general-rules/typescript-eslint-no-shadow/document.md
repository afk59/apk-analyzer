# @typescript-eslint/no-shadow

Disallow variable declarations from shadowing variables declared in the outer scope.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-shadow": "error"
  }
}

#### Options

For details, see [@typescript-eslint/no-shadow](https://typescript-eslint.io/rules/no-shadow/#options).

#### Example of Correct Code

/\*eslint no-shadow: "error"\*/
const a = '1';
export function b() {
  const a1 = '10';
  console.info(a1);
}

export const c = () => {
  const a1 = '10';
  console.info(a1);
};

console.info(a);

#### Example of Incorrect Code

/\*eslint no-shadow: "error"\*/
const a = '3';
export function b() {
  const a = '10';
  console.info(a);
}

export const c = () => {
  const a = '10';
  console.info(a);
};

console.info(a);

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
