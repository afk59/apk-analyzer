# Why can a file without a default export be imported as a default import without causing any compilation error?

**Symptom**

When a declaration file does not have a default export, using **import _xxx_ from '_module_'** does not cause a compilation error.

// test.d.ts file
export const addFunction: {
  add: (a: number, b: number) => number
}

// index.ets file
import test from './test'

test.addFunction.add(1,2)

**Possible Causes**

The compilation does not throw an error in this scenario because the configuration file has the **allowSyntheticDefaultImports** option enabled. This option allows files without a default export to be imported as default imports. In addition, it provides compatibility for importing default exports from libraries that use CommonJS (**require**) for exporting modules. For example, you can use a default import to import third-party libraries like React without encountering compilation errors.

**Example with React: using a default import to install the @types/react package without encountering any compilation errors**

import  React  from "react";
React.useId()

**Example with CommonJS: using a default import to import a CommonJS module**

// Compilation file
import allFunction from 'library'

allFunction.sub(1,2)

// Implementation file of the dependency package: index.js
function sub(a, b) {
    return a - b
}

var allFunction = { sub }
module.exports = allFunction

**Solution**

If the source file does not have a default export, you can use the following import syntax instead: **import \* as _xx_ from '_xxx_'**.
