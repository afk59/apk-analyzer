# How do I set the files to be excluded in the compilation configuration?

Perform the following configuration in the module-level **build-profile.json5** file:

"nativeLib": {
  "debugSymbol": {
    "strip": true,
    "exclude": \[
      "\*\*/3.so"
    \]
  }
},
