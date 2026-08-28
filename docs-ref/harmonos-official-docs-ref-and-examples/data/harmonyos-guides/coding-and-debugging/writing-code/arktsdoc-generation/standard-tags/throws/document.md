# @throws

Records errors that may be caused by functions. You can use the **@throws** tag multiple times in an ArkTSDoc comment.

#### Syntax

@throws description

#### Example

The following is an example of using the **@throws** tag with a description.

/\*\*
 \* @throws Will throw an error if the argument is null.
 \*/
export function bar(x: number) {
  throw new Error();
}
