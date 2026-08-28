# @typescript-eslint/quotes

Enforce the consistent use of either backticks, double, or single quotes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/kjt5GtPzS0GoZTsFB3DIlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062143Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4660F206DDAAB1F39170674272DC1F26438B1DB561027DA9494A650CFE560D70)

-   By default, this rule check whether strings are correctly wrapped in double quotes. For any adjustments, see [Options](#section182418564158).
-   This rule is recommended for checking .ts files. To check .ets files, consider using [@hw-stylistic/quotes](../../hw-stylistic-arkts-code-style-rules/hw-stylistic-quotes/document.md).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/quotes": "error"
  }
}

#### Options

For details, see [@typescript-eslint/quotes](https://eslint.nodejs.cn/docs/latest/rules/quotes#选项).

#### Example of Correct Code

export const double = "double";
export const foo = \`back
tick\`;  // backticks are allowed due to newline

#### Example of Incorrect Code

// Double quotes are recommended by default.
export const single = 'single';
export const unescaped = 'a string containing "double" quotes';
export const backtick = \`back\\ntick\`; // you can use \\n in single or double quoted strings

#### Rule Set

plugin:@typescript-eslint/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
