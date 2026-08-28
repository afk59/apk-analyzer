# How do I resolve errors with require statements in third-party packages?

**Symptom**

An error is reported during compilation when a third-party package is imported.

**Possible Causes**

Some third-party packages are migrated from npm and were originally developed for a Node environment. The **require** syntax may not be fully supported by ArkCompiler, leading to runtime errors.

**Scenario 1**

// Module/src/test.json
{a: 1, b: 2}
//use.js
let test = require("Module/src/test.json")

Change the code as follows:

// Module/src/test.json

module.exports = {a: 1, b: 2}

//use.js

let test = require("Module/src/test")

**Scenario 2**

// Module/package.json
...
main: "./src"
...
// use.js
let module = require("Module")

Change the code as follows:

// Module/package.json

"main": "./src/index.js",

// use.js

let module = require("Module")

**Scenario 3**

A warning message is displayed during compilation:

Plugin node-resolve: preferring built-in module 'util' over local alternative at '/Users/~/Documents/fe-module/demo/node\_modules/util/util.js', pass 'preferBuiltins: false' to disable this behavior or 'preferBuiltins: true' to disable this warning

**Solution**

Modify the **preferBuiltins** field in **rollup.config.js**.

plugins: \[
    resolve({
        preferBuiltins: false,    // true or false
        mainFields: \['module', 'main'\],
        extensions
    })
\];

**Scenario 4**

import {Buffer} from 'buffer'

Change the code as follows:

import {Buffer} from 'buffer/'
