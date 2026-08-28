# @performance/sparse-array-check

Avoid sparse arrays.

You are advised to modify the code to comply with the [ArkTS Performant Programming Practices](../../../../../../getting-started/learning-arkts/arkts-performant-programming-practices/document.md).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/sparse-array-check": "suggestion",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

let index = 3;
let result: number\[\] = \[\];
result\[index\] = 0;

#### Example of Incorrect Code

let count = 100000;
let arr1: number\[\] = new Array(count);
let arr2 = new Array<number>();
arr2\[9999\] = 0;

#### Rule Set

plugin:@performance/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
