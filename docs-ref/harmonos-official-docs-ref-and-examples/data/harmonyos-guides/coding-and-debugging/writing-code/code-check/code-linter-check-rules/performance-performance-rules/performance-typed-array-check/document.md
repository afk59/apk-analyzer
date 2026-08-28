# @performance/typed-array-check

Prioritize **TypedArray** for value arrays.

You are advised to modify the code to comply with the [ArkTS Performant Programming Practices](../../../../../../getting-started/learning-arkts/arkts-performant-programming-practices/document.md).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/typed-array-check": "suggestion",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

const typedArray1 = new Int8Array(\[1, 2, 3\]); 
const typedArray2 = new Int8Array(\[4, 5, 6\]);  
let res = new Int8Array(3);
for (let i = 0; i < 3; i++) {
     res\[i\] = typedArray1\[i\] + typedArray2\[i\];
}

#### Example of Incorrect Code

const typedArray1: number\[\] = new Array(1, 2, 3);
const typedArray2: number\[\] = new Array(4, 5, 6);
let res: number\[\] = new Array(3);
for (let i = 0; i < 3; i++) {
     res\[i\] = typedArray1\[i\] + typedArray2\[i\];
}

#### Rule Set

plugin:@performance/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
