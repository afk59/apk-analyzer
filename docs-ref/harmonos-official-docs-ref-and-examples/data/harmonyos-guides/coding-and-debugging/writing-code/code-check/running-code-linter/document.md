# Running Code Linter

Code Linter checks code in files or folders in a module against best practices and programming rules, which you can configure as instructed in [Configuring Code Check Rules](#section19310459444).

Of the detected issues, you can fix them manually based on the provided suggestions or have them automatically fixed with a single click.

#### Configuring Code Check Rules

When a project is created, the **code-linter.json5** configuration file is created in the root directory of the project by default. You can configure the code check scope and effective check rules. To use a historical project for development, right-click the project and choose **Code Linter** > **Generate Config File** from the shortcut menu to create the **code-linter.json5** configuration file.

The **files** and **ignore** options configure the check scope, and **ruleSet** and **rules** configure the effective check rules. Specifically, set the fields as follows:

**files**: a set of files to which the code check applies. If this field is not specified, the code check applies to the currently selected single file or all .ets files within the selected multiple files or folders.

**ignore**: a set of files to which the code check should not apply. The value is an array of directories or files relative to the root directory of the project, that is, where the **code-linter.json5** file is located. Example: **build/\*\*/\***.

**ruleSet**: rule set to be applied. Multiple rules can be imported to the rule set at once. For details, see [Code Linter Check Rules](../code-linter-check-rules/document.md). Currently, the following rule sets are supported:

-   @typescript-eslint: general rules
-   @security: security rules
-   @performance: performance rules
-   @previewer: preview rules
-   @cross-device-app-dev: rules oriented to one-time development for multi-device deployment
-   @hw-stylistic: ArkTS code style rules
-   @correctness: correctness rules
-   @compatibility: compatibility rules
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/R77vfLacReCqlYIkCVudFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=786ACF513F6C38C3850D5B7AB5843AE2E35F8266B5B33F24EE01828ECE677D68)
    
    -   The above rule sets are divided into two categories: **all** and **recommended**. The **all** rule set is the complete collection of rules, including every rule available; the **recommended** rule set is a curated selection of rules suggested for use. The **all** rule set encompasses the **recommended** rule set.
    -   If a **code-linter.json5** file is not created in the project's root directory, Code Linter will, by default, conduct checks against the rules included in the @performance/recommended and @typescript-eslint/recommended rule sets.
    

**rules**: a set of rules different from those in the specified rule set. You can edit existing rules in the rule set or add new rules. For example, you can change the severity of a rule in the rule set from **warn** to **error**.

**overrides**: custom configuration that only applies to specific files and folders.

**extRuleSet**: custom rules for code check. For details, see [Custom Rule Development Guide](https://gitcode.com/openharmony-sig/homecheck/blob/master/document/developer/ExtRule自定义规则开发指南.md). This field is supported since DevEco Studio 5.1.0 Release.

{
  "files":   // An array of glob patterns indicating a set of files to which the configuration applies. If this field is not specified, the default settings will apply.
  \[
    "\*\*/\*.js", // String.
    "\*\*/\*.ts"
  \],
  "ignore":  // An array of glob patterns indicating a set of files to which the configuration should not apply. If this field is not specified, the configuration applies to all matches of files.
  \[
    "build/\*\*/\*",    // String.
    "node\_modules/\*\*/\*"
  \],
  "ruleSet":       // Rule set to be applied.
  \[
    "plugin:@typescript-eslint/recommended"    // Rule sets that can be quickly imported in batches: plugin:@typescript-eslint/all, plugin:@typescript-eslint/recommended, plugin:@cross-device-app-dev/all, plugin:@cross-device-app-dev/recommended.
  \],
  "rules":         // Rules different from those in the specified rule set. You can edit or disable existing rules in the rule set or add new rules. ruleSet and rules jointly determine the rules to be used for code check.
  {
    "@typescript-eslint/no-explicit-any":  // ruleId can be followed by an array, of which the first element indicates the severity, and other elements indicate the rule switches.
    \[
      "error",              // Severity. Available options are suggestion, error, warn, and off.
      {
        "ignoreRestArgs": true   // Whether to enable the rule. Optional. The specific options vary by rule.
      }
    \],
    "@typescript-eslint/explicit-function-return-type": 2,   // ruleId can be followed by a number alone to indicate the severity. Available options are 3 (suggestion), 2 (error), 1 (warn), and 0 (off).
    "@typescript-eslint/no-unsafe-return": "warn"            // ruleId can also be followed by a string alone to indicate the severity. Available options are suggestion, error, warn, and off.
  },
  "overrides":      // Custom configuration that only applies to specific files and folders.
  \[
    {
      "files":   // An array of files and folders to which the overrides configuration applies.
      \[
        "entry/\*\*/\*.ts"   // String.
      \],
      "excluded":
      \[
        "entry/\*\*/\*.test.js" // An array of files and folders to be excluded. The overrides configuration will not apply to them. The value is a string.
      \],
      "rules":   // Custom rules different from those in the common configuration. You can edit or disable existing rules in the common configuration or add new rules. The custom rules have higher precedence than the common configuration.
      {
        "@typescript-eslint/explicit-function-return-type":  // ruleId: enum.
        \[
          "warn",     // Severity. The value can be error, warn, or off. The configuration here (warn for explicit-function-return-type) will overwrite the common configuration.
          {
             "allowExpressions": true    // Whether to enable the rule. Optional. The specific options vary by rule.
          }
        \],
        "@typescript-eslint/no-unsafe-return": "off"   // The configuration here (to disable the no-unsafe-return rule) will overwrite the common configuration.
      },
      "extRules": {     // You can modify or disable the rules configured in the custom rule set other than overrides. This configuration will overwrite the custom rule configuration.
        "@extrulesproject/foreach-args-check": "off"   // Overwrite the custom rule configuration and disable the @extrulesproject/foreach-args-check rule.
      }
    }
  \],
  "extRuleSet": \[     // Custom rule set configuration
    {
        "ruleSetName": "extrulesproject",     // Name of the custom rule library, which must be globally unique. The format must be either "@group name/package name" or "package name". The group name/package name can contain only lowercase letters, digits, underscores (\_), and hyphens (-), and must start with a letter. The value contains a maximum of 128 characters and cannot be used as reserved keywords of ArkTS.
        "packagePath": "D:\\\\checker\\\\extrulesproject-1.0.0.tgz",     // Path of the custom rule installation package. The path must be an absolute path.
        "extRules": {     // Custom rule name and alarm severity. The enumerated values are 3 (suggestion), 2 (error), 1 (warn), and 0 (off).
          "@extrulesproject/foreach-args-check": 1
        }
    }
  \]
}

#### Checking Code via DevEco Studio

## Procedure

Full code check: In an open code editor pane, right-click anywhere and choose **Code Linter** from the shortcut menu. Alternatively, in the project management pane, right-click one or more project files or folders and choose **Code Linter** > **Full Linter** from the shortcut menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Hd7neQTUS5SMrPWr2VvZ4A/en-us_image_0000002532750551.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0F191A464940846D6F376D69866F17D83EDCF224E857D1544B27ACC37497966)

Incremental check on Git project changes (including new, modified, and renamed files): Click the gear icon in the lower-right corner of the commit page and select **Incremental Linter**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/zHsPXHDmQce1kYbchGI6NQ/en-us_image_0000002532750553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B7EC506D5D28CCBF8DC65E2C0707D0F1B3B6369F28EA0ECFF714E3676E61176 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/K3DsIR1ARICiOtEhMWOJ8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9B2BB7E449AFC7CDF85C7A39C19EEDD2A5CAFC59DC17CB1F9D55476466C3E46)

-   Code Linter then checks your code in .ets files against the custom code check rules (if any) or default code check rules.
-   Code Linter does not check the following files and directories:
    -   src/ohosTest
    -   /src/test
    -   node\_modules
    -   oh\_modules
    -   build
    -   .preview
    -   hvigorfile.ts
    -   hvigorfile.js
    -   BuildProfile.ets

## Viewing Code Check Results and Fixing Defects

Once the code check is complete, the check results are displayed at the bottom of the tool. You can filter defects by severity. Clicking the **Filter by scene** drop-down list allows you to filter the check results by rule. Double-clicking a defect directs you to its source code. Selecting a defect shows a **Defect Description** pane on the right, providing a rule description and suggestions for fixing the defect, as well as the correct and incorrect usage of the rule. When searching for a rule, you can enable or disable the match case and match whole word options.

Click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Mw0vU9MeRrKARUEHilCgdw/en-us_image_0000002532750555.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6ACCCEB0D37EB726C6400848751E6F5BE045093B582B804AF5A9035BFC0328EC) icon to view defects that can be quickly fixed and click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/WT0pzXPXRQ-PBsw3GnHqoQ/en-us_image_0000002532750557.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D5D2A574EC1C4F64D8D6332481D70BCD544010DEFA4869BD0A8F7F5CF37BFFE) to fix defects in batches and refresh the check results.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/1KZVfuo2QHCI_b46jPd5JA/en-us_image_0000002501070518.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BE961B0970FEEE4F2128D03AF26C2FFC23564D84C9D43449EE02197136C4D4B)

There are several ways to ignore defects:

-   Ignore false positives. To do so, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/75wU3iVGSdmf53RzqMP0WA/en-us_image_0000002500910682.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A9EC6928268C7DC7EA58400593D9BD5A88F2AC7A42EA40FEF9BBD940C708909) **Ignore** next to a specific defect to ignore it, or select multiple files or defects and click the **Ignore** icon on the toolbar on the left to ignore them all at once.
-   Suppress Code Linter checks for a file or disable individual rules. To exclude a file from checks, add the **/\* eslint-disable \*/** comment to the top of the file. To disable individual rules, add the rule IDs, separated by commas (,), to **eslint-disable**.
-   Suppress Code Linter checks for a code block or a specific line of code. Specifically, add the **/\* eslint-disable \*/** comment above the code block and the **/\* eslint-enable \*/** comment below the code block; add the **/\* eslint-disable-next-line \*/** comment above the line of code.

To restore the defects, delete the aforementioned comments and run Code Linter again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/N0w_5ifwQeuWOUGXvd6P7A/en-us_image_0000002500910690.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0A33305C52027A04F42DBF6748C8E79106339519F65EB729F18721BE28D6E90)

Export the check result: Click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/QDoxIcxcQ8mIJPxpAO3qdQ/en-us_image_0000002500910688.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80979B0212938230911EB55FD1A46E51BA414CA08028379409DE1288A6F1009B) on the toolbar on the left to export the check result to an Excel file, including the line of problematic code, defect details, and severity.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/r2LgQJgwRC2U9htDRw-lCQ/en-us_image_0000002501070522.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F090B53171493AA010449EBA42CA995C294EDEC01B306E3FD61163B5D08277EA)

#### Checking Code via the CLI

DevEco Studio 6.0.1 Beta1 and later support code check via the CLI. Open a cmd or Bash window in the **_DevEco Studio installation path_/deveco-studio/plugins/codelinter/run** directory, and execute the following command:

node ./index.js \[options\] \[dir\] 

**options**: indicates available configurations. For details, see [Table 1](../../../../command-line-tools/using-codelinter/document.md#table25697717185).

**dir**: root directory of the project to be checked. This parameter is optional. If this parameter is not specified, the current context directory is used by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/NPX3vW8jR7ezKgtmBRg2zQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F8D3E80CCD120F631A8CBC56F1520BD23C9B088C30DAF14C86D4825D1EBABE8)

To use the CLI for code check, a Node.js environment is required. The version of Node.js installed locally must match exactly the version located in the **tools** directory of DevEco Studio.

#### Examples

In the following examples, the **@typescript-eslint/no-restricted-syntax** (which restricts the usage of particular syntax in code), **@typescript-eslint/naming-convention** (which enforces naming conventions), and **@hw-stylistic/file-naming-convention** (which checks the naming style of code files) rules are added to the Code Linter configuration file.

## Example 1: Checking Against Use of the **bar** Method in Class **Foo**

**Defining a rule in the configuration file**

In your ArkTS project, add the following code to the **pages/Index.ets** file:

class Foo {
  static bar() {}
}

Foo.bar();

Create the **code-linter.json5** file (do not change this file name) in the root directory of your project and add the following configuration:

{
  "rules": {
    "@typescript-eslint/no-restricted-syntax": \[
      // Set the severity. Available options are error, warn, and off.
      "error",
      {
        // The selector field is mandatory. Set it to disallow specified syntax.
        // You can use a DSL to specify the syntax patterns to disallow. Inside the square bracket following CallExpression, add your filter conditions (used to match nodes in the syntax tree).
        // callee.object.name filters the object (class, namespace, or module) that invokes the method based on the specified name. In this example, the value is Foo.
        // callee.property.name filters the invoked method based on the specified name. In this example, the value is bar.
        "selector": "CallExpression\[callee.object.name='Foo'\]\[callee.property.name='bar'\]",
        // The message field is optional. Set it to specify the error information to be displayed.
        "message": "Foo.bar() is not allowed"
      }
    \]
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/2kDoxVh4Q-2IcFEcXwM3Ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB5AC85693222FA4BEE51EB9C46E1392F429450B44E6BD73C5F91DA2D4C280EA)

For details about how to configure other fields in the **code-linter.json5** file, see [Configuring Code Check Rules](#section19310459444).

**Performing Code Check**

Perform code check on the **pages/Index.ets** file. The check result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/mqaTtYvySeKywtHTmzyumw/en-us_image_0000002532670591.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC929EEAF7827D7DEC9864BD7E58E81361C0AFEED29C1251AF62B4FC7C115861)

## Example 2: Code Linter enforces naming conventions for class **Foo**.

**Defining a Rule in the Configuration File**

In your ArkTS project, add the following code to the **pages/Index.ets** file:

class foo {    // Construct an example of incorrect naming style. foo is the incorrect class name. The correct class name should be Foo.
  bar() {} 
}

Create the **code-linter.json5** file in the root directory of your project and add the following configuration:

{
  "rules": {
    "@typescript-eslint/naming-convention": \[
      "error",
      {
        // The selector field is mandatory. It specifies what types of identifiers to target. In this example, the type is class.
        "selector": "class",
        // The format field is mandatory. It specifies the expected formats of the identifier and accepts enum values. In this example, the specified format is PascalCase.
        "format": \["PascalCase"\],
        // The custom field is optional. It defines a custom regex that the identifier must (or must not) match.
        "custom": {
          // The regex property is mandatory. It indicates a regular expression.
          "regex": "^\[a-zA-Z\]+$",
          // The match property is mandatory. The value true indicates that the identifier must match the regex, and false indicates that the identifier must not match the regex.
          "match": true
        }
      }
    \]
  },
}

**Table 1** Fields
| 
Name

 | 

Description

 | 

Mandatory or Optional

 | 

Type

 | 

Accepted Value

 |
| :-- | :-- | :-- | :-- | :-- |
| 

selector

 | 

What types of identifiers to target.

 | 

Yes

 | 

String, string array

 | 

-   **variable**: variable
-   **function**: function
-   **parameter**: parameter
-   **parameterProperty**: parameter property
-   **accessor**: get or set method
-   **enumMember**: enum member
-   **classMethod**: class method
-   **structMethod**: method in a custom component
-   **objectLiteralMethod**: object literal method
-   **typeMethod**: object type method
-   **classProperty**: class property
-   **structProperty**: property in a custom component
-   **objectLiteralProperty**: object literal property
-   **typeProperty**: object type property
-   **class**: class
-   **struct**: custom component
-   **interface**: interface declaration
-   **typeAlias**: type alias declaration
-   **enum**: enum declaration
-   **typeParameter**: generic type parameter declaration
-   **default**: all the preceding types
-   **variableLike**: same as **variable**, **function**, and **parameter**
-   **memberLike**: same as **classProperty**, **structProperty**, **objectLiteralProperty**, **typeProperty**, **parameterProperty**, **enumMember**, **classMethod**, **objectLiteralMethod**, **typeMethod**, and **accessor**
-   **typeLike**: same as **class**, **struct**, **interface**, **typeAlias**, **enum**, and **typeParameter**
-   **method**: same as **classMethod**, **structMethod**, **objectLiteralMethod**, and **typeMethod**
-   **property**: same as **classProperty**, **objectLiteralProperty**, and **typeProperty**

 |
| 

format

 | 

Expected formats of the identifier.

 | 

Yes

 | 

String array

 | 

-   **camelCase**: lower camel case, for example, **getName** and **getID** (consecutive uppercase letters are allowed), but no underscores (\_) are allowed between characters.
-   **strictCamelCase**: same as **camelCase**, except that consecutive uppercase letters are not allowed (that is, **getID** is invalid).
-   **PascalCase**: same as **camelCase**, except that the first character must be in uppercase, as in **Foo** and **CC**.
-   **StrictPascalCase**: same as **PascalCase**, except that consecutive uppercase letters are not allowed (that is, **CC** is invalid).
-   **snake\_case**: words are in lowercase, and separated by underscores (\_), as in **a\_a**. **\_a** and **a\_a\_** are invalid.
-   **UPPER\_CASE**: words are in uppercase, and separated by underscores (\_), as in **A\_A**. **\_A** and **A\_A\_** are invalid.

 |
| 

custom

 | 

Custom regex that the identifier must (or must not) match.

 | 

No

 | 

Object

 | 

-   **regex**: regular expression. Mandatory.
-   **match**: whether the identifier must match the **regex**. Mandatory. The value **true** indicates that the identifier must match the **regex**, and **false** indicates that the identifier must not match the **regex**.

 |
| 

leadingUnderscore/trailingUnderscore

 | 

Whether leading/trailing underscores are allowed.

 | 

No

 | 

String

 | 

-   **allow**: A single leading/trailing underscore (\_) is allowed. For example, **\_name** is valid.
-   **allowDouble**: A double leading/trailing underscore (\_) is allowed. For example, **\_\_name** is valid.
-   **allowSingleOrDouble**: A single or double leading/trailing underscore (\_) is allowed.
-   **forbid**: A leading/trailing underscore (\_) is not allowed at all. For example, **\_name** and **\_\_name** are invalid.
-   **require**: A leading/trailing underscore (\_) is required. For example, **\_name** and **\_\_name** are valid.
-   **requireDouble**: A double leading/trailing underscore (\_) is required. For example, **\_\_name** is valid.

 |
| 

prefix/suffix

 | 

Prefix/Suffix that the identifier must contain. If the specified prefix or suffix is not found, an error is reported.

 | 

No

 | 

String array

 | 

Custom prefix/suffix

 |
| 

filter

 | 

Configuration that should or should not be applied to the identifier.

 | 

No

 | 

Object

 | 

The configuration format is similar to that of **custom**.

**match**: whether the identifier must match the **regex**. The value **true** indicates that the identifier must match the **regex**, and **false** indicates that the identifier must not match the **regex**.

**regex**: regular expression for filtering.

NOTE:

**filter** accepts a regular expression. In this case, **match** is treated as **true**.

 |
| 

modifiers

 | 

Modifiers to apply to the identifier.

 | 

No

 | 

String array

 | 

-   **abstract**: matches any identifier with the **abstract** modifier.
-   **override**: matches any identifier declared with the **override** modifier.
-   **private**: matches any identifier declared with the **private** modifier.
-   **protected**: matches any identifier declared with the **protected** modifier.
-   **static**: matches any identifier declared with the **static** modifier.
-   **async**: matches any identifier that is async via the **async** keyword.
-   **const**: matches any identifier declared as being **const**.
-   **destructured**: matches any variable declared via an object destructuring pattern.
-   **exported**: matches anything that is exported from the module.
-   **global**: matches any global declaration.
-   **#private**: matches any identifier that starts with a number sign (#).
-   **public**: matches any identifier that is explicitly or implicitly public.
-   **requiresQuotes**: matches any name that requires quotes and contains special characters.
-   **unused**: matches anything that is not used.

 |
| 

types

 | 

Types to match.

 | 

No

 | 

String array

 | 

-   **array**
-   **boolean**
-   **function**
-   **number**
-   **string**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Ugf4nUkjQIKJUvIUn1C06g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7E207D92E141B382F1D2AD8A5F09C108672524BB67295B9B4D06470BB8F71F8)

The format of an identifier is checked in the following order: filter > types > modifiers > validate leading underscore > validate trailing underscore > validate prefix > validate suffix > validate custom > validate format

**Performing Code Check**

Perform code check on the **pages/Index.ets** file. The check result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/CkGamuYcQVKAdNCeh2DTZw/en-us_image_0000002500910686.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFE1D95E54153132DD03C28A837FF3D3086E11E3A9BD87B5AF32D022E1079084)

## Example 3: Code Linter checks the naming style of code files.

**Defining a Rule in the Configuration File**

In an ArkTS project, create the **test.ets** file in the **pages** directory.

Create the **code-linter.json5** file in the root directory of your project and add the following configuration:

{
  "rules": {
    "@hw-stylistic/file-naming-convention": \[
      // Set the severity. Available options are error, warn, and off.
      "error",
      {
        // The selector field is optional and can be set to either code or resources.
        // code indicates that the naming style check applies to code files.
        // resources indicates that the naming style check applies to resource files.
        "selector": "code"
      }
    \]
  },
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/I_MN6RJ5ROOL_CCGCnwVgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18296039E85F05DF101A6A5083DEDCCFDF78662D9F568B27677C85F333EEB66E)

If the **selector** field is not configured, the naming style check will apply to both code files and resource files by default.

**Performing Code Check**

Perform code check on the **pages/test.ets** file. The check result is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/WBHTXxPeSE6Py9nmXAkhnw/en-us_image_0000002532750547.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062139Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A7251F6E5A489C7851468FB328EEAF44BBFBF309720EC419FB0E4F0DD4D7B95)
