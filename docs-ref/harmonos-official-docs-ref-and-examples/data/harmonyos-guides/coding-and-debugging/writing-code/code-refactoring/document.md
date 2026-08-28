# Code Refactoring

#### ArkTS/TS Code Refactoring

## Extract

This refactoring offers a safe, convenient way to extract selected code block or expression into a new method, constant, interface, variable, or type alias in the local scope. In the editor, select the code fragment you want to extract, right-click it, choose **Refactor** from the shortcut menu, and select a refactoring.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/AsbuuZj4Qm25K2HygvD8Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70C793EECBE1A0F9AED146B3C1C8E58E9C0B0EC98AFDA35A3375CD385C8BA2B3)

The Extract Type Alias refactoring is only available for TypeScript.

The Extract Method refactoring works for both code blocks and complete statements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/s0ZV7Q8qQV-lTh4-S93ilA/en-us_image_0000002501070498.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A339DF57DA9C808B25EDB0EF46F571C50A3672DA13BD87D2FA79E46BF309E24 "Click to enlarge")

In ArkTS code, you can extract code for invoking a component into an @Builder decorated method, or extract a component attribute expression into an @Styles or @Extend decorated method.

**How to use**: Select the component or attribute for which you want to extract code, right-click it, choose **Refactor** from the shortcut menu, and select **Extract Method...**. Private attributes of components can be extracted into @Extend decorated methods, and universal attributes can be extracted into @Styles or @Extend decorated methods.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/8RouG6ezRyO6XI0Xzkfs8g/en-us_image_0000002500910668.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14065A48A379F1BEA3A0C4A9F1DA7C8F5F2BE597E76422C31B0A9A6547AEDD57 "Click to enlarge")

You can extract a constant from a single-line expression.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/TN7CKAwuQUu9nnpI3fRP8w/en-us_image_0000002500910658.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C0563A5FA7DFD2C0AF006CDBC1FF63880F5239005AFBEFB18DA881E080F41E6 "Click to enlarge")

You can extract an interface from the variables of the selected object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/aVqyzNxgQRqnCFQMxW8xDw/en-us_image_0000002532670575.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=314617A257C378FE8A53AC5E3D790589C2BC587AC12D4F71A51014C787E3E7E9 "Click to enlarge")

You can select an expression and extract it into a variable.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/E-X3hX-4TSG1-RXSKHNWKw/en-us_image_0000002500910656.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42B781E9A9E8797974BA2EAB8F3932FB9DDEF96DA6903AA18FA9AB0253BA737F "Click to enlarge")

## Convert

Within refactoring, several useful conversion options are provided, as listed in the table below.

**Table 1** Convert options
| 
Option

 | 

Description

 | 

How to Use

 | 

Programming Language

 |
| :-- | :-- | :-- | :-- |
| 

Convert to class

 | 

Converts a function in the JS source code into an ES6 class.

 | 

Click or select a function name, right-click **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

NOTE:

If the function is being referenced in the current project, conflicts may occur. In this case, find references to it through **Find Usages**, and then click **Do Refactor** to ignore the conflict and execute the conversion; alternatively, modify the code in all places where the function is referenced to solve the conflict, and then execute the conversion again.

 | 

JS

 |
| 

Convert to anonymous function

 | 

Converts an arrow function into an anonymous function.

 | 

Select the variable assigned to the desired arrow function, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS

 |
| 

Convert to named function

 | 

Converts an arrow function into a named function.

 | 

Select the variable assigned to the desired arrow function, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |
| 

Convert to arrow function

 | 

Converts an anonymous function into an arrow function.

 | 

Select the variable assigned to the desired anonymous function, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |
| 

Convert default export to named export

 | 

Implements conversion between default exports and named exports.

 | 

Fully select a default export statement, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |
| 

Convert named export to default export

 | 

Fully select a named export statement, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 |
| 

Convert named imports to namespace import

 | 

Implement conversion between namespace imports and namespace imports.

 | 

Fully select the desired import statements, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |
| 

Convert namespace import to named imports

 | 

Fully select a namespace import statement, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 |
| 

Convert to template string

 | 

Converts a string into a template literal.

 | 

Select a string or entire expression, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |
| 

Convert to optional chain expression

 | 

Converts a null check expression into an optional chain expression.

 | 

Select the desired consecutive null-checking expression, right-click and choose **Refactor** > **Convert** or press **Ctrl+Alt+Shift+R** (**Option+Shift+Command+R** on macOS), and select the target conversion mode from the displayed dialog box.

 | 

JS/TS/ArkTS

 |

## Rename

Use the Rename refactoring to change names of variables, methods, object attributes, files, and modules and to correct all the references to them throughout code.

**How to use**: Select the symbol you to rename, (such as a variable, class, interface, or custom component), right-click it, choose **Refactor** from the shortcut menu, and select **Rename...** (or press **Shift+F6**). In the dialog box that appears, enter a new name, specify the scope for the refactoring in **Scope**, and click **Refactor**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/RtCNtE1NS5KJMlzCs512Tw/en-us_image_0000002532670567.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37177EF9324DCAE99A95A18A63BA8E153B1B14037EF6DA2A534A5E51E4A94F2E)

You can further specify references that do not need to be renamed. In the **Rename...** dialog box, click **Preview**. In the preview window displayed, right-click the item that does not need to be renamed and choose **Exclude/Remove** from the shortcut menu. When you are done, click **Do Refactor**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Cw2xGMU2S1qqiJ3q70yX-Q/en-us_image_0000002532670577.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEA41CBFD8C8F9396DA7CEDC28063D9C7F8AAC3FE5DFEFBEDDE8E1A4D576BCB4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/KRrjvw9-SI2qCyCpP1g1XQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D71B829903711D95E4DCC06D73A3AC7AC7C69776C0E2E644F42A943C501E1874)

If there is a C++ interface call within the ArkTS file, after you use the Rename feature, the function name involved in the C++ file will also be renamed.

## Move File

With the Move File refactoring, you can easily move a file between directories. Right-click the file and choose **Refactor** > **Move File...** from the shortcut menu. When prompted, specify the destination directory and click **Refactor** to move the file. Depending on your preferences, you may also select **Search for references** to search for and update the references to the file in the project, and select **Open in editor** to open the moved file in the editor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/mDZ2ultMSeqAxMsAITSpAg/en-us_image_0000002532750535.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7035E029C23F32EB022A8C2694A009A2C5F37897520290DB91680AF782D79D80)

## Safe Delete

If you are looking to safely delete files and symbols (variables, functions, or classes) from your code, use this Safe Delete refactoring. If there are references to the item to be deleted, the editor will prompt you to make necessary adjustments.

**How to use**: Right-click the symbol or file you want to delete, and choose **Refactor** > **Safe Delete** from the shortcut menu. Click **OK** to search for usages of the item in the code. If any usage is found, click **View Usages** to view them. Proceed with necessary adjustments. If you click **Delete Anyway**, the item will be deleted regardless of conflicts.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/3pKG1CdKS4ODUFlxFYZXTg/en-us_image_0000002532750531.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1F864CE58CB9B0AE9A4838ADD299905CE4587727ED1022D038D54426CF213B0)

#### C++ Code Refactoring

In C++ code, use the reliable refactorings to improve your development efficiency.

## Inline

The Inline refactoring replaces the macro inline with its expansion. Right-click the macro you want to expand and choose **Refactor** > **Inline**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KlzVcXmMR4G6-pR3qDJSlQ/en-us_image_0000002532750523.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B9E61400E763D9F488FE9E8A4DE8D8636C72BC78CCFBBDABC4F8CD2724C10FF)

## Swap If Branches

The Swap If Branches refactoring lets you swap if branches of the selected if-else statement and negate its condition.

**Constraints**

-   The selected code block must be a complete if-else statement with a pair of braces ({}).
-   If the selected if-else statement contains a nested if-else statement, the refactoring only applies to the outermost statement. For the if() -else if()-else() structure, the refactoring only applies to the if-else structure at the last layer.
-   The condition of a value assignment statement cannot be negated.

**How to Use**

Right-click an if-else statement, and choose **Refactor** > **Swap If Branches**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/B3R6mzuDQbKI_eruRicfBA/en-us_image_0000002532670573.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13D0E9E45E7615E3F8409B6964BBDFC075352C6582DCCB0B69728E9A947F222D "Click to enlarge")

## Move to Declaration

The Move to Declaration refactoring lets you move a function body from a source file to its declaration in a header file. Right-click a function name, and choose **Refactor** > **Move to Declaration**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/kc7CbtqSTR-hShyLs94GjA/en-us_image_0000002501070496.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7050292AFD2CA75D19B260663D4599348716B1B6A8D6B653C8C4076C2D571D70)

## Move to Implementation

The Move to Implementation refactoring lets you move a function declaration to where the function is used. Right-click a function name, choose **Refactor** > **Move to Implementation**, and select the destination file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/8YWU036fSxqj6sPkIXcMxQ/en-us_image_0000002501070506.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAB3D07FCBE374008656744D208183CB4572642B496D10ADA26888B939562FC5)

## Convert To Raw String

With the Convert To Raw String refactoring, you can convert a string that contains escape characters (\\n, \\t, \\", \\\\, \\') into a raw string. Currently, only standard strings are supported. Other strings, such as u8-prefixed strings, are not supported.

Right-click the string you want to convert, and choose **Refactor** > **Convert To Raw String**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/PXRVV8UJSgW5r23nrRjE4w/en-us_image_0000002501070504.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A85113678989ED20CB4BEEC49343B8503C13EFA9DE91A1C55F7FF54F938388C "Click to enlarge")

## Generate-Constructor

Within refactoring, you can generate a default constructor for member variables of a class.

**Constraints**

1.  Uninitialized member variables of a class are not supported.
2.  This refactoring does not work in locations other than the **class** keyword, class names, and curly braces.
3.  This refactoring does not apply to classes that already have a constructor with input parameters.

**How to use**: Right-click a class name, and choose **Generate...** > **Constructor**; when prompted, click **Define**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AjDN4S2JScWLfuipJDMAxg/en-us_image_0000002501070494.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8AD0077D2784BF42C198F81A3ED1C47E2F86777C67F23F7A0D443DED505A923)

## Extract Variable

The Extract Variable refactoring enables you to create a local variable for the selected expression. Right-click an expression, and choose **Refactor** > **Extract Variable**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/JJd9nTHnRx6Uj1otUWIB4w/en-us_image_0000002500910648.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25B3C07BB1D55EB34168C1E39E81300F2C6983C22D4227E79B0F3A8B50D587BF "Click to enlarge")

## Remove Using Namespace

The Remove Using Namespace refactoring lets you remove a namespace to avoid name conflicts. Right-click the namespace you want to remove, and choose **Refactor** > **Remove Using Namespace**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/alM9xAlsTdyvOhVt4ZWg2Q/en-us_image_0000002532670569.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA6297DFCE349EC863BE64A25FBACB2E70E2372B84FBD60556CA478131FC8980)

## Add Using

The Add Using refactoring lets you add a using declaration to define a type alias. Right-click the code where you want to add a using declaration, and choose **Refactor** > **Add Using**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/wwHdoSXSSqyt2SpGBXG3LQ/en-us_image_0000002500910662.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45EF794CC1B669A2E44A7B4EA7C193D5E0A16FA16E100112F8A00EAB243E2458)

## Expand Auto Type

The Expand Auto Type refactoring lets you replace the auto type with the inferred type. Right-click the **auto** keyword, and choose **Refactor** > **Expand Auto Type**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/tSFXfiV1QBqD1fRhT-6xjg/en-us_image_0000002532750521.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB8A4D357AC18910945B2B643A4ABA8CB65AE15E7511B73A05FE2B1C5F3469E9)

## Generate-Copy/Move Members

Within refactoring, you can generate implicitly-declared copy/move members in a class. Right-click the class for which you want to add implicitly-declared copy/move members, and choose **Generate...** > **Copy/Move Members**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/XuVB--3XQXyJM0AN4TisuQ/en-us_image_0000002501070508.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062148Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A3A650A16FB0395EBE0F30548F5521D49517BFA6544229A4CD45E41F6F04066)
