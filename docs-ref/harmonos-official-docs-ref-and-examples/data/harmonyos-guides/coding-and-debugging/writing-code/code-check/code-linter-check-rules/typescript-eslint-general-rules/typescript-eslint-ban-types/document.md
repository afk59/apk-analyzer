# @typescript-eslint/ban-types

Disallow certain types.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-types": "error"
  }
}

#### Options

This rule supports the following options:

type Options = {
  types: {
    \[key: string\]: boolean | string | { message: string, fixWith: string } | null;
  };
  extendDefaults: boolean;
}

-   **types**: An object that configures which types to check and whether to disallow them. Each key in this object is a string representing the name of a type to check. The corresponding value supports the following configurations:
    -   **boolean**: A Boolean value. If **true**, the type is disallowed and the default warning message is used. If **false**, the type remains allowed (this is typically used with **{ extendDefaults: true }** to exclude certain predefined types from the check).
    -   **string**: Custom warning message to display.
    -   **{ message: string, fixWith: string }**: An object where **message** is a custom warning message, and **fixWith** is the type to use for automatic replacement.
    -   **null**: Default warning message for the type to display.

-   **extendDefaults**: A Boolean value that defaults to **true**. When set to **true**, it enables checking of TypeScript's built-in primitive wrapper types, including String, Boolean, Number, Symbol, BigInt, Function, and Object. Setting it to **false** disables checking of these types.

Example:

"@typescript-eslint/ban-types": \[
  "error",
  {
    "types": {
      "String": true,   
      "Number": false,  
      "MyType": "Do not use 'MyType'",  
      "MyTypeWithFix": {
        "message": "Do not use 'MyTypeWithFix', use 'MyType' instead",
        "fixWith": "MyType"
      }
    },
    "extendDefaults": true
  },
\]

#### Example of Correct Code

// Type casing should remain consistent in lowercase.
const str: string = 'foo';
const bool: boolean = true;
const num: number = 1;
const bigInt: bigint = 1n;

// Use the correct function types.
const func: () => string = () => 'hello';

export { str, bool, num, bigInt, func };

#### Example of Incorrect Code

// Type casing should remain consistent in lowercase.
const str: String = 'foo';
const bool: Boolean = true;
const num: Number = 1;
const bigInt: BigInt = 1n;

// Use the correct function types.
const func: Function = () => 'hello';

export { str, bool, num, bigInt, func };

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
