# @param

Provides the description of a function parameter.

To improve readability of ArkTSDoc comments, insert a hyphen (-) before the description, ensuring it is surrounded by spaces on both sides.

#### Syntax

@param \[<description>\]

#### Example

The following example demonstrates how to include a description in the **@param** tag.

Variable description:

/\*\*
 \* @param somebody Somebody's name.
 \*/
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}

Add a hyphen (-) before the variable description to make it easier to read.

/\*\*
 \* @param somebody - Somebody's name.
 \*/
export function sayHello(somebody: string): void {
  console.log('Hello ' + somebody);
}
