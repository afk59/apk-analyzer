# @performance/no-use-any-import

Import only the variables you need on demand instead of using **import** when importing the corresponding modules. This reduces the execution time of .ets files and avoids unnecessary initialization of all exported variables in the files.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@performance/no-use-any-import": "warn",
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

// Index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import { One } from '../utils/Numbers'; // It is recommended to reference variables on demand
hilog.info(0x0000, 'testTag', '%{public}d', One); // Only the variable One is used here
// Numbers.ets
export const One: number = 1;
export const Two: number = 2;

#### Example of Incorrect Code

// Index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
import \* as nm from '../utils/Numbers'; // The import \* method is not recommended
hilog.info(0x0000, 'testTag', '%{public}d', nm.One); // Only the variable One is used here
// Numbers.ets
export const One: number = 1;
export const Two: number = 2;

#### Rule Set

plugin:@performance/recommended
plugin:@performance/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
