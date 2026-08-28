# ohpm Version Number Rules

The version numbers of third-party packages managed by ohpm follow [Semantic Versioning 2.0.0](https://semver.org/) (SemVer 2.0.0) rules.

#### Version Number Format

Format: _Major version number_._Minor version number_._Patch version number_\[-_Pre-release version number_\]\[+_Build information_\], for example, 1.0.0-PRERELEASE+BUILD.

-   Major version number (**MAJOR**): Non-negative integer. It must increment when developers make incompatible API changes, with **MINOR** and **PATCH** reset to zero.
-   Minor version number (**MINOR**): Non-negative integer. It must increment when developers add new features, with **PATCH** reset to zero.
-   Patch version number (**PATCH**): Non-negative integer. It must increment when developers fix bugs or vulnerabilities.
-   Pre-release version number (**PRERELEASE**, optional): ASCII letters, digits, and hyphens (-) separated by hyphens (-) and dots (.). Spaces are not allowed. It is used to identify an unstable pre-release version (such as alpha or beta). Example: 1.0.0-alpha and 1.0.0-beta.
-   Build information (**BUILD**, optional): ASCII letters, digits, and hyphens (-) separated by plus signs (+) and dots (.). Spaces are not allowed. It is used to record additional information (such as timestamps) during compilation or build. It does not affect the version priority (during version comparison). Example: 1.0.0+20250415.

## Format Constraints

-   Standard version number: _x_._y_._z_. The standard version number can contain only three numeric components. Leading zeros are forbidden. For example, 1.0.0 is correct, but 01.0.1, 1.0.0.0, and -1.0.01 are incorrect.
-   Pre-release version: _x_._y_._z_\-PRERELEASE. If the identifier after the dot (.) in PRERELEASE is a digit, leading zeros are forbidden. For example, 1.0.0-beta.10 is correct, but 1.0.0-beta.01 is incorrect.
-   Empty identifier: Minimum one identifier is required. For example, 1.0.0-rc is valid, but 1.0.0- is invalid.

## Special Version Examples

-   0.1.0: initial development version. The API is unstable. (The software whose major version number is 0 (format: 0._y_._z_) is in the initial development phase and is considered as an unstable version.)
-   1.0.0: first stable version. The API is stable.
-   1.0.0-beta.1: pre-release version for the main version upgrade.

#### Version Comparison Rules

During version comparison, first compare the standard version number (that is, the major version number, minor version number, and patch version number). The priorities in descending order are as follows: **MAJOR**, **MINOR**, and **PATCH**.

-   Compare numeric values level by level.
    -   If the major versions are different, compare the major versions, for example, 1.0.0 < 2.0.0.
    -   If the major versions are the same, compare the minor versions, for example, 1.1.0 < 1.2.0.
    -   If both the major and minor versions are the same, compare the patch versions, for example, 1.1.1 < 1.1.2.
-   The missing field is considered as 0. For example, 1.2 is equivalent to 1.2.0, and 1 is equivalent to 1.0.0.

## Rules for Comparing Standard Versions with Pre-Release Versions

The comparison methods for standard versions and pre-release versions are as follows:

-   Fixed version comparison
    
    -   The priority follows the rule of major version number > minor version number > patch version number. When the standard version numbers are different, comparison is conducted according to the value of version numbers at the same level. For example, 1.0.2-snapshot > 1.0.0. For details, see example 3.
    
    -   If the standard version numbers are the same, the priority of the pre-release version is lower than that of the standard version. For example, 1.0.0-snapshot < 1.0.0.

-   Range version comparison
    -   If both pre-release and standard versions exist in the repository, and the dependency is specified with a standard version range (for example, >=1.0.0), the version to be installed will be selected from the available standard versions. Specifically, the latest standard version satisfying >=1.0.0 will be installed. If no qualifying standard version exists, the latest pre-release version satisfying >=1.0.0 will be installed instead. For details, see example 1.
    -   If both pre-release and standard versions exist in the repository, and the dependency is specified with a pre-release version range (for example, >=1.0.0-snapshot), the version to be installed will be selected from the available standard versions. Specifically, the latest standard version satisfying >=1.0.0 will be installed. If no qualifying standard version exists, the latest pre-release version satisfying >=1.0.0-snapshot will be installed instead. For details, see examples 4 and 5.
    -   If only pre-release versions exist in the repository, and the dependency is specified with a standard version range (for example, >=1.0.0), the version to be installed will be selected from the available pre-release versions. Specifically, the latest pre-release version satisfying >=1.0.0 will be installed. For details, see example 2.
    -   If only pre-release versions exist in the repository, and the dependency is specified with a pre-release version range (for example, >=1.0.0-snapshot), the version to be installed will be selected from the available pre-release versions. Specifically, the latest pre-release version satisfying >=1.0.0-snapshot will be installed. For details, see example 6.

// Example 1
> Available versions of dependency liba in the repository: \['1.0.0-snapshot.1', '1.0.0-snapshot.2', '1.0.0', '2.0.0-snapshot.1', '2.0.0-snapshot.2', '2.0.0', '3.0.0-snapshot.1', '3.0.0-snapshot.2'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": ">=1.0.0"
  }
}
> The liba version installed via ohpm install is 2.0.0.

// Example 2
> Available versions of dependency liba in the repository: \['1.0.0-snapshot.1', '1.0.0-snapshot.2', '2.0.0-snapshot.1', '2.0.0-snapshot.2'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": ">=1.0.0"
  }
}
> The liba version installed via ohpm install is 2.0.0-snapshot.2.

// Example 3
> Available versions of dependency liba in the repository: \['1.0.0', '1.0.2-snapshot', '2.0.0-snapshot.1', '2.0.0-snapshot.2'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": "^1.0.0"
  }
}
> If the project depends on liba,
the configuration in the oh-package.json5 file of the project is as follows: {
  "modelVersion": "x.0.0",
  "description": "Please describe the basic information.",
  "dependencies": {
    "liba": "1.0.2-snapshot"
  }
}
> The liba version installed via ohpm install is 1.0.2-snapshot.

// Example 4
> Available versions of dependency liba in the repository: \['1.0.0-snapshot', '1.0.0'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": ">=1.0.0-snapshot"
  }
}
> The liba version installed via ohpm install is 1.0.0.

// Example 5
> Available versions of dependency liba in the repository: \['0.0.1','1.0.0-snapshot', '1.0.1-snapshot'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": ">=1.0.0-snapshot"
  }
}
> The liba version installed via ohpm install is 1.0.1-snapshot.

// Example 6
> Available versions of dependency liba in the repository: \['1.0.0-snapshot.1', '1.0.0-snapshot.2', '2.0.0-snapshot.1', '2.0.0-snapshot.2'\]
> If the entry module depends on liba, the configuration in the oh-package.json5 file of the entry module is as follows:
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "Index.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "liba": ">=1.0.0-snapshot"
  }
}
> The liba version installed via ohpm install is 2.0.0-snapshot.2.

## Pre-Release Version Comparison Rules

When the major, minor, and patch version numbers are identical, the precedence between versions is determined by their pre-release identifiers. Identifiers separated by dots (.) are compared sequentially from left to right, according to the following rules:

-   Numeric identifiers: Compare numerically.
    
    Example: comparing 2.0.0-beta.2 with 2.0.0-beta.11. Since the standard versions (2.0.0) are identical, compare the pre-release identifiers sequentially: the first identifiers (beta) are the same; the second identifiers are numeric (2 and 11). Since 2 < 11, the result is 2.0.0-beta.2 < 2.0.0-beta.11.
    
-   Non-numeric identifiers: Compare lexicographically in ASCII order.
    
    Example: comparing 4.0.0-beta.2 with 4.0.0-rc.1. Since the standard versions (4.0.0) are identical, compare the pre-release identifiers: the first character 'b' comes before 'r' in lexicographical order, so 4.0.0-beta.2 < 4.0.0-rc.1.
    
-   Numeric identifiers have lower precedence than non-numeric identifiers.
    
    Example: 1.0.0-1 < 1.0.0-a.
    
-   Identifier count: A version with more identifiers has higher precedence.
    
    Example: 3.0.0-alpha < 3.0.0-alpha.1.
    
-   Hyphens (-) within a pre-release identifier are treated as part of the string and do not split the identifier.
    
    Example: comparing 2.1.0-100-1002 with 2.1.0-1001-001. Since the standard versions (2.1.0) are identical, compare the pre-release identifier segments (100-1002 and 1001-001) character by character from left to right in ASCII lexicographical order: the fourth character '-' is less than '1' in ASCII order. Therefore, the result is 2.1.0-100-1002 < 2.1.0-1001-001.
    

#### Version Range Operators

## Caret (^)

The caret operator (^) fixes the major version number while allowing upgrades to the latest version within the same major release. When the major version is 0, it fixes the first non-zero version number from the left. It can be used for automatically receiving upgrades for the current major version.

// Examples
^1.2.301 is equivalent to: 1.2.301 <= Version < 2.0.0. // Fixes the major version: 1 remains unchanged.
^0.2.301 is equivalent to: 0.2.301 <= Version < 0.3.0. // Fixes the first non-zero version from left: minor version 2 remains unchanged.
^0.0.301 is equivalent to: 0.0.301 <= Version < 0.0.302. // Fixes the first non-zero version from left: patch version 301 remains unchanged.

Since ohpm v5.0.11 (DevEco Studio 5.0.7.210), the caret operator (^) always indicates the fixed major version. The first non-zero version number is no longer fixed.

// Examples after caret (^) semantic unification
^1.2.301 is equivalent to: 1.2.301 <= Version < 2.0.0. // Fixes the major version: 1 remains unchanged.
^0.2.301 is equivalent to: 0.2.301 <= Version < 1.0.0. // Fixes the major version: 0 remains unchanged.
^0.0.301 is equivalent to: 0.0.301 <= Version < 1.0.0. // Fixes the major version: 0 remains unchanged.

## Tilde (~)

The tilde operator (~) fixes both the major and minor version numbers while allowing upgrades to the latest patch version within the specified _major_._minor_ range. It can be used for receiving only patch updates (bug fixes) while avoiding minor or major version upgrades.

// Examples
~1.2.301 is equivalent to: 1.2.301 <= Version < 1.3.0. // Fixes the major and minor version numbers: 1.2 remains unchanged.
~1.2 is equivalent to ~1.2.0, which means: 1.2.0 <= Version < 1.3.0. // Fixes the major and minor version numbers: 1.2 remains unchanged.
~1 is equivalent to ~1.x, which means: 1.0.0 <= Version < 2.0.0-0. // Fixes the major version number: 1 remains unchanged (special case).
~0.10.100 is equivalent to: 0.10.100 <= Version < 0.11.0. // Fixes the major and minor version numbers: 0.10 remains unchanged.
~0.0 is equivalent to: 0.0.0 <= Version < 0.1.0. // Fixes the major and minor version numbers: 0.0 remains unchanged.
~0 is equivalent to 0.x, which means: 0.0.0 <= Version < 1.0.0-0. // Fixes the major version number: 0 remains unchanged (special case).

## Hyphen (-)/Ellipsis (...)

The hyphen (-) and ellipsis (...) are used to specify a continuous version range that includes both the start and end versions (with spaces required before and after these symbols in the expression). Of the two, the hyphen (-) is recommended due to its broader support across toolchains. This notation is suitable for defining a closed interval and simplifying version expressions.

// Examples
1.0.1 - 2.1.1 is equivalent to: 1.0.1 <= Version <= 2.1.1
1.0.1 ... 2.1.1 is equivalent to: 1.0.1 <= Version <= 2.1.1
// Example with a missing start version field
1.1 - 2.1.0 is equivalent to: 1.1.0 <= Version <= 2.1.0
// Examples with a missing end version field
1.1.0 - 2.1 is equivalent to: 1.1.0 <= Version < 2.2.0-0
1.1.0 - 2 is equivalent to: 1.1.0 <= Version < 3.0.0-0

## Comparison Operators (>, <, >=, <=, and =)

Comparison operators (>, <, >=, <=, and =) are used to match version ranges literally. For example, ">1.2.0" means the version must be higher than 1.2.0.

#### Wildcard and Logical Operators

## Wildcard Operators (x and \*)

Wildcard operators (x and \*) indicate matching any value, typically used to omit fields and simplify range definitions.

// Examples
1.x is equivalent to: 1.0.0 <= Version < 2.0.0, that is, ^1.0.0.
1.1.x is equivalent to: 1.1.0 <= Version < 1.2.0, that is, ~1.1.0.

## Logical AND (Space)

When multiple range conditions are separated by spaces, they are combined with an implicit logical AND, that is, all conditions must be satisfied.

// Example
>=1.0.101 <2.0.100 is equivalent to: 1.0.101 <= Version < 2.0.100.

## Logical OR (||)

The logical OR operator (||) combines multiple version ranges (the union of version ranges that satisfy any one of the conditions).

// Example
^1.0.101 || ^2.0.100 is equivalent to: 1.0.101 <= Version < 2.0.0 or 2.0.100 <= Version < 3.0.0.
