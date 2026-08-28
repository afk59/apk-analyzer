# @deprecated

Indicates that an identifier has been deprecated in the code.

#### Syntax

@deprecated \[<some text>\]

#### Example

You can use the **@deprecated** tag alone, or you can include some text that describes details about deprecated.

The following is an example of using the tag to identify old functions have been deprecated since version 2.0.

/\*\*
 \* @deprecated since version 2.0
 \*/
export function old() {}
