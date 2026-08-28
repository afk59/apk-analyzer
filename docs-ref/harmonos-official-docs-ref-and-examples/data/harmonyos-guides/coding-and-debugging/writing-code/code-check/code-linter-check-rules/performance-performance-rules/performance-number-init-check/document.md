# @performance/number-init-check

Enforce correct use of numbers.

You are advised to modify the code to comply with the [ArkTS Performant Programming Practices](../../../../../../getting-started/learning-arkts/arkts-performant-programming-practices/document.md).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/number-init-check": "suggestion",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

let intNum = 1;
intNum = 2;
let floatNum = 1.3;
floatNum = 2.4;

#### Example of Incorrect Code

let intNum = 1;
// intNum is declared as int. Avoid changing it to float.
intNum = 1.1; 
let floatNum = 1.3;
// floatNum is declared as float. Avoid changing it to int.
floatNum = 2; 

#### Rule Set

plugin:@performance/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
