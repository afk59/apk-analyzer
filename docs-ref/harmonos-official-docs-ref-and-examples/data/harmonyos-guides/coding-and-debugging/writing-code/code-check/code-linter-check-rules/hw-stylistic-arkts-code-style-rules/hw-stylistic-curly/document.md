# @hw-stylistic/curly

Enforce wrapping of conditional statements and loop statements in curly braces. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/curly": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

export function test(a: number, b: number) {
  if (a > b) {
    console.info('doSomething');
  } else if (a === b) {
    console.info('doSomething');
  } else {
    console.info('doSomething');
  }

  while (a > b) {
    a--;
    console.info('doSomething');
  }

  console.info('doSomething');
}

#### Example of Incorrect Code

export function test(a: number, b: number) {
  if (a > b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else if (a === b)
  // Expected { after 'if' condition.
    console.info('doSomething');
  else
  // Expected { after 'else'.
    console.info('doSomething');
  console.info('doSomething');
}

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
