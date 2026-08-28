# {@link}

Creates a link to a specified namepath or web page. The link text can be provided in different formats.

#### Syntax

-   {@link namepathOrURL}
-   \[link text\]{@link namepathOrURL}
-   {@link namepathOrURL|link text}
-   {@link namepathOrURL link text (after the first space)}

#### Example

The following is an example of using the **{@link}** tag to provide the link text.

/\*\*
 \* See {@link MyClass}.
 \* Also, check out {@link https://www.example.com/cn/ | Example} and
 \* {@link https://www.example.com/cn/ Example}.
 \*/
export function myFunction() {}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/FkA6kLy3SmCt_GlGo3SKyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2739FF9E087B2DD6C0F2828467226A978904120E55423B423A142BF6CFADD06)

If namepath is a class name, for example, **MyClass** in the example, you need to define the class in the current module to perform correct redirection. Currently, redirection to attributes and methods in a class is not supported.
