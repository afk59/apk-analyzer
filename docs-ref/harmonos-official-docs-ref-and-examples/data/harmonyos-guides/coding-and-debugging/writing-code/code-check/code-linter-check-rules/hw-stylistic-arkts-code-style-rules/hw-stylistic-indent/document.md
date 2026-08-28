# @hw-stylistic/indent

Enforce an indentation level for **case** and **default** clauses in **switch** statements. This rule only checks .ets files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/indent": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
    case E.a:
      console.info('doSomething');
      break;
    case E.b:
    case E.c:
      console.info('doSomething');
      break;
    default:
      console.info('doSomething');
  }
}

#### Example of Incorrect Code

enum E {
  a = 'a',
  b = 'b',
  c = 'c'
}

export function test(e: E) {
  switch (e) {
      // Expected indentation of 2 relative to switch.
      case E.a:
      // Expected indentation of 2 relative to case.
      console.info('hello');
      // Expected indentation of 2 relative to case.
      break;
    case E.b:
      console.info('hello');
      break;
    case E.c:
    // Expected indentation of 2 relative to case.
    console.info('hello');
      break;
    default:
    // Expected indentation of 2 relative to default.
    console.info('hello');
  }
}

#### Rule Set

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
