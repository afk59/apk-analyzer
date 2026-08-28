# @typescript-eslint/array-type

Uses the same style consistently for arrays consistently. For example, consistently use either T\[\] or Array<T>.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/array-type": "error"
  }
}

#### Options

For details, see [typescript/array-type](https://typescript-eslint.io/rules/array-type#options).

#### Example of Correct Code

const x: string\[\] = \['a', 'b'\];
const y: readonly string\[\] = \['a', 'b'\];

export { x, y };

#### Example of Incorrect Code

const x: Array<string> = \['a', 'b'\];
const y: ReadonlyArray<string> = \['a', 'b'\];

export { x, y };

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
